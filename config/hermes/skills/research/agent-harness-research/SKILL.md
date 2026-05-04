---
name: agent-harness-research
description: Research and compare AI agent harnesses (coding/automation agents like Claude Code, Pi, OpenCode, OpenClaw, Hermes Agent) with model compatibility analysis. Covers the "Harness Effect" — how the same model performs 5-40 percentage points differently depending on the harness.
trigger: |
  When the user asks about:
    - "ハーネス" (harness) in context of AI agents/coding tools
    - Which agent harness works best with which model
    - Harness vs harness comparisons (e.g., "Pi vs OpenCode with Qwen")
    - "Harness Effect" or model-harness compatibility
    - Benchmarks across coding agents
    - agent CLI tools (Claude Code, Codex CLI, OpenCode, Pi, Aider, Cursor)
  Critical trigger: User says "ハーネス" — ALWAYS interpret as AGENT HARNESS (Claude Code, Pi, OpenCode, etc.), NOT inference server (vLLM, llama.cpp, Ollama). The user's domain is coding/automation agent harnesses.
  Secondary trigger: User asks about harness engineering in domain-specific contexts (AEC, engineering report generation, non-coding agent systems). Theodoros Galanos' work on The Harness Blog demonstrates harness engineering extends beyond coding agents into knowledge-work domains.
---

# Agent Harness Research

## Domain Clarification: What "Harness" Means in This Wiki

In this user's context, **"harness" = AI Agent Harness** (coding agent / automation agent framework), NOT inference server.

| ✅ Agent Harnesses | ❌ Not Agent Harnesses |
|---|---|
| Claude Code, Codex CLI, OpenCode, Pi | vLLM, llama.cpp, Ollama (these are inference engines) |
| OpenClaw, Hermes Agent, Aider, Cursor | SGLang, TensorRT-LLM (these are model servers) |
| Cline, Windsurf, Continue | API providers (OpenAI, Anthropic, Google) |

**Why this matters**: If the user asks about "ハーネス" and you start talking about vLLM vs llama.cpp, you will get a correction. The user's interest is in **coding agent frameworks** that harness LLMs to write/edit/run code autonomously.

## The Harness Effect (Critical Concept)

The single most important finding in this domain: **the harness is as important as the model.**

Same model, different harness:
- Claude Opus in Claude Code: **77%** (SWE-bench)
- Claude Opus in Cursor: **93%** → +16pp from harness alone
- Claude Opus with minimal scaffold: **42%** (CORE-Bench)
- Claude Opus in full Claude Code: **78%** → +36pp

**General finding**: Multiple independent studies show the harness effect ranges from **5 to 40 percentage points** depending on model and task type.

**Root causes of harness effect:**
1. **System prompt size** — Bigger is NOT better. Pi keeps <1K tokens; OpenCode can hit 10K+. Excess system prompt degrades model reasoning.
2. **Context management** — How the harness builds context incrementally vs dumping entire codebase into prompt
3. **Tool surface area** — More tools ≠ better. Pi has only 4 core tools (read/write/edit/bash) and outperforms feature-heavy harnesses
4. **Prompt caching architecture** — Claude Code's static-first layout and cache-aware compaction are major factors
5. **Batching/scheduling** — How requests are queued and scheduled affects tail latency
6. **Reasoning architecture** — Open-ended REPL vs deterministic pipeline can produce 14x token difference +8.4% quality (Lambda-RLM). See also: [[entities/theodoros-galanos]], [[concepts/lambda-rlm]]

### The Harness Effect Beyond Coding Agents

The Harness Effect is not limited to coding agents. Theodoros Galanos demonstrated it in the AEC domain with identical models:

| Metric | Open REPL Harness | Lambda-RLM Harness | Improvement |
|--------|-----------|------------|-------------|
| Total Tokens | 740K | 53K | **14x less** |
| Quality (Reward) | 0.67 | 0.73 | **+8.4%** |

Core thesis: "The agent's reasoning architecture is itself a harness design choice. Agent design and harness design are the same problem." — Galanos argues that the line between model-level reasoning architecture (open REPL vs deterministic pipeline) and harness design dissolves completely.

**Implication**: Harness engineering applies broadly beyond coding agents to any domain-specific agent system (AEC reports, HVAC analysis, document generation). The harness effect magnitude (5-40pp for coding agents, 14x token/8.4% quality for AEC) is comparable or larger in domain-specific work.

## Research Workflow

### 1. Identify the Harnesses in Scope

Major agent harnesses to track as of 2026:

| Harness | Type | Creator/Org | Model Policy |
|---------|------|-------------|--------------|
| **Claude Code** | Agent orchestrator | Anthropic→OpenAI | Anthropic models ONLY (Opus 4.7, Sonnet 4.6). Subscription $20/mo |
| **OpenCode** | Model-agnostic harness | AnomalyCo/SST | 75+ providers; Claude/GPT/Gemini/Grok/local. BYOK or $10/mo OpenCode Go |
| **Pi** | Minimalist harness | Mario Zechner | 20+ providers; optimized for local (MLX/GGUF). BYOK. **Anthropic wall**: Claude Max subscription NOT usable in Pi — double-billing |
| **Aider** | Git-first harness | Independent | BYOM (any model). Token-efficient (1/4.2 of Claude Code) |
| **Codex CLI** | Universal coding agent | **OpenAI** (Apache-2.0 OSS, 79.3K GitHub stars, Rust 96.2%) | GPT-5.5 (recommended), GPT-5.4, GPT-5.3-Codex-Spark, GPT-OSS (local), **custom providers** (DeepSeek, Qwen, etc. via config.toml), **local** (Ollama/LM Studio/MLX). Included in ChatGPT Plus/Pro/Team/Enterprise ($20-200/mo). MCP dual, sub-agents, image gen, remote TUI, code review. **Most underrated harness — commonly misreported as single-model/closed-source.** |
| **Cursor** | IDE-integrated | Cursor | Claude Opus, GPT-5, custom. Subscription $20-$200/mo |
| **OpenClaw** | Always-on Telegram agent | Peter Steinberger / NVIDIA | Built on Pi (Oz agent). Local via Ollama/LM Studio, or any API. MIT license |
| **Hermes Agent** | Self-improving persistent agent | Nous Research | Multi-model via config; DeepSeek V4, Gemini, Claude, Ollama. Open-source |

### 2. Determine the Comparison Axes

When comparing harnesses, consider these dimensions:
- **Model compatibility** — which models work, any restrictions (Anthropic wall on Pi)
- **System prompt overhead** — smaller is generally better (Pi <1K, OpenCode ≤10K)
- **Autonomy level** — can it run unattended overnight? (Claude Code yes, Cursor no)
- **Token efficiency** — cost per task (Aider best at 1/4.2 of Claude Code)
- **Local model support** — GGUF, MLX, Ollama, LM Studio
- **Architecture** — CLI vs IDE vs daemon vs Telegram bot
- **Benchmark scores** — SWE-bench, Terminal-Bench, CORE-Bench

### 3. Key Sources for Harness Research

- **thoughts.jock.pl/p/ai-coding-harness-agents-2026** — Best overview of Claude Code vs Codex vs Aider vs OpenCode vs Pi with harness effect data
- **grigio.org/opencode-vs-pi-which-ai-coding-agent-should-you-use** — OpenCode vs Pi comparison (same model, different results)
- **Terminal Trove (terminaltrove.com)** — 43 coding agents indexed with filtering
- **disler/pi-vs-claude-code** (GitHub) — Feature-level comparison Pi vs OpenCode
- **XDA Developers** — "Tested Claude Code against 3 open-source alternatives"
- **Medium: "OpenCode vs Claude Code" by Mohit Aggarwal** — Real user comparison
- **YouTube: "Pi Coding Agent Just Destroyed Claude Code"** — Independent testing
- **MightyBot "Best AI Coding Agents 2026"** — Ranked list with reasoning
- **The Harness Blog (theharness.blog)** — Harness engineering and agentic AI for AEC (Architecture, Engineering, Construction). 25+ posts by Theodoros Galanos. Key articles: "Recursive by Design" (Lambda-RLM, 14x token reduction), "The Harness Is All You Need" (domain-specific harnesses > bigger models). Contains concrete production metrics for harness effect outside coding agents. **Wiki entities**: [[entities/the-harness-blog]], [[entities/theodoros-galanos]]

### 4. Model-Harness Compatibility Analysis

When evaluating a model-harness pairing:

1. **Check provider support** — Does the harness support the model's provider? (Most support OpenAI-compatible API)
2. **Check subscription wall** — Anthropic blocks third-party harnesses from using Max credits
3. **Check system prompt size** — For small/weak models, a large system prompt (10K+) degrades performance significantly
4. **Check local quantization** — For self-hosted: GGUF (llama.cpp, Ollama) vs MLX (Apple Silicon) support
5. **Check tool-calling capability** — Does the model support the harness's tool format?

**General compatibility tiers:**

| Tier | Models | Compatible Harnesses | Notes |
|------|--------|---------------------|-------|
| 🥇 | Claude Opus 4.7 / Sonnet 4.6 | Claude Code (native), Cursor (best score 93%), OpenCode, Aider | Best reasoning, but Anthropic wall on non-Anthropic harnesses |
| 🥇 | GPT-5.4 / GPT-5 | Codex CLI (native), Pi (no wall), OpenCode, Aider, Cursor | No subscription restrictions. App scaffolding specialist |
| 🥇 | Qwen 3.5 Coder 32B | Pi (local GGUF/MLX optimized), OpenCode, Aider | Best open-weight coder. Excellent price-performance |
| 🥇 | DeepSeek V3/V4 | OpenCode (75+ providers), Aider, Pi, OpenClaw (Ollama) | Cost-efficient. Strong at multi-file tasks |
| 🥈 | Gemma 4 26B | Pi + LM Studio (local), OpenCode (Ollama) | 18GB VRAM Q4_K_M; Pi's <1K system prompt compensates for weaker model |
| 🥈 | Gemini 2.5 Pro | Pi, OpenCode, Aider | Large free tier, good at long context |
| 🥉 | Local (7B-14B) | Pi only (minimal overhead), OpenCode (with performance tax) | Smaller models are overwhelmed by large system prompts |

### 5. Presenting Results

Structure comparison responses with:
1. **Quick decision table** — which harness × model pair for which scenario
2. **The Harness Effect** — always mention this if comparing the same model across harnesses
3. **Cost analysis** — subscription vs BYOK vs double-billing traps
4. **Sources** — always cite URLs to benchmark articles

## Key Pitfalls

- **Do NOT confuse agent harnesses with inference servers** — When the user says "ハーネス" they mean Claude Code, Pi, OpenCode, OpenClaw, Hermes Agent, NOT vLLM/llama.cpp/Ollama
- **Anthropic wall on third-party harnesses** — Pi and OpenCode users must PAY API RATES even if they have Claude Max subscription. This is a policy restriction, not a technical one
- **Benchmark scores are harness-dependent** — SWE-bench scores for "Claude Opus" alone are meaningless without specifying which harness
- **Harness vs inference server are orthogonal** — You can run Pi on top of Ollama (Ollama provides the inference, Pi provides the agent harness). Don't treat them as competing categories
- **Don't claim consensus without evidence** — different reviewers get different results; multiple sources needed
- **Pi's token efficiency is situational** — The 1K system prompt advantage matters most with small/weak models; large frontier models (Opus, GPT-5) handle 10K prompts fine
- **ALWAYS verify from primary sources before publishing** — Codex CLI is commonly misreported as single-model/closed-source (it's actually Apache-2.0, supports 5+ model types via config.toml + custom providers). Always check: (1) GitHub repo for license, language, features; (2) official docs for model support list; (3) community examples of custom provider configs. Secondary articles frequently get facts wrong about rapidly-evolving tools.
- **Harness engineering != coding agent frameworks** — Theodoros Galanos' work on AEC report generation demonstrates that harness engineering applies broadly to domain-specific knowledge work (engineering documents, HVAC analysis, construction specs). The same principles (Build-Verify Loop, context engineering, loop detection) transfer across domains. Don't limit harness research to CLI coding agents.
