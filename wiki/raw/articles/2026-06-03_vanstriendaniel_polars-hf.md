# polars-hf — Read and Write Hugging Face Hub Buckets with Polars

**Source:** https://github.com/davanstrien/polars-hf
**Author:** Daniel van Strien (@vanstriendaniel / davanstrien)
**Date:** June 2026
**X Post:** https://x.com/vanstriendaniel/status/2062145387612270860

## Overview

polars-hf is a pure-Python IO plugin for Polars that enables reading and writing Hugging Face Hub Buckets (HF's S3 alternative for private and working data). Stock Polars already reads `hf://datasets/...` natively, but does not yet support `hf://buckets/...`. polars-hf fills this gap from the outside.

Status: **alpha, pre-release** (not on PyPI yet — install from git).

It returns a native `pl.scan_parquet` LazyFrame: bucket files are XET-backed, so `scan_bucket` follows the authenticated Hub redirect to a presigned URL and hands that to Polars. Polars' own Rust object store then does async, concurrent, range-read scans — so projection, predicate, and slice pushdown, streaming, and multi-file concurrency all work natively.

This may be a stopgap — native `hf://buckets/...` support is proposed upstream in Polars (pola-rs/polars#27611 for reads, pola-rs/polars#26909 for streaming sink).

**GitHub Stats:** 1 star, 0 forks, Python (as of June 2026)

## Key Features

- `scan_bucket(path)` — Returns a lazy LazyFrame from a bucket path
- `sink_bucket(df, path)` — Writes to a bucket, including partitioned writes
- Supports single files, globs, and full bucket/directory paths
- Works on Hugging Face Jobs via PEP 723 inline-dependency scripts
- Requires `polars>=1.40,<1.50` and `huggingface_hub>=1.12`
- No compiled extensions, no fork of Polars

## Author's Note (from X)

"You can already read @huggingface datasets directly in @DataPolars but not (yet!) from Buckets (HF's S3 alternative, great for private and working data). So I built a plugin to read + write Buckets straight from Polars."

## Related Projects

- [[uv-scripts-for-ai]] — Daniel's companion project of self-contained UV scripts for AI/ML tasks
- [[concepts/polars]] — The Polars DataFrame library
