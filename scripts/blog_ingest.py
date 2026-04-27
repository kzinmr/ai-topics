#!/usr/bin/env python3
"""Blog RSS ingest checkpoint producer for Hermes cron."""

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup
from readability import Document

from daily_inbox_collect import TODAY, query_todays_articles, run_blogwatcher_scan


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = HERMES_HOME.parent
AI_TOPICS_REPO = Path(os.environ.get("AI_TOPICS_REPO", str(PROFILE_ROOT / "ai-topics")))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", str(AI_TOPICS_REPO / "wiki")))
CHECKPOINT_DIR = HERMES_HOME / "cron" / "data" / "blog_ingest"
LATEST_PATH = CHECKPOINT_DIR / "latest.json"
RAW_ARTICLES_DIR = WIKI_ROOT / "raw" / "articles"

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HermesBot/1.0)",
    "Accept": "text/html,application/xhtml+xml",
}


def url_to_filename(url: str) -> str:
    digest = hashlib.md5(url.encode()).hexdigest()[:8]
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    slug = re.sub(r"[^a-z0-9]+", "-", parsed.path.lower()).strip("-")[:60]
    return f"{domain}--{slug}--{digest}.md"


def scrape_url(url: str) -> dict | None:
    try:
        with httpx.Client(timeout=30, follow_redirects=True, headers=HTTP_HEADERS) as client:
            resp = client.get(url)
            resp.raise_for_status()
    except Exception:
        return None

    if "text/html" not in resp.headers.get("content-type", ""):
        return None

    try:
        doc = Document(resp.text)
        title = doc.short_title() or "Untitled"
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, "html.parser")
        content = soup.get_text(separator="\n", strip=True)
    except Exception:
        return None

    if len(content) < 100:
        return None

    return {
        "title": title,
        "url": url,
        "content": content,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def save_article(raw: dict, source_name: str) -> str:
    RAW_ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_ARTICLES_DIR / url_to_filename(raw["url"])
    frontmatter = (
        "---\n"
        f"title: \"{raw['title'].replace('\"', '\\\"')}\"\n"
        f"url: \"{raw['url']}\"\n"
        f"fetched_at: {raw['fetched_at']}\n"
        f"source: \"{source_name}\"\n"
        "tags: [blog, raw]\n"
        "---\n\n"
    )
    body = f"# {raw['title']}\n\nSource: {raw['url']}\n\n{raw['content']}\n"
    path.write_text(frontmatter + body, encoding="utf-8")
    return str(path)


def persist_blog_articles(articles: dict) -> tuple[list[dict], list[dict]]:
    saved = []
    unsaved = []
    for item in articles.get("blog_articles", []):
        url = item.get("url", "").strip()
        title = item.get("title", "").strip()
        blog = item.get("blog", "").strip()
        if not url:
            continue
        raw = scrape_url(url)
        if raw is None:
            unsaved.append({"blog": blog, "title": title, "url": url})
            continue
        raw_path = save_article(raw, blog)
        saved.append({
            "blog": blog,
            "title": raw["title"] or title,
            "url": url,
            "raw_path": raw_path,
        })
    return saved, unsaved


def main():
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archive_path = CHECKPOINT_DIR / f"blog_ingest_{run_id}.json"
    scan = run_blogwatcher_scan()
    articles = query_todays_articles()
    saved_articles, unsaved_articles = persist_blog_articles(articles)
    output = {
        "ok": not bool(scan.get("error") and articles.get("error")),
        "date": TODAY,
        "run_id": run_id,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint_path": str(LATEST_PATH),
        "archive_path": str(archive_path),
        "scan": scan,
        "articles": articles,
        "saved_articles": saved_articles,
        "unsaved_articles": unsaved_articles,
    }
    payload = json.dumps(output, indent=2, ensure_ascii=False)
    LATEST_PATH.write_text(payload)
    archive_path.write_text(payload)
    sys.stdout.write(payload)


if __name__ == "__main__":
    main()
