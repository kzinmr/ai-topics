---
title: "AI inference is obviously profitable"
url: "https://seangoedecke.com/ai-inference-is-obviously-profitable/"
fetched_at: 2026-06-27T07:01:07.570363+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# AI inference is obviously profitable

Source: https://seangoedecke.com/ai-inference-is-obviously-profitable/

Many people
claim
that AI inference is unprofitable to serve, and thus must be subsidized by an ocean of dumb money from investors who believe that some future AI model will come to dominate the world economy. When that dumb money goes away, so will AI products. According to this view, LLMs are just inherently too expensive (in terms of money, power, and water) to be used in consumer products. In fact, they can only be used today by externalizing the costs: money onto VC funds and now retail ETF
investors
, power onto electric utility
consumers
, and water onto the
communities
where datacenters are built.
There are
good reasons
to dislike AI, but this really isn’t one of them. In fact,
AI inference is obviously profitable
.
Doing the math demonstrates that inference is profitable
Frontier AI providers are reporting 70%-80%
gross
margins
on inference, but maybe we can’t trust them. Let’s do some very rough estimates on the actual cost.
A Nvidia A100 consumes 400W of power under full load. In practice, even a carefully-tuned inference server will not be at full load all the time, but it’s at least an upper bound. Suppose you’re running a dense 70B model
, which will
fit
comfortably (unquantized) on four A100s at around 2M tokens per hour. At industrial power prices, that’s about 13c/hr in the
USA
. Suppose (pessimistically) cooling is the same cost. That’s about 13 cents per million output tokens
.
Let’s amortize the cost of the GPUs, since that’s going to be the most expensive part. An A100 costs about $20k. If each A100 lasts around five years
, you’ll have to make 16k/yr in profit to recoup your capital investment (or $1.80 per hour). At lower utilization, it’ll take longer to recoup, but your GPUs will also last longer. Either way, your overall inference costs are at about one dollar per million tokens.
GPT-5.4-mini
charges
$4.50 per million tokens, and stronger OpenAI or
Anthropic
models are three to six times as expensive. It’s hard to make a direct comparison because we don’t know the size of OpenAI or Anthropic models, but the claimed 70% or 80% profit margin is extremely plausible.
Open LLMs demonstrate that inference is profitable
What if you don’t trust my estimates either? Let’s look at the pricing of open-weights Chinese LLMs. DeepSeek have
claimed
a bit over 80% profit margin on inference for DeepSeek-R1. Since their API pricing for R1 is less than half that of OpenAI or Anthropic
, that suggests that my estimates above for inference cost might be too expensive. Cooling at scale is probably
cheaper
than power, R1 only has half the active parameters of a dense 70B model, modern GPUs are more efficient than the A100, and there are significant
economies of scale
in inference.
Since DeepSeek’s models are available for anyone to download, they can’t get away with extracting a large profit margin. One of the other inference providers would undercut them with the same model. Inference costs for DeepSeek-V4-Pro on the market are around 87 cents per million output tokens, which is probably pretty close to the actual cost of serving the model.
For AI labs, inference must subsidize training
All of this doesn’t mean that
OpenAI
or
Anthropic
are profitable. Those companies are making huge capital
investments
that may or may not pan out, and are spending enormous amounts of money on talent and compute to train brand-new models and retain users.
They’re doing crazy things like offering per-month subscription models for nearly unlimited inference, which is almost certainly not profitable. If you used an API token instead of your Anthropic subscription in Claude Code, you’d pay ten times the cost. But that doesn’t mean API-based Claude Code couldn’t be a good deal. Some people are
already using
DeepSeek’s inference API for agentic coding, because once you take away the huge profit margin it’s cheaper than the relative per-month subscription.
Why won’t OpenAI or Anthropic lower their prices? Supposedly OpenAI has
thought about it
, but for an AI lab,
inference has to subsidize training costs
. A company like OpenAI has to fund the production of new models from the inference margins on existing models (at least partially). That’s why the margins on inference are so high: the AI labs are trying to squeeze out every dollar so they can stay alive in the training arms race.
However, inference only has to subsidize training costs
for an AI lab
. If you’re merely an inference provider, you don’t have to do any training at all. Therefore, even if OpenAI and Anthropic go out of business, whoever snaps up the rights to their frontier models will be able to continue selling Opus and GPT inference at a profit
. The AI bubble popping will not mean the end of the inference business, because
AI inference is obviously profitable
.
Here's a preview of a related post that shares tags with this one.
