---
title: "Google Cogentic: Multi-Agent Proof Discovery and the Classical-Factoring Question"
created: 2026-11-26
updated: 2026-11-26
type: concept
tags:
  - ai-in-science
  - mathematics
  - formal-verification
  - multi-agent
  - cryptography
  - gemini
  - google
  - autoformalization
  - ai-research
confidence: medium
sources:
  - raw/articles/2026-11-26_google_cogentic-research-papers.md
  - "https://news.ycombinator.com/item?id=50642086"
  - "https://news.ycombinator.com/item?id=50643065"
  - "https://arxiv.org/abs/2609.40324"
related:
  - concepts/openai/formal-math-publication-2026
  - concepts/ai-mathematics-theorem-proving
  - concepts/complexity-theory-ai-breakthrough-2026-11
  - concepts/inference-side-channel-model-communication
---

# Google Cogentic: Multi-Agent Proof Discovery and the Classical-Factoring Question

On 2026-11-25 Google Research published a batch of preprints under
`google-research/google-research/cogentic_research_papers` — including a **deterministic
subexponential-time integer factorization algorithm** and discrete-logarithm results (HN 494 pts /
357 comments). A companion single paper, "Unconditional Integer Factorization in Subexponential
Time," reached the front page separately (HN 50651627). The method paper is **"Cogentic:
Multi-Agent Orchestration for Automated Proof Discovery"** (arXiv 2609.40324).

## What Cogentic is

Per the most-upvoted thread summary (david-gpu), Cogentic is **a harness, not a model**: existing
LLMs collaborate on a conjecture through a central orchestrator plus a **shared database of
intermediate proofs**. The batch was produced using **Gemini 4 Argon**. That makes it the third
distinct production pattern for AI mathematics in three months, alongside OpenAI's bulk Lean-4
publication pipeline ([[concepts/openai/formal-math-publication-2026]]) and the single-result
human-led-with-AI style of the Alpöge/Anthropic Riemann Hypothesis proof
([[concepts/ai-mathematics-theorem-proving]]).

One practitioner read of the architecture generalizes beyond math: "I think we'll see a move from
grep to code servers where the server is also the conduit between the subagents for coding too"
(wood_spirit) — the shared-proof-table is an agent-collusion substrate as much as a math tool
(compare [[concepts/inference-side-channel-model-communication]]).

## Why it does not break RSA — the numbers that ended the thread

The crypto panic that ran alongside it (see below) was deflated inside the thread by concrete
complexity accounting:

> GNFS would take 10^47 operations while this takes 10^2572 for a 4096 bit RSA key. The only
> improvement here is that this is guaranteed to work for arbitrary numbers. My money would be no
> [for breaking normal RSA key sizes]. Elliptic curve cryptography already uses a different
> mechanism that isn't susceptible to factorization improvements. — vlovich123

"Subexponential" is a *asymptotic-class* claim, not a practical attack: the result is guaranteed to
terminate for arbitrary inputs at a cost that remains astronomically above the number-field sieve.
cogman12's definitional correction is also worth keeping: "'Post quantum' really just means
'doesn't rely on integer factorization'."

## Human review as the differentiator

The reception detail that separates this release from the October OpenAI cohort: the Google papers
**are reported to be reviewed by human experts before publication** (Aaron Rotenberg, on Aaronson's
thread), though they **do not** come with Lean formalizations — the inverse of OpenAI's
machine-checkable-but-unreviewed profile. Comment #1 on the Aaronson post adds a second quality
signal: "this most recent wave of papers is becoming actually readable, as opposed to the messy AI
slop of the previous waves," which Aaronson partially confirmed ("quite readable introductions, but
I haven't yet made it far into any of them").

A supply-chain caution attached to the Lean side of the same debate: "There have been a lot of
cybersecurity bugs discovered in Lean recently though. So consider the supply chain about this for
transitive trust" (Jake A).

## The career question the thread actually argued about

The highest-engagement sub-thread was not about cryptography but about theoretical-CS careers —
"You never know if your thesis is going to be the next OpenAI/Anthropic and now Google trophy paper"
(edumucelli) versus "Can a PhD in math or theoretical CS not be about using models and agents to more
efficiently explore ideas? ... not at risk of being scooped" (brandonpelfrey). Note the ordering:
both sides now treat **lab trophy papers as the exogenous shock** to a theory career, and the
disagreement is only about whether tooling is a survivable niche. That is a large shift from the
2025 framing in [[concepts/academic-reception-of-ai-math]], where the objection was legitimacy,
not priority.

## Open questions

- No independent re-verification of the factoring or discrete-log preprints had appeared as of
  2026-11-26; "human reviewed" is a reported process claim, not an artifact (no Lean, no public
  machine check).
- Which claims are new mathematics versus rediscovery of known subexponential results is unresolved
  in-thread.
- Whether the shared-proof-table harness generalizes to software engineering (wood_spirit's
  prediction) is untested.

## Related

- [[concepts/complexity-theory-ai-breakthrough-2026-11]] — the OpenAI/Anthropic results that
  triggered the crypto-rumor wave this page is the skeptical counterweight to
- [[concepts/openai/formal-math-publication-2026]] — the industrial-scale Lean pipeline, and the
  October withdrawal cascade that sets the trust baseline
- [[concepts/ai-mathematics-theorem-proving]] — the broader autoformalization arc
- [[concepts/agent-collusion-public-infrastructure]] — shared substrates as collusion channels
