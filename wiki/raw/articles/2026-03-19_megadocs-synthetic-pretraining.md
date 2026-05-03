# Data-efficient pre-training by scaling synthetic megadocs

**Authors:** Konwoo Kim, Suhas Kotha, Yejin Choi, Tatsunori Hashimoto, Nick Haber, Percy Liang
**Date:** March 19, 2026
**Source:** arXiv:2603.18534
**Shared by:** @Grad62304977 on X (2026-05-02)

## Executive Summary

This research addresses the "data wall" in LLM pre-training — where compute availability outpaces the supply of high-quality web data. The authors propose a novel method of synthetic data augmentation called **"Megadocs."** By transforming short synthetic rephrases into long, structured documents, the researchers achieved significantly higher data efficiency and improved performance on long-context tasks compared to standard synthetic data methods.

## Key Findings

- **Data Efficiency Gains:** Pre-training on web data mixed with synthetic rephrases improves data efficiency by **1.48×** (at 32 rephrases per document)
- **Megadoc Superiority:** Using "Megadocs" (stitching or stretching documents) increases data efficiency further to **1.80×**
- **Scaling Advantage:** Performance gap between Megadocs and simple rephrasing widens as synthetic data volume increases
- **No Overfitting:** With optimal mixing and epoching, benchmark accuracy improves without overfitting

## Core Methodologies

### Synthetic Rephrasing
Generating multiple synthetic versions of existing web documents. Despite different distribution, synthetic data improves validation loss on real web data.

### The "Megadoc" Approach
1. **Stitching:** Concatenating multiple synthetic rephrases of the same original web document into a single, substantially longer document
2. **Stretching:** Inserting rationales or additional context into a document to expand its length and depth

### Benefits of Megadocs
- Specifically improve long-context loss relative to simple rephrasing
- Improve both i.i.d. loss and downstream benchmark performance

## Key Insights
- **Optimal Mixing:** Critical to ensuring synthetic data improves loss rather than causing divergence or overfitting
- **Compute vs. Data:** Megadocs scale better as compute approaches infinity
- **Distributional Shift:** Synthetic data helps validation loss on real web data despite different distribution

## Actionable Conclusions
- Structure synthetic data into longer formats (Megadocs) to maximize data efficiency
- Target ~32 synthetic generations per original document for ~1.8× efficiency boost
- Use Megadocs as targeted strategy for improving long-context capabilities

Source: https://arxiv.org/abs/2603.18534
