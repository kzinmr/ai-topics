---
title: "Pydantic Serializability"
tags: [[concepts/serialization-structured-output-schema-generation-python-pydantic]]
created: 2026-04-15
updated: 2026-04-24
type: concept
---

# Pydantic Serializability

## Overview

Pydantic's serializability system provides structured output for AI models. Key innovations include:

- **JSON Schema generation** — Automatic schema generation from Python types
- **Structured output** — Reliable structured responses from LLMs
- **Type validation** — Ensures data matches expected formats

## Implementation in LLMs

Pydantic AI uses serializability to:
1. Generate JSON schemas for tool definitions
2. Validate LLM responses against expected types
3. Enable structured output with guaranteed format

## Code Example

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class UserProfile(BaseModel):
    name: str
    age: int
    interests: list[str]

agent = Agent('openai:gpt-4', result_type=UserProfile)
result = agent.run_sync('Describe a typical developer')
print(result.data)  # UserProfile(name='Alex', age=30, interests=['coding', 'reading'])
```

## Related

- [[samuel-colvin]] — Creator
- [[concepts/pydantic-ai]] — Framework
- [[concepts/structured-outputs]] — Pattern
