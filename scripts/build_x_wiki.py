#!/usr/bin/env python3
"""Build wiki entity skeleton pages for X/Twitter accounts.

For each account in x-accounts.yaml:
1. If blog URL provided: fetch about page + discover/fetch RSS
2. Generate a wiki entity skeleton page with known info
3. The skeleton is designed to be enriched by Hermes Agent

Usage:
  python3 build_x_wiki.py                    # Process all
  python3 build_x_wiki.py --dry-run           # Preview without writing
  python3 build_x_wiki.py --handle @willccbb  # Process single account
  python3 build_x_wiki.py --enrich            # Print Discord prompt for Hermes enrichment
"""
import re
import sys
import json
import argparse
import logging
import time
import yaml
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, urljoin
import xml.etree.ElementTree as ET

import httpx
from bs4 import BeautifulSoup
from readability import Document

# Paths
ACCOUNTS_PATH = Path.home() / "x-accounts.yaml"
WIKI_ENTITIES = Path.home() / "wiki" / "entities"
WIKI_INDEX = Path.home() / "wiki" / "index.md"
WIKI_LOG = Path.home() / "wiki" / "log.md"
OUTPUT_JSON = Path.home() / "wiki" / "raw" / "x_accounts.json"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HermesBot/1.0)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def load_accounts(path: Path, handle_filter: str = None) -> list[dict]:
    """Load accounts from YAML file."""
    with open(path) as f:
        data = yaml.safe_load(f)
    accounts = data.get("accounts", [])
    if handle_filter:
        handle_filter = handle_filter.lstrip("@").lower()
        accounts = [a for a in accounts if a["handle"].lstrip("@").lower() == handle_filter]
    return accounts


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


def discover_rss(blog_url: str, html: str = None) -> str | None:
    """Try to discover RSS feed URL from blog."""
    if not blog_url:
        return None

    if html is None:
        html = fetch_page(blog_url)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    # Look for RSS/Atom link tags
    for link in soup.find_all("link", rel="alternate"):
        link_type = link.get("type", "")
        if "rss" in link_type or "atom" in link_type or "xml" in link_type:
            href = link.get("href", "")
            if href:
                return urljoin(blog_url, href)

    # Common feed paths
    parsed = urlparse(blog_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    common_paths = ["/feed", "/rss", "/atom.xml", "/feed.xml", "/rss.xml", "/index.xml"]
    for path in common_paths:
        url = base + path
        try:
            with httpx.Client(timeout=10, follow_redirects=True, headers=HTTP_HEADERS) as c:
                r = c.head(url)
                ct = r.headers.get("content-type", "")
                if r.status_code == 200 and ("xml" in ct or "rss" in ct or "atom" in ct):
                    return url
        except Exception:
            continue

    return None


def extract_about_info(blog_url: str) -> dict:
    """Fetch blog and about page, extract author info."""
    info = {"bio": "", "about_url": "", "meta_author": ""}
    if not blog_url:
        return info

    parsed = urlparse(blog_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    about_paths = ["/about", "/about/", "/about-me", "/about.html", ""]

    for path in about_paths:
        url = base + path if path else blog_url
        html = fetch_page(url)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")

        # Meta tags
        for meta in soup.find_all("meta"):
            name_attr = meta.get("name", "").lower()
            prop_attr = meta.get("property", "").lower()
            content = meta.get("content", "").strip()
            if content and name_attr in ("author", "twitter:creator"):
                info["meta_author"] = content
            if content and prop_attr in ("og:site_name", "article:author"):
                if not info["meta_author"]:
                    info["meta_author"] = content

        # Extract about page content
        if path:  # actual about page
            try:
                doc = Document(html)
                about_soup = BeautifulSoup(doc.summary(), "html.parser")
                text = about_soup.get_text(separator="\n", strip=True)
                if len(text) > 50:
                    info["bio"] = text[:2000]
                    info["about_url"] = url
                    break
            except Exception:
                pass

    return info


def extract_feed_topics(rss_url: str) -> list[str]:
    """Fetch RSS/Atom feed and return recent post titles."""
    if not rss_url:
        return []
    xml_text = fetch_page(rss_url)
    if not xml_text:
        return []

    titles = []
    try:
        xml_clean = re.sub(r'\sxmlns[^"]*"[^"]*"', "", xml_text)
        root = ET.fromstring(xml_clean)

        for item in root.iter("item"):
            t = item.findtext("title", "").strip()
            if t:
                titles.append(t)

        if not titles:
            for entry in root.iter("entry"):
                t_el = entry.find("title")
                if t_el is not None and t_el.text:
                    titles.append(t_el.text.strip())
    except ET.ParseError as e:
        log.warning(f"  Feed parse error {rss_url}: {e}")

    return titles[:20]


def slugify(text: str) -> str:
    """Convert text to a filename slug."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def generate_skeleton(account: dict, about: dict, rss_url: str, topics: list[str]) -> str:
    """Generate a wiki entity skeleton page."""
    name = account.get("name", "") or account["handle"].lstrip("@")
    handle = account["handle"].lstrip("@")
    blog_url = account.get("blog", "")
    github = account.get("github", "")
    tag_list = ["person", "x-account"] + account.get("topics", [])
    today = datetime.now().strftime("%Y-%m-%d")
    notes = account.get("notes", "")

    aliases = [f"@{handle}"]
    if name != handle:
        aliases.append(handle)

    page = f"""---
title: "{name}"
created: {today}
updated: {today}
tags: [{', '.join(tag_list)}]
aliases: {json.dumps(aliases)}
source: x-account
status: skeleton
---

# {name}

| | |
|---|---|
| **X/Twitter** | [@{handle}](https://x.com/{handle}) |
"""

    if blog_url:
        page += f"| **Blog** | [{blog_url}]({blog_url}) |\n"
    if rss_url:
        page += f"| **RSS** | {rss_url} |\n"
    if about.get("about_url"):
        page += f"| **About** | [{about['about_url']}]({about['about_url']}) |\n"
    if github:
        page += f"| **GitHub** | [{github}](https://github.com/{github}) |\n"

    if notes:
        page += f"\n## Notes\n\n{notes}\n"

    if about.get("bio"):
        page += f"\n## Bio (scraped)\n\n{about['bio'][:1500]}\n"

    if topics:
        topic_list = "\n".join(f"- {t}" for t in topics[:15])
        page += f"\n## Recent Posts\n\n{topic_list}\n"

    page += f"""
## Overview

<!-- TODO: Hermes enrichment needed -->
<!-- Research this person's work, contributions, and key ideas -->
<!-- Aim for the depth of antirez-com.md or simon-willison.md -->

## Core Ideas

<!-- TODO: Hermes enrichment needed -->

## Related

<!-- TODO: Add wikilinks to related entities/concepts -->
"""

    return page


def generate_enrich_prompt(written: list[dict]) -> str:
    """Generate a Discord message to ask Hermes to enrich pages."""
    if not written:
        return ""

    names = "\n".join(f"- `wiki/entities/{w['file']}` ({w['name']}, @{w['handle']})" for w in written)

    return f"""以下の新しいエンティティページのスケルトンを追加しました。
それぞれリサーチして充実させてください。
antirez-com.md や simon-willison.md レベルの深さを目指してください。

{names}

各ページについて：
1. X/Twitterでの活動内容・影響力を調査
2. ブログがあれば最近の記事内容を分析
3. 所属組織・プロジェクト・主要な貢献を特定
4. Core Ideas セクションにその人物の思想・主張をまとめる
5. Related セクションに関連エンティティ/コンセプトへのwikilinkを追加
6. frontmatterの status: skeleton を削除
7. 完了したらコミット＆プッシュ

1ページずつ順番に処理してください。"""


def process_account(account: dict) -> dict:
    """Process a single X account."""
    handle = account["handle"].lstrip("@")
    name = account.get("name", handle)
    blog_url = account.get("blog", "")
    rss_url = account.get("rss", "")

    log.info(f"Processing: @{handle} ({name})")

    # Fetch blog info if available
    about = {"bio": "", "about_url": "", "meta_author": ""}
    if blog_url:
        log.info(f"  Fetching blog: {blog_url}")
        about = extract_about_info(blog_url)

        # Discover RSS if not provided
        if not rss_url:
            log.info(f"  Discovering RSS...")
            rss_url = discover_rss(blog_url) or ""
            if rss_url:
                log.info(f"  Found RSS: {rss_url}")

    # Fetch feed topics
    topics = []
    if rss_url:
        log.info(f"  Fetching feed: {rss_url}")
        topics = extract_feed_topics(rss_url)
        log.info(f"  Got {len(topics)} post titles")

    time.sleep(0.5)

    return {
        "account": account,
        "about": about,
        "rss_url": rss_url,
        "topics": topics,
    }


def main():
    parser = argparse.ArgumentParser(description="Build wiki entity skeletons for X accounts")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--handle", type=str, help="Process single handle (e.g. @willccbb)")
    parser.add_argument("--enrich", action="store_true", help="Print Hermes enrichment prompt")
    parser.add_argument("--force", action="store_true", help="Overwrite existing entity pages")
    args = parser.parse_args()

    accounts = load_accounts(ACCOUNTS_PATH, args.handle)
    log.info(f"Loaded {len(accounts)} accounts from {ACCOUNTS_PATH}")

    if not accounts:
        log.error("No accounts found")
        sys.exit(1)

    WIKI_ENTITIES.mkdir(parents=True, exist_ok=True)
    results = []
    written = []

    for account in accounts:
        handle = account["handle"].lstrip("@")
        name = account.get("name", handle)
        slug = slugify(name)
        filepath = WIKI_ENTITIES / f"{slug}.md"

        # Skip existing unless --force
        if filepath.exists() and not args.force:
            log.info(f"  Skipping {slug}.md (exists, use --force to overwrite)")
            continue

        result = process_account(account)
        results.append(result)

        page = generate_skeleton(
            account, result["about"], result["rss_url"], result["topics"]
        )

        if args.dry_run:
            log.info(f"  [DRY RUN] Would write: {filepath.name}")
            print(f"\n{'='*60}\n{filepath.name}\n{'='*60}")
            print(page[:500] + "..." if len(page) > 500 else page)
        else:
            filepath.write_text(page, encoding="utf-8")
            log.info(f"  Wrote: {filepath.name}")
            written.append({"name": name, "handle": handle, "slug": slug, "file": filepath.name})

    # Save raw results
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)

    # Merge with existing data if present
    existing = []
    if OUTPUT_JSON.exists():
        try:
            existing = json.loads(OUTPUT_JSON.read_text())
        except Exception:
            pass
    existing.extend(results)
    OUTPUT_JSON.write_text(json.dumps(existing, indent=2, default=str), encoding="utf-8")
    log.info(f"Saved raw data to {OUTPUT_JSON}")

    if not args.dry_run and written:
        # Update wiki index
        entity_lines = "\n".join(
            f"- [[entities/{w['slug']}|{w['name']}]] (@{w['handle']})"
            for w in sorted(written, key=lambda x: x["name"].lower())
        )
        try:
            index = WIKI_INDEX.read_text(encoding="utf-8")
            marker = "### X/Twitter Accounts"
            if marker in index:
                # Append to existing section
                idx = index.index(marker) + len(marker)
                next_heading = index.find("\n### ", idx)
                if next_heading == -1:
                    next_heading = index.find("\n## ", idx)
                if next_heading == -1:
                    next_heading = len(index)
                existing_section = index[idx:next_heading]
                index = index[:idx] + existing_section.rstrip() + "\n" + entity_lines + "\n" + index[next_heading:]
            else:
                # Add new section after HN Popular Bloggers if it exists
                hn_marker = "### HN Popular Bloggers"
                if hn_marker in index:
                    idx = index.index(hn_marker)
                    next_heading = index.find("\n### ", idx + len(hn_marker))
                    if next_heading == -1:
                        next_heading = index.find("\n## ", idx + len(hn_marker))
                    if next_heading == -1:
                        next_heading = len(index)
                    index = index[:next_heading] + f"\n\n{marker}\n{entity_lines}\n" + index[next_heading:]
                else:
                    index += f"\n\n{marker}\n{entity_lines}\n"
            WIKI_INDEX.write_text(index, encoding="utf-8")
            log.info("Updated wiki/index.md")
        except Exception as e:
            log.warning(f"Could not update index: {e}")

        # Append to log
        today = datetime.now().strftime("%Y-%m-%d")
        handles = ", ".join(f"@{w['handle']}" for w in written)
        log_entry = f"\n## {today}\n- Added {len(written)} X account entity skeletons: {handles}\n"
        with open(WIKI_LOG, "a", encoding="utf-8") as f:
            f.write(log_entry)
        log.info(f"Updated wiki/log.md")

        log.info(f"\nDone: {len(written)} skeleton pages written")

    # Print enrichment prompt
    if args.enrich or (not args.dry_run and written):
        all_written = written if written else [
            {"name": a.get("name", a["handle"].lstrip("@")),
             "handle": a["handle"].lstrip("@"),
             "slug": slugify(a.get("name", a["handle"].lstrip("@"))),
             "file": slugify(a.get("name", a["handle"].lstrip("@"))) + ".md"}
            for a in accounts
        ]
        prompt = generate_enrich_prompt(all_written)
        print(f"\n{'='*60}")
        print("DISCORD PROMPT FOR HERMES ENRICHMENT:")
        print(f"{'='*60}")
        print(prompt)
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
