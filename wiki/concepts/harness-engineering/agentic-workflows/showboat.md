---
title: "Showboat"
type: concept
aliases:
  - showboat
  - agent-documentation-tool
created: 2026-04-12
updated: 2026-04-12
tags:
  - tool
  - agentic-engineering
  - documentation
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/"
---

# Showboat

Simon Willisonが開発した、**コーディングエージェントに「自分の作業を示させる」ためのドキュメンテーション/成果物生成ツール**。

## 目的

> "Forces agents to 'show their work' by creating verifiable, auditable testing artifacts."

エージェントの推論・テスト・実装プロセスを、検証可能なMarkdownドキュメントとして記録する。

## 主要コマンド

| コマンド | 説明 |
|----------|------|
| `showboat note` | Markdownの観察記録を追加 |
| `showboat exec` | **最も重要。** 実行したコマンドとその出力を記録。ハルシネーションを防止 |
| `showboat image` | スクリーンショットをキャプチャ（Rodneyと連携してUI検証に使用） |

### `showboat exec` の重要性
> "Records the exact command run + its output. Prevents hallucination by proving what actually happened."

エージェントが「何を実行したか」を虚偽報告するのを防ぐ。実際の出力をドキュメントに埋め込むため、後から検証可能。

## CLI設計哲学

> "Design CLIs for agents. Structure `--help` outputs to be self-documenting for LLMs."

Showboatの `--help` 出力は、LLMがツールを即座に理解・使用できるよう構造化されている。これは**エージェントファーストCLI設計**の典型例。

## 使用例

### Linear Walkthrough
```
Read the source and then plan a linear walkthrough of the code that explains how it all works in detail.
Then run "uvx showboat --help" to learn showboat - use showboat to create a walkthrough.md file in the repo
and build the walkthrough in there, using showboat note for commentary and showboat exec plus sed or grep
or cat or whatever you need to include snippets of code you are talking about.
```

→ このプロンプトで、Claude Codeは6つのSwiftファイルを詳細に解説するドキュメントを自動生成。

### APIドキュメンテーション
```
Run `uvx showboat --help` and then create a `notes/api-demo.md` showboat document and use it to test and document that new API.
```

## 関連ツール

- [[concepts/harness-engineering/agentic-workflows/rodney]] — ブラウザ自動化CLI（Showboatと連携してスクリーンショット撮影）
-  — SwiftUIスライドアプリ（Showboatでコード解説を生成）

## 関連概念

- [[concepts/agentic-manual-testing]] — Showboatの主要ユースケース
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — コード解説生成パターン
- [[concepts/harness-engineering/agentic-engineering]] — 上位概念

## 参照
- [[simon-willison]] — 開発者
