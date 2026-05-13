---
title: "How To Build Your First Agentic Search Application — Hugo Bowne-Anderson (Vanishing Gradients Annotated Presentation)"
created: 2026-02-21
author: Hugo Bowne-Anderson (@hugobowne)
guest: Doug Turnbull (@softwaredoug)
source: Substack (Vanishing Gradients)
url: https://hugobowne.substack.com/p/how-to-build-your-first-agentic-search
youtube_url: https://www.youtube.com/watch?v=AJPH9kpN3Sc
type: talk-annotated
duration: 35:22
tags: [agentic-search, tool-calling, harness-engineering, bm25, in-prompt-rl, llm-as-judge, recursive-language-models]
---

# Talk Overview

Hugo Bowne-Anderson's annotated version of Doug Turnbull's 35-minute Vanishing Gradients talk on **building agentic search applications**. Hugo provides slide-by-slide annotations with timestamps, extracted key insights, and Q&A highlights. This complements the raw transcript by adding editorial framing and cross-references to the broader agent harness discourse.

## Core Agenda (3 Parts)

1. **Why agentic search matters** — Passive vs active search spectrum (System 1/System 2), domain applicability
2. **How to structure search and exploration** — Agentic loop architecture, tool transparency, BM25 over complex stacks
3. **Hacking in-prompt reinforcement learning** — Harness validation loop, LLM-as-judge feedback, "try harder" patterns

## Key Frameworks

### Passive vs Active Search (System 1/System 2)

| Spectrum End | Thinking Mode | User State | Example |
|---|---|---|---|
| **Passive (Recommender)** | System 1 (instinctual) | Browsing without specific goal | YouTube feed, Amazon browse |
| **Active (Agentic)** | System 2 (deliberate) | Can write a paragraph describing needs | Recruiter sourcing, job hunting, legal research |

Agentic search is most powerful at the **active end** — where intent is complex and the user wants exhaustive coverage ("leave no stone unturned").

### Why Traditional Search Stacks Are Overkill

Standard search stacks involve: query understanding → business rules → embeddings → vector DB → BM25 → rerankers → post-filtering. This complexity exists to interpret **short, ambiguous keyword queries**.

For agentic search, much of this stack can be discarded because:
- The agent possesses the **full narrative context** (user's paragraph-long intent)
- The agent has **reasoning capabilities** to analyze and reformulate
- Simple, **transparent tools** (BM25, grep) let the agent understand cause and effect

**Benchmark result**: Adding a reasoning loop to a basic BM25 tool outperforms the baseline by **15-30% NDCG** on Wayfair WANDS and Amazon ESCI, with **no model training**.

### The Core Tool-Calling Loop

```python
# 40 lines of Python — the essence of agentic search
inputs = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_query}
]
# Agent loop
while True:
    response = openai.chat.completions.create(
        model="gpt-4o", messages=inputs, tools=[search_tool]
    )
    if response.choices[0].finish_reason == "stop":
        break  # Agent produced final answer
    # Parse function_call, execute tool, append results
    inputs.append(response.choices[0].message)
    inputs.append({"role": "tool", "content": execute_search(args)})
```

### In-Prompt Reinforcement Learning (Key Innovation)

The most novel technique covered: **simulating reinforcement learning within the prompt itself** by wrapping the agentic loop in a "Harness" that acts as a dissatisfied user.

**Problem**: LLMs lack domain-specific knowledge. An agent searching for "bistro table" for a restaurant may return patio furniture results and assume success.

**Solution — The Harness Validation Loop**:
1. Agent produces results via the standard tool-calling loop
2. A **validator** (LLM-as-judge, reranker, or classifier) inspects each result
3. If a result is relevant → context gets `"Great work!"`
4. If a result is irrelevant → context gets `"This doesn't make me happy! Sorry!"`
5. This **exploits the LLM's sycophantic nature** — negative feedback triggers reformulation

```python
# Pseudo-code for the harness wrapper
def harness(user_prompt):
    inputs = build_initial_context(user_prompt)
    valid = False
    while not valid:
        inputs = agent_loop(inputs)  # Inner LLM tool-calling loop
        results = extract_results(inputs[-1])
        valid = True
        for result in results:
            if not is_relevant(result, user_prompt):
                inputs.append({"role": "system",
                    "content": "This doesn't make me happy! Sorry! Try harder."})
                valid = False
                break
            else:
                inputs.append({"role": "system", "content": "Great work!"})
    return results
```

This is **"in-prompt RL"** — guiding the agent away from bad search spaces toward relevant results without manual human intervention, by simulating reinforcement signals in the prompt itself.

**Key insight**: Components discarded from the traditional search stack (rerankers, classifiers) are useful here — not as retrieval middleware, but as **validators** in the outer harness loop.

### Recursive Language Models for Long-Running Agents

For agents that run for extended periods, **linear chat history becomes a bottleneck**. Emerging technique: **Recursive Language Models** where the agent's memory isn't just the chat history but a **context variable** (like a Python dictionary or markdown file) that it can inspect and modify using code generation tools. This enables effectively **unbounded context** without suffering from context window limits.

See: [[concepts/rlm-recursive-language-models]], [[concepts/recursive-language-models]]

## Q&A Highlights

**Q: Limitations of grep/file-system search for agents?**
A: grep is transparent but lacks ranking. It assumes organized directory structures (often false). Ranked search (BM25) is superior — it cuts through arbitrary file organizations and bubbles up the most relevant results.

**Q: Frameworks like Pydantic AI for building agentic search?**
A: Build the plumbing yourself first using direct API integration. Understanding the raw loop — how tool calls are serialized and context managed — is valuable before abstracting it away. Ultimately, the best framework is whatever your engineering team is most comfortable using.

**Q: Where is agent context heading?**
A: Toward "Recursive Language Models" where agents use code generation to explore a context variable (Python dict, markdown file). This allows agents to manage their own memory, perform compaction, and handle unbounded contexts.

## Connection to Wiki Concepts

- [[concepts/agentic-search]] — Core concept page; this talk provides implementation-level detail
- [[concepts/bm25]] — BM25's transparency makes it ideal for agent-driven search
- [[concepts/rlm-recursive-language-models]] — Context variable pattern for long-running agents
- [[concepts/harness-engineering]] — The outer validation loop is harness engineering in practice
- [[entities/hugo-bowne-anderson]] — Host and curator
- [[entities/doug-turnbull]] — Speaker and practitioner
