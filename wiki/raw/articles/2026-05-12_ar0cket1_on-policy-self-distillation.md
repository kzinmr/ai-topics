---
title: "On Policy Self Distillation — X Article"
source: https://x.com/i/article/2054081238236020736
author: ar0cket1 (@ar0cket1)
date: 2026-05-12
tags: [article, opsd, distillation, training, gepa, evolutionary-algorithms, rl, reasoning]
status: raw
---

**Author:** ar0cket1 (@ar0cket1)  
**Source:** https://x.com/i/article/2054081238236020736  
**Date:** 2026-05-12  
**Type:** X Article (auth-walled — content via bookmark metadata)

# On Policy Self Distillation

I've been working on solving OPSD for a week now (and a little more). The goal is RL like upper bound, with OPD like sample efficiency while being stable. This is the results I've gotten so far + general insight and analysis about OPSD. Feel free to build off this work to solve OPSD.

My experiments are done on Olmo 3 7B dense (student is the SFT checkpoint, teacher (OPD) is the RLed final model), for OPSD its just the SFT with/without hint conditioning. (all on math data from nemotron math v2)

## Why is solving OPSD so important?

The current ideal algorithm for Continual learning is RL and if an RL like algorithm can be applied with high sample efficiency, low cost and high stability, we would be one step further towards continual learning.

RL allows for new capability increases which has allowed for the large expansion of capabilities through late 2025 and 2026 and similarly if applied to continual learning, it would create very human like capability increase.

The issue with current RL is that doing it online is extremely impractical due to the low sample efficiency (would cost $10,000,000 for 155B tokens), and by the time any person or corporation would of made a substantial capability jump there would of been a heap of new more capable model releases.

OPSD has been shown to have similar sample efficiency to OPD which is roughly 10x more efficient than RL to train. So lets assume that someone has figured out how to have an unlimited upper bound (like RL) through OPSD with 10x sample efficiency of RL. Here is the math on why continual learning would be possible:

according to statistics on model input/output/cache (98% of tokens are input, 85% are cached, less than 1% are output), costs for Kimi K2.6 to generate 1mill output tokens is roughly $50 (since input/cache take up a lot of real usage). *this is higher for frontier models.
consider that you need a backwards pass (2x forward, the forward pass which is 1x and then some more noise + teacher forcing, so close to 3.5x cost of the output tokens which are roughly $4 per million output), that brings your cost for 1 million tokens of continual learning training to $65. Consider that you are 10 RL efficient so you have 10million tokens of RL equivalent training for $65.
^this is particularly noteable since doing this continual learning (the training stage and reward) is not much more expensive than raw inference: $50 vs $65. (so the backwards pass isn't too much of a cost jump)

now the effective (10x RL scaled) tokens of gradient updates you get (this considers all inference and training, so assume this is just your GPT 5.5/Opus inference with continual learning:

$100,000 -> 15.48B (negligible)
$1,000,000 -> 154.56B (alright, but not huge)
$10,000,000 -> 1.55T (meaningful)

You also have to consider that new better models come out every so often, so lets say model life span before becoming obsolete is 2 months, this means you gotta spend this much money in 2 months *and also have team members with this level of token usage.
So even this version continual learning is more ideal for large corporations that have huge engineering teams in which you can get significant token throughput and in a few weeks/months you get meaningful gradient updates.

TLDR: solving OPSD is one step towards viable continual learning

## OPSD Observations vs OPD

The following will be observations based on 10 problems, 4 student rollouts per problem with OPSD being averaged over 25 hint types that I hand wrote (so imo its quite informative as a general understanding of how OPSD works). *all this data is shown in the big table below

- **Mean KL** of OPSD and OPD don't really matter much and often can be made and regularly are quite close to each other.
- OPSD has significantly **higher max KL** with a max of 13.249 vs OPD's 3.736 (thus KL shocks)
- KL shocks are much more regular in OPSD compared to OPD (refer to KL mass >= 0.5/1/2, where you can see that OPD has a large concentration of its KL in outlier high KL places)
- **Positive Pressure token rate**: OPSD really likes downweighting the token chosen by the student (83% down weight), vs OPD really likes up weighting the token chosen by student (80% up weight). This is really stubborn, accross all 40 hand written hints i've tried this value doesnt really like to budge much (I can get small budges but nothing that comes close to OPD). This is one of my largest concerns about OPSD (though its important to consider that you don't need OPD like behavior to be viable, and maybe dropping KL shocks is enough, which I have figured out how to do in a somewhat general way).
- OPSD also likes to mess with **high confidence (low entropy)** tokens much more than OPD, which shows its instability and KL shocks.
- OPD generally rewards strong productive search, using productive invariants or rephrasing problems in a productive way. Thus its the perfect PRM (the only correct opinion). OPSD is quite the opposite (in fact in my analysis it almost touches basically the opposite tokens to what OPD touches). OPSD rewards moves the search towards the hint's suggestion, OPSD is also very active for the following tokens: problem, Let, First, Alternatively, Wait, equation, find. OPSD also concentrates around bringing back search that already happened and skipped over productive routes. It also rewards tokens that reintroduce answer constraints, variable conditions, or solution-validity checks, but this is quite corrective. So this part of OPSD is a bit concerning, since it acts quite differently to OPD but different can still work.

## Existing Ideas for Solving OPSD

Existing idea's for OPSD included conditioning on the final answer (which in my analysis is one of the worst things you can do, with huge KL shocks). Another approach was to use RL like direction and OPSD magnitudes (which in my experience also didn't create a very OPD like KL geometry). Largely everything that I have done with combining any verifyable rewards or token masking has struggled to create anything OPD like (dropping and stuff removes KL shocks quite consistently especially if you drop the first few tokens of the teacher force, but it doesnt close the non KL shock geometry of OPSD to OPD).

In fact I tried reversing the KL of OPSD and got an improvement and something more like OPD (better positive/negative, though it likely wouldnt work in practice), but it would be cool to try doing the opposite of what OPSD suggests. I tried this reversal thing also because I observed that the tokens getting KL changes in OPSD were almost the opposite in magnitude and the opposite tokens so reversing seemed like something fun to try.

@willccbb had a few ideas in his blog about dropping KL shocks as a way to solve OPSD (which I have achieved in a meaningful way through some evolution algorithms I'll get into later), but there is still a lot of uncertainty because OPSD is not like OPD even after you remove the KL shocks (though I suspect it wouldn't be to bad since existing literature finds it to work decently well even with existing shocks).

## My results so far (and approaches)

As you just saw, I didn't have great luck handwriting prompts so I tried an evolutionary algorithm (using GEPA right now, credits to will's blog for suggesting that, I was looking for a good prompt evolution algorithm before that and that answered my question). *the hint evolution is running as I write this so I'm not done yet

I tried optimizing a hint generation prompt (such that it can be used for all problems), and overall I had it running for 20+ hours on an RTX 6000 pro and didn't get huge gains. It seems that even with evolutionary algorithms its extremely difficult to make OPSD have better positive KL pull. I was able to minimise KL shocks though via this (to approximately 1/2 naive OPSD answer only hints, with 2x the mean KL (so much stronger with 1/2 the KL shock).

^ it is unclear if this improvement is useful for solving OPSD (though its likely a move towards an improvement on top of current literature).

I have also tried a more greedy optimisting approach where I've tried to do optimize the exact hint for a singular student teacher force to see if its possible to solve OPSD given infinite compute and hint optimization. My best result with almost 40 rounds of GEPA hint mutation is still similar to OPSD positive/negative geometry (it seems from this result that the current approach of OPSD is almost inherently going to have more negative than positive, different from OPD), but I am able to drop KL.

I have also tried per prompt hint optimization, by my calculations you can do per task a hint optimization GEPA of width 3, depth 8 if you amotorize your task 8 times within the training and doing that will have an approximate 2x cost of regular OPD (but considering the sample efficiency its still 4-5x more sample efficient than RL). However there wasnt major improvement by doing this, and I found that it is rather preferable to optimize a general hint generation prompt which outperforms this specific optimization even on the problem that the specific one was optimized on (phrased this weirdly but the hint generation prompt optimization that was optimized on a seperate dataset beat the GEPA specifically on a singular problem).

The results of this optimized hint generation prompt vs OPD are here (new 5 is a random new set of OOD problems I chose to evaluate on), single lane port and native generation SOTA are both strong contenders:

noteably: giving full solution as a hint is extremely unstable and it is possible to create much more stable variants that are closer to OPD's mean KL.

## will it be solved

it seems that from this analysis that trying to make OPSD like OPD isnt a good proxy for a viable algorithm and some gaps are seemingly inherent. it is almost necessary to test it directly during training to see if it is solved.

the most immediate thing to see is if the reduced KL shocks gives a big improvement in practical training since this KL analysis is quite limited in insight. Or if it is necessary to be even more like OPD to be successful.

*I am in need of some compute to run these full experimental training runs so any compute assistance would be great.

## credits

credits to will brown and wh for their articles :) (inspiration and insight, and I borrowed the banner idea from wh's article)

(https://x.com/willccbb/status/2050038277454143918?s=20) (https://x.com/nrehiew_/status/2053482349300797526?s=20)
