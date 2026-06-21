---
title: "ML Research Practice"
type: concept
created: 2026-06-16
updated: 2026-06-16
tags:
  - ml-research
  - career
  - methodology
  - reinforcement-learning
  - optimization
sources:
  - raw/articles/2020-01-24_joschu_opinionated-guide-ml-research.md
---

# ML Research Practice

A systematic guide to ML research methodology — problem selection, progress management, and personal growth. Written by [[entities/john-schulman]] for the 2017 OpenAI Fellows program, publicly released in 2020.

## Choosing Problems

### Developing Taste

The ability to choose problems is more important than raw technical skill. It can be accelerated through:

1. **Read papers extensively and critique them** — discuss with people who have deep knowledge
2. **Work in research groups on similar topics** — absorb others' experience
3. **Seek advice from experienced researchers** — ideas are cheap, execution matters
4. **Regularly reflect on what constitutes useful research** — when is theory useful? When are empirical results transferable?

The biggest bursts of influential work are concentrated in a small number of research groups. This isn't because they are overwhelmingly better, but because they have **high density of expertise and perspective**.

### Idea-Driven vs Goal-Driven

| | Idea-Driven | Goal-Driven |
|---|---|---|
| **Motivation** | Reading a paper and thinking "I can do better" | Having a vision of new AI capabilities and solving toward it |
| **Risk** | High overlap with others, being scooped | Taking goals too literally |
| **Advantage** | Directly leverages existing knowledge | Differentiated perspective, enables team coordination |
| **Recommended** | For experienced researchers | Recommended for most people |

Schulman recommends Goal-Driven. By choosing different problems, you explore ideas that differ from the community.

### Case Study: Schulman's PhD

- **First half**: Robotic deformable object manipulation → trajectory optimization became the most impactful byproduct
- **Second half**: RL for 3D locomotion → focus on policy gradient → TRPO, GAE, PPO
- During the DQN boom many jumped to Q-learning, but Schulman judged it unsuitable for locomotion tasks and continued with policy gradient → **different problem choices led to different idea exploration**

### Constraining to General Solutions

Goal-Driven pitfall: achieving the goal too literally can lead to solutions that don't advance ML. **Solutions should be constrained to be general and potentially applicable to other problems.**

### High Goals and Incremental Improvement

- What is the potential upside? 10% improvement or 10X improvement?
- AlexNet (2012) had no revolutionary new components — **it stacked many small improvements**
- Incremental improvements are only useful in the context of a big goal. Avoid complexity that doesn't match the improvement magnitude

## Making Continual Progress

### Notebooks and Reviews

Record daily ideas and experiments, review every 1-2 weeks:

- **Experiment results** — what was discovered
- **Insights** — from yourself, colleagues, and papers
- **Code progress** — what was implemented
- **Next steps** — future work

Three values: (1) immediate recording and revisiting of ideas, (2) centralized experiment results, (3) **visualization of time usage** — self-monitoring for excessive jumping between ideas

### When to Switch Problems

> **Switching too often (giving up on promising ideas too early) is a more common failure pattern than switching too little**

- When looking back monthly, most time should be spent on projects that lead to deliverables (papers, blog posts)
- If significant time is spent on incomplete projects, strengthen consistency and follow-through
- **ε-greedy exploration**: spend one day a week on something different from the main project

## Personal Development

### Investing in Knowledge Building

Beyond current projects, **allocate some time to improving general ML knowledge**. Otherwise, you'll _plateau_ on the foundational knowledge needed for daily work.

- **Textbooks**: denser than papers. Systematize decades of ideas in unified notation
  - Recommended: *Numerical Optimization* (Nocedal & Wright), *Elements of Information Theory* (Cover & Thomas)
- **PhD theses**: (1) Introduction/Background and (3) Conclusions/Outlook are most valuable — expert unified perspective
- **Paper reimplementation**: far deeper understanding than passive reading. Fast feedback against known performance levels. When you can easily reproduce SOTA, you're ready to exceed it

## Implications for 2026

Although this article was written in 2017, its essence directly applies to AI research and development in 2026:

### 1. Goal-Driven > Idea-Driven (Even More Important in the Agent Era)

In 2026, AI agent development is driven by concrete goals like "make X work." Goal-driven development is mainstream through tools like Cursor, [[concepts/coding-agents/claude-code]], and [[concepts/coding-agents/openai-codex]].

### 2. Constraining to General Solutions (Aligns with RLHF's Essence)

Schulman's pursuit of generality in locomotion tasks mirrors the design philosophy of [[concepts/post-training/rlhf]] — learning broadly from human feedback rather than optimizing for specific tasks.

### 3. Notebook Culture → Agent Memory

Schulman's notebook and review methodology corresponds to the design principles of [[concepts/agent-memory/agent-memory-systems]] and [[concepts/agent-memory/context-engineering]]. The mechanisms by which agents record and revisit past experiments and insights are essentially an automation of this research habit.

### 4. The Importance of Textbooks (Reevaluating Fundamentals)

Even in the 2026 LLM era, foundational understanding of optimization theory and information theory is essential for [[concepts/post-training/training]] and [[concepts/post-training/post-training]]. Schulman's point that textbooks are denser than papers remains valid.

### 5. ε-Greedy Exploration (Agent Design as Multi-Armed Bandit)

In [[concepts/agent-architecture/agent-architecture]] design, balancing the main strategy with exploration is a critical design decision. [[concepts/test-time-scaling/test-time-scaling]] is itself about the explore-exploit tradeoff during inference.

## Related

- [[entities/john-schulman]] — Author. Developer of PPO, TRPO, RLHF
- [[concepts/post-training/rlhf]] — Schulman's most influential contribution
- [[concepts/post-training/reinforcement-learning]] — Schulman's primary technical domain
- [[concepts/coding-agents/coding-agents]] — The 2026 embodiment of Goal-Driven research
- [[concepts/agent-memory/context-engineering]] — The agent counterpart of notebook culture
- [[concepts/test-time-scaling/test-time-scaling]] — The inference-time version of ε-greedy exploration
