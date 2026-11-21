# Blog-ingest session notes — 2026-11-17

Run `20261117T100008Z`: 39 scanned, script saved 18, agent supplement saved 2 → 20 total.

## Technique: recovering `unsaved_articles` (agent supplement)

The blog_ingest script sometimes leaves items in `unsaved_articles` (paywall-ish, scraper rejection, title-only items). The ingest agent should recover them with a manual curl+python extract instead of leaving them unsaved:

1. `curl -sL --max-time 60 -A "Mozilla/5.0" <url> -o /tmp/<name>.html`
2. Extract with python (stdlib only, heredoc form `python3 - <<'EOF'` — double-quoted `python3 -c "..."` breaks on quotes inside regexes):
   - **Substack (dwarkesh.com etc.)**: body starts at `class="body markup"`; strip `<script>/<style>`, convert `</p|div|h#|li|blockquote|pre>` → `\n\n`, then `re.sub(r'<[^>]+>','',...)` + `html.unescape`. Cut trailer at `More from` / `Ready for more?`. Keep the intro + `Watch on YouTube...` line, the `Timestamps` block, and the `Transcript` section; drop the `Sponsors` ad block (find `\n\nSponsors\n` and jump to `Transcript\n`).
   - **simonwillison.net quotation posts**: they are ~300 chars — a quote + attribution. Strip the `Simon Willison's Weblog / Newsletter / Sponsored by:` header and the `Recent articles` tail. Keep them anyway; small raw files are fine.
3. Filename: match the script's convention `domain--path-slug--md5(url)[:8].md` (compute `hashlib.md5(url.encode()).hexdigest()[:8]`, path slug = `re.sub(r'[^a-z0-9]+','-', path.lower())`).
4. Frontmatter must match script output exactly: `title`, `url`, `fetched_at` (UTC iso), `source` (blog name, not domain), `tags: [blog, raw]`.

## Checkpoint mutation after agent supplement

After saving supplements, update BOTH checkpoint files — `latest.json` AND the run archive `blog_ingest_<run_id>.json`:
- Move entries from `unsaved_articles` → `saved_articles` with `raw_path` filled in (add `saved_by_agent: true` to distinguish).
- Set `unsaved_articles: []` so downstream blog-triage doesn't re-flag them.
- `articles.total_saved` = len(saved_articles).

## Git hygiene in this repo

- Many other cron jobs leave uncommitted changes in the worktree (other jobs' `wiki/entities/*.md` modifications, untracked newsletters). Only `git add wiki/raw/articles` + `git add wiki/log.md` — never `git add wiki/` blindly, or you'll commit half-written pages from other jobs.
- `wiki/log.md` is prepend-style: insert after the `_Log of all wiki changes. Newest entries at top._` header line.
- Commit messages: `wiki: blog-ingest <date> <UTC> — N raw articles (<highlights>)`.
- Push in separate commits is fine (raws, then log).

## Reporting

Final response = Japanese report with a highlights table (article | why notable), counts (script vs agent supplement), checkpoint/commit hashes, and the `COST_REPORT:` line.
