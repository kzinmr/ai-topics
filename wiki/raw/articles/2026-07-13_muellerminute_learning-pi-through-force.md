---
title: "Learning `pi` through force"
author: Zach Mueller
source: https://muellerminute.substack.com/p/learning-pi-through-force
published: 2026-07-13
type: article
tags:
  - coding-agent
  - pi
  - open-weight
  - glm-5-2
  - kimi
  - deep-research
  - pipeline
  - harness-engineering
  - subagents
---

# Learning `pi` through force

With the release of Sol/Terra/Luna and the reactions of those in my trusted network, for the first time since Claude Code came out, I decided to give transferring to another harness another shot. And most importantly: using Open Weight models.

It's the situation where you've been using a tool for so long that you just decide to stick with it because old habits die hard, it gets the job done, and the friction is just below annoying enough to warrant a change, and it took too much time (to me) to actually do the change.

But, I had time this weekend (as my good friend was running a 50-mile ultra) that I decided to sit down, deploy some models, and finally give Pi another shot.

This still doesn't answer **why pi,** however.

I wanted a minimal harness where I could really dig into what was going on under the hood, remove bloat from my prompts, and have the most minimal set of variables possible when attempting this conversion, since any MCP/tool call/prompt in Claude Code can be 40k+ characters if you're not careful (this is from my own data/skills).

So the goal: **by the end of the weekend, I want to convert my Claude Code workflow for deep research on model releases from Claude Code to pi with as minimal loss in quality as possible**.

This is where we go from "run this at home" to… pick your favorite cloud provider? For work, I make use of an 8xB200 node to do most of my work, and as a result, it made sense to play around with the NVFP4 NVIDIA releases of the current best SOTA models. This means:

*   **Driver/orchestrator:** GLM-5.2-NVFP4

*   **Subagent:** Kimi K2.7 Code

I'll make a small side note here: I was hoping to add in a local DeepSeek v4-Flash as an executor, but I didn't end up getting that to work.

I wrote a nice piece on [why GLM-5.2 is the start of a new era](https://lambda.ai/blog/glm-5.2-a-new-rise-to-open-weight-agentic-models), and to be true to my word, I wanted to keep my pipeline based around that model.

Along with this, I set up a few different Pi plugins, based on my own biased interest and how I wanted to port this pipeline over:

*   pi-subagents : Helps you create roles for subagents and respective model definitions. More on this later

*   pi-mcp-adapter: Not used for this, but eventually for me to interact with… well… lots of MCPs'

*   pi-lens: This one was installed on a whim, but the overall idea is to give agents language-aware info as they're writing over specific files.

Now that we have some background, let's get into what the pipeline _actually_ is. For the last few months (arguably half a year, I think), I've had a custom Claude Code pipeline that will go dig into a Hugging Face model release for me and report back a "Model Memo." The basic idea is:

*   Model releases, go grab as much information as you can on it.

*   Operate on a **tiered system for sources.**

    *   Tier 1: Hugging Face, official company blogs, papers

    *   Tier 2: Inference providers, tweets, documentation (think `vLLM`/`sgl`)

    *   Tier 3: Everyone else

*   There must be multiple T2 corroboration of a fact for it to be considered a T1 fact; T3 follows a similar vein.

*   This is used to minimize hallucinations and biased "hype"

*   Research report then chases down references in the T1 and T2 sources (adding an additional 20-30 articles) to verify/expound its own background knowledge and make sure the concept is relevant to the model that we're talking about

*   After this is done, generate a "Model Memo" which includes an executive summary, the meat of critical information (what changed, what didn't, benchmarks, etc), and a complete list of citations (with references **throughout the document**) to follow up with those who have a zero-hallucination policy.

But Zach, why not ChatGPT Deep Research?

It's hard to describe, but essentially, I don't enjoy the "taste" of those deep research reports. Nothing is wrong with them; taste is just a very personal preference situation, plus I wanted to have my own custom verification system for source citing.

This has worked exceptionally well, and it's allowed me to generate 15-20 page reports that I can read through to understand everything about underlying architectures, motivations, and areas to go further read and look at should it fancy me.

As you can imagine, it's quite an interesting task to try to toss at an Open Weight model.

The first step was prompting Fable to convert my existing skills into something Pi could use. This ended up looking like the following:

*   fetch-model: Skill to fetch a HF model card/config.json

*   fetch-arxiv: Skill to fetch an arxiv paper

*   deep-research: The multi-source research engine described earlier

*   hf-model-researcher: Orchestrator part of the pipeline (or part A if deep-research is part B)

*   Defined subagents:

    *   `hf-retriever`: Kimi, which performs parallel fetching on resources & summarizes

    *   `prose`: GLM, which helps with drafting the overall verbiage and also calls SlopGuard iteratively as it's going.

Essentially, the pipeline fetches all the data, the retriever creates briefs of everything, and a research_notes. An MD file is created which has all the information, prose creates the first draft, numeric-verifier, plus completeness critics, validators, before final delivery.

It does _not_ save on speed. On average, the Claude pipeline resolved in ~20 minutes or so; this one is 30-40 minutes. If I swapped certain areas for faster models (e.g., validation, scraping, etc., could come from a much smaller model), I could likely close this gap, but this isn't a pipeline where it needs to be as fast as possible. Usually, I'm already writing my model card as this is going on, and then I fill out the background/learn from what is in my report afterwards to update things.

[I've open-sourced all of the pipeline scripts, skills, and more here for you to dig into, since it's a hair too much to put into here.](https://github.com/muellerzr/learning-pi-through-force)

To have a systematic loop of self-improvement, we need to define a reward structure. For this problem, I set a fully generated Claude Code reference report as the "gold standard" that Pi would need to beat. I had Fable and Sol (both on xhigh) judge the content on completeness, hallucinations, and which overall each model "preferred." (I'm aware that this metric by itself can lead to a reward which does not match my own expectations, so outputs were monitored closely. What I found is that both Sol and Fable's feedback roughly mimicked my own preferences and suggestions out of the box.)

The rough reward scale was:

1.   Human preference (done at the end)

2.   **Slop Guard** must have a score of >70

3.   All numbers must be numerically accurate.

4.   The report shouldn't miss important findings from the new model.

Hypothesis here being that it should only take 3-4 loops of going through this with prompt iteration (from GLM 5.2) until a better result is found, before running it again on a few model memos to make sure it generalizes well.

Every experiment needs a baseline. Essentially, I opened Fable and went "In this folder is the information and skills for your deep research and model researcher skills. Port what you need over into pi to make it work. Use as minimal prose as necessary, but still enough to get the directive across."

This was essentially a test to learn how skills get made with Pi, how to set up the subagent calling properly, and make sure that I didn't need to do anything overly complex, and that OOTB wasn't perfect as it was.

After reading it, while factually it was great (Fable itself mentioned that it hit most of the critical areas in the report, just hallucinated a citation or two and got one number wrong), its prose read very… "this is an llm"

> **NVIDIA Nemotron-3-Ultra-550B-A55B** is the flagship of NVIDIA's open **Nemotron 3** family: a **550 billion total / 55 billion active** parameter **Mixture-of-Experts (MoE)** language model built on a **hybrid Mamba-2 + Transformer-attention** backbone, trained with a **4-bit (NVFP4) quantization-aware** recipe, and extended to a **1 million-token** context. It is a reasoning-and-agentic model: by default it first emits a reasoning trace, then a final answer, with the reasoning toggle (enable_thinking) configurable per request and a calibrated "medium-effort" mode that trades ~7% accuracy for ~2.5× fewer tokens.

The content itself isn't the problem, but the best way I can describe it is that my eyes glaze over when reading this paragraph. Absolutely not useful for something one would want to learn from, really.

What came out of this experiment was creating a prose subagent and a style prompt, which will help with keeping the prose… sane.

It took a bit of work, as out-of-the-box, each subagent in pi-subagents needs to be allowed specific tools to use, which ended up being read/write/edit/bash. It's long, yes. I probably could've optimized the prompt down quite a bit, but overall it seems to have worked fine.

From here, it essentially became a loop of generate a report, compare against the last one and our baseline, and see what feedback Fable and Sol had. Importantly, **GLM was always the one tweaking the prompt. Not Fable or Sol**. You can't have a self-healing based system if the healing comes from the model not driving things. (This is also how one goes exponential with slop, but I iterated manually each time and didn't just set a /goal to optimize for this reason).

Essentially what was found at first was because of the earlier pipeline and going from fetching to a brief to research notes to a draft, I wasn't keeping the articles themselves stored on disk and there was only a summary of each, leading to lossy information. Easy fix, just store all of the data on disk that we grab. Mix in numerical verifications, citation integrity, and some formatting adjustments and I ended up at a place where while it was slightly more verbose than the Claude Code pipeline (36 pages vs 21), it was more information dense, had prose I preferred, and also cost pennies compared to the price of using the Claude API.

I was pleasantly surprised to find that I could finally take some of my work pipelines and toss them to local models and end up preferring the prose, information it found, and more.

Was it "out-of-the-box?" Absolutely not. But no code migration ever is. And for something that I've been running for months on-end sacrificing a day or two on a weekend to convert it over was a great way to learn how a different harness works. Most importantly, **because I controlled the harness, I could tweak everything exactly to my liking**. Context bloat. Custom tool usage. Everything was available to me in the most minimal interface possible, which matters when the model only has 256k context to work off of.

I'll keep slowly migrating more of my pipelines off of the paid services from here, and leaving those stronger models (Sol, Luna, etc) for tougher work problems where it makes sense to challenge them more (e.g., autoresearch).

In the meantime, [here is a link to the Github containing my pi skills and plugins I used](https://github.com/muellerzr/learning-pi-through-force), and the various model memos you can read through to get an understanding of the various iterations.
