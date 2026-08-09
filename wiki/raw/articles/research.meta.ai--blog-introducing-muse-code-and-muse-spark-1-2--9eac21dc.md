---
title: "Introducing Muse Code and Muse Spark 1.2"
url: "https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2"
fetched_at: 2026-08-09T10:13:07.403457+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Introducing Muse Code and Muse Spark 1.2

Source: https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2

We're excited to release Muse Code (beta), a terminal coding agent powered by Muse Spark 1.2, our newest model. This marks our next step toward the frontier, with larger and much more capable models on the way.
Install Muse Code on macOS or Linux:
curl
-fsSL
https://dev.meta.ai/install.sh
|
bash
Copy installation command
Muse Code takes on complex software engineering tasks across large repositories: planning changes, writing code, and validating the results. It can coordinate multiple persistent subagents for each task, solving difficult problems faster, more accurately, and with less intervention.
Muse Code
Async Background Agents
Muse Code operates with a simple agent loop plus a set of async background agents to enhance the main agent's capability. These specialized background agents remain active throughout each session, rather than being spawned for individual tasks, helping avoid redundant information gathering. They carry out next steps and choose when to communicate back to the main agent. Their persistence reduces latency and the need for steering on difficult, multi-step tasks.
Photon Sphere
Embervault
Avo Lawn
Runtime Design
Muse Code uses a local event log in which every model call, tool run, approval, and edit is appended. This single source of truth makes the runtime replay-exact and restart-safe: after a crash, the agent can resume precisely where it stopped. That ability lets Muse Code take on long-running tasks without being derailed by failures.
Bundled Skills
Muse Code ships with several default skills.
/plan
turns a task into an approval-gated plan,
/grill
stress-tests that plan until it holds up, and
/goal
works toward successful completion of the specified objective.
The user inputs a fly-through video of a home into the terminal as an mp4 file. Muse Code
interprets the video and produces a visually rich vacation home marketing and booking page.
Muse Spark 1.2
Muse Spark 1.2 is a coding-focused update to Muse Spark 1.1, with improvements in code generation, complex debugging, codebase understanding, and end-to-end developer workflows. In Muse Spark 1.2, we significantly scaled up training compute on coding tasks while expanding training environment diversity. The model also maintains its strength in other key areas like general agents.
For more details about our evaluations, see
our report
.
Co-Training With Muse Code
We co-trained Muse Spark 1.2 with Muse Code to ensure the model exhibits its best performance and coding usability when paired together. The training included rejection sampled harness trajectories and recipe optimizations for goals, compaction, and subagents, alongside the integration of the Muse Code toolset to maximize harness compatibility.
Long-Horizon
Muse Spark 1.2 was extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research. It leverages planning to sequence work, goal conditioning to maintain direction, and context compaction to retain the knowledge needed to sustain progress.
Self-Improvement
We also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates. The model then graded candidate solutions on how well they satisfied those requirements, producing a scalable training dataset for Muse Spark 1.2. This self-improvement loop helped Muse Spark 1.2 follow complex instructions more precisely than its predecessor.
Case Study: Kernel Optimization
We tested the model's ability to iteratively optimize GPU kernels over 1,000+ tool calls (up to 24 hours). Leveraging Muse Code's agentic coding environment, the model writes, compiles, profiles, and progressively improves kernel performance relative to a provided baseline implementation. We benchmarked on KDA and MLA kernels for NVIDIA Hopper GPUs. The agent continues to achieve substantial improvements over the provided baseline implementation.
The baseline is the FLA Triton implementation of KDA. Models were prohibited from importing third-party kernel libraries such as FLA directly; instead, they had to apply specialized kernel-optimization knowledge to implement the algorithm in Triton, rather than wrap existing implementations. Muse Spark 1.2 paired a chunk-parallel preparation kernel with a sequential inter-chunk scan, combining standard fusion and tiling with KDA-specific optimizations such as re-centering the gated cumulative decay at the chunk midpoint.
We benchmark against a PyTorch reference implementation at batch size 1, number of heads 64, sequence length 8192, and latent dimension 512. Muse Spark 1.2 designed a two-kernel Triton pipeline for this workload, combining kernel fusion and tiling with MLA-specific optimizations such as reusing the shared KV latent as both K and V.
Availability
Muse Spark 1.2 is available today in Muse Code and in Meta Model API with expanded global access. We have a lot on the horizon, including new harness features and more powerful models. We can’t wait to see what you build!
Get started with Muse Code
