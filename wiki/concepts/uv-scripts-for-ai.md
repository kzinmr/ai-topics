---
title: "uv-scripts-for-ai — Self-Contained UV Scripts for AI/ML"
type: concept
created: 2026-06-07
updated: 2026-06-07
tags:
  - tool
  - open-source
  - huggingface
  - vlm
  - inference
sources:
  - https://github.com/davanstrien/uv-scripts-for-ai
  - https://x.com/vanstriendaniel/status/2062931483103252718
aliases:
  - uv-scripts-for-ai
---

# uv-scripts-for-ai

**uv-scripts-for-ai** is a repository of self-contained [[concepts/pep-723|PEP 723]] UV scripts for data and ML tasks, created by [[entities/daniel-van-strien|Daniel van Strien]]. Each script is a single Python file that declares its own dependencies inline — a portable unit runnable with `uv run` locally or `hf jobs uv run` on Hugging Face Jobs for managed GPU execution.

**GitHub:** 43 stars, 3 forks (June 2026)

## Design Philosophy

A **UV script** is a normal Python file with a PEP 723 metadata block at the top listing its dependencies. This makes each script:

- **Discrete & single-purpose** — one script, one job (from a 2-second transform to a multi-hour fine-tune)
- **Self-describing** — dependencies, docstring, and `--help` tell you what it needs and how to call it
- **Reproducible** — dependencies pinned *in the file*, no environment drift
- **Composable** — recipes hand off through the Hugging Face Hub (dataset in, dataset/model out)
- **Portable** — run with `uv run` where you have hardware, or `hf jobs uv run` on managed GPUs
- **Agent-ready** — every recipe takes `input output` args and runs from a URL; ships a ready-to-use agent skill

## Recipe Categories

| Domain | Description | Models/Tools |
|--------|-------------|-------------|
| **OCR** ⭐ | Document → text & structured data | GLM, PaddleOCR-VL, Nanonets, olmOCR, dots, and 30+ more models |
| **Vision** | Zero-shot detection & segmentation | SAM3, object detection, VLM object detection |
| **Audio** | Transcription & speech translation | Whisper variants, speech translation models |
| **Embeddings & Atlas** | Embed datasets; build interactive maps | Various embedding models |
| **Data Processing** | Filter, dedup, stats over large datasets | Polars-based, dataset-stats, deduplication |
| **Dataset Creation** | Turn PDFs/image URLs into Hub datasets | PDF extraction, IIIF tiles |
| **Synthetic Data** | Generate datasets with LLMs | Various LLM backends |
| **Inference** | Run open LLM/VLM over a dataset | vLLM, OpenAI-compatible, Transformers |
| **Entity Extraction** | NER / structured extraction | GLiNER |
| **Training** | Fine-tuning with TRL/Transformers | TRL, Transformers (migrating) |

## Quickstart

```bash
# Install uv (the only prerequisite)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run OCR on a dataset using managed GPU
hf jobs uv run --flavor l4x1 --secrets HF_TOKEN \
  https://huggingface.co/datasets/uv-scripts/ocr/raw/main/glm-ocr.py \
  davanstrien/ufo-ColPali your-username/ufo-ocr

# Or run locally
uv run https://huggingface.co/datasets/uv-scripts/ocr/raw/main/glm-ocr.py --help
```

## Agent Integration

The repository ships a ready-to-use **[`uv-recipes` agent skill](https://github.com/davanstrien/uv-scripts-for-ai/tree/main/skills/uv-recipes)** that enables AI agents to discover, run, and adapt recipes. Hugging Face also provides an [`hf` CLI skill for agents](https://huggingface.co/docs/hub/agents-cli) for driving Jobs from an editor.

On Jobs, the agent runs in a sandbox: throwaway disk, access limited to the token's repo permissions, and a cost cap per job — not arbitrary code on your machine.

## See Also

- [[concepts/uv]] — The uv Python package manager by Astral
- [[concepts/pep-723]] — Inline script metadata standard
- [[concepts/huggingface-jobs]] — HF Jobs managed GPU infrastructure
- [[concepts/polars-hf]] — Companion IO plugin for HF Buckets
- [[entities/daniel-van-strien]] — Author and ML Librarian at Hugging Face
- [[entities/_index]]
