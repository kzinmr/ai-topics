---
title: "pxpipe: Reduce Fable Costs 60% by Converting Code to Images"
url: "https://github.com/teamchong/pxpipe"
date: 2026-07-03
date_ingested: 2026-07-05
source: "github/teamchong"
type: article
authors: ["teamchong"]
tags: [article, raw, vision, multimodal, cost-optimization, image, ocr, open-source, ai-coding]
---

# pxpipe: Reduce Fable Costs 60% by Converting Code to Images

Source: https://github.com/teamchong/pxpipe

## Overview

pxpipe is a local proxy that reduces Claude Code API costs by rendering bulky text context (system prompts, tool docs, collapsed history) as compact PNG images instead of sending them as expensive text tokens. The model reads the images via its vision encoder.

## How It Works

### The Cost Reduction Mechanism

An image's token cost is fixed by pixel dimensions, not text volume. A 1928×1928 PNG costs ~4,761 vision tokens but holds ~92,000 characters. Since dense Claude Code traffic runs ~1.91 chars/text-token vs ~19.3 chars/image-token, this yields roughly 10× token reduction on imaged content.

### Pipeline

1. Intercept `/v1/messages` requests
2. Profitability gate (calibrated on 391 production rows)
3. Wrap text at 1928px columns, pack ~92K chars/page
4. Render as PNG
5. Splice back into request
6. Forward to API
7. Parallel `count_tokens` probe measures the counterfactual cost

## Key Results

- **End-to-end bill reduction**: 59–70%
- **Fable 5 accuracy**: 100/100 on novel arithmetic at −38% tokens; 98/98 on gist recall; 18/18 on state tracking; 0/16 confabulation
- **SWE-bench Lite**: 10/10 both arms at −65% request size
- **SWE-bench Pro**: 14/19 ON vs 15/19 OFF at −60%; verdicts agree 18/19
- **Demo cost**: $6.06 (pxpipe) vs $42.21 (plain)
