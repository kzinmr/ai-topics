---
title: "Single-agent AI coding is a nightmare for engineers"
source_url: "https://x.com/milksandmatcha/status/2044863551186309460"
authors: ["Sarah Chieng (@MilksandMatcha)", "@0xSero"]
date: 2026-04-17
type: twitter-thread
tags: [multi-agent, coding-agents, back-of-house, single-agent-ceiling]
---

# Single-agent AI coding is a nightmare for engineers

By Sarah Chieng (@MilksandMatcha) and @0xSero
April 17, 2026

## The Single-Agent Ceiling

Every developer building with AI agents hits a ceiling the moment their project graduates from simple tasks (like a 3D HTML snake game) to anything more practical. This happens for two reasons:
1. We expect too much from a single agent
2. We do not break problems into simple enough, verifiable tasks

The typical workflow: pay upfront subscription ($200/month), write prompts (doing both prompt AND context engineering), wait 35+ minutes while the agent is "synthesizing," "perusing," "effecting," and "germinating." End result: files of bad code, a bloated context window, counting remaining tokens on your left hand.

Then you grab an apple, compact the context, type heavy-handed verbal abuse, re-explain everything from scratch, and pray the next attempt gets further. By now, the spark and joys of AI coding are long dead.

## Stop Being a One-Shot Sloperator

Instead of selling courses on prompt engineering, SaaS context management tools, or hyping the newest model, this article walks through what actually works: running a proper "back of house" — multi-agent workflows.

## Why Multi-Agent Workflows Are Practical Now

Three factors have made multi-agent workflows much more practical:
1. Underlying models have gotten better
2. Popular AI coding agents have made multi-agent orchestration easier to set up
3. **Speed** — OpenAI's Codex Spark (powered by Cerebras) runs at roughly 1,200 tokens/second, making parallel and verification steps practical that would otherwise be too time-costly

Example: Figma MCP task to copy a website into Figma:
- Single agent workflow: 36.5 min/run average, 12 interventions, 100% failure rate
- Multi-agent workflow with Codex Spark: 5.2 min/run, 2 manual interventions, success on first try

## The Back of House Metaphor

Multi-agent workflows fix the single-agent ceiling at the architecture level. Instead of one cook doing everything, you have:

### The Head Chef (Orchestrator)
- Takes the order from the human
- Breaks it into scoped, verifiable tickets
- Hands each one to a line cook to execute
- Responsible for planning, coordination, and task decomposition
- Only tool is `delegate_task`
- Only sees high-level goals plus summaries of subagent outputs

### The Line Cooks (Subagents)
- Takes the ticket (task assignment) from the Head Chef
- Gets the job done, no questions asked
- Each gets its own fresh station (context window)
- Does its work, returns the plate, and clocks out
- Can read, write, use MCPs, and any other tools needed
- Only sees their assigned prompt and a fresh context window (no prior history)

The trick: the line cook doesn't get the full order history or the 15,000-token master plan. It gets the minimum viable context to cook one specific dish.

In AI agents like Codex, you create a line cook by telling your agent to "use subagents." The new instance gets a prompt, a set of files it can access, and any context it needs.

## Three Immediate Wins from Running a Back of House

### 1. Tokens: Your Effective Context Window Goes from ~200K to 25M+

- Human talks exclusively to the orchestrator
- Orchestrator is stripped of all tools other than `delegate_task`
- If orchestrator wants to take an action, it spawns a sub-agent via `delegate_task`
- Each sub-agent has its own fresh context window, starting only with a prompt
- Sub-agents can read, write, use MCPs, and any other tools
- Sub-agents return a summary of their work back to the Head Chef

The orchestrator never has to read files, write files, or see tool-call results directly, effectively extending its context window to as many sub-agents as it can spawn. You can work all day without losing context, compacting, or starting over.

### 2. Control: Enforce Sequential Workflows at Each Turn

Instead of one agent doing exploration, cooking, tasting, and plating, each step becomes a precise, sequential ticket:

- Sub-agent A: Breaks the order into a "contract" with subtasks and criteria
- Sub-agent B: Explores the next subtask
- Sub-agent C: Tests the code generated in the prior subtask. If tests pass validation criteria, move on. Otherwise respawn the coding line cook to fix identified issues.
- Sub-agent D: Documents the subtask and updates the scope checklist

If any subtasks remain, continue from step 2. Otherwise, service is done.

In internal trials, this sequential loop reduced manual interventions by **84.3%** compared to single-agent runs on the same brief.

### 3. Speed: Run Well-Defined Tasks in Parallel

Spawn multiple sub-agents in parallel for:
- Generating logos, images, mascots, assets, mockups, designs, or tests
- Exploring a massive codebase orders of magnitude faster
- Building multiple pages quickly, where each subagent works on separate parts of a codebase and doesn't overwrite each other

Example: Running five parallel mascot generations took roughly one minute versus five minutes sequentially (~5x speedup on taste-driven exploration tasks).

## Five Patterns That Actually Work

### Pattern 1: The Prep Line

Before service, a professional kitchen doesn't have one cook slowly dicing every single vegetable. It has a row of prep cooks each working independently on the same station.

**Use case**: Design exploration, code variations, test generation. Have line cooks each generate many options, then manually pick the best ones. Every line cook works on the same brief independently, with no file conflicts, dependency graphs, or merge logic.

**Example**: Created 50 variations of a mascot for Parchi by dispatching 5 Codex Spark sub-agents with 10 variations each, then cherry-picked the favorites.

**Key insight**: Great way to inject taste into AI workflow. Models today have very little taste. Instead of manually sourcing design examples or writing extensive style guidelines, have the Head Chef call a brigade of line cooks and cherry-pick your favorite.

### Pattern 2: The Dinner Rush

During a Friday night dinner rush, every station in the kitchen (sauté, grill, garde manger, pastry) is firing simultaneously. Each line cook owns a different job, but they're all plating at once, all contributing to the same ticket.

This is the concept behind **"swarms"**, pioneered by MoonshotAI when they trained Kimi-K2.5. Each line cook is responsible for a single, scoped, distinct task. They run simultaneously, all contributing to one shared goal.

**Requirements**:
- Deeply specific scope of work
- Scope breaks into individual, verifiable steps
- Clearly documented dependencies
- Each task should only require a predefined set of files to change (so line cooks don't overwrite each other)

**Important**: The key requirement is that tasks don't share files. The moment two line cooks need to edit the same file, you need a different pattern.

### Pattern 3: Courses in Sequence

A tasting menu doesn't come out all at once. The amuse-bouche goes out before anyone fires the appetizer, appetizers clear before entrées start plating, and dessert waits its turn. But within a single course, every station is cooking in parallel.

This is **phased parallel execution**. Break your project into courses (or "waves") where each course strictly depends on the one before it. Within each course, any number of tasks and line cooks can run in parallel.

**Perfect for**: Bigger projects like full app rebuilds or large refactors.

Requires a dependency tree, strict ordering, and refined prompts. Reference: https://factory.ai/news/missions for how they've handled this.

**Real example**: Rebuilding an entire UI. Course 1 explored and mapped everything, Course 2 built on top of that shared understanding. Neither course's line cooks needed the full conversation history — they got exactly the context brief relevant to their ticket.

As the human, you clearly define what is needed. The course structure gives you parallelism and sequencing, which is why it scales to real projects better than pure swarms.

### Pattern 4: The Prep-to-Plate Assembly

Line cooks don't each build a dish from scratch. One station trims and seasons the protein, the next sears it, the next finishes it in the oven, and the expediter plates and garnishes. Each station has one clear job, hands off cleanly, and nothing drags sauce from the previous ticket into the next.

In this pattern, line cooks operate **sequentially down the pass**. Each cook does one smaller task, validates it, then hands the workpiece to the next station.

**Perfect for**: Long-horizon tasks with clear, observable, and verifiable outcomes; research-heavy tasks; multi-step pipelines.

Core principle: Do not keep dragging unrelated history through one giant thread. Each phase gets enough context to do its part, then hands off. **State lives in files and task queues, not in conversation.**

Example: Running a custom model on specific hardware — each line cook had a clear, bounded job.

### Pattern 5: Here Comes Gordon Ramsay

In a professional kitchen, the chef makes the dish, but it does not go straight to the customer. It passes through inspection first. One person checks whether it was cooked properly while another checks whether it matches the order and is plated correctly.

This final pattern isn't a project architecture so much as a **discipline**: you separate the line cooks that write code from the line cooks that check code. One builder cooks, while two verifiers (a code reviewer and a visual/functional tester) run in parallel to validate the output. If either verifier flags an issue, the builder gets another pass.

With near-instant coding models like Codex Spark, adding verification is practically free.

**Key rule**: Only one builder writes at a time, but multiple verifiers can run simultaneously. This is the single most important rule for avoiding merge conflicts and context drift, and it applies inside every other pattern.

**When to use it**: Always. Whatever pattern you're running, layer this on top. Separating build from verify catches failures before they cascade into downstream tasks. Use browser automation, screenshots, and deterministic tests for the verify step. The goal is that no line cook's output makes it onto the pass without evidence that it works.

## Where This Is Heading

The era of the solo-agent one-shot is over. We're still early, and these patterns will keep evolving as models get faster, context windows get longer, and tooling matures.

Take off the apron and put on the chef's coat. You're running the kitchen now, and your brigade is waiting.

---

Thanks to input from Zhenwei Gao and James Wang, and @brickywhat who first introduced us to the term 'sloperator'. Illustrations by @halleychangg.
