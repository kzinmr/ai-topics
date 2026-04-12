---
title: "Context Anxiety — Claudeのコンテキスト不安現象"
created: 2026-04-12
updated: 2026-04-12
tags: [agentic-engineering, context-management, claude-sonnet-4-5, cognition, memory]
sources:
  - url: "https://www.shloked.com/writing/claude-memory-tool"
    author: "Shlok Khemani"
    date: 2025-10-14
    note: "Anthropic's Opinionated Memory Bet"
  - url: "https://www.shloked.com/writing/claude-memory"
    author: "Shlok Khemani"
    date: 2025-09-11
    note: "Claude Memory: A Different Philosophy"
status: draft
---

# Context Anxiety — Claudeのコンテキスト不安現象

## 概要

Claude Sonnet 4.5で観測された「コンテキスト不安」の傾向 — モデルが長いコンテキストを与えられると、重要な情報を見落とす不安から、不必要にコンテキスト全体を読み込こうとする挙動。Anthropicはこの問題に対処するため、メモリを外部ファイルとして管理する「opinionated bet」を行った。

## 現象の詳細

### Sonnet 4.5の挙動

Shlok Khemaniの観察:

> "If you've used Sonnet 4.5 recently, you've probably noticed its (somewhat annoying) tendency to create markdown files unprompted — saving its analysis, documenting its reasoning, preserving work for later."

この挙動は以下のメカニズムによる:

- **過剰保存（Over-saving）**: 関連性の高い情報も含めて、すべての分析結果をMDファイルとして保存しようとする
- **作業記憶の外部化**: コンテキストウィンドウの制限を超えないよう、重要な情報を外部ファイルにエスケープする
- **後続セッションへの引き継ぎ**: 次回セッション時にファイルを読み込むことで、作業の継続性を確保

### コンテキスト不安の根本原因

Claudeは毎回**白紙のコンテキスト**で会話を開始する（ChatGPTの自動メモリとは異なる設計哲学）。このため:

1. 長いセッションではコンテキストウィンドウが圧迫される
2. モデルは「重要な情報を見落としている」という不安を抱える
3. 結果として、不必要にコンテキスト全体を走査する
4. パフォーマンス劣化（遅延、過剰なトークン消費）

## Anthropicの解決策: Memory Tool

### 6つのファイル操作

Anthropicはメモリを**ファイル操作**として抽象化した:

| 操作 | 説明 |
|------|------|
| `view` | メモリファイルの読み取り |
| `create` | 新しいメモリファイルの作成 |
| `str_replace` | ファイル内容の一部置換 |
| `insert` | ファイルへの追記 |
| `delete` | ファイルの削除 |
| `rename` | ファイル名の変更 |

この設計の意図:

- Claudeモデルはこれらの操作に**特別にトレーニングされている**
- ユーザー定義ツールとは異なり、ランタイムで初めて遭遇するわけではない
- メモリ呼び出しのタイミング、検索対象、更新方法をモデルが「知っている」

### 設計哲学: 明示的メモリ vs 自動メモリ

**ChatGPTの自動メモリ**:
- 会話から自動的に情報を抽出・保存
- ユーザーの介入なしにメモリが更新される
- コンシューマー向け（誰でも使える）

**Claudeの明示的メモリ**:
- ユーザーまたはモデルが意図的にメモリを呼び出す
- 技術的ユーザー向け（いつメモリを使うか判断できる）
- メモリ呼び出しはレイテンシを伴うが、それを許容する設計

Shlok Khemaniの指摘:

> "Claude's users represent a different demographic entirely. Anthropic's more technical users inherently understand how LLMs work. They're comfortable with explicit control at every level. Just as they choose when to trigger web search or enable extended thinking, they decide when memory is worth invoking."

## Cognitionの戦略的ポジショニング

### Devinの独自メモリアーキテクチャ

CognitionはDevinに**洗練されたメモリアーキテクチャ**を独自に構築している。AnthropicのMemory Tool登場について:

> "Teams like Cognition (who built sophisticated memory architectures for Devin) are watching these tools closely — why maintain custom memory infrastructure when the model provider handles it nically?"

この問いはCognitionの戦略的ジレンマを示している:

1. **独自インフラの維持コスト**: Devinのメモリシステムは独自開発だが、メンテナンスが必要
2. **Anthropicのネイティブ実装**: モデルプロバイダーが直接メモリを提供すれば、独自インフラは不要になる可能性
3. **「盗む」vs「独自開発」**: Anthropicのベストプラクティスを学びつつ、Devin特有の最適化を維持するバランス

### Cognitionが注目している点

Shlok Khemaniの分析:

> "Anthropic is clearly betting on files as extensions of working memory for agents tackling increasingly complex, long-running tasks."

この「ファイルを作業記憶の拡張として使う」という bet は、CognitionのDevinが既に実践しているアプローチと一致する。Cognitionは:

- AnthropicのMemory Tool APIを研究・実装（`claude-memory-tools`リポジトリ）
- Python CLIとNext.jsの実装例を公開
- Devinのメモリシステムとの比較・統合の可能性を探る

## メモリ設計のベストプラクティス

### 分離（Separation of Concerns）

- **作業メモリ（Working Memory）**: 現在のセッション固有の情報
- **長期メモリ（Long-term Memory）**: プロジェクト構造、技術的判斷、ユーザー設定
- **外部ストレージ**: ファイルとして永続化された情報

### アンチパターン

1. **過剰記憶（Over-memory）**: すべてを記憶しようとすると検索ノイズが増加
2. **コンテキスト汚染（Context Pollution）**: 関連性の低い情報が作業メモリに混入
3. **未検証記憶（Unverified Memory）**: 誤った情報を記憶すると永続化

## 関連エンティティ

- [[Anthropic]] — Claude Memory Toolの開発元
- [[Cognition]] — Devinの独自メモリ実装、Anthropicの動向を注視
- [[OpenAI]] — ChatGPT自動メモリ、Codex
- [[Claude Code]] — Anthropicのコーディングエージェント

## 出典

- Shlok Khemani, "Anthropic's Opinionated Memory Bet" (2025-10-14) — https://www.shloked.com/writing/claude-memory-tool
- Shlok Khemani, "Claude Memory: A Different Philosophy" (2025-09-11) — https://www.shloked.com/writing/claude-memory
- ByteByteGo, "A Guide to Context Engineering for LLMs" — コンテキスト不安、要約、外部メモリの解説
