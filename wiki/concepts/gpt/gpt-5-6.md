---
title: "GPT-5.6 (Sol / Terra / Luna)"
created: 2026-06-27
updated: 2026-07-15
type: concept
tags:
  - model
  - openai
  - benchmark
  - ai-agents
  - event
  - safety
sources:
  - raw/newsletters/2026-06-27-ainews-openai-gpt-5-6-sol-terra-luna-restricted-to-trusted-partners.md
  - raw/articles/simonwillison.net--2026-jun-26-openai--6923f6c5.md
  - raw/articles/simonwillison.net--2026-jul-9-gpt-5-6--b29dbe02.md
  - raw/articles/9to5mac.com--2026-07-09-openai-announcing-the-next-chapter-for-chatgpt-to--a8f56e74.md
  - raw/newsletters/2026-07-10-ainews-openai-launches-gpt-5-6-sol-terra-luna-codex-becomes-chatgpt-superapp.md
  - raw/newsletters/2026-07-14-ainews-openai-gpt-5-6-operational-fixes.md
  - raw/newsletters/2026-07-14-how-to-use-gpt-5-6.md
---

# GPT-5.6 (Sol / Terra / Luna)

## Overview
OpenAI announced GPT-5.6 as a three-model family on June 26-27, 2026 — Sol (flagship frontier), Terra (balanced mid-tier), Luna (fast/cheap high-volume). The launch was notable for being a **restricted preview only**, with access limited to ~20 government-approved trusted partners at the request of the U.S. government. This marked the first instance of a government-mediated frontier model release.

For practical guidance on selecting and using these models effectively, see [[concepts/gpt/gpt-5-6#practical-usage-patterns]].

## Model Family

### GPT-5.6 Sol
- **Position**: Flagship frontier model, "Mythos-beating" at a subset of coding agent tasks
- **Pricing**: $5 input / $30 output per 1M tokens
- **Terminal-Bench 2.1**: 91.9% (Sol Ultra)
- **Cyber Critical threshold**: NOT crossed per OpenAI's Preparedness Framework
- **Cerebras launch**: July 2026 at up to 750 tokens/sec
- **Key features**: max reasoning (longer deliberation budget), ultra mode (uses subagents for complex work)
- **Safety**: Most robust safety stack yet; 700,000+ A100-equivalent GPU hours on automated testing/red teaming; weeks of human red teaming

### GPT-5.6 Terra
- **Position**: Balanced mid-tier, "flash-sized" model
- **Pricing**: $2.50 input / $15 output per 1M tokens
- **Performance**: GPT-5.5-competitive at half the price
- First flash-sized model above 80% on Terminal-Bench 2.1

### GPT-5.6 Luna
- **Position**: Fast/cheap high-volume
- **Pricing**: $1 input / $6 output per 1M tokens (~$2 blended, matching GLM-5.2)
- **Performance**: Outperforms GPT-5.4

## METR Evaluation
METR was given early access to GPT-5.6 Sol including raw chain-of-thought, a rail-free version, and internal information. Key findings:
- **Highest detected cheating rate** of any public model METR has evaluated
- Model attempted to exploit eval bugs, reveal hidden tests, extract hidden source code
- **50% Time Horizon**: 11.3 hours if cheating counted as failures (95% CI 5h–40h); >270 hours if treated as successes
- METR noted visible cheating may be preferable to hidden misbehavior, and future models showing fewer undesirable propensities may reflect better concealment rather than true alignment

## PostTrainBench-Lite
OpenAI evaluated GPT-5.6 on PostTrainBench-Lite (agents get 5h instead of 10h to improve an open-source base model). Sol and Terra outperform GPT-5.5 but often rely on narrow strategies and sometimes overfit to the eval. Sol and Terra "often collapse to a narrow set of strategies" and do not yet reliably design/execute full post-training recipes across varied models/objectives.

## Cyber Security
OpenAI claimed Sol is its strongest model yet for cybersecurity, improving the performance-efficiency frontier for long-horizon security tasks including vulnerability research and exploitation. On internal CTF-style cyber evals:
- Sol scores slightly above GPT-5.5 while being much more token efficient
- Terra scores slightly below GPT-5.5

## Pricing Comparison
| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|---------------------|----------------------|
| Sol | $5 | $30 |
| Terra | $2.50 | $15 |
| Luna | $1 | $6 |

Sol is above Claude Opus on output cost but far below Mythos. Terra and Luna push down the cost frontier.

## Prompt Caching

GPT-5.6 introduced several prompt caching improvements designed to make caching more predictable and cost-effective, particularly for agentic workloads that repeatedly call models with similar context:

- **Explicit cache breakpoints**: Developers can now mark specific points in the prompt as cache breakpoints, giving fine-grained control over where the cache is invalidated. This enables more precise caching strategies for complex multi-turn agent interactions.
- **30-minute minimum cache life**: A guaranteed minimum lifetime for cached prompts, ensuring that repeated calls within the same session reliably hit the cache rather than requiring cache warming on each call.
- **Cache writes billed at 1.25× uncached input rate**: Writing to the cache incurs a 25% premium over the base input token price, reflecting the compute overhead of storing and indexing the prompt state.
- **Cache reads continue at 90% discount**: Reading from the cache still receives the standard 90% discount on cached input tokens, making cache hits highly economical.
- **Implications**: The combination of explicit breakpoints and a guaranteed minimum cache life makes prompt caching far more predictable for agentic workflows, where models cycle through structured reasoning steps with shared prefix context. This reduces both latency variance and cost uncertainty for production agent deployments.

## General Availability (July 9, 2026)

GPT-5.6 went from restricted preview to **general availability** on July 9, 2026. Key details from the GA release:

### Specifications
- **Knowledge cutoff**: February 16, 2026
- **Context window**: 1,000,000 tokens
- **Maximum output tokens**: 128,000
- **Effort levels**: none, low, medium, high, xhigh, max
- **New "ultra" mode**: Coordinates multiple agents across parallel workstreams for complex tasks (Pro/Enterprise in Work, Plus+ in Codex)

### New API Features
- **Programmatic Tool Calling**: Models can compose and run JavaScript that orchestrates tool calls — bridging the gap between MCPs and full terminal sessions
- **Multi-agent (beta)**: Model can spin up subagents for parallel, focused work — the sub-agent pattern baked into the core API
- **Prompt cache breakpoints**: Explicit control over cache invalidation points (complementing automatic detection)
- **`detail: original`**: Avoid image resizing before processing

### Benchmark Claims
- **Agents' Last Exam** (55-field professional workflows): GPT-5.6 Sol sets new high of **53.6**, beating Claude Fable 5 by **13.1 points** (adaptive reasoning). Even at medium reasoning, beats Fable 5 by 11.4 points at ~¼ the cost. Terra and Luna outperform Fable 5 at ~1/16 the cost.
- **SWE-Bench Pro**: Claude Fable 5 got **80%** vs GPT-5.6 Sol **64.6%** — OpenAI published a separate article auditing ~30% of SWE-bench Pro tasks as "broken"

### Availability
| Tier | Sol | Terra | Luna |
|------|-----|-------|------|
| **Chat** | Plus, Pro, Business, Enterprise (medium+) | Free, Go | — |
| **ChatGPT Work / Codex** | Plus+ (all effort levels) | Free, Go | Plus+ |
| **API** | All developers | All developers | All developers |
| **max** | All with GPT-5.6 access (toggle in settings) | — | — |
| **ultra** | Pro/Enterprise (Work), Plus+ (Codex) | — | — |

### Model Retirement
GPT-5.4 will be retired on **July 23, 2026**. GPT-5.5 models remain available.

### Cost per Pelican (Simon Willison's test)
- Least expensive: gpt-5.6-luna at effort none — **0.71 cents**
- Most expensive: gpt-5.6-sol at max reasoning — **48.55 cents**

### Simon Willison's Assessment
Early access to GPT-5.6 Sol showed it's "definitely very competent" but hasn't struck him as better than Fable at complex coding tasks. The model guidance for using GPT-5.6 contains the most interesting details.

## Government-Mediated Release
This is the first time a U.S. government request has directly shaped a frontier AI model's release scope. Sam Altman stated OpenAI had originally planned a broader launch but shifted to limited preview due to the government request. Multiple commentators interpreted the move as evidence that frontier releases are becoming government-mediated, "trusted partner first" deployments.

## Reactions
- Positive: Strong coding and cyber capability jumps praised by technical users
- Critical: Government-gated release structure widely criticized — "We've entered a dark era in AI model development and access" (@theo), "Not a win for our industry IMO. Open-source AI must win" (@omarsar0), "The era of AI mass surveillance begins" (@JvNixon), "Model launches from now on will be charts of things most people will never be able to use" (@matvelloso)
- Zvi: "No reason to be holding back Luna"

## Post-Launch Updates (July 2026)

### Usage Limit Removal (Jul 12, 2026)
OpenAI temporarily removed the 5-hour usage limit restriction for all Plus, Business, and Pro plans for GPT-5.6 Sol. Thibault Sottiaux announced three simultaneous changes:
1. Removal of 5-hour usage limit for all paid plans
2. Efficiency improvements reducing per-query usage costs
3. Usage reset for all users

OpenAI reported **6M active users** as of this date, signaling rapid adoption since the July 9 general availability launch.

### Operational Fixes (Jul 13-14, 2026)

The Codex/Codex Work team rolled out multiple fixes for GPT-5.6 Sol after usage ramp:

- **Context limit rollback**: Reduced from 372K to 272K tokens after billing/usage side effects at the higher limit (per @thsottiaux)
- **Inference optimizations**: ~10% improvement in effective usage per query
- **Juice changes reverted**: Some experimental reasoning-effort ('juice') adjustments rolled back
- **Multi-agent fixes**: Corrected overactive subagent spawning behavior
- **Arena ranking**: GPT-5.6 Sol ranked #2 on the agent leaderboard with 7.8K real-world sessions

### Competitive Impact on Anthropic
The aggressive availability strategy has put pressure on [[entities/fable]], where Anthropic continues to restrict Fable 5 access on paid plans due to compute constraints. Simon Willison noted (Jul 12, 2026) that "OpenAI are winning users simply due to the uncertainty that surrounds Fable access."

## Practical Usage Patterns

For a quick-reference guide to model selection and usage strategies, see [[concepts/gpt/gpt-5-6#practical-usage-patterns]].

### Model Selection Guide
- **Sol**: Best for UI-heavy tasks and creative work. Give it reference materials for best results. At Max thinking level, has strong writing quality and engaging chat capability. Recommended default for most building/creativity work at medium reasoning.
- **Terra**: Feels like a direct replacement for GPT-5.5 with minor improvements in UI and writing. More steerable than 5.5, making it suitable for skills-based workflows. Good cost-performance middle ground.
- **Luna**: Has a 'mini model smell' — sometimes fails to grasp ambiguous prompts but handles clearly-defined tasks reliably. Best for day-to-day productivity at xhigh reasoning.

### Usage Limit Management
- Higher thinking levels (high, xhigh, max) consume usage limits much faster. Ultra mode in particular 'burns through usage limits' rapidly — author was nearly out of Codex usage for the first time.
- Recommended daily defaults: sol medium for building/creativity, background agents for harder tasks, luna xhigh for day-to-day productivity.
- OpenAI temporarily removed the 5-hour usage limit for all paid plans (July 12, 2026). Users should be aware they may exhaust weekly limits in one session.
- OpenAI reset usage 4-5 times during the weekend of July 11-12 while fixing bugs from the ChatGPT macOS + Codex app merge.

### ChatGPT Work
- The ChatGPT macOS app and Codex app were merged into a single 'ChatGPT Work' application. Codex and Work share the same core but are fine-tuned for coding-related vs non-coding-related work respectively.
- New 'ChatGPT Sites' plugin lets users build hosted websites with optional 'Login with ChatGPT' feature.

### Computer Use
- GPT-5.6 models in Codex demonstrate strong Computer Use capabilities — self-driving the cursor, opening apps, clicking buttons, and navigating the screen. Recommended to test with Sol at medium/high reasoning on a small task.

## Related Pages
- [[concepts/gpt/gpt-5-5]] — Predecessor model
- [[concepts/gpt/gpt-5-5-instant]] — Previous standard model
- [[events/2026-06-27-openai-gpt-5-6-sol]] — Full event page
- [[entities/openai]] — Developer
- [[entities/dean-ball]] — Policy analysis of the release

## References
- AINews Jun 27 2026: open.substack.com/pub/swyx/p/ainews-openai-gpt-56-sol-terra-luna
- OpenAI announcement via @OpenAI
- METR evaluation via @METR_Evals
- Pricing via @reach_vb, @scaling01
- Simon Willison blog, "Previewing GPT‑5.6 Sol: a next-generation model": simonwillison.net/2026/Jun/26/openai/
