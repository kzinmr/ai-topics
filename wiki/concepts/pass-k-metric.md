---
title: "pass^k"
type: concept
aliases:
  - pass-k
  - passk
  - pass^k metric
created: 2026-05-08
updated: 2026-05-08
tags:
  - benchmark
  - infrastructure
  - evaluation
related:
  - "[[concepts/ai-benchmarks/tau-bench]]"
  - "[[concepts/tau-squared-bench]]"
  - "[[concepts/tau-knowledge]]"
  - "[[concepts/tau-voice]]"
---

# pass^k

**pass^k** is a **reliability metric for agents** introduced in the τ-bench family. It executes the same task k times in independent trials and only considers it a "pass" if **all trials succeed**.

> While conventional pass@1 (single-trial success rate) captures "got lucky once," pass^k measures "**can do it consistently**."

## Definition

$$\text{pass}^k = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}\left[\bigwedge_{j=1}^{k} \text{success}_{i,j}\right]$$

Where:
- $N$: Number of tasks
- $k$: Number of trials per task
- $\text{success}_{i,j}$: Whether trial $j$ of task $i$ succeeded

## Why pass^k is Needed

Three problems invisible to pass@1:

| Problem | How it looks in pass@1 | How it looks in pass^k |
|------|------------------|------------------|
| **Non-determinism** | Invisible (single trial) | Manifests as failure |
| **Fragility** | Invisible | Fails on small environmental changes |
| **Tail Risk** | Buried in averages | Caught as consistency gaps |

### Example: τ-bench Retail

- GPT-4o pass@1: **~45%** (appears to succeed nearly half the time)
- GPT-4o pass^8: **<25%** (8 consecutive successes in less than a quarter of cases)

This gap (~45% vs <25%) reveals the fundamental vulnerability of agents: **they can succeed once, but not consistently.**

## Real-World Importance

The "consistency" that pass^k measures is critically important in production for the following reasons:

1. **User Trust**: An agent that occasionally fails won't be trusted
2. **Business Risk**: A single policy violation or erroneous transaction can cause legal and financial problems
3. **Scalability**: At millions of interactions, even low-probability failures occur frequently
4. **Regulatory Compliance**: In finance, healthcare, and law, consistency is a compliance requirement

## Choosing k

| k | What it measures | When to use |
|---|------------|---------|
| 1 | Basic capability | Research prototypes |
| 2-4 | Short-term reliability | Internal testing |
| 8 | Operational reliability | Pre-production evaluation |
| >8 | Strict guarantees | Regulated domains |

τ-bench adopts pass^8 as its primary metric. Succeeding on all 8 independent trials provides statistically significant evidence of reliability.

## Comparison with Other Reliability Metrics

| Metric | What it measures | Strengths | Weaknesses |
|------|---------|------|------|
| **pass@1** | Average success rate | Simple to compute | Does not measure consistency |
| **pass^k** | k consecutive success rate | Directly measures consistency | Higher evaluation cost for large k |
| **mean success rate** | Average across all trials | Shows overall capability | Hides variance |
| **std dev of success** | Variance in success rates | Quantifies dispersion | Hard to use as a threshold |

## Position in Shunyu Yao's Philosophical Framework

pass^k embodies the central thesis of Yao's "The Second Half" paper:

> "Evaluation will become more important than training."

pass^k is not just a metric — it is a **philosophy of evaluation**. The condition for a real-world trustworthy AI agent is not being able to do it once, but being able to **do it the same way, for anyone, at any time**.

## Implementation

In τ-bench, pass^k is computed by comparing database states:

1. Each task is annotated with a **ground-truth database state**
2. For each of k trials, compare the post-conversation DB state with the ground truth
3. pass^k = true only if DB states match across **all trials**

This method is efficient (no LLM-as-judge required) and highly faithful.

## Related Pages

- [[concepts/ai-benchmarks/tau-bench]] — The original benchmark where pass^k was introduced
- [[entities/shunyu-yao]] — Designer of τ-bench and pass^k
