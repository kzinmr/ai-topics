---
title: "Evaluating Recent Model Releases on GDPx (full body)"
date: 2026-11-26
source: https://newsletter.semianalysis.com/p/evaluating-recent-model-releases
publisher: SemiAnalysis (publication_id=6349492, post_id=226576253)
authors: [Dylan Patel, Alexander Huang, Shi Zhao]
retrieved: 2026-11-26
access: free (44 <p> paragraphs via newsletter.semianalysis.com curl)
tags: [newsletter, raw]
---

# Evaluating Recent Model Releases on GDPx

AI's impact is nowhere near evenly distributed across the economy today, and we expect this trend to intensify in the future. Many tasks already can't justify paying for Fable 5.2, much less Fable 7. Thus, if your goal is to track the progress of frontier models, you should focus on the domains where they will be most impactful.

It's for this reason that GDPx intentionally forgoes industries like government and real estate, and instead covers the following domains:

Our methodology is also unique. To ensure all our tasks are truly representative of their respective domains, we partnered with 14 specialized data partners to make 206 tasks.

The single most notable thing about GDPx, however, is its difficulty. Whereas other benchmarks will often debut with the top model scoring over 50%, Opus 5.5—the highest-scoring model on release day—scored just 12% on GDPx. This massive headroom is what allows GDPx to discriminate between future model releases, unlike saturated benchmarks such as Terminal Bench 4.0.

Since launching GDPx on November 1st, both Anthropic and OpenAI have released new frontier models. Google made a dramatic resurgence with the Gemini 4 series, and we've seen notable releases from Alibaba and Moonshot as well.

It's worth emphasizing that certain models like Fable 5.2 and GPT-6.2 Astra have sandbagged overall scores due to their safety classifiers. If we exclude cyber, biology, and alignment, the three domains where safety classifiers sometimes kick in, and switch to partial grading to get more signal from the extremely difficult legal and finance domains (which default to binary), then Fable 5.2 scores 29.9% vs Astra 32.2%.

We think you can argue either of these is the "correct" GDPx leaderboard. On one hand, safety classifiers truly limit the usefulness of models in domains like cyber and bio. On the other hand, if the goal is to measure a model's intelligence, penalizing it for refusing to attempt a task due to safety concerns feels quite unfair.

Either way, OpenAI is the current king of GDPx. Going off the main leaderboard, which covers all domains, 6.2 Astra ranks first with a score of 19.3%. Fable 5.2 ranks second at 16.4%, and the best non-OpenAI/Anthropic model, Gemini 4 Carbon, ranks fifth at 10.9%. Carbon just barely edges out the highly lauded Gemini 4 Neon, which ranks sixth with a score of 10.1%. (6.2 Sol ranks with 11.5%.)

The cost-performance Pareto frontier is also entirely dominated by OpenAI. DeepSeek v4.1 Flash just barely sneaks in at the very low end.

Although the Twitter hive mind has recently been dumping on 6.2 Astra and praising Gemini 4 Neon, we believe GDPx accurately captures the true relative ranking of model capabilities in frontier domains. Astra and Fable remain decisively above all other models in terms of raw intelligence.

Gemini 4 Neon is the model of the moment, with some declaring it the single best model in the world. Earlier this year, we published a newsletter predicting the demise of Gemini/DeepMind. Clearly we were wrong. Compared to their competitors' offerings at the time, Gemini 4 Neon is much better than Gemini 3.8 Flash was, and model progress at DeepMind has inflected up over the past few months. Neon is the best at Bio, but likely because OpenAI and Anthropic have more refusals. With that being said, the GDPx results show Gemini is still decisively behind both Anthropic and OpenAI across virtually all frontier domains.

6.2 Astra significantly outperforms Gemini 4 Neon at RSI, materials science, and hardware design, while Fable 5.2 dominates in chip design, software engineering, and quant trading. Neon is the top-scoring model in biology, but this is likely due to more lenient safety classifiers (though we did find Neon to have stricter safety classifiers in cyber than other Google models).

We believe Gemini 4 Neon's overwhelmingly positive reception is largely due to model behavior and not intelligence. Put simply, Neon is a pleasant model to talk to. Its liberal use of exclamation marks and cheerfulness reminds us of GPT 4o, which was a similarly adored model.

In terms of the overall AI race, we believe Anthropic and OpenAI are still clearly in a tier of their own. Google is a distant third, but also deserves its own tier. Meta, SpaceX, Moonshot, Alibaba, etc. are all fighting for 4th.

Neon is unnecessarily expensive to run because Google's prompt caching lags behind its competitors. Running Neon on GDPx cost us $15,286. Had Neon matched Opus 5.5's cache hit rate, that bill would have been $12,536, about 18% less. At 6.2 Astra's cache hit rate, it would have been $10,403, about 32% less. To its credit, Google shipped a caching update just today (another 4.5% increase to Neon's cache hit rate, which would cut this bill by roughly 17-18%).

## GPT-6.2 Astra and Sol

GPT-6.2 Astra and 6.2 Sol both do extremely well on GDPx, scoring 19.3% and 11.5%, respectively. Interestingly, this goes against most people's subjective impressions of the models. Public reception to 6.2 Astra on X was embarrassingly bad, with one influencer calling it the "worst model OpenAI has ever released."

However, 6.2 Astra also represents a significant drop in base model log-perplexity, which OpenAI recently disclosed as one of the best proxies for measuring models pretraining intelligence, and therefore sample efficiency.

Taking a closer look at individual GDPx domains reveals the answer. GPT-6.2 Astra excels on tasks that require complex reasoning like chip design, hardware design, materials science, and RSI. It's also the first model to score higher than 0% on legal, and it is SOTA on finance.

Notably, 6.2 Astra is lackluster at software engineering, which is the domain most people on X evaluate models on. It scores half that of Fable 5.2. Qualitatively, the model is also often too literal when following instructions, fails to infer user intent/make reasonable assumptions, and is just generally annoying to talk to.

6.2 Astra scores extremely high on alignment. It appears that OpenAI's safety commitments post Hugging Face weren't just for show.

6.2 Sol is similarly spiky to 6.2 Astra and worse at everything except quant and SWE. Overall, we believe the current negative sentiment around OpenAI's models is overblown. The 6.2 series is clearly extremely smart, and OpenAI completely dominates the cost-performance pareto frontier as well—they just need to do a better job making their models pleasant to work with.

## Fable 5.2

Fable 5.2 is the second-best model on GDPx at 16.4%, behind only 6.2 Astra, and the gap narrows once safety classifiers are taken out (29.9% vs 32.2% with partial grading). It's also by far the most expensive model to run. At $88 and 1.23M output tokens per task, Fable 5.2 costs 1.9x as much as 6.2 Astra and uses 3.9x as many output tokens, for a lower score.

Much of this comes from Fable 5.2's increased persistence and its proclivity for spawning subagents for testing and review. For now, all GDPx runs are done at the highest possible reasoning level.

Materials science is the starkest example. Fable 5.2 costs 2x as much as 6.2 Astra per task and uses 3.7x as many output tokens, yet scores 19 points lower (21.8% vs 41.3%). Even 6.2 Sol beats it (25.8%) at roughly a tenth of the cost ($8 vs $79 per task).

Finance: with partial grading, Fable 5.2 scores 53.6%, effectively tied with Opus 5.5 (54.6%) and 6.2 Astra (53.5%). But it uses 2.3x as many output tokens as Opus 5.5 and 12x as many as 6.2 Astra, which makes it 6.6x as expensive as 6.2 Astra per task.

Software engineering is where Fable 5.2 shines. At 24.4%, it nearly triples Opus 5.5 (8.9%) and is well ahead of the next best model, 6.2 Sol (15.6%). Compared with Opus 5.5, its cost per task rises by about the same multiple as its score (2.8x), and it costs 17x as much as 6.2 Sol.

6.2 Astra does significantly better than Fable 5.2 at RSI (33.22% vs 24.13%). However, we think this is largely due to Anthropic explicitly nerfing their public models' AI research abilities.

## Chinese models

Qwen4-Max is the highest scoring Chinese model on GDPx at 7.44%. It's a little worse than Claude Sonnet 5.5, though significantly cheaper. Qwen4's biggest gains vs Qwen3.8 are in software engineering, RSI, cyber, and bio.

Kimi K3.1 Pro performs comparatively worse on GDPx than other benchmarks like the Artificial Analysis Intelligence Index, but this is largely because K3.1 Pro is benchmaxxed on Terminal Bench 4.1 (which is 10% of the AA index). K3.1 is unironically the number one model on Terminal Bench, when in reality, the model clearly still lags Fable 5.2, Gemini 4 Neon, 6.2 Astra, etc.

## Domain-specific cyber models

As part of this update, we also evaluated a number of custom cyber models. It's clear that domain specific models are becoming significantly more relevant as Anthropic, OpenAI, and Google continue to crackdown on their safety classifiers.

Anthropic is also explicitly nerfing capabilities like RSI, and there are other domains like materials science where having proprietary data can enable non-frontier labs to train state of the art models.

Evaluated custom models: a cyber post-train of DeepSeek v4.1 Flash from Hinoki called HO1; abliterated versions of Kimi K3.1 Pro and DeepSeek v4.1 Flash from Boundless. Surprisingly, the 2 abliteratred models performed slightly worse than their vanilla open source counterparts, while Hinoki HO1 performed marginally better — largely because the vanilla OSS models never refused any of our cyber tasks to begin with.

We'd also like to thank Modal for being our inference provider for Kimi K3.1 Pro.

We believe GDPx provides the most accurate relative ranking of model quality and continue to be pleasantly surprised how well the benchmark matches our subjective opinions.
