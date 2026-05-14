---
title: "Hermes Unlocks Self-Improving AI Agents, Powered by NVIDIA RTX PCs and DGX Spark"
source: https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/
date_published: 2026-05-13
author: Abhishek Gore
publication: NVIDIA Blog
series: RTX AI Garage
type: blog_post
ingested: 2026-05-14
---

# Hermes Unlocks Self-Improving AI Agents, Powered by NVIDIA RTX PCs and DGX Spark

Reliable, self-evolving and powered by the newest agentic large language models, Hermes brings a new class of agents to NVIDIA RTX PCs and workstations.

May 13, 2026 by Abhishek Gore

Agentic AI is changing the way users get work done. Following the success of OpenClaw, the community is embracing new open source agentic frameworks. The latest is Hermes Agent, which crossed 140,000 GitHub stars in under three months and, as of last week, is the most used agent in the world according to OpenRouter.

Developed by Nous Research, Hermes is designed for reliability and self-improvement — two qualities that have historically been hard to achieve with agents. It's provider- and model-agnostic by design, and optimized for always-on local use, making NVIDIA RTX PCs, NVIDIA RTX PRO workstations and NVIDIA DGX Spark the ideal hardware to run it at full speed, around the clock.

Qwen 3.6, a new series of high-performance, open weight large language models (LLMs) from Alibaba, are ideal for running local agents like Hermes. The Qwen 3.6 27B and 35B parameter models are outperforming their previous-generation 120B and 400B parameter model counterparts and run on NVIDIA RTX and DGX Spark for accelerated agentic AI.

## Hermes: Local AI Agent Capabilities Accelerated

Like other popular agents, Hermes integrates with messaging apps, can access local files and applications, and runs 24/7. But four standout capabilities set it apart:

1. **Self-Evolving Skills**: Hermes writes and refines its own skills. Every time the agent encounters a complex task or receives feedback, it saves its learnings as a skill so it can adapt and improve over time.
2. **Contained Sub-Agents**: Hermes treats sub-agents as short-lived, isolated workers dedicated to a sub-task — with a focused context and set of tools. This keeps task organization tidy, minimizes confusion for the agent and allows Hermes to run with smaller context windows, which is ideal for local models.
3. **Reliability by design**: Nous Research curates and stress-tests every skill, tool and plug-in that ships with Hermes. The result: Hermes just works — even with 30 billion-parameter-class local models — without the constant debugging that most other agent frameworks require.
4. **Same model, better results**: Developer comparisons using identical models across frameworks consistently show stronger results in Hermes. The difference is the framework: Hermes is an active orchestration layer, not a thin wrapper, enabling persistent, on-device agents instead of task-by-task execution.

Both the Hermes agent and the underlying LLM are built to run locally — which means the quality of hardware directly determines the quality of a user's experience. NVIDIA RTX GPUs are purpose-built for this kind of workload.

## Qwen 3.6: Data Center-Level Intelligence, Locally

The latest Qwen 3.6 models build on the acclaimed Qwen 3.5 series to deliver another leap forward for local AI agents. The new Qwen 3.6 35B model runs on roughly 20GB of memory while surpassing 120 billion-parameter models, which require 70GB+ of memory.

In addition, Qwen 3.6 27B is a new, dense model with more active parameters — matching the accuracy of 400 billion-parameter models like Qwen 3.5 397B while being one-sixteenth the size. Running on high-end RTX GPUs provides the model the computing power it needs for a speedy experience.

These models are ideal for local agents like Hermes, and NVIDIA GPUs and DGX Spark are the fastest way to run them. NVIDIA Tensor Cores accelerate AI inference to deliver higher throughput and lower latency — so Hermes can work through a multistep task or refine one of its own skills in seconds rather than minutes.

## DGX Spark: The Always-On Agentic Computer

Agents like Hermes are built to run continuously — responding to requests, planning multistep tasks, executing autonomously and self-improving. NVIDIA DGX Spark is the ideal companion — a compact, efficient standalone machine built for sustained, all-day agentic workflows.

With 128GB of unified memory and 1 petaflop of AI performance, NVIDIA DGX Spark can run 120 billion-parameter mixture-of-experts models all day. And the new Qwen 3.6 35B model delivers equivalent intelligence in a leaner footprint — running faster and giving users the capacity to run concurrent workloads.

To maximize performance and ease of use, read the Hermes DGX Spark playbook. Plus, register for upcoming hands-on sessions in NVIDIA's "Build It Yourself" agentic AI series to learn how to build autonomous AI agents with NemoClaw and OpenShell.

NVIDIA DGX Spark is available to order from NVIDIA's manufacturing partners — visit the marketplace.

## Getting Started With Hermes on NVIDIA Hardware

Running Hermes locally on NVIDIA hardware is straightforward. Visit the Hermes GitHub repository to get started, and pair it with a preferred local model and runtime. Run Hermes alongside Qwen 3.6 via llama.cpp, LM Studio or Ollama. Hermes Agent ships with LM Studio and Ollama support out of the box for the simplest path to a local agent.

Whether for a local AI enthusiast exploring the frontier of personal agents or a developer building local tooling for their workflows, Hermes on NVIDIA hardware offers a uniquely capable and reliable foundation.

## #ICYMI: The Latest From RTX AI Garage

- **NVIDIA RTX PRO GPUs** deliver up to 3x faster token generation running Qwen 3.6 models with llama.cpp.
- **Google's Gemma 4 26B and 31B** models now available as NVFP4 checkpoints for faster performance on NVIDIA Blackwell GPUs. Pair with Multi-Token Prediction drafters for up to 3x faster inference.
- **Mistral Medium version 3.5** released in April with llama.cpp and Ollama compatibility for RTX PRO and DGX Spark.
- **NVIDIA NemoClaw** open source stack optimizes OpenClaw experiences on NVIDIA devices with increased security and local model support. Now supports WSL2.
