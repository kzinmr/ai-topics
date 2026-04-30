---
title: "How we optimized Dash's relevance judge with DSPy"
type: raw-article
created: 2026-04-30
url: https://dropbox.tech/machine-learning/optimizing-dropbox-dash-relevance-judge-with-dspy
source: dropbox.tech
tags: [dspy, llm-as-judge, production-case-study, gepa, mipro, model-adaptation]
---

# How Dropbox Optimized Dash's Relevance Judge with DSPy

Dropbox Dash uses a "relevance judge" to determine which files and messages are most pertinent to a user's query. This article details how Dropbox transitioned from manual prompt engineering to systematic optimization using **DSPy**, reducing costs and improving model alignment with human judgment.

---

## 1. The Core Challenge: Scaling Relevance

Relevance judges are critical for ranking, training data generation, and offline evaluation. However, manual prompt tuning is brittle:
- **Model Incompatibility:** Prompts optimized for high-end models (like OpenAI o3) often fail when moved to cheaper, smaller models.
- **Quality Plateaus:** Manual edits eventually reach a point of diminishing returns.
- **Regression Risk:** Small prompt changes can cause unexpected failures in edge cases.

## 2. Measuring Success: The Objective Function

Dropbox defines "good" performance through two primary lenses:
1. **Human Alignment:** Comparing model scores (1–5 scale) against human annotators using **Normalized Mean Squared Error (NMSE)**.
   - *NMSE of 0:* Perfect agreement.
   - *Higher NMSE:* Worse alignment.
2. **Structural Reliability:** Ensuring the model outputs valid JSON. If the output is unparseable, it is treated as a total failure.

## 3. Adapting to Large-Scale Use (gpt-oss-120b)

To scale, Dropbox moved from OpenAI's o3 to **gpt-oss-120b**. They used DSPy's **GEPA optimizer** to bridge the performance gap.

### The DSPy Reflection Loop
Instead of manual rewriting, the system uses a feedback loop:
1. **Evaluate:** Compare model output to human gold standard.
2. **Feedback:** Generate structured textual feedback on the gap.
3. **Refine:** DSPy revises the prompt based on failure patterns (e.g., "underweighting recency").

**Key Code Snippet: Feedback Construction**
```python
diff = predicted_rating - expected_rating
direction = "higher" if diff > 0 else "lower"
feedback_parts = [
    f"Predicted rating {int(predicted_rating)} but expected {int(expected_rating)}.",
    f"Model rated {abs(diff):.0f} point(s) {direction} than the expected human rating.",
]

# Include human explanation and model reasoning
if gold.explanation:
    feedback_parts.append(f"Human rationale: {gold.explanation}")
if pred.explanation:
    feedback_parts.append(f"Model's reasoning: {pred.explanation}")

feedback_parts.append(
    "Remember: when adapting the prompt, avoid overfitting to specific example(s)... "
    "Try to add a general rule to an execution plan to rate similar documents in the future."
)
```

### Results of Adaptation
- **NMSE Reduction:** Dropped **45%** (from 8.83 to 4.86).
- **Efficiency:** Adaptation time fell from **2 weeks to 2 days**.
- **Scale:** Enabled labeling **10–100x more data** at the same cost.

---

## 4. Improving Operational Reliability (gemma-3-12b)

Dropbox tested **gemma-3-12b** to see if a small model could handle the task. Initially, it failed due to formatting issues.

| Version | NMSE | Valid Format | Invalid Format |
| :--- | :--- | :--- | :--- |
| **Original Prompt (Baseline)** | 46.88 | 498 | 358 |
| **DSPy Prompt (MIPROv2)** | 17.26 | 847 | 9 |

**Insight:** DSPy reduced malformed JSON outputs by **over 97%**, proving that optimization can make small models operationally dependable.

---

## 5. Incremental Improvements for Production (o3)

For the high-stakes production o3 model, Dropbox avoided full rewrites to prevent "blast radius" regressions. They used an **Instruction Library Layer**:
- **Human-in-the-loop:** Humans write "rules of thumb" based on model errors (e.g., *"Documents older than a year should be rated one point lower"*).
- **DSPy's Role:** The optimizer selects which specific instruction bullets to include in the final prompt.
- **Benefit:** This functions like "small PRs with tests," allowing for stable, incremental gains.

## 6. Conclusion

By treating prompt engineering as a repeatable optimization loop rather than a manual craft, Dropbox achieved:
- **Lower Costs:** Successful migration to cheaper open-weight models.
- **Higher Trust:** Better alignment with human intent.
- **Agility:** The ability to swap models rapidly as the AI landscape evolves.
