---
title: "Karpathy RL Agents — Agentic Research Loop"
type: concept
aliases:
  - karpathy-loop
  - autoresearch
  - karpathy-agentic-engineering
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - person
status: draft
sources:
  - "https://www.sahmcapital.com/news/content/andrej-karpathy-says-ai-agents-are-rewriting-how-software-gets-built-adds-he-hasnt-typed-a-line-of-code-probably-since-december-2026-03-22"
  - "https://www.youtube.com/watch?v=kwSVtQ7dziU"
  - "https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html"
  - "https://github.com/karpathy/autoresearch/"
  - "https://blog.gopenai.com/the-karpathy-loop-how-a-630-line-script-is-rewriting-the-rules-of-ai-research-21190138f253"
---

# Karpathy RL Agents — Agentic Research Loop

**Autonomous Research Loop** pattern proposed by Andrej Karpathy. March 2026 [AutoResearch](https://github.com/karpathy/autoresearch/) project and elaborated on the [No Priors podcast](https://www.youtube.com/watch?v=kwSVtQ7dziU).

## Core Philosophy

### The "Loopy Era" of AI
> "One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies."

Karpathy declared that AI research has shifted from "intermittent experiments by human researchers" to "autonomous continuous improvement by agents." He calls this **"The Loopy Era."**

### The Shift from Vibe Coding to Agentic Engineering
From coining "Vibe Coding" in 2025 to "Agentic Engineering" in 2026:

> "In 2025, he created and popularized the term Vibe coding. Anyone can describe what they want and get working software. In 2026, he says we are Agentic engineering. Humans no longer write most code. We direct, supervise, and orchestrate agents."

### The Changing Role of Humans
> "You are not typing computer code. You are now spinning up AI agents."
> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change."

Since December 2025, Karpathy has publicly stated that he no longer writes raw code himself. The human role has shifted from **writing code** to **supervising, directing, and designing environments for agents.**

## AutoResearch: The Karpathy Loop

### How It Works
[karpathy/autoresearch](https://github.com/karpathy/autoresearch/) — A 630-line Python script enabling agents to conduct LLM research autonomously:

1. The agent reads `train.py` (single-GPU nanochat)
2. Forms hypotheses ("What if we increase attention depth?" "What if we adjust AdamW beta parameters?")
3. Modifies the code
4. Runs experiments with a **fixed 5-minute budget**
5. Checks validation metrics (`val_bpb`)
6. Commits if improved, reverts if not
7. Next morning, experiment logs and (hopefully) a better model await

### Results
- **700 experiments in 2 days** executed autonomously
- **20 optimizations** discovered and applied
- GitHub: 60,000+ stars, 10,000+ forks
- Featured by Fortune magazine as "The Karpathy Loop"

### program.md Pattern
> "The bottleneck in AI research has never been compute — it's been the human researcher, distracted by meetings."

Instructions to agents are given as natural language Markdown files (`program.md`). This is the **new programming interface:**

```markdown
# Research Program
- Test learning rate schedules: cosine vs linear vs constant
- Try batch sizes: 32, 64, 128, 256
- For each combo, train for exactly 5 minutes
- Log val_bpb after each run
- If val_bpb improves by >0.01, commit the change
```

## Dobby: AI Home Assistant

Karpathy built an AI home assistant called "Dobby":

> "So Dobby is in charge of the house," he said, noting the system can even detect deliveries via security cameras and automatically send alerts.

Managing lighting, climate, and security via natural language commands on WhatsApp. An example of agents autonomously executing real-world tasks.

## MicroGPT: Minimal GPT Implementation for Education

> "MicroGPT (Feb 2026 release) a GPT trained from scratch in 243 lines of pure Python + basic math—no PyTorch."

Successor to nanoGPT and llm.c. Designed so both agents and humans can understand the algorithms.

## Relationships with Related People and Projects

| Person/Project | Relationship with Karpathy |
|-------------------|-----------------|
| [[entities/simon-willison]] | Both advocate "Agentic Engineering." Willison emphasizes quality/testing, Karpathy emphasizes autonomous loops |
| [[entities/ryan-lopopolo]] | Lopopolo's Harness Engineering shares Karpathy's Loopy Era philosophy — "designing environments that move agents" |
| [[entities/boris-cherny]] | Cherny's CLAUDE.md and Karpathy's program.md follow the same paradigm — context files as the agent control layer |
| [nanochat](https://github.com/karpathy/nanochat) | Single-GPU LLM implementation that served as the base for AutoResearch |

## Karpathy's Definition of Agentic Engineering

> "Agentic engineering: Humans no longer write most code. We direct, supervise, and orchestrate agents. Technical expertise is still a multiplier, but the bits humans contribute are sparse and rare."

### Differences from Willison
| Dimension | Willison | Karpathy |
|------|----------|----------|
| Focus | Test-first, cognitive debt management | Autonomous loops, 5-min experiment budget |
| Human involvement | Humans make final decisions | Humans only supervise and design environments |
| Representative projects | Datasette, LLM | AutoResearch, MicroGPT |
| Metrics | Code quality, test coverage | Experiment count, metric improvement |

## Related Concepts

- [[concepts/harness-engineering/agentic-workflows/interactive-explanations]] — Parent concept
- [[concepts/harness-engineering]] — Lopopolo's environment design approach
- [[concepts/context-engineering]] — CLAUDE.md/program.md patterns
-  — Autonomous research concept
