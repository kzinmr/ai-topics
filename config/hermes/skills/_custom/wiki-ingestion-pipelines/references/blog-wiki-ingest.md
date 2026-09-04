# Blog Wiki Ingest — Full Reference

Full procedure for the blog-wiki-ingest cron job (executes at 07:50 UTC, after blog-ingest → blog-triage).

## Pipeline Chain

```
blog-ingest (07:00 UTC) → blog-triage (07:30 UTC) → blog-wiki-ingest (07:50 UTC)
```

## Input Format

Triage checkpoint JSON at:

```
${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json
```

Structure (same as newsletter format):

```json
{
  "triage_timestamp": "2026-07-08T07:00:57Z",
  "run_id": "20260708T070014Z",
  "source": "blog-ingest",
  "decisions": [
    {
      "item_id": "blog-1",
      "title": "Title",
      "blog": "blog-domain.com",
      "raw_path": "/opt/data/ai-topics/wiki/raw/articles/...",
      "recommended_action": "take|reference|skip",
      "star_rating": 5,
      "target_pages": ["concepts/slug", "entities/slug"],
      "body_excerpt": "...",
      "reason_ja": "★★★..."
    }
  ],
  "summary": {"total_decisions": N, "takes": N, "references": N, "key_themes": [...]}
}
```

No noise filtering needed (unlike newsletter checkpoints) — blog articles are pre-extracted content files with `raw_path`. The `blog` field is the canonical source domain.

### ⚠️ Exception: takes with `raw_path: None` (unsaved_articles)

The general rule "blog articles always have `raw_path`" has one real exception: **public court-filing PDF takes** (see `references/blog-triage-2026-08-07-patterns.md`). The triage agent can rate an unsaved courtlistener PDF as ★★★★☆ `take` for an event page (validated Aug 7, 2026: OpenAI 28-page motion to dismiss Apple suit → `events/openai-apple-conflict-2026.md`). Such a decision has `raw_path: None` and NO extractable body file.

**Source handling for a `raw_path: None` take:**
- **Frontmatter `sources`**: add the external URL directly (e.g. `- https://storage.courtlistener.com/...pdf`) — there is no raw article file to reference
- **Body**: link to the external URL inline instead of a `[[raw/articles/...]]` wikilink
- **Content basis**: you cannot read a body file for this take — rely on the triage `body_excerpt` + the verifiable title/URL (a public court filing's title states a specific, checkable legal fact). Do NOT fabricate page-body detail beyond what the title/excerpt supports
- **Verification**: the "read raw_path body" step of take verification is skipped; instead confirm the target event page's timeline genuinely terminates before the filing date (the "fresh updated date ≠ full coverage" check) and patch the timeline row + a dated section

## Checkpoint States

### State A (ok=true): Normal — valid triage decisions at triage_latest.json
1. Read `triage_latest.json`
2. Filter to `recommended_action === "take"` decisions
3. Filter to `recommended_action === "reference"` decisions
4. Filter to `recommended_action === "skip"` decisions (archive only)

### State B (ok=false, output_path given, triage_latest.json valid): **Most Common** — ~5-10% failure rate
The blog-triage agent saved the checkpoint file before rendering its cron response. The `output_path` file exists but contains a failed response. The checkpoint JSON at `triage_latest.json` is valid and complete.

**Recovery**: Read `triage_latest.json` directly and proceed as State A. See `references/blog-triage-checkpoint-recovery.md` for detailed procedure.

### State C (ok=false, no triage_latest.json): Rare — complete failure
If the checkpoint file doesn't exist, fall back to scanning raw articles directly:
```bash
ls -lt ~/wiki/raw/articles/ | head -30
```
Perform triage from scratch. This is unusual — the blog-triage pipeline is more reliable than newsletter-triage.

## Categorizing Decisions by Action Required

Blog-wiki-ingest must triage not just `take` items but also `reference` items — because reference items with a `candidate_wiki_path` pointing to an entity page still need a reference entry written.

### Decision Matrix

| recommended_action | candidate_wiki_path target | Action required |
|---|---|---|
| take | concept page | Enrich/create the concept page with new content |
| take | entity page | Enrich the entity page with a new entry |
| reference | concept page | **No action** — concept already covers topic. The reference only adds a source URL, which is already in the page's `sources` frontmatter or visible in log.md |
| reference | entity page | **Add reference entry** — the entity page (author/company) needs a chronological entry documenting the article's framing and linking back to the concept page |
| reference | None/missing | **No action** — archival only |
| skip | any | Archive only — no wiki edits needed |

### Why Entity-Page Reference Items Need Action

Blog articles provide **individual author perspective** that concept pages don't capture. When Simon Willison writes about GPT-5.6, the concept page records the factual model data (pricing, benchmarks, API features). But the **entity page** (simon-willison.md) needs a chronological entry documenting Simon's assessment — his Cost per Pelican analysis, his SWE-Bench Pro skepticism, his hands-on coding impressions.

This is the blog pipeline's unique value vs the newsletter pipeline. Newsletter data fills concept pages; blog articles fill author entity pages.

**Test**: Does the entity page already have a July 2026 entry (or near the article's date) mentioning this article? If yes → skip. If no → add reference entry.

## Same-Day Pipeline Saturation Handling (CRITICAL)

**Context**: blog-wiki-ingest runs at 07:50 UTC, AFTER newsletter-wiki-ingest (07:40), sitemap-monitor (06:00), and raw-backlog-ingest (04:00). By the time blog-wiki-ingest executes, the newsletter pipeline may have already processed content about the same events.

**Expected outcome**: ~70% of blog triage "take" decisions may already be covered by other pipelines that ran earlier the same morning. This is NOT a bug — it's the normal result of a pipeline schedule where newsletter-ingest (07:10) → newsletter-triage (07:20) → newsletter-wiki-ingest (07:40) all run before blog-ingest (07:00) → blog-triage (07:30) → blog-wiki-ingest (07:50).

### Take Verification Procedure

For each `take` decision, check whether the target pages already contain the article's content:

1. **Check if `candidate_wiki_path` pages exist on disk**: `find ~/wiki/{entities,concepts} -name "*.md"`
2. **For exists pages**: Read the actual content, not just frontmatter. Look for:
   - The article's specific claims and data points in the body
   - Not just the article URL in the `sources` frontmatter list
   - Not just a "References" section with a bare URL
3. **Grep tooltip**: Use `find ... -name "*.md" | xargs grep -l "keyword"` for true filename discovery (not `search_files` with `target='files'` which searches content, not filenames)
4. **Check log.md for same-day processing**: `grep "2026-XX-XX" ~/wiki/log.md | grep -i "topic-keyword"` to find which pipeline processed the content

### Decision by Coverage Level

| Existing coverage | Action |
|---|---|
| Page exists with full content matching article's claims | **Skip take** — content already captured. Only enrich if `reference` with entity page candidate_wiki_path needs a reference entry |
| Page exists but only in references/sources, no substantive body | **Upgrade to enrichment** — the article adds genuine content. Use `patch` (never `write_file` for rich pages) |
| Page does not exist | **Create normally** — proceed with the take as the triage recommended |
| Page exists for umbrella topic but different specific content | **Enrich** — e.g., `concepts/microsoft-mai-models.md` covered MAI-Transcribe-1 but not MAI-Thinking-1. The concept page needs new model entries |

### Concrete Example (July 8, 2026)

Blog-triage produced 3 takes:
1. Merge.dev "LLM Gateways" → `comparisons/llm-gateways.md` already existed (54 lines, created by earlier pipeline)
2. Ed Zitron "Let AI Burn" → `concepts/ai-industry-economics.md` already had content with article as source
3. OpenAI AP+ case study → `entities/openai.md` already had AP+ case study section (lines 365-391)

All 3 takes verified as already covered by earlier pipelines (newsletter-wiki-ingest at 07:40 and prior runs).

## Reference Enrichment — Entity Page Chronological Entries

This is the core value-add of blog-wiki-ingest in a same-day-saturated pipeline. Blog articles provide the author's personal perspective — their hands-on assessment, their benchmark skepticism, their practical workflow tips — that newsletter-sourced concept pages don't capture.

### Reference Enrichment Pattern

1. **Identify actionable references**: Filter reference items where `candidate_wiki_path` points to an entity page (e.g., `entities/simon-willison.md`, `entities/sierra.md`)
2. **Group by target page**: Multiple reference items targeting the same entity page can be batched into one `patch` call
3. **Read existing target page**: Identify the correct insertion point (chronological section, e.g., "July 2026 Updates")
4. **Determine content from raw_path vs triage body_excerpt**: Read the raw article file to extract the author's unique perspective — the specific claims, numbers, opinions that are not already in the concept page
5. **Add cross-wikilink**: Include a `See [[concepts/topic]]` wikilink in the entity entry to connect the author's perspective to the broader concept
6. **One `patch` call per page**: Batch all entries for the same target page into a single patch

### Concrete Example (July 10, 2026)

Blog-triage produced 1 take + 3 references:

**Take**: Muse Spark 1.1 → `concepts/meta-muse-spark.md`
- **Verified**: Page existed (102 lines, April 2026 launch) but had NO Muse Spark 1.1 coverage → genuine gap
- **Enrichment**: Added Muse Spark 1.1 section (API, llm-meta-ai plugin, agentic tool calling, Attractor States in Self-Conversation)
- **Bonus fix**: Broken wikilinks in Related section (`-  — MSL leader` with no entity name) — fixed while enriching

**Reference (entity page)**: GPT-5.6 Simon Willison → `entities/simon-willison.md`
- **Why needed**: Concept page `concepts/gpt/gpt-5-6.md` already covered GA release details including Simon's assessment (line 119-120). But entity page had no July 9 entry — Simon's Cost per Pelican analysis, SWE-Bench Pro skepticism, and hands-on coding impressions were missing from the chronological record
- **Enrichment**: Added GPT-5.6 entry to July 2026 Updates section with Simon's unique framing

**Reference (entity page, bundled)**: Muse Spark 1.1 → `entities/simon-willison.md`
- Added alongside the GPT-5.6 entry in the same patch call — Simon built llm-meta-ai and published coverage
- Cross-wikilink: `See [[concepts/meta-muse-spark#Muse Spark 1.1 (July 2026)]]`

**Reference (concept page)**: ChatGPT Work GA via 9to5Mac → `concepts/gpt/gpt-5-6.md`
- **No action**: Concept page already had the content. The article was already in `sources` frontmatter

**Reference (entity page, already covered)**: Sierra AI-pilling → `entities/sierra.md`
- **No action**: Entity page already had comprehensive AI-pilling section (lines 118-134, 15 lines of bullet points)

### Subagent Context Template (for parallel enrichment)

```
Working on the ai-topics wiki at /opt/data/ai-topics/. You have read_file, patch, and terminal tools.
Use patch() with unique old_string matching. The page is at [path] ([N] lines).
Do NOT use write_file — only patch(). The page is rich (>40 lines) and must not be overwritten.
Add source references to frontmatter sources list if needed.
Do NOT touch the `updated` field unless the page has one (concept/event pages do; entity pages may not).
The old_string must include enough surrounding context to be unique.
```

Note: Entity pages (like `simon-willison.md`) typically have no global `updated` field in frontmatter — they organize by date sections. Only `patch`, never add an `updated` field to an entity page that doesn't have one.

### Typical Reference Yield

| Pipeline state | Expected references enricheable |
|---|---|
| All takes already handled | 3-6 reference enrichments possible |
| Some takes handled, some new | 2-4 reference enrichments (including 1-2 entity page entries) |
| All takes genuinely new (rare) | 1-3 reference enrichments |
| Takes + entity-page references (mixed) | 1 take enrichment + 1-2 entity page reference entries |

## Archive Handling

After enrichment, run archive_triage.py to save skip/reference decisions:
```bash
cd /opt/data/ai-topics && python3 scripts/archive_triage.py blog --keep-reference
```

Expected output:
```json
{"blog": {"ok": true, "message": "...", "archived": N}}
```

The archive may return "All items already archived (dedup)" if the triage pipeline already ran archive. This is normal — proceed with log/commit.

## Log Entry Format

> ⚠️ **COST_REPORT belongs in the cron-response text, NOT in `log.md`.** The `COST_REPORT:` tracking line is appended to the agent's final cron output (see the token-usage-tracking instruction in the job prompt). Do not paste it into the `log.md` entry — it is a non-wiki, non-source artifact and pollutes the append-only log. Keep the log entry to the standard bullet/section format only. (Observed Aug 2026: a `COST_REPORT:` line was accidentally written into `log.md` and had to be removed in a follow-up patch.)

### Takes + References (mixed case — most common for blog-wiki-ingest)

When there's 1 take + entity-page reference entries enriched:

```
## [2026-07-10] blog-wiki-ingest | Muse Spark 1.1 enrichment, Simon Willison GPT-5.6 reference

- **Source**: blog-triage checkpoint (Jul 10 07:37 UTC) — 11 articles triaged, 1 take, 3 reference, 7 skip
- **Recovery**: blog-triage output render failed; triage checkpoint recovered from `triage_latest.json` (per pipeline recovery pattern)
- **Pages enriched**:
  - `concepts/meta-muse-spark.md` — Added Muse Spark 1.1 section: first API release, llm-meta-ai plugin (Simon Willison), agentic tool calling/computer use improvements, Attractor States in Self-Conversation finding. Fixed broken wikilinks in Related section. Updated `updated` to 2026-07-10.
  - `entities/simon-willison.md` — Added July 9 GPT-5.6 hands-on assessment entry (pricing, Agents' Last Exam vs SWE-Bench Pro skepticism, Cost per Pelican). Added Muse Spark 1.1 coverage entry (llm-meta-ai plugin, cross-wikilink to concepts/meta-muse-spark).

**Decisions:** 1 take (Muse Spark 1.1 → concepts update), 3 reference, 7 skip
```

### All Takes Handled, Only References Enriched

When all takes are handled by other pipelines and only references were enriched:

```
## [2026-07-08] wiki: Blog-wiki-ingest — LLM gateways enrichment, reference items

**Blog triage recovered from checkpoint (N decisions: X takes, Y references, Z skips). All X takes already processed by other pipelines ([list pipelines]). Processed Y reference enrichments.**

**Pages updated:**
- entities/simon-willison.md — sqlite-utils 4.0 final release entry; github-code Web Component
- concepts/notion-mcp.md — Merge Agent Handler Notion MCP integration section
- concepts/apple.md — Siri iOS 27 beta 3 voice customization

**Archived:** N items (skip/reference)
```

## Git Workflow

```bash
cd /opt/data/ai-topics
git add wiki/
git commit -m 'wiki: blog-wiki-ingest - summary'
# If pre-commit hook blocks (unstaged changes from other agents):
# git stash; git pull --rebase; git stash pop
git pull --rebase  # may fail if other agents have unstaged changes — see stash pattern
git push
```

**Apostrophes in commit messages**: article titles frequently contain apostrophes ("Don't Be a Meat Proxy", "Don't Count Google Out"). Inside a single-quoted `-m '...'`, an apostrophe needs the `'"'"'` escape: `git commit -m 'wiki: ... "Don'"'"'t Count Google Out" ...'`. Simpler alternatives: drop the apostrophe from the summary, or use double quotes for the message when the title has no double quotes inside. Validated Aug 7, 2026 (blog-wiki-ingest commit ddca2b21).

For the stash pattern when `git pull --rebase` fails with "cannot pull with rebase: You have unstaged changes":
```bash
git stash         # save other agents' unstaged changes
git pull --rebase # pull remote changes
git push          # push your commit
git stash pop     # restore other agents' changes
```

### ⚠️ Cross-Pipeline Git Staging (Parallel Pipeline Window)

In the 07:00–07:50 UTC window, blog-ingest, newsletter-ingest, sitemap-monitor, and raw-backlog-ingest are all running concurrently. Other pipeline sessions may leave **unstaged changes in `config/hermes/`** (cron job config updates, skill inventory changes) and **untracked files in `inbox/` and `raw/`**.

Using `git add wiki/` attempts to stage ALL modified files — including those from other pipelines. The staging itself succeeds, but the subsequent `git pull --rebase` fails (rebase requires a clean working tree) and the commit includes unrelated changes that shouldn't be in your wiki commit.

**Alternative staging approach for parallel pipeline windows:**

```bash
# Stage only the wiki files YOU changed — not everything in wiki/
cd /opt/data/ai-topics

# Option A: Add specific entity/concept pages + index + log
git add wiki/entities/fable.md wiki/entities/hyperbo.md wiki/entities/seangoedecke-com.md wiki/index.md wiki/log.md

# Option B: If you also changed SCHEMA.md (tag taxonomy addition)
git add wiki/SCHEMA.md wiki/entities/hyperbo.md wiki/entities/fable.md wiki/entities/seangoedecke-com.md wiki/index.md wiki/log.md

# Option C: Use git status --short to identify only your changed files
# Look for files matching "M wiki/entities/" or "M wiki/concepts/" or "M wiki/index.md" or "M wiki/log.md"
# Do NOT add "M config/" or "?? inbox/" files

# Then commit (pre-commit hooks will validate wiki/ files) and push:
git commit -m 'wiki: blog-wiki-ingest - <summary>'
git push  # skip pull --rebase entirely; your commit is the only local change
```

**Why skip `git pull --rebase`?** In a cron pipeline where you are the only session writing to the wiki repo, your commit is always a clean fast-forward. The pull-rebase only matters if another wiki-writing pipeline committed first (possible if newsletter-wiki-ingest at 07:40 committed minutes before). If `git push` fails with a non-fast-forward error, THEN fall back to pull-rebase:

```bash
git pull --rebase  # only if push fails with non-fast-forward
git push
```

**Validated**: July 18, 2026 — `git add` with specific files + `git commit` + `git push` succeeded after `git pull --rebase` failed due to config/hermes/ changes from other concurrent pipeline sessions.

**Pre-commit hook note**: When staging specific files, the pre-commit hook still validates ALL staged files' tags against SCHEMA.md. If you added a new tag (e.g., `agent-engineering`), stage SCHEMA.md alongside the entity page for a clean validation pass.

## Validated Runs

| Date | Takes handled | References enriched | Skips | Recovery path |
|---|---|---|---|---|
| 2026-07-08 | 3/3 (newsletter + prior) | 4 (simon-willison, notion-mcp, apple, ai-governance-political-pressure) | 10 | Checkpoint recovery (State B) |
| 2026-07-10 | 1/1 (Muse Spark 1.1 enrichment) | 2 entity-page entries (simon-willison GPT-5.6 + Muse 1.1 refs) + 2 no-action refs | 7 | Checkpoint recovery (State B) |
| 2026-07-17 | 1/1 (Kimi K3 concept) | 2 entity-page entries (simon-willison 6 entries, codex $HOME bug) | 7 | Full-pipeline (State D) |
| 2026-08-07 | 3/3 (gary-marcus Google thesis, seangoedecke keep-thinking, OpenAI-Apple motion-to-dismiss event page) | 2 entity-page entries (simon-willison datasette 1.0a38 SQLi + Technical Blogging) | 15 | Checkpoint recovery (State B); court-filing PDF take with `raw_path: None` (external URL in sources); archive already saved by triage → dedup 0 |

## Blog-Ingest Full-Pipeline Pattern (State D)

When the blog-ingest cron job (07:00 UTC) receives a script output with `saved_articles` containing `raw_path` values, the agent can perform triage + wiki updates in the same session — bypassing the separate blog-triage (07:30) and blog-wiki-ingest (07:50) jobs.

**Trigger**: Script output includes `saved_articles` array with `raw_path` entries AND `articles.blog_articles` with titles/URLs.

**Procedure**:
1. Read each `saved_articles[].raw_path` to assess AI relevance
2. Triage: classify as take (AI-relevant, needs wiki page), reference (enriches existing page), or skip (non-AI)
3. For takes: create concept pages or enrich existing pages
4. For references: add entries to entity pages (author perspective) or concept pages
5. Update `log.md` and `index.md`
6. Commit and push

**Advantage**: Eliminates 50-minute delay between article collection (07:00) and wiki updates (07:50). Useful when the agent has high confidence in triage decisions.

**Limitation**: No `triage_latest.json` checkpoint is produced — the triage decisions exist only in the agent's session. If the session fails, triage work is lost. The separate blog-triage job produces a durable checkpoint.

## Subagent Summary Verification Pitfall (CRITICAL)

When using `delegate_task` for parallel wiki updates, **always verify actual file contents after completion**. Subagent summaries can be misleading:

- **Observed pattern**: Task 2 (Simon Willison entity update) returned a summary mentioning "hermes-agent" and "radiko-wiki-sync" — completely unrelated to the actual work. However, reading the file confirmed all 6 entries were correctly added.
- **Root cause**: Subagent's summary generation can pick up injected context (AGENTS.md, skill descriptions) instead of summarizing the actual edits.
- **Verification**: After all subagents complete, `read_file` on each modified page to confirm edits are present. Do not trust the summary text.
- **Recovery**: If a subagent's summary looks wrong but the file is correct, proceed normally. If the file is NOT updated, re-run the edit manually.
