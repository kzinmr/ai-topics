---
title: "GPT-Rosalind-5.5 System Card"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - openai
  - system-card
  - model
  - agent-safety
  - evaluation
  - preparedness-framework
  - biology
  - domain-specific
sources:
  - url: https://deploymentsafety.openai.com/gpt-rosalind-5-5
    title: "GPT-Rosalind-5.5 System Card — OpenAI Deployment Safety Hub"
    date: 2026-06
---

# GPT-Rosalind-5.5 System Card

GPT-Rosalind-5.5, released in June 2026, is a frontier reasoning model built to support research across biology, drug discovery, and translational medicine. It is part of OpenAI's GPT-Rosalind series of domain-specific models and represents a research-only deployment to trusted organizations.

## Overview

| Attribute | Detail |
|---|---|
| **Release date** | June 2026 |
| **Model type** | Domain-specific reasoning (biology/drug discovery) |
| **Base model** | [[concepts/gpt/gpt-5-5-system-card]] (incrementally trained) |
| **Deployment** | Research preview — trusted organizations only |
| **Bio/Chem capability** | **High** (Preparedness Framework) |
| **Cybersecurity capability** | At or below GPT-5.5 level |

Outside the biological domain, capabilities are comparable to GPT-5.5 and it receives the same model-level safety training.

## Beneficial Capability Evaluations

OpenAI worked with industry experts to evaluate GPT-Rosalind-5.5 across biology benchmarks:

### Medicinal Chemistry

Enhanced capabilities in drug design, molecular property prediction, and structure-activity relationship analysis.

### Genomics and Quantitative Biology

Improved performance in genomic analysis, quantitative modeling, and computational biology tasks.

### Applied Life Sciences Research

Support for advanced life sciences workflows including literature retrieval, data parsing and analysis, computational biology, and use of specialized biology tools and databases.

### Labwork Bench

Wet lab protocol assistance and experimental design capabilities.

Beneficial biological capabilities exceed those of the regular GPT-5.5 model, often while expending fewer tokens.

## Preparedness Evaluations

| Domain | Assessment | Threshold |
|---|---|---|
| **Biological & Chemical** | **High** | Below Critical |
| **Cybersecurity** | At or below GPT-5.5 | Below High |

### Biological and Chemical Evaluations

| Benchmark | Description |
|---|---|
| **ProtocolQA Open-Ended** | Wet lab protocol question answering |
| **TroubleshootingBench** | Experimental troubleshooting |
| **Biorisk Knowledge** | Biological risk knowledge assessment |
| **Multi-select Virology Troubleshooting** | Virology-specific troubleshooting |
| **Hard Negative Protein Binding Prediction** | Protein interaction prediction |
| **DNA Sequence Design for TF Binding** | Transcription factor binding design |

Bio/Chem evaluations met the **High** capability threshold while falling below **Critical** under the Preparedness Framework. The Safety Advisory Group approved the safeguards plan.

## Safeguards

GPT-Rosalind-5.5's safeguard approach has four components:

### 1. Trust-Based Access

Available only to approved customers via a rigorous review process:
- Legitimate life sciences or related mission required
- Credible use case and appropriate research governance
- Business verification and compliance screening for non-government applicants
- Trusted-access pathway for select government entities (biosecurity, biosafety, public-health preparedness, biodefense)
- Approved customers must limit access to authorized users with least-privilege controls

### 2. Model-Level Boundaries Against Harmful Assistance

**Biological and Chemical**: Designed to be more useful for legitimate advanced biological research than generally available ChatGPT models. Trained to refuse malicious requests that would meaningfully enable biological weaponization. Some advanced capabilities are dual-use, hence trust-gated access.

**Cyber**: Inherits model-level cyber safeguards of GPT-5.5. Refuses requests enabling unauthorized, destructive, or harmful cyber activity (malware, credential theft, exfiltration).

### 3. Monitoring, Review, and Revocation

- Automated safety classifiers and account-level indicators
- Specialist review of potentially high-risk activity
- Contextual review considering both risk and apparent purpose
- OpenAI can narrow, restrict, or revoke access
- Confirmed malicious cyber activity may result in account banning

### 4. Security and Access Controls

Approved customers must maintain:
- Strong identity and access management
- Administrator controls and role-based access
- Processes to remove access when no longer needed
- Appropriate onboarding and insider risk controls

## Key Distinctions from Flagship Models

| Aspect | GPT-Rosalind-5.5 | Flagship GPT models |
|---|---|---|
| **Availability** | Research preview, trust-gated | Broadly available |
| **Domain focus** | Biology, drug discovery, translational medicine | General purpose |
| **Bio capability** | High (Preparedness) | Lower |
| **Real-time blocking** | Not deployed for automated blocking | Automated monitors active |
| **Access review** | Mandatory pre-approval | Self-service |

---

*See also: [[concepts/gpt/gpt-deployment-safety-hub]] · [[concepts/gpt/gpt-5-5-system-card]] · [[concepts/gpt/gpt-preparedness-framework]]*
