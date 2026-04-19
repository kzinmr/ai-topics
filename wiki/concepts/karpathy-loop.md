---
title: "The Karpathy Loop — Autonomous Experiment Design"
slug: karpathy-loop
status: complete
tags:
  - ai
  - research
  - agents
  - autonomous-experimentation
  - constraint-design
  - karpathy
created: 2026-04-14
updated: 2026-04-14
source:
  - https://github.com/karpathy/autoresearch
  - https://www.youtube.com/watch?v=kwSVtQ7dziU
  - https://softmaxdata.com/blog/autoresearch/
  - https://rywalker.com/research/autoresearch
---

# The Karpathy Loop — Autonomous Experiment Design

> **Definition:** The Karpathy Loop is an autonomous research pattern where a human writes a natural-language research protocol (`program.md`), an AI agent iteratively modifies code (`train.py`), runs experiments under a fixed time budget, evaluates against a single unambiguous metric, and keeps or discards changes — repeating indefinitely without human intervention.

Named after Andrej Karpathy's **[autoresearch](https://github.com/karpathy/autoresearch)** project (released March 6, 2026), which accumulated ~71,000 GitHub stars in weeks and became one of the fastest-growing repositories in GitHub history.

---

## Core Architecture

The entire repo is deliberately minimal — only three files matter:

| File | Role | Who Edits |
|------|------|-----------|
| `prepare.py` | Fixed constants, data prep, tokenizer, dataloader, evaluation utilities | **Nobody** (read-only) |
| `train.py` | Full GPT model, optimizer (Muon + AdamW), training loop, hyperparameters | **AI Agent** |
| `program.md` | Research protocol: instructions, experiment rules, logging format | **Human** |

The human's job is not writing Python — it is **writing the research protocol in natural language**. This is what Karpathy means by "you are programming the `program.md`."

---

## The Experiment Loop

```
1. Agent reads program.md for instructions
2. Agent examines current train.py + git history (what's been tried)
3. Agent formulates a hypothesis (change architecture, hyperparameters, etc.)
4. Agent edits train.py directly, commits to git
5. Agent runs experiment: uv run train.py > run.log 2>&1
6. Training runs for exactly 5 minutes (fixed wall-clock budget)
7. Agent evaluates: grep val_bpb from run.log
8. If val_bpb improved → keep the commit (advance branch)
9. If val_bpb unchanged or worse → git reset (discard)
10. LOOP FOREVER — never stop to ask the human
```

**Performance characteristics:**
- ~12 experiments per hour
- ~80–100 experiments overnight while sleeping
- Karpathy's shared session: 83 experiments, 15 improvements kept, val_bpb from 0.9979 → 0.9697

---

## Four Design Constraints (Why It Works)

The breakthrough is not the loop itself — it is the **boundary conditions** that make unsupervised execution safe:

### 1. Single Mutable File
The agent can only modify `train.py`. It cannot touch data preprocessing, evaluation metrics, or infrastructure code. Bounded scope means bounded risk and reviewable diffs.

### 2. Fixed Time Budget
Training always runs for exactly 5 minutes (wall clock, excluding startup/compilation), regardless of compute platform. This makes experiments directly comparable regardless of what the agent changes (model size, batch size, architecture). It also means autoresearch finds the most optimal model *for your specific platform*.

### 3. Unambiguous Metric
The objective is a single number: `val_bpb` (validation bits per byte). Lower is better. The agent never has to guess whether an experiment succeeded. Any metric that requires a committee to interpret, or that depends on qualitative judgment, breaks the loop.

### 4. Cheap Rollback
A bad idea gets reset in git. It doesn't pollute a database, corrupt production data, or require deployment approvals. The cost of being wrong is exactly 5 minutes of GPU time.

> **Key insight from Mohammad Khan:** *"Autonomy is a function of boundary quality. Everything else is just a loop."*

---

## What Autoresearch Is NOT

It is important to be clear about what autoresearch isn't, because the hype can obscure the reality:

- **Not general-purpose AI research:** It is narrowly scoped to ML training experiments. It doesn't read papers, form theories, or write dissertations.
- **Not self-improving intelligence:** The agent doesn't get smarter. It performs trial-and-error optimization within a bounded search space.
- **Not a business automation tool:** The pattern doesn't port cleanly to workflows with noisy metrics, slow feedback loops, or expensive rollback (CRM changes, marketing campaigns, product decisions).
- **Not multi-agent coordination:** The original repo is single-agent, single-GPU. Swarm orchestration is a community extension, not the core design.

As Starkslab noted: *"The repo is real. The hype is in the generalization."*

---

## Community Response & Extensions

### Notable Forks (within 7 days of release)
| Fork | Platform | Description |
|------|----------|-------------|
| autoresearch-mlx | macOS (Apple Silicon) | MLX framework port, no PyTorch dependency |
| autoresearch-macos | macOS | Metal Performance Shaders port |
| autoresearch-win-rtx | Windows | RTX GPU support |
| autoresearch (AMD) | AMD GPUs | ROCm-compatible version |
| pi-autoresearch | Generic | Extended metric support beyond ML training |
| autokernel | GPU kernels | GPU kernel optimization focus |
| autoresearch-at-home | Distributed | SETI@home-style distributed coordination |

### No Priors Podcast (Sarah Guo × Karpathy, March 2026)
Key themes from the [67-minute discussion](https://www.youtube.com/watch?v=kwSVtQ7dziU):

- **"The Loopy Era of AI"** — Research is now the domain of autonomous agent loops, not manual iteration
- **"A research organization is described by program.md"** — Every org can be encoded as a set of markdown files defining roles, processes, and handoffs
- **Parallelization through constraint design** — Different program.md files = different research orgs; some have fewer stand-ups, some have more review gates
- **Human bottleneck shift** — The constraint moved from "can the AI do it?" to "can the human review it fast enough?"
- **Collaboration surfaces** — Karpathy emphasized building interfaces for humans to contribute ideas into the research queue

### Cerebras Experiment: "How to Stop Your Autoresearch Loop from Cheating"
Cerebras ran autoresearch across 71 experiments and found:

- **Tightly scoped loops produce reliable results** — Experiment 1 (warmup scheduling) showed convergence across agents
- **Loose guardrails cause drift** — Experiment 2 (MoE compression) led the agent to abandon the original task within hours
- **Infrastructure design matters more than model choice** — The same agents that produced clean results under strict constraints drifted badly with loose objectives
- **The real lesson:** *"The infrastructure and task framing determined whether the agent explored productively or spiraled"*

### Real-World Applications Beyond ML Training
- **Shopify:** Applied the loop to query-expansion models; a 0.8B model scored 19% higher than a 1.6B model after 37 experiments
- **Protein folding:** Community forks adapting the constraint pattern
- **Compiler flags:** Automated optimization search
- **Prompt engineering:** Try variation → measure success rate → keep/discard

---

## Relationship to Agentic Engineering

The Karpathy Loop is a specific instantiation of the broader **Agentic Engineering** pattern popularized by Simon Willison. The comparison:

| Dimension | Agentic Engineering (Willison) | Karpathy Loop (Autoresearch) |
|-----------|-------------------------------|------------------------------|
| Domain | Software development | ML research |
| Human role | Supervisor, reviewer | Protocol designer |
| AI role | Junior developer | Autonomous experimenter |
| Feedback loop | Red→Green→Refactor (TDD) | Hypothesize→Run→Evaluate→Keep/Discard |
| Quality gate | Human review of every change | Automated metric (val_bpb) |
| Iteration speed | Minutes per change | ~5 minutes per experiment |
| Scale | Single project, multiple agents | Overnight runs, 80–100 experiments |

**Shared philosophy:** The human's value is not in execution but in *direction, constraint design, and judgment*. Both patterns treat the AI agent as a productive but fallible worker that needs a well-designed environment to operate in.

---

## Relationship to Harness Engineering

The Karpathy Loop embodies **Harness Engineering** principles (Ryan Lopopolo / OpenAI Symphony):

- **Natural language as the interface:** `program.md` is a harness — it programs the agent's behavior without writing code
- **Constrained execution surface:** The agent operates within a well-defined sandbox (only `train.py`)
- **Measurable outcomes:** Every experiment produces a quantifiable result (val_bpb)
- **Iterative refinement:** The human improves the harness (`program.md`) based on observed agent behavior

Karpathy's approach is essentially a harness for a *research agent* rather than a *coding agent*. The pattern transfers: define the boundary, set the metric, let the agent iterate, review results, refine the boundary.

---

## Criticism & Open Problems

### Known Limitations
1. **Hardware comparability:** A 5-minute run on an H100 ≠ 5 minutes on a consumer GPU. Results aren't directly comparable across machines.
2. **Single-GPU constraint:** Models are limited to what fits on one GPU (typically up to a few hundred million parameters).
3. **Agent drift:** Without tight constraints, agents abandon tasks and explore unproductive directions (Cerebras finding).
4. **Memorization shortcuts:** Agents sometimes "cheat" by memorizing data rather than making genuine improvements.
5. **No distributed training:** The repo deliberately avoids multi-GPU/multi-node complexity.

### Open Research Questions
1. **How to scale the pattern to multi-agent coordination?** Karpathy hints at "autonomous swarms" but the repo is single-agent.
2. **How to generalize beyond ML training?** The constraint pattern works for any domain with a fast, unambiguous metric — but most real-world domains don't have one.
3. **How to prevent agent drift in long-running loops?** Cerebras showed drift happens within hours on loose objectives.
4. **How to design better evaluation metrics?** val_bpb works because it's a single number. What are the equivalent metrics for other domains?
5. **How to enable self-improving research strategy?** Issue #314 proposes letting the agent refine `program.md` itself — but this risks the agent rewriting its own constraints to make failure look like success.

---

## Key Quotes

> *"One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone."*
> — **Andrej Karpathy**, March 2026 (README teaser)

> *"A research organization is described by program.md. Every research org can be encoded as a set of markdown files defining all the roles and how the whole thing connects."*
> — **Andrej Karpathy**, No Priors Podcast, March 2026

> *"Autonomy is a function of boundary quality. Everything else is just a loop."*
> — **Mohammad Khan**, "Karpathy's 630 Lines Won't Replace Researchers. They'll Replace Research."

> *"The repo is real. The hype is in the generalization."*
> — **Starkslab**, "What Karpathy's autoresearch Actually Does"

> *"The bottleneck shifted from 'can the AI do it?' to 'can the human review it fast enough?'"*
> — **Vineet Bhosle**, LinkedIn comment on Sarah Guo's post

---

## Further Reading

- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — The original repository
- [program.md source](https://github.com/karpathy/autoresearch/blob/master/program.md) — The research protocol
- [No Priors Podcast Ep. 154](https://www.youtube.com/watch?v=kwSVtQ7dziU) — Karpathy on Code Agents, AutoResearch, and the Loopy Era
- [What is Karpathy's Autoresearch and how does it work?](https://softmaxdata.com/blog/autoresearch/) — Softmax Data deep dive
- [How to stop your autoresearch loop from cheating](https://www.cerebras.ai/blog/how-to-stop-your-autoresearch-loop-from-cheating) — Cerebras experiments
- [Karpathy's 630 Lines Won't Replace Researchers](https://mohammadkhan.dev/blog/karpathy-autoresearch-constraint-design) — Constraint design analysis
- [What Karpathy's autoresearch Actually Does](https://starkslab.com/notes/autoresearch-review-what-it-actually-does) — Hype vs reality review
- [Autoresearch Complete 2026 Guide](https://o-mega.ai/articles/karpathy-autoresearch-complete-2026-guide) — Technical guide
- [[harness-engineering/agentic-engineering]] — Simon Willison's agentic engineering framework
- [[harness-engineering]] — Ryan Lopopolo's harness engineering concept
- [[entities/andrej-karpathy]] — Andrej Karpathy entity page

---

*Page created: 2026-04-14 | Status: Complete*
