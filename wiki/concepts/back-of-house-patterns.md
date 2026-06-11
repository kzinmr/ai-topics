---
title: Back of House Multi-Agent Patterns
type: concept
created: 2026-04-18
updated: 2026-04-18
tags:
  - multi-agent
  - orchestration
  - coding-agents
  - agentic-engineering
aliases: ["kitchen-metaphor", "head-chef-pattern", "line-cook-pattern", "multi-agent-kitchen"]
sources: []
---

# Back of House Multi-Agent Patterns

> Co-authored by: [[entities/milksandmatcha|Sarah Chieng]] (@MilksandMatcha) + [[entities/sero|Sero]] (@0xSero)
> Originally published: X thread "Single-agent AI coding is a nightmare for engineers" (April 2026)

A practical multi-agent workflow pattern using the professional kitchen (Back of House) metaphor. A practical framework for solving the limitations of single-agent [[concepts/single-agent-ceiling]].

## Background: The Single-Agent Ceiling

Single-agent AI coding breaks down when projects grow from simple tasks (HTML snake games, etc.) to practical scale.

**Structure of the problem:**
- Pay $200/month subscription, write prompts, wait 35+ minutes → result is bug-ridden code
- Context window balloons, falling into a "compact and re-explain from the beginning" loop
- The agent keeps displaying "synthesizing", "perusing", "effecting", "germinating" with no progress

**The "Sloperator" Anti-pattern**: A single-shot approach trying to do everything at once. Expecting too much from a single agent, failing to decompose problems into small, verifiable tasks.

## Why Multi-Agent Is Now Practical

1. **Foundation model performance improvements**
2. **Orchestration tool maturity** — OpenAI Codex, Anthropic Claude Code, MCP ecosystem
3. **Breakthrough speed** — OpenAI Codex Spark (Cerebras) runs at ~1,200 tokens/sec. This makes parallel processing and verification steps practical where time cost previously made them unrealistic.

### Empirical Data: Figma MCP Task Comparison

| Metric | Single Agent | Multi-Agent |
|--------|-------------|-------------|
| Average execution time | 36.5 min | 5.2 min |
| Manual interventions | 12 | 2 |
| Success rate | 0% | 100% (first try) |

Internal trials saw **84.3% reduction** in manual intervention for sequential loops.

## Metaphor: Kitchen Role Division

### Head Chef (Orchestrator)

- Receives orders (requests) from humans
- Decomposes work into scoped, verifiable tickets
- Assigns each ticket to Line Cooks
- **Only responsible for planning, coordination, and task decomposition**
- Only has the `delegate_task` tool
- Only sees high-level goals and sub-agent output summaries
- Does not directly read or write files

### Line Cook (Sub-agent)

- Receives tickets from Head Chef and executes without question
- Works in **their own independent, fresh context window**
- Has full access to all necessary tools: read, write, MCP usage
- Given only **minimal context** necessary for their specific task
- Returns results and **clocks out** (carries no state) after completion

**Key design principles:**
- Do not give Line Cooks a 15,000-token master plan document or full conversation history
- Only give the minimum context needed to prepare a specific dish
- **State is stored in files and task queues, not in conversation history**

## Three Immediate Benefits

### 1. Tokens: Effective Context Window ~200K → 25M+

The human only talks to the Orchestrator, who only delegates to sub-agents. Since each sub-agent has an independent context window, the Orchestrator's context never depletes — the effective context expands by the number of spawnable sub-agents.

### 2. Control: Sequential Workflow Enforced Per Turn

```
Sub-agent A: Decompose order into sub-tasks and "contracts" with criteria
    ↓
Sub-agent B: Explore and implement the next sub-task
    ↓
Sub-agent C: Test generated code. Pass → next, Fail → regenerate Sub-agent B
    ↓
Sub-agent D: Document sub-task and update scope checklist
    ↓
(If remaining tasks) → return to step 2
```

### 3. Speed: Parallel Execution of Well-Defined Tasks

5 parallel mascot generations: ~1 minute (sequential would be 5 minutes → 5x speedup). Enables large-scale codebase exploration and simultaneous multi-page construction (no file conflicts).

## 5 Practical Patterns

### Pattern 1: The Prep Line

> "In a professional kitchen, instead of one cook preparing all vegetables bit by bit before opening, multiple prep cooks each work independently"

- **Use case**: Design exploration, code variation generation, test generation
- **Characteristic**: Each Line Cook works independently on the same brief. No file conflicts, dependency graphs, or merge logic needed. Human cherry-picks results.
- **Example**: Generate 50 Parchi mascot variations → 5 Codex Spark sub-agents with 10 variations each → pick favorites

**Key insight**: Models have almost no "taste." Many developers also lack taste. Brute force solution: Have the Head Chef call many Line Cooks and let the human pick favorites. This eliminates the tedious process of manually searching for design samples or writing massive style guidelines.

### Pattern 2: The Dinner Rush

> "Like a Friday night kitchen, all stations (sauté, grill, garde manger, pastry) run simultaneously"

- **Use case**: Building multiple independent app components, creating tests for different modules, porting pages between frameworks
- **Originator**: MoonshotAI's "swarm" concept proposed during Kimi-K2.5 training

**Requirements:**
- Work scope must be deep and specific
- Decomposable into individually verifiable steps
- Dependencies must be clearly documented
- File sets for each task must be pre-defined (preventing Line Cook overwrites)

**Important:** Tasks must not share files. If two Line Cooks need to edit the same file, a different pattern is needed.

### Pattern 3: Courses in Sequence

> "Like a tasting menu served in order — amuse-bouche → appetizer → main → dessert. But within one course, all stations run in parallel"

- **Use case**: Full app rebuild, large-scale refactoring
- **Concept**: Phased parallel execution — decompose project into "courses" (waves), each dependent on the previous. Within a course, execute in parallel.

**Example:** Full UI rebuild
- Course 1: Exploration and mapping
- Course 2: Build on Course 1's shared understanding
- Each course's Line Cook receives only the context brief relevant to their ticket, not the full conversation history

Requires dependency tree, strict ordering, and refined prompts. Reference: [factory.ai/news/missions](https://factory.ai/news/missions)

### Pattern 4: The Prep-to-Plate Assembly

> "Each Line Cook doesn't make one dish from start to finish. One station trims and seasons protein, the next sears it, the next finishes in the oven, the expeditor plates and garnishes"

- **Concept**: Line Cooks pass sequentially down the line. Each cook executes one small task → verifies → passes to the next station.
- **Use case**: Long-running tasks, tasks requiring clearly observable and verifiable artifacts, research-heavy tasks, multi-step pipelines

**Core principle**: Don't drag unrelated history into one giant thread. Each phase receives only the context it needs and passes it on. **State is stored in files and task queues, not in conversation history.**

### Pattern 5: Here Comes Gordon Ramsay

> "In a professional kitchen, cooks don't serve food directly to customers. Inspection always happens"

- **Concept**: Separate the Line Cook who writes code from the Line Cook who checks it. One builder cooks, two verifiers (code reviewer and visual/functional tester) verify in parallel. If issues are found, the builder gets one more chance.
- **When to use: Always.** Layer this on top of whatever pattern you're running.

**Most important rule:** Only one builder at a time. Multiple verifiers can run in parallel. This is the single most important rule to avoid merge conflicts and context drift, applying to all other patterns.

With high-speed coding models like Codex Spark now available, adding verification costs essentially nothing. Use browser automation, screenshots, and deterministic tests as verification steps. "No Line Cook's output should pass (reach the customer) without evidence it works."

## Conclusion

The solo agent one-shot era is over. As models get faster, context windows expand, and tools mature, these patterns will continue to evolve.

> "Take off your apron and put on your chef's coat. You run the kitchen, and your brigade is waiting."

## Related Concepts

- [[concepts/single-agent-ceiling]] — Limits of single agents and the "Sloperator" anti-pattern
- [[concepts/session-hierarchy-management]] — This pattern integrated with trq212's session management into a 3-tier framework
- [[concepts/context-engineering/context-window-management|Context Window Management]] — Level 1: Context hygiene within a single session
- [[concepts/agent-team-swarm]] — Hierarchical orchestration of multi-agent teams
- [[concepts/harness-engineering/agentic-workflows/subagents]] — Sub-agent delegation patterns
- [[concepts/harness-engineering]] — Engineering methodology for agent usage
- [[concepts/context-engineering|Context Engineering]] — Context engineering

## Sources

- X thread by Sarah Chieng (@MilksandMatcha) + @0xSero (April 2026)
