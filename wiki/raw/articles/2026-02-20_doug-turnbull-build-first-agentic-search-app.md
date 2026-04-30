---
title: "How To Build Your First Agentic Search Application — Doug Turnbull (Vanishing Gradients Interview)"
created: 2026-02-20
author: Doug Turnbull (@softwaredoug)
source: YouTube (Vanishing Gradients channel)
url: https://www.youtube.com/watch?v=AJPH9kpN3Sc
type: talk
duration: 35:23
tags: [agentic-search, tool-calling, harness-engineering, bm25, llm-as-judge, pydantic-ai, reasoning-loops, long-running-agents]
---

# Talk Overview

A 35-minute interview with Doug Turnbull on the **Vanishing Gradients** podcast (hosted by Hugo Stefan). Turnbull discusses the practical side of building agentic search applications — moving from the conceptual arguments of his blog posts to actual code-level implementation patterns.

## Key Topics & Timestamps

| Time | Topic |
|------|-------|
| 00:00 | Meet Softwaredoug & What We'll Cover |
| 02:07 | Why Agentic Search Matters: Passive vs Active Search Spectrum |
| 05:02 | Real-World Use Case: Job Hunting, Exhaustive Search & Automating the Spreadsheet Loop |
| 07:23 | What Makes an Agent: Tools + Reasoning + Reformulation |
| 10:17 | Simple Tools Win: BM25 Transparency, Grep Analogy & Measured Gains |
| 12:45 | Q&A: Limits of Grep/File-System Search vs Ranked Retrieval |
| 15:13 | Under the Hood: The Core Tool-Calling Loop in Code |
| 19:39 | Improving Quality: Harness Loop, Validation, LLM-as-Judge & "Try Harder" Feedback |
| 25:08 | Where It's Going: Long-Running Agents, Memory/Compaction & Recursive LMs |
| 29:31 | Frameworks & Build-vs-Buy: Pydantic AI, Hand-Rolling, Team Comfort |

## Core Content

### Passive vs Active Search Spectrum
Turnbull frames search on a spectrum:
- **Passive:** User types query → gets results. Single-shot, no iteration.
- **Proactive:** User has a spreadsheet of 100 job postings and manually vets each one. The user *is* the agent, iterating through results.
- **Active (Agentic):** Agent automates the proactive loop — iterating results, evaluating relevance, reformulating queries, and continuing until done.

### What Makes an Agent: Tools + Reasoning + Reformulation
The three essential components:
1. **Tools** — Simple, transparent APIs (BM25, grep) that the agent can reason about
2. **Reasoning** — LLM reflects on results and decides next action
3. **Reformulation** — Agent rewrites queries based on what it learned from previous results

### Simple Tools Win
Turnbull reiterates his core argument with concrete evidence:
- BM25's transparency lets agents understand *why* results are returned
- Complex search APIs (with hidden synonym expansion, query rewriting, reranking) confuse agents
- The grep analogy: agents trained on code naturally navigate file systems; grep is a "happy path" they learned during training

### Under the Hood: The Core Tool-Calling Loop
Code-level detail on the agent loop:
1. Agent receives user query + system prompt with tool descriptions
2. Agent decides: call a tool (search) or generate final answer
3. Search results come back as structured observations
4. Agent reflects on results: "Are these relevant? Do I need to try again with different keywords?"
5. If not satisfied, agent reformulates and calls search again
6. Loop continues until agent is confident or hits iteration limit

### Improving Quality: The Harness Loop
The "try harder" pattern in code:
- **Inner loop:** Agent iterates through tool calls
- **Outer harness loop:** Validates agent output against quality criteria
- **LLM-as-a-Judge:** Scores each result; if below threshold, passes feedback back to agent ("Result X has low Y, keep trying")
- This is the concrete implementation of the two-loop architecture from the "Grep Moment" article

### Future Directions
- **Long-running agents:** Agents that persist across hours or days, revisiting search tasks
- **Memory/compaction:** Compression of agent's reasoning history to fit in context windows over long sessions
- **Recursive LMs:** The agent calling itself recursively to handle deeper search tasks

### Frameworks & Build-vs-Buy
Turnbull's pragmatic advice:
- **Pydantic AI** — Good starting point for structured outputs and tool definitions
- **Hand-rolling** — Recommended for teams that know their domain intimately; lets you control every part of the loop
- **Decision factor:** Team comfort and domain complexity, not theoretical purity

## Connection to Wiki

This interview serves as the **implementation companion** to Turnbull's conceptual blog posts. Key connections:

- **[[concepts/agentic-search]]** Level 2 (Harness Engineering) — The tool-calling loop is the harness layer in action
- **[[concepts/agentic-search]]** Two-loop architecture — The harness loop + LLM-as-judge pattern is shown in code
- **[[concepts/pydantic-ai]]** — Mentioned as a practical framework for building agentic search
- **[[concepts/bm25]]** — Endorsed as the "simple tool" that agents can reason about
- **[[entities/doug-turnbull-core-ideas]]** — This is the code-level version of the ideas documented there
- **Long-running agents + memory compaction** — Connects to [[concepts/rlm]] and context management topics

## Sources
- [Original video](https://www.youtube.com/watch?v=AJPH9kpN3Sc)
- [Building AI Applications course (Maven)](https://maven.com/hugo-stefan/building-ai-apps-ds-and-swe-from-first-principles)
