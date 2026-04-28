---
title: "Cognitive Load Patterns — Anti-Patterns and Solutions"
type: concept
aliases:
  - cognitive-load-patterns
  - zakirullin-patterns
created: 2026-04-16
updated: 2026-04-16
tags:
  - concept
  - methodology
  - software-engineering
  - design-patterns
  - anti-patterns
status: active
---

# Cognitive Load Patterns — Anti-Patterns and Solutions

Code and architecture patterns that reduce (or inflate) cognitive load, from Zakirullin's framework.

## Code-Level Anti-Patterns

### Complex Conditionals
```go
// Before 🤯 — tracking multiple logical states simultaneously
if val > someConstant
    && (condition2 || condition3)
    && (condition4 && !condition5) { ... }

// After 🧠 — introduce descriptive intermediate variables
isValid = val > someConstant
isAllowed = condition2 || condition3
isSecure = condition4 && !condition5
if isValid && isAllowed && isSecure { ... }
```

### Nested If Statements
```go
// Before — mental tracking of preconditions
if isValid {
    if isSecure {
        stuff
    }
}

// After — Early returns (guard clauses) let you focus on the happy path
if !isValid return
if !isSecure return
// 🧠 — preconditions cleared, focus on main logic
stuff
```

### Deep Inheritance Chains
`BaseController → GuestController → UserController → AdminController → SuperuserController`
- Modifying a child class requires mentally traversing parents → 🤯
- **Solution:** Prefer composition over inheritance

## Architecture-Level Insights

### Deep vs. Shallow Modules

| Type | Interface | Internals | Cognitive Load |
|------|-----------|-----------|----------------|
| **Deep Module** | Simple | Complex (hidden) | 🧠 Low |
| **Shallow Module** | Complex | Simple | 🤯 High (interaction tracking) |

**Unix I/O example:** Just 5 syscalls (`open`, `read`, `write`, `lseek`, `close`) hide hundreds of thousands of lines of complexity.

> "Important things should be big." — Carson Gross
> Critical functions can be large. Being prominent signals importance.

### SRP Reinterpreted

- **Misunderstanding:** "A module should do one thing" → leads to shallow factories like `MetricsProviderFactoryFactory`
- **Correct interpretation:** "A module should be responsible to **one user/stakeholder**"
- If bug fixes draw complaints from two business domains, that's an SRP violation

### Microservices Pitfalls

- Excessive decomposition → **distributed monolith**
- Case study: 5 developers, 17 microservices → 10-month delay, every change affects 4+ services
- **Principle:** Delay decomposition until individual deployment is truly necessary
- Historical lesson: Linux (monolithic) dominates, GNU Hurd (microkernel) is niche

### Layered Architecture (Hexagonal/Onion)

- Adding indirection ≠ true abstraction
- Debugging requires exponential mental tracing across layers
- Migration cost savings are ~10%; the real pain is data model incompatibility and **Hyrum's Law** (implicit behaviors become dependencies)

### DDD Application Scope

- DDD excels in **problem space** (ubiquitous language, bounded contexts, event storming)
- Misapplied in **solution space** (directory structure, repository patterns), it fragments subjective mental models
- Alternative: **Team Topologies** — a clear framework for distributing cognitive load across teams

## Language & Dependencies

### Choice Overload
- Too many language features force reverse-engineering "why this construct was chosen"
- C++: 21 initialization methods, context-dependent `||` operator
- Rob Pike: "Reduce cognitive load by limiting the number of choices."

### HTTP Status Codes vs. Self-Descriptive Responses
- Custom status mappings (401 vs 403 vs 418) force memorization
- Solution: self-descriptive strings in the response body `{"code": "jwt_has_expired"}`

### DRY Misuse
- Premature abstraction → tight coupling between unrelated components
- Rob Pike: "A little copying is better than a little dependency."
- Dependencies all become your code. Debugging 10+ level import stack traces is painful.

## HN Comments on Patterns

### Readability vs. Correctness Trade-off (*hackrmn*)
> "Writing readable code and writing correct code are often mutually exclusive."

Function programming eliminates variable mutation; OOP/imperative forces mental state tracking. For agentic engineering: LLM-generated code tends toward "works but unreadable" or "readable but fragile" — harness guardrails should enforce both.

### If-Mountain Architecture (*Buttons840*)
> "I realize I'm a 'developer with quirks' who builds abstractions."

Task assignment → explore relevant area → add if → test fails → add if → PR. This is the modern mainstream pattern. The real enemy isn't abstraction but **wrong abstraction** — correct abstraction dramatically reduces cognitive load.

### Early Return Debate (*mattmanser*)
> "Success values should always be returned at the end of a function."

Counterpoint: Zakirullin/Go community recommends early returns as guard clauses. Trade-off: multiple exit points require the reader to track all exit paths. Harness design should explicitly codify which convention agents follow.

### House Organization Analogy (*gnramires*)
> "Don't scatter pen collections across the house, but you don't need specialized carved niches for a $0.50 pen either."

**Rule of Three:** Consider abstraction after the 3rd duplication. 1-2 copies may have lower cognitive load than abstraction.

## Related

- [[concepts/cognitive-load-software-development]] — Main concept page
- [[concepts/cognitive-load-theory]] — Core theory and mental models
- [[concepts/cognitive-load-tool-support]] — Tooling and agentic engineering
