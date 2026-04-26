---
title: DSPy
created: 2026-04-25
updated: 2026-04-25
type: entity
tags: [open-source, tool, framework]
sources: []
---

# DSPy

DSPy (Declare + Optimize) is an open-source framework developed by Stanford's NLP group for building systems that use large language models. Instead of writing hand-crafted prompts, developers declare what the LLM should do, and DSPy optimizes the prompt automatically.

## Key Facts

- **Created by:** Stanford NLP Lab (Armen Aghajanyan, Leo Gao, et al.)
- **Type:** Open-source Python framework
- **Core idea:** Replace prompt engineering with declarative program specification
- **Approach:** Uses bootstrap-and-finetune cycles to optimize prompt templates

## Core Components

- **Signatures:** Declarative interface definitions (input/output contracts)
- **Modules:** Composable building blocks (e.g., `dspy.Predict`, `dspy.ChainOfThought`)
- **Optimizers:** Automatically tune prompt templates (e.g., `BootstrapFewShot`, `MIPRO`)

## Relationship to Wiki Topics

- [[gepa]] — GEPA (ICLR 2026 Oral) builds on DSPy's optimization philosophy, using reflective prompt evolution to surpass even RL-based methods
- [[recursive-language-models]] — RLM approach can complement DSPy by handling unbounded context in DSPy programs
- [[memory-architecture]] — Memory layers are often needed within DSPy programs for stateful agent workflows

## External Resources

- GitHub: github.com/stanfordnlp/dspy
