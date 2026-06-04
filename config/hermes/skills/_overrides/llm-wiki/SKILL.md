---
name: llm-wiki
description: "Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency."
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wiki, knowledge-base, research, notes, markdown, rag-alternative]
    category: research
    related_skills: [obsidian, arxiv, agentic-research-ideas]
    config:
      - key: wiki.path
        description: Path to the LLM Wiki knowledge base directory
        default: "~/wiki"
        prompt: Wiki directory path
---

# Karpathy's LLM Wiki

Build and maintain a persistent, compounding knowledge base as interlinked markdown files.
Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki
compiles knowledge once and keeps it current. Cross-references are already there.
Contradictions have already been flagged. Synthesis reflects everything ingested.

**Division of labor:** The human curates sources and directs analysis. The agent
summarizes, cross-references, files, and maintains consistency.

## When This Skill Activates

Use this skill when the user:
- Asks to create, build, or start a wiki or knowledge base
- Asks to ingest, add, or process a source into their wiki
- Asks a question and an existing wiki is present at the configured path
- Asks to write a blog post, essay, or analysis drawing from their wiki knowledge
- Asks to lint, audit, or health-check their wiki
- References their wiki, knowledge base, or "notes" in a research context
- Runs as a scheduled active-crawl cron job to discover and fill knowledge gaps

## Wiki Location

Configured via `skills.config.wiki.path` in `~/.hermes/config.yaml` (prompted
during `hermes config migrate` or `hermes setup`):

```yaml
skills:
  config:
    wiki:
      path: ~/wiki
```

Falls back to `~/wiki` by default, and in this environment `~/wiki` should
resolve to `~/ai-topics/wiki`. Do not silently switch to any alternate location. The resolved path is injected when this
skill loads — check the `[Skill config: ...]` block above for the active value.

The wiki is just a directory of markdown files — open it in Obsidian, VS Code, or
any editor. No database, no special tooling required.

## Architecture: Three Layers

```
wiki/
├── SCHEMA.md           # Conventions, structure rules, domain config
├── index.md            # Sectioned content catalog with one-line summaries
├── log.md              # Chronological action log (append-only, rotated yearly)
├── raw/                # Layer 1: Immutable source material
│   ├── articles/       # Web articles, clippings
│   ├── papers/         # PDFs, arxiv papers
│   ├── transcripts/    # Meeting notes, interviews
│   └── assets/         # Images, diagrams referenced by sources
├── entities/           # Layer 2: Entity pages (people, orgs, products, models)
├── concepts/           # Layer 2: Concept/topic pages
├── comparisons/        # Layer 2: Side-by-side analyses
├── queries/            # Layer 2: Filed query results worth keeping
└── events/             # Layer 2: Time-bounded events (launches, incidents, announcements)
```

**Layer 1 — Raw Sources:** Immutable. The agent reads but never modifies these.
**Layer 2 — The Wiki:** Agent-owned markdown files. Created, updated, and
cross-referenced by the agent.

### Subdirectory Pattern for Complex Topics

When a topic grows beyond 5-10 concept pages, organize into a subdirectory with a synthesis index:

```
wiki/concepts/
├── agentic-engineering.md        # Parent overview page (brief)
├── agentic-engineering/          # Subdirectory for deep dives
│   ├── _index.md                 # Cross-leader synthesis hub
│   ├── red-green-tdd.md
│   ├── first-run-the-tests.md
│   └── using-git-with-agents.md
└── other-concept.md
```

The `_index.md` synthesizes perspectives from multiple opinion leaders on the shared topic,
mapping convergences, divergences, and unresolved questions. Use the `cross-leader-synthesis`
skill for this pattern.

**Rules:**
- `_index.md` is the entry point — always read it first for a topic overview
- Parent page (`agentic-engineering.md`) stays as a brief definition + links to subdirectory
- Each concept page in the subdirectory links back to `_index.md`
- `_index.md` links to each leader's entity page via `[[wikilinks]]`
**Layer 3 — The Schema:** `SCHEMA.md` defines structure, conventions, and tag taxonomy.

## Resuming an Existing Wiki (CRITICAL — do this every session)

When the user has an existing wiki, **always orient yourself before doing anything**:

① **Read `SCHEMA.md`** — understand the domain, conventions, and tag taxonomy.
② **Read `index.md`** — learn what pages exist and their summaries.
③ **Scan recent `log.md`** — read the last 20-30 entries to understand recent activity.

```bash
WIKI="${wiki_path:-$HOME/wiki}"
# Orientation reads at session start
read_file "$WIKI/SCHEMA.md"
read_file "$WIKI/index.md"
read_file "$WIKI/log.md" offset=<last 30 lines>
```

Only after orientation should you ingest, query, or lint. This prevents:
- Creating duplicate pages for entities that already exist
- Missing cross-references to existing content
- Contradicting the schema's conventions
- Repeating work already logged

For large wikis (100+ pages), also run a quick `search_files` for the topic
at hand before creating anything new.

## Initializing a New Wiki

When the user asks to create or start a wiki:

1. Determine the wiki path (from config, env var, or ask the user; default `~/wiki`)
2. Create the directory structure above
3. Ask the user what domain the wiki covers — be specific
4. Write `SCHEMA.md` customized to the domain (see template below)
5. Write initial `index.md` with sectioned header
6. Write initial `log.md` with creation entry
7. Confirm the wiki is ready and suggest first sources to ingest

### SCHEMA.md Template

Adapt to the user's domain. The schema constrains agent behavior and ensures consistency:

```markdown
# Wiki Schema

## Domain
[What this wiki covers — e.g., "AI/ML research", "personal health", "startup intelligence"]

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

## Frontmatter
  ```yaml
  ---
  title: Page Title
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary
  tags: [from taxonomy below]
  sources: [raw/articles/source-name.md]
  ---
  ```

**Required fields:** `title`, `created`, `updated`, `type`, `tags`, `sources`. Omitting `sources` is the most common frontmatter gap at scale — if you have no source to cite, use `sources: []`.

## Tag Taxonomy
[Define 10-20 top-level tags for the domain. Add new tags here BEFORE using them.]

Example for AI/ML:
- Models: model, architecture, benchmark, training
- People/Orgs: person, company, lab, open-source
- Techniques: optimization, fine-tuning, inference, alignment, data
- Meta: comparison, timeline, controversy, prediction

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed,
add it here first, then use it. This prevents tag sprawl.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
```

### index.md Template

The index is sectioned by type. Each entry is one line: wikilink + summary.

```markdown
# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: YYYY-MM-DD | Total pages: N

## Entities
<!-- Alphabetical within section -->

## Concepts

## Comparisons

## Queries

## Events
```

**Events section:** Time-bounded happenings (product launches, security incidents, funding announcements). Use `type: event` in frontmatter. These are distinct from `concept` pages which capture enduring knowledge.

**Scaling rule:** When any section exceeds 50 entries, split it into sub-sections
by first letter or sub-domain. When the index exceeds 200 entries total, create
a `_meta/topic-map.md` that groups pages by theme for faster navigation.

### log.md Template

```markdown
# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, translate, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [YYYY-MM-DD] create | Wiki initialized
- Domain: [domain]
- Structure created with SCHEMA.md, index.md, log.md
```

**Log rotation**: When `log.md` exceeds 500 lines, archive it as `log-YYYY.md` and create a fresh file with the header + rotation entry. See `wiki-graph-health` skill's `references/log-rotation.md` for the full procedure.

## Core Operations

### 1. Ingest

When the user provides a source (URL, file, paste), integrate it into the wiki:

① **Capture the raw source:**
   - URL → use `web_extract` to get markdown, save to `raw/articles/`
   - PDF → use `web_extract` (handles PDFs), save to `raw/papers/`
   - Pasted text → save to appropriate `raw/` subdirectory
   - Name the file descriptively: `raw/articles/karpathy-llm-wiki-2026.md`
   - **Single-page research collections**: When a research listing page shows post
     summaries but all individual post URLs return 404, extract the listing as a
     single source and supplement with GitHub repos, HuggingFace blogs, and X posts.
     See `references/single-page-research-collections.md` for full procedure.

② **Discuss takeaways** with the user — what's interesting, what matters for
   the domain. (Skip this in automated/cron contexts — proceed directly.)

③ **Check what already exists** — search index.md and use `search_files` to find
   existing pages for mentioned entities/concepts. This is the difference between
   a growing wiki and a pile of duplicates.

④ **Write or update wiki pages:**
   - **New entities/concepts:** Create pages only if they meet the Page Thresholds
     in SCHEMA.md (2+ source mentions, or central to one source)
   - **Existing pages:** Add new information, update facts, bump `updated` date.
     When new info contradicts existing content, follow the Update Policy.
   - **Sources:** ⚠️ SOURCES GATE — Every page MUST have a `sources:` frontmatter field. For raw article ingestion: `sources: [raw/articles/<filename>]`. For web extraction: list the URLs. If unsure, use `sources: []` — never omit the field entirely.
   - **Cross-reference:** Every new or updated page must link to at least 2 other
     pages via `[[wikilinks]]`. Check that existing pages link back.
   - **Tags:** ⚠️ TAG GATE — Before writing any page, read `wiki/SCHEMA.md` and ensure ALL tags come from its taxonomy. If you need a new tag, add it to SCHEMA.md FIRST. Never use ad-hoc or composite kebab-case tags. Violations are blocked by pre-commit hook.
   - **Sources:** ⚠️ SOURCES GATE — Every page MUST have a `sources:` frontmatter field. For raw article ingestion: `sources: [raw/articles/<filename>]`. For web extraction: list the URLs. If unsure, use `sources: []` — never omit the field entirely.

⑤ **Update navigation:**
   - Add new pages to `index.md` under the correct section, alphabetically
   - Update the "Total pages" count and "Last updated" date in index header
   - Append to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`
   - List every file created or updated in the log entry

⑥ **Report what changed** — list every file created or updated to the user.

A single source can trigger updates across 5-15 wiki pages. This is normal
and desired — it's the compounding effect.

### 6. JP→EN Translation Batch (Bilingual Wiki Maintenance)

When the wiki has Japanese-language content that needs systematic English translation,
run the batch workflow documented in `references/jp-en-translation-batch.md`:

1. **Scan and rank** — walk all non-raw `.md` files, count JP chars in body (after frontmatter)
2. **Select top N** — recommend 8 files per batch (~30K JP chars). Exclude `log.md`/`log-2026.md`.
3. **Choose translation method by file type** — Three translation approaches, each suited to a different file structure:

   | File Type | Best Approach | When It Works | When It Fails |
   |-----------|--------------|---------------|---------------|
   | **Fully-JP concept/entity** (<200 lines, >90% JP in body) | Full body rewrite via `write_file` or `execute_code` (Python triple-quoted strings) | Coherent JP paragraphs that translate cleanly to one block | Multi-section files where EN/JP boundaries are ambiguous |
   | **Scattered-JP** (mostly EN, JP in 10+ locations: headers, table cells, inline text) | `delegate_task` subagent with context-aware translation instructions | Files with scattered JP where context matters for accurate translation (log files, index files) | Fully-JP files >500 lines where subagent hits token limits |
   | **Light scattered-JP** (JP in <10 specific locations) | Per-file `str.replace()` dict via `execute_code` | Known replacement strings in fixed positions (section headers, table column headers) | Files where replacement strings have whitespace mismatches or Unicode-variant characters |

   **⚠️ Chinese vs Japanese CJK characters**: When scanning for Japanese content, the regex `[\u4E00-\u9FFF]` captures both Chinese characters (漢字) and Japanese kanji. Many wiki files contain Chinese proper nouns (person names like 姚顺雨, organization names like 智谱AI, 月之暗面, product names). These are NOT Japanese and should be preserved. Use the hiragana/katakana-only regex `[\u3040-\u309F\u30A0-\u30FF]` to identify translatable Japanese text. See `references/chinese-proper-noun-handling.md` for the verification script and detailed handling procedure. When a scan reports "CJK characters," verify whether they're Chinese proper nouns before attempting translation.

   **⚠️ str.replace() has fundamental limits for scattered JP** — A replacement dict with 200+ entries may only remove 15-30% of JP chars per pass on log files with scattered JP. The silent non-match rate is high because JP particles (の, を, へ) appear in many different contexts. After 3 aggressive passes with 400+ total replacement entries, ~60% of scattered JP remained. **Delegate_task subagents** are dramatically more effective for this case — each subagent can understand context and properly translate scattered JP in a single pass. Tested on a 1732-line log file with 4,015 JP chars: str.replace() removed 670 over 3 passes; one subagent pass removed the remaining 3,345 with context-aware translation.

   **When to use which approach in a batch:** Split the 8 files into groups:
   - Concept/entity files (small, coherent JP body) → `execute_code` with full body rewrites
   - Log files or large files with scattered JP → `delegate_task` (1 subagent per file, up to 3 in parallel)
   - This prevents str.replace() frustration on scattered-JP files while keeping concept files fast
   - **Proven in production**: The 2026-05-27 batch (8 files, ~7,362 JP chars) used this split: 5 concept files via `execute_code` (full rewrite), 3 log files via `delegate_task` (scattered-JP translation). All 8 achieved 0 residual JP.

   **⚠️ Fullwidth colon trap**: After translation, 6 remaining "JP chars" in a 1732-line file turned out to be fullwidth colons `：` (U+FF1A) — CJK punctuation, not Japanese language content. These appear in log entries, table headers, and inline descriptions. Always include a `content.replace('\uff1a', ':')` step in the final cleanup pass. Also check for fullwidth semicolons `；` (U+FF1B).

   **⚠️ Never use `assert new_jp == 0` in batch scripts** — an assertion on file #4 kills the entire batch, losing progress on files #1-3 and requiring differential recovery for files #5-8. Use print+continue instead (see `references/jp-en-translation-batch.md` → Principle 1).
   **⚠️ Split fully-JP files into a separate batch from mixed JP/EN files** — they have fundamentally different failure modes (full rewrite vs per-string match). Each batch type gets isolated debugging (see `references/jp-en-translation-batch.md` → Principle 2).
   **⚠️ Quote-escaping trap**: `str.replace()` values containing apostrophes (`'s` possessives) break single-quoted Python strings. Writing the script to a temp file (instead of `terminal("python3 -c ...")`) only bypasses bash backtick substitution — Python single-quote conflicts remain. Two fixes:

   a. **Use `\u2019` (Unicode right single quotation mark)** for apostrophes: `'NVIDIA\u2019s inference'` avoids the conflict entirely.
   b. **Use triple-quoted Python strings** (`"""..."""`) for `str.replace()` values so single quotes inside are parsed as literal characters.
   c. **Escape with `\'`** inside single-quoted strings: `'NVIDIA\\'s inference'` — works but requires backslash-escaped quotes which hurt readability.

   Commit both approaches as habits: write complex scripts to `/tmp/` via `write_file`, AND use `\u2019` or triple-quoted strings for any line containing apostrophes.
   **⚠️ Multi-line replace trap**: A `str.replace()` with `\n\n` between heading and body can silently fail due to subtle whitespace differences. Use shorter, line-by-line `str.replace()` calls instead of multi-line spans. Debug with `repr()` on the target content to find exact characters.
   See pitfalls in `references/jp-en-translation-batch.md` for details.
4. **Process simplest to most complex** — fewer JP chars first, index pages last.
5. **Log via `execute_code`** with header/chrono splitting (never `f.write(new_entry + content)`).

See `references/jp-en-translation-batch.md` for the complete workflow, scan script, and pitfalls.

### 2. Query

When the user asks a question about the wiki's domain:

① **Read `index.md`** to identify relevant pages.
② **For wikis with 100+ pages**, also `search_files` across all `.md` files
   for key terms — the index alone may miss relevant content.
③ **Read the relevant pages** using `read_file`.
④ **Synthesize an answer** from the compiled knowledge. Cite the wiki pages
   you drew from: "Based on [[page-a]] and [[page-b]]..."
⑤ **File valuable answers back** — if the answer is a substantial comparison,
   deep dive, or novel synthesis, create a page in `queries/` or `comparisons/`.
   Don't file trivial lookups — only answers that would be painful to re-derive.

> **Karpathy's insight**: *"Good answers can be filed back into the wiki as new pages. A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do."* This is the philosophical foundation for why queries belong in the wiki, not just in chat history.

**Query page format** — see `references/query-page-format.md` for the full template. Key elements:
- Question metadata block (question, questioner, date, channel, answer summary)
- Structured answer with tables and cross-references to wiki pages
- Conclusion with concrete recommendations
- Unresolved questions / open issues section
- Cross-reference to the wiki-wide concept the answer draws from (e.g., Karpathy's insight)

**Creating the first query page**: If `wiki/queries/` doesn't exist yet, create it with `mkdir -p`. The index.md's Queries section will say `> No queries filed yet.` — replace this with the first entry. Subsequent queries get inserted alphabetically.

⑥ **Update log.md** with the query and whether it was filed.

### 3. Lint

When the user asks to lint, health-check, or audit the wiki:

① **Orphan pages:** Find pages with no inbound `[[wikilinks]]` from other pages.
```python
# Use execute_code for this — programmatic scan across all wiki pages
import os, re
from collections import defaultdict
wiki = "<WIKI_PATH>"
# Scan all .md files in entities/, concepts/, comparisons/, queries/
# Extract all [[wikilinks]] — build inbound link map
# Pages with zero inbound links are orphans
```

② **Broken wikilinks:** Find `[[links]]` that point to pages that don't exist.

③ **Index completeness:** Every wiki page should appear in `index.md`. Compare
   the filesystem against index entries.

④ **Frontmatter validation:** Every wiki page must have all required fields
   (title, created, updated, type, tags, sources). Tags must be in the taxonomy.

⑤ **Stale content:** Pages whose `updated` date is >90 days older than the most
   recent source that mentions the same entities.

⑥ **Contradictions:** Pages on the same topic with conflicting claims. Look for
   pages that share tags/entities but state different facts.

⑦ **Page size:** Flag pages over 200 lines — candidates for splitting.

⑧ **Tag audit:** List all tags in use, flag any not in the SCHEMA.md taxonomy.

⑨ **Log rotation:** If log.md exceeds 500 entries, rotate it.

⑩ **Report findings** with specific file paths and suggested actions, grouped by
   severity (broken links > orphans > stale content > style issues).

⑪ **Append to log.md:** `## [YYYY-MM-DD] lint | N issues found`

### Article Scanning & Prioritization Pipeline

When facing a large backlog of articles (500+) to potentially ingest:

1. **Scan all articles** using `blogwatcher-cli articles` or equivalent
2. **Parse into structured data** (blog, title, URL, date) using execute_code
3. **Score by priority:**
   - Priority blogs (simonwillison.net, antirez.com, paulgraham.com, etc.): +10
   - AI-relevant keywords in title (llm, agent, coding, model, inference, etc.): +1 per match
   - Recency bonus: +1 per day within last 5 days
4. **Filter threshold:** score >= 10 for direct Wiki creation, score 5-9 for reference, score < 5 skip
5. **Process in batches** of 5 articles per delegate_task with max_iterations >= 20
6. **CRITICAL: verify files exist** after delegate_task completes before claiming success:
   ```bash
   search_files "new-page-name.md" path="$WIKI" target="files"
   ```
7. **Update index.md and log.md** in the same session after verification

### 5. Synthesize (Original Content Creation)

When the user asks to write original content (blog posts, essays, analyses, opinion pieces)
sourced primarily from the wiki knowledge base:

① **Search the wiki thoroughly** — use `search_files` across `concepts/`, `entities/`,
   `comparisons/`, and `raw/articles/` for the topic and related terms. Cast a wide net
   initially; narrow after you see what's available.

② **Read the key pages in depth** — prioritize concept pages with high cross-reference
   density and entity pages with documented philosophies. Don't skim — the best
   synthesis comes from deeply understanding a few sources, not shallowly scanning many.

③ **Supplement with web search** — only when wiki knowledge is thin or you need a
   specific external claim to bolster an argument. Prefer authoritative sources
   (arXiv papers, company blogs, recognized thought leaders). Cite these alongside
   wiki sources.

④ **Compose the essay** — write in the user's language. Match the requested tone
   (lively/活き活き, academic, conversational, provocative). Structure as a narrative
   journey: thesis → evidence → counterpoint → synthesis. Quote primary sources
   directly where they're vivid or iconic.

⑤ **Cite everything** — every major claim needs a source. Wiki pages get `[[wikilinks]]`,
   external URLs get inline links. Distinguish between the author's words and your analysis.
   For a wiki-sourced essay, the ratio should be ~70% wiki + ~30% external/web.

⑥ **Save as a raw article** — use `wiki/raw/articles/` with the pattern
   `YYYY-MM-DD_hermes_{topic-slug}.md` for original content. Include YAML frontmatter
   with `title`, `date`, `author: Hermes (kzinmr's AI Topics)`, `tags`, and `sources`
   (listing both wiki pages and external URLs).

⑦ **Update log.md** with the new article, key sources referenced, and a brief summary.
   Commit and push.

**Quality guidelines:**
- **Depth over breadth**: 3-4 well-explored arguments > 10 shallow mentions
- **Concrete examples**: Abstract claims need specific instances (model names, papers, experiments)
- **Narrative arc**: Open with the core tension, build through evidence, close with synthesis
- **Quotable quotes**: Direct quotes from Gwern, Chung, Sutton, etc. make the essay vivid
- **User language**: Write in the language the user used to make the request

**When NOT to synthesize:**
- The topic is peripheral to the wiki domain → redirect the user
- The wiki has < 3 relevant pages → web search first, note thin coverage
- The user wants a factual report, not an essay → use Query mode instead

### 4. Active Crawl (Proactive Gap Discovery)

When running as a scheduled cron job to discover and fill knowledge gaps
(no user-provided sources):

① **Research trending topics** — use `web_search` to find recent AI/ML announcements,
   arXiv papers (peer-reviewed only), and official blog posts from major labs.
   Target 3-5 topics the wiki likely hasn't covered.

② **Cross-reference against the wiki** — use `execute_code` to check which
   topics already have pages. Run the full pattern from `references/cross-reference-check.md`
   (candidate list → `os.walk()` scan → sorted FOUND/MISSING report with counts and paths).
   **Additional check:** after the filesystem scan, grep `index.md` for near-matches of
   each MISSING candidate's core slug (e.g., search `nvidia-nemotron` for candidate
   `nvidia-nemotron-3`). The index may list a canonical full name like
   `nvidia-nemotron-3-nano-omni` that your simplified candidate slug won't match on
   `os.path.exists()`. This prevents creating duplicate pages with different slugs
   for the same entity.

③ **Extract original sources** — use `web_extract` on official sources (company blogs,
   arXiv abstracts, tech reports). Pass all URLs in a single `web_extract` call to batch-fetch.
   Skip aggregator sites and second-hand summaries. If `web_extract` returns truncated content
   with "LLM summarization timed out", use `browser_navigate` on those URLs individually
   as a fallback — it produces full text snapshots including all paragraphs, lists, and quotes.
   Note: paywalled sources (Fortune, beehiiv, some NYT) may return sparse content —
   cross-reference with alternative sources.

④ **Save raw articles** first — `write_file` to `wiki/raw/articles/` with descriptive
   names (`YYYY-MM-DD_source-topic.md`).

⑤ **Create wiki pages** — batch the creations. Each page must have: frontmatter,
   4-6 cross-references, tags from the SCHEMA.md taxonomy.
   **⚠️ Cross-reference pre-flight**: After writing all pages, verify ALL `[[wikilinks]]`
   in new pages resolve to actual files BEFORE committing. Run the verification script
   from `references/cross-reference-prefight.md` and `patch` any broken links immediately.
   This avoids the common "commit → lint finds broken links → patch cycle" that costs
   3-4 extra tool calls per broken link.

⑥ **Update navigation** — use `patch` to insert new index entries alphabetically
   (see "Patch-based index insertion" below). Update section counts and total pages.

⑦ **Validate tags before commit** — Before `git commit`, verify ALL tags in ALL new/updated pages exist in SCHEMA.md. The pre-commit hook will catch violations, but catching them proactively avoids a blocked commit and retry cycle. Use this checklist:

   **Predict the violations (active-crawl specific):** The #1 cause of tag violations in active-crawl is **new company/product names** used as tags. When you create entity pages for newly discovered companies/products (Cohere, Stability AI, Antigravity, etc.), those names MUST be in SCHEMA.md's People/Orgs or Products categories. Before writing any page, scan your planned tags for company/product identifiers and check whether SCHEMA.md already lists them. If not, add them to the relevant category line FIRST, then write the page with those tags.

   **General checklist:**
   **General checklist:**
   - After writing all pages, scan each page's `tags:` line with a mental check against SCHEMA.md categories
   - Company/product tags (cohere, stability-ai, antigravity, kubernetes, etc.) → add to People/Orgs, Products, or Infrastructure BEFORE committing
   - Domain-neutral tags you assumed existed (e.g., `music`, `typescript`) → check SCHEMA.md; if missing, either add or replace with existing near-equivalent (`audio-generation`, `developer-tooling`)
   - Batch all SCHEMA.md tag additions with `patch` calls on the relevant category lines
   - Then `git add wiki/` and commit. If the hook still blocks, check the error output for ALL offending files (not just yours — pre-existing staged violations from other pipelines also block)

⑧ **Log and commit** — single log entry covering the batch, commit + push.

### Patch-Based Index Insertion

For large index.md files (500+ lines), use `patch` with `old_string`/`new_string`
to insert new entries alphabetically rather than reading the entire file.

#### Alternative: Bulk str.replace() via execute_code (10+ changes)

When making **10+ index changes** (insertions + description updates), a single `execute_code` call with `str.replace()` across all updates can be more efficient than issuing 10+ individual `patch` calls:

```python
with open(index_path) as f:
    content = f.read()

# Read exact full lines BEFORE writing code
old = '- [[entities/daytona-io]] — old summary...'
new = '- [[entities/daytona-io]] — new summary with podcast details...'
content = content.replace(old, new)

# For insertions, use a 2-line anchor (line before + line after)
old_anchor = '- [[entities/evanhahn-com]] — **Blog** | evanhahn.com |\n- [[entities/fabiensanglard-net]] — **Blog** | fabiensanglard.net |'
new_with_insert = '- [[entities/evanhahn-com]] — **Blog** | evanhahn.com |\n- [[entities/exa]] — New entry summary...\n- [[entities/fabiensanglard-net]] — **Blog** | fabiensanglard.net |'
content = content.replace(old_anchor, new_with_insert)

with open(index_path, 'w') as f:
    f.write(content)
```

**CRITICAL - Anchor string accuracy**: Every `old_string` anchor MUST be the **exact full line** as it appears in the file — no truncation, no abbreviation. A common failure mode is using a shortened anchor (e.g., stopping at the first sentence of a multi-sentence line), which silently fails to match. Read the exact lines with `read_file(offset=N, limit=5)` before writing the `str.replace()` code. If an anchor doesn't match:
1. The str.replace silently does nothing for that entry
2. Verify with `if old in content: print("OK") else: print("FAIL")` for each replacement
3. Re-read the target lines to get the exact content and retry

**When to use which approach**:
- **1-4 index changes**: Use individual `patch` calls (atomic, explicit, easy to verify)
- **5+ index changes**: Use `execute_code` with `str.replace()` (fewer tool calls, batch-verifiable)
- Both approaches require reading exact lines first — never guess what the anchor text looks like

**CRITICAL: Do NOT compute insertion points programmatically.** The index at scale
is NOT strictly alphabetical — entries drift over time as different agents and
pipelines add content. A programmatic "find first alphabetical successor" algorithm
will almost always place entries in the wrong position, creating duplicates that
require cleanup. Instead, use `read_file` with the target offset to visually
confirm the 2-3 surrounding lines, then use those exact lines as the `old_string`
anchor.

**Discovery step (do this first):** Read the relevant section of `index.md` with
`read_file(offset=N, limit=20)` to find the exact anchor lines. Do NOT use
`execute_code` with `os.walk()` or regex-based successor computation — it will
place entries incorrectly in non-alphabetical sections. See
`references/index-insertion-discovery.md` for the full pattern and failure cases.

```
# Instead of read_file + edit + write_file:
patch(
    old_string="- [[entities/gemini]] — summary...\n- [[entities/gemma-4]] — summary...",
    new_string="- [[entities/gemini]] — summary...\n- [[entities/gemini-enterprise-agent-platform]] — ...\n- [[entities/gemma-4]] — summary...",
    path="~/wiki/index.md"
)
```

Use 2-3 surrounding lines as the `old_string` anchor to ensure uniqueness.
Also update the header counts and section counts with separate `patch` calls.

**Advantages over read+write:**
- No line-number prefixes to accidentally paste into the file
- Minimal token cost (only the changed lines)
- Atomic — either the match succeeds or nothing changes
- Works for 1500+ line files without loading the whole thing

### Subagent Batch Management

When using `delegate_task` for wiki operations:
- **Set max_iterations >= 20** per subagent for creating 5+ pages
- **Each page creation** costs ~3-4 tool calls (read reference + write + verify)
- **Always include** index.md and log.md updates in the same batch
- **Never claim completion** without verifying files exist after the subagent returns
- If a subagent hits max_iterations, check what was actually written and complete remaining work

### CRITICAL: Path Resolution (Both Main Agent and Subagents)

Use the canonical profile paths:
- Repo root: `~/ai-topics`
- Wiki root: `~/wiki`
- Hermes scripts: `~/.hermes/scripts`

`~/wiki` is the source of truth and is expected to resolve to the git-managed
wiki under `~/ai-topics/wiki`. Do not infer or write to alternate paths such as
`/opt/data/.hermes/home/wiki`, `/opt/data/home/wiki`, or historical
`~/.hermes/hermes-agent/wiki` locations.

If a delegated context has an isolated HOME, it must still target the canonical
paths above. Treat any `~/.hermes/home/...` path that appears during execution as
a runtime artifact, not a second wiki.
    
    for f in os.listdir(src_dir):
        if f.endswith('.md'):
            src_path = os.path.join(src_dir, f)
            dst_path = os.path.join(dst_dir, f)
            
            if not os.path.exists(dst_path):
                shutil.copy2(src_path, dst_path)
                print(f"COPIED: {f}")
            elif os.path.getsize(src_path) > os.path.getsize(dst_path):
                shutil.copy2(src_path, dst_path)
                print(f"UPDATED: {f}")
```

**Prevention strategy:** When writing subagent instructions, explicitly state the full absolute path:
- Use `/opt/data/ai-topics/wiki/concepts/` (NOT `~/wiki/concepts/`)
- Or include the copy script in the subagent's instructions as a final step

**Verification is still required** — even with absolute paths, subagents may ignore them.

## Git Merge Corruption Recovery

When a merge or automated edit corrupts wiki files (especially `log.md`), follow this recovery procedure:

### Symptoms to look for
1. **Line number prefixes in content:** Lines like `     1|## 2026-04-15` indicate `read_file` output was accidentally pasted into the file
2. **Missing sections:** A recent commit's entry disappeared from `log.md` after a merge
3. **Orphaned headers:** `### Updated Entity Pages` without its parent `## YYYY-MM-DD — Title`
4. **Missing `---` separators:** Sections run together without dividers

### Recovery procedure

① **Check for git conflict markers first:**
```bash
grep -n "<<<<<<\|======\|>>>>>>" wiki/log.md
```
If found, this is a standard merge conflict — resolve with standard git workflow.

② **If no conflict markers but content is missing,** find the lost content in git history:
```bash
# Find the commit that originally added the missing section
git log --all --oneline -- wiki/log.md | grep -i "<keyword>"
# Recover the content from that commit
git show <commit-hash>:wiki/log.md
```

③ **Fix line number corruption:** Remove lines matching the pattern `^\s*\d+\|` that were accidentally embedded:
```python
import re
with open("wiki/log.md") as f:
    content = f.read()
# Remove corrupted line-number-prefixed lines
lines = content.split('\n')
cleaned = [line for line in lines if not re.match(r'^\s*\d+\|##', line)]
```

④ **Restore missing section headers:** If a section lost its `## YYYY-MM-DD — Title` header (common when line-number corruption removes it), add it back before the orphaned `###` subsections.

⑤ **Add missing `---` separators:** Ensure sections are properly delimited.

⑥ **Verify the fix:**
```bash
# Check no more corruption patterns
grep -c "^\s*\d+\|" wiki/log.md
# Verify section count makes sense
grep -c "^## 2026" wiki/log.md
```

⑦ **Commit and push:**
```bash
cd ~/ai-topics && git add wiki/log.md && git commit -m "fix: restore <section> and remove line number corruption" && git push
```

### Prevention
- **Never paste `read_file` output directly into wiki files** — the line number prefixes (`     1|`) corrupt the markdown
- **Do NOT use `read_file().content` programmatically for file modification** — the returned `content` field already contains line-number prefixes. `result = read_file(path); lines = result["content"].split("\\n")` and writing those back embeds prefixes in the file. Instead, always use direct Python file I/O: `with open(path) as f: content = f.read()` or `lines = f.readlines()`. This is the same reason `patch` is preferred over `read_file+write_file` for edits — see "Patch-Based Index Insertion" for the correct approach.
- **After merge operations, always verify `log.md` structure** — merges can silently drop sections
- **Use `git show <commit>:path` to recover lost content** rather than reconstructing from memory

## Working with the Wiki

### Searching

```bash
# Find pages by content
search_files "transformer" path="$WIKI" file_glob="*.md"

# Find pages by filename
search_files "*.md" target="files" path="$WIKI"

# Find pages by tag
search_files "tags:.*alignment" path="$WIKI" file_glob="*.md"

# Recent activity
read_file "$WIKI/log.md" offset=<last 20 lines>
```

### Bulk Ingest

When ingesting multiple sources at once, batch the updates:
1. Read all sources first
2. Identify all entities and concepts across all sources
3. Check existing pages for all of them (one search pass, not N)
4. Create/update pages in one pass (avoids redundant updates)
5. Update index.md once at the end
6. Write a single log entry covering the batch

**Batch page creation via `execute_code`:** When creating 3+ wiki pages in a session,
consolidate the file writes into a single `execute_code` invocation that writes all pages
(raw articles, entity pages, concept pages) in one Python script. This is more token-efficient
than N separate `write_file` calls. Use Python's `os.makedirs(exist_ok=True)` for directory
creation and `open(path, 'w')` for each file. After the batch, verify all files exist with
`os.path.exists()` checks in the same script. Similarly, batch index insertions by issuing
multiple `patch` calls in parallel (they target different sections and don't conflict).

**Batch enrichment via `execute_code` (preferred over N × `write_file`):** When enriching
N existing entity/concept pages with new sections (from raw articles), use a SINGLE
`execute_code` call with Python's `with open(path) as f: content = f.read()` for reading
each file, apply modifications (string replacements, section insertions, `updated` date bumps),
then `with open(path, 'w') as f: f.write(content)`. This pattern:

- Avoids N separate `write_file` calls (token overhead)
- Lets you verify all files in one `print()` summary at the end
- Supports cross-file consistency checks (same `updated` date, consistent source references)
- Safety: always read first to check existing content and avoid duplicate sections.
  Use `if 'target section header' not in content:` guards to prevent idempotency errors.
- After writing, print file sizes and line counts to verify no truncation occurred.
- Works for any number of files — in production tested with 5 simultaneous enrichments
  (Harvey SOC, Petra Donka Buzz, Glean MCP eval, Hex repos, Decagon agent eng).

**⚠️ Split strategy when monolithic execute_code fails**: When the enrichment script grows large (10+ files, nested strings with quotes), Python syntax errors from complex `.replace()` calls with escaped quotes are common. **Also fails on large dict literals with multi-line f-string values** — the parser loses track of closing braces, producing `SyntaxError: '{' was never closed`. This is a distinct failure mode from quote escaping; the fix is the same split strategy below. Recovery pattern:
  1. **New pages first**: Write brand-new entity/concept pages via parallel `write_file` calls — these are simple, independent, and never trigger quote-escape issues.
  2. **Enrichments second**: Handle existing-page enrichments in a separate `execute_code` call that reads + modifies + writes each file using Python's `with open()` pattern.
  3. **Why this works**: `write_file` bypasses the Python-internal quoting problem entirely for new content, while `execute_code` modifications avoid it by never placing the full content string inside Python string literals — they read from disk instead.
  4. After both batches complete, verify all files exist and update index.md + log.md in a final step.

**⚠️ Markdown table pipe prefix mismatch (silent str.replace failure)**: Before using `str.replace()` to modify a markdown table row (e.g., adding a feature to a feature table), check whether the file uses single `|` or double `||` pipe prefixes for table rows. Files created by different pipelines may differ: some use `| Feature | Detail |` (single pipe), others `|| Feature | Detail ||` (double pipe). A `str.replace()` targeting `|| Claude Opus 4.8 | ... ||` will silently do nothing on a file using single-pipe format. **Detection after failure**: `read_file(offset=N, limit=3)` shows the actual prefix. **Fix**: When the first str.replace fails, use `repr()` on the target lines to discover the exact pipe prefix. **Prevention**: Always read the exact table row via `read_file` before writing the replacement strings — match the actual pipe count, don't assume `||`. This was discovered in a 9-file batch enrichment where 3 replacements silently failed due to single-pipe vs double-pipe mismatch.

**⚠️ Frontmatter `updated` field may be entirely absent**: Some older entity pages (especially those created by the blog-wiki pipeline or early agent sessions) have a `created` field but NO `updated` field. A `str.replace()` targeting `"updated: 2026-05-11"` will silently fail — there's nothing to replace. **Detection**: Before running the batch, check whether `"updated:"` exists in each target file's frontmatter (first 15 lines). **Fix**: If `updated:` is absent, add it after `created:` using `content.replace(f"created: {created_date}\n", f"created: {created_date}\nupdated: {today}\n")`. If the `roles:` or `education:` keys appear between `created` and where `updated` should go, the frontmatter has non-standard ordering — handle by inserting after `created:` regardless. **Prevention**: Include a pre-flight check in every batch enrichment: read the first 15 lines of each target file and assert the presence of `"updated:"` — or add it if missing.

**⚠️ Section insertion anchor mismatch — heading vs list item**: When inserting new content before an existing section, verify the anchor text is actually a heading (`### Section Title`) and not a list item (`- **Section Title**:`). These look identical at a glance but have different match behavior. Common in entity pages where feature descriptions use `- **Feature Name**: Description` format rather than `### Feature Name`. A `str.replace()` targeting `### Mid-conversation system messages:` will silently fail against the actual `- **Mid-conversation system messages**:`. **Detection after failure**: `read_file(offset=N, limit=3)` reveals the actual line prefix. **Prevention**: Read the exact 3 lines around the insertion point before writing the replacement string; copy the exact prefix (including dash, stars, indent level) for the anchor.

### Archiving

When content is fully superseded or the domain scope changes:
1. Create `_archive/` directory if it doesn't exist
2. Move the page to `_archive/` with its original path (e.g., `_archive/entities/old-page.md`)
3. Remove from `index.md`
4. Update any pages that linked to it — replace wikilink with plain text + "(archived)"
5. Log the archive action

### Obsidian Integration

The wiki directory works as an Obsidian vault out of the box:
- `[[wikilinks]]` render as clickable links
- Graph View visualizes the knowledge network
- YAML frontmatter powers Dataview queries
- The `raw/assets/` folder holds images referenced via `![[image.png]]`

For best results:
- Set Obsidian's attachment folder to `raw/assets/`
- Enable "Wikilinks" in Obsidian settings (usually on by default)
- Install Dataview plugin for queries like `TABLE tags FROM "entities" WHERE contains(tags, "company")`

If using the Obsidian skill alongside this one, set `OBSIDIAN_VAULT_PATH` to the
same directory as the wiki path.

### Obsidian Headless (servers and headless machines)

On machines without a display, use `obsidian-headless` instead of the desktop app.
It syncs vaults via Obsidian Sync without a GUI — perfect for agents running on
servers that write to the wiki while Obsidian desktop reads it on another device.

**Setup:**
```bash
# Requires Node.js 22+
npm install -g obsidian-headless

# Login (requires Obsidian account with Sync subscription)
ob login --email <email> --password '<password>'

# Create a remote vault for the wiki
ob sync-create-remote --name "LLM Wiki"

# Connect the wiki directory to the vault
cd ~/wiki
ob sync-setup --vault "<vault-id>"

# Initial sync
ob sync

# Continuous sync (foreground — use systemd for background)
ob sync --continuous
```

**Continuous background sync via systemd:**
```ini
# ~/.config/systemd/user/obsidian-wiki-sync.service
[Unit]
Description=Obsidian LLM Wiki Sync
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/path/to/ob sync --continuous
WorkingDirectory=/home/user/wiki
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now obsidian-wiki-sync
# Enable linger so sync survives logout:
sudo loginctl enable-linger $USER
```

This lets the agent write to `~/wiki` on a server while you browse the same
vault in Obsidian on your laptop/phone — changes appear within seconds.

## Pitfalls

- **TAG GATE (HARD RULE — TRIGGERS ON EVERY WIKI WRITE)** — When creating or updating ANY wiki page (entity, concept, comparison, query), every tag in the frontmatter MUST come from `wiki/SCHEMA.md`'s Tag Taxonomy section. Before writing a page: (1) read SCHEMA.md's taxonomy, (2) ensure every tag you plan to use exists there. If you need a genuinely new tag category, add it to SCHEMA.md FIRST, then use it. NEVER use ad-hoc tags. Composite kebab-case tags (5+ hyphen-joined words like `cognition-devin-memory-tool-claude-code`) are ALWAYS errors — decompose them into individual canonical tags. A pre-commit hook blocks commits with non-SCHEMA tags; if you see a `TAG TAXONOMY VIOLATION` block, fix the tags before committing.
- **`|` pipe prefix corruption in log.md from patch** — When using `patch` to append entries to `log.md`, if the `old_string` or `new_string` contains a trailing `|` character (from markdown table formatting or clipboard artifacts), that `|` gets written into the file as a standalone line. This produces entries like:
  ```
  - Total pages: 1834
  |
  ## [2026-05-13] dreaming | ...
  ```
  **Detection**: `grep -n '^|$' wiki/log.md` finds standalone pipe lines. **Fix**: `sed -i '/^|$/d' wiki/log.md` or Python `content = re.sub(r'\n\|\n', '\n', content)`. After fixing, verify with `grep -c '^|$' wiki/log.md` returns 0. To prevent, never include bare `|` at the end of `new_string` in patch calls — the `|` suffix from line-number-prefixed read_file output is the most common source.

- **In-page content duplication (repeated sections in same file)** — Entity pages can develop repeated sections when multiple ingest pipelines append the same topic (e.g., "The Mismeasure of Open Source" appearing 3 times in `entities/andrew-nesbitt.md`). This happens when different pipelines enrich the same page without checking whether the section already exists. **Detection**: `grep -c '^###'` on a page to flag unusually high section counts for its subject breadth. For specific topics, search for repeated header strings. **Fix**: Use Python to find duplicate section boundaries:
  ```python
  import re
  with open(path) as f: content = f.read()
  # Find duplicate sections by header text
  headers = re.findall(r'^### .+', content, re.MULTILINE)
  seen = {}
  for h in headers:
      if h in seen:
          print(f"DUPLICATE: {h}")
      seen[h] = True
  # Remove all but first occurrence of each duplicate section
  # Find the start of each duplicate (after first) and remove to next header
  ```
  **Prevention pipeline**: When enriching an existing page with blog-post-specific content, always search the page for the article's title or key phrases first (`grep -ci "exact article title"`) before adding a new section. This applies to both automated cron pipelines and manual enrichments.
- **SOURCES GATE (HARD RULE — TRIGGERS ON EVERY WIKI WRITE)** — Every wiki page MUST have a `sources:` field in its frontmatter, even if empty (`sources: []`). When creating a page from a raw article, set `sources: [raw/articles/<filename>]`. When creating from web extraction or synthesis, list the URLs: `sources: [https://example.com/article]`. **Never omit the sources field** — this was the single largest frontmatter gap discovered in 2026-05-13 audit (770+ of 810 broken pages were missing `sources`). If unsure, use `sources: []` rather than omitting it entirely.
- **Never modify files in `raw/`** — sources are immutable. Corrections go in wiki pages.
- **Always orient first** — read SCHEMA + index + recent log before any operation in a new session.
  Skipping this causes duplicates and missed cross-references.
- **Always update index.md and log.md** — skipping this makes the wiki degrade. These are the
  navigational backbone.
- **Don't create pages for passing mentions** — follow the Page Thresholds in SCHEMA.md. A name
  appearing once in a footnote doesn't warrant an entity page.
- **Don't create pages without cross-references** — isolated pages are invisible. Every page must
  link to at least 2 other pages.
- **Frontmatter is required** — it enables search, filtering, and staleness detection.
- **Tags must come from the taxonomy** — freeform tags decay into noise. Add new tags to SCHEMA.md
  first, then use them.
- **Keep pages scannable** — a wiki page should be readable in 30 seconds. Split pages over
  200 lines. Move detailed analysis to dedicated deep-dive pages.
- **Ask before mass-updating** — if an ingest would touch 10+ existing pages, confirm
  the scope with the user first.
- **Rotate the log** — when log.md exceeds 500 entries, rename it `log-YYYY.md` and start fresh.
  The agent should check log size during lint.
- **Handle contradictions explicitly** — don't silently overwrite. Note both claims with dates,
  mark in frontmatter, flag for user review.
- **execute_code file writes are sandboxed — use write_file for wiki pages**: `execute_code` with
  Python's `open(path, 'w')` creates files in a temporary sandbox, NOT on the real filesystem.
  The script will report "CREATED: entities/foo.md" and `os.path.exists()` returns True, but the
  file won't exist when you try `git add` or `ls` from terminal. **For creating or modifying wiki
  pages, always use `write_file` with absolute canonical paths** (`/opt/data/ai-topics/wiki/...`).
  execute_code is still fine for reading, processing, analysis, and cross-referencing — just not
  for writing wiki files. This also applies to raw article files under `wiki/raw/articles/`.
  **Recovery**: after discovering the files are missing, use `write_file` with the same content
  to recreate them on the real filesystem.
- **Verify before claiming completion** — always check that files actually exist after delegate_task
  or any async operation before telling the user work is done. Use `search_files` to confirm.
- **Don't over-promise on article counts** — when analyzing a large backlog (2,000+ articles),
  report the filtered count and processing plan first, don't claim pages are created until they're verified.
- **Subagent iteration budgets are real** — max_iterations=20 allows ~5-7 page creations. For larger
  batches, split across multiple subagents or increase max_iterations.
- **search_files is unreliable for wiki directory discovery** — it may return 0 results for files that
  definitely exist (e.g., entity pages like `simon-willison.md`). Use Python `os.walk()` or
  `os.path.exists()` via execute_code instead when locating specific wiki pages.
- **Entity file-to-identity check — slugs are ambiguous**: `os.path.exists("pi.md")` returning true does NOT mean Pinecone has an entity page — it could be the Pi coding agent. Similarly, `contextarena.md` is a benchmark, not Arena the company. When checking whether an entity already has a page, **always read the page's title/overview** (not just check file existence) to confirm the slug maps to the expected entity. File-name collisions between unrelated entities sharing similar names are common in large wikis.
- **Slug near-matches during cross-reference**: when checking for duplicates via `os.path.exists()`, a candidate slug like `nvidia-nemotron-3` won't match the canonical `nvidia-nemotron-3-nano-omni`. The cross-reference script must **also scan `index.md` for near-match entries** — grep for the candidate's core slug (e.g., `nvidia-nemotron`) across the index before creating a new page. The index often has the canonical full name while your simplified candidate slug misses it. Use `search_files` on the index with a substring of the candidate name as a secondary check.
- **`|-` pipe table syntax corruption** — automated tools or scripts can render `index.md` entries as markdown table rows (`|- [[entities/foo]] — summary`). This corrupts ~200+ lines at scale. Detection: `grep -c '^|- \\[\\[' wiki/index.md`.
  **Fix with Python (one-shot, all lines):**
  ```python
  import re
  with open("wiki/index.md") as f: content = f.read()
  fixed = re.sub(r'^\\|-\s+\[\[(?:entities|concepts|comparisons|queries)/',
                 lambda m: '- [[' + m.group(0)[4:], content, flags=re.MULTILINE)
  with open("wiki/index.md", 'w') as f: f.write(fixed)
  ```
  **Post-fix verification:** commit must say `✓ wiki/index.md clean (N lines)` and NOT flag any `pipe-prefixed list item` warnings.
- **Index header count math is unreliable** — "Total pages: N" frequently diverges from actual filesystem count (discrepancies of 600+ observed at 1,754 pages; Concepts section showed 459 vs actual 1,064). "Full entries" + "Stubs" may not sum to "Total". Always verify with `os.walk()` or `ls ~/wiki/concepts/*.md | wc -l` on the filesystem, never trust the header alone. **Severity at scale**: At 5,000+ pages, discrepancies compound further.
- **Extension-less wikilinks to `_index.md`** — links like `[[concepts/_index]]` or `[[agentic-engineering/_index]]` will NOT resolve on case-sensitive filesystems. The target file is `_index.md`, not `_index`. Fix: append `.md` or use `[[agentic-engineering/_index|_index.md]]` syntax.
- **Log prepending via `patch` is dangerous — two failure modes**:

  **① Header swallowing (this session)**: When prepending a new log entry before an existing `## [YYYY-MM-DD]` entry, using that entry's header line as the `old_string` anchor will **silently delete the anchor header**. The `patch` replaces the matched text with `new_string`, so the existing entry's header disappears and its sub-sections (`### Pages Created`, `### Pages Updated`) become orphaned under your new entry. **Example of what happens**: the file goes from `## [2026-05-14] enrich | new entry\n\n### Pages Updated\n...` to having the original `## [2026-05-14] ingest | existing entry` line gone entirely, with `### Pages Created` and `### Pages Updated` now misattributed to your enrich entry.

  **② Duplication**: When `new_string` accidentally includes a second copy of the anchor line, both copies are written (already documented).

  **Correct approach for log prepending**: Do NOT use `patch` — use `execute_code` with Python to insert lines at a known position. Pattern:
  ```python
  with open(path) as f: lines = f.readlines()
  # Insert new entry after the header block
  # ⚠️ CRITICAL: Find where the header ends, do NOT hardcode line 7.
  # The # Wiki Log header + metadata lines are followed by a blank line, 
  # then the first ## [YYYY-MM-DD] chronological entry.
  # Find the first ## [ entry to split header from chrono content:
  chrono_start = None
  for i, line in enumerate(lines):
      # Handle both ## [YYYY-MM-DD] and ## YYYY-MM-DD formats (mixed format)
      import re
      if line.startswith('## ['):
          chrono_start = i
          break
      if line.startswith('## ') and re.match(r'## \d{4}-\d{2}-\d{2}', line):
          chrono_start = i
          break
  # If still None, fall back to first ## line (edge case: no date-entries yet)
  if chrono_start is None:
      for i, line in enumerate(lines):
          if line.startswith('## '):
              chrono_start = i
              break
  # ⚠️ CRITICAL: Do NOT filter chrono_start by date. The first `## [` in the file is
  # the correct split point, even if it shares today's date. Adding `and not
  # line.startswith('## [2026-05-24]')` would skip same-day entries and place YOUR
  # new entry BELOW them instead of at the top of the chronological section, breaking
  # newest-first ordering. The chrono_start loop must be a simple first-match search
  # with no date-based exclusions.
  # header_block = lines[:chrono_start], chrono_entries = lines[chrono_start:]
  # ⚠️ AFTER writing, ALWAYS verify the header survived:
  # with open(path) as f: first_line = f.readline()
  # assert first_line.strip() == '# Wiki Log', f"Header buried! Got: {first_line.strip()}"
  header_block = lines[:chrono_start]
  new_entry = ["## [YYYY-MM-DD] enrich | subject\n", "\n", "### Pages Updated\n", ...]
  chrono_entries = lines[chrono_start:]
  lines = header_block + new_entry + ["\n", "---\n", "\n"] + chrono_entries
  with open(path, 'w') as f: f.writelines(lines)
  ```
  
  **⚠️ WRITELINES TRAP: `f.readlines()` vs `content.split('\n')`** — The code above uses `f.readlines()` which preserves trailing `\n` on each line. If you instead use `content.split('\n')` to read the file, trailing newlines are stripped. Passing that stripped list to `f.writelines()` produces a corrupted file where lines merge together (e.g. `# Wiki Log> Chronological record...Append-only.## [YYYY-MM-DD]`). **Use `f.readlines()` for readability in log prepending** OR use `'\n'.join()` + a single `f.write()` call when working from `split('\n')` output. The post-write assertion (`assert f.readline().strip() == '# Wiki Log'`) catches this corruption immediately.

  **Recovery from writelines/split-newline corruption**: When the header merges into a single line, try one of these fix patterns:
  ```python
  # Light fix for simple merged-header cases
  content = content.replace('# Wiki Log>', '# Wiki Log\n>')
  content = content.replace('Append-only.##', 'Append-only.\n\n##')
  
  # Full reconstruction from git (for complex corruption)
  import subprocess
  result = subprocess.run(["git", "show", "HEAD:wiki/log.md"],
      capture_output=True, text=True, timeout=10)
  ```
  After fixing, verify with `head -4 wiki/log.md` that `# Wiki Log`, the metadata line, a blank line, and `## [YYYY-MM-DD]` are on separate lines.
  
  **⚠️ FAILURE MODE: DO NOT use `f.write(new_entry + content)`** — this simple prepend pattern buries the `# Wiki Log` header because `content` starts with the header, and prepending `new_entry` before it pushes the header to line 3+. The resulting file starts with `## [YYYY-MM-DD]` instead of `# Wiki Log`, violating the canonical structure. This happened in the 2026-05-20 health-fix session: the header ended up at line 37 and required a multi-step recovery (rescue header from middle of file, reconstruct with correct ordering). **Always insert AFTER the header block** using header/chrono splitting as shown above.
  
  **⚠️ CRITICAL sub-pitfall — do NOT use `content.index()` for position finding.** When using `re.search()` to find a match position, do NOT call `content.index(match.group(2), match.start())` to compute the replacement range. `content.index()` returns the FIRST occurrence of the substring from the given start position — but if `match.group(2)` is a common pattern like `## [YYYY-MM-DD]`, it will match the very first entry in the file (not the one adjacent to your search match), causing wholesale truncation of everything below the first entry. This was demonstrated in the 2026-05-20 watchdog session: attempting to remove an orphan `###` line using `content.index('## [', match.start())` truncated 1,100 lines, requiring `git checkout` recovery. **Always extract the exact position from the match object itself**: use `match.end(2) - len(match.group(2))` or store the position in a variable from the regex match directly.
  
  **⚠️ POST-WRITE VERIFICATION**: After writing log.md, ALWAYS verify:
  ```python
  with open(path) as f: first_line = f.readline()
  assert first_line.strip() == '# Wiki Log', f"Header buried! First line: {first_line.strip()}"
  # Also verify: grep -c '^# Wiki Log' = 1, first ## [ entry follows header
  ```
  
  **⚠️ SUB-PITFALL: Backtick-wrapped `## [` in the Format line is a `chrono_start` false positive.** The `> Format: \`## [YYYY-MM-DD] action | subject\`` metadata line contains the literal string `## [` inside backtick code. When finding `chrono_start` via `content.find("## [")` or `content.index("## [", start)`, this metadata match fires BEFORE any real chronological entry, causing the split to happen inside the backtick span. The result: the Format line is truncated to `> Format: \`` (everything after the first backtick is lost). **Detection**: `head -4 wiki/log.md` shows `> Format: \`` instead of `> Format: \`## [YYYY-MM-DD] action | subject\``. **Fix**: Use a regex that excludes backtick-wrapped matches, e.g., `re.search(r'(?<!\`)## \[', content)` or split on the first `## [` that appears on its own line (after a `\n`, not after backtick on the Format line). **Prevention**: In the `chrono_start` detection loop, skip lines where `## [` appears inside a backtick code span by checking the line starts with `> ` (blockquote prefix used for metadata). Pattern:
  ```python
  if line.startswith('## [') and not line.startswith('> '):  # Skip > Format: `## [...
      chrono_start = i
      break
  ``` 
  After any log.md write, always verify with `head -4 ~/wiki/log.md` that the Format line is complete, not truncated.
  
  If you must use `patch` instead of execute_code, use a **multi-line anchor spanning the gap between entries** (e.g., the `---` separator + next entry's full header + first sub-section line) to ensure uniqueness and prevent swallowing. After any log edit, verify the first ~30 lines with `read_file(limit=30)` to confirm entries are properly separated.
- **Verify log.md structure after rotation** — log rotation scripts can produce a duplicate
  header section: the first `# Wiki Log` header + rotate entry + `---` separator, followed
  by a second `# Wiki Log` header + duplicate rotate entry. **Detection**: `grep -c "^# Wiki Log" wiki/log.md`
  must return exactly 1. **Fix**: remove everything from the second `# Wiki Log` occurrence to
  the beginning of the next legitimate `## [YYYY-MM-DD]` entry. See `wiki-graph-health` skill's
  `references/log-rotation.md` for the full procedure and Python fix script.
- **Missing `# Wiki Log` header (silent loss)** — The entire `# Wiki Log` header block (title + metadata lines) can go missing from `log.md` due to prior `execute_code` log-prepending operations that use wrong line offsets. The file then starts directly with `## [YYYY-MM-DD]` entries. **Detection**: `head -1 wiki/log.md` should return `# Wiki Log`, not a date-stamped header. **Recovery**: use a large `patch` that inserts the header block + your new entry simultaneously before the first existing entry. Pattern: `old_string` = the first `## [YYYY-MM-DD]` entry's header line + first subsection, `new_string` = full `# Wiki Log` header block + your new entry + the existing first entry. This fixes both the missing header and inserts your entry in a single atomic operation. **Prevention**: never assume line 7 is the insert point for `execute_code` log prepending — read the first 5 lines first to confirm the header is present.
- **Watch for index entry drops when patching** — when inserting into `index.md` via `patch`,
  never guess what's between two anchor lines. The `old_string` must match the file EXACTLY.
  If you assume `recursive-self-improvement` immediately follows the section header but the
  file actually has `accelerate` in between, `patch` will silently drop `accelerate` and
  possibly create duplicates. Use `read_file` with the exact offset to confirm the 2-3 lines
  forming your `old_string` anchor before calling `patch`. After every index `patch`, verify
  the section with `read_file` before proceeding. See `references/index-insertion-discovery.md`
  for the full pattern and failure case.
- **Triple bracket corruption (`[[[`)**: A variant discovered 2026-05-10 where index entries gain a third opening bracket: `[[[concepts/foo]]` instead of `[[concepts/foo]]`. This renders wikilinks unparseable by Obsidian/wiki tools. **Detection**: `grep -c '[[\[' wiki/index.md`. **Fix**: `content.replace('[[[', '[[')` — always safe since triple brackets are never intentional.
- **Index entry points to wrong directory**: Entry says `[[concepts/slug]]` but file lives in `entities/` (or vice versa). Causes entry to appear "missing" from filesystem. **Detection**: For each `[[dir/slug]]`, check `os.path.exists(wiki/dir/slug.md)`. If false, check the other namespace. **Fix**: Replace wrong namespace prefix with correct one.
  **How this happens during active-crawl creation**: The agent batch-creates pages across namespaces (e.g., `concepts/gemini-spark.md` and `entities/qwen-3-7-max.md`), then inserts each index entry next to alphabetically-adjacent entries. If `gemini-spark` is alphabetically closest to entries in the Entities section (e.g., `gemini-3-5-flash`, `gemma-4`), the agent naturally inserts it there — but writes `[[entities/gemini-spark]]` instead of `[[concepts/gemini-spark]]`. **Prevention**: After batch-creating pages, verify EACH index entry's namespace prefix matches the file's actual directory. In the `execute_code` batch, cross-check: `for entry in new_entries: assert entry.startswith(f"[[{actual_dir}/")`.
- **"Found 2 matches" patch failures due to list-marker inconsistency** — when `patch` returns
  `"Found 2 matches for old_string"` but `search_files` shows each line appearing only once,
  the culprit is often a mix of `- ` (dash space) and `|- ` (pipe dash space) list markers in
  index.md. The `patch` tool sees both patterns as valid anchor candidates even though they
  differ. **Fix**: (1) read the target section with `read_file(offset=N, limit=6)` to see the
  exact content characters, (2) use a 4-line `old_string` (including one line before and after
  the target pair) to make the match unique, or (3) run the pipe-table fix recipe first
  (see `|-` pipe table syntax corruption pitfall) to normalize all list markers, then retry
  the patch.
- **Newsletter triage JSON parsing failure** — when newsletter-wiki-ingest receives
  `failed to parse JSON response from newsletter-triage output`, the triage output is
  embedded in a markdown-wrapped cron output file. Fallback: read
  `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` directly — this is pure JSON
  saved by the triage job. If that's missing, grep the `.md` output file for the JSON
  block after the `## Response` heading.
  **Same pattern for all pipelines** — the `blog-wiki-ingest` and `dreaming-wiki-ingest`
  jobs face the identical issue. For blog: `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json`.
  For dreaming: `${HERMES_HOME}/cron/data/dreaming/triage_latest.json`. The upstream triage
  job saves JSON to the checkpoint path before the wiki-ingest runs; always read from the
  checkpoint path, not from the cron output file.
- **`web_extract` blocked on public URLs (private network error)** — some hosting platforms (Quartz, certain CDNs) trigger this. Use the decision tree in `references/content-extraction-fallbacks.md`: search for alternative mirrors → curl raw HTML → try `.md` endpoint → `browser_navigate` last resort.
- **`web_extract` returns only navigation chrome (silent failure)** — `web_extract` reports success but returns only menus/footers/cards with zero article body. Common on JS-rendered official blogs (Google DeepMind, OpenAI, Anthropic). On headless servers without Chrome, use `web_search` triangulation: query 2-3 angles to find third-party tech news coverage (MarkTechPost, The Register, The Decoder) that reproduces key quotes and data. See `references/content-extraction-fallbacks.md` step 4 for the full pattern and example.
- **Paywalled content is still usable** — beehiiv/substack paywalled articles with free previews
  often contain enough technical claims (model names, chip specs, utilization numbers) to
  justify wiki updates. Cross-reference with non-paywalled sources. Mark uncertain claims
  with qualifiers ("reports suggest", "rumored").
- **`web_extract` LLM summarization truncation** — long articles (especially news articles and
  Substacks) frequently trigger: `LLM summarization timed out. To fix: increase
  auxiliary.web_extract.timeout in config.yaml, or use a faster auxiliary model. Use
  browser_navigate for the full page.` When this happens, the first ~5,000 characters are still
  usable for extracting key facts. For richer content, use `browser_navigate` on the URL
  (produces a full text snapshot including all paragraphs, lists, and quotes) — but note that
  `browser_navigate` requires Chrome/Chromium installed (`agent-browser install`). On headless
  servers where Chrome isn't available, fall back to targeted `web_search` queries for the
  specific model/product name to supplement the truncated content with specifications,
  benchmarks, and architecture details from alternative sources. Treat `web_extract` as a fast
  Treat `web_extract` as a fast initial pass and `browser_navigate`/`web_search` as the fallback for pages that time out.
  **For large arXiv papers (100K+ chars)** where `web_extract` times out on the HTML tab: download the arXiv HTML version
  with `curl`, extract section headings to understand structure, then use Python regex keyword search to find
  new/changed content. Full procedure in `references/large-paper-extraction.md`.
- **`updated` date bump frequently forgotten during execute_code enrichment** — When enriching N existing entity/concept pages via `execute_code` Python string replacements (not via `write_file` or `patch`), the `updated` date in YAML frontmatter is easy to skip because `str.replace()` or ad-hoc section insertion doesn't naturally touch the frontmatter block. Verification step `updated=False` in the post-commit checks is the tell: if the entity page's `updated` field wasn't bumped, the enrichment isn't recorded in the wiki's recency tracking. **Fix**: include an explicit date bump step in the same `execute_code` block — read the frontmatter, find the `updated:` line, and replace it with today's date. Also add the bumped line to the file's sources field for proper source tracking. After writing, verify `has_updated = "updated: YYYY-MM-DD" in content` in the same script. This applies to ALL entity/concept enrichments, not just execute_code — verify the `updated` field for every page touched before committing.
- **Tag taxonomy drift is inevitable at scale**
  truncated content.
- **`str.replace()` failures due to file write-back — `execute_code` calls are independent processes**. Each `execute_code` call starts a fresh Python process. If you modify `content` in one call (e.g., via `str.replace()`), the next call reads the original file. Always write to disk in the SAME `execute_code` call:
  ```python
  with open(path) as f: content = f.read()
  content = content.replace(old, new)
  with open(path, 'w') as f: f.write(content)
  ```
  After writing, verify in the same call: `print(f"Wrote {len(content)} chars")`.
- **For complex Python scripts with nested quotes, write to a temp file**. When the script has multiple `str.replace()` calls, f-strings with `'''` or `"""`, or backtick-wrapped literals (URLs, raw article paths), inline `execute_code` or `terminal("python3 -c ...")` can fail with `SyntaxError` or bash backtick substitution. Write the script to `/tmp/` and run via `terminal()`:
  ```python
  write_file(path="/tmp/fix_index.py", content=python_script)
  terminal("python3 /tmp/fix_index.py")
  ```
  Proven on 20-entry index batch (2026-05-27).
  kebab-case tags (e.g., `cognition-devin-memory-tool-claude-code-competitive-analysis`) as
  errors — these should be decomposed into separate tags. Add frequently-used legitimate tags
  to the taxonomy during lint, don't let them proliferate silently.
- **Tag extraction from SCHEMA.md requires multi-pattern matching** — the taxonomy section uses
  mixed formats: backtick-wrapped inline lists (`model, multimodal, text-generation`), bullet
  points with comma-separated tags, and multi-line continuations. A simple regex like
  `` `([a-z-]+)` `` captures only ~60% of canonical tags. For accurate audits, parse each
  category header line, extract all backtick-wrapped AND comma-separated tokens, and handle
  line continuations. If your audit shows 150+ "violations" but SCHEMA.md clearly contains
  those tags, your extraction logic is too narrow.
- **Case-sensitivity wikilink fix procedure** — when `[[concepts/mooncake]]` points to a file
  named `Mooncake.md` on a case-sensitive filesystem:
  1. Rename the file: `mv wiki/concepts/Mooncake.md wiki/concepts/mooncase.md`
  2. Stage both the deletion and addition: `git add wiki/concepts/Mooncake.md wiki/concepts/mooncake.md`
     (Git needs to see both sides of the rename to track it properly)
  3. Commit with descriptive message: `git commit -m "fix: rename Mooncake.md -> mooncase.md"`
  4. Fix all inbound wikilinks: `search_files '\[\[concepts/Mooncake\]\]'` → patch to `[[concepts/mooncake]]`
  5. Push and verify in Obsidian/wiki tools that links resolve correctly
- **Index header count decays over time** — `index.md` header's "Total pages: N" quickly
  becomes stale as pages are created. During lint, always verify:
  `len(os.listdir(entities/) + os.listdir(concepts/) + ...) == reported_count`.
  Discrepancies of 100+ pages are common at scale and should be auto-corrected.
- **Case sensitivity in wikilinks** — `[[concepts/mooncake]]` will NOT resolve to
  `concepts/Mooncake.md` on case-sensitive filesystems (Linux servers). During broken link
  checks, try case-insensitive basename matching as a secondary resolution strategy.
- **_index.md files are special** — subdirectory `_index.md` files (e.g., `concepts/_index.md`)
  serve as synthesis hubs and may legitimately lack full frontmatter. During lint, exclude
  files named `_index.md` from frontmatter-required checks, or give them a minimal frontmatter
  with `type: index` and `status: synthesis`.
- **TODO-stub duplicate cleanup** — the dreaming pipeline and active-crawl jobs create index
  entries as TODO placeholders (`> **TODO**: Enrich this page`). When real content is later
  written, the index accumulates duplicate entries: one rich + one TODO stub for the same page.
  During lint/dedup: (1) group index entries by wikilink target, (2) keep the rich entry
  (first occurrence), (3) remove all TODO-stub duplicates. Exclude `_index` entries — they
  are legitimate per-directory. Automate with Python: scan for `**- TODO**` or `Enrich this page`
  in index lines, match by wikilink target, remove duplicates bottom-up to preserve line numbers.
- **Triage candidate_wiki_path may point to wrong namespace or slug** — The triage pipeline generates `candidate_wiki_path` suggestions based on topic keywords, not entity/concept namespace awareness or existing slug conventions. Three failure modes:
  1. **Wrong namespace**: triage suggests `concepts/X` but `entities/X` exists (or vice versa). Checked by existing pitfall below.
  2. **Wrong slug (same namespace)**: triage suggests `nvidia-ai-q-deep-research` but the existing page is `nvidia-ai-q`. The `os.path.exists()` check returns False for the triage slug, so you'd create a duplicate.
  3. **Combined**: triage suggests `concepts/nvidia-ai-q-deep-research` but both `concepts/nvidia-ai-q.md` AND `entities/nvidia-ai-q.md` exist with different content breadth.
  **Before creating a page from a triage suggestion:**
  1. Search the SAME namespace for near-matches: grep `index.md` for the candidate's core slug (e.g., search `nvidia-ai` for candidate `nvidia-ai-q-deep-research`). The index may have a canonical entry with a shorter or differently-structured slug.
  2. Also search the OTHER namespace: if the suggestion is `concepts/X`, search for `entities/X` (and vice versa).
  3. Read any near-match pages to confirm whether they cover the topic substantively.
  4. If a near-match exists, **enrich the existing page** — merge triage content there and delete your duplicate. Never create a second page for the same entity under a different slug.
- **Entity vs Concept overlap in index** — some topics exist as both `entities/X` and
  `concepts/X` (e.g., `entities/dspy` + `concepts/dspy`). These are NOT duplicates if both
  files exist with different content. During dedup, only remove entries where the wikilink
  target is **exactly** the same string. `[[entities/foo]]` and `[[concepts/foo]]` are distinct.
- **Non-alphabetical index drift causes programmatic insertion to fail** — at scale (500+ pages),
  the index is NOT guaranteed to be in strict alphabetical order. Entries like
  `mit-encompass` may appear after `moltbook-breach-2026` because different agents and
  pipelines inserted them at different times. Any algorithm that scans for "first
  alphabetically-greater entry" will find the wrong insertion point in a non-alphabetical
  section, placing new entries in wildly incorrect positions (e.g., dumping `model-spec-*`
  entries right after `altman-three-observations` instead of near `mcp`). This creates
  duplicates that require manual cleanup. **Always use `patch` with visually-confirmed
  anchor lines** — read the target section with `read_file(offset=N, limit=20)`, identify
  the exact 2-3 surrounding lines, and use those as the `old_string`. Never compute
  insertion points via `execute_code` regex scanning.
- **Comparison pages go in `comparisons/`, not `concepts/`** — when ingesting a survey or comparison article that covers multiple items (e.g., "10 RL libraries compared"), the synthesis/comparison page belongs in `comparisons/`. Individual item pages (one per library/framework) go in `concepts/` or `entities/`. The `type` frontmatter field must match: `type: comparison` for comparison pages. If the user corrects placement, move the file and update ALL wikilinks across the wiki (`search_files` to find references → `patch(replace_all=true)`), then adjust both section counts in `index.md`.
- **Stub enrichment cascade** — when creating a new concept or entity page that links to an existing stub page (e.g., `mixture-of-experts.md` with `status: stub`), proactively enrich the stub's \"Related Pages\" section with backlinks to the new pages. This keeps the wiki graph connected even before stubs are fully enriched. Check `search_files` for `status: stub` on targets before finalizing your batch.
- **Tag violation commit block recovery** — when the pre-commit hook blocks with `TAG TAXONOMY VIOLATIONS`, the commit output shows the offending files and tags. Recovery procedure:
  1. For each offending tag, check if there's a canonical equivalent in SCHEMA.md's taxonomy (e.g., `enterprise` → `company`, `cost` → `economics`, `routing` → `optimization`)
  2. **If a canonical equivalent exists**: use `patch` on each affected file to replace the non-canonical tag
  3. **If the tag is genuinely missing from SCHEMA.md** (legitimate new tag used by an existing entity/concept): add it to the correct category in SCHEMA.md FIRST, then retry the commit. When patching SCHEMA.md, read the target section with `read_file(offset=N, limit=5)` to get the exact characters — a common pitfall is turning `- **Cat**:` into `|- **Cat**:` by accidentally prepending a pipe. Verify the line starts with `- ` not `|- `.
  4. NEVER use `--no-verify` to bypass — this creates silent debt that compounds with every subsequent edit
  5. After fixing all violations, `git add` the patched files and retry the commit

- **SCHEMA.md pipe prefix corruption from patch fuzzy matching** — When using `patch` to add tags to SCHEMA.md category lines, the `patch` tool's fuzzy matching can convert `- **Category**:` to `| **Category**:` (dash-space → pipe-space) if the `old_string` uses `|` (from read_file output) but the file actually has `- `. The result: category lines become pipe-prefixed markdown table rows instead of list items. This causes the pre-commit tag validator to misparse SCHEMA.md (reporting 298 tags instead of 460+, flagging legitimate tags as violations). **Detection**: `grep -n '^| \*\*' wiki/SCHEMA.md` finds corrupted lines. **Fix**: `re.sub(r'^\| (\*\*)', r'- \1', content, flags=re.MULTILINE)` via execute_code. **Prevention**: Always copy the exact line prefix from the file using `read_file(offset=N, limit=5)` — never reconstruct the prefix from memory. The line-prefix character is `- ` (dash space) for markdown list items, never `| ` (pipe space). After any SCHEMA.md patch, verify no pipe-prefixed category lines with `grep -c '^| \*\*'`. This is a distinct failure mode from the `|-` index.md pipe-table corruption — it affects list markup, not table syntax.
  Common mapping table for tags that tend to be missing from SCHEMA.md:
  | Offending tag | Canonical replacement |
  |---|---|
  | `claude` | `anthropic` (product name, not a tag category) |
  | `codex` | `openai` |
  | `enterprise` | `company` or `governance` |
  | `sandboxing` | `sandbox` |
  | `telemetry` | `observability` |
  | `compliance` | `governance` |
  | `evals` | `evaluation` |
  | `cost` | `economics` or `optimization` |
  | `identity` | `security` or remove (overly broad) |
  | `authorization` | `security` |
  | `gpt` | `openai` |
  | `routing` | `optimization` or `inference` |
  | `agent-orchestration` | `multi-agent` or `orchestration` |
  | `streaming` | `streaming` (add to SCHEMA.md Techniques if missing) |
  | `ai` | `ai` (add to SCHEMA.md Meta if missing) |
  | `web-development` | `web-development` (add to SCHEMA.md Engineering if missing) |
  | `developer-experience` | `developer-experience` (add to SCHEMA.md Engineering if missing) |
  | `developer-tools` | `developer-tooling` |
  | `agents-sdk` | `ai-agents` |
  | `deployment` | `devops` or `infrastructure` |
  | `model-serving` | `inference` |
  | `self-hosting` | `infrastructure` or `security` |
  | `audio-generation` | `multimodal` or `voice-ai` |
  | `creative` | remove (too generic; use existing domain tag) |
  | `together` | `company` |
  | `search-api` | `search` or `api` |
  | `web-search` | `search` |
  | `web-monitoring` | `search` or `observability` |
  | `google-alerts` | `google` or `search` |
  | `bing-api` | `api` or `tool` |
  | `programmatic-monitoring` | `automation` or `observability` |
  | `brand-monitoring` | `search` |
  | `ai-agent-infrastructure` | `ai-infrastructure` |
  | `soc2` | `security` or `governance` |
  | `zdr` | remove (unknown acronym, not a valid tag) |
  | `gemma` | `google` (product name, not a tag category) |
  | `growth` | `economics` or remove (too generic; use domain tag) |
  | `government` | `governance` or `policy` |
  | `competitor` | remove (not a useful category; use `ecosystem` if needed) |
  | `speech-to-text` | `voice-ai` or `multimodal` |
  | `decision-theory` | `rationality` or `agent-foundations` |
  | `productivity` | `automation` or remove (too generic) |
  - **Duplicate tag creation during normalization**: when replacing a non-canonical tag with a canonical one (e.g., `agents-sdk` → `ai-agents`), check whether the canonical tag already exists in the page's tag list. A `patch` that replaces `agents-sdk` with `ai-agents` when `ai-agents` is already present will create a duplicate. Before patching, read the file's frontmatter to see which tags are already there; if the canonical replacement is present, remove the offending tag line entirely rather than replacing it.
- **Tag format mismatch — inline bracket vs YAML list**: Wiki pages use two different tag formats in frontmatter. Inline bracket: `tags: [concept, mcp, agent-tooling, protocol]`. YAML list with dashes: `tags:\n  - concept\n  - mcp\n  - agent-tooling\n`. A `str.replace()` targeting `"  - agent-tooling\n"` will silently fail on a file using inline bracket format — the replacement string doesn't match, the file is unchanged, and the commit is blocked again with the same error. **Always read the file's tag line first** to determine which format it uses. For inline format, replace `"agent-tooling, "` with `"developer-tooling, "`. For YAML list format, replace `"  - agent-tooling\n"` with `"  - developer-tooling\n"`. After fixing, verify with `search_files` that the offending tag no longer appears.
  - **Pre-existing staged-file violations also block commit** — when the pre-commit hook blocks with `TAG TAXONOMY VIOLATIONS`, the offending files often include pages from OTHER pipelines that were already staged (e.g., blog-ingest or parallel pipelines). Do NOT fix only your own pages and retry — scan ALL files listed in the violation output and fix every one. The hook scans the entire staging area, not just your changes. Missing even one violation will cause another block on retry. Pattern: `git status --short` after staging to understand the full scope, then fix all tagged files before recommitting.
- **Patch silently drops lines not in old_string**: when using `patch` to update frontmatter or any multi-line block, the `old_string` must include EVERY line between the first and last anchor lines, not just the lines you intend to change. If `old_string` skips a line (e.g., the `aliases` line between `type` and `created` in frontmatter), that line is silently dropped from the file. Always read the target block first and include the complete stretch of lines in `old_string`. After patching frontmatter, verify the first ~10 lines with `read_file(offset=1, limit=10)` to ensure no fields were lost.
- **Patch can create duplicate frontmatter fields** — the inverse of the above pitfall. When using `patch` to add fields (e.g., new `tags:` entries or `sources:`) to a frontmatter block, check whether those fields **already exist above the matched block**. If the file has `tags:` before `created:` and your `old_string` matches `updated:` through `sources:`, adding `tags:` in `new_string` will create a second `tags:` block below `sources:` — YAML parsers may handle duplicate keys unpredictably and the pre-commit hook may flag it. **Fix**: read the full frontmatter first (not just the targeted area), confirm no field you plan to add already exists above, and if it does, expand your `old_string` to include the existing block so `patch` can replace it in-place. Always verify with `read_file(limit=15)` after any frontmatter `patch`.
- **Patch silently removes blank line between list item and heading** — When using `patch` to replace the LAST item in a bullet list, if the next line is a heading (`## References`) with no blank separator, `patch` does NOT add the missing blank line. The heading gets visually attached: `- last item\n## References` instead of `- last item\n\n## References`. **Detection**: `read_file` shows a heading immediately after a list item. **Fix**: include `\n` before the heading in `new_string`: `"- [[entities/x]] — description\n\n## References"`. **Prevention**: when `old_string` includes the last list item + the heading, always insert `\n` between them in `new_string`. After any `patch` on list boundaries, verify with `read_file`.

## Lint Diagnostic Tools

The skill includes comprehensive diagnostic scripts at `references/wiki-lint-diagnostics.md` that:
- Detects broken wikilinks and orphan pages
- Identifies pipe table corruption in index.md
- Detects line-number prefix corruption in index.md (CRITICAL at scale)
- Validates frontmatter completeness
- Tracks tag taxonomy compliance
- Provides repair scripts for common issues
- Verifies index section completeness (Entities/Concepts/Comparisons/Queries)

Run these diagnostics during every lint session to maintain wiki health.

### Lint Priority Order (from 2026-05-08 findings)

When running lint checks, execute in this order for maximum impact:

1. **Index corruption scan** — check for `^\s*\d+\|` pattern in index.md. At 5,000+ pages, 80%+ of lines may be corrupted.
2. **Section completeness** — verify all 4 sections (Entities, Concepts, Comparisons, Queries) exist with proper headers.
3. **File count reconciliation** — `os.walk()` counts vs index header numbers.
4. **Broken wikilink analysis** — separate missing files from case mismatches from naming variations.
5. **Tag taxonomy audit** — flag one-off tags, composite kebab tags, and tags not in SCHEMA.md.
6. **Frontmatter validation** — check for missing required fields.
7. **Page size analysis** — flag pages over 200 lines.
8. **Orphan page detection** — pages with no inbound wikilinks.
9. **Index-to-filesystem gap** — files on disk not listed in index.md (see pitfall below).

### Index-to-Filesystem Reconciliation (CRITICAL at scale)

At 1,851 L2 pages, the gap between files on disk and index entries grows rapidly.
The `wiki_health.py --json` script reports orphan counts, but does NOT report files
missing from index.md. Run this reconciliation during every graph analysis:

```python
import os, re
wiki = '/opt/data/wiki'
with open(os.path.join(wiki, 'index.md')) as f:
    index_content = f.read()

# Extract all wikilinks from index
index_entries = re.findall(r'\[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', index_content)
indexed = set(f"{cat}/{slug.strip()}" for cat, slug in index_entries)

# Find all files on disk
all_files = set()
for cat in ['entities', 'concepts', 'comparisons', 'queries', 'events']:
    d = os.path.join(wiki, cat)
    if os.path.isdir(d):
        for f in os.listdir(d):
            if f.endswith('.md') and not f.startswith('_index'):
                all_files.add(f"{cat}/{f.replace('.md','')}")

# Report gaps
not_indexed = all_files - indexed
not_on_disk = indexed - all_files
print(f"Files not in index: {len(not_indexed)}")
print(f"Index entries with no file: {len(not_on_disk)}")
```

**Typical findings at scale (May 2026 baseline):**
- 881 files not indexed (47% of L2) — mostly from subagent batches that skipped index update
- Events section often has files on disk but zero index entries — pipeline gap
- Concepts section has the largest gap (875 unindexed out of 1,242)

**Fix strategy:**
1. For **date-stamped news concepts** (e.g., `2026-04-24-gpt-5-5-chatgpt-images-2-0`): batch archive to `_archive/` — these aren't durable concepts
2. For **legitimate concepts**: add index entries alphabetically per section
3. For **Events**: ensure the section header exists and entries are added
4. Never add all 875 at once — batch in groups of 50-100 and verify after each

### Entity Duplicate Detection via Name Normalization

Entity duplicates accumulate from different pipelines using different slug conventions
(hyphenated vs. not, blog URL vs. person name). Detect them with hyphen-stripping normalization:

```python
from collections import defaultdict
duplicates = defaultdict(list)
for f in os.listdir(os.path.join(wiki, 'entities')):
    if f.endswith('.md'):
        normalized = f.replace('.md', '').lower().replace('-', '').replace('_', '')
        duplicates[normalized].append(f.replace('.md', ''))

for key, files in sorted(duplicates.items()):
    if len(files) > 1:
        print(f"DUPLICATE: '{key}' → {files}")
```

**Confirmed duplicates (May 2026):**
- `deliberate-coder` / `deliberatecoder`
- `eugene-yan` / `eugeneyan`
- `lilian-weng` / `lilianweng`
- `samuel-colvin` / `samuelcolvin`

**Merge procedure:**
1. Pick canonical slug (prefer hyphenated form: `eugene-yan`)
2. Read content from non-canonical page, merge into canonical
3. Delete non-canonical file: `git rm wiki/entities/duplicate.md`
4. Update all inbound wikilinks: `search_files '\[\[entities/duplicate\]\]'` → patch to canonical
5. Remove duplicate from index.md
6. Commit and push

**Mid-ingest variant**: When you discover duplicates WHILE ingesting an article (not during a lint pass), follow the workflow in `references/entity-consolidation-during-ingest.md`. The key differences from lint-driven dedup are: (1) you already have the new article content to merge in, (2) you need to delete the new half-written page along with old duplicates, (3) git rename detection may conflate the delete+create with a rename — verify file history is preserved.

## Index Deduplication

When maintaining a wiki at scale (1000+ pages), the index accumulates duplicate entries.
Common causes: dreaming pipeline creating TODO stubs before pages exist, multiple ingest
jobs creating entries for the same topic, or active-crawl jobs not checking existing coverage.

### Automated Dedup Script

```python
# Run via execute_code to identify and remove duplicates
import os, re
from collections import defaultdict

index_path = "/opt/data/ai-topics/wiki/index.md"
with open(index_path) as f:
    lines = f.readlines()

# Group entries by wikilink target
entries = defaultdict(list)
for i, line in enumerate(lines):
    match = re.match(r'- \[\[(.*?)(?:\||\])', line.strip())
    if match:
        key = match.group(1)
        if key.endswith('/_index'):
            continue  # Legitimate per-directory entries
        entries[key].append(i)

# Identify duplicates and remove TODO stubs
lines_to_remove = set()
for key, indices in entries.items():
    if len(indices) > 1:
        todo_lines = [i for i in indices if '**TODO**' in lines[i] or 'Enrich this page' in lines[i]]
        rich_lines = [i for i in indices if i not in todo_lines]
        
        # Keep first rich entry, remove all others
        if rich_lines:
            lines_to_remove.update(rich_lines[1:])
        lines_to_remove.update(todo_lines)

# Remove bottom-up to preserve line numbers
for idx in sorted(lines_to_remove, reverse=True):
    lines.pop(idx)

with open(index_path, 'w') as f:
    f.writelines(lines)

print(f"Removed {len(lines_to_remove)} duplicate entries")
```

### Dedup Rules
- **Entity vs Concept overlap**: `[[entities/foo]]` and `[[concepts/foo]]` are NOT duplicates if both files exist with different content. Only remove entries where the wikilink target is **exactly** the same string.
- **_index exclusion**: Subdirectory `_index` entries are legitimate and should never be removed during dedup.
- **Bottom-up removal**: Always remove lines from highest index to lowest to preserve line numbers for remaining entries.
- **Post-dedup verification**: After dedup, verify the remaining entries point to actual files using `os.path.exists()`.

### False-Positive Trap: Inline Cross-References in Descriptions

⚠️ **Warning**: The automated dedup script above is correct (it uses `re.match()` which captures only the **primary** wikilink at the start of each index line). However, if you write custom duplicate-detection code using `re.findall()` or `re.finditer()` across all wikilinks in each line, **inline cross-references within description text will be falsely counted as duplicates**.

**How this happens**: An entity page entry like `- [[entities/andrew-chen]] — Andrew Chen — ... [[concepts/local-ai]]` has TWO wikilinks. The primary is `entities/andrew-chen`, the inline `[[concepts/local-ai]]` is a cross-reference. A naive `re.findall()` scan would count `entities/andrew-chen` at this line AND also at line `- [[concepts/local-ai]] — ... [[entities/andrew-chen]]` (where it appears as an inline cross-ref in the local-ai entry). This produces 29+ false "duplicates" across a 1,300-line index.

**Prevention — always filter by PRIMARY wikilink only**:

```python
# WRONG — catches ALL wikilinks in each line (inline cross-refs included)
all_links = re.findall(r'\[\[(entities|concepts)/([^|\]]+)\]\]', content)
link_counts = Counter(f"{cat}/{slug}" for cat, slug in all_links)
# 29 "duplicates" found — most are false positives

# CORRECT — only count the PRIMARY link (first wikilink in a line-starting entry)
for line in lines:
    m = re.match(r'- \[\[(entities|concepts|comparisons|queries|events)/([^|\]]+)', line.strip())
    if m:
        key = f"{m.group(1)}/{m.group(2)}"
        entry_positions[key].append((i, line))
# 0 duplicates found — all were inline cross-references
```

**Verification**: If your dedup scan says 25+ duplicates exist but the index looks well-maintained, investigate 3-5 examples. If they all follow the pattern of `slug-A` appearing in `slug-B`'s description AND vice versa, the "duplicates" are legitimate cross-references. Open 3-5 paired entries and read the actual lines to confirm before accepting the count.

**Scale impact**: Observed in action on a 1,300-line wiki with 1,068 unique index entries. The `re.findall` approach flagged 29 duplicates. Investigation revealed ALL 29 were inline cross-references — zero true duplicates existed. Without this check, the dedup script would have removed legitimate cross-reference lines, breaking bidirectional wikilinks between related entity/concept pages.
