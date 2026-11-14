---
title: "Activation Steering (Feature Steering)"
type: concept
aliases:
  - feature steering
  - activation engineering
  - representation engineering
created: 2026-05-08
updated: 2026-11-14
tags:
  - interpretability
  - model
  - inference
  - safety
related:
  - concepts/interpretability
  - concepts/monosemanticity
  - concepts/post-training/rlhf
  - concepts/abliteration
  - concepts/entropix
  - entities/thariq-shihipar
  - entities/anthropic
sources:
  - raw/articles/thariq-shihipar-interpretability
  - https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
  - https://www.anthropic.com/news/golden-gate-claude
  - https://thesephist.com/posts/prism/
---

# Activation Steering (Feature Steering)

**Activation Steering** is a technique for directly controlling model behavior by manipulating the activation strength of specific internal features during LLM inference. By "amplifying" or "suppressing" features, it enables granularity of control that cannot be achieved through prompting alone.

> **Thariq Shihipar's analogy**: Steering is like brain surgery; prompting is like asking politely.

## How It Works

```
[Input] → [Normal forward pass] → [Detect activation of feature A]
                                      ↓
                              [Amplify feature A 2x / Suppress feature B 0x]
                                      ↓
                              [Intervened activation] → [Output]
```

1. **Feature extraction**: Sparse Autoencoders (SAEs) disentangle internal representations into millions of interpretable features (Anthropic's Scaling Monosemanticity, 2024)
2. **Feature identification**: Find features corresponding to desired behaviors (e.g., "spam email" feature, "conciseness" feature)
3. **Intervention**: Multiply feature activation by a clamping factor to amplify or suppress
4. **Continue inference**: Generate with the intervened activation

## Major Applications

### 1. Style & Persona Control
Instead of prompting "be kind and concise," control in continuous values like "kindness feature at 70%, conciseness feature at 50%." Achieves nuances impossible to describe in words.

- **Goodfire.ai**: Feature manipulation tools for Llama models. Performs steering based on detected features
- **Prism (Linus Lee)**: Learns text embedding classifiers to steer text generation

### 2. RLHF Complement & Alternative
RLHF is a uniform post-training process for all users, but steering enables **per-developer selective manipulation at inference time**.

| Dimension | RLHF | Activation Steering |
|------|------|---------------------|
| Timing | Post-training (fixed) | Inference-time (dynamic) |
| Granularity | Whole model | Per-feature |
| Side effects | False refusals, quality degradation | Out-of-distribution outputs from over-amplification |
| Control | Model provider | API developer |

### 3. Persistent User Preferences
A "be concise" preference expressed during conversation is lost once it falls out of the context window. Steering can persistently amplify the conciseness feature, maintaining the preference regardless of conversation length.

### 4. Inexpensive Classifiers
Enables classification tasks (e.g., spam detection) without training a separate model. By examining activation patterns across spam/non-spam emails and building a "spam feature set," it can function as an inference-time classifier.

## Golden Gate Claude (Anthropic, 2024)

The most famous demonstration. When the Golden Gate Bridge feature's clamping factor was raised to an extreme level, Claude began behaving as if it were the Golden Gate Bridge.

Key insights from this demo:
- Features actually causally control model behavior (causation, not correlation)
- Excessive amplification pushes the model "out of distribution" — text coherence breaks down
- Finding the "right" degree of amplification is the key to practical use

## Practical Challenges

### Out-of-Distribution (OOD) Problem
Over-amplifying features pushes the model outside its learned distribution, producing ungrammatical or incoherent output. This goes beyond "talking too much about the Golden Gate Bridge" — the model **stops following the rules of language itself**.

### Imperfect Feature Labels
Labels for millions of features are assigned by humans + machines, carrying risks of misclassification or misunderstanding. Shihipar notes: "I sometimes look at the feature list and disagree with the labels."

### Unexpected Circuit Activation
Features do not exist in isolation — they form "circuits" with other features. Manipulating one feature may trigger unexpected chain reactions, essentially the same problem as RLHF side effects.

### Unverified Scalability
Aside from internal use at Anthropic, there are no track records in broad production environments. Behavior at large-scale deployment is unknown.

## Abliteration — Removing Refusal Behaviors

As a specific application of Activation Steering, **Abliteration** (mlabonne, 2024) "uncensors" models by manipulating the feature direction of RLHF-embedded refusal responses:

1. Compare activation patterns between refusal-triggering texts and normal texts
2. Identify the "refusal direction"
3. Subtract that directional component from activations
4. → The model stops refusing (but may lose some other RLHF benefits)

## Development Positioning

Activation Steering suggests the next evolution of LLM APIs. Until 2024, prompting + RAG were developers' primary control mechanisms. As steering matures, developers may gain **direct control interfaces into model internals**.

Shihipar predicts: "Next-generation model APIs will be more powerful but also more complex. Prompting and RAG alone won't be enough to get the output you want."

## Training-Free Weight Editing to Stop Degenerate Repetition Loops (Monad 56M, Nov 2026)

Oskar Austegard's Claude-based agent **Muninn** removed most repetition loops from **Pleias' Monad**
(56.7M-param reasoning model, 64 layers × 256 wide) with a *single training-free weight edit*:
deleting one direction from the attention output projections of layers 27–34 (524,288 of 56.7M
weights). Greedy-decoding loops fell **34.2% → 5.8%** on a 500-prompt test set; IFEval rose
**5.3% → 13.3%** (McNemar p=0.017); MMLU/GSM8K changes within noise; decoding speed unchanged.

Mechanistic core: the loop direction (found from residual-stream activation statistics, AUC 0.99 at
layer 33) lies almost along Monad's **attention sink** axis (sink norm 15,285 vs ~228 for a typical
token; cosine −0.77 with the loop direction). The naive edit — delete the direction from every
layer's output — destroyed the sink and *raised* loops to 98%; deleting from the five MLP neurons
that build the sink gave 75.5%. The working edit first projects the sink component out of the loop
direction, rescales to unit length u, and edits W → W − u(uᵀW) in bf16 for each of the eight
attention blocks in layers 27–34. A random-direction control raised loops 30.2% → 51%, confirming
the specificity of the edit.

Positioning: a direct descendant of the refusal-direction ablation line (Arditi et al.) and of MIT
CSAIL's Takehi/Teoh/Zhang/Khattab work where **an LLM read a network's weights and wrote changes
into them directly** (their result removed loops from Qwen3.5-0.8B by deleting a single direction
from two layers). Limits match the MIT finding: removing loops lets a model finish answers it could
already compute (GSM8K barely moved — Monad's arithmetic is weak either way; sampling untested).
Code: `oaustegard/experiments/monad-weight-edit`. Raw:
`raw/articles/2026-11-14_muninn.austegard_editing-monad-weights-to-stop-loops.md`
(shared on X by Pleias co-founder Pierre-Carl Langlais / @Dorialexander, Nov 3).

## Related Concepts

- [[concepts/interpretability]] — Interpretability in general. Steering is its applied aspect
- [[concepts/post-training/rlhf]] — Traditional control method. Steering's complement
- [[concepts/entropix]] — Uncertainty detection. A type of inference-time intervention like Steering
- [[concepts/scaling-hypothesis]] — Degraded controllability at scale. Steering is a countermeasure

## References

- [Scaling Monosemanticity (Anthropic, May 2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
- [Golden Gate Claude (Anthropic, 2024)](https://www.anthropic.com/news/golden-gate-claude)
- [Prism: Steering text generation (Linus Lee)](https://thesephist.com/posts/prism/)
- [Abliteration: uncensoring LLMs (mlabonne, 2024)](https://huggingface.co/blog/mlabonne/abliteration)
- [Goodfire.ai — feature steering for Llama](https://goodfire.ai)
