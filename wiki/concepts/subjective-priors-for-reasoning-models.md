---
title: "Subjective Priors — Structuring Reasoning Models with DSLs and Fine-Tuning"
aliases: ["structural priors for reasoning models", "subjective prior", "form-to-code program synthesis"]
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [reasoning-model, reasoning, domain-specific, fine-tuning, program-synthesis, ai-agents]
sources: [raw/articles/microsoft-structural-priors-2026.md]
confidence: medium
---

# Subjective Priors — Structuring Reasoning Models

Microsoft Research's framing of a persistent cost/reliability problem with general reasoning
models: for problems that recur at scale, it is cheaper and more reliable to *shape* the
model's behavior with a domain prior than to let it reason freely every time.

## Definition

A **subjective prior** is *"a distribution over programs consistent with the structure of the
domain, from the perspective of the model."* It is *subjective* in the Bayesian sense: the prior
is always relative to an agent's inductive biases, not an objective property of the domain. The
goal is not to make the model "know more" but to concentrate probability mass on programs that
respect a known structure.

Two levers install such a prior:

1. **Domain-specific languages (DSLs)** — design the language so it *constrains what can be
   expressed*, ruling out whole classes of invalid solutions at the syntax/grammar level.
2. **Fine-tuning** — shift the model's probability mass toward valid programs and away from the
   long tail of free-form generations.

## Why free-form reasoning breaks (four failure modes)

1. **Hallucinated syntax/structure** — inventing APIs, fields, or grammar rules that do not exist.
2. **Wrong decomposition** — picking an incorrect problem structure or dependency order.
3. **Inconsistent formalization** — producing semantically different formulations for the same
   problem on different attempts.
4. **Unbounded search** — reasoning over an unconstrained solution space, which is slow and
   error-prone.

Each of these is precisely what a well-chosen prior removes: a DSL eliminates (1) and shrinks
(4); fine-tuning mitigates (2) and (3) by making the preferred decomposition habitual.

## Evidence cited

- **SQL**: enforcing a well-formed query grammar as a prior yields ~99% valid-syntax rates on
  BIRD and Spider, versus error-prone free-form generation. (See [[concepts/data-analysis-agents]].)
- **Kernel generation**: a prior over *valid kernel structure* (tile/block shapes, memory layout)
  raises the fraction of correct kernels — part of MSR's broader "form-to-code" program-synthesis
  line for high-assurance code.

## Framing

This is the classical **inductive-bias / bias–variance** tradeoff re-applied to reasoning LLMs:
you give up some generality (a prior is tied to a specific domain *and* a specific model — hence
"subjective") to buy large gains in reliability and cost on the recurring, structured subset of
problems. It complements test-time scaling ([[concepts/test-time-scaling]]) — priors reduce the
search that test-time compute would otherwise brute-force.

## Open questions

- How subjective is "subjective"? Priors tuned for one model may not transfer to another.
- Where is the boundary between a hand-designed DSL prior and a learned one (fine-tuning)?
- Does a strong prior hurt on out-of-distribution problems that need to *escape* the structure?

## Related
- [[concepts/reasoning-models]] — the general class the prior is trying to discipline
- [[concepts/test-time-scaling]] — complementary: brute-force search vs. structured search
- [[concepts/data-analysis-agents]] — SQL/DSL domain where the prior pays off
- [[concepts/fine-tuning]] — one of the two levers for installing the prior
- [[concepts/sycophancy]] — a contrasting case of an unwanted prior baked in by training
