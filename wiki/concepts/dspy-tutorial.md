---
title: DSPy Tutorial (Getting Started)
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - dspy
  - optimization
  - prompting
  - education
sources:
  - raw/articles/2025-06-03_maxime-rivest-dspy-introduction.md
---

# DSPy Tutorial — Getting Started in ~1 Hour

A hands-on, practical introduction to DSPy by Maxime Rivest that covers the complete cycle: building a program, creating a synthetic gold set with a SOTA model, evaluating, and optimizing.

> *"If you know Python, in an hour you'll either have built several LLM programs, or you'll have built one, benchmarked it, and optimized it!"* — Maxime Rivest

**Original article:** [A simple introduction to DSPy](https://x.com/MaximeRivest/status/1929861781448536081) (190K views, 1.2K likes)

## The Task

Build a program that counts mentions of "Artificial Intelligence," "AI," or any other reference to AI in a given paragraph.

## Workflow Overview

```
Define Signature → Fetch Data → Apply Baseline → Create Gold Set → Evaluate → Optimize
```

## Step 1: Define the Signature

DSPy replaces manual prompt writing with **declarative Signatures**. Two syntax options:

### Shorthand (minimal)

```python
ai_counter = dspy.Predict("paragraph -> ai_occurrences_count: float")
```

Four parts:
1. `dspy.Predict` — strategy (vanilla; could be `dspy.ChainOfThought`)
2. `paragraph` — input field (str)
3. `ai_occurrences_count` — output field
4. `float` — output type constraint

### Class-based (full control)

```python
import dspy

dspy.configure(lm=dspy.LM('gemini/gemini-2.0-flash-lite', temperature=1.0, max_tokens=6000))

class count_ai_occurrences(dspy.Signature):
    """Count the number of times AI-related terms appear in the paragraph"""
    paragraph: str = dspy.InputField(desc="The paragraph to count AI mentions in")
    ai_occurrences_count: int = dspy.OutputField(desc="Number of AI mentions")

dspy_module = dspy.Predict(count_ai_occurrences)
```

**Key insight:** DSPy auto-generates the prompt from the Signature. The docstring becomes the objective, and field descriptions become instructions. No prompt spaghetti.

### Tip: Wrap as a regular function

```python
def count_ai(paragraph_text):
    return float(dspy_module(paragraph=paragraph_text).ai_occurrences_count)
```

This makes the DSPy module compose well with data analytics tools.

## Step 2: Fetch Data

Use Wikipedia API + dataframe (e.g., Datar for dplyr-style manipulation):

```python
# Fetch Wikipedia AI page, split into paragraphs
# Store in dataframe with columns: paragraph
```

## Step 3: Baseline with a Weaker Model

Apply Flash-lite to every paragraph:

```python
df['flash_response'] = df['paragraph'].apply(count_ai)
```

This gives the **baseline** — Flash-lite's performance with the default DSPy-generated prompt.

## Step 4: Create a Synthetic Gold Set

Use a **SOTA model** (Claude Sonnet 4) to generate reference answers:

```python
with dspy.context(lm=dspy.LM('anthropic/claude-sonnet-4')):
    df['resp_sonnet'] = df['paragraph'].apply(count_ai)
```

**Philosophy:** When you don't know the ground truth but know that SOTA models get it "right enough," use them to create the gold standard. Then optimize a cheaper model to approximate it.

## Step 5: Evaluate (Exact Match)

```python
df['exact_match'] = df['flash_response'] == df['resp_sonnet']
precision = df['exact_match'].mean()  # 65%
```

**Baseline precision: 65%** — Flash-lite matches Sonnet 4's answers 65% of the time.

## Step 6: Optimize with MIPROv2

### Prepare data for the optimizer

DSPy's `MIPROv2` expects data in a specific format:

```python
# Reshape dataframe into list of dspy.Example objects
# Each example has: paragraph (input) and ai_occurrences_count (gold output)
```

### Prepare the metric

```python
def exact_match_metric(gold, pred, trace=None):
    return gold.ai_occurrences_count == pred.ai_occurrences_count
```

### Set a teacher model

```python
optimizer = dspy.MIPROv2(
    metric=exact_match_metric,
    teacher_settings={'lm': dspy.LM('anthropic/claude-sonnet-4')}
)
```

The **teacher model** (Sonnet 4) composes the optimized prompts. The **student** (Flash-lite) is the one being optimized.

### Run optimization

```python
optimized_program = optimizer.compile(dspy_module, trainset=trainset)
```

## Results

| Stage | Model | Precision |
|-------|-------|-----------|
| Baseline | Flash-lite + default prompt | 65% |
| Optimized | Flash-lite + MIPROv2 prompt | **85%** |

**20% improvement** — no manual prompt tweaking needed.

## The Optimized Prompt

DSPy automatically generates something like:

```
Given the paragraph, carefully read it and count every mention of
"Artificial Intelligence", "AI", or AI-related terms (e.g., machine
learning, neural networks, deep learning, natural language processing).
Return the count as an integer.
```

## Key Takeaways for Practitioners

1. **Signatures replace prompts** — Declare I/O types and descriptions; DSPy handles the prompt structure
2. **Synthetic gold sets work** — SOTA models can generate useful training data when ground truth is unavailable
3. **Teacher-student optimization** — Strong model teaches weak model via optimized prompts (no fine-tuning needed)
4. **~50 lines of code** for the full pipeline — no prompt spaghetti
5. **Learnable in ~1 hour** if you know Python — the barrier is psychological, not technical

## See Also

- [[entities/dspy]] — DSPy framework overview, architecture, and adoption
- [[concepts/dspy-optimization]] — Deep dive into teleprompters, assertions, and fine-tuning synergy
- [[concepts/dspy-architecture]] — Signatures, Modules, Teleprompters in depth
- [[entities/omar-khattab]] — Creator of DSPy
