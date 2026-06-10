---
title: "Training Agents with Reinforcement Learning — Lightning Lesson (Notebook Walkthrough)"
author: Will Brown
date: 2025-06-10
date_ingested: 2026-06-10
source: https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/search.ipynb
type: transcript
tags:
  - ai-agents
  - reinforcement-learning
  - grpo
  - tool-calling
  - agent-evaluation
  - reinforcement-learning
  - education
  - transcript
related_article: articles/2025-06-10_willbrown_training-agents-with-rl-lightning.md
participants:
  - Will Brown (instructor)
---

# Training Agents with Reinforcement Learning — Lightning Lesson (Notebook Walkthrough)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 10, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**GitHub:** [agent-engineering/lightning-lessons/search.ipynb](https://github.com/willccbb/agent-engineering/blob/main/lightning-lessons/search.ipynb)
**Related summary:** [[raw/articles/2025-06-10_willbrown_training-agents-with-rl-lightning|Lightning Lesson Summary]]

---

## Overview

This notebook walkthrough accompanies the "Training Agents with Reinforcement Learning" lightning lesson — the second pre-course session for [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering]]. It demonstrates a complete end-to-end pipeline for training a tool-using agent with RL: from building local search tools over a Wikipedia corpus, through synthetic QA data generation, baseline evaluation with LLM judges, and into live [[concepts/grpo-rl-training|GRPO]] training using the [verifiers](https://github.com/PrimeIntellect-ai/verifiers) library.

The key idea: **you can take a working agent, define what "good" looks like, and use RL to make it better** — no supervised fine-tuning data required, just reward signals.

---

## Section 1: Setup & Imports

The notebook begins with environment setup and core imports for the OpenAI client and async utilities.

```python
import os
import json
import asyncio
from openai import AsyncOpenAI

# Initialize async client for concurrent API calls
client = AsyncOpenAI()  # Uses OPENAI_API_KEY from environment
```

**Key point:** The notebook uses `AsyncOpenAI` rather than the synchronous client. Async is essential here because the pipeline needs to make many concurrent API calls — for synthetic data generation (hundreds of QA pairs) and for running multiple agent rollouts during evaluation. Python's `asyncio` with a semaphore pattern keeps concurrency bounded.

---

## Section 2: ChromaDB Setup — Local Vector Database

The agent's knowledge base is a persistent ChromaDB collection indexing Wikipedia page titles with OpenAI embeddings.

```python
import chromadb

# Create persistent ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create/get collection for Wikipedia pages
collection = chroma_client.get_or_create_collection(
    name="wikipedia",
    metadata={"hnsw:space": "cosine"}  # cosine similarity for embedding search
)

# Index Wikipedia page titles as documents
# Each page title is embedded using text-embedding-3-small
# The embedding function is configured at the collection level
```

**Key insight:** ChromaDB with `text-embedding-3-small` provides a fully **local, deterministic** search infrastructure. There are no API rate limits, no external dependencies during evaluation or training rollouts. This is critical for [[concepts/agentic-rl|RL training]] where you may need to run thousands of rollouts — you can't afford to hit rate limits or have network failures corrupt a training run. The cosine similarity space ensures that semantically related queries retrieve the right Wikipedia pages.

---

## Section 3: Search Tools — The Agent's Toolkit

Three tools give the agent progressive disclosure over the Wikipedia corpus, mirroring real research agent patterns: **search → navigate → read**.

```python
def search_pages(query: str) -> list[dict]:
    """Search Wikipedia pages by title similarity.
    Returns top 10 matching pages with their IDs and titles.
    """
    results = collection.query(
        query_texts=[query],
        n_results=10
    )
    return [
        {"page_id": id, "title": title}
        for id, title in zip(results["ids"][0], results["metadatas"][0])
    ]

def view_sections(page_id: str) -> list[dict]:
    """View the section headings of a Wikipedia page.
    Returns a table of contents — the agent uses this to decide
    which section to read in detail.
    """
    # Retrieves section headings for navigation
    ...

def read_section(section_id: str) -> str:
    """Read the content of a specific section.
    Returns the full text of the section.
    """
    # Retrieves section content for detailed reading
    ...
```

**Key point:** The tool design follows a **hierarchical navigation** pattern:
1. `search_pages` — broad retrieval (top 10 results by embedding similarity)
2. `view_sections` — narrow navigation (table of contents for a page)
3. `read_section` — deep reading (full text of a specific section)

This three-level structure teaches the agent to explore efficiently rather than reading everything. It also makes the task more challenging for RL — the agent must learn *which* sections to read based on the question, not just brute-force all content.

---

## Section 4: Synthetic QA Dataset Generation

The training data is generated synthetically: GPT-4.1 Mini reads Wikipedia articles and produces trivia-style question-answer pairs.

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()
semaphore = asyncio.Semaphore(3)  # Limit concurrent API calls

async def generate_qa_for_page(page_id: str) -> list[dict]:
    """Generate trivia QA pairs from a single Wikipedia page."""
    async with semaphore:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": (
                    "You are a trivia question writer. Given a Wikipedia article, "
                    "generate 5 advanced pub trivia questions. Questions should be "
                    "self-contained (no reference to 'the article' or 'according to'). "
                    "Answers should be short (1-5 words)."
                )},
                {"role": "user", "content": f"Article:\n{article_text}"},
            ],
        )
        # Parse structured QA pairs from response
        ...

# Generate ~750 questions from 150 pages (5 per page)
all_qa_pairs = await asyncio.gather(*[
    generate_qa_for_page(page_id) for page_id in page_ids
])

# Publish to HuggingFace
# dataset.push_to_hub("willccbb/wiki-trivia-questions")
```

**Key insight:** The synthetic data generation has several deliberate design choices:
- **"Advanced pub trivia" framing** — forces questions that are self-contained and don't reference the source article, making them valid evaluation targets
- **Short answers (1-5 words)** — enables automated evaluation without ambiguity
- **Semaphore = 3** — balances speed against API rate limits
- **GPT-4.1 Mini as generator** — cheap enough to generate hundreds of questions, smart enough to produce quality trivia

This dataset serves dual purpose: training data for RL and evaluation benchmark for measuring agent performance.

---

## Section 5: The Verifiers Framework

[Verifiers](https://github.com/PrimeIntellect-ai/verifiers) (created by Will Brown, ~4,000 GitHub stars) provides the RL environment abstraction. It wraps tools, prompts, and evaluation into a unified interface.

```python
import verifiers as vf

# Define the system prompt for the search agent
system_prompt = """You are a Wikipedia search agent. Given a question, 
use the available tools to find information and answer accurately.
Always search before answering. Think step by step."""

# Create the tool environment
vf_env = vf.ToolEnv(
    system_prompt=system_prompt,
    tools=[search_pages, view_sections, read_section],
    dataset=qa_dataset,           # The synthetic QA pairs
    judge_model="gpt-4.1-nano",   # Cheap model for LLM-as-judge
)
```

**Key point:** `vf.ToolEnv` is the central abstraction — it encapsulates:
- The **system prompt** (how the agent behaves)
- The **tools** (what the agent can do)
- The **dataset** (what questions to evaluate on)
- The **judge model** (how to score responses)

This separation means you can swap any component independently — change the tools, update the prompt, or try a different judge — without rewriting the evaluation logic.

### Evaluation Rubric with LLM-as-Judge

```python
from verifiers.rubrics import JudgeRubric, RubricGroup

# LLM-as-judge rubric: evaluates final answer correctness
judge_rubric = JudgeRubric(
    judge_model="gpt-4.1-nano",
    rubric="Does the agent's final answer correctly answer the question? "
           "Score 1.0 for correct, 0.5 for partially correct, 0.0 for incorrect."
)

# Composable rubric group: combines multiple evaluation criteria
rubric = RubricGroup([
    judge_rubric,              # Answer correctness (LLM judge)
    # Plus format compliance, tool call validity, etc.
])

# Run evaluation
results = await vf_env.evaluate(
    model="deepseek-v3-0324",
    num_samples=10,  # Start small, then scale
    rubric=rubric,
)
```

**Key insight:** The `JudgeRubric` uses [[concepts/agent-evaluation-methodology|LLM-as-judge]] — a cheap model (GPT-4.1 Nano) evaluates whether the agent's answer matches the expected answer. This is critical for RL because you need a differentiable reward signal. The rubric is *composable* via `RubricGroup`, meaning you can combine answer correctness with format compliance and tool-use quality into a single reward function. The notebook also tests Gemma 3 12B as a cheaper judge alternative.

---

## Section 6: Baseline Evaluation with DeepSeek V3

Before training, you need a baseline. The notebook evaluates DeepSeek V3 (0324) on the Wikipedia trivia task.

```python
# Small-scale test first
baseline_10 = await vf_env.evaluate(
    model="deepseek-v3-0324",    # Via DeepInfra API
    num_samples=10,
    rubric=rubric,
)
print(f"Baseline (10 samples): {baseline_10['mean_reward']:.3f}")

# Full baseline evaluation
baseline_200 = await vf_env.evaluate(
    model="deepseek-v3-0324",
    num_samples=200,
    rubric=rubric,
)
print(f"Baseline (200 samples): {baseline_200['mean_reward']:.3f}")

# Save traces as HuggingFace dataset for analysis
# Traces include: prompt, tool calls, tool results, final answer, reward
# Pushed to: willccbb/V3-wiki-trivia-tool-use
```

**Key point:** The evaluation pipeline produces **traces** — full records of each agent rollout including the prompt, every tool call, every tool result, the final answer, and the reward score. These traces are:
1. **Saved to HuggingFace** for reproducibility and community analysis
2. **Used as training data** — the verifiers library converts traces into the format needed for GRPO training
3. **Debuggable** — you can inspect exactly where the agent succeeded or failed

The 10→200 sample progression is a practical pattern: test cheaply first, then scale up once the pipeline is validated.

---

## Section 7: GRPO Training

The culmination — using [[concepts/grpo-rl-training|Group Relative Policy Optimization]] to actually train the agent. The verifiers library handles the complexity of converting environment rollouts into RL training data.

### How GRPO Works

```python
# Pseudocode for the GRPO training loop
# (handled by the verifiers + training framework integration)

# For each training step:
#   1. Sample a batch of questions from the dataset
#   2. For each question, generate G completions (a "group")
#   3. Run each completion through vf.ToolEnv (agent uses tools, gets reward)
#   4. Compute advantages within each group:
#      advantage_i = (reward_i - mean(rewards)) / std(rewards)
#   5. Update policy to increase probability of above-average completions

# Convert evaluation traces to training dataset
training_data = vf_env.make_dataset(traces)

# The training itself uses a framework integration (e.g., PrimeIntellect's
# training stack) that consumes the dataset and runs GRPO updates
```

**Key insight:** GRPO's elegance is in eliminating the critic model. In PPO, you need a separate value network to estimate baselines — this roughly doubles memory and compute. GRPO instead computes advantages *relative to a group* of completions for the same prompt:

$$A_i = \frac{r_i - \text{mean}(\{r_1, ..., r_G\})}{\text{std}(\{r_1, ..., r_G\})}$$

If your group has G=8 completions and 2 get the right answer (reward=1.0) while 6 get it wrong (reward=0.0), those 2 correct completions get high positive advantage and the 6 incorrect ones get negative advantage. The policy is then updated to make the correct completions more likely.

This is **~50% less compute** than PPO for equivalent training quality, which is why [[concepts/grpo-rl-training|GRPO]] has become the standard RL backbone since [[concepts/deepseek-r1|DeepSeek-R1]].

### Key Training Properties

| Property | Detail |
|----------|--------|
| **Training duration** | Hours, not days — GRPO is sample-efficient |
| **Checkpointing** | Save intermediate checkpoints to resume or compare |
| **Reward signal** | Composite: answer correctness + format compliance + tool use |
| **Group size** | Typically G=8 or G=16 completions per question |
| **Learning** | Agent learns *which tools to call* and *when* through reward signals |

---

## Section 8: Putting It All Together

The complete pipeline demonstrated in the notebook:

```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│  ChromaDB Setup  │────→│  Tool Definitions │────→│  Synthetic QA Gen │
│  (Wikipedia idx) │     │  (search/nav/read)│     │  (GPT-4.1 Mini)   │
└─────────────────┘     └──────────────────┘     └───────────────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│  GRPO Training  │←────│  Trace Dataset    │←────│  Baseline Eval    │
│  (RL updates)   │     │  (HuggingFace)    │     │  (DeepSeek V3)    │
└─────────────────┘     └──────────────────┘     └───────────────────┘
        │
        ▼
┌─────────────────┐
│  Trained Agent   │
│  (better tool    │
│   use patterns)  │
└─────────────────┘
```

The agent doesn't just learn *answers* — it learns **tool-use strategies**: which queries to search with, which sections to navigate to, when to read deeper vs. when to answer from what it already knows.

---

## Key Takeaways

1. **RL trains tool-use patterns, not just answers** — the agent learns *how* to search and navigate, not just *what* to say. This is the core value of [[concepts/agentic-rl|agentic RL]] over supervised fine-tuning.

2. **Local, deterministic tools are essential for RL** — ChromaDB with embeddings provides rate-limit-free, reproducible search. You can't train with tools that fail randomly or hit API limits during thousands of rollouts.

3. **Synthetic data generation is cheap and effective** — GPT-4.1 Mini generates hundreds of trivia QA pairs from Wikipedia at low cost. Short answers (1-5 words) enable automated evaluation without ambiguity.

4. **LLM-as-judge provides scalable reward signals** — `JudgeRubric` with a cheap judge model (GPT-4.1 Nano or Gemma 3 12B) evaluates answer correctness at scale. Composable rubrics combine multiple criteria into a single reward.

5. **GRPO eliminates the critic model** — group-relative advantage computation means ~50% less compute than PPO. For each question, generate G completions, score them, and update toward above-average ones.

6. **Traces are the bridge between evaluation and training** — the verifiers library converts agent rollouts (prompts, tool calls, answers, rewards) directly into RL training datasets. This is the key integration point.

7. **Start small, then scale** — 10-sample evaluation before 200-sample baseline; test the pipeline end-to-end before committing to expensive training runs.

---

## Related

- [[raw/articles/2025-06-10_willbrown_training-agents-with-rl-lightning|Lightning Lesson Summary]]
- [[raw/articles/2025-06-10_willbrown_build-your-own-research-agent-lightning|Lightning Lesson 1: Build Your Own AI Research Agent]]
- [[transcripts/2025-06-10_willbrown_build-your-own-research-agent-notebook|Notebook Walkthrough: Build Your Own AI Research Agent]]
- [[transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture|Lesson 1: Agent Patterns & Principles (Lecture)]]
- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[entities/will-brown]]
- [[concepts/grpo-rl-training|GRPO RL Training]]
- [[concepts/agentic-rl|Agentic RL]]
- [[concepts/agent-evaluation-methodology|Agent Evaluation Methodology]]
- [[entities/prime-intellect|Prime Intellect]]
