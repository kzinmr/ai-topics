---
title: "AI is dramatically accelerating AI research right now (Ajeya Cotra / Planned Obsolescence)"
source: https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai
author: Ajeya Cotra
published: 2026-11-06
type: article
sha256: c30db5f1aed784a59a2e4c41f2a5f3e24d2280de799bb444673111f575f8b783
---

AI is dramatically accelerating AI research right now
If acceleration compounds, the naive extrapolation implies superintelligence within a year
Ajeya Cotra — Nov 06, 2026

This post discusses a public METR report on AI R&D acceleration at Anthropic. Ajeya Cotra did not work on this project or see the unredacted report; all opinions are her own and do not represent METR or the report authors. Thanks to Ryan Greenblatt for discussion, feedback, and help with modeling, and Daniel Kokotajlo, Eli Lifland, and Hjalmar Wjik for comments.

Earlier this week, Anthropic stated in their S-1 that they "may imminently meet" the threshold of "dramatically accelerated progress due to AI" as defined in their Responsible Scaling Policy. In their latest RSP (effective July 2026), this threshold will be met when:

- They observe or expect overall capabilities progress to be going twice as fast as the fastest sustained rate before AI was contributing much to AI R&D.
- This is plausibly attributable to AI automating AI R&D, rather than acceleration in compute or other inputs.

For the last few months, some of her colleagues at METR have been working on a deep-access investigation to understand how much Anthropic is being accelerated by its AI systems. From her reading of their report and Anthropic's RSP, it looks like the "dramatic acceleration" threshold has already been crossed.

The report authors found that:

Between October 2025 and October 2026, capabilities progress at Anthropic has been going about twice as fast as it had been over the previous twelve months. The measurement they report is an internal version of the Epoch Capabilities Index called AECI; a wide range of other supporting evidence for acceleration has been redacted. They said this redacted evidence was "a majority of the evidence [they] found most informative."

This is a much bigger deal than it might sound at first. Cotra thinks this report is the most important update we have gotten about AI risk in the last couple of years — much bigger than the Hugging Face attack. Naively, it points toward much shorter timelines than most external researchers (including the AI 2027 team) have projected.

Key caveats / counterpoints raised in the HN discussion (item 50397994):
- [cronin101] wonders how much is vertical scaling of model intelligence in weights vs the sheer amount of capital and horizontal scaling of agent swarms. [ctoth] replies that agent swarms and token spend ARE AI automating AI, and the RSP attribution condition specifically excludes the "capital thrown at training" concern.
- [atleastoptimal] intelligence per dollar is rising rapidly (Opus 4 was $15/$75 per M tokens; Opus 5.5 significantly better at $4/$15).
- [pizza234] quotes METR: "Anthropic has made roughly two years of historical progress over the last year [...] We are confident that the acceleration was not due to an acceleration in the scaling of training compute." Notes Anthropic heavily censored the report.
- [lukax] / [origini] speculate the Opus 5.5 gains could partly come from more user data (Fable launch without ZDR) or distillation from a bigger Fable model.
- [usernametaken29] the same report found AI could not be deployed outside a narrow domain of verifiable rewards; productivity measures are unclear and don't obviously translate to economic output; Anthropic valuation corrected ~50%.
- [reasonableklout] the author works for METR (independent oversight), not Anthropic — she is in the "slow down" camp, not the hype camp.
- [yorwba] recalls the 2025 METR study that found AI slowed experienced developers by 19%.
