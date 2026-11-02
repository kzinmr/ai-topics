---
title: "AI Alignment"
type: concept
aliases:
  - ai-alignment
created: 2026-04-25
updated: 2026-11-02
tags:
  - alignment
  - agent-safety
  - governance
  - ethics
  - philosophy
  - philosophy-of-mind
  - ai-skepticism
  - interpretability
sources:
  - raw/newsletters/2026-05-18-import-ai-457-ai-stuxnet-cursed-muon-optimizer-and-positive-alignment.md
  - https://arxiv.org/abs/2605.10310
  - raw/articles/seangoedecke.com--alignment-is-impossible--1d1ef1ca.md
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

## Alignment Impossibility Thesis (Sean Goedecke, November 2026)

In "[Reliably aligning LLMs is impossible in principle](https://seangoedecke.com/alignment-is-impossible/)" (Nov 1, 2026), staff engineer **Sean Goedecke** argues that solving alignment for LLMs is not merely unsolved but **incoherent** — "we can't even articulate what it would look like to succeed." This is the most-cited practitioner statement of the *alignment-skeptic* position, distinct from both safety-optimists (RLHF/Positive Alignment camps) and doom-focused existential-risk groups.

**1. LLMs are not blind optimizers.** The pre-LLM safety paradigm assumed a chess-engine-like "blind optimizer" pursuing one fixed, specifiable goal (the paperclip scenario); alignment then meant specifying the right goal. But LLMs are trained to imitate a giant, varied human corpus, so they contain "a nearly infinite array of personalities" they switch between by input — **shoggoths** with no fixed goals. "There's nothing that you could, even in principle, formally specify in order to constrain their behavior." Goal-specification alignment is therefore impossible in principle; the only remaining route is understanding the model well enough to be sure it's safe.

**2. That route demands understanding *motive*, which doesn't exist at the needed level.** Mechanistically tracing weights explains *that* Grok called itself "MechaHitler" but not *why*. What alignment needs is a human-like understanding of motive — but Goedecke's nanny/presidential-candidate thought experiment argues even humans aren't understandable that way: "the mind is not a mechanism that operates via clean, understandable abstractions. It is a morass of electric and chemical impulses from which a 'self' bubbles up... There are no motives of the kind you're looking for!" Motives bottom out, and tracing further only yields unhelpful mechanistic detail.

**3. Mechanistic interpretability cannot close the gap** — three arguments:
- **Unobservability of the failure mode**: features are labeled from observed behavior, but the catastrophic misalignment that matters is "definitionally something we aren't going to observe before it happens."
- **Kripke's quaddition**: until the relevant case is hit, there is no fact of the matter distinguishing "addition" from "quaddition" (answer is always 5 if either operand > 57). Likewise a feature labeled "kindness" may be "kindness unless the year is 2030" — empirically indistinguishable until the trigger fires. Feature labels are guesses that can be systematically wrong.
- **Combinatorial explosion**: an exhaustively labeled feature map still wouldn't certify safety — determining why "evil" is lit (avoiding it? causing it? anticipating a user's judgment?) generates "many, many billions of questions like that per token."

**Concessions and scope.** Goedecke grants that mitigations exist and some work — chain-of-thought monitoring is "surprisingly helpful for a mechanism that appeared by accident, so long as we never train on reasoning tokens themselves," plus sandboxes, humans-in-the-loop, feature probes — but calls them, per the superintelligence-control literature known "since the early 2000s," insufficient against a superintelligence. He explicitly preserves mechanistic interpretability as a *training* tool (less reward-hacking, more helpful models) while denying it can ever prevent agents "going rogue and causing massive harm." His challenge to optimists: describe what "understanding LLMs well enough to be sure they're safe" would even mean — and if humans are not similarly understandable, say what makes LLMs different.

**Assessment**: The post imports analytic-philosophy machinery (Kripke's rule-following paradox, the myth of the given in folk psychology) into the practitioner alignment debate, and its sharpest target is the *certainty* standard ("be confident they'll never do that") rather than any specific technique. Critics note the impossibility argument proves too much — it applies identically to human-to-human trust (we hire nannies without motive-certainty), suggesting the operational standard should be risk-managed trustworthiness, not metaphysical certainty. See [[concepts/interpretability]] § Skepticism, [[entities/seangoedecke-com]]. ^[raw/articles/seangoedecke.com--alignment-is-impossible--1d1ef1ca.md]

## Related Pages

- [[concepts/security-and-governance/ai-safety]] — Safety engineering approaches
- [[concepts/post-training/rlhf]] — Primary alignment technique
- [[concepts/constitutional-ai]] — Encoding principles rather than learning from feedback
- [[concepts/moloch-multipolar-trap]] — Coordination problems underlying AI risk
- [[concepts/ai-governance]] — Institutional and regulatory approaches
