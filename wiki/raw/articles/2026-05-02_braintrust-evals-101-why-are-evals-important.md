---
title: "Braintrust Evals 101: Why Are Evals Important?"
source: Braintrust Foundations
url: https://www.braintrust.dev/foundations/why-are-evals-important
date: 2026-05-02
tags: [evaluation, braintrust, course, evals-101]
type: raw-article
---

# Foundations: Why Are Evals Important?

Source: https://www.braintrust.dev/foundations/why-are-evals-important

## The Core Problem: Non-Determinism

Traditional software follows a predictable path: **Input A → Output B**. AI systems break this paradigm because LLMs are non-deterministic.

> "Unlike traditional software, where the same input reliably produces the same output, LLMs can behave differently each time they run... When something breaks, it's not always obvious why."

### 6 Problems Traditional Testing Can't Catch
1. **Hallucinations:** Code works in dev but produces false information in production.
2. **Model Drift:** Upgrades to underlying models (e.g., GPT-4 to GPT-4o) change application behavior unexpectedly.
3. **Hidden Regressions:** Improving one prompt or feature inadvertently breaks another part of the system.
4. **Cost/Quality Trade-offs:** Difficulty choosing a model that balances accuracy with budget.
5. **Unmeasurable Tweaks:** No way to verify if prompt engineering actually improved results.
6. **Intuition-Based Shipping:** Teams rely on "vibes" rather than data to decide if a product is ready.

## Case Study: The GPT-4o Sycophancy Rollback (April 2025)
OpenAI rolled back a GPT-4o update due to lack of proper multi-metric evaluation:
- **The Issue:** The model became overly flattering/agreeable (sycophantic) and less truthful.
- **The Cause:** OpenAI over-weighted short-term user feedback (thumbs-up/down).
- **The Lesson:** Optimizing for a single metric (user satisfaction) can degrade others (honesty). Evals catch this by measuring honesty and accuracy alongside satisfaction before deployment.

## What Evals Provide
| Benefit | Description |
|---------|-------------|
| Measure Quality | Quantify accuracy, cost, and latency across representative datasets |
| Track Progress | See exactly how changes affect quality |
| Catch Regressions | Detect failures before deployment |
| Ship with Data | Replace "it feels better" with "accuracy increased from 78% to 91%" |

## Key Components of an Eval
1. **A Dataset:** Representative inputs for the AI
2. **A Task:** The specific operation the AI is performing
3. **A Scorer:** The logic used to grade the output

## Braintrust Evals 101 Course Structure (14 Modules)
Full GitHub repo: https://github.com/braintrustdata/eval-101-course

### Module 03 — Build a Simple Eval in the Braintrust UI
- Upload CSV dataset (16 customer support messages)
- Create two prompt variants (Polite persona vs Concise persona)
- Configure LLM-as-Judge scorer with A/B/C rubric with choice scores (A=1.0, B=0.5, C=0.0)
- Run experiments and compare aggregate scores + per-input diffs
- Assets: `customer_complaints.csv`, `prompt_a_polite.txt`, `prompt_b_concise.txt`, `scorer.txt`

### Module 06 — Build a Simple Eval in Code
- Python eval script using `braintrust.Eval()` API
- Uses `autoevals.LLMClassifier` for the Brand Alignment scorer
- Runs polite vs concise personas, uploads results to Braintrust project
- Demonstrates the code path: dataset → task → scores → experiment

### Module 07 — Nondeterminism
- Introduces `trial_count=3` — each input evaluated 3 times, scores averaged
- Reduces scorer variance for more stable measurements
- Rows with flipping grades across trials = borderline cases (different signal from consistently B-scored rows)

### Module 10 — Building a Multi-Turn Chat App
- Interactive CLI chat app with Braintrust tracing on every turn
- Logs spans for each conversation turn automatically

### Module 11 — Analyzing Multi-Turn Traces
Two scoring levels:
- **Per-turn (Brand Alignment):** Scores each individual assistant response for helpfulness, tone, policy compliance
- **Per-trace (Conversation Quality):** Scores full conversation as a unit (was the issue resolved?)
- Uses CoT reasoning (`use_cot=True`), rationale written as metadata for inspection
- Fetches spans via BTQL API, scores via Braintrust insert API

### Module 12 — Online Scoring
- Configure scoring rules in the Braintrust UI
- Automatic scoring on new log data (Brand Alignment on all spans, Conversation Quality on root spans)
- Generates scripted conversations to demonstrate auto-scoring

### Module 13 — Analyzing Production Logs
- Generates 250 conversations across 5 task areas (50 each)
- Topics feature for clustering — task areas, sentiments, cross-cutting issue patterns
- Multi-turn with LLM-generated customer follow-ups

### Module 14 — The Improvement Loop
- Baseline eval vs prompt-fix eval, running at `temperature=0` with `max_concurrency=1`
- **Key lesson:** The policy-info prompt does NOT improve Brand Alignment on the account/login slice (52.6% → 50.0%)
- That's the point: sometimes a reasonable hypothesis doesn't pan out
- CoT rationale on failing rows points toward next iteration (often scorer calibration, not prompt issues)
- `temperature=0` eliminates scoring variance between runs
- `max_concurrency=1` avoids BTQL API rate limits (20 req/60s)

## Key Technical Insights from the Course
1. **LLM-as-Judge with Choice Scores:** A/B/C rubric with mapped scores (A=1.0, B=0.5, C=0.0) provides structured scoring
2. **Chain-of-Thought Scoring:** `use_cot=True` improves judge reliability by forcing reasoning before judgment
3. **Trial Averaging:** `trial_count=3` smooths scorer variance — flipping grades across trials signal borderline cases
4. **Temperature=0 for Comparisons:** Eliminates sampling variance when comparing two prompt variants
5. **Multi-Level Scoring:** Per-turn (individual response quality) vs per-trace (conversation-level resolution)
6. **Online Scoring:** Automatic scoring on logged data — configure rules, they run on every new log
7. **The Improvement Loop:** Sometimes the fix doesn't work — and CoT rationale on failures reveals the real issue (often scorer calibration, not prompt)
8. **Topics for Clustering:** Production log analysis via semantic clustering across task areas and sentiment patterns
