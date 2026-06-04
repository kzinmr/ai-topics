#!/usr/bin/env python3
"""Collect and checkpoint RSS/blog articles for Hermes cron pipeline.

Exports:
    TODAY              – today's date string (YYYY-MM-DD)
    query_todays_articles() → dict  – articles keyed by source type
    run_blogwatcher_scan() → dict   – scan results (ok / error)
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# ── Configuration ──────────────────────────────────────────────────────────

PROFILE_ROOT = Path(os.environ.get("HERMES_PROFILE_ROOT") or os.environ.get("HERMES_SUBPROCESS_HOME") or Path.home()).expanduser()
BLOGWATCHER_BIN = os.environ.get("BLOGWATCHER_BIN", str(PROFILE_ROOT / "bin" / "blogwatcher-cli"))
# The blogwatcher CLI uses ~/.blogwatcher/blogwatcher.db (old schema, not blogwatcher-cli)
# Use PROFILE_ROOT instead of Path.home() because cron HOME may differ from the actual user home
_BW_HOME = PROFILE_ROOT / ".blogwatcher"
BLOGWATCHER_DB = _BW_HOME / "blogwatcher.db"
BLOGWATCHER_WORKERS = 8
BLOGWATCHER_SILENT = True


# ── Date ───────────────────────────────────────────────────────────────────

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ── Blogwatcher scan ──────────────────────────────────────────────────────

def run_blogwatcher_scan() -> dict:
    """Run `blogwatcher-cli scan` and return results as a dict.

    Returns:
        {
            "ok": True / False,
            "scan_done_at": "...",
            "total_new": 0,
            "blogs_scanned": 0,
            "error": None | str
        }
    """
    env = {**os.environ, "BLOGWATCHER_YES": "1", "HOME": str(PROFILE_ROOT)}
    if BLOGWATCHER_SILENT:
        env["BLOGWATCHER_SILENT"] = "1"

    cmd = [
        BLOGWATCHER_BIN, "scan",
        "--workers", str(BLOGWATCHER_WORKERS),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env)

    if result.returncode != 0:
        return {
            "ok": False,
            "error": result.stderr.strip() or f"exit code {result.returncode}",
            "scan_done_at": datetime.now(timezone.utc).isoformat(),
        }

    stdout = result.stdout.strip()
    if not stdout:
        return {
            "ok": True,
            "total_new": 0,
            "blogs_scanned": 0,
            "scan_done_at": datetime.now(timezone.utc).isoformat(),
        }

    # Parse scan output like:
    #   Scanning 3 blog(s)...
    #   blog1   Source: RSS | Found: 2 | New: 1
    #   blog2   Source: HTML  | Found: 0 | New: 0
    #   blog3   Source: RSS | Found: 1 | New: 0
    #   Found 1 new article(s) total!

    new_total = 0
    blogs_scanned = 0
    new_articles_per_blog = {}

    # Extract total
    m = re.search(r"Found\s+(\d+)\s+new article\(s\)\s+total!", stdout)
    if m:
        new_total = int(m.group(1))

    # Extract per-blog lines
    for line in stdout.splitlines():
        bm = re.match(r"^\s*(\S+)\s+Source:\s+\S+\s+\|\s+Found:\s+(\d+)\s+\|\s+New:\s+(\d+)", line)
        if bm:
            blog_name = bm.group(1)
            found = int(bm.group(2))
            new = int(bm.group(3))
            new_total += new
            blogs_scanned += 1
            new_articles_per_blog[blog_name] = new

    return {
        "ok": True,
        "total_new": new_total,
        "blogs_scanned": blogs_scanned,
        "new_articles_per_blog": new_articles_per_blog,
        "scan_done_at": datetime.now(timezone.utc).isoformat(),
    }


# ── Query articles from blogwatcher DB ────────────────────────────────────

def query_todays_articles() -> dict:
    """Query the blogwatcher SQLite DB for TODAY's articles and return a structured dict.

    Only returns articles discovered in the last 24 hours (not all unread articles).
    Also filters out already-read articles to avoid re-processing.

    Returns:
        {
            "blog_articles": [...],   # list of {url, title, blog}
            "total": 0,
            "error": None | str
        }
    """
    if not BLOGWATCHER_DB.exists():
        return {
            "blog_articles": [],
            "total": 0,
            "error": "blogwatcher DB not found",
        }

    try:
        import sqlite3
        conn = sqlite3.connect(str(BLOGWATCHER_DB))
        conn.row_factory = sqlite3.Row
    except Exception as e:
        return {
            "blog_articles": [],
            "total": 0,
            "error": f"sqlite connect failed: {e}",
        }

    try:
        cur = conn.cursor()

        # Only fetch articles discovered in the last 24 hours that haven't been read yet
        cur.execute("""
            SELECT a.title, a.url, b.name AS blog,
                   a.discovered_date, a.is_read
            FROM articles a
            JOIN blogs b ON a.blog_id = b.id
            WHERE a.is_read = 0
              AND a.discovered_date >= datetime('now', '-24 hours')
            ORDER BY a.discovered_date DESC
            LIMIT 20
        """)
        rows = cur.fetchall()

        articles = []
        seen_urls = set()
        for row in rows:
            url = row["url"].strip()
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)
            articles.append({
                "url": url,
                "title": row["title"] or "",
                "blog": row["blog"] or "",
            })

        return {
            "blog_articles": articles,
            "total": len(articles),
        }
    except Exception as e:
        return {
            "blog_articles": [],
            "total": 0,
            "error": f"query failed: {e}",
        }
    finally:
        conn.close()


def mark_articles_as_read(articles: list[dict]) -> int:
    """Mark articles as read in the blogwatcher DB to prevent re-processing.
    
    Args:
        articles: List of {url, ...} dicts to mark as read.
    
    Returns:
        Number of articles marked as read.
    """
    if not BLOGWATCHER_DB.exists() or not articles:
        return 0
    
    try:
        import sqlite3
        conn = sqlite3.connect(str(BLOGWATCHER_DB))
        cur = conn.cursor()
        urls = [a.get("url", "") for a in articles if a.get("url")]
        placeholders = ",".join(["?"] * len(urls))
        cur.execute(f"UPDATE articles SET is_read = 1 WHERE url IN ({placeholders})", urls)
        count = cur.rowcount
        conn.commit()
        conn.close()
        return count
    except Exception as e:
        import logging
        logging.warning(f"Failed to mark articles as read: {e}")
        return 0


# ── Main (for standalone testing) ────────────────────────────────────────

if __name__ == "__main__":
    scan = run_blogwatcher_scan()
    articles = query_todays_articles()

    output = {
        "today": TODAY,
        "scan": scan,
        "articles": articles,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
