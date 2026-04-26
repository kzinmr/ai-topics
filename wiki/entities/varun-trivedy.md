---
title: Varun Trivedy
type: entity
handle: "@Vtrivedy10"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ai
  - ml-engineering
  - agents
  - langchain
  - harness-engineering
  - evals
  - open-source
sources: []
---


# Varun Trivedy (@Vtrivedy10)

| | |
|---|---|
| **X** | [@Vtrivedy10](https://x.com/Vtrivedy10) |
| **Blog** | [vtrivedy.com](https://www.vtrivedy.com/posts) |
| **GitHub** | [vtrivedy](https://github.com/vtrivedy) |
| **Role** | Engineer at LangChain (Open Source Agents & Harnesses) |
| **Known for** | Harness engineering research, DeepAgents, agent evaluation methodologies, Terminal Bench improvements |
| **Bio** | ML engineer and researcher currently at LangChain leading open-source agent harness development (DeepAgents). Previously founded a visual understanding startup, worked as a Scientist at AWS Life Sciences & Healthcare AI, and earned a PhD in Computer Science from Temple University. Known for pioneering the concept of "Harness Engineering" as a distinct discipline from prompt engineering. |

## Overview

Varun Trivedy (who goes by "Viv") is one of the leading voices in **harness engineering** — the discipline of building the infrastructure, tooling, and execution logic that wraps around AI models to make them useful for autonomous, long-horizon tasks. His core equation — `Agent = Model + Harness` — has become a foundational framing for how the AI engineering community thinks about building production-grade agent systems.

At LangChain, Trivedy leads the development of **DeepAgents**, an open-source agent harness that went from Top 30 to Top 5 on Terminal Bench 2.0 through harness-level improvements alone, without changing the underlying model. This work demonstrated that significant performance gains come not from model upgrades but from better context engineering, verification loops, and execution orchestration — a thesis he has articulated through both his blog posts and public talks.

Before LangChain, Trivedy was a Scientist at AWS, where he led projects building AI platforms for medical document processing, mapping the human brain, and large-scale image search and retrieval. He holds a PhD in Computer Science from Temple University, where his research focused on self-supervised learning for image retrieval and object-focused attention mechanisms. He has also founded startups in visual understanding and AI-assisted creativity.

## Core Ideas

### Harness Engineering as a Distinct Discipline

Trivedy's central thesis is that as models become commoditized, the competitive advantage shifts to the **harness** — the system that surrounds the model with tools, context, memory, and verification.

> *"If you're not the model, you're the harness."*

> *"The model contains the intelligence and the harness makes that intelligence useful."*

> *"Harnesses today are largely delivery mechanisms for good context engineering."*

In "The Anatomy of an Agent Harness" (Mar 2026), Trivedy defines a harness as **all code, configuration, and execution logic outside the model** that transforms raw intelligence into a functional work engine. Key components:

| Component | Function |
|-----------|----------|
| **Hooks/Middleware** | Deterministic execution (compaction, continuation, lint checks) |
| **Orchestration Logic** | Subagent spawning, handoffs, model routing |
| **Bundled Infrastructure** | Filesystem, sandbox, browser |
| **Tools/Skills/MCPs** | With descriptions and progressive disclosure |
| **System Prompts** | Behavioral constraints and instructions |

### The Context Rot Problem

A major insight from Trivedy's work is **context rot** — the degradation of agent performance as the context window fills with accumulated conversation history. His solutions include:

- **Compaction**: Intelligently summarizing/offloading context when nearing limits
- **Tool Call Offloading**: Retaining head/tail tokens in context; storing full output in the filesystem for on-demand retrieval
- **Skills**: Progressive disclosure of tools/MCPs to prevent startup context bloat
- **Filesystem as memory**: Using the filesystem (particularly `AGENTS.md` and Git) as durable, cross-session state

### Build-Verify-Iterate Loop

The breakthrough that moved DeepAgents from Top 30 to Top 5 on Terminal Bench 2.0 was implementing a **build-and-self-verify loop** that forces agents to test their own work before considering a task complete.

> *"Testing is a key part of autonomous agentic coding. It helps test for overall correctness and simultaneously gives agents signal to hill-climb against."*

The loop structure:
1. **Planning & Discovery**: Read task, scan codebase, build initial plan
2. **Build**: Implement with verification in mind, create tests for happy paths & edge cases
3. **Verify**: Run tests, read full output, compare against spec (NOT your own code)
4. **Fix**: Analyze errors, revisit original spec, iterate

This is enforced via a `PreCompletionChecklistMiddleware` (nicknamed the "Ralph Wiggum Loop") that intercepts the agent before exit to force a verification pass.

### Adaptive Reasoning Compute

Trivedy's work on compute allocation uses an **"xhigh-high-xhigh reasoning sandwich"**:
- High reasoning compute for planning (understand the task deeply)
- Lower reasoning compute for implementation (just execute)
- High reasoning compute for verification (critically evaluate the result)

This approach improved scores from 52.8% to 66.5% on Terminal Bench 2.0, demonstrating that smart compute allocation matters more than raw compute budget.

### Opinionated Agent Design

> *"The best agent products aren't the most flexible, they're the most opinionated."*

In "Agents Should Be More Opinionated" (Nov 2025), Trivedy argues against the "fewer knobs = better UX" intuition. Instead, he advocates for:
- Designing harnesses around specific use cases rather than building general-purpose frameworks
- Baking in lessons from model behavior patterns (intelligence spikes, failure modes)
- Making deliberate choices about what the agent can and cannot do

## Key Work

### DeepAgents (LangChain)

The open-source agent harness that Trivedy leads. Key innovations:
- **Subagents**: Delegating to isolated agents to avoid context bloat ("the dumb zone")
- **Skills**: Progressively disclosing capabilities to keep context clean
- **Trace-driven optimization**: Automated analysis of agent traces to identify failure patterns and iteratively improve harness design
- Terminal Bench 2.0 progression: Top 30 → Top 5 through harness improvements only

### Claude Code SDK & HaaS

In "The Claude Code SDK and the Birth of HaaS (Harness as a Service)" (Sep 2025), Trivedy introduced the concept of **Harness as a Service** — the idea that the shift from LLM APIs to Harness APIs represents a fundamental change in how we build with AI:

> *"As tasks require more autonomous behavior, we're seeing a shift from LLM APIs to Harness APIs."*

Key projects built on this concept:
- **claude-banana-story-agent**: Autonomous story agent creating illustrated storybooks (23 GitHub stars)
- **stranger-code**: Stranger Things-themed AI coding TUI powered by deepagents
- **talking-avatar**: AI-powered talking avatar generator

### Trace Analysis & Agent Evals

In "How we build evals for Deep Agents" (Mar 2026, co-authored with Sydney Runkle, Mason Daugherty, Eugene Yurtsev, and Harrison Chase), Trivedy outlines LangChain's methodology for evaluating agentic systems:

- Mining tracing data to improve agents
- Building eval frameworks that test long-horizon task completion
- Using automated trace analysis to identify harness-level failure patterns

### Academic Research

| Paper | Venue | Year | Focus |
|-------|-------|------|-------|
| **CNN2Graph: Building Graphs for Image Classification** | WACV | 2023 | Using GNNs to build graphs of "good" images for transductive learning |
| **Image Retrieval with Self-Supervised Divergence Minimization** | IJCAI | 2024 | Improving image retrieval via distribution matching |
| **Learning Object Focused Attention** | ICPR | 2024 | Attention mechanisms for object-level image understanding |

### Selected Projects

- **Amber**: Multi-agent system for collaborative generative media experiences (games, talking avatars)
- **StoryForest**: Interactive visual storytelling platform with AI-generated imagery
- **Edgeout.gg**: Bootstrapped gaming analytics platform (sold to blitz.gg)
- **Pubpub.org**: Non-profit academic publishing platform (co-founded)

## Blog / Recent Posts

| Date | Title | Key Takeaway |
|------|-------|--------------|
| 2026-03-10 | [The Anatomy of an Agent Harness](https://vtrivedy.com/posts/the-anatomy-of-an-agent-harness/) | Comprehensive framework: Agent = Model + Harness. Defines core primitives (filesystem, bash, sandboxes, memory, tools). |
| 2026-02-17 | [Improving Deep Agents with Harness Engineering](https://vtrivedy.com/posts/improving-deep-agents-with-harness-engineering/) | Top 30 → Top 5 on Terminal Bench 2.0 through harness changes only. Build-verify loop, adaptive compute, trace analysis. |
| 2025-11-25 | [Agents Should Be More Opinionated](https://vtrivedy.com/posts/agents-should-be-more-opinionated/) | Best agent products are opinionated, not flexible. Design around model intelligence spikes. |
| 2025-10-24 | [The Modern Planning Agent is a Dynamic, Adaptive Workflow Generator](https://vtrivedy.com/posts/the-modern-planning-agent/) | Planning agents as just-in-time workflow generators, not static planners. |
| 2025-09-23 | [The Claude Code SDK and the Birth of HaaS](https://vtrivedy.com/posts/the-claude-code-sdk-and-the-birth-of-haas/) | Shift from LLM APIs to Harness APIs. Claude Code SDK enables rapid agent development. |
| 2025-08-06 | [Welcome to My Blog](https://vtrivedy.com/) | Introduction and overview of research focus areas. |

## Related People

- **[[philipp-schmid]]** — Both write about agent harnesses and evaluation; Schmid's "2026 will be around Agent Harnesses" post echoes Trivedy's framing
- **** — Co-author on Deep Agents evals post; CEO of LangChain
- **** — Co-author on multi-agent applications and Deep Agents blog posts at LangChain
- **[[florian-brand]]** — Complementary work on RL training infrastructure and benchmark evaluation

## X Activity Themes

Trivedy's X activity (@Vtrivedy10) typically covers:

1. **Harness engineering insights** — Breaking down how specific harness components (middleware, skills, subagents) improve agent performance
2. **Benchmark results** — Sharing DeepAgents' progress on Terminal Bench 2.0 and other agent evaluation frameworks
3. **Agent development patterns** — Practical advice for building production-grade agents, including context management and verification loops
4. **Open-source advocacy** — Promoting DeepAgents, agent protocols, and community-driven improvements to agent tooling
5. **AI industry commentary** — Thoughts on the shift from model-centric to infrastructure-centric AI development, the commoditization of base models
6. **Personal reflections** — Occasional posts about the broader implications of autonomous AI systems and the future of software engineering
