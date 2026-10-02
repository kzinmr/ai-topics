---
title: "Runtime Roundup: VM Sandboxes, Multi-node clusters, and more"
url: "https://modal.com/blog/runtime-product-update-sandbox-endpoints"
fetched_at: 2026-10-02T10:01:07.203992+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Runtime Roundup: VM Sandboxes, Multi-node clusters, and more

Source: https://modal.com/blog/runtime-product-update-sandbox-endpoints

Modal just hosted our inaugural conference,
Runtime
. Here are a few of the highlights that we announced.
VM Sandboxes
VM Sandboxes give your agent access to a full Linux computer. Agents increasingly want to live inside something that looks like a real machine: running Docker stacks, local databases and dev servers, graphical environments and mobile simulators, and even monkeying around with the Linux Kernel itself.
VM Sandboxes are already in use at customers like Linear, Legora, and Snorkel powering coding agents and evals.
Learn more
Sandbox Sidecars
Sidecars are containers that run alongside your main Sandbox on the same host, but with the same isolation as separate sandboxes. This means agent-generated code can run in the main Sandbox while credentials, proxies, harness logic, or other trusted operations run in a Sidecar that the agent cannot directly access. Because the containers share a host, communication between them stays local, avoiding the network round trips that add up in execution-heavy agent loops.
Learn more
Modal Clusters
For the past 1.5 years, we've been battle-testing a new primitive: multi-node clusters. They’re now generally available through a single decorator,
@modal.clustered
. Modal Clusters support jobs that run across several coordinated containers, such as serving or training trillion-parameter models.
Modal Clusters are already powering post-training at Decagon, pre-training at 1x, and real-time inference at Runway.
Learn more
Sticky Sessions
Sticky Sessions allow you to keep a client’s interactions attached to the same running Modal container, so your application can maintain state across requests. By passing a session token with your application requests, you can guarantee routing back to the same container you started on–giving your end users a seamless reconnect experience.
For real-time use cases like serving voice models, fast container routing is critical.
Learn more
Endpoint Candidates
Endpoint Candidates help you optimize your inference servers on Modal. Mirror your production traffic to an alternative serving recipe, then compare quality, latency, throughput, and cost. You can stage multiple endpoint candidates, then benchmark to decide whether to promote to production.
Endpoint candidates to select customers in private beta, and will become generally available soon. Follow the
Modal Changelog
to learn more.
