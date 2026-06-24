#!/usr/bin/env python3
"""
Detect clusters of flat concept pages that could be grouped into subdirectories.

Reads all concept pages (excluding existing subdirs), analyzes:
  1. Common prefixes in filenames
  2. Tag co-occurrence clusters
  3. Wikilink density (pages that heavily cross-link)
  4. Existing subdirectory sizes (for comparison)

Outputs a JSON report with proposed groupings.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", os.path.expanduser("~/ai-topics/wiki")))
CONCEPTS_DIR = WIKI_ROOT / "concepts"

# Minimum cluster size to propose
MIN_CLUSTER = 3

# Known existing subdirs (skip these)
EXISTING_SUBDIRS = set()


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter as dict (lightweight, no yaml dep)."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    current_key = None
    for line in m.group(1).split("\n"):
        km = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if km:
            current_key = km.group(1)
            val = km.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                # inline list
                fm[current_key] = [v.strip().strip('"').strip("'")
                                   for v in val[1:-1].split(",") if v.strip()]
            elif val:
                fm[current_key] = val
            else:
                fm[current_key] = []
        elif current_key and line.strip().startswith("- "):
            if not isinstance(fm.get(current_key), list):
                fm[current_key] = []
            fm[current_key].append(line.strip()[2:].strip().strip('"').strip("'"))
    return fm


def extract_wikilinks(text: str) -> list:
    """Extract [[wikilink]] targets."""
    return re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", text)


def get_existing_subdirs():
    """Find existing subdirectories under concepts/."""
    if not CONCEPTS_DIR.exists():
        return set()
    return {d.name for d in CONCEPTS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith(".")}


def collect_flat_pages():
    """Collect all flat (non-subdir) concept pages with metadata."""
    pages = []
    if not CONCEPTS_DIR.exists():
        return pages
    for f in sorted(CONCEPTS_DIR.iterdir()):
        if not f.is_file() or not f.suffix == ".md":
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        links = extract_wikilinks(text)
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        pages.append({
            "slug": f.stem,
            "filename": f.name,
            "title": fm.get("title", f.stem),
            "tags": tags,
            "type": fm.get("type", "concept"),
            "links": links,
            "link_count": len(links),
            "lines": text.count("\n") + 1,
        })
    return pages


def detect_prefix_clusters(pages: list) -> list:
    """Detect pages sharing common filename prefixes."""
    prefixes = defaultdict(list)
    for p in pages:
        slug = p["slug"]
        # Try 2-part prefixes: "foo-bar-baz" → "foo-bar", "foo"
        parts = slug.split("-")
        for i in range(1, len(parts)):
            prefix = "-".join(parts[:i])
            if len(prefix) >= 3:  # skip very short prefixes
                prefixes[prefix].append(p["slug"])

    clusters = []
    for prefix, members in sorted(prefixes.items()):
        if len(members) >= MIN_CLUSTER:
            # Deduplicate: only keep if prefix is meaningful
            # (not just a common word like "ai" or "the")
            clusters.append({
                "type": "prefix",
                "prefix": prefix,
                "members": sorted(set(members)),
                "count": len(set(members)),
            })

    # Remove subsumed clusters (prefix "foo" subsumes "foo-bar")
    clusters.sort(key=lambda c: c["count"], reverse=True)
    pruned = []
    seen_members = set()
    for c in clusters:
        new_members = set(c["members"]) - seen_members
        if len(new_members) >= MIN_CLUSTER:
            c["members"] = sorted(new_members)
            c["count"] = len(new_members)
            pruned.append(c)
            seen_members.update(new_members)
    return pruned


def detect_tag_clusters(pages: list) -> list:
    """Detect pages that share specific tags (beyond generic ones)."""
    tag_pages = defaultdict(list)
    generic_tags = {"concept", "ai", "llm", "technology", "overview"}

    for p in pages:
        for tag in p["tags"]:
            if tag.lower() not in generic_tags:
                tag_pages[tag].append(p["slug"])

    clusters = []
    for tag, members in sorted(tag_pages.items()):
        if len(members) >= MIN_CLUSTER:
            clusters.append({
                "type": "tag",
                "tag": tag,
                "members": sorted(set(members)),
                "count": len(set(members)),
            })
    clusters.sort(key=lambda c: c["count"], reverse=True)
    return clusters


def detect_link_clusters(pages: list) -> list:
    """Detect pages that form a dense cross-linking subgraph."""
    # Build adjacency: page A links to page B
    page_slugs = {p["slug"] for p in pages}
    link_graph = defaultdict(set)
    for p in pages:
        for link in p["links"]:
            # Normalize: strip path prefix, get slug
            target = link.split("/")[-1]
            if target in page_slugs:
                link_graph[p["slug"]].add(target)

    # Find mutual link pairs
    mutual = defaultdict(set)
    for a, targets in link_graph.items():
        for b in targets:
            if a in link_graph.get(b, set()) or b in link_graph:
                mutual[a].add(b)
                mutual[b].add(a)

    # Greedy clustering: seed with highest-degree node, expand
    clusters = []
    used = set()
    for slug in sorted(mutual, key=lambda s: len(mutual[s]), reverse=True):
        if slug in used:
            continue
        group = {slug}
        for neighbor in mutual[slug]:
            if neighbor not in used:
                # Check if neighbor links to most of the group
                neighbor_links = link_graph.get(neighbor, set())
                overlap = len(group & neighbor_links) / len(group) if group else 0
                if overlap >= 0.3:
                    group.add(neighbor)
        if len(group) >= MIN_CLUSTER:
            clusters.append({
                "type": "link-cluster",
                "seed": slug,
                "members": sorted(group),
                "count": len(group),
            })
            used.update(group)
    return clusters


def generate_report(pages, prefix_clusters, tag_clusters, link_clusters, existing_subdirs):
    """Generate the full analysis report."""
    report = {
        "summary": {
            "total_flat_pages": len(pages),
            "existing_subdirs": sorted(existing_subdirs),
            "existing_subdir_count": len(existing_subdirs),
        },
        "prefix_clusters": prefix_clusters[:15],
        "tag_clusters": tag_clusters[:15],
        "link_clusters": link_clusters[:10],
        "recommendations": [],
    }

    # Generate recommendations
    # Priority: prefix clusters with high count > tag clusters > link clusters
    seen_slugs = set()
    for pc in prefix_clusters[:10]:
        new_members = [m for m in pc["members"] if m not in seen_slugs]
        if len(new_members) >= MIN_CLUSTER:
            report["recommendations"].append({
                "action": "create_subdir",
                "proposed_dir": pc["prefix"],
                "reason": f"Common prefix '{pc['prefix']}' ({len(new_members)} pages)",
                "members": new_members,
                "priority": "high" if len(new_members) >= 5 else "medium",
            })
            seen_slugs.update(new_members)

    for tc in tag_clusters[:10]:
        new_members = [m for m in tc["members"] if m not in seen_slugs]
        if len(new_members) >= MIN_CLUSTER:
            report["recommendations"].append({
                "action": "create_subdir",
                "proposed_dir": tc["tag"],
                "reason": f"Shared tag '{tc['tag']}' ({len(new_members)} pages)",
                "members": new_members,
                "priority": "medium" if len(new_members) >= 5 else "low",
            })
            seen_slugs.update(new_members)

    for lc in link_clusters[:5]:
        new_members = [m for m in lc["members"] if m not in seen_slugs]
        if len(new_members) >= MIN_CLUSTER:
            report["recommendations"].append({
                "action": "consider_grouping",
                "proposed_dir": lc["seed"],
                "reason": f"Dense cross-link cluster around '{lc['seed']}' ({len(new_members)} pages)",
                "members": new_members,
                "priority": "low",
            })
            seen_slugs.update(new_members)

    return report


def main():
    global EXISTING_SUBDIRS
    EXISTING_SUBDIRS = get_existing_subdirs()

    pages = collect_flat_pages()
    if not pages:
        print("No flat concept pages found.")
        sys.exit(0)

    prefix_clusters = detect_prefix_clusters(pages)
    tag_clusters = detect_tag_clusters(pages)
    link_clusters = detect_link_clusters(pages)

    report = generate_report(
        pages, prefix_clusters, tag_clusters, link_clusters, EXISTING_SUBDIRS
    )

    # Output
    output_path = Path(os.path.expanduser("~/ai-topics/scripts/hierarchy_report.json"))
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
