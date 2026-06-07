---
title: "Cognitive Load in Software Development"
type: concept
aliases:
  - cognitive-load-theory
  - zakirullin-cognitive-load
created: 2026-04-16
updated: 2026-06-03
tags:
  - concept
  - methodology
  - software-engineering
  - cognitive-science
  - agentic-engineering
status: active
sources:
  - "https://minds.md/zakirullin/cognitive#long"
  - "https://github.com/zakirullin/cognitive-load"
---

# Cognitive Load in Software Development

Artem Zakirullin's **"Cognitive load is what matters"** — A systematic framework for cognitive load in software design that has gained 12,000+ stars on GitHub.

## Core Theorem

> "Confusion costs time and money. Confusion is caused by high cognitive load. It's not some fancy abstract concept, but rather **a fundamental human constraint.**"

- Developers spend overwhelmingly more time **reading** code than writing it
- Human working memory can only hold about **4 chunks**
- Exceeding this threshold causes confusion (🤯), reducing productivity and quality

## Two Types of Cognitive Load

| Type | Description | Controllability |
|------|-------------|----------------|
| **Intrinsic Load** | Inherent difficulty specific to the task/domain | Cannot be reduced |
| **Extraneous Load** | Presentation, unnecessary abstractions, author's quirks | **Reducible (this is where to focus)** |

### Load Notation
- 🧠 = Fresh working memory, zero load
- 🧠++ = Holding 2 facts, load increasing
- 🤯 = Cognitive overload, 4+ facts

## Code-Level Antipatterns and Solutions

### Complex Conditionals
```go
// Before 🤯 — Tracking multiple logical states simultaneously
if val > someConstant
    && (condition2 || condition3)
    && (condition4 && !condition5) { ... }

// After 🧠 — Introduce descriptive intermediate variables
isValid = val > someConstant
isAllowed = condition2 || condition3
isSecure = condition4 && !condition5
if isValid && isAllowed && isSecure { ... }
```

### Nested If Statements
```go
// Before — Mental tracking of preconditions
if isValid {
    if isSecure {
        stuff
    }
}

// After — Early returns (guard clauses) let you focus on the happy path
if !isValid return
if !isSecure return
// 🧠 — Preconditions cleared, can focus on main logic
stuff
```

### Deep Inheritance Chains
`BaseController → GuestController → UserController → AdminController → SuperuserController`
- Every time you modify a child class, you need to mentally traverse the parent classes → 🤯
- **Solution:** Prefer composition over inheritance

## Architecture-Level Insights

### Deep vs. Shallow Modules

| Type | Interface | Internals | Cognitive Load |
|------|-----------|-----------|----------------|
| **Deep Module** | Simple | Complex (hidden) | 🧠 Low |
| **Shallow Module** | Complex | Simple | 🤯 High (requires tracking interactions) |

**Unix I/O Example:** Just 5 system calls (`open`, `read`, `write`, `lseek`, `close`) hide hundreds of thousands of lines of complexity

> "Important things should be big." — Carson Gross
> Critical functions can be large. Being prominent signals importance.

### Reinterpreting SRP

- **Misunderstanding:** "A module should do only one thing" → proliferation of shallow factories like `MetricsProviderFactoryFactory`
- **Correct interpretation:** "A module should be responsible to **only one user/stakeholder**"
- If bug fixes draw complaints from two business domains, that's an SRP violation

### Microservices Pitfalls

- Excessive decomposition → **Distributed Monolith**
- Case study: 5 developers, 17 microservices → 10-month delay, every change affects 4+ services
- **Principle:** Delay splitting until individual deployment is truly needed
- Historical lesson: Linux (monolithic) dominates, GNU Hurd (microkernel) remains niche

### Layered Architecture (Hexagonal/Onion)

- Adding indirection ≠ true abstraction
- Debugging requires exponential mental tracing across layers
- Migration cost savings are only ~10%; the real pain comes from data model incompatibility and **Hyrum's Law** (implicit behaviors become dependencies)

### Scope of DDD

- DDD excels in the **problem space** (ubiquitous language, bounded contexts, event storming)
- Misapplied to the **solution space** (directory structure, repository patterns), subjective mental models become fragmented
- Alternative: **Team Topologies** — a clear framework for distributing cognitive load across teams

## Languages and Dependencies

### Choice Overload
- Too many language features require reverse-engineering "why was this construct chosen?"
- C++: 21 initialization methods, context-dependent `||` operator (constraints vs logic)
- Rob Pike: "Reduce cognitive load by limiting the number of choices."

### HTTP Status Codes vs Self-Descriptive Responses
- Custom status mapping (401 vs 403 vs 418) forces rote memorization
- Solution: Self-descriptive strings in the response body `{"code": "jwt_has_expired"}`

### DRY Misuse
- Premature abstraction → tight coupling between unrelated components
- Rob Pike: "A little copying is better than a little dependency."
- All dependencies become your code. Debugging 10+ levels of import stack traces is painful

## Mental Models and Onboarding

### Familiar Projects
- Mental models internalized in long-term memory → cognitive load is low
- The more unique mental models, the longer it takes new developers to deliver value

### The 40-Minute Rule
> "If they're confused for more than ~40 minutes in a row — you've got things to improve in your code."

- If cognitive load is kept low, new project members can contribute within hours
- "Boring" systems (Unix, Kubernetes, Chrome, Redis) succeed because they minimize cognitive load

## Implications for Agentic Engineering

Zakirullin's cognitive load framework takes on **new dimensions** in the age of AI coding agents:

### 1. Agents "Transfer" Cognitive Load
- As [[concepts/cognitive-cost-of-agents]] (Simon Willison) points out, agents don't **reduce** work — they **redistribute** it
- Zakirullin's theorem: extraneous load is reducible → harness design that minimizes extraneous load when reading agent output is critical

### 2. AGENTS.md Should Be a Deep Module
- The AGENTS.md pattern from [[concepts/harness-engineering]] (~100 line TOC + details under docs/) aligns with Zakirullin's deep module principle
- Proliferation of shallow AGENTS.md files = reproducing shallow module antipatterns in agent context

### 3. Symphony Throughput and Cognitive Overload
- In an era where harnesses generate thousands of PRs per day, human reviewers easily fall into a 🤯 state
- Zakirullin's 4-chunk theorem: reviewing agent output easily exceeds the amount of context humans can hold

### 4. "Boring" Agent Pipelines Win
- Just as Unix/Kubernetes/Redis succeeded because they were "boring"
- Simple interface + complex internals hidden = easy to understand for both agents and humans

## HN Comment Analysis (104 top-level comments, 362 total comments)

[HN Thread](https://news.ycombinator.com/item?id=45074248) — Score: 1,582, key insights extracted from 104 top-level comments.

### 1. The "Readability vs Correctness" Trade-off (hackrmn, 3,995 chars)

> "Writing readable code and writing correct code are often mutually exclusive"

- **FP vs OOP Fundamental Conflict**: Functional programming eliminates variable assignment itself. OOP/imperative programming forces mental tracking of variable state
- **Implication for Agentic Engineering**: LLM agent-generated code polarizes into "works but is unreadable" or "readable but fragile." Harnesses need guardrails that **guarantee both**
- Rules enforcing early return guards + descriptive variable names in agent output help balance "correctness + readability" as hackrmn describes

### 2. Mental Model Dependency (weiliddat, 2,334 chars)

> "Cognitive load reduction doesn't happen in a vacuum. Simple language constructs don't always beat abstraction"

- Cognitive load depends on the **reader's existing mental models**. For someone familiar with a framework, the framework has lower load than a `pile of if`
- **Lesson for harness design**: The assumption that "simpler is always better" is dangerous. Consider the training distribution of the target developer (or agent)
- weiliddat's counter-rebuttal: "When working with the same team long-term, tacit knowledge accumulates and cognitive load decreases. This isn't just a problem for corporate environments that assume frequent churn of new members."

### 3. Critique of "Pile of If" Architecture (Buttons840, 1,876 chars)

> "I'm aware that I'm a 'quirky smart developer.' I end up building abstractions"

- Task assignment → search relevant code → add if → test fails → add if → send PR. This is the modern mainstream pattern
- **Reevaluating abstraction**: It's not that "abstraction is bad" but rather "**wrong abstractions** are bad." Correct abstractions dramatically reduce cognitive load
- **Agent-era paradox**: LLMs can generate abstractions in bulk, but the cognitive load on human reviewers increases proportionally with abstraction depth. Harness designers need to set thresholds for "how much abstraction is acceptable"

### 4. Noyce's Law (pessimizer, 1,585 chars)

> "Redundancy makes someone like me anxious — 'did I miss something?' — and ruins forward progress"

- A cognitive bias where seeing duplicated code or config triggers speculation that "there must be some intention behind it"
- **Reinterpreting DRY**: DRY is not string compression, but **deduplication of concepts**. However pessimizer's point is the reverse case — "unjustified duplication" is itself cognitive noise
- **Agentic Engineering**: The cost of human reviewers wondering "is there an intention?" about unnecessary duplication in agent-generated code. Checks that can be automated via linter/CI should be automated

### 5. Programming as Theory-building (physidev, 1,913 chars)

> "Scientists, mathematicians, and software engineers all do the same thing: understand something and describe it in language"

- Connection to Peter Naur's "Programming as Theory-building" paper
- Code is not just a list of instructions, but a **formalization of domain understanding**. When the theory is lost, the code loses meaning
- **Harness design**: The perspective of having agents not just "generate code" but also "maintain domain theory." Reaffirming the value of injecting domain context into AGENTS.md and prompts

### 6. Microsoft DevDiv's 4 Personas (noen, 2,092 chars)

| Persona | Focus | Strength | Risk |
|---------|-------|----------|------|
| **Mort** | Business outcomes | Ships fast | Technical debt, "pile of ifs" |
| **Elvis** | New technology | Innovation-driven | Over-engineering, instability |
| **Einstein** | Algorithmic correctness | High performance, rigorous | Over-abstraction, slow delivery |
| **Amanda** | Long-term maintainability | Clear, reviewable | Rejects necessary complexity |

> "Low ego → follow existing conventions → become familiar with them → they feel simple"

- **Lesson for team composition**: The ideal team balances all 4 personas. Make code quality a "hard requirement" not a "nice-to-have"
- **Agent persona**: LLMs can be Mort or Einstein depending on the prompt. Harness designers should be able to explicitly control "which persona to operate with"

### 7. The Merits of Early Return (mattmanser, 1,687 chars)

> "Success values should always be returned at the end of a function. Early returns should only be used for errors or null results"

- **Counterpoint**: Zakirullin/Go community recommends early return as guard clauses
- **Trade-off**: early return of success = multiple exits = reader needs to track all exit points
- **Agentic Engineering**: Whether to prioritize "single exit point" or "early return" for agents needs to be explicit in harness coding conventions

### 8. House Organization Analogy (gnramires, 2,762 chars)

> "You shouldn't scatter your pen collection all over the house. But you don't need a dedicated engraved niche for a $0.50 pen either"

- **Appropriate level of abstraction**: Neither over-organization (over-engineering) nor neglect (technical debt) is good
- **Rule of Three**: Consider abstraction from the third duplication. For the 1st-2nd time, keeping duplication may have lower cognitive load

### 9. Multi-Language Domain Hierarchy (RossBencina, 2,485 chars)

> "John Ousterhout's thesis is that there's real value in multiple programming languages working together at different levels of domain"

- TCL/Java/C (John Ousterhout's example) → maps to the Rust + Python + LLM prompt hierarchy in modern times
- **Harness design**: Agent harnesses are "glue connecting different languages/tools." Each layer having the right abstraction level is critical

### 10. Critique of the "Perfect Idea" Delusion (0xbadcafebee, 1,992 chars)

> "Why do software people delude themselves into thinking 'if I think for 15 minutes, the absolutely correct idea will come to me'?"

- Scientific verification ≠ software design. Science relies on iterative testing; software moves forward with "it works for now"
- **Agent era**: LLMs generate code that's "plausible but wrong." If the harness doesn't **automate** testing/verification, cognitive load is transferred to humans

### 11. Cyclomatic Complexity and Function Signature Design (safety1st, 1,898 chars)

- Team standard: Keep function cyclomatic complexity low
- Use function header comments to describe "developer intent"
- **Review focus**: Prioritize readability and sensibility of function signatures above all
- **Agentic Engineering**: Incorporate automated linting + signature review of agent-generated code into the harness

### 12. Corporate Environment and Engineer Short Tenure (atomicnumber3, 1,656 chars)

> "Corporations structurally create a 'can't care' environment. Account for engineers' short tenures"

- After 3+ generations of "owners," business logic degrades
- **Agentic Engineering**: Agents are the extreme of "short tenure" — they don't carry over context. The harness needs to guarantee **session persistence + context continuity**

### 13. Practical Data Modeling (sfn42, 1,548 chars)

> "Order shipped to multiple addresses? Add a relationship table and expose a v2 API that doesn't affect existing code"

- Solving through data model changes rather than excessive abstraction
- **Lesson**: The best way to reduce cognitive load is to **design data structures correctly**

### 14. Concise Summary (nathane280, 1,549 chars)

HN Comments TL;DR:
1. **Simplify conditionals** — Descriptive intermediate variables
2. **Early Returns** — Guard clauses clarify the happy path
3. **Deep Modules** — Simple interface + complex internals
4. **Composition > Inheritance** — Eliminate hidden interactions
5. **DRY = Deduplication of concepts** — Not string compression
6. **Write code for humans** — Comments describe the "why"
7. **Team balance** — Right mix of Mort/Elvis/Einstein/Amanda

## Related Concepts

- [[comparisons/aposd-vs-clean-code]] — Contrast of Ousterhout vs Martin design philosophies. Integrates Deep/Small, comments/no-comments, TDD/Bundling debates from a Cognitive Load perspective
- [[concepts/cognitive-cost-of-agents]] — Willison's cognitive debt theory (cognitive cost in the agent era)
- [[concepts/harness-engineering]] — Lopopolo's agent environment design
- [[concepts/harness-engineering]] — Developer workflow patterns
- [[concepts/context-window-management]] — Context constraint management
- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — Code design for agents

## Sources

- Artem Zakirullin, ["Cognitive load is what matters"](https://minds.md/zakirullin/cognitive#long) (2025-10, GitHub 12k+ stars)
- [HN Discussion](https://news.ycombinator.com/item?id=45074248) (Score: 1,582, 104 top-level comments, 362 total)
- John Ousterhout, "A Philosophy of Software Design" (deep/shallow modules)
- Carson Gross, "Codin' Dirty" (important things should be big)
- Rob Pike, "Less is exponentially more" (choice overload)
- Hyrum's Law (implicit behaviors as dependencies)
