---
source_url: https://www.microsoft.com/en-us/research/blog/structural-priors-for-reasoning-models/
ingested: 2026-09-17
sha256: 2ddc6fd5d06510b28f891295c220846e0068af3bf45276289778db726db16a5c
---

# Structured priors for reasoning models

Microsoft Research blog post. Authors include Siddhartha Sen and colleagues (Kernel team / MSR). Published ~2026-09-09.

## Core argument

General-purpose reasoning models are strong but "expensive and slow" on every problem. For problems that recur at scale and at pace, it is cheaper to **shape the model's behavior with a "subjective prior"** rather than let it reason freely from scratch each time.

A **subjective prior** is defined as: *"a distribution over programs consistent with the structure of the domain, from the perspective of the model."* It is *subjective* because it is relative to the model's inductive biases (a "view" of the domain), not a property of the domain itself. Two levers:

1. **Domain-specific languages (DSLs)** — write a DSL so it *constrains what can be expressed*, eliminating whole classes of invalid solutions at the language level.
2. **Fine-tuning** — shift probability mass so the model prefers valid programs / reduces variance.

## The four failure modes of free-form reasoning

The post enumerates how unconstrained reasoning models break on structured domains:

1. **Hallucinated syntax / structure** — inventing APIs, fields, or grammar rules that don't exist.
2. **Wrong decomposition** — choosing an incorrect problem structure / dependency order.
3. **Inconsistent formalization** — producing semantically different formulations for the same problem across attempts.
4. **Unbounded search** — reasoning over an unconstrained solution space, which is slow and error-prone.

## Examples / evidence

- **SQL**: constraining to well-formed queries with a DSL collapses the search space; the post reports ~99% valid-syntax rates on BIRD and Spider when the grammar is enforced as a prior, versus free-form generation.
- **Kernel generation**: a prior over *valid kernel structure* (tile/block shapes, memory layout) raises the fraction of correct kernels. This connects to MSR's Kernel / form-to-code program synthesis line (see related F* / low*-style work).

## Framing

The post positions this as the classical "bias–variance" / inductive-bias tradeoff applied to reasoning LLMs: you trade a little generality (the prior is subjective, tied to a domain and a model) for large gains in reliability and cost on the recurring problems where structure is known. "Subjective" also carries a nod to the Bayesian view — priors are always *for* an agent, not objective features of the world.

## Key terms
- subjective prior / distribution over programs
- DSL-as-prior (constraint on what is expressible)
- fine-tuning-as-prior (shifts probability mass)
- form-to-code program synthesis
- valid kernel structure
