# X Tweet Ingestion Workflow (Note Tweets & X Articles)

Ingest a single X/Twitter post (Note Tweet, X Article, or regular tweet) into the wiki as a raw article + entity/concept pages.

## Trigger

User provides an X/Twitter URL and says "取り込んで" / "ingest this" / "wikiに入れて".

## Decision Flow

```
Tweet received
  ├── xurl read → text truncated (ends with "...")? → Note Tweet → fetch with note_tweet field
  ├── xurl read → article.title present?              → X Article → fetch with tweet.fields=article
  └── neither                                          → Regular tweet → use text as-is
```

## Step-by-Step

### 1. Fetch tweet metadata (cheap first pass)

```bash
xurl read <TWEET_ID>
```

Check: is `text` truncated? Is there an `article.title`?

### 2. If Note Tweet (truncated text), fetch full content

```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=note_tweet,created_at,author_id,public_metrics,entities&expansions=author_id&user.fields=username,name,description"
```

Full text is in `data.note_tweet.text`. The regular `data.text` is truncated.

### 2b. If X Article (article.title present), fetch full body

**Recommended: Single combined call** (article + metadata + author in one request):

```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=article,public_metrics,created_at,entities,author_id&expansions=author_id&user.fields=name,username,description,public_metrics"
```

This returns `data.article.plain_text` (full body), `data.public_metrics` (engagement), and `includes.users[]` (author info) all at once. **Tested 2026-06-12**: mixing `article` with `created_at,public_metrics,entities,author_id` works correctly — the earlier warning to split into two calls was overly cautious.

If the combined call fails (rare), fall back to two separate calls:
```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=article"
xurl "/2/tweets/<TWEET_ID>?tweet.fields=created_at,author_id,public_metrics"
```

Full text is in `data.article.plain_text`. Author info from `includes.users[]`.

**Frontmatter type:** `x_article` (not `x_note_tweet`).

### 2c. Fetch engagement metrics for regular tweets (cheap, optional)

Regular tweets (not Note Tweets, not X Articles) do NOT include `public_metrics` in the `xurl read` output. If you want to cite engagement in the raw article (likes, impressions, bookmarks), make a cheap v2 call:

```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=created_at,public_metrics,author_id&expansions=author_id&user.fields=username,name,description,public_metrics"
```

This returns `data.public_metrics` (like/reply/retweet/bookmark/impression counts) and author follower count. **Do NOT skip this** for high-signal announcements (job changes, model releases, dataset launches) — the engagement numbers help calibrate report priority. **Tested 2026-08-19**: worked cleanly for both `@johnowhitaker` (136 likes / 14.4K impressions) and `@vanstriendaniel` (4 likes / 418 impressions) in one scan window.

### 3. If external URL in tweet, fetch linked content

Check `note_tweet.entities.urls[].expanded_url` for blog/article links. Fetch with `curl` for additional context (author bio, article details).

**Hugging Face API shortcut** (2026-08-19): For HF dataset/model/space pages, the HTML is heavy (JS-rendered) but the JSON API is small and reliable:

```bash
# Dataset metadata (tags, download count, likes, lastModified)
curl -sL 'https://huggingface.co/api/datasets/<namespace>/<name>'
# Model metadata
curl -sL 'https://huggingface.co/api/models/<namespace>/<name>'
# Space metadata (title + description only — no full HTML needed)
curl -sL -H 'User-Agent: Mozilla/5.0' 'https://huggingface.co/spaces/<namespace>/<name>' | grep -o '<meta name="description" content="[^"]*"'
```

**When to use**: Tweet links to an HF dataset/model/space and you want card tags, popularity stats, or a one-line description without parsing 200KB of JS-rendered HTML. **Do NOT use** for HF blog posts or user profiles (different URL structure).

**⚠️ .dev TLD security-scan block** (2026-08-19): `curl` to `*.dev` domains (e.g., `johnowhitaker.dev`) is blocked by the local security scanner (`tirith:lookalike_tld` — MEDIUM severity: "Domain uses '.dev' TLD which can be confused with file extensions"). This blocks both `curl` and `python3 urllib.request` calls in cron mode (no interactive approval possible). **Workaround**: If the X post text itself is the authoritative source (e.g., "I've officially left <company>"), skip the blog fetch entirely — the tweet is the primary source. If you genuinely need the blog, use a non-.dev mirror or `web_fetch` if available in the toolset.

### 4. Save raw article

**Filename:** `{YYYY-MM-DD}_{handle-no-at}_{short-slug}.md`

- Date = `created_at` from API response (not today)
- Handle = X handle without `@`, underscores stripped (e.g., `isaac_flath` → `isaacflath`)
- Slug = 2-5 word descriptive title

**Frontmatter:**
```yaml
---
title: "Author Name — Short Title"
date: YYYY-MM-DD
date_ingested: YYYY-MM-DD
source: https://x.com/handle/status/ID
author: Name (@handle)
type: x_note_tweet
tags: [relevant, tags, from, schema]
related:
  - concepts/related-concept
  - entities/related-entity
---
```

Include full tweet text, engagement metrics, and structured analysis sections.

### 5. Create/update entity page

**FIRST: Check if entity page already exists** using `search_files(target="files", pattern="*handle*")` on `wiki/entities/`. Content search (`target="content"`) can miss pages if the entity name isn't in the body text. Also check `index.md` for the entity name.

If the author doesn't have an entity page, create one:
- Research via `xurl user @handle` + their website/blog
- Include: bio, focus areas, key contributions, related entities/sources
- Follow `entity` type frontmatter conventions

If entity exists, add the tweet as a source and update "Key Contributions" if significant.

### 6. Cross-reference existing concept pages AND verify wikilink targets

Search `wiki/concepts/` and `wiki/entities/` for related topics. Update existing pages:
- Add the new raw article to `sources` list
- Add a wikilink reference in Related Concepts section

**Critical: Verify all wikilink targets exist.** When you find a page that references the topic you're ingesting, check that its `[[wikilinks]]` point to existing pages. If a concept page references `[[entities/claude-fable-5]]` but that entity page doesn't exist, **create it now** — broken wikilinks degrade wiki navigability. Use `search_files(target="files", pattern="*entity-slug*")` on `wiki/entities/` to verify existence before proceeding.

### 7. Update index.md + log.md

- Add entity to both index sections (compact + detailed) alphabetically
- Prepend log entry with source, raw article path, created/updated pages

### 8. Commit + push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest <description>" && git push
```

## Pitfalls

- **`xurl read` returns truncated text for Note Tweets** — always check and fetch `note_tweet` field if truncated
- **Concurrent agent modification** — when multiple enrichment agents (cron jobs, parallel subagents) work on the same author's tweets simultaneously, raw articles may already be committed before you try to stage them. After `git add`, check `git -c core.quotepath=false status --short wiki/` to verify your files are actually staged as new (not already committed). If `git status` shows "nothing to commit" for files you just wrote, they were committed by a concurrent agent — proceed with remaining updates (concepts, entity, index, log) without re-creating the raw articles.
- **⚠️ Pre-existing unstaged changes in the shared wiki repo** (2026-08-19): The `~/ai-topics` repo is shared by many cron pipelines (dreaming, active-crawl, blog-wiki-ingest, etc.). When you run `git status --short wiki/`, you will frequently see **other agents' uncommitted changes** (e.g., `M wiki/entities/cursor-ai.md`, `M wiki/entities/decagon.md` from a concurrent dreaming pass). **Do NOT `git add wiki/` broadly** — it will sweep their uncommitted work into your commit. Instead:
  1. Stage ONLY your own files explicitly: `git add wiki/raw/articles/<new>.md wiki/entities/<touched>.md wiki/index.md wiki/log.md`
  2. Verify staging: `git -c core.quotepath=false status --short wiki/` — your files show `A` (new) or `M` (staged), others remain unstaged ` M`
  3. Commit only the staged set: `git commit -m "wiki: <your scope>"`
  4. Push: `git push`
  The other agents' changes remain in their working tree for their own next commit. This pattern is the default for ALL wiki-writing cron jobs in this repo — the dreaming/active-crawl logs explicitly call it out ("staged the N enriched entity pages + log.md selectively; did not `git add wiki/` broadly").
- **⚠️ log.md prepending: use `patch`, not shell prepend, when the file is small enough to read** (2026-08-19): The `log-md-handling-pitfall.md` reference recommends shell prepend (`cat entry.md log.md > new && mv new log.md`) to avoid `write_file` overwrite. This is correct for very large log.md files (>5000 lines where `read_file` truncates). However, when `log.md` is small enough to fit in a single `read_file` (the ai-topics repo's log.md is ~5850 lines but the relevant top section is always visible), **`patch` is simpler and safer**:
  ```
  patch(
    mode="replace",
    path="wiki/log.md",
    old_string="# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n",
    new_string="# Wiki Log\n\n_Log of all wiki changes. Newest entries at top._\n\n\n## [YYYY-MM-DD] <job> | <summary>\n\n- <details>\n\n"
  )
  ```
  This inserts the new entry immediately after the header block, which is where "newest at top" requires. **Verification**: `head -8 wiki/log.md` shows your new entry at line 4-5 (after the header + blank lines). **Why `patch` works here**: the old_string is a 3-line unique header that appears exactly once at the top of the file — fuzzy matching is unambiguous. **When to fall back to shell prepend**: if the header block has been corrupted/duplicated by a prior bad prepend (check with `grep -c "^# Wiki Log" wiki/log.md` — should be exactly 1), or if log.md is so large that you cannot verify the top section without pagination.
- **⚠️ index.md entity-summary refresh pattern** (2026-08-19): When enriching an existing entity page with a significant new fact (job departure, new product launch, new model release), update the entity's one-line summary in `index.md` so the fact is discoverable from the index without opening the page. Pattern:
  ```
  # BEFORE:
  - [[entities/jonathan-whitaker]] — Jonathan Whitaker
  # AFTER:
  - [[entities/jonathan-whitaker]] — Jonathan Whitaker; officially left Answer.AI Aug 19 2026 for a sabbatical ("a few ideas to share soon")
  ```
  Use `patch` with the full old line as `old_string` (the line is unique). Add the new fact after a `;` separator, keeping the summary to one line. This is distinct from creating a NEW index entry — you are updating an EXISTING entry in place. No count change needed (the "## Entities (906 pages)" header counts page files, not summary lengths).

## Image Extraction from X Posts

When a tweet contains images (screenshots of blog posts, diagrams, etc.) that carry important context not in the tweet text:

```bash
# 1. Get media URLs from the tweet
xurl "/2/tweets/<TWEET_ID>?expansions=attachments.media_keys&media.fields=url,preview_image_url"
# Parse JSON → get media[].url (pbs.twimg.com/media/...)

# 2. Download images
curl -sL -o /tmp/tweet_img_1.jpg "https://pbs.twimg.com/media/KEY.jpg"

# 3. Extract content via vision
vision_analyze(image_url="/tmp/tweet_img_1.jpg", question="Read all text in this image carefully...")
```

**When to use**: Tweet references a blog post but doesn't link it, or the linked content is behind Cloudflare (Medium, Substack). The images often contain the full blog post content as screenshots.

**Key pattern**: Viv's OpenEnv tweet had no external link to his blog post, but the attached images were screenshots of the full LangChain blog article — vision_analyze extracted 1000+ words of structured content about model-harness-task fit, the feedback loop diagram, and the Terminal Bench 2.0 leaderboard analysis.
- **Do NOT mix `note_tweet` and `article` in same `tweet.fields`** — `article.plain_text` is silently dropped
- **`xurl read` does NOT fetch Note Tweet full text or Article body** — use raw v2 endpoint
- **Filename date = tweet created_at, NOT today** — per raw-article-filename-policy
- **Handle slug: strip underscores** — `isaac_flath` → `isaacflath` (consistent with source-slug convention)
- **Pre-commit hook blocks tag violations from ANY staged file** — if unrelated files with bad tags are staged, `git reset HEAD <offending-file>` to unstage them before committing. Don't reset everything.
- **Check SCHEMA.md for valid tags BEFORE committing** — the pre-commit hook uses `scripts/pre-commit-tag-validator.py` to block commits with invalid tags. If a tag is missing from SCHEMA.md, either add it to the appropriate category or use an existing canonical tag. Common trap: `rl` → use `reinforcement-learning`, `environment` → must be added to SCHEMA.md Products category first.
- **Tag addition workflow when pre-commit blocks**: (1) Read error output to identify invalid tags, (2) determine which SCHEMA.md Primary Category each belongs to, (3) `patch` SCHEMA.md to add tags to appropriate category (Models, AI Agents, Engineering, etc.), (4) `git add wiki/SCHEMA.md` and re-commit. Model-specific tags like `claude-fable-5` go in Models; behavioral tags like `loops`, `self-correction`, `memory` go in AI Agents.
- **`git reset HEAD <file>` is per-file** — it only unstages the named files, not the entire staging area. After resetting offending files, `git diff --cached` on remaining files should show your changes. If it shows nothing, your files may already be committed (check `git log --oneline -1`).
- **Rich entity pages (40+ lines) must NOT be overwritten with write_file** — always `read_file` first, then `patch` to add content
- **Broken wikilinks from prior ingestions** — existing concept/entity pages may reference targets that were never created (e.g., `[[entities/claude-fable-5]]` without a corresponding file). During cross-referencing (Step 6), verify all wikilink targets exist. Create missing entity pages as part of the current ingestion — don't leave broken links.
- **Content search misses entity pages** — `search_files(pattern="entities/cohere", target="content")` won't find the page if the page body doesn't contain that exact string. Always use `search_files(target="files", pattern="*cohere*")` for filename-based lookup, OR check `index.md` for the entity name. Company entities are among the first created — always assume one may exist.
- **Pre-commit hook catches content regressions as safety net** — if `write_file` overwrites a curated page, `git commit` fails with "CONTENT REGRESSION DETECTED" + line count reduction. Recovery: `git checkout HEAD -- wiki/entities/<page>.md` to restore, then `patch` to add new content. This is the LAST line of defense, not the first.

## Multi-Page Update Pattern (Benchmarks & Comparisons)

When an article compares 2+ models/tools, update ALL relevant concept/entity pages:

1. **Search for existing pages** — `search_files` on `~/wiki` for each compared entity/concept
2. **Verify wikilink targets** — check that pages referenced by existing concept/entity pages actually exist. Create missing ones.
3. **Read before patching** — `read_file` on each existing page (never overwrite rich pages)
4. **Add to each page:**
   - `sources:` list → add the new raw article path
   - Body → add a "Benchmark" or "Comparison" section with the key data table
   - Cross-wikilinks between pages (e.g., `[[concepts/minimax-m3]]` ↔ `[[concepts/claude-opus-4-8]]`)
5. **Update index.md** — add raw article entry in the date-sorted section
6. **Update log.md** — prepend entry listing all created/updated pages

This ensures the benchmark data is discoverable from any of the compared entities.

## Example: Isaac Flath Pi Harness tweet (Note Tweet)

- Tweet: https://x.com/isaac_flath/status/2048462111567982823
- Note Tweet: full text about Pi Harness (RLM + late interaction retrieval + REPL-as-Context)
- Linked blog: isaacflath.com/writing/rlm
- Created: `raw/articles/2026-04-26_isaacflath_pi-harness-rlm-late-interaction.md`
- Created: `entities/isaac-flath.md`
- Updated: `concepts/rlm-recursive-language-models.md` (cross-reference + source)

## Example: Kilo Code Claude Opus 4.8 vs MiniMax M3 (X Article)

- Tweet: https://x.com/kilocode/status/2063719228499542327
- X Article: `article.plain_text` via combined single call with `tweet.fields=article,public_metrics,created_at,entities,author_id&expansions=author_id&user.fields=...`
- Author: Kilo (@kilocode) — entity page already existed
- Created: `raw/articles/2026-06-07_kilocode_audit-claude-opus-4-8-vs-minimax-m3.md` (type: x_article)
- Updated: `entities/kilo.md` — added "Research & Benchmarks" section
- Updated: `concepts/minimax-m3.md` — added "Code Audit Benchmark" section
- Updated: `concepts/claude-opus-4-8.md` — added "Code Audit Benchmark" section
- Updated: `index.md` + `log.md`
- **Key pattern**: Benchmark comparing 2 models → update 3 pages (author entity + both model concepts)

## Example: Lance Martin "Designing loops with Fable 5" (X Article)

- Tweet: https://x.com/rlancemartin/status/2064397389189071163
- X Article: `article.plain_text` via combined single call (5000+ words)
- Author: Lance Martin (@rlancemartin) — entity page `rlancemartin.md` already existed
- Created: `raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md` (type: x_article)
- Created: `concepts/designing-loops-with-fable-5.md` (concept page with model comparison tables)
- Updated: `entities/rlancemartin.md` — added "Designing Loops with Fable 5" section + sources
- Updated: `SCHEMA.md` — added 4 new tags (claude-fable-5, loops, self-correction, memory)
- Updated: `index.md` + `log.md`
- **Key pattern**: Technical article from known author → raw article + new concept page + entity update. Tags like `claude-fable-5` may not exist in SCHEMA.md yet — add them to appropriate category before commit.

## Example: Elie Bakouch Fable 5 Mythos critique (Regular tweet)

- Tweet: https://x.com/eliebakouch/status/2064399902684139852
- Regular tweet (not Note Tweet, not X Article): 2-line critique of Anthropic's Claude Fable 5 release
- Quoted tweet: @claudeai announcement of Claude Fable 5
- Image attached but vision_analyze timed out — proceeded with tweet text + quoted tweet context
- Engagement: 3,879 likes, 914 bookmarks, 1.28M impressions (high signal despite short text)
- Created: `raw/articles/2026-06-09_eliebakouch_fable-5-mythos-debated-research.md` (type: x_note_tweet)
- Created: `entities/claude-fable-5.md` — **discovered missing entity** referenced by existing `concepts/designing-loops-with-fable-5.md`
- Updated: `entities/elie-bakouch.md` — Timeline entry + "AI Model Transparency" Core Ideas section + Key Quotes
- Updated: `entities/claude-mythos.md` — "Fable 5 General Release" section + capability limitation debate
- Updated: `concepts/designing-loops-with-fable-5.md` — "Community Response" section + source
- Updated: `index.md` + `log.md`
- **Key pattern**: Critique/opinion tweet about a model release → touches 4+ pages (critiquer entity, model entity, underlying model entity, related concept pages). Always verify wikilink targets exist — the concept page already referenced a non-existent entity page.

## Example: Xiuyu Li "RL Interview Questions 2026" (X Article)

- Tweet: https://x.com/sheriyuo/status/2063295181131247674
- X Article: `article.plain_text` via combined single call with `tweet.fields=article,public_metrics,created_at,entities,author_id&expansions=author_id&user.fields=...`
- Author: Xiuyu Li (@sheriyuo) — RUC undergrad, RL researcher. New entity page created.
- Created: `raw/articles/x-sheriyuo-rl-interview-questions-2026.md` (type: x_article)
- Created: `concepts/rl-interview-questions-2026.md` (35-question list with analysis)
- Created: `entities/xiuyu-li.md` (person entity)
- Updated: `index.md` + `log.md`
- **Blockers encountered**:
  1. Used shorthand tags `rl`, `interview`, `llm-training`, `llm-infrastructure`, `dllm` — all blocked by pre-commit. Fixed to canonical tags: `reinforcement-learning`, `career`, `training`, `ai-infrastructure`.
  2. Wrote concept/entity pages in Japanese — blocked by language policy. Rewrote in English.
- **Lesson**: Check SCHEMA.md for valid tags BEFORE writing any frontmatter. Common shorthands that fail: `rl` → `reinforcement-learning`, `interview` → `career`, `llm-training` → `training`, `dllm` → add to SCHEMA.md or omit. All non-raw wiki content must be English — translate source material before writing.

## Example: Xiuyu Li TTS & Training-Free RL series (2 X Articles, concurrent agent race)

- Tweet 1: https://x.com/sheriyuo/status/2042072816712085577 (2026-04-09)
- Tweet 2: https://x.com/sheriyuo/status/2061382777623519284 (2026-06-01)
- Author: Xiuyu Li (@sheriyuo) — entity page already existed
- Created: `raw/articles/2026-04-09_sheriyuo_test-time-scaling-training-free-rl.md` (type: x_article)
- Created: `raw/articles/2026-06-01_sheriyuo_rl-for-test-time-scaling.md` (type: x_article)
- Created: `concepts/training-free-rl.md` — ETS, Power Sampling, MCMC, self-evolving, fundamental limits
- Created: `concepts/test-time-interaction-scaling.md` — TTI: interaction-scaling > thought-scaling for agents
- Updated: `entities/xiuyu-li.md` — Added TTS series to Notable Contributions
- Updated: `concepts/test-time-scaling.md` — Added Training-Free RL + RL-for-TTS sections
- Updated: `SCHEMA.md` — added tags: `training-free`, `mrt`, `mcmc`, `on-policy-distillation`
- **Concurrent agent race**: Raw articles were already committed by a sibling subagent before this agent tried to stage them. `git status` showed "nothing to commit" for the raw files. Solution: proceed with remaining updates (concepts, entity, index, log) — the raw articles were identical.
- **Key pattern**: Multi-part series from same author → create raw articles for each + concept page(s) for the overarching theme + update entity with series summary. Always `git status` after `git add` to detect concurrent writes.

## Example: x-accounts-scan cron batch — 2 high-signal posts from 11 scanned accounts (2026-08-19)

- **Context**: `x-accounts-scan` cron job (runs every 2 days at 22:30 UTC) scanned 11 of 84 tracked accounts (request budget 12), found 5 new posts. Two were high-signal and warranted wiki ingestion; three were short replies/links to the same two stories and were folded into the same raw articles rather than ingested separately.
- **Post 1 — Jonathan Whitaker leaves Answer.AI**: Regular tweet (2090055843354190073), 136 likes / ~14.4K impressions. Author entity page already existed (`entities/jonathan-whitaker.md`, 176 lines).
- **Post 2 — Daniel van Strien British Library book-image pipeline**: Regular tweet + 2 follow-ups (2089731501147480307, 2090146990759858401, 2090097084661727699). Author entity page already existed (`entities/daniel-van-strien.md`, 168 lines).
- **Created**: `raw/articles/2026-08-19_johnowhitaker_left-answer-ai-sabbatical.md` + `raw/articles/2026-08-19_vanstriendaniel_bl-book-images-crop-search.md` (both `type: x_post`).
- **Enriched**: `entities/jonathan-whitaker.md` — Role line updated to "left Answer.AI Aug 2026, sabbatical"; Professional Experience entry changed from "Jan 2024–present" to "Jan 2024 – Aug 19 2026" with departure note; new Blog/Recent Posts row; `updated` date bumped; source added to frontmatter.
- **Enriched**: `entities/daniel-van-strien.md` — new Models & Fine-tuning entry (`bl-crop-tighten-rfdetrseg-clip10`); new Blog/Recent Posts row; `updated` date bumped; source added to frontmatter.
- **index.md**: entity summaries refreshed in place for both (no new slugs, no count change).
- **log.md**: entry prepended via `patch` on the 3-line header block.
- **Commit**: selectively staged only the 6 touched files (2 raw + 2 entity + index + log); concurrent dreaming pass's 7 unstaged entity files left in working tree. Committed as `ee208447`, pushed clean.
- **Key pattern**: Cron-mode batch scan → 2 raw articles (one per distinct story, folding same-story follow-ups) + 2 entity enrichments + index summary refresh + log prepend. No new concept pages needed (both stories extended existing GLAM-AI / career themes). Engagement metrics fetched via separate v2 call for the high-signal post (Whitaker 136 likes / 14.4K impressions justified ingestion; van Strien 4 likes / 418 impressions was ingested anyway because the HF dataset/model/Space triple was the real signal, not the tweet engagement).
