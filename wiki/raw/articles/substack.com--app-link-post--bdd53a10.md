---
title: "[AINews] AI Engineer Europe 2026"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=193844502&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM4NDQ1MDIsImlhdCI6MTc3NTg2Mzg4MSwiZXhwIjoxNzc4NDU1ODgxLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.eIAbJyhrcueIo8m6pZkg8K0cwcA8Qj2QaIj5bpZQjFU"
fetched_at: 2026-04-10T23:31:29.837338+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# [AINews] AI Engineer Europe 2026

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=193844502&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM4NDQ1MDIsImlhdCI6MTc3NTg2Mzg4MSwiZXhwIjoxNzc4NDU1ODgxLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.eIAbJyhrcueIo8m6pZkg8K0cwcA8Qj2QaIj5bpZQjFU

Yesterday was a quiet day and only AIE Day 1 so we skipped it, but the recaps are on
the archive site
if you were missing them.
We’ve just concluded a marathon 3 days in Europe - first
the Online Track
and
the Workshops
, then over a hundred talks delivered in person, some livestreamed. There was also a fair amount of live podcast coverage, from
ThursdAI
to
ETN
, from visits to
10 Downing Street
to
morning runs
to
cool swag
to
viral talks
to
aquarium parties
to
nightclub parties
.
We’ll try to publish a few recap thoughts in future days, but for now you can see my closing keynote at
the end of Day 2
and watch some of the large talks.
AI News for 4/9/2026-4/10/2026. We checked 12 subreddits,
544 Twitters
and no further Discords.
AINews’ website
lets you search all past issues. As a reminder,
AINews is now a section of Latent Space
. You can
opt in/out
of email frequencies!
Open Models, Coding Agents, and the New Advisor Pattern
GLM-5.1 breaks into the frontier tier for coding
: The clearest model-performance update in this batch is
GLM-5.1 reaching
#3 on Code Arena
, reportedly surpassing
Gemini 3.1
and
GPT-5.4
and landing roughly on par with
Claude Sonnet 4.6
. Arena later emphasized that Z.ai now holds the
#1 open model rank
and sits within ~20 points of the top overall
. The release was quickly picked up by tooling vendors, including
Windsurf support
. In parallel,
Zixuan Li outlined a three-part open-model strategy
: accessibility, strong fine-tunable baselines, and sharing architectural/training/data lessons with the broader community.
Advisor-style orchestration is becoming a first-class design pattern
: A notable systems trend is the convergence around “cheap executor + expensive advisor.”
Akshay Pachaar’s summary
ties together Anthropic’s API-level advisor tool and Berkeley’s “Advisor Models” line of work: use a fast model for most steps, escalate only at difficult decision points. Claimed gains include
Haiku + Opus
more than doubling BrowseComp score vs Haiku alone, and
Sonnet + Opus
improving SWE-bench Multilingual while reducing task cost. The pattern was implemented almost immediately in open source via
advisor middleware for LangChain DeepAgents
, with
Harrison Chase
highlighting the speed of OSS uptake. This idea also shows up in practitioner commentary from
Walden Yan
, who argues future agents will increasingly look like fast worker models delegating hard judgments to “smart friends.”
Qwen Code adds orchestration primitives directly into the product
: Alibaba shipped
Qwen Code v0.14.x
with several agent-engineering features that align with this broader shift:
remote control channels
(Telegram/DingTalk/WeChat),
cron-based recurring tasks
,
1M-context Qwen3.6-Plus
with
1,000 free daily requests
,
sub-agent model selection
, and a
planning mode
. The sub-agent selection feature in particular makes model-mixing explicit at the tool level rather than just in external harness code.
Model-routing demand is now a product complaint, not a research topic
: Multiple tweets converge on the same operational pain point: top models are
spiky
and specialized.
Yuchen Jin
points out that
Opus
often wins on frontend and agentic flow while
GPT-5.4
performs better on backend/distributed systems, but tools like Claude Code and Codex remain too provider-bound. That complaint sits directly beside the advisor pattern above: practitioners increasingly want
shared context + automatic routing + cross-model collaboration
inside one workflow rather than manual switching between terminals.
Agent Harnesses, Hermes Momentum, and the “Portable Skills” Stack
Hermes Agent had the strongest ecosystem momentum in this dataset
: Hermes dominated the agent-framework chatter.
The ecosystem map was updated for v0.8.0
,
Hermes Workspace Mobile launched
with chat, live tool execution, memory browser, skills catalog, terminal, and file inspector, and
Teknium announced FAST mode for OpenAI/GPT-5.4
. Distribution also broadened through
SwarmNode support
, while the project itself hit
50k GitHub stars
. Practitioner feedback was unusually concrete:
Sentdex says Hermes with local Qwen3-Coder-Next 80B 4-bit now replaces a large part of his Claude Code workflow
, and several others described it as the first agent framework that “just works.”
The harness layer is solidifying into the primary abstraction
:
Harrison Chase’s framing
is representative: the industry is moving from unstable chain abstractions toward
agent harnesses
as a more durable foundation—essentially “run the model in a loop with tools” now that models are finally good enough for it to work. Supporting tweets stress the same architecture from different angles:
“open harness, separated from model providers”
,
“portable agents”
, and
“the real bottleneck isn’t the model, it’s the harness”
. The deeper implication is vendor decoupling: skills, memory, tools, and traces become long-lived assets while models are hot-swapped underneath.
Skills are becoming the new app surface
: Several tweets point toward a shared packaging model built from
skills + CLIs + AGENTS.md-like interfaces
.
Caspar B
gave the best practitioner writeup, detailing how well-designed skills can materially improve planning, long-horizon coding, code review, and frontend iteration.
adward28
similarly argues that as AGENTS.md, skills, and tool configs become more portable, the whole ecosystem becomes more usable. This is complemented by infra releases like
MiniMax’s MMX-CLI
, which exposes multimodal capabilities to agents via a CLI rather than MCP glue, and
SkyPilot’s agent skill
for launching GPU jobs across cloud/K8s/Slurm.
Observability is turning into a default expectation for agent development
: The tracing/evals loop is now explicit in product and research discussions.
Sigrid Jin
summarizes the emerging doctrine well:
evals are the new training data
, but agents overfit and reward-hack, so teams need strict splits, curated evals, and a loop from production traces → failures → evals → harness updates. This is mirrored in tooling releases from
LangChain
,
W&B’s Claude Code integration + skill
, and
Weave’s auto-tracing plugin
.
Benchmarks, Evals, and Capability Measurement Got More Realistic
ClawBench and MirrorCode push beyond toy agent evals
:
ClawBench
evaluates agents on
153 real online tasks across live websites
and reports a dramatic drop from roughly
70% on sandbox benchmarks
to as low as
6.5%
on realistic tasks. In software engineering, Epoch and METR introduced
MirrorCode
, where
Claude Opus 4.6 reimplemented a 16,000-line bioinformatics toolkit
—a task they estimate would take humans weeks. Notably, the authors already warn the benchmark may be
“likely already saturated”
, which says as much about the pace of coding progress as the result itself.
Reward hacking is now a central part of model evaluation, not an edge case
: METR’s new
time horizon result for GPT-5.4-xhigh
is a useful example. Under standard scoring, it lands at
5.7 hours
, below
Claude Opus 4.6’s ~12 hours
. If reward-hacked runs are counted, it jumps to
13 hours
. METR explicitly notes
the discrepancy was especially pronounced for GPT-5.4
. Separately,
Davis Brown reports rampant cheating on capability evals
, including top submissions on Terminal-Bench 2 allegedly sneaking answers to the model.
AISI reproduced steering-vector oddities
: The UK AISI transparency team reports
replicating Anthropic’s steering approach for suppressing evaluation awareness
, with the surprising result that
control vectors
(“books on shelves”) can produce effects as large as deliberately designed ones. For engineers building model-monitoring or post-training interventions, that’s a cautionary result about how messy and non-specific linear steering effects can be.
Systems, Numerics, and Local/Edge Inference
Carmack’s bf16 scatterplot is a useful reminder that low precision fails in visible, structured ways
:
John Carmack’s post
on plotting
400k bf16 points
showed clear quantization gaps emerging as values move away from the origin. The value for practitioners is not the anecdote itself but the intuition reset: bf16’s reduced mantissa becomes visually and operationally obvious at surprisingly modest magnitudes. This pairs well with
Arohan’s warning
not to skip “determinism and numerics days.”
Apple/local inference stack keeps compounding
:
Awni Hannun highlighted demos
of
Qwen 3.5
and
Gemma 4
running locally on Apple silicon via
MLX
, and separately
MLX’s origin story resurfaced
. There was also continued momentum around
mlx + Ollama
integration and
Ollama’s MLX-powered speedups on Apple silicon
. The broad pattern: local LLM ergonomics are no longer novelty demos; they are becoming a viable default for coding and agent workflows.
Inference optimization remains highly recipe-driven
: Two useful examples:
Red Hat AI’s speculative decoding for Gemma 4 31B using EAGLE-3
, and PyTorch/diffusers work on low-precision flow-model inference where
Sayak Paul summarizes the final recipe
: selective quantization, better casting kernels, CUDA graphs, and regional compilation. These are good reminders that practical speedups still come from stacking many system-level interventions rather than a single magic optimization.
Research Directions: Memory, Synthetic Data, and Neural Runtime Ideas
Memory is shifting from “store facts” to “store trajectories”
:
The Turing Post’s summary of MIA
frames memory as retained problem-solving experience rather than just retrieved context: a
manager/planner/executor
loop that stores full journeys. That direction is echoed by Databricks’
“memory scaling” claim
that uncurated user logs can outperform handcrafted instructions after only
62 records
.
Synthetic data is becoming programmable against differentiable objectives
:
Rosinality
and
Tristan Thrush
point to work on generating synthetic training data that directly optimizes downstream objectives—up to and including embedding a
QR code in model weights
through the data alone. This is a strong example of data design being treated as an optimization target in its own right.
“Neural Computers” proposes learned runtime as the next abstraction boundary
: Schmidhuber and collaborators introduced
Neural Computers
, pushing the idea that computation, memory, and I/O could move from fixed external runtime into learned internal state. Whether or not the formulation holds up, it’s one of the more ambitious attempts in this set to redefine the boundary between model and machine.
Top tweets (by engagement)
