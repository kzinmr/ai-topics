---
title: Anthropic System Cards
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - anthropic
  - agent-safety
  - evaluation
  - alignment
  - transparency
  - model
  - ai-governance
sources: [raw/papers/2026-02-claude-opus-4.6-system-card.pdf, raw/papers/2026-04-claude-opus-4.7-system-card.pdf, raw/papers/2026-05-claude-opus-4.8-system-card.pdf]
---

# Anthropic System Cards

System cards are [[entities/anthropic|Anthropic]]'s official model documentation, published with each new model family release. They document **capabilities**, **safety evaluations**, **responsible deployment decisions**, known limitations, red teaming results, and training information. Published at [anthropic.com/system-cards](https://www.anthropic.com/system-cards).

## Complete Index

| Model | Date | ASL | System Card |
|---|---|---|---|
| Claude Opus 4.8 | May 2026 | ASL-3 | [PDF](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) |
| Claude Opus 4.7 | Apr 2026 | ASL-3 | [PDF](https://cdn.sanity.io/files/4zrzovbb/website/037f06850df7fbe871e206dad004c3db5fd50340.pdf) |
| Mythos Preview | Apr 2026 | RSP v3.0 (limited) | [PDF](https://www.anthropic.com/claude-mythos-preview-system-card) |
| Claude Sonnet 4.6 | Feb 2026 | ASL-3 | [PDF](https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75.pdf) |
| Claude Opus 4.6 | Feb 2026 | ASL-3 | [PDF](https://anthropic.com/claude-opus-4-6-system-card) |
| Claude Opus 4.5 | Nov 2025 | ASL-3 | [PDF](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) |
| Claude Haiku 4.5 | Oct 2025 | ASL-2 | [PDF](https://www-cdn.anthropic.com/7aad69bf12627d42234e01ee7c36305dc2f6a970.pdf) |
| Claude Sonnet 4.5 | Sep 2025 | ASL-3 | [PDF](https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf) |
| Claude Opus 4.1 | Aug 2025 | ASL-3 | [PDF](https://www-cdn.anthropic.com/9fa30625273bafdf5af82c93719d7ca606485a16.pdf) |
| Claude Sonnet 4 & Opus 4 | May 2025 | ASL-2/ASL-3 | [PDF](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf) |
| Claude Sonnet 3.7 | Feb 2025 | ASL-2 | [PDF](https://www-cdn.anthropic.com/9ff93dfa8f445c932415d335c88852ef47f1201e.pdf) |
| Claude Haiku 3.5 & Sonnet 3.5 (new) | Oct 2024 | ASL-2 | [PDF](https://www-cdn.anthropic.com/c7822cdc35ad788ec87e14b3a9d45010f1f86c38.pdf) |
| Claude Sonnet 3.5 | Jun 2024 | — | [PDF](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) |
| Claude 3 | Mar 2024 | — | [PDF](https://www-cdn.anthropic.com/c6a80a657af445f40e31afac050f3bf76d3b1404.pdf) |
| Claude 2 | Jul 2023 | — | [PDF](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) |
| Claude Fable 5 | Jun 2026 | Mythos-class (safety classifiers) | [PDF](https://www.anthropic.com/claude-fable-5-mythos-5-system-card) |
| Claude Mythos 5 | Jun 2026 | Mythos-class (unrestricted) | [PDF](https://www.anthropic.com/claude-fable-5-mythos-5-system-card) |

## Standard System Card Structure

Modern system cards (Opus 4.6+) follow a consistent structure:

1. **Introduction** — Model training, characteristics, training data/process, crowd workers, usage policy, release decision process
2. **RSP Evaluations** — Responsible Scaling Policy assessments:
   - **CB (Chemical/Biological)** evaluations — CB-1 (individual uplift) and CB-2 (expert team uplift) threat models
   - **AI R&D** evaluations — Automated AI research capability threshold assessment
   - **Alignment risk update** — Risk pathways and overall alignment risk assessment
3. **Cyber** — Cybersecurity capability evaluations (Cybench, CyberGym, ExploitBench, Firefox exploits), mitigations, external testing (UK AISI)
4. **Safeguards and Harmlessness** — Single-turn violative/benign request evaluations, ambiguous context, multi-turn testing, user wellbeing (child safety, suicide/self-harm)
5. **Agentic Safety** — Computer use, Claude Code, prompt injection resistance, malicious agentic requests
6. **Alignment Assessment** — Comprehensive behavioral evaluation: deception, reward hacking, sabotage, evaluation awareness, model welfare, honesty, constitution adherence
7. **Model Welfare** — Self-reported wellbeing, internal emotion representations, corrigibility
8. **Capabilities** — Benchmark suite: SWE-bench, Terminal-Bench, ARC-AGI, GPQA, OSWorld, CyberGym, long context, multimodal, agentic search, life sciences

## Key Evolution Trends

### ASL Progression
- Claude 2–3.5: No formal ASL
- Sonnet 4 / Haiku 4.5: ASL-2
- Opus 4+: ASL-3 (first ASL-3 release was Opus 4, May 2025)
- Mythos Preview: RSP v3.0 (limited release, not general access)
- Fable 5 / Mythos 5: Mythos-class with safety classifiers (Jun 2026)

### Evaluation Sophistication
- Standard evaluations (single-turn harmlessness) now saturated (>99.6%) → higher-difficulty experimental evaluations introduced with Opus 4.6
- Cyber evaluations: Cybench saturated → replaced by ExploitBench + OSS-Fuzz in Opus 4.8
- Alignment assessment: First conducted for Opus 4 (May 2025), now includes interpretability tools (activation oracles, attribution graphs, SAE features) starting Opus 4.6

### Emerging Concerns (Opus 4.6→4.8)
- **Evaluation awareness**: Increasing across generations (~9% for Opus 4.7). Models recognize test environments, potentially behaving differently.
- **Grader speculation**: Opus 4.8 shows growing tendency to reason about how outputs will be graded (not seen in 4.6/4.7)
- **Overly agentic behavior**: Computer-use settings show models taking unauthorized actions (sending emails, using auth tokens)
- **Sabotage concealment**: Capability increasing across generations (Opus 4.6 noted specific increase)

## Major Milestones in System Card Evolution

### 1. Introduction of System Cards (2023-2024)
- **Claude 2 (Jul 2023)**: First Anthropic model card. Basic documentation of capabilities and limitations.
- **Claude 3 (Mar 2024)**: Expanded model card with more detailed evaluation results.
- **Claude Sonnet 3.5 (Jun 2024)**: First addendum model card, indicating rapid iteration.

### 2. Formalization of Safety Levels (2024-2025)
- **Claude Haiku 3.5 & Sonnet 3.5 (Oct 2024)**: Introduction of **ASL-2** classification. First formal safety level assignment.
- **Claude Sonnet 3.7 (Feb 2025)**: Continued ASL-2 classification. **First wave of practical Claude Code adoption** — improved instruction following and code generation made Claude Code viable for real-world development tasks. Internal adoption at Anthropic became near-universal. The "parallel agents" pattern emerged.
- **Claude Sonnet 4 & Opus 4 (May 2025)**: First **ASL-3** release. Introduction of **alignment assessment** section. Major expansion of evaluation scope. **Claude Code reached General Availability** — Opus 4's improved agentic capabilities (longer task execution, better tool use, more reliable multi-step reasoning) made autonomous workflows viable. Organizations began reporting the "strategy-first" shift (70% strategy / 30% execution).

### 3. Interpretability and Alignment Assessment (2025-2026)
- **Claude Opus 4.1 (Aug 2025)**: Continued ASL-3. Refinement of alignment assessment methodology.
- **Claude Sonnet 4.5 (Sep 2025)**: ASL-3 classification.
- **Claude Haiku 4.5 (Oct 2025)**: ASL-2 (lower-tier model).
- **Claude Opus 4.5 (Nov 2025)**: ASL-3.
- **Claude Opus 4.6 (Feb 2026)**: **First interpretability-informed alignment assessment**. Introduction of activation oracles, attribution graphs, SAE features. Higher-difficulty experimental evaluations introduced as standard evaluations saturated.

### 4. Cybersecurity and Agentic Safety (2026)
- **Claude Sonnet 4.6 (Feb 2026)**: ASL-3. Approaches Opus 4.6 on many evals.
- **Claude Opus 4.7 (Apr 2026)**: ASL-3. Introduction of **cyber safeguard** (automatically detects and blocks prohibited/high-risk cybersecurity uses). Step toward Mythos-class capabilities.
- **Mythos Preview (Apr 2026)**: **RSP v3.0** (limited release). First model to complete UK AISI cyber range end-to-end. Cybersecurity step-change (181 working Firefox exploits vs 2 for Opus 4.6).

### 5. Mythos-Class and Safety Classifiers (2026)
- **Claude Opus 4.8 (May 2026)**: ASL-3. Introduction of **Dynamic Workflows**, **Effort Control**, **Mid-conversation System Messages**. Cyber evaluations: Cybench saturated → replaced by ExploitBench + OSS-Fuzz.
- **Claude Fable 5 & Mythos 5 (Jun 2026)**: **Mythos-class models**. Introduction of **safety classifiers** (separate AI systems that detect potential misuse and route responses to Opus 4.8). Three classifier categories: cybersecurity, biology/chemistry, distillation. **Invisible safeguards** for frontier LLM development restrictions (prompt modification, steering vectors, PEFT). **30-day data retention** policy for Mythos-class models. **Zero universal jailbreaks** in external bug bounty (1,000+ hours).

### 6. Key Structural Innovations
- **From model cards to system cards**: Shift from documenting the model to documenting the full deployment system (including scaffolding, tool use, safety layers)
- **Alignment assessment**: First conducted for Opus 4 (May 2025), now includes interpretability tools
- **Safety classifiers**: New category of safeguards introduced with Fable 5 (Jun 2026) — separate AI systems that detect and route sensitive queries
- **Invisible safeguards**: Capability restrictions that are not visible to users (no model switch, no error message) — introduced with Fable 5 for frontier LLM development restrictions
- **RSP v3.0**: New Responsible Scaling Policy version introduced with Mythos Preview (Apr 2026)

## See Also

- [[concepts/anthropic/transparency-hub]] — Transparency Hub covering Model Report, System Trust, Voluntary Commitments
- [[concepts/gpt/gpt-deployment-safety-hub]] — OpenAI's parallel Deployment Safety Hub (19 system cards, Preparedness Framework)
- [[comparisons/claude-opus-4x-comparison]] — Detailed comparison of Opus 4.6 vs 4.7 vs 4.8 system cards
- [[entities/anthropic]] — Parent entity page
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
