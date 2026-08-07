---
title: "Constrained Decoding"
type: concept
aliases:
  - constrained-decoding
  - constrained generation
  - grammar-constrained decoding
created: 2026-04-25
updated: 2026-08-07
tags:
  - concept
  - structured-outputs
  - inference
  - llm-output
  - reasoning-model
sources:
  - raw/articles/2026-05-10_fireworks-ai_constrained-generation-with-reasoning.md
  - https://fireworks.ai/blog/constrained-generation-with-reasoning
related:
  - concepts/structured-outputs
  - concepts/sglang-structured-generation-language
---

# Constrained Decoding

## Overview

Constrained decoding (constrained generation) is a technique in natural language processing where a language model's token generation is **restricted to only tokens that do not violate a predefined output structure** (JSON schema, grammar, regex, BNF). Instead of generating free-form text and validating afterward, constraints are enforced **during generation**, guaranteeing schema-valid output on the first pass.

The technique is the inference-side counterpart to the broader [[concepts/structured-outputs]] paradigm (which also includes validate-and-retry approaches). It is also closely related to grammar-constrained generation as implemented in engines such as [[concepts/sglang-structured-generation-language]].

## How It Works

The core mechanism is manipulating the model's next-token prediction space:

- **Token restriction**: at each decoding step, the logits are masked so only tokens that keep the output valid under the constraint are eligible (e.g., only `{`, `"`, digits, or a specific closing bracket depending on the schema state).
- **Acceleration side-effect**: constrained decoding can *simplify* the next-token prediction space — in structured generation tasks some token generation steps can be **skipped entirely** (boilerplate sections such as `"field": ` are emitted deterministically), so the model only generates the necessary parts of the output.
- **Efficiency claim**: by reducing the complexity of the generation task and narrowing the prediction space, models can generate structured text more quickly and with greater accuracy.

## Constrained Generation in Reasoning Models (DeepSeek R1 pattern)

Fireworks' February 2025 technical article ("From text to task: Constrained generation for structured extraction in R1") documented the interaction between constrained generation and **reasoning models** such as DeepSeek R1:

- R1 generates a reasoning process enclosed within `<think>` / `</think>` tokens, followed by a JSON-formatted output.
- **The JSON schema constraint applies exclusively to the JSON section that follows the `<think>` tags** — the reasoning chain is free-form, while the final structured output is schema-valid.
- The caller can use simple output parsing to separate the reasoning section from the structured output.
- This gives a "reasoning JSON mode": transparent chain-of-thought + guaranteed machine-readable output.

### Fireworks API pattern

Fireworks exposes this via an OpenAI-compatible API with a Pydantic schema passed as `response_format`:

```python
client = OpenAI(base_url="https://api.fireworks.ai/inference/v1", api_key=os.getenv("FIREWORKS_API_KEY"))

class QAResult(BaseModel):
    question: str
    answer: str

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-r1",
    messages=messages,
    response_format={"type": "json_object", "schema": QAResult.model_json_schema()},
    max_tokens=1000,
)
```

## Applications

Fireworks demonstrated three structured-extraction use cases with DeepSeek R1 in Reasoning JSON Mode:

1. **Structured Q&A** — schema-valid question/answer pairs (Pydantic `QAResult` pattern above).
2. **Healthcare records** — AI-generated structured clinical documentation with reasoning, enabling integration into medical systems (clinical documentation, decision support, automated reporting).
3. **Computer system specifications** — structured hardware recommendations with consistent fields.

## Why It Matters

- **Reliability**: enforcing predefined formats (JSON mode, grammar-based constraints) ensures outputs are coherent, schema-valid, and machine-readable — no fragile post-hoc parsing.
- **Transparency + structure combined**: reasoning models display their thought process *and* emit a parseable result, which improves interpretability without sacrificing integration.
- **Actionability**: structured generation makes model outputs more actionable, verifiable, and seamlessly integrable into existing workflows.

## Graph Structure Query

```
[this-concept] ──part-of──→ [concept: structured-outputs]
[this-concept] ──relates-to──→ [concept: sglang-structured-generation-language]
[this-concept] ──implemented-by──→ [entity: fireworks-ai]
```

This section informs graph queries: constrained decoding is one of the two approaches under [[concepts/structured-outputs]] (the other being validation/coercion), implemented in production by [[entities/fireworks-ai]] for reasoning-model JSON mode, and by grammar-constrained engines such as [[concepts/sglang-structured-generation-language]].

## Related Concepts

- [[concepts/structured-outputs]] — parent paradigm (validation vs constrained decoding)
- [[concepts/sglang-structured-generation-language]] — grammar-constrained generation engine
- [[concepts/serialization-llm-structured-output-ai-engineering]] — serialization angle on structured output

## Sources

- [From text to task: Constrained generation for structured extraction in R1 — Fireworks AI](https://fireworks.ai/blog/constrained-generation-with-reasoning) (published 2025-02-01; raw: [[raw/articles/2026-05-10_fireworks-ai_constrained-generation-with-reasoning.md]])
