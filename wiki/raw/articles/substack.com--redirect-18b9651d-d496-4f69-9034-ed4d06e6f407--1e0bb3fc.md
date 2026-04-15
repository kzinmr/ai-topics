---
title: "How much does distillation really matter for Chinese LLMs?"
url: "https://substack.com/redirect/18b9651d-d496-4f69-9034-ed4d06e6f407?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-15T18:21:43.443549+00:00
source_date: 2026-04-15
tags: [newsletter, auto-ingested]
---

# How much does distillation really matter for Chinese LLMs?

Source: https://substack.com/redirect/18b9651d-d496-4f69-9034-ed4d06e6f407?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Distillation has been one of the most frequent topics of discussion in the broader US-China and technological diffusion story for AI. Distillation is a term with many definitions — the colloquial one today is using a stronger AI model’s outputs to teach a weaker model. The word itself is derived from a more technical and specific definition of
knowledge distillation
(Hinton, Vinyals, & Dean 2015), which involves a specific way of learning to match the probability distribution of a teacher model.
The distillation of today is better described generally as synthetic data. You take outputs from a stronger model, usually via an API, and you train your model to predict those. The technical form of knowledge distillation is not actually possible from API models because they don’t expose the right information to the user.
Synthetic data is arguably the single most useful method that an AI researcher today uses to improve the models on a day to day basis. Yes, architecture is crucial, some data still needs exclusively human inputs, and new ideas like reinforcement learning with verifiable rewards at scale can transform the industry, but so much of the day to day life in improving models today is figuring out how to properly capture and scale up synthetic data.
To flesh out the point from the start of this piece, the argument has repeatedly been that the leading Chinese labs are using distillation for their models to steal  capabilities from the best American API-based counterparts. The most prominent case to date was surrounding the
release
of
DeepSeek
R1 — where
OpenAI accused DeepSeek of stealing their reasoning traces
by jailbreaking the API (they’re not exposed by default — for context, a reasoning trace is a colloquial word of art referring to the internal reasoning process, such as what open weight reasoning models expose to the user). Fear of distillation is also likely why Gemini quickly flipped from exposing the reasoning traces to users to hiding them. There was even very prominent, early
reasoning research that built on Gemini
!
This all leads us to today’s news, where
Anthropic named and directly accused a series of Chinese labs
for elaborate distillation campaigns on their Claude models. This is a complex issue. In this post we unpack a series of questions, beginning with the impact, and ending with politics. The core question is — how much of a performance benefit do Chinese labs get from distilling from American models.
To start, let’s review what Anthropic shared. From the
blog post
, emphasis mine:
We have identified industrial-scale campaigns by three AI laboratories—DeepSeek, Moonshot, and MiniMax—to illicitly extract Claude’s capabilities to improve their own models. These labs generated over 16 million exchanges with Claude through approximately 24,000 fraudulent accounts, in violation of our terms of service and regional access restrictions.
These labs used a technique called “distillation,” which involves training a less capable model on the outputs of a stronger one.
Distillation is a widely used and legitimate training method.
For example, frontier AI labs routinely distill their own models to create smaller, cheaper versions for their customers. But distillation can also be used for illicit purposes: competitors can use it to acquire powerful capabilities from other labs in a fraction of the time, and at a fraction of the cost, that it would take to develop them independently.
Much like the models themselves, the benefits of distillation are very jagged. For some capabilities, particularly if you don’t have a full training pipeline setup for it, quickly distilling some data from the leading frontier model in that area can yield massive performance boosts. This can definitely help the lab distilling from the API catch up much more quickly than they otherwise would. Most distillation is rather benign, using many tokens of an LLM to help process and refine existing data — putting a lot of compute into getting a few, high quality training tokens out. This sort of raw data processing work can be done on many different APIs, but one tends to be best.
When we go into what Anthropic says the three Chinese LLM builders actually used the Claude API for — as an aside, Anthropic didn’t confirm that the attack was done through the API, the chat app, or Claude Code — the actual impact of the operations is very mixed. It’s hard to know how much untracked usage these labs deployed for other projects (or other American models).
To start, Anthropic puts DeepSeek first in their blog post because they’re the household name in the US for Chinese AI. The extent of their use is actually quite small, showing how this post is more about the big picture than the details:
DeepSeek
Scale: Over 150,000 exchanges
The operation targeted:
Reasoning capabilities across diverse tasks
Rubric-based grading tasks that made Claude function as a reward model for reinforcement learning
Creating censorship-safe alternatives to policy sensitive queries
In the scale of training a language model, 150K samples is only scratching the surface as a substantive experiment. It looks like they were experimenting with some rubrics, which could’ve been for an online RL run, but that’s extremely unlikely with how distributed the access was, and then some minor stuff on completions for sensitive queries. This usage of Anthropic’s API will have a negligible impact on DeepSeek’s long-rumored V4 model (or whichever model the data here contributed to). This was also very likely a small team at DeepSeek and unknown to much of the broader training organization.
The other two labs, Moonshot AI (makers of the
Kimi
models) and MiniMax reflected much broader usage.
Moonshot AI
Scale: Over 3.4 million exchanges
The operation targeted:
MiniMax
Scale: Over 13 million exchanges
The operation targeted:
The role of distillation is constantly changing. Distilling from Claude today for its agentic behavior is much more valuable than versions of Claude have been as a teacher in the past. Claude Opus 4.6 has a well-rounded agentic navigation that none of the other models quite match. Why not try training on some of the model outputs to see if your model absorbs it? Over the next few months, that’ll be less differentiated. It’s sort of like how all the models are way better at math today than most people need — there are plenty of places to distill from.
Estimates will vary, but if each response had 10-25K tokens per exchange, the total tokens across these two labs, mostly with MiniMax, would be 150-400 billion tokens. This is a substantial amount, which could meaningfully improve a models’ post-training. For example, in Olmo 3 we had an SFT dataset of 20 billion tokens that could be built like this, and increasing it by 10X would be very reasonable.
These numbers are just scratching the surface of total synthetic data generation across APIs hosted by US companies. At the same time, quantity is a pretty crude way to measure impact. Just taking the outputs from Claude and figuring out how to add them to your model pipeline isn’t easy. The research community has seen many cases where taking outputs from a certain teacher model unexpectedly makes the student worse — subtle interactions between the data make it variable and tricky to do this type of distillation. It’s fundamentally a research problem.
This is what I’m sure the Chinese labs are innovating at. There’s an argument that Chinese frontier labs are substantially more efficient than their Western counterparts — this is misleading.
The labs operate under different constraints. The Chinese labs are likely slightly more efficient out of necessity in being lower on resources, but overall the picture of talent access is very similar. The Chinese labs also approach benchmarks differently, making it appear that they’re a bit closer than they really are (and
appearing as if they’re potentially surpassing
). This is needed to get momentum and brand recognition in the AI market.
The Chinese labs likely innovate greatly on distilling from leading API models, due to their restricted access to GPUs. GPUs could be used to construct synthetic data, but for organizations with more funding than they can spend on research compute (being supply limited), using API-based models is one of the few other options for effectively getting more compute. It’s way easier to figure out getting access to “banned” API models than it is to smuggle tens of thousands of physical GPUs and get them set up.
Share
It’s not only the Chinese labs that operate like this. Synthetic data from a model you don’t own is all arguably distillation. Distillation is a shortcut to more compute for anyone. It’s also a far less risky cost, as having a big cluster for research requires a very large financial commitment, where APIs are pay-as-you-go. For example, in
Olmo 3
we used millions of GPU hours on the
Frontier supercomputer
and Azure credits through
NAIRR
for synthetic data. We didn’t have the equivalent in GPUs (or really the cash, thank you research credits!).
All together, it’s very fair for Anthropic to be concerned about this. I still wouldn’t say it is a
crucial
factor in these Chinese labs post-training capabilities, especially not one that’ll be easy to measure in a time gap to matching the model they’re distilling from a la the US-China performance lag.
If we take a step back, there was even a time when Claude Sonnet was the flagship model ahead of Opus (I think this was with  Sonnet 3.5), much of this comes from it being
well distilled
internally from Opus checkpoints. Fast iteration and high-quality data can go very far, letting student models surpass the teacher. Frontier labs use this to their advantage, by having internal-only models for generating synthetic data, but saying that Chinese models could never pass the US frontier due to data distillation is like saying that Claude Sonnet could never beat Opus. It's unlikely, and it depends a lot on release times, but with AI models making dramatic progress, weirder things like this have already literally happened.
The biggest factor unaddressed here is how distillation from stronger teacher models is harder in an era when reinforcement learning at scale is needed to train the best models. You can spend compute carefully crafting and filtering prompts, but you still need to train the model yourself with substantial, on-policy inference — generation is the majority of the compute cost for RL and it can’t be generations from another model. For this reason, I expected this story to die down a bit. It’s clear from their
open
research
that
Chinese
labs
have excellent RL infrastructure, despite the compute shortages.
The reason I expected it to fade is that not being allowed to distill models for “competitive purposes” has violated the terms of service for API models for quite some time. Academics and open model builders in the US used to greatly worry about and debate this (and I’ve written about it multiple times in
2022
and
2023
). Only later in 2024 did that worry die down in the community (and no action has been taken against any smaller model builders).
This action from Anthropic represents another continued step ratcheting up the AI geopolitical tension. Kneecapping model distillation will be far harder than restricting the shipments of physical goods like GPUs. In many ways it seems like fully restricting distillation through distributed access methods seems almost impossible, and restricting GPU sales would be far more impactful.
Anthropic and the AI industry should choose their battles. When API endpoints are available for the best models, other entities will use that to train variants of said model. This is a natural evolution of AI models. If AI models are so precious that distillation is an extreme risk, then the models will be restricted to first-party products. Anthropic has a choice to do this with their latest models. The market for API-based model alternatives may be so competitive that some companies go this path — likely in part due to Chinese models undercutting on price — but an API is a fundamental offering that no leading lab will risk walking back from anytime soon.
