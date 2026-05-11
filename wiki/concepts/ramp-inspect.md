---
title: "Ramp Inspect (Background Coding Agent)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags:
  - coding-agents
  - ai-agents
  - sandbox
  - infrastructure
  - developer-tooling
sources:
  - "[[raw/articles/2026-05-xx_ramp_background-agent-inspect]]"
related:
  - "[[concepts/background-agents]]"
  - "[[concepts/autonomous-agents]]"
  - "[[concepts/closing-the-software-loop]]"
  - "[[entities/ramp]]"
---

# Ramp Inspect (Background Coding Agent)

Rampが内製した**バックグラウンドコーディングエージェント**「Inspect」。通常のコーディングエージェントの能力に加え、**作業検証のループを自律的に閉じる**点が特徴。

## 主要指標

- **導入率**: 全PRの約30%がInspectによって作成（わずか数ヶ月で到達）
- **実行環境**: ModalサンドボックスVM（Vite, Postgres, Temporal完備）
- **対応モデル**: 全フロンティアモデル、MCP、カスタムツール対応
- **インターフェース**: Slack、Chrome拡張、Web、VS Code、Pull Request — すべて双方向同期

## アーキテクチャ

### サンドボックス（Modal）

```
Image Registry → 30分ごとにビルド
  ├── リポジトリクローン
  ├── 依存関係インストール
  └── Snapshot保存

セッション開始 → SnapshotからVM即起動 → 即作業開始
```

- GitHub App認証（ユーザー非依存）
- git configのuser.name/emailはセッション開始時に設定

### 検証ループ

通常のコーディングエージェントとの決定的な違い:

| 通常のエージェント | Inspect |
|-------------------|---------|
| コード生成のみ | コード生成 + **自律検証** |
| テスト実行は明示的指示が必要 | 自動テスト実行 |
| 動作確認は人が行う | スクリーンショット + ライブプレビューで自律確認 |
| コンテキスト不足で制限 | Sentry, Datadog, LaunchDarkly, Braintrust, GitHub, Slack, Buildkiteに接続 |

### マルチモーダルインターフェース

- **Slack**: スクリーンショットを送ってチャット
- **Chrome拡張**: ページ要素をハイライトして変更指示
- **Webインターフェース**: ブラウザで会話
- **Pull Request**: PR上でディスカッション
- **WebベースVS Code**: 手動編集が必要な場合
- **全セッションはマルチプレイヤー**: 同僚にセッションURLを送るだけで共同作業

## 設計思想

> 「セッション速度はモデルプロバイダーのTTFTのみに制限されるべき。それ以外（クローン、インストール）はセッション開始前に完了させる。」

- **無制限の並行セッション**: 同じプロンプトで複数バージョンを試行し、最も成功したものを選択
- **アイデアの即時キャプチャ**: 夜にバグを見つけたら → Slackでセッション開始 → 朝にPR確認
- 音声入力対応

## 参照

- [Why We Built Our Background Agent — Ramp Builders](https://builders.ramp.com/post/why-we-built-our-background-agent)
- [Modal Sandboxes](https://modal.com/docs/guide/sandboxes)
