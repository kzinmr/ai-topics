---
title: LLM Steering
created: 2026-05-17
updated: 2026-05-17
type: concept
tags: [concept, interpretability, inference, local-llm]
sources:
  - wiki/raw/articles/seangoedecke.com--steering-vectors--255e1422.md
---

# LLM Steering

## Overview

LLM steering is the technique of guiding a language model's behavior by directly manipulating its internal activations during inference, rather than relying solely on prompt engineering. It works by identifying a "steering vector" — a directional representation of a concept (e.g., "respond tersely") in the model's activation space — and adding or subtracting it from the model's activations at runtime.

## How Steering Works

### Naive Steering Vector Extraction

1. Feed the model a set of prompts twice — once normally, once with a behavioral modifier appended (e.g., "respond tersely")
2. Measure the difference in activations for each prompt pair
3. Subtract the normal activation matrix from the modified one to isolate the steering vector
4. Apply this vector to the same activation layer during any future inference to produce the same behavioral shift

### Sophisticated Approach (Sparse Autoencoders)

A more advanced method uses sparse autoencoders (SAEs) to extract features from model activations — patterns of behavior that co-occur across many inputs. These features can then be mapped to individual concepts and boosted selectively. This is the approach Anthropic is pursuing with their [sparse autoencoder research](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html), primarily for interpretability and safety.

## Why Steering Hasn't Been Widely Used

Steering occupies an awkward "middle class" position in AI research:

- **Beneath the big labs**: Organizations like Anthropic and OpenAI don't need steering — they can directly train models to behave as desired. When they want behavioral control, they modify training data, not activations.
- **Out of reach for API users**: Steering requires access to model weights and internal activations. Users of ChatGPT or Claude via API cannot steer — only the model providers can.
- **Outcompeted by prompting**: For many basic applications, careful prompt engineering achieves similar results without needing access to internals. Adding "you MUST" or other qualifiers to prompts can exercise fine-grained control over model behavior.

## Why Steering Is Interesting Again (May 2026)

The release of [[DeepSeek-V4-Flash]] has changed the landscape. DeepSeek-V4-Flash is strong enough to compete with the lower end of frontier model agentic coding, yet small enough to run locally. Since steering requires a local model, this makes it practical for individual engineers to experiment with steering for the first time.

Notably, [[entities/antirez-com]] has baked steering into his [[DwarfStar 4]] project — a stripped-down version of [[llama.cpp]] designed to run only DeepSeek-V4-Flash. The steering implementation is currently rudimentary (e.g., a toy "verbosity" control replicable via prompting), but the project was only released eight days ago as of May 2026, suggesting rapid development ahead.

## Potential Applications

1. **Behavioral control panels**: Instead of fiddling with prompts, users could adjust sliders for "succinctness/verbosity" or "conscientiousness/speed" that directly manipulate activations
2. **Safety interventions**: Steering could theoretically be used to suppress undesirable behaviors (e.g., refusal patterns, sycophancy) without retraining
3. **Model introspection**: The process of identifying steering vectors contributes to mechanistic interpretability — understanding what concepts exist where in a model's representation space

## Open Questions

- **Robustness**: Do steering vectors generalize across different prompt distributions, or do they break down on out-of-distribution inputs?
- **Composability**: Can multiple steering vectors be applied simultaneously without destructive interference?
- **Safety**: If steering can suppress refusal behaviors, does it also enable jailbreaking? What guardrails are needed?
- **Scalability**: Does steering work equally well for simple behavioral adjustments (verbosity) and complex cognitive shifts (reasoning depth, factuality)?

## Related Concepts

- [[Mechanistic Interpretability]] — the scientific study of what neural networks represent internally
- [[Sparse Autoencoders]] — Anthropic's approach to extracting interpretable features from model activations
- [[Prompt Engineering]] — the alternative approach to guiding model behavior via input text
- [[DwarfStar 4]] — local inference engine with built-in steering support
- [[DeepSeek-V4-Flash]] — the model making local steering practical
