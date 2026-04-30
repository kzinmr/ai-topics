---
title: "CodeMode — LLM Code Execution Over Sequential Tool Calling"
tags: [code-execution, monty, pydantic-ai, tool-calling, sandbox, RLM]
created: 2026-04-16
updated: 2026-04-30
type: concept
---

# CodeMode — LLM Code Execution Over Sequential Tool Calling

## Definition

CodeMode is the paradigm where LLMs write code (typically Python) for batch execution rather than making sequential tool calls. Coined by Cloudflare and independently developed by Anthropic, Pydantic, and others.

> *"LLMs work faster, cheaper and more reliably when they write code instead of making sequential tool calls."* — Samuel Colvin

## The Execution Continuum

| Approach | Control | Capability | Start Latency | Cost Model |
|----------|---------|------------|---------------|------------|
| **Tool Calling** | High | Low | Sequential (4-7 round trips, ~12s) | Per-token |
| **CodeMode (Monty)** | High-Medium | Medium | 0.004ms | In-process, zero infra |
| **Sandbox Services** (Modal, E2B, Daytona) | Medium | High | ~1000ms+ | Per-execution billing |
| **Coding Agents** (Claude Code, Cursor) | Low | Very High | Minutes | High |
| **Full Computer Use** | None | Maximum | Minutes | Very high |

## Why It Works

1. **Parallel Execution**: LLM writes a single Python script using `asyncio.gather()` instead of 4-7 sequential tool calls
2. **Native Control Flow**: Loops, conditionals, transforms, comprehensions — all expressed naturally in code
3. **Lower Token Usage**: Weather comparison example: 4.1k input tokens (tool calling) vs 3.3k (CodeMode), $0.019 vs $0.017
4. **Composable**: Code can chain operations, handle errors, and transform data in ways tool calling cannot

## Monty Implementation (Pydantic)

- Minimal, secure Python interpreter written in Rust
- From-scratch bytecode VM using Ruff's parser
- **Capabilities-based security**: Zero default access, explicit grants
- **State snapshotting**: Serialize execution mid-flight to bytes, resume elsewhere
- **Binary size**: ~4.5MB, memory overhead ~5MB

## Key Advocates

- **Samuel Colvin** (Pydantic): Built Monty, advocates "start from nothing" security
- **Andrej Karpathy**: Popularized code-over-sequential-tool-calls paradigm
- **Anthropic**: Documented in multiple blog posts on agent patterns
- **Cloudflare**: Coined the term "CodeMode"

## Official Implementations

### Pydantic AI Harness — CodeMode

The [pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) library provides the canonical CodeMode implementation:

- `CodeMode` capability wraps all agent tools into a single `run_code` tool
- Powered by [Monty](https://github.com/pydantic/monty) sandbox (Rust-based Python VM)
- Supports `asyncio.gather()` for parallel tool execution within one model round-trip
- Observability via [Logfire](https://pydantic.dev/logfire) — nested tool calls as child spans

### Other Implementations

- **Anthropic** — Code execution in Claude agent mode
- **Cloudflare** — Coined the term, blog documentation

## Related Patterns

- [[concepts/harness-engineering]] — Monty as a harness environment
- [[concepts/pydantic-ai-harness]] — Official CodeMode capability library
- [[concepts/structured-outputs]] — Type safety constrains LLM output
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Alternative to MCP tool execution

## Agent around REPL: 3つの実装パターン

CodeModeをRLM（Recursive Language Model）的に使う場合、pydantic-ai上では3段階のアプローチが存在する。

### パターン1: CodeMode + output function（最小形、推奨）

既存のCodeModeを土台にし、`output_type`をoutput functionにすることでモデルに「最後は必ずsubmit(...)を呼ばせる」形にする。REPLはagentの内部実行機構、最終制御はagent側に残す。

```python
from pydantic_ai import Agent
from pydantic_ai_harness import CodeMode

def submit(answer: str) -> str:
    """Final answer — ends the run."""
    raise EndRun(answer)

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    capabilities=[CodeMode()],
    output_type=submit,
    instructions=(
        '探索・集計・中間計算は run_code で行い、'
        '確信が持てたら submit(...) で終了すること。'
    ),
)
```

DSPyのRLMに近いUXを、Pydantic AIの流儀で最も少ない独自実装で実現できる。CodeModeはすでに全ツールを1個の`run_code`ツールへ束ね、同一agent run内でREPL状態を保持し、`restart: true`でリセットできる。

### パターン2: Action → Execute → Observe の明示的外部ループ（DSPy互換）

DSPyのRLMをより忠実に移植したい場合、agentの`output_type`を`RunCode | FinalAnswer`のような構造化出力にし、各ターンでモデルに「次のaction」を1つだけ出させる。ホスト側がRunCodeを受け取ったらMonty REPLで実行し、観測結果を次ターンへ戻す。

```python
class RunCode(BaseModel):
    code: str

class FinalAnswer(BaseModel):
    answer: str

output_type = RunCode | FinalAnswer
```

Pydantic AIは複数run間で`message_history`をそのまま受け渡し可能。内部的にagentは`pydantic-graph`ベースで動いており、`agent.iter()`によるnode-level制御もあるため、"Action → Execute → Observe → Next Action"の明示ループは素直に組める。

### パターン3: graph-native版（本番向け）

Plan / RunCode / Observe / Finalizeを明示ノードに分け、Monty側はsnapshotを保存できるので中断・再開やprocess境界越しの復元が容易。Pydantic AIはdurable executionを公式に持ち、Temporal / DBOS / Prefect / Restateをサポートしているため、「RLMの状態遷移はpydantic-graph、コード実行状態はMonty snapshot」という二層化は相性が良い。

## Agent around REPL vs Agent on REPL

Montyは**REPL sandboxソリューション**として設計されている。RLMをpydantic-aiネイティブに実現する場合、「Agent on REPL」（モデルをREPLの中に閉じ込める）より**「Agent around REPL」**（REPLをagentの内部executorとして使う）として設計するのが健全。

MontyのREADMEはexperimentalと明記されており、合理的なsubsetのみ、ホスト環境アクセスはexternal function経由、サードパーティライブラリは対象外。つまり**会話制御・出力検証・承認・履歴管理・durabilityはPydantic AI外側、REPLは内側のexecutorに留める**のが正しい分離。

## Deferred Tool Calls の現状

CodeModeのドキュメントには「approval/deferredなツールはsandboxから除外」と記載があるが、v0.2.0リリースノートでは`HandleDeferredToolCalls`でinline解決できるようになっている。実装は「handlerがいれば解決、いなければエラー」という分岐。現状は「完全禁止」ではなく**「handler必須で対応中」**と読むのが正確。ドキュメントが実装に追いついていない可能性がある。
