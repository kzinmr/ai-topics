---
title: "Claude Mythos Preview"
type: concept
created: 2026-04-13
updated: 2026-05-26
tags:
  - concept
  - anthropic
  - model
  - security
  - agent-safety
  - company
aliases: ["mythos preview", "anthropic frontier red team 2026"]
related:
  - concepts/anthropic/openclaw-conflict
  - entities/dario-amodei
  - concepts/ai-agent-engineering
  - entities/mozilla
sources:
  - raw/articles/2026-05-07_mozilla_behind-the-scenes-hardening-firefox.md
  - raw/articles/blog.calif.io--p-first-public-kernel-memory-corruption--8fd5d832.md
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

### Mythos Breach (April 2026)

Despite the lockdown, Anthropic's internal "too dangerous to release" model **Mythos** was accessed on day one by four individuals in a private Discord. The group:
- Guessed the endpoint URL from naming conventions + a Mercor breach leak
- Used a contractor's legitimate evaluation credentials
- Used the model to build simple websites (not malicious purposes, but the access was unauthorized)

The incident highlights risks of: inference endpoint discoverability, credential sharing among contractors, and naming convention predictability.

## Implications

1. **Capability acceleration**: Sonnet 4.5 matching Opus 4.1 in cyber skills demonstrates rapid model improvement within a single tier
2. **Infrastructure shift**: Standard open-source tools now sufficient for multistage network attacks — no custom infrastructure needed
3. **Release caution**: The lockdown approach suggests Anthropic sees Mythos capabilities as exceeding what can be safely deployed publicly
4. **Physical world integration**: Project Vend and Project Fetch signal Anthropic's interest in AI agents operating in real-world environments, not just digital tasks

## Mozilla Firefox Hardening — Real-World Results (May 2026)

Mozilla leveraged **Claude Mythos Preview** and other AI models to conduct a large-scale Firefox security audit. In April 2026 alone, they fixed **423** security bugs — surpassing the total for all of 2025.

### Bug Breakdown

| Source | Count |
|--------|------|
| **Claude Mythos Preview** | 271 |
| External Reports | 41 |
| Other Internal (Fuzzing/Manual) | 111 |
| **Total** | **423** |

### Severity Distribution (Mythos Preview Discoveries)
- **sec-high**: 180
- **sec-moderate**: 80
- **sec-low**: 11

### Notable Discoveries

- **Sandbox Escape**: Discovered numerous bugs that were extremely difficult to detect with traditional fuzzing. The model is permitted to patch Firefox source code for sandbox-constrained execution only
- **15-year-old bug** (Bug 2024437): Recursive stack depth in `<legend>` element and cycle collection issues
- **20-year-old XSLT bug** (Bug 2025977): Reentrant call triggers hash table rehashing while pointer is in use
- **JIT optimization error** (Bug 2024918): Fake-object primitive generation in WebAssembly GC struct
- **RLBox Escape** (Bug 2029813): Breached validation logic gaps in in-process sandbox

### Pipeline Architecture

Mozilla built a project-specific pipeline consisting of:

1. **Discovery Subsystem**: Agent harness built atop existing fuzzing infrastructure
2. **Parallelization**: Jobs executed across multiple ephemeral VMs, each targeting specific files
3. **Integration**: Automatic deduplication and tracking in Bugzilla, with engineer triage
4. **Model-agnostic**: Easy transition from Claude Opus 4.6 to Mythos Preview

### Lessons Learned

Mozilla recommends that **all software projects start using AI harnesses now**:
> *"There is a bug in this part of the code, please find it and build a testcase."* Start with a simple prompt and gradually build orchestration and tooling around the "inner loop" of discovery and validation.

Going forward, they plan to transition **from file-based scanning to patch-based CI scanning**.
### Apple M5 MIE Kernel Exploit (May 2026)

The [[concepts/ai-vulnerability-discovery|Calif team]] leveraged **Claude Mythos Preview** to achieve the first public macOS kernel exploit bypassing MIE (Memory Integrity Enforcement) on the Apple M5.

#### Results Summary
- **Target**: macOS 26.4.1 (25E253) on bare-metal M5 + kernel MIE enabled
- **Attack**: Data-only kernel local privilege escalation (unprivileged user → root shell)
- Chained **2 vulnerabilities**, using only standard system calls
- **Timeline**: April 25, 2026 (bug discovery) → May 1 (verification) = **1 week**
- **Support**: Mythos Preview assisted with bug identification and overall exploit development

#### Significance
- Five-person startup breached MIE (MTE-based hardware memory safety) — which Apple invested **5 years and billions of dollars** in — in one week
- MIE was designed to neutralize all known public exploit chains (including Coruna, Darksword)
- **Definitive demonstration of AI assistance**: "Small teams can suddenly achieve what entire organizations used to need"
- The 55-page technical report will be published after Apple fixes are deployed

> *"This work is a glimpse of what is coming. Apple built MIE in a world before Mythos Preview. We're about to learn how the best mitigation technology on Earth holds up during the first AI bugmageddon."*


## Related

- [[concepts/ai-vulnerability-discovery]] — AI-assisted exploit development
- [[concepts/anthropic/openclaw-conflict]] — Anthropic's concurrent restrictions on third-party tool access
- [[entities/dario-amodei]] — Anthropic CEO, announced Mythos Preview
-  — Dual-use risk management framework-  — Project Vend, Project Fetch
## Sources

- https://red.anthropic.com/claude-mythos-preview (Apr 7, 2026) — Full Frontier Red Team Research Summary
- https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas (Apr 2026) — Newsletter analysis
- https://www.anthropic.com/news/project-glasswing — Project Glasswing (security vulnerability discovery)
