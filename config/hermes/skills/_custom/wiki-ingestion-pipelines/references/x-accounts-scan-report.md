# X Accounts Scan Report Template

Japanese-language report format for the `x-accounts-scan` cron job. Delivered to Discord.

## Report Structure

```markdown
# 📡 X Accounts Scan レポート — YYYY-MM-DD

**スキャン時刻**: YYYY-MM-DD HH:MM UTC
**スキャン対象**: {total}アカウント中 {scanned}アカウントをスキャン（予算制約）
**新規投稿**: {total_posts}件（重複排除後 {unique_articles}記事）

---

## 🔥 最重要記事

### {priority_number}. {author}「{title}」
📅 {date} | 👤 @{referrer_handles} が共有

{3-5 bullet points of key findings in Japanese}

📄 [wiki: {page_name}]({github_url})
📄 [{external_title}]({external_url})

---

## 🛠 その他の開発関連

### {number}. {author}「{title}」
📅 {date} | 👤 @{referrer}

{1-2 sentence summary}

📄 [wiki: {page}]({url})

---

## 📊 Wiki更新サマリー

| 種別 | ページ | 操作 |
|------|--------|------|
| 🔵 Concept | `{slug}` | **新規作成** |
| 🟢 Entity | `{slug}` | 更新（{what was added}） |
| 📄 Raw | {count}記事 + {count}論文 | **新規保存** |

**コミット**: [`{short_hash}`]({commit_url}) — {files_changed}ファイル、+{lines_added}行

---

## 🔍 トレンド分析

{2-3 paragraphs in Japanese identifying themes across this week's scan}
```

## Priority Assignment

| Marker | Criteria |
|--------|----------|
| 🔥 最重要 | Major policy essays, breakthrough research, widely-shared thought pieces |
| 🛠 その他 | Tool releases, minor updates, niche technical posts |

## Section Organization

Group articles by importance, not by contributor. When multiple tracked accounts share the same article (e.g., @mitsuhiko and @badlogicgames both sharing Amodei's essay), list all referrers and present the article once.

Articles that don't warrant full wiki pages (release notes, refreshed old posts) get brief mentions in the その他 section.

## Wiki Update Summary Table

Track every wiki action:
- 🔵 Concept pages (created/updated)
- 🟢 Entity pages (created/updated)  
- 📄 Raw articles (saved count)
- 📄 Raw papers (saved count)

Include the commit hash with link to GitHub.

## Trend Analysis Section

Synthesize 2-3 paragraphs identifying:
1. Cross-cutting themes across this batch
2. How they connect to broader AI ecosystem trends
3. What to watch for in coming weeks

Use Japanese throughout.
