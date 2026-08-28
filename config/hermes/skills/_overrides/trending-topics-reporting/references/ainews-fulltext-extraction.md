# AINews Full-Text Extraction (open.substack.com)

**When to use**: An AINews digest subject looks substantive (model launch, security incident, governance, agent infra) but the digest's `substack.com/redirect/*` URLs are dead — the standard case.

## Recipe

1. Newsletter filename carries the subject verbatim: `2026-08-08-ainews-zawinski-s-law-of-multiagents.md`
2. The open.substack.com URL pattern: `https://open.substack.com/pub/swyx/p/<slug>` where slug ≈ filename minus the date prefix (`ainews-zawinskis-law-of-multiagents`)
3. Fetch and strip (two-step, curl-to-file; `curl | python3` is blocked in cron mode):
```bash
curl -sL --max-time 25 "https://open.substack.com/pub/swyx/p/<slug>" -o /tmp/zaw.html
```
Then in Python: strip `<script>`/`<style>` blocks, strip tags, `html.unescape()`, collapse whitespace, then anchor on the subtitle text (e.g. "a quiet day lets us find some connections") to skip nav chrome.
4. The body contains the full digest **including the AI Twitter Recap section** — a curated scan of ~544 Twitters / 12 subreddits with engagement numbers (554K views, 13.9K likes).

## Why it matters

- AINews is now a section of Latent Space (swyx). Paid posts may show partial gating, but the Twitter Recap section was fully readable in the 2026-08-08 instance.
- The recap functions as a **free daily X-scan substitute** — replaces a manual `xurl search` sweep (Phase 3c fallback) when the active-crawl note is absent (6+ consecutive days as of 2026-08-08).
- Treat recap items as confirmed signals with engagement data; cross-check with HN Algolia point queries for ★ calibration.

## Worked example 2026-08-08

Subject: "Zawinski's Law of MultiAgents" → fetched open.substack.com → surfaced 4 of 8 report topics:
- OpenAI Astra escalated to "critical" cyber status under Preparedness Framework (OpenAI News 8/8, HN 188pts/181c)
- Zawinski's Law of MultiAgents coined (swyx) + Claude Code cross-session messaging (554K views) + auto mode default (89% dangerous-command detection)
- SWE-bench Pro harness analysis by @joelniklaus (rank correlation -0.05; 26B model in right scaffold ≈ 744B in wrong one)
- Databricks internal AI coding spend controls (~90% reduction, HN 255pts/214c)
- Also: LangChain Managed Deep Agents beta, Prime Intellect multi-agent RL, Cloudflare AI Gateway unification, T3 Code 250+ PRs

## Quick HN top-stories calibration (complement to Algolia)

A cheap "what's hot right now" scan that worked cleanly on 2026-08-08: fetch the Firebase topstories list + top ~30 items to see current point leaders (surfaced DeepSeek ARC 662pts, OpenAI cyber 188pts, DOE Genesis 259pts, Databricks 255pts):
```bash
curl -s --max-time 25 "https://hacker-news.firebaseio.com/v0/topstories.json" -o /tmp/hn_top.json
# then fetch https://hacker-news.firebaseio.com/v0/item/<id>.json for each id (score/title/url/descendants)
```
Complements `search_by_date` targeted queries (which are recency-ranked and miss items whose title lacks your keywords).

## Pitfalls

- Paid-subscriber content may be partially gated; if the anchor text isn't found, fall back to the subject line + HN Algolia.
- The `open.substack.com` URL from the digest email (with `?utm_*` params) works; the `substack.com/redirect/*` ones don't.
- Future-dated blogwatcher DB entries still appear in range queries — verify the URL is live with curl before treating as signal.
