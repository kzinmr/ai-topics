---
title: "Cheat at Search with Agents — Exhaustive Search (Supplement Lecture)"
author: Doug Turnbull (softwaredoug)
date: 2026-06-04
type: article
source_url: https://docs.google.com/presentation/d/1CHTHMot5JNZCpGjJs7w-p1Yz-D56AFLeVFhjJky5L20
series: Cheat at Search with Agents
episode: supplement (pre-lesson on long-running search)
topics:
  - agentic-search
  - beam-search
  - harness-engineering
  - subagents
  - expert-gathering
  - naics-classification
---

# Cheat at Search with Agents — Exhaustive Search (Supplement Lecture)

**Speaker:** Doug Turnbull (SoftwareDoug LLC) — http://softwaredoug.com
**Date:** 2026-06-04 (supplement to "Cheat at Search with Agents" series)
**Context:** This lecture was delivered as a supplementary session immediately before the Long Running Search Agents lesson. It covers the foundational harness generalization and introduces systematic exploration patterns (BEAM search, directory search, expert gathering) that the long-running lecture builds upon.

**Colab notebook:** https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1

---

## Goals

- Exhaustive search across an "organize" space
- Long-running search and organizing work

## Part 1: Long Running Agents Lose Track

Long-running agents inevitably lose context. The mistake made at search #10 is forgotten by search #50. Context rots; agents forget.

**Better approach: restart** — reset context / `inputs` variable and start a new agentic search run.

## Part 2: Generalizing the Harness

Recap from previous lesson: the `search()` function with a tool-calling loop can be generalized into a reusable `harness()`:

```python
def harness(inputs,
            agent_state,
            tools=None,
            stoppers=None,
            validators=None,
            text_format=str,
            model='gpt-5-nano',
            task: Optional[str] = None,
            summary=True):
    ...
```

**Key components:**
- **tools** — List of functions to treat as tools
- **validators** — List of functions to validate outputs (retry with message back)
- **stoppers** — List of functions to decide when to stop
- **text_format** — Output format (str means normal chat)
- **agent_state** — Global state also seen by tools

**Notably: nothing here has to do with search.** This is a general agentic loop pattern.

### Harness Loop Logic

```python
while not stop:
    resp, inputs = agent_run(…)
    # Call validators, append any problems
    invalid = False
    for validator in validators:
        valid = validator(resp, inputs)
        if not valid:
            invalid = True
    if invalid:
        continue
    # Call stoppers
    for stopper in stoppers:
        stop = stopper(resp, inputs, call_count)
        if stop:
            break
```

### Example: Validation

```python
resp, inputs = harness(
    inputs=inputs,
    agent_state={},
    tools=[message_of_the_day],
    validators=[only_accept_if_steve_in_resp],
    model='gpt-5-nano',
    summary=True
)
```

### Degradation Validator

A validator that checks if search quality has degraded compared to the previous round:

```python
def degrade_validator(query):
    def search_degrade_validator(resp, inputs):
        search_results = resp.output_parsed
        all_graded = []
        for input in inputs:
            if ... (is graded) ...
                all_graded.append(grades(query, result))
        if len(all_graded) > 1:
            last_smileys = count_smileys(all_graded[-2])
            current_smileys = count_smileys(all_graded[-1])
            if last_smileys > current_smileys:
                inputs.append(_error_msg(
                    f"You've degraded your relevance, previously found "
                    f"{last_smileys} relevant results, and now found "
                    f"{current_smileys}"))
                return False
        return True
    return search_degrade_validator
```

**Results:** Reject if didn't get better than last round. Stop after N rounds.

## Part 3: Subagents as Composable Building Blocks

The harness becomes a composable building block:

```
Orchestrator Agent
  ├── Harness (another loop!) → Search Tool → Agentic Loop
  ├── Harness (another loop!) → Another Search Tool → Agentic Loop
  └── Harness (another loop!) → Subagent → Agentic Loop
```

**Why this matters: context preservation**
- Orchestrator: context preserved for "big picture"
- Subagents: context preserved for "smaller bits of the problem"

## Part 4: Directory Search — BEAM Search for Systematic Exploration

### Motivation: Random Walk → Systematic Traversal

So far, search was a random walk around a space. What if there was a more systematic way?

**Inspiration: a store layout / file system**
- Navigate to categories / subcategories
- "Search" (grep) within locations
- Track visited locations
- Implement a kind of **BEAM search**

### Setup: Create a "File Path" for Every Product

```python
def build_path(row):
    category = "uncategorized"
    if row.category:
        category = slugify(row.category)
    path = f"wayfair/{category}"
    sub_category = "uncategorized"
    if row.sub_category:
        sub_category = slugify(row.sub_category)
        path = f"wayfair/{category}/{sub_category}"
    title = doc_id
    if row.title:
        title = slugify(row.title.strip())
    path += f"/{title}.txt"
    return path

corpus['path'] = corpus.apply(build_path, axis=1)
```

Structure: `wayfair/<category>/<subcategory>/<product-name-as-slug>.txt`

### Tools at a Directory

```python
def tools(path):
    """Create tools that will work with all files directly under path (no recursion)."""
    ...

ls, find_files_by_name, cat, grep = tools('wayfair/')
```

Four tools: `ls` (list subcategories), `find_files_by_name`, `cat`, `grep` (search with regex).

### Step 1: Agent Loop for a Single Directory

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

The agent finds directories to explore and files that match.

### Step 2: Wrap as a Tool

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

### Step 3: Prevent Repeat Searches

```python
def search_directory(query: str, search_path: str, agent_state):
    search_paths = agent_state['search_paths']
    if search_path in search_paths:
        if query in search_paths[search_path]:
            return f"You've already searched this path {search_path}"
```

**agent_state** lets tools respond to agent calls based on state of the process.

### Step 4: Orchestrator Agent

```python
def furniture_search(query):
    system_prompt = """
    You are searching a file system of products.
    Find the most relevant products for the query.
    The top level path is wayfair/. You can use the search tool to find
    products or categories to explore.
    They're organized as: wayfair/<category>/<subcategory>/<product-name-as-slug>.txt
    """
    inputs = [{"role": "system", "content": system_prompt},
              {"role": "user", "content": query}]
    resp, inputs = harness(
        model="gpt-5-mini",
        inputs=inputs,
        agent_state={},
        validators=[has_products_validator, has_n_products_validator],
        tools=[search_directory],  # search_directory is now a tool!
        text_format=RelevantProducts
    )
    return resp.output_parsed
```

### agent_state Persistence Across Task Resets

Currently the orchestrator resets everything when spawning subagents. But what if we reset inputs while keeping state per task?

```
Orchestrator → Subagents (agent_state = last_agent_state)
    → Run loop with cleared agent state + new inputs
    → Avoid duplicating work of past runs
```

### Relevance Feedback Placement

Where should relevance feedback go? Options:
- At the orchestrator level
- At each subagent level
- Or both (via a Reranker/Judge)

### Hybrid Approach

Relevant products can be in unexpected places. Life isn't neatly organized. Combine directory search with keyword search:

```python
resp, inputs = harness(
    model="gpt-5-mini",
    inputs=inputs,
    agent_state={},
    validators=[has_products_validator, has_n_products_validator,
                labeled_query_products(judgments, query)],
    tools=[search_directory, search_with_keywords],
    text_format=RelevantProducts
)
```

## Part 5: Expert Gathering — Search as Crawler

### Patent Search Tool

```python
def patent_search(keywords: str, agent_state=None) -> PatentSearchResults:
    """Search google patents and pull back list of title, inventors,
       assignee (usually a company) and other metadata."""
    ...
```

### System Prompt for Expert Discovery

```
We need to find recruits for our company. You're rewarded by finding more,
relevant experts.
Use the patent search to find scientists we should network with.
Add them to the expert database.
You can search the expert database to find who we've already found.
The more, new users you can add (not duplicating work of existing searching),
the better.
```

### Challenge 1: Organizing Experts into a Search Index

Use NAICS (North American Industry Classification System) codes — an existing classification the LLM already knows:

```python
class Naics(BaseModel):
    code: int
    name: str
    description: str
```

Less friction to let LLM organize how it wants using known classifications.

### Challenge 2: Avoiding Repeated Searches

Store previous searches in agent_state. Return errors for duplicate searches:

```python
def patent_search(keywords: str, agent_state) -> PatentSearchResults:
    error = _track_search(keywords, agent_state)
    if error is not None:
        return PatentSearchResults(success=False, failure_reason=error,
                                   search_results=[])
```

### Challenge 3: Long-Running Continuation (Personality Tracking)

Make output contain guidance on how to avoid errors:

```python
class Personality(BaseModel):
    """Updated state of your preferences when finding experts."""
    name: str
    techniques: list[str]  # Best techniques to find experts and avoid errors
    areas_already_searched: list[str]  # Areas already searched, should be avoided

class Result(BaseModel):
    experts: list[Expert]
    personality: Personality
```

Pass personality to next run:

```python
inputs = [
    {"role": "system", "content": system_prompt},
    {"role": "assistant", "content": personality_prompt(resp.output_parsed.personality)},
    {"role": "user", "content": f"We need electric car experts"}
]
```

### Challenge 4: Embedding-Based NAICS Search (Hallucination-Resistant)

When the LLM might hallucinate a NAICS name, resolve to embeddings:

```python
def search_local_store(query: str, naics_name: str):
    naics_embedding = minilm.encode(naics_name, convert_to_numpy=True)
    similarity = np.dot(naics_embedding, self.naics_embeddings.T)
    most_similar_naics = self.all_industry_classifications[np.argmax(similarity)]
    filtered_mask = self.db['naics_names'].apply(lambda x: most_similar_naics in x)
```

### Full Result Model

```python
class Result(BaseModel):
    experts: list[Expert]
    naics: list[Naics]  # NAICS classifications closest to user's request
    personality: Personality
```

## Key Challenges Summary

1. How to get the agent to organize experts into a useful search index
2. How to get the agent to avoid repeating searches per task
3. How to start/stop (spawn new) agent when we want to search again → making it "long running"
4. Efficient exploration with tool errors preventing repeat searches
