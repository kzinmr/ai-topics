---
name: newsletter-wiki-ingest
description: Downstream ingest stage of the newsletter or blog cron pipeline — consume a triage checkpoint JSON and create/update wiki pages autonomously.
trigger: >
  When running the newsletter-wiki-ingest or blog-wiki-ingest cron job, or when
  the user provides a triage checkpoint JSON (from newsletter-triage,
  blog-triage, or semantic-article-grouping) and asks to process the 'take'
  decisions into wiki pages. This is the downstream of newsletter-triage or
  blog-triage — not for single-article enrichment (use
  wiki-entity-enrichment-from-article for that).
---

# Newsletter Wiki Ingest

Consume a pre-triaged checkpoint and create/update wiki pages autonomously.
Supports both the newsletter and blog pipelines (the structure is identical):

- **Newsletter pipeline:** newsletter-ingest → newsletter-triage → **this skill** → git push
- **Blog pipeline:** blog-ingest → blog-triage → **this skill** → git push

## Input Format

Triage checkpoint JSON injected via `context_from` cron chaining from the
upstream triage job, OR from a file. Two possible checkpoint paths:

| Pipeline | Checkpoint path |
|----------|----------------|
| Newsletter | `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` |
| Blog      | `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` |

The `context_from` chaining injects the upstream triage output directly. If not
available via chaining, read the appropriate checkpoint file.

Structure:

```json
{
  "summary_ja": "日本語サマリー...",
  "decisions": [
    {
      "item_id": "...",
      "source": "newsletter",
      "source_name": "Newsletter Title",
      "title": "Link N",
      "url": "...",
      "recommended_action": "take",
      "reason_ja": "★★★★★ 新規概念ページ候補...",
      "candidate_wiki_path": "concepts/gpt-5.5"
    }
  ],
  "_triage_checkpoint": {
    "ok": true,
    "output_path": "...",
    "checkpoint_path": "..."
  }
}
```

## Workflow

### 0. Prerequisites — Orient on the Wiki

Before any operation, always orient:

```bash
# Read wiki orientation files
read_file ~/wiki/SCHEMA.md
read_file ~/wiki/index.md
read_file ~/wiki/log.md offset=<last 30 lines>
```

Then search for any pages that might already exist for the candidate topics:

```bash
search_files "topic-keyword" path=~/wiki/concepts target=files
search_files "topic-keyword" path=~/wiki/entities target=files
```

### 1. Load the Checkpoint

Three possible states:

**State A — Valid Checkpoint (`_triage_checkpoint.ok === true`):**
- Filter to only `recommended_action === "take"` decisions
- If no take decisions, respond `[SILENT]` (for Cron delivery)
- Continue to Step 2

**State B — No Checkpoint Data:** If the checkpoint is missing entirely (null, undefined, or the cron job was invoked directly without `context_from` chaining):
- Fall back to the **Triage Failure Recovery** section below
- Do NOT call this a "failed triage" or try to load from an alternate path
- The pipeline is simply not configured with chaining — proceed to recovery

**State C — Failed Checkpoint (`_triage_checkpoint.ok === false`):**
- Do NOT abort — fall back to the **Triage Failure Recovery** section below
- The failure message (e.g., `"failed to parse JSON response from newsletter-triage output"`) provides the diagnosis but the recovery path is the same regardless of the specific error: read raw files and triage manually

### 1a. Detect Prior Batch — Check log.md

Before creating or updating anything, scan the last 30-50 lines of log.md for an entry
matching the same source/newsletter title. If one exists, this is a **follow-up batch**:

1. Read the existing log entry to understand what was already processed
2. For each candidate_wiki_path, check if the file already exists on disk — use
   `search_files "filename.md" target=files` rather than assuming it doesn't exist
3. **If all concept-level pages already exist**, shift focus to entity-level updates
   that might have been missed (e.g., entity pages from ★★★★☆ or ★★★☆☆ decisions)
4. Skip creating pages that already exist — verify their content is sufficient instead
5. Do not duplicate log entries — append the new batch as a sub-section under the
   existing log entry (e.g., `### Follow-up Batch (Triage Processing)`)

### 2. For Each Take Decision

For each take decision:

- Read the source material: `web_extract(url)` or the raw newsletter file
- Determine page type based on `reason_ja` rating:
  - **★★★★★** → Probably create a **new concept page**
  - **★★★★☆** → Probably **update an existing page**
  - **★★★☆☆** → Probably **update an entity page**
- If `candidate_wiki_path` is provided, use it as the file path

### 3. Batch Processing Strategy

Group decisions to minimize file I/O:

1. **Create new pages first** — use `write_file` for each new page
2. **Update existing pages** — use `patch` for each update
3. **Update index.md** — add entries for new pages at correct alphabetical position in each section
4. **Update log.md** — append a single batch log entry
5. **Update total page count** in index.md header

### 4. Page Types

#### New Concept Pages (★★★★★)
Full YAML frontmatter with:
```yaml
---
title: Concept Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [relevant-tags]
aliases: [alternate-names]
sources:
  - raw/articles/source-filename.md
---
```

Target quality: self-contained but well cross-linked with `[[wikilinks]]` to 2+ existing pages.

#### Existing Page Updates (★★★★☆)
Use `patch` to add new sections. Always bump `updated` date in frontmatter.
After updating a page, verify with `read_file`.

#### Entity Page Updates (★★★☆☆)
Add new developments as bullet points under the relevant section heading.
Always bump `updated` date and append to `sources:` array.

### 5. Index & Log Updates

**Index updates** require care:
- Read enough of `index.md` with `offset/limit` to find each insertion point
- Each entry gets its own `patch` call at the correct alphabetical position
- Update total page count in header: increment by number of new pages

**Log updates** are append-only:
```markdown
## YYYY-MM-DD — News Ingest (Source Title)

### New Concept Pages
- **concepts/page.md** — One-line summary

### Updated Entity Pages
- **entities/page.md** — What was added

### Updated Concept Pages
- **concepts/page.md** — What was added

### Updated Navigation
- **index.md** — N new entries; total pages: M

### Raw Source
- `raw/articles/filename.md` — article saved as source
```

### 6. Commit and Push — CRITICAL: Do This Early

```bash
cd ~/ai-topics && git add wiki/ && git diff --stat --cached && git commit -m "wiki: <pipeline> ingest YYYY-MM-DD (Source)" && git push
```

Where `<pipeline>` is `newsletter` or `blog` depending on the source.
Always verify `git push` succeeds before reporting completion.

**Checkpoint strategy for large batches:** When ingesting 10+ decisions (multiple new pages + updates), tool call limits may be hit before you finish all updates. To prevent data loss:
1. After creating all new pages and updating index.md/log.md, **commit immediately** (don't wait to finish all entity/concept updates)
2. If some updates remain incomplete, they can be resumed in a follow-up batch
3. An uncommitted wiki with 10+ modified files is vulnerable to session loss

Where `<pipeline>` is `newsletter` or `blog` depending on the source.
Always verify `git push` succeeds before reporting completion.

## Cron Context

When running as a Cron job:
- **Detect the pipeline** — check `source` field in the first decision (newsletter vs blog), or infer from the cron job name / checkpoint path. Use this to determine the commit message prefix and log entry style.
- **No asking questions** — make reasonable autonomous decisions
- **Output in Japanese** (日本語)
- **Silent on no-op**: If no take decisions, respond exactly `[SILENT]`
- **Auto-delivery**: Final response is auto-delivered; don't use send_message

## Source File Fallback

When processing triage decisions, the raw newsletter files in `~/wiki/raw/newsletters/` may be **empty stubs (0 bytes)** or contain only metadata. This happens when the upstream `newsletter-ingest` job captured the email but failed to extract full article content.

**Detection:**
```bash
# Check file size before relying on it
wc -c ~/wiki/raw/newsletters/<filename>.md
```

**Fallback workflow:**
1. If raw file is < 1KB, treat it as a stub — skip reading it
2. Use the URL from the triage decision's `url` field with `web_extract(url)`
3. If the URL is a newsletter redirect (e.g., `substack.com/redirect/...` or `link.mail.beehiiv.com/...`), try:
   - Search for the article title + source name on the web
   - Use the search result URL instead of the redirect link
   - Note the fallback in your log entry
4. For obfuscated URLs, try `web_search` with: `"<newsletter title>" "<article keywords>" site:<domain>`

## Triage Failure Recovery

When the checkpoint is missing or failed (States B/C in Step 1), **do not abort**. Perform a manual triage from raw files, then proceed with the normal ingest workflow.

### 1. Discover Raw Newsletters

List available raw newsletter files, sorted by size (largest = most content):

```bash
ls -la ~/wiki/raw/newsletters/*.md | sort -k5 -rn
```

Read each file to identify the newsletter source name and extract actual content links:

```bash
read_file ~/wiki/raw/newsletters/<latest-file>.md
```

### 2. Filter Noise from Newsletter Candidates

The raw newsletter files contain both content and UI noise from newsletter platforms. Use the **Substack Noise Filtering** patterns from the `semantic-article-grouping` skill:

| Pattern | Type | Action |
|---------|------|--------|
| `play_audio=true`, `play_card` | Podcast/audio UI | Skip |
| `action=post-comment`, `comments=true` | Comment section | Skip |
| `submitLike=true`, `reaction` | Like/heart button | Skip |
| `share=true`, `action=share` | Share link | Skip |
| `play_card_progress_bar`, `play_card_duration`, `play_card_play_button` | Player chrome | Skip |
| `redirect/app-store` | App download page | Skip |
| `@username` (e.g., `@lenny`) | Author profile | Skip |
| `redirect/2/eyJ...` or `redirect/<uuid>` | Obfuscated redirect | Try web_extract or skip |
| `utm_campaign=email-read-in-app` | Read-in-app prompt | Skip |
| beehiiv tracking URLs | Link tracking | Resolve if possible, skip if broken |

Keep only **actual content URLs** — usually 0-4 per newsletter.

### 3. Resolve and Read Article Content

For each candidate article:

**a) If URL is a direct content URL** (medium.com, latent.space, thenewstack.io, etc.):
- Use `web_extract(url)` to fetch content
- Search for the article by title on the web if the URL is dead

**b) If URL is an obfuscated Substack redirect** (`/redirect/2/eyJ...`):
- Search for the newsletter name + article title: `web_search("<newsletter title> <article keywords>")`
- Use the direct URL from search results
- Extract content with `web_extract()` from the direct URL

**c) If URL is a beehiiv tracking link** (`link.mail.beehiiv.com`):
- The raw newsletter file may contain the actual article content inline (beehiiv often includes full article text in the email HTML)
- Search the raw file for the article's key text — many beehiiv newsletters embed the full body
- If inline content is < 500 chars, try `web_search` for the article title + source

**d) Determine relevance** using the **Value Assessment Matrix**:
| Rating | Criteria | Wiki Action |
|--------|----------|-------------|
| ★★★★★ | AI/ML concept not yet in wiki | New concept page |
| ★★★★☆ | Significant update to existing page | Update existing page |
| ★★★☆☆ | Minor add to entity page | Entity page update |
| ★★☆☆☆ | Minor mention only | Skip |
| ★☆☆☆☆ | Not AI-related (business, career, general tech) | Skip |

### 4. Semantic Grouping

Group recovered articles by topic:
- **Shared entities** (same person/company/model)
- **Related concepts** (agentic engineering, inference, harness engineering)
- **Source themes** (the same newsletter)

### 5. Merge into Normal Ingest Workflow

Once you have identified the take-able articles and their wiki paths:

1. Check existing wiki pages (same as Step 2 originally): `search_files` for matching topics
2. Create/update pages (same as Steps 3-5 normally)
3. Update index.md and log.md (same as Step 5 normally)
4. Commit and push (same as Step 6 normally)

### 6. Log the Recovery

In the log.md entry, note that the triage was performed manually due to pipeline failure:

```markdown
## YYYY-MM-DD — News Ingest (Source Title)

**Triage recovery:** Upstream newsletter-triage checkpoint failed
(`failed to parse JSON response`). Performed manual triage from raw files.

### New Concept Pages
...
```

### Key Differences from Normal Workflow

| Aspect | Normal Workflow | Recovery Workflow |
|--------|-----------------|-------------------|
| Article selection | Pre-filtered by triage job | Manual filtering needed |
| URL resolution | Already resolved | May need web_search |
| Star ratings | Pre-assigned | You assign them |
| Prior batch detection | Same (check log.md) | Same (check log.md) |
| Wiki page creation | Same | Same |

## Pitfalls

- **Always orient first** — read SCHEMA.md + index + recent log before any operation
- **Detect follow-up batches** — before creating pages for candidate_wiki_path, check the
  filesystem AND log.md. Prior runs may have already processed them. If log.md has an entry
  for the same source, read what was already done and only handle what's left (entity-level
  updates, minor patches).
- **Context compaction can mask prior work** — when running in long sessions, the system may
  inject a "Context Compaction" summary mentioning work done in an earlier window. Review this
  summary to discover already-completed tasks before acting on the triage checkpoint again.
- **Don't create duplicates** — search existing topics before creating new pages
- **Index insertion order matters** — each new entry goes at its alphabetical position
- **Total page count must be correct** — increment by number of new pages
- **Log is append-only** — use `---` separator between log entries
- **Verify files after writing** — use `search_files` or `read_file` to confirm
- **Patch over write when possible** — use `patch` for existing pages, not full rewrites
- **Subagents need explicit absolute paths** — delegated subagents may have different HOME; pass `/opt/data/ai-topics/wiki/...` explicitly
- **Don't combine [SILENT] with content** — respond with exactly `[SILENT]` and nothing else if no work to do
- **Japanese output is mandatory** for Cron reports — write the final summary in Japanese
- **Triage failure is not a skip signal** — when the upstream triage checkpoint fails, do NOT abort or output `[SILENT]`. Fall back to the Triage Failure Recovery section and perform manual triage from raw files. The failure means the triage didn't complete, not that there's nothing to do.
