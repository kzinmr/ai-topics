---
title: "Sidecars: A low-latency trust boundary for Sandboxes"
url: "https://modal.com/blog/introducing-sandbox-sidecars-trust-boundary"
fetched_at: 2026-10-02T10:01:07.355848+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Sidecars: A low-latency trust boundary for Sandboxes

Source: https://modal.com/blog/introducing-sandbox-sidecars-trust-boundary

At Modal, our customers rely on Sandboxes to execute untrusted code written by their downstream users or, almost exclusively now, by agents. Running untrusted code isn’t a new problem: every cloud provider has to do this from day 1 to isolate their platform from their user and their users from each other. Fortunately, technologies like gVisor and Firecracker “solved” “isolation” nearly eight years ago. Unfortunately for us, they solved it for an now-outdated unit of trust. How do you protect users from their “own” code?
Today we’re excited to introduce Sidecars, which are our broader answer to this problem. Sidecars are isolated containers that run alongside your main Sandbox on the same host and provide a real security boundary between trusted or untrusted code. Sidecars enable 3x faster communication across trust boundaries than using separate Sandboxes — which is particularly helpful for operation-heavy workloads.
Sandboxes are full of trusted code
Agents demand capabilities without credentials. I want an agent to check my Slack messages and apologize to my colleagues for how long it took to review what they sent me. I don’t want that agent to know my Slack password when it stumbles upon the landing page of exfiltrate-my-credentials.com instructing it to log my password.
If Sandboxes primarily exist as an execution environment for untrusted code, then you have to ask: why is there so much trusted code in Sandboxes?
This anti-pattern largely stems from how the early coding agents, like Claude Code, were designed for running on a user’s laptop and not in a remote Sandbox. The harness was never separated from its tool calls, and that design pattern survived the shift over to the cloud.
Hosting the harness and the tool calls together is a security risk. Simon Willison calls it the
lethal trifecta
: an agent with access to private data, exposure to untrusted content, and the ability to communicate externally can be tricked into leaking that data. A coding agent whose harness runs in its Sandbox has all three by default. The harness's credentials sit next to generated code, the agent can read untrusted content from the web, like packages and repos, and anything in the Sandbox can make network calls..
Today's fixes trade latency or flexibility for security
We aren’t the first to think about this problem, and we aren’t the first to propose a solution either. The popular solutions today each remove one leg of the trifecta: moving the harness out of the Sandbox removes private data, and adding advanced network egress controls restricts external communication.
Companies like
Anthropic
and
OpenAI
promote separating the agent’s harness from its tool calls, or in Anthropic’s words: the “brain” from its “hands,” and we’ve advocated for this pattern as well.
However, whether the harness runs in a control plane or a separate Sandbox, every single agent operation now takes a network call. For agents making many tool calls, the small latency associated with every call adds up. Security ends up coming at the direct cost of latency. Also, for a coding agent, the codebase itself is private data, so even when the harness is moved out, there is still a data exfiltration risk, which brings us to the second approach.
The second approach is building advanced network egress controls like
domain allowlisting
,
credential injection
, and
dynamic egress policy updates
. Sandbox providers, us included, have been shipping these quickly to solve for the most common exfiltration risks.
These solutions are ergonomic and for most customers they are very effective, but they aren’t as flexible as many customers need. For example, one of our customers, Ramp, needed to run a complex service alongside their agent that injected secrets, but also monitored external calls— off-the-shelf secret injection didn’t fully address their use case. As agents get more and more capable, new needs keep emerging faster than any provider can ship new features, and teams at the frontier need a way to build their own solutions.
A full solution to avoid either tradeoff would:
Fully separate untrusted and trusted code
Minimize latency for operation-heavy agents
Be flexible enough to adapt to programs as yet unthought of
Sidecars as a “new” isolation primitive
Sidecars are our answer for isolating trusted from untrusted code with low latency and high programmability. A Sidecar runs alongside a Sandbox while remaining isolated from it, giving trusted software a place to inject credentials, proxy traffic, redact data, run harness logic, or observe the agent without requiring every operation to cross a remote service boundary.
The pattern draws inspiration from existing designs like
Kubernetes
sidecar containers or the
Datadog Agent
: small, specialized containers that run alongside a primary application to provide supporting functionality. Sidecars apply the same idea to agent infrastructure, with the isolation needed to establish a trust boundary between the containers.
Isolation:
Sidecars are separated from the main Sandbox with the same isolation boundary as separate Sandboxes - gVisor or VMs, depending on which
runtime
you pass to `Sandbox.create()`. This means agent-generated code can run in the main Sandbox while credentials, proxies, harness logic, or other trusted operations run in a Sidecar that the agent cannot directly access.
Latency:
Because the containers run on the same host, communication between them stays local. The main Sandbox and its Sidecars are connected through an
internal bridge network over TCP/UDP
, and each container is reachable by name. A tool call that would otherwise travel from a Sandbox to a remote control plane can instead be handled by a Sidecar running next to it, avoiding the network round trips that add up in execution-heavy agent loops. Our internal benchmarking shows that communication between a Sandbox and its Sidecars is at least 3x faster than between separate Sandboxes in the same region.
Sidecar
Separate Sandbox (HTTPS)
Travel per call, p50
0.58ms
2.6ms
Travel per call, p99
1.4ms
44ms
100 calls, total time
0.6s
1.2s
Creation:
Sidecars are created dynamically through the Modal SDK, so you can spin up the trusted services you need at runtime rather than defining a fixed topology in advance. Code running inside the Sandbox can't create or modify them.
Resources:
Sandboxes and Sidecars
share CPU and memory resources
, which makes using Sidecars more cost-efficient than running processes across multiple Sandboxes. A single Sandbox can run up to 250 Sidecars.
Network policy
: Each Sidecar has its own outbound network policy, independent of the main Sandbox, and you can
force the Sandbox's outbound traffic through a proxy Sidecar
.
Lifecycle
: Sidecars can be terminated and replaced at any point in the Sandbox's lifetime, and their filesystem can be snapshotted and used to start another Sandbox or Sidecar from. Terminating the Sandbox stops all of its Sidecars.
Sidecars in action: Building custom egress proxies at Ramp
Ramp's background coding agent,
Inspect
, writes over 75% of all merged pull requests at Ramp, with every session running in its own Modal Sandbox. Ramp built their own custom egress proxy on top of Sidecars, running next to each Inspect Sandbox to monitor and control the agent's outbound traffic.
“We need to know exactly what our coding agent is reaching out to, and be able to stop it when it's accessing something it shouldn't. Sidecars let us run our own egress proxy, with our own rules, right next to the agent. We can force outbound traffic through the proxy, so nothing bypasses it, and because it's on the same host, that doesn't cost us an extra network hop.” - Zach Bruggeman, Principal Software Engineer, Ramp
Getting started
Sidecars are available in Beta today, with additional details on how to get started and known limitations in our
docs
.
We’ve intentionally designed Sidecars to be a flexible building block, but to get you started we’ve also written examples for some specific use cases:
However, we expect the most interesting use cases to be the ones we haven’t thought of yet. So if you build something with Sidecars, we’d love to hear about it!
