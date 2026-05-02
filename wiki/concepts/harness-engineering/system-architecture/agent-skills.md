---
title: "Agent Skills (SKILL.md)"
type: concept
aliases:
  - agent-skill
  - skill-bundle
  - skilling
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - reusable-workflows
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
  - "https://openai.com/index/harness-engineering-leveraging-codex/"
  - "https://github.com/openai/skills"
related:
  - " — AIスキル（汎用概念）"
  - "[[concepts/harness-engineering]] — ハーネスエンジニアリング"
  - "[[concepts/harness-engineering/system-architecture/container-context]] — コンテナコンテキスト"
---

# Agent Skills (SKILL.md bundles)

エージェントが再利用可能なワークフローパターンを**SKILL.md bundles**としてパッケージ化する仕組み。同じマルチステップパターンを毎回再発見・再計画するコストを削減する。

## 問題意識

> "Shell commands are powerful, but many tasks repeat the same multi-step patterns. Agents have to rediscover the workflow each run — replanning, reissuing commands, and relearning conventions — leading to inconsistent results and wasted execution."

## SKILL.md 構造

```
skill-folder/
├── SKILL.md          # メタデータ + 手順説明
├── api-specs/        # API仕様書
├── ui-assets/        # UIスクリーンショット、CSS参照
└── scripts/          # 実行スクリプト（Python, bash等）
```

SKILL.mdには以下が含まれる:
- **メタデータ**: スキル名、説明、バージョン、対応モデル
- **手順**: エージェントが従うべきステップバイステップの指示
- **トリガー条件**: どのプロンプト/状況でこのスキルを適用すべきか

## スキル読み込みシーケンス（決定論的）

OpenAI Responses APIでのスキル適用は**3段階の決定論的プロセス**で動作する:

1. **スキルメタデータ取得**: 名前、説明、バージョン
2. **スキルバンドル取得**: コンテナにコピー、展開
3. **コンテキスト更新**: スキルメタデータとコンテナパスをモデルコンテキストに追加

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│ 1. メタデータ │ → │ 2. バンドル取得 │ → │ 3. コンテキスト │
│   取得        │    │   コンテナに  │    │   更新         │
│              │    │   コピー/展開  │    │              │
└─────────────┘    └──────────────┘    └──────────────┘
```

## スキルの探索的実行

モデルはスキルを読み込んだ後、**プログレッシブに探索**する:
- シェルコマンド（`ls`, `cat`等）でスキルファイルを確認
- 必要な情報だけを選択的に読み込み
- スクリプトをコンテナ内で直接実行

これは**人間の開発者がドキュメントを読んでツールを使う**のと同じパターン。

## バージョン管理

スキルは**バージョン付きバンドル**として管理:
- スキルIDで識別
- バージョン番号で追跡
- APIでアップロード・取得・更新

```python
# スキル付きコンテナの作成
skilled_container = client.containers.create(
    name="agent-with-skills",
    skills=[
        {"id": "skill_123", "version": "ver_20260311"}
    ]
)
```

## OpenAI harness engineeringとの関係

> "OpenAIはHarness Engineering（LLMをツールで拡張して特定タスクに固定）から、より汎用的なAI Agent Engineering（シェル+スキル+コンテナで自律的に複雑ワークフロー）へ移行している。"

- **Harness**: 固定ツール → 固定タスク（例: web search tool）
- **Skills**: 再利用可能ワークフロー → 複数タスクに適用可能

## ベストプラクティス

1. **スコープを狭く**: 1スキル = 1明確なワークフロー
2. **バージョンピン**: 本番では固定バージョン使用
3. **自己完結**: スキル内で必要な全リソースをバンドル
4. **段階的探索**: モデルが必要なファイルだけを選択的に読み込む設計

## 関連概念

- [[concepts/harness-engineering]] — OpenAIのツール拡張アプローチ
- [[concepts/harness-engineering/system-architecture/container-context]] — スキルが展開される実行環境
- [[concepts/agent-loop-orchestration]] — スキル探索と実行のループ
-  — AIスキルの汎用概念

## 参照

- [OpenAI: From model to agent](https://openai.com/index/equip-responses-api-computer-environment/)
- [[openai]] — OpenAI
