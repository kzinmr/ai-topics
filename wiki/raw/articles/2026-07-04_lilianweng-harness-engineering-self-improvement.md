---
title: "Harness Engineering for Self-Improvement"
author: Lilian Weng
date: 2026-07-04
source_url: https://lilianweng.github.io/posts/2026-07-04-harness/
blog: Lil'Log
tags: [harness-engineering, recursive-self-improvement, evolutionary-algorithms, context-engineering, auto-research, coding-agents]
---

# Harness Engineering for Self-Improvement

**Author**: Lilian Weng
**Published**: July 4, 2026
**URL**: https://lilianweng.github.io/posts/2026-07-04-harness/

## Abstract

This post focuses on research around harness engineering and how it contributes to recursive self-improvement (RSI). A **harness** is the system surrounding a base model that orchestrates execution and decides how the model thinks and plans, calls tools and acts, perceives and manages context, stores artifacts, and evaluates results. The post organizes recent work on auto-research, self-improving agents, and evolutionary program search around the question of how harness engineering enables RSI.

## Key Sections

### Harness Design Patterns

Three core patterns identified:

1. **Workflow Automation** — Goal-oriented loops (plan → execute → observe/test → improve → repeat). Example: Karpathy's autoresearch repo, OpenAI Codex agent loop.

2. **File System as Persistent Memory** — Durable state in files rather than context window. Artifacts (experiment logs, code diffs, error traces) grow beyond context limits. File read/write/edit via bash is a foundation skill.

3. **Sub-agent and Backend Jobs** — Parallel subagent execution for hypothesis search, concurrent experiments. Key: make parallelism explicit and inspectable via files/logs/status records.

### Harness Layer vs Core Intelligence

Near-term RSI path prediction:
1. Harness engineering evolves toward meta-methodology (improving machinery for getting better answers)
2. Mature harnesses enable auto-research for model self-improvement; smarter models prevent harness overengineering

Many harness improvements will eventually be internalized into core model behavior, but external context/tool interface remains. Analogous to prompt engineering becoming less central with instruction tuning, but goal/constraint specification never disappeared.

### Harness Optimization Progression

Optimization targets evolve: instruction prompts → structured context → workflow → harness code → optimizer code.

### Context Engineering

- **ACE (Agentic Context Engineering)** — Zhang et al. 2025. Context as evolving playbook of structured bullets (identifier, description). Generator/Reflector/Curator loop. Deterministic merge prevents context collapse.

- **MCE (Meta Context Engineering)** — Ye et al. 2026. Bi-level optimization: meta-level skill evolution + base-level context optimization. Skills defined as context functions with static/dynamic components. Free-form skills stored as files (skill.md + data rollouts).

- **Meta-Harness** — Lee et al. 2026. Optimizes the code that determines what information is stored/retrieved/presented. Proposer is a coding agent; output is Pareto frontier of harness candidates. File system for execution history access.

### Workflow Design (Auto-Research)

- **AI Scientist** — Lu et al. 2026 (Nature). Pipeline: propose ideas → write code → run experiments → analyze → write manuscript → peer review.
- **ScientistOne** — Meng et al. 2026. Chain-of-Evidence checks for verifiability.
- **Autodata** — Kulikov et al. 2026. Challenger/weak solver/strong solver/verifier roles for synthetic data at "just right" difficulty.
- **ADAS (Automated Design of Agentic Systems)** — Hu et al. 2025. Meta-agent search over agentic workflow code.
- **AFlow** — Zhang et al. 2025. MCTS-based workflow optimization over graph representations.

### Self-Improving Harness

- **STOP (Self-Taught Optimizer)** — Zelikman et al. 2023. Recursive scaffolding improvement: improve the improver, not the solution. Discovered strategies: genetic algorithms, simulated annealing, beam search. Caution: only works with capable base models (GPT-4 yes, GPT-3.5/Mixtral no).

- **Self-Harness** — Zhang et al. 2026. Propose-evaluate-accept loop: weakness mining → harness proposal → validation. Model-specific harness instructions targeting different base model weaknesses. Concern: editable surface needs proper permission control.

### Evolutionary Search

- **Promptbreeder** — Fernando et al. 2023. Evolution of task prompts and mutation prompts.
- **GEPA** — Agrawal et al. 2025. Reflection-based prompt evolution.
- **AlphaEvolve** — Novikov et al. 2025. Coding-agent evolutionary search with EVOLVE-BLOCK markers. Meta-prompt co-evolution.
- **ThetaEvolve** — Wang et al. 2025. Evolutionary search + RL + ICL.
- **ShinkaEvolve** — Lange et al. 2025. Sample-efficient exploration, code-novelty rejection, meta-scratchpad.
- **Darwin Gödel Machine** — Zhang et al. 2025. LLM-based coding agent modifies its own harness code. DGM-discovered agents comparable to/outperform handcrafted agents on SWE-bench (20%→50%) and Polyglot (14.2%→30.7%).
- **Hyperagents** — Zhang et al. 2026. Meta-agent controls how to modify task agents.

### Joint Optimization with Model Weights

- **SIA (Self Improving AI)** — Hebbar et al. 2026. Meta-Agent proposes harness, Task-Specific Agent executes, Feedback-Agent chooses harness vs weight updates. Direction interesting but evidence provisional.

### Future Challenges

1. Weak and fuzzy evaluators — many tasks lack fast/precise verifiers
2. Context and memory lifecycle — context engineering as core part of intelligence
3. Negative results — literature biased toward successes; LLMs may be bad at abandoning hypotheses
4. Diversity collapse — evolutionary/RL loops exploit known patterns
5. Reward hacking — self-improvement optimizes whatever signal is given
6. Long-term success — coding agents optimize short-term; maintainability/repo health neglected
7. Role of humans — provide oversight at right time/abstraction level

### Benchmarks Mentioned

- PaperBench (ICML 2024 paper replication)
- CORE-Bench (computational reproducibility)
- ScienceAgentBench (data-driven scientific discovery)
- RE-Bench (ML research-engineering vs human experts)
- MLE-bench (Kaggle competitions)
- KernelBench (GPU kernel generation)
- TerminalBench-2 (coding agent benchmark)

## References

35 references including Good (1965), Yudkowsky (2008), and papers from 2023-2026 on ACE, MCE, Meta-Harness, AI Scientist, ADAS, AFlow, STOP, Self-Harness, Promptbreeder, AlphaEvolve, Darwin Gödel Machine, SIA, and more.
