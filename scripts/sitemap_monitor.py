#!/usr/bin/env python3
"""
Sitemap-based blog monitor for company tech blogs without RSS feeds.
Currently monitors Anthropic Engineering. Extensible to other sitemap-based sources.

Outputs JSON compatible with the blog-triage pipeline:
{
  "source": "sitemap",
  "timestamp": "ISO8601",
  "sources": [
    {
      "name": "Anthropic Engineering",
      "url": "https://www.anthropic.com/engineering",
      "sitemap_url": "https://www.anthropic.com/sitemap.xml",
      "url_pattern": "/engineering/",
      "new_articles": [...],
      "saved_articles": [...]
    }
  ]
}
"""

import json
import os
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import httpx

# --- Configuration ---
SOURCES = [
    {
        "name": "Anthropic Engineering",
        "url": "https://www.anthropic.com/engineering",
        "sitemap_url": "https://www.anthropic.com/sitemap.xml",
        "url_pattern": "/engineering/",
        "state_file": os.path.expanduser("~/.hermes/processed_anthropic_engineering.json"),
    },
]

WIKI_RAW_DIR = os.path.expanduser("~/wiki/raw/articles")
CHECKPOINT_DIR = os.path.expanduser("~/.hermes/cron/data/sitemap_monitor")
REQUEST_TIMEOUT = 30


def fetch_sitemap(url: str) -> str:
    """Fetch sitemap XML content."""
    with httpx.Client(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
        resp = client.get(url)
        resp.raise_for_status()
        return resp.text


def parse_sitemap(xml_content: str, url_pattern: str) -> list[dict]:
    """Parse sitemap XML, filter URLs matching url_pattern, return [{url, lastmod}]."""
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_content)
    
    articles = []
    for url_elem in root.findall("sm:url", ns):
        loc = url_elem.find("sm:loc", ns)
        lastmod = url_elem.find("sm:lastmod", ns)
        
        if loc is None or loc.text is None:
            continue
        if url_pattern not in loc.text:
            continue
        
        article = {"url": loc.text.strip()}
        if lastmod is not None and lastmod.text:
            article["lastmod"] = lastmod.text.strip()
        articles.append(article)
    
    return articles


def load_state(state_file: str) -> set:
    """Load previously seen URLs from state file."""
    if not os.path.exists(state_file):
        return set()
    try:
        with open(state_file) as f:
            data = json.load(f)
            return set(data.get("seen_urls", []))
    except (json.JSONDecodeError, KeyError):
        return set()


def save_state(state_file: str, seen_urls: set):
    """Save seen URLs to state file."""
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    with open(state_file, "w") as f:
        json.dump({"seen_urls": sorted(seen_urls), "updated": datetime.now(timezone.utc).isoformat()}, f, indent=2)


def scrape_article(url: str) -> dict | None:
    """Scrape an article URL and return {url, title, content_md}."""
    try:
        with httpx.Client(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
            resp = client.get(url)
            resp.raise_for_status()
            
        # Basic extraction: look for <title> and <article> content
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, "html.parser")
        
        title = soup.title.string if soup.title else url.rstrip("/").split("/")[-1]
        title = title.replace(" \\ Anthropic", "").strip()  # Clean Anthropic title suffix
        
        # Try to find main article content
        article = soup.find("article")
        if article:
            content = article.get_text(separator="\n", strip=True)
        else:
            # Fallback: get all text from body
            body = soup.find("body")
            content = body.get_text(separator="\n", strip=True) if body else resp.text
        
        # Truncate very long content
        if len(content) > 50000:
            content = content[:50000] + "\n\n[... truncated]"
        
        return {"url": url, "title": title, "content_md": content}
    except Exception as e:
        print(f"  [!] Failed to scrape {url}: {e}", file=sys.stderr)
        return {"url": url, "title": url.rstrip("/").split("/")[-1], "content_md": f"Scrape failed: {e}"}


def save_raw_article(article: dict, source_name: str) -> str:
    """Save article as raw markdown file. Returns the file path."""
    os.makedirs(WIKI_RAW_DIR, exist_ok=True)
    
    slug = article["url"].rstrip("/").split("/")[-1]
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}_anthropic-engineering_{slug}.md"
    filepath = os.path.join(WIKI_RAW_DIR, filename)
    
    content = f"""---
title: "{article.get('title', slug)}"
source: "{source_name}"
url: "{article['url']}"
scraped: "{datetime.now(timezone.utc).isoformat()}"
lastmod: "{article.get('lastmod', 'unknown')}"
type: "sitemap"
---

# {article.get('title', slug)}

**Source**: [{article['url']}]({article['url']})

{article.get('content_md', '')}
"""
    with open(filepath, "w") as f:
        f.write(content)
    
    return filepath


def main():
    start_time = datetime.now(timezone.utc)
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    
    result = {
        "source": "sitemap",
        "timestamp": start_time.isoformat(),
        "sources": [],
    }
    
    total_new = 0
    
    for source in SOURCES:
        print(f"\n[{source['name']}] Fetching sitemap: {source['sitemap_url']}")
        
        try:
            xml_content = fetch_sitemap(source["sitemap_url"])
        except Exception as e:
            print(f"  [!] Failed to fetch sitemap: {e}", file=sys.stderr)
            result["sources"].append({
                "name": source["name"],
                "error": str(e),
                "new_articles": [],
                "saved_articles": [],
            })
            continue
        
        articles = parse_sitemap(xml_content, source["url_pattern"])
        print(f"  Found {len(articles)} matching articles in sitemap")
        
        seen_urls = load_state(source["state_file"])
        new_articles = [a for a in articles if a["url"] not in seen_urls]
        
        print(f"  New: {len(new_articles)}, Previously seen: {len(seen_urls) - len(new_articles)}")
        
        saved = []
        for article in new_articles:
            print(f"  Scraping: {article['url']}")
            scraped = scrape_article(article["url"])
            if scraped:
                scraped["lastmod"] = article.get("lastmod")
                filepath = save_raw_article(scraped, source["name"])
                saved.append({"url": article["url"], "title": scraped.get("title"), "filepath": filepath})
        
        # Update state
        all_urls = seen_urls | {a["url"] for a in articles}
        save_state(source["state_file"], all_urls)
        
        result["sources"].append({
            "name": source["name"],
            "url": source["url"],
            "total_in_sitemap": len(articles),
            "new_articles": [{"url": a["url"], "lastmod": a.get("lastmod")} for a in new_articles],
            "saved_articles": saved,
        })
        total_new += len(new_articles)
    
    # Write checkpoint
    timestamp = start_time.strftime("%Y%m%d_%H%M%S")
    checkpoint_path = os.path.join(CHECKPOINT_DIR, f"sitemap_monitor_{timestamp}.json")
    latest_path = os.path.join(CHECKPOINT_DIR, "latest.json")
    
    with open(checkpoint_path, "w") as f:
        json.dump(result, f, indent=2)
    with open(latest_path, "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"\nDone. {total_new} new articles. Checkpoint: {checkpoint_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
