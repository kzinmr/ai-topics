---
title: "AI Programming as Theory Building"
date: 2026-04-10
sources:
  - "https://www.seangoedecke.com/programming-with-ai-agents-as-theory-building/"
  - "https://www.seangoedecke.com/llm-driven-agents/"
tags: [software-engineering, ai-coding, theory, peter-naur]
related:
  - "[[concepts/agentic-engineering.md]]"
  - "[[cognitive-cost-of-agents]]"
  - "[[harness-engineering]]"
---

# AI Programming as Theory Building

Sean Goedecke's analysis applying Peter Naur's 1985 "theory building" concept to AI-assisted programming.

## Peter Naur's Theory (1985)

- The primary artifact of software engineering is **not the code**, but the engineer's **mental model** ("theory") of how the system works
- Code is merely a byproduct of the theory
- Making changes requires first updating the theory, then modifying the code

## AI Agents and Theory Building

### The Critical Limitation
- AI agents are **permanently in an unfortunate position**: forced to construct a theory of the software from scratch, every single time they're spun up
- Agents lack persistent context and theory retention between sessions
- Documentation cannot fully capture a Naur theory

### Goedecke's AI-Assisted Workflow
1. Spin up 2–3 parallel agents to answer questions or draft code
2. Scan output against personal mental model
3. **Reject ~80%** (fails to align with system theory)
4. **Review ~20%** (plausible), manually test/tweak
5. **Merge ~10%** into final PR

*Result: Only ~10% of AI output is used. The engineer's theory remains the gatekeeper.*

### Can AI Agents Build Naur Theories?
- **Evidence they can**: Successfully make working changes to codebases
- **Evidence they can't**: Logs show agents struggle with novel architectures
- **Practical view**: Whether AI "truly" thinks is metaphysically debatable but practically irrelevant

## Future Directions

- **Continuous learning**: Encoding codebase knowledge directly into model weights
- **Extended context windows**: Supporting weeks-long sessions in a single agent run
- **Persistent state management**: Allowing agents to maintain and update theories over time

## Related Concepts

- [[cognitive-cost-of-agents]]: Developers losing deep understanding of their codebase
- [[concepts/agentic-engineering.md]]: Humans as orchestrators of AI agents
- [[harness-engineering]]: Designing environments for agents
