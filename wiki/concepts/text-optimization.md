---
title: "Text Optimization"
type: concept
created: 2026-06-09
updated: 2026-06-09
tags:
  - concept
  - harness-engineering
  - context-engineering
  - meta-harness
  - prompting
  - optimization
  - training
aliases:
  - "text-layer optimization"
  - "text-space learning"
  - "non-weight learning"
  - "external state updates"
  - "update-time compute"
sources:
  - raw/articles/2026-06-08_yoonho-lee_we-should-take-text-optimization-more-seriously.md
  - https://yoonholee.com/blog/2026/we-should-take-text-optimization-more-seriously/
  - https://arxiv.org/abs/2603.28052
related:
  - "[[concepts/meta-harness]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/context-engineering|Context Engineering]]"
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/rlm]]"
  - "[[entities/dspy]]"
  - "[[entities/yoonho-lee]]"
---

# Text Optimization

**Text optimization** is the practice of modifying the mutable text layer around an AI model — prompts, context, filesystem state, memory, retrieval databases, and harness code — to change future behavior. It is a legitimate learning mechanism that holds the same functional role as gradient-based weight optimization: changing behavior in response to new information, but operating in text space rather than weight space.

> Coined and popularized by [[entities/yoonho-lee|Yoonho Lee]] (Stanford) in his June 2026 essay "We Should Take Text Optimization More Seriously."

## Three Theses for Text Optimization

Lee argues for text optimization on three foundational claims:

| Thesis | Claim | Implication |
|--------|-------|-------------|
| **1. Legitimate Update Mechanism** | Text-layer changes produce the same functional effect as gradient updates — both condition future behavior on new information | Text optimization should be studied with the same rigor as weight optimization |
| **2. Sample Efficiency** | Text optimization is orders of magnitude more sample-efficient in low-data regimes | For many practical scenarios, text updates are the right choice over fine-tuning |
| **3. Update-Time Compute** | Reflective text optimization enables spending more compute learning from a single experience | A new scaling axis beyond pre-training and inference-time compute |

## Learning Outside the Weights

### The Premise

Deployed AI systems are no longer just parameter vectors queried in isolation. They are complex, stateful machines with many moving parts:

```
┌──────────────────────────────────────────────────────┐
│                  AI System State                       │
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Weights  │  │ Prompts  │  │ Memory   │            │
│  │ (gradient│  │ (text    │  │ (RAG,    │            │
│  │  updates)│  │  edits)  │  │  vector) │            │
│  └──────────┘  └──────────┘  └──────────┘            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Harness  │  │ Retrieval│  │ FS State │            │
│  │ Code     │  │ Indices  │  │ (files,  │            │
│  │ (DSPy,   │  │ (BM25,   │  │  context)│            │
│  │  skills) │  │  ColBERT)│  │          │            │
│  └──────────┘  └──────────┘  └──────────┘            │
└──────────────────────────────────────────────────────┘
```

**Learning = changing any behavior-conditioning state.** Weights are one state; text artifacts are others, with different costs, capacities, and failure modes.

### Inductive Bias of Text

Text artifacts have a favorable inductive bias grounded in Kolmogorov complexity: short specifications that explain many cases are more likely to capture real structure than long lists of exceptions. In this framing, good text updates are **compact patches to a pretrained world prior** — the LLM's learned distribution over text already encodes vast knowledge, and a well-crafted text update effectively "routes" that knowledge toward desired behavior.

### Staging Ground Pattern

A recurring pattern at scale: use the text layer to **elicit and compose** existing model capabilities, then **distill** into weights over time:

| Organization | Text-Layer Pattern | Distillation Target |
|-------------|-------------------|---------------------|
| Anthropic | System prompts + dynamic workflows | Constitutional training |
| OpenAI | Instruction hierarchy + deliberative alignment | RLHF post-training |
| Cursor | Context files + custom instructions | Model fine-tuning on traces |
| Letta | Context Constitution | Memory system training |
| Hippocratic AI | Polaris 3 prompt scaffolding | Domain-specific fine-tuning |
| Harvey | Sovereign Path continual learning | Legal domain adaptation |

## Update-Time Compute: The Third Scaling Axis

### The Analogy

```
Pre-training compute:    "How much compute to build the model?"
Inference-time compute:  "How much compute to solve this instance?"
Update-time compute:     "How much compute to learn from this experience?"
                                                         — Yoonho Lee (2026)
```

### Reflective Optimization Loop

Text-space learning enables **reflective optimization**: the system externalizes hypotheses about how it should change, tests them against evidence, and accepts or rejects revisions:

1. **Observe**: A failed trajectory or suboptimal outcome
2. **Diagnose**: Analyze traces to hypothesize root causes
3. **Abstract**: Propose candidate text-space fixes (prompt edits, retrieval changes, harness modifications)
4. **Test**: Evaluate candidates against held-out or historical data
5. **Commit**: Apply the best revision to the text layer

This mirrors scientific practice: proposing multiple theories, testing them against evidence, and crystallizing the best one. SGD cannot cheaply fork and compare — its single running parameter vector commits each update immediately.

Key implementations: [[concepts/meta-harness|Meta-Harness]] (filesystem-based reflective search), Reflexion (verbal self-reflection), Trace (execution-trace diagnosis), GEPA (Generalized Experience-Prompted Adaptation).

### When Text-Space Learning is Preferred

| Condition | Why Text-Space Wins |
|-----------|-------------------|
| Failures are expensive | Each weight update consumes many tokens; text-space amortizes diagnosis |
| Desired behavior is hard to specify | Text can be iteratively refined by domain experts ("verbal fine-tuning") |
| Abundant offline trace data | SFT and offline RL struggle with trajectory data; text-space reflection re-uses it effectively |
| Information is volatile or private | Weights amortize globally; text keeps information local, auditable, and revocable |

## The Strongest Case for Weights — And Why It's Not Enough

### Amortization

**Claim**: Weights amortize information — once trained, the behavior is "free" for every future query. Context is a finite resource.

**Counterpoint**: This is a routing problem, not a binary choice:
- **Weights** = stable, repeatedly useful, general information (arithmetic, grammar, world knowledge)
- **Text layer** = volatile, local, auditable, not-yet-trusted information (user preferences, current project state, experimental hypotheses)

Progressive disclosure systems (RAG, RLM, MemGPT, dynamic workflows) don't dump all text-layer information into every context window — they retrieve and condition on relevant information as needed. 1% of a 1M-token context is still 10K tokens — enough for substantial behavioral conditioning.

### Neural Circuit Creation

**Claim**: Only weight training creates new neural circuits. Text optimization can only elicit existing behaviors.

**Counterpoint**: The practical question isn't whether text optimization can create new latent capabilities, but **how much headroom remains** between what a model could in principle do and what it actually does in practice. The Mismanaged Geniuses Hypothesis suggests this headroom is substantial — deployed systems are bottlenecked by elicitation and composition, not by raw capability gaps.

Empirically: retrieval-augmented QA improves 20-40% with better context engineering on frozen models. Test-time scaling with the same model can improve performance 2-5×. Tool-use agents with better harnesses outperform agents with larger base models.

### The "Existence Argument"

**Claim**: Human brains learn by changing weights. It must be the right approach.

**Counterpoint**: Human cognition routinely depends on external artifacts — books, papers, code, tools, instruments. Edwin Hutchins' *Cognition in the Wild* shows ship navigation as a cognitive system of people, instruments, procedures, and external representations. Clark and Chalmers' *The Extended Mind* argues the cognitive boundary extends beyond individual brains. How much would human intellectual output suffer if we were suddenly cut off from all external text?

## Positioning in the Agent Stack

Text optimization is a cross-cutting layer that touches multiple levels of [[concepts/harness-engineering|Harness Engineering]]:

```
Harness Engineering
├── Agentic Engineering (usage patterns)
│   └── Text optimization: prompt crafting, skill definition, context curation
├── AI Agent Engineering (system patterns)
│   └── Text optimization: harness design search, DSPy program optimization
└── Context Engineering (information management)
    └── Text optimization: retrieval strategy, memory format, progressive disclosure
```

[[concepts/meta-harness|Meta-Harness]] is the most mature implementation of automated text optimization — a system that searches over harness code to maximize performance on held-out tasks.

## Research Directions

Lee identifies five directions for rigorous text optimization research:

| Direction | Status | Key Question |
|-----------|--------|-------------|
| **Theoretical analysis** | Early (PAC-Bayes, 2023-level models) | Can we formalize why text space has better inductive bias? |
| **Better evals** | CL-bench exists; TerminalBench-2 emerging | How to isolate text-layer capability from weight capability? |
| **Architecture research** | Fragmented (DSPy, OpenClaw, instruction hierarchy, skills) | What is the unified design space for text-layer systems? |
| **HCI research** | Nascent | How to let domain experts do "verbal fine-tuning"? |
| **Scaling laws** | No systematic study | What happens when text optimization gets weight-scale compute? |

## Related Concepts

- [[concepts/meta-harness]] — Automated search over harness code (Lee et al., 2026)
- [[concepts/harness-engineering]] — The discipline of building agent infrastructure
- [[concepts/context-engineering|Context Engineering]] — Curating optimal context window content
- [[concepts/test-time-scaling]] — The inference-time axis text optimization mirrors at update time
- [[concepts/rlm]] — Recursive language models as text-space context management
- [[entities/dspy]] — Declarative text-layer programming and optimization
- [[concepts/gepa]] — Generalized Experience-Prompted Adaptation
- [[entities/yoonho-lee]] — Primary advocate and Meta-Harness first author
