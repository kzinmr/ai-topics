---
title: "Agent Loop Orchestration"
type: concept
aliases:
  - agent-loop
  - orchestration-loop
  - responses-api-agent-loop
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - orchestration
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
  - "https://openai.com/index/harness-engineering-leveraging-codex/"
---

# Agent Loop Orchestration

LLMエージェントが自律的にタスクを完了させるための**実行ループ構造**。モデルがアクションを提案し、プラットフォームが実行し、結果をモデルにフィードバックする循環プロセス。

## 基本ループ

OpenAI Responses APIでの標準的なエージェントループ:

```
1. コンテキスト組み立て
   → ユーザープロンプト + 会話履歴 + ツール指示

2. モデルが次のアクションを決定
   → シェルコマンドを1つ以上提案

3. APIがコマンドをコンテナ内で実行
   → 分離された環境でコマンド実行

4. 出力をモデルにストリーミング
   → リアルタイムで結果をフィードバック

5. モデルが結果を検査
   → 追加コマンドを提案するか、最終回答を生成

6. ループ継続（モデルが追加コマンドを返さなくなるまで）
```

## 並列実行

モデルは**1つのステップで複数のシェルコマンドを提案**でき、Responses APIはそれらを**独立したコンテナセッションで並列実行**できる。

```
例: データ分析エージェント
├─ セッション1: grepでファイル検索
├─ セッション2: curlでAPIからデータ取得
└─ セッション3: 前回の結果を検証
    → 各セッションが独立して出力をストリーミング
    → APIが構造化ツール出力にマルチプレクス
```

## 出力キャップ

コマンドの出力はコンテキストウィンドウを急速に消費するため、**出力制限**が必須:

```text
text at the beginning ... 1000 chars truncated ... text at the end
```

- 先頭と末尾を保持、中間を切り捨て
- モデルが関連する結果に集中できるようノイズを削減
- ターミナルログの氾濫を防ぐ

## シェルツール vs Code Interpreter

| 機能 | Code Interpreter | Shell Tool |
|------|-----------------|------------|
| 言語 | Pythonのみ | Go, Java, Node.js, Unixユーティリティ |
| ユースケース | データ分析、スクリプト実行 | サーバー起動、API呼び出し、ファイル操作 |
| 柔軟性 | 限定的 | 幅広い（grep, curl, awk等） |
| 永続性 | セッション限り | コンテナファイルシステムで永続化 |

## OpenAI vs 他社アプローチ

| プラットフォーム | ループ管理 | 実行環境 | 出力制御 |
|----------------|-----------|---------|---------|
| **OpenAI Responses API** | ネイティブ（API内） | ホスト型コンテナ | 出力キャップ、ストリーミング |
| **Hermes (delegate_task)** | メインエージェント | 隔離ターミナルセッション | イテレーション制限 |
| **LangGraph** | カスタムグラフ | 開発者管理 | 開発者実装 |
| **Anthropic** | カスタムharness | 開発者管理 | 開発者実装 |

## OpenAI Responses APIの特徴

> "Instead of putting it on developers to build their own execution environments, we built the necessary components to equip the Responses API with a computer environment to reliably execute real-world tasks."

- **マネージド**: 開発者が独自の実行環境を構築する必要がない
- **ストリーミング**: リアルタイム出力でモデルが次の判断を動的に行える
- **並列**: 複数コマンドの同時実行で高速化
- **コンテキスト最適化**: 出力キャップでコンテキスト予算を保護

## 設計上の教訓

### ✅ ベストプラクティス
- プロンプトでシェルツールの使用を明示的に指示
- GPT-5.2以降のシェルトレーニング済みモデルを使用
- 出力キャップを常に設定
- 構造化されたツール出力でモデルの判断を支援

### ❌ アンチパターン
- 大きなファイルやテーブルをプロンプトに直接貼り付け（→ コンテキスト浪費）
- 出力制限なしでコマンド実行（→ ターミナルログ氾濫）
- ループ管理をクライアント側で実装（→ 開発者負担増）

## 関連概念

- [[concepts/harness-engineering/system-architecture/context-compaction]] — コンテキストが満杯になった際の圧縮メカニズム
- [[concepts/harness-engineering/system-architecture/container-context]] — 実行環境の永続化
- [[concepts/context-window-management]] — コンテキスト予算の戦略的管理
- [[concepts/harness-engineering]] — エージェント実行環境の設計（上位概念）

## 参照

- [OpenAI: From model to agent](https://openai.com/index/equip-responses-api-computer-environment/)
- [[openai]] — OpenAI
-  — Responses API（実装基盤）