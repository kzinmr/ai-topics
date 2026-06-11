---
title: Exhaustive Agentic Search — Filesystem Metaphor and BEAM Traversal
type: concept
created: 2026-06-04
updated: 2026-06-04
tags:
  - search
  - ai-agents
  - harness-engineering
  - evaluation
aliases:
  - beam-search-agents
  - directory-search-agents
  - filesystem-metaphor-search
  - expert-gathering-pattern
sources:
  - raw/articles/2026-06-04_softwaredoug_exhaustive-search-beam-search.md
  - https://docs.google.com/presentation/d/1CHTHMot5JNZCpGjJs7w-p1Yz-D56AFLeVFhjJky5L20
  - https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1
related:
  - concepts/agent-steering
  - concepts/long-running-search-agents
  - concepts/agentic-search
  - concepts/effective-harnesses-for-long-running-agents
---

# Exhaustive Agentic Search — Filesystem Metaphor and BEAM Traversal

Design patterns for systematic, exhaustive exploration of organized knowledge spaces using LLM agents. Replaces random keyword probing with filesystem-like traversal (BEAM search), subagent composition, and persistent state tracking.

Based on Doug Turnbull's "Cheat at Search with Agents" supplement lecture (June 2026). This lecture bridges [[concepts/harness-engineering/agent-steering]] (Part 3: steering patterns) and [[concepts/long-running-search-agents]] (the subsequent lesson on long-running strategy experiments).

## Core Insight

> "What if there was a more systematic way?" — Doug Turnbull

Traditional agentic search is a **random walk**: the agent issues keyword queries and hopes to find relevant results. BEAM search over a structured filesystem reimagines this as **systematic traversal** — closer to how a human researcher explores a library than how a search engine retrieves documents.

The filesystem metaphor gives agents:
1. **Navigation** — `ls` to see categories/subcategories
2. **Search** — `grep` to find matches within a location
3. **Tracking** — `agent_state` records visited locations
4. **Pruning** — validators reject redundant/degraded exploration

## The Generalized Harness

The foundation is a reusable `harness()` function that separates concerns:

```python
def harness(inputs,
            agent_state,
            tools=None,       # Functions the agent can call
            stoppers=None,    # Functions that decide when to stop
            validators=None,  # Functions that validate outputs (retry on failure)
            text_format=str,  # Structured output format
            model='gpt-5-nano',
            task: Optional[str] = None,
            summary=True):
```

**Key design:** The harness loop is generic — nothing about it is search-specific. It applies to any agent task with tool calling, validation, and stop conditions.

### Loop Logic

```python
while not stop:
    resp, inputs = agent_run(...)
    for validator in validators:
        if not validator(resp, inputs):
            invalid = True
    if invalid:
        continue  # Retry with validator feedback appended to inputs
    for stopper in stoppers:
        if stopper(resp, inputs, call_count):
            break
```

Validators append error messages to `inputs` when validation fails, giving the agent feedback on what went wrong.

## Filesystem-Metaphor Search

### Building the Virtual Filesystem

Map structured data (e.g., e-commerce products) into a filesystem hierarchy:

```
wayfair/
  furniture/
    sofas/
      mid-century-modern-sectional.txt
    tables/
      dining-table-oak.txt
  hardware/
    tools/
      cordless-drill.txt
```

Each "file" contains the full product text (name, description, category hierarchy) — searchable via `grep`.

### Directory Tools

```python
ls, find_files_by_name, cat, grep = tools('wayfair/')
```

Four tools at each directory level:
- **`ls`** — List subcategories (directories)
- **`find_files_by_name`** — Find files by slug pattern
- **`cat`** — Read file contents
- **`grep`** — Search within files (regex)

### Single-Directory Agent Loop

An agent searches one directory level, returning `RelevantFiles`:

```python
resp = harness(
    inputs=inputs,
    agent_state={},
    validators=[file_exists_check],
    tools=[ls, find_files_by_name, cat, grep],
    task="Find relevant products for " + query,
    text_format=RelevantFiles
)
```

Returns two types of results:
1. **Directories** — categories to `cd` into and explore
2. **Files** — matching products at this level

### Wrapping as a Tool (Subagent-as-Tool)

The directory search agent becomes a composable tool:

```python
def search_directory(query: str, search_path: str, agent_state):
    """Search this path for relevant files or directories."""
    ls, find_files_by_name, cat, grep = tools(search_path)
    resp = harness(
        inputs=inputs,
        agent_state={},
        validators=[file_exists_check],
        tools=[ls, find_files_by_name, cat, grep],
        task="Find relevant products for " + query,
        text_format=RelevantFiles
    )
    result.directories = [os.path.join(search_path, p) for p in result.directories]
    result.files = [os.path.join(search_path, p) for p in result.files]
    return result
```

### Deduplication via agent_state

Prevent the agent from searching the same path+query combination twice:

```python
def search_directory(query: str, search_path: str, agent_state):
    search_paths = agent_state['search_paths']
    if search_path in search_paths:
        if query in search_paths[search_path]:
            return f"You've already searched this path {search_path}"
```

### Orchestrator: Top-Level Search

```python
def furniture_search(query):
    resp, inputs = harness(
        model="gpt-5-mini",
        inputs=inputs,
        agent_state={},
        validators=[has_products_validator, has_n_products_validator],
        tools=[search_directory],  # Subagent wrapped as tool
        text_format=RelevantProducts
    )
    return resp.output_parsed
```

The orchestrator delegates directory exploration to `search_directory` subagents, each with fresh context.

## Agent State Persistence Across Runs

A critical pattern for long-running tasks: **reset inputs but keep agent_state**:

```
Orchestrator → Subagents (agent_state = last_agent_state)
  → Run loop with cleared agent state + new inputs
  → Avoid duplicating work of past runs
```

This is the bridge to [[concepts/long-running-search-agents]] — the state persists across context window resets.

## Hybrid Search: Directory + Keyword

Real-world data isn't perfectly organized. Relevant products can be in unexpected places ("discount bin", cross-category items). Combine structured traversal with free-form keyword search:

```python
resp, inputs = harness(
    validators=[has_products_validator, has_n_products_validator,
                labeled_query_products(judgments, query)],
    tools=[search_directory, search_with_keywords],  # Both approaches
    text_format=RelevantProducts
)
```

## Expert Gathering Pattern

The same patterns apply beyond e-commerce. The expert-gathering use case demonstrates:

### Patent Search as Crawler

```python
def patent_search(keywords: str, agent_state) -> PatentSearchResults:
    error = _track_search(keywords, agent_state)
    if error is not None:
        return PatentSearchResults(success=False, failure_reason=error, ...)
```

The tool itself enforces deduplication — the agent cannot repeat searches.

### NAICS Classification for Self-Organizing Data

Use an industry taxonomy the LLM already knows (NAICS codes) to classify discovered experts:

```python
class Naics(BaseModel):
    code: int
    name: str
    description: str
```

The local search then uses NAICS to filter: "find experts in this industry" becomes a structured query rather than a keyword search.

### Embedding-Based NAICS Search (Hallucination-Resistant)

When the LLM hallucinates a NAICS name, resolve via embeddings:

```python
naics_embedding = minilm.encode(naics_name, convert_to_numpy=True)
similarity = np.dot(naics_embedding, self.naics_embeddings.T)
most_similar_naics = self.all_industry_classifications[np.argmax(similarity)]
```

This makes the data **self-organizing**: even hallucinated queries produce useful results through semantic similarity.

### Personality Tracking for Long-Running Continuation

Agent outputs a `Personality` object that captures its learned preferences and search history:

```python
class Personality(BaseModel):
    name: str
    techniques: list[str]          # What works for finding experts
    areas_already_searched: list[str]  # What to avoid
```

This personality is injected as an assistant message in the next run, creating continuity without replaying full history.

## Architecture Diagram

```
Orchestrator Agent
  │
  ├── search_directory(query, "wayfair/furniture/", agent_state)
  │     └── harness(tools=[ls, grep, cat, find])
  │           └── Returns: directories + files
  │
  ├── search_directory(query, "wayfair/hardware/", agent_state)
  │     └── harness(tools=[ls, grep, cat, find])
  │           └── Returns: directories + files
  │
  └── search_with_keywords(query)  # Hybrid fallback
        └── Returns: direct matches

agent_state persists across all subagent calls
```

## Design Principles

1. **Filesystem as search metaphor** — Navigate, search, track, prune
2. **Harness is generic** — Nothing about it is search-specific; it's a tool-calling loop with validation and stop conditions
3. **Subagents as composable tools** — Each directory search is a wrapped subagent
4. **State persistence > context replay** — Keep agent_state, reset inputs
5. **Hybrid approaches** — Structured traversal + keyword search for coverage
6. **Self-organizing data** — Use taxonomies the LLM knows (NAICS) so even hallucinated queries match
7. **Personality tracking** — Agent learns and passes forward what works and what to avoid

## Connection to Existing Concepts

- [[concepts/harness-engineering/agent-steering]] — The BEAM search section there introduces the concept; this page provides full implementation details
- [[concepts/long-running-search-agents]] — Builds on these patterns with experimental results on yield-per-call optimization
- [[concepts/agentic-search]] — Broader paradigm; this is a specific technique within it
- [[concepts/effective-harnesses-for-long-running-agents]] — Anthropic's complementary approach to multi-context-window agents
- [[concepts/test-time-scaling]] — PRM-based beam search for reasoning; this applies beam search to information retrieval
