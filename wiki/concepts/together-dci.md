---
title: "Together AI Dedicated Container Inference (DCI)"
type: concept
created: 2026-05-10
updated: 2026-06-03
tags:
  - inference
  - hardware
  - huggingface
  - infrastructure
  - developer-tooling
  - workflow
sources:
  - https://www.together.ai/blog/deploy-and-inference-any-model-from-huggingface
  - raw/articles/together.ai--blog-deploy-and-inference-any-model-from-huggingface--6d3cfbd9.md
---

# Together AI Dedicated Container Inference (DCI)

> "Agents open up work that used to be off-limits, not because it was technically impossible, but because it required niche expertise most of us didn't have. Containerization, inference server configs, model-specific environment setup: these are the kinds of tasks that used to demand either deep expertise or hours of self-education before you could even get started. Agents allow for an elegant way to bridge those pre-requisite knowledge gaps."
>
> — Together AI Blog, May 2026

## Overview

Together AI offers **Dedicated Container Inference (DCI)** — a private, GPU-backed environment for running any Hugging Face model. Unlike shared inference endpoints, DCI gives you a fully managed container where you bring the model and Together handles the infrastructure.

## Key Features

| Feature | Description |
|---------|-------------|
| **Any Model Support** | Deploy any model from Hugging Face — no waiting for managed endpoint support |
| **Private GPU Environment** | No shared resources, no fighting for compute capacity |
| **Fully Managed** | Together handles container orchestration, inference server setup, dependencies |
| **Pay-for-What-You-Use** | Cost model designed for experimentation without cluster management overhead |
| **Production-Grade** | Ready for immediate inference once deployed |

## Agent-Assisted Deployment Workflow

Together AI demonstrates how coding agents can bridge the expertise gap between "model exists on Hugging Face" and "model running in production":

### Step-by-Step Process

1. **Install the Together dedicated containers skill**:
   ```bash
   npx skills add togethercomputer/skills
   ```
   This pulls in the `together-dedicated-containers` skill, which gives the agent knowledge about Together's infrastructure configuration.

2. **Start agent session with single prompt**:
   ```
   I want to deploy this model on Together's dedicated containers https://huggingface.co/netflix/void-model
   ```

3. **Agent auto-generates complete setup**:
   - Pulls model details from Hugging Face
   - Figures out correct inference server configuration for the model architecture
   - Generates container config files
   - Produces complete, runnable setup

4. **Run inference**:
   ```bash
   tg beta jig submit --watch --payload '{
     "video_url": "https://...",
     "prompt": "Empty park bench with fallen leaves",
     ...
   }'
   ```

### Case Study: Netflix void-model

When Netflix released `void-model` (video object removal with physical interaction handling) on Hugging Face, Together's team went from "model dropped" to "running container" in a single agent session. The output lives at:
- `github.com/blainekasten/together-void-model-container`

**void-model capabilities**: Removes objects from videos along with all induced interactions — not just secondary effects like shadows/reflections, but physical interactions like objects falling when a person is removed.

## Inference API Pattern

Together's DCI uses **asynchronous inference**:

```json
{
  "model": "void-byoc",
  "request_id": "019dc0f3-3c73-7a3f-b4b6-87ad06091180",
  "status": "running",
  "claimed_at": "2026-04-24T19:24:19.447457Z",
  "created_at": "2026-04-24T19:24:19.444567Z",
  "done_at": null,
  "info": null,
  "inputs": {
    "prompt": "Empty park bench with fallen leaves on the ground",
    "video_url": "...",
    "quadmask_url": "...",
    "use_pass2": false
  },
  "outputs": null,
  "priority": 1
}
```

When complete, `outputs` includes a URL to the hosted result:
```bash
curl -L -O \
  https://api.together.ai/v1/storage/REQUEST_ID-output.mp4 \
  --header "Authorization: Bearer $TOGETHER_API_KEY"
```

## Why DCI Matters for AI Agents

The traditional workflow for deploying a new model involved:
1. Understanding model architecture requirements
2. Configuring inference server (vLLM, TGI, etc.)
3. Setting up container with correct dependencies
4. Managing GPU resources and scaling
5. Wiring up API endpoints

**With agent-assisted DCI**: All of this happens automatically from a single natural language prompt. The key insight from Together's team:

> "That's the unlock. Not speed. Access."

This represents a shift in how developers interact with ML infrastructure — agents bridge the expertise gap between wanting to try a model and actually running it in production.

## Related Concepts

- [[concepts/deepseek-v4-serving]] — Together's experience serving DeepSeek-V4 on B200 GPUs
- [[concepts/serving-llms-vllm]] — vLLM inference server (common backend for DCI)
- [[entities/together-ai]] — Together AI company profile
- [[concepts/agent-workflows]] — How coding agents automate infrastructure tasks

## References

- [Deploy and inference any model from HuggingFace](https://www.together.ai/blog/deploy-and-inference-any-model-from-huggingface) — Together AI Blog, May 2026
- [Serving DeepSeek-V4: why million-token context is an inference systems problem](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem) — Together AI Blog, May 2026
- [Together Dedicated Containers Skill](https://github.com/togethercomputer/skills) — GitHub repo
- [Netflix void-model](https://huggingface.co/netflix/void-model) — Hugging Face model page
