---
title: "self-tuning inference for open models"
url: "https://www.together.ai/blog/polymorphic-inference"
fetched_at: 2026-11-05T10:01:11.506369+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# self-tuning inference for open models

Source: https://www.together.ai/blog/polymorphic-inference

At Together AI, we focus on making AI abundantly available to every individual user and organization. Our research team – the researchers behind FlashAttention, ThunderKittens, ThunderAgent, and more – has been a key driver behind our inference excellence. As the inference market grows exponentially, we’ve been focusing on how to scale our research capacity to enable abundant intelligence for all.
This has required a shift in our thinking from Static Inference to
Polymorphic Inference
– which is our response to the velocity of new model releases, diversity of model architectures, fast-changing workloads, and fast-changing hardware platforms. In this blog, we’ll highlight our research agenda for the Polymorphic Inference era – and how we are continuously using AI agents to optimize their own inference with
Continuous Compilation
.
‍
What is Polymorphic Inference?
Over the past year, there has been a marked step change in the diversity of open-source models and the ways that these models are deployed in production environments. We see this step change as requiring a new approach that we call
Polymorphic Inference
.
Polymorphic Inference (inference in “many shapes” from Greek) is a response to a number of changes we are seeing across the industry, for us primarily defined by the convergence of a few trends:
Increasing
velocity
of model releases. Open-source models are coming out at a faster clip – and are far more diverse – than ever before. 80% of traffic on OpenRouter goes to models released in the
last three months
.
Increasing
diversity
of model architectures. All of the top-ten most popular OSS models in use today use
different architectures
(not to mention the many closed-source architectures served by our partners).
Traffic shapes that continuously evolve.
We serve new users, organizations, and geographies every day across a broad range of workload shapes and SLAs. Product or algorithmic changes in harnesses, post-training of open-source models can all lead to changes to traffic shapes (e.g., a new post-train that increases the amount of tokens that a model spends thinking in exchange for higher quality).
Hardware that is changing
faster and more frequently
. We have seen major changes in inference serving capabilities from B200 to GB300, and are on the cusp of seeing the first Vera Rubin deployments (not to mention CPU-level optimizations, advanced storage systems, and alternative inference chips).
Polymorphic Inference
is our response to these changes – inference that changes and adapts to these rapidly-changing environments.
We contrast this against the state of the world before the explosion of OSS inference – which we retroactively call the era of “Static Inference.” Whereas modern Polymorphic Inference takes on infinite different shapes, Static Inference is defined by closed models, traditional Transformer architectures, single-user, and single-hardware-platform inference.
From Static to Polymorphic Inference
One of our motivations behind writing this blog post is that a lot of the discourse around inference systems remains quite focused on the legacy Static Inference paradigm.
For example, the typical vLLM, SGLang, or InferenceX / AgentX recipe online is launched with a static hyperparameter-tuned inference engine configuration. A config optimized for one setting is not necessarily the best one for another setting.
Open-source kernels are frequently released assuming some static traffic shapes and design decisions that can be miscalibrated against real production traffic. A classic example is MoE kernels; an MoE kernel that works well against random tokens may not transfer to real production settings.
We take some of the blame here! For a long time, it has been possible to write kernels that are optimal for a variety of settings. FlashAttention, near and dear to our hearts, is still one of the best ways to run training workloads and many prefill workloads.
And nearly two years ago we wrote about megakernels for AI inference, a single kernel painstakingly designed around a single static shape (e.g., batch size one Llama 1B). But through the experience of putting some of the first megakernels into production for our customers last year, we learned an interesting lesson:
megakernel fusion is actually not the right design goal for modern Polymorphic Inference!
In the era of Polymorphic Inference, every variation – from model architecture (e.g. MoE), to workload (dynamic workloads larger than batch size 1) – requires different technical approaches.
Optimizing Polymorphic Inference for diverse, rapidly-changing conditions
At Together, we are systems and AI researchers at heart – so we view this as an incredibly exciting time to be rethinking our research agenda for this bright new future.
‍
So, what’s the solution when your production traffic becomes ever more diverse? Get the AI agents to optimize themselves. This is the RSI moment for OSS models!
Achieving Polymorphic Inference requires solving a number of technical challenges in how we serve models. An ideal Polymorphic Inference experience is one that responds to the rapidly changing landscape of model architectures and workloads.
For example:
If your traffic shape changes – either through a product change or a change in user behavior – you should expect your inference system to adapt quickly.
If you are deploying workloads on a new model – you should expect your inference provider to approach ideal hand-tuned baselines as soon as possible.
If you have an existing product with stable user traffic, and you deploy it on a new hardware platform – you should expect performance to approach hardware bounds as quickly as possible.
These are lofty goals, but we believe that they are worth striving for. For us, one of the keys to achieving these goals is
getting AI agents to help optimize themselves
. The RSI loop is here for OSS models!
Continuous Compilation with Together Compiler
One of the projects that we’re announcing today as a first step towards achieving our goals for Polymorphic Inference is
Together Compiler
,
a rapid AI-powered performance optimization RSI loop. Today, Together Compiler powers
Continuous Compilation
optimization loops across many of our top production inference workloads.
Together Compiler takes the classic challenge of optimizing inference workloads and recasts it from a traditional compiler translation problem to an agentic search problem. Together Compiler identifies a core set of key optimization patterns and pairs a swarm of agents with a high-fidelity persistent engine for fast iterations. This work was the result of many months of work by Together’s Frontier Performance team, notably from Reyna Abhyankar and Dylan Lim!
Together Compiler is running
in production
today on some of our most popular serverless endpoints, where it has found further gains on top of already highly optimized code.
Excitingly, Together Compiler gives us the ability to
quickly adapt
to rapidly changing model architectures and traffic workloads. We call this capability
Continuous Compilation
. Whereas previously new workloads would require new sets of hand-written kernels and optimizations, Continuous Compilation driven by Together Compiler means that we can
automatically
adapt to new traffic shapes and workloads.
What’s coming next from Together AI’s Research team
We’ve learned a ton scaling Together AI to serve trillions of tokens per day (and for the first time even serving more tokens than closed-source model labs on OpenRouter earlier in October!). This has informed our vision and research agenda for the Polymorphic Inference era. Here’s a little preview of some of the things coming up on our research agenda:
Self-serve Continuous Compilation with Together Compiler
‍
Performance optimization needs to be a function of the workload deployment: the model, engine, traffic shape, and customer use case. Soon, our customers will be able to use Together Compiler to optimize their dedicated endpoints for their unique workloads at the click of a button.
Together Compiler is available to end customers in limited beta today –
reach out
if you want early access!
Shape-shifting speculative decoding
Inference engine configurations proposed in open-source repositories, VLLM, InferenceX, AgentX launch the engine with a fixed speculative decoding draft model and lookahead parameter. Speculative decoding needs to adapt per-domain, per-request, per-token and as a function of the traffic load.
ThunderAgent Router: Routing across heterogeneous deployments
Serverless inference endpoints serve an enormous number of users, each bringing their own traffic shapes and SLAs. This heterogeneity requires us to dynamically route requests across workers and deployment configurations across our clusters. We released ThunderAgent as an ICML 2026 Spotlight paper to share some early insights and have expanded on these foundations in production.
Together Post-Training
Several customers now want to incorporate open-source model backends into their AI applications. This requires choosing an open-source model, selecting and customizing the harness to the customer’s specific tool calls and use cases, and post-training the model to interact well with this harness. Our close partnerships with model labs including Moonshot, Minimax, and others allows us to help our customers customize open-source models for their own use cases and really own their intelligence stack.
TogetherLink: Workload-aware model routing
As OSS models improve, a key piece is getting them into everyone’s hands. The common perception is that a closed source model like Opus 5.5 is always best. But, as the history of AI has repeatedly shown us, ensembling a few pretty good models can definitely outperform using a singular great model, if combined in the right way. This builds on our roots in weak supervision at Stanford’s Hazy Research Lab (
Ask Me Anything
) and on our own work on combining models (
Mixture-of-Agents
, ICLR 2025).
Abundant intelligence for all
Inference is one of the most fascinating problems in AI Systems and we’ve unlocked a whole host of new insights through the scale at which we serve. To achieve our goal of making AI abundant for
everyone
we need our inference systems to continuously customize to each user and each workload in the Polymorphic Inference era. We’re excited to help close the loop and play a small role in making AI systems truly recursively self-improving.
If the ideas behind Polymorphic Inference ring true to your organization or your use case,
please reach out for early access
– we’d love to help you navigate these new complexities.
And lastly – if you want to help us tackle the challenge of Polymorphic Inference together, please take a look at our
careers page
– we’re hiring!
