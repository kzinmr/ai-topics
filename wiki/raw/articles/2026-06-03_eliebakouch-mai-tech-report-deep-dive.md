---
title: "Elie Bakouch Deep Dive: Microsoft MAI Tech Report Analysis"
author: "Elie Bakouch (@eliebakouch)"
date: 2026-06-03
source_url: https://x.com/eliebakouch/status/2061965825037254947
type: x-thread
tags: [microsoft, mai, model-training, moe, reinforcement-learning, scaling-laws, pre-training, post-training, grpo]
---

# Elie Bakouch Deep Dive: Microsoft MAI Tech Report Analysis

**Source**: [X megathread](https://x.com/eliebakouch/status/2061965825037254947) by Elie Bakouch (@eliebakouch), LLM trainer at PrimeIntellect (prev. HuggingFace)
**Date**: 2026-06-03
**Engagement**: 1,516 likes, 1,104 bookmarks, 139K impressions

## Thread Content

**[1]** microsoft MAI tech report is a gold mine, one of the most transparent for a model at this scale.

this model uses zero synthetic data or distillation from previous models. this means reasoning, agentic behavior, tool use are all learned fully during post-training with no cold start. bold choice that makes it harder and requires more iterations to reach sota, but you get FULL control over your model series and it proves they are serious about being a frontier lab.

the tech report is insanely detailed and precise about numbers. to give an example, they give the exact MFU across all the iterations of the model, with the exact changes etc. they also share the full scaling ladder recipe, to my knowledge this is the first time i've seen this in a tech report at this scale

let's look at all of this in this likely very long thread 🧵

**[2]** some overview about the model shape. it's a 1T model with 35B active, trained on 33.5T tokens (30T pre-training, 3.55T mid-training).

main choices are:
&gt; interleaved dense/MoE layers
&gt; local/global sliding window attention
&gt; LatentMoE

let's go through each part https://t.co/8oymXpOyAE

**[3]** about attention, they don't mention using any form of sink or gate for SWA but otherwise fairly standard:

&gt; small window size (512)
&gt; NoPE on global layers
&gt; QK Norm
&gt; no q head expansion for swa layers
&gt; 5:1 ratio is a bit more conservative than Mimo V2.5 Pro (7:1) https://t.co/5m5rFpIapD

**[4]** very important change, they alternate dense and MoE layers. last model to have done this was Llama 4, with the same expert sparsity (top-k / total expert) BUT with a big shared expert.

they found that if you interleave dense:MoE, you rely less on shared expert (and hence remove it) and this interleaving scheme leads to better efficiency.

they start with a dense layer for stability like previous reports found

(second pic is from llama 4 blog)

**[5]** here is how MAI sparsity compares to other recent models

parameter sparsity: total / active params
expert sparsity: total nb of experts / routed

effective sparsity for experts takes into account the dense:MoE interleaving https://t.co/eVy3ATe2gU

**[6]** they use LatentMoE from nvidia to compress the dimension of the expert, routing decision is based on the original representation https://t.co/cjRi6xBO9v

**[7]** they use global load balancing, meaning you compute the metrics to do the load balancing at the GLOBAL batch level. this helps a lot since microbatches might not be diverse enough, and this can hurt expert specialization.

this is from a Qwen paper that i cite all the time aha, here is the main plot
https://t.co/bFU2Gf5oTT

**[8]** they use loss-based load balancing (this is also what Qwen uses) and say that the optimal load balancing varies with the expert capacity.

expert capacity is the "max amount of tokens that an expert can process", this only makes sense with token dropping methods (if the model has too many tokens routed, you just drop them). but they end up using a dropless implementation (which is standard afaik?)

**[9]** my favorite part: the scaling ladder 😍

the only knob they change is model depth (number of layers), everything else is derived from it with heuristics https://t.co/Pqbvml5smp

**[10]** (while i'm writing this, let's play a game, guess how many tweets this thread is going to be lol)

**[11]** the only knob they change is model depth (number of layers), everything is derived from it with heuristics.

first heuristic:

hidden size = L * 256/3

this is derived from recent models, here is how it compares to others.

other parameters:
- fixed expert sparsity (unless ablated)
- FFN expansion is 2x, latentMoE hyperparameters are 2x compression -> 3x expansion (see the plot on latentMoE to understand what this means)

**[12]** for tokens per parameter (TPP), they mention it varies by ablation. ablations run at 100/200 TPP which is around "chinchilla optimal". chinchilla for dense is ~20 TPP, so a ~5-10x factor from their MoE setup? interesting https://t.co/pvhMpMFJSI

**[13]** arch ablations run at 100/200 TPP*

**[14]** the rule to promote a new architecture is based on this scaling ladder. they have this Efficiency Gain (EG) metric which basically quantifies "to reach the loss our candidate got, how much more compute would the baseline have needed?"

"compute" here can mean flops or time, but as we'll see later, the pipeline is often optimized for flops first, then optimized for time.

the marin folks have a quite similar setup!

**[15]** the "loss" definition is VERY important, the scaling ladder heavily relies on this. it's a NLL private set (negative log likelihood) with:

50% code
17.5% STEM
17.5% Math
10% General knowledge
5% Multilingual

they then use this target NLL and normalize it with an in-house model. normalization matters because raw NLL scales differ across benchmarks

**[16]** they found a ton of public leakage in pre-training data, and hence why they don't trust public benchmarks for measuring improvement. NLL-based evaluations are also much faster and don't rely on capacity like multi-choice formats that are easily benchmaxable.

actually imo the only issue here is that this doesn't really transfer to post-training capacity, there might be a way to adapt it tho by doing NLL on reasoning traces?

**[17]** the pre-training data part is amazing, and has a lot of olmo vibes to it (hi @soldni @kylelostat @HannaHajishirzi and co <3)

they put a lot of care into extraction and dedup (we will see a very good example of why dedup matters)

the data comes from both common crawl (very nice of them to say this) and private sources

no synthetic data (intentionally), and they have targeted sub-pipelines for different domains

**[18]** the full pipeline is EXTREMELY detailed in appendix A, with very precise numbers, this is amazing https://t.co/o5rqlKetkz

**[19]** and here is all the "tools" that they use https://t.co/4OljIZCjXJ

**[20]** one VERY BIG question when you have sourced the data is how to mix them. and this heavily depends on the metric you choose to optimize. the issue here is that optimizing the mixture for one domain means that you automatically lose on another one in most cases, it's illustrated nicely here with this nice html/code val loss plot

**[21]** one very cool thing i forgot here is that the different domains don't react the same to things like architecture changes, here you can see that increasing sparsity helps code a lot but much less other domains which is a super interesting finding imo https://t.co/ByhMt8ujgv

**[22]** there are some solutions here with automatic mixing (which is basically an optimization problem). idea is to have small scale proxies to predict larger scale optimal mixture.

and they found that this actually doesn't transfer at scale, here is the example they cite with a "stem heavy mix" vs "code heavy mix"

btw this is a 20T token ablation on a ~615B total param model which is almost the same compute as the final model training :)))))

**[23]** and they even trace back to the fact that part of the STEM content was less deduped than others, which scales badly as flops increase.

this is actually the big point about dedup being so important here, it basically increases the number of effective epochs without you really knowing

**[24]** data ablation setup

for data quality, they either upweight a single source by 50% and train from scratch to see marginal utility, or ablate within the full mixture on the scaling ladder with epoch-matched downsampling and forecast to target scale via EG. for mid-training they do single-source microanneals (LR decay from an intermediate checkpoint) to locally tune weights.

for data mixing, they do (1) thousands of small models on sampled mixtures to forecast optimal mix (2) hierarchical search, local within category + global between categories with an 8 epoch cap (3) verify by training finalists at ~2.8x compute and checking the optimum is scale-stable. the scaling ladder discipline is applied throughout, not just tacked on at the end

**[25]** and they even trace back to the fact that part of the STEM content was less deduped than others, which scales badly as flops increase.

this is actually the big point about dedup being so important here, it basically increases the number of effective epochs without you really knowing

**[26]** on STEM mid-training data they use the same taxonomy as essential web from @essential_ai, code is filtered with repo level quality metrics

https://t.co/mPKrp9wQfG https://t.co/2vmBBp8mHH

**[27]** about long context, they basically use the same mixture as 32k with proper packing, which makes sense because they don't have long agentic rollouts yet but also previous ai2 paper found that long context data didn't matter that much surprisingly during this phase https://t.co/1S50x4Msxt

**[28]** the training loss is beautiful, no spike at all, the dream of every people pre-training model aha https://t.co/OfCiyHFSRx

**[29]** pre-training learning recipe:

> AdamW with slightly different betas (usually we see 0.9, 0.95)
> weight decay of 0.1, but 0.01 on attention and 0.005 on embedding (funny that they just didn't remove it for embedding)
> learning rate decay to 10% with cosine schedule, they found that decaying to a lower value hurts post RL results (quite novel!)
> DROPOUT IS BACK (with a quite high value of 0.15!!!) they add this before residual
> they do a simple N(0,0.02) init (deepseek/kimi models use N(0,0.006)) except on pre residual proj where they scale down by the number of residual connections
> global batch of 134M (quite high as well but that make sense)

last point is from GPT-2 paper and i think it's one of the first times i've seen this again!!

**[30]** training sequence length is 16k which is quite high, they use EP=64 with zero2, and zero3 during long context extension (which is only 150B btw)

they do one schedule per phase iiuc and don't rewarm the lr between them https://t.co/SaVun2fEvp

**[31]** some cool results on RMSNorm init impacting the contribution of attention at init (when random) and hence leading to small instabilities in the load balancing https://t.co/8hAQrtRYXz

**[32]** here is the full precision scheme https://t.co/pGowaahD12

**[33]** here is open base model evaluated on their NLL bench 

i also understand better this post by @NandoDF aha https://t.co/ZFybHo9HIY https://t.co/kqoeYX5ygv

**[34]** overview of all the system optimization they do https://t.co/RD1alPIJhl

**[35]** tons of content on MFU optimization between different versions

the MFU value (if BF16?) is relatively low around 20% tho 😮

claude summarized it better than i could so here you go https://t.co/2FZbtCWfOy

**[36]** also just realized while going through the paper again to see if i missed smth but kinda crazy that they use tied weight embedding at this scale, not sure i understand this choice https://t.co/TkZVPJHb9W

**[37]** the model/performance co design part is interesting but they doesn't seem to consider inference much here?

**[38]** Less knowledgable about RL but will dump some info in a "less structured" way (as if it was structured before lol)

first, no synthetic data so no cold start phase, which is a very very important info to keep in mind https://t.co/6eX3WPkS0C

**[39]** main differences in GRPO are:
&gt; length penalty
&gt; entropy-based outer clip
&gt; no KL term (makes sense here since the model is not cold started)
&gt; normalization is global instead of per response https://t.co/0W467D1pqY

**[40]** length penalty is very elegant and simple tbh https://t.co/LcPkkAzhQV

**[41]** the entropy based clipping is pretty cool, it keeps the model's entropy around 0.3 which seems to be their sweet spot, but we add a pretty crucial HP here imo https://t.co/eUnEMXyJp2

**[42]** wrong text: "here is the final mixture, 50%+ code is quite high but that makes sense. also you can see that some mix percentages look relatively close to the target loss: 55% code final mix -> 50% weight in target loss, 15% for stem -> 17.5% target loss. not the case for math tho

mid-training mixture increases stem and math to 35%"

**[43]** @TL343 no thanks a lot for the catch https://t.co/E0MHkTaB49

**[44]** they do difficulty filtering with a two stage pass rate https://t.co/0fEc1ts7q8

**[45]** also some top p masking like in deepseek, not familiar with this so don't have much to add but doesn't seem super standard? https://t.co/24xjUmk55O

**[46]** they do some rounds of RL -&gt; self distillation SFT to recover -&gt; RL iiuc, they claim this might be because of train/inference mismatch and do it less often when they fix it and use bf16 https://t.co/5oi8PooRML

**[47]** some of the best practices that they found. points 3/4 are very interesting imo and might be interesting for mid-training as well

see https://t.co/wtMrduNAuH https://t.co/8kwR3xant7

**[48]** also not sure why they don't do OPD instead of SFT in the consolidation phase https://t.co/ZRZHdGYSXN

**[49]** a lot more on data curation/creation to bootstrap good reasoning without prior model https://t.co/1qM0uMDQ0r

**[50]** microsoft uses SGlang wow https://t.co/CflgYIQU6B

**[51]** good infra numbers about the final training run, love the transparency here https://t.co/Bj3SV8Qcle

**[52]** will conclude by this, 40% higher throughput per Watt (or is it different from "rack power budget"?) is pretty impressive and bullish on microsoft chips https://t.co/SkbINHlLAH

**[53]** this was an insanely good read, i think this is the most detailed report i've read at this scale in some aspects. i really hope MAI continues releasing those tech reports, thanks a lot to the team for this gift 🥹
https://t.co/BOvdLdgu8R

**[54]** @pingToven it was a mistake, took way too much time ahahah

**[55]** @stochasticchasm @pingToven i think it took me ~4 😭

**[56]** and if you're done with this thread and still want to read more about this report, pease take a look at the goat @stochasticchasm recap https://t.co/SjUlb7PpUy

**[57]** done @MicrosoftAI, only 47 tweet sorry :(

https://t.co/njuml0VoB0

