#!/usr/bin/env python3
"""Weekly Dreaming — Phase 1: Data Collection

Collects the past week's inbox data (RSS scans + newsletters) and outputs
structured JSON for the LLM to analyze during Phase 2 (REM + Deep Sleep).

The script runs BEFORE the LLM processes the dreaming task. Its stdout is
injected into the cron prompt as context.
"""

import json
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# Paths
INBOX_DIR = Path.home() / "ai-topics" / "inbox"
RSS_SCANS_DIR = INBOX_DIR / "rss-scans"
NEWSLETTERS_DIR = INBOX_DIR / "newsletters"
WIKI_DIR = Path.home() / "wiki"
CONCEPTS_DIR = WIKI_DIR / "concepts"
ENTITIES_DIR = WIKI_DIR / "entities"
COMPARISONS_DIR = WIKI_DIR / "comparisons"
QUERIES_DIR = WIKI_DIR / "queries"
RAW_ARTICLES_DIR = WIKI_DIR / "raw" / "articles"

WEEK_DAYS = 7
MAX_ARTICLES = 300  # Prevent context overflow


def get_date_range():
    """Return (start_date, end_date) strings for the past N days."""
    today = datetime.now()
    start = today - timedelta(days=WEEK_DAYS)
    return start.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")


def collect_daily_scans(start_date, end_date):
    """Parse articles from daily RSS scan reports."""
    articles = []
    if not RSS_SCANS_DIR.exists():
        print(f"WARNING: RSS scans directory not found: {RSS_SCANS_DIR}", file=sys.stderr)
        return articles

    for scan_file in sorted(RSS_SCANS_DIR.glob("daily-scan-*.md")):
        match = re.search(r"daily-scan-(\d{4}-\d{2}-\d{2})\.md", scan_file.name)
        if not match:
            continue
        scan_date = match.group(1)
        if not (start_date <= scan_date <= end_date):
            continue

        try:
            content = scan_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"WARNING: Failed to read {scan_file.name}: {e}", file=sys.stderr)
            continue

        # Pattern: - [Title](URL) — source
        for line in content.splitlines():
            m = re.match(r"-\s*\[([^\]]+)\]\(([^)]+)\)\s*[—\-]\s*(.*)", line.strip())
            if m:
                title, url, source = m.groups()
                # Skip non-article lines (Reddit section headers, etc.)
                if title.startswith("#") or title.startswith("##"):
                    continue
                articles.append({
                    "title": title.strip(),
                    "url": url.strip(),
                    "source": source.strip(),
                    "date": scan_date,
                    "type": "rss_scan",
                })

    return articles


def collect_newsletters(start_date, end_date):
    """Parse articles from newsletter digests."""
    articles = []
    if not NEWSLETTERS_DIR.exists():
        print(f"WARNING: Newsletters directory not found: {NEWSLETTERS_DIR}", file=sys.stderr)
        return articles

    for nl_file in sorted(NEWSLETTERS_DIR.glob("*-newsletter.md")):
        match = re.search(r"(\d{4}-\d{2}-\d{2})-newsletter\.md", nl_file.name)
        if not match:
            continue
        nl_date = match.group(1)
        if not (start_date <= nl_date <= end_date):
            continue

        try:
            content = nl_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"WARNING: Failed to read {nl_file.name}: {e}", file=sys.stderr)
            continue

        current_title = None
        for line in content.splitlines():
            m_title = re.match(r"##\s*\d+\.\s*(.+)", line.strip())
            if m_title:
                current_title = m_title.group(1).strip()
            m_url = re.match(r"-\s*\*\*URL:\*\*\s*(.+)", line.strip())
            if m_url and current_title:
                articles.append({
                    "title": current_title,
                    "url": m_url.group(1).strip(),
                    "source": "newsletter",
                    "date": nl_date,
                    "type": "newsletter",
                })
                current_title = None

    return articles


def list_existing_wiki_pages():
    """List existing wiki pages across all Layer 2 directories."""
    pages = []
    for subdir in [CONCEPTS_DIR, ENTITIES_DIR, COMPARISONS_DIR, QUERIES_DIR]:
        if subdir.exists():
            for page_file in sorted(subdir.rglob("*.md")):
                if page_file.name == "_index.md":
                    continue
                rel = page_file.relative_to(WIKI_DIR)
                pages.append(str(rel))
    return pages


def count_recent_raw_articles():
    """Count raw articles modified in the past week."""
    if not RAW_ARTICLES_DIR.exists():
        return 0
    week_ago = time.time() - (WEEK_DAYS * 24 * 60 * 60)
    count = 0
    for f in RAW_ARTICLES_DIR.glob("*.md"):
        if f.stat().st_mtime > week_ago:
            count += 1
    return count


def count_by_source(articles):
    """Count articles per source."""
    counts = {}
    for art in articles:
        src = art["source"]
        counts[src] = counts.get(src, 0) + 1
    return counts


def count_by_date(articles):
    """Count articles per date."""
    counts = {}
    for art in articles:
        d = art["date"]
        counts[d] = counts.get(d, 0) + 1
    return counts


def main():
    start_date, end_date = get_date_range()

    print(f"Collecting weekly data: {start_date} to {end_date}", file=sys.stderr)

    rss_articles = collect_daily_scans(start_date, end_date)
    print(f"  RSS scan articles: {len(rss_articles)}", file=sys.stderr)

    nl_articles = collect_newsletters(start_date, end_date)
    print(f"  Newsletter articles: {len(nl_articles)}", file=sys.stderr)

    all_articles = rss_articles + nl_articles
    # Truncate if too many
    truncated = len(all_articles) > MAX_ARTICLES
    if truncated:
        print(f"  WARNING: Truncating from {len(all_articles)} to {MAX_ARTICLES} articles", file=sys.stderr)
        all_articles = all_articles[:MAX_ARTICLES]

    existing_pages = list_existing_wiki_pages()
    print(f"  Existing wiki pages: {len(existing_pages)}", file=sys.stderr)

    recent_raw = count_recent_raw_articles()
    print(f"  Recent raw articles (past week): {recent_raw}", file=sys.stderr)

    source_counts = count_by_source(all_articles)
    date_counts = count_by_date(all_articles)

    output = {
        "week_range": {"start": start_date, "end": end_date},
        "total_articles": len(all_articles),
        "rss_articles": len(rss_articles),
        "newsletter_articles": len(nl_articles),
        "recent_raw_articles": recent_raw,
        "truncated": truncated,
        "source_counts": source_counts,
        "date_counts": date_counts,
        "articles": all_articles,
        "existing_wiki_pages": existing_pages,
    }

    # Output JSON to stdout (injected into cron prompt)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
