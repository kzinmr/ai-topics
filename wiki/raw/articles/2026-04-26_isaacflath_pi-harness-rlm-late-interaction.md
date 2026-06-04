---
title: "Isaac Flath — Pi Harness: RLM + Late Interaction Retrieval"
date: 2026-04-26
date_ingested: 2026-06-04
source: https://x.com/isaac_flath/status/2048462111567982823
author: Isaac Flath (@isaac_flath)
type: x_note_tweet
tags: [rlm, late-interaction, retrieval, agent-harness, harness-engineering, pylate, context-engineering, repl, code-act]
related:
  - concepts/rlm-recursive-language-models
  - entities/lighton
  - entities/isaac-flath
---

# Pi Harness: RLM + Late Interaction Retrieval

**Source:** [X/Twitter Note Tweet](https://x.com/isaac_flath/status/2048462111567982823) by Isaac Flath (@isaac_flath), 2026-04-26
**Engagement:** 650 likes, 1,137 bookmarks, 50 retweets, 41K impressions

---

## Full Text

RLM is the most important foundation of my Pi Harness (other than Pi of course). It's seeded with late interaction retrieval results (thanks to @lightonai for pylate).

The Agent initiates it with query then..

**SETUP**

A python REPL is created and seeded with:
1. Late interaction search to pre-filter. Instead of doing top 3/5/10, it's top hundreds of documents. This is set into a `context` variable.
2. Python functions are loaded in to do more searches if `context` variable isn't enough. And to make llm calls with cheaper models in parallel batches.

**ITERATION**

From there, an LLM iterates in the REPL based on the query. It's just like exploring in a jupyter notebook. The LLM writes prose (like a markdown cell) and code to be run in the REPL each turn.

This allows the LLM to sort, filter, and synthesize information. It can fan out and ask smaller models to summarize, combine, contrast, or do anything else to documents to help it understand the data.

After several turns the LLM responds with the final answer. Either because it found the answer, or hit the budget limit.

Context as a Python variable, LLM as the programmer, REPL as the runtime.

**WHY THIS WORKS**

1. **Richer Shell.** Agents (and subagents) work by intermixing code and prose/thinking. But they use static scripts or bash that run and exit and start over each tool call. That's not ideal for exploration and synthesis of data. For that, state is useful to continue building and exploring the data as you learn more. There's a reason jupyter notebooks have been popular with data scientists.

2. **Keeps main agent context clean.** The better context you have the better the agent will perform (duh!). This means three things: better human input, less missing search results, and less incorrect search results. Letting the agent iterate allows it to synthesize just what is needed and nothing else. All bad paths or peeks at something that turns out to be irrelevant stays out of main agent context.

3. **Stack the good ideas!** People often compare late interaction search vs RLM. Or static vs dynamic languages. Or agentic search vs semantic search. But...You can just use them all together for what they're each good at. Use them all for the area they're really great for.

Read the full post which has more detail about how and why.

https://isaacflath.com/writing/rlm

---

## Key Concepts

- **Pi Harness**: Isaac Flath's agent harness architecture, built on RLM as its foundation
- **Late Interaction Retrieval**: Pre-filtering with hundreds of documents (not top-k) using ColBERT-style late interaction models via [PyLate](https://github.com/lightonai/pylate) from [[entities/lighton|LightOn]]
- **REPL-as-Context**: The Python REPL serves as the runtime context — context is stored as Python variables, the LLM acts as the programmer
- **Iterative Synthesis**: LLM writes prose + code each turn (like Jupyter notebook cells), enabling stateful exploration
- **Budget-Limited Iteration**: Continues until answer found or budget limit hit
- **Composability Philosophy**: "Stack the good ideas" — combine late interaction search + RLM + agentic search + semantic search, using each for what it's best at

## Connection to RLM Framework

This tweet describes a practical implementation of the [[concepts/rlm-recursive-language-models|RLM (Recursive Language Models)]] paradigm with a specific twist: the REPL is **seeded** with late interaction retrieval results (hundreds of documents via ColBERT/PyLate), giving the RLM a richer starting context than typical top-k retrieval.

## Related Links

- [[concepts/rlm-recursive-language-models]] — The underlying RLM framework
- [[entities/lighton]] — PyLate / late interaction retrieval library
- [[entities/isaac-flath]] — Author
