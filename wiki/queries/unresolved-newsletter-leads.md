---
title: "Unresolved Leads — Newsletter Coverage Pending Primary Sources"
created: 2026-11-01
updated: 2026-11-03
type: query
tags:
  - newsletter
  - reproducibility
  - epistemology
  - ai-research
  - research
sources:
  - raw/newsletters/2026-10-31-two-ai-labs-say-they-refuted-eth.md
  - raw/newsletters/2026-11-02-who-is-hacking-europe-s-supermarket-freezers.md
---

# Unresolved Leads — Newsletter Coverage Pending Primary Sources

Holds newsletter-derived claims that were triaged but could **not** be ingested into a
wiki page, either because the source body was unreachable (expired tracking tokens,
Cloudflare challenges, paywalls) or because the claim could not be corroborated by a
primary source. Each entry records what was seen, what was checked, and what would
resolve the lead. This page exists so unreachable-but-relevant coverage is archived
rather than silently dropped.

Entries are ordered newest first. When a lead is resolved, move its content to the
owning concept/event page and mark the row `resolved` with a date rather than deleting it.

## Open leads

### 2026-11-02 — "🧊 Who Is Hacking Europe's Supermarket Freezers?" (Superintelligence, getsuperintel.site, uid≈869)

| Field | Value |
|---|---|
| Subject | `🧊 Who Is Hacking Europe's Supermarket Freezers?` |
| Sent | 2026-11-02 (received via newsletter-ingest run `20261103T101038Z`) |
| Raw | `raw/newsletters/2026-11-02-who-is-hacking-europe-s-supermarket-freezers.md` (tracking URLs only, no body) |
| Links | 20 total: `link.mail.beehiiv.com/v2/c/` tracking URLs + subscribe/social variants |
| Body access | **Unreachable.** Sampled v2/c/ links (Link 1, Link 2) returned HTTP 200 Cloudflare `Just a moment...` challenge pages. Direct-slug guesses on `getsuperintel.site` / `read.getsuperintel.com` fell back to beehiiv's generic ~203KB 404 template. No inbox pre-triage summary available for this run. |
| Triage decision | reference → this page (newsletter-triage 2026-11-03) |

**Topic-level assessment.** Food cold-chain IoT security — subject suggests a
cybersecurity/physical-infrastructure story, not AI/LLM core. No obvious connection point
to existing agent/security pages at subject level. Per the AI-scope rule this stays a
*durable lead* rather than a take; if a later issue or canonical URL reveals an
AI-agent angle (e.g. agentic exploitation of IoT fleets), re-evaluate.

**To resolve this lead.**
1. Check the publication's beehiiv public archive (`getsuperintel.site` archive listing)
   for the verbatim subject line once Cloudflare stops challenging.
2. If the body shows an AI/agent dimension, create or extend the relevant security
   concept page and mark this row `resolved` with a date.

### 2026-11-01 — "Two AI Labs Say They Refuted ETH" (beehiiv uid=861)

| Field | Value |
|---|---|
| Subject | `Two AI Labs Say They Refuted ETH` |
| Sent | 2026-10-31 (received via newsletter-ingest run `20261101T101032Z`) |
| Raw | `raw/newsletters/2026-10-31-two-ai-labs-say-they-refuted-eth.md` (78 lines — tracking URLs only, no body) |
| Links | 16 total: 15 × `link.mail.beehiiv.com/v2/c/` tracking URLs + 1 × `beeiivstatus.com` status pixel |
| Body access | **Unreachable.** 3 sampled v2/c/ links returned HTTP 403 with a Cloudflare `Just a moment...` challenge page (~7KB), including with a browser User-Agent. Per-link kill switch exhausted; the block was batch-level, not per-URL. |
| Inbox classification | `importance: high`, `newsjacking_score: 4`, topics `ai-for-math, automated-theorem-proving, formal-verification, contested-claims` |

**What the wiki already covers.** [[concepts/openai-eth-refutation-verification-crisis]]
(2026-10-27, `confidence: medium`) documents OpenAI's 67-page *The Exponential Time
Hypothesis Is False* preprint, the Impagliazzo/Paturi/Williams shepherd group, the
`oai-math-revised` community fork on Terence Tao's blog, and the Lean-verification
caveat. It is sourced from three primary artifacts (the PDF preprint, OpenAI's
`building-scientific-understanding` post, Tao's guest post).

**What would be genuinely new.** The subject says **two** labs. The existing page
records exactly one lab (OpenAI) and a *human* verification crisis, not a second
independent refutation. A confirmed second lab (DeepMind / AlphaProof-style prover, or
an independent group) announcing its own ETH refutation would be a distinct, page-changing
development — it would shift the story from "one contested lab claim under shepherding"
to "convergent independent claims", which materially changes the credibility assessment
and the verification-cost argument in the Open questions section.

**Verification attempts (all negative, 2026-11-01).**
- HN Algolia story search on the exact subject, on `refuted ETH exponential time
  hypothesis`, and on `ETH refutation AI lab` → **zero matching stories**.
- DuckDuckGo HTML search on the exact quoted subject → no organic results parsed.
- No primary source (preprint, lab blog post, Lean artifact) could be located.

**Decision.** Not ingested. Per the single-source rule for "AI disproves X" claims, a
403-blocked newsletter subject line is not sufficient evidence to append a
contested claim to an already-`confidence: medium` page — especially when the only
available description of the claim comes from a curator whose own summary could not be
read. The inbox pre-triage also flagged an unresolved ambiguity worth noting: it
speculated ETH could mean the Erdős Tree / Happy Ending conjecture rather than the
Exponential Time Hypothesis. Resolving that ambiguity requires the body text, which is
unavailable, so even the *topic* of the newsletter is not confirmed.

**To resolve this lead.**
1. Search the verbatim subject line for a beehiiv public archive
   (`<publication>.beehiiv.com/archive`) to identify the publication behind uid=861.
2. Check arXiv cs.CC for an ETH-refutation submission dated after 2026-10-31 from an
   author set not matching the OpenAI preprint.
3. Check [[entities/google-deepmind]] and the official DeepMind blog for an
   ETH/complexity-theory post.
4. If a primary source appears, update
   [[concepts/openai-eth-refutation-verification-crisis]] with a dated, contested-framed
   "Second independent claim" section (per AGENTS.md: keep the older interpretation with
   date and source rather than replacing it), and mark this row `resolved`.

## See Also

- [[concepts/openai-eth-refutation-verification-crisis]] — the page this lead targets
- [[concepts/ai-mathematics-theorem-proving]] — landscape for AI theorem proving
- [[entities/terry-tao]] — host of the `oai-math-revised` community fork
