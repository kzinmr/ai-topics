---
title: Telegram Managed Bots
type: concept
created: 2026-04-27
updated: 2026-04-27
status: L2
sources: [https://core.telegram.org/bots/features#managed-bots, https://core.telegram.org/bots]
tags: [telegram, bots, managed-bots, platform-feature, bot-management]
---

# Telegram Managed Bots

Telegram Bot platformの**Managed Bots**機能は、1つのボットが他のボットを作成・管理・共有できるシステム。2025-2026年に正式導入され、Telegram Bot ecosystemの階層管理・マルチテナント化を可能にした。

## Core Concept

Managed Botsは、管理者ボット（manager bot）が下位ボット（managed bots）のライフサイクルを制御する機能。Telegram BotFather上で「Bot Management Mode」を有効化すると使用可能になる。

**主要特徴**:
- 管理者ボットが新規ボットを作成・管理・共有できる
- 共有URL形式: `https://t.me/newbot/{manager}/{new_username}?name={new_name}`
- 管理者は `getManagedBotToken` で各managed botのトークンにアクセス
- `managed_bot` 更新イベントでマネージャーボットに通知が来る
- 組織・チーム・SaaSプロバイダー向けのマルチテナントbot構築基盤

## Architecture

```
Manager Bot
    ├── Managed Bot A (token via getManagedBotToken)
    ├── Managed Bot B (token via getManagedBotToken)
    └── Managed Bot C (token via getManagedBotToken)
```

各managed botは独立したbotとして動作するが、トークン管理・設定・共有はmanager botを通じて行う。Telegram公式API経由で一元管理できる。

## Use Cases

| Use Case | Description |
|----------|-------------|
| **SaaS Multi-tenant** | 1つのmanager botで顧客ごとに個別botを生成・管理 |
| **Organization/team** | チームメンバーごとにアクセス権限付きbotを自動作成 |
| **Bot marketplace** | 公式/サードパーティbotの管理・デプロイメント基盤 |
| **White-label bots** | 企業ブランドごとにbotをカスタマイズして配布 |

## Related Features

Managed BotsはTelegram Bot platformの他の機能と組み合わせて使用される:

- **[Bot-to-Bot Communication](bot-to-bot-communication.md)** — bot同士の相互通信（infinite loop防止要件あり）
- **Mini Apps (Web Apps)** — JavaScriptベースのTelegram UI統合
- **Payments** — Telegram Starsを通貨としたデジタルトランザクション
- **Web Login** — ウィジェット/`login_url`による軽量認証

## Significance

Managed Botsは、Telegram Bot platformを単なるチャットボットフレームワークから**マルチテナントbot管理プラットフォーム**へ進化させた。SaaS企業や組織が、顧客/チームごとに個別化されたbotを効率的にデプロイ・管理できる基盤を提供する。特にAI agentプラットフォームとの統合（AI-powered support bots, AI content agentsなど）において、managed botsは重要なインフラストラクチャとなる。

## References

- [Telegram Bot Features — Managed Bots](https://core.telegram.org/bots/features#managed-bots)
- [Telegram Bot Platform Overview](https://core.telegram.org/bots)
- [Telegram Bot API Reference](https://core.telegram.org/bots/api)
