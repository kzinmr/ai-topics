# Machine Studying

> https://jacobxli.com/blog/2026/machine-studying/

**Authors:** Jacob Xiaochen Li (MIT CSAIL), Rick Battle (Broadcom), Omar Khattab (MIT CSAIL)
**Published:** June 17, 2026
**Type:** Blog post / Research overview

---

We increasingly need AI agents to work in domains they never saw during training, like using a new programming library or leveraging the emerging literature around a new disease. Such domains most naturally appear as a **corpus of documents**, like a textbook on a technical subject or the manual describing a new tool.

Faced with such a corpus, current agents overwhelmingly rely on inference compute and immediately reduce this problem either to "RAG" or to "long context", and then simply rely on in-context learning, on weight updates that approximate it, or on agentic search and recursion that scales it to longer contexts. If a domain is important enough, today's best practice is to hand-build an RL environment (or buy one!) so agents can practice some relevant skills via trial and error. Across all of these, we can't help but notice that our agents today engage with new domains in shallow, hand-engineered ways. **Humans can turn reading a textbook and actively thinking about the material into deep knowledge and even expertise. Why can't agents yet?**

We call this problem **Machine Studying**. Given nothing but a corpus D = (d₁, …, dₙ), can AI systems autonomously develop *expertise* in the underlying domain? A studying algorithm is **whatever the agent does *to itself* using D before anything is known about downstream evaluation**. Studying may update the agent's weights or anything in its harness. Importantly, machine studying is not definitionally about "internalizing a corpus into the weights": almost every agent *will still have complete access to the corpus* at test time! The question is how much expertise it can develop in that corpus.

## 1. Studying converts a corpus into expertise

We start by defining **expertise**. An expert in a domain D is **an agent that can *efficiently* turn inference compute into accurate work**. A sharp novice might eventually pass an open-book exam through sheer brute force, but only an expert can produce high-quality answers with ease and go above and beyond with more time. Concretely, we measure expertise as the *weighted area* under the agent's performance curve as inference compute grows. (This in turn gives us a notion of the **intelligence of an agent**: a smart agent can *quickly develop expertise* in a new subject. And by that token, it doesn't appear that current agents are very smart yet.)

## 2. Can't the agent just search the corpus?

Search/retrieval is not the same as expertise. An expert doesn't just find relevant passages — they know what to look for, when to stop, and how to connect disparate pieces of information.

## 3. Expertise is the efficiency of turning inference compute into accuracy

Formally measured as weighted area under the performance vs. inference compute curve.

## 4. StudyBench: can agents acquire expertise in novel domains?

We instantiate this in **StudyBench**, a benchmark to investigate the ability of agents to study. Two tasks:
- **Studying-DSPy**: agents must develop expertise in the DSPy library (a small library with a deliberately small API surface)
- **Studying-OpenClaw**: agents must develop expertise in the OpenClaw domain

## 5. Equally capable models can have very different levels of expertise

GPT-5.1 fails the deterministic API checks for using DSPy far more often than GPT-5.4-mini. GPT-5.1 was calling APIs that *did* exist in 2024 but were since deprecated — stale knowledge. When we read the failing trajectories more broadly, the agents usually land on a plausible solution early and then engineer around it, where a repository "expert" would have either known a better solution or had a better idea of when to keep searching.

For studying experiments, they use Qwen3.5-9B — small enough to train and probe many times, but a very *competent* model with no trouble writing good Python or PyTorch. Its bottlenecks are not around capability but around familiarity with the downstream domain.

## 6. Three broad paradigms for studying

### Self-supervised objectives
A natural first bet is that studying reduces to some **self-supervised ML objective**. Examples: next-token prediction over the corpus text, test-time training, compacting KV caches. They test **continual pre-training** (CPT) — training LoRA adapters for NTP over the raw corpus. CPT(code) over the DSPy codebase (459k tokens) and CPT(doc) over its documentation (160k tokens). Training on raw text can degrade post-trained abilities, so they mix in self-sampled coding traces as an anchor.

### Synthetic data and environments
A second bet is that studying needs models to **synthesize their own training data**. Models produce entity-rich retellings, synthetic Q&A, active reading strategies, or meta-learn self-edits. They test **synthetic fine-tuning** (SFT) — using DeepSeek-V4-Flash to read the codebase and write Q&A pairs, then training on those pairs with on-policy distillation recovery.

A natural extension: turn synthesized questions into material for on-policy RL with self-synthesized environments. **Pedagogical RL** is one natural choice, guiding *sampling* with privileged information.

### Amortized context management
Skip weight updates entirely and let **agents manage notes** in their prompt or environment. Examples: accumulating strategies across attempts, thinking offline, persistent peek into external context, compiling documents into **a wiki they maintain** (links to Karpathy's LLM Wiki pattern). They test **writing a cheatsheet** — agent explores the repository and writes itself a note prepended to every future question.

## 7. Memorization is no substitute for expertise

Results with Qwen3.5-9B:
- CPT(code) and CPT(doc) approaches: encode corpus into weights but show limited expertise gains
- SFT + OPSD: synthetic fine-tuning with on-policy self-distillation shows initial promise but struggles to scale
- Weight updates alone don't reliably produce expertise in agents

## 8. Retrieval is no substitute for expertise either

Simply having access to the corpus at test time doesn't guarantee expertise. The agent needs to know *what* to search for and *when* to stop.

## Epilogue

Weight updates are expected to become essential to deep studying. They are skeptical that approximating long-context attention is the right objective. **Pedagogical RL** and combining context management with weight updates are promising directions.

The key insight: machine studying is a central and unrecognized bottleneck for downstream AI success. "Continual learning" is widely discussed but mostly about improving on the job and across sessions, avoiding catastrophic forgetting — not about developing genuine expertise from a new corpus.

---

## References from the article

- [StudyBench dataset on HuggingFace](https://huggingface.co/datasets/jacobli/studybench)
- [Pedagogical RL by Noah Ziems](https://noahziems.com/pedagogical-rl)
- [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [On-policy distillation - Thinking Machines Lab](https://thinkingmachines.ai/blog/on-policy-distillation/)
- Arxiv refs: 2506.06266, 2512.23675, 2602.16284, 2512.24601, 2508.06813, 2004.10964, 2508.09494, 2506.10943, 2504.07952, 2504.13171, 2605.19932, 2605.12484, 2407.10930, 2409.07431, 2302.00487, 2606.05661
