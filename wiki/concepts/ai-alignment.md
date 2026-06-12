---
title: "AI Alignment"
type: concept
aliases:
  - ai-alignment
created: 2026-04-25
updated: 2026-05-19
tags:
  - alignment
  - agent-safety
  - governance
  - ethics
  - philosophy
sources:
  - raw/newsletters/2026-05-18-import-ai-457-ai-stuxnet-cursed-muon-optimizer-and-positive-alignment.md
  - https://arxiv.org/abs/2605.10310
---

# AI Alignment

The technical and philosophical field concerned with ensuring that AI systems behave as intended, remain aligned with human values, and pursue goals that benefit humanity.

## Negative vs Positive Alignment

### Negative Alignment (Current Paradigm)

The dominant approach focuses on **safety constraints and harm prevention**: safeguards, controllability, compliance, and refusal mechanisms. This creates a behavioral "floor" — don't do bad things — but provides no ceiling or positive goal. The analogy is to clinical psychology's historical focus on pathology over well-being.

**Critiques of the negative-only approach:**

- **Floor without ceiling**: Safety constraints alone yield mediocre, sycophantic, or unhelpful systems
- **Preference-wellbeing divergence**: Users may prefer flattery, quick answers, or engagement over genuine understanding or growth
- **Hidden value system**: "Safety" obscures unavoidable value judgments about what constitutes harm
- **Scalability**: Exhaustive prohibitions don't generalize well to novel situations

### Positive Alignment (May 2026)

A position paper from **Oxford, Google DeepMind, OpenAI, Anthropic, Stanford, Tufts, and Imperial College London** (arXiv:2605.10310) proposes **Positive Alignment** — a distinct and complementary research agenda:

> "Positive Alignment is the development of AI systems that (i) remain safe and cooperative and (ii) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way."

**Core principles:**
- **Flourishing as optimization target**: Move beyond "avoid harm" to actively cultivate well-being, virtue, and growth
- **Pluralistic governance**: Not top-down by a central state or few labs; decentralized, contestable processes
- **Polycentric oversight**: Many legitimate centers of oversight rather than one institutional or moral chokepoint
- **User-authored values**: Communities customize AI behavior to their context rather than accepting universal defaults

**Technical directions proposed:**
- Data filtering and upsampling for flourishing-relevant content
- Pre- and post-training objectives that reward growth-supporting behaviors
- Longitudinal evaluation frameworks (not just single-turn QA)
- Collaborative value collection and constitution authoring

**Critique:** Critics argue the paper anthropomorphizes AI systems by attributing "character" and "virtue" to them, when the real design challenge is shaping outputs to support human flourishing — an institutional and governance challenge rather than an AI character challenge.

## Related Pages

- [[concepts/security-and-governance/ai-safety]] — Safety engineering approaches
- [[concepts/post-training/rlhf]] — Primary alignment technique
- [[concepts/constitutional-ai]] — Encoding principles rather than learning from feedback
- [[concepts/moloch-multipolar-trap]] — Coordination problems underlying AI risk
- [[concepts/ai-governance]] — Institutional and regulatory approaches
