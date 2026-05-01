---
title: "DSPy.RLM"
type: concept
description: "Recursive Language Model — 大規模コンテキストをsandobx Python REPLでプログラム的に探索するDSPyモジュール"
category: concepts
sub_category: AI Agent Architectures
tags: [dspy, rlm, context-management, inference-time-scaling, sandbox, python-repl, pydantic-ai, code-mode, monty]
status: complete
related:
  - dspy
  - gea
  - alex-zhang
  - omar-khattab
  - context-fragments
  - long-context-coding-agents
created: 2026-04-21
updated: 2026-04-30
sources:
  - https://dspy.ai/api/modules/RLM/
  - https://github.com/alexzhang13/rlm
  - https://dspy.ai/tutorials/rl_ai_program/
---

# DSPy.RLM (Recursive Language Model)

## TL;DR

RLMは、LLMが**sandbox済みPython REPL**を通じて大規模コンテキストをプログラム的に探索できるDSPyモジュール。コンテキストを直接プロンプトに詰めるのではなく、「変数空間」（REPL内のデータ）と「トークン空間」（LLMが処理する内容）を分離し、モデルが本当に必要时才動的にコンテキストをロードする。

> *"Most people misunderstand RLMs to be about LLMs invoking themselves. The deeper insight is LLMs interacting with their own prompts as objects."*
> — Omar Khattab

## コア概念

### 問題: Context Rot

コンテキストが大きくなるにつれLLM性能が低下する現象（**context rot**）。従来の方法は全コンテキストをプロンプトに押し込むが、RLMは**選択的読み込み（selective reading）**で解決する。

### アーキテクチャ: REPLループ

RLMは以下の反復ループで動作する：

```
1. LLMはコンテキストの概要メタデータを受け取る（フルコンテキストではない）
2. LLMがPythonコードを書いてデータを探索（検索、フィルタ、集約）
3. コードがsandboxedインタープリタで実行され、LLMに出力が表示される
4. llm_query(prompt)でサブLLMを呼び出し、セマンティック分析可能
5. SUBMIT(output)で最終回答を返して終了
```

### 変数空間 vs トークン空間

| 空間 | 内容 | LLMの処理 |
|------|------|-----------|
| **変数空間** | REPL内のデータ（コンテキスト全体） | コードで操作 |
| **トークン空間** | LLMが実際に処理する内容 | メタデータ + 出力結果 |

## APIリファレンス

### コンストラクタパラメータ

| パラメータ | 型 | デフォルト | 説明 |
|-----------|----|-----------|------|
| `signature` | `str \| Signature` | 必須 | 入出力定義（例: `"context, query -> answer"`） |
| `max_iterations` | `int` | 20 | REPL交互ループの最大回数 |
| `max_llm_calls` | `int` | 50 | 実行あたりの最大llm_query呼び出し数 |
| `max_output_chars` | `int` | 10,000 | REPL出力に含める最大文字数 |
| `verbose` | `bool` | `False` | 詳細ログ出力 |
| `tools` | `list[Callable]` | `None` | インタープリタから呼び出せる追加ツール関数 |
| `sub_lm` | `dspy.LM` | `None` | サブクエリ用LM（デフォルトは`dspy.settings.lm`）。安いモデル推奨 |
| `interpreter` | `CodeInterpreter` | `None` | カスタムインタープリタ（デフォルトはDeno/Pyodide WASM） |

### 組み込みツール

| ツール | 説明 |
|-------|------|
| `llm_query(prompt)` | サブLLMでセマンティック分析（~500K文字対応） |
| `llm_query_batched(prompts)` | 複数プロンプトを並列実行（バッチ処理用） |
| `print()` | 出力表示（結果確認に必須） |
| `SUBMIT(...)` | 最終出力を提出して実行終了 |
| `re, json, collections, math` | Python標準ライブラリ |

## 使用例

### 基本的な使い方

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-5"))

rlm = dspy.RLM("context, query -> answer")

result = rlm(
    context="...very long document or data...",
    query="What is the total revenue mentioned?"
)
print(result.answer)
```

### 安価なサブLMを使用

```python
main_lm = dspy.LM("openai/gpt-5")
cheap_lm = dspy.LM("openai/gpt-5-nano")  # 抽出は安いモデルに委任

dspy.configure(lm=main_lm)
rlm = dspy.RLM("data, query -> summary", sub_lm=cheap_lm)
```

### 複数型出力

```python
rlm = dspy.RLM("logs -> error_count: int, critical_errors: list[str]")
result = rlm(logs=server_logs)
print(f"Found {result.error_count} errors")
```

### カスタムツール

```python
def fetch_metadata(doc_id: str) -> str:
    """ドキュメントIDのメタデータを取得"""
    return database.get_metadata(doc_id)

rlm = dspy.RLM(
    "documents, query -> answer",
    tools=[fetch_metadata]
)
```

### 非同期実行

```python
import asyncio

rlm = dspy.RLM("context, query -> answer")

async def process():
    result = await rlm.aforward(context=data, query="Summarize this")
    return result.answer

answer = asyncio.run(process())
```

### トレジェクトリ確認

```python
result = rlm(context=data, query="Find the magic number")

for step in result.trajectory:
    print(f"Code:\n{step['code']}")
    print(f"Output:\n{step['output']}\n")
```

## 出力構造

`dspy.RLM`は`Prediction`を返す：

- シグネチャで定義した出力フィールド（例: `result.answer`）
- `trajectory`: 各ステップのreasoning, code, outputを含む辞書のリスト
- `final_reasoning`: 最終ステップのLLM推論

## 設置要件

### Deno必須

RLMは**Deno + Pyodide**でWASMサンドボックスを構築する：

```bash
curl -fsSL https://deno.land/install.sh | sh
```

> ⚠️ **Known Issue**: DenoキャッシュがDSPyから見えない問題が報告されている。シェル再起動後、`deno --version`で確認すること。

外部サンドボックスプロバイダの使用も対応予定（ドキュメント準備中）。

## ベンチマーク結果

| モデル | 性能 |
|-------|------|
| RLM(GPT-5-mini) vs GPT-5 | OOLONG (132k context) で **114%向上** |
| RLM-Qwen3-8B vs Qwen3-8B | 4ベンチマーク平均で **28.3%向上** |
| コスト | ベースモデル呼び出しと同等〜それ以下（中央値） |

## 技術的深層

### RLM ≠ 自己呼び出し

Khattabが強調する通り、RLMの本質は「LLMが自分自身を呼び出す」ことではない。より深い洞察：

> *"LLMs interacting with their own prompts as objects"*

つまり、LLMは自分のプロンプトを**データとして操作する**。これは**out-of-coreアルゴリズム設計**のパターンを言語モデルに適用したもの。

### Mismanaged Geniuses Hypothesisとの接続

RLMは[Mismanaged Geniuses Hypothesis](mismanaged-geniuses-hypothesis)における**Recursive型**の実装証明：

- `for`ループによる任意の深さへの分解
- プログラム的分解によるほぼ無限のコンテキスト対応

### Context Fragmentsとの接続

RLMの「外部化されたオブジェクト」は[Context Fragments](context-fragments)の着想源。REPL変数がコンテキストフラグメントとして機能する。

## pydantic-ai でのRLM実現パターン

DSPyのRLMと同様の「REPLを介したコンテキスト分解」は、pydantic-ai + Montyでも実現可能。ただしアプローチが異なる。

| 次元 | DSPy.RLM | pydantic-ai native |
|---|---|---|
| REPL | Deno + Pyodide（WASMサンドボックス） | Monty（Rust製バイトコードVM） |
| ループ制御 | DSPyモジュール内部 | Agent output function / pydantic-graph |
| 状態管理 | REPL変数空間 | Monty snapshot + message_history |
| 制御権 | DSPyフレームワーク | Pydantic AI（Agent around REPL） |

実装パターンは3段階（詳細は[[concepts/code-mode]]）:

1. **最小形**: `Agent(..., capabilities=[CodeMode()], output_type=submit)` — DSPy RLMに近いUXを最少独自実装で
2. **DSPy互換ループ**: `RunCode | FinalAnswer` 構造化出力 + 明示的Action→Execute→Observeループ
3. **graph-native版**: Plan/RunCode/Observe/Finalizeをpydantic-graphノードに分解 + Monty snapshotでdurable execution

## RLM × Programmatic Tool Calling: 独立した2つのパラダイム

RLMと[[concepts/programmatic-tool-calling|Programmatic Tool Calling(PTC)]]は、同じ「LLMがコードを書く」基盤を共有しながらも、**異なる問題を異なる解決策で解く、独立進化したパラダイム**である。

### RLMはPTCを陽に取り込んでいない

RLMの論文（arXiv:2512.24601, Dec 2025）とDSPy.RLMのAPIを精査した結果：

1. **RLMの組み込みツールは`llm_query(prompt)`のみ** — これは外部ツール呼び出しではなく、**モデル自身の再帰的サブクエリ**。PTCの`allowed_callers`概念は存在しない。
2. **RLMの`tools`パラメータは汎用`Callable`** — 任意のPython関数を受け入れるが、PTC的な"async tool wrapping + allowed_callers"は提供しない。
3. **RLMが解く問題は「コンテキスト管理」** — 巨大ドキュメントをREPL変数として与え、モデルがコードで探索・分解・再帰クエリする。PTCが解く「ツールオーケストレーション」は射程外。

### 問題の違い

| 次元 | RLM | Programmatic Tool Calling |
|------|-----|--------------------------|
| **問題** | Context rot（コンテキスト増大による性能劣化） | ツール定義膨張・中間結果ブロート |
| **検索空間** | 100万トークン以上のドキュメント | 2,500+ APIエンドポイント |
| **モデルの行動** | コードで文脈を探索 → `llm_query`で再帰分析 | コードでツールをasync呼び出し → 結果をフィルタ |
| **再帰性** | **本質的** — `llm_query`がサブLMを起動 | **なし** — ツール呼び出しはフラット |
| **ツール起源** | `tools`パラメータ（任意Python関数） | `allowed_callers`付きのMCP/APIツール定義 |
| **`allowed_callers`** | 概念なし | **中核機構** |

### 基盤の共通性

両者に共通するのは、サンドボックスコード実行という**基盤**だけ：

```
LLMがコードを書く → サンドボックスで実行 → 結果だけがモデルに返る
```

この基盤は同じだが、コードの**中身**が根本的に異なる：

- RLMのコード: `data[start:end]`, `re.findall(pattern, text)`, `llm_query("summarize this")`, `SUBMIT(answer)`
- PTCのコード: `await tool_a(input)`, `await tool_b(result)`, `asyncio.gather(...)`, `print(filtered)`

### アーキテクチャ上の自由度: 合成可能だが設計されていない

RLMの`tools`パラメータにPTC的なツール関数を渡すことは**技術的に可能**：

```python
# RLMのtoolsにPTC的な関数を渡す（可能だが、PTCのasync wrappingはない）
rlm = dspy.RLM(
    "context, query -> answer",
    tools=[search_api, fetch_document]  # 任意のPython関数
)
```

しかしこれは**設計された統合ではなく、偶発的な拡張性**。以下の制約がある：

1. PTCの`allowed_callers`によるセキュリティ境界がない — RLM内の全コードが全ツールにアクセス可能
2. ツールのasync自動ラッピングがない — PTCではツールが自動的にasync変換される
3. `caller`識別子がない — PTCのレスポンスには`caller`フィールドでコード→ツール呼び出しを追跡できる
4. ツール結果のコンテキスト除外保証がない — PTCではプログラム的呼び出しの結果は自動的にコンテキストから除外される

### 結論: 独立した2つのパラダイム

```
RLM:                                   PTC:
コードで文脈を探索                     コードでツールを呼び出す
    ↓                                       ↓
llm_queryで再帰分析                    await tool()で外部実行
    ↓                                       ↓
SUBMITで最終回答                       print(stdout)で終了
```

両者は**補完関係**にある：
- RLMは「何を分析するか」の選択（コンテキスト分解）
- PTCは「どう実行するか」の制御（ツールオーケストレーション）

真の統合（RLM内でPTCツールを呼び出し→結果をさらに再帰分析）は、現状では**手動構成が必要**であり、フレームワークレベルでは未対応。ただし[[concepts/pydantic-ai-harness]]（Monty + CodeMode）は両方を内包できるプラットフォームとして最も統合に近い。

## ステータス・既知問題

| 項目 | ステータス |
|------|----------|
| API安定性 | **Experimental** — 将来バージョンで変更可能性あり |
| スレッドセーフティ | カスタムインタープリタ使用時はスレッドセーフではない。並列使用時は別インスタンスを作成すること |
| Deno依存 | 必须 — インストールとキャッシュ設定に注意 |

## 関連プロジェクト

- [DSPy](dspy) — RLMを提供するDeclarative LMプログラミングフレームワーク
- [GEPA](gepa) — 同一著者のGenetic Pareto Prompt Evolution
- [Alex Zhang](alex-zhang) — RLMの第一著者
- [Omar Khattab](omar-khattab) — RLM共著者、DSPy創設者
- [Context Fragments](context-fragments) — RLMのexternalized objectsに着想を得た概念
- [Long Context Coding Agents](long-context-coding-agents) — RLM関連技術
- [[concepts/pydantic-ai-harness]] — MontyベースのCodeModeを提供
- [[concepts/code-mode]] — Agent around REPLパターンの詳細
- [[concepts/monty-sandbox]] — Rust製REPLサンドボックス

## See Also

- [[concepts/_index]]
- [[concepts/rlm-recursive-language-models]]
- [[concepts/dspy]]
