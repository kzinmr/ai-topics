---
title: "RAM: Relative Adoption Metric"
url: "https://substack.com/redirect/40d782e5-a5a1-4935-8e56-77bbc8e6bc97?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-14T20:42:49.461927+00:00
source_date: 2026-04-14
tags: [newsletter, auto-ingested]
---

# RAM: Relative Adoption Metric

Source: https://substack.com/redirect/40d782e5-a5a1-4935-8e56-77bbc8e6bc97?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Download counts alone can hide which models are truly breaking out across different size classes.
While building
The ATOM Project
and other tools to measure the open ecosystem at
Interconnects.ai
, we are often frustrated with using downloads as a primary metric. We, and the community, know that small models are downloaded much more, so it makes some adoption metrics favor organizations releasing small models. Over the 1,100+ leading LLMs we track carefully, more than 1.4 billion of ~2 billion total downloads come from models in the 1-9B range.
This small model dominance happens to be partially caused by far more models
being released
at that size. Among the top 10 downloaded models at each size category, the median models from 1-9B parameters are only downloaded about 4X the count of models of 100B+ parameters. Still, this difference combined with the potential of small models to be outliers in downloads—by being loaded in the continuous integration (CI) tests of ML developers checking their code and other at-scale automated systems—makes small models dominate plots.
We created the
Relative Adoption Metric
, reported as a RAM Score, to be able to tell within 30-90 days if a new model is on track to be ecosystem defining. We can already see that some models, such as GPT-OSS, are truly exceptional. In releasing only 2 models, OpenAI is well on the map as a top 5-10 open model lab in adoption metrics—this is hard to see when comparing organizations versus each other, when OpenAI's competitors may have many models.
We're also excited to see that some recent larger models from newer AI labs on the scene, such as MiniMax or Moonshot AI, are outperforming the metric, indicating competition in the large MoE space dominated by DeepSeek earlier in the year.
We're excited to support the ecosystem with this new tool!
