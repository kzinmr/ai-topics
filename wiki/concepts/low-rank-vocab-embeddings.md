---
title: "Low-Rank Vocab Embeddings (LoRE)"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [model, transformer-architecture, optimization, training-efficiency, model-training, small-models]
sources:
  - raw/articles/gilesthomas.com--2026-10-low-rank-vocab-matrices--070bffa6.md
confidence: low
related: [concepts/llm-parameter-counts, concepts/peft-lora-and-qlora, concepts/scaling-laws, concepts/small-language-models, concepts/tokenization]
---

# Low-Rank Vocab Embeddings (LoRE)

**LoRE** ("low-rank embeddings", Giles Thomas's coinage, Oct 2026) applies the LoRA factorisation trick to the *vocab matrices* of a transformer instead of to a fine-tune adapter: replace the `vocab × d_model` weight matrix `W` with a rank-*r* pair `W′ = AB`, `A: vocab × r`, `B: r × d_model`. At `r=128` on a 50,257-token vocabulary, a 38.6M-parameter matrix becomes 6.5M — **~6× smaller** for that matrix alone. Because `Z = X(AB) = (XA)B`, the computation is a bottlenecked pass through an *r*-dimensional hidden space rather than the full embedding space.

The idea is not new (Thomas cites **Mamba-1**, "Imitating Tokens with Low-Rank Embeddings" — and deliberately avoids the clashing acronym) and he explicitly does not claim it will be adopted.

The premise is [[concepts/llm-parameter-counts]]'s ugliest fact: in small models, half the budget buys I/O, not thinking. For Thomas's 163M GPT-2-style model, embeddings (39M) + output head (39M) = **~half the parameters**; with weight tying still ~30%. Even Qwen 3.6 35B MoE spends ~1B of its 3B *active* parameters on the two vocab matrices.

## The measured result (163M GPT-2 small, 8×A100 40GB)

Two seeds (42, 123), test loss vs the no-LoRE baseline:

| LoRE placement | Param count | Test-loss delta (seed 42) | Delta (seed 123) |
|---|---|---|---|
| Input embeddings only | 130.9M (−39%) | **−0.073** | **−0.013** |
| Output head only | 130.9M | +0.138 | +0.115 |
| Both ends | 98.9M (−39%) | +0.072 | +0.101 |

Three claims survive:

1. **Output-head LoRE costs loss.** +0.115 to +0.138, worse than the +0.02–0.04 reported by Andrew Thompson (model *Maba*), who supplied the original suggestion.
2. **Input-embedding LoRE *reduced* test loss — reproduced across two independent seeds.** Losing parameters and gaining test loss is not the expected direction. Thomas's lab note: "well, that's a bit of a shocker!"
3. **Deltas are near-additive** (seed 42: −0.073 + 0.138 = 0.065 vs measured 0.072; seed 123: 0.102 vs 0.101) — i.e. the two ends are, at this scale, roughly independent interventions.

## Where the effect is *not* real: initialisation

"Smart init" (scale the inner low-rank factor by `1/√r`) was applied to the **wrong side** of the pair in the first runs. Corrected, the story partly inverts:

| Config | Test loss (wrong init) | Test loss (corrected init) |
|---|---|---|
| Output-head only | 3.737128 | 3.785209 |
| Both ends | 3.671585 | 3.741209 |

Correct init *worsened* the output-head runs and **destroyed additivity** (sum-of-parts 0.113 vs measured 0.142). Thomas's landscape image: the wrong-variance init started the model on a mountain next to a deep valley; the correct init starts it on a hill next to a shallower one. The wrong init's own signature was visible as a broken **first-step training loss** (11.8–11.9 against the expected ~10.82 = ln 50257, the perplexity of a uniform guesser) — a useful free sanity check for any vocab-matrix surgery.

So the −0.073 input-only gain is *independent* of the init bug (the input side was never touched by it) but is uncorrected-for-init in the mixed table, and the mechanism is unexplained. Plausible candidates (untested): an implicit regulariser / bottleneck on token identity, or a variance change in the token-representation distribution.

## Scaling kills the parameter argument

| Model | Vocab-matrix cost | Share of params |
|---|---|---|
| GPT-2 small 163M | ~77M | ~47% (untied) |
| Qwen 3.6 35B MoE | ~1B | 33% of *active* params |
| Kimi K3 (160k vocab, 7,168 hidden) | ~2.3B | ~2% of 104.2B active, **<0.1% of 2.8T total** |

LoRE is a **small-model intervention**. Thomas's own guess is that it degrades in usefulness with scale — unless the input-side loss improvement is real and doesn't weaken, which is the open question.

## Why this matters

- Compute ≠ parameters: input-embedding LoRE saves almost no FLOPs (embedding lookups are compute-cheap) while cutting 39% of parameters. Spend the win on a wider/deeper network or a bigger vocab, not on wall-clock.
- Any **vocab-size / multimodal-token** design decision inherits this tax — see [[concepts/tokenization]] and Neomme's factorised token embeddings.
- Methodologically: it is a worked example of an intervention whose *direction of effect* flipped on an initialisation detail, and of an author publishing the reversal. Treat every number above as **n=1 per cell, one architecture (GPT-2 small), one dataset** — `confidence: low` is deliberate.

## Open questions

- Isomorphic-compute test: output-only LoRE + 39% more tokens at matched FLOPs (Thomas notes his Chinchilla runs scaled the model ~41% / tokens 41%, so the comparison is suggestive, not clean) — see [[concepts/scaling-laws]].
- Does input-only LoRE hold at GPT-2 medium/large, and on Qwen/Mistral-style architectures (Maba is already a different architecture)?
- Is the input-side gain a bottleneck or an init/distribution artefact?

## Related
- [[concepts/llm-parameter-counts]] — the budget arithmetic that motivates LoRE
- [[concepts/peft-lora-and-qlora]] — the same factorisation, used for adaptation rather than architecture
- [[concepts/scaling-laws]] — how to spend the saved parameters
- [[concepts/small-language-models]] — the regime where this matters at all
- [[entities/gilesthomas]] — author; 46-post "LLM from scratch" series

## Sources
- Giles Thomas, "Fun with low-rank vocab matrices (and a bonus test loss reduction?)", 2026-10, https://www.gilesthomas.com/2026/10/low-rank-vocab-matrices ^[raw/articles/gilesthomas.com--2026-10-low-rank-vocab-matrices--070bffa6.md]
