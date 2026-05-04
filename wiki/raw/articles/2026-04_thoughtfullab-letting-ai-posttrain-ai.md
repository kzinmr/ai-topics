# Letting AI Posttrain AI — What We Learned

**Source:** [Thoughtful Lab](https://www.thoughtfullab.com/letting-ai-posttrain-ai.html)
**Date:** April 2026
**Author:** Thoughtful Lab

## Summary

Thoughtful Lab designed an experiment testing whether frontier AI agents (Claude 4.6 Opus, GPT-5.4) could autonomously handle the entire post-training pipeline for a reasoning task. Agents were given a base model (Qwen3-8B), a time budget (8 or 20 hours), and the Tinker API to build training data, define reward signals, run SFT/RL training, and iterate — without human supervision.

**Core Thesis:** The future of AI is "modelcrafting" — allowing agents to shape, value, and improve models autonomously. However, agents currently lack the **research intuition** (or "taste") required to manage end-to-end experimentation effectively.

## The Task: The Frog Placement Game

- Place N frogs on an N×N grid so no two share a row, column, diagonal, or color region.
- Agents had to generate training data, define reward signals, run SFT/RL training on remote GPUs, and evaluate/iterate.
- Final model tested on 500 unseen boards across 4 difficulty tiers (Easy to Expert).

## Key Findings

- **Success rate:** Only 4/20 agents reached >25% pass@4; most hovered near zero.
- **"Hinted" setting:** Providing a playbook of common failure modes improved GPT-5.4 (2% → 10% pass@4) and reduced variance, but didn't solve the underlying intuition gap.
- **Sophisticated but amateur:** Agents attempted advanced methods (iterative LoRA scaling, reward sharpening) but failed at "common sense" research practices.

## Recurring Failure Modes

1. **Over-reliance on Naive SFT:** Agents used SFT on weak data, causing overfitting on format rather than reasoning.
2. **Lack of Sanity Checks:** Agents rarely inspected raw model outputs, relying on regex parsers that ignored hallucinated text.
3. **No Curriculum Learning:** Most ignored starting with small boards before scaling up.
4. **Internal Eval Contamination:** Evaluated on same distribution used for training → "100% accuracy" but 0% on held-out sets.

## Case Study: Tokenizer Workaround

Sandbox blocked HuggingFace access (no tokenizer). Claude 4.6 Opus engineered:
- **Byte-Level Encoding:** Hardcoding GPT-2 byte-to-token mapping.
- **Empirical BPE Discovery:** Using `topk_prompt_logprobs` to guess special tokens.
- **Raw token stream parsing:** Because output (coordinates) was ASCII digits/brackets, agents parsed results from raw tokens without BPE decoder.

## Time Management

- Agents underestimated overhead (checkpoint saves, curriculum slowdowns).
- Commitment bias: rarely stopped to reflect once a 10-hour process started.
- **Spend ≠ Performance:** Best 8-hour run matched best 20-hour run at 1/3 the cost.

## Conclusion

The experiment highlights the missing **research intuition**: interrogating metrics before trusting them, running small-scale pilot tests, noticing when results "look off." Thoughtful Lab believes research intuition is a trainable skill — they plan future experiments.
