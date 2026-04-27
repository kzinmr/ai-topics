#!/usr/bin/env python3
"""Daily Inbox Collector — pre-run script for Hermes cron.

Runs blogwatcher-cli scan, queries the DB for today's new articles,
and reads the newsletter digest. Outputs structured JSON to stdout
for the Hermes agent to triage and process.

Exit 0 even on partial failure — partial data is still useful.
"""
import json
import os
import sqlite3
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path.home() / ".blogwatcher-cli" / "blogwatcher-cli.db"
INBOX_NL = Path.home() / "ai-topics" / "inbox" / "newsletters"
WIKI_CONCEPTS = Path.home() / "ai-topics" / "wiki" / "concepts"
WIKI_ENTITIES = Path.home() / "ai-topics" / "wiki" / "entities"

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def run_blogwatcher_scan() -> dict:
    """Run blogwatcher-cli scan and parse stdout."""
    result = {"ran": False, "stdout": "", "succeeded": 0, "failed": 0, "total": 0,
              "failures": [], "new_from_scan": 0}
    try:
        proc = subprocess.run(
            [str(Path.home() / "bin" / "blogwatcher-cli"), "scan"],
            capture_output=True, text=True, timeout=120,
        )
        result["ran"] = True
        result["stdout"] = proc.stdout + proc.stderr
        # Parse summary line: "Scanned N blog(s): M succeeded, K failed"
        for line in result["stdout"].splitlines():
            if "Scanned" in line and "succeeded" in line:
                import re
                m = re.search(r"Scanned (\d+).*?(\d+) succeeded.*?(\d+) failed", line)
                if m:
                    result["total"] = int(m.group(1))
                    result["succeeded"] = int(m.group(2))
                    result["failed"] = int(m.group(3))
            if "Found" in line and "new article" in line:
                import re
                m = re.search(r"Found (\d+) new", line)
                if m:
                    result["new_from_scan"] = int(m.group(1))
        # Parse failures
        current_blog = None
        for line in result["stdout"].splitlines():
            stripped = line.strip()
            if stripped.startswith("Error:"):
                if current_blog:
                    result["failures"].append({"blog": current_blog, "error": stripped})
            elif stripped and not stripped.startswith("Source:") and not stripped.startswith("Found") and not stripped.startswith("Scanned"):
                current_blog = stripped
    except Exception as e:
        result["error"] = str(e)
    return result


def query_todays_articles() -> dict:
    """Query DB for articles discovered today."""
    data = {"total": 0, "by_blog": {}, "blog_articles": [], "reddit_articles": {}}
    if not DB_PATH.exists():
        data["error"] = "DB not found"
        return data
    try:
        conn = sqlite3.connect(str(DB_PATH))
        conn.row_factory = sqlite3.Row

        # Count per blog
        rows = conn.execute("""
            SELECT b.name, COUNT(*) as cnt
            FROM articles a JOIN blogs b ON a.blog_id = b.id
            WHERE DATE(a.discovered_date) = ?
            GROUP BY b.name ORDER BY cnt DESC;
        """, (TODAY,)).fetchall()
        for r in rows:
            data["by_blog"][r["name"]] = r["cnt"]
            data["total"] += r["cnt"]

        # Non-Reddit articles (all)
        rows = conn.execute("""
            SELECT b.name, a.title, a.url
            FROM articles a JOIN blogs b ON a.blog_id = b.id
            WHERE DATE(a.discovered_date) = ?
              AND b.name NOT LIKE 'r/%'
            ORDER BY b.name;
        """, (TODAY,)).fetchall()
        data["blog_articles"] = [{"blog": r["name"], "title": r["title"], "url": r["url"]} for r in rows]

        # Reddit articles (max 5 per sub)
        for sub in ["r/LocalLLaMA", "r/LocalLLM", "r/AI_Agents"]:
            rows = conn.execute("""
                SELECT a.title, a.url
                FROM articles a JOIN blogs b ON a.blog_id = b.id
                WHERE DATE(a.discovered_date) = ? AND b.name = ?
                ORDER BY a.id DESC LIMIT 5;
            """, (TODAY, sub)).fetchall()
            if rows:
                data["reddit_articles"][sub] = [{"title": r["title"], "url": r["url"]} for r in rows]

        conn.close()
    except Exception as e:
        data["error"] = str(e)
    return data


def read_newsletter() -> dict:
    """Read today's newsletter digest if it exists."""
    data = {"exists": False}
    nl_path = INBOX_NL / f"{TODAY}-newsletter.md"
    if not nl_path.exists():
        return data
    try:
        content = nl_path.read_text()
        data["exists"] = True
        data["path"] = str(nl_path)
        data["size_bytes"] = len(content)
        # Extract subject
        for line in content.splitlines():
            if line.startswith("**Subject:**"):
                data["subject"] = line.replace("**Subject:**", "").strip()
            if line.startswith("**Articles scraped:**"):
                try:
                    data["articles_scraped"] = int(line.split(":")[-1].strip())
                except ValueError:
                    pass
        # Extract article titles and URLs (## N. Title  then - **URL:** ...)
        articles = []
        current_title = None
        seen_titles = set()
        for line in content.splitlines():
            if line.startswith("## ") and line[3:4].isdigit():
                # e.g. "## 1. The inevitable need..."
                current_title = line.split(".", 1)[-1].strip() if "." in line else line[3:].strip()
            elif line.strip().startswith("- **URL:**") and current_title:
                url = line.split("**URL:**")[-1].strip()
                if current_title not in seen_titles:
                    articles.append({"title": current_title, "url": url})
                    seen_titles.add(current_title)
                current_title = None
        data["articles"] = articles
    except Exception as e:
        data["error"] = str(e)
    return data


def get_existing_wiki_topics() -> set:
    """Get set of existing wiki concept/entity filenames for dedup."""
    topics = set()
    for d in [WIKI_CONCEPTS, WIKI_ENTITIES]:
        if d.exists():
            for f in d.rglob("*.md"):
                topics.add(f.stem)  # e.g. "claude-mythos-glasswing"
    return topics


def main():
    output = {
        "date": TODAY,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "scan": run_blogwatcher_scan(),
        "articles": query_todays_articles(),
        "newsletter": read_newsletter(),
        "existing_wiki_topics": sorted(get_existing_wiki_topics()),
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
