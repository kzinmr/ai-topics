---
title: "HN discussion: OpenAI disbands its robotics team as its general models start running robots"
url: https://fortune.com/2026-11-13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/
hn_item: https://news.ycombinator.com/item?id=50487184
date: 2026-11-13
fetched_at: 2026-11-16T11:15:00Z
source: hn-algolia
extraction: partial_paywalled
status: raw
---

# OpenAI disbands its robotics team as its general models start running robots

Fortune, 2026-11-13 (paywalled — Fortune returned 404/503 to programmatic fetch; content reconstructed from the HN discussion). HN item 50487184, 179 points, 73 comments.

Headline claim: OpenAI has disbanded its robotics team as its general-purpose models start running robots directly. (This echoes the 2021 disbanding of OpenAI's original robotics research team — HN surfaced the VentureBeat 2021 story alongside.) Per a commenter, researchers were not laid off but moved to other teams.

## HN discussion highlights

**Bitter Lesson debate (dominant thread):**
- scottLobster: "The Bitterer Bitter Lesson is that there are no exponentials, only S-Curves."
- jvanderbot: the Bitter Lesson can be true and you can still want bespoke solutions — it says everything about how to do research that lasts, nothing about what to build today; "that might still be a PID loop, EKF, and Homographies sometimes." Chesterton's baby/bathwater WRT humanoids.
- ainch: Sutton himself still thinks current methods are insufficient — the question is whether we have algorithms that scale sufficiently with compute.
- glalonde: the bitter lesson assumes compute is cheap and abundant, which isn't true in most robotics contexts unless the datacenter is right next to the robot; adamnemecek: also fast enough for split-second decisions. robotresearcher: it also has to make economic sense — the robot has to do something valuable to pay for the tokens.
- woopsn: if you're building robots you need a robotics team regardless; if your general model blows specialized ones out of the water, send someone to CoRL.

**Architecture of LLM-run robots:**
- deadbabe: is there a primer on using LLMs to control robots? Seems token-inefficient to stream commands at 60fps.
- tracerbulletx: robots are layered systems — realtime loops on servos/embedded hardware, tiers of increasing policy, each capable of working without higher layers.
- lukan: LLMs are used for the big picture (situation, goal, how to achieve it), not direct servo control. Tadpole9181: hierarchical — SOTA model directs intent, smaller reactive models translate intent into actions, deterministic layer handles inverse kinematics ("like how I control my body").
- gopalv: frontier models are ~36ms behind per action in game-playing settings; the idea is to have a frontier model *build* fast low-level "Reflex agents" out of its own weights; dwattttt: at ~30ms per choice you can choose what lower-level systems drive toward, but can't generate the drive signals — that needs 1kHz+.
- veganmosfet points to an NVIDIA study: research.nvidia.com/labs/srl/projects/astranomy/
- photochemsyn: "termite mound" model — harness-type LLM coordinating robot swarms inside a non-LLM deterministic controller that rejects banned actions; the only plausible safe architecture once you accept alignment can be internally subverted.
- cobychapple: "nothing says reflexes like getting a 429 rate limit halfway down the stairs." raincole: "General models can {insert something general models will be very good at}. They are very bad at it. Every single time."

**Motivation skepticism:**
- winfredJa: looks like general cost cutting to boost numbers before IPO; counter (seanmcdirmid): researchers were reassigned, not fired — though robotics is more capital-intensive than software.
- jacquesm: anything with a motor should have sufficient executive authority on-board to decide how to safely power down; loss of communications is a major impediment to deploying robotics — regulation "written in blood" territory.
- torginus: if general models run on-robot they must be small/cheap, which would be surprising; even a 30B quantized LLM at meaningful speed costs tens of thousands in silicon. janalsncm: easier to train a big model and distill than train small from scratch — never say never.
- jeffbee: does this mean anything for OpenAI's Richmond, CA robot research office?
