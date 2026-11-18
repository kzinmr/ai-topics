# Newsletter Triage 2026-11-18 Patterns (run 20261118T101015Z)

Batch: 4 newsletters / 80 raw links (Ben's Bites "Productiv-icky", Lenny's Newsletter
"35 premium tools free for a year", beehiiv AI-chip "Plot twist: US says NVIDIA cut off the
suspect chip buyer last year", Simon Willison "Datasette in the browser"). Yield: 3 takes,
6 references, 5 skips.

## 1. Cross-pipeline dedup won again — Simon Willison Substack == blog-ingest take

Simon Willison publishes every post to BOTH simonwillison.net (blog-ingest, 07:00 UTC) and
his Substack (newsletter-ingest). The blog-domain raw was already on disk:
`raw/articles/simonwillison.net--2026-nov-17-datasette-lite--18a63a59.md`, and today's
blog-triage (`triage_latest.json`, run 20261118T100050Z, 10:30 UTC) already listed it as a
`take` along with "External sandboxes for coding agents".

**Check the blog-triage `decisions` array FIRST for any simonw Substack batch** — it is the
fastest dedup filter and catches the whole author's day. Downgrade both to `reference`
against `entities/simon-willison.md` (1115 lines, `updated:` 11-16 — a stale `updated:` date
does NOT mean the specific article is captured; the Datasette 1.0 section stopped at 1.0a42 /
datasette-maplibre and had no Datasette Lite service-worker content).

## 2. Ben's Bites is a high-yield source despite an inbox "low" rating

The inbox pre-triage rated Ben's Bites ★low / "skip unless scraping reveals a notable
launch". Scraping the custom domain post via `open.substack.com` returned 23 substantive
`<p>` paragraphs with 12 real external links, and 3 of them were genuine gaps:

- **Claude Meetings** (claude.com/resources/articles/claude-meetings) — Anthropic's meeting
  agent, ZERO grep hits across concepts/entities/events → new concept page.
- **tldraw "disposable software"** — "what's worth building when code is disposable:
  throwaway internal tools & jigs"; existing `concepts/agent-first-design.md` and
  `harness-engineering/agent-ergonomics.md` do not carry the disposable-code thesis.
- **Gamma Model Index** (research.gamma.app/2026/11/model-index) — product-side measured
  provider spend; OpenAI passed Anthropic for the first time since 2023. Rare empirical
  provider-share time series; no `model-index` page existed.

Lesson: for editorial roundups the inbox subject-line rating is near-useless; the value is
entirely in the curated link list, which only HTML extraction reveals. Never batch-skip a
Ben's Bites issue on inbox rating alone.

## 3. Pure-promo Substack can still carry one reference-worthy fact

Lenny's "35 premium tools free for a year" is 100% subscription marketing — but the
OpenRouter section contained operator metrics (11B → 1T+ monthly tokens while cutting cost
per token ~60%; 640K failed requests rerouted/month; EU zero-data-retention) plus Lenny's
own confirmation of the Stripe acquisition already recorded in `entities/openrouter.md`.
Split the single durable-fact item out as its own `reference`; batch-skip the promo body.

## 4. Beehiiv v2/c batch with no inbox article detail → topic-level batch skip

20 links, all `link.mail.beehiiv.com/v2/c/<hex>` with no `articles`/`key_claims` payload in
the inbox summary (only `importance: low` and guessed topics). Nothing resolvable, nothing
but the subject line. Same-day blog-triage had already taken Ed Zitron's "The NVIDIA Bubble",
and `export-controls` / `ai-supply-chain-security` / `ai-bubble-economics` pages exist → one
★2 batch-skip entry for all 20 links rather than 20 stub decisions.

## 5. `candidate_wiki_path` verification: use the absolute wiki root

Pre-commit validates `candidate_wiki_path`. An `os.path.exists("concepts/agentic-commerce.md")`
check executed with cwd=`~/ai-topics` reported False while the page actually existed at
`~/ai-topics/wiki/concepts/agentic-commerce.md` (10KB). Always prefix
`/opt/data/ai-topics/wiki/`. Also: `grep -rl "agentic-commerce]]"` returning only pages that
*link to* it is not proof of absence, and `ls wiki/concepts/ | grep commerce` is the cheap
correct check.
