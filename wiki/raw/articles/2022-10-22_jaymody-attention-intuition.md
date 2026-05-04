---
title: "An Intuition for Attention"
author: "Jay Mody"
url: "https://jaykmody.com/blog/attention-intuition/"
date: 2022-10-22
tags:
  - attention
  - transformer
  - intuition
  - educational
---

# An Intuition for Attention

Derivation of Scaled Dot-Product Attention.

## Core Problem: Key-Value Lookups
Attention = fuzzy dictionary lookup. Instead of exact match, take weighted sum of values based on similarity.

## Dot Product as Similarity
Word vectors where similar meanings cluster together. Dot product measures similarity.

## Derivation:
1. Compute similarity: QK^T
2. Normalize with softmax
3. Weighted sum with V

## Scaled Dot-Product Attention
```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

### Why scaling?
Large d_k → large dot products → softmax gradients vanish. Divide by sqrt(d_k) fixes this.

### Implementation:
```
def attention(Q, K, V):
    d_k = K.shape[-1]
    return softmax(Q @ K.T / np.sqrt(d_k)) @ V
```
