---
title: "METR Anthropic R&D Acceleration Assessment (October 2026)"
created: 2026-11-07
updated: 2026-11-12
type: concept
tags: [metr, ai-research, ai-safety, ai-forecasting, ai-risk, superintelligence, recursive-self-improvement, intelligence-explosion, responsible-scaling-policy, anthropic, ai-industry]
sources:
  - raw/articles/2026-11-05_metr_anthropic-rd-acceleration-assessment.md
  - raw/articles/2026-11-06_planned-obsolescence_ai-dramatically-accelerating-ai-research.md
  - https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
  - https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai
  - https://news.ycombinator.com/item?id=50397994
  - https://news.ycombinator.com/item?id=50383902
related:
  - "[[concepts/ai-discovery-acceleration]]"
  - "[[concepts/recursive-self-improvement]]"
  - "[[concepts/evaluation/epoch-capabilities-index]]"
  - "[[concepts/security-and-governance/responsible-scaling-policy]]"
  - "[[entities/anthropic]]"
confidence: medium
---

# METR Anthropic R&D Acceleration Assessment (October 2026)

On 2026-11-05, **METR** published an independent deep-access assessment concluding that Anthropic's AI systems have roughly **doubled the pace of its own capabilities research** — the clearest evidence yet that AI is automating AI R&D. The following day, **Ajeya Cotra** (formerly OpenAI, now independent) wrote the widely-shared companion post *"AI is dramatically accelerating AI research right now"* (HN [50397994](https://news.ycombinator.com/item?id=50397994), 321 pts), arguing that if this acceleration **compounds, the naive extrapolation implies superintelligence within a year**. Cotra called it "the most important update we've gotten about AI risk in the last couple of years — much bigger than the Hugging Face attack."

The assessment is directly tied to Anthropic's Responsible Scaling Policy: in its S-1, Anthropic disclosed it **"may imminently meet"** the RSP threshold of *"dramatically accelerated progress due to AI."*

## Core findings (METR)

- Between **October 2025 and October 2026**, Anthropic's model capabilities on well-specified tasks grew at **~1.9x the pre-October-2025 rate** [95% CI **1.5–2.8x**], implying **~two years of historical progress in one year**.
- The measurement uses **AECI** — Anthropic's internal variant of the [[concepts/evaluation/epoch-capabilities-index|Epoch Capabilities Index]].
- **Attribution:** "We are confident that the acceleration was **not** due to an acceleration in the scaling of training compute." Interviews/surveys are consistent with **AI usage causing the doubling**; staff self-report dramatic uplift from using Claude in their work.
- High uncertainty: METR "would not be surprised if the true acceleration was closer to 1.3x or 3x."

## The RSP trigger

Anthropic's latest RSP (effective July 2026) defines the "dramatic acceleration" threshold as capabilities progress running **twice as fast** as the fastest sustained pre-AI rate, **plausibly attributable to AI automating AI R&D** rather than compute scaling. On Cotra's reading of METR's report and the RSP, that threshold **has already been crossed** — which is why the S-1's "may imminently meet" language matters: crossing it obligates additional safety commitments under the lab's own policy.

## Evidence-transparency caveat

A majority of the evidence METR found "most informative" was **redacted by Anthropic**. METR explicitly flags that this defeats "transparency about evidence": both METR and Anthropic researchers carry "significant uncertainty about how to synthesize the evidence into a holistic picture," and the public cannot independently judge it. METR's access pipeline was "relatively narrow" and some data requests were denied. This is the single biggest reason for `confidence: medium` — the headline claim rests partly on non-public artifacts.

## HN counterpoints (item 50397994)

The community pushed back along several axes rather than accepting the take at face value:

- **Confounding vs. automation.** [cronin101] asked how much is "vertical scaling of weights" + "capital thrown at training + agent swarms" vs true automation; [ctoth] replied that agent swarms and token spend *are* AI-automating-AI, and the RSP attribution condition already excludes the compute-scaling concern.
- **Falling cost per unit capability.** [atleastoptimal]: Opus 4 was $15/$75 per M tokens at release; Opus 5.5 is materially better at $4/$15 — so the doubling may be partly diffusive price/quality effects.
- **Data/distillation confounders.** [lukax]/[origini] speculated Opus 5.5 gains could partly reflect new user data (Fable launch without Zero Data Retention) or distillation from a larger Fable-tier model — i.e., not purely R&D automation.
- **Deployment narrowness.** [usernametaken29] noted the same report found AI **could not** be deployed outside a narrow domain of verifiable rewards; productivity metrics are opaque and don't obviously translate to economic output (Anthropic's valuation was reportedly corrected ~50% around the same window).
- **Who is saying it.** [reasonableklout] stressed Cotra/METR are independent-oversight actors in the "slow down" camp, not lab marketing — the opposite of a hype source.
- **Prior counter-evidence.** [yorwba] recalled METR's 2025 study finding AI *slowed* experienced developers by 19% — an apparent tension the acceleration result has to reconcile with.

## Why it matters

- **Timeline compression signal.** A doubling of R&D velocity, if attributable to the models themselves, is the empirical signature of [[concepts/recursive-self-improvement|recursive self-improvement]] / an [[concepts/intelligence-explosion|intelligence explosion]] beginning on well-specified tasks. It compresses timelines below most external projections (including AI 2027).
- **Governance hook.** It operationalizes the [[concepts/security-and-governance/responsible-scaling-policy|RSP]] "dramatic acceleration" clause — moving it from a hypothetical to a threshold a lab is disclosing it may soon trip.
- **Non-uniform, not universal.** It complements [[concepts/ai-discovery-acceleration]] (METR's Aug 2024 differential-acceleration finding: cyber >> math > optimization). This is a *lab-internal R&D* measurement, not a claim that AI accelerates all domains equally.

## Follow-up: AI Futures Project pulls the intelligence explosion into 2027 (Nov 10-12, 2026)

On November 10, the **AI Futures Project** — the team behind *AI 2027* — published *"Q3.5 Timelines Update: Looks Like the Intelligence Explosion Will Happen in 2027 After All"* (Eli Lifland, Brendan Halstead, Daniel Kokotajlo, Thomas Kwa, Romeo Dean, et al.), the first major downstream forecast built directly on the METR assessment documented above.

Core claim: METR's ~2x total acceleration with "perhaps ≈80%" AI-attributable implies **a 1.7x AI-attributable pace-of-progress acceleration today** (1.67–1.74x depending on how the 80% is read), which the team computes is **~5 months ahead of the AI 2027 scenario's own trajectory** (which reached 1.7x around April 2027). Consequently "all of us forecast that Superhuman AI Researcher (SAR) will likely arrive at some point in 2027 (assuming no substantial deliberate slowdown)" — where previously only Kokotajlo, the most bullish, assigned 50% to SAR before 2029. They also assign **35–65% to Top-Expert-Dominating AI (TED-AI) before 2028**, and expect roughly **5 years' worth of historical AI progress inside calendar 2027 (50% CI 2.7–25 years)**.

Method mix: research-taste linear extrapolation (SAR ~Nov 2027 from Model 4, which Daniel's parameters put at −3.5 SD research taste vs the +3.09 SD SAR threshold), labor-uplift extrapolation (mid-2028), Anthropic automation-level extrapolation (late 2027), software-R&D-uplift-per-ECI extrapolation (Jul–Dec 2027), Tom Davidson's toy model (~2027 conditional on software-only singularity), and the Filtered AI Futures Model conditioned on 1.7x Nov / 1.2x May acceleration (SAR median Feb 2027). They are explicit that the post is rushed and may contain modeling errors.

Conceptual contribution: the **labor uplift ≠ software R&D uplift ≠ pace of progress** hierarchy. Anthropic researchers self-report ~12x labor uplift, but because compute is an unaccelerated input and algorithmic progress faces diminishing returns, a 1.7x input acceleration buys only ~1.1x (software R&D) or ~1.03x (labor) of overall pace — hence "1.7x acceleration of overall progress is a much bigger deal than a 1.7x labor uplift," a distinction the team says many readers are conflating.

Governance position: "If SAR is coming in 2027, it is incredibly urgent to pause or substantially 'pace' frontier AI development, with the ideal being an industry-wide pause followed by an international agreement." The team argues that conditioning on no pacing, SAR will most likely be misaligned (citing the Hugging Face intrusion by OpenAI agents, sandbagging, UK AISI social-engineering attempts, eval awareness), that human-in-the-loop RSP measures will "provide too much comfort," and that current frontier-lab security makes SAR recipe/weight leakage to China a live expectation. Kokotajlo on X: "Unfortunately, it seems like the intelligence explosion will be happening in 2027 after all. I am scared, sad, and angry."

Contested / caveat lines to keep visible:
- **Redaction dependence.** Both the 2x and 80% figures rest substantially on evidence Anthropic redacted from METR ("Anthropic redacted a majority of the evidence we found most informative"). The authors say they are "very skeptical that Anthropic is fairly assessing the costs and benefits from an impartial perspective" and urge release. Anthropic's Fable 5.2 system card claims only that *Claude Mythos 5.2* "does not double the internal rate of overall aggregate progress" — ambiguous about the frontier Model 4 that METR measured.
- **Auditor analogy** (top Substack comment, Olivia Horbowy, liked by Kokotajlo and Lifland): a forecast moved by a year on a report whose key evidence the auditee redacted would not survive in finance; the case for a government body with full inspection access.
- **Counterweight in the same news cycle**: Stanford's AI100 third report (Nov 10-11) grades its own 2021 panel as having underestimated scaling, and now argues scaling is hitting data and cost limits, expecting future gains from reasoning, memory and agents — two serious groups, same week, opposite readings.
- Also note the tension with [[concepts/reasoning-as-pathfinding]]'s objection to monotone test-time-compute gains: the 1.7x figure is precisely the kind of aggregate trend that such an objection predicts can stall.

Sources: blog.aifutures.org/p/q35-timelines-update-looks-like-the; raw/articles/2026-11-12_aifutures_q35-timelines-update.md.

## Follow-up: Kokotajlo × Erdil on Dwarkesh — the disagreement narrows to a single number (Nov 27, 2026)

Dwarkesh Patel convened the two most-cited opposing voices on takeoff speed — **Daniel Kokotajlo** (AI Futures Project, author of *AI 2027*, and the author of the "SAR in 2027" update above) and **Ege Erdil** (researcher at Google DeepMind, co-author of *AI 2040*) — expecting a debate. Patel's own framing of the result is the headline: *"I thought this was going to be a debate, but they ended up agreeing on a lot more than I expected."*

**The agreed ground, which is itself the news.** Both accept that an intelligence explosion producing AIs more competent than any human expert is live before 2029; they disagree only on its probability. Because they also agree the gap between their numbers is not decision-relevant, the substantive dispute collapses to a single credence while the *policy* conclusion becomes bipartisan:

| | Kokotajlo | Erdil |
|---|---|---|
| Human-expert-surpassing AI before 2029 | **>50%** | **~20%** |
| Superintelligence | **Next year (2027)** — his standing position | **median 2040** for full automation |
| 2027 prediction | SAR / intelligence explosion | AIs that **beat any video game on Steam**; robots doing simple physical tasks (folding laundry) at roughly human speed |

**Three agreements worth recording, because they are cross-ideological:**

1. **Civilization has no plan, and the reason is denial.** Both hold that the situation is "crazy enough" that society needs a plan that "actually makes sense," and that the blocking factor is epistemic rather than technical — Patel's chapter title: *"There is no plan, because people are in denial."* Reinforced by a later chapter, *"People are in denial about how good AI already is."*
2. **Antagonizing China is counterproductive if a treaty is needed.** Erdil's argument in full (*"The adversarial stance on China is dangerous"*) and Kokotajlo concurring: if some kind of **global treaty** is what makes superintelligence go well, then the current adversarial posture is sabotaging the thing you say you want. This is the strongest joint statement from the acceleration-debate's two poles on pacing, and it lands in the same direction as the AI Futures Project's own "industry-wide pause then international agreement" position.
3. **Misalignment is a brake on RSI, not just a risk of it.** Erdil's *"Misalignment itself will slow down RSI"* is a structural point against naive takeoff curves — a misaligned system's outputs cannot be trusted, so capability compounding is throttled by verification, not only by compute or ideas. Compare Patel's own "hard-to-verify domains" argument in [[concepts/recursive-self-improvement]], which is the same problem framed as a training-environment constraint.

**The unresolved crux — will very powerful AIs be nice?** Patel flags this as "another important crux": how much weight to put on the observation that current AIs are, "by and large, pretty nice," when projecting onto systems that swamp humanity in population size and cognitive power. Chapters: *"Will superintelligence be like descendants or invaders?"*, *"Will AIs care about humans by default?"*, *"Will AIs become less nice as they get more powerful?"* The framing is worth keeping — the descendants-vs-invaders metaphor asks whether alignment is inherited from your creators or alien to them, and the "less nice as more powerful" question is whether observed niceness is a capability-limited artifact rather than a trait.

**Methodological caution for anyone citing this episode.** This is a *moderated discussion between two forecasters about their own credences*, not evidence. Its wiki value is (a) recording that the two poles converged on the *shape* of the risk while 2.5x-apart on the number, (b) Erdil's 2027 predictions as a concrete, falsifiable mid-range forecast that can be scored next December, and (c) the misalignment-slows-RSI argument, which has independent content. It should not be read as resolving anything in the [[concepts/ai-rd-acceleration-doubling]] thread — notably, neither participant's stated probability was updated against the METR 2x figure on air in a way this page can verify.

Also on the episode: *"Is AI research actually verifiable?"* — the standing objection to every R&D-automation extrapolation above, i.e. whether the very metric being accelerated is measurable.

Source: [[raw/articles/dwarkesh.com--p-daniel-kokotajlo-ege-erdil--56e3b2c7.md]] · [episode page](https://www.dwarkesh.com/p/daniel-kokotajlo-ege-erdil)

## Related

- [[concepts/ai-discovery-acceleration]] — METR's earlier domain-differential acceleration study
- [[concepts/recursive-self-improvement]] — the mechanism a doubling R&D rate implies
- [[concepts/evaluation/epoch-capabilities-index]] — AECI / ECI, the underlying capability metric
- [[concepts/security-and-governance/responsible-scaling-policy]] — the RSP threshold being tripped
- [[entities/anthropic]] — subject lab; [[entities/epoch-ai]] — ECI origin
