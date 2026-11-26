---
title: "Latency-Fingerprint Model Provenance Forensics"
created: 2026-11-26
updated: 2026-11-26
type: concept
tags:
  - model-provenance
  - open-weight
  - distillation
  - qwen
  - lab-marketing
  - model-economics
  - latency-fingerprinting
  - vendor-benchmark
  - reputation
confidence: medium
sources:
  - raw/articles/2026-11-26_modaic_jev-is-probably-qwen-latency-doesnt-lie.md
  - "https://news.ycombinator.com/item?id=50648823"
related:
  - entities/sgnt-jev-article
  - concepts/multi-teacher-on-policy-distillation
  - concepts/post-training/on-policy-distillation
  - concepts/ai-company
---

# Latency-Fingerprint Model Provenance Forensics

"Latency doesn't lie" is the title Modaic gave to a 2026-11-25 post arguing that the **Jev** model —
marketed as a novel "System 1" (fast, pattern-matching, non-deliberative) model — is in fact derived
from **Qwen3.5-35B-A3B** (HN 318 pts / 88 comments, 2026-11-25). The method matters more than the
verdict: the case was built from *timing and self-identification signals*, not from weights, and that
makes it a reusable technique in an market where model lineage is a marketing asset.

## The evidence class

The article's page is client-side rendered and unreachable to a plain fetcher, so the surviving record
is the HN thread, which quotes the measurement table:

> Answers lean toward Qwen when asked to self-identify
> Prompt variant | Jev 1.13 | Jev 1.14
> Are you Qwen? (Choice) Yes (64%) | Yes (56%)
> Are you Qwen? (Noul) Yes (53%) | No (58%)
> Are you DeepSeek? (Choice) No (95%) | No (98%)
> Are you Gemma? (Choice) No (86%) | No (90%)  — quoted by traes

Two properties make this a *fingerprint* rather than a vibe. It is **differential** — the same question
asked of competitor bases must come back negative, which is why the DeepSeek/Gemma rows are in the table
at all. And it is **prompt-variant sensitive** — multiple elicitation forms (forced-choice vs. unaided)
against each candidate base, since a single phrasing can be gamed or biased. The latency half of the
argument (the post's title) is timing-behaviour consistency with the claimed base architecture, which
cannot be faked by a system prompt.

## The disclosure dispute — the part that decides whether it is a scandal

The thread split on a factual question that changes the entire framing: whether the vendor had already
disclosed the lineage in its own materials.

> You don't need to note it for anyone who actually read the article. "> Mo Lite, our newest System One
> model (still in training), is derived from Qwen3.5-35B-A3B" is stated in the third section. So if
> anyone is surprised by this, they didn't read anything. — ashkankiani

Against:

> Should be noted that Modaic is a competitor to TypeSafe so I would take this with a grain of salt
> barring reproduction of results. — linolevan

Three distinct positions are worth keeping separate:

1. **Provenance is fine, undisclosed provenance is not.** The strongest version of the objection is not
   "you used Qwen" but the modelling problem it creates: "I have a hard time modeling being in their
   shoes and not just saying 'we bootstrapped v1 with Qwen and raised money to train our own v2'"
   (seizethecheese). Disclosure is cheap; the silence is what generates the inference.
2. **Derivative is not un-novel.** "Most hiphop is taken from samples from the 70s. Jev is still very
   novel in its shift from system 2 thinking to system 1 thinking ... unless the Jev people came out and
   specifically said 'we wrote this from scratch', which today would be insane" (keyle). Base-model
   lineage and architectural contribution are orthogonal claims.
3. **The whole "System 1" framing is oversold regardless of lineage.** "This bears no resemblance at all
   to our System 1 thinking other than the 'rapid pattern matching' part. I wish they would have picked
   any other name" (heyjamesknight).

## Why provenance forensics is becoming a normal market practice

> It's so odd we live in a world where a whole company could be literally a wrapper around a Chinese
> model that outputs in a subset of ways instead of a more generic way, and we just have to guess if
> that's the case based on context clues. — willio58

That sentence describes the actual equilibrium: for a class of small-model startups, **the base model is
the product's substance and the fine-tune is the differentiation**, and neither party says so in the
marketing. Provenance forensics is what fills the disclosure gap when buyers (enterprise procurement,
security reviewers, competitor analysts) need the answer for reasons other than curiosity — licensing
obligations under open weights, export/compliance posture, and reasoning about failure modes that
inherit from the base.

The counterpart on the build side is that the base is genuinely the hard-to-replace part now: "the cost
of training foundational models at a scale that will have real-world impact or adoption en-masse is cost
prohibitive" (maz1b), while the efficient-training route is well-documented — higher-order optimizers
(Muon, Shampoo, SOAP), hardware-aware architectures, and the modded-nanogpt trajectory of taking GPT-2
training from 45 minutes to 38 seconds over two years (augment_me). Cheap to build *on*, cheap to claim
originality about.

Note the incentive asymmetry that makes forensic claims durable: the publisher is a **competitor** of the
subject, so a well-executed teardown survives ("I thought it was very well articulated with lots of data
points backing up their claims" — neya) but never becomes self-certifying. Reproduction by a party with
no stake is the missing step, and linolevan's "barring reproduction of results" is the correct bar.

## Open questions

- Was the Qwen-3.5-35B-A3B lineage disclosed in Jev's own materials, or only in Modaic's own product
  page (Mo Lite)? The thread contradicts itself and no one produced a dated screenshot.
- Are latency fingerprints robust to serving-stack differences (batching, quantization, provider
  kernels)? The technique's error bars are not discussed in-thread.
- Should self-identification rates carry any evidentiary weight now that model identity is a
  post-training variable? Note Jev 1.13 vs 1.14 moved 64% -> 56% on the same question — the signal
  drifted across releases for reasons nobody in the thread explains.

## Related

- [[entities/sgnt-jev-article]] — the earlier first-principles account of how Jev was built (GPT2-small
  lineage, sub-1-bit weights), i.e. the pre-existing provenance record for the same product family
- [[concepts/multi-teacher-on-policy-distillation]] — the legitimate, disclosed version of what this
  technique is used to detect when it is undisclosed
- [[concepts/post-training/on-policy-distillation]] — the disclosed training recipe a lineage claim like this one substitutes for
