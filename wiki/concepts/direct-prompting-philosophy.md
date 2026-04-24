---
title: "Direct Prompting Philosophy"
type: concept
created: 2026-04-13
updated: 2026-04-13
tags: [prompting, intuition, agentic-engineering, workflow-design, anti-overengineering]
aliases: ["just-talk-to-it", "intuition-driven-development", "direct-prompting", "no-bs-agentic"]
related: , [[claude-code-best-practices]], [[cli-over-mcp-pattern]], [[inference-speed-development]]
sources:
  - url: "https://steipete.me/posts/2025/just-talk-to-it"
    author: "Peter Steinberger (@steipete)"
    date: "2025-10"
    title: "Just Talk To It - the no-bs Way of Agentic Engineering"
---

# Direct Prompting Philosophy

**Direct Prompting Philosophy** (or "Just Talk To It") is an anti-overengineering approach to agentic development. It rejects complex orchestration layers (RAG pipelines, subagent frameworks, custom hooks, elaborate prompt templates) in favor of **direct, conversational interaction** with the AI coding agent, guided by human intuition and iterative refinement.

The core thesis: *"Don't waste your time on stuff like RAG, subagents, Agents 2.0 or other things that are mostly just charade. Just talk to it. Play with it. Develop intuition."* — Peter Steinberger

---

## Why Direct Prompting Works

### 1. Modern LLMs Don't Need Crutches
Agents like Claude Code and Codex already have:
- Full codebase awareness
- Tool execution capabilities
- Context window management
- Iterative self-correction

Adding orchestration layers **duplicates functionality** and introduces failure points.

### 2. Parallel Windows > Subagent Frameworks
> "What others do with subagents, I usually do with separate windows. This gives me complete control and visibility over the context I engineer."

**The Terminal Grid Pattern:**
- Run 3-8 independent agent instances in split terminal panes
- Each gets a focused, isolated context
- Human acts as the **router and merger**
- No framework overhead, no coordination bugs, full visibility

### 3. Intuition Over Specifications
Instead of writing exhaustive spec files upfront:
- Start with a 1-2 sentence prompt
- Watch the agent's direction
- Steer mid-flight: `"what's the status?"`, `"try another approach"`, `"focus on X"`
- Iterate until satisfied

**Result:** Faster convergence, fewer misaligned implementations, continuous human engagement.

---

## The Anti-Patterns It Rejects

| Pattern | Why It Fails | Direct Alternative |
|---------|--------------|-------------------|
| **RAG for codebase** | Fragile chunking, loses architectural context | Agent reads repo directly |
| **Subagent orchestration** | Coordination overhead, context duplication | Parallel terminal windows |
| **Elaborate prompt templates** | Stale quickly, model already knows patterns | Short, natural language |
| **Automated hooks/workflows** | Reduces human engagement, hard to debug | Manual intervention when needed |
| **Pre-written context dumps** | Context poison, wastes tokens | On-demand file references |

### The "Context Poison" Warning
> "I bet that you'd get better result if you ask your agent to 'google AI agent building best practices' and let it load some websites than this crap. You could even make the argument that this slop is context poison."

Third-party "best practice" guides, outdated prompt templates, and copied workflows often **degrade** performance because:
- They conflict with the model's native capabilities
- They add noise to the context window
- They create false expectations about what the agent can do

---

## When to Use Direct Prompting

| Scenario | Recommended Approach |
|----------|----------------------|
| **Feature development** | Direct prompting + iterative steering |
| **Refactoring** | Short prompt + agent execution + human review |
| **Debugging** | Copy-paste error verbatim + "fix this" |
| **UI/UX iteration** | Screenshot + "make it look like this" |
| **Architecture decisions** | "Give me 3 options before making changes" |
| **Complex multi-system work** | Break into isolated subtasks → parallel windows |

### When NOT to Use It
- **Automated CI/CD pipelines** (use scripts, not prompts)
- **Production deployments** (require deterministic processes)
- **Team-wide standards enforcement** (use linters, formatters, CLAUDE.md)
- **Security-critical code** (requires formal verification, not prompting)

---

## The Human Skill: Developing Intuition

Direct prompting shifts the developer's role from **prompt engineer** to **intuitive director**:

1. **Read the room**: Notice when the agent is confused, drifting, or overconfident
2. **Steer mid-flight**: Intervene with course corrections before wasted work
3. **Recognize patterns**: Know when a task needs breaking down vs. when it can be handled in one shot
4. **Trust but verify**: Accept good output quickly; catch bad output early

> "Many of the skills needed to manage agents are similar to what you need when managing engineers — almost all of these are characteristics of senior software engineers."

The irony: **AI makes senior skills more valuable, not less.** Junior devs struggle because they lack the architectural intuition to know *what* to ask for or *when* to intervene.

---

## Connection to [[inference-speed-development]]

Direct prompting enables the inference-speed cycle:
- **No orchestration overhead** → faster iteration
- **Short prompts** → quicker context setup
- **Parallel windows** → concurrent task execution
- **Intuitive steering** → faster convergence to correct output

The combination creates a development rhythm measured in **minutes, not hours**.

---

## Related Concepts

-  — The broader methodology this serves
- [[claude-code-best-practices]] — Practical implementation patterns
- [[cli-over-mcp-pattern]] — Why minimal tooling pairs with direct prompting
- [[inference-speed-development]] — How this enables rapid iteration
- [[context-window-management]] — Why short prompts preserve context

## Sources

- [Peter Steinberger: Just Talk To It](https://steipete.me/posts/2025/just-talk-to-it) — Primary source
- [Peter Steinberger: My Current AI Dev Workflow](https://steipete.me/posts/2025/optimal-ai-development-workflow/) — Parallel windows, minimal prompting
- [Peter Steinberger: Live Coding Session](https://steipete.me/posts/2025/live-coding-session-building-arena) — Real-time steering tactics
