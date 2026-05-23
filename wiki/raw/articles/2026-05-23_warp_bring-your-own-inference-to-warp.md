---
title: "Bring your own inference to Warp"
source: "Warp Blog"
url: "https://www.warp.dev/blog/bring-your-own-inference-to-warp"
scraped: "2026-05-23T06:00:40.300749+00:00"
lastmod: "2026-05-22T17:27:59.000Z"
type: "sitemap"
---

# Bring your own inference to Warp

**Source**: [https://www.warp.dev/blog/bring-your-own-inference-to-warp](https://www.warp.dev/blog/bring-your-own-inference-to-warp)

Product
Bring your own inference to Warp
Zach Lloyd
May 20, 2026
Today we’re releasing one of the most requested updates from the Warp community: more control over inference.
Developers want to choose their own models, use their own provider accounts, control inference costs, and experiment with new providers without leaving Warp. Starting today, we’re making two updates that make Warp more flexible:
BYOK is now available on the Free plan.
Warp now supports custom inference endpoints compatible with the OpenAI Chat Completions API.
You can now power Warp’s agent experience with your own OpenAI, Anthropic, or Google API key, or connect Warp to an OpenAI-compatible endpoint such as OpenRouter, LiteLLM, z.ai, an internal gateway, or your own hosted inference setup.
Why now
We recently
open-sourced the Warp client
because we want Warp to become more open, customizable, and shaped by how developers actually work. Bringing your own inference to power the Warp Agent is a part of that.
The Warp Agent will still be the best and simplest way to use AI in Warp. It is built directly into the ADE, so it can use your terminal state, indexed codebase, rules, notebooks, workflows, env vars, and MCP servers without extra setup. It also works natively with Warp’s code review, agent management, and Oz cloud platform.
At the same time, the model layer should be more flexible. Developers should be able to use Warp Agent with the inference setup that works best for them: providers or models Warp does not support natively yet, specific model configurations, custom routing behavior, provider settings, internal gateways, or existing credits and commitments with model providers.
Warp should provide the integrated agentic development experience. Developers should be able to choose the inference behind it.
What’s available today
BYOK has been available on Warp’s paid plans, and we’re now making it available on the Free plan as well. Free users can add their own API key for supported providers, including OpenAI, Anthropic, and Google, and use it to power Warp’s agent experience. BYOK on Free is login-gated, but free for individual users.
Warp also now supports custom inference endpoints compatible with the OpenAI Chat Completions API. You can use this to connect Warp to a model router, gateway, hosted provider, internal endpoint, or self-hosted inference setup.
A custom inference endpoint can be useful if you want to:
use a model provider Warp does not support natively yet
route requests through a model router or gateway
experiment with your own hosted or self-hosted inference setup
We expect developers and teams to use this in a lot of different ways, and we’re excited to see what people connect.
How pricing works
For individual developers and small teams, BYOK and custom inference endpoint usage are free in Warp. Whether you are on Free, Build, or Max, Warp will not charge Warp credits when you bring your own API key or connect your own compatible inference endpoint, as long as the usage is for an individual or a company with 10 people or fewer.
For many developers, Warp’s bundled inference will still be the simplest option. Warp includes access to major models from providers like OpenAI, Anthropic, and Google, as well as top-tier open source models, in a single plan with no setup required. We also handle provider relationships, model availability, routing, and ZDR guarantees with our contracted model providers. Because Warp benefits from volume discounts with model providers, Warp credits can still be a convenient and cost-effective way to use frontier models without managing separate provider accounts, API keys, billing, or endpoint configuration.
BYOK and custom endpoints are for developers who want control over inference, including the ability to experiment with providers and models Warp does not natively support yet. Bundled inference is for developers who want Warp to handle model access and infrastructure for them.
For companies with more than 10 people, BYOK and custom endpoint usage needs to go through Warp’s Business or Enterprise plans. Larger teams use Warp’s managed harness as part of a broader platform offering: tool orchestration, context management, team usage visibility, admin controls, governance, security policies, and the infrastructure needed to deploy AI agents across an organization.
For Business and Enterprise customers, bringing your own inference will consume platform credits. These credits are based on the time agents are actively doing work on Warp’s managed systems, not the cost of the underlying model inference. Since the customer is providing the model provider, API key, or endpoint, BYOK and custom endpoint usage will consume Warp credits at a significantly lower rate than usage where Warp also provides the underlying model inference.
What’s next
Longer term, developers and teams will not use one model, one provider, or one harness. They will use different setups depending on the task, cost, latency, security requirements, and execution environment. Warp should be the best interface for that world.
Next, we’re planning to add a lightweight Rust client harness to our
open-source repo
, so Warp can connect directly to local models without routing through Warp’s servers. We also plan to support
Agent Client Protocol
, so developers can bring other agent harnesses into Warp’s terminal UI. These paths will be fully client-side and will not require login.
This is consistent with the direction we described when we open-sourced the Warp client: we want Warp to be more open, more customizable, and shaped by how developers actually want to work, while still keeping the product coherent and sustainable.
To get started, open Warp and go to Settings → AI to add your API key or configure a custom inference endpoint.
Try it out and let us know what providers, endpoints, local model setups, and agent harnesses you want Warp to support next. We’d love your feedback.
Related articles
May 19, 2026  ·  6 min
A single pane of glass for managing all of your cloud agents
With Oz, engineering teams can now integrate, orchestrate, control, and improve any cloud agent at scale including Claude Code, Codex, Warp Agent, and whatever comes next.
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
