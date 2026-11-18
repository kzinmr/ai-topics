---
title: "Microsoft AI Team"
type: entity
created: 2026-06-20
updated: 2026-07-24
tags:
  - microsoft
  - lab
  - model
  - company
sources:
  - raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md
  - raw/articles/2026-07-23_microsoft-ai_frontier-diffusion-and-control.md
  - https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf
aliases: ["MAI", "Microsoft AI"]
related:
  - entities/microsoft
  - entities/mai-thinking-1
---

# Microsoft AI Team

The **Microsoft AI Team (MAI)** is a research and development group within Microsoft focused on building frontier reasoning models and exploring scaling laws. The team emerged as a significant internal AI research division following Microsoft's renegotiated partnership with [[entities/openai]] in April 2026, which gave Microsoft freedom to develop its own models alongside its Copilot strategy.

## Key Ideas

### MAI-Thinking-1
A 35B active / 1T total parameter MoE model designed for STEM reasoning and coding. See [[entities/mai-thinking-1]] for the full profile.

### Hill-Climbing Machine
A process of treating model development as a system-level optimization problem, using reinforcement learning for rapid iterative improvement. Rather than designing models top-down, MAI frames model development as an empirical optimization process.

### Scaling Laws Research
Focus on empirically-driven improvements to architecture and data scaling.

## Relation to Microsoft

The Microsoft AI Team operates as an internal research division of [[entities/microsoft]], distinct from Microsoft's OpenAI partnership. While Microsoft retains strategic ties to OpenAI (with IP license through 2032), MAI represents Microsoft's bet on proprietary in-house model development — paralleling investments by [[entities/google-deepmind]] and [[entities/meta-ai]].

## Related Concepts
- [[entities/mai-thinking-1]] — MAI flagship reasoning model
- [[entities/microsoft]] — Parent company
- [[concepts/post-training/reinforcement-learning]] — Core training methodology
- [[concepts/mixture-of-experts]] — Model architecture
- [[concepts/mai-thinking]] — Hill-climbing approach concept

## Frontier Diffusion & Control Strategy (July 2026)

In July 2026, Microsoft AI CEO Mustafa Suleyman published "[Frontier Diffusion & Control](https://x.com/i/article/2080328073724260352)," outlining the team's strategy for optimizing the cost-to-outcome frontier across Microsoft's product ecosystem.

### Core Strategy: Hill-Climbing System

MAI frames model deployment as a **hill-climbing system** where the model is only one part of a larger optimization engine. The full system includes:

- **Harness**: The product-specific agent infrastructure surrounding the model
- **Memory**: Persistent context and state management
- **Context**: Task-specific information and environment
- **Tools and Skills**: Capabilities externalized outside the model
- **User Interactions**: Real-world feedback signals

This architecture ensures that evals continue to improve even when any given model is replaced — achieving **model independence**. By externalizing harness, memory, context, and skills outside the model, the system is not locked to any single model provider.

### In-Product RLEs (Reinforcement Learning Environments)

Rather than training models in abstract settings, MAI builds **Reinforcement Learning Environments inside the actual product harness**. Models are trained and rewarded based on completing real customer tasks against the same infrastructure they'll encounter in production. This contrasts with traditional RLHF, which operates in a separate, simplified feedback loop disconnected from real usage patterns.

Model independence and product-specific evals give MAI "a direct hill to climb, and to keep refining until we reach the right quality-cost target." MAI models are now outperforming general-purpose frontier models in many use cases while using a fraction of the tokens.

### Products Using MAI

Microsoft is routing traffic to MAI models across its first-party surfaces where they match or outperform frontier alternatives:

- **GitHub Copilot** — Code completion and generation
- **Excel** — Data analysis and formula generation
- **Outlook** — Email and calendar assistance
- **Copilot Chat** — General-purpose AI assistant
- **PowerPoint** — Presentation creation

### Enterprise Template Thesis

The approach Microsoft takes with its first-party products serves as a **template for enterprise customers**. Using [[entities/microsoft|Microsoft]] Foundry and the MAI toolchain, any enterprise can build their own proprietary [[concepts/enterprise-rle|RLEs]] with:

- Proprietary evals tuned to their domain
- Custom workflows and context
- Model-independent harness architecture
- Continuous hill-climbing against their own quality-cost targets

This extends frontier AI diffusion beyond Microsoft's products into the broader enterprise ecosystem.

## MAI Code 2 & Code 2 Flash (November 17, 2026)

Two new coding models aimed at **everyday enterprise coding tasks at scalable prices**, explicitly *not* tuned for fundamental science or very long-horizon agentic work. Launched in GitHub Copilot; Code 2 Flash in limited-access preview in Microsoft Foundry, with OpenRouter/Vercel/Hermes/OpenCode/Kilo promised soon ([[entities/microsoft]]'s first broad third-party distribution for MAI).

- **MAI Code 2** — frontier price-performance for common enterprise tasks: production-ization, deep debugging, multi-file implementation, repo-wide reasoning, UI. Averaged over DeepSWE 1.1, TerminalBench 2.1, SWE-Atlas and FrontierCode v1.1 (run on MSBench with GitHub Copilot CLI, max reasoning effort): **98% of GPT-6.1 Sol at 40% of the cost; 96% of Claude Opus 5.5 at 5% of the cost**. Blind frontend evals (258 annotators): preferred over GPT-6 Sol 64% of the time.
- **MAI Code 2 Flash** — high-volume routine work (explanations, targeted edits, fixes): comparable to GPT-6 Luna and Claude Haiku 5.5 at 65% / 20% of the cost across three day-to-day coding benchmarks.
- **MAI Work Flash** — a Code-2-Flash-derived single model now serving M365 + Fabric IQ: on par with GPT-6 Luna on Excel/PowerPoint internal benchmarks, ~GPT-6.1-Sol quality on Word with ~42% fewer input tokens, beats GPT-6 Luna on Teams instruction-following/tool-calling with up to 28% fewer tokens.
- Also announced: **MAI Cyber 2 Flash** ("leading security, lower cost") as part of a "seven new world-class models at scalable price-performance" line.

All comparisons are Microsoft-internal (MSBench; Artificial Analysis for FrontierCode; costs at a 50% promotional price) — vendor-reported. Strategically, this is the Frontier Diffusion thesis in action: cheaper task-specific models replacing OpenAI-dependent frontier calls inside Microsoft's own harnesses (see [[concepts/enterprise-rle]]).

## Sources
1. [MAI-Thinking-1: Building a Hill-Climbing Machine -- Microsoft AI Technical Report](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
2. [Frontier Diffusion & Control -- Mustafa Suleyman, Microsoft AI](https://x.com/i/article/2080328073724260352) (July 23, 2026)
3. [MAI Code 2 and Code 2 Flash: Everyday coding at scalable prices](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) (Nov 17, 2026; raw: raw/articles/2026-11-17_microsoft-ai_mai-code-2.md)
