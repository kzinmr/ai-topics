# TPW curate-link take: body-fetch fallbacks & 403 framing-only (2026-10-23)

True Positive Weekly (Andriy Burkov, pub 61455 / @aiweekly) is a pure link digest —
the skill already says "skip the digest, gap-check its curated URLs, take the
primaries." When you take an individual TPW curate link you must fetch its real body
(BODY-READING MANDATE), which the digest never contains. Patterns from a 2026-10-23 run:

## Plain-blog domains are direct-curlable
Most TPW primaries are personal/company blogs. `curl -sL --max-time 20 <url>` returns
the full HTML; extract `<article>` (or full body) + strip `<script>/<style>` via a
`/tmp` python script. Validated 200 + full body:
- `jasperlu.com/blog/training-search-agents-grpo/` — 104KB, real GRPO tutorial.
- `warlock.ai/blog/warcraftsim-1/` — 1.1MB, full self-play RL writeup.

md5-based temp filenames can swap which file is which — label your extraction output
by a distinctive title string, not the filename, before trusting it.

## 403 → record as framing-only WITH a provenance caveat (do NOT skip the take)
`chapterpal.com/s/<hash>/tokenomics-…` returned **HTTP 403** (curl), and the raw
newsletter digest was a link-stub. The take is still valid because the topic
fills a genuine coverage gap and the framing is known from the curate title.
Action: write the section with what is verifiable (the framing/claim), add an
explicit **"Provenance caveat: primary returned 403, only framing recorded, re-fetch
before citing specific numbers"** note, and cite the raw digest path. This is the
paywalled/unreachable analogue of the "note `paywalled` + qualifiers" rule — same
principle for a hard-403 external page: keep the take, mark it low-confidence, never
fabricate numbers.

## Routing: pick the page that holds the SPECIFIC contribution, not the title keyword
The triage's `candidate_wiki_path` is a suggestion, verify routing:
- "Training search agents with GRPO" → NOT a generic RL page; belongs in
  `concepts/agentic-search.md` which already has a SID-1 GRPO research section — add
  the hands-on practitioner section as the complement (research-level vs tutorial).
- "self-play RL on one desktop (Warcraft)" → `concepts/spade-self-play-environments.md`
  (the self-play-scaling page), NOT a non-existent `reinforcement-learning.md`.
- "Tokenomics where tokens are used" → `concepts/agent-economics.md` (existing
  1000×-multiplier page) as the bottom-up breakdown complement.
Before creating any page: `grep -ril "<topic-keyword>" wiki/concepts/` to find the
page that already discusses the mechanism — extend it instead of a new umbrella.

## Contested same-metric figures: record both, don't overwrite
Modal interview said "$5B series C"; the entity page recorded "$4.65–4.7B" (May 2026).
Per AGENTS.md "矛盾を消さない": kept both with date/source attribution as a
"contested/updated datapoint" rather than replacing. Small but the right reflex when a
newer source restates a number slightly differently.
