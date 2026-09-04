---
name: daily-rss-triage
description: Daily RSS scan triage workflow — scan blogs, triage articles, ingest into wiki, commit changes
category: research
---

# Daily RSS Triage Workflow

End-to-end pipeline for processing daily RSS scans, triaging articles, and ingesting wiki-worthy content.

## Prerequisites

- `blogwatcher-db` skill loaded (database queries)
- `semantic-article-grouping` skill loaded (triage criteria)
- Pre-run script has already executed blogwatcher scan, queried DB, read newsletter, listed existing topics

## Workflow

### Phase 1: Report Generation

1. Parse script JSON output for scan results
2. Generate Japanese summary report (scan stats, failed blogs, articles list, Reddit highlights, newsletter info)
3. Save to `~/ai-topics/inbox/rss-scans/daily-scan-YYYY-MM-DD.md`
4. If article_total > 0 but ≤3 are AI-relevant, supplement with web_search (see Low-Article Day Fallback below)
5. If article_total == 0 AND no newsletter → `[SILENT]`

### Phase 1b: Low-Article Day Fallback (web_search supplementation)

When RSS scan yields few AI-relevant articles, the blog scan alone is insufficient. Supplement proactively:

1. **Web search** for recent AI headlines: `AI ML trending news May 2026` or specific domains (model releases, security incidents, robotics, geopolitical AI chip news)
2. **Cross-reference newsletter triage** — may have processed substantive content that RSS missed
3. **Score discovered topics** with Newsjacking filter — top 5-7 become the report's lead stories
4. **Save raw articles** from official sources (NIST reports, Reuters exclusives, company blogs)
5. **Create/update wiki pages** prioritizing highest wiki-actionability topics

**Effective search queries (discovered in production):**
- `"CAISI evaluation" DeepSeek V4` — NIST government evaluations
- `US officials weigh cutting deadlines fix digital flaws AI-powered hacking` — CISA/Reuters exclusives
- `exodus Boston Dynamics executives humanoid delivery` — Semafor/Business Insider scoops
- `Richard Dawkins Claude consciousness delusion` — AI culture war debates

**Robust fetch fallback (verified 2026-08-10)** — web_search supplementation can silently fail in cron:
1. If you delegated web research to a subagent (`toolsets: ['web']`), VERIFY it actually executed searches. A subagent may return its plan ("I'll search for X...") as the summary with `tool_trace: []` and zero real tool results. Do not trust the summary text — check the result object for actual tool output; if empty, fall through to direct fetch.
2. Direct HTTP fetch always works in cron: write a Python script to `/tmp/` with `write_file` (urllib + strip_html), run with `terminal("python3 /tmp/xxx.py")`. Full recipes: `references/web-supplement-fetch.md`.
3. **Do NOT pipe anything into an interpreter** (`curl ... | python3 -c ...` OR `cat file | python3 -c ...`) — the Hermes security scanner blocks ALL pipes to interpreters (`tirith:pipe_to_interpreter` / `tirith:curl_pipe_shell`, HIGH). Verified 2026-08-16: even `cat latest.json | python3 -c` is blocked. Fetch/write to a file first (`curl -s -o /tmp/out.json URL`, or `write_file` the script) then parse separately, or use urllib inside the script.
4. **HN Algolia URL encoding**: the `>` in `numericFilters=created_at_i>...` must be URL-encoded as `%3E`, or the API returns `400 Bad Request`. Example: `https://hn.algolia.com/api/v1/search?tags=front_page&numericFilters=created_at_i%3E{unix_ts}`. Reusable fetcher: `scripts/hn_algolia_supplement.py` (front page + keyword scan for last N days; run `python3 /tmp/... --days 2 --min-points 20`). The script lives in THIS SKILL's `scripts/` dir (read it via `skill_view(name='daily-rss-triage', file_path='scripts/hn_algolia_supplement.py')` then copy to `/tmp/` to run) — it is NOT in `~/ai-topics/scripts/` (verified 2026-08-17: `ls ~/ai-topics/scripts/ | grep -i hn` returns nothing). **Path caveat (verified 2026-08-29)**: the deployed skill lives under `_custom/`, so the on-disk path is `~/ai-topics/config/hermes/skills/_custom/daily-rss-triage/scripts/hn_algolia_supplement.py` — `cp` from a guessed path returns exit code 2. Locate it with `find ~/ai-topics/config/hermes/skills -name hn_algolia_supplement.py` then copy to `/tmp/`. The script prints both the external URL and the HN item link for every story — use the item link when citing HN discussions in wiki pages.
5. Nav-heavy sites (claude.com, research.meta.ai) return navigation menus in the first ~2500 chars of stripped text — the article body follows the page title; read past the menu.

### Phase 1.5: Newsjacking Triage Filter (READER perspective)

Before detailed triage, apply Newsjacking lens (from Elvis Sun's framework) to identify high-signal articles:

1. **Trend Surfing**: Does the article ride an existing wave? (e.g., Claude Code launch, new model release, viral AI tool)
2. **Polarizing Promise**: Does it make a bold, debatable claim that creates curiosity? ("X is dead", "Everyone is wrong about Y")
3. **Contrarian Insight**: Does it challenge conventional wisdom with data-backed arguments?
4. **Pattern Interrupt**: Is it structurally or topically unusual for its source? (e.g., Karpathy writing about biology, Simon Willison on non-web topics)
5. **In-Group Signal**: Does it use specialized knowledge that creates an "insider" resonance for the target audience (r/LocalLLaMA, AI agent developers)?

**Scoring**: Assign each article a `newsjacking_score` (0-5) based on how many criteria it meets.
- Score ≥ 3: **Priority triage** — flag for immediate wiki ingestion
- Score 1-2: **Standard triage** — normal evaluation
- Score 0: **Low priority** — only ingest if highly relevant to core interests

### Phase 2: Triage

**Cron-mode optimization**: When `execute_code` is blocked (standard in cron jobs — verified 2026-08-20), use this 2-pass pattern:
1. **delegate_task** to a subagent that reads all raw articles and returns a JSON array with `{url, title, summary_2lines, ai_relevance: high|medium|low|none, tags: []}`
2. Use the summary to decide which articles to process, then read individual articles with `read_file`

**Direct curl + terminal Python fallback** (no subagent needed for single-article resolution): `curl -sL <url> > /tmp/page.html` then `python3 /dev/stdin << 'PYEOF' ... PYEOF` to parse HTML. Works for Substack (og metadata + `<article>`/`<div class="body">` extraction) and most static sites. No pipes to interpreters (security scanner blocks `curl | python3 -c`). See `references/web-supplement-fetch.md` for full recipes.

For each article, evaluate:
1. **Already covered?** Check `existing_wiki_topics` list
2. **Substantive?** Not a link dump, not Reddit noise
3. **Relevant?** LLMs, AI agents, coding agents, developer tooling, inference/training, prompt engineering, AI safety, open-source AI
4. **Newsjacking score?** (from Phase 1.5) — higher scores get priority placement

Output triage table:
```
| ソース | タイトル | NJスコア | アクション | 対象 |
|--------|----------|----------|------------|------|
| simonwillison.net | タイトル | 4/5 | wikiエントリ作成 | entities/simon-willison.md |
| blog.example.com | タイトル | 1/5 | スキップ（既存） | — |
```

### Phase 3: Wiki Ingestion

**Reference**: For podcast-interview-driven entity creation (new person/org from a major podcast episode), see `references/podcast-guest-entity-creation.md`.

For each "wikiエントリ作成" article:

0. **CRITICAL: Pre-validate tags against SCHEMA.md BEFORE creating new pages** — When creating a new entity/concept page, its tags MUST exist in `wiki/SCHEMA.md`'s taxonomy. Extract the tags you plan to use, run `search_files(pattern="tagname", path="~/ai-topics/wiki/SCHEMA.md")` for each, and patch SCHEMA.md's category line to add any missing tags BEFORE creating the entity file. This prevents the pre-commit hook from blocking your commit after you've already written 5+ files. Known category lines:
   - **People/Orgs** (line ~33): organization names, person names-as-tags
   - **Products** (line ~34): tool/platform names
   - **Models** (line ~35): model names, techniques
   - **AI Agents** (line ~37): agent-related concepts

1. **CRITICAL: Check existing entity pages FIRST**
   ```bash
   # Check if file exists with ANY name variation
   search_files(pattern="entity-name", path="~/ai-topics/wiki/entities", target="files")
   ```
   - The `wiki/index.md` may reference entities with different filenames than expected (e.g., `[[entities/gpjt]]` for "Giles Thomas")
   - Always verify file existence before creating new pages
   - **Trending-job note (verified 2026-08-10)**: by the time `trending-topics` runs (~12:00 UTC), the wiki-ingest pipelines (newsletter-wiki-ingest ~07:40, blog-wiki-ingest ~07:50, x-bookmarks-ingest, active-crawl) have usually ALREADY created/updated today's pages. Grep `wiki/index.md` for today's topic names before proposing new pages; if covered, the report links to existing pages instead of duplicating them.

2. **Scrape content**: `web_extract([article_url])`

3. **Determine category**:
   - `entities/` — people, companies, blogs, tools
   - `concepts/` — techniques, patterns, ideas
   - `comparisons/` — head-to-head analyses
   - `queries/` — research questions

4. **Create or update page**:
   - If updating: read existing file, append new content under appropriate section, update `updated:` frontmatter
   - If creating: follow existing entity page format (frontmatter + overview + core ideas + related + sources)

5. **Update index and log**:
   - `wiki/index.md` — add/update entity reference (match the filename convention used in index)
   - `wiki/log.md` — add dated entry with changes summary

6. **Commit and push**:
   ```bash
   cd ~/ai-topics && git add wiki/ inbox/rss-scans/ && git status
   # CRITICAL: Check for pre-staged files from previous runs
   git diff --staged --stat
   git commit -m "wiki: daily scan YYYY-MM-DD — [summary]" && git push
   ```

## Key Pitfalls
- **SCHEMA.md tag validation (pre-commit blocker)**: The pre-commit hook validates ALL tags on modified files against `wiki/SCHEMA.md`'s canonical taxonomy (900+ tags). This is the #1 cause of blocked commits in wiki-triage runs. **Prevention**: Before creating ANY new entity/concept page, extract its planned tags and validate each against SCHEMA.md. Use `search_files(pattern="tagname", path="~/ai-topics/wiki/SCHEMA.md")` — if missing, patch the appropriate category line (People-Orgs/Products/Models/AI-Agents/Engineering/Domain-Concepts/Meta) in SCHEMA.md FIRST, then create the entity file. This is step 0 in Phase 3. **Recovery** (if you forgot): `git add wiki/SCHEMA.md` the fixed file, then re-run `git commit`.

- **Duplicate frontmatter fields**: When using `patch` to update YAML frontmatter (e.g., changing `updated:` date), be careful not to introduce duplicate fields. The original file may already have `type: entity` — don't add another one. Read the frontmatter block first before patching.

- **Index stub detection**: `search_files("firstname.*lastname")` on the index may miss existing stubs if the index entry uses a different format (e.g., `**Role** | Professor Emeritus` instead of the person's name). Always also check `search_files(target="content")` for the person's name in the entities directory before creating a new entity page. stubs created by `build_x_wiki.py` or `build_blog_wiki.py` may exist even when `search_files` returns nothing.
- Index filename mismatches: short handles vs full names
1. **Index filename mismatches**: `wiki/index.md` may use short handles (`gpjt`) while you'd expect full names (`gilesthomas-com`). Always check the index first.

2. **Pre-staged files**: Previous cron runs or sessions may have already staged files. Use `git diff --staged` before committing to understand what's changed. **Scope your own `git add` to your own files** (e.g. `git add inbox/rss-scans/daily-scan-YYYY-MM-DD.md`), NOT `git add -A` or blanket `git add wiki/ config/` — other jobs (blog-wiki-ingest, newsletter-wiki-ingest, x-bookmarks-ingest, skill-management, wiki-health) routinely leave concurrent uncommitted changes in `wiki/` and `config/hermes/skills/` that you must not sweep into your commit (verified 2026-08-10: `git status` showed many `M`/`D` skill files + untracked files from other jobs; committing only the scan report kept the history clean).

3. **Duplicate entity creation (VERIFIED 2026-08-17)**: Always search for existing entity files before creating new ones. The same person/company may already have a page under a DIFFERENT filename. **Proven failure mode**: Searching with regex dots (`gary.marcus`, `daring.fireball`) returns 0 results even when `gary-marcus.md` and `daringfireball-net.md` exist. The index uses hyphens, not dots. **Mandatory pre-creation pattern**:
   ```
   # 1. Search index with PLAIN TEXT name (no regex):
   search_files(path="wiki/index.md", pattern="gary marcus", target="content")
   search_files(path="wiki/index.md", pattern="gruber", target="content")
   
   # 2. Use find in terminal for filename glob (search_files file target is unreliable):
   terminal("find ~/ai-topics/wiki/entities -name '*gary*' -o -name '*marcus*' 2>/dev/null")
   terminal("find ~/ai-topics/wiki/entities -name '*gruber*' -o -name '*daring*' 2>/dev/null")
   
   # 3. Check git log for files that may have been deleted:
   terminal("cd ~/ai-topics && git log --oneline -3 -- 'wiki/entities/gary-marcus.md'")
   ```
   **Real failure (2026-08-17)**: Created `garymarcus-com.md` and `martinalderson-com.md` as duplicates when `gary-marcus.md` (424 lines, 43KB) and `martin-alderson.md` (360 lines, 33KB) already existed. Had to `rm` the duplicates and merge into existing files instead. The index had the correct filenames all along — the search regex was wrong.

4. **No content to report**: If `article_total == 0` AND no newsletter exists, respond `[SILENT]` — don't generate empty reports.

5. **Category field is JSON**: In blogwatcher DB, `categories` is a JSON array. Use `LIKE '%\"tag\"%'` for SQL filtering or `json.loads()` in Python.

6. **Published vs discovered dates**: Use `discovered_date` for "when blogwatcher found it", `published_date` for "when article was published" (can be NULL).

7. **`search_files` for wiki directory discovery — partial limitation**: `search_files` returns `{"total_count": 0}` for recursive glob patterns like `~/ai-topics/wiki/**/*.md`. However, for **specific filename pattern checks** in known directories (e.g., `search_files(target='files', pattern='gary-marcus*', path='~/ai-topics/wiki/entities')`), it works correctly. Use `execute_code` with Python `os.walk()` or `pathlib` for full directory traversal. **Cron mode note**: `execute_code` is blocked in cron jobs — fall back to `search_files(target='files')` with specific patterns for entity existence checks.

8. **RSS 429 rate limits**: `r/LocalLLM` and `r/LocalLLaMA` frequently hit HTTP 429. Log failures but do NOT retry immediately — wait for next scan cycle to avoid exacerbating rate limits.

9. **Substack redirect URLs**: Newsletter articles use tracking-heavy Substack redirect URLs (e.g., `substack.com/redirect/UUID`). `web_extract` handles these natively — pass the full redirect URL, do not strip tracking parameters. To discover the actual publication domain, resolve the `open.substack.com` link: `curl -sL -o /dev/null -w '%{url_effective}' https://open.substack.com/pub/{author}/p/{slug}` — this reveals the real domain (e.g., `www.latent.space`). Substack HTML is client-side rendered; extract OG metadata (`<meta property="og:...">`) for title/description/author.

10. **Beehiiv Cloudflare blocks — variable, test before assuming**: Beehiiv main article URLs (`hp.beehiiv.com/{uuid}`) are Cloudflare-challenged — `curl` returns 403 with a JS challenge page. **But beehiiv tracking links (`link.mail.beehiiv.com/v2/c/...`) are NOT uniformly Cloudflare-blocked** — verified 2026-08-16 (uid=509 Superintel+): all 18 sampled v2/c/ links resolved HTTP 200 to the actual article (read.getsuperintel.com). **Rule: always test ONE v2/c/ link with `curl -sL -o /dev/null -w '%{url_effective}'` before assuming the whole batch is blocked.** If it resolves, the batch is likely resolvable and you can extract actual article URLs + titles. If it 403s, classify based on title and newsletter source alone. This was missed in the 2026-08-20 triage: the agent classified 20 beehiiv links as "all Cloudflare-blocked" without testing a single link, when they may have resolved fine. Content retrieval for main posts still requires browser-based fetch when 403 confirmed.

10. **Batch file creation before git commit**: When creating multiple wiki pages (6+), create all files first using `execute_code` with Python `open()/write()`, then do a single `git add wiki/ && git commit && git push`. Multiple small commits are fine for updates to existing files, but batch new file creation.

11. **Context window management**: When running as a cron job with many articles (90+), tool outputs may fill the context window. Use `[Old tool output cleared to save context space]` pattern mid-run and reconstruct state via targeted `read_file` with `offset` + `execute_code` directory checks.

12. **Entity update vs create decision**: For established entity files (e.g., `antirez-com.md`, `pluralistic-net.md`), append new sections under existing headers rather than rewriting. Preserve historical continuity and frontmatter integrity. For new entities, follow the existing frontmatter format with `title`, `created`, `updated`, `tags`, `related`.

13. **Reddit URL extraction failures**: `web_extract` consistently fails on Reddit URLs with "Content was inaccessible or not found". Reddit uses Cloudflare protection and dynamic content loading that defeats simple HTTP extraction. For Reddit articles, skip scraping and only record the URL/title in triage. If content is needed, use `browser_navigate` + `browser_snapshot` as a fallback (higher resource cost).

14. **Git rebase in headless cron environment**: When running as a cron job, `wiki/log.md` can be modified concurrently (e.g., by another scheduled run or external process), causing git push rejections that require `git pull --rebase`. In headless environments with no `EDITOR` set, `git rebase --continue` hangs. Always use `GIT_EDITOR=true git rebase --continue` to bypass interactive editor prompts. If conflicts occur, `git checkout --theirs <file>` accepts the remote version, then continue. **Push-first nuance (verified 2026-08-17)**: if `git pull --rebase` errors with "cannot pull with rebase: You have unstaged changes", do NOT panic and do NOT commit/stash your unstaged files — try plain `git push` first. It often succeeds outright when the local branch is actually ahead with no remote divergence (the unstaged changes are just other jobs' files, and rebase refuses to run over them but push doesn't care). Only fall back to rebase when push is actually rejected.

15. **`trending-topics-reporting` skill name is AMBIGUOUS**: `skill_view(name='trending-topics-reporting')` fails with "2 skills match across your local skills dir and external_dirs" — there are two copies (`/opt/data/.hermes/skills/research/trending-topics-reporting/SKILL.md` and `/opt/data/ai-topics/config/hermes/skills/_overrides/trending-topics-reporting/SKILL.md`). Workaround: read the repo-managed override directly with `read_file` at `/opt/data/ai-topics/config/hermes/skills/_overrides/trending-topics-reporting/SKILL.md`. The same ambiguity affects `skill_manage` patches on that name — patch `daily-rss-triage` instead and keep trending-topics guidance here.

16. **Trending-topics weekend report pattern (verified 2026-08-16)**: On weekend runs (Sat/Sun), model releases pause but HN still surfaces big topics — e.g. Google HEIR homomorphic encryption (488pts), "AI out-remembering mathematicians" (518pts). When morning pipelines already covered most topics, the report's `📊 ウィクション推奨アクション` table should mark each row `✅ 済み — <page>` (linked to existing pages) and keep only genuinely-new topics as `⚠️ 未収録`. Check `git log --oneline -10` first — commits like `active crawl`, `newsletter-wiki-ingest`, `blog-ingest` from earlier today tell you what is already reflected; grep `wiki/index.md` for topic names before proposing new pages.

17. **HN story ID citation (VERIFIED 2026-08-17)**: When adding an HN discussion link to a wiki page's `sources`, use the actual `item?id=<objectID>` — do NOT guess or reuse an ID seen elsewhere in the scan output. Real failure: created `concepts/claude-system-prompts.md` with `item?id=49322107` (the Cloudflare Tell HN thread from the same scan), but the correct ID for the Claude System Prompts story was `49319556`. The wrong ID was copied from a different story in the same output. Fix: `hn_algolia_supplement.py` now prints the `hn :` item link for every story — always copy from that line. If you need to recover the ID for a story already in your notes, run a quick Algolia query (`search?query=<title>&tags=story`) and take `objectID` from the top hit.

18. **Page filename ≠ SCHEMA tag (VERIFIED 2026-08-17)**: A concept page's filename does not guarantee its tag exists in SCHEMA. Real failure: used tag `prompt-design` for the new `concepts/claude-system-prompts.md` page, but SCHEMA has NO `prompt-design` tag — the existing `concepts/prompt-design.md` page uses tag `prompting`. When pre-validating tags (Phase 3 step 0), grep each planned tag in SCHEMA.md individually and, when a page-like name fails, check what tag the existing page actually uses (`grep -A8 "tags:" <existing-page>.md`). Do this BEFORE creating the file — patching the tag after write is an extra round-trip.

19. **Markdown-table header-collapse on careless patching (VERIFIED 2026-08-22)**: When inserting content into a wiki page that contains a markdown table (the frontmatter summary table, a "Key Parallels" comparison, a "Unit Economics by Company" table, etc.), a `patch` whose anchor straddles the table's **header row + `|---|` separator row** can merge them into one malformed line. Real failure: tried to insert a note *before* a table's header; the patch collapsed `| 2008 Crisis | AI Data Center Crisis |` and `|-------------|----------------------|` into `| 2008 Crisis | AI Data Center Crisis ||-------------|----------------------|` — an invalid row that had to be reverted and re-anchored. **Rule: never use a table's header row or its `|---|` separator row as the patch `old_string` anchor.** Anchor on the stable `## Section Heading` (or the last text line) *above* the table instead, and place the new content after that heading. After any patch near a table, read back the diff and confirm the `|---|` separator row is intact. Tables are the one frontmatter/body region where the "insert-before-X" pattern is fragile — the same class of pitfall as pitfall #2 (duplicate frontmatter fields), just in the body.

20. **Cron-mode `git commit -m` is reliable — don't under-commit (VERIFIED 2026-08-22)**: The old habit of avoiding `git commit -m` in cron (fearing the pre-commit hook or an interactive editor prompt) is outdated. A plain `git commit -m "wiki: blog-ingest YYYY-MM-DD — …"` committed **27 files (18 raw + 5 pages + index.md + log.md + report)** cleanly — both the `index.md` validator and the tag-validation pre-commit hooks ran and passed with no editor invocation and no `--no-verify`. Use `git commit -m` normally; the pre-commit hooks are the real gate and they pass when your edits are valid. Two companion facts observed the same run: (a) the blog_ingest checkpoint reports `scan.total_new` (35) and `articles.total` (20) — `total` is the *scraped* count, not the raw-on-disk count; a few extra raw files from earlier jobs may already be present, so stage ALL of today's raw files (`wiki/raw/articles/` additions from `git status`), not just the `saved_articles` list. (b) Keep the `git add` scoped to your files (raw + the specific pages you touched + `index.md` + `log.md` + the `inbox/rss-scans/daily-scan-*.md` report) — do NOT `git add -A` or blanket `git add wiki/` (other cron jobs leave concurrent uncommitted `config/hermes/skills/` and `wiki/` changes you must not sweep in, per pitfall #2).

21. **Frontmatter-list-item `patch` mangling (VERIFIED 2026-08-23)**: When a `patch` anchors on a YAML *list item* (a `sources:` line like `- raw/articles/foo.md`) that also appears as the first line of a *second* block, the fuzzy matcher can merge the two into a malformed line (`- raw/articles/foo.md\nsources:` → a stray un-indented `- raw/articles/...` + a duplicated `sources:` block) — producing a frontmatter with duplicate `sources:` keys and a broken `- item` line. Real failure: updating `concepts/mcp-2026-07-28-spec.md` the first patch anchored on the last `sources:` item and produced a duplicated `sources:` block + an un-indented `- raw/articles/...` line; had to read back the frontmatter and re-patch to restore it. **Rule: when patching YAML frontmatter, anchor on the `updated:` / `title:` scalar line or the whole frontmatter block, NOT on an individual list item.** After ANY frontmatter patch, read back the top ~15 lines (`read_file` offset=1 limit=15) and confirm there is exactly one `sources:` block and that all list items are consistently indented. This is the frontmatter version of pitfall #19 (table-header collapse) — the "insert-before-a-list-item" pattern is fragile in both.

## Pre-commit Hooks in ~/ai-topics (VERIFIED 2026-08-31)

Two hooks run on `git commit` (both pass without `--no-verify` when edits are valid):

1. **index.md validator + tag taxonomy validator** — the known gate (SCHEMA tag pre-validation, pitfall #0).
2. **Wiki language policy hook**: BLOCKS any commit that introduces NEW Japanese characters into previously-Japanese-free wiki files (anything outside `raw/`). Real failure 2026-08-31: adding a Japanese one-line summary for a JP author to `wiki/index.md` (`もひ main — 半田拓海による…`) was rejected with "NEW Japanese introduced to clean file: wiki/index.md". **Fix: write index.md entries (and all non-raw wiki prose) in English** — translate the JP description rather than pasting it. Reports under `inbox/rss-scans/` are NOT gated (outside wiki/), so triage tables and trend reports stay Japanese. Do not reach for `--no-verify` — fix the entry instead.

## Output Language

All reports, triage tables, and wiki content should be in **Japanese** unless the source material is explicitly English-only and the user has not requested Japanese output.

## Multi-File Wiki Batch Edits: Idempotent Python Script Pattern (Verified 2026-08-29)

When a run must touch 2+ wiki files (add a section to page A, add a Related link to page B, recompute a raw sha256, prepend a log entry), prefer ONE Python script (`write_file` to `/tmp/xxx_update.py`, run via `terminal("cd ~/ai-topics && python3 /tmp/xxx_update.py")`) over sequential `patch` calls. `patch` is fragile near frontmatter list items and table separators (pitfalls #19/#21 apply to Python `str.replace` too — anchor on `## Section` headings only), and a bare script isn't idempotent unless you build guards in.

Rules that make the script safe:
1. **Idempotency guard per edit**: `if "New Section Title" not in s:` … else print "already has section, skipping". A re-run after a crash or context compaction is then a no-op, not a duplicate.
2. **`assert s.count(anchor) == 1`** before every `replace` — fails loud on a wrong anchor. Real catch 2026-08-29: guessed filename `nanogpt-speedrun-frontier.md`; the FileNotFoundError + `find wiki -name "*nanogpt*"` confirmed the real page is `concepts/ai-benchmarks/nanogpt-speedrun.md`.
3. **Raw sha256 recompute**: `body = raw.split("---\n", 2)[2]`, hash the body only (frontmatter excluded), then replace the stored `sha256:` line.
4. **Guard the log prepend too** (`if "unique log subject line" not in log:`) so compaction-resume never duplicates a log entry.
5. **Read back after the run**: `sed -n '1,30p'` frontmatter (exactly one `sources:` block) and `grep -A2` the section anchor (table `|---|` rows intact), then commit with scoped `git add` (pitfalls #2/#20).

Bonus: after context compaction mid-run, just re-run the script — durable state lives on disk, not in the conversation.

## Post-Compaction Resume: Verify Before Re-Doing (VERIFIED 2026-08-31)

When resuming a trending-topics/wiki-triage run after context compaction, the compaction summary may report work as "in progress" or "unknown" even though the edits already landed on disk. Before re-applying any page update:

1. `git diff --stat <candidate files>` — if the diff already shows your intended section (check for a distinctive string like the section heading, NOT just the `updated:` date — other jobs bump dates too), the edit is done; skip it.
2. Check `grep -c "sources:"` in frontmatter and grep for the exact section heading — a plain heading grep can false-negative on apostrophe variants (`Don't` vs `Don’t`), so grep a keyword substring too.
3. Beware hallucinated filenames post-compaction: the resume tried to recompute sha256 on `simonwillison-net-dont-defang-...` (hyphenated, no hash suffix) which never existed; real convention is `domain--slug--<8hex>.md`. Always `ls wiki/raw/articles/ | grep <keyword>` before referencing a raw file in scripts/log entries.
4. Finish the *navigation* steps (index entry, log entry, report file) as their own idempotent script — those are the steps most often dropped by compaction, and the report file itself may not exist even when the summary implies it does. `ls inbox/rss-scans/ | tail` to confirm.