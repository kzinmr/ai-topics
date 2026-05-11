---
title: Bespoke Labs
created: 2026-05-08
updated: 2026-05-08
type: entity
tags:
  - company
  - open-source
  - training
  - ai-agents
  - reinforcement-learning
aliases: [bespokelabs, BespokeLabs.AI]
sources: [raw/articles/2026-05-08_bespokelabs_multi-turn-tool-use-rl.md]
related:
  - concepts/multi-turn-tool-use-rl
  - concepts/bfcl-v3
  - concepts/grpo
---

# Bespoke Labs

AI research company focused on **agent optimization** through cutting-edge research on environments, data curation, and evolutionary algorithms. Builds tools and datasets for the open-source AI community.

| Field | Details |
|---|---|
| **Founded** | 2024 (inferred) |
| **Location** | San Francisco Bay Area |
| **Website** | [bespokelabs.ai](https://www.bespokelabs.ai) |
| **GitHub** | [github.com/bespokelabsai](https://github.com/bespokelabsai) |
| **HuggingFace** | [huggingface.co/bespokelabs](https://huggingface.co/bespokelabs) |
| **X/Twitter** | [@bespokelabsai](https://x.com/bespokelabsai) |
| **Key People** | Richard Zhuang, Trung Vu, Alex Dimakis, Maheswaran Sathiamoorthy |
| **Funding** | Fortune 500 enterprise customers; Lambda Labs, NSF IFML, JSC, TRI (research support) |

## Mission

> "Ship Reliable Agents" — optimize agents for Fortune 500 enterprises and frontier labs.

Bespoke Labs argues that manual prompt engineering doesn't scale for complex agent orchestration. Their approach advocates for **scalable methods like RL** to teach agents tool use, rather than relying on human-crafted rules or expensive human demonstrations.

## Products & Projects

### Curator
Open-source Python library for **synthetic data curation** at scale. Supports bulk inference via LiteLLM, vLLM, and popular batch APIs (Gemini, etc.). Used to create major open reasoning datasets.

- **GitHub**: [bespokelabsai/curator](https://github.com/bespokelabsai/curator) — 2.9k+ stars
- **Features**: Structured output support, async operations, caching, fault recovery, CLI viewer
- Used to create: OpenThoughts-114k, Bespoke-Stratos-17k, OpenThoughts2-1M, OpenThoughts-Agents

### OpenThoughts
Community-driven effort to curate the best **open post-training datasets**. Collaboration with Stanford, UC Berkeley, University of Washington, JSC, LAION, UCLA, UNC Chapel Hill, and Toyota Research Institute.

- **Website**: [openthoughts.ai](https://openthoughts.ai)
- **Key datasets**: OpenThoughts-114k, OpenThoughts2-1M, OpenThoughts3 (accepted to ICLR 2026)
- **Models trained**: OpenThinker2-32B (outperforms DeepSeek-R1-32B)
- **Active project**: OpenThoughts-Agents (best open agent training datasets)

### Evalchemy
Evaluation framework for AI agents. (GitHub: [mlfoundations/evalchemy](https://github.com/mlfoundations/evalchemy))

## Research

Bespoke Labs has papers accepted to **ICLR 2026** in multiple tracks:

| Paper | Topic | Venue |
|---|---|---|
| OpenThoughts | Open reasoning datasets (used by 200+ model builders) | ICLR 2026 |
| TerminalBench | Benchmark for terminal/CLI agents | ICLR 2026 |
| GEPA | Evolutionary algorithms for agent optimization | ICLR 2026 |

### Multi-Turn Tool Use with RL (April 2025)
Improved Qwen2.5-7B-Instruct by **+23%** (55% → 78%) on BFCL multi-turn tool use benchmark using GRPO with only 100 training samples. Demonstrated that agents can learn to **orchestrate multiple tools** without a single human or teacher model demonstration. Key findings:
- Simple binary reward (correctness) outperforms complex multi-component rewards
- Overlong filtering + small KL weight (0.001) prevents completion length blowup
- Reference model update every 100 steps boosts performance

→ See [[concepts/multi-turn-tool-use-rl]]

## Partners & Supporters

| Partner | Role |
|---|---|
| Lambda Labs | Compute sponsor |
| NSF IFML | Research funding |
| Jülich Supercomputing Center | Compute infrastructure |
| Toyota Research Institute | Research collaboration |

## External Links
- [Blog](https://www.bespokelabs.ai/blog)
- [Discord](https://discord.com/invite/KqpXvpzVBS)
- [LinkedIn](https://www.linkedin.com/company/104375224)
