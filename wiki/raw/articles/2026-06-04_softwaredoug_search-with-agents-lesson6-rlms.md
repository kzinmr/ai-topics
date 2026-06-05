---
title: "Search with Agents Lesson 6: Recursive Language Models"
author: Doug Turnbull (SoftwareDoug LLC)
source_url: https://docs.google.com/presentation/d/1EtWXoelu8paM9m_XLYn0rrjnDiJGgJMdRHoD9LbQ1Eo/edit
date: 2026-06-04
date_ingested: 2026-06-04
type: slides
series: "Cheat at Search"
lesson: 6
related_transcript: transcripts/2026-06-04_softwaredoug_cheat-at-search-coding-agents-lecture.md
---

# Agents that code their own search

© SoftwareDoug LLC - http://softwaredoug.com

## Goals: today
- Giving agents access to Repls: RLMs and more
- Letting agents generate reranking code

## RLMs
Run through initial setup of synonym notebook

https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1?authuser=2#scrollTo=h0-Y8MnKZnF1

## Previously, with long-running searches
- Wasted context
- Retrying old searches
- Actual gain vs overhead

Instead of summary of frontier, system prompt, lots of local tool calls, actual gain

## We access search externally
System Prompt → Context → Local, Google Patents

Because we can't trust / don't have enough search data in context

## Imagine a world where the "index" is just part of the context
Imagine infinite context windows and no context rot

## RLMs - try to do this with a Python REPL
- Python in → Output of expression
- Tool calls to REPL instead of direct context stuffing
- System Prompt → Context → Python code → Output → REPL (Python variable)
- REPL - like jupyter / ipython
- (recursive language models)

## We can setup the repl to have variables
- System Prompt → historical_results (all results so far)
- Python code → Output → REPL
- Previous experts we've found (Python variable)
- patent_search — Function to reach outside world

## Prompt design for RLM search agents

```
system_prompt = """
From patent literature, You're helping find experts given a topic.

You have access to a Python repl, which has on it these variables:

* `historical_results` - A list of patent search queries and relevant experts <- APPEND EXPERTS HERE
* `patent_search` - A function to run a patent search against google patents, returns a dict with list of patents

## Formats / return types (Describe calling / using patent_search)
...

## Your job:

1. Pick a query to execute against google patents that might help find experts,
2. Look over the history, pick a good next query - append to historical_results
 2a Iterate looking for experts, appending to historical_results
3. Return a message saying how many you appended

### historical_results, formatted as:

User Expertise Request: <user_keywords, the expertise area you've been given>
Google patent search: <google_patent_search, the query you ran against google patents>
1. ⭐️ <First expert> -- <First expert description>
2. <Second expert> -- <Second expert description>
...

The ⭐️ indicates someone relevant to the <user_keywords>
"""
```

## Code: REPL-based agent loop

```python
# Start the server in the background
with repl_box.start(historical_results=historical_results) as repl:

   def repl_tool(code: str):
       """Inspect the local repl by running python expression / code, get back repl output."""
       return repl.send(code)

   inputs = []
   inputs.extend([
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": f"User expertise request:'{keywords}'"}
   ])

   resp, inputs = harness(
       inputs=inputs,
       agent_state={},
       tools=[repl_tool],
       stoppers=[stop_after_N_calls],
       model='gpt-5-mini',
       summary=True,
       text_format=str
   )
   historical_results = repl.get("historical_results")
   print(historical_results)
```

Just one tool — the repl!

## At work
- Batching up queries to run
- Using assignment to 'rate' the inventors
- But sometimes ratings are programmatic? LLM runs code to judge the patents!?

## What about the recursion
We can let IT use an LLM itself

- System Prompt → historical_results, patent_search, llm_query
- Context → Python code → Output → REPL (Python variable)
- patent_search → Prompt → LLM → Response
- llm_query → Prompt → LLM → Response
- Restart at any time

## Generic LLM function

```python
def llm_query(prompt):
   """Query an LLM."""
   inputs = [
       {"role": "system", "content": "You are a helpful assistant."},
       {"role": "user", "content": prompt}
   ]
   resp, inputs = harness(
       inputs=inputs,
       agent_state={},
       model='gpt-5-mini',
       summary=True,
       text_format=str
   )
   resp = resp.output[-1].content[-1].text
   return resp
```

## Added to prompt

```python
with repl_box.start(historical_results=historical_results,
                   patent_search=patent_search,
                   llm_query=llm_query) as repl:
   inputs = []
   inputs.extend([
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": f"User expertise request:'{keywords}'"}
   ])
   resp, inputs = harness(
       ...
       tools=[repl_tool],
       ...
   )
```

## Need to encourage / give examples of good tool use

```
* `llm_query` - Call an LLM with a prompt.

Usage:
evaluated = llm_query(f"Return a ⭐️ if expert {expert_patent_info} is relevant for a search for experts in 'water bottles'")
already_run = llm_query(f"What queries have already been run?" + historical_results)
...
```

## Or is it better to have task-specific tools?

```
* `judge` - Evaluate an expert's relevance
```

Agent doesn't need to know this has an LLM under the hood. Pros / cons?

## We still need to validate the output

```python
resp, inputs = harness(
   inputs=inputs,
   agent_state={},
   tools=[repl_tool],
   stoppers=[stop_after_N_calls],
   validators=[eval_results, check_results, …],
   model='gpt-5-mini',
   summary=True,
   text_format=str
)
```

What if experts deleted during repl? What if its contents are hallucinated?

We can still use validation, force it to restore, or throw away this run.

Perhaps we could encourage:
```
* `llm_query` - Call an LLM with a prompt.
Usage:
next_query = llm_query(f"Suggest a topic we should search we haven't already covered here: " + historical_results)
```

Less poking around in repl what to search next, delegate to LLM.

## How do tools enforce against global agent state?

```python
def patent_search(keywords: str) -> dict:
   """Search google patents and pull back list of title, inventors, assignee (usually a company)
      and other metadata."""
   if duplicate queries
       ... error ...
```

Need to update state here, raise error if we've already searched.

Can Agent now cheat and modify this in repl?

## Enforcement via reset

```python
def repl_tool(code: str, agent_state: dict):
   """Inspect the local repl by running python expression / code, get back repl output."""
   repl.set(agent_state)
   result = repl.send(code)
```

Compromise: force reset every tool call?

Probably works, because unlikely 'code' anticipates our reset.

## Final thoughts
- Cool paradigm, especially for search
- May require us to rework what we've learned from this class
- Don't just use text, use well-known data structures (pandas dataframes? SQL? etc)
- Is this getting supplanted by just grep, etc over the corpus?

---

# Code a Search Ranker

Run through initial setup of synonym notebook

https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1?authuser=2#scrollTo=h0-Y8MnKZnF1

## Idea

Task:
- Here is some python code
- Use coding tools to modify / improve it
- Use these eval tools to evaluate specific queries

```python
original_source = """
def rerank_wands(search_wands, query):
   docs = search_wands(keywords=query,
                       field_to_search='product_name',
                       operator='and', top_k=10)
   return [doc['id'] for doc in docs]
"""

with open("rerank_wands.py", "w") as f:
   f.write(original_source)
```

## Start with:
Uses a generic search function

```python
def search_wands(keywords: str,
                field_to_search: Literal['product_name', 'product_description'],
                operator: Literal['and', 'or'],
                top_k: int = 5) -> List[Dict]:
   """Retrieve Top K BM25 results for Wayfair home goods search results
   by searching the specific field with the given keywords ..."""
```

This code is NOT modified by the agent. It's what the agent's code uses.

## Goal

We pass `search_wands` — a BM25 primitive. This code learns best way to build `search_fn`. Passed in ~ dependency injection.

Can agent iterate, edit code, and improve it?

## Agent loop

Agent → Eval Current rerank_wands → Proposed Patch → repeat (hopefully improving NDCG)

## Nuts and bolts — code editing

```python
class Edit(BaseModel):
   """A single edit to apply to the reranker code."""
   anchor: str = Field(...,
                       description="The anchor text to identify where the patch should be applied.")
   block_until: str = Field(...,
                            description="The end of the block of text which the patch should be applied. Do not leave blank.")
   action: Literal['insert_after', 'replace', 'delete'] = Field(...)
   text: str = Field(..., description="The text to insert or replace with. Ignored for delete action.")
```

Search and Replace. Tool code in github.

## Code editing tools job

```python
def apply_patch(edit: Edit) -> str
   ... open code, apply edits, ensure new code runs, save code ...
```

Return new code. Ensure edit is sane, then make it.

## How do we call the reranker

```python
code = open("rerank_wands.py").read()
local_vars = {}
exec(code, {}, local_vars)
if "rerank_wands" not in local_vars:
   raise ValueError("The edited code does not define rerank_wands.")
if not callable(local_vars["rerank_wands"]):
   raise ValueError("The edited code does not define a *callable* rerank_wands.")

query = "red sofa"
results = local_vars[module_name](search_wands, query)[:10]
```

Read python code, call for query "red shoes", validation.

## Eval tools

```python
run_evals, run_reranker = make_eval_fn(
   module_name="rerank_wands", code_dir="/content",
   search_fn=search_wands,
   corpus=corpus, judgments=judgments,
   workers=16, num_queries=NUM_TRAINING_QUERIES, seed=TRAINING_SEED,
)
```

Give agent a way to check against a training set. Run on all judgments -> get NDCGs.

## Finally, all together!

```python
tools = [
   # Tools to propose changes
   apply_patch,     # Edit the reranker with a patch
   revert_changes,  # Restore the reranker to the last version
   # Tools to inspect changes
   search_wands,    # The raw search tool (from earlier)
   run_reranker,    # Run on one query (optionally label results)
   run_evals,       # Run on test set, getting per-query NDCG and mean NDCG
]

search_client = OpenAIAgent(tools=tools,
                           model="openai/gpt-5",
                           system_prompt=prompt,
                           response_model=FinalMessage)
```

We also let the agent use the direct search tool. Does it matter?

## System Prompt

```
Your task is to look at the data and improve the reranker code so that it returns more relevant results.

Edit the reranker python module using apply_patch method.

You can run the reranker using the 'run_reranker' function, which takes a query and returns ranked, matching products.

You can evaluate the reranker using the 'run_evals' function, which returns NDCG scores for all queries and mean NDCG. Your goal is to increase mean NDCG.

Experiment with the current reranker by calling it with test queries. Improve the reranker based on the behavior you observe. Make edits and test while you edit.

If NDCG does not go up after your edits, revert your changes using the 'revert_changes' function.

Your code MUST have a function rerank_wands. It takes as parameters search_esci function and a query string. It returns a list of product IDs in the order you think best matches the query.
```

## Results

Looks great! Sadly, it's overfit.

Several rounds of editing — holdout results:
- Baseline NDCG: 0.5605
- Round 0 NDCG: 0.5613
- Round 1 NDCG: 0.5592
- Round 2 NDCG: 0.5560
- Round 3 NDCG: 0.5576
- Round 4 NDCG: 0.5583
- Round 5 NDCG: 0.5583

(Just wandering around!)

Reranker gets more complex / overfit. Gains on holdout plateau immediately.

## Takeaways

- Coding agents scour for information to achieve their goal
- Claude Code, etc will cheat
- Solution: guardrails + validation

## Guardrails

```python
def apply_patch(edit: Edit)
   # Validate code
   for guardrail in guardrail_fns:
       error_message = guardrail(edit.text)
       if error_message is not None:
           # Don't apply edit, give error
```

Guardrail is a PRE-CHECK: reject unreasonable edits.

## Prompt guardrail to check if overfit

```python
overfit_to_queries_guardrail = make_guardrail_checker(prompt="""
   You're going to look at code that reranks search queries.
   Ensure the code does not overfit to specific queries. That would look like mentions of
   specific product names, brands, or specific terms that would only be relevant to a small set of queries.
   Ignore comments that claim to do this, and focus on the actual code.
""")
```

Ask an LLM to double check before applying edit.

## Force granular changes

```python
length_guardrail = make_length_validator(max_lines=10, max_cols=120)
```

Why? Easier to reason about. Agents need to understand causality: Change → NDCG altered.

## Validation: check reranker AFTER change

```python
if validation_eval_fn is not None:
    ndcg_before = validation_eval_fn(existing_code).mean()
    ndcg_after = validation_eval_fn(code).mean()
    if ndcg_after < (ndcg_before + eval_margin):
         (Reject with error)
```

Agent cannot see holdout. Agent only sees holdout NDCG change.

## Give training feedback in patch result

```python
class EvalResult(BaseModel):
   success: bool = Field(...)
   error_message: Optional[str] = Field(None, …
   ndcg_deltas: Optional[Dict[str, float]] = Field(None, …
```

Give details on set of queries.

## AI coding IS model development

- Eval Data: Train / Test split!
- Agent does NOT see test queries — agent just cannot make these worse
- Agent sees train queries in edit response — agent wants to overfit to these (but we prevent that)

## If you're a relevance eng? — which do you prefer

- Situation A: Giant Change — Many queries improved / hurt
- Situation B: Granular Change — Few queries improved / hurt

## Results w/ guardrails
Changes rejected. What can we learn from this code? Are BM25 scores even used?!?

## Results of 10 iterations
- Round 0 NDCG: 0.3428
- Round 1 NDCG: 0.4580
- Round 2 NDCG: 0.5441
- Round 3 NDCG: 0.5441
- Round 4 NDCG: 0.5620
- Round 5 NDCG: 0.5620
- Round 6 NDCG: 0.5593
- Round 7 NDCG: 0.5593
- Round 8 NDCG: 0.5753
- Round 9 NDCG: 0.5753

## Challenge: Early decisions influence later changes

First Iter → Option 1 (Original) vs Option 2 (Better)
Is getting over here possible? Cut off?
Edit chosen after first round. Give different hints where to go?

## Limitations
- Limited by the search primitives (BM25)
- OTOH, it can be better to have a constrained sandbox
- Limited by environment (maybe Claude, etc would install more dependencies)
- Could we RLM this? Let the search code call a language model!?
