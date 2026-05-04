---
title: "Computing Distance Matrices with NumPy"
author: "Jay Mody"
url: "https://jaykmody.com/blog/distance-matrices-with-numpy/"
date: 2021-04-04
tags:
  - numpy
  - optimization
  - vectorization
  - knn
---

# Computing Distance Matrices with NumPy

Optimizing kNN distance computation from O(n^3) to O(n^2) using vectorization.

## Four Implementations (fastest to slowest):

### No Loops (0.22s on CIFAR-10 subset)
Expands Euclidean formula: (x-y)^2 = x^2 - 2xy + y^2
```
x2 = np.sum(X**2, axis=1).reshape(-1, 1)
y2 = np.sum(X_train**2, axis=1)
xy = np.matmul(X, X_train.T)
dists = np.sqrt(x2 - 2*xy + y2)
```

### Performance (5000 train, 500 test):
| Method | Time |
|--------|------|
| Three Loops | Hours (est.) |
| Two Loops | 39.71s |
| One Loop (broadcasting) | 28.71s |
| No Loops (vectorized) | 0.22s |

### Key Insight
BLAS-backed matrix multiplication is orders of magnitude faster than Python loops. For production, use sklearn.
