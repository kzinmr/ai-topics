---
title: "Loopcraft — The Art of Stacking Loops / Salty Lesson for Agents"
type: concept
created: 2026-06-12
updated: 2026-06-12
tags:
  - concept
  - ai-agents
  - agentic-engineering
  - prompting
  - workflow
sources:
  - "AINews 2026-06-12"
---

# Loopcraft — The Art of Stacking Loops / Salty Lesson for Agents

> **Definition:** Loopcraft is the philosophy that the primary leverage in agent systems is not better prompts, but loops that prompt agents autonomously — stacked to compound. The **Salty Lesson** is its core principle: *"Don't fix things yourself. Focus on systems that scale with more agents, like goals and orchestration."*

The Salty Lesson is the agent-engineering counterpart to [[concepts/rich-suttons-bitter-lesson|Rich Sutton's Bitter Lesson]]. Where Sutton says general methods leveraging computation beat hand-crafted features, the Salty Lesson says **loop-based systems leveraging many agents beat hand-crafted prompts**. The bitter part was for model researchers; the salty part is for agent builders.

---

## The Salty Lesson

| Dimension | Bitter Lesson (Sutton) | Salty Lesson (Steipete/Boris) |
|-----------|-----------------------|------------------------------|
| **Target** | Model research | Agent engineering |
| **Stop** | Hand-crafting features | Hand-crafting every prompt |
| **Instead** | Leverage computation at scale | Leverage agents at scale (loops + orchestration) |
| **Core** | *"General methods leveraging computation win"* | *"Don't fix things yourself. Focus on systems that scale"* |

---

## Origins (AINews 2026-06-12)

- **Steipete:** *"You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."*
- **Boris** (Claude Code lead): *"I don't prompt Claude anymore. I write loops, the loops do the work."*
- **[[entities/andrej-karpathy|Karpathy]]** on [[concepts/karpathy-loop|Autoresearch]]: *"To get the most out of the tools...you have to remove yourself as the bottleneck."*

All three converge: the human's time belongs on **systems** (loops, goals, orchestration), not individual prompts.

---

## Stacking Loops

Agent systems are stacks of loops that amplify each other:

```
Layer 3: Meta-orchestration (which agents to deploy, when)
Layer 2: Agent-level loop (plan → act → evaluate → repeat)
Layer 1: Tool-level loop (call → process → next)
```

> *"The entire game of the next century is to be able to stack loops as effectively as possible."* — AINews

---

## Related Concepts

| [[concepts/karpathy-loop]] | Tightly-scoped loopcraft in ML research — guardrails define autonomy |
| [[concepts/agent-loop-orchestration]] | The think→act→evaluate patterns loopcraft builds on |
| [[concepts/bitter-lesson-agent-harnesses]] | Minimal harness as the bridge between Bitter and Salty Lessons |
| [[concepts/compound-engineering-loop]] | How loopcraft compounds through the engineering process |
| [[concepts/rich-suttons-bitter-lesson]] | The original that inspired the Salty Lesson framing |
| [[entities/andrej-karpathy]] | Karpathy — demonstrated loopcraft via autoresearch |
| [[entities/steipete]] | Steipete — key articulator of "design loops, not prompts" |

---

## Practical Implications

1. **Optimize the loop, not the prompt.** A good loop with mediocre prompts beats a good prompt with no loop.
2. **Design for agent scaling.** If adding another agent doesn't help, your architecture is wrong. Goals and orchestration are scaling primitives.
3. **Remove yourself from the critical path.** Ask: *"If I stopped touching this system, would it keep improving?"* If no, you've built a puppet, not a loop.

---

*Page created: 2026-06-12 | Status: Complete*
