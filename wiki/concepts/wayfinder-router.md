---
title: Wayfinder Router
aliases: [Deterministic LLM Routing]
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [model-routing, llm-proxy, cost-optimization, open-source, deterministic, self-hosted, local-llm]
sources: [raw/articles/2026-06-25_wayfinder-router_deterministic-llm-routing.md]
---

# Wayfinder Router

Wayfinder Router is a deterministic, offline LLM query router that scores prompts by structural complexity and routes them to different model tiers — without ever calling a model to make the routing decision. It is a Python package (`wayfinder-router` on PyPI) created by [itsthelore](https://github.com/itsthelore/wayfinder-router), released as open source. The project received 121 points on Hacker News.

## Core Idea

Wayfinder scores a prompt's structure (length, headings, lists, code blocks) and wording (proofs, mathematical notation, hard constraints) on a **0.0–1.0 complexity scale**. Prompts below a configurable threshold go to a small/local model; prompts at or above the threshold go to a large/cloud model. The key differentiator: **the routing decision is deterministic, sub-millisecond, and fully offline** — no API key, no network, no model call needed to make it.

This contrasts sharply with [[concepts/ai-gateway]]-style routers that call an LLM judge (RouteLLM, NotDiamond, OpenRouter Auto) to decide routing, adding latency, cost, and non-determinism to the very step meant to save money.

## How It Works

The scoring engine extracts structural and lexical features from the raw prompt text:

- **Structural features**: word count, heading count, list item count, code block count, and other document-structure signals
- **Lexical features** (off by default): reasoning terms ("prove", "theorem"), mathematical symbols, and constraint terms ("must", "required") — these ship off by default because a double-blind test showed the lift does not generalize well

Each feature is normalized and weighted (configurable in `wayfinder-router.toml`), then combined into a single 0.0–1.0 score. The decision is:

- **Binary mode** (default): a single threshold cut — below goes local, at/above goes cloud
- **Tiered mode**: ordered score bands route to any number of models (e.g., 3B → 70B → cloud frontier)
- **Classifier mode**: a fitted multinomial-logistic model per-model, generated via calibration

## No Model Call Required

The routing decision itself uses no model — it is pure Python, pure math on the prompt text. This means:

- **Sub-millisecond latency**: no network round-trip to decide routing
- **Fully offline**: works without internet, no API key needed for the routing decision
- **Deterministic**: the same prompt always gets the same score and same route
- **Zero cost for routing**: the decision is free, regardless of how many requests flow through

This is the fundamental contrast with judge-based routers (RouteLLM, NotDiamond, Martian) that call an LLM to classify difficulty, adding cost and randomness to every routing decision.

## Driving Motivation: [[concepts/llm-cost-crisis]]

Wayfinder directly addresses the [[concepts/llm-cost-crisis]] by preventing simple prompts ("summarize this", "fix my typo") from consuming expensive frontier-model tokens. Cheap prompts stay local; only genuinely hard prompts reach the expensive model. This is structural cost optimization — no model call to decide, no per-request overhead.

## Relationship to [[concepts/ai-gateway]]

Wayfinder and AI gateways answer different questions and **compose together**:

| Tool | Question Answered | Mechanism |
|------|-------------------|-----------|
| **Wayfinder** | Which *tier* does this prompt deserve? (cheap vs. expensive by difficulty) | Deterministic structural scoring |
| **AI Gateway** (LiteLLM, Bifrost, OpenRouter) | Which *provider* should serve this call? (by price, availability, failover) | Provider routing and load balancing |

The recommended pattern: run Wayfinder first to make the cheap-vs-expensive call, then a gateway underneath to reach the specific providers.

## Contrast with [[concepts/kv-aware-routing]]

Both Wayfinder and [[concepts/kv-aware-routing]] are routing strategies for LLM inference, but they optimize fundamentally different things:

- **Wayfinder**: Routes by *prompt difficulty* — simple prompts go to cheap models, complex ones to expensive models. Cost-driven.
- **KV-Aware Routing**: Routes by *cache state* — requests go to the worker whose KV cache has the most prefix overlap. Latency-driven, for multi-turn or agentic workloads.

They are complementary: Wayfinder decides *which model tier*, KV-aware routing decides *which worker* within a tier.

## Enabling [[concepts/cpu-inference-llm]]

Wayfinder is designed to pair directly with [[concepts/cpu-inference-llm]] for the "local" tier. Since Wayfinder's routing decision requires no model call and no GPU, the entire local pipeline — scoring + local inference — can run on consumer hardware:

- A local Ollama, vLLM, or llama.cpp server handles the easy prompts
- The cloud tier (OpenAI, Anthropic, Gemini) handles only the hard ones
- Wayfinder sits in front, invisible to the client

This makes CPU inference economically viable at scale: you pay for the cloud model only when you actually need it.

## Calibration

Wayfinder supports calibration on your own data. The `calibrate` command reads a labeled JSONL dataset (`{"text": ..., "label": "local"|"cloud"}`) and prints a config fragment. It runs offline and never calls a model. Three calibration modes exist:

- `--mode threshold`: sweeps the binary cut to maximize accuracy
- `--mode tiers`: ordinal multi-model band placement
- `--mode classifier`: fits a deterministic L2-regularized Newton/IRLS multinomial-logistic model, converging in a handful of iterations

A cost-aware objective (`--objective knee`) chooses the knee of the quality×savings curve automatically, avoiding collapse to "always route to the expensive model" on skewed labels.

## Feedback Loop

Wayfinder includes a built-in feedback mechanism for continuous improvement:

- `/v1/feedback` endpoint accepts `{"text": "...", "label": "local"|"cloud"}` judgments
- `recalibrate` command re-fits the routing config from accumulated feedback
- An automated `judge` command runs both tiers and uses a deterministic text comparator, with trust gates (Cohen's κ ≥ 0.6 against human gold set) before emitting a config

## Deployment

Wayfinder runs as:

- **Gateway**: an OpenAI-compatible `/v1/chat/completions` endpoint — point any existing client at it by changing one `base_url`. Supports streaming, Anthropic Messages API adapter (for Claude Code), and production features (circuit breaker, rate limiting, virtual API keys, response cache)
- **Library**: `from wayfinder_router import score_complexity` — score prompts in-process with zero dependencies beyond the Python standard library
- **Service**: `wayfinder-router service install` registers it with the OS service manager (launchd on macOS, systemd on Linux)

Every response carries `x-wayfinder-router-model`, `x-wayfinder-router-score`, and `x-wayfinder-router-mode` headers for observability.

## CLI Quickstart

```bash
# Score a prompt
echo "Summarise this paragraph in one sentence." | wayfinder-router route -

# Install and run the gateway
pip install "wayfinder-router[gateway]"
wayfinder-router init
wayfinder-router serve --port 8088

# Run with zero keys for a dry-run
wayfinder-router serve --dry-run
```

## Limitations

Wayfinder's structural approach has known blind spots acknowledged in the project's own FAQ and benchmarks:

- **Semantic difficulty is invisible**: a subtle code snippet or "what is the 100th prime number?" has no structural tell — a semantic router beats Wayfinder there
- **Short-but-hard prompts**: Wayfinder is no better than random on RouterBench's short-but-hard items
- **Lexical features don't generalize**: the lexical cues (math terms, constraints) showed lift in development but failed to generalize in a double-blind test, losing to a plain word-count baseline

The benchmark (`make benchmark`) is honest about where Wayfinder wins and loses against baselines and a perfect oracle.
