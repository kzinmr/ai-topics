---
title: "DeepSeek's 10 trillion USD grand strategy"
source: https://x.com/bookwormengr/status/2057909493250539891
author: "@bookwormengr"
date: 2026-05-22
type: x_article
topics: [deepseek, ai-hardware, kv-cache, moe, chinese-ai-ecosystem, business-strategy, mla, dsa, engram]
---

Have you ever wondered, how DeepSeek may make money, and lot of it? 
They didn't come up with competitive coding plans like GLM, MoonShot and MiniMax. They don't have multimodal, audio, video models. Till date they don't have a harness (they have begun hiring recently for building a harness)? DeepSeek is also committed to open source in the long term and is too happy to share their secret sauce. Is this madness? Is this sheer waste of money? Are investors who are about to invest 10B USD in them throwing money into a drain?

No - quite the contrary, imho!!! 

Here I present observations about what they have done till date, and a strategy they seem to be following. Liang Wenfeng's (DeepSeek CEO) eyes seem to be on much bigger prize and they could achieve 1T USD valuation, while helping create a 10T USD industry!

## Revisiting DeepSeek's Hero's Journey

DeepSeek has always gone against the wind of building incrementally better models and trying to sell immediate applications - e.g. coding plans. I wrote this viral tweet on 27th Jan 2025 about what I saw as DeepSeek's Hero's Journey. The story is getting only more interesting.

When people were trying building dense models, DeepSeek went after Mixture of Expert models (MoE) that were hard to train.
They worked from 'first principal' approach and invented new algorithm GRPO to replace dominant PPO algorithm for Reinforcement Learning (RL) that was more expensive to implement.
They figured out Reinforcement Learning from Verified Rewards (RLVR) as a key strategy to improve reasoning ability of models.
They came up with a simple strategy for Speculative Decoding through "Multi Token Prediction" that also densified the training signal.
They perfected "ZERO bubble" pipelines to improve use of limited GPU resources.
They published Expert Load balancer to make it easy for everyone deploy Mixture of Expert models. Particularly with "Wide Expert Parallel" strategy models can be served much more economically as one can have large batches.
They invented MLA, DSA, CSA, HCA to reduce KV Cache need and keep computation demand against growing context near constant.
They invented Engram to trade memory for compute.
They invented mHC to achieve stable training as model size grows. And the list continues....

In Hero's Journey story structure (the most universal), hero never decides what his journey is going to be. He learns along the way and figures out a great mission for himself and completes it against all the odds. He meets many detractors, but he ignores them. He meets many bad faith actors. He has great flaw or shortcoming - but he overcomes them to accomplish his mission. He confronts challenges that seem unsurmountable, but figures out how to make alliances and how to use precious resources wisely. This is what gets the audience to root for the hero. This is what earns DeepSeek their fan following and global respect and also detractors.

As I will show you in detail, DeepSeek is on this journey for long enough now and have discovered the ultimate destiny: it is not selling coding plans, but to enable a 10T USD Chinese AI hardware ecosystem and achieve 1T USD valuation for itself. In doing so they will enable many new entrants in the western hardware ecosystem as well.

## KV Cache Calculations

Let us do some fun KV cache math first. I compute for 1M context. I assume 8 bit KV precision and 16 bit indexer precision.

For 1M context:
- DeepSeek V4 needs only **5.48GB HBM**
- GLM5 needs **60GB HBM**
- Qwen3-235B-A22B needs whopping **89GB**

Mind you:
- DeepSeek is 1.6T parameter model
- GLM5 is around 700B parameter, it already uses DeepSeek's MLA and DSA; though not latest compressed attention
- Qwen3-235B-A22B is around 235B and uses GQA attention

This small size of KV cache - without compromising on quality - is the reason they can offer long held cache at such a ridiculously low price - less than 3% price of Cache hits for Sonnet 4.6 - and they hold it for multiple hours. Small amount of cache for long horizon task enables offloading to SSDs and reloading very cost effective. This reduces requirement of HBM that is in short supply and hardest to make memory from Chinese AI hardware industry perspective.

## Method Behind the Madness

### NAND & SSD Beneficiary
Who supplies SSD in large quantity? YMCT is emerging as 3D NAND giant. NAND allows DeepSeek to avoid re-computation of KVs. In turn, DeepSeek creates a large market for NAND & SSD - not just of YMTC's but everyone else's as well.

### LPDDR Memory
LPDDR memory has great potential to be a place where you hold weights and stream them into HBM as needed, reducing the pressure on HBM demand. SGLang team has published great blog about it.

While DeepSeek did not do anything specifically for this - their MoE architecture with large number of experts and 4 bit weights make it easy to implement this scheme.

This innovation combined with super compact KV Cache (lossless) reduce HBM demand significantly.

Who in China makes LPDDR? CXMT. They are only 0.5 Gen behind on speed for LPDDR and 1 generation behind on density. Not very far!

### Engram: Trading Memory for Compute
LPDDR supports holding large amount of "Engram". In their Engram paper DeepSeek showed that while MoE scales capacity via conditional computation, Transformers lack a native primitive for knowledge lookup. They're forced to inefficiently simulate retrieval through computation. They introduce Engram, a module that modernizes classic N-gram embedding into an O(1) hash-based lookup, creating a complementary sparsity axis they call conditional memory. This saves computation, but needs memory to host the embeddings table which can be large in size. It is a classic memory-compute substitution, but with the insight that the "memory" side is dramatically cheaper per bit retrieved (a LPDDR lookup vs. a full forward pass through transformer layers), making it a very favorable trade at scale.

## DeepSeek's Long Game

From all these innovations, DeepSeek's game doesn't seem to be immediate profits of few hundred millions given all the choices they have made (no multimodality yet, no voice models, video - what is that?) - but they are playing a patient 10T USD game to enable alternative hardware ecosystem.

It is not only about making Chinese memory players key players on Chinese and global AI hardware arena, but also reducing the resource demand itself, to be able to train and serve AI models cost effectively - this will enable many GPU/ASIC makers as well as networking chip makers as they will become viable options. All these innovations will also help Western open source ecosystem as well as new hardware makers.

## DeepSeek's Innovations Summary

### 1. Mixture of Expert (MoE) and MLA (DeepSeek V2, May 2024)
MoE made it possible to train very intelligent models at 40-50% less compute. MLA made it possible to reduce KV cache by 90%. This made offloading KV cache to SSD quite efficient. It later unlocked training DeepSeek V3 which was near closed source at the time with only 2048 H800 nerfed GPUs.

### 2. DSA (DeepSeek V3.2 Exp)
DSA reduces compute for long context scenarios and also relieves pressure on HBM bandwidth. It ensures computation doesn't grow with growing context — processing time for DeepSeek-v3.2 stays flat with context.

### 3. mHC (Dec 2025)
mHC: Manifold-Constrained Hyper-Connections is a macro-architecture innovation that reinvents how information flows between transformer layers. Instead of the standard residual connection (x + F(x)) used since ResNet, mHC expands the residual stream into multiple parallel information highways and allows learned mixing between them — but crucially constrains the mixing matrices to be doubly stochastic (via Sinkhorn-Knopp projection onto the Birkhoff polytope), which mathematically guarantees that signal magnitude is preserved across arbitrary depth.

This solves the catastrophic instability that plagued unconstrained Hyper-Connections (initially invented at ByteDance), where signal amplification exploded to 3000× at 27B scale, collapsing training entirely.

The compute cost is minimal: mHC adds only 6.7% wall-clock training overhead since it doesn't change the FLOPs of attention or FFN layers, only how their outputs are routed between layers.

Performance gains at 27B parameters: +7.2 points on BIG-Bench Hard reasoning, +3.2 on DROP, +2.8 on GSM8K math, and +1.4 on MMLU general knowledge.

### 4. CSA, HSA (DeepSeek V4, April 2026)
Reduce KV need by another 90% by compressing KV tokens and reduces FLOPs needed by large margin relieving pressure on both HBM and GPU/ASIC.

### 5. Engram (Q1 2026)
Trade memory (LPDDR memory) for compute.

### 6. Compute and Communication Overlap
Extreme focus on Compute and Communication overlap, and innovations like Dual Path. DeepSeek goes further to advise hardware vendors on their ASIC design to make sure they don't waste precious silicon resources.

### 7. TileLang
Investment in TileLang points in the consistent direction that they are not just dealing with their own compute crunch but making Chinese hardware ecosystem competitive with western ecosystem. With Tilelang it is possible to develop kernel once and have it run successfully on multiple hardware platforms. This also unlocks more western hardware like AMD.

Note: many AI platforms in China either provide CUDA compatibility or CUDA translation layer: Moore Threads, MetaX, Biren, and Iluvatar CoreX are the most CUDA-compatible Chinese chips via translation layers. They do not need TileLang (in theory).

## Large Scale RL and RSI

With access to more compute (due to more potential hardware options) and reduction in compute demand, DeepSeek can take on much more ambitious training projects; particularly RL post training. RL involves generating large number of trajectories - generating trillions of tokens. It can get expensive real fast. Furthermore to train 1M context models, you need to generate trajectories that long. Training models for such long trajectories enables long horizon tasks.

Furthermore, availability of more hardware at DeepSeek due to increased options will enable automated research (RSI). RSI involves AI itself designing and carrying out experiments. The approach has large number of trials and errors and can get costly very quickly. However, RSI is important to explore the entire design space. DeepSeek will need to be RSI capable before they hit AGI followed by ASI.

## What DeepSeek Does Today, Rest of the Industry Does Tomorrow

DeepSeek's innovations around Mixture of Expert, MLA, DSA have been picked up by rest of the AI labs from around the world and from China.

For example, ZAI - makers of GLM family of models - use MLA and DSA. Kimi (Moonshot) has adopted MLA and have no hesitation in saying their architecture is based on DeepSeek's architecture. In return DeepSeek uses Muon optimiser that was first used by Kimi (Moonshot) for large scale training.

NOTE:
- MoE was invented at Google in 2017 with Noam Shazeer as the key author. DeepSeek applied it at massive scale and invented their own tricks.
- The Muon (MomentUm Orthogonalized by Newton-Schulz) optimizer was created by machine learning researcher Keller Jordan in late 2024. Kimi (Moonshot) team were the first one to use it at massive scale.

## What About Making $$$?

OpenAI received warrant/options to buy stocks of AMD and Cerebras at a low price, based on consumption milestones. It is a great deal for AMD and Cerebras. OpenAI being committed to them, makes they likely to succeed in the long run.

Quote from AMD announcement: "As part of the agreement, to further align strategic interests, AMD has issued OpenAI a warrant for up to 160 million shares of AMD common stock, structured to vest as specific milestones are achieved. The first tranche vests with the initial 1 gigawatt deployment, with additional tranches vesting as purchases scale up to 6 gigawatts. Vesting is further tied to AMD achieving certain share-price targets and to OpenAI achieving the technical and commercial milestones required to enable AMD deployments at scale."

I forecast DeepSeek to enter in such agreements with multiple Chinese memory, ASIC, CPU and networking stack makers and work closely with them to make their hardware stacks viable for leading AI workloads.

Given combined valuation of all Western (including East Asian allies) AI stocks far exceeds 10T USD. This collaboration-that-awards-equity approach allows DeepSeek to help create equally big industry in China and claim their piece of the pie while achieving 1T USD valuation for themselves.

This will allow them to make far more $$$ while also achieving their goal in their words of "AGI for everyone". Liang Wenfeng - a big fan of Jim Simons - is too smart a capitalist to miss this!

This is the only thing that makes sense, if you look at everything DeepSeek have done so far...

## Sources Referenced in Article

- [KV Cache Calculator](https://kvcache.ai/tools/kv-cache-calculator/)
- [DeepSeek V2 Paper (arXiv:2405.04434)](https://arxiv.org/pdf/2405.04434)
- [DeepSeek V3.2 Paper (arXiv:2512.24880)](https://arxiv.org/pdf/2512.24880)
- [DeepSeek V3 Paper (arXiv:2512.02556)](https://arxiv.org/pdf/2512.02556)
- [MoE Paper (arXiv:1701.06538)](https://arxiv.org/pdf/1701.06538)
- [DeepSeek V4 Paper (HuggingFace)](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf)
- [AMD + OpenAI Partnership Announcement](https://www.amd.com/en/newsroom/press-releases/2025-10-6-amd-and-openai-announce-strategic-partnership-to-d.html)
- [LMSYS GB200 Part 2](https://www.lmsys.org/blog/2025-09-25-gb200-part-2/)
- [Engram Paper (arXiv:2602.21548)](https://arxiv.org/pdf/2602.21548)
- [mHC Paper (arXiv:2601.07372)](https://arxiv.org/pdf/2601.07372)
- [Wikipedia: Liang Wenfeng](https://en.wikipedia.org/wiki/Liang_Wenfeng)
- [Author's earlier viral tweet (Jan 27, 2025)](https://x.com/bookwormengr/status/1883712073814954379)
- [Author's Substack](https://polymath707.substack.com/)
