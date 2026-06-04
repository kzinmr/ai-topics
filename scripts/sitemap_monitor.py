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
import concurrent.futures
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
        "file_prefix": "anthropic-engineering",
        "title_suffixes": [" \\ Anthropic", " | Anthropic"],
        "state_file": os.path.expanduser("~/.hermes/processed_anthropic_engineering.json"),
    },
    # --- Tier 1: Paraform Talent Density Index companies (no RSS) ---
    {
        "name": "Cohere Blog",
        "url": "https://cohere.com/blog",
        "sitemap_url": "https://cohere.com/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "cohere",
        "title_suffixes": [" | Cohere"],
        "state_file": os.path.expanduser("~/.hermes/processed_cohere_blog.json"),
    },
    {
        "name": "ElevenLabs Blog",
        "url": "https://elevenlabs.io/blog",
        "sitemap_url": "https://elevenlabs.io/sitemap/articles__en.xml",
        "url_pattern": "/blog/",
        "file_prefix": "elevenlabs",
        "title_suffixes": [" | ElevenLabs"],
        "state_file": os.path.expanduser("~/.hermes/processed_elevenlabs_blog.json"),
    },
    {
        "name": "Harvey Blog",
        "url": "https://www.harvey.ai/blog",
        "sitemap_url": "https://www.harvey.ai/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "harvey",
        "title_suffixes": [" | Harvey", " - Harvey"],
        "state_file": os.path.expanduser("~/.hermes/processed_harvey_blog.json"),
    },
    {
        "name": "Glean Blog",
        "url": "https://www.glean.com/blog",
        "sitemap_url": "https://www.glean.com/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "glean",
        "title_suffixes": [" | Glean"],
        "state_file": os.path.expanduser("~/.hermes/processed_glean_blog.json"),
    },
    {
        "name": "Factory Blog",
        "url": "https://factory.ai/news",
        "sitemap_url": "https://factory.ai/sitemap.xml",
        "url_pattern": "/news/",
        "file_prefix": "factory",
        "title_suffixes": [" | Factory"],
        "state_file": os.path.expanduser("~/.hermes/processed_factory_blog.json"),
    },
    {
        "name": "Cartesia Blog",
        "url": "https://cartesia.ai/blog",
        "sitemap_url": "https://cartesia.ai/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "cartesia",
        "title_suffixes": [" | Cartesia"],
        "state_file": os.path.expanduser("~/.hermes/processed_cartesia_blog.json"),
    },
    {
        "name": "Decagon Blog",
        "url": "https://decagon.ai/blog",
        "sitemap_url": "https://decagon.ai/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "decagon",
        "title_suffixes": [" | Decagon"],
        "state_file": os.path.expanduser("~/.hermes/processed_decagon_blog.json"),
    },
    # --- Existing Top-10 companies (no RSS) ---
    {
        "name": "Cursor Blog",
        "url": "https://cursor.com/blog",
        "sitemap_url": "https://cursor.com/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "cursor",
        "title_suffixes": [" | Cursor", " - Cursor"],
        "state_file": os.path.expanduser("~/.hermes/processed_cursor_blog.json"),
    },
    {
        "name": "Fireworks AI Blog",
        "url": "https://fireworks.ai/blog",
        "sitemap_url": "https://fireworks.ai/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "fireworks-ai",
        "title_suffixes": [" | Fireworks AI", " | Fireworks"],
        "state_file": os.path.expanduser("~/.hermes/processed_fireworks_ai_blog.json"),
    },
    {
        "name": "Mistral AI Blog",
        "url": "https://mistral.ai/news/",
        "sitemap_url": "https://mistral.ai/sitemap.xml",
        "url_pattern": "/news/",
        "file_prefix": "mistral-ai",
        "title_suffixes": [" | Mistral AI", " | Mistral"],
        "state_file": os.path.expanduser("~/.hermes/processed_mistral_ai_blog.json"),
    },
    {
        "name": "Pinecone Blog",
        "url": "https://www.pinecone.io/blog/",
        "sitemap_url": "https://www.pinecone.io/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "pinecone",
        "title_suffixes": [" | Pinecone"],
        "state_file": os.path.expanduser("~/.hermes/processed_pinecone_blog.json"),
    },
    {
        "name": "The Browser Company Blog",
        "url": "https://arc.net/blog",
        "sitemap_url": "https://arc.net/sitemap.xml",
        "url_pattern": "/blog",
        "file_prefix": "the-browser-company",
        "title_suffixes": [" | Arc", " | Arc Browser"],
        "state_file": os.path.expanduser("~/.hermes/processed_the_browser_company_blog.json"),
    },
    {
        "name": "Warp Blog",
        "url": "https://www.warp.dev/blog",
        "sitemap_url": "https://www.warp.dev/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "warp",
        "title_suffixes": [" | Warp"],
        "state_file": os.path.expanduser("~/.hermes/processed_warp_blog.json"),
    },
    # --- Tier 1 additions: Hebbia, Parallel Web Systems, Hex Technologies ---
    {
        "name": "Hebbia Blog",
        "url": "https://www.hebbia.ai/blog",
        "sitemap_url": "https://www.hebbia.ai/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "hebbia",
        "title_suffixes": [" | Hebbia"],
        "state_file": os.path.expanduser("~/.hermes/processed_hebbia_blog.json"),
    },
    {
        "name": "Hex Technologies Blog",
        "url": "https://hex.tech/blog",
        "sitemap_url": "https://hex.tech/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "hex-technologies",
        "title_suffixes": [" | Hex"],
        "state_file": os.path.expanduser("~/.hermes/processed_hex_technologies_blog.json"),
    },
    {
        "name": "Parallel Web Systems Blog",
        "url": "https://parallel.ai/blog",
        "sitemap_url": "https://parallel.ai/sitemap.xml",
        "url_pattern": "/blog/",
        "file_prefix": "parallel-web-systems",
        "title_suffixes": [" | Parallel"],
        "state_file": os.path.expanduser("~/.hermes/processed_parallel_web_systems_blog.json"),
    },
]

WIKI_RAW_DIR = os.path.expanduser("~/wiki/raw/articles")
CHECKPOINT_DIR = os.path.expanduser("~/.hermes/cron/data/sitemap_monitor")
REQUEST_TIMEOUT = 15
MAX_ARTICLES_PER_SOURCE = 10  # Limit on first run; state files track seen URLs thereafter


def fetch_sitemap(url: str) -> str:
    """Fetch sitemap XML content, following sitemap index files if needed."""
    with httpx.Client(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
        resp = client.get(url)
        resp.raise_for_status()
        xml_text = resp.text
    
    # Check if this is a sitemap index (points to sub-sitemaps)
    if "<sitemapindex" in xml_text[:500]:
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        root = ET.fromstring(xml_text)
        sub_sitemaps = []
        for sm_elem in root.findall("sm:sitemap", ns):
            loc = sm_elem.find("sm:loc", ns)
            if loc is not None and loc.text:
                sub_sitemaps.append(loc.text.strip())
        
        # Fetch all sub-sitemaps and combine
        combined_urls = []
        for sub_url in sub_sitemaps:
            try:
                with httpx.Client(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
                    sub_resp = client.get(sub_url)
                    sub_resp.raise_for_status()
                sub_root = ET.fromstring(sub_resp.text)
                # Extract <url> elements and add to combined XML
                for url_elem in sub_root.findall("sm:url", ns):
                    combined_urls.append(url_elem)
            except Exception as e:
                print(f"  [!] Failed to fetch sub-sitemap {sub_url}: {e}", file=sys.stderr)
        
        # Reconstruct as a single sitemap XML
        combined = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url_elem in combined_urls:
            combined += ET.tostring(url_elem, encoding="unicode") + "\n"
        combined += "</urlset>"
        return combined
    
    return xml_text


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


def scrape_article(url: str, title_suffixes: list[str] | None = None) -> dict | None:
    """Scrape an article URL and return {url, title, content_md}."""
    try:
        with httpx.Client(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
            resp = client.get(url)
            resp.raise_for_status()
            
        # Basic extraction: look for <title> and <article> content
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, "html.parser")
        
        title = soup.title.string if soup.title else url.rstrip("/").split("/")[-1]
        # Strip configured suffixes from title
        if title_suffixes:
            for suffix in title_suffixes:
                if title.endswith(suffix):
                    title = title[:-len(suffix)].strip()
        
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


def save_raw_article(article: dict, source_name: str, file_prefix: str) -> str:
    """Save article as raw markdown file. Returns the file path."""
    os.makedirs(WIKI_RAW_DIR, exist_ok=True)
    
    slug = article["url"].rstrip("/").split("/")[-1]
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}_{file_prefix}_{slug}.md"
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


def process_source(source: dict) -> dict:
    """Process a single sitemap source. Returns result entry dict."""
    print(f"\n[{source['name']}] Fetching sitemap: {source['sitemap_url']}")
    
    try:
        xml_content = fetch_sitemap(source["sitemap_url"])
    except Exception as e:
        print(f"  [!] [{source['name']}] Failed to fetch sitemap: {e}", file=sys.stderr)
        return {
            "name": source["name"],
            "error": str(e),
            "new_articles": [],
            "saved_articles": [],
        }
    
    articles = parse_sitemap(xml_content, source["url_pattern"])
    print(f"  [{source['name']}] Found {len(articles)} matching articles in sitemap")
    
    seen_urls = load_state(source["state_file"])
    new_articles = [a for a in articles if a["url"] not in seen_urls]
    
    print(f"  [{source['name']}] New: {len(new_articles)}, Previously seen: {len(seen_urls) - len(new_articles)}")
    
    saved = []
    to_scrape = new_articles[:MAX_ARTICLES_PER_SOURCE] if len(new_articles) > MAX_ARTICLES_PER_SOURCE else new_articles
    skipped = len(new_articles) - len(to_scrape)
    if skipped > 0:
        print(f"  [{source['name']}] Limiting to {MAX_ARTICLES_PER_SOURCE} scrapes (skipping {skipped}) — remainder tracked in state for future runs")
    for article in to_scrape:
        print(f"  [{source['name']}] Scraping: {article['url']}")
        scraped = scrape_article(article["url"], source.get("title_suffixes"))
        if scraped:
            scraped["lastmod"] = article.get("lastmod")
            filepath = save_raw_article(scraped, source["name"], source["file_prefix"])
            saved.append({"url": article["url"], "title": scraped.get("title"), "filepath": filepath})
    
    # Update state
    all_urls = seen_urls | {a["url"] for a in articles}
    save_state(source["state_file"], all_urls)
    
    return {
        "name": source["name"],
        "url": source["url"],
        "total_in_sitemap": len(articles),
        "new_articles": [{"url": a["url"], "lastmod": a.get("lastmod")} for a in new_articles],
        "saved_articles": saved,
    }


def main():
    start_time = datetime.now(timezone.utc)
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    
    # Process sources in parallel (8 workers to stay within 120s cron limit)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_source = {executor.submit(process_source, s): s for s in SOURCES}
        source_results = []
        for future in concurrent.futures.as_completed(future_to_source):
            source = future_to_source[future]
            try:
                entry = future.result()
            except Exception as e:
                print(f"  [!] [{source['name']}] Unhandled error: {e}", file=sys.stderr)
                entry = {
                    "name": source["name"],
                    "error": str(e),
                    "new_articles": [],
                    "saved_articles": [],
                }
            source_results.append(entry)
    
    total_new = sum(len(r.get("new_articles", [])) for r in source_results)
    
    result = {
        "source": "sitemap",
        "timestamp": start_time.isoformat(),
        "sources": source_results,
    }
    
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
