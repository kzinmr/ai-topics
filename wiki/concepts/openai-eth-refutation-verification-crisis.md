---
title: "OpenAI ETH Refutation and the AI-Generated Proof Verification Crisis"
created: 2026-10-27
updated: 2026-10-27
type: concept
tags:
  - ai-in-science
  - formal-verification
  - mathematics
  - autoformalization
  - reproducibility
  - research-collaboration
  - verification
  - openai
sources:
  - raw/articles/2026-10-25_openai-math_eth-false-paper.md
  - raw/articles/2026-10-26_openai_building-scientific-understanding.md
  - raw/articles/2026-10-24_terrytao_oai-math-revised.md
confidence: medium
---

# OpenAI ETH Refutation and the AI-Generated Proof Verification Crisis

On 2026-10-25 OpenAI published a preprint claiming a **refutation of the Exponential Time Hypothesis (ETH)** — one of the most load-bearing conjectures in complexity theory — alongside two other results in harmonic analysis and quantum field theory. The episode matters less for the theorem than for what it forced: OpenAI publicly abandoned the "release the model output" model of AI-math publication in favour of **external expert shepherd groups**, and the mathematics community responded by building an independent revision infrastructure. ^[raw/articles/2026-10-26_openai_building-scientific-understanding.md]

## The claimed result

The 67-page preprint *The Exponential Time Hypothesis Is False* gives a deterministic algorithm for exactly counting satisfying assignments of an arbitrary k-CNF formula: for every fixed k ≥ 2, on a formula with n variables and m clauses it uses `poly_k(n, m)` space and runs in time

> (n + m)^{O_k(1)} · 2^{ n/(log n)^{1/2 + o(1)} }

ETH postulates that deciding 3-SAT on n variables requires 2^{Ω(n)} worst-case time, so this super-polynomial-speedup family refutes it. The paper's structure is a five-stage pipeline: a fast counting algorithm via **shared linear summaries**, construction of **low-degree replacement forms**, counting common zeros of sparse polynomial equations, then the reduction from #k-SAT to zero-counting, with appendices on partitioning satisfying assignments and exact arithmetic/space. ^[raw/articles/2026-10-25_openai-math_eth-false-paper.md]

ETH has been used as a hypothesis in hundreds of papers to derive conditional hardness across graph algorithms, computational biology, databases, and computational geometry, so a confirmed refutation reopens the hardness baseline for all of them. The claim was **verified in Lean** internally before release. Note the usual caveat: a machine-checked proof certificate establishes internal consistency of the argument as formalized, not that the formalization captures the intended conjecture.

## Three results, three release strategies

OpenAI framed its manuscripts as "a form of raw research data" and asked external experts to act as **shepherds**, each of whom advised a different release strategy:

| Result | Field | Strategy |
|---|---|---|
| Local smoothing conjecture (⇒ Kakeya + Stein restriction, all dimensions) | Harmonic analysis | Release raw AI output; let researchers self-organize |
| ETH is false | Complexity theory | Release AI output **and** fund an external explainer group |
| QFT result | Physics | Defer release of AI artifacts to the collaborators |

The ETH group is led by **Russell Impagliazzo** (UCSD), **Ramamohan Paturi** (UCSD) and **Ryan Williams** (MIT) — Impagliazzo being one of the hypothesis's originators. The group's conditions: all raw data public for independent verification, and OpenAI funding a conference on the result's implications for the field.

The four stated collaboration principles are the reusable part of this release:

1. **Transparency** — no NDAs; participants free to discuss, share intermediates, publish.
2. **No academic credit** — OpenAI claims no credit; shepherding does not imply the steward made the discovery.
3. **Recognition** — the group gets credit for the *understanding* it produces, not the discovery.
4. **Independence** — voluntary, unpaid, and participants do not speak for OpenAI.

OpenAI acknowledged the tradeoff explicitly: shepherding accelerates contextualization, but "choosing initial shepherds necessarily shapes who gets involved first and creates asymmetry of information." ^[raw/articles/2026-10-26_openai_building-scientific-understanding.md]

## The community countermove: oai-math-revised

Two days before the ETH announcement, a guest post on Terence Tao's blog announced **`oai-math-revised`** (github.com/mathcommunity/oai-math-revised), a community hub for revising OpenAI's math write-ups. Its diagnosis: the write-ups at github.com/openai/math "can be difficult to understand and can have incomplete citations." Founded by Abhinav Nellore, Johannes Schmitt, Soledad Villar and Rachel Ward, it mirrors OpenAI's repository with community-authored revisions. ^[raw/articles/2026-10-24_terrytao_oai-math-revised.md]

This is the structural novelty of the 2026 AI-math moment: verification has **forked out of the lab**. In the August 2026 wave of AI-announced open-problem advances, explanation was a lab-controlled step. By October, an independent revision layer exists that the lab does not host, edit, or endorse — a de facto peer-review pipeline for machine-generated proofs, running on the git-forge model rather than the journal model.

## Context

This sits inside a fast-moving AI-math sequence: OpenAI's 2026-08-01 announcement of ten Astra advances on long-open math/TCS problems (~$2,000 total inference cost, all Lean-certified), the 2026-08-24 Station multi-agent discovery environment, and OpenAI's earlier 2026-10-06 mathematics release. Compare [[concepts/station-autonomous-math-discovery]], which distributes discovery across agents, whereas here the distribution is across *human verifiers*.

## Open questions

- No public verdict yet on the ETH claim; the shepherding group's assessment is pending as of 2026-10-27.
- Whether "no academic credit" is enforceable in practice, or whether early shepherds accumulate citation advantage regardless.
- Whether community revision forks become a standing requirement for lab AI-math releases, or remain a one-off response to weak write-ups.
- Cost asymmetry: producing an AI proof is cheap, but the shepherding group + funded conference is expensive — the verification cost now dominates the generation cost by orders of magnitude.

## See Also

- [[concepts/ai-mathematics-theorem-proving]] — landscape page for AI theorem proving
- [[concepts/station-autonomous-math-discovery]] — decentralized multi-agent math discovery
- [[concepts/llm-price-collapse-2026]] — same fortnight's frontier-model price war
- [[entities/openai]] — the lab behind the releases
