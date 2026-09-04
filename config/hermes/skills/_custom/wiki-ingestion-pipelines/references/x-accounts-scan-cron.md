# x-accounts-scan cron: agent-side procedure

Procedure the agent runs AFTER `fetch_x_accounts.py` emits its JSON
(cron job `x-accounts-scan`, ~22:30 UTC every 2 days). The script only fetches,
dedups and attaches link metadata; wiki ingestion is the agent's job.

## Steps

1. Read the summary JSON injected into the cron prompt (`new_posts[]`, handles,
   `external_urls`, link titles/descriptions, `referenced_tweet_types`).
2. Triage each post:
   - Substantial product/release/announcement content → create/update a wiki page.
   - Person-event mentions → patch the person's existing entity page.
   - Off-topic replies, thin link-dumps, legacy-doc references → skip, log the skip.
3. Before ANY ingestion, fetch full tweet context via xurl direct-ID lookup
   (see "Context retrieval" below) — the script's snippet is truncated.
4. Prefer updating existing entity pages (`grep` the entities/ dir for the person
   or org) over creating new pages. Create new event/concept pages only when the
   topic is central to the source.
5. Update `wiki/index.md` (correct section) + append `wiki/log.md` in the same
   commit. Commit: `cd /opt/data/ai-topics && git add wiki/ && git commit -m
   "wiki: x-accounts-scan — <summary>" && git pull --rebase && git push`.
6. Final response is the Japanese Discord report: per-post sections, wiki actions
   taken, sources with links, and explicit skips.

## Context retrieval (xurl)

- Conversation search for older tweets returns `result_count: 0` on the free
  tier — skip it, go straight to direct-ID lookup:
  `xurl --auth oauth2 "/2/tweets/<ID>?tweet.fields=note_tweet,created_at,public_metrics,referenced_tweets,in_reply_to_user_id,entities"`
- Follow `referenced_tweets[].id` upstream (replied_to / quoted) to find the root
  announcement — the scan output often contains only a follow-up reply whose real
  payload lives one or two tweets up (e.g. @teknium's "50% context reduced" reply
  pointed to the actual Hermes Agent v0.21.0 announcement tweet, itself quoting
  the @NousResearch release tweet).
- Do NOT pass `tweet.mode=extended` — invalid parameter, request rejected.
- `entities.urls[].description` in the lookup response already carries the release
  notes / article summary, often enough without scraping the URL.

## Report-quality pitfalls

- The script summary can report `source_posts: 0` while `new_posts[]` still
  contains linked posts — trust `new_posts[]` in the detail JSON over aggregate
  counters; verify via xurl before claiming "no links".
- `referenced_tweet_types: ["replied_to"]` means the post is a reply — its
  standalone text may be meaningless without the parent. Always fetch the parent.

## Tag taxonomy gotcha

- The pre-commit tag validator blocks non-taxonomy tags (e.g. `release` is NOT in
  SCHEMA.md; `product-release` isn't either). Safe event-page tags seen passing:
  `announcement`, org tags (`nous-research`), product tags (`hermes-agent`),
  topic tags (`context-compression`, `agent-communication`). When in doubt, drop
  the doubtful tag — `type: event` already conveys the class. Fix the tag; do not
  use `--no-verify`.

## Sibling-edit warning

- index.md / log.md are often touched concurrently by other cron jobs
  (hot-posts, health-fix, skeleton-enrich). Patch with minimal anchored
  old_string. Stage ONLY `wiki/` (never `git add -A`) — other jobs leave
  unrelated dirty state (jobs.json, skills) in the repo working tree, and
  `git pull --rebase` fails on unstaged changes; the commit itself still pushes.
