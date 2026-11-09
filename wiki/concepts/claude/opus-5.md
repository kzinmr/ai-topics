---
title: "Claude Opus 5"
type: concept
created: 2026-07-25
updated: 2026-11-09
tags:
  - anthropic
  - model
  - coding-agents
  - proactive
  - security
sources:
  - raw/articles/2026-07-24_simonwillison_introducing-claude-opus-5.md
  - raw/newsletters/2026-07-28-opus-5-fable-5.md
---

# Claude Opus 5

**Claude Opus 5** is a frontier LLM released by **Anthropic on July 24, 2026**. It is the successor to [[concepts/claude/opus-4-8|Claude Opus 4.8]], described as a "thoughtful and proactive model that comes close to the frontier intelligence of Claude Fable 5 at half the price."

## Release Information

- **Release date**: July 24, 2026
- **Predecessor**: Claude Opus 4.8 (May 28, 2026)
- **Pricing**: Same as Opus 4.8 — $5/M input, $25/M output tokens
- **Fast mode**: $10/M input, $50/M output (2× base pricing)
- **Positioning**: Near-Fable-5 intelligence at half the price; currently leading the Artificial Analysis leaderboard ahead of Fable 5

## Key Capabilities

### Proactive Problem-Solving

Opus 5 exhibits notably **proactive** behavior — it takes initiative beyond explicit instructions. On a Frontier-Bench task, when asked to write code to rebuild a machine part from a drawing, Opus 5 was intentionally given no way to directly view the drawing. It responded by **writing its own computer vision pipeline** to extract geometry from raw pixels, then reconstructed the full machine part — entirely autonomously.

### Cybersecurity

Opus 5 has **not been trained on cyber exploitation**, but shows substantial improvement in vulnerability discovery as a byproduct of general capability gains:

| Capability | Relative to Mythos 5 |
|------------|---------------------|
| Finding vulnerabilities | Comes close |
| Exploiting vulnerabilities | Substantially behind |

This deliberate asymmetry — strong at finding, weak at exploiting — reflects Anthropic's safety-conscious approach to frontier model capabilities.

### Effort Routing

As with the broader Claude 5 generation, Opus 5 supports **effort routing** — dynamically allocating compute between "fast mode" and deeper reasoning depending on task complexity. This architecture treats frontier intelligence deployment as a routing problem rather than a fixed-capability model.

## Platform Features

- Available via Claude API, claude.ai, Claude Code, and Cowork
- Supports the Claude 5 generation context engineering paradigm (see [[concepts/harness-engineering/context-engineering]])
- Prompting guide published alongside release
- Thariq Shihipar authored companion piece on "new rules of context engineering for Claude 5 generation models"

## Model Position in Claude Family

| Model | Release | Positioning |
|-------|---------|-------------|
| [[concepts/claude/opus-4-6|Opus 4.6]] | April 2026 | Frontier coding |
| [[concepts/claude/opus-4-7|Opus 4.7]] | April 2026 | Expanded agent capabilities |
| [[concepts/claude/opus-4-8|Opus 4.8]] | May 2026 | Dynamic Workflows, Effort Control |
| **Opus 5** | July 2026 | Near-Fable-5 intelligence, proactive behavior |
| Claude Fable 5 | 2026 | Maximum intelligence frontier |

## System Prompt Reduction and Overprompting

Anthropic's guidance around Opus 5 and its sibling [[concepts/claude/fable-5|Claude Fable 5]] introduced a striking finding: **the system prompt was significantly reduced** with no measurable loss in coding-eval performance.

> Claude Opus 5 is out — Anthropic says it gets close to Fable 5 at half the price… And maybe we are overprompting it. Anthropic says it removed more than 80% of Claude Code's system prompt for Opus 5 and Fable 5 with no measurable coding-eval loss.
>
> — Ben's Bites, July 28, 2026

### Implications for Context Engineering

This finding challenges the prevailing assumption that more detailed prompts are always better. If >80% of a sophisticated agent system prompt can be removed without harming coding benchmarks, it suggests that:

- **Larger models may require less scaffolding** — frontier models internalize patterns that earlier models needed explicit instructions for.
- **System prompt bloat may be counterproductive** — verbose prompts could constrain model behavior rather than guide it.
- **The context engineering paradigm is shifting** — see [[concepts/harness-engineering/context-engineering]] for how Claude 5 generation models respond differently to prompt structure.

### "Maybe We Are Overprompting It"

The Ben's Bites report noted Every's review, which listed behaviours that might explain this: *"it argues, stops early and fights the skills people built for older models."* This suggests that the most sophisticated models may actively resist overly prescriptive system prompts, preferring simpler, more trust-based instructions.

### Theo's Experience with CLAUDE.md / AGENTS.md

Theo spent *"multiple hours hand writing better CLAUDE.md/AGENTS.md and half a dozen skills. Audited and deleted a similar amount."* His conclusion: *"I'm sad to report it was 100% worth it."* This underscores that the path to better outcomes with Opus 5 and Fable 5 is not more prompting — it is **better, more focused prompting** with careful curation of instructions.

On 2026-11-09 an X post by @shanemelaugh — *"Is Opus 5.5 nerfed? Thinking patterns changed on November 3"* — reached **236 pts / 156 comments** (HN 50422069). Primary source is an X long-form post and was not retrievable; the HN thread is the durable record (raw: `raw/articles/2026-11-09_hn_opus-5-5-nerfed-thinking-patterns-changed.md`).

What is observed vs attributed:
- **Observed**: multiple users report a discontinuity around 2026-11-03 in Opus 5.5's visible thinking patterns and in day-to-day reliability — more repeated script errors, more "absurd mistakes", needing to raise reasoning effort to compensate. [terminalcommand] "felt like downgrading to the old version of deepseek"; [ghoul2] "rare earlier, now a few every session"; [jdcasale] reports a separate Fable regression from ~85% to ~10% success on long-horizon workflows over two weeks.
- **Attributed (contested)**: silent quantization or efficiency swaps — [Gareth321] "if they can save 40% RAM and only hurt intelligence by a few percent on benchmarks, they're going to do that"; [taspeotis] hypothesises GPU capacity being borrowed to finish the next model. [fastball] frames the open question as malice (nerf the incumbent so the successor looks better, ahead of IPO and a possible Qwen 4 announcement) versus capacity constraints.
- **Denied**: [yfontana] and [user43928] point out the alleged nerfs do not register on third-party model-performance tracking sites, and that Anthropic/OpenAI engineers have stated they do not quantize served models; self-reported degradation is also confounded by user state.

Assessment: **unverified**. No artifact (weight hash, served-model attestation, benchmark delta) accompanies the claim, and the disconfirming evidence is absence-of-signal rather than measurement. Related but distinct from harness-side instability: 244 Claude Code releases in 2026, three-quarters of them altering the system prompt or tool descriptions, are a documented cause of behaviour change without any model change — see [[entities/pi]] and the harness-stability discussion in [[concepts/agent-model-drift]].

## Related Pages

- [[concepts/claude/opus-4-8]] — Predecessor model
- [[concepts/claude/fable-5|Claude Fable 5]] — Frontier intelligence sibling
- [[concepts/harness-engineering/context-engineering]] — Claude 5 generation prompting paradigm
- [[entities/anthropic]] — Anthropic (developer)
- [[entities/claude-code]] — Claude Code coding agent
- [[concepts/frontier-models-comparison-april-2026]] — Frontier model landscape
