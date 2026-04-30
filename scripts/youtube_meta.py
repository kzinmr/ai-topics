#!/usr/bin/env python3
"""
youtube_meta.py — Extract metadata from YouTube video pages via local HTTP fetch.
Use when youtube-transcript-api is unavailable (no pip) and web_extract returns
incomplete content.

Usage:
    python3 youtube_meta.py VIDEO_ID [--all-langs] [--json]

Examples:
    python3 youtube_meta.py UXQ916WRK0A
    python3 youtube_meta.py UXQ916WRK0A --json
    python3 youtube_meta.py UXQ916WRK0A --all-langs
"""

import urllib.request
import json
import re
import sys

VIDEO_URL_TEMPLATE = "https://www.youtube.com/watch?v={}"

def extract_meta(video_id, all_langs=False):
    url = VIDEO_URL_TEMPLATE.format(video_id)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        },
    )
    resp = urllib.request.urlopen(req, timeout=15)
    content = resp.read().decode("utf-8", errors="replace")

    meta = {}

    # Title (from <title> tag, strip " - YouTube" suffix)
    m = re.search(r"<title>(.*?)</title>", content)
    meta["title"] = m.group(1).replace(" - YouTube", "").strip() if m else None

    # Channel name
    m = re.search(r'"author"[^:]*:\s*"([^"]+)"', content)
    meta["channel"] = m.group(1) if m else None

    # Description (handles escaped chars)
    m = re.search(r'"shortDescription"\s*:\s*"((?:[^"\\]|\\.)*)"', content)
    if m:
        desc = m.group(1).replace("\\n", "\n").replace('\\"', '"').replace("\\\\", "\\")
        meta["description"] = desc
    else:
        meta["description"] = None

    # Length in seconds
    m = re.search(r'"lengthSeconds"\s*:\s*"?(\d+)"?', content)
    if m:
        s = int(m.group(1))
        meta["length_seconds"] = s
        meta["duration"] = f"{s // 60}:{s % 60:02d}"
    else:
        meta["length_seconds"] = None
        meta["duration"] = None

    # Keywords
    m = re.search(r'"keywords"\s*:\s*(\[.*?\])', content)
    if m:
        try:
            meta["keywords"] = json.loads(m.group(1))
        except json.JSONDecodeError:
            meta["keywords"] = []
    else:
        meta["keywords"] = []

    # View count
    m = re.search(r'"viewCount"\s*:\s*"(\d+)"', content)
    meta["view_count"] = int(m.group(1)) if m else None

    # Publish date
    m = re.search(r'"publishDate"\s*:\s*"([^"]+)"', content)
    meta["publish_date"] = m.group(1) if m else None

    # Upload date
    m = re.search(r'"uploadDate"\s*:\s*"([^"]+)"', content)
    meta["upload_date"] = m.group(1) if m else None

    # Video ID
    m = re.search(r'"videoId"\s*:\s*"([^"]+)"', content)
    meta["video_id"] = m.group(1) if m else video_id

    # Caption languages
    meta["caption_languages"] = list(set(re.findall(r'"languageCode"\s*:\s*"([^"]+)"', content)))
    meta["has_captions"] = len(meta["caption_languages"]) > 0

    if all_langs:
        # Also list all unique caption languages
        pass

    # Channel subscriber count
    m = re.search(r'"subscriberCount"\s*:\s*"(\d+)"', content)
    meta["subscriber_count"] = int(m.group(1)) if m else None

    # Category
    m = re.search(r'"category"\s*:\s*"([^"]+)"', content)
    meta["category"] = m.group(1) if m else None

    return meta


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} VIDEO_ID [--all-langs] [--json]", file=sys.stderr)
        sys.exit(1)

    video_id = sys.argv[1]
    all_langs = "--all-langs" in sys.argv
    as_json = "--json" in sys.argv

    meta = extract_meta(video_id, all_langs=all_langs)

    if as_json:
        print(json.dumps(meta, indent=2, ensure_ascii=False))
    else:
        print(f"Title:        {meta['title']}")
        print(f"Channel:      {meta['channel']}")
        print(f"Duration:     {meta['duration']}")
        print(f"Published:    {meta['publish_date']}")
        print(f"Views:        {meta['view_count']:,}" if meta['view_count'] else "Views:        N/A")
        print(f"Captions:     {'Available (' + str(len(meta['caption_languages'])) + ' langs)' if meta['has_captions'] else 'None'}")
        if meta["keywords"]:
            print(f"Keywords:     {', '.join(meta['keywords'][:10])}")
        print(f"\nDescription:")
        desc = meta.get("description", "")
        if desc:
            print(desc[:2000])
        else:
            print("(none)")


if __name__ == "__main__":
    main()
