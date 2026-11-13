---
title: "FastAPI"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - api
  - python
  - developer-tooling
  - open-source
sources:
  - https://github.com/fastapi/fastapi
aliases:
  - fastapi
  - FastAPI
---

# FastAPI

**FastAPI** (Sebastián Ramírez, ~80k stars, MIT) is the de-facto standard Python web framework for building **API-first services**, built on Starlette (async) + Pydantic (validation) with automatic OpenAPI docs. It became the default way to expose ML/LLM functionality: inference microservices, RAG endpoints, agent tool servers, and OpenAI-compatible proxies are overwhelmingly FastAPI apps.

## Why it dominates AI serving code

- **Pydantic-native** — request/response models double as documentation and validation; the same Pydantic skill transfers to structured-output work ([[concepts/structured-outputs]]-adjacent) and to [[concepts/pydantic-ai]].
- **Async-first** — Starlette/uvicorn under the hood; SSE/WebSocket streaming for token streams is idiomatic.
- **Type hints everywhere** — a generation of ML engineers learned "real Python typing" through FastAPI tutorials.
- **OpenAPI/Swagger free** — auto-generated docs make internal model APIs self-documenting.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    text: str
    max_tokens: int = 256

@app.post("/generate")
async def generate(p: Prompt):
    return await model.generate(p.text, p.max_tokens)
```

## Role in the LLM stack

| Layer | FastAPI's role |
|---|---|
| Model serving | Custom inference APIs around vLLM/TGI; the OpenAI-compatible server pattern |
| Agent tool servers | MCP-era "tools as HTTP endpoints"; auth/quotas around agent tool calls |
| RAG backends | Embedding/retrieval endpoints in front of Vespa/Redis/pgvector |
| Eval harnesses | FastAPI-fronted judges and human-eval UIs |

FastAPI is also a frequent subject in "LLM writes boilerplate well" discussions — its tutorial-driven, convention-heavy surface is exactly what code-generation models handle reliably, which accelerated its adoption among ML teams without web backgrounds.

## Related

- [[concepts/pydantic-ai]] — agent framework on the same Pydantic foundation
- [[concepts/pydantic]] — the validation layer FastAPI is built on
- [[concepts/structured-outputs]] — Pydantic schemas as LLM output contracts
- [[concepts/vllm]] — the serving engines FastAPI wrappers commonly front
- [[concepts/vector-databases]] — RAG backends exposed via FastAPI
- [[concepts/mlops]] — model deployment layer
