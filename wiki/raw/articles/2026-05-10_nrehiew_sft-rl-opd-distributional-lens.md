---
title: "SFT, RL, and On-Policy Distillation Through a Distributional Lens"
source: "X (Twitter) Post"
author: "wh (@nrehiew_)"
date: 2026-05-10
scraped: 2026-05-11
url: "https://x.com/i/status/2053482349300797526"
tweet_id: "2053482349300797526"
type: "x-thread"
engagement:
  views: 181000
  bookmarks: 573
  likes: 87
  reposts: 7
tags: [post-training, sft, rl, on-policy-distillation, llm-training]
---

# SFT, RL, and On-Policy Distillation Through a Distributional Lens

I have been thinking about post-training methods in terms of distributions. A language model is a distribution over sequences. When we post-train it and attempt to teach it a task, we are reshaping this distribution. Different post-training methods differ in how they reshape this distribution, what they treat as the target and how directly they define this target.

This is neither a very precise statement nor is it meant to be fully rigorous. I just find it to be a useful mental model, but I think it explains a lot of the qualitative differences between SFT, RL, and On-Policy Distillation. This is the intuition I want to explore in this post.

## A Distributional View of Post-Training

Under this view, the most important question to ask is: What is the target distribution?

[Content continues — see full X post for complete text]

---
*Note: This is an X-native long-form post. Full content at: https://x.com/i/status/2053482349300797526*
