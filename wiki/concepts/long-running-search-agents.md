---
title: Long Running Search Agents — Design Patterns
type: concept
created: 2026-06-02
updated: 2026-06-02
tags:
  - agentic-search
  - durable-execution
  - context-management
  - agents
  - evaluation
sources:
  - https://docs.google.com/presentation/d/1EqEXSIjZo-MyA7f7r5nCuzCBrQmY0pA4VHtqayXPr70/edit
  - https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1
  - raw/articles/2026-06-04_softwaredoug_exhaustive-search-beam-search.md
---

# Long Running Search Agents — Design Patterns

Design patterns for search agents that run unattended for hours, days, or weeks — and the progressive strategies for avoiding context exhaustion, duplicate work, and diminishing returns.

Based on Doug Turnbull's [[entities/doug-turnbull-speaking|Cheat at Search]] lecture series (June 2026), with experimental results on a patent-search task.

## Problem Statement

A search agent tasked with "find all Java/Spring/Hibernate experts who want remote work" or "find kitty litter experts from the patent database" can run indefinitely. The fundamental challenge: **how to maximize actual gain (new experts found) while minimizing wasted context (duplicate searches, repeated API calls) over an unbounded number of runs.**

### Key Metrics

| Metric | Goal |
|--------|------|
| Duplicate searches | Minimize |
| External API calls (Google Patents) | Minimize |
| Total new experts over time | Maximize |
| **Yield per call** (new experts / total calls) | Maximize |

## Strategy 1: Single Context (Baseline)

Run the agent in one continuous context window with a stopper (e.g., stop after N tool calls).

```python
resp, inputs = harness(
    inputs=inputs,
    agent_state=agent_state,
    tools=[patent_search],
    stoppers=[stop_after_N_calls],
    model='gpt-5-mini',
)
```

**Result: 35 experts / 44 calls = 0.795 yield per call, no duplicates.**

**Limitation:** Single context won't scale. The agent will eventually exhaust its context window and degrade. Reality: need to restart the task regularly.

## Strategy 2: Cron Job (Fresh Context Restarts)

Simulate the agent restarting with fresh context each run, carrying state via `agent_state`:

```python
all_results = []
for _ in range(6):
    inputs = [{"role": "system", "content": system_prompt},
              {"role": "user", "content": "We need kitty litter experts"}]
    resp, inputs = harness(inputs=inputs, agent_state=agent_state, ...)
```

**Result: 56 new experts / 77 calls = 0.72 yield, but 34 duplicate searches.**

**Problem:** Each restart wastes tokens re-sending the same system prompt and user query. The agent retries old searches because it lacks awareness of what's been done. The wasted context grows proportionally with N historical queries — O(n) growth makes this unscalable.

## Strategy 3: Context Compaction

Instead of replaying full history, summarize previous search results into the prompt:

```python
if search_summary:
    inputs.append({"role": "assistant",
                   "content": "Summary of previous searches:\n\n" + search_summary})
search_summary += summarize_search_results(inputs)
```

**Result: 31 experts / 42 calls = 0.738 yield.**

**Analysis:** Slightly worse than single context (expected), but still O(n) in the summary size. Works for a few runs, not indefinitely. Compaction of a large set of historical queries doesn't fundamentally solve the scaling problem.

> **Key insight:** "We need O(n) context to warn against / fail at n queries. Compaction of large set of data doesn't help. For long strategies, need a different way to guide the LLM."

## Strategy 4: Local Index / Memory (Biggest Gain)

Replace context-based tracking with a **local dataframe** that persists across runs:

```python
class ExpertDatabase:
    def __init__(self, model):
        self.db = pd.DataFrame(columns=[
            'run_id', 'full_name', 'user_keyword_search',
            'found_with', 'expert_naics_numbers', 'expert_naics_names',
            'request_naics_numbers', 'request_naics_names', 'description'
        ])
```

### Two-Tool Architecture

1. **`search_local_store(query, naics_name)`** — Check local memory before making external API calls
2. **`add_expert_to_local_store(expert, ...)`** — Insert new experts, return duplicates

The local index is **self-organizing**: using a taxonomy the agent already knows (NAICS industry codes), the LLM can search even with hallucinated codes and still find relevant experts.

**Result: 51 new experts / 19 calls = 2.68 yield per call.**

This is a **3.7x improvement** over Strategy 2 (cron job) and **3.4x improvement** over Strategy 1 (single context). The biggest gains come from avoiding wasted external API calls — local checks are cheap.

> "This makes the data self-organizing!" — Using structured taxonomies (NAICS) for local search means hallucinated queries still match relevant entries.

## Strategy 5: Frontier Prompt (Guided Exploration)

After establishing a local index, the next challenge: how to guide the agent to explore new territory rather than searching in already-explored areas.

### Topic Modeling + Next-Query Selection

```python
def summarize(user_keywords, expert_db, run_id):
    unique_queries = expert_db.past_patent_searches[run_id].names
    docs = [simple_preprocess(t) for t in unique_queries]
    dictionary = corpora.Dictionary(docs)
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    lda = LdaModel(...)  # Cluster previously searched queries
```

A separate "next topic" LLM uses the topic model to suggest new search directions:

```python
def next_topic_prompt(user_keywords, expert_db, run_id):
    summary = summarize(keywords, expert_db, run_id)
    return f"""While searching for {user_keywords}, here's what to do next
    (because we've already searched the obvious places): {summary}"""
```

### Example Frontier Output

> **Recommendation:** End-of-life and compostability of cat litter
>
> **Rationale:** Several topics touch on biodegradable/compostable litter, but there's less focus on what happens after use. This subtopic helps distinguish between plant-based vs mineral-based litters in real-world waste streams.
>
> **Keywords to search:** "OK compost" "home" vs "industrial", "EN 13432", "EN 14855"

**Result: 55 new experts / 33 calls = 1.667 yield.**

Fewer local calls than Strategy 4, slightly more experts. But the key finding: **changing goals / redirecting doesn't help until we've exhausted the easy cases.** The frontier prompt's benefit only materializes after the local index has accumulated enough history to identify gaps.

### Architecture: Two-Loop Design

```
Topics Thusfar → Next-Topic LLM → Rewritten Search → Agentic Loop → Google Patents → Local DB → New Experts
```

This separates **exploration planning** (what to search next) from **execution** (how to search and extract).

## Strategy 6: Non-Agentic Query Model

An alternative: replace the entire agentic loop with a trained query-scoring model:

```
Query History + State (topics, NAICS counts) → Query Model → Single Query → Google Patents → Local DB
```

Instead of an agent reasoning about what to search, a supervised model directly predicts the next query given the current state.

### Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Query prediction model** | Simpler prediction, traditional ML task, low cost at scale | Loses agentic reasoning, harder to model |
| **Long-running agent + frontier** | Easy to setup, agentic reasoning for troubleshooting | Hoping LLM makes principled decisions, prompt magic |
| **Hybrid** | Query scorer + LLM candidates | Best of both? |

## Strategy 7: Agent Self-Querying

Two forward-looking ideas:

1. **Query old context:** Agent can search its own previous runs via a `my_old_context_search` tool
2. **Generate code to explore state:** Agent writes Python scripts to analyze its own accumulated data — turning the local index from passive storage into an active research tool

```python
resp, inputs = harness(
    inputs=inputs,
    agent_state=agent_state,
    tools=[patent_search, my_old_context_search],
    stoppers=[stop_after_N_calls],
)
```

## Experimental Summary

| Strategy | New Experts | Total Calls | Yield/Call | Duplicates | Key Insight |
|----------|------------|-------------|-----------|-----------|------------|
| 1. Single context | 35 | 44 | 0.795 | 0 | Good start, but context exhaustion inevitable |
| 2. Cron job (restart) | 56 | 77 | 0.720 | 34 | Wasted context grows O(n) |
| 3. Compaction | 31 | 42 | 0.738 | — | Still O(n), doesn't scale indefinitely |
| **4. Local index** | **51** | **19** | **2.68** | **Few** | **Biggest gain — avoid external API waste** |
| 5. Frontier prompt | 55 | 33 | 1.667 | Fewer local | Helps only after easy cases exhausted |
| 6. Query model | TBD | TBD | TBD | TBD | Simpler but loses reasoning |

## Design Principles

1. **Local memory before external calls** — The single biggest efficiency gain. Check what you know before searching outside.
2. **Self-organizing data** — Use structured taxonomies (NAICS, schemas) so even hallucinated queries produce useful results.
3. **O(1) or O(log n) state in prompt** — Don't let historical context grow linearly. Summarize the frontier, not the history.
4. **Separate planning from execution** — A "next topic" LLM guides the agent loop; the agent handles detailed search and extraction.
5. **Monitor diminishing returns** — Track when the agent stops finding new experts and intervene (human-in-the-loop, strategy change).
6. **Agent can query its own state** — Treat accumulated data as a research resource, not just a deduplication filter.

## Connection to Broader Concepts

- [[concepts/agentic-search]] — Agentic search paradigm; this lecture provides the empirical foundation for "agents make dumb retrievers smart"
- [[concepts/durable-execution]] — State persistence patterns; the local index is a form of durable state
- [[concepts/context-fragments]] — Memory state fragmentation; Strategy 3 (compaction) directly addresses this
- [[concepts/effective-harnesses-for-long-running-agents]] — Anthropic's harness design; complementary perspective from a search engineer
- [[concepts/managed-agents]] — Brain/hands separation; Strategy 5's two-loop design mirrors this pattern
- [[concepts/delta-channels]] — LangGraph's delta checkpointing; solves the same O(n) context problem differently
- [[entities/doug-turnbull]] — Doug Turnbull's core ideas on search and relevance

## Related Raw Articles

- [[raw/articles/2026-06-02_softwaredoug_cheat-at-search-long-running-search]] — This lecture (Google Slides source)
- [[transcripts/2026-06-02_softwaredoug_cheat-at-search-long-running-search-lecture]] — Lecture transcript (with audience Q&A on goal mode, context vs memory, access control, taxonomy)
