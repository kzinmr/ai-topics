---
title: "Kimi K3 - How to Run Locally | Unsloth Documentation"
source: "https://unsloth.ai/docs/models/kimi-k3"
date: 2026-07-29
scraped: 2026-07-30
type: guide
---

# Kimi K3 - How to Run Locally

Kimi K3 by Moonshot AI is a 2.8T parameter open-weight model (104B active) built for SOTA coding, agentic, long-context, and chat workloads. It is the **strongest open model** to date, rivaling Claude 4.8 Opus and GPT-5.6. Kimi K3 has native vision, a 1M-token context window and uses MXFP4. Full-precision inference requires 1.56 TB of storage and 1-bit Kimi K3 Unsloth Dynamic GGUF requires **594 GB (62% less)**.

Dynamic 1-bit reaches **~78.9%** top-1 accuracy while being **62% smaller**. Dynamic 2-bit 861.3GB reaches **~90%** accuracy while being **45% smaller**. Run Kimi-K3-GGUF via Unsloth Studio or llama.cpp. Kimi K3 can run on a NVIDIA DGX Station or Mac Studio connected to a 128GB RAM device.

For **lossless** Kimi K3, use Q8 (UD-Q8_K_XL), which is **50GB larger** than Q4 (UD-Q4_K_XL).

**Table: Hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

| Dynamic 1-bit S | Dynamic 1-bit M | Dynamic 2-bit XXS | Dynamic 2-bit XL | Q8 (Lossless) |
| --------------- | --------------- | ----------------- | ---------------- | ------------- |
| 610 GB          | 665 GB          | 726 GB            | 880 GB           | 1.6 TB        |

## Kimi K3 GGUF Implementation Details

Built on top of llama.cpp PR with Unsloth fork which includes vision support and some bug fixes.

1. The mmproj / vision tower is similar to the Kimi-K2.5 tower, but with RMSNorm, no biases, a non-square fused QKV (qkv width != n_embd) and a post-norm projector.
2. When running llama.cpp, the n_tokens * 40 budget failed at large batch sizes, so had to up to n_tokens * 160
3. Had to convert the Kimi chat template to a jinja format.
4. Kimi by default has been trained with **preserved thinking on**, so all thinking traces are kept.

## Quantization Analysis

Like Kimi K2.6 and K2.7, K3's UD-Q8_K_XL is lossless because Kimi uses MXFP4 for MoE weights and BF16 for everything else, and Q8_K_XL follows that exactly. UD-Q4_K_XL is similar except some remaining tensors (except norms etc) are Q8_0, so it is near full precision and requires 1.56 TB RAM/VRAM.

| Quant | GB | mean KLD | PPL(q) | top-1 agree % | RMS dp % |
|-------|-----|----------|--------|---------------|----------|
| UD-IQ1_S | 594.0 | 0.5645 | 2.5789 | 78.875 +/- 0.107 | 36.495 |
| UD-IQ1_M | 648.9 | 0.4789 | 2.3639 | 81.219 +/- 0.103 | 33.629 |
| UD-IQ2_XXS | 711.1 | 0.3784 | 2.1266 | 84.127 +/- 0.096 | 29.826 |
| UD-Q2_K_XL | 861.3 | 0.1779 | 1.7359 | 90.390 +/- 0.077 | 19.862 |
| UD-Q4_K_XL | 1,510 | - | 1.4579 | - | - |
| UD-Q8_K_XL | 1,560 | - | 1.4581 | - | - |

Dynamic-1bit quant reaches 2.58 perplexity with 79% top-1 accuracy. Community quants are larger yet degrade far more — a 618.9 GB IQ1_M quant had 54.56 perplexity (21× worse). IQ2_XXS at 725 GB had 96 PPL vs Unsloth's 711 GB at 2.12 PPL (45× worse).

## Usage Guide

Kimi K3 is **thinking-only**, with `preserve_thinking` always enabled and max thinking on by default. Instant mode is not supported. Thinking effort: "low", "high", "max".

| Default | Agentic |
|---------|---------|
| temperature = 1.0 | temperature = 1.0 |
| top_p = 0.95 | top_p = 1.0 |

- Context length = up to 1,048,576
- Low, High, Max Thinking togglable in Unsloth
- ~20 tokens/s generation on B200s, >120 tokens/s throughput
- Recommended: UD-IQ1_S (594GB) for best size/quality balance
- Rule of thumb: RAM+VRAM ≈ the quant size

## Run in Unsloth Studio

Unsloth Studio is an open-source web UI for local AI. Automatically offloads to RAM and detects multiGPU setups. Runs on MacOS, Windows, Linux.

Features: search/download/run GGUFs and safetensor models, self-healing tool calling + web search, code execution (Python, Bash), automatic inference parameter tuning, fast CPU + GPU inference via llama.cpp, train LLMs 2x faster with 70% less VRAM.

Install: `curl -fsSL https://unsloth.ai/install.sh | sh` (MacOS/Linux/WSL) or `irm https://unsloth.ai/install.ps1 | iex` (Windows). Launch: `unsloth studio`. Secure HTTPS via Cloudflare tunnel: `unsloth studio --secure`.

## Run in llama.cpp

Requires Unsloth's custom fork of llama.cpp for Kimi K3 vision support (built on llama.cpp PR #26185). Build instructions for CUDA, Metal, CPU inference provided.

Download model manually: `hf download unsloth/Kimi-K3-GGUF --local-dir unsloth/Kimi-K3-GGUF --include "*mmproj-BF16*" --include "*UD-IQ1_S*"`

## Benchmarks

| Benchmark | Kimi K3 (max) | Claude Fable 5 (max) | GPT-5.6 Sol (max) | Claude Opus 4.8 (max) | GPT-5.5 (xhigh) | GLM-5.2 (max) |
|-----------|-------------|---------------------|-------------------|----------------------|-----------------|---------------|
| GPQA Diamond | 93.5 | 92.6 | **94.1** | 91.0 | 93.5 | 91.2 |
| HLE-Full | 43.5 / 56.0 | **53.3 / 63.0** | 44.5 / 58.0 | 49.8 / 57.9 | 41.4 / 52.2 | — |
| DeepSWE | 67.5 | 70.0 | **73.0** | 59.0 | 67.0 | 46.2 |
| Terminal-Bench 2.1 | 88.3 | 88.0 | **88.8** | 84.6 | 83.4 | 82.7 |
| BrowseComp | **91.2** | 88.0 | 90.4 | 84.3 | 84.4 | — |
| GDPval-AA v2 (Elo) | 1686 | **1747** | 1736 | 1593 | 1491 | 1510 |
| OSWorld 2.0 | 58.3 | **66.1** | 62.6 | 55.7 | 49.5 | — |
| MMMU-Pro | 81.6 / 83.4 | 81.2 / **86.5** | **83.0** / 84.6 | 78.9 / 82.7 | 81.2 / 83.2 | — |
| MathVision | 94.3 / 97.8 | 94.8 / **98.6** | **95.8** / 97.8 | 86.7 / 97.1 | 92.2 / 96.8 | — |

GGUF: https://huggingface.co/unsloth/Kimi-K3-GGUF
