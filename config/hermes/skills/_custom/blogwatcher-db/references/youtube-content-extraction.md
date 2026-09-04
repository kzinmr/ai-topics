# YouTube Content Extraction from Blogwatcher URLs

Some blogs tracked by blogwatcher (notably "AI Engineer") publish conference talk recordings on YouTube, not written articles. When a blogwatcher URL is `youtube.com/watch?v=...`, use this extraction path instead of web scraping.

## Detection

Check the article URL field from the blogwatcher query — if it matches `youtube.com/watch?v=`, proceed with yt-dlp extraction.

## Prerequisites

`yt-dlp` is available at `/opt/data/bin/yt-dlp`. It can extract video descriptions, metadata, and auto-generated subtitles.

## Step 1: Get video description + metadata

```bash
yt-dlp --skip-download --print "%(title)s|||%(description)s|||%(duration)s|||%(view_count)s|||%(upload_date)s|||%(channel)s|||%(webpage_url)s" "VIDEO_URL"
```

This gives a pipe-delimited output with all metadata fields. The description often contains a useful summary, timestamps, and speaker links.

## Step 2: Download auto-generated English subtitles

```bash
yt-dlp --write-auto-subs --sub-lang en --skip-download -o "/tmp/yt_subs_%(id)s" "VIDEO_URL"
```

This downloads subtitles as WebVTT (`.en.vtt`). yt-dlp auto-converts to SRT (`.en.srt`) by default.

## Step 3: Clean up SRT auto-subtitles

YouTube auto-generated subtitles show 2-3 overlapping lines at a time, causing triplication in plain-text extraction. **Do NOT just join all text lines.** Use this cleanup pattern:

```python
import re

with open('/tmp/yt_subs_VIDEO_ID.en.srt', 'r') as f:
    content = f.read()

# Parse each subtitle block
blocks = re.split(r'\n\n+', content.strip())
all_text = []

for block in blocks:
    lines = block.strip().split('\n')
    if len(lines) < 3:
        continue
    text_lines = []
    for l in lines[2:]:
        l = l.strip()
        if l and not re.match(r'^\d{2}:\d{2}:\d{2}', l):
            text_lines.append(l)
    if text_lines:
        # Take only the LAST text line per block (newest in auto-subs)
        all_text.append(text_lines[-1])

# Remove consecutive duplicates
deduped = []
prev = ''
for t in all_text:
    if t != prev:
        deduped.append(t)
        prev = t

text = ' '.join(deduped)
text = re.sub(r'\s([?.!,](?:\s|$))', r'\1', text)  # fix spacing before punctuation
text = re.sub(r'\s+', ' ', text).strip()
```

**Pitfall:** `pip install youtube_transcript_api` may fail (no `pip` binary in this environment). Use yt-dlp's `--write-auto-subs` instead — it works without additional dependencies.

## Step 4: Determine content status

- **`content: full`** — auto-subs downloaded AND processed into >1,000 chars of clean text
- **`content: stub`** — auto-subs unavailable, or yielded <1,000 chars after cleanup. Save with description + metadata only.

## Raw article frontmatter for YouTube sources

```yaml
---
title: "Talk Title"
source_url: "https://www.youtube.com/watch?v=VIDEO_ID"
source_domain: "youtube.com/@channelname"
author: "Speaker Name"
affiliation: "Company/Org"
date: YYYY-MM-DD
date_ingested: YYYY-MM-DD
type: raw_article
content: full
format: youtube_transcript
duration_seconds: NNNN
view_count: NNNN
tags:
  - tag1
  - tag2
---
```

## Full example pipeline

See the "Persona Engineering" article (2026-07-29) at `/opt/data/ai-topics/wiki/raw/articles/2026-07-29_ai-engineer-persona-engineering.md` for a complete example of a YouTube talk saved as a raw article with full transcript.
