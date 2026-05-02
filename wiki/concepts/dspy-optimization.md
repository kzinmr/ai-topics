---
title: "DSPy Optimization — Teleprompters, Assertions, Fine-Tuning"
tags:
  - concept
  - dspy
  - optimization
  - teleprompter
  - assertion
  - fine-tuning
created: 2026-04-28
updated: 2026-04-28
type: concept
---

# DSPy Optimization Techniques

## 1. Teleprompters (Optimizers)

Teleprompters are the optimization engine of DSPy. Given training data and a [[concepts/dspy-architecture|metric]], they automatically optimize the entire pipeline's prompts.

### Optimizer Comparison

| Optimizer | Algorithm | Cost | Quality |
|-----------|-----------|------|---------|
| `BootstrapFewShot` | Auto-collect correct demonstrations | Low | Baseline |
| `BootstrapFewShotWithRandomSearch` | Correct examples + random search | Medium | Good |
| `MIPROv2` | Bayesian optimization + Chain of Thought | High | State-of-the-art |
| `COPRO` | Gradient-based prompt evolution | Medium | Good |
| `Ensemble` | Multi-module majority voting | Variable | Reliable |

### Optimization Pipeline

1. **Candidate generation:** Optimizer extracts demonstrations from training examples
2. **Evaluation:** Each candidate is scored against the metric
3. **Selection:** Pareto-optimal solutions (quality vs token cost) are selected
4. **Compilation:** Selected demonstrations are embedded into the final prompt

## 2. DSPy Assertions — Computational Constraints

Introduced in DSPy v2.3, Assertions provide **runtime validation** with automatic self-correction.

```python
@dspy.assert
def validate_answer(answer):
    assert len(answer) < 100, "Answer too long"
    assert not any(word in answer.lower()
        for word in ["i don't know", "unknown"]), "No uncertainty allowed"
```

**How it works:**
1. Assertion violation detected → DSPy automatically **re-invokes** the LM
2. Violation details are fed back as context to the LM
3. Retries up to N times (configurable)
4. If still failing, an exception is raised

This is fundamentally different from **post-hoc validation** — it embeds a **self-correction loop** directly into the pipeline.

## 3. Fine-Tuning + Prompt Optimization Synergy

Paper: *"Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together"* (July 2024)

**Key findings:**
- Prompt optimization alone → +15% improvement
- Fine-tuning alone → +12% improvement
- **Combined** → +23% improvement (synergistic, not additive)

**Why:** Fine-tuning improves the model's fundamental reasoning ability, while prompt optimization tunes task-specific strategies. They operate on **different dimensions**, creating synergy when combined.

---

## See Also

- [[concepts/dspy]] — Main DSPy concept page
- [[concepts/dspy-architecture]] — How optimizers interact with Signatures and Modules
- [[concepts/gepa]] — Genetic prompt evolution (advanced optimizer approach)
- [[concepts/dspy-comparisons]] — Comparison with other optimization paradigms
