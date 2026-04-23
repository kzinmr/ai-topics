---
title: "CLI-First Development"
aliases:
  - cli-first-development
  - cli-first-agents
  - command-line-first
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - development-workflow
status: draft
sources:
  - "https://steipete.me/posts/2025/shipping-at-inference-speed"
  - "https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/"
---

# CLI-First Development

ソフトウェア開発を**CLI（コマンドラインインターフェース）から始める**アプローチ。エージェント時代の開発ワークフローの核心パターン。

## 核心原則

> *"Most apps are data pipelines. Starting with a CLI allows agents to execute, verify output, and close the feedback loop without UI overhead."*
> — Peter Steinberger

UIから始めるのではなく、まずCLIでコアロジックを構築し、エージェントが即座に実行・検証できる環境を作る。

## なぜCLI-Firstなのか

### 1. フィードバックループの高速化

| 開始点 | エージェントの実行 | 検証方法 | フィードバック速度 |
|--------|------------------|----------|------------------|
| **CLI** | 即座に実行可能 | 標準出力・終了コード | 数秒 |
| **Web UI** | ブラウザ操作が必要 | 視覚的確認 | 数分 |
| **Mobile App** | シミュレーター/実機 | UIテスト | 数十分 |

### 2. エージェントとの相性

- CLIは**構造化された入出力**を持つ → エージェントが理解しやすい
- テスト自動化が容易 → エージェントが自己検証できる
- バッチ処理・パイプライン化 → 並列実行が可能

### 3. 認知負荷の削減

UIの細かい調整（パディング、色、レイアウト）に時間を取られることなく、**ロジックの正確性**に集中できる。

## Sankalpの実践：CC → Codex → Cursor

Sankalpは以下のようにツールを使い分けている：

```
Claude Code (CC)  →  メインドライバー。CLIベースで高速実装
     ↓
GPT-5.2-Codex     →  レビュー・バグ発見。P1/P2の深刻度タグ付け
     ↓
Cursor            →  手動編集・コードリーディング
```

このパイプラインはCLI-firstの思想を反映している：
1. CCでCLIから実装を開始
2. Codexでバグを自動発見
3. 必要に応じてCursorで手動修正

## Steipeteの実践：言語選択

| 用途 | 言語 | 理由 |
|------|------|------|
| **CLI** | Go | シンプルな型システム、高速なリンティング、エージェントが扱いやすい |
| **Web** | TypeScript | 豊富なエコシステム、エージェントの学習データが多い |
| **macOS/UI** | Swift | Xcodeは不要。Swift build + Codexでシミュレーター操作 |

## 実践パターン

### パターン1: CLIプロトタイプ → Web拡張

```bash
# 1. CLIでコアロジックを構築
$ python cli_tool.py --input data.json --output result.json

# 2. エージェントがCLIを検証・修正
$ claude "Fix the date parsing in cli_tool.py"

# 3. Web UIは後に追加
$ claude "Build a web frontend for cli_tool.py using FastAPI"
```

### パターン2: テスト駆動CLI開発

```bash
# 1. テストを書く
$ claude "Write tests for the data processing pipeline"

# 2. CLIで実行
$ python -m pytest tests/ -v

# 3. 合格したらWeb UIに拡張
```

### パターン3: バックグラウンドタスク委任

```bash
# メインエージェントがCLIタスクをバックグラウンドで実行
$ claude --background "Run the full test suite and report failures"
# 別の作業を継続しながら、完了したら通知を受ける
```

## UIは「最後に」触る

CLI-firstのアプローチでは、UIは以下の理由で最後に触る：

1. **UIは主観的**：パディング1pxの違いに議論する時間はもったいない
2. **UIは変更容易**：ロジックが固まってからUIを作れば、手戻りが少ない
3. **エージェントはCLIが得意**：構造化された入出力を扱う方が正確

> *"Building software is like walking up a mountain. You don't go straight up, you circle around it and take turns, sometimes you get off path and have to walk a bit back, and it's imperfect, but eventually you get to where you need to be."*
> — Peter Steinberger

## 関連概念

- [[agent-first-design]] — エージェント向けコード設計
- [[context-window-management]] — CLIはコンテキスト消費が少ない
- [[agentic-engineering]] — 上位概念

## 参照

- [[steipete]] — CLI-first開発の提唱者
- [[entities/sankalp-sinha.md]] — CC → Codex → Cursorのパイプライン実践者
- [Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
- [A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
