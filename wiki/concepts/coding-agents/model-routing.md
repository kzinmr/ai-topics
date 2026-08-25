---
title: Model Routing — Per-Turn Cost Optimization for AI Coding
type: concept
created: 2026-05-09
updated: 2026-08-25
tags:
  - inference
  - optimization
  - coding-agents
  - economics
  - claude-code
  - openai
  - google
sources:
  - https://x.com/i/article/2053183959341711361
  - "[[raw/articles/2026-06-03_solo-ai-agency-kimi-2-6]]"
  - "[[raw/articles/2026-08-25_factory_model-routing-belongs-in-the-harness]]"
  - "https://factory.com/news/model-routing-belongs-in-the-harness"
---

# Model Routing — Per-Turn Cost Optimization for AI Coding

Model routing is a technique that dynamically selects the best-fit model for each individual query or turn in an AI coding session, rather than committing to a single model upfront.

## Augment Prism (May 2026)

Augment Code's **Prism** is the first production-grade per-turn model router for coding agents. It routes each turn to the model that fits the work, with cache eviction costs baked into the decision.

### Key Metrics
- **20-30% cost reduction** per task at **similar or better quality** (on Augment's internal multi-turn coding benchmark)
- Teams sending 10,000 messages/month: ~$20,000/month savings
- Two routing families:
  - **Prism (Claude + Gemini)**: Targets Opus 4.7 quality
  - **Prism (GPT + Kimi)**: Targets GPT 5.5 quality

### Design
- Billing rolls up under a single "Prism" line item — the underlying model is not surfaced to users
- Router considers: task complexity, context size, cache state, model capability
- Switch decision weighs expected quality gain against cache eviction cost

## Why It Matters

No single model wins every task within a session. Simple autocompletion doesn't need a frontier model; complex debugging might. Per-turn routing optimizes both cost and quality simultaneously, which fixed-model strategies cannot achieve.

See full router config and benchmarks: [[concepts/coding-agents/ai-coding-cost-optimization]].

## Solo Agency 3-Tier Routing (June 2026)

A real-world production deployment of model routing from a solo AI agency operator running 14 clients at $40k MRR. The routing strategy pairs explicit decision rules with cost-of-failure economics:

```yaml
default: kimi-2.6

routes:
  production:     # coding, content, automations, debugging
    model: kimi-2.6
  high_stakes:    # architecture, security, genuinely novel problems
    model: claude-opus-4-6
  cleanup:        # lint, format, boilerplate
    model: local-qwen
```

**Decision heuristic:** "If the cost of a wrong answer is more than 100x the model cost difference, use the expensive model." For 90% of production work (building, coding, content, automations), Kimi 2.6 delivers indistinguishable shipped quality at 6x lower cost. The remaining 10% — architecture decisions, security reviews, genuinely novel problems — routes to a premium model.

**Economics:** ~$240/month on Kimi 2.6 for the bulk of delivery + ~$110/month on Opus for high-stakes work = ~$350 total AI inference for $40,000 in monthly revenue. Running the same load entirely on a frontier model would cost $1,500-$5,000+/month and hit rate limits.

**Relationship to other routing approaches:**
- **Augment Prism**: Automated per-turn routing with cache-awareness — the professional, managed equivalent
- **Ronin config**: Static keyword-triggered routing with similar 3-tier pattern — the explicit, transparent equivalent
- **Solo agency routing**: Cost-of-failure heuristic routing — the practical, economics-driven approach

Source: [[raw/articles/2026-06-03_solo-ai-agency-kimi-2-6]]

## Devin Fusion: Dynamic Mid-Session Routing (June 2026)

Cognition's **Devin Fusion** introduces a different routing paradigm: rather than routing per-turn to a single model, it runs two parallel agents (frontier "main" + cost-effective "sidekick") and routes **dynamically mid-session** using lightweight classifiers. Model switching happens during context compaction, making it cache-free.

Key distinction from per-turn routing: the sidekick pattern retains frontier intelligence for planning/review while offloading execution — achieving 35% cost reduction at maintained quality.

This approach is best understood as a synthesis strategy rather than pure routing. See [[concepts/multi-model-synthesis-strategies]] for the full taxonomy comparing Devin Fusion, OpenRouter Fusion, and Sakana Fugu.

Source: [[raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness]]

## Factory Droid: Routing in the Harness (Aug 2026)

[[entities/factory|Factory]] published a position paper arguing that model routing **belongs in the agent harness, not at the gateway or model-serving layer** — a third architectural point distinct from both per-turn routing (Augment Prism) and mid-session synthesis (Devin Fusion). Factory's **Factory Router** has routed production customer work for 2+ months.

### Production Results
- **58% aggregate cost cut** vs pricing every call at the frontier model; **median routed session saved 76%**, and 9 in 10+ sessions saved at least half
- Routed sessions **matched frontier-pinned sessions across 8 production measures** (task completion, command/test failures, repeated edits, delivered artifacts, user acceptance)
- **Median turn latency fell 81s → 49s** (efficient models respond faster on the turns they handle)
- Benchmarks: **99% of frontier pass rate on Terminal-Bench 2**, **96% on Legacy-Bench**, at ~20% lower cost per successful run

### Why the Harness (vs Gateway)
The three layers a request crosses — model serving, gateway, harness — each make the model choice with different information:
- **Model serving** (deepest): sees capacity + endpoint state; routes across deployments for load balancing. No task context.
- **Gateway**: sees every request, allowed-model policy, provider health; enforces the allowed set, picks provider, handles failover. Attractive for its central position, but it sees the request as an opaque completion — a cache-blind, request-sized view.
- **Harness** (where the agent loop lives): owns **session cache state**, assembles the request's system instructions/tools/reasoning settings **around the chosen model before the request exists**, and observes **task outcomes** (test results, repeated edits, user acceptance) that no other layer sees.

Two consequences make routing harness-only:
1. **Cache-awareness**: switching models discards the warm prefix — the next call re-processes the accumulated transcript at fresh-input rates (5–10× the cached rate). Only the harness knows whether the work has stalled (worth paying fresh) or is on steady progress (stay on the warm model). "Staying put is itself a routing decision." A gateway that switches without preserving the warm prefix is cache-blind: in Factory's modeled data, fully-uncached cost exceeds the all-frontier baseline by turns 6–20 and reaches **2.12× at turns 61–150, 2.37× at turns 151–200**, while cache-aware routing stays at **0.19–0.28×** the same baseline.
2. **Request building + outcome signal**: the harness must choose the model before assembling the request (model families aren't wire-compatible — switching can discard encrypted reasoning content). And because it runs the tools and checks the work, it can tie each routing decision to the outcome that followed, using that history to refine the routing policy.

### Design Implications
- **Subagent/mission splitting**: the harness writes each worker's spec and picks its model from the job description; a strong parent can use efficient workers for exploration while keeping its warm prefix. Median Factory Mission spans **423 turns / ~12 hours**; routing saved **37.8%** of complete mission cost.
- **Validator model ≠ implementer model**: a useful review job fails where the implementer doesn't, so Factory's default validator comes from a different model family than its default implementer.

This is a direct counterpoint to [[concepts/coding-agents/ai-coding-cost-optimization|Manifest's deprecation post-mortem]] (which argued routing complexity isn't worth it for mid-complexity routers) — Factory's position is that routing *is* worth it, provided it lives where cache state and task outcomes are visible.

Source: [[raw/articles/2026-08-25_factory_model-routing-belongs-in-the-harness]]

## Related Concepts

- [[concepts/inference-optimization]]
- [[entities/augment]]
- [[concepts/llm-cost-optimization]]
- [[concepts/coding-agents/ai-coding-cost-optimization]] — Ronin's complete system with manual config-based router
- [[concepts/multi-model-synthesis-strategies]] — Broader taxonomy of multi-model approaches (sidekick, panel synthesis, orchestration)
- [[concepts/model-switching-in-graph-workflows]] — KV cache and context management when switching models in graph-based workflows

## Manual Router Architecture (Ronin, May 2026)

As an alternative to automated routing like Prism, [[entities/ronin-deronin|Ronin]] (@DeRonin_) documented a **static, keyword-triggered** router config that splits work across 4 model tiers:

| Tier | Model | Trigger Keywords | % of Work |
|------|-------|-----------------|-----------|
| Premium | Claude Opus 4.6 | "plan", "architect", "design system", "security review" | ~10% |
| Workhorse | Kimi 2.6 | "review", "debug", "refactor", "implement", "build" | ~80% |
| Utility | Claude Haiku 4.5 | "lint", "format", "fix typo", "rename" | ~5% |
| Local | Ollama:Qwen 3:7b | "autocomplete", "stub", "boilerplate" | ~5% |

Key difference from Prism: Ronin's router uses **explicit keyword matching** against the user's prompt (static config) while Prism uses **per-turn learned routing** with cache-awareness built into the decision. Ronin's approach is simpler to implement and reason about, and achieved a 92.6% bill reduction ($4,200→$312/month) with no quality loss.

The core insight: Kimi 2.6 matches Sonnet 4.6 on shipped code quality at 1/6 the cost, making Sonnet a poor default in 2026. The router is complementary to Augment Prism — Prism automates the routing that Ronin's config manually encodes.

See full router config and benchmarks: [[concepts/coding-agents/ai-coding-cost-optimization]].

## Manifest's Router Deprecation (July 2026)

In July 2026, **Manifest** published a candid post-mortem on why they deprecated their LLM router. The core argument: **LLM routing complexity may not justify the cost savings**.

### Key Arguments
- **Routers introduce a second source of failure**: When routing decisions are wrong, debugging is significantly harder — the user sees a bad output but the root cause may be the router, not the model
- **Model capability convergence**: As frontier models converge in quality and pricing (e.g., GPT-5.6 and DeepSeek V4 Flash price war), the marginal benefit of routing shrinks
- **Operational overhead**: Maintaining routing rules, updating model selections, and monitoring routing accuracy adds engineering burden that offsets savings
- **Simplicity wins**: For most teams, picking one model and optimizing prompts/context is higher-leverage than managing a routing layer

### Counterpoint
The routing landscape is not uniform: Augment Prism (automated, per-turn) and Ronin (static, keyword-based) operate at different levels of complexity than Manifest's deprecated system. The Manifest post-mortem applies most directly to **mid-complexity routers** — those too complex to be static rules but not sophisticated enough to be fully automated with cache-awareness.

### Source
- Manifest blog: [Why We Deprecated Our LLM Router](https://manifest.build/blog/why-we-deprecated-our-llm-router/)
- HN discussion: 121 points
- Raw article: [[raw/articles/2026-07-31_manifest_deprecated-llm-router]]
