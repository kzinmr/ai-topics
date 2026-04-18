---
title: "[AINews] The Two Sides of OpenClaw"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=194589475&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQ1ODk0NzUsImlhdCI6MTc3NjQ5NTE3MywiZXhwIjoxNzc5MDg3MTczLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.pwubx80T-1JAbWJjXjSlpCjcRajmsC-m2S9cAJEn2NE"
fetched_at: 2026-04-18T06:53:03.561584+00:00
source_date: 2026-04-18
tags: [newsletter, auto-ingested]
---

# [AINews] The Two Sides of OpenClaw

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=194589475&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQ1ODk0NzUsImlhdCI6MTc3NjQ5NTE3MywiZXhwIjoxNzc5MDg3MTczLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.pwubx80T-1JAbWJjXjSlpCjcRajmsC-m2S9cAJEn2NE

In an opportune coinciding of big three letter conferences, the
TED talk
and the
AIE talks
of Peter Steinberger dropped today. To the general public, the inspiring story of OpenClaw was delightfully
told onstage
, which recaps all the highs:
To the engineering audience, it was more sober, talking about the unprecedented levels of security incidents (60x more reports than curl, at least 20% of skill contributions malicious) and scaling issues involved in maintaining the fastest growing open source project in history:
An AMA moderated by me is included at the end.
Contrast them, thoughts welcome.
AI News for 4/16/2026-4/17/2026. We checked 12 subreddits,
544 Twitters
and no further Discords.
AINews’ website
lets you search all past issues. As a reminder,
AINews is now a section of Latent Space
. You can
opt in/out
of email frequencies!
Anthropic’s Claude Opus 4.7 and Claude Design rollout
Claude Design launched as Anthropic’s first design/prototyping surface
:
@claudeai
announced
Claude Design
, a research-preview tool for generating prototypes, slides, and one-pagers from natural-language instructions, powered by
Claude Opus 4.7
. The launch immediately framed Anthropic as moving beyond chat/coding into design tooling; multiple observers called it a direct shot at
Figma/Lovable/Bolt/v0
, including
@Yuchenj_UW
,
@kimmonismus
, and
@skirano
. The market reaction itself became part of the story, with
@Yuchenj_UW
and others noting Figma’s sharp drawdown after the announcement. Product details surfaced via
@TheRundownAI
: inline refinement, sliders, exports to
Canva/PPTX/PDF/HTML
, and handoff to
Claude Code
for implementation.
Opus 4.7 looks stronger overall, but the rollout was noisy
: third-party benchmark posts were broadly favorable.
@arena
put
Opus 4.7 #1 in Code Arena
, +37 over Opus 4.6 and ahead of non-Anthropic peers there; the same account also had it at
#1 overall in Text Arena
with category wins across coding and science-heavy domains
here
.
@ArtificialAnlys
reported a near three-way tie at the top of its
Intelligence Index
—
Opus 4.7 57.3
,
Gemini 3.1 Pro 57.2
,
GPT-5.4 56.8
—while also placing Opus 4.7 first on
GDPval-AA
, their agentic benchmark. They also noted
~35% fewer output tokens
than Opus 4.6 at higher score, and introduction of
task budgets
plus full removal of extended thinking in favor of adaptive reasoning. But user experience was mixed in the first 24 hours:
@VictorTaelin
reported regressions and context failures,
@emollick
said Anthropic had already improved adaptive thinking behavior by the next day, and
@alexalbert__
confirmed that many initial bugs had been fixed. There were also complaints about product stability in Design itself from
@theo
and account-level safety issues from the same account
here
.
Cost/efficiency discussion became almost as important as raw quality
:
@scaling01
claimed
~10x fewer tokens
for some ML problem runs versus prior high-end models while maintaining similar performance, while
@ArtificialAnlys
placed Opus 4.7 on the
price/performance Pareto frontier
for both text and code. Not every benchmark agreed on absolute leadership—e.g.
@scaling01
noted it still trails
Gemini 3.1 Pro
and
GPT-5.4
on
LiveBench
—but the consensus from these posts is that Anthropic materially improved the model’s agentic utility and efficiency.
Computer use, coding agents, and harness design
Computer-use UX is becoming a mainstream product category
: OpenAI’s Codex desktop/computer-use updates drew unusually strong practitioner reactions.
@reach_vb
called
subagents + computer use
“pretty close” to AGI in practical feel;
@kr0der
,
@HamelHusain
,
@mattrickard
, and
@matvelloso
all emphasized that Codex Computer Use is not just flashy but
fast
, able to drive
Slack, browser flows, and arbitrary desktop apps
, and may be the first genuinely usable computer-use platform for enterprise legacy software.
@gdb
explicitly framed Codex as becoming a
full agentic IDE
.
The field is converging on “simple harness, strong evals, model-agnostic scaffolding”
: several high-signal posts argued that reliability gains now come more from harnesses than from chasing the very largest models.
@AsfiShaheen
described a three-stage financial analyst pipeline—
router / lane / analyst
—with strict context boundaries and gold sets for each stage, arguing that many bugs were actually instruction/interface bugs.
@AymericRoucher
extracted the same lesson from the leaked Claude Code harness: simple planning constraints plus a cleaner representation layer outperform “fancy AI scaffolds.”
@raw_works
showed an even starker example:
Qwen3-8B
scored
33/507
on LongCoT-Mini with
dspy.RLM
, versus
0/507
vanilla, arguing the scaffold—not fine-tuning—did “100% of the lifting.” LangChain shipped more of these patterns into product:
@sydneyrunkle
added
subagent support to
deepagents deploy
, and
@whoiskatrin
announced
memory primitives in the Agents SDK
.
Open-source agent stacks continue to proliferate
: Hermes Agent remained a focal point. Community ecosystem overviews from
@GitTrend0x
highlighted derivatives like
Hermes Atlas
,
Hermes-Wiki
, HUDs, and control dashboards.
@ollama
then shipped
native Hermes support
via
ollama launch hermes
, which
@NousResearch
amplified. Nous and Kimi also launched a
$25k Hermes Agent Creative Hackathon
@NousResearch
, signaling a push from coding/productivity into
creative agent
workflows.
Agent research: self-improvement, monitoring, web skills, and evaluation
A cluster of papers pushed agent robustness and continual improvement forward
:
@omarsar0
summarized
Cognitive Companion
, which monitors reasoning degradation either with an LLM judge or a hidden-state
probe
. The headline result is notable: a
logistic-regression probe on layer-28 hidden states
can detect degradation with
AUROC 0.840
at
zero measured inference overhead
, while the LLM-monitor version cuts repetition
52–62%
with ~11% overhead. Separate work on web agents from
@dair_ai
described
WebXSkill
, where agents extract reusable skills from trajectories, yielding up to
+9.8 points on WebArena
and
86.1% on WebVoyager
in grounded mode. And
@omarsar0
also highlighted
Autogenesis
, a protocol for agents to identify capability gaps, propose improvements, validate them, and integrate working changes without retraining.
Open-world evals are becoming a serious theme
: several posts argued current benchmarks are too narrow.
@CUdudec
endorsed open-world evaluations for long-horizon, open-ended settings;
@ghadfield
connected this to regulation and “economy of agents” questions; and
@PKirgis
discussed
CRUX
, a project for regular
open-world evaluations
of AI agents in messy real environments. On the measurement side,
@NandoDF
proposed broad
NLL/perplexity-based eval suites
over out-of-training-domain books/articles across
2500 topic buckets
, though that sparked debate about whether perplexity remains informative after RLHF/post-training from
@eliebakouch
,
@teortaxesTex
, and others.
Document/OCR and retrieval evals also got more agent-centric
:
@llama_index
expanded on
ParseBench
, an OCR benchmark centered on
content faithfulness
with
167K+ rule-based tests
across omissions, hallucinations, and reading-order violations—explicitly reframing the bar from “human-readable” to “reliable enough for an agent to act on.” In retrieval,
@Julian_a42f9a
noted new work showing
late-interaction retrieval representations can substitute for raw document text in RAG
, suggesting some RAG pipelines may be able to bypass full-text reconstruction.
Open models, local inference, and inference systems
Qwen3.6 local/quantized workflows were a practical bright spot
:
@victormustar
shared a concrete
llama.cpp + Pi
setup for
Qwen3.6-35B-A3B
as a local agent stack, emphasizing how viable local agentic systems now feel. Red Hat quickly followed with an
NVFP4-quantized Qwen3.6-35B-A3B
checkpoint
@RedHat_AI
, reporting preliminary
GSM8K Platinum 100.69% recovery
, and
@danielhanchen
benchmarked dynamic quants, claiming many Unsloth quants sit on the
Pareto frontier for KLD vs disk space
.
Consumer-hardware inference keeps improving
:
@RisingSayak
announced work with
PyTorch/TorchAO
enabling
offloading with FP8 and NVFP4 quants
without major latency penalties, explicitly targeting consumer GPU users constrained by memory. Apple-side local inference also got a showcase with
@googlegemma
, which demoed
Gemma 4 running fully offline on iPhone
with long context.
Inference infra updates worth noting
:
@vllm_project
highlighted
MORI-IO KV Connector
with AMD/EmbeddedLLM, claiming
2.5× higher goodput
on a
single node
via a PD-disaggregation-style connector. Cloudflare continued its agent/AI-platform push with
isitagentready.com
@Cloudflare
,
Flagship
feature flags
@fayazara
, and
shared compression dictionaries
yielding dramatic payload reductions such as
92KB → 159 bytes
in one example
@ackriv
.
AI for science, medicine, and infrastructure
Scientific discovery and personalized health were prominent applied themes
:
@JoyHeYueya
and
@Anikait_Singh_
posted about
insight anticipation
, where models generate a downstream paper’s core contribution from its “parent” papers; the latter introduced
GIANTS-4B
, an RL-trained model that reportedly beats frontier models on this task. On the health side,
@SRSchmidgall
shared a biomarker-discovery system over wearable data whose first finding was that “
late-night doomscrolling
” predicts depression severity with
ρ=0.177, p<0.001, n=7,497
—notable because the model itself named the feature. Separately,
@patrickc
argued current coding agents are already highly useful for
personalized genome interpretation
, describing <$100 analysis runs that surfaced a roughly
30× elevated melanoma predisposition
plus follow-on interventions.
Large-scale compute buildout remains a core meta-story
:
@EpochAIResearch
surveyed all
7 US Stargate sites
and concluded the project appears on track for
9+ GW by 2029
, comparable to
New York City peak demand
.
@gdb
framed Stargate as infrastructure for a “
compute-powered economy
,” while
@kimmonismus
put today’s annual global datacenter capex at roughly
5–7 Manhattan Projects per year
in inflation-adjusted terms.
Top tweets (by engagement)
