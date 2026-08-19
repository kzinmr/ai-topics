---
title: "Daniel van Strien — British Library book image dataset + cheap crop-tightening model + semantic search Space"
date: 2026-08-19
date_ingested: 2026-08-19
source: https://x.com/vanstriendaniel/status/2090146990759858401
author: Daniel van Strien (@vanstriendaniel)
type: x_post
tags:
  - person
  - huggingface
  - datasets
  - vlm
  - image-generation
  - open-source
  - gl
related:
  - entities/daniel-van-strien
  - concepts/ai-patterns-for-glam
---

# Daniel van Strien — 1M British Library book images: crop-tightening model, weak-label distillation, semantic search (X posts, Aug 18–19 2026)

## Posts

1. **Aug 18 2026** (reply, https://x.com/vanstriendaniel/status/2089731501147480307):
   > Masks are the crop_masks config: https://huggingface.co/datasets/biglam/british-library-book-images/viewer/crop_masks
   > Model + training data: https://huggingface.co/small-models-for-glam/bl-crop-tighten-rfdetrseg-clip10
   > The whole run was distilled from weak labels — no human annotations anywhere, and the full 1M-image corpus cost $3.24 of GPU.

2. **Aug 19 2026** (quoted, https://x.com/vanstriendaniel/status/2090146990759858401):
   > You can do semantic search across these images and get clean cutouts here: https://huggingface.co/spaces/davanstrien/bl-images-search
   > A search result for "mount everest" (with images)

3. **Aug 19 2026** (short reply, https://x.com/vanstriendaniel/status/2090097084661727699):
   > via https://huggingface.co/datasets/biglam/british-library-book-images

## What's in it

- **Dataset**: `biglam/british-library-book-images` — 1M British Library book (page/illustration) images, public domain. HF card tags: `image`, `digital-humanities-research`, `glam`, `book-illustration`. 2,428 downloads / 45 likes as of Aug 19 2026. Includes a `crop_masks` config with pre-computed object masks.
- **Model**: `small-models-for-glam/bl-crop-tighten-rfdetrseg-clip10` — an RF-DETR-based segmentation model ("crop tighten") to auto-crop images down to the object of interest. Trained by **distillation from weak labels — zero human annotations**; full 1M-image corpus processed for **$3.24 of GPU**.
- **Search Space**: `davanstrien/bl-images-search` — "Search 1M British Library book images by description" — semantic (text-to-image) search across the corpus, returning clean cutouts (thumbnails with titles/years), e.g. query "mount everest".

## Significance

Direct continuation of Daniel's GLAM-AI work (British Library Living with Machines background, [[concepts/ai-patterns-for-glam]]). Demonstrates his cost-efficiency thesis at corpus scale: sub-$5 GPU spend to process a 1M-image collection, end-to-end with no human labels — the kind of "efficient, accessible ML" pattern he advocates for libraries/archives/museums. The `small-models-for-glam` org suggests an ongoing series of GLAM-oriented small models.

## Sources

- https://x.com/vanstriendaniel/status/2089731501147480307
- https://x.com/vanstriendaniel/status/2090146990759858401
- https://x.com/vanstriendaniel/status/2090097084661727699
- https://huggingface.co/datasets/biglam/british-library-book-images
- https://huggingface.co/small-models-for-glam/bl-crop-tighten-rfdetrseg-clip10
- https://huggingface.co/spaces/davanstrien/bl-images-search
