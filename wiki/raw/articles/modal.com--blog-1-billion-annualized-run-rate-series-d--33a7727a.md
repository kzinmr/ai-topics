---
title: "Modal crosses $1B in Annualized Run Rate and raises $750M Series D"
url: "https://modal.com/blog/1-billion-annualized-run-rate-series-d"
fetched_at: 2026-10-15T10:01:37.297034+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Modal crosses $1B in Annualized Run Rate and raises $750M Series D

Source: https://modal.com/blog/1-billion-annualized-run-rate-series-d

Just five months ago, when we announced our Series C, I wrote that
demand was accelerating
. Since then, usage has tripled and we’ve grown more than 15x year-over-year. We recently crossed $1B in annualized run rate with no sign of slowing down.
Software can do things that were impossible just a few years ago
It’s clear that AI has unlocked a whole new set of software capabilities. So many incredible applications exist now that couldn’t have been built before. The old stack doesn’t quite fit them. They need different building blocks and a new way to think about infrastructure.
We’re powering a ton of these applications. Among them is TypeSafe AI’s Jev, one of the fastest-growing products ever. It served
1T tokens on Modal
in its first three days, and the TypeSafe team stayed focused on shipping instead of managing infrastructure.
And it’s happening in many different verticals
DoorDash’s AI platform team uses Modal to get apps across the company from experiment to production. Cognition, Ramp, Linear, and Hebbia are building background agents that are experts in their fields. Runway is generating life-like video, in every region of the world. Physical Intelligence, Generalist AI, and 1X are training robots. Chai Discovery and Achira run drug discovery on Modal, as do scientists working through
Claude Science
.
Every shift needs new infrastructure
Every shift in software changes both what people can build and the infrastructure they need to build it. I've been writing software since the early nineties, and this isn't the first step-change: we've had the web, the cloud, big data, mobile, and several other shifts.
When the cloud started, suddenly you had to deal with distributed systems, sharding, and config management. None of our original tools were built for it, so developers created new ones: Docker, Kubernetes, Terraform, etc.
The friction with AI is pretty clear by now. GPUs are scarce, and models are quite large and slow to load. LLMs write code now! And it has to run somewhere, isolated from everything else. Sure, you can build for all of those considerations on the old stack, and plenty of people have, but you end up in YAML hell and GPU procurement purgatory.
So we went deep. We threw out most of the existing stack and built our own file system, container runtime, scheduler, and networking from the ground up, on a capacity pool that now spans 20+ clouds.
What developers need is better building blocks
The beauty of software is composability. If you have the right building blocks — general-purpose, battle-tested, and scalable — there’s infinite combinations of things you can build.
Functions were our first building block: you write code, and Modal runs it. This turned out to be incredibly useful, especially for Gen AI: image generation with diffusion models, music at Suno, LLM inference with SGLang and vLLM, and model training.
We launched Sandboxes in 2023 when we noticed that people were using LLMs to generate code. Sandboxes exploded and three years later, it’s a $300M run rate product just on its own. Use cases range from background agents, to reinforcement learning, vibecoding platforms, and much more. We’ve spun up close to 3 billion sandboxes, and they scale to a
million concurrent
.
We’re launching a lot more
A new world of software capabilities requires a new set of building blocks and we’re just getting started.
We recently launched
multi-node training
– one decorator gives you a fully RDMA-connected cluster with no capacity commitment. We’re moving up the stack and launching a number of products in RL and post-training as well.
On the inference side, we’ve been launching
Modal servers
, which is a better solution for HTTP servers, as well as some really cool features around LLM serving, such as
Endpoint Candidates
.
With Sandboxes,
virtual machines
are now generally available.
These are just a few of the many more developments to come.
We’ve raised more capital
When we started Modal five years ago, I couldn't have imagined most of the applications running on it today. It's just as difficult to imagine the software people will be creating two years from now, but what I do know is that it's going to require an entirely new set of building blocks. We want a lot of it to run on Modal.
To keep building what's next, we’ve raised a $750M Series D at a $15.75B post-money valuation. Accel led the round. Kleiner Perkins joined, and all of our existing investors participated, including Menlo Ventures, General Catalyst, Redpoint, Lux Capital, Amplify Partners, and Bain Capital Ventures.
I'm obviously biased, but I can't think of a better time to be building software.
If you’re interested in joining our team of 200+ across NY, SF, and Stockholm, check out our
open roles
.
