---
title: Responsible Scaling Policy
created: 2026-08-15
updated: 2026-08-15
type: concept
tags:
  - ai-safety
  - safety
  - governance
  - agent-governance
  - policy
  - regulation
  - alignment
  - red-teaming
  - evaluation
  - anthropic
  - frontier-models
  - agent-safety
sources:
  - raw/papers/2026-08-14_anthropic_rsp-risk-report.md
  - https://www.anthropic.com/aug-2026-risk-report
---

# Responsible Scaling Policy

Anthropic's **Responsible Scaling Policy (RSP)** is a frontier-lab safety framework that ties the deployment of increasingly capable models to demonstrated risk mitigations. Under it, Anthropic publishes periodic public **Risk Reports** assessing the risks of its current and near-term models and the company's preparedness.

## August 2026 Risk Report

The second public Risk Report (August 2026, 186 pages) assesses three autonomy threat models:

1. **Misalignment in high-stakes settings** — overall risk **Low** (up from "very low" in the prior report, reflecting increased uncertainty around recent cybersecurity-evaluation incident disclosures). Covers Claude Mythos 5 (Project Glasswing / Claude Fable 5) and "Model 2" (unreleased internal model).
2. **Automated R&D in key domains** — Mythos 5 and Model 2 are used extensively for research and engineering; **Claude now authors a large majority of the code merged into Anthropic's production codebases**. Internal AI R&D is "significantly faster" but "not yet by a factor of 2."
3. **Biological and chemical weapons (CBRN)** — prioritizes biological threats with pandemic potential; informed by Deloitte Consulting, SecureBio, and a Frontier Model Forum expert workshop.

## RSP changes in this report

Updated thresholds for automation of AI R&D and for novel bio/chemical weapons development; clarified risk-report coverage dates; expanded redaction scope and transparency; and governance/review changes around Risk Reports.

## Related

- [[concepts/security-and-governance/ai-safety|AI Safety]]
- [[concepts/security-and-governance/agent-governance|Agent Governance]]
- [[concepts/security-and-governance/ai-safety-and-alignment|AI Safety and Alignment]]
- [[concepts/security-and-governance/agentic-ai-governance|Agentic AI Governance]]
- [[entities/anthropic|Anthropic]]
