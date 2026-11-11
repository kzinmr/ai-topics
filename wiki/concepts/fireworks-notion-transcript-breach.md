---
title: "Fireworks AI Breach — Notion AI Transcript Exposure (Nov 2026)"
type: concept
created: 2026-11-11
updated: 2026-11-11
tags:
  - security
  - supply-chain
  - data-breach
  - ai-infra-security
  - third-party-risk
  - llm-inference
  - data-retention
confidence: high
sources:
  - https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor
  - raw/articles/2026-11-11_notion_fireworks-breach-incident.md
  - https://news.ycombinator.com/item?id=50437106
---

# Fireworks AI Breach — Notion AI Transcript Exposure (Nov 2026)

In November 2026, **Notion disclosed a security incident at third-party AI inference vendor Fireworks AI** that exposed a limited set of **unattributable Notion AI chat transcripts** used for Notion's "Insights" classification feature (HN 162pts). It is the flagship example so far of the *AI supply-chain* failure mode: your data leaves your vendor (Notion) to an inference vendor (Fireworks), and the inference vendor gets breached.

## Facts (as disclosed)

- Notion's incident page: leaked data included "unattributable Notion AI chat transcripts used for the Insights feature" — chats were not labeled with author or workspace, contained no tool-call results, and carried no workspace/user/company identifiers beyond the transcript text itself. Users are advised to "treat this unattributable data as" potentially sensitive.
- Only "2 members of your workspace may have been affected" per affected-org notices — several HN admins reported exactly the same "2 members" template wording, raising template-vs-actual-scale questions.
- Root-cause chain (community reconstruction, [happygoose]): Notion likely uploaded conversation transcripts to Fireworks as a **batch-inference "dataset"** to exploit batch pricing discounts — Fireworks' ZDR-by-default posture does not apply to dataset-style retention a customer explicitly requests ([edot] pointed out: if Fireworks is ZDR, what leaked is what a customer asked to be retained).
- Fireworks' own breach page additionally mentions leaked **customer model weights and training datasets**.

## Incident-response criticism (HN item 50437106)

- [werrett] (a Fireworks customer): Fireworks' Oct 9 initial notification said customers were "not impacted"; the same customer later discovered **their Anthropic API keys used on Fireworks had been hijacked**, requiring a days-long investigation — and had still not received formal breach notification.
- [peri-cl]: an individual Fireworks customer received *no* communication at all — learned of the breach only via HN.
- Notion criticized for gating affected-member visibility behind Enterprise-plan admin sharing ([frankotron], [Andugal]); [thinkindie] found the self-service list at `app.notion.com/ai/transcript-data` without Enterprise.
- [alentodorov] on Notion's post: "the whole incident response post feels like a huge cop-out — 'abundance of caution', the vendor is one of the biggest, so ofc it's not our fault for choosing them."
- [leafingensemble] tied product quality to financials: Fireworks reportedly raised $1.505B at a $17.5B valuation while its usage dashboard is unreliable — an AI-infra valuation-vs-operations critique.
- [3s] raised the structural point: ZDR claims are unverifiable without secure hardware attestation (Apple Private Cloud Compute class).

## Assessment & significance

Confidence: the *fact* of the breach and transcript exposure is vendor-disclosed (high); the batch-dataset root cause is community inference (medium). The incident is a concrete instance of the [[concepts/ai-supply-chain-security]] risk class and undercuts "big vendor = safe vendor" assumptions. It pairs with the 2026 pattern of AI-infra-provider breaches (see [[concepts/ai-containment-escape]] for adjacent failure modes) and will likely feature in enterprise AI-vendor due-diligence checklists.

## Related

- [[entities/fireworks-ai]] — the breached inference provider
- [[entities/notion]] — the affected customer-facing product
- [[concepts/ai-supply-chain-security]] — risk class this instantiates
- [[concepts/ai-industry-economics]] — AI-infra valuation context
