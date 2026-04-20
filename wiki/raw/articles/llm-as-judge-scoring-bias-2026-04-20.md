---
title: "Evaluating Scoring Bias in LLM-as-a-Judge"
source_type: paper
url: https://arxiv.org/html/2506.22316v4
authors: "Qingquan Li, Shaoyu Dou, Kailai Shao, Chao Chen, Haixiang Hu"
venue: arXiv 2506.22316v4
published: 2025-06
created: 2026-04-20
tag: llm-evaluation
---

# Evaluating Scoring Bias in LLM-as-a-Judge

**Paper:** Evaluating Scoring Bias in LLM-as-a-Judge
**Authors:** Qingquan Li, Shaoyu Dou, Kailai Shao, Chao Chen, Haixiang Hu (Ant Group)
**Venue:** arXiv:2506.22316v4
**Dataset:** https://github.com/KMdsy/scoring_bias/

## Overview

First dedicated examination of **scoring bias** in LLM-as-a-Judge systems. Unlike prior work on comparative (pairwise) evaluations, this addresses **scoring-based evaluations** (absolute scores), which are more practical in industrial settings.

**Scoring bias** = measurable scoring shifts when the scoring prompt is perturbed.

## Three Novel Scoring Biases Identified

### 1. Rubric Order Bias
Order of score descriptions within the rubric affects judgments:
- **Ascending-Numeric:** Score 1 → 5 (conventional)
- **Descending-Numeric:** Score 5 → 1
- **Random-Numeric:** Random order

### 2. Score ID Bias
Different representations of score values influence judgments:
- Arabic numerals: `{1, 2, 3, 4, 5}`
- Letter-grades: `{E, D, C, B, A}`
- Roman numerals: `{i, ii, iii, iv, v}`

### 3. Reference Answer Score Bias
Attaching a specific score `k` to reference answers (Ref-k) impacts scoring robustness:
- Ref-5 (full marks) = highest accuracy, most stable
- Ref-1 to Ref-4 = unstable, distorting

## Key Experimental Results

### Reference Answer Bias Is Most Dangerous
| Model | Perturbation | Flip Rate | MAD |
|-------|--------------|-----------|-----|
| GPT-4o | Ref-5 | **45.54%** | **0.5604** |
| Qwen3-8B | Descending-Numeric | **46.22%** | **0.5296** |

Nearly half of scores corrupted when reference answer has score-5 attached.

### Powerful Models More Robust
- GPT-4o: FRs < 25%, MADs < 0.3 (except Ref-5)
- Qwen3-8B: FRs up to 46.22% under simple rubric reordering

## Key Findings

1. **More powerful models are more robust** — use GPT-4o-class for high-stakes
2. **Bias can have positive effects** — Roman numerals improve GPT-4o accuracy
3. **Models have inherent scoring tendencies:**
   - DeepSeek-V3-671B: Prefers score 5 (>50%)
   - GPT-4o/Mistral: Prefers score 4
4. **Descending rubric order often better than ascending**

## Mitigation Strategies

1. **Use stronger models** for high-stakes evaluations
2. **Use descending rubric order** (not ascending)
3. **Consider letter grades or Roman numerals** for score IDs
4. **Use full-mark (score 5) reference answers** when using references
5. **Avoid** random rubric ordering, score 1-4 reference answers

## Practical Recommendations

| Scenario | Recommendation |
|----------|----------------|
| High-stakes evaluation | GPT-4o or equivalent |
| Standard evaluation | Descending rubric order |
| Using reference answers | Always score-5 (full-mark) |
| Avoid | Random ordering, low-scored references |

## Broader LLM-as-Judge Best Practices (from other sources)

1. **Ditch the 1-10 scale** — use binary or small discrete scales
2. **Start with human labels** — don't evaluate in a vacuum
3. **Choose judge model carefully** — bigger is usually better
4. **Write explicit rubrics** — crisp criteria reduce ambiguity
5. **Prefer decision-based checks** — DAG/QAG more stable than free-form scoring
6. **Use ensembles** — multiple judges improve robustness
7. **Validate against human baselines** — before deploying