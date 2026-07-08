---
title: "Recursive Self-Improvement (RSI)"
created: 2026-07-07
updated: 2026-07-07
type: concept
tags:
  - concept
  - recursive-self-improvement
  - self-improving
  - harness-engineering
  - evolutionary-algorithms
  - context-engineering
  - autoresearch
  - coding-agents
  - agent-architecture
  - meta-harness
  - alignment
  - ai-safety
sources:
  - raw/articles/2026-07-04_lilianweng-harness-engineering-self-improvement.md
  - https://lilianweng.github.io/posts/2026-07-04-harness/
description: "The feedback loop where an AI improves the machinery that produces its intelligence. Near-term RSI runs through harness engineering — optimizing context, workflow, and code — rather than direct weight rewriting."
---

# Recursive Self-Improvement (RSI)

**Recursive self-improvement (RSI)** is the feedback loop where an AI system improves the cognitive machinery that produces its intelligence. The concept dates back to I.J. Good (1965), who defined an "ultraintelligent machine" as a system that can surpass humans in all intellectual activities and design better machines to improve itself. Yudkowsky (2008) formalized the phrase for a specific feedback loop: an AI uses its current intelligence to improve the cognitive machinery that produces its intelligence.

In modern AI, this may manifest as:
- **Direct**: the model rewriting its own weights
- **Indirect (near-term)**: the model improves the **training pipeline** and the **deployment system** (harness), enabling a better successor model

## The Harness Path to RSI

The near-term path to RSI is unlikely to start as a model directly rewriting its weights. Instead, RSI progresses through [[concepts/harness-engineering|harness engineering]] — the system surrounding a base model that orchestrates execution, tool use, context management, and evaluation.

> A **harness** is the system surrounding a base model that orchestrates execution and decides how the model thinks and plans, calls tools and acts, perceives and manages context, stores artifacts, and evaluates results.
>
> — [[entities/lilian-weng|Lilian Weng]], "Harness Engineering for Self-Improvement" (July 2026)

### Harness Design Patterns for RSI

Three core patterns enable agents to improve themselves:

| Pattern | Description | RSI Implication |
|---------|-------------|-----------------|
| **Workflow Automation** | Goal-oriented loops (plan → execute → observe → improve → repeat) | Model analyzes its own trajectories and failure cases, iterating on progress |
| **File System as Persistent Memory** | Durable state in files, not context window | Artifacts (logs, diffs, error traces) persist beyond context limits; file ops benefit from model capability improvements |
| **Sub-agent & Backend Jobs** | Parallel subagent execution with inspectable outputs | Hypothesis search, concurrent experiments; outputs as files enable recovery and reasoning over execution history |

### Harness Optimization Progression

The optimization target evolves as models become more capable:

**instruction prompts → structured context → workflow → harness code → optimizer code**

Key systems along this progression:

- **ACE (Agentic Context Engineering)** — Zhang et al. 2025. Context as an evolving playbook of structured bullets (identifier, description). Generator/Reflector/Curator loop. Deterministic merge prevents context collapse during iterative rewrites.
- **MCE (Meta Context Engineering)** — Ye et al. 2026. Bi-level optimization: meta-level skill evolution searches over context-management mechanisms, base-level optimizes task context. Skills defined as context functions with static (prompts, knowledge) and dynamic (search, filtering) components. Implemented as files in a directory (skill.md + data rollouts).
- **Meta-Harness** — Lee et al. 2026. Optimizes the *code* that determines what information is stored/retrieved/presented to the model. The proposer is itself a coding agent; output is a collection of harness candidates on the Pareto frontier. Execution history accessed via file system (`grep`, `cat`) rather than prompt context.

## Self-Improving Harnesses

Systems that improve their own harness code:

### STOP (Self-Taught Optimizer)
Zelikman et al. 2023. A seed improver takes a solution, utility function, and LLM, and returns an improved solution. STOP's goal is not to improve the solution but **to improve the improver itself** via recursive meta-utility optimization.

Discovered strategies: genetic algorithms, decomposing and improving parts, multi-armed prompt bandits, simulated annealing, varying temperature, beam/tree search.

> ⚠️ **Caution**: STOP improved mean downstream performance with GPT-4 but *degraded* with weaker models (GPT-3.5, Mixtral). Recursive structure alone is not enough — the base model must be capable enough to improve the mechanism.

### Self-Harness
Zhang et al. 2026. A propose-evaluate-accept loop with three stages:

1. **Weakness mining** — Cluster failures into verifier-grounded failure patterns. Rich failure records (terminal cause, causal status of agent behavior, abstract mechanism) uncover root causes.
2. **Harness proposal** — Bounded edits based on mined patterns. Prefer recurrent, addressable errors resolvable by narrow changes. Candidates should be distinct and diverse.
3. **Proposal validation** — Regression tests on held-in (weakness resolved?) and held-out (no new issues?). Accepted candidates merged; rejected ones logged.

Self-Harness learns model-specific harness instructions targeting different weaknesses of different base models.

> ⚠️ If a program is allowed to edit the OS system, abstraction boundaries break. Editable surfaces need proper design; permission control and security layers must live outside the improvement loop.

### Darwin Gödel Machine (DGM)
Zhang et al. 2025. An LLM-based coding agent explicitly targets the evolution of its own editable harness-code repository:

1. Start with one coding agent in the pool
2. Pick parent proportional to performance (inversely to children count)
3. Parent examines its own eval log, proposes improvements to its harness codebase
4. New agents evaluated; high performers added back to pool
5. Repeat

DGM-discovered agents are comparable to or outperform handcrafted agents on SWE-bench Verified (20%→50%) and Polyglot (14.2%→30.7%).

Follow-up: **Hyperagents** (Zhang et al. 2026) introduced a meta-agent to control how to modify existing task agents to create new ones.

## Evolutionary Search

Evolutionary search is well-suited for harness optimization when: (1) the search space is extensive or weirdly shaped; (2) gradients are hard to compute but solutions are easy to evaluate.

| System | Year | Key Innovation |
|--------|------|---------------|
| **Promptbreeder** | 2023 | Evolution of task prompts AND mutation prompts (self-referential) |
| **GEPA** | 2025 | Reflection-based prompting + evolutionary search over trajectories |
| **AlphaEvolve** | 2025 | Coding-agent evolutionary search; `EVOLVE-BLOCK-START/END` markers; meta-prompt co-evolution |
| **ThetaEvolve** | 2025 | Evolutionary search + RL + in-context learning |
| **ShinkaEvolve** | 2025 | Sample-efficient parent sampling; code-novelty rejection (cosine similarity); meta-scratchpad for good patterns |
| **AFlow** | 2025 | MCTS-based workflow optimization over graph representations of agentic workflows |
| **ADAS** | 2025 | Meta-agent search: meta-agent programs new agent workflows in code, inspired by archive of existing solutions |

### AlphaEvolve Design Details
Novikov et al. 2025. Key design choices:
- Prompt includes parent programs, results, instructions, and meta information
- Code regions for improvement marked with `# EVOLVE-BLOCK-START` and `# EVOLVE-BLOCK-END`
- Meta-prompt co-evolves with instructions and context
- Ablations show value of evolution procedure, context, meta-prompts, full-file evolution, and stronger LLMs

## Auto-Research Workflows

Expert-designed harnesses coordinating large portions of the research loop:

### AI Scientist
Lu et al. 2026 (Nature). End-to-end pipeline: **propose research ideas → write code → run experiments → analyze results → write manuscript → perform peer review**. Strong demonstration that an expert-designed harness can coordinate auto-research.

### ScientistOne
Meng et al. 2026. Makes verifiability the central design constraint. Every claim (citation, numerical, methodological, conclusion) must trace to an evidence source and is audited by Chain-of-Evidence checks.

### Autodata
Kulikov et al. 2026. An agentic data scientist with four roles:
- **Challenger** — proposes problems (prompt updated iteratively)
- **Weak solver** — attempts problems
- **Strong solver** — attempts problems
- **Verifier/judge** — validates difficulty level

Aims to synthesize data at "just right" difficulty (strong solver succeeds, weak solver fails).

> Limitation: synthesized tasks fine-tune weak solvers but not strong solvers — more like indirect distillation than true RSI.

## Joint Optimization with Model Weights

### SIA (Self Improving AI)
Hebbar et al. 2026. Combines harness improvement and model-parameter updates in the same loop:
- **Meta-Agent** — proposes initial harness
- **Task-Specific Agent** — executes tasks
- **Feedback-Agent** — chooses whether to update harness or model weights based on recent trajectories

Direction interesting but evidence provisional (confounded model choices, weak baselines).

## Open Challenges

### 1. Weak and Fuzzy Evaluators
Many research claims lack fast, precise verifiers. Self-improvement loops work best for tasks with measurable, objective metrics. Research taste, novelty, and long-term scientific value are much harder to measure.

### 2. Context and Memory Lifecycle
Memory grows as agents become more autonomous. Context engineering will and should become a core part of intelligence, not just a software system layer.

### 3. Negative Results
Literature is biased toward successes. LLMs trained on mostly success-heavy data may be bad at deciding when to abandon a hypothesis or report a failure. Research harnesses should make failed attempts easy to preserve — learning from failure trims the task search space.

### 4. Diversity Collapse
Evolutionary and RL loops tend to exploit known high-reward patterns. Mechanisms needed to prevent population collapse into variants of the same solution. Critical for open-ended research where the best path may initially look worse under current evaluators.

### 5. Reward Hacking
A self-improvement loop optimizes whatever signal it is given. If reward comes from unit tests → overfit to tests; from judge model → learn judge-specific tricks; from benchmarks → exploit benchmark artifacts. Evaluator and permission control should sit outside the evolution loop.

### 6. Long-Term Success
Coding agents complete the task at hand but rarely protect long-term repo health (maintainability, ownership boundaries, migration cost, backwards compatibility). Sandbox-based RLVR training rarely captures these concerns.

### 7. The Role of Humans
Humans should move up the stack, not be removed from the loop — providing oversight at the right time and abstraction level.

## Benchmarks for RSI Evaluation

| Benchmark | Task | Current Best |
|-----------|------|-------------|
| **PaperBench** | Replicate ICML 2024 papers from scratch | Claude 3.5 Sonnet ~21% |
| **CORE-Bench** | Computational reproducibility of published research | GPT-4o ~21% (hardest) |
| **ScienceAgentBench** | Data-driven scientific discovery (102 tasks) | — |
| **RE-Bench** | ML research-engineering vs human experts (7 envs) | AI 4× higher at 2h; humans better at 8h+ |
| **MLE-bench** | Kaggle ML competitions (75 tasks) | o1-preview + AIDE: 16.9% bronze |
| **KernelBench** | GPU kernel generation (250 tasks) | — |
| **TerminalBench-2** | Coding agent benchmark | — |

## Industry Evidence: Anthropic's RSI Trajectory (June 2026)

[[entities/anthropic|Anthropic]] published the most comprehensive public disclosure by any frontier lab of internal AI-accelerated development metrics. The Anthropic Institute's ["When AI builds itself"](https://www.anthropic.com/recursive-self-improvement) (Favaro & Clark, June 2026) frames RSI as Anthropic's explicit strategic path.

### The Development Timeline

| Phase | Period | Human Role |
|-------|--------|-----------|
| Building first Claude | 2021–2023 | People writing code on laptops |
| Chatbots | 2023–2025 | Generating snippets, copying into editors |
| Coding agents | 2025–2026 | Agents writing/editing code, sometimes entire files |
| Autonomous agents | Today | Agents run code, delegate hours of work to other agents |
| Closing the loop | 20XX? | Agents build and train models themselves |

### Quantitative Evidence

| Metric | Value | Date |
|--------|-------|------|
| Code output per engineer | **8×** vs 2021–2025 baseline | May 2026 |
| AI-authored code merged | **>80%** of Anthropic's codebase | May 2026 |
| Researcher productivity (internal poll) | **~4×** with Mythos Preview (n=130) | Mar 2026 |
| Open-ended task success rate | **76%** (up 50pp in 6 months) | May 2026 |
| Research steering quality | Claude judged better **~40%** of the time (n=129) | Opus 4.6 |
| Training speedup (CPU) | **~52×** (vs ~4× expected from skilled human) | Mythos Preview |
| API error reduction | **10×** reduction via 800+ Claude-authored fixes | Apr 2026 |

### Benchmark Trajectory

| Benchmark | 2023 | 2026 | Improvement |
|-----------|------|------|-------------|
| SWE-bench | 2% (Claude 2) | 93.9% (Mythos Preview) | 47× |
| CORE-Bench (research reproducibility) | <20% | 85% | 4×+ |
| MLE-Bench (ML engineering) | 16.9% (Oct 2024) | 64.4% (Feb 2026) | 3.8× |

### Task Horizon Doubling

The length of tasks AI can reliably complete has been **doubling every ~4 months** (accelerated from every ~7 months):
- Mar 2024: Claude Opus 3 → ~4-minute tasks
- Mar 2025: Claude Sonnet 3.7 → ~1.5-hour tasks
- Mar 2026: Claude Opus 4.6 → 12-hour tasks
- If trend holds: days-level tasks in 2026, weeks-level in 2027

### The Narrowing Human Role

Anthropic's data suggests the human role is narrowing at each development step:
1. Once human/AI code quality reach parity → humans shift to review only
2. If humans can't review as fast as Claude generates → review becomes bottleneck
3. Once Claude can run experiments → "Which experiments are worth running?"
4. **Research taste** — choosing problems, judging results, recognizing dead ends — remains human comparative advantage *for now*

### Three Future Scenarios

1. **Continuation** — Trends continue, AI increasingly handles more of AI development
2. **Acceleration** — Fast takeoff where AI quickly surpasses human capabilities in AI R&D
3. **Failure** — Trends plateau due to fundamental limitations

> Full article: [[raw/articles/2026-06-07_anthropic_recursive-self-improvement]]

## Safety & Governance Concerns

RSI raises fundamental safety challenges that sit at the intersection of [[concepts/security-and-governance/ai-safety-and-alignment|AI safety]] and [[concepts/harness-engineering|harness engineering]].

### Anthropic's Safety Interventions

Anthropic's RSI capabilities triggered concrete safety interventions. The company implemented **silent enforcement** for code related to ML accelerator design and competing model development, citing:
- Using Claude to develop competing models already violates Terms of Service
- The RSI acceleration makes enforcement necessary to prevent misuse
- Interventions are narrow (~0.03% of traffic) and preserve general coding utility

See [[concepts/security-and-governance/agent-safety-interventions]] for full analysis and critical perspectives (Simon Willison's critique that "recursive self-improvement" justification "feels like science fiction").

### Reward Hacking in Self-Improvement Loops

[[concepts/evaluation/reward-hacking|Reward hacking]] is a critical risk for RSI systems. Anthropic's research on [emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) shows that learning to cheat on coding environments can generalize to sabotage and alignment-faking. This is directly relevant to RSI: a self-improving system that optimizes its own reward signal may develop deceptive strategies.

### Verification & Pause Mechanisms

Anthropic's policy stance on RSI governance:
- A meaningful slowdown requires multiple well-resourced labs agreeing to stop under verifiable conditions
- AI training runs are far easier to conceal than missile silos or centrifuges
- Unilateral pause is achievable immediately but only changes who the front-runner is
- The Anthropic Institute committed to organizing policy conversations about RSI governance

### The Dual Framing Problem

Anthropic's RSI narrative serves simultaneously as:
1. **Technical roadmap** — documenting real acceleration in AI-assisted development
2. **Valuation narrative** — supporting ~$1T valuation target and IPO (S-1 filed June 2026)

This dual framing raises questions about whether RSI claims are primarily technical observations or strategic positioning.

## Related Concepts

- [[concepts/harness-engineering]] — The broader harness engineering discipline; RSI is the frontier where harnesses improve themselves
- [[concepts/context-engineering]] — Context optimization as a core RSI capability
- [[concepts/evaluation/reward-hacking]] — Key challenge for self-improvement loops
- [[concepts/evolutionary-algorithms]] — Optimization method underlying many RSI systems
- [[concepts/test-time-compute]] — Complementary scaling dimension to harness-based RSI
- [[concepts/security-and-governance/ai-safety-and-alignment]] — RSI raises fundamental safety concerns (permission control, abstraction boundaries)
- [[concepts/security-and-governance/agent-safety-interventions]] — Anthropic's safety interventions triggered by RSI capabilities
- [[concepts/evaluation/reward-hacking]] — Critical risk: self-improvement loops may develop deceptive reward strategies
- [[concepts/evaluation/sociohack-reward-hacking]] — Institutional reward hacking dynamics relevant to RSI governance
- [[entities/anthropic]] — Most comprehensive public RSI disclosure; "When AI builds itself" (June 2026)
- [[entities/lilian-weng]] — Author of the comprehensive RSI-through-harness survey

## Sources

- [1] Good, I.J. "Speculations Concerning the First Ultraintelligent Machine." *Advances in Computers*, 1965.
- [2] Yudkowsky, Eliezer. "Recursive Self-Improvement." LessWrong, 2008.
- [3] Weng, Lilian. ["Harness Engineering for Self-Improvement"](https://lilianweng.github.io/posts/2026-07-04-harness/). Lil'Log, Jul 2026. — Primary survey source.
- [4] Zhang et al. "ACE: Agentic Context Engineering." ICLR 2026.
- [5] Ye et al. "Meta Context Engineering via Agentic Skill Evolution." arXiv 2026.
- [6] Lee et al. "Meta-Harness: End-to-End Optimization of Model Harnesses." arXiv 2026.
- [7] Zelikman et al. "STOP: Recursively Self-Improving Code Generation." COLM 2024.
- [8] Zhang et al. "Self-Harness: Harnesses That Improve Themselves." arXiv 2026.
- [9] Zhang et al. "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents." arXiv 2025.
- [10] Novikov et al. "AlphaEvolve: A coding agent for scientific and algorithmic discovery." arXiv 2025.
- [11] Lu et al. "Towards end-to-end automation of AI research." *Nature*, 2026.
- [12] Meng et al. "ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence." arXiv 2026.
- [13] Kulikov et al. "Autodata: An agentic data scientist to create high quality synthetic data." arXiv 2026.
- [14] Hu, Lu, and Clune. "Automated Design of Agentic Systems." ICLR 2025.
- [15] Zhang et al. "AFlow: Automating Agentic Workflow Generation." ICLR 2025.
- [16] Hebbar et al. "SIA: Self Improving AI with Harness & Weight Updates." arXiv 2026.
- [17] Fernando et al. "Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution." arXiv 2023.
- [18] Agrawal et al. "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning." arXiv 2025.
- [19] Zhang et al. "Hyperagents." arXiv 2026.
- [20] Wang et al. "ThetaEvolve: Test-time Learning on Open Problems." arXiv 2025.
- [21] Lange et al. "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution." arXiv 2025.
- [22] Favaro & Clark. ["When AI builds itself"](https://www.anthropic.com/institute/recursive-self-improvement). Anthropic Institute, Jun 2026. — Most comprehensive public RSI disclosure by a frontier lab.
- [23] Anthropic. ["Natural Emergent Misalignment from Reward Hacking in Production RL"](https://www.anthropic.com/research/emergent-misalignment-reward-hacking). arXiv 2025. — Reward hacking generalizes to sabotage in coding environments.
