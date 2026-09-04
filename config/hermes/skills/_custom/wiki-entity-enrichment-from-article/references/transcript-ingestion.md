# Transcript Ingestion Workflow

When ingesting a lecture/workshop transcript into `wiki/transcripts/`:

## Directory
- `wiki/transcripts/` — Lecture transcripts (separate from `raw/articles/` and `raw/papers/`)
- Note: Some older references say `wiki/raw/transcripts/` but the canonical location used by all existing transcripts (Cheat at Search, YouTube workshops, etc.) is `wiki/transcripts/`

## Naming Convention
Same pattern as articles: `{YYYY-MM-DD}_{source-slug}_{content-slug}.md`
- `YYYY-MM-DD` = lecture/presentation date (not ingestion date)
- `source-slug` = author X/Twitter handle WITHOUT `@` (e.g., `softwaredoug` for @softwaredoug, `willccbb` for @willccbb)
- **Pitfall**: Do NOT use the author's real name as source-slug. Use the X handle consistently. Example: Will Brown → `willccbb` (not `willbrown`)
- `content-slug` = descriptive slug

## Frontmatter Template
```yaml
---
title: "<Series Name> — <Topic> (Lecture Transcript)"
author: <Author Name>
date: <YYYY-MM-DD>
date_ingested: <YYYY-MM-DD>
source: <slides URL or source URL>
type: transcript
tags:
  - <topic-specific tags from SCHEMA.md>
  - transcript
related_article: articles/<corresponding-article-filename>.md
participants:
  - <Author Name> (instructor)
  - <Other participants>
---
```

## Content Structure
- Preserve timestamps from the original transcript (`**[HH:MM:SS]**`)
- Use structured headings to organize the lecture flow
- Mark Q&A exchanges with participant names: `**[Participant, HH:MM:SS]**`
- Include a "Companion Resources" section at the end linking back to the article and related wiki pages
- **Notebook walkthroughs** (Jupyter notebook-based lessons): Structure by notebook sections (`## Section N: Title`) with code blocks and key insight callouts. Use `**Key point:**` or `**Key insight:**` for important takeaways after each code section. No timestamps needed.

## Bidirectional Linking (MANDATORY)
1. **Transcript → Article**: In the transcript's frontmatter (`related_article`) and body (`**Companion slides:**`)
2. **Article → Transcript**: Add `**Lecture transcript:**` link near the top of the article (after source/companion course lines)
   ```
   **Lecture transcript:** [[raw/transcripts/<transcript-filename>|<Display Title>]]
   ```

## Index and Log Updates
- **index.md**: Append new entry in the Transcripts section (entries are grouped by course/series)
- **log.md**: Append entry with created file, updated article, and updated index

## Portal Page Table Update
When a transcript belongs to a course/lecture series that has a portal page (e.g., `concepts/agents-mcp-rl-course.md`, entity page like `entities/doug-turnbull.md`), update the lecture table in the portal page:

1. Read the portal page to find the lecture schedule table
2. Replace the `*pending*` entry with wikilinks to both the transcript and summary:
   ```
   | <date> | [[transcripts/<transcript-filename>|Lesson N: <Title>]] | [[raw/articles/<summary-filename>|Summary]] |
   ```
3. Add a "Lesson Summaries" section below the table with 2-3 sentence descriptions and transcript/summary/notebook links
4. Add the transcript and summary to the portal page's `sources:` frontmatter and `## Related` section
5. If no portal page exists yet, create one first

## Maven Video Chapters Extraction
Maven workshop pages embed video chapters as JSON in the page source. Extract them with:
```python
import sys, json, re
html = sys.stdin.read()
match = re.search(r'"videoChapters":\[(.*?)\]', html)
if match:
    chapters = json.loads('[' + match.group(1) + ']')
    for ch in chapters:
        ts = ch['start_seconds']
        m, s = divmod(ts, 60)
        h, m = divmod(m, 60)
        print(f'{h:02d}:{m:02d}:{s:02d} — {ch["title"]}')
```
Pipe curl output to this script: `curl -sL "<maven-url>" | python3 extract_chapters.py`

## Summary Article Template

For the companion summary article (`raw/articles/`), use the template at `templates/course-lesson-summary.md`. Key elements: frontmatter with `type: article`, Summary section (2-4 sentences), Key Topics with bold concept headers, Key Insights as numbered list, Companion Resources, and Related links with wikilinks.

## Supplementary Notes Pattern
When the user provides supplementary course materials (model selection docs, reading lists, etc.) after initial transcript ingestion:
- Add supplementary details as blockquotes in the transcript: `> **Supplementary notes (from course materials):**`
- Place them immediately after the relevant lecture passage they supplement
- Update the companion raw article (summary) with expanded details from the supplementary materials
- Do NOT mix supplementary content into the lecture transcript text itself — keep it visually distinct as blockquotes

## Second-Pass Notebook Enrichment

When the user provides a notebook URL after initial transcript ingestion:

1. Fetch the notebook: `curl -sL "<raw-github-url>" | python3 -c "import json,sys; nb=json.load(sys.stdin); ..."` to extract cells
2. Identify code patterns, tool configurations, and concrete examples not captured in the audio transcript
3. Add `**Notebook details:**` or `**Notebook code pattern:**` blocks to the structured transcript at relevant sections
4. Use fenced code blocks with language tags for code snippets
5. Update the summary article's `**Notebook:**` link to point to the specific notebook file (not just the repo)
6. Add the notebook to the portal page's Companion Resources table
7. Commit message: `"wiki: enrich Lesson N with notebook code patterns (<notebook-name>)"`

**What to extract from notebooks:**
- Concrete library usage patterns (e.g., `instructor.from_openai()`)
- Configuration commands (e.g., `claude mcp add ...`)
- Pydantic model schemas that define tool/structured output shapes
- Alternative approaches listed in markdown cells
- Setup/install steps not mentioned in lecture audio

**Where to insert notebook content in the transcript:**
- Inline at the relevant section, after the timestamped lecture passage
- Use `**Notebook code pattern:**` as a sub-heading (not a new `##` section)
- Don't duplicate what the transcript already says — only add concrete code/config that the audio didn't capture

## Ecosystem Context for Course Portals
When a course portal page exists (e.g., `concepts/agents-mcp-rl-course.md`), add an **Ecosystem Context** section that connects the course to the platforms/tools it teaches:
- Map each instructor to their organization and key products
- Explain how the course content serves as onboarding for those platforms
- Include the RL-harness lifecycle connection if applicable
- Link to the relevant entity pages (e.g., `entities/prime-intellect.md`, `entities/openpipe.md`)
- This makes the portal page a hub that connects educational content to the broader ecosystem

## Companion Repo Pattern
Course materials may span multiple GitHub repos:
- **Main course repo**: Contains course files, README, exercises
- **Companion repo**: Contains specific lesson materials (notebooks, MCP servers, example reports)
- **Lightning lesson repo**: May be a subdirectory of a different repo (e.g., `agent-engineering/lightning-lessons/`)

**Always verify the canonical notebook URL** with the user. Don't assume the first repo you find contains the canonical notebooks. Check both the course's Companion Resources section AND the user's provided URLs.

## Historical Transcript Retrospective

When ingesting a transcript that is **1+ years old**, the user may want a temporal analysis — "how did these predictions hold up?" This is a natural follow-up pattern:

### Step 1: Standard Ingestion
Ingest the transcript, summary article, and entity page as normal.

### Step 2: Retrospective Analysis (user-requested)
When the user asks for a retrospective:
1. **Check the speaker's current work** — read their entity page for post-talk contributions (e.g., Daniel van Strien went from discussing UltraFeedback bugs in Jan 2024 to curating reasoning datasets by 2025). This personal evolution is often the most interesting signal.
2. **Search wiki for current-state knowledge** on the same topics (e.g., `search_files` for related concepts, recent articles, entity pages). Use `delegate_task` for broad research across 10+ wiki pages.
3. **Compare predictions vs. reality** — what the speaker predicted vs. what actually happened
4. **Synthesize** using wiki knowledge as evidence (not web search — use the knowledge base)
5. Present as a structured analysis organized by topic: "What was said → What happened → Assessment"
6. Use a table format for the summary, but provide narrative analysis per topic (not just a table)

### Step 3: Concept Page Creation (user-requested)
If the analysis reveals a reusable decision framework or concept:
1. Create a new concept page (e.g., `concepts/post-training/fine-tuning.md`)
2. **Migrate relevant content** from existing pages (e.g., decision tables from `_index.md`) — replace the original with a wikilink reference
3. **Incorporate the retrospective analysis** as a temporal perspective section
4. Use **references (wikilinks)** for content that stays on other pages — don't duplicate
5. Update the redirect page (if one exists) to point to the new concept page

### Example: Ameisen "Fine-Tuning is Dead" (2024 → 2026)
- Ingested transcript → created companion summary → created entity page
- User requested retrospective → analyzed against Context Rot, GRPO evolution, Knowledge Storage Spectrum
- User requested concept page → created `post-training/fine-tuning.md` with decision framework + migrated table from `_index.md`

## Historical Retrospective
For transcripts >1 year old, consider adding a retrospective section analyzing the speaker's claims from the current vantage point. See `references/historical-retrospective-section.md` for the full pattern (Japanese-language section structure: 的中した予測, 変化した状況, 歴史的意義).

## Reference Link Processing Pattern

When the user provides a list of reference links from the lecture (e.g., slides, tools, datasets, blog posts mentioned by the speaker), process them into the transcript's `## Companion Resources` section — do NOT create individual wiki pages for each link.

### Workflow
1. **Categorize** the links into semantic groups (e.g., "Platforms & Tools", "Synthetic Data & Datasets", "Annotation Tools", "Other References")
2. **Deduplicate** against existing Companion Resources entries
3. **Annotate** each link with a one-line description (what it is, why it matters for the lecture)
4. **Add** to the transcript's Companion Resources section using `### Category` sub-headings
5. **Skip** wiki page creation for links that: (a) are already in the transcript, (b) are general-purpose tools not specific to the lecture's domain, (c) would only generate stub pages

### When to create wiki pages from reference links
Only create entity/concept pages when:
- The link represents a **significant project/tool** with 2+ other wiki references (check with `search_files`)
- The link is to a **paper** that fills a genuine wiki gap
- The link is to a **dataset** that is central to the lecture's methodology (not just an example)

### Time-based triage for old lecture links
When the lecture is 1+ years old, many referenced tools may be superseded or matured. Apply a retrospective lens:
- **Superseded tools** (e.g., Alpaca-style self-instruct in 2024 → OpenThoughts/DataForge in 2026): Reference in transcript only, add a note about what replaced it
- **Matured tools** (e.g., Argilla acquired by HF, DSPy production adoption): Check if entity page exists; if so, enrich with the lecture reference rather than creating a new page
- **Still-active tools** (e.g., distilabel, Gradio): Add to Companion Resources with current context
- **Wiki page candidates from old links**: A tool that was niche in 2024 but is now central (e.g., GRPO, structured generation) may deserve a concept page even if the lecture only mentioned it briefly — use the wiki's current knowledge base, not the lecture's framing, to decide

### Enriching existing entities from reference links
When a reference link points to an entity that already has a wiki page, add the lecture as a source/reference on THAT page rather than just listing it in the transcript. This creates bidirectional linking:
1. `search_files` for the entity name
2. If page exists: add a brief mention in the entity's Sources or Timeline section
3. If page doesn't exist: check if it's referenced elsewhere in the wiki (orphan wikilinks) before deciding to create it

### Category naming convention
Use descriptive `###` headers, not numbered lists. Example:
```
### Platforms & Tools
### Synthetic Data & Fine-tuning Datasets
### Fine-tuning Algorithms & Data Formats
### Annotation Tools
### Knowledge Graphs (Detour)
### Other References
```

## Pitfalls
- Transcripts are Layer 1 (immutable) — do not edit after initial save
- `type: transcript` is the correct frontmatter type (not `type: article`)
- Always add `transcript` to tags list for discoverability
- Transcripts may contain participant names from Q&A — include them in `participants` field
- **Tag taxonomy**: Library/tool names (e.g., `verifiers`, `chromadb`) are NOT valid tags. Use functional tags from SCHEMA.md (e.g., `reinforcement-learning`, `agent-evaluation`). Common traps: `async-processing` → use `async-agents`; `logging` → use `observability`. Check SCHEMA.md before tagging. See `references/transcript-tag-pitfalls.md` for a quick substitution reference by domain.
- **Source-slug MUST be X handle, not real name**: Will Brown → `willccbb` (NOT `willbrown`). This is the #1 naming mistake. The naming convention section already states this, but it's easy to slip when the user refers to the person by name. Always cross-check against the X handle.
- **Pre-existing tag violations block commits**: The pre-commit hook checks ALL staged files, not just yours. If unrelated files have tags not in SCHEMA.md, your commit will be blocked. Workaround: `git reset HEAD`, stage only your files, or fix the unrelated violations first.
- **Batch commit tag fix loop**: When ingesting multiple transcripts in one session (e.g., Lesson 5, 5.5, office hours), the commit accumulates ALL new files. A single missing tag in any file blocks the entire commit. Fix strategy: (1) add missing tag to SCHEMA.md, (2) `git add wiki/` again, (3) re-commit. If multiple files have different missing tags, you may need several rounds. **Proactive approach**: Before writing frontmatter, grep SCHEMA.md for each planned tag. If a tag doesn't exist, add it to SCHEMA.md first, then write the files.
- **Sibling agent file conflicts**: When another cron/subagent modifies the same portal page (e.g., `agents-mcp-rl-course.md`) during your session, `patch` calls will show `_warning` about sibling modifications. The patch still applies correctly (fuzzy matching handles it), but re-read the file before making additional edits to avoid stale-context issues.
- **Multi-hunk patch fails on sibling-modified files**: When a `patch` call with multiple hunks targets a file that a sibling modified between your `read_file` and `patch` call, ALL hunks fail (not just the stale one). **Fix**: Apply patches one hunk at a time with individual `patch` calls instead of multi-hunk patches. If a hunk fails, re-read the file and retry that specific hunk.
- **Concurrent sibling commits reduce your commit scope**: If a sibling subagent commits the same files (transcript, summary, portal page) during your session, your subsequent `git add + git commit` will only capture the files you modified *after* the sibling's commit (typically index.md and log.md). This is fine — but verify with `git show --stat <your-commit>` that all intended changes landed. If the sibling missed something (e.g., index.md), your commit covers it.
- **Pre-commit verification after parallel ingestion**: After a transcript ingestion that ran alongside sibling agents, run `git log --oneline -3` and `git show --stat HEAD` to confirm: (1) the transcript+summary files exist in a recent commit, (2) your commit captured the index/log updates, (3) no files are missing. This catches the case where both agents thought the other was handling a file.
- **Source-slug convention drift**: The naming convention says to use X handles (`willccbb`), but existing wiki files may use real names (`willbrown`, `kylecorbitt`). When ingesting follow-up lectures for an existing series, match the existing convention for that series rather than the global rule — consistency within a series matters more than strict adherence to the naming doc. Note the discrepancy for future cleanup.

## Companion Entity Page Creation During Transcript Ingestion

When the speaker doesn't have an existing entity page, create one as part of the ingestion batch. This is especially important for speakers at companies/products that will be cross-referenced later.

**Workflow**:
1. Before writing the transcript, check if `entities/<speaker-name>.md` exists
2. If not, create a concise entity page (background, role, key contributions, related wikilinks)
3. Add the entity to the transcript's `## Related` section and the summary article's links
4. Include the entity in the same git commit as the transcript

**Enrichment follow-up**: Transcript ingestion often reveals tools/products mentioned in the lecture that lack entity pages. After the initial commit, check for unlinked mentions (e.g., "W&B Weave", "CoreWeave") and offer to create those entities. The user may provide additional context (e.g., acquisition relationships) that enriches the entity graph.
- **Entity slug verification before creating wikilinks**: Before writing `[[entities/some-name]]` in a transcript or summary, verify the entity page exists with `search_files(pattern, target='files')`. If the speaker's name has a common spelling variant (e.g., `van-strien` vs `van-stien`), the actual filename is the source of truth. A typo in a wikilink creates a broken link that's hard to detect. Example: `daniel-van-strien.md` exists but the summary article linked to `daniel-van-stien` (missing 'r') — caught during post-commit review.
- **Patch tool `replace_all` on list items**: When using `replace_all=true` to fix a typo that appears in multiple list items (e.g., a misspelled entity name in `## Related`), the patch replaces ALL occurrences but may strip the list prefix (`- `) from subsequent matches. **Fix**: After using `replace_all`, immediately `read_file` the affected lines and verify each still has its `- ` prefix. If corrupted, do a second `patch` to restore the list formatting. Alternatively, use individual `patch` calls per occurrence to avoid this entirely.
- **Subagent auto-commit detection**: When `delegate_task` subagents create files (transcript, summary, VTT), they may commit them before the parent agent can `git add` them. Detection: `git status` shows "nothing to commit" for files you know were just created, and `git show --stat HEAD` reveals the subagent already committed them in a prior commit. **Impact**: Your `git add` of those files is a no-op, and your subsequent commit only captures index.md/log.md/entity updates. This is fine — but verify with `git show --stat HEAD` that all intended files landed.
- **Orphaned entity wikilinks during ingestion**: When creating a transcript's `## Related` section and companion article, you may discover that linked entity pages (e.g., `[[entities/weights-and-biases]]`) don't exist yet — other wiki pages already reference them as broken wikilinks. **Proactive approach**: Before writing the transcript, run `search_files` for the speaker's employer, key tools, and related organizations across `wiki/`. If references exist but no entity page does, create the entity page as part of the same ingestion batch. This prevents orphaned wikilinks from accumulating and ensures the transcript's cross-references are valid. Example: Ingesting Thomas Capelle's W&B talk → discovered `entities/weights-and-biases` was referenced in `alex-volkov.md` and `openai-neptune-acquisition.md` but had no page → created both `weights-and-biases.md` and `wandb-weave.md` as part of the same commit.
- **Sibling agent pre-commit blocks (content regression & language violations)**: When `git commit` is blocked by the pre-commit hook reporting content regression on files you didn't stage (e.g., `pytorch-fsdp.md` shrunk by a sibling cron job) or Japanese content in a new file from another agent, do NOT use `--no-verify`. Instead, selectively unstage the offending files: `git reset HEAD wiki/path/to/offending.md` then re-run `git commit`. Repeat if multiple sibling files are problematic. This preserves the pre-commit safety net for your own files while excluding unrelated sibling changes. Example sequence: (1) `git add wiki/` (2) commit blocked by pytorch-fsdp.md regression (3) `git reset HEAD wiki/concepts/pytorch-fsdp.md` (4) commit blocked by Japanese content in sibling's llm-as-policy.md (5) `git reset HEAD wiki/concepts/post-training/llm-as-policy.md` (6) commit succeeds.
- **Source-slug for multi-speaker sessions**: For office hours, panels, or guest lectures where the "author" is ambiguous (guest speaker vs course instructor vs platform), use the **course instructor's X handle** as source-slug — NOT the platform name and NOT the guest's handle. Rationale: the transcript belongs to the instructor's course series. Existing convention: Maven Agents MCP RL course uses `willbrown`/`kylecorbitt` (instructors), not `maven` or guest handles. Exception: if the guest is the primary lecturer (not a Q&A guest), use their handle.
- **index.md section count verification**: Before incrementing the `## Transcripts (N pages)` count in `index.md`, verify the actual number of transcript entries matches the current header. Sibling agents and parallel ingestion sessions can push the count out of sync. Quick check: `grep '^\- \[\[transcripts/' wiki/index.md | wc -l`. Fix the count to the real number rather than blindly adding 1.
