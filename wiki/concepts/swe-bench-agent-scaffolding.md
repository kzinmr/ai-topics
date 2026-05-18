---
title: "SWE-bench Agent Scaffolding (Claude 3.5 Sonnet)"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - benchmark
  - architecture
  - anthropic
  - evaluation
  - coding-agents
aliases:
  - SWE-bench Sonnet agent
  - minimal agent scaffold
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_swe-bench-sonnet.md
  - https://www.anthropic.com/engineering/swe-bench-sonnet
related:
  - swe-bench
  - agent-harnesses
  - coding-agents
  - building-effective-agents
---

# SWE-bench Agent Scaffolding (Claude 3.5 Sonnet)

Claude 3.5 SonnetがSWE-bench Verifiedで49%を達成（当時のSOTA 45%を更新）した際のエージェント設計。**「可能な限りモデル自身に制御を委ね、 scaffoldingを最小限に」** という設計哲学。

## Agent アーキテクチャ

### コンポーネント
- **Prompt**: 提案アプローチを示唆するが、過度に長く/詳細すぎない
- **Bash Tool**: シェルコマンド実行（スキーマはシンプル、説明に重み）
- **Edit Tool**: ファイル・ディレクトリの閲覧と編集
- **Loop**: モデルが「完了」と判断するか200kコンテキスト長を超えるまで継続

### 設計哲学

> ハードコードされた特定パターンやワークフローに従わせるのではなく、モデル自身の判断で問題解決の方針を選択させる。

### Prompt

```
<uploaded_files>{location}</uploaded_files>
I've uploaded a python code repository in the directory {location}.
Consider the following PR description:
<pr_description>{pr_description}</pr_description>

Follow these steps to resolve the issue:
1. Explore the repo to familiarize yourself with its structure.
2. Create a script to reproduce the error and execute it
3. Edit the sourcecode of the repo to resolve the issue
4. Rerun your reproduce script and confirm that the error is fixed!
5. Think about edgecases and make sure your fix handles them as well

Your thinking should be thorough and so it's fine if it's very long.
```

### Bash Tool設計

シンプルなスキーマ（コマンド文字列のみ）だが、descriptionで詳細な指示:
- 入力のエスケープ
- インターネット非接続の明示
- バックグラウンド実行方法
- 長時間実行コマンドへの対処

## 重要な洞察

> SWE-benchはモデル単体ではなく、**エージェントシステム全体**を評価する。同じモデルでもscaffolding次第で性能が大きく変わる。

オープンソース開発者やスタートアップが、同一モデル周りのscaffolding最適化で大きな改善に成功している（[[agent-harnesses|Harness Effect]]）。

## SWE-bench vs SWE-bench Verified

| | SWE-bench | SWE-bench Verified |
|---|---|---|
| 問題数 | 2,294 | 500 |
| 品質 | GitHub issue外の追加コンテキストが必要な問題を含む | 人間レビュー済み、解決可能な問題のみ |
| 用途 | 広範な評価 | 明確なコーディングエージェント性能測定 |

## 結果

- Claude 3.5 Sonnet (upgraded): **49%** on SWE-bench Verified
- 前SOTA: 45%
- 「50%を超えたモデルはまだない」状態を突破目前

## See Also

- [[concepts/swe-bench]] — SWE-bench benchmark overview
- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
- [[agent-harnesses]] — Agent harness comparison
- [[concepts/building-effective-agents]] — Building effective agents (Anthropic)
- [[concepts/coding-agents]] — Coding agents overview
