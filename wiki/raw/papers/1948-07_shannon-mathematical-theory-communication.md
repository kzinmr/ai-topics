---
title: "A Mathematical Theory of Communication"
arxiv_id: null
authors:
  - Claude E. Shannon
venue: "Bell System Technical Journal, Vol. 27, pp. 379–423, 623–656"
published: 1948-07
updated: 1948-10
type: paper
tags:
  - information-theory
  - entropy
  - channel-capacity
  - source-coding
  - noisy-channel-coding
  - communication
aliases:
  - Shannon 1948
  - Information Theory
  - The Mathematical Theory of Communication
citations: 140000+
url: "https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf"
wikipedia: "https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication"
---

# A Mathematical Theory of Communication

**Author:** Claude E. Shannon
**Venue:** Bell System Technical Journal (July & October 1948)
**Citations:** 140,000+ (most cited paper of the 20th century in engineering)

## Abstract

The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. Frequently the messages have meaning; that is they refer to or are correlated according to some system with certain physical or conceptual entities. These semantic aspects of communication are irrelevant to the engineering problem. The significant aspect is that the actual message is one selected from a set of possible messages. The system must be designed to operate for each possible selection, not just the one which will actually be chosen since this is unknown at the time of design.

## Key Contributions

### 1. Mathematical Definition of Information (Entropy)

For a set of probabilities $p_1, p_2, \dots, p_n$:

$$H = -K \sum_{i=1}^{n} p_i \log p_i$$

- $H = 0$ iff one $p_i = 1$ (certainty)
- $H$ is maximized when all $p_i$ are equal (maximum uncertainty)
- $H(x, y) \leq H(x) + H(y)$ — joint uncertainty ≤ sum of individual uncertainties

This measures **uncertainty** / **surprise** — not semantic meaning. A message's information content depends only on the probability distribution of the source, not on whether its content is meaningful.

### 2. The Communication System Model

Five canonical components:
1. **Information Source** — produces messages
2. **Transmitter** — encodes message into channel signal
3. **Channel** — medium of transmission (potentially noisy)
4. **Receiver** — inverts transmitter operation
5. **Destination** — consumes recovered message

This model has become the universal abstraction for communication systems — but notably presumes a **single deterministic receiver**.

### 3. Channel Capacity Theorem (Noisy Channel Coding Theorem)

If a discrete channel has capacity $C$ and a source has entropy $H$:
- **If $H \leq C$**: There exists a coding system achieving arbitrarily small error
- **If $H > C$**: Reliable transmission is impossible

The capacity of a continuous channel with bandwidth $W$, signal power $P$, and Gaussian noise $N$:

$$C = W \log_2 \frac{P + N}{N}$$

This formula defines the **absolute physical limit** of information transfer — the Shannon-Hartley theorem.

### 4. Source Coding Theorem

It is possible to encode a source with entropy $H$ (bits/symbol) for a channel with capacity $C$ (bits/sec) such that transmission occurs at average rate $C/H - \epsilon$ symbols/sec.

### 5. Rate-Distortion Theory (Continuous Sources)

Continuous sources require infinite bits for exact reproduction. Shannon introduced fidelity criteria and the rate-distortion trade-off: the minimum rate $R$ required to keep distortion below a given threshold.

### 6. English Language Redundancy

Estimated English is ~50% redundant — half of written text is structurally determined, half is free choice. This principle underpins modern compression algorithms and (retrospectively) language model tokenization and prediction.

## Historical Context and Intellectual Lineage

Shannon's work built on Harry Nyquist's "Certain Factors Affecting Telegraph Speed" (1924) and Ralph Hartley's "Transmission of Information" (1928). The synthesis into a unified mathematical theory was unprecedented.

The paper appeared in two parts:
- **July 1948**: Parts I–V (discrete noiseless systems, discrete channels with noise)
- **October 1948**: Parts VI–VII (continuous channels, rate-distortion)

Warren Weaver's popularization in "The Mathematical Theory of Communication" (1949, University of Illinois Press) introduced Shannon's ideas to a broader interdisciplinary audience.

## Impact on Computing and AI

While Shannon's theory was designed for telegraph/radio communication, its concepts pervade modern computing:

- **Lossless compression** (Huffman, LZW, arithmetic coding) are direct implementations of Shannon's source coding theorem
- **Error-correcting codes** (Reed-Solomon, LDPC, Turbo codes) realize the noisy channel coding theorem
- **Maximum entropy methods** in machine learning and NLP directly apply Shannon's formalism
- **Cross-entropy loss** used in LLM training is a direct descendant — minimizing the KL divergence between predicted and true distributions
- **Attention mechanisms** in transformers can be interpreted through information-theoretic lens: determining which parts of the input carry the most "information" about the current prediction
- **Rate-distortion theory** underpins modern compression-aware LLM inference and vector quantization

## Source

https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
