---
title: "interconnects scrape"
source_url: https://www.interconnects.ai/p/open-source-ai-reading-list
ingested: 2026-09-14
fetched_at: 2026-09-14T11:23:41.406190Z
sha256: 9687fa282d61a60dcffb0304dd068c251bc339e84cf8c10d369a4ddd3fd5683c
---

# interconnects

Open-Source AI & Open Models Reading List

SubscribeSign inOpen-Source AI & Open Models Reading List

How to get up to speed on open models and their implications.

112618ShareHey all! I’ve been prepping for some public-audience and policy-facing writing on open models, so I figured I would share my research materials. There’s lots of wonderful stuff in here.

This is my list of the best writing on open models in the last few years. If someone decides they want to get up to speed on the area, reading this will be a comprehensive overview of the state of affairs. Please comment pieces to consider adding below, and I’ll update this over time.

List last updated: 13 Sep. 2026

Share

Foundation

What open models are, why people release them, how they relate to business strategy, and what the risks are.

On open source AI strategy, a walkthrough of how open-source software has been used by businesses and early signs of what that means for AI — From Open Source Software to Open Source Strategy, Bill Gurley (May 2026).

One of the clearest articulations is Mark Zuckerberg’s comments around Llama 3’s release as to why Meta releases open models — Open Source AI is the Path Forward, Mark Zuckerberg (Jul. 2024)

Why you should view open models on a gradient, rather than binary open/closed, based on factors such as licenses, cost of running the model, data access, etc. — The Gradient of Generative AI Release: Methods and Considerations, Irene Solaiman (Feb. 2023).

The role open models will play in the economy of the future, as a complement to strong closed models. Why open models will be used to create custom agentic workflows in enterprises across the world – What comes next with open models, Nathan Lambert / Interconnects (Mar. 2026)

A position on how open models will capture value by providing a complementary tool to large swaths of the existing economy, drawing on the history of IP and current debates on open vs. closed models (e.g. distillation) — Some Simple Economics of Open versus Closed AI, Christian Catalini (Aug. 2026)

Why open models will constantly be behind closed models in performance — Open models in perpetual catch-up, Nathan Lambert / Interconnects (Feb. 2026)

Where adoption differs for open and closed models — Open and closed models are on different exponentials, Nathan Lambert / Interconnects (Jun. 2026)

A clear articulation on how to balance releasing powerful open-weight models while taking safety seriously — A Safe Path to Open Weights, Thinking Machines Lab (Jul. 2026).

Early paper on marginal risks that showed text-focused LLMs very marginally increased documented potential risks of models — On the Societal Impact of Open Foundation Models, Sayash Kapoor, Rishi Bommasani et al. (Feb. 2024).

Closed models safety guardrails are regularly bypassed causing a plethora of real AI-risks before hypothetical risks of open weight models have emerged — The Myth of unsafe Open Source AI, Florian Brand (Jun. 2026).

The mass reduction in open data, which is a crucial factor that has hampered truly open AI research — Consent in Crisis: The Rapid Decline of the AI Data Commons, Shayne Longpre et al. (Jul. 2024).

Recent examples on how strong Chinese models impact the AI ecosystem — Kimi K3: The open-weights escalation, Nathan Lambert / Interconnects (Jul. 2026) / GLM-5.2 is the step change for open agents, Nathan Lambert / Interconnects (Jun. 2026).

A summary of the story of open models in 2025: Nathan Lambert on China’s AI Ecosystem and the Open Model Gap | The Curve 2025, Golden Gate Institute for AI (Nov. 2025).

[Optional] Latest data on open model adoption: A general summary on US vs. China model adoption — The ATOM Report (Apr. 2026), The latest data on model downloads, derivatives, and research adoption by region — Interconnects Adoption Dashboard, and The most important models to know about in the ecosystem — Interconnects Artifacts Hub

Interconnects AI is a reader-supported publication. Consider becoming a subscriber.

US-China Competition

Who is leading in open models, how this has changed over time, how China maintains its leading position, and relevant history.

Why the U.S. needs to invest in open models for fundamental R&D / innovation in the face of growing competition from China – The ATOM Project, Nathan Lambert (Aug. 2025)

The lens as to why open models help spur research innovation and beneficial outcomes for AI — Why I build open language models, Nathan Lambert / Interconnects (Oct. 2024)

Why open models foster education, innovation and competition, three core American values — Banning Open Source AI Would Be A Mistake, Nathan Lambert & Kevin Xu (Jun. 2026)

Why the recent “vibe regulation” / vague federal oversight mechanisms set us up for a clash and-or ban of frontier open models in the near future — 6 months to live for open models, Nathan Lambert / Interconnects (Jul. 2026)

[Optional] Fully open language model technical reports to illustrate the start of the art in understanding: Pythia (EleutherAI, 2023), Olmo (2024), Olmo 2 (2024), Olmo 3 (2025)

Chinese open-source history leading up to AI — Chinese Open Source: A Definitive History, Kevin Xu (Mar. 2026).

China’s structural advantages in open-source — China’s Structural Advantage in Open Source AI, Kevin Xu (Jun. 2025).

How Chinese labs themselves discuss building models, and how the Chinese industry differs from the U.S. — Notes from inside China’s AI labs, Nathan Lambert / Interconnects (May 2026).

Why Chinese labs are so good at keeping up with American competition (e.g. American open weight labs struggle to compete with Chinese labs on fair performance comparisons) — GLM-5.3: How Chinese labs keep stride with the frontier, Nathan Lambert / Interconnects (Aug. 2026).

Prominent uses of Chinese models by Western companies have prompted meaningful regulatory attention (more discussion)

Lawmakers have probed the following companies over using Chinese models: DoorDash (CNBC, Jul. 31 2026), Airbnb (Bloomberg, Apr. 29 2026; Semafor, Apr. 29 2026), Anysphere / Cursor (Bloomberg, Apr. 29 2026; Semafor, Apr. 29 2026), Apple (Reuters, May 17 2025)

Other western companies have very publicly shifted the models they use from American, closed labs to Chinese open models to save costs. Examples include Perplexity prominently and rapidly adopted DeepSeek R1 (Forbes, Jan. 28 2025) and Thomson Reuters building on Qwen to move off Claude (Business Insider, Aug. 24 2026)

Leave a comment

Technical Details

What is distillation and how much does it help Chinese labs, how do open models impact frontier AI risks like cybersecurity, and how far are open models behind the closed frontier?

The open-closed model gap has reduced in recent years, and is now at roughly 4-6 months. The leading open models have all come from Chinese labs since ~2024.

SemiAnalysis article which ran independent evaluations, concluding that open models have been getting closer to the closer frontier of performance over time — Are Open Models Catching Up?, SemiAnalysis (Aug. 2026)

Open models are on the Pareto cost frontier, while not at the absolute performance frontier. E.g. DeepSeek V4 Flash, see evaluation and cost on Artificial Analysis.

Data sources from Epoch AI and Artificial Analysis (and U.S. v China, related) showing the open-closed gap over time.

An independent analysis of the open-closed gap across a mix of public and private evaluations — How far behind are open models?, Håvard Tveit Ihle (May 2026)

E.g. in 2025, the product lead of Z.ai said with respect to their release time “Get it out fast. We open source it within a few hours.” — The Z.ai Playbook, ChinaTalk (Nov. 21, 2025)

Cyber, risks & open models (I plan to develop this further)

Why we cannot effectively ban open models as used by bad actors for cyber capabilities (they will always have access) — The OpenAI/Huggingface incident; how we should manage the imminent arrival of autonomous hacking too cheap to meter, Joshua Saxe (Jul. 2026)

What the government should do to observe, orient, decide, and act with respect to emerging cyber threats (versus blocking models based on in-house capability assessments) — We urgently need a coherent national AI cybersecurity policy, Joshua Saxe (Aug. 2026)

Why you cannot expect to control access to AI at a certain threshold (e.g. open weight models) and need to prepare society to tackle risks downstream of available intelligence — Nonproliferation is the wrong approach to AI misuse, Helen Toner (Apr. 2025)

Distillation – the process of training on output tokens from another model – is the single most eventful debate around open models in 2026.

For basic background, see a textbook chapter on synthetic data & distillation generally, from Reinforcement Learning from Human Feedback (post-training textbook published in 2026)

How distillation helps the Chinese labs, but doesn’t take away from their innovation — How much does distillation really matter for Chinese LLMs?, Nathan Lambert / Interconnects (Feb. 2026)

A very transparent documentation of how Chinese company use Anthropic’s products and circumvent the terms of service or intended use. The report details at-scale usage of Anthropic’s products by banned parties, as a mix of technical distillation (mentioned via SFT data) and extensive routing of Claude into their products and services without telling users —Detecting and countering misuse of AI: September 2026.

A recent paper that showed that the frontier labs had implementations in their APIs that made systematic extraction of reasoning traces (the crucial part of modern training) through clever tricks. Recent distillation paper, my writing on it — Stealing Reasoning Traces from Proprietary LLM APIs, Panfilov, Schmotz, Shumailov et. al 2026 (more on X). Anthropic confirmed this technique was used by Chinese labs.

Why the political panic over distillation, claiming that distillation is the only reason Chinese models are close to the frontier, is not grounded in the evidence — The distillation panic, Nathan Lambert / Interconnects (May 2026)

How labs can use distillation to improve models in an era of scaling RL environments across agentic behaviors — How distillation is used today and what performance uplift it gives to open models, Nathan Lambert (Jul. 2026)

[Optional] More history: In 2024, I wrote Frontiers in synthetic data where the key points were that synthetic data, primarily in “distilling” models by training with SFT on outputs from a stronger model, was the dominant form of distillation. Frontier labs had been shifting the logit-based, knowledge distillation, confirmed earliest in Gemini and continuing to this day. In early 2025, there was substantial debate on if DeepSeek-R1 was distilled from OpenAI’s o1 model. There is no clear evidence suggesting that they did, and in Apr. of 2025 I wrote confidently that DeepSeek did not distill. At the time of R1, it is more possible than I gave it credit to that DeepSeek did distill some o1 traces to make it easier for them to train their R1 model – based on the above reasoning trace extraction methods. This does not take away from the innovation of it, but it’s worth being realistic and is a way that distillation could accelerate China closing the gap to American labs.

112618SharePreviousDiscussion about this postCommentsRestacksInterconnects AI reply rulesMax Körbächer19hLiked by Nathan LambertCan approve, very helpful list, I had a few of them already bookmarked!

ReplyShareCeline Nguyen19hLiked by Nathan Lambertthank you so much for this!! really fortuitous timing bc I was just trying to collect my own reading list on open-weight models, but this is a much better starting point—really appreciate you sharing

ReplyShare4 more comments...TopLatestDiscussionsNo posts

Ready for more?
