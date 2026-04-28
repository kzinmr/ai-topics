---
title: "Cognitive Load Tool Support — Agentic Engineering & Tooling"
type: concept
aliases:
  - cognitive-load-tooling
  - cognitive-load-agentic
created: 2026-04-16
updated: 2026-04-16
tags:
  - concept
  - methodology
  - software-engineering
  - agentic-engineering
  - tooling
status: active
---

# Cognitive Load Tool Support — Agentic Engineering & Tooling

How Zakirullin's cognitive load framework gains **new dimensions** in the age of AI coding agents, and what practical tooling supports it.

## Agentic Engineering Implications

### 1. Agents "Transfer" Cognitive Load
As [[concepts/cognitive-cost-of-agents]] (Simon Willison) points out, agents don't **reduce** work — they **redistribute** it. Zakirullin's theorem: extraneous load is reducible → harness design must minimize extraneous load when reading agent output.

### 2. AGENTS.md as a Deep Module
[[concepts/harness-engineering]]'s AGENTS.md pattern (~100 line table of contents + details in `docs/`) fits Zakirullin's deep module principle. Proliferating shallow AGENTS.md files replicates the shallow module anti-pattern in agent context.

### 3. Symphony Throughput & Cognitive Overload
When harnesses generate thousands of PRs per day, human reviewers easily enter 🤯 state. Zakirullin's 4-chunk theorem: reviewing agent output often exceeds the context a human can hold.

### 4. "Boring" Agent Pipelines Win
Just as Unix/Kubernetes/Redis succeed because they're "boring": simple interfaces + complex internals = understandable for both agents and humans.

## Tooling Recommendations from HN Analysis

### Noyce's Law — Redundancy Anxiety (*pessimizer*)
> "Redundancy makes people like me anxious: 'Did I miss something?'"

Duplicated code/settings trigger cognitive bias — the mind assumes intent behind every repetition. **DRY reinterpretation:** DRY is about eliminating conceptual duplication, not string compression. Agent-generated code should have unnecessary duplication automated away by linters/CI.

### Four Developer Personas (*noen, Microsoft DevDiv*)

| Persona | Focus | Strength | Risk |
|---------|-------|----------|------|
| **Mort** | Business outcome | Ships fast | Technical debt |
| **Elvis** | New tech | Innovation-driven | Over-engineering |
| **Einstein** | Algorithmic correctness | High performance | Over-abstraction |
| **Amanda** | Long-term maintainability | Clear, reviewable | Rejects necessary complexity |

> "Low ego → follow existing conventions → become familiar → feel simple"

LLMs can become any persona depending on the prompt. Harness designers should **explicitly control which persona** the agent operates as.

### Cyclomatic Complexity & Function Signatures (*safety1st*)
- Team standard: keep cyclomatic complexity low
- Function header comments should describe "developer intent"
- **Review priority:** function signature readability and sensibility
- For agentic engineering: automate linting + signature review in the harness

### The "Perfect Idea" Delusion (*0xbadcafebee*)
> "Why do software people assume 15 minutes of thought produces the correct idea?"

Scientific validation ≠ software design. Science is iterative testing; software proceeds with "good enough." LLMs generate "plausible but wrong" code — harnesses must **automate** testing/validation, otherwise cognitive load shifts to humans.

### Multi-Language Domain Hierarchy (*RossBencina*)
John Ousterhout's thesis: different programming languages cooperating at different domain levels has real value. TCL/Java/C → modern equivalent: Rust + Python + LLM prompts. Harness design should treat the harness as "glue between different languages/tools," with each layer at the right abstraction level.

### Corporate Environment & Short Tenure (*atomicnumber3*)
> "Companies structurally create environments where no one can care. Account for short engineer tenures."

After 3+ "owners," business logic degrades. Agents are the extreme of short tenure — they carry no context. Harnesses must provide **session persistence + context continuity**.

### Practical Data Modeling (*sfn42*)
> "Order ships to multiple addresses? Add a relationship table, expose a v2 API that doesn't affect existing code."

The best way to reduce cognitive load is **getting the data model right** — not excessive abstraction.

## Concise Summary (*nathane280*)

1. **Simplify conditionals** — descriptive intermediate variables
2. **Early returns** — guard clauses clarify the happy path
3. **Deep modules** — simple interface + complex internals
4. **Composition > inheritance** — eliminate hidden interactions
5. **DRY = conceptual deduplication** — not string compression
6. **Code is for humans** — comments describe "why"
7. **Team balance** — Mort/Elvis/Einstein/Amanda mix

## Related

- [[concepts/cognitive-load-software-development]] — Main concept page
- [[concepts/cognitive-load-theory]] — Core theory and mental models
- [[concepts/cognitive-load-patterns]] — Code and architecture anti-patterns
- [[concepts/cognitive-cost-of-agents]] — Willison's cognitive debt theory
- [[concepts/harness-engineering]] — Agent environment design
- [[concepts/context-window-management]] — Context constraint management
