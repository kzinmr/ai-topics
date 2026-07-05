---
title: "polars-hf — HF Buckets IO Plugin for Polars"
type: concept
created: 2026-06-07
updated: 2026-06-07
tags:
  - data-science
  - huggingface
  - open-source
  - tool
  - plugins
sources:
  - https://github.com/davanstrien/polars-hf
  - https://x.com/vanstriendaniel/status/2062145387612270860
aliases:
  - polars-hf
---

# polars-hf

**polars-hf** is a pure-Python IO plugin for [[concepts/polars|Polars]] that enables reading from and writing to Hugging Face Hub Buckets — HF's S3-compatible storage alternative for private and working data. Created by [[entities/daniel-van-strien|Daniel van Strien]], it fills a gap in Polars' native Hugging Face integration.

## Overview

Stock Polars natively supports `hf://datasets/...` and `hf://spaces/...` URLs for reading data, but does not yet support `hf://buckets/...` — Hugging Face's S3 alternative for private and working data. polars-hf bridges this gap with a pure-Python plugin that requires no compiled extensions and no fork of Polars.

**Status:** alpha, pre-release (June 2026). Not on PyPI yet; installed from git via `uv add "polars-hf @ git+https://github.com/davanstrien/polars-hf"`.

## How It Works

Bucket files on Hugging Face Hub are XET-backed. `scan_bucket()` follows the authenticated Hub redirect to a presigned `cas-bridge.xethub.hf.co` URL and hands that to Polars. Polars' own Rust object store then performs async, concurrent, range-read scans — so projection, predicate, and slice pushdown, streaming, and multi-file concurrency all work natively.

This is the same mechanism upstream's `hf://` reader uses; the difference is that the signed URL is resolved in Python because stock Polars cannot attach a bearer token to a generic `https://` URL.

## API

```python
import polars as pl
import polars_hf as plhf

# Read from a bucket (returns LazyFrame):
lf = plhf.scan_bucket("hf://buckets/my-namespace/my-bucket/data/*.parquet")

# Supports single files, globs, and full directories:
df = lf.filter(pl.col("label") == 1).select("text", "label").head(100).collect()

# Write to a bucket (including partitioned writes):
plhf.sink_bucket(df, "hf://buckets/my-namespace/my-bucket/output/")
```

## Use on Hugging Face Jobs

With PEP 723 inline-dependency scripts, polars-hf runs on Hugging Face Jobs with zero local setup:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["polars-hf @ git+https://github.com/davanstrien/polars-hf@main"]
# ///
import polars as pl
import polars_hf as plhf
plhf.scan_bucket("hf://buckets/me/data/*.parquet").collect()
```

Run with: `hf jobs uv run --secrets HF_TOKEN --flavor cpu-upgrade my_script.py`

## Upstream Status

Native `hf://buckets/...` support is proposed for Polars upstream:
- [pola-rs/polars#27611](https://github.com/pola-rs/polars/issues/27611) — reads
- [pola-rs/polars#26909](https://github.com/pola-rs/polars/issues/26909) — streaming sink

If these land, polars-hf becomes redundant; until then, it fills the gap from the outside.

## Requirements

- `polars>=1.40,<1.50`
- `huggingface_hub>=1.12`

## See Also

- [[concepts/polars]] — The Polars DataFrame library
- [[concepts/uv-scripts-for-ai]] — Companion project of self-contained UV scripts for AI/ML
- [[entities/daniel-van-strien]] — Author and Machine Learning Librarian at Hugging Face
- [[concepts/huggingface-jobs]] — Managed GPU infrastructure for running scripts
- [[entities/_index]]
