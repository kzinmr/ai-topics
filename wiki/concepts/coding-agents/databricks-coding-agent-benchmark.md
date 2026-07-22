---
title: "Databricks Coding Agent Benchmark"
created: 2026-07-10
updated: 2026-07-22
type: concept
tags: [coding-agents, agent-evaluation, benchmark, databricks, enterprise-ai, swere-bench, evaluation, cost-optimization, model-routing, open-weight, claude-code, codex, devin, pi, omnigent]
sources:
  - raw/articles/2026-07-08_databricks-coding-agent-benchmark.md
  - "https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase"
---

## Overview

In July 2026, [[entities/databricks]] published an internal methodology and results for benchmarking coding agents on their own **multi-million line production codebase** — a significant departure from public synthetic benchmarks like [[swe-bench]]. Rather than relying on leaked, public-domain tasks, Databricks constructed a private benchmark from their own merged pull requests, spanning 10+ languages (Scala, Go, Rust, Java, Python, TypeScript, Protobuf, Bazel) and verified by the original PR test suites.

The exercise was motivated by a practical need: with the rapid expansion of coding agent models and harnesses, Databricks wanted a data-driven way to select the right model-and-harness combination for everyday engineering tasks while optimizing for **cost-per-task** rather than cost-per-token.

## Key Findings

### 1. Three Capability Tiers Emerge

Models and harnesses clustered into three distinct capability tiers:
- **Top tier** (87%+ pass rate): Frontier models (Opus 4.8, GLM 5.2) solving all problem complexities, but at high cost ($1.94–$1.28/task).
- **Mid tier**: Effective for moderate-complexity tasks, significantly cheaper.
- **Lower tier**: Sufficient for common operational tasks (flag flips, config updates) at very low cost.

The practical implication: engineers should **route tasks by complexity**, using cheaper models for the ~25% low-complexity work and mid-tier models for ~60% medium-complexity tasks, rather than defaulting to the most expensive model across the board. Databricks specifically identified Haiku and GPT 5.4 Mini class of models as suitable for these routine operational tasks.

### 2. Open Models Are Competitive for Daily Coding

GLM 5.2 landed in the top capability tier, statistically tied with Opus 4.8 on quality (87%) while costing **$1.28/task vs $1.94/task**. Databricks reported that internal developers piloting GLM for daily development gave qualitative feedback consistent with the benchmark scores. The company is now actively deploying open-weight models as daily drivers for coding.

### 3. Price-Per-Task ≠ Price-Per-Token

Token pricing is a poor proxy for end-to-end task cost. Sonnet 5 is ~1.7× cheaper per token than Opus 4.8, but on Databricks' tasks it cost **$2.09/task vs $1.94** and scored 6 points lower (81% vs 87%). Sonnet consumed 1.9× more tokens because it "worked longer and read more to get there." This underscores the need for task-level benchmarking rather than reasoning from token price sheets.

### 4. Harnesses Dramatically Impact Efficiency

Running the same model through different harnesses ([[entities/claude-code]]/[[entities/codex]] vs [[entities/pi]]) yielded **>2× cost differences** while quality remained identical. Pi sent ~3× less context per turn, kept a tighter working set, and finished tasks in fewer rounds. The lesson: model choice is only part of the puzzle — harness architecture (context management strategy, tool use patterns) is equally consequential for cost.

## Methodology

Databricks' benchmark construction followed a rigorous pipeline:

1. **Candidate Selection**: Pulled from recently merged, human-written PRs with associated high-quality test suites. Filtered out bot commits, auto-generated changes, and fully AI-generated code.

2. **Task Construction**: For each candidate PR:
   - The PR description was rewritten as an **outcome-oriented prompt** — stating the problem/goal and constraints, but removing any description of the solution (which would make the task too easy).
   - The test files were held out as the evaluation criterion. Non-test files were what the agent had to reproduce.
   - Build system dependency analysis identified which test targets to run for validation.

3. **Test Suite Refinement**: Manual inspection of each sample. Some original PR tests were rewritten to allow alternative implementations or to grade behavior rather than exact string matching (e.g., for non-deterministic outputs).

4. **Execution**: Coding agents were instantiated with standard out-of-the-box setups and all tools Databricks engineers would have. When the agent declared completion, the code was checkpointed, held-out tests were patched in, and pass/fail was determined by test execution — **no LLM judge** was used, as Databricks found LLM judges "reward sounding right over being right."

5. **Git History Sealing**: A critical guardrail — early runs showed agents recovering the "correct" implementation from git history. For subsequent runs, the working copy was severed from the repository entirely to prevent this leakage.

6. **Telemetry**: [[entities/databricks]] used **Unity AI Gateway** to capture logs of all coding interactions, enabling task-complexity analysis and revealing that ~25% of tasks were low-complexity and ~60% medium complexity — yet expensive models were the default choice.

## Implications

### For Enterprise AI Strategy

The benchmark demonstrates that any organization with a backlog of merged PRs already possesses a private, high-quality coding agent benchmark — one that no model has trained on and that is graded by the team's own test suites. This "bring your own benchmark" approach avoids the training-data contamination problems endemic to public benchmarks like [[swe-bench]].

### For Coding Agent Evaluation

The results challenge three common industry assumptions:
- **"More expensive models are always better"** — task routing by complexity can dramatically reduce costs without sacrificing outcomes.
- **"Token price predicts task cost"** — reasoning efficiency varies widely; task-level benchmarking is essential.
- **"The native harness is optimal"** — simpler harnesses like [[entities/pi]] can match or exceed the efficiency of model-native harnesses.

### For the Broader Ecosystem

Databricks' investment in Omnigent as a model-and-harness-swapping layer reflects a strategic bet on **avoiding vendor lock-in** not just across model providers, but across harness architectures. The follow-up work on intelligent routing via Unity AI Gateway points toward automated model selection based on task characteristics.

### DIY Benchmarking Takeaway

Databricks emphasizes that **any team with a backlog of merged PRs already possesses a private, high-quality coding agent benchmark** — one no model has trained on, graded by the team's own test suites. The tasks are self-contained and the test infrastructure already exists. This "bring your own benchmark" approach is presented as an accessible starting point for any engineering organization.

## Related Pages

- [[coding-agents]] — Overview of the coding agent landscape
- [[swe-bench]] — The dominant public benchmark for coding agents
- [[evaluation-coding-agents]] — General evaluation approaches for coding agents
- [[entities/databricks]] — Company profile
- [[entities/claude-code]] — Anthropic's coding agent harness
- [[entities/codex]] — OpenAI's coding agent
- [[entities/devin]] — Cognition's autonomous coding agent
- [[entities/pi]] — Lightweight coding agent harness
