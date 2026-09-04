# Substack Redirect-Stub Title Discovery (validated 2026-08-03, extended 2026-08-05)

When `open.substack.com/pub/{pub}/p/{slug}` returns HTTP 200 but only a ~1.3KB stub page, the `<title>` element contains the **canonical redirect URL with a `?triedRedirect=true` suffix**. Use the title as a discovery mechanism to find the canonical domain, then re-fetch it directly.

## Symptom
- curl `open.substack.com/pub/robotic/p/latest-open-artifacts-23-laguna-s21` → HTTP 200, html size ~1345 bytes
- `<title>` = `https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21?triedRedirect=true`
- No `<article>` paragraphs, no JSON-LD headline, no external links

## Distinguish from other stub patterns
| `<title>` pattern | Meaning | Action |
|---|---|---|
| `https://...?triedRedirect=true` | Redirect stub to canonical custom domain | Parse title → strip query param → re-fetch canonical URL |
| `Just a moment...` | Cloudflare challenge | Skip immediately (no auth available to solve) |
| Tiny page, login/subscribe prompt | Paywall interstitial | Skip or use section-heading technique |

## Fix
1. Extract `<title>` from the stub HTML
2. Strip the `?triedRedirect=true` query parameter → canonical URL
3. curl the canonical URL directly
4. Full JSON-LD (headline, date, authors, isAccessibleForFree) + `<article>` paragraphs become available

## Validated (batch 1: 3 publications, 2026-08-03, all resolved to full bodies)
- `open.substack.com/pub/robotic/p/latest-open-artifacts-23-laguna-s21` → `www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21` (Interconnects = Nathan Lambert's publication, pub_id=48206; co-author Florian Brand)
- `open.substack.com/pub/thesignal/p/deepseeks-flash-sale-googles-gemini` → `thesignal.substack.com/p/deepseeks-flash-sale-googles-gemini`
- `open.substack.com/pub/hugobowne/p/open-weight-ai-is-becoming-infrastructure` → `hugobowne.substack.com/p/open-weight-ai-is-becoming-infrastructure`

After canonical re-fetch: 188KB–300KB HTML, JSON-LD present, 16–37 substantive paragraphs (sufficient for BODY-READING MANDATE).

## Validated (batch 2: 3 publications, 2026-08-05, all resolved to full bodies)
Newsletter-triage run 20260805T101419Z: three Substack posts returned redirect stubs on the first `open.substack.com` pass; canonical re-fetch returned full article bodies (69 / 37 / 50 paragraphs respectively). Batch pattern: when several `open.substack.com/pub/{pub}/p/{slug}` links all return stub titles, re-fetch each canonical domain — do NOT assume the links are dead.

- `open.substack.com/pub/swyx/p/unpacking-chatgpt-work` → `www.latent.space/p/unpacking-chatgpt-work` (Latent Space / swyx; guest post by Shlok Khemani — 69 paragraphs, deep ChatGPT Work architecture analysis)
- `open.substack.com/pub/bensbites/p/what-my-agent-knows-about-me` → `www.bensbites.com/p/what-my-agent-knows-about-me` (Ben's Bites; 37 paragraphs)
- `open.substack.com/pub/lenny/p/what-if-youre-not-supposed-to-have` → `www.lennysnewsletter.com/p/what-if-youre-not-supposed-to-have` (Lenny's Newsletter; 50 paragraphs, but paid-gated body — Molly Graham guest post, non-AI)

Notes from batch 2:
- The canonical domains (`latent.space`, `bensbites.com`, `lennysnewsletter.com`) are the publications' own custom domains, not `*.substack.com` — the stub title is the reliable discovery mechanism when the custom domain is not known in advance.
- Extraction used the `<article>` + `<p>` regex approach (see `references/substack-article-body-extraction.md`): strip scripts/styles, filter paragraphs with len > 40 chars, also capture `<h1>/<h2>` headings for section structure.
- Even when the stub title resolves, `NO_TITLE` may appear in the re-fetch if the canonical page returns redirect HTML again — check the extracted paragraphs count (69 paras = success) rather than the title field alone.

## Resolve-once / slice-read pattern (batch triage, 2026-08-05)
For batches of 3+ newsletter URLs, resolve all of them ONCE into a `/tmp` JSON dict (`{name: {title, headings, paras}}`) via a single write_file+terminal script, then read specific index ranges per analysis pass with `python3 -c "import json; d=json.load(open('/tmp/file.json')); [print(f'{i}:', p[:300]) for i,p in enumerate(d['name']['paras'][start:stop], start=start)]"`. Benefits: (1) URLs fetched exactly once, no re-fetch cost when you need paras 35-69 after reading 0-34; (2) context stays small — only the slice you're currently analyzing enters the window; (3) the `/tmp` JSON doubles as the source for the `body_excerpt` fields in the final triage JSON. This is the batch analogue of the concurrent `read_file` pattern for raw-article files.

## Relationship to other fallbacks
- Complements `references/substack-custom-domain-bypass.md` (Cloudflare-blocked `open.substack.com`, known custom domains like `latent.space`) and `references/substack-publication-patterns.md` (`substack.com/home/post/p-{post_id}` fallback).
- The redirect-stub title is a **discovery mechanism**: it works even when you do NOT know the canonical domain in advance — the stub tells you where to go. Try it before guessing domain names.
- Interconnects canonical domain: `www.interconnects.ai` (substack pub handle "robotic"). Applies to its `p/{slug}` posts and to AINews-adjacent roundups.

## Archive-path symlink note (same run)
`archive_triage.py` may print a nested success path like `/opt/data/.hermes/home/ai-topics/wiki/raw/archived/...` while the file actually lands at the canonical `/opt/data/ai-topics/wiki/raw/archived/...`. `/opt/data/.hermes/home/ai-topics` is a symlink to `/opt/data/ai-topics` — verify with `ls` at the canonical path before treating the save as a nested-path failure (distinct from the triage-JSON `expanduser` pitfall, where the nested save is a real bug). In the 2026-08-05 run the archive printed the nested path but `stat -c '%i'` confirmed identical inodes (1320737) for both paths — same file, no fix-up needed.
