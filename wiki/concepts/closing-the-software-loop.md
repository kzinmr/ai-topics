---
title: "Closing the Software Loop"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [agentic-engineering, coding-agents, autonomous-agents, workflow, software-engineering, ai-adoption]
sources:
  - "[[raw/articles/2026-01-25_benedict_closing-software-loop]]"
related:
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/autonomous-agents]]"
  - "[[concepts/background-agents]]"
---

# Closing the Software Loop

Benedict Brady（Meridian）が提唱する、**自律的なソフトウェア改善ループ**の概念。Andrej Karpathyの「Teslaの自動運転チームが休暇に行っても車が改善し続ける」というビジョンに触発された。

## ソフトウェア開発ループの進化

### フェーズ1: 従来型（数日〜数週間/反復）

```
ユーザーフィードバック → プロダクトチームが仕様化 → 
エンジニアが実装 → コードレビュー → デプロイ
```

### フェーズ2: エージェント支援型（数時間〜数日/反復）

```
ユーザーフィードバック → プロダクトチームが仕様化 → 
コーディングエージェントが実装（ overnight） → 人間がレビュー
```

- 週単位の機能が overnight で実装可能に
- プロダクトチームは**詳細な仕様とバグボード**の維持が重要に
- エージェントに**実験室（Laboratory）**を与える: ログ検査、dev環境デプロイ、ブラウザ/モバイルシミュレーター

### フェーズ3: フル自己改善型（未来）

```
自律的バグ検出 → 自律的仕様化 → 自律的実装 → 自律的レビュー → デプロイ
```

**不足しているピース**: 自律的なバグ報告生成と機能要求の理解

#### データ収集の道筋

| 手段 | 説明 | 例 |
|------|------|-----|
| テレメトリ | レガシーシステムのログからバグを自動検出・バグボード化 | Datadog, Sentry |
| チャット製品 | ユーザーのチャットでの機能要求を仕様化 | Meridianの投資戦略リクエスト |
| 自律インタビュー | エージェントがユーザーインタビューを実施 | Listen Labs |

## Meridianでの実践例

「BTCを$75k以下の時だけ毎週$100購入」というユーザー要求:
- 従来: プロダクトチームが仕様化 → エンジニアが価格監視サービスを実装 → 数週間
- エージェント支援型: 詳細仕様をエージェントに与え複数実装案を試行 → 数日

## 人間の役割の変化

| 役割 | 従来 | Closed Loop |
|------|------|------------|
| プロダクトマネージャー | 仕様作成 | 自律生成された仕様の検証・優先順位付け |
| エンジニア | 実装 | アーキテクチャ設計 + エージェントのコードレビュー |
| QA | テスト | エージェントのテスト戦略監査 |

## 参照

- [Closing the Software Loop — Benedict Brady](https://www.benedict.dev/closing-the-software-loop) (2026-01-25)
- [Give your agent a laboratory — Brian Lovin](https://brianlovin.com/writing/give-your-agent-a-laboratory-jH5ryjC)
