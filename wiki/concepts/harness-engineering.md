---
title: "Harness Engineering"
created: 2026-04-30
updated: 2026-04-30
tags:
  - concept
  - ai-evals
  - data-science
  - llm-engineering
  - evaluation
aliases:
  - harness
  - evals-harness
  - evaluation-harness
related:
  - [[concepts/ai-evals]]
  - [[concepts/critique-shadowing]]
  - [[concepts/llm-as-judge]]
  - [[concepts/ai-observability]]
  - [[entities/hamel-husain]]
  - [[entities/shreya-shankar]]
  - [[concepts/ai-evals-people]]
sources:
  - raw/articles/2024-03-26_hamel-revenge-data-scientist.md
---

# Harness Engineering

**Harness Engineering** is the practice of building systems that constrain, guide, and evaluate LLMs to ensure reliability in production. The term describes the full stack of tests, specifications, observability tools, and evaluation pipelines that surround an LLM—the "harness" within which a stochastic model can produce dependable outputs.

The concept was popularized by [[entities/hamel-husain|Hamel Husain]], who argues that **60-80% of development time** on LLM-powered products should be spent on the harness (error analysis, evaluation, debugging), not on model selection or prompt engineering.

## Summary

Harness Engineering reframes the work of building reliable AI systems from "find a better model" to "build a better testing and evaluation framework." It asserts that foundation models are already capable enough; the bottleneck is the quality of the systems that constrain and verify their outputs. This work is fundamentally a **data science** practice—requiring exploratory data analysis, experimental design, metric design, and error classification—not just software engineering.

## Key Ideas

### The Harness as Data Science

In his 2024 essay "The Revenge of the Data Scientist," Husain argues that the harness is largely a data science problem:

| Modern LLM Task | Classic Data Science Equivalent |
| :--- | :--- |
| Reading traces, categorizing failures | **Exploratory Data Analysis (EDA)** |
| Validating an LLM judge | **Model Evaluation** |
| Building test sets from logs | **Experimental Design** |
| Expert labeling | **Data Collection** |
| Monitoring production performance | **Production ML** |

This view positions the data scientist—not the ML engineer—as the central figure in building production-ready LLM systems.

### The Five Eval Pitfalls (Husain, 2024)

Husain identifies five common mistakes in LLM evaluation, each rooted in a failure to apply data science fundamentals:

1. **Generic Metrics** — Using off-the-shelf scores (helpfulness, coherence) that cannot diagnose specific application failures.
2. **Unverified Judges** — Deploying an LLM-as-judge without measuring precision/recall against human-labeled data.
3. **Bad Experimental Design** — Generating synthetic test sets by prompting an LLM for "50 queries" instead of grounding data in production logs.
4. **Bad Data and Labels** — Outsourcing labeling instead of having domain experts define criteria iteratively (responding to *criteria drift*).
5. **Automating Too Much** — Trying to automate the data inspection step itself, which requires human judgment for business-specific quality.

### Binary Over Likert

A core Harness Engineering principle: replace subjective 1-5 Likert scales with **binary pass/fail** criteria tied to business outcomes. This enables:
- Clearer error classification
- More reliable inter-labeler agreement
- Direct traceability to product requirements

### Vibe-Based Engineering

The opposite of Harness Engineering—building on "vibes" by using off-the-shelf metrics without examining raw data. Husain characterizes this as the dominant mode of AI development circa 2024, and the primary problem Harness Engineering aims to solve.

## Terminology

- **Harness**: The full stack of tests, evaluation pipelines, observability, and constraints surrounding an LLM.
- **Criteria Drift**: The phenomenon where stakeholders don't know what they want until they see the LLM's output—the act of labeling helps define requirements.
- **Vibe-based Engineering**: Building AI features using generic metrics without data-driven verification.
- **Error Analysis**: The process of reading LLM traces and categorizing failure modes—the highest-ROI activity in Harness Engineering.

## Examples & Applications

### Real-World Impact

The Harness Engineering philosophy is embedded in major production evaluation tools:
- **evals-skills** (Husain's OSS plugin): Automates `eval-audit`, `error-analysis`, `generate-synthetic-data`, `write-judge-prompt` for AI coding agents.
- **Inspect AI** (UK AISI): Evaluation framework that operationalizes harness concepts.
- **LangSmith / Braintrust**: Commercial eval platforms that provide harness infrastructure.
- **OpenAI Evals**: Open-source framework for standardized LLM evaluation.

### The 60-80% Rule

Husain's estimate that the majority of LLM development time should be spent on evaluation and error analysis, not on model selection or prompt tuning, is a central tenet of Harness Engineering. It reframes resource allocation: the scarce resource is not model capability but harness quality.

## Graph Structure Query

```
[harness-engineering] ──popularized-by──→ [entity: hamel-husain]
[harness-engineering] ──contrasts──→ [concept: vibe-based-engineering]
[harness-engineering] ──extends──→ [concept: ai-evals]
[harness-engineering] ──embodies──→ [concept: data-science-fundamentals]
[harness-engineering] ──relates-to──→ [concept: ai-observability]
[harness-engineering] ──relates-to──→ [concept: llm-as-judge]
[harness-engineering] ──teaches──→ [concept: critique-shadowing]
[harness-engineering] ──coauthor──→ [entity: shreya-shankar]
```

This concept was popularized by [[entities/hamel-husain|Hamel Husain]], contrasts with vibe-based engineering, extends the broader [[concepts/ai-evals]] framework, and is taught through methods like [[concepts/critique-shadowing]].



## The Harness > Model Principle (2026 Consensus)

By April 2026, production agent teams have converged on a clear hierarchy: **the harness is doing more work than the model in any production agent worth its compute bill.**

- The model picks the next action
- The harness validates it, runs it in a sandbox, captures the output, decides what to feed back, decides when to stop, decides when to checkpoint, decides when to spawn a subagent
- Swap the model for a different one of similar quality and a good harness still ships
- Swap the harness for a worse one and the best model in the world still produces an agent that randomly forgets what it was doing

This is operationalized through the **file-system-as-state** pattern: think → act → observe → repeat. The model is stateless; the harness must be stateful. Every action is logged and replayable. Claude Code, Cursor, Devin, Aider, OpenHands, and goose have all converged on this architecture.

Key implication for resource allocation: if you're building anything more elaborate than a single-shot tool call, **the harness is where you should be spending your time. The model is a component inside it.**

## Harness Components in Production (2026 Stack)

| Component | Production Default | Purpose |
|-----------|-------------------|---------|
| Orchestration | LangGraph | Typed state, conditional edges, durable workflows |
| Protocol | MCP | Clean separation of capabilities/tools/resources |
| Tracing | Langfuse / LangSmith | "What did the agent actually do?" |
| Evals | Langfuse evals / Braintrust | "Is the agent better or worse than yesterday?" |
| Sandbox | E2B / Browserbase / Modal | Blast radius containment |
| State | File system / Postgres | Think-act-observe loop persistence |

**Source**: 2026 Agent Engineering Guide (published April 2026), Claude Code engineering team postmortems.

## Related Concepts

- [[concepts/agentic-engineering]] — The practice of engineering with AI coding agents, tightly coupled to harness engineering.
- [[concepts/ai-evals]] — The broader evaluation framework that harness engineering operationalizes.
- [[concepts/critique-shadowing]] — Husain's methodology for building aligned LLM judges.
- [[concepts/llm-as-judge]] — Core technique that requires harness validation.
- [[concepts/ai-evals-people]] — The community of practitioners (Husain, Shreya Shankar, drmaciver) advancing eval methodology.
- [[entities/hamel-husain]] — Primary proponent and popularizer.
- [[entities/shreya-shankar]] — Co-creator of AI evals course, major contributor to the movement.

## References

- Husain, H. (2024). ["The Revenge of the Data Scientist"](https://hamel.dev/blog/posts/revenge/) — Foundational essay arguing the harness is data science.
- Husain, H. (2024). ["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/) — Practical guide to building evaluation systems.
- Husain, H. et al. (2024). ["What We've Learned From a Year of Building with LLMs"](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/) — Industry reference outlining harness practices.
