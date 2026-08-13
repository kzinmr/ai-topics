---
title: "J-Lens (Jacobian Lens)"
created: 2026-08-13
updated: 2026-08-13
type: concept
tags: [interpretability, mechanistic-interpretability, activation-steering, reasoning, chain-of-thought, open-weight, llm]
sources:
  - raw/articles/2026-08-13_fireworks-ai_J-Lens-Kimi-K3-Qwen.md
---

# J-Lens (Jacobian Lens)

J-Lens (short for **Jacobian Lens**) is an [[concepts/interpretability]] technique introduced by [[entities/anthropic]] researchers. It is a trained probe that reads a model's hidden state at a given layer and reports which words or concepts the model is "already leaning toward" *before* it writes the next token. In effect, it lets researchers peer inside a model mid-thought and observe a concept forming before it appears in visible output.

The term draws on the same family of ideas as [[concepts/mechanistic-interpretability]] and [[concepts/activation-steering]]: instead of treating a model as a black box that maps input to output, J-Lens treats the model's internal activations as something that can be inspected, fitted to, and read back as vocabulary.

## What it does

J-Lens works as a **classifier on top of a model's internal state** at specific token positions and layers. For a given position-layer pair (a "cell"), the fitted probe produces a ranked list of tokens that the probe associates most strongly with that internal state. That ranked list is the "readout" — the vocabulary the model is carrying internally at that moment, independent of what it has actually written.

Fireworks AI (see [[entities/fireworks-ai]]) reproduced the technique on two open-weight models — [[concepts/kimi-k3]] and Qwen3.5-9B (see [[concepts/qwen-3-8]]) — and dubbed the recovered mid-draft vocabulary **silent signals**: vocabulary associated with the final output that is recovered by a fitted lens before the output exists.

## Calibration

The lens is fitted separately from the examples it is later tested on. For the Kimi K3 runs, Fireworks fitted the lens on 14 task-independent calibration passages covering diverse topics (metal heat treatment, linguistic borrowing, crop rotation, traditional navigation), kept separate from 10 hold-out user prompts. Each passage produced one estimate per sampled layer, and the 14 estimates were averaged into the fitted lens. A predeclared starting window and the final position (which has no following token) were excluded from fitting.

## Paired Copy Experiment

The cleanest demonstration is the **Paired Copy Experiment**: the model is asked to echo the same sentence twice under two different focus instructions. For example, Kimi is asked to write back "The old painting hung crookedly on the wall." while (a) focusing on evaluating `3^2 - 2`, or (b) concentrating on citrus fruits.

Both times the model produces the *identical* visible output. The lens readout, however, differs: arithmetic vocabulary (e.g. 7, 9, 3, "answer", "seven") appears in the top-10 under the arithmetic focus, and citrus vocabulary (orange, lemon, lime, "citrus") appears under the citrus focus — and the two never leak into each other. Because the visible tokens are identical, the readout contrast cannot be explained by the displayed text; the hidden state tracks task focus independent of what is written.

## Results

Across the ten Kimi examples, each of the 20 reviewed word lists (two per example) had at least one listed word among the readout's top-10 results. Notable cases:

- **Order-of-operations math**: intermediate values 21 and 42 appear in the readout before either number is written.
- **Factual riddle**: the word "spider" reads out before the entity is named in text.
- **Rhyming couplet**: several rhyme candidates read out before their first exact appearance.
- **Single-word answers**: both the eventual answer and unchosen alternatives (e.g. "soccer" alongside "football", "basketball") appear together.

## Cross-model transfer

To test generality, the 20 word lists selected using Kimi's readouts were applied *unchanged* to a separately fitted Qwen3.5-9B lens (own tokenizer, own lens, deterministic completions with thinking disabled). **19 of 20 word lists** met the "found" criterion (a listed word in the top-10 at a sampled position and depth), confirming the phenomenon generalizes across different model architectures and labs.

## Where the signals live

A task-transcript region test split each transcript into three phases — user message prefill, chat-template prefill, and eligible response prefix — to separate prompt interpretation from active generation. On Kimi, silent signals appeared in 40/40 user-message regions, 40/40 chat-template regions, and 24/24 eligible response-prefix regions (16/40 cases had no verbose prefix, so only 24 remained). Qwen was nearly identical (39/40, 39/40, 23/24), showing the "readable before it's said" pattern holds both while digesting the prompt and while mid-generation.

## Limitations

The method checks for **individual tokens**, which breaks on tokenizer differences. Qwen splits "21" and "42" into two tokens each, so a single-token lens cannot recover them as unified matches — Qwen scored 0/3 on the "intermediate results" probe family for that episode despite scoring normally elsewhere. A multi-token lens is a natural future extension.

## Significance

The results show internal states carry task-relevant concepts long before they are written to the context window. This is a concrete step toward opening the black box of AI: models carry more insight than just their output, and open-weight models allow independent researchers to fit probes, reproduce measurements, and test what the signals do. Because the same effect shows up in two openly available models from different labs, it is reproducible in a way that closed models do not permit. The run itself is not cheap — roughly 7,168 backward evaluations per passage and about 74 node-hours (592 GPU-hours) across 14 passages — but it is feasible with open weights.

## See also

- [[concepts/interpretability]]
- [[concepts/mechanistic-interpretability]]
- [[concepts/activation-steering]]
- [[concepts/chain-of-thought]]
- [[entities/anthropic]]
- [[entities/fireworks-ai]]
