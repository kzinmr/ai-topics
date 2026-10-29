---
title: "Recursive Decision Models (RDMs)"
created: 2026-10-28
updated: 2026-10-28
type: concept
tags:
  - rlm
  - decision-model
  - system-one
  - structured-outputs
  - classifiers
  - dspy
  - agent-architecture
  - inference
aliases: [RDM, RDMs, Recursive Decision Model]
related: "[[concepts/rlm-recursive-language-models]], [[concepts/system-one-models]], [[entities/raw-works]], [[entities/typesafe-ai]], [[concepts/dspy]]"
sources:
  - raw/articles/2026-10-01_raw-works_recursive-decision-models.md
  - https://raw.works/recursive-decision-models/
---

# Recursive Decision Models (RDMs)

## Summary

**Recursive Decision Models (RDMs)** apply the harness principles of [[concepts/rlm-recursive-language-models|Recursive Language Models]] — externalized context, programmatic decomposition, and bounded self-recursion — to [[concepts/system-one-models|decision models / System One models]] (like TypeSafe AI's Jev) instead of generative LLMs. The concept was introduced by Raymond Weitekamp ([[entities/raw-works|@raw_works]]) in his October 1, 2026 post on raw.works. The result is a "cascade of fans and funnels": an LLM fans out options, a decision model keeps one or two, and each one kept opens a smaller fan.

## The three non-negotiables

Weitekamp's design constraints for any RDM system:

1. **Externalized, decomposable context** — the system must externalize context and be able to programmatically decompose slices of that context.
2. **Recursive decision calling** — the decision model must have the choice to call *another decision model*, up to a maximum recursion depth.
3. **Generative-model independence** — the system must work with *and without* any generative model. It must stand alone as "pure decision models" and also compose with LLMs and agents.

## Implementation sketch (DSPy)

RDMs became expressible once the DSPy team (per Weitekamp, "my esteemed peers at cmpnd.ai") added support for the TypeSafe System One API via `dspy.experimental.Noul` / `TypeSafe`. An RDM is a `dspy.Module` that:

- makes **one request to the decision model** (`dspy.Predict(signature)`) per level;
- for each affirmative decision output, runs the same-named tool one depth level deeper;
- bounds recursion with `max_depth`.

Canonical example: a `Search` signature asking *"Is the answer stated in this text?"* (a `Noul`/boolean output) paired with a `look` tool that recursively halves the text — a decision-model-driven binary search over a handbook, with no generation involved.

Weitekamp prototyped the idea in a repo dubbed **"one-system"**, which began as a "LiteLLM for Jev" gateway before he realized recursion could be supported by composing requests through the gateway itself.

## Naming debate

Weitekamp deliberately picks "decision models" over Diogo Almeida's preferred "System One models" (Almeida argues some machine-native types are "not decisions"), noting the zeitgeist is trending towards "decision models". See [[entities/typesafe-ai]] for the Jev/System One lineage.

## Graph Structure Query

```
[recursive-decision-models] ──author──→ [entity: raw-works]
[recursive-decision-models] ──extends──→ [concept: rlm-recursive-language-models]
[recursive-decision-models] ──applies-to──→ [concept: system-one-models]
[recursive-decision-models] ──embodies──→ [concept: harness-engineering]
[recursive-decision-models] ──uses──→ [entity: typesafe-ai] (Jev via dspy.experimental.TypeSafe)
```

> Authored by [[entities/raw-works|Raymond Weitekamp]]; generalizes [[concepts/rlm-recursive-language-models]] from generative models to [[concepts/system-one-models|decision models]]; enabled by DSPy's TypeSafe System One support ([[concepts/dspy]], [[entities/typesafe-ai]]).

## Related Concepts

- [[concepts/rlm-recursive-language-models]] — the parent harness pattern (LLM + REPL + `llm_query()`); RDM swaps the generative model for a decision model.
- [[concepts/system-one-models]] — the class of fast structured-decision models (Jev) that RDMs recursively compose.
- [[entities/typesafe-ai]] — Jev / TypeSafe System One API, the decision-model substrate.
- [[concepts/dspy]] — the framework in which RDM modules are expressed (`dspy.Module`, `Noul`, `TypeSafe`).
- [[entities/raw-works]] — RAW Works / Weitekamp's research practice; also see his ypi recursive coding agent and mycelium.

## Sources

- [Recursive Decision Models](https://raw.works/recursive-decision-models/) (raw.works, Oct 1, 2026)
- Raw: `raw/articles/2026-10-01_raw-works_recursive-decision-models.md`
