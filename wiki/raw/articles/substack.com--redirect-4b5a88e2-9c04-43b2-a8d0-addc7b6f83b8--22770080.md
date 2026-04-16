---
title: "shreyansh26/FlashAttention-PyTorch: Implementation of FlashAttention (FA1-FA4) in PyTorch for educational and algorithmic clarity · GitHub"
url: "https://substack.com/redirect/4b5a88e2-9c04-43b2-a8d0-addc7b6f83b8?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-16T19:09:13.389277+00:00
source_date: 2026-04-16
tags: [newsletter, auto-ingested]
---

# shreyansh26/FlashAttention-PyTorch: Implementation of FlashAttention (FA1-FA4) in PyTorch for educational and algorithmic clarity · GitHub

Source: https://substack.com/redirect/4b5a88e2-9c04-43b2-a8d0-addc7b6f83b8?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

FlashAttention in PyTorch
This repository contains simplified educational implementations of FlashAttention versions 1 through 4. The goal is correctness and clarity, not CUDA-level performance. Each version keeps the same exact attention math while changing the orchestration so the algorithmic differences are visible in plain PyTorch.
torch>=2.8.0
triton>=3.4.0
flash_attention_core
- Shared package with reference attention, masking helpers, config/types, and versioned implementations.
flash_attention.py
- Unified forward demo for
fa1
through
fa4
.
bench.py
- Unified benchmark entry point with
--version
and
--causal
.
check_backward.py
- Unified forward and backward correctness check.
tests
- Small regression suite covering all versions.
Non-causal attention with an optional key-padding mask of shape
(batch, kv_len)
.
Causal attention via
--causal
.
fa1
- Baseline tiled online-softmax FlashAttention.
fa2
- Sequence-parallel / split-Q ownership with deferred normalization and LSE-centered state.
fa3
- Explicit staged pipeline with ping-pong tile buffers.
fa4
- Explicit scheduler, main/softmax/correction phases, and conditional rescaling.
Where the simplified code leaves out real CUDA behavior such as TMA, WGMMA, TMEM, FP8 paths, or multi-CTA coordination, the version modules call that out in comments.
python flash_attention.py
python flash_attention.py --version fa3 --causal --dump-state
python flash_attention.py --version fa3 --fp8 --dump-state
--fp8
is only implemented for
fa3
. It models the official FA3 FP8 forward
path with simplified per-tile block quantization metadata in regular PyTorch.
FP8 backward is intentionally unsupported, matching the released FA3 support
boundary.
python bench.py --type flash --version fa2 --b 1 --h 2 --q_len 4096 --kv_len 4096 --d 128
python bench.py --type normal --causal --b 1 --h 2 --q_len 4096 --kv_len 4096 --d 128
python bench.py --type flash --version fa3 --fp8 --b 1 --h 2 --q_len 4096 --kv_len 4096 --d 128
These implementations are intentionally simplified and educational rather than
performance-tuned kernels, so benchmark numbers should be taken with a grain of
salt.
bench.py
uses Triton's benchmark helper when running on CUDA and reports both
forward_ms
and
backward_ms
. For
--type flash
, the backward timing measures
the simplified manual backward implementation. For
--type normal
, the
backward timing measures PyTorch autograd on the reference attention path. For
fa3 --fp8
, only the forward timing is reported and backward is marked as
unsupported.
Add
--profile
to capture separate PyTorch profiler traces for the forward and
backward benchmark paths.
Forward and Backward Correctness
python check_backward.py
python check_backward.py --version fa4 --causal --q_len 256 --kv_len 256 --d 64
check_backward.py --version fa3 --fp8
is intentionally unsupported because
the educational FP8 mode only models the released FA3 forward path.
python -m unittest discover -s tests
python -m unittest tests.test_flash_attention_long
