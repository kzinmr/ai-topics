---
title: "DSPy.RLM"
description: "Recursive Language Model — 大規模コンテキストをsandobx Python REPLでプログラム的に探索するDSPyモジュール"
category: concepts
sub_category: AI Agent Architectures
tags: [dspy, rlm, context-management, inference-time-scaling, sandbox, python-repl]
status: complete
related:
  - dspy
  - gea
  - alex-zhang
  - omar-khattab
  - context-fragments
  - long-context-coding-agents
created: 2026-04-21
updated: 2026-04-21
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

## See Also

- [[concepts/_index.md]]
- [[concepts/rlm-recursive-language-models.md]]
- [[concepts/dspy.md]]
