# Hermes Agent LLM o11y 連携戦略 v2
## Braintrust 主系 + Arize Phoenix 待機系 並列アーキテクチャ

---

## 1. 要件整理

1. **普段は Braintrust** でトレース管理・失敗分析・スコアリング
2. **Arize Phoenix (OSS)** にいつでも切り替え可能な状態を維持
3. **中間フォーマット** を持ち、Braintrust→Phoenix の互換インポートが効く
4. 失敗トレースの管理 → Skill 修正 / GRPO 改善ループへの接続

---

## 2. アーキテクチャ: Canonical Trace Format (CTF) パターン

### 核心思想

Braintrust と Phoenix に **直接結合しない**。
間に **Canonical Trace Format (CTF)** という自前の中間表現を挟む。

```
Hermes Agent
  │
  │ Plugin Hooks (pre/post_api_request, pre/post_tool_call, etc.)
  │
  ▼
┌──────────────────────────────────────────────────────────┐
│  hermes-o11y plugin (collector layer)                    │
│                                                          │
│  1. Hook データ → CTF (Canonical Trace Format) に正規化  │
│  2. CTF → ローカル JSONL にも常時追記 (耐障害性)          │
│  3. CTF → 設定された backend(s) へ非同期 flush            │
└──────┬───────────────────┬───────────────────┬───────────┘
       │                   │                   │
       ▼                   ▼                   ▼
  ┌──────────┐     ┌──────────────┐    ┌──────────────┐
  │ JSONL    │     │ Braintrust   │    │ Phoenix      │
  │ (always) │     │ (primary)    │    │ (standby or  │
  │          │     │              │    │  parallel)   │
  └──────────┘     └──────────────┘    └──────────────┘
       │                   │                   ▲
       │                   │                   │
       │              BTQL export               │
       │                   │    ┌───────────┐   │
       └───────────────────┴──▶│ CTF→OTLP  │───┘
                               │ replayer  │
                               └───────────┘
                                    │
                                    ▼
                            ┌──────────────┐
                            │ RL Pipeline  │
                            │ (GRPO etc.)  │
                            └──────────────┘
```

### なぜ CTF を挟むか

| 直接送信 | CTF 経由 |
|---------|----------|
| Braintrust SDK ↔ Phoenix OTLP のフォーマット差を吸収不能 | CTF が唯一の真実。どちらにも変換可能 |
| 片方がダウンすると欠損 | JSONL にも常時書くのでゼロロス |
| 後から Phoenix に移行するとき再インストルメントが必要 | CTF JSONL を Phoenix に replay するだけ |
| RL パイプラインが Braintrust API に依存 | CTF JSONL を直接 ShareGPT 変換してRL投入可能 |

---

## 3. Canonical Trace Format (CTF) 仕様

```jsonc
// 1 session = 1 JSON object (JSONL の 1 行)
{
  "trace_id": "session_20260412_035213_72a77fbb",
  "session_id": "72a77fbb",
  "start_time": "2026-04-12T03:52:13.000Z",
  "end_time": "2026-04-12T03:58:42.000Z",
  "model": "anthropic/claude-sonnet-4-20250514",
  "platform": "telegram",
  "completed": true,
  "interrupted": false,
  "scores": {
    "completed": 1.0,
    "tool_error_rate": 0.1,
    // LLM-as-judge scores (Phase 2)
    "task_success": null
  },
  "metadata": {
    "hermes_version": "0.8.0",
    "user_message_preview": "DGX Sparkの評判を..."
  },
  "spans": [
    {
      "span_id": "llm_001",
      "parent_span_id": null,
      "type": "llm",
      "name": "llm_call_0",
      "start_time": "2026-04-12T03:52:14.200Z",
      "end_time": "2026-04-12T03:52:18.500Z",
      "input": { "approx_tokens": 3200, "message_count": 5 },
      "output": { "finish_reason": "tool_calls", "content_chars": 0 },
      "metrics": {
        "duration_ms": 4300,
        "prompt_tokens": 3150,
        "completion_tokens": 420,
        "total_tokens": 3570,
        "cache_read_tokens": 1200
      }
    },
    {
      "span_id": "tool_call_b5c360",
      "parent_span_id": "llm_001",
      "type": "tool",
      "name": "web_search",
      "start_time": "2026-04-12T03:52:18.600Z",
      "end_time": "2026-04-12T03:52:21.100Z",
      "input": { "query": "NVIDIA DGX Spark review benchmark..." },
      "output": { "success": true, "result_preview": "Found 5 results..." },
      "metrics": { "duration_ms": 2500 },
      "scores": { "tool_success": 1.0 }
    }
    // ... more spans
  ]
}
```

### CTF の設計原則

1. **自己完結**: 1 行で 1 session の全 span を含む。Braintrust / Phoenix どちらにも import 可能
2. **Hermes 互換**: session_id, model, completed/interrupted は Hermes の既存フィールドと一致
3. **ShareGPT 変換可能**: spans から conversation を再構成して `trajectory_compressor.py` に渡せる
4. **OpenInference 互換**: span.type は Phoenix の `openinference.span.kind` にマッピング可能

---

## 4. Plugin 設計: `hermes-o11y`

### ディレクトリ構造

```
~/.hermes/plugins/hermes-o11y/
├── plugin.yaml
├── __init__.py          # register() + hook handlers + collector
├── ctf.py               # Canonical Trace Format dataclasses & serialization
├── backends/
│   ├── __init__.py
│   ├── jsonl.py         # Always-on: CTF → JSONL file
│   ├── braintrust.py    # CTF span → Braintrust Logger API
│   └── phoenix.py       # CTF span → OTLP/gRPC (Phoenix)
├── exporters/
│   ├── ctf_to_sharegpt.py   # CTF → ShareGPT JSONL (for RL)
│   ├── ctf_to_otlp.py       # CTF JSONL → Phoenix replay
│   └── btql_to_ctf.py       # Braintrust export → CTF (backfill)
└── requirements.txt
```

### plugin.yaml

```yaml
name: hermes-o11y
version: "0.1.0"
description: "LLM observability with pluggable backends (Braintrust, Phoenix, JSONL)"
author: "kzinmr109"
requires_env: []  # backends check their own env vars
provides_hooks:
  - on_session_start
  - pre_api_request
  - post_api_request
  - pre_tool_call
  - post_tool_call
  - post_llm_call
  - on_session_end
```

### ctf.py — データ構造

```python
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional
import json
import uuid

@dataclass
class CTFSpan:
    span_id: str
    type: str                      # "llm" | "tool" | "chain"
    name: str
    start_time: str
    end_time: Optional[str] = None
    parent_span_id: Optional[str] = None
    input: dict = field(default_factory=dict)
    output: dict = field(default_factory=dict)
    metrics: dict = field(default_factory=dict)
    scores: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    error: Optional[str] = None

    @staticmethod
    def now() -> str:
        return datetime.now(timezone.utc).isoformat()

@dataclass
class CTFTrace:
    trace_id: str
    session_id: str
    start_time: str
    model: str
    platform: str = ""
    end_time: Optional[str] = None
    completed: Optional[bool] = None
    interrupted: bool = False
    scores: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    spans: list = field(default_factory=list)  # List[CTFSpan]

    def add_span(self, span: CTFSpan):
        self.spans.append(span)

    def to_jsonl_line(self) -> str:
        d = asdict(self)
        return json.dumps(d, ensure_ascii=False, default=str)

    @classmethod
    def from_dict(cls, d: dict) -> 'CTFTrace':
        spans_raw = d.pop('spans', [])
        trace = cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})
        trace.spans = [CTFSpan(**s) for s in spans_raw]
        return trace
```

### __init__.py — Collector + Hook Registration

```python
import logging
import os
import time
import threading
from pathlib import Path
from .ctf import CTFTrace, CTFSpan

logger = logging.getLogger(__name__)

# ── In-memory state (per session) ──────────────────────
_traces: dict[str, CTFTrace] = {}   # session_id → active trace
_pending_spans: dict[str, tuple[CTFSpan, float]] = {}  # span key → (span, monotonic_start)
_lock = threading.Lock()

# ── Backend registry ───────────────────────────────────
_backends = []

def _init_backends():
    from .backends.jsonl import JSONLBackend
    # JSONL is always on
    _backends.append(JSONLBackend())

    if os.environ.get("BRAINTRUST_API_KEY"):
        try:
            from .backends.braintrust import BraintrustBackend
            _backends.append(BraintrustBackend())
            logger.info("hermes-o11y: Braintrust backend enabled")
        except ImportError:
            logger.warning("hermes-o11y: braintrust SDK not installed")

    if os.environ.get("PHOENIX_COLLECTOR_ENDPOINT"):
        try:
            from .backends.phoenix import PhoenixBackend
            _backends.append(PhoenixBackend())
            logger.info("hermes-o11y: Phoenix backend enabled")
        except ImportError:
            logger.warning("hermes-o11y: opentelemetry SDK not installed")

def _emit(event: str, trace: CTFTrace, span: CTFSpan = None):
    for backend in _backends:
        try:
            getattr(backend, event)(trace, span)
        except Exception as e:
            logger.warning("hermes-o11y backend %s.%s failed: %s",
                           type(backend).__name__, event, e)

# ── Hook Handlers ─────────────────────────────────────

def _on_session_start(session_id, model="", platform="", **kw):
    with _lock:
        trace = CTFTrace(
            trace_id=f"session_{session_id}",
            session_id=session_id,
            start_time=CTFSpan.now(),
            model=model,
            platform=platform,
        )
        _traces[session_id] = trace
    _emit("on_trace_start", trace)

def _pre_api_request(session_id, api_call_count=0,
                     model="", approx_input_tokens=0, **kw):
    with _lock:
        trace = _traces.get(session_id)
        if not trace:
            return
        span = CTFSpan(
            span_id=f"llm_{session_id}_{api_call_count}",
            type="llm",
            name=f"llm_call_{api_call_count}",
            start_time=CTFSpan.now(),
            input={"approx_tokens": approx_input_tokens,
                   "model": model},
        )
        key = f"llm_{session_id}_{api_call_count}"
        _pending_spans[key] = (span, time.monotonic())

def _post_api_request(session_id, api_call_count=0,
                      api_duration=0, finish_reason="", usage=None, **kw):
    with _lock:
        key = f"llm_{session_id}_{api_call_count}"
        entry = _pending_spans.pop(key, None)
        trace = _traces.get(session_id)
        if not entry or not trace:
            return
        span, _ = entry
        span.end_time = CTFSpan.now()
        span.output = {"finish_reason": finish_reason}
        span.metrics = {
            "duration_ms": round((api_duration or 0) * 1000),
            **(usage or {}),
        }
        trace.add_span(span)
    _emit("on_span_end", trace, span)

def _pre_tool_call(tool_name, args=None, tool_call_id="",
                   session_id="", **kw):
    with _lock:
        span = CTFSpan(
            span_id=tool_call_id or f"tool_{time.monotonic_ns()}",
            type="tool",
            name=tool_name,
            start_time=CTFSpan.now(),
            input={"tool_name": tool_name, "args": _safe_truncate(args)},
        )
        _pending_spans[tool_call_id] = (span, time.monotonic())

def _post_tool_call(tool_name, args=None, result=None,
                    tool_call_id="", session_id="", **kw):
    with _lock:
        entry = _pending_spans.pop(tool_call_id, None)
        trace = _traces.get(session_id)
        if not entry or not trace:
            return
        span, start_mono = entry
        span.end_time = CTFSpan.now()
        is_error = _detect_error(result)
        span.output = {
            "success": not is_error,
            "result_preview": _safe_truncate(result, 2000),
        }
        span.metrics = {"duration_ms": round((time.monotonic() - start_mono) * 1000)}
        span.scores = {"tool_success": 0.0 if is_error else 1.0}
        if is_error:
            span.error = _safe_truncate(result, 500)
        trace.add_span(span)
    _emit("on_span_end", trace, span)

def _post_llm_call(session_id, user_message="",
                   assistant_response="", conversation_history=None,
                   model="", **kw):
    with _lock:
        trace = _traces.get(session_id)
        if not trace:
            return
        trace.metadata["last_user_message"] = _safe_truncate(user_message, 500)
        trace.metadata["turn_count"] = len(conversation_history or [])

def _on_session_end(session_id, completed=False, interrupted=False,
                    model="", **kw):
    with _lock:
        trace = _traces.pop(session_id, None)
        if not trace:
            return
        trace.end_time = CTFSpan.now()
        trace.completed = completed
        trace.interrupted = interrupted
        tool_spans = [s for s in trace.spans if s.type == "tool"]
        errors = sum(1 for s in tool_spans if s.scores.get("tool_success", 1.0) < 0.5)
        trace.scores = {
            "completed": 1.0 if completed and not interrupted else 0.0,
            "interrupted": 1.0 if interrupted else 0.0,
            "tool_error_rate": errors / max(len(tool_spans), 1),
        }
    _emit("on_trace_end", trace)

# ── Utilities ──────────────────────────────────────────

def _safe_truncate(val, max_len=1000):
    if val is None:
        return None
    s = str(val) if not isinstance(val, str) else val
    return s[:max_len] if len(s) > max_len else s

def _detect_error(result):
    if not result:
        return True
    if isinstance(result, str):
        try:
            import json
            d = json.loads(result)
            if isinstance(d, dict):
                if d.get("error") is not None: return True
                if d.get("success") is False: return True
        except (json.JSONDecodeError, ValueError):
            if result.strip().lower().startswith("error:"): return True
    return False

# ── Plugin Entry Point ─────────────────────────────────

def register(ctx):
    _init_backends()
    ctx.register_hook("on_session_start", _on_session_start)
    ctx.register_hook("pre_api_request", _pre_api_request)
    ctx.register_hook("post_api_request", _post_api_request)
    ctx.register_hook("pre_tool_call", _pre_tool_call)
    ctx.register_hook("post_tool_call", _post_tool_call)
    ctx.register_hook("post_llm_call", _post_llm_call)
    ctx.register_hook("on_session_end", _on_session_end)
    logger.info("hermes-o11y: registered with %d backend(s)", len(_backends))
```

---

## 5. Backend 実装

### 5.1 JSONL Backend (常時 ON — これが互換ファイル)

```python
# backends/jsonl.py
import json
from pathlib import Path
from datetime import datetime

class JSONLBackend:
    """CTF → ~/.hermes/o11y/traces-YYYY-MM-DD.jsonl"""

    def __init__(self):
        self._dir = Path.home() / ".hermes" / "o11y"
        self._dir.mkdir(parents=True, exist_ok=True)

    def _path(self) -> Path:
        return self._dir / f"traces-{datetime.utcnow():%Y-%m-%d}.jsonl"

    def on_trace_start(self, trace, span=None): pass
    def on_span_end(self, trace, span=None): pass

    def on_trace_end(self, trace, span=None):
        """Session 完了時に 1 行書き出す"""
        line = trace.to_jsonl_line()
        with open(self._path(), "a", encoding="utf-8") as f:
            f.write(line + "\n")
```

**この JSONL が Braintrust⇔Phoenix の互換ブリッジとなる。**

### 5.2 Braintrust Backend

```python
# backends/braintrust.py
import os
import logging

logger = logging.getLogger(__name__)

class BraintrustBackend:
    def __init__(self):
        import braintrust
        self._bt = braintrust.init_logger(
            project=os.environ.get("HERMES_O11Y_BT_PROJECT", "hermes-agent"),
            async_flush=True,
        )
        self._root_spans = {}  # session_id → braintrust span

    def on_trace_start(self, trace, span=None):
        root = self._bt.start_span(
            name=f"session-{trace.session_id}",
            span_attributes={"type": "task"},
            input={"session_id": trace.session_id},
            metadata={"model": trace.model, "platform": trace.platform},
        )
        self._root_spans[trace.session_id] = root

    def on_span_end(self, trace, span=None):
        if not span:
            return
        root = self._root_spans.get(trace.session_id)
        if not root:
            return
        child = root.start_span(
            name=span.name,
            span_attributes={"type": span.type},
            input=span.input,
        )
        child.log(
            output=span.output,
            metrics=span.metrics,
            scores=span.scores or {},
            metadata=span.metadata,
        )
        child.end()

    def on_trace_end(self, trace, span=None):
        root = self._root_spans.pop(trace.session_id, None)
        if not root:
            return
        root.log(
            output={"completed": trace.completed},
            scores=trace.scores,
            metadata=trace.metadata,
        )
        root.end()
```

### 5.3 Phoenix Backend (OpenTelemetry OTLP)

```python
# backends/phoenix.py
import os
import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

# Span kind mapping: CTF type → OpenInference span kind
_KIND_MAP = {
    "llm": "LLM",
    "tool": "TOOL",
    "chain": "CHAIN",
}

class PhoenixBackend:
    def __init__(self):
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.resources import Resource

        endpoint = os.environ.get("PHOENIX_COLLECTOR_ENDPOINT", "http://localhost:6006/v1/traces")

        resource = Resource.create({"service.name": "hermes-agent"})
        provider = TracerProvider(resource=resource)
        exporter = OTLPSpanExporter(endpoint=endpoint)
        provider.add_span_processor(BatchSpanProcessor(exporter))

        self._tracer = provider.get_tracer("hermes-o11y")
        self._root_contexts = {}  # session_id → (otel_span, context)

    def on_trace_start(self, trace_obj, span=None):
        from opentelemetry import context as otel_ctx
        otel_span = self._tracer.start_span(
            name=f"session-{trace_obj.session_id}",
            attributes={
                "openinference.span.kind": "AGENT",
                "session.id": trace_obj.session_id,
                "llm.model_name": trace_obj.model,
                "metadata.platform": trace_obj.platform,
            },
        )
        ctx = otel_ctx.set_value("current_span", otel_span)
        self._root_contexts[trace_obj.session_id] = (otel_span, ctx)

    def on_span_end(self, trace_obj, span=None):
        if not span:
            return
        entry = self._root_contexts.get(trace_obj.session_id)
        if not entry:
            return
        parent_otel_span, parent_ctx = entry
        from opentelemetry import trace as otel_trace, context as otel_ctx

        ctx = otel_trace.set_span_in_context(parent_otel_span, parent_ctx)
        child = self._tracer.start_span(
            name=span.name,
            context=ctx,
            attributes={
                "openinference.span.kind": _KIND_MAP.get(span.type, "CHAIN"),
                "input.value": str(span.input)[:4000],
                "output.value": str(span.output)[:4000],
                **({
                    "tool.name": span.name,
                } if span.type == "tool" else {}),
                **({
                    "llm.model_name": span.input.get("model", ""),
                } if span.type == "llm" else {}),
            },
        )
        for k, v in (span.metrics or {}).items():
            child.set_attribute(f"metrics.{k}", v)
        if span.error:
            child.set_attribute("status", "ERROR")
            child.set_attribute("error.message", span.error[:1000])
        child.end()

    def on_trace_end(self, trace_obj, span=None):
        entry = self._root_contexts.pop(trace_obj.session_id, None)
        if not entry:
            return
        otel_span, _ = entry
        otel_span.set_attribute("output.value", str({"completed": trace_obj.completed}))
        for k, v in (trace_obj.scores or {}).items():
            otel_span.set_attribute(f"scores.{k}", v)
        otel_span.end()
```

---

## 6. 相互変換 & 切り替え運用

### 6.1 普段の運用: Braintrust 主系

```bash
# .hermes/.env に追加
BRAINTRUST_API_KEY=sk-bt-...
# PHOENIX_COLLECTOR_ENDPOINT は設定しない → Phoenix backend は起動しない
```

- CTF JSONL は **常に** `~/.hermes/o11y/traces-YYYY-MM-DD.jsonl` に蓄積
- Braintrust UI でトレース閲覧・失敗フィルタ・スコアリング

### 6.2 Phoenix への切り替え/並列起動

```bash
# Phoenix サーバーを起動 (この VM で)
python -m phoenix.server.main serve  # → localhost:6006

# .hermes/.env に追加
PHOENIX_COLLECTOR_ENDPOINT=http://localhost:6006/v1/traces
# Hermes を再起動 → 両方に送信開始
```

### 6.3 過去データの Phoenix インポート (CTF → OTLP replay)

```python
# exporters/ctf_to_otlp.py
"""Replay CTF JSONL files into Phoenix via OTLP."""
import json
from pathlib import Path
from .backends.phoenix import PhoenixBackend
from .ctf import CTFTrace

def replay_to_phoenix(jsonl_path: str, endpoint: str = "http://localhost:6006/v1/traces"):
    import os
    os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = endpoint
    backend = PhoenixBackend()

    with open(jsonl_path) as f:
        for line in f:
            trace = CTFTrace.from_dict(json.loads(line))
            backend.on_trace_start(trace)
            for span in trace.spans:
                backend.on_span_end(trace, span)
            backend.on_trace_end(trace)

    print(f"Replayed {jsonl_path} to Phoenix at {endpoint}")

if __name__ == "__main__":
    import sys
    replay_to_phoenix(sys.argv[1])
```

### 6.4 Braintrust からの backfill (BTQL → CTF)

```python
# exporters/btql_to_ctf.py
"""Export Braintrust traces → CTF JSONL (for archival or Phoenix migration)."""
import requests, os, json

def export_from_braintrust(project_id: str, output_path: str,
                           filter_expr: str = None):
    API_URL = "https://api.braintrust.dev"
    headers = {"Authorization": f"Bearer {os.environ['BRAINTRUST_API_KEY']}"}

    where_clause = f"WHERE {filter_expr}" if filter_expr else ""
    query = f"""
        SELECT id, input, output, scores, metadata, span_attributes, metrics,
               created, span_id, root_span_id, span_parents
        FROM project_logs('{project_id}', shape => 'traces')
        {where_clause}
        LIMIT 10000
    """

    resp = requests.post(f"{API_URL}/btql", headers=headers,
                         json={"query": query, "fmt": "json"})
    rows = resp.json().get("data", [])

    # Group by root_span_id (= trace)
    from collections import defaultdict
    traces = defaultdict(list)
    for row in rows:
        traces[row.get("root_span_id", row["id"])].append(row)

    with open(output_path, "w") as f:
        for root_id, spans in traces.items():
            ctf = _bt_rows_to_ctf(root_id, spans)
            f.write(ctf.to_jsonl_line() + "\n")

    print(f"Exported {len(traces)} traces to {output_path}")
```

---

## 7. 失敗トレース管理 → RL 改善ループ

### 7.1 失敗トレースの抽出

```python
# exporters/ctf_to_sharegpt.py
"""CTF JSONL → ShareGPT format for RL training."""
import json

def extract_failures(ctf_jsonl_path: str, output_path: str,
                     threshold: float = 0.5):
    failures = []
    with open(ctf_jsonl_path) as f:
        for line in f:
            trace = json.loads(line)
            if trace.get("scores", {}).get("completed", 1.0) < threshold:
                failures.append(trace)

    # Convert to ShareGPT format compatible with trajectory_compressor.py
    trajectories = []
    for trace in failures:
        conv = _ctf_to_sharegpt(trace)
        trajectories.append({
            "conversations": conv,
            "timestamp": trace["end_time"],
            "model": trace["model"],
            "completed": trace["completed"],
            "failure_scores": trace["scores"],
        })

    with open(output_path, "w") as f:
        for t in trajectories:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    print(f"Extracted {len(failures)} failed traces → {output_path}")
    return failures
```

### 7.2 失敗分類 → 改善ルーティング

```
失敗トレース
    │
    ├─ failure_reason: skill_missing
    │   → Hermes auto skill creation (既存機能)
    │
    ├─ failure_reason: skill_incorrect
    │   → Skill revision (conversation history から修正版生成)
    │
    ├─ failure_reason: tool_misuse / hallucination
    │   → GRPO negative example
    │   → trajectory_compressor.py → tinker-atropos
    │
    ├─ failure_reason: context_overflow
    │   → System prompt / compression tuning
    │
    └─ failure_reason: timeout / api_error
        → Infra fix (not model issue)
```

### 7.3 GRPO 接続パイプライン

```bash
# 1. 失敗トレース抽出
python -m hermes_o11y.exporters.ctf_to_sharegpt \
  ~/.hermes/o11y/traces-2026-04-*.jsonl \
  --output failed_trajectories.jsonl \
  --threshold 0.5

# 2. トークン圧縮 (既存の trajectory_compressor.py)
python trajectory_compressor.py \
  --input failed_trajectories.jsonl \
  --target_max_tokens 16000

# 3. GRPO 学習 (既存の tinker-atropos)
python rl_cli.py "Train GRPO on failed trajectories from o11y export"
```

---

## 8. 運用モード早見表

| モード | 設定 | 動作 |
|--------|------|------|
| **Braintrust のみ** (推奨デフォルト) | `BRAINTRUST_API_KEY=...` | CTF JSONL ✅ + Braintrust ✅ |
| **Phoenix のみ** (OSS) | `PHOENIX_COLLECTOR_ENDPOINT=...` | CTF JSONL ✅ + Phoenix ✅ |
| **両方並列** | 両方設定 | CTF JSONL ✅ + Braintrust ✅ + Phoenix ✅ |
| **オフライン** | 何も設定しない | CTF JSONL ✅ のみ (後から replay 可能) |
| **Braintrust → Phoenix 移行** | `btql_to_ctf.py` + `ctf_to_otlp.py` | Braintrust 過去データを Phoenix に replay |
| **Phoenix → Braintrust 移行** | CTF JSONL を Braintrust に replay | 逆方向も CTF 経由で可能 |

---

## 9. 実装順序

| Phase | スコープ | 所要時間 |
|-------|---------|----------|
| **P0** | CTF 定義 + JSONL backend + plugin 骨格 | 0.5日 |
| **P1** | Braintrust backend | 0.5日 |
| **P2** | Phoenix backend + OTLP | 1日 |
| **P3** | CTF↔ShareGPT 変換 + 失敗抽出 | 1日 |
| **P4** | CTF→OTLP replayer + BTQL→CTF exporter | 1日 |
| **P5** | 失敗分類 LLM-as-judge + RL パイプライン接続 | 1週間 |

**P0-P2 までで「いつでも切り替え可能」の要件を満たす。**
