# The Anatomy of an Agent Harness
**Source:** https://blog.langchain.com/the-anatomy-of-an-agent-harness
**Author:** Vivek Trivedy (LangChain)
**Date:** 2026-03-10
**Extracted:** 2026-04-25

## Key Takeaways

- Agent = Model + Harness. The model contains intelligence; the harness makes it useful.
- Harness includes: system prompts, tools/skills/MCPs, bundled infrastructure (filesystem, sandbox), orchestration logic, hooks/middleware
- A raw model cannot out-of-the-box: maintain durable state, execute code, access realtime knowledge, setup environments

## Core Harness Components

1. **Filesystems for Durable Storage** — Most foundational primitive. Enables incremental work, state persistence, natural collaboration surface
2. **Bash + Code as General Purpose Tool** — Enables autonomous problem-solving via ReAct loops
3. **Tools & Skills** — MCPs, custom tools, encoded engineering taste
4. **Orchestration Logic** — Subagent spawning, handoffs, model routing
5. **Feedback Loops** — Agent self-review → agent-to-agent review → human checkpoint
6. **Recovery Mechanisms** — Garbage collection, quality grading, refactoring PRs

## Key Quotes

> "If you're not the model, you're the harness."

> "Harness engineering helps humans inject useful priors to guide agent behavior. And as models have gotten more capable, harnesses have been used to surgically extend and correct models to complete previously impossible tasks."

## Related to Wiki

- [[harness-engineering]] — Ryan Lopopolo's broader thesis
- [[context-engineering]] — Previous paradigm layer
- [[openai-symphony]] — Symphony orchestrates many coding agents via harness
