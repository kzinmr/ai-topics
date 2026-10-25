# Pure-link-digest newsletter: take the curated links, not the curation

Validated 2026-10-23 (True Positive Weekly #183, Andriy Burkov, pub 61455 / @aiweekly).

## The apparent contradiction
The skill's "Non-AI Content to Skip" says pure link-digest newsletters (TPW / AI Weekly)
should be **skipped immediately** because the body is a shallow bullet list with no editorial
analysis. That rule targets the **curation itself** — do NOT create a wiki page *for the
newsletter as a source*, and do NOT treat Burkov's 1-line bullet descriptions as content depth.

But that does NOT mean all 20 link items are skips. TPW's curated **external links** frequently
point at primary-source articles that sit directly in the wiki's core (agent economics, agentic
RL, search-agent training). Evaluate each curate link **on its own merits**, exactly like any
other article, and `take` the ones that fill a real coverage gap.

## Decision logic
1. Resolve the newsletter POST page (for TPW use `open.substack.com/pub/aiweekly/p/true-positive-weekly-NNN` — it returns the bullet list + every external URL in `href=`).
2. Strip substack noise + footer/social links (linktr.ee, etc.).
3. For each remaining external URL, run the normal BODY-READING + coverage-gap check.
4. `take` any link whose target fills a genuine gap (verified by reading the target's own page, not the TPW bullet). Mark the source as "TPW curate link" and tell downstream to **re-fetch the target body** (TPW bullets are 1-line, so `body_excerpt` is a paraphrase, not the real opening — flag for downstream enrichment).
5. `skip` the rest (self-help color, finance-specialized, toy items, vendor product pages).

## Concrete yields from TPW #183 (all became takes)
- **Tokenomics: Quantifying where tokens are used in agentic software engineering** (chapterpal.com) -> `concepts/agent-economics.md` — token-spend breakdown of coding agents, absent from cost-estimate-centric pages.
- **Training search agents with GRPO** (jasperlu.com) -> `concepts/agentic-search.md` — GRPO RL recipe for tool-using search agents.
- **WarcraftSim: Beating Warcraft III's hardest AI with self-play RL on one desktop** (warlock.ai/blog/warcraftsim-1) -> `concepts/reinforcement-learning.md` — small-compute self-play counterpoint to Modal's large-GPU RL.

Skipped from same issue: Felix Rieseberg "how to be more ambitious" (self-help), Jane Street AR-diffusion market data (finance-specialized, AR-diffusion general coverage already in `entities/siyan-zhao.md`), Reddit "1.5 years of RAG in fintech" (weak primary source), 14-byte NN maze (toy), Datadog Toto 2 (off-core time-series).

## Net lesson for the skip rule
"Skip pure link digests" = skip the digest AS A WIKI SOURCE, not skip the link targets. Keep the
skip-rate guidance for the curation layer (~85% skip is still expected — most TPW links are
already-covered or off-core), but always run the per-link gap check before committing all to skip.
