#!/usr/bin/env python3
"""
Scrape 4 articles and save as raw article files in wiki/raw/articles/
"""
import requests
import re
import json
import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse

OUTPUT_DIR = "/opt/data/ai-topics/wiki/raw/articles"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

ARTICLES = [
    {
        "url": "https://darioamodei.com/post/policy-on-the-ai-exponential",
        "title_hint": "Dario Amodei — Policy on the AI Exponential",
        "source_slug": "darioamodei",
        "content_slug": "policy-on-the-ai-exponential",
        "x_referrers": ["mitsuhiko", "badlogicgames"],
        "author_hint": "Dario Amodei",
    },
    {
        "url": "https://lucumr.pocoo.org/2026/6/10/gaslighting/",
        "title_hint": "Gaslighting Openness",
        "source_slug": "pocoo",
        "content_slug": "gaslighting-openness",
        "x_referrers": ["mitsuhiko"],
        "author_hint": "Armin Ronacher",
    },
    {
        "url": "https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/",
        "title_hint": "Lines of Code Got a Better Publicist",
        "source_slug": "curlewis",
        "content_slug": "lines-of-code-got-a-better-publicist",
        "x_referrers": ["badlogicgames"],
        "author_hint": None,
    },
    {
        "url": "https://hynek.me/articles/ditch-codecov-python/",
        "title_hint": "How to Ditch Codecov for Python Projects",
        "source_slug": "hynek",
        "content_slug": "how-to-ditch-codecov-for-python-projects",
        "x_referrers": ["hynek"],
        "author_hint": "Hynek Schlawack",
    },
]


def extract_date_from_meta(soup, url):
    """Extract publication date from meta tags, JSON-LD, or URL."""
    # 1. Check meta tags
    for meta in soup.find_all("meta"):
        prop = meta.get("property", "")
        name = meta.get("name", "")
        content = meta.get("content", "")
        if prop in ("article:published_time", "og:article:published_time") and content:
            return content
        if name in ("date", "pubdate", "DC.date.issued", "citation_date") and content:
            return content

    # 2. Check JSON-LD
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                for key in ("datePublished", "dateCreated", "dateModified"):
                    if key in data and data[key]:
                        return data[key]
                # Check nested in graph
                if "@graph" in data:
                    for item in data["@graph"]:
                        for key in ("datePublished", "dateCreated", "dateModified"):
                            if key in item and item[key]:
                                return item[key]
        except (json.JSONDecodeError, TypeError):
            pass

    # 3. Check time element
    time_el = soup.find("time")
    if time_el and time_el.get("datetime"):
        return time_el["datetime"]

    # 4. Extract from URL pattern (YYYY/MM/DD or YYYY/M/D)
    url_match = re.search(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
    if url_match:
        y, m, d = url_match.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"

    return None


def extract_title(soup, url):
    """Extract title from page."""
    # og:title
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        return og_title["content"].strip()

    # title tag
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        t = title_tag.string.strip()
        # Remove site name suffix
        t = re.sub(r'\s*[|–—\-–]\s*.*$', '', t).strip()
        return t

    # h1
    h1 = soup.find("h1")
    if h1:
        return h1.get_text().strip()

    return urlparse(url).path.split("/")[-1].replace("-", " ").title()


def parse_date(raw_date):
    """Parse a date string into YYYY-MM-DD format."""
    if not raw_date:
        return None
    raw_date = str(raw_date).strip()

    formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d %b %Y",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(raw_date, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue

    # Try ISO 8601 with timezone offset
    iso_match = re.match(r'(\d{4}-\d{2}-\d{2})', raw_date)
    if iso_match:
        return iso_match.group(1)

    print(f"  WARNING: Could not parse date: {raw_date}")
    return None


def extract_author(soup, url):
    """Extract author from meta tags, JSON-LD, or page content."""
    # Meta author
    for name in ("author", "article:author"):
        meta = soup.find("meta", attrs={"name": name})
        if meta and meta.get("content"):
            return meta["content"].strip()

    # JSON-LD author
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                author = data.get("author")
                if isinstance(author, dict):
                    return author.get("name", None)
                elif isinstance(author, list) and author:
                    first = author[0]
                    if isinstance(first, dict):
                        return first.get("name", None)
                    elif isinstance(first, str):
                        return first
                elif isinstance(author, str):
                    return author
        except (json.JSONDecodeError, TypeError):
            pass

    # rel=author link
    author_link = soup.find("a", rel="author")
    if author_link:
        return author_link.get_text().strip()

    return None


def extract_text(soup, url):
    """Extract main article text content."""
    domain = urlparse(url).netloc

    # Try to find article/main content
    content = None

    # Common article selectors
    selectors = [
        "article",
        '[role="main"]',
        "main",
        ".post-content",
        ".article-content",
        ".entry-content",
        ".content",
        ".post",
        ".article-body",
        "#content",
        ".page-content",
    ]

    for sel in selectors:
        el = soup.select_one(sel)
        if el:
            # Check if it has substantial text
            text = el.get_text(separator="\n", strip=True)
            if len(text) > 500:
                content = el
                break

    if not content:
        # Fall back to body, removing nav, header, footer, sidebar
        body = soup.find("body")
        if body:
            for tag_name in ("nav", "header", "footer", "aside", "script", "style", "noscript"):
                for el in body.find_all(tag_name):
                    el.decompose()
            content = body

    if not content:
        return soup.get_text(separator="\n", strip=True)

    # Extract text preserving some structure
    lines = []
    for el in content.descendants:
        if isinstance(el, str):
            text = el.strip()
            if text:
                lines.append(text)
        elif el.name in ("p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre", "td", "th"):
            text = el.get_text(strip=True)
            if text:
                lines.append(text)

    # Remove duplicate consecutive lines
    cleaned = []
    prev = None
    for line in lines:
        if line != prev:
            cleaned.append(line)
        prev = line

    return "\n\n".join(cleaned)


def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = []

    for i, article in enumerate(ARTICLES):
        url = article["url"]
        print(f"\n{'='*60}")
        print(f"[{i+1}/4] Fetching: {url}")
        print(f"{'='*60}")

        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            print(f"  Status: {resp.status_code}, Size: {len(resp.text)} bytes")
        except Exception as e:
            print(f"  ERROR fetching: {e}")
            results.append({"url": url, "status": "FAILED", "error": str(e)})
            continue

        soup = BeautifulSoup(resp.text, "html.parser")

        # Extract date
        raw_date = extract_date_from_meta(soup, url)
        parsed_date = parse_date(raw_date) if raw_date else None

        if not parsed_date:
            # If URL has date, try that
            url_match = re.search(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
            if url_match:
                y, m, d = url_match.groups()
                parsed_date = f"{y}-{int(m):02d}-{int(d):02d}"
                print(f"  Date from URL: {parsed_date}")
            else:
                print(f"  WARNING: Could not determine date for {url}")
                parsed_date = "UNKNOWN"

        print(f"  Raw date: {raw_date} -> Parsed: {parsed_date}")

        # Extract title
        title = extract_title(soup, url)
        print(f"  Title: {title}")

        # Extract author
        author = extract_author(soup, url)
        if not author and article["author_hint"]:
            author = article["author_hint"]
        print(f"  Author: {author}")

        # Extract text
        text = extract_text(soup, url)
        print(f"  Text length: {len(text)} chars")

        # Build filename
        source_slug = article["source_slug"]
        content_slug = article["content_slug"]

        # Determine date for filename
        date_for_filename = parsed_date if parsed_date and parsed_date != "UNKNOWN" else "0000-00-00"
        filename = f"{date_for_filename}_{source_slug}_{content_slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Get domain for source field
        domain = urlparse(url).netloc

        # Build frontmatter
        x_refs = article["x_referrers"]
        x_ref_str = ", ".join(f"@{r}" for r in x_refs)

        frontmatter = f"""---
type: article
title: "{title}"
source: {domain}
date: {parsed_date}
url: {url}"""
        if author:
            frontmatter += f"\nauthor: {author}"
        frontmatter += f"""
x_referrer: {x_ref_str}
---

"""
        # Write the raw file (frontmatter + full text)
        full_content = frontmatter + text
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)

        print(f"  Saved: {filename}")
        print(f"  File size: {len(full_content)} bytes")
        results.append({"url": url, "status": "OK", "file": filename, "date": parsed_date})

    print(f"\n{'='*60}")
    print("SUMMARY:")
    for r in results:
        status = r["status"]
        if status == "OK":
            print(f"  ✅ {r['file']} (date: {r['date']})")
        else:
            print(f"  ❌ {r['url']}: {r.get('error', 'unknown')}")


if __name__ == "__main__":
    main()
