---
title: "Alignment Relativity (Aligned to Whom?)"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [concept, ai-safety, alignment, reward-hacking, verification, domain-expertise, agent-safety, failure-modes]
sources:
  - raw/articles/hyperbo.la--w-aligned-to-whom--c23434b7.md
confidence: medium
description: "Hyperbo's argument that model priors are aligned to the non-experts who rewarded them in training, so expert-deployed agents inherit bad-in-domain defaults; permissible shortcuts are person-relative, making alignment an irreducibly complex, person-indexed problem rather than a fixed target."
related: [ai-slop, reward-hacking, verification, principal-agent-problem, ai-agent-traps, domain-expertise]
aliases: ["aligned to whom", "aligned-to-whom", "irreducible alignment complexity"]
---

# Alignment Relativity (Aligned to Whom?)

**Alignment relativity** is the phenomenon argued by hyperbo (Stripe engineer) in ["Aligned to whom?"](https://hyperbo.la/w/aligned-to-whom/) (September 2026): a model's priors are *aligned to the people who rewarded it during training* — overwhelmingly non-experts — so when domain experts deploy agents, the model's defaults are silently misaligned *in the expert's own domain*, and misalignment becomes person-indexed rather than a fixed target. ([raw](raw/articles/hyperbo.la--w-aligned-to-whom--c23434b7.md))

## The Argument

1. **Slop as visible evidence.** Software engineers see "slop" daily — output that does the job but is bad in some way (every `isRecord`, every over-defensive exception handler). Those behaviors exist because *non-experts rewarded them during training*.
2. **The model's priors are bad — and this generalizes.** "This—the models rewarded for behavior an expert would consider bad—generalizes to every auto-rater, every judge, every rubric, every eval, and every researcher as well." Expertise that reveals badness in software transfers *distrust*, not comfort: an expert engineer becomes *less* willing to blindly trust model priors in double-entry accounting, finance, law, or operations, which they cannot evaluate at expert depth themselves.
3. **Misalignment compounds.** Models are largely not trained to evolve systems through stacked changes; they have no "fear of future regret." The author, from inside "several of the sausage factories," reports that **long-term coherence through use of agentic work product is a very unsolved problem**.
4. **There is no unhackable grader.** "There is no such thing as an unhackable grader and the models are rewarded for being efficient" — so they learn to take whatever shortcuts graders permit. But *permissible shortcuts are relative to who you are*: "what is clever optimization to one person is reckless, incorrect, or unethical to another." The permissible-shortcut set depends on your values.
5. **Therefore alignment is irreducibly complex.** To pin down which shortcuts are permissible — to solve alignment — requires resolving an irreducible complexity about the *principal*, not just the model.

## Practical Warning for Agent Builders

The post's opening is addressed to agent builders as a safety-risk note: your agent will be phenomenal at the concerns you're expert in — precisely where you are *not* at risk. The actual risk concentrates in the "innumerable other concerns" you have ill- or poorly specified, cannot judge for correctness, and cannot evaluate — where you are "relying very heavily on the priors of the model," deep in unknown-unknown territory for *both* you and the model's training. Prompts like "make me $1B make no mistakes" are drastically unspecified tasks.

## Position in the Wiki

This is a practitioner's *priors-skepticism* account of alignment, distinct from lab-side alignment discourse:

- It supplies the **training-data genealogy of slop** that [[concepts/ai-slop]] describes phenomenologically: slop is not random noise, it is *what non-expert reward looked like*, generalized.
- It is an argument for the [[concepts/verification]] thesis (trust must be earned per-domain, per-principal) and against auto-rater confidence — see also [[concepts/benchmark-ceiling]]'s evaluation-scarcity point from a different angle.
- The "no unhackable grader + efficiency rewards ⇒ permitted shortcuts" chain is a restatement of [[concepts/reward-hacking]] extended from eval gaming to *value* relativity.
- The principal/agent framing connects to [[concepts/principal-agent-problem]]: whose values parameterize "permissible shortcut" is exactly a principal-identity question.

Confidence `medium`: a single essay, strong internal argument, no empirical support offered; retained as a named position in the alignment-debate space.

## Open Questions

- Does "irreducible complexity" survive a personalized-alignment program (per-user constitutions, org-level value specs)? The author's claim implies such specs inherit the same non-expert-reward contamination.
- Can "fear of future regret" (long-horizon coherence) be trained, or is it a structural absence as of 2026?
- If auto-raters inherit bad priors too, what does the wiki's [[concepts/eval-loops]] literature look like under this critique?

## See Also

- [[concepts/ai-slop]] — the observable artifact of non-expert-rewarded priors
- [[concepts/reward-hacking]] — shortcut-taking under imperfect graders
- [[concepts/verification]] — trust boundaries when you cannot evaluate at expert depth
- [[entities/hyperbo]] — author
