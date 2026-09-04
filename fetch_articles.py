#!/usr/bin/env python3
"""Fetch web articles and save them as markdown with frontmatter for wiki ingestion."""

import urllib.request
import ssl
import re
import json
from html.parser import HTMLParser
from datetime import datetime, timezone

OUTPUT_DIR = "/opt/data/ai-topics/wiki/raw/articles"

ARTICLES = [
    {
        "url": "https://huggingface.co/blog/Samoed/mteb-v3-leaderboard",
        "path": f"{OUTPUT_DIR}/2026-06-12_samoed_mteb-v3-leaderboard.md",
        "title": "MTEB v3 Leaderboard",
        "tags": ["embedding", "leaderboard", "mteb"],
    },
    {
        "url": "https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos",
        "path": f"{OUTPUT_DIR}/2026-06-15_emollick_what-it-feels-like-to-work-with-mythos.md",
        "title": "What it feels like to work with Mythos",
        "tags": ["claude", "ai-safety"],
    },
    {
        "url": "https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/",
        "path": f"{OUTPUT_DIR}/2026-06-13_simon-willison_publishing-wasm-wheels.md",
        "title": "Publishing WASM Wheels for Python",
        "tags": ["webassembly", "python", "pyodide"],
    },
]


class TextExtractor(HTMLParser):
    """Extract text content from HTML, skipping scripts and styles."""

    def __init__(self):
        super().__init__()
        self._skip = False
        self._text_parts = []
        self._in_script = False
        self._in_style = False
        self._in_nav = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in ("script", "style"):
            self._in_script = tag == "script"
            self._in_style = tag == "style"
            self._skip = True
        if tag == "nav":
            self._in_nav = True
            self._skip = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in ("script", "style"):
            self._in_script = False
            self._in_style = False
            self._skip = False
        if tag == "nav":
            self._in_nav = False
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            text = data.strip()
            if text:
                self._text_parts.append(text)

    def get_text(self):
        return "\n".join(self._text_parts)


def fetch_url(url):
    """Fetch content from a URL."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; HermesAgent/1.0)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_article_from_huggingface(html):
    """Extract article content from Hugging Face blog pages."""
    # Try to find the main content area
    # Look for prose-content or article body
    content = html

    # Extract JSON-LD if available for metadata
    jsonld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    metadata = {}
    if jsonld_match:
        try:
            data = json.loads(jsonld_match.group(1))
            if isinstance(data, dict):
                metadata["title"] = data.get("headline", "")
                metadata["date"] = data.get("datePublished", "")
                metadata["author"] = data.get("author", {}).get("name", "") if isinstance(data.get("author"), dict) else ""
                metadata["description"] = data.get("description", "")
        except json.JSONDecodeError:
            pass

    # Try to extract the main article content
    # HF blogs often have content in a div with specific classes
    body_match = re.search(r'<div[^>]*class="[^"]*prose[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)

    # Extract and clean markdown-like content
    # HF blog content is often stored in a script tag or data attribute
    content_match = re.search(r'"content"\s*:\s*"((?:[^"\\]|\\.)*)"', content)
    if content_match:
        raw_content = content_match.group(1)
        # Unescape JSON string
        raw_content = raw_content.replace("\\n", "\n").replace("\\t", "\t").replace('\\"', '"').replace("\\\\", "\\")
        return raw_content, metadata

    # Fallback: extract from article tag
    article_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
    if article_match:
        article_html = article_match.group(1)
        extractor = TextExtractor()
        extractor.feed(article_html)
        return extractor.get_text(), metadata

    # Final fallback: full page text
    extractor = TextExtractor()
    extractor.feed(content)
    return extractor.get_text(), metadata


def extract_article_from_substack(html):
    """Extract article content from Substack/oneusefulthing pages."""
    # Try JSON-LD first
    jsonld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    metadata = {}
    if jsonld_match:
        try:
            data = json.loads(jsonld_match.group(1))
            if isinstance(data, dict):
                metadata["title"] = data.get("headline", data.get("name", ""))
                metadata["date"] = data.get("datePublished", "")
                metadata["author"] = data.get("author", {}).get("name", "") if isinstance(data.get("author"), dict) else data.get("author", "")
                metadata["description"] = data.get("description", "")
        except json.JSONDecodeError:
            pass

    # Try og:title and og:description
    for pattern, key in [
        (r'<meta[^>]*property="og:title"[^>]*content="([^"]*)"', "title"),
        (r'<meta[^>]*content="([^"]*)"[^>]*property="og:title"', "title"),
        (r'<meta[^>]*property="og:description"[^>]*content="([^"]*)"', "description"),
        (r'<meta[^>]*content="([^"]*)"[^>]*property="og:description"', "description"),
    ]:
        m = re.search(pattern, html)
        if m and not metadata.get(key):
            metadata[key] = m.group(1)

    # Try to find the article body
    # Substack uses <div class="available-content"> or similar
    content_match = re.search(r'<div[^>]*class="[^"]*available-content[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
    if content_match:
        extractor = TextExtractor()
        extractor.feed(content_match.group(1))
        return extractor.get_text(), metadata

    # Try article tag
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_match:
        extractor = TextExtractor()
        extractor.feed(article_match.group(1))
        return extractor.get_text(), metadata

    # Try main content area
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if main_match:
        extractor = TextExtractor()
        extractor.feed(main_match.group(1))
        return extractor.get_text(), metadata

    # Fallback
    extractor = TextExtractor()
    extractor.feed(html)
    return extractor.get_text(), metadata


def extract_article_from_simonwillison(html):
    """Extract article content from simonwillison.net."""
    # Simon Willison's blog has clean HTML structure
    jsonld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    metadata = {}
    if jsonld_match:
        try:
            data = json.loads(jsonld_match.group(1))
            if isinstance(data, dict):
                metadata["title"] = data.get("headline", data.get("name", ""))
                metadata["date"] = data.get("datePublished", "")
                author = data.get("author", {})
                if isinstance(author, dict):
                    metadata["author"] = author.get("name", "")
                elif isinstance(author, str):
                    metadata["author"] = author
                metadata["description"] = data.get("description", "")
        except json.JSONDecodeError:
            pass

    # Try og tags
    for pattern, key in [
        (r'<meta[^>]*property="og:title"[^>]*content="([^"]*)"', "title"),
        (r'<meta[^>]*content="([^"]*)"[^>]*property="og:title"', "title"),
        (r'<meta[^>]*property="og:description"[^>]*content="([^"]*)"', "description"),
        (r'<meta[^>]*content="([^"]*)"[^>]*property="og:description"', "description"),
    ]:
        m = re.search(pattern, html)
        if m and not metadata.get(key):
            metadata[key] = m.group(1)

    # Simon Willison uses <div class="entry-content"> or <article>
    entry_match = re.search(r'<div[^>]*class="[^"]*entry-body[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
    if not entry_match:
        entry_match = re.search(r'<div[^>]*class="[^"]*entry-content[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
    if entry_match:
        extractor = TextExtractor()
        extractor.feed(entry_match.group(1))
        return extractor.get_text(), metadata

    # Try article tag
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_match:
        extractor = TextExtractor()
        extractor.feed(article_match.group(1))
        return extractor.get_text(), metadata

    # Fallback
    extractor = TextExtractor()
    extractor.feed(html)
    return extractor.get_text(), metadata


def create_frontmatter(title, created, updated, article_type, tags, sources):
    """Create YAML frontmatter."""
    tags_str = ", ".join(tags)
    sources_str = ", ".join(sources)
    return f"""---
title: "{title}"
created: "{created}"
updated: "{updated}"
type: {article_type}
tags: [{tags_str}]
sources: [{sources_str}]
---
"""


def html_to_markdown_friendly(text):
    """Basic cleanup of extracted text for markdown output."""
    # Normalize whitespace
    lines = text.split("\n")
    cleaned = []
    prev_blank = False
    for line in lines:
        line = line.strip()
        if not line:
            if not prev_blank:
                cleaned.append("")
                prev_blank = True
            continue
        prev_blank = False
        cleaned.append(line)
    return "\n".join(cleaned)


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for article in ARTICLES:
        url = article["url"]
        path = article["path"]
        print(f"\n{'='*60}")
        print(f"Fetching: {url}")
        print(f"Saving to: {path}")

        try:
            html = fetch_url(url)
            print(f"  Downloaded {len(html)} bytes")

            # Extract content based on site
            if "huggingface.co" in url:
                body, metadata = extract_article_from_huggingface(html)
            elif "oneusefulthing.org" in url:
                body, metadata = extract_article_from_substack(html)
            elif "simonwillison.net" in url:
                body, metadata = extract_article_from_simonwillison(html)
            else:
                extractor = TextExtractor()
                extractor.feed(html)
                body = extractor.get_text()
                metadata = {}

            # Use metadata if available
            title = metadata.get("title", article["title"])
            if not title:
                title = article["title"]

            body = html_to_markdown_friendly(body)

            # Create frontmatter
            frontmatter = create_frontmatter(
                title=title,
                created=now,
                updated=now,
                article_type="article",
                tags=article["tags"],
                sources=[url],
            )

            # Write file
            full_content = frontmatter + "\n" + body
            with open(path, "w") as f:
                f.write(full_content)

            print(f"  ✓ Written {len(full_content)} chars to {path}")
            print(f"  Title: {title}")
            print(f"  Body preview: {body[:100]}...")

        except Exception as e:
            print(f"  ✗ Error processing {url}: {e}")
            # Write a placeholder so the file exists
            frontmatter = create_frontmatter(
                title=article["title"],
                created=now,
                updated=now,
                article_type="article",
                tags=article["tags"],
                sources=[url],
            )
            with open(path, "w") as f:
                f.write(frontmatter + f"\n[Failed to fetch content: {e}]\n")
            print(f"  Wrote placeholder to {path}")


if __name__ == "__main__":
    main()
