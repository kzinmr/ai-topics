# X Accounts Scan → Discord Report Template

Template for the Japanese-language Discord report produced by the `x-accounts-scan` cron job. Use this structure when generating the final report.

## Report Structure

```
## 📡 X Accounts Scan レポート — YYYY-MM-DD (HH:MM UTC)

### スキャン概要
| 項目 | 数値 |
|------|------|
| 追跡アカウント | N |
| スキャン実行 | N / N（予算消化）|
| 新規投稿 | **N件** |
| エラー | N |

### 🔥 主な発見

#### 1. Account Name (`@handle`) — テーマ見出し 🏷️

**① Project/Topic Name — 一言説明**
- 箇条書きでポイント（日本語、簡潔に）
- 🔗 [URL](URL)

**② Second Topic**
- ...

> 💡 **評価**: なぜ重要か・AI/エージェント分野での位置づけを1-2文。

#### 2. Next Account...

---

#### N. その他ピックアップ

| アカウント | 内容 | AI関連度 |
|-----------|------|---------|
| Name (`@handle`) | 簡潔な説明 | ⭐⭐〜⭐ |

### ✍️ Wiki 更新内容

| 操作 | ファイル | 内容 |
|------|----------|------|
| ✏️ 更新 | `entities/xxx.md` | 説明 |
| 🆕 作成 | `concepts/xxx.md` | 説明 |
| 🆕 保存 | `raw/articles/xxx.md` | 説明 |
| 📋 更新 | `index.md` · `log.md` | 更新反映 |

**コミット**: `abc1234` — `wiki: ...`

### 📊 トレンド観測

1. **テーマ1**: 説明
2. **テーマ2**: 説明
```

## Formatting Conventions

- **Language**: Japanese throughout (report body, evaluations, table headers)
- **Emoji**: Use sparingly — section headers (📡, 🔥, ✍️, 📊) and topic markers (🛠️, 🎙️, 🔒) only
- **@handles**: Always include with backtick code formatting (`@handle`)
- **Links**: Use `🔗` prefix for external links, keep URLs compact
- **Evaluations**: Each major discovery gets a `> 💡 **評価**:` block — 1-2 sentences max, focused on AI/agent relevance
- **AI関連度**: Star rating (⭐〜⭐⭐⭐) for items in the misc section. ⭐ = tangential, ⭐⭐ = somewhat relevant, ⭐⭐⭐ = directly AI/agent
- **Wiki update table**: Use emoji for operation type — ✏️ update, 🆕 create, 📋 index/log
- **Commit hash**: 7-char short form

## Content Selection Rules

1. **Prioritize posts with external URLs** — pure text posts rarely warrant wiki pages
2. **Skip replies** unless they contain standalone value — see "Reply Evaluation Heuristics" below
3. **Group by account** — if one account has multiple posts, present them together
4. **De-prioritize non-AI content** — Python libraries, desktop toolkits, open-source governance → "その他ピックアップ" section only
5. **Save raw articles** for any blog post that gets wiki attention (entities updated or concepts created)

### Reply Evaluation Heuristics

When evaluating whether a reply has standalone value (rule #2), ask: **"If you strip the @mentions and reply context, does this post still communicate something meaningful?"**

| Signal | Action |
|--------|--------|
| Links to a **new model release, tool, or project** (HF repo, GitHub repo, launch page) | ✅ Has standalone value — process it |
| Links to a **substantive blog post or paper** by the author | ✅ Has standalone value — process it |
| Links to **minor docs update, changelog entry, config tweak** | ❌ Skip — "その他ピックアップ" at most |
| Pure text reply (opinion, agreement, critique) without external link | ❌ Skip |
| Multiple replies from same account forming a **coherent thread** (same topic, consecutive timestamps) | Evaluate as group — may have standalone value together |
| Reply linking to author's own previous work (e.g., "we updated this") | Check if the linked content is new or already captured in wiki |
| Non-AI domain link (general software, personal projects unrelated to AI/agents) | ❌ Skip |

**Example from 2026-07-31 scan**:
- Daniel Han reply "Lossless UD-Q8_K_XL is out!" linking to HF model page → ✅ processed (new model quantization)
- Dax Raad reply "updated:" linking to privacy docs page → ❌ skipped (docs-only, no new substance)

## Wiki Update Workflow During Scan

When processing new posts for wiki updates:

1. **Check entity page exists** — search by handle substring first (e.g., `dbreunig` → may be `drew-breunig.md`):
   ```bash
   grep -rl 'handle_name' ~/wiki/entities/ 2>/dev/null
   ```
2. **Read existing entity page** before patching — never overwrite rich pages
3. **Scrape linked articles** → save to `wiki/raw/articles/YYYY-MM-DD_domain_slug.md`
4. **Patch entity pages** with new projects, writings, timeline entries
5. **Update related concept pages** if the post references relevant concepts (e.g., GEPA, DSPy)
6. **Update `updated` dates** in frontmatter of all modified pages
7. **Append to `log.md`** and update `index.md` entry description
8. **Commit + push** with descriptive message: `wiki: x-accounts scan — <summary>`

## Commit & Push Pitfall

`git pull --rebase origin main` **fails** in `~/ai-topics` when the working tree has pre-existing unstaged changes (which is common — other cron jobs leave `AGENTS.md`, `config/`, `skills/` dirty): `error: cannot pull with rebase: You have unstaged changes.` Do **not** stash, do **not** commit the unrelated files, and do **not** treat this as a blocker. The pre-commit hook validates index.md + tags on commit, so after `git add` of your wiki files + `git commit`, just run a plain `git push` — it succeeds (fast-forward) even when the rebase attempt failed. Verify with `git log --oneline -1` and the push output line `main -> main`.

Also: stage **only** the files this scan touched (`git add wiki/...` explicitly, never `git add -A`) — the repo routinely carries unrelated in-flight changes from other jobs.

## Example

See the 2026-07-25 scan report for a full worked example with 12 new posts across 6 accounts.
