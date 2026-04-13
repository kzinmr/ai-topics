---
title: Alex L. Zhang
description: MIT CSAIL PhD student (Khattab, Kraska). Creator of Recursive Language Models (RLMs), KernelBench (ICML 2025 Best Paper), GPU MODE. "Language models will be scaffolds."
aliases:
  - alex-zhang
  - alexlzhang
  - a1zhang
twitter: https://x.com/a1zhang
github: https://github.com/alexzhang13
website: https://alexzhang13.github.io/
status: complete
depth_tracking:
  created: 2026-04-13
  last_updated: 2026-04-13
  target_depth: antirez/simon-willison quality
  key_works: [RLM, KernelBench, GPU MODE, VideoGameBench]
  quote_sources:
    - "Language models will be scaffolds" (X/Twitter, 2025)
    - RLM blogpost (Oct 2025), arXiv paper (Dec 2025)
    - ICML 2025 Best Paper: KernelBench
related:
  - rlms
  - omar-khattab
  - tim-kraska
  - gpu-mode
  - kernelbench
  - akira-realmcore
  - slate
---

# Alex L. Zhang (@a1zhang)

**Position:** PhD Student, MIT CSAIL (OASYS Lab)

**Advisors:** Omar Khattab, Tim Kraska

**Domain:** Inference-time scaling, Recursive Language Models, GPU kernel optimization, LLM evaluation

**Core Thesis:**
> *"Language models will be scaffolds."*
> — Alex Zhang, on the future of LLMs as structural frameworks rather than end products

---

## Profile

Alex L. Zhang is a PhD student at MIT CSAIL in the OASYS lab, advised by **Omar Khattab** (DSPy, ColBERT) and **Tim Kraska** (databases, ML systems). His research centers on **inference-time computation** — how LLMs can programmatically manage their own reasoning, context, and execution environments to achieve capabilities beyond what context windows allow.

**Background:**
- Princeton CS department top graduate; mentors: Karthik Narasimhan, Khanh Nguyen, Ofir Press, Kai Li
- Founded and ran Princeton's largest AI student organization
- Interned at Snapchat, Apple, Claryo (AI/ML research)
- Sakana AI (Tokyo, summer 2025)
- VantAI (NYC, 1 year, AI-based drug discovery)
- Previously made and sold PC games (~100k+ players for one title)

He is the first author of **Recursive Language Models (RLMs)**, a paradigm that treats long prompts as external state and allows LLMs to recursively decompose and query their own context. He also created **KernelBench** (ICML 2025 Best Paper), **GPU MODE** (community event for GPU kernel optimization), **VideoGameBench**, and **SWE-bench Multimodal**.

---

## RLM: Recursive Language Models (2025)

**Paper:** arXiv:2512.24601 (December 2025, revised January 2026)
**Co-authors:** Alex L. Zhang, Tim Kraska, Omar Khattab
**Blog:** [Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/) (October 2025)
**Code:** [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm) (3,296⭐, 604 forks, 20 contributors)
**Minimal implementation:** [github.com/alexzhang13/rlm-minimal](https://github.com/alexzhang13/rlm-minimal)

RLM is Zhang's flagship contribution — an **inference-time scaling paradigm** that fundamentally rethinks how LLMs handle long context.

### The Core Idea

> *"We propose Recursive Language Models, or RLMs, a general inference strategy where language models can decompose and recursively interact with their input context as a variable."*

Standard LLM APIs: `llm.completion(prompt, model)`
RLM API: `rlm.completion(prompt, model)` — drop-in replacement

Instead of stuffing everything into the context window, RLM:
1. **Stores long context as a variable** in an external environment (Python REPL/Jupyter)
2. **Root LM (Depth=0)** receives only the query + environment pointer — never sees full context directly
3. **LM writes code** to `peek`, `grep`, `partition`, or `transform` the context
4. **Spawns sub-LM calls** (Depth=1+) on specific subsets via `llm_query()`
5. **Composes results** into a final answer via `FINAL(...)` or `FINAL_VAR(...)`

```python
from rlm import RLM

rlm = RLM(
    backend="openai",
    backend_kwargs={"model_name": "gpt-5-mini"},
    environment="local",
)
result = rlm.completion("Analyze this 10M-token document...")
```

### The "Context Rot" Problem

> *"Anthropic defines context rot as 'when the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases', but many researchers in the community know this definition doesn't fully hit the mark... it's almost like, as the conversation goes on, the model gets…dumber?"*
> — Alex Zhang, RLM blogpost

Zhang observed that standard benchmarks (RULER) show 90%+ accuracy, but **real-world** long conversations or bloated code histories cause models to degrade. His hypothesis: long sequences are **out-of-distribution (OOD)** for training data due to higher entropy and lack of natural occurrence. RLMs bypass this entirely by never feeding full context to a single call.

**Critical finding:** GPT-5-mini degrades faster than GPT-5 as context grows, confirming that **context rot severity scales with model size/capability** — smaller models lose coherence more rapidly when overloaded with context.

### RLM Architecture: REPL-Based Execution

The core loop operates via a persistent **REPL (Read-Eval-Print Loop)** environment:

```python
state ← InitREPL(prompt=P)
state ← AddFunction(state, sub_RLM)
hist ← [Metadata(state)]
while True:
    code ← LM(hist)
    (state, stdout) ← REPL(state, code)
    hist ← hist ∥ code ∥ Metadata(stdout)
    if state[Final] is set: return state[Final]
```

**Key Design Benefits:**
- Root LM context rarely clogs (grows slowly with metadata only)
- On-the-fly context subsetting without expensive indexing
- Modality-agnostic (any data loadable into memory)
- New axis for **test-time compute scaling** (trajectory is learnable/RL-ifiable)

### Key Results

#### OOLONG Benchmark (Context Rot)

**Setup:** Queries over 3k–6k rows of unlabeled data requiring semantic mapping & counting.

| Context Size | Method | Performance vs Baseline | Cost |
|--------------|--------|------------------------|------|
| ~132k tokens | RLM(GPT-5-mini) | **+34 pts (~114% ↑)** over GPT-5-mini | Cheaper (median) |
| ~132k tokens | RLM(GPT-5-mini) | Outperforms **GPT-5** by 34+ points | Cheaper (avg) |
| ~263k tokens | RLM(GPT-5-mini) | **+15 pts (~49% ↑)** over GPT-5-mini | — |
| **Ablation** | Remove recursion | **-10% drop** | Proves sub-calls are essential |

**Critical ablation:** Removing recursion drops performance by ~10%, proving that **semantic mapping requires recursive sub-calls** — the root LM alone cannot handle complex context decomposition.

#### BrowseComp-Plus (Extreme Scale)

**Setup:** Multi-hop QA over ~100K documents (~5k words avg). Tested on 10, 50, 100, and 1000 docs.

| Method | 1000 docs (~10M+ tokens) |
|--------|-------------------------|
| **RLM(GPT-5)** | **Only method with perfect performance** |
| ReAct + GPT-5 + BM25 | Fails |
| Full-context GPT-5 | Fails |
| Truncated GPT-5 | Fails |

**Cost analysis:** API cost scales reasonably with context length; **no external retriever indexing required**.

#### CodeQA & OOLONG-Pairs

| Benchmark | Task Type | RLM(GPT-5) | Baseline |
|-----------|-----------|------------|----------|
| **CodeQA** | Fixed files | 62.0% | 24.0% (base) |
| **OOLONG-Pairs** | O(N²) quadratic | 58.0% | 0.1% (base) |

#### RLM-Qwen3-8B (First Natively Recursive LM)

- **Data:** 1,000 filtered trajectories from Qwen3-Coder-480B-A35B acting as RLM on LongBenchPro
- **Filtering:** Removed 0-score/1-turn trajectories; fixed template mistakes (FINAL() vs FINAL_VAR())
- **Training:** 300 steps, batch size 64, ~48 H100 hours using `prime-rl`
- **Result:** **+28.3% average improvement** over base Qwen3-8B as RLM
- **Key insight:** Training only the *root* model to manage REPL and launch sub-calls is sufficient; leaf sub-calls behave like general-purpose reasoning

### RLM-Qwen3-8B: First Natively Recursive LM

Zhang's team post-trained the first natively recursive language model using a **simple distillation recipe**:
- **Data:** 1,000 filtered trajectories from Qwen3-Coder-480B-A35B acting as RLM on LongBenchPro
- **Filtering:** Removed 0-score/1-turn trajectories; fixed template mistakes (FINAL() vs FINAL_VAR())
- **Training:** 300 steps, batch size 64, ~48 H100 hours using `prime-rl`
- **Result:** +28.3% average improvement over base Qwen3-8B as RLM
- **Key Insight:** Training only the *root* model to manage REPL and launch sub-calls is sufficient; leaf sub-calls behave like general-purpose reasoning

### Emergent Strategies (Interpretability)

The REPL environment makes RLM decision trajectories **highly interpretable**:

| Strategy | Description | Example |
|----------|-------------|---------|
| **Peeking** | Inspects first N chars to infer structure | `context[:2000]` |
| **Greing** | Regex/keyword narrowing | `re.findall(r"User: \d+", context)` |
| **Partition + Map** | Chunks context, recursive LMs per chunk | Split 10k lines → label each → aggregate |
| **Summarization** | Compresses subsets for root LM | `summarize(chunk)` |
| **Long-Input/Long-Output** | Sequential programmatic transformations | `git log -p --cc --reverse --topo-order` |

> *"For histories longer than 75k tokens, GPT-5 can't even solve 10% of the histories! ... RLM(GPT-5) chooses to one-shot the task by programmatically processing the sequence of diffs!"*
> — Alex Zhang, RLM blogpost

### Critical Observations

1. **REPL is necessary for long inputs; sub-calling is critical for info-dense tasks.** Even without recursion, RLMs outperform baselines on long contexts. Sub-calling adds 10–59% gains on dense tasks like OOLONG-Pairs.
2. **Performance scales inversely with complexity.** Base models degrade sharply as tasks move from O(1) → O(N) → O(N²). RLMs degrade at a much slower rate.
3. **Model-agnostic but behavior varies.** GPT-5 is conservative with sub-calls; Qwen3-Coder is liberal (sometimes making thousands of calls per task). Prompt tuning is required per model family.
4. **Tradeoff at small contexts.** Base LLMs slightly outperform RLMs on short inputs due to RLM's overhead. RLMs shine when |P| ≫ K.

### RLM vs. Other Approaches

| Approach | How it handles long context | Limitation |
|----------|----------------------------|------------|
| **Context Window** | Stuff everything in | Context rot, O(n) memory/compute |
| **Context Compaction** | Summarize/compress | Lossy, information destroyed |
| **RAG Agents** | BM25/vector retrieval | Misses cross-chunk connections |
| **ReAct** | Tool use + fixed context | Bounded by window size |
| **RLM** | External environment + recursion | Exhaustive, programmable, composable |

### Philosophical Shift: Context-Centric vs Problem-Centric Decomposition

> *"RLMs are fundamentally different than modern agents... LMs should decide how to break down a problem to be digestible for an LM."*
> — Alex Zhang, RLM blogpost

This represents a fundamental philosophical shift in how we think about AI systems:

| Dimension | Modern Agents | RLMs |
|-----------|--------------|------|
| **Decomposition** | Human-designed workflows (problem-centric) | LM-autonomous context partitioning (context-centric) |
| **Context Management** | External retrieval + fixed windows | REPL environment with recursive access |
| **Control Flow** | Orchestrator decides steps | LM writes code to decide its own steps |
| **Scalability** | Limited by orchestrator design | Scales with base model improvements |

Zhang's insight: **The LM should control its own context access patterns**, not rely on hardcoded agent loops.

### RLMs ≠ Agents

> *"RLMs defer context management and decomposition decisions entirely to the language model, rather than hardcoding workflows like agents do."*

Key distinction: Agents rely on *human-designed* task decomposition. RLMs let the *LM decide* how to decompose context. This is a fundamental philosophical shift from workflow engineering to model autonomy.

### Limitations & Systems Challenges

- **Blocking execution:** Recursive calls are synchronous; no prefix caching or async parallelism
- **Variable runtime/cost:** Queries range from seconds to minutes depending on partition strategy
- **Inference engine gap:** *"Getting RLMs to work at scale requires re-thinking our design of inference engines."*
- **Recursion depth:** Currently capped at 1 (sub-calls are LMs, not RLMs). Deeper recursion (RLMs calling RLMs) unexplored but expected to yield stronger systems
- **Prompt brittleness:** FINAL()/FINAL_VAR() tag parsing fails occasionally; models sometimes output plans as answers
- **Coding dependency:** Models without strong coding ability struggle with REPL interaction

### The "Scaffolds" Thesis

Zhang's broader vision is that **LLMs will become scaffolds** — structural frameworks that organize computation, rather than end products that directly generate answers. RLM is a concrete instantiation of this: the LM scaffolds the reasoning process by managing an external environment, delegating sub-tasks, and composing results.

> *"If a model handles 10M tokens natively, an RLM could handle 100M+."*
> — Alex Zhang, on the scaling potential of RLMs

### Connection to Slate/Thread Weaving

RLM's philosophy directly influenced **Akira @realmcore_**'s **Slate** and its **Thread Weaving** architecture. Slate implements RLM principles for coding agents, with the key addition of **episodic memory** and **progressive disclosure** to manage knowledge overhang. Zhang and Khattab's work on RLM provided the theoretical foundation; Slate provided the practical implementation for agentic coding.

---

## KernelBench: LLM GPU Kernel Writing (2025)

**Paper:** *KernelBench: Can LLMs Write Efficient GPU Kernels?*
**Venue:** ICML 2025, DL4C & SSI-FM Workshop (🏆 **Best Paper**)
**Co-authors:** Anne Ouyang, Simon Guo, Simran Arora, Alex Zhang, William Hu, Christopher Re, Azalia Mirhoseini

KernelBench evaluates whether LLMs can write efficient GPU kernels (CUDA, Triton).

### Key Details
- **250 carefully selected PyTorch ML workloads** as test cases
- **New metric: `fast_p`** — percentage of generated kernels that are functionally correct AND offer speedup > threshold p over baseline
- **Frontier reasoning models perform best out of the box but still fall short overall**, matching PyTorch baseline in <20% of cases
- **Results improve with execution + profiling feedback** during iterative refinement
- **Benchmark difficulty increases** as speedup threshold p rises
- Connected to the broader **GPU MODE** community event

### Why It Matters
KernelBench established the first rigorous benchmark for LLM-assisted GPU kernel generation. The finding that even frontier models struggle (<20% match baseline) highlights a significant gap in LLM code generation for systems-level programming.

---

## GPU MODE

Zhang is part of the core team running the **GPU MODE leaderboard**, a community-driven platform for GPU kernel optimization competitions:

- **NVFP4 Blackwell competition** with NVIDIA
- **Three $100k–$1M competitions** with AMD
- **Model optimization competition** with Jane Street

GPU MODE reflects Zhang's belief in **community-driven benchmarking** — real problems, real hardware, real performance metrics. It complements his academic work by creating a practical testing ground for LLM-assisted systems programming.

---

## Other Projects & Publications

### Project Popcorn 🍿 (2025)
Details TBD — mentioned in research highlights as ML Systems work.

### Triton Kernels for OSS AlphaFold3 (2024)
Contributed Triton kernels for the open-source AlphaFold3 implementation. Gained 1k+ ⭐'s on GitHub.

### Neo-1 (2025)
Model development project — details TBD.

### KernelLLM-8B (2025)
Model combining kernel optimization with language modeling — details TBD.

### VideoGameBench (2025)
**Status:** Under review
Evaluates whether Vision-Language Models can complete popular video games. Extends LLM evaluation beyond text into interactive, multimodal domains.

### SWE-bench Multimodal (2025)
**Venue:** ICLR 2025
**Question:** Do AI Systems Generalize to Visual Software Domains?
Extended SWE-bench to multimodal software engineering tasks, testing whether AI systems can handle visual programming interfaces and GUI-based development.

### Language-guided World Models (2024)
**Venue:** SpLU-RoboNLP @ ACL 2024 (Oral)
Model-based approach to AI control using language guidance for world model learning in robotics.

### Scalable Video Understanding Benchmarks through Sports (2024)
**Venue:** DMLR Workshop @ ICLR 2024
Used sports as a domain for building scalable video understanding benchmarks — structured, rule-based environments with clear success criteria.

### Transaction Fee Mining and Mechanism Design (2023)
**Venue:** arXiv
Early work on blockchain/crypto — analyzing transaction fee mechanisms and their economic properties.

### Device-Independent Adaptive Tremor Suppression Orthoses (2019)
Early work in assistive technology — developing software for medical devices to suppress tremors.

---

## Research Trajectory

Zhang's work shows a clear evolution from **evaluation** to **systems** to **inference-time computation**:

### Phase 1: Evaluation & Benchmarking (2019–2024)
- Video understanding, sports analytics
- World models for AI control
- Transaction fee mechanisms
- *Theme:* How do we measure and evaluate AI systems?

### Phase 2: LLM Evaluation (2024–2025)
- SWE-bench Multimodal — do AI systems generalize to visual software?
- VideoGameBench — can VLMs complete games?
- KernelBench — can LLMs write GPU kernels?
- *Theme:* Rigorous, practical benchmarks for frontier capabilities

### Phase 3: Inference-Time Scaling (2025–)
- RLM — recursive language models for unbounded context
- KernelBot — competition platform for GPU code
- Project Popcorn — ML systems optimization
- *Theme:* How can LLMs programmatically manage their own computation?

### The Through-Line
Each phase addresses the same fundamental question: **How do we make AI systems more capable, more efficient, and more measurable?**

---

## Relationships & Collaborations

**Advisors:** Omar Khattab (MIT EECS, DSPy/ColBERT), Tim Kraska (MIT CSAIL, databases/ML systems)

**Key Collaborators:**
- **Omar Khattab** — RLM co-author, PhD advisor
- **Tim Kraska** — RLM co-author, PhD advisor
- **Anne Ouyang** — KernelBench co-author (Stanford)
- **Simon Guo** — KernelBench co-author
- **Simran Arora** — KernelBench co-author
- **William Hu** — KernelBench co-author
- **Christopher Re** — KernelBench co-author (Stanford)
- **Azalia Mirhoseini** — KernelBench co-author

**Mentors (Princeton):**
- Karthik Narasimhan — NLP, reinforcement learning
- Khanh Nguyen — NLP, machine learning
- Ofir Press — LLM efficiency, attention mechanisms
- Kai Li — Computer architecture, memory systems

**Community Connections:**
- **Akira @realmcore_** — Slate/Thread Weaving (RLM-influenced coding agent)
- **GPU MODE community** — GPU kernel optimization enthusiasts
- **Sakana AI** — Summer 2025 internship (evolutionary AI, open models)
- **VantAI** — Drug discovery research (2024)

---

## Impact Metrics

- **RLM GitHub:** 3,296⭐, 604 forks, 20 contributors
- **KernelBench:** ICML 2025 Best Paper
- **SWE-bench Multimodal:** ICLR 2025
- **GPU MODE:** Active community with NVIDIA, AMD, Jane Street competitions
- **RLM-Qwen3-8B:** First natively recursive LM; 28.3% improvement over base
- **AlphaFold3 Triton kernels:** 1k+ ⭐'s on GitHub

---

## Key Quotes

> *"Language models will be scaffolds."*
> — Alex Zhang, on the future of LLMs

> *"Getting RLMs to work at scale requires re-thinking our design of inference engines."*
> — Alex Zhang, RLM paper

> *"RLMs defer context management and decomposition decisions entirely to the language model, rather than hardcoding workflows like agents do."*
> — RLM blogpost

> *"If a model handles 10M tokens natively, an RLM could handle 100M+."*
> — Alex Zhang, on the scaling potential of RLMs

> *"For histories longer than 75k tokens, GPT-5 can't even solve 10% of the histories! ... RLM(GPT-5) chooses to one-shot the task by programmatically processing the sequence of diffs!"*
> — Alex Zhang, RLM blogpost

---

## See Also

- [[rlms]] — Recursive Language Models
- [[omar-khattab]] — PhD advisor, DSPy/ColBERT/GEPA creator
- [[tim-kraska]] — PhD advisor, MIT CSAIL databases/ML systems
- [[gepa]] — Genetic-Pareto prompt evolution (Khattab group)
- [[slate]] — Swarm-native coding agent (RLM-influenced)
- [[akira-realmcore]] — Slate creator, Thread Weaving architecture
- [[gpu-mode]] — GPU kernel optimization community
- [[kernelbench]] — LLM GPU kernel writing benchmark
- [[colbert]] — Late interaction retrieval paradigm (Khattab)
- [[dspy]] — Declarative LM programming framework (Khattab)
