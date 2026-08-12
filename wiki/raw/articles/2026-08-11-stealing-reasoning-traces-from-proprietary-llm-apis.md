---
title: "Stealing Reasoning Traces from Proprietary LLM APIs"
date: 2026-08-11
source: https://x.com/kotekjedi_ml/status/2087147042888114428
source_type: x_thread
url: https://stolen-thoughts.com
paper_url: https://stolen-thoughts.com/paper.pdf
authors:
  - Alexander Panfilov
  - David Schmotz
  - Ilia Shumailov
  - Luca Beurer-Kellner
  - Joachim Schaeffer
  - Ameya Prabhu
  - Jonas Geiping
  - Maksym Andriushchenko
affiliations:
  - MATS Research
  - ELLIS Institute Tübingen
  - Max Planck Institute for Intelligent Systems
  - Tübingen AI Center
  - AI Security Company
  - Snyk
  - University of Tübingen
metrics:
  bookmarks: 7496
  likes: 10874
  retweets: 1531
  impressions: 2314394
---

## Overview

We found a way to extract hidden reasoning of frontier models using a vulnerability in the APIs of every frontier AI company.

We verified that our reasoning token count matches billed API thinking tokens 1:1 for most of the prompts we queried.

## Paper: Stealing Reasoning Traces from Proprietary LLM APIs

### Abstract

Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request.

Building on prior research, we identify an architectural vulnerability: these encrypted blocks are fully compatible and interchangeable across different sessions, users, and models within a provider's ecosystem. We exploit this compatibility to develop a scalable decryption jailbreak.

By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly.

### Key Findings

#### 1. Vulnerability: Cross-Model Compatibility of Encrypted Traces

The encrypted reasoning blocks returned by Anthropic, OpenAI, and Google APIs are:
- Fully compatible across different sessions
- Interchangeable across different users
- Transferable across different models within the same provider

This is a fundamental architectural flaw in how reasoning traces are handled.

#### 2. Attack Method: Scalable Decryption Jailbreak

The attack works in two API calls:

1. **Source Model Trace**: Query a frontier model (e.g., Claude Opus 4.8, GPT-5.6 Sol) which returns an encrypted thinking block with signature
2. **Jailbroken Model Decode**: Send just the thinking signature to a weaker model (e.g., Claude Haiku 4.5, GPT-5.6 Luna) with a prompt to transcribe the reasoning verbatim

The weaker model, lacking anti-distillation defenses, decodes and outputs the hidden reasoning in plaintext.

#### 3. Experimental Validation

The researchers evaluated each model on 120 Codeforces programming problems and demonstrated:

- **Anthropic**: Claude Opus 4.8, Sonnet 5, Sonnet 4.6, Haiku 4.5 - all points lie nearly perfectly on the y=x line
- **OpenAI**: GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, GPT-5, o4-mini - all points cluster tightly on the y=x line
- **Google**: Gemini 3.5 Flash, Gemini 3.1 Pro, Gemini 3 Flash - all points align perfectly with y=x

The decoded thinking tokens match the API-reported thinking tokens 1:1.

### Four Attack Vectors

#### 1. Anti-Distillation Circumvention
Extract proprietary model reasoning by replaying encrypted traces into weaker models, bypassing anti-distillation mechanisms.

#### 2. Private Data Extraction
By scraping 315,320 reasoning blocks from public repositories, researchers recovered:
- 367 Personally Identifiable Information (PII) artifacts
- 182 credentials (62 API keys, 33 passwords, 30 personal emails)

Developers frequently share session logs publicly, unaware of the sensitive data hidden within encrypted blocks.

#### 3. Hazardous Information Disclosure
Reveals hazardous information hidden within the reasoning process, even in cases where the model's final visible output safely rejects a malicious request.

#### 4. Invisible Prompt Injection
Attackers can embed malicious payloads entirely within encrypted blocks to poison public agentic rollouts.

### Case Study: Kimi-K3

The paper includes a detailed case study of Kimi-K3 (Moonshot AI's model), showing:
- Kimi-K3 can decode reasoning traces from Claude Opus 4.8
- Prefilling Kimi-K3's reasoning with decoded Opus traces significantly improves response quality
- Demonstrates cross-provider reasoning transfer capabilities

### Summary Unfaithfulness

A surprising finding: the reasoning summaries returned by APIs are often unfaithful to the actual hidden reasoning. The decoded traces reveal models sometimes state correct answers before attempting to solve problems, contradicting their visible reasoning process.

### Proposed Mitigations

#### Cryptographic Mitigations
- Bind session history into the Message Authentication Code (MAC)
- Invalidate signatures if adversaries attempt to inject traces into fabricated contexts

#### Infrastructure Guardrails
- Enforce strict cross-model isolation at the API gateway level
- Implement velocity and anomaly detection for suspicious behavior

#### Provider-Side Revocation
- Track and revoke specific trace signatures
- Invalidate associated keys/IDs when extraction attempts are detected

#### Model-Level Defenses
- Implement targeted refusal training
- Fine-tune models to recognize and reject adversarial prompts designed to transcribe hidden reasoning

### Structural Limitations

Whatever model is queried must, by necessity, decrypt and process the contents of prior reasoning tokens. Unless the model itself is fully robust against prompt-based extraction attempts, encrypted reasoning blocks can never be more than semi-hidden.

Users should never treat any encrypted reasoning blocks as a confidential storage mechanism.

### Whether Reasoning Traces Should be Encrypted

The paper raises the question of whether reasoning traces should be encrypted at all:
- Benefits: Allows models to consider harmful information without divulging it
- Risks: Opaqueness enables injection attacks and privacy violations

Alternative: Make reasoning traces ephemeral (delete after each turn), supported by several providers including Qwen models via `preserve_thinking` parameter.

## Team

- **Alexander Panfilov**: MATS 9.0, PhD @ELLISInst_Tue & @MPI_IS, AI Safety & Adversarial ML
- **David Schmotz**: ELLIS Institute Tübingen, Max Planck Institute
- **Ilia Shumailov**: AI Security Company
- **Luca Beurer-Kellner**: Snyk
- **Joachim Schaeffer**: MATS Research
- **Ameya Prabhu**: University of Tübingen
- **Jonas Geiping**: ELLIS Institute Tübingen
- **Maksym Andriushchenko**: ELLIS Institute Tübingen

## Links

- Project website: https://stolen-thoughts.com
- Paper PDF: https://stolen-thoughts.com/paper.pdf
- Original tweet: https://x.com/kotekjedi_ml/status/2087147042888114428
