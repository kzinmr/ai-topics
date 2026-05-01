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

## RLM × Programmatic Tool Calling: 補完する2軸（関数軸 vs データ軸）

### 根本的なフレーミング

RLMと[[concepts/programmatic-tool-calling|PTC]]は、LLMの2つの根本的な問題に、同じ解決策（コード実行）を適用したものと理解できる：

| 軸 | PTCが解決する問題 | RLMが解決する問題 |
|----|------------------|------------------|
| **中心** | **ツール（関数）** — 「どう実行するか」 | **データ（文脈）** — 「何を分析するか」 |
| **LLMの代替対象** | 逐次ツール呼び出し（N回の`tool_use`ブロック） | RAG / 長文脈プロンプト（全データの詰め込み） |
| **問題** | ラウンドトリップ爆発・中間結果ブロート | Context rot（コンテキスト増大による性能劣化） |
| **コードが書く対象** | `await tool_a()`, `asyncio.gather()` | `context[start:end]`, `re.findall()`, `llm_query()` |
| **コードの目的** | ツールの実行順序・分岐・並列化を自由に制御 | データの探索範囲・分解方法を自由に選択 |
| **コードの入出力** | 入力を決めてツールを呼び、結果を変数で受け取る | 文脈を切り出して分析し、集約して回答する |
| **決定論の次元** | 実行順序の決定論（同じコードなら同じツールが同じ順序で呼ばれる） | 探索戦略の決定論（同じコードなら同じ範囲を見る） |
| **自由度の次元** | 逐次ツール呼び出しより高い（コードで条件分岐・並列実行が可能） | RAG/長文脈より高い（コードで探索範囲・分解粒度を自由に制御） |

### 補完関係の図示

```
                ↑ RLM (データ軸: 何を分析するか)
                │   コードで文脈を探索・分解・再帰分析
                │   context[start:end], llm_query(), SUBMIT()
                │
                │   ★ Tool-Augmented RLM (案A)
                │   PTC in RLM — 環境にtoolsを追加
                │   context探索 + await tool() + llm_query()
                │
    ────────────┼──────────────────────────────────→ PTC (関数軸: どう実行するか)
                │   コードでツールをasync呼び出し・並列化
                │   await tool(), asyncio.gather()
                │
                │   RLM as PTC Tool (案B)
                │   PTCエージェントがRLMをツールの一つとして呼ぶ
```

### 具体例で見る違い

**PTCのコード（関数軸）:**
```python
# 「どう実行するか」に集中
results = await asyncio.gather(
    query_database("SELECT * FROM sales"),
    fetch_weather("Tokyo"),
    search_docs("budget 2025"),
)
aggregated = sorted(results[0], key=lambda x: x['revenue'])[:5]
print(aggregated)
```

**RLMのコード（データ軸）:**
```python
# 「何を分析するか」に集中
budget_sections = [s for s in context if "budget" in s.lower()]
for i, section in enumerate(budget_sections[:10]):
    analysis = llm_query(f"Extract key numbers from: {section}")
    print(f"Section {i}: {analysis}")
SUBMIT(synthesized_answer)
```

**統合されたコード（Tool-Augmented RLM, 案A）:**
```python
# 両軸を同時に扱う
relevant = [s for s in context if "revenue" in s.lower()]  # RLM: 文脈探索
financials = await query_financial_api({"ids": extract_ids(relevant)})  # PTC: 外部実行
analysis = llm_query(f"Compare: {relevant} vs {financials}")  # RLM: 再帰分析
print(analysis)
```

### なぜこのフレーミングが重要か

PTCとRLMを「コード実行」という共通基盤で1つにまとめてしまうと、**それぞれが解決している本質的に異なる問題が見えなくなる**。一方で「全く別物」として扱うと、**統合時の相乗効果を見落とす**。

正しい理解:
- PTCは**関数軸**の最適化（標準のtool callingが非効率なのをコードで改善）
- RLMは**データ軸**の最適化（RAG/長文脈が非効率なのをコードで改善）
- 両者は直交するため、統合（Tool-Augmented RLM, 案A）によって両軸を同時に最適化できる

### DSPy実装における現状と第一原理の可能性

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

### 第一原理からの再検討: PTC統合のための環境拡張設計

上の分析は「DSPy.RLM実装における現状」としては正確だが、RLM論文の**純粋なアーキテクチャ**から見ると、PTC統合はむしろ自然な拡張である。

#### RLM論文の環境抽象化

RLM論文が定義する環境は、以下の3要素からなる：

```
Environment = {
  REPL: Python実行環境（状態永続、sandboxed builtins）
  context変数: 巨大な入力データ
  llm_query(): 再帰的サブLM呼び出し
  SUBMIT(): 最終回答
}
```

この環境は **「モデルが記号的に操作できる対象の集合」** として設計されている。論文の強調：

> *"The key insight is that long prompts should not be fed into the neural network directly but should instead be treated as **part of the environment** that the LLM can **symbolically interact with**."*

論文で「環境の部品」として想定されているのは`context`変数だけだが、**この抽象化は任意の「記号的操作可能な対象」に拡張可能**である。

#### Tool-Augmented Environment Design

PTCツールをRLM環境の第一級市民として統合する設計：

```
Tool-Augmented Environment = {
  REPL: Python実行環境（sandboxed, async対応）
  context変数: 入力データ（RLM由来）
  tools: PTCツール群（async関数として公開） ← NEW
  llm_query(): 再帰的サブLM呼び出し（RLM由来）
  SUBMIT(): 最終回答（RLM由来）
}
```

RLMのループは変わらないが、コードが書ける対象が増える：

```python
# 純粋RLMのコード（論文の例）
for i, section in enumerate(context):
    buffer = llm_query(f"Section {i}: {section}")
    print(f"Tracked: {buffer}")

# Tool-Augmented RLMのコード（同じループ構造）
for i, section in enumerate(context):
    # RLM: コードで文脈を探索
    relevant = [s for s in section if "budget" in s.lower()]
    # PTC: コードで外部ツールを呼び出し
    financial_data = await query_financial_api({"ids": extract_ids(relevant)})
    # RLM: 再帰分析
    analysis = llm_query(f"Analyze: {relevant}, {financial_data}")
    print(f"Tracked: {analysis}")
```

#### なぜRLMの環境抽象化がPTCと相性が良いか

| RLM環境の特性 | PTC統合との整合性 |
|--------------|------------------|
| **REPLで任意のPythonコード実行** | PTCツールも`await tool()`で呼べる — コードの延長線上 |
| **結果はREPLの変数空間に留まる** | PTCツール結果もモデルコンテキストに入らず、変数空間で保持 |
| **sandboxed builtins** | PTCの`allowed_callers`はsandboxの一種 |
| **llm_queryで再帰分析** | PTCツール結果をllm_queryの入力にできる |
| **SUBMITで最終回答** | PTCツール結果を含む最終回答を提出 |

#### 3つの統合アーキテクチャ

論文の環境抽象化を尊重した場合、3つのアーキテクチャが考えられる：

##### 案A: PTC in RLM（RLMが外側、PTCが内側）★ 推奨

```
RLM Root（環境にcontext + tools + llm_query）
  └── モデルがPythonコードを書く
        ├── context[start:end]  ← RLM: 文脈探索
        ├── await tool_a()       ← PTC: ツール呼び出し
        └── llm_query(...)       ← RLM: 再帰分析
  └── SUBMIT(answer)
```

**利点**: RLMのループ構造（探索→分析→集約）を維持したまま、PTCツールを追加。環境の一貫性が高い。

##### 案B: RLM as PTC Tool（PTCが外側、RLMがツールの一つ）

```
PTC Agent
  ├── await search_db(query)
  ├── await rlm_analyze(context, sub_query)  ← RLMを「ツール」として呼ぶ
  ├── await fetch_details(ids)
  └── submit(answer)
```

**利点**: AnthropicのPTC APIに直接載せられる。ただしRLMの再帰的探索が「外部ツール呼び出し」に埋没し、文脈探索の自然さが失われる。

##### 案C: Dual Environment（環境の二層化）

```
Layer 1: PTC Environment（tool orchestration）
  └── await tool_a(), await tool_b()
      └── Layer 2: RLM Environment（context decomposition）
            └── context探索, llm_query(), SUBMIT()
```

**利点**: 関心の分離。ただし環境の切り替えにオーバーヘッド。

#### 設計上の課題

真の統合には以下の設計判断が必要：

1. **ツール発見**: PTCツールの定義（input_schema）をどうRLM環境に注入するか？
   - Cloudflare CodeModeの教訓: `search()` + `execute()`の2ツールに圧縮するのが最適
   - → 環境に`discover_tools(query)` + `call_tool(name, args)`を追加

2. **セキュリティ境界**: `allowed_callers`に相当する制御をどうREPLに課すか？
   - RLM論文のsandboxed builtinsは「危険な関数を消す」だけ
   - PTCは「許可されたツールだけを呼べる」というpositive model
   - → RLMのsandboxに`allowed_callers`相当の許可リストを追加

3. **結果ルーティング**: PTCツールの結果はモデルコンテキストに入れず、REPL変数空間に留める
   - RLMはすでに`print()`出力だけをモデルに見せている
   - → PTCツール結果も`print()`されたものだけがモデルコンテキストに入る（自然な拡張）

4. **再帰との相互作用**: PTCツール結果 + 再帰的llm_queryの合成
   - → `llm_query(tool_result + context_snippet)` で両者を合成可能（REPL変数空間なら自然）

#### まとめ

DSPy.RLMが現在PTCを「陽に取り込んでいない」のは実装の制約であって、**アーキテクチャ上の必然ではない**。RLM論文の環境抽象化は、PTCツールを第一級市民としてホストするよう設計されていると言える。

設計判断としては**案A（PTC in RLM）**が優れている：
- RLMのループ構造を維持
- PTCツールを環境の一部として自然に統合
- Cloudflare CodeModeの`search()+ execute()`パターンを環境層に移植可能
- pydantic-ai-harness（Monty + CodeMode）がこのアーキテクチャに最も近い実装

実装の最短経路は、RLM環境の`tools`パラメータを「単なるPython関数のリスト」から「async対応・allowed_callers付き・結果自動フィルタリング付きのPTCツールコレクション」に昇格させること。これはDSPy.RLMの変更でも、pydantic-ai-harness上の独立実装でも可能。

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
