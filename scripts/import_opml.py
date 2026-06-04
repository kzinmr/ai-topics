#!/usr/bin/env python3
"""Import blogs from OPML into blogwatcher-cli."""

import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main():
    profile_root = Path(os.environ.get("HERMES_PROFILE_ROOT") or os.environ.get("HERMES_SUBPROCESS_HOME") or Path.home()).expanduser()
    opml_path = profile_root / "ai-topics" / "config" / "feeds" / "blogs.opml"
    bw_bin = os.environ.get("BLOGWATCHER_BIN", str(profile_root / "bin" / "blogwatcher-cli"))

    tree = ET.parse(opml_path)
    root = tree.getroot()

    count = 0
    for outline in root.findall(".//outline[@type='rss']"):
        name = outline.get("text", "")
        feed_url = outline.get("xmlUrl", "")
        html_url = outline.get("htmlUrl", "")

        if not name or not html_url:
            continue

        # Use blogwatcher-cli add with --feed-url
        cmd = [bw_bin, "add", name, html_url]
        if feed_url:
            cmd.extend(["--feed-url", feed_url])

        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env={**os.environ, "BLOGWATCHER_YES": "1"})

        if result.returncode == 0:
            count += 1
        else:
            print(f"FAIL: {name} ({html_url}) - {result.stderr.strip()}", file=sys.stderr)

    print(f"Added {count} blogs from {opml_path}")


if __name__ == "__main__":
    main()
