---
title: "OpenAI Math Preprint Race (November 2026)"
created: 2026-11-25
updated: 2026-11-25
type: concept
tags:
  - openai
  - mathematics
  - ai-research
  - reasoning
  - ai-safety
  - formal-verification
  - autoformalization
  - lab-marketing
  - ai-reputation
  - priority-dispute
confidence: medium
sources:
  - raw/articles/2026-11-25_openai_openai-math-matrix-multiplication-exponent.md
  - raw/articles/2026-11-25_openai_openai-math-vp-vnp-preprint.md
  - "https://news.ycombinator.com/item?id=50637220"
  - "https://news.ycombinator.com/item?id=50632756"
related:
  - concepts/openai/formal-math-publication-2026
  - concepts/ai-mathematics-theorem-proving
  - concepts/academic-reception-of-ai-math
  - entities/openai-astra
---

# OpenAI Math Preprint Race (November 2026)

In late November 2026 OpenAI's `openai/math` GitHub preprint channel produced two results in
two days that were received as the strongest single-lab TCS/math week of the year — and, in
parallel, the sharpest escalation of the lab-vs-lab **priority race** that began with the
October 2026 publication program (see
[[concepts/openai/formal-math-publication-2026]]).

## The two results

| Preprint | Posted | Claim | HN |
|---|---|---|---|
| "The matrix multiplication exponent is nine fourths" | Nov 24, 2026 | omega = 9/4 = 2.25 exactly (both upper and lower bound), plus ~8 further results in the same drop | 705 pts / 388 comments |
| "VP and VNP are different" | Nov 23, 2026 | VP != VNP separation; OpenAI states it solved it **before** Anthropic | 94 pts / 92 comments |

The matrix-multiplication item is the one that drew frontier attention: commenters noted the
post is "8 other results" beyond the headline, and that the significance is the **exactness**
of the bound rather than the upper bound alone.

## The notation fight was the top thread, not the math

A large share of the 388-comment thread argued about the HN title rather than the proof:

- orlp: "Title is incorrect (it says O(n^2.25) …), we already knew that, and that's not what
  this result describes. It should be Θ(n^2.25), or the original title."
- krackers: "Annoyingly the Wikipedia page doesn't even mention the previous improved upper
  bound from their October results."
- tczMUFlmoNk: "…'Being Θ(n^2.25)' is a property of a function, not an algorithm, and not a
  problem"; hansvm replied that the shorthand is standard once the implicit optimal-algorithm
  function is made explicit; henrymerrilees added that "the pesky epsilon in the upper bound
  means it isn't big-theta either".
- vlovich123 questioned soundness for rectangular sizes, where the lower bound is below 2.25
  while 2.25 remains an upper bound.

Read as signal: a general-audience headline about a complexity-theory constant generated a
thread in which the most-upvoted content was professional mathematicians correcting the
statement of the result. This is the same reception pattern the "verification DoS" critique
predicted ([[concepts/academic-reception-of-ai-math]]).

## The priority dispute and its verification gap

The VP != VNP post's framing — "we solved it before Anthropic" — turned the release itself into
a race dispute. Commenters focused on the mechanism rather than the theorem:

- uptrails: OpenAI and Anthropic are "doing the same thing: spending tens of millions to
  destroy a small but prestigious academic community in order to generate PR that's
  disproportionate to the actual value of the generated proofs", the only difference being
  that OpenAI tweets about it less; separately, "It is vitally important for us to know which
  of the two companies with nearly-identical AI models spent more tokens than the other on
  every open problem in math."
- The anti-sleeper-proof mechanism being discussed is **commitment before disclosure**: publish
  or timestamp hashes of results in advance. layer8 noted labs "don't even need to publish the
  hashes in advance … if they timestamp them using a trusted TSA"; urban referenced reversible
  hashing tooling in `smhasher` as a toy analogue.
- case540 pushed the plain open-science position: "How does anyone think OpenAI not releasing
  results is a good thing. Release results."
- theseamusjames (outside math): "Maybe the most surprising thing … has been how much ego there
  is in these discoveries … it definitely feels like it's the prestige that's really motivating
  people."

No independent verification of either November preprint had appeared at the time of writing,
and both landed on a channel whose October cohort saw 3 withdrawals plus 14 repairs inside 24
hours. `confidence: medium` accordingly.

## Open questions

- Does the 9/4 result survive peer review / Lean formalization, and does it imply anything for
  rectangular-matrix exponents?
- Will either lab adopt advance cryptographic commitment (TSA-stamped hashes) as the norm for
  AI-generated priority claims, making the race auditable instead of narrated?

## Related

- [[concepts/openai/formal-math-publication-2026]] — the October 722-paper program this race grew out of
- [[concepts/ai-mathematics-theorem-proving]] — capability survey across geometry/complexity/group theory
- [[concepts/academic-reception-of-ai-math]] — AHM objection + Karagila "verification DoS"
- [[entities/openai-astra]] — the model family doing the proving
