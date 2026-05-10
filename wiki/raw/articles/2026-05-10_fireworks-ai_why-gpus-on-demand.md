---
title: "GPUs on-demand: Not serverless, not reserved, but some third thing"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/why-gpus-on-demand"
scraped: "2026-05-10T01:21:01.822323+00:00"
lastmod: "2026-02-12T18:53:02.000Z"
type: "sitemap"
---

# GPUs on-demand: Not serverless, not reserved, but some third thing

**Source**: [https://fireworks.ai/blog/why-gpus-on-demand](https://fireworks.ai/blog/why-gpus-on-demand)

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
Why Gpus On Demand
GPUs on-demand: Not serverless, not reserved, but some third thing
PUBLISHED
6/3/2024
Table of Contents
Tl;dr
Intro
Fireworks Offerings
On-demand GPUs performance details
Conclusion
Table of Contents
Table of Contents
Tl;dr
Intro
Fireworks Offerings
On-demand GPUs performance details
Conclusion
Table of Contents
Note: Fireworks A100 and H100 prices have since been reduced to $2.90 and $5.80!
Tl;dr
•
On-demand GPUs are a great option for scaling companies who need reliability and speed but cannot yet commit to long-term enterprise reservations of GPUs
•
“Graduating” from serverless to on-demand deployments starts to make sense economically when you are running ~100k+ tokens per minute
•
On identical H100 hardware, Fireworks’ software advantage provides 53% cost reduction and 60% latency reduction compared to running vLLM with GPUs on competing platforms. This allows you to simultaneously serve more users, at lower cost, with faster response times
•
Fireworks on-demand deployments require no software installation. Simply choose your model and GPU configuration and get started in seconds, without paying for boot times. Your GPU even scales to zero when you are not using it!
Intro
One of the most rewarding things at Fireworks is being a part of the scaling journey for many, exciting AI start-ups. Over the last few months, we’ve seen an explosion in the number of companies beginning to productionize generative AI. A question that we commonly get is:
“How should I think about serving LLMs via (1) A Serverless, token-based options vs (2) A GPU, usage time-based option? “
We’re writing this post to help explain the tradeoffs of serverless vs dedicated GPU options.
Fireworks Offerings
Fireworks has 3 offerings for LLM serving: (1) Serverless (2) On-demand (3) Enterprise.
Serverless
Fireworks hosts our most popular models “serverless”, meaning that we operate GPUs 24/7 to serve these models and provide an API for any of our users to use the models. Our serverless offering is the fastest, widely available platform and we’re proud of its production-readiness. Serverless is the perfect option for running limited traffic and experimenting with different LLM set-ups. However, serverless has limitations:
Serverless is not personalized for you
Your LLM serving can be made faster, higher-quality or lower cost based on personalization on several levels:  Our serverless platform is designed to excel at a variety of goals and support hundreds of base models and fine-tuned models. However, a personally-tailored stack still may provide better experiences.
•
GPU configuration -
The quantity, type and configuration of GPUs can be tailored based on business needs, like optimizing for speed vs cost or providing more capacity for product launches
•
Serving stack -
The software itself ****can be tuned based on factors like prompt length and UX goals (latency vs throughput, etc)
•
Models
- Serverless model selection is curated by Fireworks, so niche models may not be available
Serverless performance is affected by others -
Other Fireworks users share our serverless deployment, so speeds vary depending on overall usage. If you happen to use the deployment at the emptiest hours, you’ll experience the fastest speeds and vice versa. Our public platform is still independently benchmarked to have the lowest variation in latency, but consistent performance is paramount for certain use cases, like live voice chat agents.
Serverless has volume constraints -
Generally, when businesses have the volume to use significant GPU capacity, it doesn’t make sense to use serverless because:
•
Rate limits don’t allow it -
Since GPU deployments are shared, we employ rate limits to ensure that a few actors can’t greatly affect everyone else’s experience. Our rate limits (600 RPM by default) are significantly higher than rate limits of other serverless inference providers (often below 50 RPM) but businesses with significant volume could struggle to run their app entirely on Fireworks
•
Private GPUs may be cheaper with large volume -
Given (a) Efficiency improvements from personalized set-ups and (b) GPU pricing that builds in “bulk discounts” compared to serverless, large businesses generally receive cheaper pricing by reserving their own GPU
Enterprise Reserved GPUs
Given these constraints, companies with large usage volumes often reserve their own private GPU(s) for set periods of time. This commitment also enables Fireworks to help companies personally configure their serving set-up and provide SLAs and guaranteed support. However, many scale-up companies in the midst of prototyping are unable to commit to enterprise reserved capacity.
On-demand GPUs
To make it easier for scaling teams to benefit from Fireworks, we offer on-demand, dedicated GPUs with our FireAttention stack. Users pay per hour and can scale their GPU usage up or down automatically based on traffic. Configurations can automatically scale up and down from 0 GPUs, so developers pay nothing during idle periods. Compared to serverless, using your own GPU can provide:
•
Guaranteed speed and reliability
by using private GPUs
•
More model choice -
import your custom base model or use dozens of Fireworks-provided base models
•
Improved speed
- configure the number of set-up of GPUs based on your goals and optimize the Fireworks serving stack based on your prompt length
•
Lower costs,
especially with high volume. Costs reduce as volume increases.
•
Capacity for higher request volume
, with no hard rate limits
On-demand GPUs performance details
An important consideration in deciding to use on-demand deployments is expected performance vs price, so we have included some performance details and FAQs.
What latency improvements can I expect compared to vLLM or hosting my own GPU?
Generally, we see that Fireworks is ~40-60% faster compared to open-source solutions but performance varies depending on model and workload. We obtained the below results using the min worldsize (minimum # GPUs to host a specific model) on H100 GPUs on Fireworks vs vLLM software. The latency was calculated with heavy throughput, so the GPU on Fireworks simultaneously delivered significantly better speed and throughput.
Mixtral 8x7b
Prompt Lengths (Tokens)
Fireworks Latency
vLLM Latency
Very long prompt (32000 input, 100 output)
3319 ms (at 0.293 QPS)
6049 ms (at 0.165 QPS)
Long prompt (4000 input, 200 output)
4900 ms (at 1.623 QPS)
8060 ms (at 0.124 QPS)
Short prompt (128 input, 4 output)
118 ms (at 8.31 QPS)
285 ms (at 3.51 QPS)
Llama 3 8B
Prompt Lengths (Tokens)
Fireworks Latency
vLLM Latency
Long prompt (4000 input, 200 output)
2117 ms (at 7.5 QPS)
2877 ms (at 0.348 QPS)
Medium prompt (2000 input, 100 output)
740 ms (at 1.33 QPS)
1509 ms (at 0.663 QPS)
Short prompt (128 input, 4 output)
43.3 ms (at 22.51 QPS)
247 ms (at 4.056 QPS)
What throughput/cost improvements can I expect compared to vLLM or hosting my own GPU?
The efficiency of the
FireAttention
serving stack means that the same H100/A100 chip running on FireAttention can handle significantly more volume than an H100/A100 running software like vLLM.
•
GPU:GPU comparison:
Generally, we observed that an H100 running FireAttention provides ~350% the capacity of an H100 running vLLM
•
Cutting # GPUs:
Therefore, if you were running 10 GPUS on vLLM, you could run ~3 GPUs on Fireworks.
•
Cutting costs:
Thus, if you were running an H100 at $4.69/hour (pricing similar to competing platforms), you’d save ~53% by switching to Fireworks H100s priced at $7.79/hour by reducing your number of total GPUs
•
Detailed numbers:
See below for our calculations on cost per token when running on H100(s) at capacity. We achieved the numbers using a prompt with input lengths of 4000 and output lengths of 200, but found similar results across different prompts.
Model
Fireworks $/1M tokens on saturated GPU (H100 served at $7.79/hour)
vLLM $/1M tokens on saturated GPU (H100 served at $4.69/hour)
Mixtral 8x7b
$0.23
$0.49
How else is running a GPU on Fireworks different from provisioning my own GPU with vLLM?
•
The best serving stack, managed and updated for you:
Fireworks is constantly improving our serving stack and our on-demand deployments (see our June
performance updates
). By choosing Fireworks, you’ll get the world’s most efficient serving stack automatically managed for you
•
Set-up in seconds:
Get a hyper-optimized set-up in seconds instead of spending hours configuring software on your own GPU. No paying for start-up times either on Fireworks. Simply specify the model and deployment configuration and get started right away, saving you both time and money
•
Production reliability:
Fireworks only utilizes the most reliable Cloud infrastructure providers for our GPUs. The same infrastructure for on-demand powers companies like Uber, Doordash and Cursor
•
Compatibility with tuning and other Fireworks services:
Optimize your on-demand serving experience with Fireworks innovations, like our fine-tuning service, exclusive models and
structured outputs
I’m using Fireworks’ serverless model hosting. When does it make sense for me to "graduate" to on-demand?
•
Tokens/minute:
Cost-wise, we generally see that it makes sense to switch when achieving volumes nearing ~500,000 tokens/minute.
•
RPM
: 500,000 tokens/minute translates to 100 RPM with 5000 input + output tokens per request, or RPM of 500 RPM with 1000 tokens per request. Generally this “break-even” point makes for a smooth transition from our 600 RPM rate limit
•
Unit economics of switching:
Cost per tokens when using on-demand deployments continue to decrease until approaching the figures above of $0.23/1M tokens with Mixtral and $0.092/1M tokens with Llama 3 8B
Model
Tokens/min needed to reach serverless price
Serverless $/1M tokens price
On-demand $/1M tokens for saturated GPU
Mixtral 8x7b
377,584
$0.5
$0.23
Llama 3 8B
649,166
$0.2
$0.09
Conclusion
Using GPUs on-demand can provide a cheaper, faster and more reliable solution than serverless, especially when operating with higher volume. On-demand GPUs can act as a great bridge to a longer-term reserved GPU solution, where developers can benefit from completely personalized set-ups and enterprise SLAs. Fireworks is committed to enabling businesses to scale on our platform from testing an initial prototype on serverless through to serving millions of end users on reserved GPUs.
When you’re ready to get started, check out our
docs
or hear about our latest product updates for on-demand
in this blog post.
Looking for more performance numbers or interested in chatting directly about on-demand deployments? Feel free to directly schedule time with our PM (
https://calendly.com/raythai
). We can’t wait to see what you build!
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
