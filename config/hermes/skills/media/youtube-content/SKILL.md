---
name: youtube-content
description: >
  Fetch YouTube video transcripts (or metadata fallback) and either (1) transform
  into structured content (chapters, summaries, threads, blog posts), or (2)
  ingest into the wiki as a raw article with entity/concept page enrichment.
  Use when the user shares a YouTube URL or video link, asks to summarize a
  video, requests a transcript, wants to extract and reformat content from any
  YouTube video, OR asks to integrate a YouTube talk into the wiki.
---

# YouTube Content Tool

Extract transcripts from YouTube videos and convert them into useful formats.

> **Channel-level monitoring**: To track a YouTube channel for new videos (RSS-based, auto-discovers new content daily), use the `blogwatcher` skill's "YouTube Channel Monitoring" workflow. This skill handles **individual video** transcript extraction and wiki ingestion.

## Setup

### Option A: youtube-transcript-api (pip, preferred)
```bash
pip install youtube-transcript-api
```
Requires pip/venv/ensurepip availability. Not available on all systems.

### Option B: yt-dlp binary (no install, this env's default)
Permanently installed at `/opt/data/bin/yt-dlp`. Update periodically:
```bash
curl -sL "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp" -o /opt/data/bin/yt-dlp
chmod +x /opt/data/bin/yt-dlp
```
This is the **reliable fallback** for environments where pip/venv are unavailable.
Internally uses YouTube's Android VR Player API to bypass timedtext signature expiry and bot detection.

## Helper Script

`SKILL_DIR` is the directory containing this SKILL.md file. The script accepts any standard YouTube URL format, short links (youtu.be), shorts, embeds, live links, or a raw 11-character video ID.

```bash
# JSON output with metadata
python3 SKILL_DIR/scripts/fetch_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Plain text (good for piping into further processing)
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only

# With timestamps
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --timestamps

# Specific language with fallback chain
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --language tr,en
```

## Output Formats

After fetching the transcript, format it based on what the user asks for:

- **Chapters**: Group by topic shifts, output timestamped chapter list
- **Summary**: Concise 5-10 sentence overview of the entire video
- **Chapter summaries**: Chapters with a short paragraph summary for each
- **Thread**: Twitter/X thread format — numbered posts, each under 280 chars
- **Blog post**: Full article with title, sections, and key takeaways
- **Quotes**: Notable quotes with timestamps

### Example — Chapters Output

```
00:00 Introduction — host opens with the problem statement
03:45 Background — prior work and why existing solutions fall short
12:20 Core method — walkthrough of the proposed approach
24:10 Results — benchmark comparisons and key takeaways
31:55 Q&A — audience questions on scalability and next steps
```

## Workflow

1. **Fetch metadata** using `youtube_meta.py`:
   ```bash
   python3 ~/ai-topics/scripts/youtube_meta.py VIDEO_ID --json
   ```
   This gives title, channel, duration, description, caption language availability.

2. **Fetch transcript** using the best available method:

   **Method A — yt-dlp (primary, this env)**: Pre-installed at `/opt/data/bin/yt-dlp`.
   ```bash
   /opt/data/bin/yt-dlp --write-auto-subs --sub-langs "en" --skip-download \
     -o "/tmp/yt_transcript_%(id)s" "https://www.youtube.com/watch?v=VIDEO_ID"
   ```
   VTT output lands at `/tmp/yt_transcript_VIDEO_ID.en.vtt`.
   Clean the triplicated lines (VTT cue overlap) using the Python dedup script in step 4d below.

   **Method B — python helper script (when pip available)**:
   ```bash
   python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only --timestamps
   ```

3. **Validate**: confirm the output is non-empty and in the expected language.

4. **Clean VTT output** (yt-dlp only): VTT files have overlapping cue regions causing triplicated lines. Use Python to deduplicate:

   ```python
   import re
   with open('/tmp/yt_transcript_VIDEO_ID.en.vtt', 'r') as f:
       content = f.read()
   lines = content.split('\\n')
   segments = []
   current_start = 0.0
   for line in lines:
       line = line.strip()
       if '-->' in line:
           start_str = line.split(' --> ')[0]
           parts = start_str.split(':')
           if len(parts) == 3:
               h, m, s = parts
               current_start = float(h)*3600 + float(m)*60 + float(s)
           elif len(parts) == 2:
               m, s = parts
               current_start = float(m)*60 + float(s)
           continue
       if not line or line in ['WEBVTT','Kind: captions','Language: en'] or line.isdigit():
           continue
       clean = re.sub(r'<[^>]+>', '', line)
       clean = re.sub(r'\\s+', ' ', clean).strip()
       if clean:
           found = any(clean == t for _, t in segments)
           if not found:
               mins = int(current_start // 60)
               secs = int(current_start % 60)
               segments.append((f'{mins:02d}:{secs:02d}', clean))
   ```

5. **Chunk if needed**: If the transcript exceeds ~50K characters, split into overlapping chunks (~40K with 2K overlap) and summarize each chunk before merging.

6. **Transform** into the requested output format. If the user did not specify a format, default to a summary.

7. **Verify**: re-read the transformed output to check for coherence, correct timestamps, and completeness before presenting.

## Pitfalls

### Patch Tool Quirk with Markdown Lists

When using `patch` to add items to markdown lists (e.g., adding a talk entry to `doug-turnbull-speaking.md`), the tool may introduce a stray `|` prefix on each patched line if the `old_string` doesn't perfectly account for the leading whitespace and `-` character. **Always verify the patched file** after applying — if `|` characters appear at line starts, run a second patch to strip them.

### Avoid `&` in Commit Messages

`git commit -m "..."` with `&` in the message (e.g., "Turnbull & Tunkelang") causes the terminal tool to error, interpreting `&` as a backgrounding operator. **Use "and" instead**: `-m "wiki: add Talk Title talk (Speaker and Guest)"`.

### VTT Triplicated Lines

The yt-dlp VTT output has overlapping cue regions that produce triplicated lines. Always run the Python dedup script (step 4d in the Workflow section) before extracting meaningful text.

### No `himalaya` or Dedicated Mail Client

This profile uses Gmail IMAP via `process_email.py` for newsletter ingestion. Do NOT use himalaya, mutt, or any other mail client — it disrupts `\Seen` flags and the `Processed` label dedup.

### Tag Taxonomy Validation on Git Commit

The pre-commit hook validates ALL frontmatter `tags:` against `wiki/SCHEMA.md` canonical tags. Non-canonical tags block the commit. **Before committing wiki changes, verify every tag on new/modified pages is in the SCHEMA taxonomy.**

Common non-canonical → canonical mappings:

| Non-Canonical | Canonical |
|---------------|-----------|
| `interview-series` | `developer-experience` or `ai-agents` |
| `telegram` | `agent-communication` |
| `whatsapp` | `agent-communication` |
| `meetup` | `community` |
| `tutorial` | `developer-tooling` |
| `youtube` | Add to SCHEMA.md Meta category first (legitimate source-type tag) |

If a legitimate new tag category is needed, add it to `wiki/SCHEMA.md` first. Alternative: map it via `scripts/tag_normalization.py`. Emergency override: `git commit --no-verify`.

When writing **new wiki pages** (entities, concepts, comparisons), always check the SCHEMA taxonomy before setting frontmatter tags — not just after the commit fails. This avoids a round-trip fix.

## Error Handling

- **No captions available** (`has_captions: false` or empty `caption_languages`): This is a distinct case from "transcript disabled" — the video simply has no subtitles. Use the **Description-as-Outline fallback**:

  1. Extract chapter markers from the YouTube description (usually timestamps like `00:00 Topic`).
  2. Build a chapter summary table from those markers as the raw article skeleton.
  3. Supplement with `web_search` for each speaker's background, published work, and companion articles (Substack, blog posts).
  4. Write the raw article with a prominent note:
     ```markdown
     > **Note**: No captions were available for this episode at time of ingestion. Content below is based on the YouTube chapter markers, description, and cross-referencing with the speakers' published work. This page will be enriched when transcript becomes available.
     ```
  5. Entity page creation/enrichment can still proceed — use web research + the raw article's chapter-based insights.
  6. The transcript gap primarily affects quote extraction and nuance; the chapter markers provide sufficient structure for entity pages.
- **Private/unavailable video**: relay the error and ask the user to verify the URL.
- **No matching language**: retry without `--language` to fetch any available transcript, then note the actual language to the user.
- **Dependency missing**: If `pip`/`venv`/`ensurepip`/`uv` is unavailable or blocked (the default in this environment), use **yt-dlp binary (step 4)** at `/opt/data/bin/yt-dlp` for transcript text. It's pre-installed and doesn't need Python dependencies. If that fails, use `youtube_meta.py` for metadata (step 3), then the Description-as-Outline fallback (step 5).
- **Timedtext API returns 0 bytes**: The `baseUrl` extracted from `ytInitialPlayerResponse.captions.playerCaptionsTracklistRenderer.captionTracks` may appear valid but return empty responses. This occurs even with cookie-sharing opener + proper User-Agent. Likely causes: URL signature expiry (fast-expiring tokens bound to visitor data), IP-based throttling, or bot detection. Use **yt-dlp binary (step 4)** instead — it bypasses this via the Android VR Player API. Do NOT attempt retry loops on the timedtext URL.
- **No JavaScript/browser**: YouTube's SPA rendering and timedtext API may require JS headers that `urllib.request` cannot provide. `web_extract` (LLM-processed HTML) gives title + truncated description but NOT transcript content.

---

## Wiki Ingestion (when the user asks to integrate a YouTube video into the wiki)

After extracting video content, follow this workflow to save it as a wiki raw article and enrich existing entity/concept pages.

### Video Type Classification

Before writing, classify the video as one of:

| Type | Frontmatter `author` | Frontmatter `guest` | Entity Actions | Concept Section Title |
|------|---------------------|---------------------|----------------|----------------------|
| **Solo talk** | Speaker Name (@handle) | (none) | Enrich speaker's speaking page only | `### Talk: "Title" (Date)` |
| **Panel/discussion** | Host Name (@handle) | Guest Name(s) | Enrich host's speaking page + CREATE guest entity page (if none exists) | `### Discussion: "Title" (Date)` |

For panel/discussion videos:
- Check if the guest already has a wiki entity page via `search_files` before creating
- If creating, write a skeleton entity page with `status: skeleton` and `sources:` linking to the raw article
- The concept page section should frame both perspectives (host + guest) — not just the host's thesis

### 1. Save Raw Article — Companion Sources

If the user also provided a **Google Slides link** alongside the YouTube URL, extract both:
- Fetch slides via `/export/txt` (structured outline, tables, section headings)
- Fetch transcript via yt-dlp (spoken nuance, quotes, framing)
- Fuse into a single raw article using slides' structure as outline and transcript for depth

See `wiki-ingestion-pipelines` reference `references/manual-article-ingest-patterns.md` → **Pattern 10: Google Slides / Presentation Export for Content Extraction** for the full workflow.

**X/Twitter article companion** — When the user provides both an X/Twitter article URL AND a YouTube URL about the same topic, treat them as complementary sources:
- The X article is typically structured, polished, and pattern-focused (ideal for concept page patterns)
- The YouTube video provides depth, expert perspective, quotes, and context (ideal for entity page biographies)
- Save BOTH as separate raw articles (not fused into one)
- Use parallel `delegate_task` subagents for the enrichment phase: one for entity pages, one for concept pages. See `wiki-entity-enrichment-from-article` reference `references/parallel-entity-concept-creation.md` for the full pattern.

**GitHub companion repo** — Many workshop/course videos have a companion GitHub repo linked in the description (e.g., `github.com/hugobowne/build-your-own-ai-assistant`). Fetch the README via `web_extract` on `raw.githubusercontent.com/.../main/README.md`. This gives the structured build pipeline, tool list, and architectural overview that complements the spoken transcript.

**Substack companion article** — Vanishing Gradients and similar channels often publish a companion blog post on Substack summarizing the workshop. Fetch via `web_extract` on the canonical Substack URL.

**⚠️ Truncation risk** — Both GitHub READMEs and Substack articles frequently trigger `web_extract` LLM summarization timeout (~5K char limit). When truncated, fall back to `execute_code` with `urllib.request` (stdlib, no pip) to get full text. See `wiki-ingestion-pipelines` reference `references/web-extract-execute-code-fallback.md` for the complete fallback pattern.

Use `write_file` to create:

Frontmatter for the combined article:
```markdown
---
title: "Video Title — Speaker Name"
created: YYYY-MM-DD
author: Speaker Name (@handle)
source: YouTube
url: https://www.youtube.com/watch?v=VIDEO_ID
type: talk  # or "panel" for discussions with guests
duration: MM:SS
tags: [relevant-tags]
---

# Talk Overview

Brief 2-3 sentence summary of the video's topic and significance.

## Core Thesis

The video's main argument, extracted from the description/transcript.

## Key Insights

- Bullet points or tables of the talk's key arguments
- Include quotes with context

## Connection to Wiki Concepts

Map the talk to existing wiki concepts:
- [[concepts/agentic-search]] — How the talk validates or extends existing coverage
- [[entities/speaker-name]] — If a person entity page exists
```

### 2. Enrich Person Entity Pages

For talks by tracked personalities (e.g., Karpathy, Willison, Turnbull):

- **Speaking page** (`entities/{name}-speaking.md`): Add to Conference Talks list. Format:
  ```markdown
  - **\"Talk Title\"** (Month YYYY): MM-minute talk — 1-sentence summary of the core argument. [[raw/articles/YYYY-MM-DD_slug]]
  ```
- **Main entity page** (`entities/{name}.md`): Add as a "Recent" item or link from related sections if the talk covers a new topic.

### 3. Enrich Concept Pages

If the talk provides a new framework, taxonomy, or insight that extends existing concept pages:

- Add a dedicated subsection (e.g., `### Talk: "Title" (Date)`)
- Extract the speaker's framework/stages as a table or bullet list
- Cross-reference with existing subsections (academic papers, other practitioner perspectives)
- Add the talk to the concept page's `Sources` section (both frontmatter and bottom list)

### 4. Update Wiki Metadata

- **`wiki/log.md`**: Prepend a new entry with the date, what was done, and which pages were touched
- **`wiki/index.md`**: Only if a new entity or concept page was created (not for enrichment of existing pages)

### 5. Commit & Push

```bash
cd ~/ai-topics
git add wiki/
git commit -m "wiki: add Talk Title talk (Speaker) — raw article + enrich speaking/concept pages"
git push
```

See also: [[wiki-entity-enrichment-from-article]] for general article enrichment patterns, [[wiki-git-sync]] for commit conflict handling.

### Multi-Episode Series Ingestion (3-Phase Parallel Pipeline)

For series with 2+ episodes (podcasts, course playlists), use this proven 3-phase pipeline. The Show Us Your (Agent) Skills ep2-4 ingestion (3 episodes, 14 speakers, 5 concept pages enriched) validated this approach end-to-end.

#### Phase 1: Download + Metadata + Raw Articles (parent agent)

Run metadata fetch and transcript download for ALL episodes in a single `execute_code` block:

```python
import subprocess, json
video_ids = ["VID1", "VID2", "VID3"]
for vid in video_ids:
    # Metadata
    subprocess.run(["python3", "~/ai-topics/scripts/youtube_meta.py", vid, "--json"], ...)
    # Transcript
    subprocess.run(["/opt/data/bin/yt-dlp", "--write-auto-subs", "--sub-langs", "en",
        "--skip-download", "-o", f"/tmp/yt_transcript_{vid}", f"https://www.youtube.com/watch?v={vid}"], ...)
```

Then write all raw articles from the parent agent (NOT subagents). Use YouTube chapter markers from descriptions as the chapter table. The parent agent has the full picture of which speakers appear across episodes.

#### Phase 2: Entity Pages (parallel delegate_task subagents)

Dispatch ONE subagent per episode (respecting `max_concurrent_children=3`):

```
Subagent 1: ep N speakers → CREATE new entity pages + ENRICH existing ones
Subagent 2: ep N+1 speakers → same
Subagent 3: ep N+2 speakers → same
```

Each subagent receives:
- Transcript path on disk
- Raw article path
- List of speakers with (CREATE|ENRICH) + key talking points
- Format reference (existing entity page example)
- Instructions to use web_search for background research

**Critical**: Include in the subagent context that it must use `read_file` on the raw article first (not the full transcript unless needed for quotes). The raw article already distills the key insights.

#### Phase 3: Concept Pages (parent agent)

After subagents complete, enrich concept pages from the parent agent.
See `references/batch-youtube-concept-enrichment.md` for the full read→patch→verify pattern and pitfall guide.

Concept pages that typically benefit: `agentic-engineering.md`, `agent-skills.md`, `coding-agents.md`, `ai-safety.md`, `reward-hacking.md`, `context-engineering.md`.

#### Commit Pattern

Subagents write files to disk. The parent agent does ONE commit at the end:
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest SERIES_NAME epX-Y — N raw articles, M new entity pages, E enriched entities, C enriched concept pages" && git push
```

Verify pre-commit hooks pass (tag validation, index.md clean).

### Podcast Companion to Existing Article

When a podcast episode is a companion/discussion of a recently ingested article, use the enrichment-only workflow in `references/podcast-companion-ingestion.md`. Key difference: no new concept pages — focus on enriching existing pages with podcast-exclusive Nuances, predictions, and framing.
