---
title: "3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/3d-fireoptimizer"
scraped: "2026-05-10T01:27:03.580129+00:00"
lastmod: "2026-02-12T18:52:02.000Z"
type: "sitemap"
---

# 3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving

**Source**: [https://fireworks.ai/blog/3d-fireoptimizer](https://fireworks.ai/blog/3d-fireoptimizer)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
3d Fireoptimizer
3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving
PUBLISHED
6/14/2025
Table of Contents
Tradeoffs when designing AI systems
The optimization search space
Model Architecture
Parallelism Strategies
Hardware Selection
Quantization
Speculation
Combinatorial complexity
3D FireOptimizer tunes the knobs, so you don’t have to.
Case Studies
Summary
Table of Contents
Table of Contents
Tradeoffs when designing AI systems
The optimization search space
Model Architecture
Parallelism Strategies
Hardware Selection
Quantization
Speculation
Combinatorial complexity
3D FireOptimizer tunes the knobs, so you don’t have to.
Case Studies
Summary
Table of Contents
Once you’ve launched your AI app, the next problem you often need to solve is maintaining quality while meeting the cost and latency bars needed to scale. However, there is no “one size fits all” approach to achieving optimal LLM performance – it depends heavily on your unique workload and the tradeoffs you make across the stack. With an explosion of choices across hardware, low-level optimizations, and model families, navigating this space on your own is more challenging than ever.
At Fireworks, we help our customers find the sweet spot for their specific use case. We’ve previously published several
blogs regarding tradeoffs in LLM serving
and our approaches to them. Now, we’re excited to announce a new toolkit in our
FireOptimizer
tuning stack:
3D FireOptimizer
.
3D FireOptimizer automatically searches through thousands of options to find configurations that achieve the optimal quality, throughput, and latency for your workload.
In this blog, we dive into the dimensions that matter, walk through key levers 3D FireOptimizer uses, and explore a few examples. Whether you're optimizing for speed, throughput, or latency, Fireworks helps you get the best configuration — without the guesswork.
To request access to an optimized-endpoint for your workload, please fill out this <1 min
contact form
.
Tradeoffs when designing AI systems
We generally consider three metrics when designing AI systems: speed, throughput (cost), and quality.
No two LLM use cases are exactly the same – the tradeoffs that matter when building a chat application can be very different from those for a coding assistant or summarization agent. For example, here are just some of the variables that affect AI system design:
•
Prompt (input) length
– context-heavy applications may have up to 100k to 1M input tokens
•
Generation (output) length
– reasoning use cases may produce thousands of tokens while classification produces just one
•
Pattern and degree of prompt repetitiveness
– repetitive prompts from shared context or multi-turn tool call history allow for effective prompt caching
•
Predictability of the model output
– the outputs of rewriting or summarization cases are “easier to guess” and make optimizations like speculation more useful than in use cases like creative writing
•
Request arrival pattern
– some traffic patterns are spikey while others are more evenly distributed
Typically, the goal in designing your inference stack is to find the optimal setup to serve a particular traffic pattern at a minimum speed and quality with the lowest possible cost.
The optimization search space
There are many levers one can pull to try and satisfy the above objective. Let’s explore some of the key vectors in detail:
Model Architecture
Choosing
the right model family
and size for a given task has the biggest impact on the 3-D tradeoff. Different models will vary in their architectures, from the number of parameters to how they approach attention (MHA/MQA/GQA/MLA) to their feed-forward network design (MoEs vs MLPs). These naturally create differences in performance bottlenecks and, especially when considering size, out-of-the-box quality.
Fireworks supports 1000s of models, and we help customers experiment with different sizes and perform targeted quality improvements with Supervised and Reinforcement Fine-Tuning to help you fully explore the limits of different model variants.
Parallelism Strategies
We support a number of parallelism strategies, including data, tensor, and sequence parallel-sharding, disaggregation, different flavors of attention, and several variants of MoE sharding.
Each of these stresses GPU resources in a different way: memory for model weights, how compute is allocated, memory for KV cache, communication requirements, and others. All of these sharding options can be mixed and matched with each other depending on the use case.
Hardware Selection
Fireworks supports many hardware types, such as L40s, A100s, H100s, H200s, MI300Xs and the latest editions like B200s and the upcoming Mi325Xs.
Each hardware type has different performance characteristics such as TFLOPs, memory bandwidth, and supported operations. Newer hardware comes with the best absolute speed but may be more expensive.
Quantization
Lowering precision via quantization is a proven way to extract more speed and throughput, especially on newer hardware generations. Fireworks supports more than eight turn-key quantization recipes based on published methods and novel in-house research and developed quantization-aware fine tuning recipes to mitigate quality impacts of quantization. We also now support the newest hardware-accelerated formats like NF4 on B200s. For a more in-depth look, please see our
quantization blog
and recent B200/NF4 announcement.
Speculation
Fireworks supports several different types of
speculation strategies
that excel in different scenarios. Choosing the right approach and number of speculation tokens is specific to every use case. For example, a code rewriting use case may use N-grams and Predicted Outputs, a chat use case may utilize a smaller speculator model, and a custom use case may want to train a bespoke EAGLE speculator.
We always bring the latest research in speculative decoding and do in-house experimentation with custom speculator architectures–for example, we’ve recently added support for tuning and serving
EAGLE3
–a novel speculator architecture. You can train or fine-tune speculators through FireOptimizer.
Combinatorial complexity
It’s not sufficient to pull just one of the above levers at a time, as changing one lever may affect how another should be pulled. For example, quantizing a model in a certain way can increase the available free KV cache space. This in turn may change how you might want to parallelize or replicate the model based on the SLAs, as well as the hardware type it can be run on. However, this is also a function of how much prompt caching can help the use case, as well as the number of tokens that need to be generated.
There is no single right setting for each knob, and every knob affects every other.
Thus the search space easily exceeds 100,000 possible combinations!
3D FireOptimizer tunes the knobs, so you don’t have to.
At Fireworks we run a lot of production workloads of varying shapes and sizes, constantly running extensive performance sweeps on different hardware with varying settings. This has given us a number of heuristics and precomputed profiles that help us efficiently prune the search space.
As a result, after potentially tuning a model or speculator specifically to your use case’s unique data distribution, 3D FireOptimizer can ingest your workload characteristics and desired SLAs to offer you a choice between a few optimal configurations.
Case Studies
To see 3D FireOptimizer in action, let’s dive into a few examples to show how endpoints created using 3D FireOptimizer offer a much better QPS vs Latency tradeoff compared to the baseline available through our public platform alone, by holding the same quality bar.
Case 1: Whole-codebase agentic code completion
Our first use case is whole-codebase agentic code completion with
Deepseek V3
. This workload is characterized by a large prompt cache, with only a small portion of code newly generated. In particular, here are the Pareto optimal curves for 120k input and 400k output tokens, caching 116k tokens in the prompt. Notice how 3D FireOptimizer finds a configuration to offer the same QPS at much lower latency!
Case 2: Code-Rewriting
Another code use case is
code-rewriting. This use case has a workload shape of 2500 prompt tokens, 1500 generation tokens and uses Qwen Coder 2.5 14B.
Case 3: Chatbot
Lastly, we can consider a typical chat bot
with a relatively small prompt and a small prompt cache. Again using Deepseek V3, here are the Pareto curves for a 5000 token input, 500 token output, and 1500 token prompt cache.
Summary
Optimizing LLM serving isn’t just about one metric — it’s a complex balancing act across
speed, cost, and quality
. At Fireworks, we’ve built the
3D FireOptimizer
as part of our FireOptimizer toolkit to help customers intelligently navigate these tradeoffs. Whether you're serving creative writing prompts in real-time, running high-throughput catalog processing, or working with 100k-token contexts, every use case brings unique SLAs and workload patterns.
3D FireOptimizer evaluates model architecture, quantization level, speculation strategy, hardware type, parallelism scheme, and more — understanding that tweaking one lever often affects all the others. Rather than leaving customers to guess from hundreds of thousands of configuration combinations, our system draws from deep profiling data, rule-based heuristics, and real-world production usage to find optimal setups for any use case. To get started with a 3D FireOptimizer optimized endpoint,
please fill out this <1 min contact form
.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
