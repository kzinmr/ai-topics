# X Accounts Scan → Wiki Ingest Workflow

Manual workflow for processing `x_accounts_latest_full.json` scan results into wiki pages.

## Input Location

`${HERMES_HOME}/cron/data/x_accounts_latest_full.json`

## JSON Structure

```json
{
  "generated_at": "ISO timestamp",
  "new_posts": [
    {
      "created_at": "ISO timestamp",
      "edit_history_tweet_ids": ["..."],
      "entities": { "urls": [...] },
      "id": "tweet_id",
      "text": "tweet text",
      "account_handle": "handle_without_at",
      "account_name": "Display Name",
      "external_urls": ["https://..."]
    }
  ],
  "errors": [],
  "scan_meta": {
    "request_budget": 12,
    "tracked_accounts": 84,
    "accounts_selected": 12,
    "accounts_scanned": 12,
    "accounts_skipped_budget": 72,
    "cursor_start": N,
    "cursor_next": N
  }
}
```

## Post Evaluation Criteria

For each post in `new_posts`, decide: **ingest**, **update existing**, or **skip**.

### Cross-Pipeline Dedup (check FIRST)

Many tracked X accounts are **also newsletter/blog pipeline sources** (Nathan Lambert/Interconnects, Simon Willison, etc.). When a post links to one of *their own* articles, that article is often already ingested by the newsletter or blog pipeline — sometimes hours earlier. Before creating/updating anything for such a post:

1. Grep concept/entity pages for the article topic or title (e.g., `grep -rl 'glm-5.3' concepts/`).
2. Read the matching page's frontmatter `sources` — if it already lists a `raw/newsletters/...` or `raw/articles/...` file for that article, AND the page body already has a section synthesizing it, the post is a **duplicate**.
3. Action: **take no wiki action** — note "already ingested via <pipeline>" in the Discord report (no duplicate raw-article save, no re-adding the blog post to the entity page).

Canonical example (2026-08-15 scan): Nathan Lambert's X post linking to "GLM-5.3: How Chinese labs keep stride with the frontier" (interconnects.ai) — the newsletter pipeline had already created `concepts/glm-5-3.md` with a full "Strategic Analysis (Nathan Lambert / Interconnects)" section and `entities/nathan-lambert.md` with the post listed. Correct action was "no action, note duplicate."

### Skip (always)
- **Replies without standalone value**: @eliebakouch replying about a paper → skip, the paper link is the value, not the reply
- **Ephemeral status/bug reports**: Posts about temporary service outages, software bugs, or status page incidents (e.g., "Claude Fable 5 is down") → skip. These have no lasting knowledge value and clutter the wiki if archived.
- ⚠️ **Thread exception**: When multiple `new_posts` from the *same account* are consecutive replies forming a coherent thread (e.g., 3-4 replies linking to related models in a family), evaluate the thread as a *group*. A thread may have standalone value even when each individual reply wouldn't. Look for: same topic across replies, shared domain/theme in URLs, 🧵 emoji or thread markers, consecutive timestamps (seconds apart). Treat the thread as one ingestion unit.
- **Non-AI domain**: microfluidics, hardware projects, personal travel updates
- **Retweets / quote tweets with no added analysis**: just resharing a link

### Update Existing (preferred over new page)
- **Link to own blog post**: check if entity page exists → add blog post to their "Blog/Recent Posts" section
- **Link to official docs**: e.g. Claude Sonnet 5 prompting guide → add to relevant entity's sources
### Conference appearance: add to entity's "Speaking Engagements" or "Overview" section

### YouTube Video Handling

When a post links to a YouTube talk/presentation, Jina Reader (`curl -sL 'https://r.jina.ai/URL' -H 'Accept: text/markdown'`) returns page metadata only — title, description, view count, publish date. It does NOT return the transcript. (Jina may emit a `401: Unauthorized` warning for YouTube URLs yet still return title, view count, publish date, and description — treat that warning as cosmetic, not a fetch failure.) The video description is typically sufficient for wiki updates: it contains the talk's core thesis, key arguments, and speaker context.

For wiki entity page updates from YouTube links:
- Add to **Speaking Engagements** section (create one if it doesn't exist) with: date, event, title, link, view count
- Add a row to **Blog/Recent Posts** table with a one-paragraph summary derived from the video description
- The description alone provides enough signal for a substantive wiki entry — full transcripts are rarely needed

If deeper analysis of the talk's content is needed, load the `youtube-content` skill for transcript extraction via yt-dlp. But for routine x-accounts-scan ingest, the description-based approach is fast and sufficient.

### Create New Page
- **arXiv paper**: always check if concept page already exists (grep `~/wiki/` for paper ID or topic). If exists, enrich with new source. If not, create concept page.
- **New tool/project blog post**: check `~/wiki/concepts/` and `~/wiki/entities/` first. Create concept page if no coverage exists.
- **Significant standalone tweet**: rare — only if the tweet itself contains novel insight (not just link-sharing)

## Workflow Steps

```
1. Read x_accounts_latest_full.json
2. For each post:
   a. Extract external_urls
   b. Check existing wiki pages (grep ~/wiki/ for URLs, handles, topics)
   c. Classify: skip / update existing / create new
   d. For "create new": fetch URL content via Jina Reader
3. Delegate to subagents (2-3 posts per subagent, max 2 parallel)
4. Subagent tasks include: read SCHEMA.md, create/update pages, update index.md + log.md
5. Verify results, commit + push
```

## Subagent Delegation Pattern

Batch posts into 2 subagents:
- **Subagent A**: New concept/page creation (research-heavy)
- **Subagent B**: Existing entity page updates (patch-based)

Provide each subagent with:
- Exact file paths to create/modify
- URLs to fetch via Jina Reader (`curl -sL 'https://r.jina.ai/URL' -H 'Accept: text/markdown'`)
- SCHEMA.md conventions reminder
- "Do NOT overwrite existing pages >40 lines — use patch to append"

## Jina Reader Fallback

When terminal `curl` is blocked in cron context, delegate URL fetching to subagents (they have terminal access in their own session).

## Cron Job Report Format (Japanese / Discord)

When the x-accounts-scan cron job fires, the final response is delivered to Discord. Use this Japanese report template:

```
## 📡 X Accounts 定期スキャン レポート (YYYY-MM-DD HH:MM UTC)

\`\`\`
スキャン対象: Nアカウント → Nアカウント選択 → 新規投稿 N件
\`\`\`

### 🔍 検出内容

**名前（@handle）** — 所属/役割 と投稿内容の概要:

| 項目 | 説明 | URL |
|---|---|---|
| ... | ... | ... |

### 📝 注目ポイント

- 技術的な意義（なぜ重要なのか）
- 投稿者の文脈（なぜこの人の発言が注目に値するのか）
- エコシステムへの影響

### ✅ Wiki 更新

- 更新したページ一覧
- 推奨される後続アクション（concept ページ作成など）

### 📊 スキャンサマリー

| 項目 | 値 |
|---|---|
| 追跡アカウント数 | N |
| 今回スキャン数 | N |
| 新規投稿 | N件 |
| 処理済キャッシュ | N（TTL N日） |
| 次回カーソル | N |
```

**Report guidelines**:
- Always use Japanese for Discord delivery
- Use emoji section headers (📡, 🔍, 📝, ✅, 📊)
- Use code block for the quick summary line
- Prioritize *why* the finding matters over *what* was found
- Include wiki action summary even if no pages were created/updated
- If zero new posts found, respond with exactly `[SILENT]` to suppress delivery
- Keep report concise — 1-3 substantive findings per report max, don't enumerate trivial posts
- When the same account has multiple posts about the same topic (e.g., an announcement + follow-up), note the effective topic count in the summary line: `新規投稿 N件（実質Mトピック）` to avoid inflating significance

## Output

- New concept pages in `~/wiki/concepts/`
- Updated entity pages in `~/wiki/entities/`
- Updated `~/wiki/index.md` and `~/wiki/log.md`
- Git commit: `wiki: ingest x-accounts scan (YYYY-MM-DD) — summary`

## Commit / push (see ingest-stage-git-sync.md)

This job produces a **wiki-content commit** (entity pages + index.md + log.md + any
new raw article), NOT a raw-only commit. The concrete procedure, the sibling-subagent
concurrent-edit hazard on `index.md`/`log.md`, and push-verification mechanics are in
`references/ingest-stage-git-sync.md` → "Wiki-content commits". Key points:

- Stage explicit paths (`git add wiki/entities/... wiki/index.md wiki/log.md
  wiki/raw/articles/...`), never `git add -A`.
- `git status --short wiki/` immediately before staging — a sibling cron job /
  subagent may have touched index.md/log.md in the meantime (fuzzy-patch usually still
  succeeds but verify the edit landed).
- Pre-commit hook validates index.md + tag taxonomy; a clean "✓ wiki/index.md clean" +
  "✅ Tag validation passed" is the success signal (no `--no-verify`).
- Verify after push: `git rev-list --left-right --count origin/main...HEAD` == `0 0`.
