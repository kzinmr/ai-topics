---
title: "Throw-Away First Draft Pattern"
aliases:
  - throw-away-draft
  - throwaway-first-draft
  - draft-compare-iterate
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - development-pattern
status: draft
sources:
  - "https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/"
---

# Throw-Away First Draft Pattern

エージェントに**最初に捨て台本（throw-away draft）を書かせ**、それを自分のメンタルモデルと比較してから、改めて反復する開発パターン。

## 核心原則

> *"Create branch, let CC build end-to-end, compare vs. mental model, then iterate with refined prompts."*
> — Sankalp

完璧な指示を出して一発で完成させるのではなく、**まずエージェントに自由に書かせて、その出力から学ぶ**。

## なぜ「捨て台本」を書くのか

### 1. メンタルモデルの検証

自分が思っていた仕様と、エージェントが理解した仕様の**ギャップを可視化**できる。

```
あなたのメンタルモデル    エージェントの出力
       ↓                        ↓
   「こうあるべき」    ←→    「こう実装された」
              ↓ ギャップを分析
         「どこが違ったか」を特定
              ↓
       修正した指示で再実装
```

### 2. 指示の精度向上

最初に書いたプロンプトが不正確だった場合、エージェントの出力を見ることで**どこが曖昧だったか**が明確になる。

### 3. 予期せぬ発見

エージェントは時として**人間が思いつかなかったアプローチ**を提案する。捨て台本によって、新しいアイデアを発見できる。

## 実践ステップ

### Step 1: 要件を明確化

```bash
# まずエージェントに質問して要件を固める
$ claude "What are the edge cases for this feature?"
```

### Step 2: ブランチを作成

```bash
$ git checkout -b draft/feature-x
```

### Step 3: エンドツーエンドで実装させる

```bash
# 最小限の指示でエージェントに自由に書かせる
$ claude "Implement feature X based on the requirements we discussed"
```

### Step 4: メンタルモデルと比較

```bash
# 差分を確認
$ git diff main
# テストを実行
$ python -m pytest tests/
```

### Step 5: 改善した指示で反復

```bash
# ギャップを分析して、より正確な指示を出す
$ claude "The date parsing is off. Use ISO 8601 format, not US format. Also, handle null cases explicitly."
```

### Step 6: 必要に応じてブランチを破棄

```bash
# エージェントのアプローチが完全に間違っていた場合
$ git checkout main
$ git branch -D draft/feature-x
# 新しいブランチでやり直し
$ git checkout -b draft/feature-x-v2
```

## Sankalpのワークフローとの関係

Sankalpは以下のようにツールを使い分けている：

| ツール | 役割 | Throw-Away Draftとの関係 |
|--------|------|------------------------|
| **Claude Code** | メインドライバー | 捨て台本の作成・反復 |
| **GPT-5.2-Codex** | レビュー・バグ発見 | 捨て台本の検証 |
| **Cursor** | 手動編集・リーディング | 最終調整 |

## 従来の開発との違い

| 従来の開発 | Throw-Away Draft |
|-----------|-----------------|
| 完璧な仕様書を先に書く | まずエージェントに書かせる |
| 一度に完成を目指す | 反復的に改善する |
| 人間がコードを書く | 人間は指示を書く |
| バグは後で見つかる | 最初からバグを前提とする |

## 注意点

### 捨て台本は「捨てる」ことが前提

- ブランチで隔離する
- mainにはマージしない（改善版を作る）
- エージェントの出力を鵜呑みにしない

### メンタルモデルとの比較が重要

- エージェントの出力を「正解」と思わない
- 自分の理解とどこが違ったかを分析する
- 違いから学ぶことで、次の指示が精密になる

## 関連概念

- [[context-window-management]] — 捨て台本はコンテキストを消費する
- [[cli-first-development]] — CLIで捨て台本を書くと検証が高速
- [[../agentic-engineering]] — 上位概念

## 参照

- [[sankalp]] — Throw-Away First Draftパターンの提唱者
- [A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
