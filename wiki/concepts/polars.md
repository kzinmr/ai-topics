---
title: "polars"
type: concept
aliases:
  - polars
created: 2026-04-25
updated: 2026-06-07
tags:
  - data-science
  - open-source
  - developer-tooling
sources:
  - https://pola.rs
  - https://github.com/davanstrien/polars-hf
---

# Polars

**Polars** is a high-performance DataFrame library for Python and Rust, designed for fast data processing on both single machines and distributed setups. It uses Apache Arrow as its memory model and provides a lazy query engine with automatic optimization, predicate/projection pushdown, and streaming execution.

## Overview

Polars offers two API modes: **eager** (immediate execution) and **lazy** (query optimization + deferred execution). The lazy API builds a query plan that is optimized before execution, enabling automatic predicate pushdown, projection pushdown, and slice pushdown — only the columns and rows actually needed are read from storage.

Polars natively supports reading from many sources including CSV, JSON, Parquet, Delta Lake, and cloud storage (S3, GCS, Azure). It has deep Hugging Face Hub integration: `pl.scan_parquet("hf://datasets/org/dataset/**/*.parquet")` works natively for Hub datasets.

## Hugging Face Ecosystem

### Native HF Support
Polars can read directly from Hugging Face Hub datasets and spaces via `hf://` URLs:
```python
import polars as pl
df = pl.scan_parquet("hf://datasets/username/dataset/*.parquet").collect()
```

### HF Buckets (via polars-hf)
HF Buckets are Hugging Face's S3-compatible storage for private and working data. Native Polars does not yet support `hf://buckets/...` URLs. **[[entities/daniel-van-strien|Daniel van Strien]]'s** [[concepts/polars-hf|polars-hf]] fills this gap as a pure-Python IO plugin, providing `scan_bucket()` and `sink_bucket()` functions that return native LazyFrames with full pushdown support.

Upstream support is proposed: [pola-rs/polars#27611](https://github.com/pola-rs/polars/issues/27611) (reads) and [pola-rs/polars#26909](https://github.com/pola-rs/polars/issues/26909) (streaming sink).

## Key Features

- **Lazy evaluation** with automatic query optimization
- **Predicate pushdown** — filters applied at the storage layer
- **Projection pushdown** — only needed columns are read
- **Streaming engine** — processes data larger than memory
- **Expression-based API** — composable, readable transformations
- **GroupBy and window functions** with high performance
- **Multi-file concurrent scanning** via Rust object store
- **IO plugin system** — extensible for custom storage backends (e.g., polars-hf for HF Buckets)

## See Also

- [[concepts/polars-hf]] — IO plugin for Hugging Face Hub Buckets
- [[concepts/uv-scripts-for-ai]] — UV scripts that leverage Polars for AI data processing
- [[entities/daniel-van-strien]] — Author of polars-hf and polars-related tooling
- [[entities/_index]]
