---
title: "OpenAI Formal Mathematics Publication Program (722 Papers)"
created: 2026-10-08
updated: 2026-10-09
type: concept
tags:
  - openai
  - mathematics
  - ai-research
  - reasoning
  - open-weight
  - ai-safety
confidence: high
sources:
  - raw/newsletters/2026-10-07-openai-revolutionizes-math-with-ai.md
  - raw/newsletters/2026-10-07-41-experiments-while-the-team-slept-what-do-we-trust.md
  - raw/articles/2026-10-08_arxiv_deepmind_math-paper-withdrawals.md
  - raw/articles/2026-10-08_openai_openai-math-repo-history-withdrawals.md
  - raw/articles/2026-10-07_ahmath_ahmath-statement-on-openai-math.md
  - raw/articles/2026-10-08_akaragila_openai-partition-principle-mathematics.md
related:
  - entities/openai
  - entities/deepmind
  - concepts/openai/reflections-on-openai
  - concepts/ai-mathematics-theorem-proving
  - concepts/station-autonomous-math-discovery
  - concepts/mathcode
  - concepts/ai-benchmarks/hle
  - concepts/academic-reception-of-ai-math
  - entities/association-for-human-mathematics
---

# OpenAI Formal Mathematics Publication Program (722 Papers)

On October 6–7, 2026 OpenAI announced (https://openai.com/index/openai-revolutionizes-math-with-ai) what it calls the first industrial-scale program of AI-generated formal mathematics: **722 Lean 4 formalized papers** covering **8,290 theorems**, of which **1,563 resolve long-standing open problems** — roughly **90% of Lean-4-formalizable open problems** in the surveyed corpus. The headline result is a formal proof of the **quasi-Riemann hypothesis** and **89 other Millennium Prize–related problems**. The model behind the run is **GPT-5.6-Codex**, and the artifacts (proofs, `proof.md` / `proof Lean.lean` pairs, READMEs with progress notes) were published on **Hugging Face** and mirrored on arXiv.

## Why this is a capability story, not a benchmark story

AI2's interpretation (https://arxiv.org/pdf/2610.00072) frames the announcement as the moment "AI capability stopped being a benchmark story and became an evidence story." Unlike SWE-bench-style evals, the 722 papers are **verifiable, citable artifacts**: a Lean 4 proof either compiles or it does not, and it does not saturate. The AI2 note "41 experiments while the team slept — what do we trust?" makes the trust argument explicitly: benchmarks degrade under optimization pressure, formal proofs cannot.

## The 400,000-worker "swept" pipeline

OpenAI describes a fully **swept** (autonomous) pipeline in which GPT-5.6-Codex ran approximately **400,000 parallel worker sessions** ("experiments while the team slept"). This is the agentic-scaling pattern applied to mathematics: no human-in-the-loop per problem, long-horizon tool use (Lean REPL interaction, library search), and massive parallelism with automatic grading by the Lean kernel.

## Independent replication within 24 hours (and the caveat)

**Google DeepMind** ran its own solver over the published corpus and reported **505 of 722 problems resolved** in its first pass, then **677** (later 678) after iteration — and **formally withdrew three of its own pre-existing papers** (related to the Weil-class / Kuga–Satake / Hodge-conjecture line) because a sign error invalidated a stabilization-trace cancellation argument that two dependent papers relied on. DeepMind also reports **~42% (300/719)** of its top-line results now machine-formalized.

The caveat matters for how much of this is "new mathematics" versus "translation work": DeepMind's withdrawals show that even carefully curated human formal libraries contain defects, and that AI-generated formalization is currently as much an **audit and mechanization engine** for existing literature as a discovery engine. The two labs' numbers (OpenAI 1,563 open problems "solved", DeepMind resolving 677 of OpenAI's 722) are **not directly comparable** — different solvers, different success criteria (full formal closure vs. partial progress notes), different problem sets — and should be read as "two frontier labs can now mechanically grind a large fraction of a formalized open-problem corpus," not as a leaderboard.

## The 24-hour withdrawal cascade (October 7-8)

The release was marketed as settled progress, but within a day the `openai/math` repo's own `history.md` recorded **three withdrawals** — *Algebraicity of Weil classes on split abelian eightfolds*, *Algebraicity of Kuga-Satake Correspondences for K3 Surfaces*, and *The rational Hodge conjecture for products of K3 surfaces* — after a sign error invalidated a stabilization-trace cancellation argument that two dependent papers relied on. A further **14 manuscripts received proof repairs** (Lipschitz heights/Ashkin-Teller, Kähler MMP/abundance, taming/hypersymplectic deformation, Box Transport, BSD), and 13 more were re-versioned to cite the corrected companions. Formalization coverage of top-line results was reported at **300/719 (~42%)**. ^[raw/articles/2026-10-08_openai_openai-math-repo-history-withdrawals.md]

## Community reaction: "power, not scholarship"

The release triggered an organized academic backlash. The **[[entities/association-for-human-mathematics|Association for Human Mathematics]]** issued a statement (Oct 7) declaring that "releasing over 700 files at once is not a demonstration of scholarship, but a demonstration of power," and accusing OpenAI of ignoring its own Advisory Group on Mathematics and AI. Set theorist **Asaf Karagila** — the domain expert on the Partition Principle vs. Axiom of Choice problem OpenAI claimed to solve — reviewed the preprint and said it "sucked," warranting desk rejection, and called the mass release "the equivalent of a Denial of Service" on the community. The next-day withdrawals retroactively strengthened these critiques. See [[concepts/academic-reception-of-ai-math]] for the full analysis.

## Open questions

- What fraction of the 1,563 "long-standing open problems" are genuinely open versus obscure/uninteresting restatements? The corpus-selection policy is not fully disclosed.
- Does Lean-kernel verification transfer credit to the model, the retrieval/strategy scaffolding, or the Lean mathlib ecosystem?
- If formal proof becomes commodity labor, what happens to the "AI did X breakthrough" framing that currently anchors AI-safety capability reports?

## Related

- [[entities/openai]] — the lab behind GPT-5.6-Codex and the publication program
- [[entities/deepmind]] — independent replication and the three withdrawals
- [[concepts/openai/reflections-on-openai]] — internal culture context for Codex
- [[concepts/ai-mathematics-theorem-proving]] — the broader Lean/autoformalization arc
- [[concepts/station-autonomous-math-discovery]] — autonomous math-discovery agent research
- [[concepts/mathcode]] — earlier code-and-math reasoning evals
- [[concepts/ai-benchmarks/hle]] — Humanity's Last Exam, the soft-eval counterpart
- [[concepts/academic-reception-of-ai-math]] — mathematicians' backlash (AHM, Karagila)
- [[entities/association-for-human-mathematics]] — the group that condemned the release
