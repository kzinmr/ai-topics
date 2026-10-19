# Trending-topics report filename convention (verified 2026-10-19)

`inbox/rss-scans/` uses TWO distinct filename families. Do not confuse them:

| Family | Filename | Produced by |
|---|---|---|
| Daily RSS scan triage | `daily-scan-YYYY-MM-DD.md` | daily-rss-triage Phase 1 |
| Trending-topics report | `trending-topics-YYYY-MM-DD.md` | trending-topics cron (12:00 UTC) |
| Weekly digest | `weekly-ai-digest-YYYY-MM-DD.md` | Weekly AI digest (Mon 00:00) |

The trending-topics run writes `trending-topics-*.md`, NOT `daily-scan-*.md`, even though it reuses
this skill's triage/Newsjacking methodology. Check `ls inbox/rss-scans/ | tail` before writing so you
follow the actual convention rather than assuming the daily-rss-triage name.

## Reusable trending-topics run recipe (verified 2026-10-19)

1. **State first, always**: `date -u`; `ls inbox/rss-scans/ | tail`; `git log --oneline -12`. The log
   tells you what the morning pipelines (active-crawl ~11:00, blog-wiki-ingest ~07:50,
   newsletter-wiki-ingest ~07:40, weekly digest Mon 00:00) already ingested — those topics are cited,
   not recreated.
2. **Checkpoints**: read `~/.hermes/cron/data/blog_ingest/latest.json` (`date`, `run_id`,
   `scan.total_new`, `articles.total`) and `newsletter/latest.json` (`run_id`, `processed_count`,
   `processed_messages[].subject/raw_path`). `newsletter-triage/latest.json` and
   `triage/latest.json` carry STALE timestamps (verified 10-19: May/July) — ignore them, use the
   top-level ingest checkpoints. A raw newsletter digest whose links are all
   `substack.com/app-link/post?...play_card...` is a podcast email with no extractable article body —
   classify from the subject line only, don't burn calls on the links.
3. **HN scan**: `find ~/ai-topics/config/hermes/skills -name 'hn_keyword_supplement.py'` → the file is
   a markdown doc; extract the ```python block with a regex script (write_file, no pipes), run
   `python3 /tmp/hn/hn_kw_run.py 3 80`. ALSO run `hn_algolia_supplement.py --days 2 --min-points 100`
   for the front page. Always take `ext:`/`hn:` pairs verbatim from output (pitfall #17).
4. **Top-comment mining**: for each candidate story, `https://hn.algolia.com/api/v1/items/<objectID>`
   returns `children[].text`. This is the highest-value, cheapest supplement — the reusable arguments
   live in the top 3 comments (quoted by username in the report and on the wiki page).
5. **Path verification before citing "✅ 済み"**: one batched `cd wiki && find concepts entities
   -iname '*<kw>*'` sweep per keyword (recursive from wiki root). Never derive a path from a git-log
   title or an HN headline.
6. **Wikilink verification before commit**: every `related:` frontmatter entry and every
   `[[concepts/...]]` in body must resolve to a real file — run a `test -f wiki/$p.md` loop over the
   list. Two ghost links (`concepts/agent-security`, `concepts/ai-content-detection`) had to be
   retargeted to `ai-agent-security` / `llm-text-detection-classical-ml` this run.
7. **Tag pre-validation** is still the gate: `ai-gateway` was NOT in SCHEMA (a page named
   `concepts/ai-gateway.md` uses tag `protocol`/`infrastructure`, not `ai-gateway`). Added it to the
   **Infrastructure** category line. Pre-validate with
   `python3 .githooks/pre-commit-tag-validator.py` before `git commit` — it reports violations for
   staged files without needing a commit attempt.

## Report framing that worked

Lead with a one-line thesis for the window, then 6-8 numbered topics with: bold one-line summary,
"why it matters" analysis (not a summary restatement), verbatim quotes from HN top comments attributed
by username, a `→ 新規/追記: <verified page path>` line, and `🔗 ext + HN item?id=`. Close with a
`📊 ウィキ推奨アクション` table (`✅ 本日新規` / `✅ 本日追記` / `⚠️ 未収録`) and a 総括 paragraph.
Japanese for the report; wiki pages and index entries stay English (pre-commit JP hook, pitfall in
"Pre-commit Hooks").
