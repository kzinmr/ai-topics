---
title: "Cheat at Search — Long Running Search Agents (Slides)"
author: Doug Turnbull (@softwaredoug)
date_ingested: 2026-06-02
type: article
tags:
  - agentic-search
  - long-running-agents
  - context-management
  - memory
  - harness-engineering
  - search
  - ai-agents
  - crawling
  - local-index
  - topic-modeling
sources:
  - https://docs.google.com/presentation/d/1EqEXSIjZo-MyA7f7r5nCuzCBrQmY0pA4VHtqayXPr70/edit
---

# Cheat at Search — Long Running Search Agents

**Author:** Doug Turnbull (SoftwareDoug / softwaredoug.com)
**Date:** June 2, 2026
**Format:** Google Slides presentation
**Companion course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)

---

## Overview

This lecture covers **long-running search agents** — agents that operate over extended periods (days, weeks, months) to perform iterative search tasks. The key challenges are:

- How to avoid exhausting context over many runs
- How to guide agents toward novel searches (not just steering away from bad ones)
- How to balance fresh context with accumulated knowledge

---

## 1. The Task: Gather Experts via Patent Search

The motivating example is a **recruiter-like scenario**: finding experts in a given domain using Google Patent Search as a proxy for a real candidate search system (e.g., LinkedIn, Indeed).

**Product rationale:** "As a recruiter, I want to find Java programming experts who know Spring and Hibernate and want to work remotely."

The recruiter's manual workflow involves:
1. Iterating through keyword-based searches
2. Collating results manually (spreadsheet)
3. Tracking what they've found to avoid duplication

**Goal:** Agentify this process — have an agent perform searches, maintain a spreadsheet of found experts, avoid duplicate work, and continuously find novel relevant people.

---

## 2. Search vs. Crawling

Long-running search agents blur the line between **search** and **crawling**:

- **Search:** A one-shot query to find relevant results
- **Crawling:** A long-running process that visits sources over time, avoids revisiting, and builds up a local index

The agent uses a **prompt to make a bespoke index** focused on a specific problem — instead of a generic web crawler, it's building a specialized local store of experts.

---

## 3. Measurement Framework

**Metrics to optimize:**
- Minimize duplicate patent searches
- Minimize total calls to Google Patents API (cost: tokens + external API fees)
- Maximize total experts found over time

**Per-call yield** = experts found / patent search calls

Tool calls are a good proxy for output tokens (and thus cost), because tool call requests are output tokens being emitted.

---

## 4. Approach 1: Single Large Context

The simplest approach — let the agent run with ever-growing context:

- Append all tool call results to the same context
- Agent sees full history of what it's done
- **Result:** 35 experts for 44 calls (yield: 0.795)
- No duplicates (prevented by tool guardrail)

**Problem:** Context grows linearly. Won't work for truly long-running tasks (context window limits, context rot).

---

## 5. Approach 2: Cron Job (Fresh Context + Persistent Memory)

Simulate a cron job that restarts the agent periodically:

- **Fresh context** each run (no accumulated history)
- **Persistent agent state** (search tracker remembers all past queries)
- Tool returns errors for previously-searched queries

**Result:** 56 experts for 77 calls (yield: 0.72)

**Key insight:** The agent wastes many tool calls retrying searches that have already been done. These failed attempts eat up context and output tokens, but don't appear in the fresh context.

**Why keep memory but reset context?** The goal is to find more experts — we don't want the agent repeating yesterday's searches. Fresh context avoids context rot, but persistent memory prevents duplication.

---

## 6. Approach 3: Compaction (Search History Summary)

Instead of letting the agent discover past searches through trial and error, **inject a summary** of previous searches into the prompt:

```
Summary of previous searches:
Searched: cat litter, Found: Interactive Pet Accessories, Litter Apparatus...
```

**Result:** 31 experts for 42 calls (yield: 0.738)

**Trade-offs:**
- Saves tool calls (no wasted attempts)
- But the summary grows proportionally to N (number of historical queries)
- OK for a few runs, but not indefinite
- **We need O(n) context to warn against n queries** — no magic compaction can avoid this

---

## 7. Approach 4: Local Index (Expert Database)

Maintain a **local index** that the agent can search and insert into:

**Architecture:**
- External API: Google Patents (expensive — external cost)
- Local index: Pandas DataFrame (cheap — internal only)
- Agent writes to and reads from the local index

**Benefits:**
- Agent checks local index before making external calls
- Reduces wasted external API calls
- Agent self-organizes the data (generates NAICS classifications, descriptions)

**Data structure (ExpertDatabase):**
- `run_id`, `full_name`, `user_keyword_search`, `found_with`
- `expert_naics_numbers`, `expert_naics_names` (industry taxonomy)
- `request_naics_numbers`, `request_naics_names`
- `description`

**NAICS taxonomy:** A U.S. industry classification system. The agent generates NAICS codes when inserting experts — this makes the data self-organizing because the same agent does both indexing and searching.

**Result:** 51 experts for 19 patent search calls (yield: 2.68)

**Key insight:** The local index serves as both a search tracker AND a knowledge store. The agent doesn't need a separate duplicate-checking system — it can query the local store to see what's already been found.

---

## 8. Approach 5: Frontier Exploration (Topic Clustering)

The remaining challenge: even with a local index, the agent still wastes calls exploring internal APIs. How do we express the **frontier** of what's been searched without listing every detail?

**Solution: LDA topic clustering + LLM-guided next topic selection**

1. **Cluster past queries** using LDA (Latent Dirichlet Allocation) — a classic ML technique that groups queries into topics
2. **LLM selects next topic** — given the topic summaries, an LLM generates a new subtopic to explore
3. **Rewrite the search prompt** — the selected topic becomes the new instructions for the search agent

**Example flow:**
```
Topics thus far → Next topic selection LLM → "Find biodegradable kitty litter"
→ Rewritten search prompt → Agentic loop → Google Patents → New experts → Local DB
```

**Example LLM-generated direction:**
> "Recommendation: End-of-life and compostability of cat litter. Rationale: Several topics touch on biodegradable/compostable litter, but there's less focus on what happens after use..."

**Result:** 55 experts for 33 calls (yield: 1.667) — fewer local calls, slightly more experts

**Key insight:** Topic-guided exploration doesn't help much until the "easy cases" are exhausted. Biggest gains come from the local index itself.

---

## 9. Alternative: Non-Agentic Query Prediction

A completely different approach — **skip the agent entirely**:

- Train a model to predict the next best query given the history of queries and their results
- Reward = number of new experts found
- Features: NAICS counts, topic breakdowns, run history

**Pros:** Simpler prediction task, potentially very low cost per query
**Cons:** Loses agentic reasoning to explore and reflect on results

**Hybrid approach:** Use a query scorer to rank LLM-generated candidate queries, combining traditional ML efficiency with agentic creativity.

---

## 10. Monitoring and Human-in-the-Loop

- Track when **diminishing returns** set in
- Save state for troubleshooting
- Don't hesitate to get **human in the loop**
- New requests can be injected into the same run

---

## 11. Future: Agents Querying Their Own History

What if agents could **search their old context** as a tool?

```python
tools=[patent_search, my_old_context_search]
```

Even more: what if agents could **generate their own code** to explore past state and the corpus?

---

## Key Takeaways

1. **Local index is the biggest win** — maintain a structured store that the agent reads and writes
2. **Fresh context + persistent memory** is a viable pattern for long-running tasks
3. **Compaction helps but scales linearly** — can't run indefinitely
4. **Topic clustering guides exploration** — helps after easy cases are exhausted
5. **Tool calls = cost proxy** — minimize both external API calls and wasted internal calls
6. **Agent self-organization** — when the same agent indexes and searches, it uses consistent terminology
7. **Crawling > searching** — long-running tasks are more like crawlers than search engines

---

## Related

- [[articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents|Steering Lost Agents — Cheat at Search (Slides)]]
- [[articles/2026-05-20_softwaredoug_cheat-at-search-llm-query-understanding|LLM Query Understanding — Cheat at Search (Slides)]]
- [[concepts/agentic-search|Agentic Search]]
- [[concepts/context-engineering|Context Engineering]]
