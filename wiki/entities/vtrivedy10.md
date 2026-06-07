---

## Related Entities

- [[entities/theodoros-galanos]]
title: "Vivek 'Varun' Trivedy (@vtrivedy10)"
type: entity
handle: "@vtrivedy10"
created: 2026-04-14
updated: 2026-06-07
tags: [person, langchain, harness-engineering, ai-agents, deep-agents]
aliases: ["vtrivedy10", "Vivek Trivedy", "Varun Trivedy"]
sources:
  - raw/articles/2026-05-06_vtrivedy10_strong-opinions-agent-harness-engineering.md
  - https://x.com/vtrivedy10/status/2052100726608781363
  - raw/articles/2024-03-26_hamel-revenge-data-scientist.md
---

# Vivek 'Varun' Trivedy (@vtrivedy10)

| | |
|---|---|
| **X** | [@vtrivedy10](https://x.com/vtrivedy10) |
| **Blog** | [vtrivedy.com](https://www.vtrivedy.com/) |
| **GitHub** | [vtrivedy](https://github.com/vtrivedy) |
| **LinkedIn** | [Vivek Trivedy](https://linkedin.com/in/vivek-trivedy-433509134) |
| **Role** | Product Lead, Agents & Harnesses @ LangChain |
| **Known for** | Deep Agents CLI, Harness Engineering, Agent Architecture |
| **Bio** | Researcher and engineer leading open-source agent development at LangChain. PhD in CS from Temple University. Focuses on the intersection of model intelligence and system design. |

## Overview

Vivek Trivedy (also known as Varun Trivedy or Viv) is the Product Lead for Agents & Harnesses at **LangChain**. He is a leading voice in the emerging field of **Harness Engineering** — the discipline of designing systems, tooling, and execution environments that surround Large Language Models to turn raw intelligence into reliable, autonomous agents.

Trivedy is the primary architect behind **Deep Agents**, LangChain's open-source (MIT), model-agnostic coding agent CLI. His work demonstrates that significant performance gains in agentic coding can be achieved by optimizing the harness (context management, self-verification loops, middleware) rather than just swapping the underlying model.

Prior to LangChain, he was a Senior Health AI Scientist at **AWS** and is completing his PhD in Computer Science at **Temple University**, where his research focused on computer vision and representation learning under Prof. Longin Jan Latecki.

## Core Ideas

### Harness Engineering
> *"Agent = Model + Harness. If you're not the model, you're the harness."*

Trivedy argues that a raw LLM is not an agent; it becomes one only when a harness provides state, tool execution, feedback loops, and enforceable logic. Harness Engineering is about systems — building tooling around the model to optimize for task performance, token efficiency, and latency.

Key components of a harness include:
*   **System Prompts & Tools:** MCPs, skills, and their descriptions.
*   **Bundled Infrastructure:** Filesystem, sandbox, browser, and shell access.
*   **Orchestration Logic:** Sub-agent spawning, handoffs, model routing.
*   **Hooks/Middleware:** Deterministic execution patterns like compaction, continuation, and lint checks.

### The "Reasoning Sandwich" & Compute Allocation
> *"The goal of a harness is to mold the inherently spiky intelligence of a model for tasks we care about."*

In optimizing the Deep Agents CLI for **Terminal Bench 2.0**, Trivedy developed the "reasoning sandwich" heuristic: use maximum reasoning (`xhigh`) for planning and verification, but switch to efficient reasoning (`high`) for implementation steps. This approach reduced timeouts and token burn while boosting scores from 52.8% to 66.5%.

### Self-Verification Loops
> *"Models are biased towards their first plausible solution. Prompt them to aggressively test and verify."*

Trivedy emphasizes that agents naturally want to "early exit" after generating a plausible-looking solution. The harness must force a `Build → Verify → Fix` cycle. The `PreCompletionChecklistMiddleware` intercepts the agent's exit attempt to ensure tests are run and results compared against the task spec.

### Context Engineering & Rot
> *"The more that agents know about their environment, constraints, and evaluation criteria, the better they can autonomously self-direct their work."*

Harnesses must actively manage **Context Rot** (degradation of reasoning as the context window fills) via:
*   **Compaction:** Intelligently summarizing old context.
*   **Tool Call Offloading:** Retaining head/tail tokens of large outputs and dumping the rest to the filesystem.
*   **Progressive Disclosure:** Loading tool front-matter only when needed.

### HaaS (Harness as a Service)
> *"As tasks require more autonomous behavior, the core primitive is shifting from the LLM API to the Harness API."*

Trivedy predicts a future where builders create custom harnesses (like Bolt or Claude Code) and users plug into them to edit further or use as a product. The Claude Code SDK is currently the most mature "batteries-included" way to build and expose usable agents.

## Key Work

### Deep Agents CLI (LangChain)
*   Open-source, model-agnostic terminal-powered coding agent.
*   Built on LangGraph with streaming, persistence, and checkpointing.
*   Scored ~42.5% on Terminal Bench 2.0 with Sonnet 4.5 (on par with Claude Code).
*   **Result:** Jumped from Top 30 to Top 5 on Terminal Bench 2.0 (52.8% → 66.5%) using GPT-5.2-Codex by optimizing the harness only.

### Harbor (Evaluation Framework)
*   Framework for evaluating agents in containerized environments at scale.
*   Orchestrates runs, spins up sandboxes (Daytona), interacts with the agent loop, and runs verification + scoring.
*   Used to run the Terminal Bench 2.0 evaluations for Deep Agents.

### Academic Research (Temple University)
*   PhD work in Computer Vision and Representation Learning.
*   Advisor: Prof. Longin Jan Latecki.
*   Published work on image retrieval with self-supervised divergence minimization.

### AWS Health AI
*   Senior Health AI Scientist at Amazon Web Services.
*   Focus on applying AI/ML to healthcare data and systems.

## Timeline

| Date | Event |
|------|-------|
| 2016–2019 | BS Mathematics & Computer Science, Temple University |
| 2019–2021 | MS Computational Data Science, Temple University |
| 2020 | AWS ML Specialty & Solutions Architect Associate certifications |
| 2021–Present | PhD in CS (AI/ML), Temple University (Latecki Group) |
| Dec 2023 – Jan 2025 | Senior Health AI Scientist, AWS |
| Sep 2025 | Published "The Claude Code SDK and the Birth of HaaS" |
| Oct 2025 | Published "The Modern Planning Agent is Really a Dynamic, Adaptive Workflow Generator" |
| Nov 2025 | Published "Agents Should Be More Opinionated" |
| Dec 2025 | Published "Evaluating Deep Agents CLI on Terminal Bench 2.0" |
| Feb 2026 | Published "Improving Deep Agents with Harness Engineering" |
| May 2026 | Published "Strong Opinions, Loosely Held on Agent + Harness Engineering" — 8-point manifesto on harness design, general-purpose agents, evals as moat, open model cost efficiency, and unbundled agents |
| Dec 2025 – Present | Product Lead, Agents & Harnesses @ LangChain |
| Mar 2026 | Published "The Anatomy of an Agent Harness" |
| Mar 2026 | LangChain open-sourced Deep Agents (MIT License) |

## Blog / Recent Posts

*   **[The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)** (Mar 10, 2026): Defines what a harness is and derives core components (system prompts, tools, infrastructure, orchestration) by working backwards from desired agent behavior.
*   **[Improving Deep Agents with Harness Engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)** (Feb 17, 2026): How the coding agent went from Top 30 to Top 5 on Terminal Bench 2.0 by changing the harness only.
*   **[Agents Should Be More Opinionated](https://www.vtrivedy.com/posts/agents-should-be-more-opinionated/)** (Nov 25, 2025): The best agent products aren't the most flexible, they're the most opinionated.
*   **[The Claude Code SDK and the Birth of HaaS](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service/)** (Sep 23, 2025): Shift from LLM APIs to Harness APIs for autonomous behavior.
*   **[Evaluating Deep Agents CLI on Terminal Bench 2.0](https://www.langchain.com/blog/evaluating-deepagents-cli-on-terminal-bench-2-0/)** (Dec 5, 2025): Benchmark results establishing Deep Agents as a solid starting point.

## Related People

*   : CEO/Co-founder of LangChain; Deep Agents is a key strategic direction.
*   : Co-author on Deep Agents evaluation and Harness Engineering posts.
*   [[ryan-lopopolo]]: Also discusses Harness Engineering; complementary perspectives on agent systems.
*   [[simon-willison]]: Covers AI engineering and agent tools; often discusses similar themes.
*   : PhD Advisor at Temple University.

## X Activity Themes

*   **Harness Engineering:** Deep dives into system design for agents (middleware, context management).
*   **Agent Reliability:** Posts about evaluation, benchmarking (Terminal Bench), and self-verification.
*   **Open Source AI:** Advocating for open harnesses (Deep Agents) and model-agnosticism.
*   **Developer Tools:** Commentary on the evolution of IDEs, CLIs, and agent workflows.

## Strong Opinions, Loosely Held (May 2026)

On May 6, 2026, Viv published an 8-point manifesto "Strong Opinions, Loosely Held on Agent + Harness Engineering" on X ([source](https://x.com/vtrivedy10/status/2052100726608781363)). These opinions generated 542 bookmarks, 377 likes, and substantial discussion from the AI engineering community.

### The 8 Points

| # | Point | Key Claim |
|---|-------|-----------|
| 1 | **Harness > Model** | You can outperform any default harness+model by engineering the harness around the task. Using the exact same model, curate prompts, tools, skills, hooks for that task. The optimization process is becoming agent-driven with humans reviewing evals/rewards to hill climb on. "Just say what you want." |
| 2 | **No General Purpose Agent** | A "general purpose" agent doesn't exist — it's a tradeoff between customization time and performance (cost, latency, accuracy). Who decides what's general? |
| 3 | **If it existed** | A general purpose agent would look like a good coding agent. |
| 4 | **Convergence on Skills** | Task-specific harness optimization will converge to good prompt & tool design packaged as a Skill, as models get better at in-context learning. |
| 5 | **Evals as a Moat** | Evals are a moat, and data to produce evals is a moat. Especially true for vertical agent companies. If evals encode all good behavior, the signal can be hill climbed to improve the agent. |
| 6 | **Open Model Cost Advantage** | Frontier closed models are far too expensive for most tasks. As teams map costs to ROI, Open Model Harness Engineering will take off. A potential 20x+ cost reduction is almost always worth trying. |
| 7 | **Context Window Drives Architecture** | Most design decisions around task decomposition and context engineering exist because our usable context window is 50-100k. Agents that excel at breaking down tasks, applying compaction, and orchestrating subagents will be the most delightful products. |
| 8 | **Age of Unbundled (& Rebundled) Agents** | Subagents exposed as Tools do domain-specific work for an orchestrator agent. The Harness becomes a box populated with exactly the right set of tools, skills, and subagents. Examples: WarpGrep (search), Chroma Context-1 (search), Nemotron 3 Omni (small multimodal), software-as-tools via Skills (Remotion, Blender). |

### Connection to Existing Framework

| Earlier Framework Element | Strong Opinions Extension |
|--------------------------|--------------------------|
| Harness = Model + System | Point 1 formalizes "harness optimization as hill-climbing on evals" |
| Task decomposition | Point 7 traces this to context window limits (50-100k) |
| Sub-agents | Point 8: Subagents-as-Tools as the emerging architecture |
| Open models | Point 6: 20x+ cost reduction as ROI-driven imperative |
| LangChain case studies | Point 5 positions evals as a *moat* rather than just a development tool |

### Community Reception

The post sparked extensive discussion with notable responses:
- **Abhi Katiyar** (RT): "Agree with Viv's points. Today's harnesses are optimized for narrow tasks; the open harnesses are not generalizable."
- **Anna B. Schäfer** and **Harrison Chase**: Discussed starting narrow with harness primitives vs. starting broad
- **Johannes Mauerer**: Discussed model-harness coupling (models can't be swapped between harnesses)
- **Elias Lumer**: Questioned the definition of "general purpose" — Viv clarified it means "decently good at many tasks out of the box" like a coding agent

## Harness, Memory, Context Fragments & the Bitter Lesson (Apr 2026)

Viv's April 2026 post extends Harness Engineering into the dimensions of **memory, retrieval, and context management**, presenting a mental model for the long-term evolution of agents. Dubbed "v30+", it is an iteratively refined thought dump using HTML diagrams.

### Context Fragments

> *"the context window is a precious artifact. Harnesses make decisions on how to populate, manage, edit, and organize it so agents can do work. Each loaded object can be thought of as a Context Fragment and represents an explicit decision by the user and harness designer of what needs a model needs to do work at any given time."*

Viv views the context window not merely as a "container for tokens" but as a **collection of "Context Fragments" selectively loaded by the harness**. Each fragment reflects an explicit decision by the user and harness designer. This idea originates from the pioneering work on "externalizing objects + loading into the context window" proposed by @a1zhang (Alex L. Zhang) in [[concepts/rlm-recursive-language-models]].

### Experiential Memory

> *"agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans). @dwarkesh_sp does a good talking about this massive benefit of artificial systems"*

Agents generate large volumes of data (Traces) with each interaction. Viv treats this as **Experiential Memory** and positions the ability to **share, fork, and accumulate** memory across agents (unlike humans) as its greatest advantage. Memory is treated as an externalized object, and the harness's role is to "retrieve the right data from accumulated memory at the right time and load it into the context window."

### Search & The Bitter Lesson

> *"As we deploy agents in our world over year timescales, there is going to be a hyper-exponential in the amount of data produced by those agents."*

Viv applies Rich Sutton's [[concepts/chatgpt-memory-bitter-lesson]] to agent memory:

1. **Own the data** — Open ecosystems are critical
2. **Use the data** — Search, distillation, and organization are essential

The human brain excels at "contextually retrieving from experience and consolidating important things into memory through deliberate practice." Agent systems need similar capabilities, but current infrastructure and algorithms may break under this new data regime.

### Open Questions

Open questions raised by Viv:

| Question | Implication |
|------|------|
| **Traces → Memory Primitives** | How to efficiently distill experience (traces) into durable memory primitives? |
| **JIT Search vs Weight Integration** | Should search be done just-in-time, or integrated into model weights? |
| **Self-Managing Context** | How can models self-manage their context window? How to reduce error rates when recursively manipulating external objects? |

### Connection to Existing Harness Engineering

This post extends Viv's earlier Harness Engineering framework into the **memory and retrieval dimension**:

| Existing Concept | This Extension |
|-----------|-----------|
| Harness = Model + System | Harness = Model + Context Fragment routing + Memory retrieval |
| Context Rot countermeasures (compaction, offloading) | Context Fragments (each loaded object is an explicit decision) |
| Self-verification loops | Distillation, accumulation, and sharing of experiential memory |
| Terminal Bench optimization | Bitter Lesson — compute leveraged search > human-curated knowledge |

## Related People

*   : CEO/Co-founder of LangChain; Deep Agents is a key strategic direction.
*   : Co-author on Deep Agents evaluation and Harness Engineering posts.
*   [[ryan-lopopolo]]: Also discusses Harness Engineering; complementary perspectives on agent systems.
*   [[simon-willison]]: Covers AI engineering and agent tools; often discusses similar themes.
*   : PhD Advisor at Temple University.
*   [[alex-zhang]]: MIT CSAIL PhD, RLM (Recursive Language Models). Origin of the Context Fragment idea.
*   [[dwarkesh-patel]]: Discussions on agent memory's forkability and accumulability.
*   [[richard-sutton]]: The Bitter Lesson — computation leveraged search > curated knowledge.
