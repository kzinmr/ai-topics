---
title: NVIDIA RTX AI Garage
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [concept, nvidia, product, ai-agents, local-llm, hardware, ecosystem]
sources:
  - "raw/articles/2026-05-13_nvidia_rtx-ai-garage-hermes-agent-dgx-spark.md"
  - https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/
  - https://www.nvidia.com/en-us/ai-on-rtx/
---

# NVIDIA RTX AI Garage

NVIDIA's RTX AI Garage is a program for optimizing, curating, and recommending AI tools, models, and agents running on RTX hardware (RTX PCs, RTX PRO workstations, DGX Spark). It serves as a bridge between the open-source AI ecosystem and NVIDIA hardware.

## Program Positioning

RTX AI Garage is not just a blog series, but an optimization layer composed of the following elements:

- **Curation**: Selects and recommends open-source AI agents and models that work most effectively on RTX hardware
- **Playbook**: Provides concrete setup instructions in the `dgx-spark-playbooks` repository on GitHub
- **Optimization validation**: Benchmarks combinations of NVIDIA technologies (NVFP4 quantization, TensorRT-LLM acceleration) with open-source tools
- **Hands-on sessions**: Practical workshops on NemoClaw + OpenShell via the "Build It Yourself" agentic AI series

## Recommended Agent Frameworks

### Hermes Agent (May 2026~)
- **Selection reason**: Self-improving skills, contained sub-agents, reliability by design
- **140K+ GitHub stars / 3 months** — Overwhelming community adoption
- **Most-used agent on OpenRouter** (May 2026)
- **Superior results with same model**: Designed as an "active orchestration layer"
- **Recommended model**: Qwen 3.6 35B (120B-class intelligence with 20GB memory)

### NemoClaw (March 2026~)
- NVIDIA's proprietary secure agent development stack
- OpenShell sandbox + Privacy Router + Network Policy Engine
- Added WSL2 support in May 2026

### OpenClaw (Pioneer)
- First recommended agent on RTX AI Garage
- Success with "Build a Claw" campaign
- Lightweight design for edge devices / DGX Spark

## Supported Models & Optimizations

| Model | Optimization | Target Hardware | Release |
|--------|--------|-----------------|----------|
| Qwen 3.6 35B | General inference | DGX Spark, RTX PRO | 2026-05 |
| Qwen 3.6 27B | General inference (dense) | RTX PRO | 2026-05 |
| Gemma 4 26B/31B | NVFP4 + Multi-Token Prediction | Blackwell GPU | 2026-05 |
| Mistral Medium 3.5 | llama.cpp/Ollama compatible | RTX PRO, DGX Spark | 2026-04 |
| GPT-OSS-120B | MXFP4 quantization | DGX Spark | Ongoing |

## Value Added by RTX AI Garage

Compared to setting up DGX Spark yourself, going through RTX AI Garage provides:

1. **Reduced model selection effort**: NVIDIA benchmarks each model on DGX Spark and specifies optimal quantization formats (NVFP4/MXFP4). Users don't need to compare models or run quantization experiments themselves
2. **Time savings via Playbook**: Official setup instructions published on GitHub, saving trial-and-error time
3. **NVFP4 optimization benefits**: NVIDIA's proprietary NVFP4 quantization is optimized for Blackwell GPU Tensor Cores, faster than generic quantization. This optimization may not be available with self-setup
4. **Hardware-software integration verified**: Integration with NVIDIA software stack (TensorRT-LLM, CUDA-X, NIM) is pre-validated
5. **Community + official support**: Hands-on sessions, newsletters, continuous updates via social media

## Information Channels

- **Blog**: [blogs.nvidia.com](https://blogs.nvidia.com/blog/) — Articles tagged RTX AI Garage
- **GitHub**: [NVIDIA/dgx-spark-playbooks](https://github.com/NVIDIA/dgx-spark-playbooks)
- **Newsletter**: RTX AI PC newsletter (subscribe from NVIDIA AI PC page)
- **Social**: Facebook, Instagram, TikTok, X @NVIDIA
- **Workstation**: LinkedIn, X @NVIDIAWorkstation

## Related

- [[entities/nvidia-dgx-spark]] — DGX Spark hardware platform
- [[entities/hermes-agent]] — Hermes Agent by Nous Research
- [[entities/nvidia-nemoclaw]] — NemoClaw secure agent framework
- [[entities/openclaw]] — OpenClaw agent framework
- [[concepts/local-ai]] — Local AI landscape (May 2026)
- [[concepts/harness-engineering]] — Harness engineering (agent framework optimization)
