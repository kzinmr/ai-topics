---
title: "Announcing custom models and on-demand H100s with 50%+ lower costs and latency than  vLLM"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/custom-models-h100s-on-demand-deployments"
scraped: "2026-05-10T01:27:26.385337+00:00"
lastmod: "2026-02-12T18:53:01.000Z"
type: "sitemap"
---

# Announcing custom models and on-demand H100s with 50%+ lower costs and latency than  vLLM

**Source**: [https://fireworks.ai/blog/custom-models-h100s-on-demand-deployments](https://fireworks.ai/blog/custom-models-h100s-on-demand-deployments)

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
Custom Models H100s On Demand Deployments
Announcing custom models and on-demand H100s with 50%+ lower costs and latency than  vLLM
PUBLISHED
6/3/2024
Table of Contents
Introduction
Custom model import
H100s and improved performance
Auto-scale improvements
Conclusion
Table of Contents
Table of Contents
Introduction
Custom model import
H100s and improved performance
Auto-scale improvements
Conclusion
Table of Contents
Introduction
At Fireworks, we’re empowering developers to productionize generative AI with unparalleled speed, quality and cost. In March, we launched on-demand (dedicated) deployments, which lets developers provision their own GPU(s) for guaranteed latency and reliability. These GPUs run on the proprietary Fireworks serving stack, which enables much faster serving speeds than competing and open-source solutions, like vLLM, even on an identical hardware set-up.
Today, we’re making on-demand deployments more configurable and powerful with the launch of:
Custom HuggingFace models
- Import models from Hugging Face files, unlocking thousands of models to be productionized on Fireworks
H100s and improved performance
We’re bringing (a) H100 hardware options and (b) Serving stack optimizations and long-prompt optimizations for even better performance. One H100 on the FireAttention stack has the throughput of 3 H100s running vLLM while providing ~60% faster speeds
Auto-scale to and from 0.
Use on-demand deployments like serverless models by just querying the API. No need to explicitly start or stop the deployment or pay for start-up times. Automatically scale capacity with usage to multiple GPUs.
Custom model import
We’ve seen the open-source community’s strong response to custom models like
Hermes 2 Pro Llama 3
,
a variation of Llama with enhanced function calling and task following. By choosing from countless custom models, developers can select the model that has the best quality for their use case. We’ve made it simple to import these models into Fireworks to use with our affordable and optimized infrastructure.
How do I import models?
Simply provide Fireworks with files for your model in the Hugging Face model format and upload the model with the following command.
1
2
firectl create model <MODEL_ID
>
/path/to/files
Then you can spin up an
on-demand deployment
in seconds without needing to install or configure software. We support models from the most popular model architecture, including Llama and Mixtral. See our full
docs
for more details.
H100s and improved performance
At Fireworks, we know there’s no one-size-fits-all model and serving configuration. The best serving stack configuration depends on specific goals and prompts. Fireworks has been personally tailoring serving configurations for our enterprise customers. Now, Fireworks is bringing personalized optimizations and choices to the public through our on-demand GPUs.
•
Long prompt optimizations:
Users can specify whether they have a long prompt (> ~3000 tokens) and we’ll automatically apply a number of performance tweaks for this prompt size. From our benchmarks, we’ve seen speed increase by ~20% and throughput by up to 100%.
Model
Performance with long prompt flag
Performance w/o long prompt flag
Llama 3 8B (with 4k token prompt)
2117 ms latency, 7.5 QPS
2625 ms latency, 3.01 QPS
•
Further serving stack optimizations:
We’ve added a number of on-demand performance stack improvements for both A100 and H100s. We now observe 60% latency and 350% capacity improvements compared to vLLM. Therefore, developers using vLLM could go from running 10 GPUs with vLLM to 3 GPUs on Fireworks, while serving the same throughput. Check out this
blog
for detailed performance breakdowns.
Prompt (on Llama 3 8B)
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
•
H100s
: Users now have the ability to choose to use H100 GPUs, instead of only using A100 GPUs. Compared to the A100, the H100 offers lower latency and more capacity (ability to serve more requests on one chip). Our hourly H100 price by itself is less expensive than providers like HuggingFace TGI ($10). Even compared to platforms offering H100s at prices like $4.79, we tested our on-demand solutions to be ~53% more affordable
on a per-token basis
, since Fireworks GPUs are significantly more efficient.
Auto-scale improvements
We’ve made it easier and more configurable to use on-demand deployments by introducing the ability to scale to and from 0. By default, GPUs will ****start up and scale down automatically based on usage. If you haven’t used your model for a while (default one hour), your GPU capacity will be scaled to 0 and you won’t be charged for this idle time. When you get a request, your GPU will be automatically spun back up and usable again. Users do not pay for start-up time.
This makes it both much easier and cost-effective to use on-demand deployments. Simply query the API - no need to set up the deployment before each usage! Reduce costs as well by ensuring that your deployments are scaled down when they’re not in use.
Beyond scaling from 0, you can also set your deployments to scale to multiple GPUs to support spikes in traffic. We’ve also made our auto-scaling logic configurable, meaning that you can set the specific time to wait before scaling a deployment up and down with traffic. This provides maximum choice in optimizing for cost-savings and user experience.
Conclusion
Through these improvements, Fireworks on-demand deployments provide the fastest and most affordable solution to serve LLM traffic on private GPUs for predictable performance.
•
Managed and automatic
- No need to specially configure software or models. Get started on seconds and have the market’s most performant software stack automatically managed for you
•
The fastest, highest-quality user experiences -
Provide your users with the best experiences by using the lowest-latency and that enables the best model quality, through custom models and Fireworks’ fine-tuned and exclusive models
•
Cost-effective -
Go from 10 GPUs to 3 by using Fireworks’ hyper-optimized stack with market-leading throughput
On-demand deployments provide options for reliable, fast serving at scale for businesses that are ready to scale up from our serverless offering but not yet ready for long-term, enterprise contracts. Curious about performance details of on-demand deployments or want more info about how on-demand deployments compares to serverless or other frameworks? Check out our deep dive on
why on-demand deployments
.
When you’re ready to get started, check out our
docs
. At Fireworks, we’re creating the best platform for everyone to serve generative AI models in production, from nascent start-ups to large enterprises.
We’d love your feedback! Please contact us on
Discord
or
Twitter
. If you’re looking to learn more about on-demand deployments, feel free to directly schedule time with our PM (
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
