---
title: The Bitter Lesson of Agent Harnesses
category: concepts
status: active
tags: [ai-agents, agent-frameworks, browser-agents, rl, minimalism]
aliases: ["The Bitter Lesson of Agent Frameworks"]
---

# The Bitter Lesson of Agent Harnesses

**Author:** Gregor Zunic (@gregpr07)
**Source:** [Browser Use Blog](https://browser-use.com/posts/bitter-lesson-agent-frameworks)
**Date:** January 16, 2026
**Original Tweet:** [x.com/gregpr07/status/2047358189327520166](https://x.com/gregpr07/status/2047358189327520166)

## Overview

Gregor Zunic, founder of Browser Use, shares lessons learned from building browser agents at scale. The core thesis: **the less you build in your agent framework, the more it works**. All the value comes from the RL-trained model, not from abstractions.

## 🔑 Key Excerpts & Core Principles

> *"All the value is in the RL'd model, not your 10,000 lines of abstractions."*

> *"An agent is just a for-loop of messages. The only state an agent should have is: keep going until the model stops calling tools."*

> *"The Bitter Lesson from ML research is clear: general methods that leverage computation beat hand-crafted human knowledge every time."*

> *"Agent frameworks fail not because models are weak, but because their action spaces are incomplete."*

> *"The bitter lesson: The less you build, the more it works."*

## 🚫 Why Traditional Frameworks Fail

- **Abstractions freeze assumptions:** Planning modules, verification layers, and output parsers encode developer biases, not model capabilities.
- **RL breaks constraints:** Models trained on millions of examples anticipate patterns developers can't predict. Over-specification prevents models from leveraging their training.
- **99% of the work is in the model:** Modern LLMs handle tasks natively (e.g., Claude Code writing AppleScript directly) without specialized tools or rigid wrappers.

## 💡 The Browser Use Agent Philosophy

- **Core Insight:** Frameworks fail due to *incomplete action spaces*, not weak models.
- **The Inversion Strategy:** Start with maximal capability, then restrict. Give the LLM near-human browser freedom, then layer on safety/structure based on evaluations.
- **Architecture:** Replaced brittle primitives (`click/type/scroll`) with raw control surfaces:
  - **Chrome DevTools Protocol (CDP):** Direct browser control.
  - **Browser Extension APIs:** Handles permissioned state & active window access.
  - Together, they create a nearly complete action space, enabling self-correction.

## ⚙️ Technical Implementation Details

### Context Bloat Problem
Browser state snapshots easily exceed `50KB+` per request. After ~10 interactions, context hits `500KB+`, causing hallucinations, lost coherence, and crashes.

### Ephemeral Tool Solution
Limits retained outputs to the last `X` calls. Sacrifices cache slightly to prevent context overload. The model only needs recent state; older snapshots are noise.

```python
@tool("Get browser state", ephemeral=3)  # Keep last 3 only
async def get_state() -> str:
    return massive_dom_and_screenshot
```

### Explicit Termination (`done` Tool)
Naive "stop when no tool calls" causes premature exits. The explicit `done()` tool forces intentional completion.
- **CLI Mode:** Stops on no tool calls (quick interactions)
- **Autonomous Mode:** Stops *only* on explicit `done()` call

```python
@tool('Signal that the current task is complete.')
async def done(message: str) -> str:
    raise TaskComplete(message)
```

### Model-Agnostic Protocol (Covers 95% of use cases)
```python
class ChatAnthropic:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...

class ChatOpenAI:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...

class ChatGoogle:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...
```

## 💻 Core Agent Loop Architecture

The entire agent is reduced to:

```python
while True:
    response = model(messages, tools)
    if response.tool_calls:
        for tc in response.tool_calls:
            messages.append(tc.execute())
    else:
        break  # Or await done()
```

Everything else — retries, rate limits, connection recovery, context compaction, token tracking — is ops, not agent.

## 🛠 Actionable Takeaways & Resources

- **Open Source SDK:** The minimal architecture is released as [`agent-sdk`](https://github.com/browser-use/agent-sdk) on Browser Use's GitHub. Includes a re-implementation example of Claude Code.
- **Recommendation:** Use the SDK for production, or simply paste context into Claude Code/Gemini CLI and build custom agents in your preferred language.
- **Try the Product:** [bu.app](https://bu.app) — Browser Use's agent product.
- **Infrastructure:** [Cloud Docs](https://docs.cloud.browser-use.com) | [Open Source Docs](https://docs.browser-use.com)

## 📜 Key Quotes & Important Facts

> *"As long as in principle everything is possible, LLMs are extremely good at fixing themselves on the fly."*

> *"That's ops. Solved problems. Necessary — but don't confuse it with the agent itself."*

> *"The less you build, the more it works."*

## Related Resources
- [browser-harness](https://github.com/browser-use/browser-harness) — Self-healing browser harness
- [agent-sdk](https://github.com/browser-use/agent-sdk) — Minimal agent architecture SDK
- [bu.app](https://bu.app) — Browser Use's production agent product
