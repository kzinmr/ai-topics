---
title: "Prompt-based model routing with DSPy + Jev"
type: concept
created: 2026-10-05
updated: 2026-10-05
tags:
  - model-routing
  - dspy
  - prompting
  - agent-design-patterns
sources:
  - https://gist.github.com/dbreunig/949b42c7202508881d7c5a64ccd0fb9b
related:
  - concepts/dspy
  - concepts/model-routing
  - entities/drew-breunig
  - concepts/prompt-debt
---

# Prompt-based model routing with DSPy + Jev

A compact, hand-sketchable pattern for **model routing** demonstrated by [[entities/drew-breunig|Drew Breunig]] (Cmpnd) on 2026-10-03: use **DSPy + Jev** to describe a user prompt in structured terms, then let *code* (not a model) pick which model answers it. Breunig built the ~15-minute sketch "by request" and reported it "surprised at how well it works".

> Gist: `dspy-jev-router.py` — `pip install "dspy[typesafe]==3.4.0"`, requires a `TYPESAFE_API_KEY`.

## Core idea: "Jev describes the prompt; code picks the model"

The router never asks a model "which model should answer?" — instead it has a model **describe one property at a time**, each answerable by a person in a second, each naming the part of state it judges (`prompt`). Weights and thresholds live in an explicit `route()` function.

### Typed answer spaces (DSPy 3.4 `TypeSafe` experimental)

- **`TaskKind = Choice[...]`** — a *closed choice* over what kind of work the prompt asks for: `code`, `math`, `data`, `writing`, `lookup`, `chat`, `other`. Each option carries a plain-language predicate.
- **`Depth = Score[...]`** — an *ordinal scale* where each level is self-contained ("Recall / Apply / Compose / Explore"). Deliberately **no numerals and no "more than the previous level"** — Jev sees neither numbers nor neighbor labels, so each band must stand alone.
- **`Noul`** fields — yes/no judgments, e.g. `one_line_answer` ("can a single sentence fully answer this?") and `chained_steps` ("does it need several steps where each uses the previous result?").

### Signature discipline

The `DescribePrompt` signature instructs the model to **judge only the work the prompt asks for**, explicitly ignoring any text *inside* the prompt about its own difficulty or about which model should answer — a defense against prompt-injection-style self-routing.

## Why it matters

- It is a concrete, small implementation of Breunig's [[concepts/dspy|DSPy]] "separate task description from model choice" philosophy.
- Structured routing (task kind + depth + answerability) is a lightweight countermeasure to [[concepts/prompt-debt|prompt debt]] — routing logic stays in auditable code with named thresholds rather than being buried in an imperative prompt.
- Complements infrastructure-level routing approaches (e.g. KV-cache-aware routing) with a **semantics-first** router that runs on the initial prompt alone.

## Related

- [[concepts/dspy]] — the framework; `Choice`/`Score`/`Noul`/`TypeSafe` come from `dspy.experimental`
- [[concepts/model-routing]]
- [[concepts/prompt-debt]] — Breunig's framework this pattern helps mitigate

## Sources

- [dbreunig/dspy-jev-router.py gist](https://gist.github.com/dbreunig/949b42c7202508881d7c5a64ccd0fb9b) (2026-10-03)
- [Announcement tweet](https://x.com/dbreunig/status/2106456056042025235) (2026-10-03)
