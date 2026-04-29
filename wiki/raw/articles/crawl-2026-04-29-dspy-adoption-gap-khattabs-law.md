# If DSPy Is So Great, Why Isn't Anyone Using It? — DSPy's Adoption Gap

**Source:** Agent Wars / Skylar Payne
**URL:** https://agent-wars.com/news/2026-03-24-dspy-adoption-gap-llm-engineering
**Date:** March 24, 2026
**Author:** Skylar Payne
**Type:** AI Engineering Analysis Article

---

## Summary

Skylar Payne argues that every serious AI engineering team eventually reinvents DSPy's core abstractions (typed signatures, composable modules, prompt management, optimizers) through pain — but does it worse. The article introduces **"Khattab's Law"** as a named observation.

## Khattab's Law

Named after DSPy creator Omar Khattab: **Any sufficiently complex AI system eventually reinvents DSPy's core abstractions on its own:** typed I/O signatures, composable modules, prompt versioning, retry logic, and model-swapping shims. Teams do this ad hoc, buggily, and after significant pain.

## The Seven-Stage Evolution

The article traces a canonical evolution of a typical LLM pipeline:

1. Raw OpenAI API call (simple, direct)
2. Add retry logic and error handling
3. Add prompt templates and versioning
4. Add Pydantic parsing for structured output
5. Add RAG retrieval context
6. Add eval scaffolding
7. Result: A fragile, hand-rolled framework that recreates DSPy poorly

## Production Users

Companies cited as production DSPy users: JetBlue, Databricks, Replit, VMware, Sephora — reporting faster model swaps, more maintainable pipelines, less plumbing work.

## The Download Gap

- DSPy: ~4.7M monthly downloads
- LangChain: ~222M monthly downloads
- The gap suggests PR/adoption friction despite technical merit

## Criticism and Counterarguments

Hacker News commenters raised several valid points:

1. **Lighter alternatives:** LiteLLM and Vercel AI SDK handle model abstraction and typed outputs just as cleanly
2. **MIPROv2 under-discussed:** DSPy's actual differentiator — Bayesian prompt optimization — was barely covered in the article
3. **Evaluation-first requirement:** DSPy needs labeled training/evaluation data before optimization works — a researcher's discipline many product teams aren't ready for
4. **Academic origins:** DSPy was designed for benchmarks with ground-truth labels; production systems often don't have that luxury

## Key Insight on Adoption Barrier

DSPy's architecture enforces an **evaluation-first mental model** that can actively impede iteration speed for teams in exploratory phases. The framework is genuinely valuable for teams with stable, well-defined tasks who need systematic prompt optimization at scale, but its positioning as a general antidote to LLM engineering pain is undercut by its steep learning curve and labeled data requirements.
