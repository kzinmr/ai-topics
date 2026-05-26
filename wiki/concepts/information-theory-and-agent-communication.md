---
title: "Information Theory and AI Agent Communication"
tags:
  - methodology
  - agent-communication
created: 2026-05-07
updated: 2026-05-07
type: concept
aliases:
  - Information Theory and AI Agents
  - Shannon's Communication Model for Agent Systems
sources:
  - "[[raw/papers/1948-07_shannon-mathematical-theory-communication.md]]"
  - "[[raw/papers/2020-02-25_2002.10689_predictive-v-information.md]]"
related:
  - concepts/agent-protocols
  - concepts/agent-serverless
  - concepts/mcp
  - concepts/functional-core-imperative-shell
---

# Information Theory and AI Agent Communication

## Overview

Shannon (1948)'s "A Mathematical Theory of Communication" defined information as probabilistic uncertainty and proposed a five-element model: information source, transmitter, channel, receiver, and destination. This framework was originally designed for communication engineering (telegraphy, radio), and its core premise — a **single deterministic receiver** — is fundamentally being reconsidered for today's AI agent systems.

Predictive $\mathcal{V}$-Information (Xu et al., ICLR 2020) introduced the realistic constraint of "observer computational capability" to Shannon theory, showing that information **has different value depending on the receiver's model class.** This has direct implications for inter-agent communication.

---

## 1. Implicit Assumptions and Limits of Shannon's Model

### Shannon's Communication System
```
Information Source → Transmitter (Encoder) → [Channel (Noise)] → Receiver (Decoder) → Destination
```

This model rests on the following assumptions:
1. **Source and destination are symmetric** — encoding and decoding are reversible operations
2. **The receiver has ideal decoding capability** — there exists coding that achieves channel capacity
3. **"Meaning" is out of scope** — communication is limited to an engineering problem
4. **Single sender, single receiver** — multi-party communication beyond broadcasting is out of scope

### Divergence from Modern AI Agent Environments

| Shannon's Assumption | AI Agent Reality |
|---|---|
| Single destination | Bidirectional, multi-directional communication between multiple agents |
| Source doesn't consider receiver capability | Agents adjust messages to match the counterparty's "model class" |
| Noise is a physical property of the channel | Noise = agent interpretation error, context loss, hallucination |
| Meaning is irrelevant | **Semantic alignment** is essential in agent communication |
| Encode/decode are known functions | Encode/decode themselves are learnable (LLM natural language protocols) |

---

## 2. Predictive V-Information: Extending Shannon with "Computational Reality"

Xu et al. (2020) extended Shannon's mutual information $I(X;Y)$ and proposed **predictive $\mathcal{V}$-information**.

### Definition
Predictive $\mathcal{V}$-entropy:
$$H_{\mathcal{V}}(Y) = \inf_{f \in \mathcal{V}} \mathbb{E}[-\log f(Y)]$$

Predictive $\mathcal{V}$-information:
$$I_{\mathcal{V}}(X \to Y) = H_{\mathcal{V}}(Y) - H_{\mathcal{V}}(Y|X)$$

Here $\mathcal{V}$ is a specific model class (linear models, neural networks of a specific depth, etc.).

### Differences from Shannon

| Property | Shannon Information | $\mathcal{V}$-Information |
|---|---|---|
| Data Processing Inequality | $I(X;Y) \geq I(f(X);Y)$ (processing only reduces information) | $I_{\mathcal{V}}(X;Y) \leq I_{\mathcal{V}}(f(X);Y)$ (computation **increases information**) |
| Observer Dependency | None (universal) | Present (depends on model class $\mathcal{V}$) |
| High-Dimensional Estimation | Difficult (kernel density estimation, etc.) | Estimable with PAC guarantees |
| DPI | Always holds | Broken by computation |

### Key Insight: Computation "Creates" Information

In Shannon theory, data processing (e.g., $X \to f(X)$) can never increase information. However, in deep learning, raw data contains information "invisible" to simple models, and computation (multi-layer transformations) makes that information **usable**.

This is precisely the information-theoretic explanation of what the Transformer's attention mechanism does:
- Raw token sequences have low mutual information
- The self-attention mechanism "creates through computation" relationships between tokens
- With each deeper layer, $\mathcal{V}$-information increases (Shannon information is unchanged or decreases)

---

## 3. Implications for AI Agent-to-Agent Communication

### 3.1 Inter-Agent Protocols Presuppose a "Common Model Class"

In Shannon's model, communication works if sender and receiver share the same codebook. But in agent systems:

```
Agent A (Llama 3-70B)
    ↓ natural language message
Agent B (GPT-4o)
```

A and B have **different model classes $\mathcal{V}_A$ and $\mathcal{V}_B$**. A message that has "high information content" for $\mathcal{V}_A$ may be noise for $\mathcal{V}_B$.

**Practical implications**:
- Structured protocols like MCP and Function Calling serve to align $\mathcal{V}$ between agents
- When using natural language as a protocol, it must be transformed into "representations the agent can understand"
- Between agents with different base models, **protocol learning** to establish a common $\mathcal{V}$ is necessary

### 3.2 Information-Theoretic Interpretation of the Agent Harness Effect

The Harness Effect (5-40pp performance difference for the same model depending on harness) can be explained within the $\mathcal{V}$-information framework:

```
Model (base LLM) → Harness (Encoder) → Channel (API/CLI) → Decoder (Model)
```

The harness reconstructs inputs so that information becomes **usable** for the model's $\mathcal{V}$. Claude Code's system prompt design, OpenCode's function call wrappers, and Cursor's context management can all be interpreted as attempts to maximize $\mathcal{V}$-information for the same base model.

### 3.3 Multi-Agent Collaboration: Computation as Information Creation

The core insight of V-Information — **computation creates information** — applies directly to multi-agent systems:

1. **Information transfer from Agent A→Agent B**: A's output becomes the prerequisite for B's "information creation through computation"
2. **Chain of Thought (CoT)**: Intermediate reasoning steps have zero information in the Shannon sense, but are essential for subsequent layers from a $\mathcal{V}$-information perspective
3. **Multi-agent debugging**: Different agents extract different $\mathcal{V}$-information from the same observation

### 3.4 Shannon Capacity and New Constraints on Inter-Agent Communication

Shannon's channel capacity formula:
$$C = W \log_2 \frac{P + N}{N}$$

Analogous concepts in agent systems:
- **$W$ (bandwidth)** = Context window size (token count)
- **$P$ (signal power)** = Relevant information density (useful information per token)
- **$N$ (noise power)** = Hallucination, irrelevant context, prompt injection
- **$C$ (capacity)** = Effective information an agent can process in a single exchange

```python
# Effective capacity of agent communication
C_effective = context_window * log2(
    (relevant_signal + hallucination_noise) / hallucination_noise
)
```

**Observation**: As LLM context windows expand (128K→1M→10M tokens), **signal-to-noise ratio (SNR)** degradation is becoming the new bottleneck. This is a "reinvention of the Shannon capacity problem."

### 3.5 Rate-Distortion Theory and Inter-Agent Information Compression

Shannon's rate-distortion theory defines the minimum transmission rate $R(D)$ given an acceptable error $D$. In agent context:

- **Rate $R$** = Number of tokens exchanged between agents
- **Distortion $D$** = Degradation in task completion quality

Inter-agent protocols (MCP, Function Calling, JSON mode) achieve **lower rate for the same distortion** or **lower distortion for the same rate** compared to natural language communication. This is because structured protocols align $\mathcal{V}$.

---

## 4. Unified Framework: A 3-Layer Model of Agent Communication

Integrating Shannon (1948) and $\mathcal{V}$-Information (2020) yields a hierarchical model of agent communication:

| Layer | Shannon Equivalent | Agent Instantiation | Constraints |
|---|---|---|---|
| **Physical Layer** | Channel capacity $C$ | Context window, API rate limits, latency | $W$ (bandwidth), $N$ (noise) |
| **Code Layer** | Source/channel coding | System prompt, function definitions, MCP tool schema | Common $\mathcal{V}$ alignment |
| **Semantic Layer** | Domain Shannon considered "out of scope" | Goal alignment, task decomposition, inter-agent coordination protocols | Information loss due to $\mathcal{V}_A \neq \mathcal{V}_B$ |

**Modern agent communication problems center on Layer 3 (Semantic Layer), which Shannon considered out of scope.** $\mathcal{V}$-Information bridges Layer 2 and Layer 3 — because it formalizes how "what counts as information" changes based on the receiver's model class.

---

## 5. Conclusions and Future Research Directions

1. **Shannon's framework is necessary but insufficient** — essential for understanding physical transmission limits, but cannot handle semantic alignment between agents
2. **V-Information is a practical extension** — by introducing observer dependence, it can formalize communication between agents with different model capabilities
3. **Protocol design guideline**: Inter-agent protocols should maximize $\mathcal{V}$-information by aligning participants' $\mathcal{V}$ and providing a common encoding space
4. **Theoretical foundation for Harness Engineering**: The Harness Effect can be understood in the $\mathcal{V}$-information framework as "encoder design that maximizes a model's usable information"

See also: [[raw/papers/1948-07_shannon-mathematical-theory-communication.md]], [[raw/papers/2020-02-25_2002.10689_predictive-v-information.md]]

## See Also

- [[concepts/predictive-v-information]]
