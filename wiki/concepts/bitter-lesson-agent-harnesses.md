---
title: "The Bitter Lesson of Agent Harnesses"
type: concept
aliases:
  - bitter-lesson-of-agent-frameworks
  - minimal-agent-architecture
tags:
  - ai-agents
  - harness-engineering
status: complete
description: "Gregor Zunic (Browser Use founder) の提唱する 'The less you build, the more it works' — 最小限のエージェントアーキテクチャ哲学。"
created: 2026-04-30
updated: 2026-04-30
sources:
  - "https://browser-use.com/posts/bitter-lesson-agent-frameworks"
  - "https://x.com/gregpr07/status/2047358189327520166"
  - "raw/articles/the-bitter-lesson-of-agent-harnesses-2026-04-24--d9ffedba.md"
related:
  - "[[concepts/harness-engineering]]"
  - "[[entities/browser-use]]"
  - "[[concepts/agent-loop]]"
---

# The Bitter Lesson of Agent Harnesses

> **Definition:** Rich Sutton's "The Bitter Lesson" (general methods that leverage computation will always surpass hand-crafted knowledge) applied to agent frameworks. **"The less you build, the more it works"** — the value of an agent framework lies not in 10,000 lines of abstraction, but in the RL-trained model.

## Core Thesis

- **All the value is in the RL'd model, not your 10,000 lines of abstractions**
- **An agent is just a for-loop of messages.** The only state: keep going until the model stops calling tools
- **Agent frameworks fail not because models are weak, but because their action spaces are incomplete**

## Why Traditional Frameworks Fail

1. **Abstractions freeze assumptions** — Planning modules, validation layers, and output parsers encode developer biases. They are not the model's actual capabilities
2. **RL breaks constraints** — Models trained on millions of samples discover patterns developers cannot predict. Over-specification impedes leveraging the model's training
3. **99% of the work is in the model** — Modern LLMs can handle tasks natively without specialized tools (e.g., Claude Code writing AppleScript directly)

## Browser Use Architecture Philosophy

### Inversion Strategy
Start with maximum capability, then impose constraints based on evaluation. Give LLMs nearly the same browser freedom as humans, then layer safety/structure on top.

### Raw Control Surfaces
Replace brittle primitives (click/type/scroll) with:
- **Chrome DevTools Protocol (CDP):** Direct browser control
- **Browser Extension APIs:** Authorized state and active window access

→ Produces a nearly complete action space, enabling self-correction.

## Technical Implementation Details

### Context Bloat Problem
Browser state snapshots are 50KB+ per request. After about 10 interactions this reaches 500KB+, causing hallucination, coherence loss, and crashes.

### Ephemeral Tool Solution
Keep only the last X call outputs. The model only needs the most recent state; old snapshots are noise.

```python
@tool("Get browser state", ephemeral=3)  # Keep last 3 only
async def get_state() -> str:
    return massive_dom_and_screenshot
```

### Explicit Termination (`done` Tool)
Naive "stop without tool calls" leads to premature termination. An explicit `done()` tool forces intentional completion.
- **CLI Mode:** Stop without tool calls (quick interactions)
- **Autonomous Mode:** Stop only on explicit `done()` call

### Model-Agnostic Protocol
```python
class ChatAnthropic:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...

class ChatOpenAI:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...

class ChatGoogle:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...
```

## Core Agent Loop

The entire agent reduces to this:

```python
while True:
    response = model(messages, tools)
    if response.tool_calls:
        for tc in response.tool_calls:
            messages.append(tc.execute())
    else:
        break  # Or await done()
```

> "Everything else — retries, rate limits, connection recovery, context compaction, token tracking — is ops, not agent."

## Implementation Resources

- **[agent-sdk](https://github.com/browser-use/agent-sdk)** — Minimal agent architecture SDK (open source)
- **[browser-harness](https://github.com/browser-use/browser-harness)** — Self-healing browser harness
- **[bu.app](https://bu.app)** — Browser Use production agent product
- [Cloud Docs](https://docs.cloud.browser-use.com) | [Open Source Docs](https://docs.browser-use.com)

## Relationship to Harness Engineering

While [[concepts/harness-engineering]] provides a comprehensive "Agent = Model + Harness" framework, the Bitter Lesson approach advocates the inverse. **Maximize model capability with minimal harness** — the two are complementary.

| Dimension | Harness Engineering | Bitter Lesson |
|------|-------------------|---------------|
| Focus | Reliability/safety/traceability | Minimal abstraction / maximizing model capability |
| Approach | Systematic control layers | "Less is more" — only what is needed |
| Suitability | Production/enterprise | Fast iteration/startups |
| Common ground | Leveraging RL-trained models | Leveraging RL-trained models |

## Sources

- [The Bitter Lesson of Agent Frameworks](https://browser-use.com/posts/bitter-lesson-agent-frameworks) (2026-01-16, Gregor Zunic)
- [x.com/gregpr07/status/2047358189327520166](https://x.com/gregpr07/status/2047358189327520166) (2026-04-24)
- [agent-sdk GitHub](https://github.com/browser-use/agent-sdk)
