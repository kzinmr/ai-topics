---
title: "Agentic Loop — The Canonical AI Agent Execution Pattern"
type: concept
slug: agentic-loop
status: complete
tags:
  - agent-loop
  - ai-agents
  - architecture
  - tool
  - cognition
created: 2026-05-13
updated: 2026-05-13
aliases: [agent loop, ReAct loop, decide-act-observe, agent execution cycle]
sources:
  - https://stevekinney.com/writing/agent-loops
  - https://agentic.ai/what-is-agentic-ai
  - https://www.anthropic.com/research/building-effective-agents
  - raw/articles/2026-05-27_openai_building-self-improving-tax-agents-codex.md
---

# Agentic Loop — The Canonical AI Agent Execution Pattern

> **Definition:** The agentic loop is the repeating cycle that all AI agents converge on: **decide what to do next → act (call a tool) → observe the result → decide again**. It continues until the goal is met, the agent gets stuck, or a human intervenes. This loop is what separates an agent from a chatbot.

As Steve Kinney observed after reading through the source code of every major agent framework: "Not similar. The *same*. A while loop that calls an LLM, checks if the response contains tool calls, executes them if it does, and stops if it doesn't."

## The Canonical Loop (6 Lines)

```javascript
while (!done) {
  const response = await callLLM(messages);
  if (response.toolCalls.length > 0) {
    const results = await executeTools(response.toolCalls);
    messages.push(...results);
  } else {
    done = true;
    return response;
  }
}
```

Every framework — Claude Code, Codex, Cursor, Vercel AI SDK, LangGraph, smolagents — implements this same structure. The loop is **solved**. The engineering *around* the loop (context management, safety controls, cost containment) is where all interesting decisions live.

## Origins: The ReAct Paper (2022)

The pattern was formalized by Yao et al. (Princeton & Google Research) in the **ReAct paper** ([arXiv:2210.03629](https://arxiv.org/abs/2210.03629)) — **Rea**soning + **Act**ing. The paper demonstrated that interleaving reasoning traces with tool-use actions produces better results than either alone.

## The Three-Stage Cycle

| Stage | Action | Description |
|-------|--------|-------------|
| **1. Decide** | Look at the goal and current state. Pick next action. | Search, write code, call API, ask user, or stop |
| **2. Act** | Execute via a tool. | HTTP request, file edit, shell command, browser navigation |
| **3. Observe** | Read result. Update memory. Detect errors. | Continue, retry, change strategy, or finish |

This is sometimes called the **Perceive → Reason → Act → Observe** cycle in four-stage formulations.

## Named Variants

| Name | Context | Distinctive Feature |
|------|---------|-------------------|
| **ReAct Loop** | Academic (2022) | Formal reasoning + acting interleaving |
| **Ralph Wiggum Loop** | Coding agents | Named after Simpsons character; "keep running, keep trying, never give up" |
| **Karpathy Loop** | ML research | Fixed time budget, single metric, indefinite iteration |
| **/goal Loop (Claude Code)** | Claude Code | Condition-driven; evaluator model (Haiku) judges completion from transcript |
| **/goal Loop (Codex)** | Codex CLI | Persisted goal with runtime continuation prompts + `update_goal` tool |
| **Autoresearch Loop** | General optimization | Continuous improvement against a measurable target |

## What Separates Agents from Chatbots

| Capability | Chatbot | Agentic AI |
|------------|---------|------------|
| Generates text/code | ✅ | ✅ |
| Calls external tools/APIs | ❌ | ✅ |
| Plans multi-step work | ❌ | ✅ |
| Executes without per-step approval | ❌ | ✅ |
| Recovers from errors and retries | ❌ | ✅ |
| Decides when task is done | ❌ | ✅ |

The line is sharp: **who decides what action happens, and who executes it**. A chatbot generates text for a human to act on. An agent acts itself.

## Self-Improving Agent Loop (Case Study: Thrive × OpenAI Tax AI)

In May 2026, **Thrive Holdings** and OpenAI published a case study on a self-improving tax return agent built with [[entities/codex|Codex]]. The system processes **7,000+ tax returns** for 30+ accounting firms, demonstrating a **self-improving loop** pattern distinct from the canonical ReAct loop:

### The Three-Stage Improvement Loop

| Stage | Component | Description |
|-------|-----------|-------------|
| **1. Feedback** | Expert practitioners | Corrections captured as structured data — not ad-hoc notes |
| **2. Evidence** | Production traces | Full path from source documents → extracted fields → filed return enables field-level comparison |
| **3. Fix** | Codex task environment | Bounded writable worktree + read-only production context → eval targets → scoped engineering tasks |

### Key Metrics
- **Accuracy**: 25% → **86%** within 6 weeks (75% correct field completion threshold)
- **Field-level correctness**: up to **97%**
- **Throughput**: ~**50%** increase
- **Practitioner impact**: One senior accountant: 180 hours → **15 hours** per tax season

### Codex Task Environment Pattern

Each improvement cycle follows a structured pattern:

```
repo/ → branch: codex/fix-{task-id}/
  ├── AGENTS.md
  ├── tasks/{task-id}/
  │   ├── task.yaml
  │   ├── EXEC_PLAN.md
  │   └── RESULTS.md
  ├── app/tax-ai/{domain}/
  ├── evals/
  │   ├── datasets/{failure-pattern}.yaml
  │   ├── suites/{failure-pattern}.yaml
  │   ├── suites/{regression}.yaml
  │   └── graders/{domain}.yaml
  ├── skills/
  └── scoped-tools/
```

Codex inspects the full context (trace, repo, evals, skills) and proposes changes validated against targeted + regression test suites before human review.

This pattern generalizes beyond tax: any production system where expert corrections can be structured as eval targets and Codex/[[concepts/agentic-engineering|agentic engineering]] can be dispatched to fix them fits the model.

## Stopping Conditions

Well-designed agents include exit criteria:
- Task marked complete (`update_goal` tool → `achieved`)
- Maximum iterations reached
- Token budget exhausted
- Agent determines it cannot make further progress (stuck)
- Human review step triggered

Without stopping conditions, an agent can spin indefinitely, wasting resources.

## The Loop Is the Easy Part

> "If you're building an agent, start with the 30-line version. Get it working. Then add safety controls, then context management, then observability. Resist the urge to start with a framework — you'll understand the framework better once you've hit the problems it was designed to solve. The loop is the easy part. Making it reliable is the whole job." — Steve Kinney

The real engineering challenges are around the loop:
- **Context management**: Compaction, summarization, memory
- **Safety controls**: Kill switches, audit logs, human-in-the-loop
- **Cost containment**: Token budgets, iteration caps
- **Graceful degradation**: What happens when the agent gets stuck
- **Observability**: Tracing each iteration for debugging

## Related Concepts

- [[concepts/karpathy-loop]] — Autonomous ML research variant
- [[concepts/pi-autoresearch]] — Generalized metric optimization variant
- [[concepts/codex-goal]] — Codex built-in Ralph loop (`/goal`)
- [[concepts/claude-code-goal]] — Claude Code goal-driven autonomous workflow (`/goal`)
- [[concepts/self-improving-agents]] — Agents that improve themselves over runs
- [[concepts/agentic-engineering/_index]] — Broader agentic engineering cluster
- [[concepts/reasoning-models]] — Chain-of-thought, tree-of-thought reasoning

## References

- [The Anatomy of an Agent Loop](https://stevekinney.com/writing/agent-loops) — Steve Kinney, March 2026
- [What Is Agentic AI?](https://agentic.ai/what-is-agentic-ai) — Agentic.ai guide
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — Yao et al., 2022
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic, 2024
