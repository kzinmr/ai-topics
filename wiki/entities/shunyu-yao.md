---
title: "Shunyu Yao (姚顺雨)"
tags: [person]
created: 2026-04-13
updated: 2026-04-24
type: entity
---

# Shunyu Yao (姚顺雨)

## Profile

- **Name:** Shunyu Yao (姚顺雨)
- **X/Twitter:** [@shunyuyao12](https://x.com/ShunyuYao12)
- **Homepage:** [ysymyth.github.io](https://ysymyth.github.io/)
- **Current:** Research Scientist at OpenAI (Computer-Using Agent / CUA)
- **Previous:** Research Scientist at Anthropic (large-scale RL for LLM capabilities), Google DeepMind
- **PhD:** Princeton University (advisor: Karthik Narasimhan), 2019–present
- **Undergrad:** Tsinghua University, Yao Class (姚班), 2015–2019
- **Postdoc:** Berkeley Center for Theoretical Physics (brief, before Anthropic)
- **Physics background:** Stanford Institute for Theoretical Physics work with Douglas Stanford and Stephen Shenker

Shunyu Yao is one of the most influential researchers in the language agent space. His work spans from the foundational ReAct paradigm (2022) through Tree of Thoughts (2023), Reflexion (2023), CoALA (2023–2024), SWE-bench/SWE-agent (2023–2024), and tau-bench (2024–2025). He currently works on Computer-Using Agents at OpenAI. His Google Scholar citations total nearly 16,000, with ReAct and Tree of Thoughts each cited over 4,000 times.

## Core Ideas

### 1. ReAct — Synergizing Reasoning and Acting (2022)

ReAct interleaves **reasoning traces** (thoughts about what to do) with **task-specific actions** (tool calls, environment interactions). This was one of the first demonstrations that LLMs benefit from structured reasoning + acting loops rather than pure next-token generation.

> "The use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner."
> — ReAct paper abstract

**Impact:** ReAct became the standard paradigm for agent frameworks (LangChain, AutoGPT, etc.). Yao showed that reasoning is not just about getting the right answer — it's about the **process** of arriving at it through action-feedback loops.

### 2. Tree of Thoughts — Deliberate Problem Solving (2023)

Tree of Thoughts generalizes Chain-of-Thought by allowing LLMs to explore **multiple reasoning paths** in a search tree, with evaluation and backtracking at each node.

> "ToT frames any problem as a search over a tree of thoughts... The associative 'System 1' of LMs can be beneficially augmented by a 'System 2' based on searching a tree of paths to the solution."
> — Tree of Thoughts paper

**Results:** GPT-4 with CoT solved only 4% of Game of 24 tasks; ToT achieved 74%. This demonstrated that **inference-time compute** (search) can dramatically outperform single-pass reasoning.

### 3. Reflexion — Verbal Reinforcement Learning (2023)

Reflexion reinforces agents through **linguistic feedback** rather than weight updates. Agents maintain an episodic memory of self-reflections and use them to improve future decisions.

> "Reflexion achieves 91% pass@1 on HumanEval, surpassing GPT-4's 80%."
> — Reflexion paper abstract

**Significance:** This paper bridged the gap between RL and language agents — showing that **verbal feedback** in context can serve the same function as gradient-based RL, without the computational cost of fine-tuning. This anticipates the "scaffold vs RL" debate that Yao would later address in "The Second Half."

### 4. CoALA — Cognitive Architectures for Language Agents (2023–2024)

CoALA provides a **unified framework** for understanding language agents as cognitive architectures with:
- **External actions** (grounding): interacting with environments via tools
- **Internal actions** (reasoning, retrieval, learning): manipulating internal memory and thoughts
- **Short-term working memory** and **long-term memories** (episodic, semantic)

> "CoALA neatly specifies a language agent starting with its action space, which has 2 parts: External actions for grounding, Internal actions for reasoning, retrieval, learning."
> — CoALA paper

**Impact:** CoALA became the standard taxonomy for classifying agent architectures and is referenced in the awesome-language-agents repository with 1,197 stars.

### 5. SWE-bench & SWE-agent — Real-World Software Engineering (2023–2024)

**SWE-bench** evaluates LLMs on their ability to resolve real-world GitHub issues. **SWE-agent** provides an Agent-Computer Interface (ACI) optimized for software engineering tasks.

> "We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language agents."
> — SWE-bench paper abstract

**Results:** SWE-bench established that coding benchmarks must measure **real-world problem resolution**, not just code generation. SWE-agent achieved state-of-the-art results by designing the interface specifically for agent capabilities rather than human usability.

### 6. tau-bench — Tool-Agent-User Interaction (2024–2025)

tau-bench tests agents on **multi-turn conversations** with simulated human users, where agents must use domain-specific APIs while following policy guidelines.

> "Even state-of-the-art function calling agents (like GPT-4o) succeed on <50% of tasks, and are quite inconsistent (pass^8 < 25% in retail)."
> — tau-bench paper abstract

**Key insight:** The **pass^k** metric measures reliability across k independent trials — a critical dimension for real-world deployment that single-shot benchmarks miss.

### 7. Computer-Using Agent (CUA) at OpenAI (2024–present)

Yao's current work at OpenAI focuses on agents that can **perceive and act on computer screens** — navigating websites, filling forms, and performing digital automation tasks.

**Related:** Microsoft's Fara-7B benchmarked against CUA systems shows OpenAI's computer-use-preview achieving 70.9% on WebVoyager. Yao's CUA work is foundational to OpenAI's agent strategy.

### 8. "The Second Half" — RL Generalization and the Future of AI (2025)

Yao's most philosophical blog post argues that **RL has finally generalized** across domains, marking a paradigm shift:

> "In three words: RL finally works. More precisely: RL finally generalizes. After several major detours and a culmination of milestones, we've landed on a working recipe to solve a wide range of RL tasks using language and reasoning."

**The Recipe:**
- Massive language pre-training
- Scale (data and compute)
- Reinforcement learning with language as the action space
- Reasoning as a form of action that doesn't directly affect the external world

**The Shift:** From "problem-solving" to "problem-defining":
> "The second half of AI — starting now — will shift focus from solving problems to defining problems. In this new era, evaluation becomes more important than training."

**Three components of RL through Yao's lens:**
1. **Algorithm** — "the trivial part" (PPO, GRPO, etc.)
2. **Environment** — where the agent interacts (most important)
3. **Priors** — what the agent brings (language pre-training is a powerful prior)

Yao's key insight:
> "Thinking, or reasoning, is a strange kind of action — it does not directly affect the external world, yet the space of reasoning is vast. By adding reasoning into the action space of any RL environment, we make use of the language pre-training priors to generalize."

This connects directly to **Alex Zhang's RLM** work — both treat reasoning as an action within an environment, and both recognize that the environment design is the bottleneck, not the algorithm.

## Key Publications

| Year | Title | Venue | Citations* |
|------|-------|-------|-----------|
| 2022 | ReAct: Synergizing Reasoning and Acting in LLMs | ICLR 2023 (Oral, top 5%) | 6,598+ |
| 2023 | Tree of Thoughts: Deliberate Problem Solving | NeurIPS 2023 (Oral) | 3,606+ |
| 2022 | WebShop: Scalable Real-World Web Interaction | NeurIPS 2022 | 887+ |
| 2023 | Reflexion: Language Agents with Verbal RL | NeurIPS 2023 | — |
| 2023 | CoALA: Cognitive Architectures for Language Agents | TMLR 2024 | 4,511+ |
| 2023 | SWE-bench: Can LLMs Resolve Real-World GitHub Issues? | ICLR 2024 (Oral) | — |
| 2024 | SWE-agent: ACI for Software Engineering | NeurIPS 2024 | — |
| 2024 | tau-bench: Tool-Agent-User Interaction | ICLR 2025 | — |
| 2024 | FireAct: Toward Language Agent Fine-tuning | — | — |
| 2024 | PhD Thesis: Language Agents: From Next-Token Prediction to Digital Automation | Princeton | — |
| 2025 | Contextual Experience Replay for Self-Improvement | ACL 2025 | — |

*Google Scholar citation counts (approximate, as of early 2026)

## Blog Posts & Public Commentary

| Date | Title | Key Insight |
|------|-------|-------------|
| Oct 2025 | "The Second Half" | RL has generalized; evaluation > training; problem-defining > problem-solving |
| Feb 2026 | "My infant year as an AI researcher" | Personal reflection on early research career |
| Ongoing | Online Talks | "Language Agents: From Next-Token Prediction to Digital Automation" |

## Career Timeline

1. **2015–2019:** Tsinghua University, Yao Class (姚班) — theoretical computer science foundation
2. **2019–2024:** Princeton PhD under Karthik Narasimhan — language agents, grounding, reasoning
3. **2019–2021:** Collaboration with Matthew Hausknecht on text game agents
4. **2022–2023:** ReAct, WebShop, Tree of Thoughts — foundational agent paradigms
5. **2023:** Anthropic — large-scale RL for LLM capabilities
6. **2023–2024:** Reflexion, CoALA, SWE-bench — cognitive architectures and real-world evaluation
7. **2024–present:** OpenAI — Computer-Using Agent (CUA)
8. **2025:** "The Second Half" blog post articulating the shift from training to evaluation
9. **2025:** tau-bench, SWE-agent — multi-turn evaluation and agent-computer interfaces

## Connection to Alex Zhang's RLM

Yao's "Second Half" framework and Zhang's RLM work converge on a critical insight: **the environment is the bottleneck**.

| Yao's Framework | Zhang's RLM | Convergence |
|-----------------|-------------|-------------|
| "Environment is the key component of RL" | "Context is an environment (REPL)" | Both treat interaction as fundamental |
| "Reasoning is an action in the RL space" | "Model writes code to manage context" | Both externalize computation |
| "Evaluation > Training" | "RLM-Qwen3-8B beats Qwen3-8B by 28.3%" | Both validate via empirical benchmarks |
| "RL finally generalizes" | "RLMs trained with RL will be next milestone" | Both see RL-trained scaffolds as future |

Prime Intellect (building on both researchers' work) captures the synthesis:
> "Teaching models to manage their own context end-to-end through reinforcement learning will be the next major breakthrough."

## Quotes

> "RL finally works. More precisely: RL finally generalizes. After several major detours and a culmination of milestones, we've landed on a working recipe to solve a wide range of RL tasks using language and reasoning."
> — Shunyu Yao, "The Second Half" (2025)

> "The second half of AI — starting now — will shift focus from solving problems to defining problems. In this new era, evaluation becomes more important than training."
> — Shunyu Yao, "The Second Half" (2025)

> "Thinking, or reasoning, is a strange kind of action — it does not directly affect the external world, yet the space of reasoning is vast. By adding reasoning into the action space of any RL environment, we make use of the language pre-training priors to generalize."
> — Shunyu Yao, "The Second Half" (2025)

> "We can understand this by looking through the lens of reinforcement learning (RL), which is often thought of as the key to unlocking AGI... In RL, there are three key components: algorithm, environment, and priors. For a long time, RL researchers focused on the algorithm... but the algorithm is the trivial part."
> — Shunyu Yao, "The Second Half" (2025)

> "You can't connect the dots looking forward; you can only connect them looking backward."
> — Shunyu Yao, "The Second Half" (2025), quoting Steve Jobs

## Related Concepts

- **[[overreacted-io]]** — Yao's foundational reasoning+acting paradigm
- **[[concepts/tree-of-thoughts]]** — Search-based deliberation for LLMs
- **[[concepts/reflexion]]** — Verbal reinforcement learning
- **[[concepts/coala]]** — Cognitive architectures for language agents
- **[[concepts/swe-bench]]** / **[[concepts/swe-agent]]** — Real-world code evaluation
- **[[concepts/tau-bench]]** — Tool-Agent-User interaction benchmark
- **[[concepts/computer-using-agent]]** — Yao's current work at OpenAI
- **** — Designing environments for agents
- **** — Yao argues for environment-first RL design
- **[[concepts/rlm-recursive-language-models]]** — Zhang/Khattab/Kraska's parallel work on environment-first context management
- **** — Yao's philosophical framework for AI's future

## Status

- **Entity status:** Full (L1+L2+L3 complete)
- **Quality target:** ~14KB, high quote rate (>30%), conceptual connections mapped
- **Cross-connections:** Alex Zhang (RLM/environment design), Omar Khattab (ColBERT→RLM lineage), Karthik Narasimhan (advisor lineage), Noah Shinn (Reflexion, Sierra)
- **Next enrichment:** Monitor CUA developments at OpenAI, "Second Half" reception in community, tau-bench v3 results
- **Last updated:** 2026-04-13
