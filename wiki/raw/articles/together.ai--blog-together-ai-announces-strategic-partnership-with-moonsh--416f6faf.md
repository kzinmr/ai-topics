---
title: "Together AI announces strategic partnership with Moonshot AI to natively serve Kimi models"
url: "https://www.together.ai/blog/together-ai-announces-strategic-partnership-with-moonshot-ai-to-natively-serve-kimi-models"
fetched_at: 2026-07-30T10:06:48.135361+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Together AI announces strategic partnership with Moonshot AI to natively serve Kimi models

Source: https://www.together.ai/blog/together-ai-announces-strategic-partnership-with-moonshot-ai-to-natively-serve-kimi-models

Today we're announcing a strategic partnership with Moonshot AI, one of the leading model labs pushing the open source frontier with large-scale MoE architectures. Under this partnership, Together AI becomes a launch platform for Moonshot's model releases, starting with Kimi K3 and extending to every open weights model Moonshot ships going forward.
For developers building on open models, this means day zero access to Moonshot's frontier releases through Together AI’s US-hosted infrastructure, pricing model, and tooling, while ensuring zero data retention and compliant access to models and data. Developers can also post train these models with their own data to deliver the quality and performance for their app.
Frontier performance, open weights
Kimi K3 is the largest open model released to date: a 2.8T parameter sparse Mixture-of-Experts model with native vision support and a 1M token context window. Moonshot built it around two new architectural components:
Kimi Delta Attention (KDA)
, which changes how information flows across sequence length and delivers significantly faster decoding at long context lengths.
Attention Residuals (AttnRes)
, which improves how representations are retrieved across model depth, adding meaningful training efficiency at minimal extra compute cost.
Layered on top are a set of optimizer refinements, including per-head Muon and quantile-based expert load balancing, that Moonshot says combine to deliver roughly 2.5x better scaling efficiency compared to Kimi K2. The result is a model built for long-horizon coding, agentic workflows, game development, and knowledge-intensive tasks, with benchmark results that put it in direct competition with the leading proprietary systems on the market today.
Production Inference Platform
Kimi models are available across Together AI Inference products – including Serverless, Provisioned Throughput and Dedicated Inference. Developers can go from trying these models to applying them to their production use cases with SLA-backed products and autoscaling.
With
Provisioned Throughpu
t, teams can use reserved inference capacity for frontier open models with token-based pricing and a 99% uptime SLA. It’s the reserved-capacity guarantee developers already expect from closed-model providers, now available for open weights. No GPU-hour math, just guaranteed throughput at a predictable price. For teams looking for more control with all the benefits of a production-ready platform, they can use
Dedicated Model Inference
with fast deployment, better token economics and continuous research innovations shipped into the product.
‍
Post Training
Developers can also post train Kimi models to deliver better quality for their target use case.  With custom training, including full-weight and LoRA reinforcement learning as well as advanced supervised fine-tuning, developers can configure training through the Python SDK and granular primitives, and run multiple LoRA experiments concurrently on dedicated capacity. Custom training connects experimentation directly to production. When a checkpoint is ready to evaluate, it can be deployed natively to inference, with no separate handoff between training and serving and no rebuilding.
‍
What this partnership unlocks for developers
‍
Day zero availability:
Kimi K3 is available on Together AI with the highest model quality and performance, validated by Moonshot. Future Moonshot releases will also ship on Together at launch.
Proven scale with production-ready infrastructure:
Together AI's research-optimized inference stack is tuned for large sparse MoE models like K3, so developers get the performance the architecture promises rather than a generic deployment. Together’s inference stack already serves production traffic for companies like Cursor, Y Combinator and Decagon, deploying coding and agentic workloads at scale.
One integration, the full Moonshot lineup:
As Moonshot ships new models, they'll land in the same Together AI Models library, behind the same API you're already calling. No new SDKs, no separate account, no re-plumbing your app each time a new Kimi model drops.
Day zero post training:
Together customers can use Kimi models as their base model for fine-tuning, with the flexibility to remove the attribution required in the MIT license.
Open weights, your choice of control:
Because Kimi K3 is open-weight, you can run it serverless on Together for speed of iteration, or move to Provisioned Throughput or Dedicated Model Inference as your usage scales, without being locked into a single provider's roadmap.
‍
Join the conversation
Want to hear directly from the team behind Moonshot AI and Together AI? Join Feihu Tang from the Moonshot AI team and Jue Wang and Zain Hasan from Together AI to talk through the technical decisions behind Kimi K3, how to actually run it on Together, and what's coming next. Bring your questions.
RSVP and set a reminder for the Moonshot x Together Webinar
