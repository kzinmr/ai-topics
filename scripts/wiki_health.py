#!/usr/bin/env python3
"""Wiki Health Digest – generates a markdown report or JSON on the AI-topics wiki.

Usage:  python scripts/wiki_health.py              # markdown report to stdout
        python scripts/wiki_health.py --json       # JSON to stdout (for agent consumption)
        python scripts/wiki_health.py > report.md
"""

import argparse
import datetime
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

def resolve_wiki_root() -> Path:
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

def parse_frontmatter(text: str) -> dict:
    """Return the YAML frontmatter dict from file text, or {} on failure."""
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
        data = {}
        for line in fm_text.splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                data[key.strip()] = val.strip().strip('"').strip("'")
        return data


def collect_md_files(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(directory.rglob("*.md"))


def slug_from_path(path: Path, base: Path) -> str:
    return str(path.relative_to(base).with_suffix(""))


def parse_date(val) -> datetime.date | None:
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
    raw = fm.get("tags", [])
    if isinstance(raw, list):
        return [str(t) for t in raw if t]
    if isinstance(raw, str):
        raw = raw.strip("[]").strip()
        if raw:
            return [t.strip().strip('"').strip("'") for t in raw.split(",") if t.strip()]
    return []


# ---------------------------------------------------------------------------
# Data collection — single-pass (optimized: read once, keep content)
# ---------------------------------------------------------------------------

PageRecord = dict  # {path, fm, content, category, slug}


def load_l2_pages() -> dict[str, list[PageRecord]]:
    """Single-pass: read each file once, keep frontmatter + full content."""
    categories = {
        "entities": ENTITIES_DIR,
        "concepts": CONCEPTS_DIR,
        "comparisons": COMPARISONS_DIR,
    }
    result: dict[str, list[PageRecord]] = {}
    for cat, d in categories.items():
        pages = []
        for p in collect_md_files(d):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                text = ""
            fm = parse_frontmatter(text)
            pages.append({
                "path": p,
                "fm": fm,
                "content": text,
                "category": cat,
                "slug": str(p.relative_to(d).with_suffix("")),
            })
        result[cat] = pages
    return result


def load_raw_articles() -> list[Path]:
    if not RAW_ARTICLES_DIR.is_dir():
        return []
    return sorted(RAW_ARTICLES_DIR.glob("*.md"))


def _build_referenced_stems(l2: dict[str, list[PageRecord]]) -> set[str]:
    """Build a set of raw article stems referenced from any L2 page content.
    
    Uses set-based matching instead of O(N*M) substring search.
    """
    stems: set[str] = set()
    for cat, pages in l2.items():
        for rec in pages:
            content = rec["content"]
            # Look for raw/article references in wikilinks and plain text
            for prefix in ("raw/articles/", "articles/"):
                idx = 0
                while True:
                    idx = content.find(prefix, idx)
                    if idx == -1:
                        break
                    # Extract the stem after the prefix
                    start = idx + len(prefix)
                    end = start
                    while end < len(content) and content[end] not in (" ", "\n", ")", "]", "|", ">"):
                        end += 1
                    ref = content[start:end]
                    # Strip .md extension if present
                    if ref.endswith(".md"):
                        ref = ref[:-3]
                    if ref:
                        stems.add(ref)
                    idx = end
    return stems


def _build_referenced_slugs(l2: dict[str, list[PageRecord]]) -> set[str]:
    """Build set of all L2 page slugs (for orphan detection)."""
    slugs: set[str] = set()
    for cat, pages in l2.items():
        for rec in pages:
            # Full relative path from wiki root
            rel = str(rec["path"].relative_to(WIKI_ROOT).with_suffix(""))
            slugs.add(rel)
            # Also add with .md extension
            slugs.add(str(rec["path"].relative_to(WIKI_ROOT)))
    return slugs


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
        for rec in l2.get("entities", [])
        if str(rec["fm"].get("status", "")).strip().lower() == "skeleton"
    )
    lines.append(f"- **Skeleton entities**: {skeleton_count}")
    lines.append(f"- **Total Layer 2 pages**: {total}")
    return "\n".join(lines)


def section_stale_pages(l2: dict) -> str:
    lines = ["## 🕰️ Stale Pages (>30 days since update)\n"]
    stale: list[tuple[int, str]] = []

    for cat, pages in l2.items():
        for rec in pages:
            fm = rec["fm"]
            d = parse_date(fm.get("updated") or fm.get("created"))
            if d is None:
                continue
            age = (TODAY - d).days
            if age > 30:
                rel = f"{cat}/{rec['slug']}"
                stale.append((age, rel))

    stale.sort(key=lambda x: -x[0])

    if not stale:
        lines.append("_No stale pages found — everything updated within the last 30 days._ ✅")
    else:
        lines.append(f"Found **{len(stale)}** stale pages. Top 10:\n")
        lines.append("| # | Page | Days since update |")
        lines.append("|---|------|-------------------|")
        for i, (age, rel) in enumerate(stale[:10], 1):
            lines.append(f"| {i} | `{rel}` | {age} |")

    return "\n".join(lines)


def section_unprocessed_raw(l2: dict, raw_articles: list[Path]) -> str:
    """Uses set-based stem matching instead of O(N*M) substring search."""
    lines = ["## 📬 Unprocessed Raw Articles\n"]

    if not raw_articles:
        lines.append("_No raw articles found._")
        return "\n".join(lines)

    referenced = _build_referenced_stems(l2)

    unprocessed: list[Path] = []
    for raw_path in raw_articles:
        stem = raw_path.stem
        name = raw_path.name
        if stem not in referenced and name not in referenced:
            unprocessed.append(raw_path)

    lines.append(
        f"**{len(unprocessed)}** of {len(raw_articles)} raw articles are not referenced from any Layer 2 page.\n"
    )

    if unprocessed:
        unprocessed_sorted = sorted(unprocessed, key=lambda p: p.name, reverse=True)
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
        for rec in pages:
            rel = str(rec["path"].relative_to(WIKI_ROOT).with_suffix(""))
            rel_md = str(rec["path"].relative_to(WIKI_ROOT))
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
        cutoff = datetime.datetime.now().timestamp() - 7 * 86400
        for p in WIKI_ROOT.rglob("*.md"):
            try:
                if p.stat().st_mtime >= cutoff:
                    new_files.append(str(p.relative_to(REPO_ROOT)))
            except OSError:
                pass
        lines.append("_(Using file modification time — git not available)_\n")

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
        for rec in pages:
            for tag in extract_tags(rec["fm"]):
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
# JSON output — structured data for agent consumption
# ---------------------------------------------------------------------------

def build_json(l2: dict, raw_articles: list[Path]) -> dict:
    """Build a structured JSON object with all health data."""
    # Overview
    page_counts = {}
    for cat in ("entities", "concepts", "comparisons"):
        page_counts[cat] = len(l2.get(cat, []))
    total_l2 = sum(page_counts.values())

    skeleton_count = sum(
        1 for rec in l2.get("entities", [])
        if str(rec["fm"].get("status", "")).strip().lower() == "skeleton"
    )

    # Stale pages
    stale: list[dict] = []
    for cat, pages in l2.items():
        for rec in pages:
            fm = rec["fm"]
            d = parse_date(fm.get("updated") or fm.get("created"))
            if d is None:
                continue
            age = (TODAY - d).days
            if age > 30:
                stale.append({"page": f"{cat}/{rec['slug']}", "days": age, "category": cat})
    stale.sort(key=lambda x: -x["days"])

    # Unprocessed raw articles
    referenced = _build_referenced_stems(l2)
    unprocessed = [
        p.name for p in raw_articles
        if p.stem not in referenced and p.name not in referenced
    ]

    # Orphan pages
    try:
        index_text = INDEX_FILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        index_text = ""

    orphans = []
    for cat, pages in l2.items():
        for rec in pages:
            rel = str(rec["path"].relative_to(WIKI_ROOT).with_suffix(""))
            rel_md = str(rec["path"].relative_to(WIKI_ROOT))
            if rel not in index_text and rel_md not in index_text:
                orphans.append(rel)
    orphans.sort()

    # Tag distribution
    tag_counts: Counter[str] = Counter()
    for cat, pages in l2.items():
        for rec in pages:
            for tag in extract_tags(rec["fm"]):
                tag_counts[tag] += 1

    # Index corruption check
    index_corruption = _check_index_corruption(index_text)

    # Japanese content check
    jp_stats = _count_jp_content()

    return {
        "date": TODAY.strftime("%Y-%m-%d"),
        "overview": {
            "entities": page_counts["entities"],
            "concepts": page_counts["concepts"],
            "comparisons": page_counts["comparisons"],
            "total_l2": total_l2,
            "raw_articles": len(raw_articles),
            "skeleton_entities": skeleton_count,
        },
        "stale_pages": stale,
        "unprocessed": {
            "count": len(unprocessed),
            "total": len(raw_articles),
            "latest_20": unprocessed[:20],
        },
        "orphan_pages": orphans,
        "orphan_count": len(orphans),
        "tags": {
            "unique": len(tag_counts),
            "top_15": [{"tag": t, "count": c} for t, c in tag_counts.most_common(15)],
        },
        "index_corruption": index_corruption,
        "jp_content": jp_stats,
    }


def _count_jp_content() -> dict:
    """Count Japanese characters in wiki body content (excl. raw/)."""
    import re
    jp_re = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
    jp_files = []
    total_jp = 0
    for root, dirs, files in os.walk(WIKI_ROOT):
        if "raw" in Path(root).relative_to(WIKI_ROOT).parts:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            try:
                with open(fp) as fh:
                    text = fh.read()
            except Exception:
                continue
            lines = text.split("\n")
            body_start = 0
            fm_count = 0
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    fm_count += 1
                    if fm_count == 2:
                        body_start = i + 1
                        break
            if fm_count < 2:
                body_start = 0
            body = "\n".join(lines[body_start:])
            count = len(jp_re.findall(body))
            if count > 0:
                rel = str(Path(fp).relative_to(WIKI_ROOT))
                jp_files.append((rel, count))
                total_jp += count
    jp_files.sort(key=lambda x: -x[1])
    return {
        "total_files": len(jp_files),
        "total_jp_chars": total_jp,
        "top_10": [{"file": f, "jp_chars": c} for f, c in jp_files[:10]],
    }


def _check_index_corruption(index_text: str) -> dict:
    """Check index.md for common corruption patterns."""
    import re
    issues = []

    # Pipe prefix corruption: |- [[slug]]
    pipe_count = len(re.findall(r'^\|- \[\[', index_text, re.MULTILINE))
    if pipe_count > 0:
        issues.append({"type": "pipe_prefix", "count": pipe_count})

    # Line number corruption:  N|content
    line_no_count = len(re.findall(r'^\s*\d+\|##', index_text, re.MULTILINE))
    if line_no_count > 0:
        issues.append({"type": "line_number_prefix", "count": line_no_count})

    # Triple bracket: [[[slug]]
    triple_count = len(re.findall(r'\[\[\[', index_text))
    if triple_count > 0:
        issues.append({"type": "triple_bracket", "count": triple_count})

    # Space-prefixed list: ' - [[slug]]'
    space_prefix_count = len(re.findall(r'^ - \[\[', index_text, re.MULTILINE))
    if space_prefix_count > 0:
        issues.append({"type": "space_prefix", "count": space_prefix_count})

    return {
        "has_issues": len(issues) > 0,
        "issues": issues if issues else None,
    }


def section_jp_content() -> str:
    """Generate JP content monitoring section for markdown report."""
    stats = _count_jp_content()
    if stats["total_files"] == 0:
        return "## 🇯🇵 Japanese Content\n\n✅ **Zero Japanese characters** in wiki body content.\n"
    
    lines = [
        "## 🇯🇵 Japanese Content Monitoring",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Files with JP | {stats['total_files']} |",
        f"| Total JP chars | {stats['total_jp_chars']:,} |",
        "",
        "### Top 10 Files (by JP char count)",
        "",
    ]
    for item in stats["top_10"]:
        lines.append(f"- `{item['file']}` — {item['jp_chars']:,} JP chars")
    
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Wiki Health Digest")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of markdown")
    args = parser.parse_args()

    l2 = load_l2_pages()
    raw = load_raw_articles()

    if args.json:
        data = build_json(l2, raw)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        report_parts = [
            f"# 🩺 Wiki Health Digest — {TODAY.strftime('%Y-%m-%d')}\n",
            section_overview(l2, raw),
            section_stale_pages(l2),
            section_unprocessed_raw(l2, raw),
            section_orphan_pages(l2),
            section_growth(l2),
            section_tag_distribution(l2),
            section_jp_content(),
            "---\n_Generated by `scripts/wiki_health.py`_\n",
        ]
        print("\n\n".join(report_parts))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"# Wiki Health Digest — ERROR\n\n```\n{exc}\n```", file=sys.stderr)
        raise SystemExit(1)
