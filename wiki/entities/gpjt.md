---
title: "Giles Thomas (gpjt)"
tags: [person]
created: 2026-04-24
updated: 2026-04-15
type: entity
---

# Giles Thomas

## Overview

Giles Thomas is a software engineer and blogger known for his detailed, hands-on series **"Writing an LLM from scratch"** — a comprehensive, iterative exploration of building and training large language models on consumer hardware. His work bridges the gap between academic deep learning theory and practical, accessible implementation, demonstrating that meaningful LLM training can be done locally on a single RTX 3090.

## Core Project: Writing an LLM from Scratch

A multi-part blog series documenting the end-to-end process of building and training a language model from first principles. Key themes:

- **Reproducibility**: Every experiment is documented with exact configurations, hyperparameters, and results
- **Local Training**: Demonstrates that competitive model quality can be achieved on consumer GPUs (RTX 3090) through careful optimization
- **Iterative Improvement**: Each post introduces a specific intervention and measures its impact on model loss

### Part 32k: Gradient Accumulation (April 2026)

A landmark post demonstrating how to simulate cloud-scale batch sizes on consumer hardware:

- **Problem**: RTX 3090 max batch size of 6 vs. cloud batch size of 96 (8× A100 40GB)
- **Solution**: Gradient accumulation — run multiple forward/backward passes, accumulate gradients, step optimizer once
- **Critical Insight**: Batch size dominates model quality. Gradient accumulation improved loss by 0.113765 through stacked interventions, while simply increasing batch size to 96 improved it by 0.252474 (**>2x larger impact**)

#### Key Technical Findings

**Loss Scaling Correction:**
```python
# WRONG: accumulating unscaled losses multiplies effective learning rate
(loss / gradient_accumulation_steps).backward()  # CORRECT: scale before backward

if (step + 1) % gradient_accumulation_steps == 0 or step == len(dataset) - 1:
    optimizer.step()
    optimizer.zero_grad()
```

**DDP Optimization with `no_sync()`:**
```python
is_last = accumulation_step == gradient_accumulation_steps - 1

with model.no_sync() if not is_last else nullcontext():
    scaler.scale(train_loss / gradient_accumulation_steps).backward()
```

Defers gradient synchronization until the final accumulation step, reducing communication overhead in distributed training.

#### Results Summary

| Run | Test Loss | Improvement vs Baseline |
|-----|-----------|------------------------|
| 8×A100M40-baseline | 3.691526 | — |
| 1×RTX3090-baseline | 3.683835 | +0.007691 |
| 1×RTX3090-stacked-interventions | 3.538161 | +0.153365 |

**Surprise Finding**: The local RTX 3090 run slightly outperformed the cloud 8×A100 baseline, suggesting that hardware differences (memory bandwidth, thermal throttling, or non-determinism) can produce meaningful variation even with identical code and data.

#### Stacked Interventions

The series systematically tested and combined:
1. **Gradient clipping** (max norm 3.5) — stabilizes training
2. **Learning rate scheduling** (0.0014 → 5% warmup → cosine decay to 0.00014) — better convergence
3. **Weight decay** (0.01) — regularization
4. **Dropout removal** — reduces noise in final training phase
5. **QKV bias** — attention mechanism refinement (excluded from final stack due to negative impact)

### Key Themes

- **Practical Deep Learning**: Focus on what works in real training scenarios, not just theory
- **Consumer Hardware Accessibility**: Democratizing LLM training by showing what's possible on a single GPU
- **Empirical Rigor**: Every intervention is measured against baselines with exact loss numbers
- **Open Documentation**: All code, configurations, and results are shared publicly

## Writing Style

Giles writes in a highly technical, experiment-driven style. Each post is structured as a scientific investigation:
1. State the hypothesis or problem
2. Describe the implementation
3. Present quantitative results (loss curves, timing data)
4. Analyze surprises and discrepancies
5. Document lessons learned for future experiments

This approach makes his series valuable for both learning deep learning fundamentals and understanding practical training optimization.

- [LLM from Scratch Part 32l — Interventions: Updated Instruction Fine-Tuning Results](https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests) (2026-04-22) — Technical deep-dive on interventions (updating instruction fine-tuning results). Key insight: test set loss doesn't necessarily reflect real-world utility.

## Related

- [[concepts/llm-training-fundamentals]] — Core concepts of training language models
-  — Technique for simulating large batch sizes
-  — DDP and multi-GPU training patterns
-  — Running LLM training on consumer hardware
- [[geohot-github-io]] — Another advocate for accessible, minimal deep learning (tinygrad)

## Sources

- [Giles' Blog](https://www.gilesthomas.com/)
- [Writing an LLM from scratch, part 32k](https://www.gilesthomas.com/2026/04/llm-from-scratch-32k-interventions-training-our-best-model-locally-gradient-accumulation)
