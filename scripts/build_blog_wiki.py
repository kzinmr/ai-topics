#!/usr/bin/env python3
"""Build wiki entity pages for blog authors from OPML.

For each blog:
1. Fetch the site's about/top page to identify the author
2. Fetch the RSS feed to get recent post titles (reveals topics/interests)
3. Generate a wiki entity page with author info and interests

Usage:
  python3 build_blog_wiki.py                    # Process all
  python3 build_blog_wiki.py --dry-run           # Preview without writing
  python3 build_blog_wiki.py --limit 5           # Process first N only
"""
import xml.etree.ElementTree as ET
import re
import sys
import json
import argparse
import logging
import time
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
from bs4 import BeautifulSoup
from readability import Document

# Paths
OPML_PATH = Path.home() / "ai-topics" / "config" / "feeds" / "blogs.opml"
WIKI_ENTITIES = Path.home() / "wiki" / "entities"
WIKI_INDEX = Path.home() / "wiki" / "index.md"
WIKI_LOG = Path.home() / "wiki" / "log.md"
OUTPUT_JSON = Path(__file__).resolve().parent / "cache" / "blog_authors.json"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HermesBot/1.0)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def parse_opml(path: Path) -> list[dict]:
    """Parse OPML and return list of {name, rss_url, html_url}."""
    tree = ET.parse(path)
    blogs = []
    for outline in tree.iter("outline"):
        if outline.get("type") == "rss":
            blogs.append({
                "name": outline.get("text", ""),
                "rss_url": outline.get("xmlUrl", ""),
                "html_url": outline.get("htmlUrl", ""),
            })
    return blogs


def fetch_page(url: str, timeout: int = 20) -> str | None:
    """Fetch a URL, return text or None."""
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True, headers=HTTP_HEADERS) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.text
    except Exception as e:
        log.warning(f"  Fetch failed {url}: {e}")
        return None


def extract_author_from_bio(bio: str) -> str | None:
    """Try to extract author name from bio text using common patterns."""
    if not bio:
        return None

    # Clean up excessive whitespace/newlines for matching
    bio_clean = re.sub(r'\s+', ' ', bio).strip()

    def clean_name(name: str) -> str:
        """Remove trailing punctuation, article words, and extra text."""
        name = name.strip().rstrip('.,!')
        # Remove trailing "I'm", "I am", etc. that leaked into the match
        name = re.sub(r"\s+I['\s]", '', name)
        return name

    # "My name is [Name]" — highest confidence
    m = re.search(r"[Mm]y name is\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z.\-']*){0,3})", bio_clean)
    if m:
        return clean_name(m.group(1))

    # "written and produced by [Name]" — before generic "[Name] is"
    m = re.search(r"written\s+(?:and\s+\w+\s+)?by\s+([A-Z][a-zA-Z\s\-']+?)(?:\s+\.)", bio_clean)
    if m:
        return clean_name(m.group(1))

    # "I'm [Name]" / "I am [Name]"
    m = re.search(r"(?:I'm|I am)\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z.\-']*){0,3})", bio_clean)
    if m:
        name = clean_name(m.group(1))
        # Filter out common false positives
        if name.lower() not in ('i', 'a', 'the', 'this', 'that', 'deep', 'very', 'really', 'also', 'just', 'currently', 'still', 'always', 'often', 'sometimes', 'usually', 'deeply', 'part', 'both', 'here', 'trying', 'making'):
            return name

    # "[Name] worked/was/founded/created/runs/lives" — opening sentence
    # Exclude "is written" to avoid matching site names
    m = re.search(r"^([A-Z][a-zA-Z\s\-']{2,30})\s+(?:worked|was|founded|created|runs|lives)", bio_clean)
    if m:
        return clean_name(m.group(1))

    # "by [Name],"
    m = re.search(r"\bby\s+([A-Z][a-zA-Z\s\-']{2,20})\b[,.\s]", bio_clean)
    if m:
        return clean_name(m.group(1))

    return None


def extract_about_info(html_url: str) -> dict:
    """Try to find about page and extract author info."""
    info = {"author": "", "bio": "", "about_url": ""}

    # Try common about page paths
    parsed = urlparse(html_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    about_paths = ["/about", "/about/", "/about-me", "/about.html", "/info", ""]

    for path in about_paths:
        url = base + path if path else html_url
        html = fetch_page(url)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")

        # Try to find author name from meta tags
        for meta in soup.find_all("meta"):
            name_attr = meta.get("name", "").lower()
            prop_attr = meta.get("property", "").lower()
            content = meta.get("content", "").strip()
            if content and name_attr in ("author", "twitter:creator"):
                info["author"] = content
            if content and prop_attr in ("og:site_name", "article:author"):
                if not info["author"]:
                    info["author"] = content

        # Extract readable text from about page
        if path:  # actual about page, not homepage
            try:
                doc = Document(html)
                about_soup = BeautifulSoup(doc.summary(), "html.parser")
                text = about_soup.get_text(separator="\n", strip=True)
                if len(text) > 50:
                    info["bio"] = text[:2000]
                    info["about_url"] = url
                    # If meta tags didn't give us an author, try bio extraction
                    if not info["author"]:
                        extracted = extract_author_from_bio(text)
                        if extracted:
                            info["author"] = extracted
                    break
            except Exception:
                pass

    # Final fallback: try bio extraction even from homepage if no about page found
    if not info["author"] and info["bio"]:
        extracted = extract_author_from_bio(info["bio"])
        if extracted:
            info["author"] = extracted

    return info


def extract_feed_topics(rss_url: str) -> list[str]:
    """Fetch RSS/Atom feed and return recent post titles."""
    xml_text = fetch_page(rss_url)
    if not xml_text:
        return []

    titles = []
    try:
        # Strip namespaces for simpler parsing
        xml_clean = re.sub(r'\sxmlns[^"]*"[^"]*"', "", xml_text)
        root = ET.fromstring(xml_clean)

        # RSS format
        for item in root.iter("item"):
            t = item.findtext("title", "").strip()
            if t:
                titles.append(t)

        # Atom format
        if not titles:
            for entry in root.iter("entry"):
                t_el = entry.find("title")
                if t_el is not None and t_el.text:
                    titles.append(t_el.text.strip())
    except ET.ParseError as e:
        log.warning(f"  Feed parse error {rss_url}: {e}")

    return titles[:20]  # Last 20 posts


def slugify(text: str) -> str:
    """Convert text to a filename slug."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def generate_entity_page(blog: dict, about: dict, topics: list[str]) -> str:
    """Generate a wiki entity markdown page."""
    author = about.get("author", "") or blog["name"]
    bio = about.get("bio", "")
    today = datetime.now().strftime("%Y-%m-%d")

    # Infer interest areas from post titles
    topic_list = "\n".join(f"- {t}" for t in topics[:15]) if topics else "- (no recent posts found)"

    page = f"""---
title: "{author}"
created: {today}
updated: {today}
tags: [person, blogger, hn-popular]
aliases: ["{blog['name']}"]
---

# {author}

| | |
|---|---|
| **Blog** | [{blog['name']}]({blog['html_url']}) |
| **RSS** | {blog['rss_url']} |
"""
    if about.get("about_url"):
        page += f"| **About** | [{about['about_url']}]({about['about_url']}) |\n"

    if bio:
        page += f"\n## Bio\n\n{bio[:1500]}\n"

    page += f"\n## Recent Posts (topics/interests)\n\n{topic_list}\n"

    return page


def process_blog(blog: dict) -> dict:
    """Process a single blog: fetch about + feed, return result."""
    name = blog["name"]
    log.info(f"Processing: {name}")

    about = extract_about_info(blog["html_url"])
    topics = extract_feed_topics(blog["rss_url"])

    # Small delay to be polite
    time.sleep(0.5)

    return {
        "blog": blog,
        "about": about,
        "topics": topics,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    blogs = parse_opml(OPML_PATH)
    log.info(f"Found {len(blogs)} blogs in OPML")

    if args.limit:
        blogs = blogs[:args.limit]

    WIKI_ENTITIES.mkdir(parents=True, exist_ok=True)
    results = []
    written = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(process_blog, b): b for b in blogs}
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)

                blog = result["blog"]
                about = result["about"]
                topics = result["topics"]
                author = about.get("author", "") or blog["name"]
                slug = slugify(author)
                filepath = WIKI_ENTITIES / f"{slug}.md"

                page = generate_entity_page(blog, about, topics)

                if args.dry_run:
                    log.info(f"  [DRY RUN] Would write: {filepath.name} ({author})")
                else:
                    filepath.write_text(page, encoding="utf-8")
                    log.info(f"  Wrote: {filepath.name}")
                    written.append({"author": author, "slug": slug, "file": filepath.name})

            except Exception as e:
                log.error(f"  Error: {e}", exc_info=True)

    # Save raw results for later use
    OUTPUT_JSON.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    log.info(f"Saved raw data to {OUTPUT_JSON}")

    if not args.dry_run and written:
        # Update wiki index
        entity_lines = "\n".join(
            f"- [[entities/{w['slug']}|{w['author']}]]" for w in sorted(written, key=lambda x: x["author"].lower())
        )
        index = WIKI_INDEX.read_text(encoding="utf-8")
        index = index.replace(
            "<!-- Entity pages: people, organizations, products, models -->",
            f"<!-- Entity pages: people, organizations, products, models -->\n\n### HN Popular Bloggers\n{entity_lines}"
        )
        WIKI_INDEX.write_text(index, encoding="utf-8")

        # Append to log
        today = datetime.now().strftime("%Y-%m-%d")
        log_entry = f"\n## {today}\n- Ingested {len(written)} blog author entities from hn-popular-blogs-2025.opml\n"
        with open(WIKI_LOG, "a", encoding="utf-8") as f:
            f.write(log_entry)

        log.info(f"Done: {len(written)} entity pages written, index updated")


if __name__ == "__main__":
    main()
