---
title: "Nathan Lambert"
tags: [person]
created: 2026-04-24
updated: 2026-08-15
type: entity
aliases:
  - natolambert
  - nathan-lambert
sources:
  - https://www.interconnects.ai/p/the-distillation-panic
  - https://www.natolambert.com/
  - https://www.interconnects.ai/
  - https://www.interconnects.ai/p/some-ideas-for-what-comes-next-may
  - raw/newsletters/2026-06-01-open-and-closed-models-are-on-different-exponentials.md
  - raw/newsletters/2026-06-14-welcome-to-the-agi-era-of-ai-governance.md
  - raw/newsletters/2026-06-17-state-of-the-blog-mid-2026.md
  - raw/articles/2026-06-16_interconnects_post-training-recipe-review.md
  - raw/newsletters/2026-07-12-6-months-to-live-for-open-models.md
  - raw/newsletters/2026-08-02-latest-open-artifacts-23-laguna-s2-1-inkling-kimi-k3-show-the-utility-of-open-mo.md
  - raw/newsletters/2026-08-03-introducing-our-artifacts-hub-and-adoption-dashboard.md
  - raw/newsletters/2026-08-10-5-useful-things-you-ll-learn-in-my-new-post-training-textbook-shipping-now.md
  - raw/newsletters/2026-08-12-i-wrote-an-ai-textbook-how-long-until-ai-can-do-it-better.md
  - raw/newsletters/2026-08-14-glm-5-3-how-chinese-labs-keep-stride-with-the-frontier.md
---

# Nathan Lambert (@natolambert)

## Overview

Nathan Lambert is a Senior Research Scientist and **Post-Training Lead** at the **Allen Institute for AI (AI2)**. He previously worked at **HuggingFace** as a Research Scientist and RLHF Team Lead (2022–2023). He earned his Ph.D. at UC Berkeley in model-based reinforcement learning. He is one of the most prominent open voices on **RLHF**, post-training techniques, and the open-source AI movement.

He writes the newsletter **Interconnects** (~70K subscribers, ~900 paid), hosts **Interconnects Interviews** podcast, and is authoring **"The RLHF Book"** (published via Manning, also freely available online at rlhfbook.com with 1,764+ GitHub stars). He founded **Interconnects AI, LLC** in January 2026 and signed advising agreements with **Arcee AI** and **Mercor** after departing Ai2.

## Background

- **Ph.D.**, UC Berkeley (2017–2022) — Model-based reinforcement learning, robotics, microrobotics
- **Internship**, Tesla — Battery engineering
- **Research Scientist Intern**, DeepMind (2021)
- **Student Researcher**, Facebook/Meta (2019–2020)
- **Research Scientist & RLHF Team Lead**, HuggingFace (May 2022 – Oct 2023)
- **Senior Research Scientist**, Allen Institute for AI (Oct 2023 – Present)
- **Founder**, Interconnects AI (Jan 2022 – Present)

His unconventional path — starting his Ph.D. in MEMS/physics, being rejected by top RL groups (Levine, Abbeel), finishing with no NeurIPS/ICML/IRCL papers, and then landing at HuggingFace — is one he shares openly to demystify AI research careers.

## Key Contributions

### OLMo & OLMo 3
- Core contributor to the **OLMo** (Open Language Model) family — Ai2's fully open LLM project releasing model weights, training data, and code
- **OLMo 3** (Dec 2025): Post-training lead for the 7B and 32B model family, including the first fully open 32B reasoning model (OLMo 3 Think 32B)
- Pioneered the "Model Flow" concept — releasing every stage, checkpoint, and data artifact to enable reproducibility

### Tülu 3
- Lead author on **Tülu 3** (Nov 2024) — a family of fully open state-of-the-art post-trained models (8B, 70B, 405B)
- Introduced **RLVR** (Reinforcement Learning with Verifiable Rewards) — training on math problems with verifiable outcomes instead of reward models
- Beat Llama 3.1 Instruct at 8B and 70B on focused tasks

### RewardBench
- Co-created **RewardBench** — the first comprehensive benchmark for evaluating reward models
- Evaluated RMs trained with PPO, DPO, and other methods across chat, reasoning, and safety tasks

### Zephyr (HuggingFace)
- Key contributor to **Zephyr-β** — a small, powerful chat model trained with Direct Preference Optimization (DPO)
- Demonstrated that effective alignment can be achieved without massive compute budgets

### The RLHF Book
- Open-source textbook at [rlhfbook.com](https://rlhfbook.com) (1,764+ GitHub stars)
- Covers RLHF from fundamentals through advanced topics: Constitutional AI, synthetic data, over-optimization, character training
- **Now shipping** (Aug 2026): physical copies available via Manning, 50% off until Aug 19, 2026
- Comes with a full **12-hour course**; the book is ~25% RL by word/page count
- Includes the **PPO clipping figure** — the surrogate objective reduces to six regions

### ATOM Project (American Truly Open Models)
- Launched in 2025 as a community movement to reinvigorate U.S. investment in open AI models
- Argues that America is losing open-model leadership to China (which has 5+ labs producing leading open models)
- Recommends at least one U.S. lab focused on training open models with 10,000+ leading-edge GPUs

## Interconnects Newsletter & Media

- **Newsletter**: Weekly analysis of AI trends, model releases, and research papers (~70K subscribers, ~900 paid)
- **Podcast**: "Interconnects Interviews" featuring conversations with leading AI researchers
- **Top podcast appearances**: Lex Fridman (2x), Latent Space (2x), ChinaTalk (5x), The MAD Podcast, Lawfare's "Scaling Laws", AI Summer
- **2025 highlights**: Covered DeepSeek V3/V4, OLMo 3 launch, RLVR revolution, sycophancy in LLMs
- **2026 highlights**: ATOM Report release, RAM metric development, Gemma 4 analysis, RLHF Book publication

### May 2026: The Distillation Panic

**"The Distillation Panic" (May 4, 2026)**: Published a major policy intervention arguing that the term "distillation attacks" is a dangerous misnomer. Key arguments:
- The real problematic behavior is **API abuse** (jailbreaking, identity spoofing, extracting reasoning traces), not distillation itself
- Anti-distillation rhetoric risks criminalizing a fundamental technique used by Anthropic, OpenAI, xAI, Nvidia, and Ai2
- Proposed alternative terminology: call it "API abuse," "jailbreaking," or "hacking" instead of "distillation attacks"
- Warned of regulatory overreach: H.B. 8283, NSTM-4 Executive Order, and Congressional probes could create a de facto ban on open-weight models
- Cited Kevin Xu's "crutch" theory — Chinese reliance on distillation may prevent original research development
- **Created concept**: [[concepts/ai-api-abuse]] — distinguishing illegitimate API access from legitimate model distillation

See [[raw/articles/2026-05-04_interconnects_distillation-panic]] and [[concepts/model-distillation]].

### April 2026 Developments

**ATOM Report & RAM Metric**: Released "The ATOM Report" with updated Relative Adoption Metric (RAM) showing:
- GPT-OSS's exceptional per-model performance despite only 2 releases
- Chinese models dominating top 10 LMArena positions
- Meta's Llama derivative share dropping from 50% to 15%
- RAM Score methodology: time+size normalized adoption trajectory prediction

**Gemma 4 Analysis**: Published insights on open model success factors, noting:
- 2026 open model landscape is crowded (Qwen 3.5, Kimi K2.5, GLM 5, MiniMax M2.5, GPT-OSS, Arcee Large, Nemotron 3, OLMo 3)
- Open models feel like "dark matter" — huge potential but few clear recipes
- Agentic AI and OpenClaw will spur mass experimentation with open models
- Key success factors: licensing simplicity, ecosystem support, release cadence

**RLHF Book Completed — Now Shipping**: The RLHF Book is now shipping in physical copies via Manning (also available free at rlhfbook.com with 1,764+ GitHub stars), 50% off until Aug 19, 2026, with a full 12-hour course included.

**Post-Training Course**: Announced development of a comprehensive post-training course covering SFT, DPO, RLVR, and synthetic data pipelines.

**"My bets on open models, mid-2026" Newsletter (Apr 15, 2026)**: Comprehensive analysis covering:
- **Capability Gap Persists**: Open models will not fully catch up to closed models; the gap is sustained by compute advantages, research depth, and real-world usage data
- **Chinese Open-Weight Labs**: Heavily benchmark-focused, effective distillation users, but expected to face funding constraints by late 2026
- **RL & Real-World Data Advantage**: Shift to RL-dominated training makes user interaction data critical; closed labs can leverage online RL from direct user feedback (e.g., Claude Code, Codex) to accelerate beyond open models
- **Open Model Market Fit**: Will dominate repetitive automation tasks (API market share), driving investment into domain-specific efficient open models
- **U.S. Adoption Shift**: U.S. will regain open-model adoption leadership starting early 2027; key catalysts: Google Gemma 4, Nvidia Nemotron, Arcee AI
- **Local Agents as "Dark Matter"**: "Local agents, OpenClaw, and other personal agents represent a large, to date, mostly ignored market for open model usage. It is a sort of dark matter, with pervasive, massive potential for influence on the balance of open-to-closed models"
- **Regulatory Reality**: Bans on frontier models are unenforceable; another sovereign will always train and release them
- **Funding Evolution**: New funding structures will emerge as enterprises and sovereigns recognize that dependencies on single, for-profit companies for AI access are unreliable

### Interconnects Podcast — Arcee AI Interview (May 2026)

Lambert hosted **Mark McQuade** (CEO) and **Lucas Atkins** (CTO) of [[entities/arcee-ai|Arcee AI]] on the Interconnects Interviews podcast. The conversation covered:
- Arcee's pivot from post-training services to **pretraining from scratch** with Trinity Large (400B/13B MoE)
- The **Muon optimizer** — Adam alternative that achieved better results with less compute on Trinity Large
- **DeepSeek-style auxiliary-loss-free load balancing** for MoE routing
- Training on **22,048 NVIDIA B300 GPUs** via TorchTitan — the largest known non-hyperscaler training cluster
- The **$20M training cost** and business model of selling post-trained open models to enterprises
- Lambert's assessment that Arcee is "taking the most real approach to monetizing open models"

### Interconnects Podcast #18 — Finbarr Timbers Interview (Jun 2026)

Lambert hosted **[[entities/finbarr-timbers|Finbarr Timbers]]** (ex-DeepMind, Midjourney, Ai2; Tülu 3, OLMo 3 co-author) for a comprehensive review of frontier post-training recipes from InstructGPT (2022) through 2026 models. Key topics:

- **Recipe evolution timeline**:
  - 2022–2023 (InstructGPT): Single SFT → reward model → RL pipeline
  - 2024 (Llama 3, Tülu 3): Open recipes formalizing SFT → DPO → RL with verifiable rewards
  - 2025 (DeepSeek R1): Reasoning RL makes large-scale RL the centerpiece
  - 2026 (MiMo Flash V2 onward): Recipes fragment into specialist models merged back into one

- **MOPD (Multi-teacher On-Policy Distillation)**: The dominant 2026 post-training pattern. Train N domain-specialist teachers (each SFT + RL on relevant domains), then train one general student by sampling its own trajectories, minimizing reverse-KL to the relevant teacher's output distribution per rollout. Lineage: MiMo Flash v2 → DeepSeek V4 & Nemotron 3 Ultra (scaling to 10+ teachers)

- **Models discussed**: MiMo Flash, DeepSeek V4, GLM 5, Kimi K2.6, Nemotron 3 Ultra

Source: [[raw/articles/2026-06-16_interconnects_post-training-recipe-review]]

### June 2026: Open and closed models are on different exponentials

**"Open and closed models are on different exponentials" (Jun 1, 2026)**: Published a provocative economic analysis arguing that open and closed models follow fundamentally different growth curves:

- **Coding agents create premium market**: Past the Opus 4.5 and Codex 5.2 thresholds, coding agents created the first large market willing to pay dramatically more for top intelligence. Users who rely on coding agents will always pay more for the best (Lambert: "I would pay $2000/month for the tools today")
- **Closed labs as Apple+Microsoft hybrid**: Frontier labs will look like a mix of Apple (integrated, hard-to-replicate technology) and Microsoft (high-leverage subscriptions). Expects Anthropic and OpenAI to reach $2-10T valuations in 5-10 years, forming an oligopoly like today's cloud market
- **Open model economics on a different curve**: Open models optimize for cost efficiency, accessibility, and democratization — a fundamentally different exponential from the premium-intelligence curve
- **Integration benefits favor closed labs**: The integration of model weights, harnesses, tools, and serving infrastructure has massive returns that open models (designed for diverse serving situations) cannot capture
- **No walls in progress**: Every direction of model improvement (speed, intelligence, specialization) remains open; there have been no walls in progress
- **Short-term vs long-term**: Near-term markets will be dictated by compute buildout and token subsidization; the true economic divergence between open and closed is a 5-10 year timeline

Added source: `raw/newsletters/2026-06-01-open-and-closed-models-are-on-different-exponentials.md`

### June 2026: Welcome to the AGI era of AI governance

**"Welcome to the AGI Era of AI Governance" (Jun 14, 2026)**: Published a policy analysis arguing that the June 12 Fable 5 export control event marks a fundamental transition from the ChatGPT governance era to the AGI governance era:

- **Government internalized AGI framing**: The Friday night government instruction to Anthropic (blocking model access for foreign nationals/overseas users) shows regulators have moved past viewing AI as a ChatGPT-era technology
- **Export bans as permanent**: Model weight export prohibitions are irreversible policy tools creating structural geopolitical divisions
- **Anthropic's advocacy boomerang**: Lambert argues Anthropic's nuclear-weapon metaphors and catastrophic-risk framing accelerated the regulatory environment that now governs Anthropic itself
- **Open-source warning**: The export control precedent can be extended to open-weight model distribution — a structural threat to open-source AI
- **Starting gun, not incident**: The event is characterized as the first instance of AGI-level government intervention, setting precedent for more aggressive regulation across jurisdictions

Contrast with Amodei's transparency-to-binding-regulation framework: Lambert's analysis centers on the geopolitical trigger (export controls) and the unintended consequences of Anthropic's own advocacy narrative, rather than institutional mechanisms like FAA-style testing agencies.

Source: `raw/newsletters/2026-06-14-welcome-to-the-agi-era-of-ai-governance`

### May 2026: Some ideas for what comes next

Published a comprehensive AI landscape analysis covering the state of the industry in May 2026. Key arguments:

- **Open models lack an "agent moment"**: Unlike Claude Code + Opus 4.5 driving Anthropic's surge, open models have no equivalent killer application — 5-6 months behind and counting
- **Gemini gap**: Google's Gemini lacks competitors for Claude Code and Codex in the coding agent space, leaving a two-horse race between Anthropic and OpenAI
- **No open-weights Mythos this year**: Despite progress, a truly frontier open model comparable to Anthropic's Mythos is unlikely in 2026
- **American open models gaining momentum**: Nvidia Nemotron and Google Gemma 4 under Apache 2.0 are outperforming Qwen in key benchmarks, shifting the open-model center of gravity
- **Anthropic vs OpenAI intensifies**: Both companies are just hitting their stride; competition is accelerating rather than consolidating
- **Power structures asserting control**: Existing institutions (governments, large corporations) are increasingly shaping AI development through regulation, compute allocation, and partnership strategies

### Departure from Ai2 (June 2026)

Nathan Lambert **departed the Allen Institute for AI (Ai2)** in June 2026, marking a significant transition in his career. Key details:

- His **last day** was in June 2026
- He joined Ai2 as "an accident" — meeting Luca at **ICML 2023** led to his role
- Proudest achievement: the **OLMo work** — leading post-training for the fully open LLM family
- Will **continue in this space**, focusing on making the open ecosystem better coordinated
- Reflects on the various paths to AI impact **beyond frontier performance**
- His departure marks the end of a ~3-year tenure at Ai2 (Oct 2023 – June 2026)

### July 2026: 6 months to live for open models

**"6 months to live for open models" (Jul 12, 2026)**: Lambert published his most urgent policy analysis to date, arguing that open-source AI faces an existential regulatory threat within the next 6 months. Key arguments:

- **White House executive order imminent**: Multiple sources cite White House discussions on managing open models via a new executive order. While official details are unconfirmed, the likely scope covers Chinese-origin models and government uses — but "this is how the dominoes start to fall."
- **6-month window**: The most likely action is to ban or indefinitely delay any open-weights model above the capability range of GPT 5.5, Claude Opus 4.8, or GLM-5.2. Given the consistent capability gap, Lambert projects this threshold will be crossed within 6 months.
- **Distillation as regulatory capture**: Argues that the distillation debate has become a "regulatory capture campaign" led by Anthropic. Anthropic's anti-Chinese model political campaign — blog posts, letters to representatives, minimal technical evidence — would grant Anthropic "substantial economic security" if the Chinese model makers they accused were banned.
- **Open models lack a champion**: Unlike frontier labs with effective lobbying, open models have no central economic actor to represent the downside of regulatory action.
- **Dual policy pressure**: Two simultaneous policy discussions — distillation restrictions and frontier capability regulation — create a "surging platform of support for a potential ban of open models in the next 6 months."
- **Anthropic's effective ask**: Lambert argues Anthropic is effectively requesting the wholesale banning of Chinese open-weight models in the US, which would "demolish the open model economy" of inference companies, fine-tuning providers, and new products.
- **Short-term off-ramp**: A US company releasing a similarly capable open model (Microsoft, Meta, or Reflection) would shift focus from "only China is building open models via distillation" to collaborative ecosystem management. Lambert calls this "an existential priority for open-source."
- **No ban without global agreement**: A US-only ban before China would be "speedrunning dystopia" — bad actors would still have access while positive actors are kneecapped. Only global agreement can add a ceiling on open-source progress.
- **Coalition building**: Lambert urges the diffuse open-source community to organize lobbying efforts immediately, as "everyone else outside the frontier labs needs to start working today."

Source: [6 months to live for open models](https://www.interconnects.ai/p/6-months-to-live-for-open-models) (Jul 12, 2026, Robotic/Interconnects)

### August 2026: Open Artifacts #23 — the consolidation prediction was wrong

**"Latest open artifacts (#23): Laguna S2.1, Inkling, & Kimi K3"** (Aug 2, 2026, Robotic/Interconnects) documents that the widely-predicted **industry consolidation did not happen** — instead, model-training capability is *diffusing*:

- **Consolidation was the prediction**: many astute observers predicted that labs training frontier models would need to consolidate (given training economics).
- **Reality — diffusion**: "All of these labs we thought would need to consolidate are realizing that the demand for tokens is incredibly high." **Thinking Machines** transitioned to an open-model company (first model: Inkling, 975B-A41B multimodal MoE), and newer entrants like **Xiaomi** are still accumulating mindshare.
- **Roundup content**: Laguna S2.1 (poolside), Inkling (Thinking Machines), Kimi K3 (Moonshot, covered separately), LongCat 2.0 1.6T (Meituan), DeepSeek V4-Flash-0731, plus new open-model releases: **Tencent Hy3** (295B-A21B MoE, notable license change), **Motif-3-Beta** (Korean Motif, 314B-A13B), **AMD Instella-MoE-16B-A3B-Think** (trained on Instinct cards, Base/SFT/MidTrain/DPO all public), **swiss-ai Apertus-v1.5-70B** (2T-token continued pretraining).
- **Thesis**: "the demand for tokens is incredibly high" — the market for open weights is growing fast enough that new entrants keep arriving rather than being absorbed.

Source: [Latest open artifacts (#23)](https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21) (Aug 2, 2026, Robotic/Interconnects)

### Artifacts Hub & Adoption Dashboard (Aug 2026)

Interconnects expanded its open-models coverage into standalone tracking projects:

- **Artifacts Hub**: a curated view of models trending on Hugging Face (**792 models**), highlighting inference tokens via OpenRouter and model intelligence via Artificial Analysis, alongside tailored adoption metrics
- **Adoption Dashboard**: a living dashboard of download and derivative-model numbers by geography and organization — visualizing the US-China adoption gap and growing players in the open ecosystem

Source: [Introducing our Artifacts Hub and Adoption Dashboard](https://www.interconnects.ai/p/introducing-our-artifacts-hub-and) (Aug 2026).

### August 2026: "I wrote an AI textbook — how long until AI can do it better?"

**"I wrote an AI textbook — how long until AI can do it better?"** (Aug 12, 2026, Robotic/Interconnects): Lambert reflected on writing his RLHF post-training textbook ([[concepts/post-training/rlhf|Reinforcement Learning from Human Feedback]], Manning) and argued that **models have stagnated in long-form, non-fiction writing** — a capability he considers a prerequisite for autonomous open-science problem solving:

- **Stagnation thesis**: "Models being stagnant in long-form, non-fiction writing should be alarming to those reliant on models autonomously solving grand, open science problems in the near future. The models today struggle to organize and compellingly present some of the most established science in their area." He calls current long-form output "entropy-increasing" and writes that today's LLMs cannot "express the full extent of their knowledge in underspecified problems."
- **Concrete model experience**: GPT models excel at finding typos — GPT 5.5 Pro found deep, surprising typos across his 200-300 page near-final PDF manuscript. Claude models are more useful as an editor: "a lot more taste," better understanding of the task's mental model, and suggestions that unstick writer's block. The recurring failure mode: models check every unit (sentence/equation/figure) but cannot revisit components and string them together as additions compound.
- **AI usage in the book**: Less than 1% of the book's sentences came from AI models — the few included because he, as an expert, felt the reader needed that exact sentence. Used Claude Code to process editor comments in LaTeX (navigating delimiter-marked comments, printing context, classifying typo vs. nuanced fix) and to sync Markdown/LaTeX versions of the book — an agent task he estimates would have taken five times longer manually.
- **Capability assessment**: Models are great in two contexts — (1) truly verifiable domains and (2) given a ton of context and making a small edit (bug-finding, specific math problems, feedback) — but not open-ended prose generation. He calls long-form writing "a strong tell" that inference-time scaling remains unlocked for one of the great intellectual pursuits.
- **Prediction**: "In 2-5 years I still expect the best textbooks to be heavily crafted by the human hand" — longer than many predicted, though long-form writing will fall before creative writing.
- **Context**: Written the same day Anthropic published a blog post on Claude making progress on a famous open science problem; Lambert notes scientific problems have vast breadth and "I don't think current AI models have as much coverage as many think."

Source: [I wrote an AI textbook — how long until AI can do it better?](https://www.interconnects.ai/p/i-wrote-an-ai-textbook-how-long-until) (Aug 12, 2026, Robotic/Interconnects).

### August 2026: GLM-5.3 — How Chinese labs keep stride with the frontier

**"GLM-5.3: How Chinese labs keep stride with the frontier"** (Aug 14, 2026, Robotic/Interconnects): Lambert's strategic analysis of the GLM-5.3 release, framing it as evidence of a **structural release-cycle advantage** for Chinese labs rather than a one-off model milestone. See [[concepts/glm-5-3]] for the full synthesis; key arguments:

- **~750B parameters vs Kimi K3**: GLM-5.3 is roughly a third of Kimi K3's size yet lands at the frontier of agentic coding benchmarks — an efficiency data point for the open-weights race.
- **Division of labor across Chinese labs**: Z.ai (GLM) leads in **post-training** (same-base post-training-only upgrade via strong RL pipelines); Moonshot (Kimi) leads in **pretraining** scale.
- **Release-cycle advantage**: Chinese labs operate on daily/weekly cadence vs US labs' monthly; open weights deployed widely generate user data that feeds the next post-training round — a compound learning engine.
- **Chinese RL data industry**: US data companies now sell training/eval data to Chinese labs (GLM-5.3's 2,436-vuln disclosure ledger as an example), inverting the older distillation narrative.
- **Staged release as safety experiment**: Z.ai's coding-plan → API → HF-weights staging plus request classifier and CoT monitoring lets it observe misuse before broad weight release; open-weights diffusion is a one-way door once guardrails become removable.

Source: [GLM-5.3: How Chinese labs keep stride with the frontier](https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride) (Aug 14, 2026, Robotic/Interconnects).

## Core Ideas

### Post-Training Is the New Bottleneck
> "Pretraining scaling as we know it is ending. Post-training is where the action is."

Lambert argues that the frontier of AI capability has shifted from pretraining scale to post-training quality. Mastering SFT, DPO, RLVR, and synthetic data pipelines is now the primary differentiator between models.

### Open Models Are Essential for Research
The OLMo project embodies his belief that truly open models — with full transparency into data, code, architecture, and training — are necessary for scientific progress. Closed models prevent reproducibility and independent verification.

### RLHF Is Underexplored and Misunderstood
Most people think RLHF is "solved." Lambert argues it's barely scratched the surface. His book and newsletter consistently push the narrative that RLHF, DPO, and related techniques are still evolving rapidly, especially with the shift to AI-generated feedback and verifiable rewards.

### AI Feedback Is Democratizing Post-Training
With GPT-4-tier models available as evaluators, the cost of preference data has dropped from ~$5–20/sample (human) to <$0.01/sample (AI). This makes high-quality post-training accessible to smaller labs.

### The "American DeepSeek" Problem
China is producing leading open models (Qwen, DeepSeek, Kimi) while the U.S. is closing off its best models. Lambert's ATOM Project is a call to action to maintain U.S. leadership in open AI research.

## Writing Style

Lambert writes with a distinctive mix of technical rigor and personal candor. He shares his career struggles openly (no top-tier papers during Ph.D., rejected by major labs) and uses his newsletter as both a research outlet and a personal journal. His posts often combine:
- Deep technical analysis of model releases
- Interviews with researchers at frontier labs
- Personal reflections on AI's trajectory
- Policy commentary on open vs. closed AI

## Related

- [[concepts/allen-institute-ai]] — Current employer, OLMo project
-  — Previous employer, Zephyr and TRL work
- [[concepts/post-training/rlhf]] — Core research area, book author
- [[concepts/post-training/rlhf-dpo-preference]] — Direct Preference Optimization, Zephyr
- [[concepts/post-training]] — His primary research focus
- [[entities/teknium]] — Fellow post-training researcher, Nous Research co-founder
-  — Co-created reward model evaluation benchmark-  — Advocate for fully open AI development- [[concepts/model-distillation]] — Fundamental ML technique; Lambert's "Distillation Panic" defends it from criminalization
- [[concepts/ai-api-abuse]] — Term Lambert coined to replace the misleading "distillation attacks" framing
- [[events/distillation-attacks-2026]] — Anthropic's accusations that prompted Lambert's response
- [[concepts/post-training]] — His newsletter and podcast-  — Open post-training model family he leads
## Key Links

- **Website**: [natolambert.com](https://www.natolambert.com/)
- **Newsletter**: [interconnects.ai](https://www.interconnects.ai/)
- **RLHF Book**: [rlhfbook.com](https://rlhfbook.com/)
- **GitHub**: [github.com/natolambert](https://github.com/natolambert)
- **LinkedIn**: [linkedin.com/in/natolambert](https://linkedin.com/in/natolambert)
- **X/Twitter**: [@natolambert](https://x.com/natolambert)
- **Google Scholar**: Available on his website

## References

- 2026-04-12-nathan-lambert-open-model-consortium
