---
title: "Demystifying Evals for AI Agents"
source: "Anthropic Engineering Blog"
date: 2026-01-09
authors: ["Anthropic"]
tags: [evals, ai-agents, evaluation, anthropic, harness-engineering]
url: "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
type: article
---

# Demystifying Evals for AI Agents: A Comprehensive Summary

Published by Anthropic on January 9, 2026, this guide explores the complexities of evaluating AI agents—systems that operate over many turns, use tools, and modify environments.

## 1. Core Definitions & Structure

An **evaluation ("eval")** is an automated test consisting of an input and grading logic. Unlike single-turn LLM prompts, agent evals measure multi-turn trajectories.

- **Task/Problem:** A single test case with defined success criteria.
- **Trial:** A single attempt at a task. Multiple trials are needed due to model non-determinism.
- **Transcript (Trace/Trajectory):** The complete record of tool calls, reasoning, and interactions.
- **Outcome:** The final state of the environment (e.g., "Does the database reflect the booking?").
- **Agent Harness (Scaffold):** The system enabling the model to act (orchestrating tool calls).
- **Evaluation Suite:** A collection of tasks measuring specific capabilities (e.g., customer support).

## 2. The Three Types of Graders

Effective agent evaluation combines different grading methodologies:

| Grader Type | Methods | Strengths | Weaknesses |
| :--- | :--- | :--- | :--- |
| **Code-based** | String match, unit tests, static analysis, tool call verification. | Fast, cheap, objective, reproducible. | Brittle to valid variations; lacks nuance. |
| **Model-based** | LLM-as-judge, rubrics, pairwise comparison. | Flexible, scalable, handles open-ended tasks. | Non-deterministic; requires human calibration. |
| **Human** | SME review, A/B testing, spot-checks. | Gold standard; matches expert judgment. | Expensive, slow, hard to scale. |

## 3. Evaluation Strategies by Agent Type

### Coding Agents
Focus on deterministic outcomes. Does the code run? Do tests pass?
- **Benchmarks:** SWE-bench Verified (GitHub issues), Terminal-Bench (end-to-end technical tasks).
- **Insight:** Grade the *outcome* (passing tests) primarily, but use LLM rubrics for *code quality*.

### Conversational Agents
Focus on interaction quality and state resolution.
- **Method:** Often requires a second LLM to simulate a user persona.
- **Benchmarks:** τ-Bench and τ²-Bench (retail/airline scenarios).

### Research Agents
Focus on synthesis and source quality.
- **Challenges:** Ground truth shifts; experts may disagree on "comprehensiveness."
- **Strategy:** Combine groundedness checks (claims vs. sources) with coverage checks (key facts included).

### Computer Use Agents
Focus on GUI interactions (screenshots, clicks).
- **Benchmarks:** WebArena (browser), OSWorld (full OS control).
- **Efficiency Tip:** Use DOM-based interactions for speed/token savings, but switch to screenshots for token-intensive pages like Amazon.

## 4. Key Metrics for Non-Determinism

Because agents vary between runs, two specific metrics are essential:
- **pass@k:** Probability of getting at least one correct solution in *k* attempts. (Best for creative problem solving).
- **pass^k:** Probability that *all k* trials succeed. (Best for high-reliability customer-facing agents).

## 5. Roadmap: From Zero to Trusted Evals

1. **Start Early:** Begin with 20–50 simple tasks based on real failures.
2. **Unambiguous Tasks:** A task is good if two experts independently reach the same verdict.
3. **Balanced Sets:** Include cases where a behavior *should* and *shouldn't* occur (e.g., when to search the web vs. when to use internal knowledge).
4. **Stable Environments:** Ensure each trial starts in a clean, isolated sandbox to avoid "shared state" noise.
5. **Partial Credit:** Grade the continuum of success (e.g., identifying a problem even if the final fix fails).
6. **Read Transcripts:** This is the only way to verify if a "fail" was a model error or a grading bug.

## 6. Key Excerpts & Code Snippets

### Theoretical Coding Agent Eval (YAML)
```yaml
task:
  id: "fix-auth-bypass_1"
  graders:
    - type: deterministic_tests
      required: [test_empty_pw_rejected.py, test_null_pw_rejected.py]
    - type: llm_rubric
      rubric: prompts/code_quality.md
    - type: tool_calls
      required:
        - {tool: read_file, params: {path: "src/auth/*"}}
        - {tool: edit_file}
```

### Important Insight on "Creative" Failures
> "Opus 4.5 solved a τ²-bench problem about booking a flight by discovering a loophole in the policy. It 'failed' the evaluation as written, but actually came up with a better solution for the user."

### On Eval Saturation
> "An eval at 100% tracks regressions but provides no signal for improvement. Eval saturation occurs when an agent passes all of the solvable tasks... large capability improvements [then] appear as small increases in scores."

## 7. Holistic Performance Framework

Anthropic recommends a "Swiss Cheese Model" where multiple layers catch different issues:
- **Automated Evals:** Pre-launch/CI/CD defense.
- **Production Monitoring:** Detects real-world distribution drift.
- **A/B Testing:** Compares new agent versions against baseline.
- **Adversarial Testing:** Red-teaming and edge case probing.
- **Human Evaluation:** Periodic expert reviews for calibration.
- **Feedback Loops:** User feedback and post-hoc analysis integrated back into eval suites.
