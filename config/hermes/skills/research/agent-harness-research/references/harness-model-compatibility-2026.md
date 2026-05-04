# Agent Harness × Model Compatibility Data (2026)

Sources compiled from multiple independent tests (thoughts.jock.pl, grigio.org, Terminal Trove, XDA Developers, disler/pi-vs-claude-code Git repo, MightyBot, patloeber.com).

## Detailed Benchmark Data

### Harness Effect: Same Model, Different Harness

| Model | Harness | Score | Source |
|-------|---------|:-----:|--------|
| Claude Opus | Cursor | **93%** | Matt Mayer independent test |
| Claude Opus | Claude Code | 77% | Matt Mayer; −16pp from harness |
| Claude Opus | Minimal scaffold | 42% | CORE-Bench |
| Claude Opus | Claude Code (full) | 78% | CORE-Bench; +36pp from scaffold |
| GPT-5.4 | Codex CLI (CLI scaffold) | **56.4%** | SWE-bench Pro (Scale SEAL public) |
| GPT-5.3 Codex | Codex CLI (CLI scaffold) | **56.8%** | SWE-bench Pro (Scale SEAL public) |
| GPT-5.5 | Codex CLI | **58.6%** | SWE-bench Pro (benchlm.ai Apr 29, 2026) |
| Claude Opus 4.5 | Codex CLI | **45.9% ± 3.6%** | SWE-bench Pro (SEAL standard scaffold; note same model in Claude Code's scaffold scores very differently) |
| GPT-5.4 | Aider | ~65% | Community estimates |
| Claude Opus | Claude Code | **72.7%** | SWE-bench Verified (official) |
| Claude Opus | OpenCode | ~70-72% | Community estimates (no official benchmark) |

### System Prompt Overhead

| Harness | System Prompt Size | Performance Impact |
|---------|:-----------------:|-------------------|
| **Pi** | **<1,000 tokens** | Minimal overhead. Solved physics problem in 1 attempt while OpenCode failed with same model |
| Claude Code | ~数千トークン | Moderate. Prompt caching architecture mitigates cost |
| Aider | 効率的 | 4.2x fewer tokens than Claude Code. Excellent for iterative work |
| **OpenCode** | **≤10,000 tokens** | Highest overhead. Feature-rich system prompt degrades small models |
| Cursor | Medium | Does not apply when human is at keyboard (handles ambiguity interactively) |

### Local Model Performance

| Setup | Throughput | Notes |
|-------|:----------:|-------|
| Pi + Gemma 4 26B (Q4_K_M, LM Studio) | Fast | 18GB VRAM (all 26B must load despite MoE) |
| Pi + Qwen 3.5 Coder 32B (local) | Fast | Recommended by community |
| OpenCode + Qwen 3.5 Coder 32B (Ollama) | Moderate | 10K system prompt tax on weaker model |
| Claude Code + local | N/A | Anthropic models only |

### Token Cost Comparison (Per Task)

| Harness | Relative Cost | Best Budget Model |
|---------|:------------:|-------------------|
| Aider | **1x** (baseline) | DeepSeek / Sonnet |
| Codex CLI | ~1.5x | GPT-5.4 (included in subscription) |
| Pi | ~2x | GPT-5, Qwen, DeepSeek |
| OpenCode | ~2-3x | Claude, GPT, DeepSeek, Qwen |
| Claude Code | **3-4x** | Opus 4.7 / Sonnet 4.6 (subscription + overage) |

## Provider Support Matrix

| Provider | Claude Code | OpenCode | Pi | Aider | Codex CLI | Cursor | OpenClaw | Hermes |
|----------|:-----------:|:--------:|:--:|:-----:|:---------:|:------:|:--------:|:------:|
| **Anthropic (Claude)** | ✅ Native | ✅ | ✅ (wall) | ✅ | ❌ | ✅ | ✅ | ✅ |
| **OpenAI (GPT)** | ❌ | ✅ | ✅ | ✅ | ✅ Native | ✅ | ✅ | ✅ |
| **Google (Gemini)** | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| **DeepSeek** | ❌ | ✅ | ✅ | ✅ | ✅ (config.toml) | ❌ | ✅ (Ollama) | ✅ |
| **Qwen** | ❌ | ✅ | ✅ | ✅ | ✅ (LM Studio config.toml) | ❌ | ✅ (Ollama) | ✅ |
| **xAI (Grok)** | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Ollama (local)** | ❌ | ✅ | ✅ | ✅ | ✅ (`--oss` flag) | ❌ | ✅ | ✅ |
| **LM Studio (local)** | ❌ | ✅ | ✅ | ✅ | ✅ (config.toml) | ❌ | ✅ | ✅ |
| **MLX (Apple)** | ❌ | ❌ | ✅ (native) | ❌ | ✅ (config.toml) | ❌ | ❌ | ❌ |
| **75+ providers** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

## Pricing Models

| Harness | Entry Price | Full Price | Model Inclusion |
|---------|:-----------:|:----------:|-----------------|
| **Claude Code** | $20/mo (Pro) | $100-200/mo (Max) | Claude models only. Overage on non-subscription models |
| **Codex CLI** | $20/mo (Plus) | $200/mo (Pro) | GPT-5.5/gpt-5.4/Codex-Spark included. Local OSS (GPT-OSS) via `--oss` included. Custom providers (DeepSeek/Qwen) — API charges apply separately. **Best value**: native GPT-5.5 at no extra cost |
| **OpenCode** | Free (BYOK) | $10/mo (Go) | 75+ providers. Bring your own API keys |
| **OpenCode Go** | $10/mo | $10/mo | Includes Zen token credits |
| **Pi** | Free (BYOK) | Free (BYOK) | 20+ providers. **Anthropic wall**: Claude credits don't work |
| **Aider** | Free (BYOK) | Free (BYOK) | Any model via API |
| **Cursor** | $20/mo | $200/mo | Claude/GPT models included |
| **OpenClaw** | Free | Free | MIT license. Local-only or BYOK |
| **Hermes Agent** | Free | Free | Open-source. Multi-model via config |

## Key Quoted Sources

> "Same model, different harness: 16 percentage points (77% → 93%, Opus, Claude Code vs Cursor). Multiple independent studies show a 5-40 point range from harness quality alone."
> — thoughts.jock.pl, "Claude Code vs Codex vs Aider vs OpenCode vs Pi 2026"

> "Pi's minimal approach cuts context overhead and runs faster with local models while producing cleaner output. OpenCode is heavier but gives you more out of the box."
> — grigio.org, "OpenCode vs Pi: Which AI Coding Agent Should You Use?"

> "The tool everyone recommends for beginners is also the tool that will embarrass you in production."
> — Chew Loong Nian, Towards AI (on Ollama with concurrent users — applies to inference, not agent harness, but the principle generalizes)

> "Anthropic does not allow 3rd-party harnesses (like Pi) to use Claude Max subscription credits. Users must pay API rates on top of subscriptions."
> — thoughts.jock.pl, on the "Anthropic Wall"
