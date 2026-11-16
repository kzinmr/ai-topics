---
title: "OpenAI Second Robotics Disbandment (2026)"
type: event
created: 2026-11-16
updated: 2026-11-16
tags: [robotics, openai, ai-agents]
sources:
  - raw/articles/2026-11-13_hn-discussion_openai-robotics-disband.md
  - https://fortune.com/2026-11-13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/
  - https://news.ycombinator.com/item?id=50487184
confidence: medium
related:
  - "[[concepts/robotics]]"
  - "[[concepts/embodied-ai]]"
  - "[[entities/openai]]"
---

# OpenAI Second Robotics Disbandment (2026)

On November 13, 2026, Fortune reported that **OpenAI disbanded its robotics team as its general-purpose models started running robots directly** (HN 179 pts / 73 comments). Researchers were reportedly reassigned rather than laid off. The move echoes OpenAI's **July 2021 disbanding of its original robotics research team** — this is the second time the lab has folded a dedicated robotics group on the argument that general models subsume it.

## What was claimed

- Dedicated robotics team dissolved; general models now drive robots end-to-end.
- Reported amid pre-IPO positioning at OpenAI, which HN commenters read as cost/streamlining optics ("looks like general cost cutting to boost some numbers before IPO"), though robotics is the more capital-intensive division.
- Open question raised on HN: what happens to OpenAI's Richmond, CA robot research office.

## HN technical reception: skepticism of "general models run robots"

- **Layered-architecture consensus**: real robots run realtime servo loops on embedded hardware with tiers of increasing policy; frontier LLMs handle situation assessment and goal selection ("big picture"), while fast reactive layers and deterministic inverse-kinematics controllers handle actuation at 1kHz+ (tracerbulletx, lukan, Tadpole9181, dwattttt).
- **Latency floor**: ~36 ms per model action is the frontier even in game-playing; that allows *choosing targets* for low-level systems, not generating drive signals. Emerging pattern: have the frontier model *build* distilled fast "reflex" policies out of its own weights (gopalv).
- **Bitter Lesson debate**: jvanderbot — the Bitter Lesson guides long-lived research, not today's build decisions ("might still be a PID loop, EKF, and homographies"); ainch — Sutton himself thinks current methods are insufficient; glalonde — the lesson assumes cheap abundant compute, false on or near the robot; robotresearcher — and the tokens must be economically justified by robot value.
- **Safety/edge-compute objections**: jacquesm — robots must hold on-board authority to safely power down; cloud-only control invites regulation "written in blood." cobychapple — "nothing says reflexes like getting a 429 rate limit halfway down the stairs."
- Pointed to as the reference architecture: NVIDIA SRL's **Astranomy** project (research.nvidia.com/labs/srl/projects/astranomy/).

## Wiki context

The first disbandment (2021) is the canonical pre-Bitter-Lesson datapoint in [[concepts/robotics]]; the 2026 version inverts the argument — the specialized team is gone not because general models failed at robotics but because they reportedly started *succeeding* at the high-level layer, with the low-level layer remaining classical control. Compare Chinese embodied-AI players still running dedicated teams ([[entities/agi-bot]], [[entities/unitree-robotics]]).

## Caveats

Source is a single paywalled Fortune article; content reconstructed from the HN discussion thread (`raw/articles/2026-11-13_hn-discussion_openai-robotics-disband.md`). Details (team size, reassignments, Richmond office) unconfirmed by OpenAI as of 2026-11-16. `confidence: medium` pending an official statement or second independent source.

## Related

- [[concepts/robotics]] — Bitter Lesson in robotics, two-disbandment timeline
- [[concepts/embodied-ai]] — general-model-vs-specialized-stack debate
- [[entities/openai]] — org changes 2026

## Sources

- [[raw/articles/2026-11-13_hn-discussion_openai-robotics-disband]] — HN thread reconstruction, item 50487184
