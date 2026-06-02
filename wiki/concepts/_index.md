---
title: "Concepts"
tags:
  - training
  - concept
  - ai-agents
  - model
  - local-llm
  - prompting
  - rag
  - evaluation
  - inference
created: 2026-04-24
updated: 2026-05-26
---

# Concepts

AI and LLM concept pages organized by topic.

## Overview

## AI Agent Architecture Patterns

- [[concepts/functional-core-imperative-shell]] — Architecture pattern separating deterministic, pure-functional processing (core) from side-effect-heavy decision making (shell). In AI agents, the functional core handles mechanical, verifiable tasks while the imperative shell manages validation, evaluation, and strategic decision-making.
- [[concepts/reasoning-compression]] — The principle that software complexity and reasoning requirements will be compressed over time as models improve, eliminating the need for extensive exploration and reducing the imperative shell to validation/evaluation only.
- [[concepts/agent-serverless]] — Serverless deployment pattern for AI agents — managed environments with built-in SaaS integration, permissions, and security. Includes enterprise tiers with persistent logs, audit trails, and turnkey agent infrastructure.
- [[concepts/agent-iam]] — Agent IAM / Non-Human Identity Security for managing permissions and access control for AI agents interacting with enterprise systems.
- [[concepts/automation-series]] — 10-part series by Antoine Buteau on automation architecture: three kinds of work (deterministic/probabilistic/accountable), bounded agents, the automation boundary (code vs model vs human), HITL as design pattern, state/idempotency/queues, observability/replay, failure modes/blast radius, and an architecture worksheet.
- [[concepts/bitter-lesson-harnessing]] — How model intelligence evolution affects the importance of harness engineering — as models get smarter, harness complexity becomes less critical.
- [[concepts/generative-app-evolution]] — Generative App Evolution pattern: UI → Stateless App → Stateful App progression in AI-driven applications.
- [[concepts/information-theory-and-agent-communication]] — Reinterpretation of Shannon's (1948) Mathematical Theory of Communication from the perspective of AI inter-agent communication. Integration with V-Information (Xu et al., 2020) yields a 3-layer model of agent communication. Information-theoretic foundations of the harness effect, context window as Shannon capacity analogue.

## Harness-Engineering

- [[concepts/harness-engineering/agentic-engineering-patterns]] — A guide project started by Simon Willison on February 23, 2026, systematizing practical patterns for getting the best results from coding agents (Claude Code, OpenAI Codex, Gemini CLI, etc.).
- [[concepts/harness-engineering/agentic-engineering]] — Based on the concept popularized by Simon Willison's [Agentic Engineering guide](https://simonwillison.net/2025/Apr/11/agentic-engineering/).
- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — A philosophy of designing codebases to be "easy for AI agents to work with" rather than "easy for humans to navigate."
- [[concepts/harness-engineering/agentic-workflows/agentic-manual-testing]] — Exploratory testing by coding agents. Leveraging agents' manual testing capabilities to discover issues that pass automated tests (crashes, missing UI, edge cases).
- [[concepts/harness-engineering/agentic-workflows/anti-patterns]] — Anti-patterns warned about by Simon Willison when using coding agents. Particularly serious: "pushing unreviewed code onto others."
- [[concepts/harness-engineering/agentic-workflows/cli-first-development]] — An approach that starts software development from the CLI (command-line interface). A core pattern of development workflow in the agent era.
- [[concepts/harness-engineering/agentic-workflows/code-hoarding]] — Simon Willison's advocated practice of intentionally accumulating learned skills and solutions for reuse.
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — Cognitive debt accumulated through losing understanding of how AI-agent-generated code works. The cognitive version of technical debt. Accelerated by [[concepts/vibe-coding]].
- [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Simon Willison's iterative improvement cycle of collaboration between AI coding agents and human developers.
- [[concepts/harness-engineering/agentic-workflows/context-window-management]] — Patterns for effectively managing coding agent context windows to optimize quality and cost. Detailed in Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/).
- [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] — The first four-word prompt when giving a coding agent a project. Simon Willison's minimal instruction for switching the agent into testing mindset.
- [[concepts/harness-engineering/agentic-workflows/hoard-things-you-know]] — Simon Willison's concept of knowledge hoarding and reuse. In the agent era, recording and accumulating what "you know how to do" becomes a powerful weapon.
- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — A conceptual model for understanding the inner workings of coding agents. Detailed in Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/how-agents-work/).
- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — Patterns for having coding agents generate interactive animations and visualizations for intuitive understanding of algorithms and concepts.
- [[concepts/harness-engineering/agentic-workflows/karpathy-rl-agents]] — Andrej Karpathy's Autonomous Research Loop pattern. Based on the [AutoResearch](https://github.com/karpathy/autoresearch/) project (March 2026) and statements on [No Priors podcast](https://www.youtube.com/watch?v=kwSVtQ7dziU).
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Patterns for having coding agents generate structured walkthroughs of a codebase. Effective for understanding existing code, reviewing one's own forgotten code, and understanding how vibe-coded code works.
- [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] — Simon Willison's prompt-centric software development methodology. A workflow where detailed specifications are written as prompts for AI coding agents to implement.
- [[concepts/harness-engineering/agentic-workflows/red-green-tdd]] — Patterns for applying test-first development with coding agents. Core concept of Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/).
- [[concepts/harness-engineering/agentic-workflows/rodney]] — Simon Willison's Chrome DevTools Protocol-based CLI browser automation tool. Designed for coding agents to test and verify Web UIs.
- [[concepts/harness-engineering/agentic-workflows/showboat]] — Simon Willison's documentation/artifact generation tool for having coding agents "show their work."
- [[concepts/harness-engineering/agentic-workflows/subagents]] — Patterns where the main AI agent spawns independent sub-agents in parallel, each executing tasks in isolated contexts and terminal sessions.
- [[concepts/harness-engineering/agentic-workflows/throw-away-draft-pattern]] — A development pattern where agents first write a throw-away draft, compare it with the developer's mental model, then iterate.
- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] — Patterns for integrating coding agents with Git. Detailed in Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/).
- [[concepts/harness-engineering/agentic-workflows/vibe-coding]] — Simon Willison's defined development style of "coding with LLMs without paying any attention to the code."
- [[concepts/harness-engineering/context-engineering]] — A systematic approach to effectively utilizing context windows and maximizing LLM performance. Positioned as a cross-cutting technical component of Harness Engineering.
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Three new features released by Anthropic on the Claude Developer Platform enabling large-scale tool use.
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — Execution loop structure for LLM agents to autonomously complete tasks. A cyclic process where the model proposes actions, the platform executes them, and results are fed back to the model.
- [[concepts/harness-engineering/system-architecture/agent-security-patterns]] — Security control patterns for safe agent interaction with external systems. Implemented in the OpenAI Responses API's container environment.
- [[concepts/harness-engineering/system-architecture/agent-skills]] — A mechanism for agents to package reusable workflow patterns as SKILL.md bundles. Reduces the cost of rediscovering and re-planning the same multi-step patterns each time.
- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — Comparison of design philosophies for "memory" systems in AI assistants/agents. OpenAI, Anthropic, and Cognition (Devin) each adopt different approaches, reflecting differences in product targets (consumer vs engineer) and architectural philosophy (automatic vs explicit).
- [[concepts/harness-engineering/system-architecture/anthropic-memory-tool-cognition]] — In October 2025, Anthropic officially introduced the Memory Tool to the Claude API. This was a very "opinionated" design providing 6 file operations (view, create, str_replace, insert, delete, rename) natively to the model. Cognition (developer of Devin) quickly caught onto this move...
- [[concepts/harness-engineering/system-architecture/building-effective-agents]] — Practical guidelines for building LLM agents, derived from Anthropic's collaboration with dozens of teams.
- [[concepts/harness-engineering/system-architecture/claude-code-best-practices]] — Anthropic official best practices for using Claude Code (agentic coding tool).
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — A pattern for exposing MCP (Model Context Protocol) servers as code APIs, allowing agents to write code and call tools. Same core insight as Cloudflare's "Code Mode."
- [[concepts/harness-engineering/system-architecture/container-context]] — Hosted containers providing persistent execution environments for agents. A "model workspace" integrating filesystem, database, and network access.
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Discovered during Cognition's integration of Claude Sonnet 4.5 into Devin.
- [[concepts/harness-engineering/system-architecture/context-compaction]] — A mechanism for long-running agents to preserve important information and compress unnecessary data when context window limits are reached. A native feature of the OpenAI Responses API.
- [[concepts/harness-engineering/system-architecture/effective-harnesses-for-long-running-agents]] — Anthropic's 2-agent harness pattern for long-running agents, developed for the Claude Agent SDK.
- [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] — Anthropic's systematic guide to evaluating (Evals) AI agents.
- [[concepts/harness-engineering/system-architecture/harness-design-long-running-apps]] — Agent harness patterns designed by Anthropic for long-running application development. Inspired by the GAN (Generative Adversarial Network) Generator-Evaluator loop.
- [[concepts/harness-engineering/system-architecture/infrastructure-noise]] — A study quantifying the impact of infrastructure setup alone on scores in agentic coding benchmarks.
- [[concepts/harness-engineering/system-architecture/multi-agent-research-system]] — A research system built by Anthropic that runs multiple Claude agents in parallel.
- [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] — Anthropic's methodology for designing tools for AI agents. An approach of "writing tools for agents, and using agents to optimize the tools."

## Fine-Tuning

- [[concepts/fine-tuning/axolotl]] — Axolotl is a YAML-configured fine-tuning framework supporting 100+ models with LoRA/QLoRA, DPO/KTO/ORPO/GRPO, and multimodal capabilities.
- [[concepts/fine-tuning/grpo-rl-training]] — Group Relative Policy Optimization — a reinforcement learning approach for fine-tuning language models that compares multiple completions within a group to learn preferred behaviors without requiring 
- [[concepts/fine-tuning/peft-lora-qlora]] — Full fine-tuning of a 70B model requires hundreds of GBs of GPU memory. PEFT methods reduce this dramatically by:
- [[concepts/fine-tuning/pytorch-fsdp]] — FSDP enables distributed training of large models by sharding model parameters, gradients, and optimizer states across multiple GPUs.
- [[concepts/fine-tuning/quantization-overview]] — Quantization reduces model precision (FP32 → FP16 → INT8 → INT4) to decrease memory requirements and improve inference speed with minimal accuracy loss.
- [[concepts/fine-tuning/rlhf-dpo-preference]] — After Supervised Fine-Tuning (SFT), preference optimization methods align models with human values and desired behaviors. These methods differ in data requirements, complexity, and training stability.
- [[concepts/fine-tuning/trl]] — TRL is HuggingFace's library for fine-tuning language models with reinforcement learning and preference optimization methods.
- [[concepts/fine-tuning/unsloth]] — Unsloth is a fine-tuning optimization library providing 2-5x faster training with 50-80% less memory usage through custom Triton kernels and LoRA/QLoRA optimization.

## Local-Llm

- [[concepts/local-llm/dgx-spark-nim]] — Two DGX Sparks can be connected via QSFP cable (ConnectX-7, 200 Gbps) for distributed inference. Parallel inference runs via MPI + NCCL v2.28.3 over RoCE (RDMA over Converged Ethernet).
- [[concepts/local-llm/gguf]] — GGUF is the quantization format used by llama.cpp for efficient CPU/Apple Silicon inference.
- [[concepts/local-llm/inference-hardware]] — Hardware options for running LLMs locally, from consumer GPUs to edge devices.
- [[concepts/local-llm/model-distillation]] — 1. Model compression: Creating smaller, efficient models suitable for consumer hardware
- [[concepts/local-llm/model-quantization]] — Without quantization, most open-weight models would not fit in consumer GPU VRAM (24 GB on RTX 4090) or even the DGX Spark's 128 GB unified memory.
- [[concepts/local-llm/ollama]] — (content needed)
- [[concepts/local-llm/self-hosting-ai-development]] — The core tension: control and cost predictability vs. convenience and performance.
- [[concepts/local-llm/server-dgx-spark]] — Complete setup guide for running a local LLM server on NVIDIA DGX Spark, with focus on NemoClaw integration for secure AI agent development.

## Openclaw

- [[concepts/openclaw/anthropic-conflict]] — In April 2026, Anthropic blocked third-party AI agent frameworks (including OpenClaw) from accessing Claude models through flat-rate subscription plans (Pro/Max). This decision triggered a significant controversy over platform control, developer access, and the economics of AI agent infrastructure.
- [[concepts/openclaw/architecture-comparison]] — An architectural comparison analysis based on elvis (@elvis_)'s 9-hour parallel source code study of Hermes Agent vs OpenClaw conducted in April 2026.
- [[concepts/openclaw/ecosystem-tools]] — An MCP-first developer tool ecosystem developed by Peter Steinberger (@steipete). OpenClaw sits at the core, with multiple CLI/MCP servers interconnected.
- [[concepts/openclaw/five-tier-precedence]] — The hierarchical priority model adopted by OpenClaw's skill loading system. One of the most important architectural differences when contrasted with Hermes Agent's self-authoring approach.
- [[concepts/openclaw/philosophy]] — The core of OpenClaw's design philosophy: "Primitives over Defaults." Similar to the design philosophy of the Linux kernel or Kubernetes.

## Ai-Organization

- [[concepts/ai-organization/ai-org-context-as-moat]] — In an era where AI replaces the execution layer, a company's competitive advantage converges on its unique context for "what and how to decide." Integrates McKinsey's Agentic Organization framework, Reworked's Diamond Org Chart discussion, and Agile Leadership Day's practical organizational model.
- [[concepts/ai-organization/ai-org-from-hierarchy-to-intelligence]] — The Hierarchy to Intelligence model practiced by Jack Dorsey at Block (formerly Square) starting in 2024. Abandons traditional hierarchical decision-making in favor of "context-driven autonomous execution + transparency-based monitoring." Views AI not as a mere productivity tool but as a "redesign of coordination mechanisms themselves."
- [[concepts/ai-organization/ai-org-solo-founder-and-super-ic]] — As the AI tool stack matures, the paradigm of "1 person = traditional 10-person team" is becoming reality. Integrates discussions from the Reddit r/ClaudeCode community and FourWeekMBA, cataloging the rise of solo founders, the emergence of super ICs, and their limitations and challenges.

## Inference

- [[concepts/inference/llama-cpp]] — llama.cpp is a C/C++ inference engine for running LLMs efficiently on consumer hardware, created by Georgi Gerganov.
- [[concepts/inference/sglang]] — SGLang's signature optimization. Builds a tree-structured KV cache across requests sharing common prefixes:
- [[concepts/inference/vllm]] — vLLM is a high-throughput LLM serving engine with PagedAttention optimization.
- [[concepts/tensorrt-llm]] — NVIDIA's optimized inference engine with TensorRT compiler, FP8/FP4 quantization, Triton integration. Highest throughput on NVIDIA GPUs.

## Ai-Infrastructure-Engineering

- [[concepts/ai-infrastructure-engineering/_index]] — Parent page: AI Infrastructure Engineering. GPU/VRAM fundamentals, distributed training, model serving, observability, cost optimization.
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPU memory hierarchy, VRAM requirement calculation, roofline model, batching economics, quantization effects.
- [[concepts/ai-infrastructure-engineering/distributed-training]] — DDP → FSDP → DeepSpeed ZeRO stages, 3D parallelism (TP/PP/EP), strategy selection guide.
- [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — Deployment architectures, autoscaling strategies (HPA, predictive, serverless), load balancing, cost optimization.
- [[concepts/ai-infrastructure-engineering/llm-observability]] — Inference metrics (TTFT, TPOT, ITL), GPU/VRAM monitoring, cost attribution, production patterns, vLLM OTel integration.

## Web-Filesystem

- [[concepts/web-as-filesystem]] — An abstraction mounting all web documents as a Unix filesystem. Enables agents to naturally use `tree`, `grep`, `cat`, and `find`, eliminating code hallucinations. Implementation by Nia (Nozomio Labs).

## Sandbox

- [[concepts/sandbox/in-process]] — In-process sandboxing isolates LLM-generated code execution within the host process using language-level security boundaries — without requiring Docker, cloud accounts, or external infrastructure.
- [[concepts/sandbox/infrastructure]] — Infrastructure-level sandboxing refers to OS/hypervisor-level isolation technologies used to safely execute AI agent code — particularly LLM-generated or user-supplied code — without compromising the host.
- [[concepts/sandbox/js-runtime]] — JavaScript/TypeScript runtimes form a critical layer of the AI agent stack. Unlike Python's single CPython implementation, the JS ecosystem offers three competing runtimes with fundamentally different architectures.

## Agent-Loop-Orchestration

- [[concepts/agent-loop-orchestration]] — OpenAI Responses API patterns for orchestrating agent loops. See harness-engineering/system-architecture/agent-loop-orchestration.md for full content.

## Agent-Sandboxing

- [[concepts/agent-sandboxing]] — Agent Sandboxing is a spectrum of technologies for safely isolating AI agent dynamic code execution. Organizes isolation technologies like gVisor, Firecracker microVM, WASM, etc. Standard containers are insufficient due to shared kernel.

## Agent-Survival-Benchmark

- [[concepts/agent-survival-benchmark]] — An open-source benchmark measuring LLM agent survivability and performance under PvP (player vs player) pressure.

## Agent-Team-Swarm

- [[concepts/agent-team-swarm]] — Agent team swarm refers to coordination patterns where multiple AI agents work together in distributed, emergent structures rather than rigid hierarchies.
- [[concepts/agent-team-swarm/managed-devins]] — Cognition's evolved approach to multi-agent coordination, introduced in Devin 2.2.

## Agentic-Alternative-To-Graphrag

- [[concepts/agentic-alternative-to-graphrag]] — A November 2025 paper by Contextual AI (George Halal, Jackie Zhang, Sheshansh Agrawal) proposing that the reference traversal problem in RAG pipelines should be solved via agentic tool-use rather than graph-based approaches.

## Agentic-Browsing

- [[concepts/agentic-browsing]] — Agentic Browsing refers to AI agents that autonomously navigate websites, click buttons, fill forms, and execute multi-step web tasks without human intervention. Tools like Browser Use, Playwright MCP, and Puppeteer enable agents to interact with web UIs as humans do — clicking, scrolling, typing, and reading structured and unstructured content.

## Agentic-Engineering

- [[concepts/agentic-engineering]] — This stub exists for backwards compatibility while content is organized into the harness-engineering/ subdirectory structure.

## Agentic-Manual-Testing

- [[concepts/agentic-manual-testing]] — Manual testing enhanced with AI agent assistance. See harness-engineering/agentic-workflows/agentic-manual-testing.md for full content.

## Agentic-Pbt

- [[concepts/agentic-pbt]] — Anthropic + Hypothesis joint research (NeurIPS 2025 DL4C Workshop). Claude Code agents autonomously infer code invariants (properties) from type annotations, docstrings, function names, and comments, then generate and execute PBT using the Hypothesis framework.

## Agentic-Rag

- [[concepts/agentic-rag]] — Agentic RAG integrates autonomous AI agents into the RAG pipeline, enabling dynamic retrieval, iterative context refinement, and adaptive workflow orchestration. It addresses limitations of traditional RAG approaches.

## Agentic-Security

- [[concepts/agentic-security]] — Agentic Security encompasses the security patterns, protocols, and tools for protecting AI agents, MCP servers, and the broader agent ecosystem. Covers authentication, authorization, data exfiltration prevention, MCP server security, prompt injection defense, and sandboxing strategies for agentic systems.

## Agentic-Scaffolding

- [[concepts/agentic-scaffolding]] — "Scaffolding" patterns for safely operating agents in production. Infrastructure design that maximizes agent capabilities while managing risk.

## Agentic-Theory

- [[concepts/agentic-theory]] — Sean Goedecke's analysis applying Peter Naur's 1985 "theory building" concept to AI-assisted programming.

## Agentic-Web

- [[concepts/agentic-web]] — (content needed)

## Agentic-Workflow-Patterns

- [[concepts/agentic-workflow-patterns]] — (content needed)

## Ai-Addiction-Burnout

- [[concepts/ai-addiction-burnout]] — AI coding tools trigger a compulsion loop similar to slot machines:

## Ai-Agent-Memory-Middleware

- [[concepts/ai-agent-memory-middleware]] — A cross-cutting analysis of storage infrastructure for AI agents to persist state, share context across sessions, and coordinate across multi-agent pipelines.

## Ai-Agent-Memory-Two-Camps

- [[concepts/ai-agent-memory-two-camps]] — Classification of AI memory/context tools into two fundamentally different paradigms: Memory Backends vs Context Substrates.

## Ai-Agent-Traps

- [[concepts/ai-agent-traps]] — A systematic framework from Google DeepMind (2026) for understanding how the open web can be weaponized against autonomous AI agents. Defines six categories of adversarial content engineered to exploit agent vulnerabilities.

## Ai-Autonomy-Debate

- [[concepts/ai-autonomy-debate]] — The AI Autonomy Debate centers on whether AI agents should operate fully autonomously or maintain human oversight in the loop. What started as a niche technical discussion has become one of the most contentious issues in AI development.

## Ai-Bubble-Economics

- [[concepts/ai-bubble-economics]] — The AI Bubble Economics concept encompasses the growing body of analysis questioning whether the unprecedented capital flowing into artificial intelligence infrastructure is backed by real economic value or driven by speculative hype.

## Ai-Coding-Agent-Criticism

- [[concepts/ai-coding-agent-criticism]] — Armin Ronacher (lucumr.pocoo.org) identified a structural asymmetry in how AI coding agents are debated:

## Ai-Coding-Reliability

- [[concepts/ai-coding-reliability]] — The central tension: AI tools can write code faster than any human, but writing code is not the same as shipping reliable software. The industry is discovering this distinction at scale in 2026.

## Ai-Digital-Nato

- [[concepts/ai-digital-nato]] — In April 2026, OpenAI, Anthropic, and Google began sharing threat intelligence through the Frontier Model Forum (founded with Microsoft in 2023) to detect and counter what they term "adversarial distillation" attacks.

## Ai-Evals

- [[concepts/ai-evals]] — Product-specific evaluation systems for measuring whether an AI application works correctly on real tasks with real data. Not foundation model benchmarks like MMLU, HELM, or GPQA.

## Ai-Index-Report-2026

- [[concepts/ai-index-report-2026]] — The annual AI Index report published by Stanford University's HAI (Human-Centered AI Institute). Contains comprehensive data on AI R&D, technical performance, economic impact, and ethics/governance.

## Ai-Memory-Systems

- [[concepts/ai-memory-systems]] — OpenAI's ChatGPT Memory, Anthropic's Claude Memory (in development), and Cognition's Devin Memory are each based on different design philosophies. This page compares the three approaches and explores optimal memory system design for coding agents.

## Ai-Military

- [[concepts/ai-military]] — Coverage of AI systems (particularly Claude) outperforming US military teams in wargame simulations, and the subsequent Pentagon-Anthropic dispute over military use of AI.

## Ai-Observability

- [[concepts/ai-observability]] — AI observability extends traditional software observability (metrics, logs, traces) to cover the unique challenges of LLM-powered applications: non-deterministic outputs, token usage, agent decision traces, and hallucination monitoring.

## Ai-Privacy-Tools

- [[concepts/ai-privacy-tools]] — In early 2026, the AI security community identified a novel technique dubbed "Slingshot" — a CORS-based attack vector that allows AI agents and browser automation tools to bypass traditional web security boundaries.

## Ai-Safety

- [[concepts/ai-safety]] — AI Safety encompasses the technical and philosophical work of ensuring that increasingly capable AI systems behave as intended, remain aligned with human values, and can be understood and controlled by humans.

## Ai-Subprime

- [[concepts/ai-subprime]] — Ed Zitron's analysis drawing parallels between the 2008 subprime mortgage crisis and the current AI industry economics.

## Anthropic-Managed-Agents

- [[concepts/anthropic-managed-agents]] — Anthropic Managed Agents is a platform that accelerates AI agent development from prototype to production by 10x. It delegates infrastructure setup (sandboxes, authentication, permissions, checkpoints, error recovery) to Claude, allowing developers to focus on task definition, tools, and guardrail design.

## Anthropic-Openclaw-Conflict

- [[concepts/anthropic-openclaw-conflict]] — In April 2026, Anthropic blocked third-party AI agent frameworks (including OpenClaw) from accessing Claude models through flat-rate subscription plans (Pro/Max). This decision triggered a significant controversy.

## Attention-Mechanism-Variants

- [[concepts/attention-mechanism-variants]] — Modern transformer architectures use different attention mechanisms to optimize the trade-off between modeling capacity, compute efficiency, and context length. A prerequisite concept for [[concepts/context-engineering]].

## Back-Of-House-Multi-Agent-Patterns

- [[concepts/back-of-house-multi-agent-patterns]] — Multi-agent workflow patterns using the kitchen metaphor. Proposed by Sarah Chieng ([[concepts/@milksandmatcha]]) and [@0xSero] in April 2026.

## Back-Of-House-Patterns

- [[concepts/back-of-house-patterns]] — Multi-agent workflow patterns using the professional kitchen (Back of House) metaphor. A practical framework for overcoming single-agent limitations ([[concepts/single-agent-ceiling]]).

## Base-Consistency

- [[concepts/base-consistency]] — BASE is an alternative consistency model to ACID, designed for distributed systems that prioritize availability over strict consistency.

## Behavioral-Trait-Transmission

- [[concepts/behavioral-trait-transmission]] — Language models that share initialization can transmit behavioural traits through training data that is semantically unrelated to those traits — a phenomenon discovered by Anthropic and academic researchers.

## Blogwatcher

- [[concepts/blogwatcher]] — Blogwatcher is a CLI-based blog and RSS feed monitoring tool (written in Go) for tracking technical blogs and newsletters. It periodically scans configured RSS/Atom feeds, detects new posts, and can be integrated into automated workflows for content discovery and curation.

## Building-Effective-Agents

- [[concepts/building-effective-agents]] — Anthropic's foundational guide to building effective AI agents with simple, composable patterns. Defines workflows vs. agents, five building block patterns, and the ACI (Agent-Computer Interface) concept.

## Caid-Coordination

- [[concepts/caid-coordination]] — A coordination framework from CMU (2026) for running multiple coding agents in parallel on complex software engineering tasks. Uses git operations as the core coordination primitive.

## Capabilities-Based-Security

- [[concepts/capabilities-based-security]] — Security model starting from zero access, explicitly granting capabilities. See sandbox patterns for full content.

## Causal-Backbone-Conjecture

- [[concepts/causal-backbone-conjecture]] — The conjecture proposes that agent-like structures emerge naturally from resource constraints, not from the need to model "a sufficiently rich set of tasks." In environments with finite resources (computation, energy, information), the optimal strategy is to allocate resources causally — building a causal backbone that captures the most predictive features.

## Chaos-Engineering

- [[concepts/chaos-engineering]] — Chaos Engineering is the discipline of experimenting on a system to build confidence in its ability to withstand turbulent conditions in production. For microservices, this means intentionally injecting failures to test resilience.

## Chatgpt-Memory-Bitter-Lesson

- [[concepts/chatgpt-memory-bitter-lesson]] — Analysis of ChatGPT's memory system through the lens of Rich Sutton's Bitter Lesson — arguing that the best way to build agent memory is not to build one at all, but to embrace stateless, context-window-based approaches.

## Chief-Of-Staff-Agent-Patterns

- [[concepts/chief-of-staff-agent-patterns]] — Anthropic cookbook: [The Chief of Staff Agent](https://platform.claude.com/cookbook/claude-agent-sdk-01-the-chief-of-staff-agent)

## Claude-47-Tokenizer

- [[concepts/claude-47-tokenizer]] — Claude Opus 4.7 was released on April 16, 2026, marking the first tokenizer change. This change results in the same input text being mapped to 40% more tokens.

## Claude-Agent-Sdk-Sre-Patterns

- [[concepts/claude-agent-sdk-sre-patterns]] — Anthropic cookbook: [The Site Reliability Agent](https://platform.claude.com/cookbook/claude-agent-sdk-03-the-site-reliability-agent)

## Claude-Code-Best-Practices

- [[concepts/claude-code-best-practices]] — Practical patterns and techniques for effective Claude Code usage, synthesized from experienced users' real-world workflows. These complement the internal patterns found in the leaked Claude Code source code.

## Claude-Code-Source-Patterns

- [[concepts/claude-code-source-patterns]] — Analysis of tactical engineering patterns found in Claude Code's leaked source code (March 2026). Reveals how Anthropic builds production-grade coding agents with emphasis on prompt composition, caching strategies, and tool integration architecture.

## Claude-Memory-Tool

- [[concepts/claude-memory-tool]] — Analysis of how Cognition (makers of Devin) is adopting Claude's memory approach — and what this reveals about competitive dynamics in the coding agent space.

## Claude-Memory

- [[concepts/claude-memory]] — Analysis of Claude's memory system design — how Anthropic uses filesystem-based memory (`CLAUDE.md`, `.agent/` directories) instead of proprietary databases, treating the filesystem as the single source of truth for agent context.

## Claude-Mythos-Glasswing

- [[concepts/claude-mythos-glasswing]] — The model was revealed via a CMS misconfiguration leak on March 26, 2026, when security researchers discovered ~3,000 unpublished Anthropic assets publicly accessible. Anthropic confirmed the leak was accidental and contained pre-release model artifacts.

## Claude-Mythos-Preview

- [[concepts/claude-mythos-preview]] — Anthropic did not release Claude Mythos publicly. The preview is restricted to frontier red team research and select partners. This decision was characterized by The Signal Newsletter as a "lockdown" of the most capable AI systems.

## Cli-Over-Mcp-Pattern

- [[concepts/cli-over-mcp-pattern]] — Standard CLIs like `gh`, `vercel`, `psql` have well-defined interfaces that can be exposed through MCP for agent consumption.

## Closing-Agent-Loop

- [[concepts/closing-agent-loop]] — Cognition's philosophy for autonomous development: Devin doesn't just write code — it handles the entire development loop.

## Coala

- [[concepts/coala]] — CoALA (Cognitive Architectures for Language Agents) is a unified conceptual framework that maps modern LLM-based agents to the 50-year lineage of cognitive science and symbolic AI. It addresses the fragmentation in agent design by providing a structured cognitive architecture.

## Code-Mode

- [[concepts/code-mode]] — CodeMode is the paradigm where LLMs write code (typically Python) for batch execution rather than making sequential tool calls. Coined by Cloudflare and independently developed by Anthropic, Pydantic, and others.

## Cognition-Ai-Data-Analyst

- [[concepts/cognition-ai-data-analyst]] — Design for turning Cognition/Devin into a 24/7 data analysis agent. MCP + Knowledge settings + DANA dedicated agent. Integration of codebase context understanding × data analysis. Includes end-to-end bug debugging (with Datadog integration).

## Cognition-Devin-Philosophy

- [[concepts/cognition-devin-philosophy]] — A consistent philosophy on AI coding agents from the Devin team at Cognition Labs (CEO: Scott Wu @ScottWu46).

## Cognitive-Cost-Of-Agents

- [[concepts/cognitive-cost-of-agents]] — In April 2026, [[entities/simon-willison]] published a deeply personal reflection after using Claude Code intensively for a full month. The post, "The cognitive impact of coding agents," challenged the prevailing narrative that coding agents are pure productivity multipliers.

## Cognitive-Debt

- [[concepts/cognitive-debt]] — The accumulated mental overhead of understanding and maintaining complex AI-generated code. See harness-engineering/agentic-workflows/cognitive-debt.md for full content.

## Cognitive-Load-Software-Development

- [[concepts/cognitive-load-software-development]] — Artem Zakirullin's "Cognitive load is what matters" — a systematic framework for cognitive load in software design that has gained 12,000+ stars on GitHub.

## Compute-Scaling-Bottlenecks

- [[concepts/compute-scaling-bottlenecks]] — The concept was most thoroughly articulated by Dylan Patel of SemiAnalysis, particularly in his March 2026 Dwarkesh Podcast appearance, where he traced the entire AI compute stack from silicon atoms to training clusters.

## Context-Compression

- [[concepts/context-compression]] — Methods for reducing the size of context windows while preserving task-relevant information. Critical prerequisite for [[concepts/context-engineering]] — addresses the fundamental constraint that LLMs have finite context capacity.

## Context-Engineering

- [[concepts/context-engineering]] — This stub exists for backwards compatibility while content is organized into the harness-engineering/ subdirectory structure.

## Context-Fragments

- [[concepts/context-fragments]] — A concept proposed by Vivek Trivedy (@vtrivedy10) in April 2026. A framework that views the context window as "a collection of objects selectively loaded by the harness."

## Context-Graph

- [[concepts/context-graph]] — Living record of decision traces stitched across entities and time — the foundational architecture for AI agent decision-making in enterprise workflows.

## Context-Routing

- [[concepts/context-routing]] — Multi-domain agents load all domains' knowledge, tool sets, and instructions for every query. This is wasteful of context and causes attention dilution.

## Context-Window-Management

- [[concepts/context-window-management]] — The core challenge: LLMs have a fixed context window, but software projects have unbounded complexity. Effective management is the difference between a productive AI session and a confused, expensive spiral.

## Constitutional-Ai

- [[concepts/constitutional-ai]] — Anthropic's methodology for aligning AI via explicit constitutional principles. Three Poles of Alignment (Principles, Policies, Personality) framework from Boaz Barak's 2026 analysis. Claude Constitution vs. OpenAI Model Spec comparison. Covers RLAIF, anthropomorphism critique, and AI-led ethics debate.

## Data-Analysis-Agents

- [[concepts/data-analysis-agents]] — A comprehensive concept of AI data analysis agents. Pipeline: data exploration → schema understanding → query generation → execution → verification → visualization → reporting. Compares two major approaches: OpenAI's internal data agent (GPT-5.2) and Cognition DANA/Devin. Includes relationships with DWH semantic layers and golden queries.

## Critique-Shadowing

- [[concepts/critique-shadowing]] — A 7-step iterative methodology for building aligned LLM-as-Judge evaluators, coined by Hamel Husain. The core insight: the process of building an LLM judge forces domain experts to carefully examine their own definition of quality, revealing assumptions that were previously implicit.

## Cybersecurity-Proof-Of-Work

- [[concepts/cybersecurity-proof-of-work]] — A concept coined by Drew Breunig in April 2026, observing that as LLMs like Claude Mythos become increasingly effective at finding security vulnerabilities, cybersecurity transforms into an economic equation of attacker compute cost vs defender compute cost.

## Dark-Factory-Software-Factory

- [[concepts/dark-factory-software-factory]] — "Dark Factory" refers to the highest level of software development automation where humans write no code and perform no reviews. A metaphor derived from Fanuc's unmanned factories (where robot-operated factories need no lighting = dark).

## Death-Of-Browser

- [[concepts/death-of-browser]] — 1. Cognitive load limits: Humans are exhausted by numerous tabs, popups, and SEO spam.

## Decoder-Only-Gpt

- [[concepts/decoder-only-gpt]] — The decoder-only GPT (Generative Pre-trained Transformer) is the dominant architecture behind modern large language models (ChatGPT, Claude, Gemini, etc.). Andrej Karpathy's microgpt project (February 2026) provides an educational implementation.

## Deep-Agents

- [[concepts/deep-agents]] — Deep agents are autonomous AI agents that combine multiple architectural patterns to handle complex, multi-step tasks with minimal human intervention.

## Direct-Prompting-Philosophy

- [[concepts/direct-prompting-philosophy]] — The core thesis: "Don't waste your time on stuff like RAG, subagents, Agents 2.0 or other things that are mostly just charade. Just talk to it. Play with it. Develop intuition." — Peter Steinberger

## Dspy-Rlm

- [[concepts/dspy-rlm]] — Recursive Language Model — A DSPy module that programmatically explores large contexts using a sandbox Python REPL.

## Dspy

- [[concepts/dspy]] — DSPy is a framework developed by Omar Khattab's Stanford NLP group for declaratively programming LLMs as "optimizable modules" rather than through "prompts." Through the abstractions of Signature/Module/Teleprompter, it transforms manual prompt engineering into automatic compile-time optimization.

## Ecs-Fargate-Scaling

- [[concepts/ecs-fargate-scaling]] — An experimental validation of scaling AWS ECS Fargate like Lambda. Optimizing burst handling performance for SQS workloads.

## Elixir-Beam-Agent-Orchestration

- [[concepts/elixir-beam-agent-orchestration]] — Patterns for leveraging Elixir/BEAM (Erlang VM) for AI agent orchestration. The approach adopted by [[concepts/openai-symphony]]'s Ryan Lopopolo.

## Evaluation-Flywheel

- [[concepts/evaluation-flywheel]] — A development pattern from OpenAI's cookbook that cycles through evaluation and improvement.

## Event-Driven-Architecture

- [[concepts/event-driven-architecture]] — Event-Driven Architecture (EDA) is a software design pattern where services communicate asynchronously through events rather than synchronous API calls. Services publish events to a central event bus for consumption by other services.

## Exec-Plans

- [[concepts/exec-plans]] — A pattern where agents create a plan before executing tasks. Separating planning from execution improves transparency, reproducibility, and debuggability.

## Experiential-Memory

- [[concepts/experiential-memory]] — A concept proposed by Vivek Trivedy (@vtrivedy10) in April 2026. A framework for sharing, forking, and reusing "experiential memory" accumulated by agents through interactions.

## Flashattention-Pytorch-Educational

- [[concepts/flashattention-pytorch-educational]] — [shreyansh26/FlashAttention-PyTorch](https://github.com/shreyansh26/FlashAttention-PyTorch) is a project that implements the FlashAttention algorithm (FA1 through FA4) in PyTorch with educational and algorithmic clarity.

## Formal-Verification-Llm-Agents

- [[concepts/formal-verification-llm-agents]] — Formal verification is the practice of mathematically proving that code always satisfies its specifications—including all edge cases. AI is poised to bring this from a fringe academic pursuit into mainstream software engineering.

## Functional-Emotions-Llms

- [[concepts/functional-emotions-llms]] — The discovery that Large Language Models develop internal representations of emotion concepts that causally influence model behavior, including alignment-relevant outcomes. Based on Anthropic's 2026 interpretability research.

## Gemini

- [[concepts/gemini]] — (content needed)

## Autonomous-Component-Optimization

- [[concepts/autonomous-component-optimization]] — Daniel Miessler's proposed general self-improvement cycle (Map→Execute→Log→Collect→Optimize→Update). An extension of the Karpathy Loop's ML hyperparameter tuning to any knowledge workflow.

## Intent-Based-Engineering

- [[concepts/intent-based-engineering]] — A concept identifying the new bottleneck in AI development: the "articulation gap." Demonstrates the shift in engineering from "how to build" to "how to describe a good state." Proposed by Daniel Miessler.

## Philosophy & Critique

- [[concepts/techno-pessimism]] — Curtis Yarvin's techno-pessimism manifesto. A rebuttal to Marc Andreessen's "Techno-Optimist Manifesto." Argues that technological acceleration is the cause, not the cure, for the decline of civilization. The core concept is the divergence of two curves: technology's upward trajectory and the human spirit's (thymos) downward trajectory.
