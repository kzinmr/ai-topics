---
title: "OpenAI Astra"
type: entity
created: 2026-08-03
updated: 2026-09-04
tags:
  - model
  - openai
  - mathematics
  - reasoning
  - ai-safety
  - preparedness-framework
  - cybersecurity
  - safety
sources:
  - raw/articles/garymarcus.substack.com--p-openais-amazing-but-vastly-oversold--9b1f0537.md
  - raw/articles/garymarcus.substack.com--p-two-critical-updates-re-astra-and--79f7c1a6.md
  - raw/newsletters/2026-08-10-the-model-openai-won-t-release.md
  - raw/newsletters/2026-08-23-openai-slows-for-show-anthropic-s-strong-bonds-and-china-s-open-offensive.md
  - raw/articles/2026-08-28_openai_cursor-contract-wind-down.md
  - raw/articles/simonwillison.net--2026-sep-3-gpt6-astra--74293eba.md
  - raw/articles/garymarcus.substack.com--p-hot-take-on-gpt-6-astra--fbf12bd8.md
related:
  - entities/openai
  - concepts/gpt/gpt-5-6
  - concepts/ai-reasoning
  - concepts/ai-benchmarks
---

# OpenAI Astra

**Astra** is OpenAI's next major model family. As of August 2026, an internal version solved 10 major open problems in mathematics, quantum complexity, and theoretical computer science, claimed at a total compute cost of ~$2,000 at Sol API prices. The results generated massive public attention and debate.

## Key Capabilities (Claimed)

- Solved 10 open mathematical conjectures including new circuit lower bounds for computing the permanent
- Published a 249-page paper with results (but notably, no methodology or model details)
- Superseded previous GPT-5.6 as the leading math/reasoning model
- Elon Musk cited it as evidence of reaching The Singularity

## Preparedness Framework: Critical Cybersecurity Rating (August 2026)

On Friday, August 7, 2026, [[entities/openai|OpenAI]] said it can no longer rule out that Astra meets the **Critical** cybersecurity bar in its own Preparedness Framework — the level at which a model finds and weaponizes zero-day flaws in hardened real systems with no human in the loop. This makes Astra the **first model ever treated as Critical** under the framework.

- **First-ever Critical rating**: No prior model has been treated as Critical. [[concepts/gpt/gpt-5-6|GPT-5.6 Sol]] sat one rung lower, at **High** — consistent with the GPT-5.6 documentation, which states Sol did NOT cross the Cyber Critical threshold.
- **Work paused**: Internal work on Astra is paused pending stronger controls: sealed test environments, restricted network and tool access, sandboxed execution, and chain-of-thought monitoring.
- **Release implications**: With Critical on the table, releasing Astra becomes a governance problem, not just a capability milestone — a sharp counterpoint to the math-breakthrough narrative.

#### The "Slows for Show" interpretation (The Signal, Alex Banks, Aug 23 2026)

[[entities/alex-banks|Alex Banks]] (The Signal) read the pause not as precaution but as **positioning ahead of an expected IPO filing**. Two concrete framings the wiki had not captured:

- **The pause costs ~20% extra compute just to monitor** OpenAI's most capable models ("watching what they do"). Banks argues a lab genuinely alarmed by a dangerous model would not need a viral announcement to stop training it — so a public announcement signals confidence, not caution: "you can only sacrifice a lead you can afford to lose." Altman had confirmed near-term releases are unaffected, so "nothing customers touch actually slowed down."
- **The same week shipped two desktop-privacy features that undercut the safety framing**: a **ChatGPT Apple Messages plugin** in the Mac desktop app (ChatGPT Work + Codex) that reads your iMessages, catches up on missed conversations, and drafts/sends replies; and **Computer History**, which lets ChatGPT remember your activity across every app and website on the computer so future answers need less explaining. Banks' read: the frontier-training pause and the always-watching desktop features landed in the same seven days.

The pause section above remains the factual record (Aug 7 Critical rating, two-week RL pause, largest frontier training run on hold); this subsection records the contrarian narrative framing that circulated in the AI-press roundups of the week.

Source: raw/newsletters/2026-08-23-openai-slows-for-show-anthropic-s-strong-bonds-and-china-s-open-offensive.md (The Signal).

## Critical Analysis: The Fallacy of Composition

**Gary Marcus** argued that the public reaction commits the [fallacy of composition](https://en.wikipedia.org/wiki/Fallacy_of_composition): inferring that success in one domain (math) implies success in all domains. Key criticisms:

1. **Domain specificity**: Math benefits from verifiable synthetic data and symbolic verification tools — properties not shared by most real-world problems
2. **Unknown methodology**: No information on how many conjectures were attempted, failure rate, human involvement, or verification process
3. **Selective reporting**: The $2,000 cost likely excludes failed attempts and human expert salaries
4. **Proof quality**: Astra's proof-writing is reportedly not on par with the proofs themselves — characteristic of ChatGPT-generated proofs that elaborate on boilerplate but introduce key steps nonchalantly
5. **Historical parallel**: IBM Watson won Jeopardy but failed at cancer treatment — domain success ≠ universality

**Ernie Davis** (NYU) added: the claim that this is "plausibly the most significant day in the history of mathematics" is absurd — Hilbert's 23 problems yielded one solved result every 9 years, and Astra's results are nowhere near that league.

## Reproducibility & Follow-up (Aug 2026)

A follow-up post by [[entities/gary-marcus|Gary Marcus]] (Aug 4, 2026) added two updates to the Astra story.

**UPDATE 1 — Rapid partial replication.** Within 24 hours of the announcement, **Levent Alpöge**, a mathematician at [[entities/anthropic|Anthropic]], reported reproducing half of Astra's math results using **Fable**, a model Anthropic had already publicly released — "totally autonomous, generic prompt, no internet" (+ paranoia to ensure no information leaked). Marcus drew two implications:

- **The real advance may be problem selection, not the model.** If OpenAI's contribution was using AI to find which open problems are amenable to a certain search-and-verify technique, "maybe once that subset has been flagged, maybe many systems can do them" — which is exactly what Alpöge's replication suggests.
- **It undercuts the "major breakthrough" narrative.** Astra is an advance "to some degree," but that degree "may well turn out to be merely incremental relative to other recent models."

**Non-disclosure of failures.** OpenAI's Noam Brown acknowledged failures on other problems ("Sadly no Millennium Prize problems (yet)") but OpenAI does not report which problems were tried and failed — Marcus calls this "a numerator without a denominator, always a worrisome sign."

**Naming indecision.** Per The Information, OpenAI has not decided whether to call Astra GPT 6 or GPT 5.7. Marcus: if Astra were a genuine quantum leap, that would not be such a hard choice.

**UPDATE 2 — Terence Tao on "proof indigestion."** A July 26 lecture by Terence Tao (pre-dating the Astra announcement) introduces **proof indigestion**: what happens if AI produces a lot of true-but-not-useful mathematics. Tao distinguishes solving open problems — which Astra seems strong at, perhaps with important limits — from building theory, where there is no evidence Astra can contribute. Tao is open to AI in mathematics; Marcus calls the lecture mandatory reading for anyone thinking about how AI will affect mathematics.

A postscript illustrates Brandolini's law, with engineer Wouter Vreugdenhil's observation: "OpenAI sustain investor faith with minimal effort. Proving them wrong takes years and expertise most people lack."

## What Astra Does NOT Solve

- Hallucination and reliability problems
- PDF number extraction
- Creative writing (YouTube script generation)
- Military strategy or open-ended world reasoning
- Autoformalization (turning human math into Lean/Coq formal proofs)
- General AGI/ASI

## Soft Release as GPT-6 Astra (September 3, 2026)

On September 3, 2026, OpenAI **soft-released Astra as "GPT-6 Astra"** — resolving the naming indecision Marcus had flagged in August ([[#Reproducibility & Follow-up (Aug 2026)]]). Rollout: a limited set of organizations first, then all ChatGPT Plus/Pro/Business/Enterprise users plus the OpenAI API and AWS. API model label: `gpt-6-astra`.

**Pricing**: $10/M input, $50/M output — priced identically to [[events/claude-fable-5-1-release-sep-2026|Claude Fable 5/5.1]], making it explicitly OpenAI's Fable competitor (see [[comparisons/llm-api-pricing]]).

### Benchmark results (OpenAI self-reported + Artificial Analysis)

- **ARC-AGI-3: 99.9%** — but with a critical harness caveat: the score was achieved for **$19K using OpenAI's custom "Provider Adapter harness"**, which preserves opaque reasoning state between requests and compacts long conversations so the model reuses prior work. Under the **default ARC-AGI harness the model scored 62.7%** (for $26K). Fable 5 has no published ARC-AGI-3 result (see [[concepts/ai-benchmarks/arc-agi-3]]). This is a textbook benchmark-framing case (cf. [[concepts/ai-benchmarks/benchmaxxing]]): a 37-point spread between harnesses on the same model.
- **Security (post-Hugging-Face-incident posture)**: 100% on ExploitBench (GPT-5.6 Sol: 78.5%), 42.4% on ExploitGym (Sol: 30.3%), 99.2% within four attempts on SRE-Bench binary reverse engineering (Sol: 68.7%). Consistent with the first-ever Critical cybersecurity rating in August ([[#Preparedness Framework: Critical Cybersecurity Rating (August 2026)]]).
- **Long context**: 100% at 256K–512K and 96.3% at 512K–1M on OpenAI's eight-needle benchmark — potentially "vanquishing" one of long-context's ongoing challenges (cf. [[concepts/context-engineering/context-rot]], [[concepts/embedding-long-context-degradation]]).
- **Artificial Analysis Intelligence Index**: 61 — equal to GPT-5.6 Sol, **5 points below Claude Fable 5.1** (max with fallback), and trailing Meta's Muse Spark 1.3 (max). Astra does **not** top the leaderboard.
- **Coding Agent Index**: leads the cost-efficiency frontier — at max effort, same cost as Sol (max) with 2 points higher score, and **less than half the per-task cost of Claude Fable 5 for the same score**.

### Gary Marcus's "hot take" (Sep 3, 2026)

Gary Marcus's immediate reaction zeroed in on the same mechanism as the ARC harness caveat: Astra "creates a dense compact symbolic world model to complete ARC-AGI-3 environments" — e.g., in environment s5i5, recording level/hub-orientation/mechanism lengths as structured text state ("L8: hub q2 (8↓). Lengths: 14=1…") and mapping operations to exact controls. This fits Marcus's standing theses: the [[#Critical Analysis: The Fallacy of Composition|fallacy of composition]] (narrow-suite dominance ≠ generality) and the world-models-over-autoregression argument ([[concepts/world-models-for-agents]]) — the "world model" here being an in-context scaffold the harness preserves, not evidence the base model has world modeling.

**Contested (2026-09-03):** OpenAI frames Astra as the leading frontier model; Artificial Analysis places it below Fable 5.1 on general intelligence, above it on coding-agent cost-efficiency. Both readings are current record until independent third-party evals land.

Source: [[raw/articles/simonwillison.net--2026-sep-3-gpt6-astra--74293eba.md]] (Simon Willison), [[raw/articles/garymarcus.substack.com--p-hot-take-on-gpt-6-astra--fbf12bd8.md]] (Gary Marcus).

### Same-Day Context: Daybreak for Frontline Defenders

The Astra release was announced alongside **Daybreak for Frontline Defenders** — a $1B initiative subsidizing defender access to OpenAI's cyber capabilities for critical-infrastructure teams — published one day earlier as the policy answer to Astra's Critical rating. The pairing is strategic: the Critical rating creates urgency, the subsidy channels it into defender-oriented deployment. See [[concepts/daybreak-for-frontline-defenders]].

## Broader Context

The Astra announcement illustrates a recurring pattern in AI: impressive narrow capabilities are extrapolated to universal intelligence claims. The gap between "excellent at some math" and "AGI" remains vast, and the methodology behind the results remains opaque.

## See Also

- [[entities/openai|OpenAI]]
- [[concepts/ai-reasoning|AI Reasoning]]
