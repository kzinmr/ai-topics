---
title: "LLMs as a Cognitive Crutch — the Anti-AI-Research Position (eva.ac)"
type: concept
created: 2026-11-02
updated: 2026-11-02
confidence: medium
tags: [concept, ai-skepticism, developer-experience, human-agent-collaboration, cognition, ai-commentary]
sources:
  - raw/articles/2026-11-01_eva-ac_llms-to-think.md
related:
  - concepts/illusion-of-thinking
  - concepts/ai-skepticism-movement
  - concepts/zombie-statistics
---

# LLMs as a Cognitive Crutch — the Anti-AI-Research Position (eva.ac)

HN 71 pts, 2026-11-01: an independent security researcher at **eva.ac** ("So I guess everyone uses LLMs to think now") explains why they refuse LLMs for research and publishing. The post is a practitioner-artifact of the anti-LLM-for-cognition position — worth capturing as the cleanest recent articulation of a stance that is usually scattered across replies.

## Core arguments

1. **Intrinsic motivation protection.** The researcher's work is done "for fun"; delegating the exploration ("staring at devtools, binary ninja... tracing with nothing but GitHub code search and a dream") destroys the point. Offloading "the tedious bits" isn't neutral because *the tedious bits are where the fun and the learning live*.
2. **Attribution impossibility.** "I cannot take credit for something an LLM did for me, and I also cannot credit an LLM properly, as they aren't a person." Publishing LLM-produced research under one's own name is treated as an integrity violation, not an efficiency gain.
3. **Confident-wrongness intolerance.** Watching a model proceed confidently in a wrong direction — and running "really stupid" commands en route — is described as unbearable to observe, enough to abort runs mid-stream. (This is an aesthetic/tolerance claim, not a capability claim; the author explicitly concedes LLMs are powerful.)
4. **Guidance still dominates.** "Throw an LLM at the Linux kernel and tell it to find an RCE without guidance — it probably couldn't." Recent headline AI-discovered vulnerabilities were found by *skilled researchers with token budgets*, which reframes lab marketing: the same php2shell story was told three ways — Calif ("AI found these vulns with a human guiding it"), OpenAI ("the agent uncovered critical vulnerabilities"), Wiz (a middle point). Narrative divergence between collaborating firms is itself the evidence.
5. **Marketing-driven disclosure harm.** Dropping PoC videos of unpatched 0days on X is pure marketing that "does nothing but make everything worse"; and OpenAI's "patch the world" framing omits what it *could* do with its compute (e.g. AI-assisted backporting of fixes to old PHP versions) but doesn't.

## How this fits the wiki's skeptic corpus

Unlike benchmark-driven skepticism ([[concepts/illusion-of-thinking]]) or evidence-hygiene concerns ([[concepts/zombie-statistics]]), this is **craft-based skepticism**: the cost of LLM delegation is measured in skill formation, attribution, and enjoyment — quantities benchmarks don't see. It pairs with Sean Goedecke's agent-native-tool fallacy on the economics side and with the "everyone uses LLMs to think now" title's implied social-proof pressure: the author's deviation is framed against 2026 defaults, making the post a document of a norm transition.

Confidence: **medium** — a single anonymous practitioner's self-report about their own workflow; its generalizations (marketing critique, guidance-dominance) are opinion, recorded as such.

## Related

- [[concepts/illusion-of-thinking]] — benchmark-side evidence that reasoning gains are bounded
- [[concepts/ai-skepticism-movement]] — the organized-skeptic counterpart to this craft-based position
- [[concepts/zombie-statistics]] — the epistemic-cost side of AI-mediated work

## Source

- eva.ac, "So I guess everyone uses LLMs to think now" (2026-11-01, HN 71) — raw: `raw/articles/2026-11-01_eva-ac_llms-to-think.md`
