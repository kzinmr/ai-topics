---
title: [AINews] Tasteful Tokenmaxxing — Comprehensive Summary
category: other
status: active
---

# [AINews] Tasteful Tokenmaxxing — Comprehensive Summary

## 🔑 Key Excerpts & Important Facts
> *"please read the code"* — Dex Horthy, retracting his "vibe-coding" stance and emphasizing code review over raw generation.

> *"you want to go for depth (e.g. do more serial autoresearch loops) than go for breadth (e.g. solve a problem by kicking off 5, 10, 50, 500 parallel runs of the LLM slot machine)."* — Mikhail Parakhin, CTO of Shopify, on "tasteful tokenmaxxing".

> *"traces capture agent errors and inefficiencies, and that compute should be pointed at understanding traces to generate better evals, skills, and environments"* — Vtrivedy10 on agent data primitives.

**Critical Benchmarks & Specs:**
- **Qwen3.6-27B** beats Qwen3.5-397B-A17B: `SWE-bench Verified 77.2 vs 76.2` | `SWE-bench Pro 53.5 vs 50.9` | `Terminal-Bench 2.0 59.3 vs 52.5` | `SkillsBench 48.2 vs 30.0`
- **OpenAI Privacy Filter**: `1.5B total / 50M active MoE` | `128k context` | Apache 2.0
- **Google TPU v8**: `TPU 8t` (~3x compute/pod vs Ironwood) | `TPU 8i` (1,152 TPUs/pod) | Scales to `1M TPUs` in single cluster
- **Inference Gains**: Cohere W4A8 in vLLM → `58% faster TTFT` | `45% faster TPOT` vs W4A16 | SonicMoE on Blackwell → `54%/35% higher fwd/bwd TFLOPS`
- **Scaffold Impact**: Qwen3.6-35B + `little-coder` agent → `78.7%` on Polyglot benchmark (jump from `19%` to `78%`)

---

## 📊 Core Industry Theme: "Tasteful Tokenmaxxing"
- **Shift in AI Leadership Focus**: Post-AIE Miami, CTOs, VPs, and Founders are prioritizing **"Tokenmaxxing"** — maximizing AI adoption while avoiding the wasteful, low-quality output cycles warned against by Gergely Orosz.
- **Quality over Quantity**: Senior leaders increasingly align with the **"Zechner side"** of Alex Volkov's Z/L continuum, favoring architectural rigor over cheap, high-volume code generation.
- **Strategic Recommendation**: Prioritize **depth** (serial autoresearch loops, iterative refinement) over **breadth** (massive parallel LLM runs). This reduces token waste, improves output quality, and aligns with enterprise cost/efficiency goals.

---

## 🤖 Open Models & Releases
| Model | Key Features | Benchmarks / Specs | Ecosystem Support |
|-------|--------------|-------------------|-------------------|
| **Qwen3.6-27B** | Dense, Apache 2.0, thinking/non-thinking modes, unified multimodal | Beats Qwen3.5-397B-A17B across coding evals | vLLM (day-0), Unsloth (18GB GGUF), llama.cpp, Ollama |
| **OpenAI Privacy Filter** | Lightweight Apache 2.0 PII detection/masking | 1.5B total / 50M active MoE, 128k context | Targets enterprise/agent pipeline redaction |
| **Xiaomi MiMo-V2.5-Pro** | Long-horizon agents, 1,000+ autonomous tool calls | SWE-bench Pro 57.2, Claw-Eval 63.8, τ3-Bench 72.9 | Hermes/Nous integration |
| **Xiaomi MiMo-V2.5** | Native omnimodality | 1M-token context window | Arena listed for Text/Vision/Code |

---

## 🏗️ Infrastructure & Enterprise Platforms
- **Google Cloud Next (TPU v8)**:
  - Split architecture: `TPU 8t` (training) & `TPU 8i` (inference)
  - `TPU 8i` supports 1,152 TPUs/pod for low-latency, high-throughput multi-agent workloads
  - Google claims scalability to **1M TPUs in a single cluster**, signaling vertical integration of chips, models, agent tooling, and enterprise control planes.
- **Gemini Enterprise Agent Platform**: Evolution of Vertex AI. Includes `Agent Studio`, `200+ models via Model Garden`, and native support for Gemini 3.1 Pro/Flash Image, Lyria 3, and Gemma 4.
- **Workspace Intelligence GA**: Semantic layer over docs, sheets, meetings, and mail. Paired with `Gemini Embedding 2 GA` (unified multimodal embeddings across text, image, video, audio, documents).

---

## 🔄 Agent Ecosystem & Developer Workflows
- **Agent Harness Convergence**: Vendors are standardizing around cloud-hosted, shared-context, approval-gated, long-running execution models.
  - OpenAI: Workspace agents in ChatGPT (Codex-powered, cross-platform)
  - Google: Gemini Enterprise Agent Platform
  - Cursor: Slack invocation for task kick-off & streaming updates
- **Model Flexibility Push**: VS Code/Copilot now supports **BYO-key/model** across all plans (Anthropic, Gemini, OpenAI, OpenRouter, Azure, Ollama, local backends). Addresses industry overfitting to single-harness models.
- **Traces & Evals as Core Primitive**:
  - Traces are becoming the foundational data layer for agent improvement.
  - Push for **open traces** and **Agent Data Protocol (ADP)** standardization.
  - LangChain teasing stronger evaluation/testing product direction.

---

## ⚙️ Post-Training, RL & Inference Optimization
- **Perplexity's Post-Training Playbook**: Search-augmented SFT + RL pipeline improves factuality, citation quality, instruction following, and efficiency. Qwen-derived systems now match/beat GPT-family models on factuality at lower cost.
- **Neural Garbage Collection**: RL jointly learns reasoning and KV-cache retention/eviction without proxy objectives.
- **Over-Editing Benchmark**: Addresses co-editing degradation in multi-agent workflows.
- **Cohere W4A8 quantization**: 58% faster TTFT, 45% faster TPOT in vLLM vs W4A16.
- **SonicMoE on Blackwell**: 54% higher fwd TFLOPS, 35% higher bwd TFLOPS.

---

## 🌐 Events & Community
- **AIE Miami (March 2026)**: Catalyst for tasteful tokenmaxxing discourse
- **AI Engineer Singapore**: Upcoming event for AI engineering community
- **AI Engineer NYC**: Community gathering

---

## Key Voices
| Person | Role | Position |
|--------|------|----------|
| Mikhail Parakhin | Shopify CTO | Depth-first tokenmaxxing |
| Dex Horthy | AI practitioner | Retracted vibe-coding, code review focus |
| Alex Volkov | AI researcher | Z/L continuum framework |
| Gergely Orosz | Engineer | Warns against wasteful AI adoption |
| Vtrivedy10 | Agent ecosystem | Traces as core primitive |
