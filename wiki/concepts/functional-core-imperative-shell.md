---
title: "Functional Core, Imperative Shell"
type: concept
aliases:
  - fcis
  - functional-core-imperative-shell
  - agentic-shell-pattern
description: "Architecture pattern where deterministic, verifiable processing forms the 'functional core' and human validation, evaluation, and decision-making form the 'imperative shell.' As AI agents improve, more work migrates to the core, leaving humans focused on judgment calls."
category: concepts
sub_category: AI Agent Architecture
tags: [ai-agents, architecture-patterns, deterministic-core, human-in-the-loop, validation, decision-making]
status: complete
created: 2026-04-30
updated: 2026-04-30
source_slack: "C077ACXR5UY, 2026-03-30 23:54"
source_user: "U076RPG60QY (Kazuki Inamura)"
---

# Functional Core, Imperative Shell (FCIS)

## TL;DR

The **Functional Core, Imperative Shell** pattern separates software into two layers:
- **Functional Core**: Deterministic, verifiable, automatable processing (data transformation, code generation, mechanical tasks)
- **Imperative Shell**: Validation, evaluation, strategic decision-making about the external world

As AI agents become more capable, more work migrates from the shell to the core. The human role shifts from "doing the work" to "validating outcomes and making strategic decisions."

## Origin

This concept emerged from a Slack discussion (2026-03-30 23:54) about the future of software development with AI agents:

> "検証や評価や意思決定という、外界のモデリングしか残ってない (機械処理可能なfunctional coreの外側としての真のImperative Shellが残る形)"

The pattern is inspired by functional programming's separation of pure functions (no side effects) from impure operations (I/O, state changes). In the AI agent context, the "pure" core is what agents can automate, while the "impure" shell is what still requires human judgment.

## The Core/Shell Model

```
┌──────────────────────────────────────────────┐
│           IMPERATIVE SHELL                   │
│  ┌────────────────────────────────────────┐  │
│  │     FUNCTIONAL CORE (Agent)            │  │
│  │  - Data processing                     │  │
│  │  - Code generation                     │  │
│  │  - Mechanical execution                │  │
│  │  - Deterministic tasks                 │  │
│  └────────────────────────────────────────┘  │
│  - Validation                                │
│  - Evaluation                                │
│  - Strategic decision-making                 │
│  - External world modeling                   │
└──────────────────────────────────────────────┘
```

### Functional Core (What Agents Do)
- Data transformation and ETL
- Code generation and refactoring
- API calls and integrations
- Test execution and verification
- Document processing
- Repetitive mechanical tasks

**Key property**: Given the same input, produces the same output. Verifiable and automatable.

### Imperative Shell (What Humans Do)
- **Validation**: Is the output correct? Does it meet requirements?
- **Evaluation**: Is this the right approach? What are the trade-offs?
- **Decision-making**: What should we do next? What's the strategic direction?
- **External world modeling**: Understanding context, business needs, user expectations

**Key property**: Requires judgment, context, and understanding of the external world.

## The Shift: Why This Matters

As AI models improve, the **functional core expands** and the **imperative shell shrinks**:

```
Time →
┌──────────────────────────────────────────────┐
│ Shell shrinks                                │
│  ┌────────────────────────────────────┐      │
│  │ Core expands                       │      │
│  │                                    │      │
│  │                                    │      │
│  └────────────────────────────────────┘      │
└──────────────────────────────────────────────┘
```

### Phase 1: Manual Work (Today)
- Humans do both core and shell work
- Agents assist with some core tasks
- Heavy human involvement in execution

### Phase 2: Agent-Dominated Core (Near Future)
- Agents handle most core work
- Humans focus on shell (validation, decisions)
- Clear separation of responsibilities

### Phase 3: Thin Shell (Future)
- Agents handle nearly everything
- Human role is primarily strategic oversight
- Validation becomes the primary human task

## Practical Implications

### For Software Development
1. **Define clear boundaries**: What can agents do autonomously vs. what needs human review?
2. **Maximize the core**: Automate everything that's deterministic and verifiable
3. **Minimize the shell**: Keep human tasks focused on judgment, not execution

### For Team Organization
1. **Role evolution**: Developers shift from "coders" to "validators/strategists"
2. **Quality gates**: Humans validate at key points, not during execution
3. **Strategic focus**: More time for architecture, less for implementation

### For Agent Design
1. **Verifiable outputs**: The core must produce deterministic, testable results
2. **Clear interfaces**: Shell and core communicate through well-defined boundaries
3. **Observable behavior**: Humans need visibility into what the agent is doing

## Relationship to Other Patterns

### [[concepts/bitter-lesson-harnessing]]
- FCIS is the **architectural manifestation** of the Bitter Lesson
- As models improve, more work moves to the core
- Harness complexity decreases as the core handles more

### [[concepts/reasoning-compression]]
- Reasoning compression **reduces the shell's workload**
- Compressed reasoning = more deterministic processing in the core
- Less exploration needed = thinner shell

### [[concepts/generative-app-evolution]]
- Generative apps follow the FCIS pattern
- UI generation (core) → Business logic (core) → Human validation (shell)
- The shell handles statefulness and external context

### [[concepts/agent-serverless]]
- Serverless agents naturally embody FCIS
- The managed environment handles the core
- Humans manage the shell (configuration, validation)

## Examples

### Example 1: Code Generation
```
Functional Core (Agent):
- Parse requirements → Generate code → Run tests → Fix errors

Imperative Shell (Human):
- Review architecture decisions
- Validate business logic
- Decide whether to merge
```

### Example 2: Data Analysis
```
Functional Core (Agent):
- Fetch data → Clean → Transform → Generate visualizations

Imperative Shell (Human):
- Interpret results
- Decide which metrics matter
- Determine next steps
```

### Example 3: Customer Support
```
Functional Core (Agent):
- Parse inquiry → Search knowledge base → Draft response

Imperative Shell (Human):
- Handle escalations
- Validate response appropriateness
- Update knowledge base
```

## Design Principles

1. **Maximize the Core**: Automate everything that can be deterministic
2. **Minimize the Shell**: Keep human tasks focused on judgment
3. **Clear Boundaries**: Define exactly where agent responsibility ends
4. **Verifiable Outputs**: The core must produce testable results
5. **Observable Behavior**: Humans need visibility into agent execution
6. **Thin Shell, Wide Core**: As agents improve, the shell should shrink

## Future Trajectory

The FCIS pattern suggests a clear trajectory:
- **Short-term**: Agents assist with core tasks, humans do shell work
- **Medium-term**: Agents dominate the core, humans focus on validation
- **Long-term**: Agents handle nearly everything, humans provide strategic oversight

The key insight: **software complexity is not a permanent property — it's a temporary artifact of our current reasoning limitations.** As models improve, more complexity moves to the core, leaving only the truly non-deterministic tasks for humans.

## Sources

- Slack discussion (C077ACXR5UY, 2026-03-30 23:54): Original insight about FCIS
- Functional Programming "Boundaries" pattern (Gary Bernhardt): Inspiration for core/shell separation
- [[concepts/bitter-lesson-harnessing]]: Related concept about model capability evolution
