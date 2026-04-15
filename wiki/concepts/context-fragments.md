---
title: Context Fragments
created: 2026-04-16
updated: 2026-04-16
status: active
depth: L2
tags: [harness-engineering, memory, context-management, agent-design]
source: https://x.com/vtrivedy10/status/... (Vivek Trivedy, Apr 2026)
related:
  - harness-engineering
  - chatgpt-memory-bitter-lesson
  - claude-memory
  - ai-agent-memory-middleware
  - memory-systems-design-patterns
  - rlm-recursive-language-models
  - experiential-memory
---

# Context Fragments

Vivek Trivedy (@vtrivedy10) が2026年4月に提唱した概念。コンテキストウィンドウを「harnessが選択的にロードするオブジェクトの集合」として捉えるフレームワーク。

## 核心的な定義

> *"the context window is a precious artifact. Harnesses make decisions on how to populate, manage, edit, and organize it so agents can do work. Each loaded object can be thought of as a Context Fragment and represents an explicit decision by the user and harness designer of what needs a model needs to do work at any given time."*

### Context Fragmentとは

各Context Fragmentは：
- **明示的意思決定の産物** — ユーザーまたはharness設計者が「このデータは作業に必要」と判断してロードしたオブジェクト
- **自己完結的な意味単位** — ファイル、ドキュメント、メモリ、ツール定義など
- **動的に管理される** — harnessが追加・編集・削除・優先順位付けを行う

## 源流：RLMとExternalized Objects

このアイデアは [[rlm-recursive-language-models]] のAlex Zhang (@a1zhang) が提唱した「externalizing objects + loading into the context window」に由来する。RLMは「言語モデルは最終製品ではなく、プログラム内のモジュールである」というパラダイムを提示し、Context Fragmentsはその実装上の具体化と言える。

## Harnessの役割

Vivによるharnessの再定義：

| 従来のharness定義 | Context Fragments拡張 |
|-----------------|---------------------|
| Model + Tool routing | Model + Context Fragment routing + Memory retrieval |
| ツール呼び出しの管理 | どのオブジェクトをコンテキストにロードするか |
| エージェントの行動制御 | コンテキストの「編集・整理・優先順位付け」 |

## Experiential Memoryとの関係

> *"agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans)."*

Context Fragmentsは**Experiential Memory**（[[experiential-memory]]）の検索結果としてコンテキストウィンドウにロードされる。エージェント間のメモリ共有・フォーク・蓄積が可能になるため、個のエージェントの経験が集合知として再利用される。

## The Bitter Lessonとの接続

VivはRich Suttonの「Bitter Lesson」をエージェントメモリに適用する：

- **compute leveraged search > human-curated knowledge**
- 大量の経験データから検索・蒸留・整理する能力が競争優位になる
- オープンエコシステムが重要 — データの所有と利用

## Open Questions

Vivが提起した未解決の問い：

1. **Traces → Memory Primitives** — 経験（トレース）を効率的に蒸留し、長期的なメモリプリミティブにする方法
2. **JIT Search vs Weight Integration** — 検索はjust-in-timeか、モデル重みに統合すべきか
3. **Self-Managing Context** — モデルが自身のコンテキストウィンドウを自己管理する方法。再帰的外部オブジェクト操作時のエラー率低減

## 実装上の含意

### Harness Design

1. **Fragment selection policy** — どのオブジェクトをロードするか
2. **Fragment lifecycle** — 追加、編集、削除、圧縮
3. **Cross-fragment reasoning** — 複数フラグメントにまたがる推論
4. **Error recovery** — フラグメント操作失敗時のリカバリ

### Memory Architecture

- **L1: In-Context Fragments** — 現在の作業に必要なオブジェクト
- **L2: Local Memory Store** — セッション間で永続化されたフラグメント
- **L3: Shared Memory Pool** — エージェント間で共有・フォーク可能な蓄積メモリ

## Related Concepts

- [[harness-engineering]] — Harness Designの拡張版
- [[experiential-memory]] — エージェントの経験蓄積メモリ
- [[chatgpt-memory-bitter-lesson]] — Bitter Lessonとメモリ
- [[claude-memory]] — ファイルベースのメモリ（L2実装）
- [[ai-agent-memory-middleware]] — クラウドスケールのメモリ（L3実装）
- [[memory-systems-design-patterns]] — メモリ設計パターン横断分析
- [[rlm-recursive-language-models]] — 源流となったRLM/Externalized Objects
