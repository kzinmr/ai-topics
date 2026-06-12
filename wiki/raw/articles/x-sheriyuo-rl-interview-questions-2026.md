---
type: x_article
title: "RL Interview Questions 2026"
author: Xiuyu Li (@sheriyuo)
url: https://x.com/sheriyuo/status/2063295181131247674
article_url: https://x.com/i/article/2063294118101688321
zhihu_url: https://zhuanlan.zhihu.com/p/2046740446353811230
published: 2026-06-06
fetched: 2026-06-12
metrics:
  impressions: 336616
  likes: 1905
  bookmarks: 4742
  retweets: 179
  replies: 16
tags: [reinforcement-learning, grpo, ppo, training, career]
---

# RL Interview Questions 2026

After seeing several people receive PhD offers and then immediately land highly paid industry positions during spring recruiting, I started wondering whether going straight into industry might actually be the better move.

So I went through essentially every RL-related interview experience I could find on Zhihu, combined them with recent discussions and my own observations, and distilled everything into 35 of the most interesting questions.

Think of it as an RL interview benchmark.

CN version in Zhihu: https://zhuanlan.zhihu.com/p/2046740446353811230

A few notes:
- The list does not strictly separate LLM RL from Agentic RL. Some questions have very different answers depending on the setting.
- Nearly every question can be extended much further. No reference answers are provided. If you use an LLM, keep asking follow-up questions and search extensively.
- Modern RL hiring increasingly expects full-stack understanding. If you are an algorithm researcher, people will still ask infrastructure questions. The reverse is also true.
- Data-related questions are not included. Those are almost impossible to memorize and depend heavily on your actual experience.
- Memorizing interview questions is not enough. Deep understanding matters far more.

## Algorithm

1. Why use Actor-Critic instead of a pure Critic approach?
2. What is the relationship between KL divergence, cross entropy, and MLE?
3. How should rewards be designed in different RL scenarios?
4. How do importance sampling, rejection sampling, and other Monte Carlo methods fit into RL?
5. How is advantage computed in PPO and GRPO? Why subtract a baseline? Is standard deviation normalization really necessary?
6. How do RL training and test-time scaling perform exploration differently?
7. How does PPO clipping work? Why take the minimum objective? What happens without clipping? How does CISPO differ?
8. Why does GRPO include a KL penalty? How is the KL computed? Why do methods such as DAPO and GSPO remove it?
9. During LLM training, what happens if loss is accidentally All Reduced multiple times?
10. What is the reward function in DPO? Can reward hacking occur? How can it be mitigated?
11. What methods address train-inference mismatch in MoE models, and how do they work?
12. How should group size, learning rate, PPO epochs, and generation length be selected during RL training?
13. Compared with GRPO, how do Dr.GRPO, DAPO, GSPO, CISPO, SAPO, DPPO, MaxRL, and SimKO improve the training process? What are their limitations?
14. How do TRPO, DPPO, and AReaL enforce trust-region constraints on RL objectives?
15. Can RL fundamentally expand the capability frontier of LLMs?
16. Based on works such as ProRL, how should we think about scaling the boundaries of RL training?
17. What improvements does OPD introduce over traditional RL and SFT? What are its applications?
18. At which stage of training does reasoning ability emerge in LLMs?
19. From DeepSeek R1 to V3.2 and future V4 systems, what RL-related improvements have been introduced? How is RL different in MoE models?

## Infrastructure

20. Ignoring CPU offload, how many model copies exist in memory during GRPO training? How much memory can various optimizations save?
21. Distributed inference: KV cache transfer optimization and multi-GPU communication strategies.
22. INT8 versus FP8. What are the tradeoffs? Which precisions are preferred for training and inference?
23. What is the long-tail problem in RL rollouts, and how can it be addressed?
24. What issues does continuous batching introduce in RL training? How do vLLM and SGLang differ?
25. How do you measure utilization in vLLM and SGLang? How do you evaluate KV cache utilization during training?
26. How is backpropagation implemented in large-scale multi-node RL training?
27. What asynchronous RL frameworks exist, and what synchronization bottlenecks do they solve?
28. In AReaL or other partially rollout frameworks, are KV caches from previous policies preserved?
29. How does Expert Parallelism affect MoE throughput?
30. In long-context training, how should compute-communication overlap be designed? How do Megatron and FSDP differ in parallelism strategies?
31. How do you enable deterministic execution? What is batch invariance? What causes it? Is atomic add involved? Can atomic add solve the issue?
32. How do AReaL and slime differ in their understanding of the RL rollout bottleneck?
33. How should we think about staleness in fully asynchronous RL training? What are typical values in practice?
34. How does data flow through slime? How is it integrated with Megatron? How is the loss computed?
35. If you had to choose among VeRL, TRL, Unsloth, AReaL, and slime, which one would you use and why?

Good luck. And remember: interview preparation helps, but genuine understanding scales much further than memorized answers.
