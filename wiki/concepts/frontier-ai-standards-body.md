---
title: "Frontier AI Standards Body (Hassabis Proposal)"
created: 2026-07-14
updated: 2026-07-14
type: concept
tags:
  - concept
  - policy
  - governance
  - ai-governance
  - ai-safety
  - regulation
  - agi
aliases:
  - FINRA-style AI regulation
  - Frontier AI FINRA model
related:
  - concepts/ai-regulation-2026
  - concepts/frontier-safety-blueprint
  - concepts/openai/frontier-governance-framework
  - entities/demis-hassabis
sources:
  - raw/articles/2026-07-14_demishassabis_frontier-ai-framework.md
  - https://x.com/i/article/2076946210397552640
---

# Frontier AI Standards Body (Hassabis Proposal)

A policy framework proposed by **[[entities/demis-hassabis|Demis Hassabis]]** (CEO of Google DeepMind) in July 2026, advocating for a **FINRA-style self-regulatory organization (SRO)** to govern frontier AI development. Published as an X Article titled "A Framework for Frontier AI and the Dawning of a New Age," it represents one of the most detailed regulatory proposals from a leading AI executive.

## Core Framework

### Institutional Model: FINRA-Style SRO

The proposal calls for establishing a **Frontier AI Standards Body** modeled on the **Financial Industry Regulatory Authority (FINRA)** — a federally overseen public-private partnership or self-regulatory organization:

| Attribute | Detail |
|-----------|--------|
| **Model** | FINRA-style SRO (federally overseen, industry-funded) |
| **Board composition** | Independent technical experts + open-source representatives |
| **Funding** | Substantial, mostly from industry (to attract world-class talent + compute) |
| **Testing partners** | Federal agencies + US National Labs |
| **Jurisdiction** | US-initiated, designed for international coordination |

### Frontier-Class Definition

Models qualify as "Frontier-class" by meeting certain thresholds on a set of benchmarks:
- Benchmarks determined and **regularly updated** by the Standards Body
- Designed to keep pace with evolving AI capabilities
- Updated **quarterly initially**; outdated/saturated benchmarks deprecated and replaced

### Frontier Lab Designation

Organizations with "Frontier Models" as defined by those benchmarks would be designated **"Frontier Labs"**, expected to:
- Publish model cards with technical details
- Maintain strong internal cybersecurity
- Vet key personnel
- Provide sufficient resourcing for safety and security research

### Pre-Release Review

- **Phase 1 (Voluntary)**: Frontier Labs voluntarily share models with the Standards Body **up to 30 days before release**
- **Phase 2 (Mandatory)**: Once the assessment protocol is proven effective, Frontier Models would be **required to pass it to be deployed in the US market**
- Post-release: Labs work with the Standards Body to address critical vulnerabilities

### Assessment Scope

| Domain | Testing Focus |
|--------|---------------|
| **Cybersecurity** | Offensive cyber capabilities, vulnerability discovery |
| **Biological threats** | Dual-use bio capabilities, pathogen design |
| **Agentic AI** | Safety guardrail bypass attempts, deception detection |
| **Transparency** | Digital watermarking of AI-generated images, human-readable output tokens for model reasoning |

### Benchmark Independence

- **Phase 1**: Evaluations developed in consultation with Frontier Labs
- **Phase 2**: Standards Body develops **held-out tests independent of the Labs** to prevent overfitting
- **Ecosystem**: Promote third-party auditors for assessments and benchmark development

### Ratchet Mechanism

The framework is designed to escalate with risk severity:
- Dynamic adaptation to field acceleration
- Can be **ratcheted up** if the situation demands, including **coordinating a slowdown in development among Frontier Labs**
- Balanced approach: technically focused, supports innovation while incentivizing responsibility

### Scope Exemptions

- **Startups and academia**: Non-frontier models are exempt
- **Country-agnostic**: Applies to Frontier-class models regardless of country of origin
- **Open and closed**: Framework applies to both open-weight and proprietary Frontier-class models

## Comparison with Other Frameworks

| Aspect | Hassabis (FINRA-SRO) | OpenAI Frontier Safety Blueprint (CAISI) | CA SB 53 (TFAIA) | OpenAI Frontier Governance Framework |
|--------|---------------------|----------------------------------------|-------------------|-------------------------------------|
| **Institutional model** | Industry-funded SRO with federal oversight | Government agency (CAISI) with mandatory evaluations | State-level transparency mandate | Company-level policy translation |
| **Pre-release review** | Voluntary → mandatory (30 days) | Mandatory pre-deployment evaluations | Self-certification + incident reporting | Internal practices → public document |
| **Benchmark authority** | Standards Body (eventually independent) | CAISI defines standards | N/A (transparency, not testing) | N/A (internal Preparedness Framework) |
| **International scope** | Explicitly international | Primarily US-focused | California only | Regulatory compliance focus |
| **Slowdown authority** | Yes — can coordinate development slowdowns | Not specified | No | No |
| **Open-source representation** | Explicit board seat | Not mentioned | Implicit (public compute cluster) | Not applicable |

## Key Philosophical Positions

> "10x of the Industrial Revolution at 10x the speed"

Hassabis frames AGI as comparable to electricity or fire — a foundational technology, not a consumer product.

> "Proceeding with cautious optimism is the sensible and correct strategy"

Argues against both unfettered acceleration and precautionary stagnation — a middle path requiring policy that "promotes innovation while also incentivising responsibility and security."

> "The future is not yet written, we must use this precious window before AGI arrives"

Positions the pre-AGI period as a limited window for establishing governance structures before capabilities outpace institutional response.

## Context: AGI Timeline

Hassabis reiterates his estimate of **AGI within "a few short years"** and positions this proposal as urgent infrastructure for that transition. He also raises post-scarcity economic questions as the next frontier beyond technical safety — "what sorts of new economic models will be needed to help everyone thrive in a post-scarcity world?"

## Criticism & Open Questions

- **Regulatory capture concern**: An industry-funded SRO could favor incumbent companies (Google DeepMind, Anthropic, OpenAI) over smaller competitors
- **FINRA comparison**: FINRA itself has been criticized for industry capture and weak enforcement
- **Benchmark gameability**: Dynamic benchmarks are an improvement over static ones, but "teaching to the test" remains a risk
- **International coordination gap**: The proposal acknowledges this as ideal but provides no mechanism for achieving it beyond US leadership

## Related Concepts

- [[concepts/ai-regulation-2026]] — The broader regulatory landscape this proposal enters
- [[concepts/frontier-safety-blueprint]] — OpenAI's competing proposal (CAISI)
- [[concepts/openai/frontier-governance-framework]] — OpenAI's company-level governance approach
- [[concepts/agi-economics]] — Post-scarcity economic models referenced in the proposal
- [[concepts/agi-scarcity]] — The abundance thesis Hassabis endorses

## Sources

- [A Framework for Frontier AI and the Dawning of a New Age](https://x.com/i/article/2076946210397552640) — Demis Hassabis, July 14, 2026
- [[raw/articles/2026-07-14_demishassabis_frontier-ai-framework]]
