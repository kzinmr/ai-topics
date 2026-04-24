---
title: "Self-Hosting AI for Development"
type: concept
created: 2026-04-13
updated: 2026-04-13
tags: [self-hosting, local-llm, qwen, opencode, cost-optimization, model-comparison]
aliases: ["self-hosted-coding-agents", "local-ai-development", "qwen-coder-workflow", "ai-inference-economics"]
related: [[claude-code-best-practices]], [[cli-over-mcp-pattern]], [[inference-speed-development]], [[openclaw]]
sources:
  - url: "https://steipete.me/posts/2025/self-hosting-ai-models/"
    author: "Peter Steinberger (@steipete)"
    date: "2025-07-31"
    title: "Self-Hosting AI Models After Claude's Usage Limits"
---

# Self-Hosting AI for Development

**Self-Hosting AI for Development** covers the practical considerations, economics, and workflow implications of running AI coding models on personal or cloud infrastructure rather than relying solely on API-based services.

The core tension: **control and cost predictability vs. convenience and performance**.

---

## The Trigger: Why Self-Host?

Steipete's exploration was triggered by Anthropic's Claude Max subscription changes:
- **Before**: 5-hour daily usage window (predictable)
- **After**: Weekly limits (unpredictable for heavy users)
- **Impact**: ~$6,000/mo in API costs at heavy usage levels

For developers hitting rate limits or seeking cost optimization, self-hosting becomes attractive.

---

## Tool Landscape Evaluation (2025-07)

| Tool | Verdict | Key Characteristics |
|------|---------|-------------------|
| **Claude Code** | 👑 **Primary** | Best single-model optimization, superior tool-use |
| **opencode** | ✅ **Top Contender** | Multi-provider, Qwen 3 Coder optimized, rapidly improving |
| **charm crush** | ⚠️ Promising | Beautiful CLI, but edit tool bugs block workflow |
| **claude-code-router** | ❌ Not Recommended | Degrades tool-use quality vs. native Anthropic |
| **Cline** | ❌ Workflow Mismatch | VS Code extension, underperforms in tests |
| **amp** | ⚠️ Niche | Opinionated CLI, token-efficient but underperforms |
| **Gemini CLI / Qwen Code** | ✅ **Best for Debugging** | Extremely fast, large contexts, tool-calling issues |

> **Key Insight:** *"Tooling & the right system prompt are crucial. Claude Code's strength is being optimized for just one model, and it shows."*

---

## Infrastructure Reality Check

### Hardware Requirements for Competitive Models

**Steipete's Test Rig:**
```
8x H200 (1128GB GPU VRAM total)
176 CPU cores, 1450GB RAM
Ubuntu 24.04, CUDA 12.8
Cost: $15/hour
```

**Model: Qwen3-Coder-480B (FP8)**
- Context: 400K tokens
- KV Cache: ~4.2MB/token (FP16)
- 1M context requires: 17-30 H200s

**Local Hardware That Failed:**
- Mac Studio 512GB RAM: Insufficient for competitive models
- Deepseek Coder V2: ~25 tok/s (not fun for development)
- Quantized R1: ~8-15 tok/s, 128K context (significant downgrade)

### The Cloud GPU Economics

| Option | Cost/Hour | Reliability | Notes |
|--------|-----------|-------------|-------|
| **H200 Spot** | ~$6 | Unreliable | Preemption risk |
| **H200 Regular** | ~$14-15 | Stable | Best current choice |
| **B200 Spot** | ~$4 | Immature | Software not ready |

---

## Cost Analysis: Self-Hosting vs. APIs

### Per 1M Tokens Comparison

| Provider | Input Cost | Output Cost | Notes |
|----------|------------|-------------|-------|
| **Qwen 3 Coder (Alibaba)** | $1-$6 | $5-$60 | Scales with context usage |
| **Anthropic Opus** | $15 | $75 | Premium baseline |
| **Anthropic Sonnet** | $3 | $15 | Balanced |
| **Gemini 2.5 Pro** | $1.25-$2.50 | $10-$15 | Cost-efficient |
| **Cerebras Code Max** | $200/mo | - | 5,000 msgs/day, 20x faster |

### Self-Hosting Economics

| Scenario | Cost | Notes |
|----------|------|-------|
| **24/7 Runtime** | ~$11,000/month | $360/day × 30 |
| **Daily Rebuild** | ~$2,600/month | 30-60 min setup daily |
| **Heavy Day (500M tokens)** | ~$200-1000 via API | ≈ 8h of self-hosted rig |

> **Verdict:** *"Commercially, paying per token is the economically saner choice."*

**The math is clear:** Unless you're processing billions of tokens daily, API costs are lower than dedicated GPU infrastructure.

---

## The Practical Stack Recommendation

Steipete's final verdict:

```
Primary: Claude Code (terminal + coding)
Fallback: opencode + Qwen on Alibaba/Cerebras (simpler tasks, rate limit backup)
Debugging: Gemini CLI (fast, large contexts)
```

**Why this works:**
- Claude Code handles the heavy lifting where quality matters most
- opencode + Qwen provides cost-effective backup when limits hit
- Gemini fills the debugging niche where speed > precision

---

## Open Source Model Reality

### Chinese Models Closing the Gap

> "Chinese labs release better and more capable models. It's great to know that open-source models are merely 6-12 months behind the best commercial ones."

**Qwen 3 Coder specifically:**
- Usable for daily development
- Cost-effective via cloud APIs
- Not yet competitive with Opus/Sonnet for complex tasks
- Gap is narrowing rapidly

### The Context Window Trade-off

| Approach | Context | Quality | Cost |
|----------|---------|---------|------|
| **Commercial (Opus)** | 200K | Best | High |
| **Commercial (Gemini)** | 1M | Good | Medium |
| **Self-Hosted (Qwen FP8)** | 400K | Good | Infrastructure |
| **Self-Hosted (Qwen FP16)** | 32K | Best | Infrastructure |

**The fundamental constraint:** Higher precision = less context. Most development work requires large context, forcing a quality compromise.

---

## Setup Complexity

### vLLM Deployment on 8x H200

The setup takes ~2-3 hours and involves:
1. Provisioning Vast.ai instance
2. SSH configuration
3. vLLM deployment with specific parameters
4. Client configuration (Cline, Cursor, CLI)
5. Authentication bypass for local access

**The hidden cost:** Ongoing maintenance, monitoring, debugging infrastructure issues instead of building software.

---

## When Self-Hosting Makes Sense

| Scenario | Recommended | Why |
|----------|-------------|-----|
| **Privacy requirements** | ✅ Yes | Data never leaves your infrastructure |
| **Extreme usage volume** | ✅ Maybe | >10B tokens/month justifies infrastructure |
| **Model experimentation** | ✅ Yes | Full control over parameters, fine-tuning |
| **Cost optimization** | ❌ No | APIs are cheaper for most use cases |
| **Reliability concerns** | ❌ No | Cloud infrastructure has its own failure modes |
| **Daily development** | ⚠️ Depends | Quality gap still matters for complex tasks |

---

## Connection to Other Patterns

- [[cli-over-mcp-pattern]] — Self-hosted models still benefit from CLI-first interaction
- [[inference-speed-development]] — Local inference adds latency; cloud APIs may be faster
- [[openclaw]] — Steipete's OpenClaw project aims to make agent infrastructure more accessible

## Sources

- [Peter Steinberger: Self-Hosting AI Models After Claude's Usage Limits](https://steipete.me/posts/2025/self-hosting-ai-models/) — Primary source, comprehensive infrastructure analysis
- [Vast.ai Documentation](https://vast.ai/) — GPU marketplace for self-hosting
- [vLLM Documentation](https://docs.vllm.ai/) — High-throughput inference server
