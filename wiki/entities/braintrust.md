---
title: "Braintrust"
type: entity
created: 2026-05-30
updated: 2026-05-30
tags:
  - company
  - evaluation
  - observability
  - developer-tooling
  - codex
aliases: ["Braintrust AI"]
sources:
  - https://openai.com/index/braintrust
---

# Braintrust

**Braintrust** is the observability and evaluation platform for shipping quality AI products. Founded by **Ankur Goyal** (CEO), it provides tools for monitoring, testing, and evaluating AI systems in production.

## Codex Case Study (May 2026)

OpenAI published a case study on how Braintrust engineers use **[[entities/codex|Codex]]** with GPT-5.5 to turn customer feature requests into preview branches in minutes.

### Key Metrics

| Metric | Value |
|--------|-------|
| Team adoption | **50% of Braintrust moved to Codex in one month** |
| Workflow change | Customer requests → preview branches in minutes (vs. backlog) |
| Experimentation | Test-driven autonomous problem-solving enabled by speed |

### The Speed Advantage

CEO Ankur Goyal identified speed as the primary differentiator:

> "It sounds simple, but Codex can literally print more text in the terminal without getting slow, and other models just can't replicate that."

The speed difference fundamentally changes how engineers interact with the coding agent:

1. **Before Codex**: Feature requests entered a backlog, got prioritized later, required step-by-step prompting
2. **With Codex**: Copy request → create preview branch → show customer in minutes → iterate in real time

### Novel Experimentation Workflow

Goyal described a shift from interactive prompting to autonomous experimentation:

> "With Codex, I've shifted to writing a test that demonstrates a problem, creating a sandbox environment, and then letting Codex run in that environment. This is a novel use case for me, and I can run experiments because of the speed."

This represents a **test-driven autonomous coding** pattern:
- Engineers define the problem via tests
- Codex runs in a controlled sandbox environment
- Faster idea-to-solution cycle enables more experimentation
- Speed makes autonomous problem-solving economically viable

### Why Speed Enables Autonomy

The case study highlights that **speed is not just a performance metric — it's an enabler of new workflows**:
- Slower tools require more hands-on guidance (higher cost per experiment)
- Faster tools allow engineers to "set and forget" — define the problem, let the agent work
- Real-time customer iteration becomes possible when feature demos take minutes instead of days

> "The more code we write, the more customer problems we can solve, and Codex is the most effective way to do that right now."

## Related

- [[entities/codex]] — OpenAI's coding agent used by Braintrust
- [[entities/openai]] — Platform provider
- [[entities/gpt-5-5]] — Model powering the Codex workflow
