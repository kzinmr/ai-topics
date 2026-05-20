---
title: "A Taxonomy of RL Environments for LLM Agents"
source: "https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/"
author: "Hanchung Lee (Han Lee)"
date: 2026-03-21
type: article
tags: [rl-environments, agent-harness, verifier, state-management, llm-agents, reinforcement-learning, task-design]
---

# A Taxonomy of RL Environments for LLM Agents

**Core thesis**: The reinforcement learning environment — not just model architecture or post-training recipes — determines what an agent can learn to do. A poorly designed environment leads to brittle, gamed behavior. A well-designed one enables robust, transferable skills.

## The Canonical Loop

An RL environment for LLM agents bundles five objects:

> **Formal definition**
> $$E = \{T, H, V, S, C\}$$
> where
> $T$ = tasks
> $H$ = agent harness
> $V$ = verifier
> $S$ = state management
> $C$ = configuration

The training loop: environment presents a task → harness manages model interaction with tools → verifier scores the output → state evolves across turns/episodes.

**Terminology mapping**:
- **Trajectory** (RL): state-action-reward sequence seen by trainer
- **Trace** (observability): structured execution log (tool calls, intermediate outputs)

## $T$: Tasks

Tasks are problems the agent solves. Their structural variety shapes which capabilities are learned.

### Task Taxonomy

| Task Type | Description | Examples |
|-----------|-------------|----------|
| Single-turn Q&A | prompt → answer, check correctness | Math benchmarks, SimpleQA |
| Multi-hop search | chain searches, synthesize sources | BrowseComp, WebWalkerQA |
| Open-ended research | report quality, no single answer | ADR-Bench, ResearchRubrics |
| Agentic tool-use | call tools in correct sequence | tau-bench, function-calling benchmarks |
| Stateful enterprise | modify persistent DB state, access controls | EnterpriseOps-Gym |
| Code generation | write code, run it, check outputs | SWE-Bench, LiveCodeBench |
| Code review & repair | detect bugs, suggest fixes, verify patches | CodeReview-Bench, DebugBench |
| Repository-level coding | multi-file edits, navigate large codebases | SWE-Bench Verified, RepoBench |
| Productivity workflows | email, calendar, notifications | WorkArena, OSWorld |
| Document authoring | create/edit/summarize across apps | BrowserGym, GAIA |

### Design Principles

- **Stochasticity matters**: clean deterministic environments → brittle agents. Inject noise (e.g., 5–10% tool errors during training) to handle production flakiness.
- **Reward sparsity**: no positive-reward-only tasks; agents must distinguish good from bad actions.
- **Curriculum**: order tasks by difficulty (e.g., 9th grade algebra → 12th grade calculus). AgentScaler uses fundamental capabilities → domain-specific.
- **Cost tension**: single-turn verifiable tasks are cheap; long-horizon tasks are expensive but most valuable.

### Synthetic Task Generation

- **Back translation**: start from desired output, reconstruct task input.
- **Graph-based synthesis**: build knowledge graph, generate multi-hop queries.

## $H$: Agent Harness

The harness enables model–environment interaction. It's scaffolding, not knowledge.

```
H = {
    rollout_protocol,   # SingleTurn | MultiTurn | Agentic
    tools,              # Available tools per rollout
    system_prompt,      # Agent instructions
    context_manager,    # Context overflow handling
    turn_limit,         # Max interactions per rollout
    sandbox,            # Code execution sandbox
    state               # Persistent state across turns
}
```

### Rollout Protocols

| Type | Description | When to Use |
|------|-------------|-------------|
| Single-Turn | one prompt, one response | Math, factual QA |
| Multi-Turn | back-and-forth dialogue | Games, structured tasks |
| Tool-Use | model calls tools, receives results | Agent benchmarks |
| Stateful Tool-Use | tools modify persistent state | Enterprise workflows, SWE-Bench |
| Agentic | full OODA loop (Observe–Orient–Decide–Act) | Deep research, complex workflows |

### Tools Landscape

| Category | Tools | Deterministic | Stateful |
|----------|-------|---------------|----------|
| IR | web_search, scholar_search | No (live web) | No |
| Content extraction | jina_reader, visit, web_scrape | No | No |
| Code execution | python_interpreter, shell, sandbox | Yes (same code) | Yes |
| File ops | file_read, file_write | Yes | Yes |
| Browser automation | playwright, link_click | No | Yes |
| Task management | todo, section_write | Yes | Yes |

**Modern design trend**: reduce tools to atomic primitives (`read`, `write`, `edit`, `bash`, `tasks` for subagents, `mcp` for MCP resources, `skill`, `askUserQuestions`).

### Context Management (for 600+ turn episodes)

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| Recency-based | keep N most recent turns | Simple, loses early context |
| Markovian recon | reconstruct state from scratch each turn | Principled, expensive |
| Reference-preserving summarization | summarize old context, keep citations | Preserves verifiability |
| Reference-preserving folding | compress context without losing references | Best for research tasks |

## $V$: Verifier

Maps (task, trajectory, trace) → reward signal. Determines what behavior is rewarded — and what the agent optimizes for.

### Verifier Types

| Type | How it Works | Best For |
|------|-------------|----------|
| Exact Match (EM) | compare output to ground truth | Math, factual QA |
| LLM-as-Judge | model scores output against rubric | Open-ended generation, summarization |
| Execution-based | run generated code, check outputs | SWE-Bench, LiveCodeBench |
| Process-based | check intermediate steps | Multi-step reasoning |
| Human evaluation | manual scoring | Research quality, creative work |
| Hybrid | combine multiple verifiers | Robust evaluation |

### Design Principles

- **Verifiers must be cheap at scale** — if verification costs more than generation, training throughput collapses.
- **Verifier quality determines agent quality** — noisy verifiers teach agents to exploit noise.
- **Process + outcome rewards** — reward good reasoning, not just correct answers.
- **Avoid verifier hacking** — agents will find and exploit verifier blind spots.

## $S$: State Management

State is what persists across turns. In the canonical loop: environment initializes state → agent acts → state updates → next turn.

### State Scoping

| Level | Persistence | Example |
|-------|------------|---------|
| Turn-level | one interaction | tool call + response |
| Episode-level | one task | scratchpad, working memory |
| Session-level | across tasks | user preferences, long-term memory |
| Environment-level | global | shared knowledge base, DB |

### State Representations

- **Structured**: JSON, database records
- **Unstructured**: text, conversation history
- **Hybrid**: structured fields + free-text notes
- **Observable vs hidden state**: what the agent can see vs what the environment tracks internally

## $C$: Configuration

Configuration controls environment behavior without changing the task/harness/verifier/state definitions.

- **Model**: which LLM, temperature, max_tokens
- **Hardening**: guardrails, safety filters
- **Runtime**: sandbox type, network policies
- **Curriculum**: task ordering, difficulty progression
- **Sampling**: number of rollouts, exploration parameters

## Design Implications

1. **The environment IS the curriculum** — task structure + verifier design determine what an agent learns more than model architecture.
2. **Invest in verifier quality** — it's the single most leveraged component; noisy verifiers poison everything downstream.
3. **Train in noisy environments** — deterministic training → brittle production agents.
4. **Separate harness from environment** — the harness is temporary scaffolding; the environment structure is durable.
5. **State management is underinvested** — most agent failures trace to poor state design, not model capability gaps.
