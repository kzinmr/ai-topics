---
title: "TorchTPU — native PyTorch backend for Google TPUs"
url: https://github.com/google-pytorch/torch_tpu
source: github.com/google-pytorch
date: 2026-10-20
fetched_at: 2026-10-21
type: raw-article
tags: [pytorch, tpu, google, ai-infrastructure, distributed-training, open-source]
confidence: high
---

# TorchTPU: PyTorch backend for Google TPUs (Google, Oct 20 2026)

Source: https://github.com/google-pytorch/torch_tpu (README)
HN: https://news.ycombinator.com/item?id=... (346 pts, Oct 20 2026)

## Description
Provides a PyTorch backend for Google's Tensor Processing Units (TPUs), enabling users to run PyTorch models and operations on TPU devices. Includes custom ATen kernels for various PyTorch operations, a compilation cache for optimizing execution, and examples for distributed training and model inference.

## Features
- PyTorch ATen kernel implementation for TPU.
- Compilation cache for optimized execution of XLA computations.
- Support for distributed training (Data Parallelism, Tensor Parallelism).
- Examples for various models (Llama, Qwen, ResNet, DLRM, minGPT, UNet).
- Integration with `torch.compile()` for graph mode execution.
- Utilities for debugging and benchmarking.

## Positioning / significance
A **native** PyTorch-on-TPU backend — Google releasing a first-party ATen-kernel backend that lets PyTorch run directly on TPUs, with `torch.compile()` graph-mode integration and an XLA compilation cache. Lowers the barrier for running the dominant (CUDA-centric) PyTorch training/serving stack on Google silicon, and is part of Google's broader PyTorch-first strategy (vs the historical JAX/XLAndominance on TPU).

## User guide & notebooks
User guide at https://torchtpu.readthedocs.io/ (static version of interactive Marimo notebooks, run via `marimo edit file.py`; easiest on a TPU VM / v6e GCE instance).

## Installation
Python 3.11+ (matches PyTorch Release Compatibility Matrix). PyPI release 0.2.0:
```bash
pip install torch_tpu==0.2.0 --extra-index-url https://download.pytorch.org/whl/cpu
```
Build from source via Bazel: `bazel build --config=wheel_common //ci/wheel:torch_tpu_wheel` (RBE remote cache enabled by default; `--config=no_rbe` to strip).

## Notes
- Repo org: google-pytorch/torch_tpu. Examples cover Llama, Qwen (LLMs) plus ResNet/DLRM/minGPT/UNet.
- Related to prior torch_xla path; this is a dedicated ATen-kernel backend.
