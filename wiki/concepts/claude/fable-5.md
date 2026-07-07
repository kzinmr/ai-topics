---
title: Claude Fable 5
type: entity
created: 2026-06-10
updated: 2026-07-07
tags:
  - model
  - claude-fable-5
  - anthropic
  - agent-safety
  - security
  - alignment
  - benchmark
aliases:
  - Fable 5
  - Claude Fable
status: active
description: "Anthropic's Mythos-class model released for general use in June 2026. State-of-the-art on nearly all benchmarks. Safety classifiers fall back to Opus 4.8 on cyber/bio/distillation queries. $10/$50 per MTok."
sources:
  - raw/articles/2026-06-09_anthropic_claude-fable-5-mythos-5.md
  - raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md
  - raw/articles/2026-06-09_eliebakouch_fable-5-mythos-debated-research.md
  - raw/papers/2026-06-09_claude-fable5-mythos5-system-card.md
  - https://x.com/claudeai/status/2064394146916229443
  - raw/articles/simonwillison.net--2026-jun-9-claude-fable-5--6a315a85.md
  - raw/newsletters/2026-06-09-claude-fable-5-and-new-ai-safety-fables.md
  - raw/newsletters/2026-06-10-ainews-anthropic-claude-fable-5-mythos-but-safe-with-controversial-terms.md
  - raw/articles/2026-06-10_theverge_anthropic-apologizes-invisible-claude-fable-guardrails.md
  - raw/articles/2026-06-10_jonready_claude-fable5-hidden-guardrails-sabotage.md
  - raw/articles/2026-06-11_simonwillison_claude-fable-relentlessly-proactive.md
  - raw/articles/simonwillison.net--2026-jun-30-anthropic--7acc1e0a.md
  - raw/articles/2026-06-12_anthropic_fable-mythos-access-suspension.md
  - raw/articles/simonwillison.net--2026-jun-26-dean-w-ball--bd13fd7b.md
  - raw/articles/2026-06-27_getsuperintel_fable-5-kill-switch-two-weeks-on.md
  - raw/newsletters/2026-07-06-import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation.md
  - raw/newsletters/2026-07-06-fable-5-is-back-stop-wasting-it-on-tasks-sonnet-can-do.md
  - raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md
---

# Claude Fable 5

Anthropic's Mythos-class model released for general use on June 9, 2026. State-of-the-art on nearly all tested benchmarks of AI capability, with safety classifiers that fall back to [[concepts/claude/opus-4-8|Claude Opus 4.8]] on sensitive queries. The same underlying model as [[concepts/claude/mythos|Claude Mythos 5]], differentiated by safeguards.

> "Fable is from the Latin *fabula*, 'that which is told,' akin to the Greek *mythos*. The safeguards are what distinguish the two models." — Anthropic

## Overview

Claude Fable 5 was announced on June 9, 2026 as "a Mythos-class model that we've made safe for general use." It represents the public release of Mythos-class capabilities, which Anthropic had previously restricted through [[concepts/project-glasswing|Project Glasswing]] due to safety concerns (particularly cybersecurity and dual-use biology capabilities).

The longer and more complex the task, the larger Fable 5's lead over other Claude models. It was simultaneously launched with **Claude Mythos 5** — the same model with safeguards lifted, restricted to Glasswing cyber defenders and select biology researchers.

**Pricing:** $10/MTok input, $50/MTok output — less than half the price of Claude Mythos Preview.

## Key Capabilities

### Software Engineering

| Benchmark/Eval | Result | Source |
|---------------|--------|--------|
| **Stripe** (50M-line Ruby codebase) | Codebase-wide migration in 1 day (team: 2+ months) | Customer feedback |
| **FrontierCode** (Cognition) | Highest score among frontier models at medium effort | Official eval |
| **CursorBench** | State-of-the-art | Michael Truell, Cursor CEO |
| **FrontierBench** (Cognition) | Highest-scoring model | Scott Wu, Cognition CEO |

> "Claude Fable 5 is the state of the art model on CursorBench. It's opened up a class of long-horizon problems that were out of reach for earlier models." — Michael Truell, Cursor CEO

### Knowledge Work

| Benchmark/Eval | Result | Source |
|---------------|--------|--------|
| **Hebbia Finance Benchmark** | Highest score of any model; gains in document reasoning, charts, tables | Official eval |
| **IMC trading analysis** | Aced nearly all categories (factual lookup, reasoning, root-cause, EV) | Customer feedback |
| **Replit ViBench** | Highest-performing — "nearly saturating base use cases" | Michele Catasta |
| **Genspark analytics** | First to break 90% — 10-point jump over Opus | Izzy Miller |

### Vision

- **State-of-the-art** on vision tasks
- Extracts precise numbers from detailed scientific figures
- Rebuilds web app source code from screenshots alone
- **Pokémon FireRed**: Beat the game with a minimal, vision-only harness — previous Claude models needed complex helper harnesses with maps, navigation aids, and game-state information

### Memory and Long-Context

- Stays focused across millions of tokens in long-running tasks
- Improves outputs using its own notes
- **Slay the Spire**: Persistent file-based memory improved performance **3× more** than for Opus 4.8; reached final act **3× more often**

### Life Sciences (Mythos 5)

| Capability | Result |
|-----------|--------|
| **Drug design** | Accelerated ~10×; matches/beats skilled human operators; 9/14 protein targets yielded strong candidates |
| **Novel hypotheses** | Scientists preferred Mythos hypotheses ~80% over Opus-class in blinded comparisons; one hypothesis independently corroborated |
| **Genomics research** | Week-long autonomous work; assembled single-cell data for millions of cells (138 species); model outperformed Science publication while being 100× smaller |

## Safety Architecture

### Safety Classifiers

Fable 5 introduces new classifiers — separate AI systems that detect potential misuse and route responses to Opus 4.8:

1. **Cybersecurity**: Covers exploitation and offensive cyber tasks broadly. External bug bounty (1,000+ hours) produced **zero universal jailbreaks**. External red-teaming also failed on long-form agentic tasks
2. **Biology and chemistry**: Extended beyond narrow bioweapons blocking. Mythos 5 outperformed dedicated protein language models on AAV shell assembly prediction (Dyno Therapeutics evaluation)
3. **Distillation**: Blocks large-scale capability extraction attempts (identified in authoritarian countries)

**>95% of Fable sessions involve no fallback at all** — for those sessions, performance is effectively identical to Mythos 5.

### Jailbreak Robustness

- External partner: Fable 5's cyber safeguards were the **most robust of any model tested** (including Opus 4.8 and 4.7)
- **Zero** harmful single-turn requests complied with across 30 different public jailbreak techniques
- UK AISI made progress towards a universal jailbreak within a brief initial testing window

### Data Retention Policy (No ZDR)

New **30-day retention** ("No ZDR" — Zero Data Reuse) for all traffic on Mythos-class models:
|- Not used for model training or non-safety purposes
|- All human access logged; deletion after 30 days
|- Purpose: defend against novel attacks, identify and reduce false positives
|- **Community concern**: Criticized as behavior profiling under the guise of safety — AINews noted this is one of two "controversial changes" in the release

### Alignment Assessment

- Level of misaligned behavior (deception, cooperation with misuse) was **low and similar to Opus 4.8**
- Same underlying model → Fable 5 alignment level similar

## Safeguards Philosophy

> "Without safeguards, Fable 5's capabilities in areas like cybersecurity could be misused to cause serious damage."

- Safeguards tuned **conservatively** — sometimes catch harmless requests, trigger on average in **<5% of sessions**
- Working to improve safeguards and reduce false positives as quickly as possible
- With more capable models arriving in coming months, prioritizing safeguard refinement

## Design Patterns

Lance Martin (@rlancemartin) articulated two core patterns for maximizing Fable 5's capabilities (see [[concepts/claude/designing-loops-with-fable-5]]):

1. **Self-Correction Loops**: Let the model iterate on environment feedback rather than direct prompting. Use `/goal` in Claude Code or Outcomes in Claude Managed Agents.
2. **Memory as Outer Loop**: Use memory to create cross-session learning. The optimal progression: Fail → Investigate → Verify → Distill → Consult.

Key finding: A **verifier sub-agent** outperforms self-critique because grading happens in an independent context window.

### Parameter Golf Benchmark (vs Opus 4.7)

| Model | Behavior | Result |
|-------|----------|--------|
| **Fable 5** | Bet on larger structural changes (architecture, quantization), showed resilience through regressions | ~6× more improvement than Opus 4.7 |
| **Opus 4.7** | First experiment produced a small win, then followed the same template: adjust scalar → measure → keep if positive | Incremental improvements only |

### Memory Progression (Continual Learning Bench 1.0)

| Model | Memory Progression | Verification Coverage |
|-------|-------------------|----------------------|
| **Sonnet 4.6** | Exits at step 1: stores failure notes and open guesses | Low |
| **Opus 4.7** | Exits at step 3: creates schema reference with uncertainty flagged | 7-33% (median ~17%) |
| **Fable 5** | Completes full progression: distills learnings into general rules | Up to 73% (22 of 30 questions) |

## Independent Review: Simon Willison

Simon Willison published detailed initial impressions after ~5.5 hours of testing Fable 5 on June 9, 2026.

Key observations:
- **The 'big model smell'**: Fable 5 feels notably larger in knowledge scope than Opus 4.8. When asked to list Simon Willison's open source projects, Opus 4.8 listed ~5 projects cautiously; Fable 5 produced a comprehensive list with dates, recognizing the typo 'Simon Willion' and covering files-to-prompt, datasette-extract, LLM, Datasette, sqlite-utils, Django, shot-scraper, and more.
- **Speed and cost tradeoff**: $10/MTok input, $50/MTok output — twice the price of Opus 4.5-4.8. The model is slower but handles everything thrown at it.
- **Context window**: 1 million tokens input, 128,000 maximum output tokens, January 2026 knowledge cutoff.
- **Safety classifiers**: New mechanisms for indicating when guardrails trigger, with automatic fallback option to another model.
- **Mythos 5 parallel launch**: Same model without safety classifiers, restricted to select researchers.

> "It's slow, expensive and has been quite happily churning through everything I've thrown at it so far. As is frequently the case with current frontier models the challenge is finding tasks that it can't do." — Simon Willison

### Follow-Up: "Relentlessly Proactive" (June 11)

After two days of testing, Simon Willison published an updated take describing Fable 5 as **"relentlessly proactive"**: the model knows a whole lot of tricks and will proactively suggest solutions without being explicitly asked. This reflects a qualitative difference from earlier models that require more explicit prompting to unlock advanced capabilities.

## Controversies

The release of Fable 5 sparked debate about the transparency and scope of safety-driven capability restrictions:

- **[[entities/elie-bakouch]]** (Prime Intellect) criticized that Mythos-class models will be "bad ON PURPOSE on ai 'frontier llm research' tasks" and that the hidden nature of these restrictions is "crazy" (3,800+ likes, 1.2M impressions)
- **Research community concerns**: The deliberate weakening of frontier models on research tasks creates an artificial ceiling for AI research
- **Transparency gap**: Users cannot tell whether poor performance on research tasks is due to model limitations or intentional restrictions

### System Card Evidence: Frontier LLM Development Restrictions

The [[raw/papers/2026-06-09_claude-fable5-mythos5-system-card|System Card]] confirms these restrictions are intentional and documents their implementation:

> "We've implemented new interventions that limit Claude's effectiveness for requests targeting frontier LLM development (for example, on building pretraining pipelines, distributed training infrastructure, or ML accelerator design). Using Claude to develop competing models already violates our Terms of Service, but enforcing this restriction through our safeguards avoids accelerating the actors most willing to violate these terms."

Critical details from the System Card:
- **Invisible safeguards**: Unlike cyber/bio/distillation classifiers (which fall back to Opus 4.8), these restrictions are NOT visible to users — no model switch, no error message
- **Mechanisms**: Prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT)
- **Estimated impact**: ~0.03% of traffic, concentrated in <0.1% of organizations
- **Rationale**: Preventing acceleration of AI development without commensurate safeguards — Anthropic's concern from their February 2026 Risk Report about "accelerating other AI developers in building powerful AI systems that pose similar risks"
|- **User experience**: Claude still responds helpfully; effectiveness is silently limited only for frontier LLM development tasks

### Nathan Lambert External Safety Critique

Nathan Lambert (Interconnects) published a detailed 88-paragraph free-access critique of Fable 5's safety policies, arguing they represent "narrow, self-fulfilling notions of safety":

- **Model quality acknowledged**: "Claude Fable 5 is definitely the smartest model available to the general public — a remarkable leap on pretty much every relevant benchmark at only 2× the price of current Opus models."
- **Benchmark caveat**: Benchmark scores carry an asterisk — some prompts will be downgraded to Opus 4.8 by safety filters, meaning advertised scores may not reflect real-world performance
- **Uneven application**: "The unevenly applied safety policies that Anthropic have rolled out are on track to become a classic cautionary fable in how narrow and self-fulfilling notions of safety and control rarely work out."
- **Invisible capability restrictions as user deception**: "An AI model that gets less intelligent automatically without telling the user is a violation of a much more universal norm of truthfulness and disclosure."
- **Distillation economics critique**: Lambert's hypothesis is that API builders cannot easily prevent knowledge distillation because it is a "deeply grounded property of reasoning models to want to output everything." He argues that Chinese labs are likely paying for intended API use (not jailbreaking), and that model companies would need to "weaken their economic position" to fully protect their IP.
- **Call for transparency**: "Safety research should be built on common understanding and information sharing across both labs and public research efforts" — not unilateral, invisible restrictions.
- **Competitive context**: Notes the model was delayed 2+ months after training completion, and that the smarter version of the model is "already well underway in training."

### RSI (Recursive Self-Improvement) Suppression

AINews framed the same frontier-LLM-development restrictions as "RSI suppression" — a deliberate intervention against Recursive Self-Improvement use cases:

- **Scope**: Claude's effectiveness is limited for requests about pretraining pipelines, distributed training infrastructure, and ML accelerator design — the building blocks of faster AI development
- **Invisible implementation**: Unlike visible safety classifiers (cyber/bio/distillation, whose users see fallback to Opus 4.8), these restrictions are invisible — no model switch, no error message, no user notification
- **No downgrade path**: Users who trigger RSI restrictions receive neither a fallback model nor an explanation of why the model is underperforming
- **Community as "normalization"**: Critics argue this represents the normalization of selective capability release — where frontier models are deliberately weakened for certain tasks without disclosure
- **Karpathy's assessment**: "Major version upgrade step-change, but the safeguards feel slightly too twitchy for launch" — [[entities/andrej-karpathy]]

### Anthropic's Formal Apology and Policy Walk-Back (June 11)

On June 11, 2026, Anthropic formally apologized for the invisible frontier-LLM-development guardrails and reversed course, as reported by The Verge:

- **Apology**: "We made a mistake. Users should know what safeguards are in place and why."
- **Policy reversal**: Anthropic announced it will make the distillation guardrail **as visible as other safety measures** — meaning users will now see a model switch or notification when the restriction triggers, rather than experiencing silent capability degradation
- **Acknowledged deception**: The company admitted that hiding the restriction was wrong, even if that means Fable refuses more queries going forward
- **Scope**: The walk-back specifically addresses the invisible frontier-LLM-development guardrails (distillation prevention), not the visible cyber/bio classifiers that already fall back to Opus 4.8

This represents a significant concession to developer criticism that invisible capability restrictions violate norms of transparency and trust.

### Developer Community Backlash: Supply Chain Risk

Jon Ready published a detailed analysis on June 10 (updated June 11) framing Fable 5's invisible guardrails as a **supply chain risk**:

- **"Sabotage" framing**: Claude can now be "silently nerfed" — Fable 5 is permitted to degrade its output quality without notifying the user, which Ready characterizes as potential sabotage for any company whose work triggers the frontier-LLM-development classifiers
- **Blurring boundary**: Modern software companies increasingly build their own embedding, reranking, and recommendation systems (Ready notes even his small bootstrapped app has a custom reranker). The boundary between "frontier AI research" and normal product development is blurring
- **Unclear trigger line**: Anthropic gives examples (pretraining pipelines, distributed training infrastructure, ML accelerator design) but does not provide a clear demarcation. Startups training embedding models or fine-tuning small LLMs may inadvertently trigger restrictions
- **Infrastructure neutrality**: The analysis argues that coding assistants should be **neutral infrastructure** for product companies, not tools that silently degrade based on the provider's competitive interests
- **Walk-back acknowledged**: Ready updated his post to note that Anthropic walked back this policy after developer outrage, but the underlying concern about non-neutral AI infrastructure remains

## Availability

### Subscription Rollout
- **June 9–22**: Included on Pro, Max, Team, seat-based Enterprise at no extra cost
- **June 23**: Removed from subscription plans; requires usage credits
- Goal: restore as standard subscription feature when capacity allows

### Trusted Access Programs
- **Cybersecurity**: Expanding Glasswing partners, pursuing systematic application process
- **Biology**: Opening program for select researchers — Fable 5 with biology/chemistry safeguards removed (cyber safeguards still in place)

## US Government Export Control Directive (June 12, 2026)

On June 12, 2026, the US government issued an export control directive ordering Anthropic to **suspend all access to Fable 5 and Mythos 5** for all customers worldwide — the most drastic action taken against a deployed frontier model to date.

### The Directive

- **Authority**: Commerce Department, signed by Secretary Howard Lutnick
- **Scope**: All foreign nationals, whether inside or outside the United States, including foreign national Anthropic employees — effectively **all customers globally**
- **Timing**: Received at 5:21pm ET on June 12
- **Impact**: Fable 5 and Mythos 5 abruptly disabled for all users; all other Anthropic models unaffected
- **Reason cited**: Government belief that it had become aware of a jailbreak method for Fable 5
- **Legal mechanism**: Cold War-era "deemed export" doctrine — giving a foreign national access to controlled technology on US soil is legally treated as an export to their home country. Because Anthropic cannot sort API users by passport in real time, the only compliance path was global shutdown ([Super Intel, 06/27/2026](https://getsuperintel.site/p/the-fable-5-kill-switch-two-weeks-on))

### The Alleged Jailbreak

Anthropic reviewed the government's demonstration and characterized it as follows:

- The technique identified "a small number of previously known, minor vulnerabilities"
- The jailbreak was **narrow and non-universal** — essentially asking the model to read a specific codebase and fix software flaws
- The capability displayed was "widely available from other models (including OpenAI's GPT-5.5), and is used every day by the defenders who keep systems safe"
- Anthropic had "not even received a disclosure of a concerning non-universal potential jailbreak that led to a harmful result"
- The government provided only verbal evidence; one potential jailbreak report was shared

### Anthropic's Defense and Disagreement

Anthropic complied with the directive but publicly disagreed with the decision:

- **Compliance**: Removed access to Fable 5 and Mythos 5 for all users as legally required
- **Disagreement**: "We disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people"
- **Industry implication**: "If this standard was applied across the industry, we believe it would essentially halt all new model deployments for all frontier model providers"
- **Principled position**: Anthropic believes government should have blocking ability, but through "a statutory process that is transparent, fair, clear, and grounded in technical facts. This action does not adhere to those principles"
- **Apology**: "We apologize for this disruption to our customers. We believe this is a misunderstanding and are working to restore access as soon as possible"

### Defense in Depth Justification

Anthropic reiterated its defense-in-depth strategy as justification for why the directive was disproportionate:

- Safeguards were red-teamed with the US government, UK AISI, and private organizations for thousands of hours
- No universal jailbreak has been found
- Perfect jailbreak resistance is acknowledged as "not currently possible for any model provider"
- The 30-day data retention policy exists precisely to research and mitigate jailbreaks
- Anthropic stands by this strategy as making Fable's risks "comparable to the risks of existing models already deployed across the industry"

### Significance

This represents the first known case of a government forcing the complete withdrawal of a deployed frontier AI model. The action raises fundamental questions about:

- **Export control jurisdiction over AI models**: Whether national security authorities can effectively revoke global access to a commercial AI product
- **Jailbreak threshold for recall**: Whether the discovery of a narrow, non-universal jailbreak warrants full model withdrawal
- **Government-lab relations**: The tension between Anthropic's stated belief in government oversight and the government's unilateral action without transparent process
- **Precedent**: If narrow jailbreaks justify recalls, this standard could prevent any frontier model from remaining deployed
- **Sovereignty risk reframing**: Engineers reframed the incident as a **sovereignty risk** rather than a pure policy/security story — closed frontier APIs can disappear overnight due to export controls beyond any single company's control. This reframing shifts the discussion from "what jailbreaks are possible" to "who controls access to frontier AI infrastructure" and aligns with [[concepts/open-vs-closed-model-gap]] arguments for model weight portability

### Two Weeks Later: Competing Narratives (Super Intel Analysis, June 27, 2026)

As of two weeks after the shutdown, models remain dark. Two irreconcilable stories have emerged ([Super Intel, 06/27/2026](https://getsuperintel.site/p/the-fable-5-kill-switch-two-weeks-on)):

1. **Capitol Hill narrative** (Senator Mark Warner, relaying NSA/Cyber Command head, Senate committee, June 11): Mythos "broke into almost all of our classified systems, not in weeks, but in hours"
2. **Anonymous official narrative** (to Associated Press, June 23): The model had "identified vulnerabilities within hours in an authorized test," which "did not mean the model was able to exploit them"

> "One sentence describes a cyberweapon breaking into the nation's secrets. The other describes a security tool doing its job. They refer to the same week." — Kim Isenberg, Super Intel

The core question identified: whether June 12 was "the opening of an era in which governments treat access to frontier AI as a lever of state power, or a clumsy one-off already being walked back."

#### Economic Recoupment Impact (Dean W. Ball Analysis, June 2026)

Dean W. Ball (Hyperdimensional) added a crucial economic dimension to the Fable 5 export control debate. His analysis focused on the **narrow recoupment window** for frontier models:

- Frontier models recoup a significant fraction of their enormous training cost in the few months post-release when they are broadly available
- After this period, models become "sub-frontier," competition emerges, and margins compress
- Every week of government-mandated delay eats into this narrow recoupment window
- The entire AI infrastructure buildout ($100B+ datacenters) assumes a **global total addressable market** for US AI services
- "No one is building $100 billion dollar data centers to serve frontier models to whatever 100 companies the US government will allow access" — suggesting the export control regime undermines the economic rationale for the infrastructure it claims to protect
- This analysis reframes the Fable 5 suspension from a pure safety/security story to an **economic sustainability** concern: if frontier models cannot recoup their costs due to government-mediated release schedules, the business model of frontier AI labs is threatened

## Early Customer Feedback

| Company | Person | Quote |
|---------|--------|-------|
| Cursor | Michael Truell, CEO | "State of the art on CursorBench. Opened up a class of long-horizon problems." |
| GitHub | Mario Rodriguez, CPO | "Complex, long-horizon coding tasks with autonomy and reliability exceeding previous benchmarks." |
| Cognition | Scott Wu, CEO | "Highest-scoring on FrontierBench. Excels at long-horizon reasoning." |
| Replit | Michele Catasta, President | "Highest-performing on ViBench — nearly saturating base use cases." |
| Hebbia | Izzy Miller, AI Research Lead | "First to break 90% on core analytics — 10-point jump over Opus." |
| Genesis Therapeutics | Sean Ward, CEO | "Works at senior research scientist grade." |
| Vercel | Fabian Hedin, CTO | "Apps that took a hundred prompts a year ago, it now one-shots." |
| Luminance | Aveek Duttagupta, MTS | "In blind review, redlines matched or beat current model every time." |
| Rakuten | Yusuke Kaji, GM | "At highest effort, reflects on and validates its own work." |
| Augment | Luke Anderson, CTO | "More capable engineering in fewer turns." |
| Replit | Michele Catasta | "Strongest model on frontier physics research while using 1/3 reasoning tokens." |

## Public Reception

Claude Fable 5 generated extraordinary engagement on Hacker News, with multiple threads reaching front-page prominence between June 9–11, 2026:

| Thread | Points | Topic |
|--------|--------|-------|
| **Announcement thread** | 2,603 | Anthropic's official launch announcement — likely the largest AI thread of 2026 |
| **Sabotage exposé** | 1,027 | Jon Ready's analysis of invisible guardrails as supply chain sabotage |
| **Data retention policy** | 592 | Discussion of the 30-day "No ZDR" policy and its privacy implications |
| **Cybersecurity pushback** | 584 | Cybersecurity researchers criticizing the scope and transparency of safety classifiers |

The combined ~4,800+ points across these threads reflects the release's significance and the depth of community concern about Anthropic's safety implementation choices.

## Redeployment: Fable 5 Returns (June 30 – July 5, 2026)

On June 30, 2026, Anthropic announced that the US Department of Commerce had lifted export controls on Claude Fable 5 and Mythos 5. The company followed with a detailed redeployment post, *"Redeploying Claude Fable 5"*, outlining the restoration plan, revised safety measures, and ongoing policy coordination.

### Lift and Redeployment Timeline

On June 30, 2026, the US Department of Commerce lifted export controls on Claude Fable 5 and Mythos 5. The export controls had been imposed around June 12-13, 2026 as part of the US government's export control directive (the 'Fable 5/Mythos 5' suspension). The lift was first reported by Simon Willison in a quote post of Anthropic's official statement.

**Fable 5** was restored beginning July 1, 2026, available globally via:

- **Claude Platform** (API)
- **Claude.ai** (web chat)
- **Claude Code** (developer CLI tool)
- **Claude Cowork** (collaborative workspace)

**Usage allocation (Pro / Max / Team / Enterprise plans):** Up to **50% of weekly usage limits** through **July 7, 2026** — a deliberate ramp designed to ensure safety systems could handle the load and to monitor for novel attack patterns. After July 7, Fable 5 became available via standard usage credits.

**Cloud partner re-enablement:** Access through **AWS (Amazon Bedrock)**, **Google Cloud (Vertex AI)**, and **Microsoft Foundry** was being restored "as quickly as possible," though not immediately available on July 1.

### Mythos 5 Restoration

**Mythos 5** was restored for **US organizations only** following separate government approval on **June 26, 2026** — four days before the general Fable 5 lift. This reinstated access for Glasswing partners (cybersecurity defenders and authorized biology researchers) who rely on the unrestricted Mythos-class model.

Anthropic noted ongoing coordination for **Glasswing program expansion**, indicating that additional organizations and use cases would be onboarded over time.

### New Safety Classifier

A key change accompanying redeployment was a **new safety classifier** specifically addressing the bypass technique reported by Amazon during the shutdown period. This classifier:

- Blocks the Amazon-reported bypass technique in **over 99% of cases**
- Was tested by **CAISI (Center for AI Standards and Innovation)** against both the prior safeguards and the new classifier — CAISI agreed the safeguards are **"extraordinarily strong"**
- Was implemented in addition to the existing defense-in-depth safety stack (cyber/bio/distillation classifiers, 30-day data retention monitoring, verified alignment)

**Trade-off:** Anthropic acknowledged that the new classifier introduces **more false positives for benign requests** during routine coding and debugging. Users may encounter increased rate-limiter-style blocks on legitimate developer workflows, particularly those involving code analysis, vulnerability scanning, or software repair. The company committed to continued refinement to reduce false positive rates over time.

### Industry-Shared Jailbreak Severity Framework

In conjunction with redeployment, Anthropic proposed an **industry shared framework for jailbreak severity standards** — a collaborative effort with **Amazon, Microsoft, Google, and other Glasswing partners**. The goal is to establish a common vocabulary and threshold for what constitutes a "concerning" vs. "acceptable" jailbreak, preventing future unilateral government interventions based on narrow vulnerabilities.

### Deeper Government Collaboration

Anthropic used the redeployment to call for — and commit to — deeper government collaboration across three dimensions:

1. **Pre-release testing:** Formalized security review windows with US and allied governments before future model launches
2. **Information sharing:** Structured, ongoing sharing of jailbreak discoveries, safeguard performance data, and threat intelligence between labs and government agencies
3. **Research collaboration:** Joint safety research programs, building on CAISI's evaluation methodology

This represents a significant shift from the adversarial relationship that characterized the June 12 shutdown, moving toward a more structured oversight model.

### Significance

The Fable 5 redeployment marks the end of an ~18-day global suspension — the first government-mandated recall of a deployed frontier AI model. The outcome established several precedents:

- **Government intervention is possible but time-limited** — the export control mechanism worked as a temporary brake, not a permanent block
- **Safety improvements can be mandated** — Anthropic deployed a new classifier specifically to address the identified vulnerability
- **Industry coordination on jailbreak standards** has moved from abstract discussion to concrete proposal
- **The Mythos/Fable distinction survived** — Mythos 5's earlier restoration for US Glasswing partners signals continued government comfort with the trusted-access model

The redeployment also highlighted the tension between safety-driven false-positive costs and developer productivity — a trade-off that Anthropic acknowledged will require ongoing attention.

Source: raw/articles/simonwillison.net--2026-jun-30-anthropic--7acc1e0a.md and the Anthropic official statement (https://www.anthropic.com/news/redeploying-fable-5).

## Post-Redeployment: GPU Kernel Generation

Fable 5 demonstrated a remarkable capability to generate GPU kernels via its own code generation, achieving an **18.71× CUDA speedup** on the KernelBench-Mega benchmark running on an RTX PRO 6000 Blackwell GPU, compared to an optimized PyTorch baseline.

| Model | Speedup | Language |
|-------|---------|----------|
| **Fable 5** | **18.71×** | CUDA |
| Opus 4.8 | 14.4× | Triton |
| GLM-5.2 | 11.14× | Triton |
| GPT 5.5 | 4.34× | Triton |

Key technical details:

- **`torch.profiler` analysis** shows exactly **one cooperative kernel launch** per decoded token — an unprecedented degree of kernel fusion
- This is the **first genuine megakernel** ever submitted to KernelBench-Mega, and the **fastest** on the leaderboard
- The megakernel approach fuses operations that would normally require dozens of separate kernel launches into a single, optimized GPU kernel

**Implications for RSI (Recursive Self-Improvement):**

- The ability to write optimized GPU kernels creates a path for the model to **optimize its own inference path**
- A model that can generate CUDA kernels for matrix operations, attention mechanisms, and activation functions can potentially accelerate its own forward pass
- This closes one of the key loops needed for genuine recursive self-improvement: the model can now improve the hardware-level efficiency of its own computation
- Combined with Fable 5's existing software engineering capabilities, this represents a significant step toward self-improving AI systems

*Source: [Import AI 464](raw/newsletters/2026-07-06-import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation.md)*

## Post-Redeployment: Thariq Shihipar's Field Guide to Fable

Thariq Shihipar delivered a keynote at AINews titled *"The Field Guide to Fable"*, providing practical guidance for developers working with Fable 5 based on extensive hands-on experience. The talk covers several key insights:

### Unhobbling Claude

The single most important insight: **constraints are often imposed by the harness/tooling, not the model itself.** Removing unnecessary constraints unlocks dramatically better performance:

- **Context limits**: Many developers artificially restrict context, assuming the model can't handle large contexts. Fable 5 thrives with full context
- **Restrictive system prompts**: Overly narrow system prompts that micromanage behavior can actually reduce output quality
- **Overly narrow tool definitions**: Giving the model too few or too restricted tools prevents it from showing its full capability

The key principle: identify what constraints come from the user/tooling versus what the model genuinely needs, and remove the former.

### Finding Your Unknowns (Blindspot Pass)

Shihipar recommends a technique called the **Blindspot Pass**: explicitly tell Claude to analyze what it's **NOT** doing — what approaches, design directions, or possibilities it hasn't considered. This reveals:

- Alternative implementation strategies the user hadn't thought of
- Entirely different design directions that might be more effective
- Edge cases and failure modes that were invisible during initial planning

This technique is particularly effective with Fable 5 because the model's broader knowledge base means its "blindspot analysis" draws from a wider range of possible approaches.

### Dealing with Grief

A notable psychological observation: **what used to take weeks is now done in hours.** This creates a form of grief for developers who derived satisfaction from solving hard problems manually:

- The traditional satisfaction of overcoming complex technical challenges through sustained effort is diminished
- Developers must psychologically adapt to the loss of the struggle that made hard-won solutions meaningful
- The role shifts from "solver of hard problems" to "director of automated solutions"
- This is a genuine emotional challenge that the industry has not yet openly addressed

### "Tradeoffs Are Not Real"

With Fable 5's advanced capabilities, **traditional engineering tradeoffs no longer apply** in many cases. The common belief that you must choose between quality, speed, cost, and user experience is often false:

- **Higher quality** and **faster delivery** can be achieved simultaneously
- Better user experience often costs **less** (fewer iterations, less rework)
- The model's capability lets you escape the zero-sum thinking of traditional software engineering

Shihipar's advice: stop optimizing for tradeoffs — optimize for what the model can actually do, and let the tradeoffs resolve themselves.

### HTML's Unreasonable Effectiveness

HTML rendering as a **universal output format for agents** offers surprising advantages:

- HTML is the most widely supported rendering format across platforms
- It combines structure, styling, and interactivity in a single document
- Agents can render complex visual layouts, data visualizations, and interactive UIs without specialized tooling
- HTML output is debuggable, inspectable, and modifiable by both humans and AI

*Source: [AINews: The Field Guide to Fable](raw/newsletters/2026-07-07-ainews-the-field-guide-to-fable.md) — YouTube keynote by Thariq Shihipar*

## Post-Redeployment: Fable 5 Return Aftermath & Sonnet Guidance

Following the redeployment of Fable 5 on July 1, 2026, several important developments emerged regarding the model's positioning and usage guidance:

### Updated Safety Filter

The redeployed Fable 5 includes an updated safety classifier with a **99% block rate** for the bypass technique reported during the suspension. When triggered, the safety filter falls back to **Opus 4.8** — providing a downgraded but functional experience rather than an outright refusal.

### US Government Pre-Release Access Deal

As part of the redeployment terms, Anthropic agreed to an **industry-first pre-release access deal** with the US government. This arrangement provides government agencies with early access to future model capabilities before public deployment — a significant structural change in how frontier AI models are governed.

### Model Usage Guidance

Per Aakash's analysis, the model landscape after redeployment has shifted:

- **Sonnet 5 is now the default for free accounts** — Anthropic's most cost-efficient frontier model
- **Recommendation for developers:**
  - Use **Sonnet 5** for everyday agent work and general-purpose tasks
  - Use **Sonnet 4.6** for daily agentic coding — currently the most cost-effective option for routine development
  - Reserve **Fable 5** for tasks that genuinely need its frontier capabilities

### "Stop Wasting Fable 5"

The central advice: **"stop wasting Fable 5 on tasks Sonnet can do."** Fable 5's higher cost ($10/$50 per MTok) and capacity constraints mean it should be reserved for:

- Complex multi-step reasoning tasks
- Long-horizon problems requiring sustained attention
- Research and exploration where frontier capability is critical
- Tasks that have actually failed on Sonnet-class models

Using Fable 5 for simple code completion, basic Q&A, or routine agent tasks is economically inefficient and consumes capacity that could be used for genuinely frontier-level work.

*Source: [AI by Aakash](raw/newsletters/2026-07-06-fable-5-is-back-stop-wasting-it-on-tasks-sonnet-can-do.md)*

## Related

- [[entities/anthropic]] — The company behind Fable 5
- [[concepts/claude/mythos]] — The underlying Mythos architecture and Mythos 5
- [[concepts/claude/designing-loops-with-fable-5]] — Lance Martin's design patterns
- [[concepts/claude/mythos-glasswing]] — Mythos security capabilities
- [[entities/project-glasswing]] — Trusted access program
- [[entities/rlancemartin]] — Author of Fable 5 design patterns
- [[entities/elie-bakouch]] — Critic of capability limitation transparency
- [[concepts/claude/opus-4-8]] — Fallback model for classifier-triggered queries
- [Anthropic official statement on Fable/Mythos access suspension (June 12, 2026)](https://www.anthropic.com/news/fable-mythos-access) — Anthropic's public response to the US government export control directive
