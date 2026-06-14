---
title: "Rio 3.5 Open 397B — Frontier-Class Open Model from IplanRIO"
source_url: "https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B"
date: 2026-06-13
source_type: model-card
language: en
tags:
  - model-release
  - moe
  - open-source
  - reasoning
  - swireasoning
  - multimodal
  - coding-agent
  - multilingual
---

# Rio 3.5 Open 397B

**Source**: [HuggingFace Model Card](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)
**License**: MIT | **Downloads**: 112,371 | **Likes**: 184
**Architecture**: Qwen3_5MoeForConditionalGeneration (MoE, 397B total / 17B active)
**Context**: 1,010,000 tokens (1M) | **Created**: 2026-06-11

---

---
library_name: transformers
language:
- pt
- en
license: mit
base_model:
- Qwen/Qwen3.5-397B-A17B
pipeline_tag: image-text-to-text
---

# Rio 3.5 Open 397B

![Rio 3.5 Open 397B benchmark results](rio-3.5-open-benchmarks.png)

**Rio 3.5 Open 397B** is a frontier-class general-purpose AI model developed by [IplanRIO](https://iplanrio.rio.rj.gov.br/), the municipal IT company of Rio de Janeiro's city government. Post-trained from Qwen 3.5 397B, Rio 3.5 Open 397B delivers state-of-the-art open-model performance across agentic coding, mathematics, STEM, multilingual, and multimodal benchmarks — surpassing its base model by significant margins and competing with the world's best open and proprietary models.

Rio 3.5 Open 397B features **SwiReasoning**, a training-free inference framework based on [Shi et al. (2025)](https://arxiv.org/abs/2510.05069) that dynamically switches between explicit chain-of-thought and latent-space reasoning, guided by entropy-based confidence signals. This enables both higher accuracy and dramatically improved token efficiency. This model was explicitly trained to maximize the efficiency gained via latent reasoning.

## Key Features

- **397B total / 17B active parameters** (Mixture-of-Experts)
- **1,010,000 token (1M) context window**
- **SwiReasoning integration** — dynamic explicit/latent reasoning switching for Pareto-superior accuracy and efficiency
- **General-purpose** — strong agentic coding, reasoning, instruction-following, and multimodal performance
- **Post-trained from Qwen 3.5 397B**
- **Multilingual** — strong performance in Portuguese, English, Chinese, and dozens of other languages
- **MIT License** — fully open for commercial and research use

## Benchmark Results

### Agentic Coding & Software Engineering

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Terminal-Bench 2.1 | 70.8 | 52.5 | 70.3 | 67.9 | 66.7 | **78.2** |
| DeepSWE | 23.0 | 6.0 | – | 8.0 | 24.0 | **70.0** |
| SWE-Bench Pro | 58.1 | 50.9 | 57.6 | 59.0 | **59.5** | 58.6 |
| SWE-Bench Verified | 80.2 | 76.2 | 77.7 | 80.6 | 80.2 | **82.9** |
| SWE-Bench Multilingual | **77.0** | 69.3 | 75.8 | 76.2 | 76.7 | – |

### Knowledge & Reasoning

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| GPQA Diamond | 90.9 | 88.4 | 90.3 | 90.1 | 90.5 | **93.6** |
| HLE | 36.5 | 28.7 | 34.7 | 37.7 | 36.4 | **41.4** |
| MMLU-Pro | 88.0 | 87.8 | **88.5** | 87.5 | 87.1 | – |
| MMLU-Redux | 94.6 | 94.9 | 94.5 | 94.8 | **95.3** | – |
| SuperGPQA | **72.3** | 70.4 | 71.4 | 69.9 | 71.3 | – |
| Apex | 29.2 | 9.4 | 22.7 | 38.3 | 24.0 | **80.2** |

### Mathematics

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| HMMT 2026 Feb | 93.9 | 87.9 | 92.9 | 95.2 | 92.7 | **98.5** |
| IMOAnswerBench | 89.5 | 80.9 | 86.0 | **89.8** | 86.0 | – |

### Multilingual

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| MMMLU | **89.8** | 88.5 | 89.0 | 87.9 | 87.5 | – |
| MMLU-ProX | **85.6** | 84.7 | 85.4 | 83.9 | 83.7 | – |

### Multimodal

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| MMMU-Pro | 78.4 | 79.0 | 79.0 | – | 79.4 | **81.2** |
| MathVision | 89.1 | 88.6 | **90.3** | – | 87.4 | – |
| VideoMMMU | 81.6 | 84.7 | 85.4 | – | – | **86.4** |

### Agents & Instruction Following

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| MCP-Atlas | 74.2 | 74.2 | 73.2 | 73.6 | 66.6 | **75.3** |
| IFBench | 78.4 | 76.5 | **79.1** | 77.0 | 76.0 | 76.0 |
| IFEval | 93.4 | 92.6 | **94.6** | 91.9 | 94.5 | – |

### Economic Value

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | Qwen 3.7 Plus | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| GDPval (estimated) | 1533 | 1200 | 1520 | 1554 | 1482 | **1769** |

### Gains Over Base Model (Qwen 3.5 397B)

| Benchmark | Base Model | Rio 3.5 Open 397B | Δ |
|:---|:---:|:---:|:---:|
| Terminal-Bench 2.1 | 52.5 | 70.8 | **+18.3** |
| DeepSWE | 6.0 | 23.0 | **+17.0** |
| SWE-Bench Pro | 50.9 | 58.1 | **+7.2** |
| SWE-Bench Verified | 76.2 | 80.2 | **+4.0** |
| SWE-Bench Multilingual | 69.3 | 77.0 | **+7.7** |
| GPQA Diamond | 88.4 | 90.9 | **+2.5** |
| HLE | 28.7 | 36.5 | **+7.8** |
| HMMT 2026 Feb | 87.9 | 93.9 | **+6.0** |
| IMOAnswerBench | 80.9 | 89.5 | **+8.6** |
| Apex | 9.4 | 29.2 | **+19.8** |
| GDPval (estimated) | 1200 | 1533 | **+333** |

## SwiReasoning: Latent/Explicit Reasoning

Rio 3.5 Open 397B integrates [SwiReasoning](https://arxiv.org/abs/2510.05069) (Shi et al., 2025), a training-free inference framework that dynamically alternates between two reasoning modes:

- **Explicit reasoning** — standard chain-of-thought in natural language, where the model commits tokens to a single reasoning path
- **Latent reasoning** — continuous reasoning in hidden space, where the model explores multiple implicit paths simultaneously without emitting tokens

The switching is governed by **block-wise confidence** estimated from entropy trends in the next-token distribution. When confidence is low (entropy trending upward), the model enters latent mode to explore alternatives. When confidence recovers, it switches back to explicit mode to commit to a solution.

This approach achieves a **Pareto-superior** trade-off: higher accuracy at unlimited budgets *and* dramatically better token efficiency under constrained budgets. As with previous Rio generations, the model was post-trained to maximize the gains obtained from latent reasoning.

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "prefeitura-rio/Rio-3.5-Open-397B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

prompt = "Write a poem about Rio de Janeiro."

messages = [
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=81920,
    temperature=0.6,
    top_p=0.95,
)

response = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)
print(response)
```

### Using with vLLM

```bash
vllm serve prefeitura-rio/Rio-3.5-Open-397B \
    --tensor-parallel-size 8 \
    --max-model-len 1048576 \
    --trust-remote-code
```

### Using with SGLang

```bash
python -m sglang.launch_server \
    --model-path prefeitura-rio/Rio-3.5-Open-397B \
    --tp 8 \
    --context-length 1048576 \
    --trust-remote-code
```

## Model Details

| | |
|:---|:---|
| **Developer** | IplanRIO — Empresa Municipal de Informática e Planejamento S.A. |
| **Base Model** | Qwen 3.5 397B |
| **Architecture** | Mixture-of-Experts (MoE) Transformer |
| **Total Parameters** | ~397B |
| **Active Parameters** | ~17B |
| **Context Length** | 1,010,000 tokens (1M) |
| **Training Method** | Post-training |
| **Inference Enhancement** | SwiReasoning (latent/explicit switching) |
| **License** | MIT |
| **Languages** | Multilingual (en, pt, zh, ja, ko, fr, de, es, ar, and more) |

## Citation

If you use SwiReasoning, please also cite:

```bibtex
@misc{shi2025swireasoning,
    title={SwiReasoning: Switch-Thinking in Latent and Explicit for Pareto-Superior Reasoning LLMs},
    author={Dachuan Shi et al.},
    year={2025},
    eprint={2510.05069},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## Acknowledgments

Rio 3.5 Open 397B is built upon the exceptional work of the [Qwen Team](https://github.com/QwenLM) and their Qwen 3.5 model family. We also acknowledge the authors of [SwiReasoning](https://github.com/sdc17/SwiReasoning) for their innovative inference framework.

Developed in Rio de Janeiro 🇧🇷 by [IplanRIO](https://iplanrio.rio.rj.gov.br/).