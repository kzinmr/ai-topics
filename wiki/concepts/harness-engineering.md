---
title: "Harness Engineering"
created: 2026-04-30
updated: 2026-05-10
tags:
  - concept
  - evaluation
  - data-science
  - model
  - langchain
  - coding-agents
  - middleware
aliases:
  - harness
  - evals-harness
  - evaluation-harness
  - better-harness
  - agent-harness-engineering
related:
  - "concepts/ai-evals]]"
  - "concepts/critique-shadowing]]"
  - "concepts/llm-as-judge]]"
  - "concepts/ai-observability]]"
  - "entities/hamel-husain]]"
  - "entities/shreya-shankar]]"
  - "entities/vtrivedy10]]"
  - "entities/addy-osmani]]"
  - "concepts/ai-evals-people]]"
sources:
  - raw/articles/2024-03-26_hamel-revenge-data-scientist.md
  - raw/articles/2026-02-17_langchain-improving-deep-agents-harness-engineering.md
  - raw/articles/2026-04-08_langchain-better-harness-hill-climbing-evals.md
  - raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md
  - raw/articles/2026-05-09_addyosmani-agent-harness-engineering.md
  - https://x.com/vtrivedy10/status/2052100726608781363
  - https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
  - https://blog.langchain.com/better-harness-a-recipe-for-harness-hill-climbing-with-evals/
description: "The practice of building evaluation and constraint systems around LLMs for production reliability. Includes production case studies from LangChain, Addy Osmani's Agent = Model + Harness framework, and the Agent Harness Engineering discipline."
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

## LangChain Harness Engineering Case Studies

LangChain published two case studies in early 2026 demonstrating harness engineering in production coding agents, showing how systematic harness improvements can achieve dramatic performance gains without touching the underlying model.

### Improving Deep Agents (+13.7pts on Terminal Bench 2.0)

In February 2026, LangChain published ["Improving Deep Agents with Harness Engineering"](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering), describing how they improved a deep coding agent by **+13.7 points** on Terminal Bench 2.0 — modifying only the harness, not the model.

**Key techniques used:**

| Technique | Description | Impact |
|-----------|-------------|--------|
| **Build-Verify Loop** | Agent writes code → harness runs it → harness feeds compiler/test output back to agent in a tight loop. The agent sees failures immediately rather than discovering them later. | Eliminates "blind coding" where the agent writes a full file without ever running it |
| **Context Engineering** | Harness curates what the model sees at each step: prunes stale observations, prioritizes recent errors, injects file structure context. The model always works with a focused, relevant context window. | Prevents context pollution and keeps the agent on task |
| **Loop Detection** | Harness monitors for repeated actions (e.g., the same failing edit applied 3+ times) and intervenes — either by injecting a "you're stuck" prompt or by forcing a different approach. | Breaks agent fixation loops that waste tokens and time |
| **Reasoning Sandwich** | Before each action: "Here's what we know and what we need." After each action: "Here's what happened and what it means." The harness wraps every model call with structured reasoning prompts that frame the next step. | Improves action quality by forcing explicit state awareness |

**Results:**
- **+13.7 points** on Terminal Bench 2.0 over the baseline agent
- All gains came from harness changes — the underlying model was unchanged
- The harness became the primary differentiator between a mediocre agent and a competitive one
- Error analysis revealed that most failures were harness failures (context mismanagement, missing feedback loops), not model capability failures

**Practical takeaway:** Before reaching for a better model, examine whether your harness is feeding the agent the right information at the right time. The Build-Verify Loop alone often accounts for half the gains.

### Better Harness: Eval-Driven Hill-Climbing

In April 2026, LangChain followed up with ["Better Harness: A Recipe for Harness Hill-Climbing with Evals"](https://blog.langchain.com/better-harness-a-recipe-for-harness-hill-climbing-with-evals/), making the case that **evals are the training data for autonomous harness optimization**.

The core insight: once you have reliable, task-specific evals, you can treat harness parameters (context window size, tool selection strategy, stop conditions, error recovery policies) as hyperparameters and optimize them through systematic experimentation — a process they call **harness hill-climbing**.

**The recipe:**

| Step | Description |
|------|-------------|
| 1. **Define task-specific evals** | Binary pass/fail criteria tied to real user outcomes. No generic "helpfulness" scores. |
| 2. **Create a holdout set** | Reserve 20-30% of eval cases that the optimizer never sees during tuning. Prevents overfitting to the eval set. |
| 3. **Parameterize the harness** | Expose harness behaviors as tunable parameters: retry counts, tool selection policies, context pruning strategies, stop conditions. |
| 4. **Run hill-climbing experiments** | Systematically vary one harness parameter at a time, measure eval performance, accept improvements. Use the holdout set only for final validation. |
| 5. **Human review gates** | Before shipping a harness change, a human reviews a sample of holdout-set traces to catch subtle regressions that evals miss. |

**Results reported:**
- Harness hill-climbing produced consistent incremental gains (1-3 points per cycle) that compounded over multiple cycles
- The holdout set caught 3 cases of eval overfitting where training-set performance improved but holdout performance regressed
- Human review identified 2 subtle regressions (the agent was "passing" evals via technically correct but unhelpful strategies)
- Teams that adopted formal harness hill-climbing processes shipped agent improvements 2-3x more frequently than teams relying on ad-hoc prompt changes

**Practical takeaway:** Treat your harness as a learned system, not a fixed scaffold. Evals provide the signal; hill-climbing provides the optimization process; holdout sets and human review provide the safety rails. This is [[entities/vtrivedy10|Vivek Trivedy]]'s recommended approach for teams that have graduated from ad-hoc prompt engineering to systematic agent development.

## The "Token Burn" Crisis (May 2026)

As agentic workloads shift from single-turn to multi-step autonomous agents, flat-rate pricing models are breaking:

- **Theo's Experiment (May 2026)**: A single Copilot message chain consumed **60M+ tokens**, estimated at **$221 in inference costs** against a standard $40 subscription
- **Cost Implications**: This means every deep agent session is a money-losing proposition for flat-rate services
- **Harness as cost-control**: The harness must manage not just correctness but token budget — deciding when to compact, when to stop, and when to spawn cheaper sub-models

This creates a structural tension: better harnesses → more autonomous agents → higher token consumption → unsustainable unit economics. The resolution likely involves tiered pricing, harness-level token budgets, and model-switching strategies.

## Context Pipelines as Competitive Moats (May 2026)

From swyx's AINews analysis (May 2026), the "product boundary" is shifting from model weights to the harness middleware:

- **Repo state curation**: How repo state is fetched, ranked, and compressed for the agent
- **Measurable impact**: Tuning prompts and middleware moved **gpt-5.2-codex from 52.8% to 66.5%** on Terminal-Bench 2.0
- **Open harness ecosystem momentum**: Hermes Agent Kanban (visual multi-agent coordination), deepagents, Flue-style systems
- **Cost efficiency**: Teams achieving **>20x cheaper agents** by tuning open models inside high-quality harnesses rather than using frontier APIs
- **LangGraph improvements**: Model-specific harness configs, schema migrations, node-level error handlers

## Addy Osmani's Agent Harness Engineering Framework (May 2026)

On May 9, 2026, [[entities/addy-osmani|Addy Osmani]] published a comprehensive synthesis of the agent harness engineering movement, framing coding agents as **Model + Harness** and codifying the disciplines that differentiate production harnesses from ad-hoc scaffolding.

### The Ratchet: Every Mistake Becomes a Rule

The core operational pattern: treat every agent mistake as a permanent signal, not a one-off fluke. When an agent ships a commented-out test, the response is not "retry and hope" but a systematic chain:

1. **Update AGENTS.md** — "Never comment out tests; delete or fix them."
2. **Add a pre-commit hook** — Automatically flag `.skip(` in the diff.
3. **Update the reviewer subagent** — Block commented-out tests at review time.

**Constraints should only be added when you observe a real failure, and removed only when a capable model renders them redundant.** Every line in a good system prompt should trace back to a specific, historical failure. This makes harness engineering inherently codebase-specific — the right harness is entirely shaped by its unique failure history.

### Working Backwards from Behavior

The design methodology: start with the desired behavior and build the component that delivers it. Each harness component must have a distinct, nameable job:

| Component | Function |
|-----------|----------|
| **Filesystem + Git** | Durable state, versioning, coordination surface |
| **Bash + Code Execution** | General-purpose tooling via ReAct loop |
| **Sandboxes** | Isolated runtime with pre-installed defaults |
| **Memory + Search** | Continual learning (AGENTS.md, web search, MCP) |
| **Context Management** | Compaction, tool-call offloading, progressive disclosure |
| **Hooks** | Enforcement layer — silent success, verbose failure |
| **Rulebook** | Flat markdown file as pilot's checklist, earned through past failures |

### Battling Context Rot

Three primary techniques for managing context window scarcity:

- **Compaction** — Intelligently summarizing and offloading older context.
- **Tool-call offloading** — Storing massive outputs in the filesystem, keeping only headers/footers in context.
- **Progressive disclosure** — Revealing instructions and tools only when a task requires them.

### Long-Horizon Execution Patterns

Autonomous work patterns that prevent early stopping and poor decomposition:

- **Loops** — Intercepting model exit attempts, forcing continuation against a completion goal in a fresh context window.
- **Planning** — Decomposing goals into step-by-step plans with self-verification hooks.
- **Splits** — Separating generation and evaluation into distinct agents to avoid self-grading bias.

### Harnesses Don't Shrink, They Move

A key systems insight: as models improve, the need for harnesses does not disappear — it shifts. Better models make old scaffolding redundant but unlock new, harder tasks with entirely new failure modes. Every harness component encodes an assumption about what the model cannot do alone. When the model improves, outdated scaffolding is removed, and new scaffolding is built for the next horizon.

There is also an active feedback loop: today's models are post-trained with specific harnesses in the loop, creating a degree of **overfitting** — the model gets exceptionally good at the specific harness actions its designers prioritized.

### Claude Code Architecture (Fareed Khan)

The clearest public picture of a mature production harness: almost every concept maps to a named component — context injection as the knowledge layer, loop state in the memory store, destructive-action hooks behind the permission gate, subagent context firewalls as the multi-agent layer, and MCP servers + bash plugged into the tool dispatch registry. Claude Code's trajectory is about the harness at least as much as the model beneath it.

### Industry Convergence

The top coding agents today look more like each other than their underlying models do. Harness patterns are converging across platforms. The open frontier: orchestrating multiple agents in parallel, enabling agents to analyze their own traces, and building environments that dynamically assemble tools just-in-time.

**Sources**: Addy Osmani's X Article (May 9, 2026), Fareed Khan's Claude Code architecture breakdown, HumanLayer "skill issue" framing, Anthropic Engineering long-running app guides, Birgitta Böckeler on user-side experience.

## Viv Trivedy's "Strong Opinions, Loosely Held" (May 2026)

On May 6, 2026, [[entities/vtrivedy10|Viv Trivedy]] published an 8-point manifesto on agent + harness engineering that synthesized and extended the field's consensus:

| # | Point | Significance for Harness Engineering |
|---|-------|-------------------------------------|
| 1 | **Harness > Model** | Formalizes the LangChain finding: harness optimization (prompts, tools, skills, hooks) outperforms model swapping. Optimization is becoming agent-driven. |
| 2-3 | **No general purpose agent** | Challenges the notion of a universal agent; what exists is a tradeoff between customization and performance |
| 4 | **Convergence on Skills** | Harness optimization packages into Skills as models improve at in-context learning — reducing harness complexity over time |
| 5 | **Evals as a moat** | Extends the [[concepts/ai-evals]] framework with a business moat thesis: data to produce evals is a competitive advantage |
| 6 | **Open model cost advantage** | 20x+ cost reduction from open models drives harness engineering investment — aligning with the Context Pipelines finding above |
| 7 | **Context window drives architecture** | Most task decomposition exists because usable context is 50-100k — directly ties [[concepts/context-engineering]] to architectural decisions |
| 8 | **Age of Unbundled Agents** | Subagents as Tools within a harness — see [[concepts/unbundled-agents]] |

**Key takeaway**: Viv's manifesto provides a unified framework connecting harness hill-climbing (Point 1), evals as moat (Point 5), and open model cost dynamics (Point 6) — all pointing to harness engineering as the primary differentiator in production AI.

## Sierra: Harness-as-a-Service at Scale

[[entities/sierra|Sierra]], the AI customer service platform, demonstrates harness engineering at enterprise scale:

| Metric | Value | Date |
|--------|-------|------|
| Valuation | $15B | May 2026 |
| ARR | $100M → $200M+ | Nov 2025 → May 2026 |
| Revenue multiple | 50-75x | May 2026 |

Sierra's value proposition is fundamentally harness engineering: deploying conversational AI agents that integrate with enterprise systems, handle end-to-end customer service, and deliver measurable business outcomes. The company represents the "Service-as-Software" thesis where the harness — not the model — is the product.

## Infrastructure: Zyphra TSP and DORA (May 2026)

Training and inference infrastructure advances enabling better harnesses:
- **Zyphra TSP**: Folded Tensor + Sequence Parallelism hitting **173M tok/sec** on 1024 MI300X GPUs (vs 86M for standard approaches)
- **DORA**: Asynchronous RL system with **8.2x rollout speedup** and 2.12x end-to-end throughput improvement

## Related Concepts

- [[concepts/agentic-engineering]] — The practice of engineering with AI coding agents, tightly coupled to harness engineering.
- [[concepts/ai-evals]] — The broader evaluation framework that harness engineering operationalizes.
- [[concepts/critique-shadowing]] — Husain's methodology for building aligned LLM judges.
- [[concepts/llm-as-judge]] — Core technique that requires harness validation.
- [[concepts/ai-evals-people]] — The community of practitioners
- [[concepts/context-engineering]] — The practice of optimizing context windows for LLM agents, a cross-cutting component of harness engineering.
- [[concepts/unbundled-agents]] — Viv Trivedy's pattern of specialist subagents as Tools within a harness.
- [[concepts/karpathy]] — Andrej Karpathy, AI researcher and educator who coined context engineering and vibe coding.
- [[concepts/rlm-recursive-language-models]] — Recursive decomposition as a harness pattern; RLM's programmatic context management aligns with harness engineering's build-verify loop.
- [[entities/hamel-husain]] — Primary proponent and popularizer.
- [[entities/shreya-shankar]] — Co-creator of AI evals course, major contributor to the movement.
- [[entities/vtrivedy10]] — LangChain contributor; advocates eval-driven harness hill-climbing for production agents.
- [[entities/sierra]] — Enterprise harness-as-a-service at $15B valuation
- [[concepts/service-as-software]] — Business model thesis behind Sierra

## References

- Husain, H. (2024). ["The Revenge of the Data Scientist"](https://hamel.dev/blog/posts/revenge/) — Foundational essay arguing the harness is data science.
- Husain, H. (2024). ["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/) — Practical guide to building evaluation systems.
- Husain, H. et al. (2024). ["What We've Learned From a Year of Building with LLMs"](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/) — Industry reference outlining harness practices.
