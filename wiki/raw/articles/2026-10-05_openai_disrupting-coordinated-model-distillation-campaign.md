---
title: 'Disrupting a coordinated model-distillation campaign | OpenAI'
source: 'openai'
url: 'https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign'
date: '2026-10-05'
type: raw_article
tags: [raw, source]
fetched: '2026-10-05'
sha256: 9be7ff1aa68ee0f7fc15c88b0ca67549897701f0d243e075ebff973ec3eee242
description: 'OpenAI discloses and disrupts a coordinated adversarial-distillation campaign that extracted protected reasoning from its models; a core cluster is attributed to individuals associated with Moonshot AI.'
---

We recently identified and disrupted a coordinated campaign designed to extract protected reasoning from our models, with the earliest observed activity occurring in the first week of July. This activity is consistent with **adversarial distillation**: the systematic and unauthorized use of one model's outputs or reasoning to help train, reproduce, or improve another model. Protected reasoning is the model's internal record for working through a task; extracting it can reveal information withheld from the final answer and help others reproduce the model's capabilities.

The operators did not break our encryption, compromise a database, or gain direct access to stored user conversations. Instead, they manipulated model interactions so that protected reasoning could be reproduced in forms visible to the requester in a coordinated, scaled manner that violated our terms of service. This manipulation is not a vulnerability unique to OpenAI's models, and we have shared information about it with industry partners through the Frontier Model Forum to strengthen collective defenses.

## What we observed

Operators attempted to extract protected reasoning in novel ways, including by copying encrypted reasoning from one conversation and asking a model in another conversation to decrypt and transcribe the hidden reasoning content.

Independent security researchers also brought related cross-model and conversation-compaction vulnerabilities to our attention through responsible disclosure (arXiv:2608.09867, "Stealing Reasoning Traces from Proprietary LLM APIs"). We investigated their findings and confirmed the attack paths were real.

The activity began on July 1, initially at low volume, until high-volume spikes on July 24–25 consisting of 16,000 requests using a relevant extraction pattern from over 4,000 users. Further investigation identified related prompt-pattern activity across a cluster of more than 15,000 users, fully disrupted by July 28. The activity evolved over time, reinforcing that adversarial distillation is a broader security challenge requiring layered, adaptive defenses.

## Attribution

It is unclear whether all operators originated from a single actor. However, OpenAI attributes a core cluster of the activity to individuals associated with **Moonshot AI**, the developer of Kimi.

## Why this matters

Adversarial distillation poses safety and national security risks. Extracted reasoning could train another model without preserving the safeguards applied to the original model's user-facing outputs. At scale, distillation accelerates transfer of advanced capabilities without the same investment in safety — heightened as models gain dual-use capabilities. This risk is not unique to OpenAI; similar techniques may affect other advanced AI systems, making it a shared security challenge.

## How we responded

Mitigation combined account enforcement, technical controls, and partner coordination: banning/restricting fraudulent accounts, strengthening signup and infrastructure controls, expanding monitoring. OpenAI strengthened protections for hidden reasoning across users, workspaces, organizations, and model families; closed a pathway allowing someone possessing another user's encrypted reasoning to replay and recover its contents; added checks to detect and hold streamed output that might expose reasoning. When activity moved through third-party services, OpenAI worked with providers to disrupt accounts.

Findings were shared through the Frontier Model Forum and government channels. **Systems that support portable or replayable reasoning artifacts may face related risks.**

## What comes next

Adversarial distillation attempts are expected to grow more sophisticated. Partner-hosted deployments need the same protections as first-party services, and tool-output attacks require protections beyond ordinary visible text. Continued focus: stronger technical protections against extraction, better detection/enforcement against coordinated campaigns, deeper threat-information sharing across industry and government.
