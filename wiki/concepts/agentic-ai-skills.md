---
title: "Agentic AI Skills Design"
created: 2026-04-27
updated: 2026-04-27
tags: [skills, agentic-ai, prompt-engineering, harness-engineering]
aliases: [ai-skills, agent-skills]
related: [[concepts/agent-harness]], [[concepts/harness-engineering]], [[concepts/personal-os-for-ai-agents]], [[concepts/tool-orchestration]]
sources: [
  "https://x.com/IntuitMachine/status/2043071219667480853"
]
---

# Agentic AI Skills Design

## Summary

Agentic AI Skills Design is the discipline of writing reusable documents that teach AI systems how to approach entire categories of tasks — not what to do in one specific situation, but the process and judgment framework. A well-designed skill transforms an AI from a one-shot responder into a persistent capability that compounds over time as models improve.

## The 10 Design Principles

### 1. Skills Are Recipes, Not Orders
A skill describes a process with parameters (inputs). "Analyze customer feedback" is an order; "Skill: Thematic Analysis, Parameters: CORPUS, QUESTION, DEPTH, Process: Read → Identify → Name → Examples → Synthesize" is a recipe. One recipe, hundreds of use cases.

### 2. Teach Thinking, Not Conclusions
Good skills invoke judgment, not replace it. The test: can you invoke this skill to argue the opposite conclusion and get an appropriately different answer based on evidence? If it always points one direction, it's a prompt in disguise.

### 3. Draw the Line Between Judgment and Computation
Judgment = where intelligence lives (reading documents, weighing considerations, pattern recognition). Computation = where reliability lives (database queries, arithmetic, sorting). Skills should orchestrate this boundary explicitly: mark which steps require judgment (let AI think) and which require computation (call a tool).

### 4. The Magic Is in Reading Everything
Don't pre-filter documents to "relevant" — you don't know what's relevant until you've read it. Build skills that read everything and synthesize (diarization), noticing contradictions and tracking how stories change over time. The power is in synthesis from the full picture.

### 5. The Right Document at the Right Moment
Don't load everything everywhere. Build resolvers — routing systems that load the right context at the right moment. A great assistant doesn't read the entire company manual when you ask a question. Your AI's attention is precious; spend it on what matters.

### 6. Push Intelligence Up, Push Execution Down
Three-layer architecture:
- **Top (Skills)** — Rich documents with process, judgment, wisdom. Where 90% of value lives.
- **Middle (Harness)** — Thin plumbing (maybe 200 lines of code). Runs AI in loop, manages context, calls tools.
- **Bottom (Tools)** — Fast, simple programs. Same input, same output, every time.

Anti-pattern: "fat harness" with embedded business logic and thin skills as afterthoughts.

### 7. Fast and Narrow Beats Slow and General
General-purpose tools are slow, bloat context, and hide complexity. Build tools that are fast, narrow, and dumb — each does one thing in under half a second. Tools are scaffolding, not architecture. Delete them when done.

### 8. Chase "Pretty Good" — That's Where Improvement Lives
"OK" responses (not "Bad" or "Great") are where refinement lives. "Bad" are bugs; "OK" means the mechanism functioned but something fell short. Build a learning loop focused on lukewarm responses — read what the AI produced, read user feedback, identify the gap, modify the skill to close it.

### 9. Write It Once, It Runs Forever
Every skill is a permanent upgrade. Unlike a clever prompt you forget, a skill is saved, versioned, and available forever. It runs at 3 AM. When models improve, every skill automatically gets better. Over time, skills compound like company assets — but they don't depreciate.

### 10. Same Process, Different World
A skill encodes a process that works across domains. The same investigative skill can be used for medical research, forensic analysis, or policy compliance — the process is the same, the world changes with each invocation.

## Key Ideas

- Skills encode process; models provide capability — the compounding effect comes from their interaction
- The harness should be thin; intelligence should live in skills, not code
- Resolution/routing is critical for managing finite attention budgets
- "OK" responses contain more improvement signal than "Bad" responses
- Append-only data patterns (JSONL) prevent agent-induced data loss
- Cross-module references enable knowledge graph traversal without loading everything

## Pitfalls

- Writing skills as orders instead of recipes (baked-in specifics)
- Pre-deciding outcomes in skills (turning AI into a puppet)
- Letting AI do computation that tools should handle
- Over-engineering schemas first pass (agents struggle with sparse data)
- Not splitting modules (loading too much context for simple tasks)
- One-off work instead of codifying into skills

## Related Concepts
- [[concepts/agent-harness]] — The harness layer that skills sit above
- [[concepts/harness-engineering]] — Principles of agent harness design
- [[concepts/personal-os-for-ai-agents]] — File-based personal OS using skills
- [[concepts/context-management]] — Managing context windows and attention
