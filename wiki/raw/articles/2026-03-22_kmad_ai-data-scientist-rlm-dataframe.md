---
title: "A Data Scientist RLM That Lives in Your Program"
source: https://kmad.ai/A-Data-Analysis-Agent-That-Lives-in-Your-Program
author: Kevin Madura
url: https://kmad.ai/A-Data-Analysis-Agent-That-Lives-in-Your-Program
date: 2026-03-22
type: article
tags: [rlm, dspy, data-analysis, sandbox, dataframe, pyodide, deno, wasm, benchmark]
---

# A Data Scientist RLM That Lives in Your Program

*… or how to process DataFrames with RLMs and DSPy*

**Author**: Kevin Madura (kmad.ai)
**Date**: March 22, 2026

## Background: Recursive Language Models

After experimenting with Recursive Language Models (RLMs) since their publication, I've been continually impressed by the powerful simplicity of the approach. For some of my existing workflows, it's been a drop-in replacement, dramatically simplifying tasks like extracting long-form data from 100+ page documents.

The core premise of an RLM is to embed an LLM inside a REPL, giving it access to its inputs symbolically. The distinction discussed in this post, compared to typical coding agents, is **interactivity versus programmability**. Coding agents provide interactivity out of the box; RLMs and Signatures allow you to "inline" intelligence within a data pipeline.

According to Omar (the paper's co-author), a model qualifies as an RLM if:

1. The user prompt is a symbolic object (variable, file, etc.) rather than just a sequence of tokens in the Transformer context window
2. The model must interact with that symbolic object by writing code in a persistent REPL environment
3. The code that the model writes must be able to invoke an LLM/RLM inside the REPL (e.g., within loops or recursive functions), and—crucially—not as a discrete sub-agent tool

The initial RLM implementation focused on strings accessed as variables in the REPL. But a REPL can support all sorts of types. Allowing an LLM to work with direct access to native variables lets it freely navigate and explore the contours of the data without you having to specify everything up front.

## DataFrame as RLM Extension

Most data science work involves cleaning, combining, analyzing, or reviewing multiple DataFrames at once. The only way today to process structured data is to point a code-writing agent (like Claude Code or Codex) to generate custom scripts for specific tasks. Depending on your objective, this approach can be brittle (for example, outlining a data cleaning approach as a skill). While it can work, it's not exactly ergonomic for integrating into larger systems or pipelines.

DSPy shines here thanks to its flexible abstractions that don't "get in your way."

## DSPy, RLMs, and the Sandbox

DSPy added RLM support the same week the work was published (Alex Zhang is a PhD student working with Omar Khattab, the creator of DSPy, both at MIT CSAIL).

To add DataFrame support, Kevin Madura has proposed a PR that establishes a **protocol for defining how custom types—like DataFrames—can be exposed to the RLM sandbox**.

### SandboxSerializable Protocol

The PR implements a new `SandboxSerializable` protocol (using `typing.Protocol`) with four abstract methods:

- `sandbox_setup` — specify imports needed in the sandbox environment
- `to_sandbox` — serialize the object for the REPL
- `sandbox_assignment` — define how the object is assigned as a REPL variable
- `rlm_preview` — generate a preview of what the LLM sees in its prompt

Any type implementing this protocol automatically inherits a concrete `to_repl_variable()` method. This standardizes how types interact with the REPL while also allowing the flexibility to specify imports and fine-tune serialization logic as needed.

### Why This Matters

Under the hood, DSPy uses **Deno and Pyodide** to actually execute REPL code. For types that need extra imports, this lets us specify what's needed in the sandbox at setup. Fortunately for us, Pyodide supports `pyarrow` and `pandas` out of the box.

## Example Usage: Cohort Retention Analysis

Mock data generated for users, events, and subscriptions with embedded signals (e.g., the worst channel should be `paid_campaign_x` with the highest churn of ~45%).

### DSPy Signature

```python
class CohortRetentionAnalysis(dspy.Signature):
    """You are a data analyst investigating why user retention is dropping.
    Investigate the data step by step. Compute retention by cohort,
    segment by acquisition channel, compare feature usage between
    retained and churned users, and identify the root cause of churn."""

    users: DataFrame = dspy.InputField(desc="User profiles with signup_date, acquisition_channel, country")
    events: DataFrame = dspy.InputField(desc="Feature usage events with user_id, event_type, timestamp")
    subscriptions: DataFrame = dspy.InputField(desc="Subscription records with status, plan, mrr, cancellation_reason")

    overall_churn_rate: float = dspy.OutputField(desc="Overall churn rate as a decimal (e.g. 0.25 for 25%)")
    worst_channel: str = dspy.OutputField(desc="Acquisition channel with highest churn rate")
    key_finding: str = dspy.OutputField(desc="The main insight about what differentiates churned users")
    recommendations: str = dspy.OutputField(desc="2-3 actionable recommendations based on the analysis")
```

### Results

The RLM completed in 7 iterations, accurately predicting the expected churn rate and correctly identifying the worst channel:

| Metric | Expected | Actual |
|--------|----------|--------|
| Overall Churn Rate | ~23–25% | 23.8% |
| Worst Channel | paid_campaign_x (≈45% churn) | paid_campaign_x (44.76%) |
| Advanced Reports Use | ~33–35% adoption outside PCX | 33–35% for other channels, 18.7% for PCX |
| PCX Churn among Non-Users of Advanced Reports | Highest | Churn concentrated among non-users |

## Benchmarking: InfiAgent-DABench

InfiAgent-DABench is a benchmark of **257 data analysis questions across 68 CSV files**, spanning summary statistics, correlation analysis, distribution analysis, feature engineering, outlier detection, and machine learning.

The entire solver is minimal:

```python
def run_task(question, constraints, format_spec, csv_path, verbose=False):
    data = DataFrame(pd.read_csv(csv_path))
    rlm = dspy.RLM(DataAnalysisTask, max_iterations=15, verbose=verbose)
    result = rlm(data=data, question=question, constraints=constraints, format_spec=format_spec)
    return result.answer
```

### Results

| Model | Easy (82) | Medium (87) | Hard (88) | Total (257) | Avg Iters | Avg Time |
|-------|-----------|-------------|-----------|-------------|-----------|----------|
| Qwen 3.5 397B | 72 (88%) | 79 (91%) | 72 (82%) | 223 (86.8%) | 2.8 | 24.4s |
| MiniMax M2.7 | 75 (91%) | 75 (86%) | 72 (82%) | 222 (86.4%) | 6.1 | 73.7s |

Both models achieve ~87% accuracy with the same solver code. The notable difference is **efficiency**: Qwen solves tasks in 2.8 iterations on average (24s), while MiniMax requires 6.1 iterations (74s). This suggests Qwen is better at planning its analysis upfront, while MiniMax takes a more exploratory approach.

## Next Steps

1. **Support for Additional Types**: Extend the protocol to other complex data structures—images, geospatial data, or domain-specific objects
2. **Prompt Optimization with GEPA**: Use GEPA's `optimize_anything` to evolve the solver code itself
3. **Interactive Debugging & Traceability**: Explore improved debugging tools for RLM sessions
4. **End-to-End Pipelines**: Integrate RLM-empowered objects into larger data pipelines or external orchestration systems
