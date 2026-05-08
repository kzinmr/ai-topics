---
title: "A simple introduction to DSPy"
author: Maxime Rivest
date: 2025-06-03
url: https://x.com/MaximeRivest/status/1929861781448536081
type: x_article
getxapi: true
tags:
  - dspy
  - tutorial
  - prompt-engineering
  - optimization
  - getting-started
summary: >
  Maxime Rivest's one-hour DSPy tutorial covering the full cycle: defining a Signature,
  fetching data from Wikipedia, creating a gold set with Claude Sonnet 4, and optimizing
  Gemini Flash-lite prompts via MIPROv2 to achieve a 20% precision improvement.
---

# A simple introduction to DSPy

**Author:** Maxime Rivest 🧙‍♂️🦙🐧 (@MaximeRivest)
**Date:** June 3, 2025
**Views:** 190K+ | **Likes:** 1.2K | **Replies:** 27

## Introduction

DSPy is simple and powerful. It is the best way to build LLM software right now. Despite that, lots of people keep putting off learning it. Maxime admits he did—for a whole year—thinking he would need a substantial time investment before he could "get it." That's not the case! It took him one hour.

This article covers the entire cycle: building a program, creating a gold set (synthetically, with AI—and yes, it's actually useful, not just contrived!), and evaluating the results.

**Task:** Build a program that counts mentions of "Artificial Intelligence," "AI," or any other ways of referring to AI.

## Overview

1. Define a DSPy signature for counting AI mentions
2. Fetch data from Wikipedia
3. Create a training dataset using a stronger model (Claude Sonnet 4)
4. Optimize a weaker model (Gemini Flash-lite 2.0) to match the stronger model's performance

## Step 1: Define the AI Task Signature

In DSPy, define the task using a **Signature class** instead of writing prompts manually. DSPy provides two syntax options:

### Shorthand syntax

```python
ai_counter = dspy.Predict("paragraph -> ai_occurrences_count: float")
```

This tells the LLM:
- **Input**: `paragraph` (str)
- **Output**: `ai_occurrences_count` (float)
- **Strategy**: `dspy.Predict` (vanilla, no special strategy)

### Full class-based syntax

```python
import dspy

# Setup the LLM
dspy.configure(lm=dspy.LM('gemini/gemini-2.0-flash-lite', temperature=1.0, max_tokens=6000))

# Define the signature
class count_ai_occurrences(dspy.Signature):
    """Count the number times the word 'Artificial Intelligence'
    or 'AI' or any other reference to AI or AI-related terms appears in the paragraph"""
    paragraph: str = dspy.InputField(desc="The paragraph to count the AI mentions in")
    ai_occurrences_count: int = dspy.OutputField(desc="The number of times the word 'Artificial Intelligence' or 'AI' appears in the paragraph")

dspy_module = dspy.Predict(count_ai_occurrences)
```

This gets turned into a prompt automatically by DSPy — no manual prompt writing.

### Optional: Wrapping as a regular function

Maxime wraps the DSPy module in a function for data analytics compatibility:

```python
# The DSPy module requires keyword args and returns output as an object
# Wrapping simplifies integration with data analytics tools
```

## Step 2: Fetch Data

Fetches content from the Wikipedia AI page using the Attachments library and stores it in a dataframe. Uses Datar (R's dplyr-inspired data manipulation for Python).

## Step 3: Applying the AI to paragraphs

Applies the function to every row in the dataframe — loops through each paragraph, sends it to Flash-lite, and stores the AI mention count in a `flash_response` column. This is the **baseline**.

## Creating the Gold Set

Uses **Claude Sonnet 4** (a SOTA model) to create reference answers on a sample of paragraphs. The goal: optimize Flash-lite's prompt to approximate Sonnet 4's responses. This is useful when you don't know the answer yourself but know that SOTA models get it "right enough."

```python
# Using dspy.context to switch the LLM for gold set creation
# Applies the program to each paragraph, saves results in resp_sonnet column
```

## Evaluation

Uses **exact match** as the metric. Adds an `exact_match` column (true/false) comparing Flash-lite and Sonnet responses.

**Baseline precision:** 65% with Flash-lite and the default prompt.

## Preparing for the Optimizer

Reshapes the dataframe into the format `dspy.MIPROv2` expects, and prepares the exact-match metric:

```python
# Metric must use .[output_name] to access x (gold set) and y (trained model output)
```

Sets a **teacher model** (Sonnet 4) for prompt composition via `teacher_settings`:

```python
# Optimizer = MIPROv2
# teacher_settings = {lm: dspy.LM('anthropic/claude-sonnet-4')}
```

## Automatic Prompt Optimization

Runs MIPROv2 to automatically optimize the prompt. The optimizer finds the best prompt structure to make Flash-lite's outputs match Sonnet 4's.

### Results

| Model | Precision |
|-------|-----------|
| Flash-lite (baseline) | 65% |
| Flash-lite (MIPROv2 optimized) | **85%** |

**Flash-lite improved by 20%** — no prompt spaghetti required.

The entire pipeline (fetch data → create gold set → tune → evaluate) fits in **~50 lines of code**.

## Key Takeaways

1. **DSPy's Signature system** replaces manual prompt writing with declarative I/O contracts
2. **Synthetic gold sets** with SOTA models are genuinely useful for optimization
3. **MIPROv2 optimizer** can automatically improve a weaker model's prompt to match a stronger model
4. **No prompt spaghetti** — DSPy handles the prompt structure automatically
5. **Learnable in ~1 hour** if you know Python
