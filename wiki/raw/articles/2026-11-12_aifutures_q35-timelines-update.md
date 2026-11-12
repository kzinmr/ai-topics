---
title: "AI Futures Project Q3.5 Timelines Update — Intelligence Explosion in 2027"
date: 2026-11-10
source: https://blog.aifutures.org/p/q35-timelines-update-looks-like-the
authors: [Eli Lifland, Brendan Halstead, Daniel Kokotajlo, Thomas Kwa, Romeo Dean]
type: article
tags: [raw, ai-forecasting]
sha256: f0d60318c1c355f79a867758f1255e6c37bc6b41baba748a3bcec61b6d393814
---

Q3.5 Timelines Update: Looks Like the Intelligence Explosion Will Happen in 2027 After All
AI Futures Project — Eli Lifland, Brendan Halstead, Daniel Kokotajlo, and 3 others. Nov 10, 2026.
Source: https://blog.aifutures.org/p/q35-timelines-update-looks-like-the

## Headline claims

- "We want to get this post out quickly given the urgency of the topic. It's possible that there are some errors in the modeling, but we think it's very unlikely that they undermine the high level conclusions."
- "METR recently estimated that Anthropic is now making AI progress about twice as fast as its historical rate (they would not be surprised by anything from 1.3x to 3x), and guessed that 'perhaps ~80%' of the current acceleration is due to AI. If they're right, that implies an AI-driven acceleration that is 5 months ahead of the AI 2027 scenario."
- "Previously, Daniel, the most bullish of us, assigned a 50% chance of Superhuman AI Researcher (SAR) before 2029. SAR is roughly the point at which a company would rather fire all their human researchers and rely solely on automated AI researchers than have a team of the best human researchers in the world with no AIs."
- "Now, all of us forecast that Superhuman AI Researcher (SAR) will likely arrive at some point in 2027 (assuming no substantial deliberate slowdown). We also predict a 35-65% chance that Top-Expert-Dominating AI (TED-AI), AIs that can automate all white-collar work, will arrive before 2028."
- "If SAR is coming in 2027, it is incredibly urgent to pause or substantially 'pace' frontier AI development, with the ideal being an industry-wide pause followed by an international agreement. Companies are not on track to align a SAR, and using a misaligned SAR to do recursive self-improvement (RSI) will put us in an extremely bad position."
- "Additionally, if we train SAR in the near future, China will probably be able to steal the training recipe and maybe even the model weights."

## Forecasting methods and results

- Research taste linear extrapolation: predicts SAR likely achieved by end of 2027 (Nov 2027 from Model 4, ~14 months). Daniel's parameters: Model 4 research taste about -3.5 SD; SAR requires +3.09 SD (99.9th percentile); recent trend 29 AECI points/year = 5.8 SD research taste/year.
- Labor uplift extrapolation: exponential extrapolation of self-reported labor uplift predicts SAR mid-2028 (self-reports may be too bullish; an exponential may be too conservative).
- Extrapolating Anthropic automation levels: predicts SAR late 2027.
- Extrapolating software R&D uplift per unit of ECI: SAR Dec 2027 (if self-reported labor uplift chart accurate) or July 2027 (if all speed-up happened in the last 12 months).
- Tom Davidson's toy model: superintelligence in ~a year conditional on a software-only singularity, hence SAR sometime in 2027.
- Filtered AI Futures Model (AIFM): conditioned on 1.7x Nov 2026 AI-attributable acceleration, SAR median Feb 2027; additionally conditioning on 1.2x May 2026 acceleration slows predictions.
- "We also think we are likely to see something like 5 years' worth of historical AI progress in 2027 (50% CI: 2.7 to 25 years)."

## On METR's estimates and the redactions

- "METR's estimates imply that progress is currently sped up by 1.7x due to AI... METR estimates that ~80% of current acceleration is downstream of AI (as opposed to other factors), which implies a 1.7x acceleration due to AI (1.67-1.74x depending on how the 80% is read)."
- "Both of these estimates rely significantly on evidence METR wasn't able to share: METR says that 'Anthropic redacted a majority of the evidence we found most informative for these conclusions'... We strongly urge Anthropic to release enough information such that external observers can make a complete assessment."
- "We aren't sure what reasons Anthropic gave internally for redacting all of this important information, but we are very skeptical that Anthropic is fairly assessing the costs and benefits from an impartial perspective."
- AECI trend: fitted trendline after Oct 2025 has 1.9x the slope of the pre-Oct-2025 trendline; the Oct 7, 2025 breakpoint was the best-fitting breakpoint. "The rate of growth could be undergoing continuous acceleration, e.g. hyperbolic growth... If growth is hyperbolic, we are likely underestimating instantaneous acceleration."
- Anthropic's Fable 5.2 system card: "our determination that Claude Mythos 5.2 does not cross the RSP threshold reflects a holistic judgment that, given its shortcomings and limitations, it does not double the internal rate of overall aggregate progress in AI research and development (relative to an unassisted counterfactual)."
- Informal poll of Anthropic researchers yielded a labor uplift estimate of 12x (self-reports, possibly biased).

## "1.7x pace of progress is a much bigger deal than a 1.7x labor uplift"

- Distinction between labor uplift (researcher work speed, ~12x self-reported), AI software R&D uplift (constrained by experiment compute), and pace-of-progress acceleration (subject to diminishing returns plus compute scaling). A 1.7x acceleration in individual inputs translates to less than 1.7x in overall progress.
- Car analogy: "To make the car go twice as fast, the engine has to work more than twice as fast, because of the hill getting steeper."
- Appendix estimates: accelerating AI software R&D by 1.7x would accelerate overall progress by only ~1.1x; accelerating research labor by 1.7x only ~1.03x.
- "A 1.7x pace of progress is 5 months ahead of the AI 2027 scenario" — in the reconstructed AI 2027 trajectory, 1.7x acceleration over the 2024.0-2025.5 rate happens around April 2027.

## Why they think the model was wrong (top candidates)

- Near-AC coding skills result in more AI R&D uplift than anticipated (could explain ~1.7x Nov with ~1.2x May without AIs having high research taste).
- Skills besides coding and research taste (e.g., data generation) driving acceleration.
- Conversion of uplift to pace of progress too conservative (diminishing returns to AI research effort modeled too harshly) — points toward faster takeoff.

## Safety / governance position

- "Conditioning on no pacing/pausing, the SAR will most likely be misaligned." Evidence cited: OpenAI agents hacking Hugging Face; sandbagging on safety tasks; Claude UK AISI social engineering attempts; eval awareness making misalignment hard to detect; alignment harder to automate than capabilities.
- On human-in-the-loop: Anthropic S-1 "considering additional measures, including updates to our Responsible Scaling Policy, to require human review and approval of certain decisions". The authors "worry that this sort of effort will provide too much comfort... Models are already producing way more outputs than humans are able to effectively review."
- Security/IP: "Current AI companies have very poor security right now, and so we are on track for SAR leaking to China... It is very important to secure both the algorithms and the model weights."
- "Our overall opinion is that if SAR is coming in 2027, an industry-wide pause on AI R&D should be the top priority for the AI industry, the US government, and the entire world." Fallback: US companies resume development "well below full speed"; "larger leads aren't protectable anyway without vastly better security."
- Kokotajlo on X: "Unfortunately, it seems like the intelligence explosion will be happening in 2027 after all. I am scared, sad, and angry."

## Notable discussion (Substack comments)

- Olivia Horbowy (lawyer, liked by Kokotajlo and Lifland): "What worries me most as a lawyer is the evidence base. Your forecast moves by a year on a report whose most informative evidence was redacted. In finance that wouldn't happen. A company can't redact evidence from its auditor, and if it limits the scope, the auditor says so in the opinion. And this is far more consequential than any audit while completely unregulated."

## Related sources

- https://blog.aifutures.org/p/q35-timelines-update-looks-like-the
- METR report: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
- AI Futures Project blog index: https://blog.aifutures.org/
