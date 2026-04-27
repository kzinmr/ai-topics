# Arize Phoenix — Trace Ingestion Research Summary

Researched from https://docs.arize.com/phoenix (v14.x, June 2025)

---

## 1. How Phoenix Ingests Traces (OTLP)

Phoenix is built **entirely on OpenTelemetry**. It accepts traces via the standard **OTLP protocol** — there is no proprietary ingestion format.

### Server Endpoints

When you run `phoenix serve` (or Docker, etc.):

| Endpoint | URL | Purpose |
|----------|-----|--------|
| UI | `http://localhost:6006` | Web dashboard |
| OTLP HTTP | `http://localhost:6006/v1/traces` | HTTP/protobuf trace ingestion |
| OTLP gRPC | `http://localhost:4317` | gRPC trace ingestion |

### Setup with `phoenix.otel` (the recommended wrapper)

Phoenix provides `arize-phoenix-otel`, a thin wrapper around the standard OpenTelemetry SDK that configures sensible defaults:

```python
pip install arize-phoenix-otel
```

```python
from phoenix.otel import register

# Reads PHOENIX_COLLECTOR_ENDPOINT env var (default: http://localhost:6006)
# Returns a standard OpenTelemetry TracerProvider
tracer_provider = register(
    project_name="my-llm-app",  # maps to Phoenix "project"
    auto_instrument=True,        # auto-discovers installed OpenInference instrumentors
)
tracer = tracer_provider.get_tracer(__name__)
```

Environment variables:
```bash
export PHOENIX_COLLECTOR_ENDPOINT="http://localhost:6006"  # self-hosted
# export PHOENIX_COLLECTOR_ENDPOINT="https://app.phoenix.arize.com/s/your-space"  # cloud
# export PHOENIX_API_KEY="your-api-key"  # only for cloud/authenticated instances
```

### Or use raw OpenTelemetry (no Phoenix SDK dependency)

Since Phoenix just speaks OTLP, you can use the standard OTel SDK directly:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

resource = Resource(attributes={"service.name": "my-project"})
provider = TracerProvider(resource=resource)
provider.add_span_processor(
    SimpleSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:6006/v1/traces"))
)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

**Key insight**: The `service.name` resource attribute becomes the **project name** in the Phoenix UI.

---

## 2. Manual Instrumentation (Tracing Helpers)

Phoenix provides decorator and context-manager helpers via the `openinference-instrumentation` package. These are the primary way to do manual instrumentation.

### Decorators (`@tracer.chain`, `@tracer.tool`, `@tracer.llm`, `@tracer.agent`)

```python
from phoenix.otel import register

tracer_provider = register(project_name="my-agent")
tracer = tracer_provider.get_tracer(__name__)

@tracer.chain
def my_workflow(input: str) -> str:
    """Input/output are auto-captured from function args and return value."""
    result = call_llm(input)
    return result

@tracer.tool
def get_weather(city: str) -> str:
    """tool-description (docstring becomes tool description)"""
    return "sunny"

@tracer.agent
def my_agent(input: str) -> str:
    return run_agent_loop(input)

@tracer.llm
def invoke_llm(messages: list) -> str:
    response = openai_client.chat.completions.create(
        model="gpt-4o", messages=messages
    )
    return response.choices[0].message.content or ""
```

### Context Managers (for partial-function tracing)

```python
from opentelemetry.trace import Status, StatusCode

# Chain span
with tracer.start_as_current_span(
    "my-workflow",
    openinference_span_kind="chain",  # <-- key param
) as span:
    span.set_input("user question")
    result = do_work()
    span.set_output(result)
    span.set_status(Status(StatusCode.OK))

# Tool span
with tracer.start_as_current_span(
    "tool-span",
    openinference_span_kind="tool",
) as span:
    span.set_input("input")
    span.set_output("output")
    span.set_tool(
        name="get_weather",
        description="finds the weather for a given city",
        parameters={"city": "London"},
    )
    span.set_status(Status(StatusCode.OK))

# LLM span
with tracer.start_as_current_span(
    "llm_span",
    openinference_span_kind="llm",
) as span:
    span.set_input(messages)
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4", messages=messages
        )
    except Exception as error:
        span.record_exception(error)
        span.set_status(Status(StatusCode.ERROR))
    else:
        span.set_output(response)
        span.set_status(Status(StatusCode.OK))
```

### Rich LLM Span Attributes (messages, tokens, tool calls)

For LLM spans that need full message/token detail in the UI, use the helper functions from `openinference.instrumentation`:

```python
import openinference.instrumentation as oi
from openinference.instrumentation import (
    get_input_attributes,
    get_llm_attributes,
    get_output_attributes,
)

# Build rich attributes for an LLM span
attrs = {
    **get_input_attributes({"messages": messages, "model": "gpt-4"}),
    **get_llm_attributes(
        provider="openai",
        system="openai",
        model_name="gpt-4",
        input_messages=[
            oi.Message(role="user", content="Hello")
        ],
        invocation_parameters={"temperature": 0.7},
        tools=[oi.Tool(json_schema={...})],
    ),
}

with tracer.start_as_current_span(
    "llm_call",
    attributes=attrs,
    openinference_span_kind="llm",
) as span:
    response = openai_client.chat.completions.create(...)
    span.set_attributes({
        **get_llm_attributes(
            output_messages=[oi.Message(role="assistant", content=response_text)],
            token_count=oi.TokenCount(prompt=50, completion=100),
        ),
        **get_output_attributes(response),
    })
```

### Context Attributes (session_id, metadata, etc.)

```python
from openinference.instrumentation import using_attributes

with using_attributes(session_id="session-123", user_id="user-456"):
    # All spans created within this block get session_id and user_id
    my_workflow("hello")
```

---

## 3. OpenInference Semantic Conventions (the data model for LLM spans)

OpenInference defines the **span attribute schema** that Phoenix understands. These are set as OpenTelemetry span attributes.

### Span Kinds (required: `openinference.span.kind`)

| Span Kind | Description |
|-----------|-------------|
| `CHAIN` | A workflow step or glue code between components |
| `LLM` | A call to a Large Language Model |
| `TOOL` | A call to an external tool/function |
| `AGENT` | An agent that orchestrates LLM + tool calls |
| `RETRIEVER` | A data retrieval step (e.g., vector search) |
| `RERANKER` | Reranking of retrieved documents |
| `EMBEDDING` | An embedding generation call |
| `GUARDRAIL` | Content safety/moderation check |
| `EVALUATOR` | An evaluation of LLM outputs |

### Key Span Attributes

| Attribute | Semantic Meaning |
|-----------|------------------|
| `input.value` | The input to the span (string or JSON) |
| `output.value` | The output of the span |
| `input.mime_type` / `output.mime_type` | `"text/plain"` or `"application/json"` |
| `llm.model_name` | Model identifier (e.g., `gpt-4o`) |
| `llm.provider` | Provider name (e.g., `openai`) |
| `llm.input_messages` | JSON array of input messages |
| `llm.output_messages` | JSON array of output messages |
| `llm.token_count.prompt` | Prompt token count |
| `llm.token_count.completion` | Completion token count |
| `llm.token_count.total` | Total token count |
| `llm.invocation_parameters` | JSON of model params (temperature, etc.) |
| `llm.tools` | Tool definitions available to the LLM |
| `tool.name` | Name of the tool |
| `tool.description` | Description of the tool |
| `tool.parameters` | JSON of tool input parameters |
| `session.id` | Session identifier |
| `user.id` | User identifier |
| `metadata` | Arbitrary JSON metadata dict |
| `tag.tags` | Array of string tags |
| `retrieval.documents` | Array of retrieved documents |

---

## 4. Import & Export Capabilities

### Importing Traces

Phoenix can import traces from **pandas DataFrames** that contain OpenInference-formatted span data:

```python
import phoenix as px

# Import from a DataFrame
px.launch_app(trace=px.TraceDataset(df))

# Import from a previously-saved file
px.launch_app(
    trace=px.TraceDataset.load(
        'f7733fda-6ad6-4427-a803-55ad2182b662',
        directory="/my_saved_traces/"
    )
)
```

**Note**: There is NO direct JSONL file import endpoint. The import path is: your data → pandas DataFrame → `px.TraceDataset(df)` → `px.launch_app(trace=...)`. Alternatively, you can **replay spans via OTLP** (construct OTel spans programmatically and send them to the OTLP endpoint).

### Exporting / Querying Traces (Python Client + DSL)

Phoenix has a **Python client** with a powerful query DSL:

```python
from phoenix.client import Client
from phoenix.trace.dsl import SpanQuery

client = Client()  # reads PHOENIX_COLLECTOR_ENDPOINT env var

# --- Download ALL spans as a DataFrame ---
df = client.spans.get_spans_dataframe()
df = client.spans.get_spans_dataframe(project_name="my-project")

# --- Query with filters ---
query = SpanQuery().where(
    "span_kind == 'LLM'",
).select(
    input="input.value",
    output="output.value",
)
df = client.spans.get_spans_dataframe(query=query)

# --- Filter by time range ---
from datetime import datetime, timedelta
df = client.spans.get_spans_dataframe(
    start_time=datetime.now() - timedelta(days=7),
    end_time=datetime.now(),
)

# --- Filter for FAILED spans (errors) ---
query = SpanQuery().where(
    "status == 'ERROR'",
).select(
    input="input.value",
    output="output.value",
)
failed_df = client.spans.get_spans_dataframe(query=query, project_name="my-agent")

# --- Filter by evaluation results ---
query = SpanQuery().where(
    "evals['correctness'].label == 'incorrect'"
)

# --- Filter by metadata ---
query = SpanQuery().where(
    'metadata["topic"] == \'programming\''
)

# --- Filter for substring in attribute ---
query = SpanQuery().where(
    "'error' in output.value"
)

# --- Explode retrieval documents ---
query = SpanQuery().where(
    "span_kind == 'RETRIEVER'",
).select(
    input="input.value",
).explode(
    "retrieval.documents",
    reference="document.content",
    score="document.score",
)

# --- Join child spans to parents ---
query_parent = SpanQuery().where("parent_id is None").select(
    input="input.value", output="output.value"
)
query_child = SpanQuery().where("span_kind == 'RETRIEVER'").select(
    span_id="parent_id"  # re-index by parent
).concat("retrieval.documents", reference="document.content")

import pandas as pd
parent_df = client.spans.get_spans_dataframe(query=query_parent)
child_df = client.spans.get_spans_dataframe(query=query_child)
result = pd.concat([parent_df, child_df], axis=1, join="inner")
```

The query DSL filter strings are **Python boolean expressions** that work both in code and in the Phoenix UI search bar.

---

## 5. Data Model (Project → Trace → Span hierarchy)

```
Project ("my-llm-app")
  └── Trace (single end-to-end request, identified by trace_id)
        ├── Span: root (kind=CHAIN or AGENT, parent_id=None)
        │     ├── Span: LLM call (kind=LLM)
        │     ├── Span: tool call (kind=TOOL)
        │     └── Span: LLM call (kind=LLM)
        └── ... more traces
```

- **Project**: Top-level grouping. Set via `project_name` in `register()` or the `service.name` OTel resource attribute.
- **Session**: Optional grouping across traces via `session.id` attribute (e.g., a multi-turn conversation).
- **Trace**: A tree of spans sharing the same `trace_id`. Represents one end-to-end operation.
- **Span**: A single unit of work. Has a `span_id`, optional `parent_id`, `span_kind`, attributes, status, start/end time.

---

## 6. Self-Hosting Summary

```bash
# Install and run
pip install arize-phoenix
phoenix serve
# → UI at http://localhost:6006
# → OTLP HTTP at http://localhost:6006/v1/traces
# → OTLP gRPC at localhost:4317

# Or Docker
docker run -p 6006:6006 -p 4317:4317 arizephoenix/phoenix:latest
```

- 100% free, no feature gates
- SQLite by default, supports PostgreSQL / Aurora for production
- Supports OAuth2, LDAP, RBAC, data retention policies
- Can be fully air-gapped

---

## 7. Practical Recipe: Building Your System

For your use case (collect agent traces externally, import into Phoenix, query failures):

### Option A: Send traces directly via OTLP (recommended)

```python
# In your agent code
from phoenix.otel import register
from opentelemetry.trace import Status, StatusCode

tracer_provider = register(
    project_name="my-agent",
    # endpoint read from PHOENIX_COLLECTOR_ENDPOINT env var
)
tracer = tracer_provider.get_tracer(__name__)

@tracer.agent
def run_agent(user_input: str) -> str:
    llm_result = call_llm(user_input)
    tool_result = call_tool(llm_result)
    return synthesize(tool_result)

@tracer.llm
def call_llm(prompt: str) -> str:
    # your LLM call here
    return response

@tracer.tool
def call_tool(query: str) -> str:
    # your tool call here
    return result
```

### Option B: Replay external data as OTLP spans (batch import from JSONL)

```python
import json
from phoenix.otel import register
from opentelemetry.trace import Status, StatusCode

tracer_provider = register(project_name="imported-traces")
tracer = tracer_provider.get_tracer("importer")

# Read your JSONL file and replay as OTel spans
with open("traces.jsonl") as f:
    for line in f:
        record = json.loads(line)
        with tracer.start_as_current_span(
            record["name"],
            openinference_span_kind=record.get("kind", "chain"),
        ) as span:
            span.set_input(record.get("input", ""))
            span.set_output(record.get("output", ""))
            if record.get("error"):
                span.set_status(Status(StatusCode.ERROR, record["error"]))
            else:
                span.set_status(Status(StatusCode.OK))

tracer_provider.shutdown()  # flush all spans
```

### Query failed traces and export

```python
from phoenix.client import Client
from phoenix.trace.dsl import SpanQuery

client = Client()

# Get all failed spans
failed = client.spans.get_spans_dataframe(
    query=SpanQuery().where("status == 'ERROR'").select(
        input="input.value",
        output="output.value",
    ),
    project_name="my-agent",
)

# Export to CSV/JSON
failed.to_csv("failed_traces.csv")
failed.to_json("failed_traces.json", orient="records", lines=True)
```
