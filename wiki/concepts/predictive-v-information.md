---
title: 'Predictive \mathcal{V}-Information'
type: concept
aliases:
  - V-Information
  - Predictive V-Information
  - 予測的V-情報
  - Usable Information Under Computational Constraints
tags:
  - methodology
created: 2026-05-08
updated: 2026-05-08
sources:
  - "raw/papers/2020-02-25_2002.10689_predictive-v-information.md"
---
# Predictive $\\mathcal{V}$-Information

**Predictive $\\mathcal{V}$-Information** is an information-theoretic framework that explicitly accounts for the computational and modeling constraints of the observer. Proposed by Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stewart, and Stefano Ermon in 2020 as a variational extension of Shannon information theory, published at ICLR 2020[^1].

## Overview

Traditional Shannon information theory measures the **physical existence** of information. This assumes the observer has infinite computational power, making it insufficient for describing the behavior of real-world machine learning systems (e.g., neural networks).

Predictive $\\mathcal{V}$-Information quantifies "how much information is **usable** to a given observer" by restricting the observer's capabilities to a specific function class $\\mathcal{V}$.

| Perspective | Shannon Information | Predictive $\\mathcal{V}$-Information |
|----------|-------------|-------------------------------------|
| **Observer** | Omnipotent (infinite compute) | Constrained (function class $\\mathcal{V}$) |
| **Data Processing Inequality (DPI)** | Always holds (information cannot be created) | **Can be violated** (computation can create usable information) |
| **Symmetry** | Symmetric ($I(X;Y) = I(Y;X)$) | Asymmetric ($I_{\\mathcal{V}}(X \\to Y) \\neq I_{\\mathcal{V}}(Y \\to X)$) |
| **Estimation** | Difficult in high dimensions | Reliably estimable with PAC guarantees |
| **Use** | Theoretical communication limits | Practical machine learning and fairness |

## Definitions

### $\\mathcal{V}$-Entropy
The minimum expected loss (uncertainty) when predicting target variable $Y$ using models from function class $\\mathcal{V}$:

$$H_{\\mathcal{V}}(Y) = \\inf_{f \\in \\mathcal{V}} \\mathbb{E}[L(f, Y)]$$

### Conditional $\\mathcal{V}$-Entropy
The residual uncertainty in predicting $Y$ after observing input $X$, using models from function class $\\mathcal{V}$:

$$H_{\\mathcal{V}}(Y|X) = \\inf_{f \\in \\mathcal{V}} \\mathbb{E}[L(f(X), Y)]$$

### $\\mathcal{V}$-Information
Defined as the difference between the two:

$$I_{\\mathcal{V}}(X \\to Y) = H_{\\mathcal{V}}(Y) - H_{\\mathcal{V}}(Y|X)$$

## Theoretical Significance

### DPI (Data Processing Inequality) Violation

In Shannon theory, processing (transforming) data cannot increase information ($I(X;Y) \\ge I(g(X);Y)$). However, under $\\mathcal{V}$-Information, **computation can increase usable information**:

$$I_{\\mathcal{V}}(g(X) \\to Y) \\ge I_{\\mathcal{V}}(X \\to Y)$$

This explains how deep neural networks extract increasingly linearly separable and "usable" feature representations as they go deeper. Information that was inaccessible to observer $\\mathcal{V}$ in raw data becomes "usable" through appropriate transformation $g$.

### PAC-Style Estimation Guarantees

Shannon mutual information is extremely difficult to estimate for high-dimensional continuous variables. $\\mathcal{V}$-Information, by restricting the observer's function class, enables reliable estimation from finite data.

### Generalization of Existing Metrics

| Metric | Condition as Special Case |
|------|----------------------|
| **Shannon mutual information** | $\\mathcal{V}$ is the set of all measurable functions |
| **Coefficient of determination $R^2$** | $\\mathcal{V}$ is the set of linear models |

## Applications

### 1. Structure Learning

When learning dependencies between variables, can identify which dependencies a specific model class can actually exploit. Enables more realistic causal graph construction than traditional mutual information.

### 2. Fair Representation Learning

In fairness contexts, we want representation $Z$ to minimize information about sensitive attribute $S$. $\\mathcal{V}$-Information provides a realistic fairness guarantee: "information that a specific limited adversary cannot extract." Shannon information assumes an "omnipotent adversary," making it overly restrictive.

### 3. Deep Representation Learning

Theoretically explains the phenomenon where features become increasingly "linearly separable" through deeper layers of a network. While Shannon information stays constant or decreases through layers, $\\mathcal{V}$-Information formalizes why it increases.

## Comparison with Related Concepts

| Concept | Relationship |
|------|------|
| **Shannon information theory** | Parent theory. $\\mathcal{V}$-Information is a variational extension; when $\\mathcal{V}$ is all measurable functions, it reduces to Shannon mutual information |
| **Coefficient of determination $R^2$** | Special case of $\\mathcal{V}$-Information (restricted to linear model class) |
| **Information Bottleneck (IB)** | Related but different. IB addresses the compression-prediction trade-off; $\\mathcal{V}$-Information focuses on observer constraints |
| **Variational Information Theory** | Part of a broader framework. $\\mathcal{V}$-Information provides practical estimation of information using variational lower bounds |

## References

[^1]: Xu et al., "A Theory of Usable Information Under Computational Constraints", ICLR 2020. https://arxiv.org/abs/2002.10689

## See Also

- [[concepts/representation-learning]] — As a theoretical foundation for representation learning
