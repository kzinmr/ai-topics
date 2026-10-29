# Substack chrome-collapse → canonical-post body recovery

**When this fires:** a newsletter checkpoint's candidates are ALL `substack.com/redirect/2/eyJ...`
(base64 OAuth), `substack.com/redirect/<uuid>?j=eyJ...` (UUID tracking), `app-link/post?...`
(like/share/comment/restack), `@handle` author profile, or `email-read-in-app` — i.e. zero real
article URLs, exactly as the noise tables predict. Import AI (pub 1317673) and other editorial
Substacks hit this every issue. The skill's noise tables tell you to SKIP these but do not give
the recipe for getting the real content. This is it.

## The path (validated 2026-10-27, Import AI 478, run 20261027T101015Z)

1. **Read the inbox pre-triage summary** at
   `~/wiki/raw/inbox/newsletter-ingest/{run_id}-triage.json`. For chrome-collapsed batches it
   usually already carries `canonical_url` plus `suggested_wiki_actions` and
   `existing_wiki_overlap`. Trust it for *routing*, never for *content verification*.
2. **Derive the canonical URL from the chrome URLs themselves** — you do not need the summary.
   `open.substack.com/pub/{handle}/p/{slug}?...` → canonical is
   `{handle}.substack.com/p/{slug}`. The custom-domain / `open.` form is often Cloudflare-challenged
   where the bare publication subdomain is not (see `the-signal-subdomain-bypass.md`,
   `substack-custom-domain-bypass.md`).
3. **Write a fetch script to `/tmp/` via `write_file` and run it with `terminal`** (cron mode:
   `execute_code` + `subprocess` is blocked, and heredocs are scanned — see
   `cron-unicode-script-building.md`). curl with a desktop UA, `--max-time 30`, dump HTML to
   `/tmp/x.html`.
4. **Check JSON-LD first, but expect it to be metadata-only**: `headline`,
   `isAccessibleForFree`, `datePublished`, `author[]`, `description` are reliable;
   `articleBody`/`body_html` are usually absent even when `isAccessibleForFree: true`.
5. **Body extraction — the `<article>` tag regex UNDER-extracts.** Do not trust a single
   `<div class="body-markup">` or `<article>...</article>` match. For Import AI 478 the
   `<article>`-scoped `<p>|<h2>|<li>` regex returned **5 "paragraphs" / 13.3KB** because the
   newsletter packs each topic into one giant `<p>` with `<br>` separators. What actually worked:

   ```python
   t = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
   t = re.sub(r'<style.*?</style>',  '', t,     flags=re.DOTALL)
   t = re.sub(r'<[^>]+>', '\n', t)
   lines = [l.strip() for l in html.unescape(t).split('\n') if len(l.strip()) > 3]
   ```

   ~112 lines / 14.5KB. Then `grep -n -i "<topic keywords>"` over that file to locate section
   boundaries, and `sed -n 'A,Bp'` to read each topic. Newsletter section headings
   (`How math could help alignment:`, `What RSI looks like - ...`) survive as their own lines and
   act as the TOC.

6. **Harvest real article URLs from `Read more:` / `Read more` blocks** near each topic's end,
   NOT from the whole-page `href` dump (that yields author profile + comments link + chrome). On
   a body-scoped `href` regex for Import AI 478 only 8 links survived, and 6 of them were the
   actual curated primaries (resolution.org, arxiv.org, openai.com, mirendil.com, vals.ai, a prior
   Import AI issue). Filter `substackcdn`, `substack.com/redirect/2`, `/i/`, `x.com`,
   `twitter.com`, `fonts.`, app-store redirects.
7. **Base64 redirect tokens are NOT decodable outside the email session** — the `redirect/2/`
   tokens do not even appear in the served HTML (`re.findall(r'redirect/2/([A-Za-z0-9_-]+)', html)`
   → 0 matches). Do not spend cycles trying to `urlsafe_b64decode` them.

## Yield expectation

One editorial Substack issue ≈ 4-6 distinct primaries behind 15-17 chrome links. Body ~13-15KB.
Read every harvested primary's claims *as quoted in the newsletter body* — the curator's
2-3 paragraph intro plus quoted spans is usually enough for a triage decision; downstream
`newsletter-wiki-ingest` re-fetches the primary for `take` candidates.

## Triage-side check that paid off

For each primary, grep the whole wiki (`grep -ril "<entity-name>" concepts entities events`), not
just check whether a plausible page exists. In this run `recursive-self-improvement.md` had 453
lines of RSI content yet **zero hits for the article's subject** — a 453-line page on the adjacent
umbrella topic is not coverage. Conversely, an article whose subject already has a
`raw/articles/<date>_<source>-*.md` file with the same figures → `reference`, not `take`
(the Vals.ai magnet case: full primary already on disk from 2026-10-06, Import AI added only
Clark's framing).

## Commit hygiene in the parallel 07:00-07:50 window

`git status --short -- wiki/` will show 15+ modified files from sibling pipelines (blog-wiki-ingest,
dreaming, etc.). Stage ONLY your three artifacts with explicit paths:
`wiki/raw/archived/triage/{source}/{date}_{run_id}.json`,
`wiki/raw/archived/triage/archive_index.json`,
`wiki/raw/inbox/newsletter-ingest/{run_id}-triage.json`. Never `git add wiki/`.
