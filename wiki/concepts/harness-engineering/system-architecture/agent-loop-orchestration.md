---
title: "Agent Loop Orchestration"
type: concept
aliases:
  - agent-loop
  - orchestration-loop
  - responses-api-agent-loop
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - orchestration
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
  - "https://openai.com/index/harness-engineering-leveraging-codex/"
---

# Agent Loop Orchestration

An **execution loop structure** for LLM agents to autonomously complete tasks. A cyclic process where the model proposes actions, the platform executes them, and results are fed back to the model.

## Basic Loop

Standard agent loop in the OpenAI Responses API:

```
1. Context Assembly
   → User prompt + conversation history + tool instructions

2. Model Determines Next Action
   → Proposes one or more shell commands

3. API Executes Commands in Container
   → Commands execute in an isolated environment

4. Output Streamed to Model
   → Results fed back in real time

5. Model Inspects Results
   → Either proposes additional commands or generates a final response

6. Loop Continues (until the model stops returning additional commands)
```

## Parallel Execution

The model can **propose multiple shell commands in a single step**, and the Responses API can **execute them in parallel in independent container sessions**.

```
Example: Data Analysis Agent
├─ Session 1: grep file search
├─ Session 2: curl API data fetch
└─ Session 3: Verify previous results
    → Each session streams output independently
    → API multiplexes into structured tool outputs
```

## Output Capping

Command output rapidly consumes the context window, making **output capping** essential:

```text
text at the beginning ... 1000 chars truncated ... text at the end
```

- Preserves beginning and end, truncates middle
- Reduces noise so the model can focus on relevant results
- Prevents terminal log overflow

## Shell Tool vs Code Interpreter

| Feature | Code Interpreter | Shell Tool |
|------|-----------------|------------|
| Language | Python only | Go, Java, Node.js, Unix utilities |
| Use Case | Data analysis, script execution | Server startup, API calls, file operations |
| Flexibility | Limited | Broad (grep, curl, awk, etc.) |
| Persistence | Session-limited | Persisted via container filesystem |

## OpenAI vs Other Approaches

| Platform | Loop Management | Execution Environment | Output Control |
|----------------|-----------|---------|---------|
| **OpenAI Responses API** | Native (in-API) | Hosted containers | Output capping, streaming |
| **Hermes (delegate_task)** | Main agent | Isolated terminal sessions | Iteration limits |
| **LangGraph** | Custom graph | Developer-managed | Developer-implemented |
| **Anthropic** | Custom harness | Developer-managed | Developer-implemented |

## OpenAI Responses API Features

> "Instead of putting it on developers to build their own execution environments, we built the necessary components to equip the Responses API with a computer environment to reliably execute real-world tasks."

- **Managed**: Developers don't need to build their own execution environments
- **Streaming**: Real-time output allows the model to make dynamic decisions
- **Parallel**: Speed up via simultaneous command execution
- **Context Optimization**: Output capping protects the context budget

## Design Lessons

### ✅ Best Practices
- Explicitly instruct shell tool usage in prompts
- Use shell-trained models (GPT-5.2 and later)
- Always set output caps
- Use structured tool outputs to support model decision-making

### ❌ Anti-Patterns
- Pasting large files or tables directly into prompts (→ wastes context)
- Running commands without output limits (→ terminal log overflow)
- Implementing loop management on the client side (→ increased developer burden)

## Related Concepts

- [[concepts/harness-engineering/system-architecture/context-compaction]] — Compression mechanism for full context windows
- [[concepts/harness-engineering/system-architecture/container-context]] — Execution environment persistence
- [[concepts/context-window-management]] — Strategic context budget management
- [[concepts/harness-engineering]] — Agent execution environment design (higher-level concept)

## References

- [OpenAI: From model to agent](https://openai.com/index/equip-responses-api-computer-environment/)
- [[entities/openai]] — OpenAI
-  — Responses API (Implementation Base)