# Braintrust Python SDK — Logging/Tracing API Reference

> Source: braintrust v0.14.0 PyPI package introspection + official docs at braintrust.dev

---

## 1. Data Model

```
Organization
 └── Project          (created implicitly by init_logger(project="..."))
      ├── Logs         (production traces — via Logger)
      └── Experiments  (eval runs — via init_experiment / Eval)

Within Logs or Experiments:
  Trace (= a tree of Spans sharing the same root_span_id)
   └── Span (root, type="task" by default)
        ├── Span (child, e.g. type="llm")
        ├── Span (child, e.g. type="tool")
        │    └── Span (grandchild)
        └── Span (child, e.g. type="score")
```

A **trace** is a DAG (usually a tree) of **spans**. Each span has:
- `id` — unique span identifier
- `span_id`, `root_span_id`, `span_parents` — tree structure (managed by SDK)
- `input`, `output`, `expected` — arbitrary JSON-serializable data
- `scores` — `dict[str, float]` (values between 0 and 1)
- `metadata` — `dict[str, Any]` (arbitrary key-value pairs)
- `metrics` — `dict[str, float]` (auto-populated: `start`, `end`; you can add `tokens`, `prompt_tokens`, `completion_tokens`)
- `error` — optional error string
- `tags` — `list[str]` (aggregated/unioned at trace level)
- `span_attributes` — `{"name": str, "type": str}` where type is one of: `"llm"`, `"score"`, `"function"`, `"eval"`, `"task"`, `"tool"`, `"automation"`, `"facet"`, `"preprocessor"`, `"review"`

---

## 2. Creating a Logger

```python
import braintrust

# Returns a Logger object. Creates the project if it doesn't exist.
logger = braintrust.init_logger(
    project="My Project",        # project name (creates if needed)
    # project_id="...",          # alternative: use project UUID
    async_flush=True,             # default: batch & send in background thread
    # api_key="...",             # or set BRAINTRUST_API_KEY env var
    # app_url="https://www.braintrust.dev",  # default
    # org_name="my-org",         # if you belong to multiple orgs
    # set_current=True,          # sets as global current logger
)
# Type: braintrust.Logger
```

Environment variable setup:
```bash
export BRAINTRUST_API_KEY="your-api-key"
```

---

## 3. Logging Traces with Hierarchical Spans

### 3a. Simple flat log (no spans)

```python
# Logger.log() creates a single span (no hierarchy). Returns the span id.
span_id = logger.log(
    input={"question": "What is 2+2?"},
    output={"answer": "4"},
    expected={"answer": "4"},
    scores={"accuracy": 1.0},
    metadata={"model": "gpt-4o", "user_id": "u123"},
    tags=["math", "simple"],
)
# NOTE: Once you call logger.start_span(), you can no longer call logger.log()
# unless you pass allow_concurrent_with_spans=True.
```

### 3b. Hierarchical spans with context managers (RECOMMENDED)

```python
import braintrust

logger = braintrust.init_logger(project="My Project")

# Root span — use context manager to auto-end and auto-set as current
with logger.start_span(name="handle_request", type="task") as root_span:
    root_span.log(input={"query": "How do I reset my password?"})

    # Child span — nested context manager
    with root_span.start_span(name="retrieve_docs", type="tool") as retrieval_span:
        retrieval_span.log(
            input={"query": "password reset"},
            output={"docs": ["doc1", "doc2"]},
            metadata={"num_results": 2},
        )

    # Another child span
    with root_span.start_span(name="generate_answer", type="llm") as llm_span:
        llm_span.log(
            input=[{"role": "user", "content": "How do I reset my password?"}],
            output={"role": "assistant", "content": "Go to Settings > Security..."},
            metrics={
                "prompt_tokens": 25,
                "completion_tokens": 40,
                "tokens": 65,
            },
            metadata={"model": "gpt-4o"},
        )

    root_span.log(
        output={"answer": "Go to Settings > Security..."},
        scores={"helpfulness": 0.9},
    )

# Produces trace tree:
# handle_request (task)
#   ├── retrieve_docs (tool)
#   └── generate_answer (llm)
```

### 3c. @traced decorator (auto-logs function input/output)

```python
import braintrust

logger = braintrust.init_logger(project="My Project")

@braintrust.traced
def fetch_context(query: str) -> list[str]:
    """Input args and return value are auto-logged to the span."""
    return ["doc1", "doc2"]

@braintrust.traced
def generate_response(query: str, context: list[str]) -> str:
    return "Based on the docs..."

@braintrust.traced
def handle_request(query: str) -> str:
    """Spans automatically nest: handle_request > fetch_context, generate_response"""
    context = fetch_context(query)
    response = generate_response(query, context)
    return response

# Call it — creates a 3-span trace automatically
result = handle_request("How do I reset my password?")
logger.flush()  # ensure all logs are sent
```

With decorator arguments:
```python
@braintrust.traced(name="Custom Name", type="tool", notrace_io=True)
def my_func(x):
    # notrace_io=True prevents auto-logging of input/output
    braintrust.current_span().log(output="custom output")
    return x
```

### 3d. Module-level start_span (alternative to @traced)

```python
import braintrust

logger = braintrust.init_logger(project="My Project")

# Uses the same precedence as @traced: current span > current experiment > current logger
with braintrust.start_span(name="my_operation") as span:
    span.log(input={"key": "value"})
    # ...
    span.log(output={"result": 42})
```

### 3e. Manual span management (no context manager)

```python
span = logger.start_span(name="my_span")
span.log(input={"x": 1})
# ... do work ...
span.log(output={"y": 2})
span.end()  # MUST call end() if not using context manager
```

---

## 4. Attaching Scores, Metadata, Tags

### On a span (via span.log)

```python
with logger.start_span(name="my_task") as span:
    span.log(
        scores={"accuracy": 0.95, "relevance": 0.8},  # values must be 0-1
        metadata={"model": "gpt-4o", "prompt_version": "v2", "user_id": "u123"},
        tags=["production", "customer-support"],
    )
```

**Multiple `span.log()` calls are merged** into one logical row. So you can log incrementally:

```python
with logger.start_span(name="pipeline") as span:
    span.log(input={"query": "hello"})
    # ... do work ...
    span.log(metadata={"step": "retrieval", "num_docs": 5})
    # ... do more work ...
    span.log(output={"answer": "world"}, scores={"quality": 0.9})
```

### At span creation time

```python
with logger.start_span(
    name="my_task",
    type="task",
    input={"query": "hello"},             # passed as **event kwargs
    metadata={"user_id": "u123"},
    tags=["production"],
) as span:
    span.log(output={"answer": "world"})
```

### Via set_attributes (name/type only)

```python
with logger.start_span() as span:
    span.set_attributes(
        name="renamed_span",
        type="llm",
        span_attributes={"name": "my_llm_call", "type": "llm"},
    )
```

### Feedback (after the fact, by span ID)

```python
# Logger.log_feedback — attach scores/comments to an existing span by ID
logger.log_feedback(
    id=span_id,                              # from logger.log() or span.id
    scores={"user_rating": 1.0},             # thumbs up
    expected={"answer": "correct answer"},   # ground truth
    comment="User confirmed this was helpful",
    metadata={"user_id": "u456"},            # audit metadata (not main event metadata)
    source="external",                       # "external" | "app" | "api"
)

# Span.log_feedback — same but on the span object directly (no id needed)
with logger.start_span(name="task") as span:
    span.log_feedback(
        scores={"thumbs_up": 1.0},
        comment="Looks good",
    )
```

### Update span after the fact

```python
# Update a span after it's been flushed
logger.update_span(
    id=span_id,
    output={"async_result": "computed later"},
    scores={"async_score": 0.75},
)
```

---

## 5. Distributed Tracing (cross-service)

```python
# ---- Service A ----
import braintrust
logger = braintrust.init_logger(project="My Project")

with logger.start_span(name="api_handler") as span:
    # Export an opaque string that encodes span identity
    exported = span.export()  # str — pass this to Service B
    # e.g., send as HTTP header: X-Braintrust-Parent: {exported}
    span.log(input={"request": "..."})

# ---- Service B ----
import braintrust
logger = braintrust.init_logger(project="My Project")

# Resume the trace by passing parent=exported
with logger.start_span(name="downstream_task", parent=exported) as child:
    child.log(input={"received": "..."})
    child.log(output={"processed": "..."})
```

The `export()` method returns an opaque string. Parse with `SpanComponentsV4.from_str()` if needed.

---

## 6. Fetching / Exporting Traces

### 6a. Via the SDK — Experiment.fetch()

Experiments (not Loggers) implement `ObjectFetcher` with a `.fetch()` method:

```python
import braintrust

experiment = braintrust.init_experiment("My Project", name="my-experiment")
# ... log spans ...

for record in experiment.fetch():
    print(record)  # dict with id, input, output, scores, metadata, etc.
```

### 6b. Via REST API — BTQL queries (primary method for production logs)

The `/btql` endpoint accepts SQL-like queries. This is **the main way to fetch project logs**:

```python
import requests, os

API_URL = "https://api.braintrust.dev"
headers = {"Authorization": f"Bearer {os.environ['BRAINTRUST_API_KEY']}"}

# Fetch traces (root spans) from project logs
query = """
  SELECT id, input, output, scores, metadata, span_attributes, metrics
  FROM project_logs('YOUR_PROJECT_ID', shape => 'traces')
  WHERE scores.accuracy > 0.8
  LIMIT 100
"""

response = requests.post(
    f"{API_URL}/btql",
    headers=headers,
    json={"query": query, "fmt": "json"},
)
data = response.json()
for row in data["data"]:
    print(row)
```

Fetch ALL spans (not just roots):
```python
query = """
  SELECT *
  FROM project_logs('YOUR_PROJECT_ID')
  LIMIT 1000
"""
```

Export to Parquet:
```python
response = requests.post(
    f"{API_URL}/btql",
    headers=headers,
    json={
        "query": "SELECT * FROM project_logs('PROJECT_ID')",
        "fmt": "parquet",
    },
)
with open("export.parquet", "wb") as f:
    f.write(response.content)
```

Fetch child spans by trace metadata:
```python
query = f"""
  SELECT span_attributes, metrics, input, output
  FROM project_logs('{PROJECT_ID}', shape => 'traces')
  WHERE metadata.user_id = 'u123'
  LIMIT 10
"""
```

Fetch experiment results:
```python
query = f"""
  SELECT id, input, output, scores, expected
  FROM experiment('{EXPERIMENT_ID}')
"""
```

### 6c. REST API — CRUD endpoints

```python
# List experiments with metadata filter
response = requests.get(
    f"{API_URL}/v1/experiment",
    headers=headers,
    params={
        "project_id": "YOUR_PROJECT_ID",
        "metadata": json.dumps({"env": "production"}),
    },
)
experiments = response.json().get("objects", [])
```

---

## 7. Span.link() and Span.permalink()

```python
with logger.start_span(name="my_task") as span:
    # Non-blocking link (preferred for production)
    url = span.link()       # e.g. "https://www.braintrust.dev/app/my-org/p/My%20Project/logs/..."

    # Blocking permalink (may resolve data with server)
    url = span.permalink()  # same format, but blocks until resolved

    span.log(metadata={"braintrust_link": url})
```

---

## 8. OpenTelemetry

Braintrust **receives** OTel spans for Go, C#, Ruby, and Java (languages without native SDK decorators) — you use standard OTel `setAttribute` calls and Braintrust maps them:
- Custom attributes → `metadata` field
- `braintrust.tags` attribute → `tags` field

There is a JS integration (`@braintrust/otel`) for OpenTelemetry export.

**There is NO documented OTel-compatible _export_ format** — i.e., you cannot export Braintrust traces as OTel spans. The export path is BTQL → JSON/Parquet.

---

## 9. Key Helper Functions

```python
import braintrust

# Get currently-active span (from context var — set by context managers / @traced)
span = braintrust.current_span()  # returns NoopSpan if nothing active

# Get currently-active logger
logger = braintrust.current_logger()

# Flush all pending logs across all loggers
braintrust.flush()

# Wrap OpenAI client for auto-tracing
import openai
client = braintrust.wrap_openai(openai.OpenAI())
# Also: wrap_anthropic(), wrap_litellm()
```

---

## 10. SpanTypeAttribute Enum Values

```python
from braintrust import SpanTypeAttribute

SpanTypeAttribute.LLM          # "llm"
SpanTypeAttribute.SCORE        # "score"
SpanTypeAttribute.FUNCTION     # "function"
SpanTypeAttribute.EVAL         # "eval"
SpanTypeAttribute.TASK         # "task" (default for root spans)
SpanTypeAttribute.TOOL         # "tool"
SpanTypeAttribute.AUTOMATION   # "automation"
```

You can also just pass the string: `type="llm"`.

---

## 11. ThreadPoolExecutor Support

```python
import braintrust

# Standard ThreadPoolExecutor loses context vars. Use this instead:
with braintrust.TracedThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(my_traced_function, arg1, arg2)
    result = future.result()
```

---

## 12. Serverless / Sync Flush

```python
# In serverless environments (Lambda, Cloud Functions), disable async flush:
logger = braintrust.init_logger(project="My Project", async_flush=False)
# This ensures logs are sent synchronously before the function exits.
```

---

## 13. Complete End-to-End Example

```python
import braintrust
import openai
import os

# Initialize
logger = braintrust.init_logger(project="Customer Support Bot")
client = braintrust.wrap_openai(openai.OpenAI())  # auto-traces LLM calls

@braintrust.traced
def retrieve_docs(query: str) -> list[dict]:
    """Auto-logged: input=(query,), output=return value"""
    # ... vector search ...
    return [{"id": "doc1", "text": "Reset password at Settings > Security"}]

@braintrust.traced
def answer_question(query: str) -> dict:
    docs = retrieve_docs(query)

    # LLM call is auto-traced by wrap_openai
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"Context: {docs}"},
            {"role": "user", "content": query},
        ],
    )
    answer = response.choices[0].message.content

    # Add metadata to current span
    braintrust.current_span().log(
        metadata={"num_docs": len(docs), "model": "gpt-4o"},
        tags=["customer-support"],
        scores={"has_sources": 1.0 if docs else 0.0},
    )
    return {"answer": answer, "sources": docs}

# Run — produces trace:
# answer_question (task)
#   ├── retrieve_docs (task)
#   └── OpenAI Chat Completion (llm)  ← auto-created by wrap_openai
result = answer_question("How do I reset my password?")

# Later: attach user feedback
logger.log_feedback(
    id=braintrust.current_span().id,  # or save the id from earlier
    scores={"thumbs_up": 1.0},
    comment="This solved my problem!",
)

logger.flush()
```
