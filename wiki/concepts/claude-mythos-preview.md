---
title: "Claude Mythos Preview"
created: 2026-04-13
updated: 2026-04-13
tags: [concept, anthropic, frontier-models, cybersecurity, red-team, dual-use]
aliases: ["mythos preview", "anthropic frontier red team 2026"]
related:
  - concepts/anthropic-openclaw-conflict
  - entities/dario-amodei
  - concepts/ai-agent-engineering
---

# Claude Mythos Preview

## Overview

**Claude Mythos** is Anthropic's next-generation frontier model series. The first preview was announced on **April 7, 2026**, accompanied by a detailed Frontier Red Team research summary covering cybersecurity, biorisk, nuclear safeguards, and autonomous systems capabilities.

## Key Capabilities (Red Team Findings)

### Cybersecurity

- **Multistage Network Attacks**: Current Claude models can now succeed at multistage attacks on networks with dozens of hosts using only standard, open-source tools — no custom tooling required (a significant shift from previous generations)
- **Smart Contract Vulnerabilities**: Claude Opus 4.5, Claude Sonnet 4.5, and GPT-5 identified exploits worth a combined **$4.6M** on contracts exploited *after* their knowledge cutoffs
- **Cyber Competition Performance**: Claude consistently places in the **top 25%** of human-focused cyber competitions but still trails elite human teams on the most complex challenges
- **Property-Based Bug Hunting**: Custom agent infers general code properties and runs property-based testing; currently reporting bugs in top Python packages (several already patched post-manual validation)

### Model Progression

| Model | Cyber Capability | Notes |
|-------|----------------|-------|
| Claude Sonnet 4.5 | **≥ Opus 4.1** | Matches or eclipses prior generation's top model |
| Claude Opus 4 | Major improvement | Notable gains over prior generations |
| Claude Opus 4.5 | Frontier | Smart contract exploit discovery at $4.6M+ value |

### Autonomous Systems

- **Project Vend** (Phases 1 & 2): Tested Claude autonomously managing an office retail store for ~1 month. Phase 1 underperformed; Phase 2 introduced operational adjustments. Highlights trajectory toward AI-managed real-world commerce, but underscores current robustness gaps.
- **Project Fetch**: Explored AI-to-robotics integration — Claude assisting human operators executing complex physical tasks using a robot dog.

### Dual-Use Risk Management

- **Nuclear Safeguards**: Co-developed classifier with **NNSA & DOE labs** that distinguishes concerning vs. benign nuclear conversations with high preliminary accuracy
- **Biorisk**: AI accelerates biological/medical research but is inherently dual-use. Anthropic positions biorisk evaluation and mitigation as non-negotiable components of responsible AI development

## The "Lockdown" Decision

Anthropic **did not release Claude Mythos publicly**. The preview is restricted to frontier red team research and select partners. This decision was characterized by The Signal Newsletter as a "lockdown" — reflecting Anthropic's cautious approach to releasing capabilities that outpace existing safety frameworks.

> *"The idea of an AI running a business doesn't seem as far-fetched as it once did. But the gap between 'capable' and 'completely robust' remains wide."*
> — Anthropic Frontier Red Team

## Implications

1. **Capability acceleration**: Sonnet 4.5 matching Opus 4.1 in cyber skills demonstrates rapid model improvement within a single tier
2. **Infrastructure shift**: Standard open-source tools now sufficient for multistage network attacks — no custom infrastructure needed
3. **Release caution**: The lockdown approach suggests Anthropic sees Mythos capabilities as exceeding what can be safely deployed publicly
4. **Physical world integration**: Project Vend and Project Fetch signal Anthropic's interest in AI agents operating in real-world environments, not just digital tasks

## Related

- [[concepts/anthropic-openclaw-conflict]] — Anthropic's concurrent restrictions on third-party tool access
- [[entities/dario-amodei]] — Anthropic CEO, announced Mythos Preview
- [[concepts/ai-safety-and-alignment]] — Dual-use risk management framework
- [[concepts/agent-autonomous-systems]] — Project Vend, Project Fetch

## Sources

- https://red.anthropic.com/claude-mythos-preview (Apr 7, 2026) — Full Frontier Red Team Research Summary
- https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas (Apr 2026) — Newsletter analysis
- https://www.anthropic.com/news/project-glasswing — Project Glasswing (security vulnerability discovery)
