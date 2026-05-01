---
title: "Improving Deep Agents with Harness Engineering"
source: "https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering"
date: 2026-02-17
author: Vivek Trivedy (LangChain)
tags: [harness-engineering, agents, langchain, coding-agents, evals, middleware]
---

# Improving Deep Agents with Harness Engineering

**Source:** LangChain Blog
**Key Achievement:** Coding agent performance on **Terminal Bench 2.0** improved from **52.8 to 66.5 (+13.7 points)** solely by modifying the harness, keeping the model (`gpt-5.2-codex`) fixed.

## 1. Defining Harness Engineering
Harness Engineering is the practice of building systems and tooling around a model to optimize for task performance, token efficiency, and latency.

> "The goal of a harness is to mold the inherently spiky intelligence of a model for tasks we care about."

### The Optimization Knobs
1. **System Prompt:** Instructions and personas.
2. **Tools:** Capabilities provided to the agent.
3. **Middleware:** Hooks around model and tool calls (e.g., intercepting exits or tracking edits).

## 2. The Improvement Loop: Trace Analyzer Skill
To improve the agent, LangChain uses a repeatable "Agent Skill" to analyze errors at scale using **LangSmith** traces.

**The Workflow:**
1. **Fetch:** Pull experiment traces from LangSmith.
2. **Analyze:** Spawn parallel error analysis agents to find failure modes.
3. **Synthesize:** A main agent aggregates findings and suggests harness changes.
4. **Implement:** Targeted changes are made to the harness (often with human verification to prevent overfitting).

## 3. Key Strategies for Performance Gains

### A. Build & Self-Verify
Agents often suffer from a "one-and-done" mentality. To fix this, LangChain implemented a **Build-Verify Loop**:
- **Guidance:** The system prompt now mandates: *Planning & Discovery → Build → Verify (run tests) → Fix.*
- **PreCompletionChecklistMiddleware:** A hook that intercepts the agent before it exits, forcing a final verification pass against the original task specification.

### B. Context Engineering
Agents struggle with environment discovery. The harness now handles "onboarding" the agent:
- **LocalContextMiddleware:** Automatically maps directory structures (`cwd`) and locates system tools (e.g., Python paths) upon startup.
- **Time Budgeting:** Injects heuristic warnings about remaining time to nudge the agent toward completion and verification.
- **Testing Standards:** Prompting stresses that code will be measured against programmatic tests, forcing the agent to avoid "slop buildup" and handle edge cases.

### C. Loop Detection
To prevent "doom loops" (where an agent makes repetitive, failing edits to the same file):
- **LoopDetectionMiddleware:** Tracks per-file edit counts. After `N` edits, it injects a prompt: *"...consider reconsidering your approach."*

### D. Adaptive Reasoning Compute
Using `gpt-5.2-codex` reasoning modes (`low` to `xhigh`), they discovered a **"Reasoning Sandwich"** baseline:
- **Strategy:** Spend high compute on **Planning** and **Verification**, while using lower compute for implementation.
- **Finding:** Running exclusively on `xhigh` actually *decreased* scores (53.9%) due to timeouts. The balanced approach reached 66.5%.

## 4. Practical Takeaways for Developers
1. **Context is the Engineer's Job:** Don't rely on agents to search for tools or directory structures; deliver that context via middleware.
2. **Aggressive Self-Verification:** Models are biased toward their first solution. Use middleware to force them to run tests and compare outputs against the spec.
3. **Use Traces as Signal:** Debug the toolset and the reasoning simultaneously. Often, a "reasoning error" is actually a missing tool or instruction.
4. **Design for Today, Plan for Tomorrow:** Use guardrails (like loop detection) to fix current model shortcomings, but expect these to become obsolete as models improve.
5. **Tailor to the Model:** A harness optimized for Codex may not perform as well for Claude without specific iteration.
