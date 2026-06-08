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
  - multi-agent
  - orchestration
  - ralph-loop
  - cost-optimization
  - cron
created: 2026-05-13
updated: 2026-06-08
aliases: [agent loop, ReAct loop, decide-act-observe, agent execution cycle]
sources:
  - https://stevekinney.com/writing/agent-loops
  - https://agentic.ai/what-is-agentic-ai
  - https://www.anthropic.com/research/building-effective-agents
  - raw/articles/2026-05-27_openai_building-self-improving-tax-agents-codex.md
  - raw/articles/2026-06-08_mvanhorn_wtf-is-a-loop.md
  - https://thriveholdings.com
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

## Loop Evolution Spectrum (2022–2026)

Matt Van Horn's research synthesis (June 2026) identifies five stages in the evolution of agent loops:

| Stage | Era | Pattern | Key Innovation | Limitation |
|-------|-----|---------|----------------|------------|
| **1. ReAct** | 2022 | Academic while-loop | Reasoning + acting interleaving | One model, one loop, human watching |
| **2. AutoGPT** | 2023 | Goal-driven self-prompting | Autonomous goal pursuit | Infamous for spinning forever; seeded "agents are a toy" |
| **3. Ralph** | Jul 2025 | Bash one-liner piping prompt file | Context reset to anchor files each iteration | Terminal must stay open; single-agent |
| **4. /goal** | Spring 2026 | Validator-gated loop | Small model (Haiku) judges completion | Still single-agent, human-kicked |
| **5. Orchestration** | 2026 | Multi-loop supervision | Scheduling, durability, concurrent dispatch | Cost management; verification gaps |

> "Single-agent ralph is old hat; multi-agent supervision is the new layer." — synthesis from Van Horn's research, June 2026

Stage 5 introduced four structural changes: (1) the loop became the unit of work, not the task; (2) loops supervise other loops concurrently and on schedule; (3) scheduling replaces human kickoff — runs on infrastructure time, not attention; (4) durability becomes explicit with git-backed state and crash recovery.

### Boris Cherny's Three Personal Stages

Boris Cherny (Claude Code creator, Anthropic) described his own progression at WorkOS Acquired Unplugged (June 2, 2026):

1. **Manual + autocomplete** — write code by hand
2. **Parallel sessions** — run 5–10 Claude sessions, prompt each one
3. **Loop author** — don't prompt at all; write loops that prompt Claude; ~200 agents read GitHub/Slack/Twitter and decide what to build

> "I don't prompt Claude anymore. My job is to write loops." — Boris Cherny, June 2026

He landed 259 PRs in 30 days with 100% of contributions written by Claude Code (reported December 2025).

## The "Cron + Decision-Maker" Framing

A persistent skeptic argument: "loops are just cron jobs rebranded." The honest answer is half-right:

- **Yes**, the scheduling layer is cron. Boris runs his on cron. Claude Code's `/loop` uses cron under the hood.
- **No**, cron never had a decision-maker in the body. A cron job runs a fixed script. A loop runs a model that observes current state, decides next action, executes, verifies, and decides whether to continue.

```
Cron:     timer → fixed script → output
Loop:     timer → model(observes, decides, acts, verifies) → continue or stop
Orchestration: timer → model(dispatches sub-loops, supervises, aggregates) → durable state
```

The interesting engineering is everything you wrap around that decision-maker so it "does not run off a cliff."

## Economics: The Loop Is Now the Expensive Part

As the model cost of writing code approaches zero, the cost of running the loop has become the dominant expense:

> "Every ai agent i shipped this year is a for-loop, an llm call, and a try/catch around the json parsing. The only thing agentic about it is the anthropic bill at the end of the month." — @rohit_jsfreaky, June 2026

**Case study:** Uber capped engineers at **$1,500/person/month** for Claude Code + Cursor after burning its annual AI budget in four months.

> "The costliest thing in AI coding is no longer writing code, it's managing the agent loop." — @runes_leo, June 2026

### Three Hard Stops for Production Loops

| Guard | Purpose |
|-------|---------|
| **Maximum iteration count** | Prevent infinite loops |
| **No-progress detection** | Abort when agent is stuck |
| **Token/dollar budget ceiling** | Hard cost cap per run |

Without guardrails: "infinite loops and billing surprises orders of magnitude over budget" (@cv_usk, June 2026).

## Skills > Loops

Peter Steinberger's complementary thesis: the reusable unit inside the loop is a **skill**, not a prompt. A loop with no reusable skills is `while(true)` around a stranger. A loop that calls a library of sharp, tested, named skills is a system that compounds.

> "If you do something more than once, turn it into an automated skill. If you do something hard, turn it into a skill afterward so next time is free." — @steipete, recurring thesis, June 2026

This connects to the [[concepts/agentic-engineering|agentic engineering]] practice of building reusable [[concepts/agent-skills|agent skills]] as the durable asset, with loops as the plumbing that invokes them.

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
- [WTF Is a Loop? Peter Steinberger vs. Boris Cherny](https://x.com/i/article/2063850827694096385) — Matt Van Horn, June 2026
- [Boris Cherny: Why Coding Is Solved, and What Comes Next](https://www.youtube.com/watch?v=RkQQ7WEor7w) — Sequoia AI Ascent / WorkOS Acquired Unplugged, June 2026
- [Ralph Loop](https://ghuntley.com/ralph/) — Geoffrey Huntley, July 2025
- [Gas Town](https://github.com/gastownhall/gastown) — Steve Yegge, January 2026
