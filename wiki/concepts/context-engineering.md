---
title: "Context Engineering — Anthropic's Dynamic Token Curation Framework"
status: draft
created: 2026-04-13
source: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
author: "Anthropic Engineering"
tags: [context-engineering, prompt-engineering, jit-retrieval, compaction, memory-management]
related: [claude-memory, chatgpt-memory-bitter-lesson, harness-engineering]
---

# Context Engineering — Anthropic's Dynamic Token Curation Framework

Anthropicが提唱する**コンテキストエンジニアリング** — プロンプトエンジニアリングからのパラダイムシフト。静的な指示書きから、エージェントループ全体での**動的トークンキュレーション**へ。

> "Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information."
> — Anthropic Engineering, Sep 2025

## パラダイムシフト: Prompt vs Context Engineering

| 次元 | プロンプトエンジニアリング | コンテキストエンジニアリング |
|------|--------------------------|------------------------------|
| **焦点** | システム指示の作成・整理 | 推論中の**コンテキスト全体**の管理 |
| **スコープ** | 離散的・1回限りのタスク | 反復的・循環的（エージェントターンごと） |
| **構成要素** | システムプロンプト、few-shot例 | システムプロンプト、ツール、MCP、外部データ、メッセージ履歴、ランタイム検索 |

## The Finite "Attention Budget" & Context Rot

LLMはアーキテクチャ的に**有限の注意力バジェット**を持つ：

- **Context Rot**: トークン数増加に伴い、想起精度が**勾配的に**低下（ハードな崖ではない）
- **Transformerの制限**: 全トークンが全トークンに注目 → `n²` のペアワイズ関係
- **位置エンコーディング補間**: 長いコンテキストを可能にするが、長期推論の精度が低下
- **トレーニングバイアス**: モデルは主に短いシーケンスでトレーニングされている

> "Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM."

## JIT Context Strategy（Just-in-Time コンテキスト）

**Anthropicが推奨するメモリ戦略**: 事前に全データをロードするのではなく、**必要なときに必要なだけ取得**。

```
軽量識別子（ファイルパス、保存クエリ、Webリンク）を保持
         ↓
ランタイムでツール経由でデータ取得（glob, grep, read）
         ↓
エージェントが段階的にコンテキストを発見
```

### 人間の認知との類似性

| 人間の認知 | エージェントのJIT |
|------------|-------------------|
| 暗記ではなく索引に依存 | ファイルシステム・ブックマークに依存 |
| 必要に応じて参照 | ツール呼び出しで動的取得 |
| メタデータで行動を信号化 | フォルダ階層・命名規則・タイムスタンプ |

### ハイブリッド戦略（Anthropic推奨）

```
静的/重要なコンテキスト → 事前ロード（CLAUDE.md等）
動的コンテキスト     → JIT取得（glob/grep/検索）
```

> 例: `CLAUDE.md`を最初にドロップ + `glob`/`grep`でオンデマンドファイルナビゲーション

## 長時間タスクのための3つのメモリ戦略

| 戦略 | 仕組み | ユースケース | 実装ヒント |
|------|--------|-------------|-----------|
| **Compaction** | コンテキスト限界付近で会話を要約 → 高忠実度サマリーで再開 | 対話フロー、詳細なやり取り | アーキテクチャ決定と未解決バグを保持。冗長なツール出力を削除。**再現性を最優先**し、次に精度を調整 |
| **Agentic Memory** (構造化メモ書き) | エージェントがコンテキスト外に永続メモを保存（`NOTES.md`、TODOリスト）→ 後で読み戻し | 反復的開発、明確なマイルストーン | 数千ステップにわたる進捗/依存関係の追跡を可能にする。Claude Dev Platform memory tool（ベータ）はファイルベース外部メモリをサポート |
| **Sub-Agent** | メインエージェントが高レベル計画を調整 → サブエージェントが詳細実装 | 大規模タスク分解 | 各サブエージェントが独立したコンテキストを持つため、メインエージェントの注意力を節約 |

## ツール設計のメモリへの影響

- **トークン効率**: ツールは自己完結的で、冗長な出力を避ける
- **オーバーラップ禁止**: 重複するツールは意思決定麻痺を引き起こす
  > "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better."
- **入力パラメータ**: 記述的で明確、モデルの強みに合わせる

## Shlok Khemaniの「Bitter Lesson」との関係

| Khemaniの主張 | Anthropicの実装 |
|---------------|-----------------|
| 「最良のメモリはメモリなし」 | JIT Context — 事前ロードせず必要時に取得 |
| ファイルシステムがメモリ | CLAUDE.md + glob/grep パターン |
| ステートレスセッション | Compactionで状態をリセット、サマリーで継続 |
| 計算がメモリを置き換える | Sub-Agentでコンテキストを分散、注意力バジェットを節約 |

**両者は同じ結論に収束**: 外部データベースではなく、**ファイルシステム + 動的取得**がスケーラブルなメモリ戦略。

## Sources

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic Engineering, Sep 29, 2025
- [ChatGPT's Memory Problem](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson) — Shlok Khemani（比較分析）
