---
title: "How Abundant designed efficient rollout architecture with Modal Sandboxes"
url: "https://modal.com/blog/abundant-efficient-rollout-architecture-with-modal-sandboxes"
fetched_at: 2026-11-20T10:01:15.389228+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# How Abundant designed efficient rollout architecture with Modal Sandboxes

Source: https://modal.com/blog/abundant-efficient-rollout-architecture-with-modal-sandboxes

Abundant
builds reinforcement learning environments that frontier labs like OpenAI, Anthropic, Google, and Meta use to train and evaluate their models. Labs improve agent capability by giving them difficult tasks that Abundant designs, letting the model attempt it, and grading the result as pass or fail.
Each task is an RL rollout with a full environment. The model needs instructions, a defined goal, and a verifier to decide whether the task was completed. But it also needs infrastructure: compute to power the run, Dockerfiles, and isolation. Depending on the task, an agent may even need accelerators like GPUs.
Abundant has created over 75,000 rollouts — ranging from GPU kernel optimization to long-horizon coding — each of which runs in a Modal Sandbox. Modal makes their rollout infrastructure easy to build and cost-efficient to run, enabling the Abundant team to focus on their core business.
Building a rollout platform on Modal
Today, almost all of Abundant’s rollout platform runs on Modal. Modal Functions power Abundant’s scheduler API to start tasks, clean up dead runs, and review rollouts. Modal Sandboxes power the rollout environments.
Expand image
Close
Abundant initially chose to evaluate Sandbox providers because they wanted to avoid managing EC2 clusters directly, which would pull engineering time away from their core business of building RL environments. Modal enabled them to build their infrastructure directly in code, launch Sandboxes easily via API, and elastically scale their traffic as business grew. As of November 2026, Abundant runs over two million Sandboxes per month.
“Modal lets us focus on our core business without worrying about whether our infrastructure will work. We’re able to work in code and scale our traffic based on customer demands in a given moment.”
Kyle van den Bergh
Member of Technical Staff, Abundant
Designing efficient and reliable architecture with Modal’s team
Modal worked with the Abundant team to design and build their rollout architecture, focusing on designing a system that didn’t leave Abundant having to pay heavily for idle compute.
Each rollout has a few steps: launch the task, attempt the task, verify the work, and report the work. Throughout the rollout, a “monitor” needs to verify that the Sandbox is still active.
Expand image
Close
While Abundant had considered hosting the monitor outside of the Sandbox, they ultimately chose to include the rollout monitor inside the Sandbox and then used short-lived Modal Functions to start Sandboxes.
The small rollout monitor inside the Sandbox makes periodic HTTP calls: a heartbeat every 30 seconds, live events, and the final result. If a Sandbox goes quiet, the control plane will attempt to connect three times before terminating it.
Lowering resource requests with CPU and memory bursting
Abundant also needed to solve for Sandboxes that didn’t consume CPU and memory resources at consistent rates. The Modal team surfaced this opportunity directly, sharing that Abundant could lower their CPU and memory resource requests by utilizing “bursting,” a unique feature to Modal where Sandboxes automatically size up (and back down) when they need additional resources.
Bursting means that if a Sandbox needs more resources than it originally requested, it can use those resources if there’s room on the machine. With bursting, Sandboxes that would otherwise be throttled by CPU restrictions or hit OOM errors are able to keep working. While most fixed-resourcing models mean that teams have to provision sandboxes for their peak consumption, bursting means that teams can request for average usage while still accommodating peaks.
By lowering the resource request and utilizing bursting, the Abundant team was able to reduce the amount of idle compute they were paying for. It also simplified the decision of how much compute to allocate to specific Sandboxes. Because of the wide range of tasks that Abundant was designing, individually deciding how much CPU and memory to allocate was tedious, and the risk of losing progress to OOMs was potentially costly.
Designing verifiers
A verifier that is hard to reward-hack makes a model more capable because the models can’t cheat at the task. Creating strong verifiers therefore includes work before the rollout ships to test the task with adversarial agents.
In early tests, Abundant discovered that models were occasionally finding copies of their task instructions, which created evaluation awareness and skewed results. When running benchmarks, it’s crucial that agents think they’re in the real world completing the job organically, with the same environment and information they’d see in production.
To correct this, Abundant changed how runs are started, ensuring that all instructions are deleted before work is completed. They also created a reviewer agent that ran as part of the verification step, reviewing agent traces and flagging if the agent showed signs of evaluation awareness.
The results
The rollout architecture took the Abundant team around two weeks total to implement. Cost-efficient and reliable rollouts gave Abundant time to focus on what they actually care about: making sure task verification is high quality and helping AI labs test and improve models.
For example, the team released a benchmark
Frontier RSI
, which tests an agent’s ability to improve itself. Modal powered over 1,300 hours of agent-research time over nearly 500 agent trials to build the initial published results.
“Our rollout infrastructure sits behind our first public benchmark, Frontier RSI, which tests state of the art language models and their ability to improve themself. Modal helped us run over 1,300 hours of agent research time efficiently, reliably, and easily. Because of Modal, we can focus on the data and designing open-ended, multi-step, difficult tasks to make agents better.”
Kyle van den Bergh
Member of Technical Staff, Abundant
