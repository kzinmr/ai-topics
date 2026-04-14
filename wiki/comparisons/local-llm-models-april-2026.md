---
status: active
created: 2026-04-15
updated: 2026-04-15
tags: [local-llm, models, comparison, open-weights, MoE]
source_article: AINews - Top Local Models List - April 2026
---

# Local LLM Models Comparison — April 2026

Top open-weight and locally-runnable models as of April 2026. Focus on models that can run on consumer hardware (single GPU or CPU).

## Frontier Open-Weight Models

| Model | Size | Active Params | Architecture | License | Hardware Target | Notable Features |
|-------|------|---------------|-------------|---------|-----------------|------------------|
| **gpt-oss-120b** | 117B | 5.1B | MoE | Apache 2.0 | Single H100 GPU | o4-mini class reasoning, configurable reasoning effort, Harmony format |
| **gpt-oss-20b** | 21B | 3.6B | MoE | Apache 2.0 | 16GB VRAM (consumer GPU) | Lightweight reasoning, phone-edge deployable |
| **GLM-4.5** | — | — | Dense | — | Consumer GPU | Strong on Terminal-Bench (Claude-level) |
| **GLM-4.5-Air** | — | — | MoE | — | 3x RTX 3090 + CPU | MoE offloading via llama.cpp `-n-cpu-moe` |
| **Qwen 3 Coder** | — | — | Dense | — | Consumer GPU | Top performer on AlgoTune ($1/task budget) |
| **Claude Opus 4.1** | — | — | Dense | Proprietary | API-only | Best coding model (for now), agentic tasks |

## Small Specialized Models

| Model | Size | Use Case | Performance | Hardware | Notes |
|-------|------|----------|-------------|----------|-------|
| **KittenTTS** | <25MB (~15M params) | Text-to-Speech | 8 expressive voices (4M/4F) | Raspberry Pi, phones (CPU) | Edge-first design, multilingual planned |
| **Falcon Perception** | 0.6B | Vision-Language (segmentation) | Outperforms SAM 3 | MacBook (MLX) | Specialized beats generic |
| **SauerkrautLM-Doom** | 1.3M (ModernBERT-Hash) | VizDoom gameplay control | 31ms inference on CPU, beats larger API LLMs | CPU | Narrow but dominant on target task |
| **Gemma 4 E2B** | — | On-device inference | ~40 tok/s | iPhone 17 Pro (MLX) | Mobile-first demo |

## Training & RL Efficiency

| Model/Project | Technique | Throughput Gain | Notes |
|---------------|-----------|-----------------|-------|
| **OLMo 3** | Async RL (was sync) | 4× tokens/sec | Engineering postmortem available |
| **Cursor Blackwell** | Warp decode optimization | 1.84× faster MoE generation | Improved output quality |
| **Muon optimizer** | Matmul + epilogue design | — | Coming to consumer Blackwell cards |
| **gpt-oss-120b training** | — | ~2.1M H100 hours | Comparable to DeepSeek-R1's 2.66M H800 hours |

## Tooling & Ecosystem Updates

| Tool | Update | Impact |
|------|--------|--------|
| **llama.cpp** | `-n-cpu-moe` / `--cpu-moe` flags | Trivial MoE layer offloading to CPU (no regex hacks) |
| **Ollama** | NVIDIA + Qualcomm partnership | Hardware acceleration for gpt-oss |
| **vLLM** | gpt-oss integration | Production serving support |
| **HuggingFace Transformers** | v4.55.0 | Native gpt-oss support |
| **GGUF format** | gpt-oss quants available | Low-resource and edge deployments |
| **Unsloth** | Free notebook supports 500+ models | Training/fine-tuning accessibility |
| **Harmony (OpenAI)** | Open-sourced | New chat template with "channels" concept |

## Benchmark Notes

### AlgoTune (Cost-Aware Benchmark)
- Budgets models at $1 per task
- **Qwen 3 Coder** and **GLM 4.5** beat Claude Opus 4 on cost efficiency
- Open-weight models competitive when cost is factored

### Terminal-Bench
- **GLM-4.5** places among Claude-level models
- Measures real terminal interaction capability

### GPQA (Graduate-Level Google-Proof Q&A)
- **gpt-oss-120b** scores ~80
- Impressive for a single-GPU runnable model

### AIME (Math)
- Gains from ~50% to ~56-58% with async RL improvements
- Ahead of DeepSeekR1-Zero-Math, competitive with o1-mini

## Key Observations

1. **MoE is the dominant architecture for local deployment** — Both gpt-oss models use MoE, and llama.cpp added dedicated MoE offloading support. The active parameter count (5.1B for 120B model) is what matters for inference speed.

2. **Apache 2.0 licensing is a major differentiator** — OpenAI's choice of Apache 2.0 for gpt-oss removes copyleft restrictions, making it suitable for commercial deployment. This contrasts with more restrictive open-weight licenses.

3. **Specialization > Scale for edge** — The trend continues: small focused models (1.3M, 0.6B, 15M params) outperform larger general models on their target tasks while running on consumer hardware.

4. **Apple Silicon is becoming a first-class local inference target** — MLX ecosystem growth (Gemma 4, Falcon Perception, ESM-2 port) makes Macs viable local LLM platforms.

5. **The "lobotomization" debate** — Community feedback on gpt-oss notes heavy safety filtering ("safetymaxxing") that may reduce general utility. This is a recurring tension in open-weight releases from major labs.

## Related wikilinks

- [[concepts/local-llm/gguf]] — GGUF quantization format
- [[concepts/local-llm/llama-cpp]] — llama.cpp inference engine
- [[concepts/local-llm/model-quantization]] — Quantization techniques
- [[concepts/local-llm/model-distillation]] — Knowledge distillation
- [[entities/openai]] — OpenAI (gpt-oss creator)
- [[comparisons/frontier-models-2026-04]] — Frontier Models Comparison

## Sources

- AINews - Top Local Models List - April 2026 (substack.com)
- r/LocalLlama, r/LocalLLM community discussions
- OpenAI gpt-oss model cards and research blog
- HuggingFace (gpt-oss collection, Transformers v4.55.0)
- llama.cpp GitHub (PR #15091, -n-cpu-moe feature)
- OLMo 3 engineering postmortem (@finbarrtimbers)
- Cursor Blackwell performance reports
- Unsloth training notebook documentation
- Apple MLX ecosystem updates
- Community benchmarks: AlgoTune, Terminal-Bench, GPQA, AIME
