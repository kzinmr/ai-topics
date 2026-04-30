#!/usr/bin/env python3
"""Wiki Health Digest – generates a markdown report on the AI-topics wiki.

Usage:  python scripts/wiki_health.py          # prints report to stdout
        python scripts/wiki_health.py > report.md
"""

import datetime
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    # Minimal fallback: we only need safe_load for small frontmatter blocks.
    yaml = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

def resolve_wiki_root() -> Path:
    """Prefer the Hermes canonical ~/wiki, with repo-local fallback for dev runs."""
    home_wiki = Path.home() / "wiki"
    if home_wiki.exists():
        return home_wiki
    return Path(__file__).resolve().parent.parent / "wiki"


WIKI_ROOT = resolve_wiki_root()
REPO_ROOT = WIKI_ROOT.parent
ENTITIES_DIR = WIKI_ROOT / "entities"
CONCEPTS_DIR = WIKI_ROOT / "concepts"
COMPARISONS_DIR = WIKI_ROOT / "comparisons"
RAW_ARTICLES_DIR = WIKI_ROOT / "raw" / "articles"
INDEX_FILE = WIKI_ROOT / "index.md"

TODAY = datetime.date.today()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(path: Path) -> dict:
    """Return the YAML frontmatter dict for a markdown file, or {} on failure."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}

    # Frontmatter is between the first two '---' lines.
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm_text = parts[1]
    if yaml is not None:
        try:
            data = yaml.safe_load(fm_text)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}
    else:
        # Ultra-minimal parser when PyYAML is missing
        data = {}
        for line in fm_text.splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                data[key.strip()] = val.strip().strip('"').strip("'")
        return data


def collect_md_files(directory: Path) -> list[Path]:
    """Recursively collect all .md files under *directory*."""
    if not directory.is_dir():
        return []
    return sorted(directory.rglob("*.md"))


def slug_from_path(path: Path, base: Path) -> str:
    """Return the relative stem usable as a wiki slug (no .md extension)."""
    return str(path.relative_to(base).with_suffix(""))


def parse_date(val) -> datetime.date | None:
    """Best-effort parse of a date-like value from frontmatter."""
    if isinstance(val, datetime.datetime):
        return val.date()
    if isinstance(val, datetime.date):
        return val
    if isinstance(val, str):
        for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                return datetime.datetime.strptime(val.strip(), fmt).date()
            except ValueError:
                continue
    return None


def extract_tags(fm: dict) -> list[str]:
    """Return list of tags from frontmatter, handling both list and string."""
    raw = fm.get("tags", [])
    if isinstance(raw, list):
        return [str(t) for t in raw if t]
    if isinstance(raw, str):
        # Could be comma-separated or bracketed list stored as string
        raw = raw.strip("[]").strip()
        if raw:
            return [t.strip().strip('"').strip("'") for t in raw.split(",") if t.strip()]
    return []

# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

def load_l2_pages() -> dict[str, list[tuple[Path, dict]]]:
    """Return {category: [(path, frontmatter_dict), ...]} for all L2 pages."""
    categories = {
        "entities": ENTITIES_DIR,
        "concepts": CONCEPTS_DIR,
        "comparisons": COMPARISONS_DIR,
    }
    result: dict[str, list[tuple[Path, dict]]] = {}
    for cat, d in categories.items():
        pages = []
        for p in collect_md_files(d):
            fm = parse_frontmatter(p)
            pages.append((p, fm))
        result[cat] = pages
    return result


def load_raw_articles() -> list[Path]:
    if not RAW_ARTICLES_DIR.is_dir():
        return []
    return sorted(RAW_ARTICLES_DIR.glob("*.md"))

# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def section_overview(l2: dict, raw_articles: list[Path]) -> str:
    lines = ["## 📊 Overview Stats\n"]
    total = 0
    for cat in ("entities", "concepts", "comparisons"):
        n = len(l2.get(cat, []))
        total += n
        lines.append(f"- **{cat.title()}**: {n} pages")
    lines.append(f"- **Raw articles**: {len(raw_articles)}")

    skeleton_count = sum(
        1
        for _, fm in l2.get("entities", [])
        if str(fm.get("status", "")).strip().lower() == "skeleton"
    )
    lines.append(f"- **Skeleton entities**: {skeleton_count}")
    lines.append(f"- **Total Layer 2 pages**: {total}")
    return "\n".join(lines)


def section_stale_pages(l2: dict) -> str:
    lines = ["## 🕰️ Stale Pages (>30 days since update)\n"]
    stale: list[tuple[int, str, Path]] = []

    for cat, pages in l2.items():
        for path, fm in pages:
            d = parse_date(fm.get("updated") or fm.get("created"))
            if d is None:
                continue
            age = (TODAY - d).days
            if age > 30:
                rel = f"{cat}/{slug_from_path(path, WIKI_ROOT / cat)}"
                stale.append((age, rel, path))

    stale.sort(key=lambda x: -x[0])  # stalest first

    if not stale:
        lines.append("_No stale pages found — everything updated within the last 30 days._ ✅")
    else:
        lines.append(f"Found **{len(stale)}** stale pages. Top 10:\n")
        lines.append("| # | Page | Days since update |")
        lines.append("|---|------|-------------------|")
        for i, (age, rel, _) in enumerate(stale[:10], 1):
            lines.append(f"| {i} | `{rel}` | {age} |")

    return "\n".join(lines)


def section_unprocessed_raw(l2: dict, raw_articles: list[Path]) -> str:
    lines = ["## 📬 Unprocessed Raw Articles\n"]

    if not raw_articles:
        lines.append("_No raw articles found._")
        return "\n".join(lines)

    # Build a big string of all L2 content for substring matching
    l2_content_parts: list[str] = []
    for cat, pages in l2.items():
        for path, _ in pages:
            try:
                l2_content_parts.append(path.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                pass
    l2_blob = "\n".join(l2_content_parts)

    unprocessed: list[Path] = []
    for raw_path in raw_articles:
        # Check both with and without .md extension
        stem = raw_path.stem  # filename without .md
        name = raw_path.name  # filename with .md
        if stem not in l2_blob and name not in l2_blob:
            unprocessed.append(raw_path)

    lines.append(f"**{len(unprocessed)}** of {len(raw_articles)} raw articles are not referenced from any Layer 2 page.\n")

    if unprocessed:
        # Sort newest first: try to extract date from filename, fallback to name sort
        def sort_key(p: Path) -> str:
            return p.name

        unprocessed_sorted = sorted(unprocessed, key=sort_key, reverse=True)

        lines.append("Latest 20 unprocessed:\n")
        for p in unprocessed_sorted[:20]:
            lines.append(f"- `{p.name}`")
        if len(unprocessed) > 20:
            lines.append(f"- _…and {len(unprocessed) - 20} more_")

    return "\n".join(lines)


def section_orphan_pages(l2: dict) -> str:
    lines = ["## 🔗 Orphan Pages (not in index.md)\n"]

    try:
        index_text = INDEX_FILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        lines.append("_Could not read index.md — skipping orphan check._")
        return "\n".join(lines)

    orphans: list[str] = []
    for cat, pages in l2.items():
        for path, fm in pages:
            # Build the slug that would appear in index.md
            # Index uses format like [[entities/adam-mastroianni]] or [[concepts/agentic-engineering/_index]]
            rel = str(path.relative_to(WIKI_ROOT).with_suffix(""))
            # Also check with .md in case index links include it
            rel_md = str(path.relative_to(WIKI_ROOT))
            if rel not in index_text and rel_md not in index_text:
                orphans.append(rel)

    if not orphans:
        lines.append("_All Layer 2 pages are listed in index.md._ ✅")
    else:
        lines.append(f"Found **{len(orphans)}** orphan pages not referenced in `index.md`:\n")
        for o in sorted(orphans):
            lines.append(f"- `{o}`")

    return "\n".join(lines)


def section_growth(l2: dict) -> str:
    lines = ["## 🌱 Growth (Last 7 Days)\n"]

    new_files: list[str] = []
    git_ok = False

    try:
        result = subprocess.run(
            [
                "git", "log",
                "--diff-filter=A",
                "--since=7 days ago",
                "--name-only",
                "--pretty=format:",
            ],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode == 0:
            new_files = [f for f in result.stdout.splitlines() if f.strip()]
            git_ok = True
    except Exception:
        pass

    if not git_ok:
        # Fallback: use mtime
        cutoff = datetime.datetime.now().timestamp() - 7 * 86400
        for p in WIKI_ROOT.rglob("*.md"):
            try:
                if p.stat().st_mtime >= cutoff:
                    new_files.append(str(p.relative_to(REPO_ROOT)))
            except OSError:
                pass
        lines.append("_(Using file modification time — git not available)_\n")

    # Categorise
    buckets: Counter[str] = Counter()
    for f in new_files:
        if f.startswith("wiki/entities/"):
            buckets["entities"] += 1
        elif f.startswith("wiki/concepts/"):
            buckets["concepts"] += 1
        elif f.startswith("wiki/comparisons/"):
            buckets["comparisons"] += 1
        elif f.startswith("wiki/raw/articles/"):
            buckets["raw articles"] += 1
        elif f.startswith("wiki/"):
            buckets["other wiki"] += 1
        else:
            buckets["non-wiki"] += 1

    total = sum(buckets.values())
    lines.append(f"**{total}** new files added in the last 7 days:\n")

    if buckets:
        lines.append("| Category | New files |")
        lines.append("|----------|-----------|")
        for cat in ("entities", "concepts", "comparisons", "raw articles", "other wiki", "non-wiki"):
            if buckets.get(cat, 0) > 0:
                lines.append(f"| {cat.title()} | {buckets[cat]} |")
    else:
        lines.append("_No new files in the last 7 days._")

    return "\n".join(lines)


def section_tag_distribution(l2: dict) -> str:
    lines = ["## 🏷️ Tag Distribution (Top 15)\n"]

    tag_counts: Counter[str] = Counter()
    for cat, pages in l2.items():
        for _, fm in pages:
            for tag in extract_tags(fm):
                tag_counts[tag] += 1

    if not tag_counts:
        lines.append("_No tags found._")
        return "\n".join(lines)

    top = tag_counts.most_common(15)

    lines.append("| # | Tag | Count |")
    lines.append("|---|-----|-------|")
    for i, (tag, count) in enumerate(top, 1):
        lines.append(f"| {i} | `{tag}` | {count} |")

    unique = len(tag_counts)
    lines.append(f"\n_{unique} unique tags across all Layer 2 pages._")

    return "\n".join(lines)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    l2 = load_l2_pages()
    raw = load_raw_articles()

    report_parts = [
        f"# 🩺 Wiki Health Digest — {TODAY.strftime('%Y-%m-%d')}\n",
        section_overview(l2, raw),
        section_stale_pages(l2),
        section_unprocessed_raw(l2, raw),
        section_orphan_pages(l2),
        section_growth(l2),
        section_tag_distribution(l2),
        "---\n_Generated by `scripts/wiki_health.py`_",
    ]

    print("\n\n".join(report_parts))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"# Wiki Health Digest — ERROR\n\n```\n{exc}\n```", file=sys.stderr)
    sys.exit(0)
