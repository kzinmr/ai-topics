---
title: "Product updates: Sandbox Sidecars, new models, a refreshed dashboard, and more"
url: "https://modal.com/blog/product-updates-sidecars-models-dashboard"
fetched_at: 2026-09-16T10:01:35.075040+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Product updates: Sandbox Sidecars, new models, a refreshed dashboard, and more

Source: https://modal.com/blog/product-updates-sidecars-models-dashboard

August brought new model support, faster Function calls, and major improvements across Modal Sandboxes. Here are the highlights.
🤖 Day-zero support for Kimi K3, Qwen 3.8, GLM 5.3, and GLM 5.3 Flash
Explore four frontier open-weight models now supported on Modal Auto Endpoints.
All four are supported as Shared Endpoints with
token-based pricing
, or as Dedicated Endpoints
billed by the GPU second
.
Kimi K3:
Moonshot’s 2.8T-parameter multimodal model with native vision and a 1M-token context window. We partnered with Moonshot and vLLM on day-zero support, with a custom DFlash speculator delivering 460 tokens per second on agentic workloads.
Qwen3.8-2.4T-A95B:
Qwen’s 2.4T-parameter, text-only Mixture-of-Experts model activates 95B parameters per token and is built for coding, research, and long-horizon agentic tasks. We delivered day-zero support with SGLang and a custom DFlash speculator.
GLM-5.3:
Z.ai
’s 753B-parameter Mixture-of-Experts model activates 40B parameters per token and supports a 1M-token context window. It is built for complex coding and long-horizon agentic tasks.
GLM-5.3-Flash:
Z.ai
’s natively multimodal 320B-parameter Mixture-of-Experts model activates 18B parameters per token and supports a 1M-token context window, bringing visual understanding to coding and agentic workflows.
Create a Dedicated Endpoint or use a Shared Endpoint →
💸 Improving control over spend
Two updates for better usage control:
Environment-level budgets
are now available for all Team and Enterprise workspaces. Owners and Managers can set a compute-usage budget per Environment and track current-cycle compute usage against it — useful for giving teams their own guardrails without splitting workspaces.
Read the docs
.
The usage limits UI got a refresh.
Threshold billing and usage limits are now presented with consistent terminology and numbers that add up at a glance, so it's clearer what your limits are and how to adjust them.
🌎 Lower pricing for broad region selection
The pricing multiplier for broad region selection has dropped from 1.5x to 1.15x. Broad regions—including the US, EU, and APAC—keep workloads closer to users or data while preserving a larger capacity pool for better availability and faster scheduling.
Read our guide to region selection →
🔒 Private Environments with default roles
You can now set a default Role for a Restricted Environment. Set the default to No Access and explicitly grant Viewer or Contributor access to the Members who need it; everyone else can't discover or access the Environment at all. Workspace Owners and Managers retain Contributor access. This effectively gives you private Environments for sensitive projects within a shared workspace.
Read the docs →
🌓 A refreshed dashboard has landed
We’ve updated the dashboard with improved navigation, a new color system for visualizations, and a light mode appearance option. Light mode is available in beta for all users, with other changes rolling out gradually over the coming days.
🧩 Sandbox Sidecars enter public alpha
Sandbox Sidecars are now in public alpha. Sidecars run additional containers beside a main Sandbox on the same host, connected through a low-latency internal network. They are useful for
custom network proxies
, multi-container workloads, and separating an agent harness from its tool execution.
Explore Sandbox Sidecars →
📊 Better observability for Sandbox CPU and memory requests
We've shipped a set of graphs to make it easier to specify Sandbox CPU and memory requests, helping you avoid OOMs or CPU contention without paying for more resources than you need. These charts show various percentiles of how much CPU and memory the Sandboxes in each of your Apps consume, so you can set request sizes accordingly.
Learn more
.
🔲 VM Sandboxes now in public beta
VM Sandboxes have entered public beta. They run a real Linux kernel, so they can support workloads that run Docker containers within the Sandbox, or that require Linux features like eBPF, systemd, cgroups, or custom filesystem mounts. This generally also leads to better filesystem performance for I/O-sensitive workloads.
Check out our docs
to get started.
📦 Now GA: Sandbox directory snapshots and new Sandbox filesystem API
Sandbox directory snapshots let you snapshot selected directories instead of an entire container filesystem. You can use them to update system dependencies separately from application code, speed up resumptions of previous sessions, and restore application state into a warm pool of Sandboxes.
Read the docs
for more.
Additionally, our new Sandbox filesystem API is now GA. The new filesystem API offers improved reliability and better performance for small files.
Learn more.
🌐 Regional Proxies
You can now choose a region when creating a Modal Proxy in workspace settings. Proxies provide static outbound IPs for Functions and Sandboxes, letting you connect to resources protected by IP allowlists. Placing a Proxy closer to those resources gives you more control over where traffic is routed and can reduce network latency.
Read the docs →
💻 SDK updates
We’ve released version 1.5.5 of the Python SDK and version 0.10.0 of the JavaScript and Go SDKs. Updates across these releases include new log APIs, faster Sandbox filesystem writes in JS and Go, and improved autoscaler configuration reporting.
Read the changelogs:
Python
·
JavaScript
·
Go
📚 More from Modal
📈 Scaling to 1 million concurrent Sandboxes in seconds
We rebuilt our scheduling system to support millions of concurrent Sandboxes and tens of thousands of creations per second. In testing, we started one million Sandboxes in under a minute while keeping median time to interactivity below half a second.
Read the blog →
⚡ Bringing serverless functions closer to the speed of wire
We rebuilt the Function I/O path around a faster, geographically distributed routing layer, moving non-critical work off the hot path and minimizing shared-storage access. The result is ~80ms lower p50 latency, with additional savings possible.
Read the blog →
🌓 Kimi K3 by Moonshot available on Modal
We partnered with Moonshot and vLLM to bring day-zero Kimi K3 support to Modal, pairing the 2.8T-parameter multimodal model with a custom-trained DFlash speculator. On agentic workloads, our speculator increases interactivity from 100 to 460 tokens per second and per-GPU throughput from 800,000 to 1.5 million tokens per minute.
Read the blog →
📸 How Botika runs full-stack generative AI on Modal
Modal supports Botika’s entire AI stack, from processing a 100-terabyte image dataset to training foundation models and serving roughly 15 models in production. With Modal, its infrastructure can absorb a two- to threefold traffic increase in seconds without manual intervention.
Read the blog →
🤖 Run Devin Outposts and Cursor Cloud Agents on Modal
You can now run Devin Outposts and Cursor Cloud Agent workers inside customizable Modal Sandboxes. Bring your own images, dependencies, secrets, and CPU or GPU resources while we handle isolated environments, fast startup, and elastic capacity for every session.
Read about Devin Outposts →
Run Cursor Cloud Agents →
⚡ Runtime: a conference by Modal
Join us October 1st at The Midway in San Francisco for Runtime, our conference for engineers running AI in production. We’ll have three tracks covering inference, training, and agents, with technical deep dives and speakers including Scott Wu (Cognition), Bryan Catanzaro (NVIDIA), and Cat Wu (Anthropic).
Explore the lineup and apply to attend →
📍Upcoming events
See all upcoming events on
Modal’s calendar
.
