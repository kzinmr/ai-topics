---
title: "BrainChop — portable brain segmentation on tinygrad"
type: concept
aliases:
  - brainchop
  - brainchop-cli
created: 2026-04-25
updated: 2026-11-21
tags:
  - open-source
  - medical-imaging
  - inference
  - tool
sources:
  - https://pypi.org/project/brainchop/
  - https://github.com/neuroneural/brainchop-cli
  - wiki/entities/spike.md
---

# BrainChop

**BrainChop** is a lightweight, portable brain-MRI segmentation tool written
in Python on top of [[concepts/tinygrad|tinygrad]], created by
[[entities/spike|Spike (Mike Doan)]]. Its pitch is "runs on pretty much
everything": no PyTorch/TensorFlow dependency, CPU/GPU/CUDA/WebGPU backends
inherited from tinygrad, distributed as a pure-Python PyPI package.

## Key Facts (verified via PyPI, 2026-11-21)

| Field | Value |
|-------|-------|
| Author | Mike Doan (Spike) — spikedoanz@gmail.com |
| License | MIT |
| Latest release | 0.2.5 (first releases 0.1.x in mid-2024) |
| Repo | `neuroneural/brainchop-cli` |
| Dependencies | numpy, tinygrad, niimath, requests, safetensors |

## Usage

```bash
# zero-install via uv
uvx brainchop --help

# segment a brain MRI
brainchop input.nii.gz -o output.nii.gz

# choose a model / skull-strip / BEAM-optimized inference
brainchop input.nii.gz -m subcortical --skull-strip --beam 2 -o out.nii.gz
```

Python API: `bc.load → bc.segment → bc.save`, plus `bc.optimize(model,
beam=N)` (BEAM block-emphasis attention masking-style optimization) and
`bc.export(model, dir)` for **WebGPU model export** — browser-side
segmentation.

## Why It Matters to This Wiki

- **Canonical tinygrad application**: BrainChop is the flagship real-world
  use case cited on [[concepts/tinygrad]] — proof that a minimalist DL
  framework can carry production-adjacent medical imaging workloads.
- **Spike's minimalism thesis in practice**: fits the
  [[entities/spike]]"from bits to intelligence" program — small, hackable,
  dependency-light ML stacks built from first principles.
- Model zoo includes subcortical segmentation, tissue segmentation
  (`tissue_fast`), and skull stripping; models shipped as `safetensors`.

## Related Pages

- [[entities/spike]] — creator (Mike Doan)
- [[concepts/tinygrad]] — underlying inference engine
- [[concepts/software-minimalism]] — small, hackable, dependency-light ML stacks
