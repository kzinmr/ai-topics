---
title: "[AINews] Humanity's Last Gasp"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=194253252&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQyNTMyNTIsImlhdCI6MTc3NjIyMjM3MSwiZXhwIjoxNzc4ODE0MzcxLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.RViTeEmXXJQHrrkzEmevskkWdBcRGeVMKIBsR5fEOCM"
fetched_at: 2026-04-15T03:06:19.867020+00:00
source_date: 2026-04-15
tags: [newsletter, auto-ingested]
---

# [AINews] Humanity's Last Gasp

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=194253252&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQyNTMyNTIsImlhdCI6MTc3NjIyMjM3MSwiZXhwIjoxNzc4ODE0MzcxLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.RViTeEmXXJQHrrkzEmevskkWdBcRGeVMKIBsR5fEOCM

One topic that has come up again and again across Latent Space and AI Engineer is how much harder everyone seems to be working:
How can it both be true that “Agents are doing more work and yet Everyone is working harder”? How can it be true that
Claude Mythos has been used internally for 2 months
, and yet
Claude keeps going down
? How can it be true that Model and Agent Labs are more productive than ever and yet
acquihiring
and
acquiring
more than ever?
A simple thought exercise we’ve made before is the “
Turkey problem
”, where, based on real evidence and an abundance of historical data, Turkeys should conclude that life is fantastic and all of humanity is set up to make turkeys well fed as far as they’ve ever experienced. Turkey doomsayers would be alarmist, crackpots, and then ignored. Until Thanksgiving.
Are engineers, or all knowledge workers in general, turkeys, in this scenario? Should our “elasticity” and value of work be increasingly positive, right up to some crossover point we become
horses
? Now that
SWE-Bench is saturated
(with
SWE-Bench Pro soon to be, Mythos is at 78%
) and
GDPval rates GPT 5.4
as better than/equal to human experts 83% of the time in most swathes of the economy, what’s left?
Notion is working on
Notion’s Last Exam
. Greg and Francois are have set out
ARC-AGI-3
. I’m working on the next frontier of coding evals. But it all seems somewhat moot if
hardware is destiny
and AGI is predictably a 20GW supercluster away…
…or are there
more valuable problems left
?
AI News for 4/3/2026-4/4/2026. We checked 12 subreddits,
544 Twitters
and no further Discords.
AINews’ website
lets you search all past issues. As a reminder,
AINews is now a section of Latent Space
. You can
opt in/out
of email frequencies!
Top Tweets (by engagement)
Google’s Chrome “Skills” turns prompts into reusable browser workflows
: Google introduced
Skills in Chrome
, letting users save Gemini prompts as one-click actions that run against the current page and selected tabs. Google also shipped a
library of ready-made Skills
, which makes this more than prompt history: it’s effectively lightweight end-user agentization inside the browser.
Tencent’s HYWorld 2.0 positions world models as editable 3D scene generators, not video models
: Ahead of release,
@DylanTFWang
teased
HYWorld 2.0
as an
open-source, engine-ready 3D world model
that generates editable 3D scenes from a single image.
Google DeepMind shipped Gemini Robotics-ER 1.6
: The new model, announced by
@GoogleDeepMind
, improves
visual/spatial reasoning
for robotics, adds safer physical reasoning, and is available in
Gemini API / AI Studio
. Follow-up posts highlight
93% instrument-reading success
and better handling of physical constraints like liquids and heavy objects.
OpenAI expanded Trusted Access for Cyber with GPT-5.4-Cyber
: OpenAI says
GPT-5.4-Cyber
is a fine-tuned version of GPT-5.4 for defensive security workflows, available to higher-tier authenticated defenders under its Trusted Access program.
Hugging Face launched “Kernels” on the Hub
:
@ClementDelangue
announced a new
repo type for GPU kernels
, with precompiled artifacts matched to exact GPU/PyTorch/OS combinations and claimed
1.7x–2.5x speedups
over PyTorch baselines.
Cursor described a multi-agent CUDA optimization system built with NVIDIA
:
@cursor_ai
says its multi-agent software engineering system delivered a
38% geomean speedup across 235 CUDA problems in 3 weeks
, a concrete example of agents being applied to systems optimization rather than app scaffolding.
Agent Infrastructure: Hermes, Deep Agents, and Production Harnesses
Hermes Agent is becoming a serious open local-agent stack, with reliability and memory as the differentiators
: Several posts converged on the same theme: users are migrating from alternatives to
Hermes Agent
because it is more durable for long-running work. The project shipped a substantial
v0.9.0
update with
web UI, model switching, iMessage/WeChat integration, backup/restore, and Android-via-tmux support
via
@AntoineRSX
, while Tencent highlighted a
one-click Lighthouse deployment
for always-on cloud hosting with messaging integrations. On the memory side,
hermes-lcm v0.2.0
from
@SteveSchoettler
adds
lossless context management
with persistent message storage, DAG summaries, and tools to expand compacted context. Community posts from
@Teknium
,
@aiqiang888
, and others reinforce that Hermes’ key advantage is less raw model IQ than
operational stability, extensibility, and deployability
.
LangChain is pushing “deep agents” toward deployable, multi-tenant, async systems
: The
deepagents 0.5
release adds
async subagents, multimodal file support, and prompt-caching improvements
. Related posts emphasize that
deepagents deploy
is an
open alternative to managed agent hosting
, with upcoming work around
memory scoped to user/agent/org
and
custom auth / per-user thread isolation
via
@LangChain
and
@sydneyrunkle
. The interesting pattern here is a shift from “agent demos” to
platform concerns
: tenancy, isolation, long-lived tasks, and integration surfaces like Salesforce and Agent Protocol-backed servers.
Harness design is becoming a first-class engineering topic
: Multiple posts argued that agent performance depends at least as much on the scaffold as the model.
@Vtrivedy10
made the clearest case for
task-specific open harnesses
over ideology (“thin vs thick”), while
@kmeanskaran
stressed workflow design, memory switching, and tool output control over frontier-model chasing. This aligns with
@ClementDelangue
asking for a curated mapping from
models to their best coding/agent harnesses
, which is increasingly necessary as open-weight models diversify.
Robotics, World Models, and 3D Generation
Google’s Gemini Robotics-ER 1.6 is a notable productization step for embodied reasoning
: The release from
@GoogleDeepMind
emphasizes better
visual/spatial understanding
, tool use, and physical constraint reasoning. Follow-ups note
10% better human injury-risk detection
, support for reading complex analog gauges, and availability in the API;
@_philschmid
highlighted
93% success on instrument-reading tasks
. This feels less like a robotics foundation-model paper drop and more like a
developer-facing embodied-reasoning API
.
World models are shifting from cinematic demos to editable spatial artifacts
: Tencent’s
HYWorld 2.0 teaser
explicitly contrasted itself with video-generation systems by framing the output as a
real 3D scene
that is editable and engine-ready. On the web side,
Spark 2.0
from
@sparkjsdev
shipped a
streamable LoD system for 3D Gaussian splats
, targeting
100M+ splat worlds
on WebGL2 across mobile, web, and VR. Together these suggest the stack for “AI-generated 3D” is maturing from content generation into
interactive rendering and downstream use
.
Open 3D generation is advancing on topology, UVs, rigging, and animation readiness
:
@DeemosTech
introduced
SATO
, an autoregressive model for
topology and UV generation
, while
@yanpei_cao
released
AniGen
, which generates
3D shape, skeleton, and skinning weights
from one image. These are meaningful because the bottleneck in production 3D pipelines is rarely “can you generate a mesh?”; it’s whether the asset is structured enough to animate, texture, and edit.
Models, Benchmarks, and Specialized Systems
