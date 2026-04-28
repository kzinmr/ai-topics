---
title: "Structured Outputs — Reliable LLM Output via Schema Validation"
tags: [llm-output-formatting-json-pydantic-reliability-type-safety-function-calling]
created: 2026-04-15
updated: 2026-04-24
type: concept
---

# Structured Outputs — Reliable LLM Output via Schema Validation

## Definition

Structured outputs is the paradigm of constraining LLM generation to produce valid, machine-readable data (JSON, XML, Pydantic models) rather than free-form text. This enables reliable integration of LLMs into software systems without post-hoc parsing or fragile prompt engineering.

> *"We're not changing the language of programming — we're relearning how to program with data structures."* — Jason Liu

## Two Approaches

| Approach | Mechanism | Pros | Cons |
|----------|-----------|------|------|
| **Validation/Coercion** | Generate text → validate against schema → retry on failure | Model-agnostic, works with any LLM API | May require multiple retries |
| **Constrained Decoding** | Force the model to only generate valid tokens per schema | Single-pass guarantee | Requires custom inference engine |

## Key Players

### Jason Liu (Instructor)
Created the **Instructor** library (11K+ stars, 6M+ monthly downloads), cited by OpenAI as inspiration for their native structured output feature. Key insight: Pydantic models can serve as the contract between LLMs and application code.

> *"Pydantic is all you need"* — AI Engineer Keynote (Nov 2023)

The Instructor pattern:
```python
from pydantic import BaseModel
import instructor
from openai import OpenAI

class User(BaseModel):
    name: str
    age: int

client = instructor.from_openai(OpenAI())
user = client.chat.completions.create(
    model="gpt-4",
    response_model=User,
    messages=[{"role": "user", "content": "Extract: John is 30 years old"}]
)
# Returns User(name='John', age=30) — type-safe!
```

### Samuel Colvin (Pydantic AI)
Extended the structured output paradigm to **agent tool calling**. In Pydantic AI, all tool parameters, agent inputs, and agent outputs are validated through Pydantic schemas — ensuring end-to-end type safety in agentic workflows.

### Rahul (Guardrails AI / Jsonformer)
Pioneered **constrained decoding** with Jsonformer — modifying the model's generation process to only produce valid JSON per schema. This became foundational for Guardrails AI and influenced how the industry thinks about LLM output reliability.

## OpenAI Native Support
OpenAI now offers native structured output via `response_format` parameter, guaranteeing JSON Schema compliance. This validates the Instructor/Pydantic approach at the platform level.

## Cross-Language Ecosystem
| Language | Library | Approach |
|----------|---------|----------|
| Python | Instructor, Pydantic AI, Guardrails AI | Validation + Constrained |
| JavaScript/TypeScript | Zod, Instructor-js | Validation |
| Rust | schemars, serde_json | Validation at compile time |

## Why It Matters for AI Agents

1. **Reliability**: Agents can't proceed if tool calls return invalid data
2. **Composability**: Structured output from one agent becomes validated input for the next
3. **Testing**: Deterministic validation enables unit testing of LLM pipelines
4. **Developer Experience**: Type hints + IDE autocomplete for LLM outputs

## Related

- [[concepts/pydantic]] — Foundation library
- [[concepts/pydantic-ai]] — Agent-level structured outputs
-  — Constrained decoding with regex/grammars
-  — Grammar-constrained generation
- [[jason-liu]] — Instructor creator
- [[rahul]] — Guardrails AI / Jsonformer creator
- [[samuel-colvin]] — Pydantic creator
