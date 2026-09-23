#!/usr/bin/env python3
"""Generic article fetcher for active-crawl.

Fetches a URL, strips HTML to readable text, prints to stdout.
Used by the active-crawl agent to pull source material before hand-writing
a normalized raw article with proper SCHEMA frontmatter (source_url, ingested,
sha256). Does NOT write files itself — the agent reviews output first.

Usage: python3 fetch_article.py <url> [max_chars]
"""
import re
import sys
import html
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def fetch(url, ua=UA):
    req = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    })
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read()
        cs = r.headers.get_content_charset() or "utf-8"
    return raw.decode(cs, errors="replace")


def html_to_text(h):
    h = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    h = re.sub(r"<style.*?</style>", "", h, flags=re.S)
    h = re.sub(r"<(br|/p|/div|/h[1-6]|/li|/tr)[^>]*>", "\n", h, flags=re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r" ?\n ?", "\n", h)
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h.strip()


if __name__ == "__main__":
    url = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 9000
    doc = fetch(url)
    text = html_to_text(doc)
    print(f"RAWLEN={len(doc)} TEXTLEN={len(text)}")
    print("=====TEXT=====")
    print(text[:n])
