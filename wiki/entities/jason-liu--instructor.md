---
title: Jason Liu — Instructor Library & Structured Outputs
type: entity-subpage
parent: jason-liu
created: 2026-04-27
updated: 2026-04-27
tags:
  - instructor
  - structured-outputs
  - pydantic
  - model

---

# Jason Liu: Instructor Library & Structured Outputs

## "Pydantic is All You Need" — Structured Outputs as the Foundation

Liu's keynote at the **AI Engineer Summit 2023** (\"Pydantic is all you need\") crystallized his core philosophy: the problem with LLM integration isn't the models — it's the interface between probabilistic outputs and deterministic software.

> \"Imagine hiring an intern to write an API that returns a string you have to JSON load into a dictionary and pray the data is still there. You'd probably fire them and replace them with GPT. Yet, many of us are content using LLMs in the same way.\"

His argument has three pillars:

1. **Schema-first design** — Define what you want as a Pydantic model, not as a prompt template
2. **Validation as self-correction** — Treat LLM errors as validation failures with clear error messages the model can use to retry
3. **Backwards compatibility** — Make Software 3.0 work with existing paradigms (type hints, dataclasses, ORM patterns)

Instructor's API is intentionally minimal:

```python
from instructor import from_openai
from pydantic import BaseModel
from openai import OpenAI

class User(BaseModel):
    name: str
    age: int

client = from_openai(OpenAI())
response = client.create(model="gpt-4o", response_model=User,
    messages=[{\"role\": \"user\", \"content\": \"John is 25 years old\"}])
# response is a validated User(name=\"John\", age=25)
```

### Validation Errors as a Feature, Not a Bug

Liu reframes the LLM reliability problem through the lens of **classical software validation**:

> \"Instead of framing 'self-critique' or 'self-reflection' in AI as new concepts, we can view them as validation errors with clear error messages that the system can use to self-correct.\"

Instructor implements a **reasking mechanism** that automatically:
1. Parses the LLM's raw output
2. Validates it against the Pydantic schema
3. On failure, sends the validation error back to the model as context for retry
4. Repeats until valid output is produced or max retries is reached

This turns the probabilistic LLM into a deterministic function from the caller's perspective — a critical requirement for production systems.

### Multi-Language, Multi-Provider Structured Outputs

Since the original Python release, Instructor has expanded to **5 languages** (Python, TypeScript, Ruby, Go, Elixir) plus a **Rust** implementation, and supports every major LLM provider:

- OpenAI, Anthropic, Google, Vertex AI, Cohere
- Ollama, llama-cpp-python (local/offline models)
- Any provider with function calling capabilities

The cross-language strategy reflects Liu's belief that **structured outputs are a universal need**, not a Python-specific convenience.

### Software 3.0 — Classical Engineering Meets LLMs

Liu's vision of \"Software 3.0\" is that structured outputs allow developers to:
- **Own the objects we define** — typed models, not loose JSON
- **Control the functions we implement** — explicit tool contracts
- **Manage the control flow** — retries, validation, error handling
- **Own the prompts** — declarative schema definitions that generate prompts automatically

> \"This approach makes Software 3.0 backwards compatible with existing software, demystifying language models and returning us to a more classical programming structure.\"

### Instructor Library — Flagship Project

The flagship open source project — a thin wrapper around LLM APIs that adds:
- **response_model parameter** — specify a Pydantic model, get validated objects back
- **Automatic retries** — configurable max retries with validation error feedback
- **Streaming with structure** — partial objects as tokens arrive, maintaining type safety
- **Multi-provider support** — same API across OpenAI, Anthropic, Google, local models
- **Multi-language ports** — TypeScript, Ruby, Go, Elixir, Rust implementations
- **11,000+ GitHub stars, 6M+ monthly PyPI downloads**
- **Cited by OpenAI** as inspiration for their Structured Outputs API feature

### Structured Outputs By Example

A hands-on educational site (github.com/jxnl/structuredoutputsbyexample) showcasing extraction patterns across:
- Basic data extraction
- Classification tasks
- Streaming responses
- Multiple LLM providers
- Real-world use cases (search queries, content moderation, data transformation)

### Key Blog Writings on Structured Outputs

- **AI Engineer Keynote: Pydantic is all you need** (Nov 2023) — The talk that launched his public profile, arguing that structured outputs via Pydantic solve the fundamental LLM integration problem
- **Pydantic is Still All You Need: Reflections on a Year of Structured Outputs** (Sep 2024) — One-year retrospective: \"nothing's really changed in the past year. The core API is still just one function call.\" Covers 40% month-over-month growth, multi-language expansion, and the case for validation-first design
- **Bridging Language Models with Python with Instructor, Pydantic, and OpenAI's Function Calls** (Medium, 2023) — Technical deep-dive into why Pydantic is the right abstraction between LLMs and traditional software

## See Also

- [[jason-liu--key-work]] — Jason Liu's career, RAG Master Series, and consulting practice.
- [[jason-liu--context-engineering]] — Context engineering for RAG and agentic systems.
- [[structured-outputs]] — Schema-first design for LLM integration.
- [[pydantic]] — Data validation library used as the foundation of Instructor.
- [[llm-engineering]] — Best practices for building production LLM applications.
