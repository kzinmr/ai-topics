---
title: "DSPy — Declarative Self-improving Python for LMs"
tags: [training, concept, ai-agents, llm, prompting, rag, evaluations]
created: 2026-04-24
updated: 2026-04-29
type: concept
sources:
  - raw/articles/crawl-2026-04-29-dspy-adoption-gap-khattabs-law.md
---

# DSPy: Declarative Self-improving Language Systems

**DSPy** (Declarative Self-improving Python for LMs, "dee-spai") is a **declarative LM programming framework** developed by Stanford NLP Group (Omar Khattab, Arnav Singhvi et al.). It replaces manual prompt engineering with a compilable, optimizable program specification.

## Core Philosophy: Prompting is Not Programming

> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."* — Omar Khattab (2024)

**Traditional approach (prompt engineering):**
1. Break problem into steps
2. Write prompts by trial and error for each step
3. Rewrite prompts when model changes
4. Pipeline quality depends directly on prompt quality

**DSPy approach (declarative programming):**
1. Declare input/output contracts via **Signature**
2. Compose inference patterns via **Module**
3. Define success criteria via **Metric**
4. Optimize automatically via **Teleprompter**

This mirrors the shift PyTorch brought to deep learning — from manual weight tuning (NumPy) to declarative module composition with automatic optimization (backprop → Teleprompter).

## Architecture Overview

DSPy's architecture is built on three abstractions:

- **[[concepts/dspy-architecture|Signatures]]** — Declarative input/output contracts (model-independent)
- **[[concepts/dspy-architecture|Modules]]** — Composable inference patterns (e.g., ChainOfThought, ReAct)
- **[[concepts/dspy-architecture|Teleprompters]]** — Automatic optimization engine (compile-time)

See [[concepts/dspy-architecture]] for the full architectural deep-dive.

## Modules and Pipeline Patterns

DSPy provides a rich set of composable modules (`dspy.Predict`, `dspy.ChainOfThought`, `dspy.ReAct`, `dspy.ProgramOfThought`, `dspy.MultiChainComparison`) and supports patterns like RAG, multi-hop search, and multi-agent debate — all **model-independent**.

See [[concepts/dspy-modules]] for the complete module reference and pipeline pattern examples.

## Optimization Techniques

DSPy offers three complementary optimization approaches:

1. **[[concepts/dspy-optimization|Teleprompters]]** — Data-driven prompt optimization (BootstrapFewShot, MIPROv2, COPRO, Ensemble)
2. **[[concepts/dspy-optimization|Assertions]]** — Runtime validation with automatic self-correction loops
3. **Fine-Tuning + Prompt Optimization synergy** — Combined approach yields +23% improvement (synergistic, not additive)

See [[concepts/dspy-optimization]] for detailed coverage.

## Paradigm Comparisons

| Dimension | DSPy | LangChain | RLMs | GEPA |
|-----------|------|-----------|------|------|
| **Philosophy** | Declarative (what) | Imperative (how) | Recursive (self-manage) | Evolutionary |
| **Optimization** | Compile-time | Manual | Inference-time | Generational |
| **Control** | Teleprompter | Developer | LM itself | Algorithm |
| **Best for** | Repetitive pipelines | Broad integrations | Ultra-long context | Deep prompt evolution |

See [[concepts/dspy-comparisons]] for the full comparison tables.

## Design Philosophy Evolution

| Phase | Version | Key Innovation |
|-------|---------|----------------|
| **Phase 1** | DSP (2022) | Manual prompt wrappers, no optimization |
| **Phase 2** | DSPy v1 (2023) | Teleprompters, Signature/Module abstractions (ICLR 2024 Spotlight) |
| **Phase 3** | DSPy v2 (2024) | Assertions, Fine-tuning integration, MIPROv2 |
| **Phase 4** | DSPy v3 (2025+) | GEPA integration, multi-module GRPO, RLM convergence |

### Khattab's Law: The Production Adoption Gap (2026)

Skylar Payne (March 2026) introduced **"Khattab's Law"** — named after DSPy creator Omar Khattab — which holds that *any sufficiently complex AI system eventually reinvents DSPy's core abstractions on its own*: typed I/O signatures, composable modules, prompt versioning, retry logic, and model-swapping shims. Teams do this ad hoc, buggily, and after significant pain, tracing a canonical seven-stage evolution:

1. Raw API call → 2. Add retry logic → 3. Add prompt templates/versioning → 4. Add Pydantic parsing → 5. Add RAG retrieval → 6. Add eval scaffolding → 7. A fragile hand-rolled framework that poorly recreates DSPy

**Production users** include JetBlue, Databricks, Replit, VMware, and Sephora — reporting faster model swaps, more maintainable pipelines, and less plumbing overhead.

**Download gap:** DSPy ~4.7M monthly downloads vs LangChain ~222M, indicating significant adoption friction despite technical merit.

### Adoption Barriers

Despite the argument for DSPy, adoption faces genuine obstacles:

1. **Labeled data requirement:** DSPy's optimization loop requires labeled training/evaluation datasets — a researcher's discipline that many product teams lack
2. **Exploratory friction:** The evaluation-first mental model can impede iteration speed for teams figuring out *what* their LLM system should do
3. **Lighter alternatives:** LiteLLM and Vercel AI SDK handle model abstraction and typed outputs without DSPy's complexity
4. **Academic roots:** Originally designed for benchmarks with ground-truth labels; production systems often don't have that luxury
5. **MIPROv2 underutilized:** DSPy's true differentiator — Bayesian prompt optimization — is rarely used even by adopters, suggesting the framework's main value may be its type-safe pipeline abstractions rather than its optimization engine

DSPy is genuinely valuable for teams with stable, well-defined tasks requiring systematic prompt optimization at scale, but its positioning as a universal antidote to LLM engineering pain is undercut by the labeled data requirement and the availability of lighter-weight alternatives for simpler use cases.

## RLM Bundled in DSPy v3.1.3: Multi-layered Sandboxing

DSPy v3.1.3 bundles RLM (Recursive Language Models) with a notable **multi-layered sandboxing architecture**: `rlm on pyodide on deno`. This creates a defense-in-depth execution model where:

- **Deno** provides the outer runtime with capability-based permissions (filesystem, network access control)
- **Pyodide** (Python compiled to WebAssembly) provides the inner sandbox, with a 128MB memory ceiling — variables exceeding this are passed via JSON-RPC through a virtual filesystem (`inject_var` method)
- **RLM** runs atop this stack, using the sandboxed Python REPL to interact with its own prompt as data

This pattern originates from Simon Willison's [Pyodide sandboxing on Deno](https://til.simonwillison.net/deno/pyodide-sandbox), which demonstrated that combining Deno's permission model with Pyodide's WASM isolation creates a practical sandbox for untrusted LLM-generated code. DSPy's adoption of this architecture signals that **secure code execution is becoming a first-class concern for agentic frameworks**, not an afterthought.

The Pyodide 128MB FFI crash ceiling is a known limitation — large data payloads require JSON-RPC virtual filesystem transfer rather than direct memory sharing. This is an acceptable tradeoff for security, but worth monitoring as RLM usage scales.

## Application Guidelines

**Use DSPy when:**
- Same task is **repeated** in a pipeline
- **Evaluation metrics** are clearly defined
- 10-50+ training examples are available
- Pipeline runs across multiple LLMs
- Prompt maintenance cost is high

**Avoid DSPy when:**
- One-off exploratory queries (no evaluation data)
- Highly **dynamic tasks** (frequent Signature changes)
- **Real-time adaptation** needed (consider RLMs)
- Broad **ecosystem integrations** critical (consider LangChain)

## Key Papers

| Date | Title | Insight |
|------|-------|---------|
| Oct 2023 | DSPy: Compiling Declarative LM Calls (ICLR 2024) | Teleprompter paradigm |
| Dec 2023 | DSPy Assertions | Self-correcting pipelines |
| Jul 2024 | Fine-Tuning and Prompt Optimization | Synergistic combination (+23%) |
| 2025 | GEPA | Genetic prompt evolution |
| 2025 | RLMs | Recursive context processing |

---

## See Also

- [[concepts/dspy-architecture]] — The three core abstractions
- [[concepts/dspy-modules]] — Module reference and pipeline patterns
- [[concepts/dspy-optimization]] — Teleprompters, Assertions, Fine-Tuning
- [[concepts/dspy-comparisons]] — DSPy vs LangChain, RLMs, GEPA
- [[concepts/gepa]] — Genetic prompt optimization
- [[concepts/rlms]] — Recursive Language Models
- [[omar-khattab]] — Creator of DSPy
