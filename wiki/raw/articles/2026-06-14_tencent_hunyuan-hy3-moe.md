---
title: "Tencent Hy3 Preview — 295B MoE Reasoning and Agent Model"
source_url: "https://github.com/Tencent-Hunyuan/Hy3-preview"
source_url_2: "https://huggingface.co/tencent/Hy3-preview"
date: 2026-06-13
source_type: model-release
language: en
tags:
  - model-release
  - moe
  - open-source
  - reasoning
  - coding-agent
  - context-learning
  - tencent
---

# Tencent Hy3 Preview (295B A21B MoE)

**Source**: [GitHub: Tencent-Hunyuan/Hy3-preview](https://github.com/Tencent-Hunyuan/Hy3-preview)
**HuggingFace**: [tencent/Hy3-preview](https://huggingface.co/tencent/Hy3-preview)
**Stars**: 375 | **Forks**: 18 | **Created**: 2026-04-21
**Architecture**: MoE, 295B total / 21B active, 192 experts top-8
**Context**: 256K | **License**: Tencent Hy Community License

---

<p align="left">
    <a href="README_CN.md">中文</a>&nbsp;｜&nbsp;English
</p>
<br>

<p align="center">
 <img src="assets/logo-en.png" width="400"/> <br>
</p>

<div align="center" style="line-height: 1;">


[![License](https://img.shields.io/badge/License-Tencent%20Hy%20Community-blue)](#license)
&nbsp;&nbsp;
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Tencent%20Hy-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/tencent/Hy3-preview)
&nbsp;&nbsp;
[![ModelScope](https://img.shields.io/badge/ModelScope-Tencent%20Hy-624aff)](https://modelscope.cn/models/Tencent-Hunyuan/Hy3-preview)
&nbsp;&nbsp;
[![cnb.cool](https://img.shields.io/badge/cnb.cool-Tencent%20Hy-blue?logoColor=white)](https://cnb.cool/ai-models/tencent/Hy3-preview)
&nbsp;&nbsp;
[![GitCode](https://img.shields.io/badge/GitCode-Tencent%20Hy-red?logoColor=white)](https://ai.gitcode.com/tencent_hunyuan/Hy3-preview)

</div>

<p align="center">
    🖥️&nbsp;<a href="https://aistudio.tencent.com/"><b>Official Website</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    💬&nbsp;<a href="https://github.com/Tencent-Hunyuan/Hy3-preview"><b>GitHub</b></a></p>

---

## Table of Contents

- [Model Introduction](#model-introduction)
- [Highlights](#highlights)
- [Benchmark Results](#benchmark-results)
  - [STEM & Reasoning](#stem--reasoning)
  - [Context Learning & Instruction Following](#context-learning--instruction-following)
  - [Code & Agent](#code--agent)
- [News](#news)
- [Model Links](#model-links)
- [Quickstart](#quickstart)
- [Deployment](#deployment)
  - [vLLM](#vllm)
  - [SGLang](#sglang)
- [Training](#training)
- [Quantization](#quantization)
- [License](#license)
- [Contact Us](#contact-us)

---

## Model Introduction

**Hy3 preview** is a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and 3.8B MTP layer parameters, developed by the Tencent Hy Team. Hy3 preview is the first model trained on our rebuilt infrastructure, and the strongest we've shipped so far. It improves significantly on complex reasoning, instruction following, context learning, coding, and agent tasks.


| Property | Value |
|:---|:---|
| Architecture | Mixture-of-Experts (MoE) |
| Total Parameters | 295B |
| Activated Parameters | 21B |
| MTP Layer Parameters | 3.8B |
| Number of Layers (excluding MTP layer) | 80 |
| Number of MTP Layers | 1 |
| Attention Heads | 64 (GQA, 8 KV heads, head dim 128) |
| Hidden Size | 4096 |
| Intermediate Size | 13312 |
| Context Length | 256K |
| Vocabulary Size | 120832 |
| Number of Experts | 192 experts, top-8 activated |
| Supported Precisions | BF16 |

## Highlights

- **STEM & Reasoning** — Complex reasoning underpins everything else. Hy3 preview performs well on challenging STEM benchmarks like FrontierScience-Olympiad and IMOAnswerBench, and achieved excellent results in the Tsinghua Qiuzhen College Math PhD qualifying exam (Spring '26) and the China High School Biology Olympiad (CHSBO 2025), demonstrating generalizable reasoning capacity.

- **Context Learning & Instruction Following** — Real-world tasks require the ability to parse messy, lengthy contexts and follow complex rules. We built CL-bench and CL-bench-Life from our own business scenarios to innovatively measure context learning ability. Hy3 preview exhibits solid gains in both context learning and instruction following capabilities.

- **Code & Agent** — Coding and agents saw the biggest gains. With a rebuilt RL infrastructure and larger-scale training tasks, we posted competitive scores across mainstream coding agent benchmarks (SWE-bench Verified, Terminal-Bench 2.0) and search agent benchmarks (BrowseComp, WideSearch).

## Benchmark Results

### Pre-trained Model Performance

| Category | Benchmark (Metric) | # Shots | Kimi-K2 BASE | DeepSeek-V3 BASE | GLM-4.5 BASE | Hy3 preview-Base |
|---|---|---|---|---|---|---|
| | #ActivatedParams | - | 32B | 37B | 32B | 21B |
| | #TotalParams | - | 1043B | 671B | 355B | 295B |
| **English** | MMLU | 5-shot | **88.24** | 87.68 | 87.73 | 87.42 |
| | MMLU-Pro | 5-shot | **65.98** | 63.98 | 63.67 | 65.76 |
| | MMLU-Redux | 5-shot | **87.18** | 86.81 | 86.56 | 86.86 |
| | ARC-Challenge | 0-shot | **96.66** | 94.65 | 96.32 | 95.99 |
| | DROP | 5-shot | 86.40 | **86.50** | 82.90 | 85.50 |
| | PIQA | 4-shot | **84.93** | 84.22 | 84.71 | 84.39 |
| | SuperGPQA | 5-shot | 51.10 | 46.17 | 49.64 | **51.60** |
| | SimpleQA | 5-shot | **34.37** | 26.15 | 29.26 | 26.47 |
| **Code** | MBPP-plus | 3-shot | **81.35** | 75.47 | 78.05 | 78.71 |
| | CRUXEval-I | 3-shot | 68.01 | 67.79 | 68.51 | **71.19** |
| | CRUXEval-O | 3-shot | 69.62 | **71.00** | 67.75 | 68.38 |
| | LiveCodeBench-v6 | 1-shot | 30.86 | 29.31 | 27.43 | **34.86** |
| **Math** | GSM8K | 4-shot | 93.46 | 88.15 | 90.06 | **95.37** |
| | MATH | 4-shot | 71.20 | 59.37 | 61.00 | **76.28** |
| | CMath | 4-shot | 90.83 | 85.50 | 89.33 | **91.17** |
| **Chinese** | C-Eval | 5-shot | **91.51** | 90.35 | 85.84 | 89.80 |
| | CMMLU | 5-shot | **90.72** | 87.90 | 86.46 | 89.61 |
| | Chinese-simpleQA | 5-shot | **74.58** | 68.72 | 68.49 | 69.73 |
| **Multilingual** | MMMLU | 5-shot | 77.63 | 79.54 | 79.26 | **80.15** |
| | INCLUDE | 5-shot | 75.66 | 77.86 | 76.27 | **78.64** |

### Instruct Model Performance

#### STEM & Reasoning

Complex reasoning underpins everything else. Hy3 preview performs well on challenging STEM benchmarks like FrontierScience-Olympiad and IMOAnswerBench. It also achieved excellent results in the Tsinghua Qiuzhen College Math PhD qualifying exam (Spring '26) and the China High School Biology Olympiad (CHSBO 2025), demonstrating a high degree of generalizable reasoning capacity.

<p align="center"><img src="assets/bench_stem.jpg" width="800" alt="STEM & Reasoning benchmarks"/></p>

#### Context Learning & Instruction Following

Real-world tasks require the ability to parse messy, lengthy contexts and follow complex rules. We built CL-bench and CL-bench-Life from our own business scenarios to innovatively measure context learning ability. Hy3 preview exhibits solid gains in both context learning and instruction following capabilities.

<p align="center"><img src="assets/bench_context.jpg" width="800" alt="Context Learning & Instruction Following benchmarks"/></p>

#### Code & Agent

Coding and agents saw the biggest gains. With a rebuilt RL infrastructure and larger-scale training tasks, we posted competitive scores across mainstream coding agent benchmarks (SWE-bench Verified, Terminal-Bench 2.0) and search agent benchmarks (BrowseComp, WideSearch).

<p align="center"><img src="assets/bench_agent_overview_v3.jpg" width="800" alt="Agent benchmarks overview"/></p>

Coding is about whether a model can execute in a development environment. Search is about whether it can find and combine information from the open web. Both matter for complex agent scenarios like OpenClaw. Hy3 preview scores well on ClawEval and WildClawBench — a sign that its agent capabilities are becoming practical.

<p align="center"><img src="assets/bench_claw_agent.png" width="800" alt="Claw Agent benchmarks"/></p>

Beyond public benchmarks, we built internal evaluation sets to test the model in real development scenarios. On Hy-Backend (backend-focused tasks), Hy-Vibe Bench (real-user dev workflows), and Hy-SWE Max, Hy3 preview scores competitively against other open-source models.

<p align="center"><img src="assets/bench_claw_agent2.jpg" width="800" alt="Internal benchmarks"/></p>

## News


* **[2026-04-23]** 🔥 We open-source **Hy3 preview** model weights on [Hugging Face](https://huggingface.co/tencent/Hy3-preview), [ModelScope](https://modelscope.cn/models/Tencent-Hunyuan/Hy3-preview), and [GitCode](https://ai.gitcode.com/tencent_hunyuan/Hy3-preview).

## Model Links


| Model Name | Description | Hugging Face | ModelScope | GitCode |
|:---|:---|:---:|:---:|:---:|
| Hy3 preview | Instruct model | 🤗 [Model](https://huggingface.co/tencent/Hy3-preview) | [Model](https://modelscope.cn/models/Tencent-Hunyuan/Hy3-preview) | [Model](https://ai.gitcode.com/tencent_hunyuan/Hy3-preview) |
| Hy3 preview-Base | Pre-trained base model | 🤗 [Model](https://huggingface.co/tencent/Hy3-preview-Base) | [Model](https://modelscope.cn/models/Tencent-Hunyuan/Hy3-preview-Base) | [Model](https://ai.gitcode.com/tencent_hunyuan/Hy3-preview-Base) |

## Quickstart

Deploy Hy3 preview with [vLLM](#vllm) or [SGLang](#sglang) first, then call the OpenAI-compatible API:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="hy3-preview",
    messages=[
        {"role": "user", "content": "Hello! Can you briefly introduce yourself?"},
    ],
    temperature=0.9,
    top_p=1.0,
    # reasoning_effort: "no_think" (default, direct response), "low", "high" (deep chain-of-thought)
    extra_body={"chat_template_kwargs": {"reasoning_effort": "no_think"}},
)
print(response.choices[0].message.content)
```

> **Recommended parameters**: `temperature=0.9`, `top_p=1.0`.
>
> **Reasoning mode**: Set `reasoning_effort` to `"high"` for complex tasks (math, coding, reasoning) or `"no_think"` for direct responses.

See the [Deployment](#deployment) section below for how to start the API server.

## Deployment

Hy3-preview has 295B parameters in total. To serve it on 8 GPUs, we recommend using H20-3e or other GPUs with larger memory capacity.

### vLLM

Build vLLM from source:
```bash
uv venv --python 3.12 --seed --managed-python
source .venv/bin/activate
git clone https://github.com/vllm-project/vllm.git
cd vllm
uv pip install --editable . --torch-backend=auto
```

Start the vLLM server with MTP enabled:

```bash
vllm serve tencent/Hy3-preview \
  --tensor-parallel-size 8 \
  --speculative-config.method mtp \
  --speculative-config.num_speculative_tokens 1 \
  --tool-call-parser hy_v3 \
  --reasoning-parser hy_v3 \
  --enable-auto-tool-choice \
  --served-model-name hy3-preview
```

### SGLang

Build SGLang from source:
```bash
git clone https://github.com/sgl-project/sglang
cd sglang
pip3 install pip --upgrade
pip3 install "transformers>=5.6.0"
pip3 install -e "python"
```

Launch SGLang server with MTP enabled:

```bash
python3 -m sglang.launch_server \
  --model tencent/Hy3-preview \
  --tp 8 \
  --tool-call-parser hunyuan \
  --reasoning-parser hunyuan \
  --speculative-num-steps 1 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 2 \
  --speculative-algorithm EAGLE \
  --served-model-name hy3-preview
```

## Training

Hy3 preview provides a complete model training pipeline, supporting both full fine-tuning and LoRA fine-tuning, with DeepSpeed ZeRO configurations and LLaMA-Factory integration.

For detailed training documentation, please refer to: [Training Guide](./train/README.md)

## Quantization

We provide [AngelSlim](https://github.com/tencent/AngelSlim), a more accessible, comprehensive, and efficient toolkit for large model compression. AngelSlim supports a comprehensive suite of compression tools for large-scale multimodal models, including common quantization algorithms, low-bit quantization, and speculative sampling.

## License


Hy3 preview is released under the **Tencent Hy Community License Agreement**. See [LICENSE](./LICENSE) for details.

## Contact Us

If you would like to leave a message for our R&D and product teams, welcome to contact us. You can also reach us via email:

📧 **hunyuan_opensource@tencent.com**

---

<p align="center">
  <i>Hy3 preview is developed by the Tencent Hy Team.</i>
</p>
