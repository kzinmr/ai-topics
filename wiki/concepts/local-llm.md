# Local LLM

Running large language models on personal hardware instead of cloud APIs.

## Status
active
## Created
2026-04-10
## Tags
inference, open-source, privacy, local-first

## Summary

Local LLM refers to the practice of running large language models on personal hardware (consumer GPUs, Apple Silicon, edge devices) rather than relying on cloud-hosted APIs. The movement has grown significantly in 2025-2026 due to:

1. **Privacy & Data Sovereignty** — No data leaves the device, critical for enterprises and privacy-conscious users
2. **Cost Efficiency** — No API call costs, one-time hardware investment
3. **Offline Capability** — Models work without internet connectivity
4. **Customization** — Fine-tune, quantize, and modify models without vendor lock-in
5. **Open Source Ecosystem** — Community-driven model improvements and tooling

## Key Technologies

### Inference Engines
- **llama.cpp** — C/C++ implementation by Georgi Gerganov, runs on CPU/Apple Silicon
- **Ollama** — User-friendly local LLM runner with model library
- **LM Studio** — Desktop GUI for discovering and running local models
- **vLLM** — High-throughput serving with PagedAttention
- **MLX** — Apple Silicon optimized inference framework

### Quantization Formats
- **GGUF** — llama.cpp format, enables CPU/edge inference
- **GPTQ/AWQ** — GPU-optimized 4-bit/3-bit quantization
- **EXL2** — High-efficiency format for consumer GPUs

### Notable Open Models
- **Llama 3/4** (Meta) — Foundation models with commercial-friendly licenses
- **Qwen 3.x** (Alibaba) — Strong multilingual and coding performance
- **Mistral/Mixtral** (Mistral AI) — Efficient sparse MoE architecture
- **Gemma 4** (Google) — Lightweight models for local deployment
- **Hermes** (Nous Research) — Uncensored, instruction-tuned variants

## Key Figures

### Georgi Gerganov (@ggerganov)
- Creator of llama.cpp and whisper.cpp
- Joined Hugging Face in 2025 to cement open-source inference stack
- Pioneer of GGML/GGUF quantization ecosystem
- GitHub: github.com/ggerganov

### Nous Research (@NousResearch)
- Hermes model family, open-weight post-training
- Strong local LLM community presence
- Teknium leads post-training efforts

### Ollama Team
- Simplified local LLM deployment
- Model library with one-command downloads
- Strong Apple Silicon support

## Community Hubs

### Reddit
- **r/LocalLLaMA** — Largest community (~500K+ members), model comparisons, hardware benchmarks, uncensored model discussions
- **r/LocalLLM** — Technical discussions, setup guides, troubleshooting
- **r/AI_Agents** — Agent frameworks using local LLMs, workflow automation

### Discord/Forums
- llama.cpp Discord
- Ollama community channels
- Hugging Face forums

## Trends (2026)

1. **Consumer GPU Boom** — RTX 50 series, AMD RX 8000, Apple M-series chips driving local inference
2. **Small Model Renaissance** — 3B-8B parameter models approaching 70B+ quality via better training
3. **Agentic Local AI** — Local LLMs powering autonomous agents for privacy-sensitive workflows
4. **Hybrid Cloud+Local** — Routing simple tasks locally, complex tasks to cloud
5. **Edge Deployment** — Phones, Raspberry Pi, and IoT running quantized models
6. **Digital Sovereignty** — Enterprise and government adoption for data control

## Related wikilinks

- [[concepts/harness-engineering]] — Structured environments for local AI workflows
- [[concepts/agentic-engineering]] — Local LLMs as development partners
- [[entities/llama-cpp]] — The inference engine powering most local deployments
- [[entities/gguf]] — Quantization format enabling consumer hardware inference
- [[entities/georgi-gerganov]] — llama.cpp creator
- [[entities/nous-research]] — Open-weight model developers
- [[concepts/claude-code-leak]] — Open-source model transparency vs proprietary
- [[concepts/project-glasswing]] — Privacy considerations in AI deployment
- [[entities/anthropic]] — Anthropic's stance on model transparency
- [[entities/openai-spud]] — OpenAI hardware integration plans
- [[entities/meta]] — Meta's Llama open-source strategy
- [[entities/qwen3-6-plus]] — Qwen series, strong local performance
- [[entities/gemma-4]] — Google's local-friendly model line
- [[entities/mistral-voxtral-tts]] — Mistral's multimodal local models

## Sources

- r/LocalLLaMA community discussions (2025-2026)
- llama.cpp GitHub repository
- Ollama documentation
- LM Studio docs
- Various hardware benchmark threads on Reddit
- Open-source model comparison sites (ComputingForGeeks, Till Freitag blog)
