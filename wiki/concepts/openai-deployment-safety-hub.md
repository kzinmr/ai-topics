---
title: OpenAI System Cards (Deployment Safety Hub)
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, system-card, ai-safety, evaluations, preparedness-framework, frontier-models, ai-governance, gpt, model-card, transparency]
sources: [raw/articles/2026-06-10_openai-deployment-safety-hub.md]
---

# OpenAI System Cards (Deployment Safety Hub)

**OpenAI's Deployment Safety Hub** ([deploymentsafety.openai.com](https://deploymentsafety.openai.com/)) is the central repository for all of OpenAI's system cards — safety documentation published alongside every major model and product release. It functions as the single index for understanding how OpenAI evaluates, monitors, and improves the safety of deployed AI systems.

## Hub as Central Index

Unlike [[concepts/anthropic-system-cards]] which lives on Anthropic's main blog, OpenAI maintains a dedicated standalone domain for deployment safety. This architectural choice signals that system cards are treated as a distinct product surface — not blog posts, not press releases, but a structured safety documentation corpus with **20 system cards** spanning from the o-series through the GPT-5 era.

The hub provides:
- **Chronological listing** of all system cards (newest first)
- **Search** across all cards
- **RSS feed** for update notifications
- **Cross-links** to Safety approach, Trust & transparency, and Research portals

## Complete System Card Index

| # | System Card | Date | Type | Key Safety Theme |
|---|---|---|---|---|
| 0 | [o3 and o4-mini](https://deploymentsafety.openai.com/o3-and-o4-mini) | 2025-04-16 | Reasoning | First Preparedness Framework v2; no High threshold reached; reward hacking detected by METR |
| 1 | [GPT-Rosalind-5.5](https://deploymentsafety.openai.com/gpt-rosalind-5-5) | 2026-06-03 | Domain-specific | Bio/Chem High capability; research-only deployment |
| 2 | [GPT-5.5 Instant](https://deploymentsafety.openai.com/gpt-5-5-instant) | 2026-05-05 | Instant model | First Instant model treated as High in Cyber + Bio/Chem |
| 3 | [GPT-5.5](https://deploymentsafety.openai.com/gpt-5-5) | 2026-04-23 | Flagship | Complex real-world work; tool use; code + research |
| 4 | [ChatGPT Images 2.0](https://deploymentsafety.openai.com/chatgpt-images-2-0) | 2026-04-21 | Image generation | Thinking mode for image gen; web search integration |
| 5 | [GPT-5.4 Thinking](https://deploymentsafety.openai.com/gpt-5-4-thinking) | 2026-03-05 | Reasoning | First general-purpose model with High Cyber mitigations |
| 6 | [GPT-5.3 Instant](https://deploymentsafety.openai.com/gpt-5-3-instant) | 2026-03-02 | Instant model | Faster responses; same safety as GPT-5.2 Instant |
| 7 | [GPT-5.3-Codex](https://deploymentsafety.openai.com/gpt-5-3-codex) | 2026-02-05 | Agentic coding | First launch treated as High in Cybersecurity |
| 8 | [GPT-5.2-Codex](https://deploymentsafety.openai.com/gpt-5-2-codex) | 2025-12-18 | Agentic coding | Addendum to GPT-5.2; project-scale tasks |
| 9 | [GPT-5.2](https://deploymentsafety.openai.com/gpt-5-2) | 2025-12-11 | Model family | Update to GPT-5; same safety approach as GPT-5.1 |
| 10 | [GPT-5.1-Codex-Max](https://deploymentsafety.openai.com/gpt-5-1-codex-max) | 2025-11-18 | Agentic coding | Agent sandboxing; configurable network access |
| 11 | [GPT-5.1 Instant & Thinking](https://deploymentsafety.openai.com/gpt-5-1) | 2025-11-12 | Addendum | Next iteration of GPT-5 series |
| 12 | [GPT-5.1-Codex](https://deploymentsafety.openai.com/gpt-5-1-codex) | 2025-10-23 | Agentic coding | — |
| 13 | [GPT-5-Codex](https://deploymentsafety.openai.com/gpt-5-codex) | 2025-10-09 | Agentic coding | — |
| 14 | [Sora 2](https://deploymentsafety.openai.com/sora-2) | 2025-09-30 | Video generation | Nonconsensual likeness; photorealistic person restrictions |
| 15 | [GPT-5](https://deploymentsafety.openai.com/gpt-5) | 2025-08-07 | Flagship | Unified system (fast + reasoning); safe-completions; Bio/Chem High |
| 16 | [gpt-oss-120b & gpt-oss-20b](https://deploymentsafety.openai.com/gpt-oss) | 2025-08-05 | Open-weight | Apache 2.0; adversarial fine-tuning tested; model card (not system card) |
| 17 | [ChatGPT Agent](https://deploymentsafety.openai.com/chatgpt-agent) | 2025-07-17 | Agentic | Deep research + Operator + terminal; Bio/Chem High (precautionary) |
| 18 | [4o Native Image Generation](https://deploymentsafety.openai.com/4o-native-image-generation) | 2025-03-25 | Image generation | Addendum to GPT-4o; photorealistic output |
| 19 | [Deep Research](https://deploymentsafety.openai.com/deep-research) | 2025-02-25 | Agentic | Multi-step web research; o3-based; privacy protections |

## Preparedness Framework Categories

OpenAI evaluates models under its **Preparedness Framework** across three tracked categories:

| Category | Threshold Levels | Current Status |
|---|---|---|
| **Biological & Chemical** | Low → Medium → High → Critical | Several models at High (GPT-5, ChatGPT Agent, GPT-Rosalind-5.5) |
| **Cybersecurity** | Low → Medium → High → Critical | First High treatment with GPT-5.3-Codex (Feb 2026) |
| **AI Self-Improvement** | Low → Medium → High → Critical | Not yet reached High for any model |

When a model meets the **High** threshold, OpenAI activates a suite of safeguards including:
- Enhanced monitoring
- Restricted deployment scope
- Safety Advisory Group (SAG) review
- External red teaming

## Key Evolution Trends

### Safety Level Escalation
- **2025 H1**: Deep Research, 4o Image Gen — standard evaluations, no special Preparedness levels
- **2025 H2**: GPT-5 → Bio/Chem High (precautionary); ChatGPT Agent → Bio/Chem High; gpt-oss → adversarial fine-tuning testing
- **2026 Q1**: GPT-5.3-Codex → first **Cybersecurity High** treatment
- **2026 Q2**: GPT-5.5 Instant → both Cyber and Bio/Chem High; GPT-Rosalind-5.5 → domain-specific Bio/Chem High

### Agentic Model Proliferation
The Codex series (GPT-5-Codex → 5.1-Codex → 5.1-Codex-Max → 5.2-Codex → 5.3-Codex) shows rapid iteration on agentic coding models, each with its own system card documenting:
- Agent sandboxing architecture
- Network access controls
- Terminal and code execution safety
- Prompt injection resistance

### Open-Weight Model Documentation
The gpt-oss model card is notably labeled a **model card** (not system card), acknowledging that open-weight models will be used in diverse systems by diverse stakeholders. The adversarial fine-tuning testing — confirming that even robust fine-tuning doesn't reach High capability — sets a precedent for open model safety documentation.

### Domain-Specific Deployment
GPT-Rosalind-5.5 (biology/drug discovery) represents a new pattern: **domain-restricted deployment** with access limited to qualified scientists, research institutes, and government partners. This is a departure from the general-availability model used for GPT-5.x.

## Comparison with Anthropic System Cards

| Dimension | OpenAI | [[concepts/anthropic-system-cards\|Anthropic]] |
|---|---|---|
| **Hosting** | Dedicated subdomain (deploymentsafety.openai.com) | Main site (anthropic.com/system-cards) |
| **Naming** | "System Card" (all models) | "System Card" (all models) |
| **Safety Framework** | Preparedness Framework (3 tracked categories) | Responsible Scaling Policy (ASL-2 through ASL-4) |
| **Coverage** | 19 cards (Feb 2025 – Jun 2026) | 15 cards (Jul 2023 – May 2026) |
| **Open-weight** | Yes (gpt-oss model card) | No |
| **Domain-specific** | Yes (GPT-Rosalind for biology) | No |
| **Agentic focus** | Strong (5 Codex-specific cards) | Growing (Claude Code, computer use) |
| **External audits** | Government red teaming, bug bounty | UK AISI, third-party evaluators |

## See Also

- [[concepts/model-cards-system-cards]] — General framework for model/system cards
- [[concepts/anthropic-system-cards]] — Anthropic's parallel system card index
- [[entities/openai]] — OpenAI entity page
- [[concepts/openai-frontier-governance-framework]] — OpenAI's governance approach
- [[concepts/codex-safety-at-openai]] — Codex-specific safety considerations
