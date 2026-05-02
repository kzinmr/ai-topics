---
title: "OpenClaw Ecosystem"
type: concept
aliases:
  - open-claw-ecosystem
  - openclaw
  - clawdbot
  - moltbot
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - ai-agents
  - open-source
  - robotics
  - ecosystem
status: complete
sources:
  - url: "https://openclaw.ai/"
    title: "OpenClaw Official Site"
  - url: "https://github.com/PlaiPin/rosclaw"
    title: "RosClaw — ROS2 Integration"
  - url: "https://medium.com/@mingyang.heaven/the-openclaw-ecosystem-architectural-deep-dive-into-4-ai-agent-frameworks-45eeb2276185"
    title: "The OpenClaw Ecosystem: Architectural Deep-Dive (Mingyang He, 2026)"
  - url: "https://evoailabs.medium.com/when-ai-gets-physical-hands-a-review-of-openclaw-on-the-unitree-g1-and-other-robots-0fbf06a1d4c8"
    title: "When AI Gets Physical Hands: OpenClaw on Unitree G1 (EvoAI Labs, 2026)"
---

# OpenClaw Ecosystem

**OpenClaw**（旧称 Clawdbot / Moltbot）は、**Peter Steinberger**（2026年に OpenAI に参画）が開発したオープンソースの AI エージェントプラットフォーム。Telegram、Discord、Signal、WhatsApp など 40 以上のメッセージングチャネルを統合し、LLM（Claude、DeepSeek、GPT など）が自律的にマルチステップの実世界タスクを実行できるようにする。

2026年現在、オープンソースコミュニティから生まれた 3 つの派生フレームワークを含む、活発なエコシステムを形成している。

## アーキテクチャ

```
ユーザー（WhatsApp/Telegram/Discord/Slack）
        ↓
OpenClaw Gateway（中央集約型 WebSocket Gateway）
        ↓
    AI Agent + Tools + Memory
        ↓
    RosClaw Plugin（ROS2 連携）
        ↓
    物理ロボット（Unitree G1 など）
```

### コアコンポーネント
- **TypeScript 実装**: 43万行以上のコード
- **40+ メッセージングチャネル統合**: Telegram、Discord、Signal、WhatsApp、Slack など
- **54+ ビルトインスキル**: メール、カレンダー、ホームオートメーション等
- **WebSocket Gateway**: 中央集約型のメッセージルーティング

## エコシステムの4つのフレームワーク

| フレームワーク | 哲学 | 言語 | 特徴 |
|--------------|-------|------|------|
| **OpenClaw** | 包括性（Comprehensiveness） | TypeScript | 430K LoC、フル機能、ゲートウェイアーキテクチャ |
| **Nanobot** | 極限ミニマリズム | — | 最小構成、軽量 |
| **ClawWork** | 経済的説明責任 | — | タスクの経済的制約・コスト管理 |
| **ZeroClaw** | ハードウェアレベルのパフォーマンス | Rust | 低レイテンシ、ハードウェア最適化 |

## ロボティクス連携

OpenClaw は物理ロボットの制御にも拡張されている：
- **RosClaw**: ROS2 ブリッジプラグイン（rosbridge_server + WebSocket）
- **Unitree G1**: 四足歩行ロボットの制御
- **Reachy Mini**: ヒューマノイドプラットフォームの制御
- **ゼロコードロボティクス**: AI が「何を」するかを理解し、「どうやって」は自動解決

### マルチエージェントロボット協調
Chris Dietrich が提唱するビジョン：
- 複数のロボットインスタンスが協調してタスクを実行
- Signal/WhatsApp/Web インターフェースを横断した通信
- 知覚データの共有とタスク交渉

## セキュリティとガバナンス

- **サンドボックスセキュリティ**: コード実行の隔離
- **Durable Task Flow**: 2026.4.2 リリースで導入された耐久性のあるタスクオーケストレーション
- **プラグインアクティベーション境界**: 厳格な権限制御

## エンタープライズ応用

OpenClaw の自律エージェント能力は、特に以下の分野で注目されている：
- **ヘルスケア**: ワークフロー自動化、コンプライアンス対応
- **RPA**: 従来の RPA の AI 拡張
- **カスタマーサポート**: マルチチャネル自動応対

## 関連概念

- [[concepts/agent-orchestration-frameworks]] — エージェントオーケストレーション比較
- [[concepts/agent-swarms]] — マルチエージェント創発的振る舞い
- [[concepts/telegram-managed-bots]] — Telegram ボットエコシステム
- [[concepts/monty-sandbox]] — コード実行サンドボックス

## ソース

- [OpenClaw Official Site](https://openclaw.ai/)
- [OpenClaw Ecosystem Deep-Dive](https://medium.com/@mingyang.heaven/the-openclaw-ecosystem-architectural-deep-dive-into-4-ai-agent-frameworks-45eeb2276185)
- [OpenClaw + Robotics](https://www.openclawrobotics.com/)
- [OpenClaw on Unitree G1](https://evoailabs.medium.com/when-ai-gets-physical-hands-a-review-of-openclaw-on-the-unitree-g1-and-other-robots-0fbf06a1d4c8)
