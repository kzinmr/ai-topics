---
title: Cheat at Search — Steering Lost Agents (Agentic Design Patterns for Search)
type: raw-article
source: https://docs.google.com/presentation/d/1N7WqZ7vVgh60qi7Tt269XPXXPzrHb4cqvXvAAWbqqeM
author: Doug Turnbull (@softwaredoug)
date: 2026-05-27
lecture_transcript: transcripts/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents-lecture.md
tags:
  - agentic-search
  - agent-steering
  - harness-engineering
  - search
  - ai-agents
---

# 3. Cheat at Search — Steering Lost Agents
## Agentic Design Patterns for Search

**Source:** Google Slides presentation by SoftwareDoug LLC (65 slides)
**Context:** Part 3 of the Cheat at Search series. Part 1 covered NDCG/search evaluation. Part 2 covered LLM Query Understanding. This part covers agent steering patterns.
**Lecture transcript:** [[transcripts/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents-lecture|Cheat at Search — Steering Lost Agents (Lecture Transcript)]]

---

## 1. Goals

- The knobs humans control, and what agents control
- How we control the direction agents go
- Adding guardrails to the agentic process
- Delegating to subagents

Architecture: **Agentic Loop** → **Harness (another loop!)** → **Tools**

---

## 2. Agentic Loop and the Harness

- **Agentic Loop:** The core tool-calling loop (agent decides which tools to invoke).
- **Harness (Control Plane):** Evaluates the agent's response, can force a retry, stop the agent, or modify behavior.
- **Tools respond based on internal state**, e.g., returning an error:
  > "Error: you're calling me illegally because you need to do X first with foo"
- Agentic loop connects to agent_state; tools can inspect and respond to state.

---

## 3. Who Controls What?

### Agent Controls
- Which tools to call
- The order and frequency of tool calls
- The final output (subject to override)

### Human / Developer Controls
- **Task definition:** system prompt, tools provided, context
- **Tool responses:** what the tool returns, including error messages
- **User validation & feedback:** injecting messages like "This output is malformed, try again" or "Relevant results look like …"

---

## 4. Concrete Example: Agentic Search with Filesystem-like Tools

Instead of a classic search engine, the agent uses three custom tools that simulate a filesystem:

- `ls_wands` — list "files" (products) in a directory
- `grep_wands` — search for regex inside product descriptions
- `cat_wands` — read a specific "file" (product details)

Tool signatures:
```python
def ls_wands(path: str, glob: str, max_results: int = 50, agent_state=None) -> list[str] | str:
    """List files in a directory matching the glob, at most 50 results.
    WANDS filesystem layout: /<category>/<subcategory>/<product_name>-<doc_id>.txt
    File contents: <Product Name> (ID: <doc_id>) \n <description>"""

def grep_wands(pattern: str, glob: str, num_results: int = 50, agent_state=None) -> list[dict[str, str]] | str:
    """Search for a regex pattern in files matching the glob, at most 50 results."""
```

System prompt excerpt:
> "You take user search queries and use filesystem tools to find relevant products… It's important to return results ranked from most to least relevant… Gather results until you have 10 best matches you can find… Return the *DOC IDs*, not paths, in the response."

**Note:** This is NOT a true `bash` tool; bash would allow deeper exploration/code generation. These constrained tools work for a small catalog (~45K docs).

---

## 5. Guardrails & Validation

### Simple Loop ("Ralph loop")
Just tell the agent to try again up to 10 times:
```python
max_loops = 10
for _ in range(max_loops):
    resp = agent.loop(inputs=inputs, agent_state=agent_state, logger=logger)
    inputs.append({"role": "user", "content": "Try to find better results!"})
```

### Validation with a Rule
Force a retry if criteria not met (e.g., not enough results):
```python
def validate_min_results(resp, min_results=10):
    results = getattr(resp, "ranked_results", None) if resp else None
    count = len(results or [])
    if count >= min_results:
        return True
    return "Please return at least 10 results to give the user a good variety to choose from."
```

### LLM Judge Validation
A dedicated LLM judges the quality:
```python
msg = validate_llm_judge(query, resp)
if msg is not True:
    inputs.append({"role": "user", "content": msg})
    continue
```
The judge behaves like a user reacting:
- "These aren't relevant…"
- "Hmm let's try over here then"

### Why "User" Feedback Works
- Models are trained to serve users; user-like messages steer them effectively.
- Feedback can be automated (from a reranker, LLM judge, or learned model).
- Similar to a human reaction: "No! That's not what I want…"

---

## 6. Steering with a Judge / Reranker

Three options for incorporating a quality model:

1. **Reranker inside the search tool** — black-box, agent unaware.
2. **Reranker as a separate tool** — agent could call it, but enforcing the call is hard.
3. **Evaluate in response** — provide feedback as a user message; keeps agent on track without requiring a systematic tool call.

> "Don't trust it to call the tool systematically like code (let code do that!)"

**Types of quality models:** Reranker, LLM as Judge, Learning to Rank, CrossEncoder.

**Exhaustive search use case:** Can find hard negatives for training — agents guided around nooks and crannies using manual/automated feedback.

---

## 7. Priming: Starting in the Right Place

**Problem:** Starting from a poor initial state wastes tokens.

**Solution 1 — Few-shot examples in prompt:**
Add concrete examples of relevant/irrelevant products to the system prompt. Example format:
```
User Query: wood coffee table set by storage
Product Name: stuber 3 piece coffee table set
Product Description: sleek mid-century modern design...
Product Category: Furniture
Relevance: Partial
```

**Solution 2 — Query interpretation/expansion:**
```python
def interpret_query(keywords):
    system_prompt = """Interpret search queries for a home goods/furniture store
    like Wayfair into a description of what's needed in a few sentences.
    State it in the voice of the user "I am looking for <detailed info>"
    Pick the most likely intent, don't guess at multiple ones."""
```

**Solution 3 — Agentic skills / query plan:**
Vector DB stores "how to search for X" documents. Query is matched to relevant skill docs, which are injected into the prompt. Rules are managed by the dev team and PMs.

---

## 8. Tool Guards: The Stick 🏒

Tools can maintain state and reject redundant/inefficient calls:
- "You've already been here dope!" — prevents repeated searches of the same area
- Tools check agent_state before executing, return errors for invalid usage
- Tool error messages ARE prompt engineering — guide the agent with helpful messages

Example:
```python
def search_bm25(keywords, top_k=5, agent_state=None):
    if top_k > 100:
        raise ValueError("top_k must be <= 100")
    guard_error = guard_disallow_repeated_queries(
        {"tool_name": "search_bm25", "query": keywords}, agent_state)
    if isinstance(guard_error, str) and guard_error:
        return guard_error  # Return helpful message to guide agent
```

---

## 9. Subagents & Delegation

### Problem: Long-running agents lose track
- Context rots over many search iterations
- Agents forget mistakes made at search #10 by search #50
- Beginner mistake: many complex tools with many parameters → curse of dimensionality

### Solution: Orchestrator-Subagent pattern
```python
# Main agent delegates to subagents
Main agent:
    → Subagent: Search task A (fresh agent_run, tool calling loop)
    → Subagent: Search task B (fresh agent_run, tool calling loop)
```

Each subagent gets a fresh run with clean context. The orchestrator synthesizes results. Subagents can receive automated feedback.

### Different start positions
When there are multiple reasonable starting points for a search, delegate to separate subagents exploring different paths.

---

## 10. Beyond Search: BEAM Search for Systematic Exploration

**Problem:** Is "search" the right primitive for exhaustive exploration? Randomly moving around a graph is not systematic.

**Alternative:** BEAM search over the filesystem — visiting each location systematically, not revisiting. Navigate to categories/subcategories, search (grep) within them, and track which locations have been visited.

---

## 11. Results Progression (WANDS Dataset, NDCG)

| Variant | Mean NDCG |
|---------|-----------|
| BM25 (no agent) | 0.5408 |
| Agentic + FS Tools | 0.5565 |
| Agentic + FS Tools + Few Shot | 0.5652 |
| Agentic + FS Tools + Delegation | 0.5661 |

**Key insight:** Even without super complex tools, delegation provides a modest but meaningful improvement. The bigger wins come from few-shot priming (+0.0087 over FS Tools baseline).

---

## 12. Key Design Principles

1. **Agent picks the tools; you control how tools respond** — tool responses are prompt engineering
2. **Harness > Model** — the control loop matters more than the specific model
3. **User-feedback messages steer agents** — leverage training bias toward user satisfaction
4. **Tool guards prevent wasted exploration** — return errors for redundant/inefficient calls
5. **Prime with few-shot examples** — avoid wasting tokens on initial exploration
6. **Delegate long/complex tasks to subagents** — fresh context prevents context rot
7. **Simple tools > complex tools** — avoid the curse of dimensionality

---

**Colab notebook:** https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1
