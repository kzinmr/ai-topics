---
title: "Introducing Muse Spark: Scaling Towards Personal Superintelligence"
url: "https://substack.com/redirect/ad5e29d4-ba95-4af1-86da-6a32b8b9eb1f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-10T14:11:15.768077+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Introducing Muse Spark: Scaling Towards Personal Superintelligence

Source: https://substack.com/redirect/ad5e29d4-ba95-4af1-86da-6a32b8b9eb1f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

To build personal superintelligence, our model’s capabilities should scale predictably and efficiently. Below, we share how we study and track Muse Spark's scaling properties along three axes: pretraining, reinforcement learning, and test-time reasoning.
Pretraining
. The pretraining phase is where Muse Spark acquires its core multimodal understanding, reasoning, and coding abilities — the foundation that reinforcement learning and test-time compute build upon.
Over the last nine months, we rebuilt our pretraining stack with improvements to model architecture, optimization, and data curation. Together, these advancements increase the capability we can extract from every unit of compute. To rigorously evaluate our new recipe, we fit a scaling law to a series of small models and compare the training FLOPs required to hit a specific level of performance. The results are clear: we can reach the same capabilities with over an order of magnitude less compute than our previous model, Llama 4 Maverick. This improvement also makes Muse Spark significantly more efficient than the leading base models available for comparison.
