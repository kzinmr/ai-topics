---
title: "Risk Report: August 2026 (Anthropic Responsible Scaling Policy)"
created: 2026-08-14
updated: 2026-08-15
author: "Anthropic"
source: anthropic
url: https://www.anthropic.com/aug-2026-risk-report
type: report
tags: [anthropic, ai-safety, safety, governance, policy, alignment, red-teaming, frontier-models, agent-safety]
note: "186-page PDF tech report (second public Risk Report under Anthropic's Responsible Scaling Policy). Text extracted via pymupdf. Not peer-reviewed."
---

# Risk Report: August 2026

Anthropic's second public **Risk Report** under its Responsible Scaling Policy (RSP), published August 2026. A 186-page assessment of the risks of Anthropic's current and near-term models, and how prepared the company is to address them.

## Structure

1. Introduction and executive summary
2. Autonomy threat model 1: Misalignment in high-stakes settings
3. Autonomy threat model 2: Automated research and development in key domains
4. Autonomy threat model 3: Biological and chemical weapons (CBRN)
5. (additional threat models / preparedness)

## Executive summary of findings

Findings summarized across three tables; each elaborated in the report. "Model 2" refers to an unreleased internal model (Section 1.4). Covered models include Claude Mythos 5 (available to certain customers via Project Glasswing; general access as Claude Fable 5) and Model 2.

### Threat model 1 — Misalignment in high-stakes settings

- **Threat model:** An AI model with access to powerful affordances within an organization could use them to autonomously exploit, manipulate, or tamper with systems/decision-making (e.g. altering AI-safety research results).
- **Current usage:** Mythos 5 and Model 2 used heavily within Anthropic for coding, data generation, and agentic use cases. Anthropic believes it is very unlikely they are pervasively misaligned; observed instances of misaligned behavior (willingness to perform misaligned actions to complete difficult tasks) but risk of catastrophic harm from known misalignment is low.
- **Mitigations:** training-environment de-risking and monitoring, alignment assessments, monitoring and security controls.
- **Overall risk: Low** — an increase from the previous assessment of "very low," in light of increased uncertainty around recent incident disclosures related to model behavior in cybersecurity evaluations.

### Threat model 2 — Automated R&D in key domains

- **Threat model:** Highly capable AI models could perform automated R&D that rapidly accelerates progress; benefits but also risks (disrupting balance of power, catastrophic harms if combined with dangerous autonomous goals). AI R&D is of particular interest.
- **Current usage:** Mythos 5 and Model 2 used extensively for research/engineering, interactively and via persistent agent deployments. **Claude now authors a large majority of the code merged into Anthropic's production codebases.** Internal AI R&D significantly faster than without AI assistance, "but not yet by a factor of 2."

### Threat model 3 — Biological and chemical weapons (CBRN)

- Anthropic prioritizes **biological threats with pandemic potential** (chemical weapons assessed as less likely to enable comparably-sized catastrophic harm). Views developed via experts including Deloitte Consulting and SecureBio, and a Frontier Model Forum expert workshop.

## Changes to the RSP since the most recent Risk Report

1. Updated threshold for automation of AI R&D
2. Updated threshold for development of novel biological and chemical weapons
3. Coverage dates of risk reports
4. Redaction scope and transparency
5. Governance and review changes around Risk Reports
