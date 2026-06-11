---
title: Back of House Multi-Agent Patterns
type: concept
created: 2026-04-18
updated: 2026-04-18
tags: [multi-agent, coding-agents, orchestration, agentic-engineering]
aliases: ["back-of-house", "kitchen metaphor", "head chef pattern"]
sources: []
---

# Back of House Multi-Agent Patterns

Multi-agent workflow patterns using the kitchen metaphor. Proposed by Sarah Chieng ([[entities/milksandmatcha]]) and [@0xSero] in April 2026.

## Single-Agent Ceiling

First, the problem definition. Why single-agent AI coding is a nightmare for engineers:

- Pay $200/month subscription, write prompts, wait 35+ minutes only to see "synthesizing", "perusing", "effecting", "germinating"
- Result is bug-ridden code, bloated context windows, counting remaining tokens on left hand
- Compact the context, yell at the agent, explain everything from scratch again... repeat
- At this point, the joy of AI coding is dead

**Root causes:**
1. Expecting too much from a single agent
2. Not decomposing problems into small, verifiable tasks

Most people respond with (a) prompt engineering courses, (b) context management SaaS, or (c) promoting the latest model, but the actual approach is different.

## Back of House (Kitchen) Metaphor

In a professional kitchen, one cook does not do everything:

### Head Chef (Orchestrator)
- Receives orders from humans
- Decomposes work into scoped, verifiable tickets
- Assigns each ticket to Line Cooks
- Only responsible for planning, coordination, and task decomposition
- Only has `delegate_task` tool
- Only sees high-level goals and sub-agent output summaries

### Line Cook (Subagent)
- Receives tickets from Head Chef and executes without question
- Works in a fresh context window (station) per agent
- Has full access to all necessary tools: read, write, MCP
- Given only minimal context necessary for their task
- Returns results and clocks out upon completion

**Key point:** Do not give Line Cooks a 15,000-token master plan document or full conversation history. Only give the minimum context needed to prepare a specific dish.

## Why Multi-Agent Is Now Practical

1. **Foundation model performance improvements**
2. **Evolution of orchestration tools** — OpenAI Codex's deep orchestration, Anthropic Claude Code and MCP ecosystem expansion
3. **Speed** — OpenAI Codex Spark (@cerebras) runs at ~1,200 tokens/sec. This makes parallel processing and verification steps practical where time cost previously made them unrealistic.

## Specific Improvement Results

Comparison on a website copy task using Figma MCP:

| Metric | Single Agent | Multi-Agent |
|--------|-------------|-------------|
| Average execution time | 36.5 min | 5.2 min |
| Manual interventions | 12 | 2 |
| Success rate | 0% | 100% first try |

Internal trials saw **84.3% reduction** in manual intervention for sequential loops.

## Three Immediate Benefits

### 1. Tokens: Effective Context Window ~200K → 25M+

- Human only talks to the Orchestrator
- Orchestrator has no tools other than `delegate_task`
- Each sub-agent has a fresh context window
- Since Orchestrator doesn't directly read or write files, effective context expands by the number of spawnable sub-agents

### 2. Control: Sequential Workflow Enforced Per Turn

```
Sub-agent A: Decompose order into sub-tasks and "contracts" with criteria
    ↓
Sub-agent B: Explore the next sub-task
    ↓
Sub-agent C: Test generated code. Pass → next, Fail → regenerate Sub-agent B
    ↓
Sub-agent D: Document sub-task and update scope checklist
    ↓
(If remaining tasks) → return to step 2
```

### 3. Speed: Parallel Execution of Well-Defined Tasks

- 5 parallel mascot generations: ~1 minute (sequential would be 5 minutes → 5x speedup)
- Large-scale codebase exploration
- Simultaneous multi-page construction (no file conflicts)

## 5 Practical Patterns

### Pattern 1: The Prep Line

In a professional kitchen, instead of one cook preparing all vegetables bit by bit before opening, multiple prep cooks each work independently.

**Use case:** Design exploration, code variation generation, test generation
**Characteristics:**
- Each Line Cook works independently on the same brief
- No file conflicts, dependency graphs, or merge logic needed
- Human cherry-picks results

Example: Generate 50 Parchi mascot variations → 5 Codex Spark sub-agents with 10 variations each → pick favorites

**Key insight:** Models have almost no "taste." Many developers also lack taste. Brute force solution: Have the Head Chef call many Line Cooks and let the human pick favorites.

### Pattern 2: The Dinner Rush

Like a Friday night kitchen — all stations (sauté, grill, garde manger, pastry) run simultaneously. Each Line Cook handles a different job while contributing to the same ticket.

**Use case:** Building multiple independent app components, creating tests for different modules, porting pages between frameworks
**Originator:** MoonshotAI's "swarm" concept proposed during Kimi-K2.5 training

**Requirements:**
- Work scope must be deep and specific
- Decomposable into individually verifiable steps
- Dependencies must be clearly documented
- File sets for each task must be pre-defined (preventing Line Cook overwrites)

**Important:** Tasks must not share files. If two Line Cooks need to edit the same file, a different pattern is needed.

### Pattern 3: Courses in Sequence

Like a tasting menu served in order — amuse-bouche → appetizer → main → dessert. But within one course, all stations run in parallel.

**Use case:** Full app rebuild, large-scale refactoring
**Concept:** Phased parallel execution — decompose project into "courses" (waves), each dependent on the previous. Within a course, execute in parallel.

Example: Full UI rebuild
- Course 1: Exploration and mapping
- Course 2: Build on Course 1's shared understanding
- Each course's Line Cook receives only the context brief relevant to their ticket, not the full conversation history

Requires dependency tree, strict ordering, and refined prompts. Reference: https://factory.ai/news/missions

### Pattern 4: The Prep-to-Plate Assembly

Each Line Cook doesn't make one dish from start to finish. One station trims and seasons protein, the next sears it, the next finishes in the oven, the expeditor plates and garnishes.

**Concept:** Line Cooks pass sequentially down the line. Each cook executes one small task → verifies → passes to the next station.

**Use case:** Long-running tasks, tasks requiring clearly observable and verifiable artifacts, research-heavy tasks, multi-step pipelines

**Core principle:** Don't drag unrelated history into one giant thread. Each phase receives only the context it needs and passes it on. **State is stored in files and task queues, not in conversation history.**

### Pattern 5: Here Comes Gordon Ramsay

In a professional kitchen, cooks don't serve food directly to customers. Inspection always happens. One person checks proper preparation, another confirms it matches the order and is properly plated.

**Concept:** Separate the Line Cook who writes code from the Line Cook who checks it. One builder cooks, two verifiers (code reviewer and visual/functional tester) verify in parallel. If issues are found, the builder gets one more chance.

**Most important rule:** Only one builder at a time. Multiple verifiers can run in parallel. This is the single most important rule to avoid merge conflicts and context drift, applying to all other patterns.

**When to use:** Always. Layer this on top of whatever pattern you're running. By separating build and verification, failures can be caught before they cascade to downstream tasks. Use browser automation, screenshots, and deterministic tests as verification steps.

With high-speed coding models like Codex Spark now available, adding verification costs essentially nothing.

## Conclusion

The solo agent one-shot era is over. As models get faster, context windows expand, and tools mature, these patterns will continue to evolve.

Take off your apron and put on your chef's coat. You run the kitchen, and your brigade is waiting.

---

*Thanks to input from Zhenwei Gao and James Wang, and @brickywhat who first introduced us to the term 'sloperator'. Illustrations by @halleychangg.*

## Related Concepts

- [[concepts/single-agent-ceiling]] — Limits of single agents and the "Sloperator" anti-pattern
- [[concepts/agent-team-swarm/agent-team-swarm]] — Hierarchical orchestration of multi-agent teams
- [[concepts/harness-engineering/agentic-workflows/subagents]] — Sub-agent delegation patterns
- X thread by @MilksandMatcha (April 2026)
