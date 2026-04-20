---
title: "Personal Superintelligence — パーソナルAIの進化と哲学的対立"
aliases:
  - personal-ai-agents
  - personal-superintelligence
  - ambient-computing-agents
  - context-aware-ai
created: 2026-04-15
updated: 2026-04-15
tags:
  - concept
  - front-page
  - personal-ai
  - synthesis
  - ambient-computing
  - data-sovereignty
status: active
---

# Personal Superintelligence — パーソナルAIの進化と哲学的対立

**「AIは中央で全てを自動化するべきか、それとも個人それぞれが自分の目標に向かう道具となるべきか。」**

2025年後半から2026年にかけて、AI業界で最も重要な哲学的分岐が表面化している。それは**「superintelligenceの行き先」**をめぐる対立である。

## 二つのビジョン

```
Central Automation (OpenAI/Anthropic/Google)
    AIが全ての仕事を自動化
    → 人間はその配分を受ける

Personal Empowerment (Meta/OpenClaw/Local AI)
    個人がAIを自分の目標に向ける
    → 人間が主体性を持つ
```

## 主要プレイヤー別アプローチ

| プレイヤー | 実現方法 | データ主権 | 哲学 |
|---|---|---|---|
| [[meta]] | Muse Spark + Ray-Ban AI Glasses | Metaクラウド | 「Personal superintelligence for everyone」 |
| [[peter-steinberger]] | OpenClaw/Claudbot | ユーザーローカル | 「You own your agent」 |
| [[shlok-khemani]] | OpenPoke/Vajra | Filesystem-first | 「Personality ≠ Execution」 |
| [[george-hotz]] | tinygrad + local inference | フリー | 「All compute is equal」 |
| [[mario-zechner]] | pi coding agent | ローカル | 「Strip away the bloat」 |
| [[sero]] | Open Orchestra/Thrive | ローカル+分散 | 「Freedom Tech」 |

## 3つの哲学的分岐点

### ① データ主権 — 「who knows you?」

> *"Personal superintelligence that knows us deeply, understands our goals, and can help us achieve them will be by far the most useful."*
> — Mark Zuckerberg, July 2025

Zuckerbergの言う「knows us deeply」は、Metaのプラットフォーム上にユーザーデータを集約するモデル。対照的に、[[shlok-khemani]]はファイルベースのメモリ（CLAUDE.md、`.agent/`ディレクトリ）を提唱し、**ユーザーが自分のデータを直接管理・可視化できること**を重視する。

| アプローチ | 長所 | 懸念 |
|---|---|---|
| **プラットフォーム集約** (Meta) | 豊富なコンテキスト、シームレス統合 | データロックイン、プライバシー |
| **Filesystem-first** (Khemani/Anthropic) | 透明性、ポータビリティ、Git管理 | 設定コスト、ユーザー負担 |
| **ローカル完全分離** (OpenClaw/Sero) | 完全なデータ主権 | モデル制約、インフラ自己管理 |

### ② ハードウェア — 「where does the agent live?」

Metaは **Ray-Ban AI Glasses** を「primary computing device」と位置づける。2025年に700万台以上を販売、2026年には年間2000-3000万台の製造能力を目標とする。VisionClaw（Xiaoan Sean Liu）はRay-Ban Meta + Gemini Live API + OpenClawを組み合わせ、「what you see/hear」を理解するエージェントの実現を実証した。

対照的に、ローカルAIコミュニティは **既存のハードウェア**（consumer GPU、Apple Silicon）上での実行を志向する。[[georgi-gerganov]] の llama.cpp、[[mario-zechner]] の pi エージェントはいずれも「特別なデバイス」を必要としない。

### ③ オープン vs クローズド — 「who controls the model?」

MetaのMuse Spark（2026年4月発表）は**closed-source**。Llama系列のオープン哲学からの断裂がコミュニティで指摘されている（"rip LLaMA"）。一方、[[anthropic-openclaw-conflict]] で見られたように、Anthropicもまたサードパーティエージェントをサブスクリプションから排除する方向に動いている。

**皮肉な収束**: Meta（オープン源流）とAnthropic（元々クローズド）が、異なる理由で同じ「プラットフォーム制御」の方向に進んでいる。

## 重要トレンド（2026年）

### 1. VisionClawパターン — ウェアラブル×エージェント

2026年2月、開発者Xiaoan Sean Liuが **VisionClaw** を発表。Meta Ray-Ban Glasses + Google Gemini Live API + OpenClawフレームワークを組み合わせ、**「画面もキーボードもない」** エージェント体験を実証。

```
Sensory Input (glasses camera/mic)
    → Cloud Cognition (Gemini Live API, WebSocket)
        → Local Execution (OpenClaw function calls)
            → Real-world actions
```

これはMetaの「glasses that understand our context」ビジョンを**コミュニティ主導で先取り**した実装。

### 2. Agentic Shopping — Metaの商業戦略

Zuckerbergは2025年Q4決算で「AI-driven commerce」を強調。Instagram/WhatsApp上のエージェントが商品発見〜購入を代行するモデル。Metaの個人データ（興味、関係性、購買履歴）を最大限に活用する戦略。

### 3. Infrastructure Spend War

Metaは2026年に **$115B-$135B** の設備投資を計画。VR/Reality Labs投資を削減し、AIグラスと基盤モデルに集中。これは「metaverse failed, superintelligence next」のシフトを意味する。

### 4. Data Sovereignty Movement

OpenClawコミュニティ、Seroの「Freedom Tech」、ローカルLLM愛好家は**「ユーザーが自分のエージェントとデータを所有する権利」** を主張。[[anthropic-openclaw-conflict]] はこの運動の転換点となった。

## 概念マップ

```
Personal Superintelligence
├── Central Automation (OpenAI/Anthropic/Google)
│   ├── Platform-controlled agents
│   ├── Subscription economics
│   └── Closed model access
│
├── Personal Empowerment (Meta/OpenClaw/Local)
│   ├── Wearable-first (Ray-Ban, VisionClaw)
│   ├── Filesystem-first (CLAUDE.md, OpenPoke)
│   └── Local-first (llama.cpp, pi, Open Orchestra)
│
└── Key Tensions
    ├── Data ownership: Platform vs User
    ├── Hardware: Glasses vs Existing devices
    ├── Models: Closed vs Open source
    └── Economics: Subscription vs Self-hosted
```

## 定点ウォッチ対象

### 四半期チェック項目
1. **Meta製品展開** — Muse Spark API公開、Ray-Ban AI機能追加、Agentic Shoppingローンチ
2. **OpenClawエコシステム** — OpenAI統合後の方向性、サードパーティツールアクセス
3. **ローカルAI** — llama.cppの新機能、piエージェントの進化、Gemma 4 on-device
4. **規制・プライバシー** — ウェアラブルAIの法的枠組み、データ主権立法
5. **業界対立** — Anthropic vs OpenClawの解決、Googleのサードパーティポリシー

### 要監視プレイヤー
- **[[meta]]** — Personal Superintelligenceビジョンの実行
- **[[peter-steinberger]]** — OpenAIでのpersonal agent開発
- **[[shlok-khemani]]** — ファーストパーソンAIのアーキテクチャ
- **[[sero]]** — Freedom Tech / ローカルインフラ
- **[[mario-zechner]]** — Minimal agent on consumer hardware
- **[[george-hotz]]** — Open source GPU driver / tinygrad

## 関連コンセプト

- [[death-of-browser]] — ブラウザの脱人間化（エージェントがUIを操作）
- [[anthropic-openclaw-conflict]] — プラットフォーム制御 vs オープンアクセス
- [[open-claw-ecosystem]] — OpenClawとパーソナルAIエージェント運動
- [[meta-muse-spark]] — Muse Sparkモデル詳細
- [[local-llm]] — ローカルLLM推論
- [[harness-engineering/agentic-workflows/_index]] — エージェント活用開発パターン
- [[cache-first-engineering]] — プロンプトキャッシュ最適化
- [[ai-privacy-tools]] — AIエージェントのプライバシー課題

## 関連エンティティ

- [[meta]] — Personal Superintelligence提唱
- [[mark-zuckerberg]] — Meta CEO、ビジョン策定
- [[alexandr-wang]] — Meta Superintelligence Labs責任者
- [[peter-steinberger]] — OpenClaw創設者
- [[shlok-khemani]] — パーソナルAIメモリの研究者
- [[sero]] — Freedom Tech / ローカルAIインフラ
- [[mario-zechner]] — ローカルLLMエンジニアリング
- [[george-hotz]] — オープンソースAIハードウェア

## Sources

- [Meta: Personal Superintelligence (Zuckerberg, July 30, 2025)](https://www.meta.com/superintelligence/)
- [VisionClaw: Turning Ray-Ban Meta Glasses into an Autonomous Super-Agent (Elluminate Me, Feb 2026)](https://elluminateme.com/artificial-intelligence/visionclaw/)
- [Meta's Ray-Ban Display turns AI agents into a hands-free OS (The Relay, 2025)](https://therelaymag.com/metas-ray-ban-display-turns-ai-agents-into-a-hands-free-os/)
- [Meta Positions AI Glasses and Personal Agents at Center of Growth (AI Insider, Jan 2026)](https://theaiinsider.tech/2026/01/29/meta-positions-ai-glasses-and-personal-agents-at-the-center-of-its-next-growth-phase/)
- [Anthropic-OpenClaw Conflict (Apr 2026)](~/wiki/concepts/anthropic-openclaw-conflict.md)
- [Shlok Khemani — Personal AI Research](~/wiki/entities/shlok-khemani.md)
