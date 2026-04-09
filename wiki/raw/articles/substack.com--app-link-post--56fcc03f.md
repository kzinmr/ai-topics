---
title: "[AINews] Gemma 4 crosses 2 million downloads"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=193410041&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM0MTAwNDEsImlhdCI6MTc3NTUyMTA1OCwiZXhwIjoxNzc4MTEzMDU4LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.C5XEDx_vczbnEwR4oz4Rak_Fk5VhVTftEx2akOcUqko"
fetched_at: 2026-04-09T16:26:00.494539+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# [AINews] Gemma 4 crosses 2 million downloads

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=193410041&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM0MTAwNDEsImlhdCI6MTc3NTUyMTA1OCwiZXhwIjoxNzc4MTEzMDU4LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.C5XEDx_vczbnEwR4oz4Rak_Fk5VhVTftEx2akOcUqko

We commented on this
last Thursday
, but Gemma 4’s continued deployment and positive reviews over the weekend has pushed it to
around 2 million downloads in its first week
!
(For contrast,
Gemma 3
totaled 6.7m downloads
in the past year,
Gemma 2
had 1.4m downloads since Jun 2024 launch, whereas
Qwen 3.5
has gained about
27m
downloads inclusive of the 1.5 months
since their 397B-A17B flagship model drop
)
The
Gemma 4 keynote
will be live in 3 days from London, which you can bookmark now:
Separately, we’d also highlight the Hermes Agent hype - our friends at the
Turing Post
have a good writeup on
the Hermes vs OpenClaw differences
.
AI News for 4/4/2026-4/6/2026. We checked 12 subreddits,
544 Twitters
and no further Discords.
AINews’ website
lets you search all past issues. As a reminder,
AINews is now a section of Latent Space
. You can
opt in/out
of email frequencies!
Gemma 4’s Rapid Local Adoption and the On-Device Open Model Moment
Gemma 4 is driving a sharp “local-first” wave
: multiple posts pointed to Gemma 4 becoming the top trending / #1 model on Hugging Face, with strong enthusiasm for its practical usability rather than just leaderboard performance—see
@ClementDelangue
,
@GlennCameronjr
, and
@Yampeleg
. The strongest signal was how quickly people were running it on consumer Apple hardware:
@adrgrondin
showed
Gemma 4 E2B
on an
iPhone 17 Pro
at roughly
40 tok/s
with
MLX
;
@enjojoyy
reported a similar iPhone deployment;
@_philschmid
highlighted Gemma 4 E2B in
AI Edge Gallery
using skills for Wikipedia queries. Red Hat also published
quantized Gemma 4 31B
model cards in
NVFP4
and
FP8-block
formats with instruction-following evals live, and reasoning/vision evals pending, via
@RedHat_AI
. Together these posts suggest Gemma 4 is not just another open release; it is becoming a reference point for
edge inference, Apple Silicon tooling, and low-friction local deployment
.
The commercial implication is pressure on paid chat subscriptions and cloud dependence
: some of the more viral commentary was reductive, but it captures a real shift.
@AlexEngineerAI
argued that Gemma 4 running locally closes enough of the gap to make a Claude subscription less compelling for some users, while
@ben_burtenshaw
reminded people that
HF-hosted models are free to use
and can replace portions of an agent workflow. On the infra side,
@ollama
launched
Gemma 4 on Ollama Cloud
backed by
NVIDIA Blackwell GPUs
, making it available to tools like OpenClaw and Claude-style workflows without self-hosting. The notable ecosystem post from
@osanseviero
also underscored how broad the launch coordination was—
HF, vLLM, llama.cpp, Ollama, NVIDIA, Unsloth, SGLang, Docker, Cloudflare
and others—which is a reminder that “open model success” increasingly depends on
simultaneous downstream systems support
, not just weights.
Hermes Agent’s Self-Improving Agent Loop, OpenClaw Friction, and the Push for Open Trace Data
Hermes Agent was the dominant agent-framework story in this batch
: the core narrative is that Nous’ system is winning mindshare by combining
persistent memory
,
self-generated/refined skills
, and a more opinionated self-improvement loop. The launch of a
Manim skill
by
@NousResearch
was especially resonant because it demonstrated an agent skill that produces immediately legible artifacts—technical animations and explainers—rather than yet another PDF summarizer. This was amplified by demos and reactions from
@ErickSky
,
@lucatac0
,
@Sentdex
,
@casper_hansen_
, and
@noctus91
. Product updates from
@Teknium
added
slash-command skill loading
for Discord/Telegram bots, while community tools like
Hermes HUD
mapped live processes to tmux panes and surfaced approvals via
@aijoey
, and multiple WebUI integrations emerged from
@Teknium
,
@nesquena
, and
@magiknono
.
The contrast with OpenClaw centered on architecture and business-model fragility
: several posts compared the two directly.
@TheTuringPost
summarized the distinction as
human-authored skills vs self-forming skills
,
Markdown memory vs persistent/searchable memory stacks
, and
gateway control plane vs self-improving loop
. That framing was echoed by practitioners like
@SnuuzyP
,
@DoctaDG
, and
@spideystreet
, many of whom cited easier onboarding and less manual skill fiddling. The backdrop here was mounting frustration with Claude subscription gating and uptime:
@theo
reported Claude Code errors when analyzing its own source;
@Yuchenj_UW
and
@ratlimit
highlighted outages;
@Yuchenj_UW
argued the
$20/$200 subscription model is structurally mismatched to 24/7 agent workloads
. That economic critique helps explain the rhetorical momentum behind
@NousResearch
’s “
Open Source is inevitable
.”
A more important long-term thread was open agent data
:
@badlogicgames
released
pi-share-hf
for publishing coding-agent sessions as Hugging Face datasets with PII defenses, then published his own sessions via
@badlogicgames
.
@ClementDelangue
explicitly framed this as the missing ingredient for
open-source frontier agents
: the community already generates the traces, so it should crowdsource the dataset. This connected cleanly to
@salman_paracha
’s
Signals
paper on trajectory sampling/triage for agentic interactions and Baseten’s argument that self-improving models should learn directly from
recorded production traces
instead of requiring clean sandboxes, via
@baseten
. This is arguably the most technically substantive “agent” trend here: not just better harnesses, but an emerging stack around
trace capture, curation, and training from real usage
.
New Research Signals: RL, Routing, Agent Evaluation, and Small Specialized Models
Post-training and RL efficiency remained active areas of substance
:
@TheTuringPost
highlighted Alibaba Qwen’s
FIPO
(
Future-KL Influenced Policy Optimization
), which assigns more credit to tokens that strongly affect future steps; the reported results included reasoning traces extending from roughly
4K to 10K+ tokens
and
AIME
gains from around
50% to ~56–58%
, ahead of cited DeepSeekR1-Zero-Math and around/overtaking o1-mini depending on setup.
@finbarrtimbers
wrote up how
OLMo 3
moved from synchronous to
asynchronous RL
, producing a
4× throughput
gain in tokens/sec. Other notable paper pointers included
Self-Distilled RLVR / RLSD
via
@_akhaliq
and
@HuggingPapers
, plus
Path-Constrained MoE
via
@TheAITimeline
, which constrains routing paths across layers to improve statistical efficiency and remove auxiliary load-balancing losses.
Agent and benchmark research is shifting away from toy tasks
:
@GeZhang86038849
introduced
XpertBench
, explicitly targeting
expert-level, open-ended workflow evaluation
rather than saturated exam-style benchmarks.
@TheTuringPost
shared a survey on tool use covering the progression from single function calls to
long-horizon orchestration
, replanning, feedback loops, and efficiency concerns such as latency/cost budgets. In data/enterprise workflows,
@CShorten30
pointed to Shreya Shankar’s
Data Agent Benchmark
for multi-step queries across heterogeneous DB systems. These are all signs that eval design is catching up to what production agent builders care about:
workflow completion, ambiguity handling, orchestration quality, and cost
.
Small specialized models continued to make strong case-study arguments
:
@DavidGFar
released
SauerkrautLM-Doom-MultiVec-1.3M
, a
1.3M-parameter ModernBERT-Hash
model trained on
31K human-play frames
that outperformed far larger API-accessed LLMs on a VizDoom task while running in
31 ms on CPU
. The result is narrow, but the point is important: appropriately scoped models can dominate on
real-time control tasks
where latency and architecture matter more than broad world knowledge. Relatedly,
@MaziyarPanahi
pushed
Falcon Perception
, a
0.6B
segmentation-oriented vision-language model reportedly outperforming SAM 3 in his comparisons and running on MacBooks with MLX; this was echoed by
@Prince_Canuma
and
@ivanfioravanti
. The recurring theme is that
specialization + better systems fit
can beat generic scale.
OpenAI and Anthropic: Policy Signaling, Governance Scrutiny, and Compute Economics
OpenAI’s biggest public move was political, not product
: the company and its allies pushed a new
“Industrial Policy for the Intelligence Age”
framing, summarized by
@kimmonismus
,
@OpenAINewsroom
, and
@AdrienLE
. Key ideas included a
Public Wealth Fund
,
portable benefits
,
32-hour workweek pilots
, a
Right to AI
, stronger provenance/audit infrastructure, and containment playbooks for dangerous released models. The notable strategic message is that OpenAI is now publicly asserting a transition toward
superintelligence
as an active policy problem, not a distant hypothetical. Reactions were mixed: some saw it as unusually frank about disruption, others as premature or politically convenient, e.g.
@Dan_Jeffries1
and
@jeremyslevin
. OpenAI also launched a
Safety Fellowship
via
@OpenAI
and
@markchen90
.
At the same time, scrutiny around Sam Altman and OpenAI governance intensified sharply
: a major New Yorker investigation was amplified by
@RonanFarrow
,
@NewYorker
, and lengthy community summaries like
@ohryansbelt
. The reporting revisited the 2023 firing/reinstatement saga with claims about internal memos, allegations of deception, board manipulation, safety-process concerns, and the under-resourcing of superalignment. OpenAI-side pushback arrived via
@tszzl
, who said the alignment team remains one of the largest and most compute-rich programs at the company. Separately,
@anissagardizy8
and
@kimmonismus
reported tension between Altman and CFO
Sarah Friar
, especially around compute spending and IPO readiness.
Anthropic’s counterpoint was compute and revenue scale
:
@AnthropicAI
announced an agreement with
Google and Broadcom
for
multiple gigawatts of next-generation TPU capacity
coming online from
2027
, to train and serve frontier Claude models. Anthropic also stated its run-rate revenue has surpassed
$30B
, up from
$9B
at the end of 2025, via
@AnthropicAI
. That pairs with reporting on the economic tension in frontier labs:
@kimmonismus
cited WSJ reporting that revenues are exploding, but
training and inference costs remain enormous
, with OpenAI projecting
$121B compute spend by 2028
. For engineers, the practical takeaway is straightforward: the frontier race is increasingly bottlenecked not by model ideas alone, but by
capital structure, long-dated compute contracts, and serving economics
.
Systems and Infra: Faster RL, Faster MoE Decoding, Better GPU/Edge Tooling
Several posts were unusually concrete about systems wins
:
@cursor_ai
reported
1.84× faster MoE token generation on Blackwell GPUs
with improved output quality via “warp decode,” a result tied directly to more frequent Composer model updates.
@tri_dao
noted that a
fast Muon optimizer
path is coming to
consumer Blackwell cards
, because the implementation is expressed as
matmul + epilogue
, allowing reuse of the mainloop work. On the RL side,
@finbarrtimbers
provided a rare engineering postmortem on making OLMo 3’s RL stack asynchronous for a
4× throughput
jump.
The Apple/local stack and training/inference education ecosystem also kept improving
:
@josephjojoe
open-sourced an
MLX port of ESM-2
for protein modeling on Apple Silicon, broadening local bio-LLM experimentation.
@rasbt
added an RSS feed to the
LLM Architecture Gallery
, a small but useful quality-of-life improvement for keeping up with model designs.
@UnslothAI
said its free notebook can now train/run
500+ models
. For deeper systems understanding,
@levidiamode
praised Hugging Face’s
Ultra-Scale Playbook
for unifying
DP/TP/PP/EP/context parallelism
with empirical scaling evidence across up to
512 GPUs
.
Top tweets (by engagement)
Gemma 4 on-device demo
:
@adrgrondin
showing
Gemma 4 E2B
on
iPhone 17 Pro
at ~
40 tok/s
with MLX was the standout technical viral post.
Claude subscription and local-open-model substitution
:
@AlexEngineerAI
captured the mood that local open models are now “good enough” for many workflows.
Open source posture
:
@NousResearch
distilled the broader movement with “
Open Source is inevitable
.”
Claude outages and gating backlash
:
@ratlimit
,
@theo
, and
@Yuchenj_UW
collectively turned uptime and subscription economics into a mainstream engineering complaint.
OpenAI governance investigation
:
@RonanFarrow
and
@ohryansbelt
drove the biggest technically adjacent corporate-governance story of the day.
Anthropic compute scale
:
@AnthropicAI
announcing
multi-gigawatt TPU capacity
and
@AnthropicAI
citing
$30B run-rate revenue
were among the clearest signals of frontier-lab scale.
