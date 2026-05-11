---
title: "Agent Media — WikiからマルチチャネルAutoresearch Deskへの進化"
type: concept
aliases:
  - agent-media
  - autoresearch-desk
  - エージェントメディア
created: 2026-05-11
updated: 2026-05-11
tags:
  - concept
  - agent-media
  - skill-graph
  - context-engineering
status: active
description: "構造化知識ベース（wiki）を、audience-awareなマルチチャネル配信システムへ進化させる設計思想。KhairallahのContext Engineering + RoninのSkill Graphの統合。"
sources:
  - "Khairallah AL-Awady — How to Master Context Engineering (May 2026)"
  - "Ronin (@DeRonin_) — Skill Graph Content Engine (April 2026)"
  - "Hermes wiki自身の構造と配信パイプライン"
---

# Agent Media — Autoresearch Desk

**Agent Media**とは、構造化された知識ベース（wiki）をAIエージェントが「編集者」として運用し、複数チャネル・複数オーディエンスに**プラットフォームネイティブな形で知識を再配信する**システムの設計思想である。

従来のwikiは「人間が来て探す」プル型。Autoresearch Deskは「エージェントがオーディエンスに合わせて配信する」プッシュ型。

## 設計の源泉

Autoresearch Deskは2つの独立したフレームワークの交差点に成立する：

| フレームワーク | 提供するもの | 出典 |
|--------------|------------|------|
| **Context Engineering**（実践者視点） | 4ファイルアーキテクチャ、動的ローディング、メモリ進化ラダー、オーディエンス定義の必要性 | Khairallah AL-Awady |
| **Skill Graph**（実装視点） | フォルダ構造、wikilink遷移、repurpose chain、platform-native再思考、Litmus Test | Ronin (@DeRonin_) |

## 現在のWiki vs Autoresearch Desk

| 次元 | 現在のWiki | Autoresearch Desk |
|------|-----------|-------------------|
| **配信モデル** | プル型（人間が来て探す） | プッシュ型（エージェントが届ける） |
| **チャネル** | 単一（Discord） | マルチチャネル（Discord / Slack / Telegram / X） |
| **オーディエンス認識** | なし（全員に同じ情報） | セグメント別（技術深度/ビジネス/クイック） |
| **コンテンツ変換** | 生の更新通知 | プラットフォームネイティブ再構成 |
| **フィードバックループ** | なし | エンゲージメント追跡→配信最適化 |
| **index.md** | 存在するが配信用ではない | 配信エージェント用ブリーフィング |

## アーキテクチャ設計

### 提案フォルダ構造

既存のwiki構造に `agent-media/` レイヤーを追加する：

```
wiki/
├── concepts/          # 既存: 知識ノード
├── entities/          # 既存: 人物・組織ノード
├── raw/               # 既存: ソース記事
├── SCHEMA.md          # 既存: 品質基準（= Standards File）
├── index.md           # 既存: 全体インデックス（キュレーション用）
│
└── agent-media/       # NEW: 配信エンジンレイヤー
    ├── index.md                # コマンドセンター（配信エージェント用ブリーフィング）
    ├── voice/
    │   ├── brand-voice.md      # wikiの声：分析的・技術的正確・日本語/英語バイリンガル
    │   └── channel-tone.md     # チャネル別トーン適応
    ├── channels/               # チャネル別プレイブック
    │   ├── discord.md          # リアルタイム、技術深度、対話的
    │   ├── slack.md            # チーム向け、構造化、アクション指向
    │   ├── telegram.md         # ビルダー向け、示唆重視、リンクベース
    │   └── x.md                # パブリック、短形式、フック駆動
    ├── engine/
    │   ├── repurpose.md        # wiki知識→チャネル別変換チェーン
    │   ├── hooks.md            # チャネル別フックパターン
    │   └── scheduling.md       # 配信カレンダー（Daily Report等）
    └── audience/
        ├── practitioners.md    # 技術実践者（エージェント開発者）
        ├── researchers.md      # AI研究者
        ├── builders.md         # プロダクトビルダー（PM/起業家）
        └── knowledge-workers.md # 知識労働者（AI活用者）
```

### repurpose.md: Wiki知識→マルチチャネル変換チェーン

Roninのrepurpose chainを知識配信に適応：

```
1つのWiki更新（例: context-engineering概念ページの拡充）
    │
    ├─→ Discord: 技術的詳細 + コードレベル変更 + [[wikilinks]]
    │   "context-engineeringにKhairallahの4ファイルアーキテクチャを追加。
    │    動的コンテキストローディングの実装パターンは→ [[concepts/skill-graph]]"
    │
    ├─→ Slack: 構造化サマリー + アクションアイテム
    │   "📋 Context Engineering精緻化: 3層モデル、4ファイルアーキテクチャ、
    │    メモリ進化ラダーを追加。Autoresearch Desk設計に直接適用可能。"
    │
    ├─→ Telegram: 示唆 + リンク + ビジネス文脈
    │   "AIエージェントが「記憶喪失の天才」ではなくなる方法。
    │    Context Engineeringの実践フレームワークをwikiに統合しました。
    │    詳細→ [link]"
    │
    └─→ X: 短形式フック + 1インサイト
        "prompt engineering = syntax.
         context engineering = infrastructure.
         infrastructure beats syntax every single time.
         6週間でAIに「目」を与える方法をwiki化しました。"
```

### channel-tone.md: チャネル別トーン適応

| チャネル | トーン | 深度 | 長さ | 頻度 |
|---------|--------|------|------|------|
| **Discord** | 分析的・対話的・技術的正確 | 深い | 中〜長 | 更新発生時 |
| **Slack** | 構造化・プロフェッショナル・アクション指向 | 中 | 中 | Daily Report |
| **Telegram** | カジュアル・示唆重視・ビルダー向け | 浅〜中 | 短〜中 | 1-2/日 |
| **X** | 短形式・フック駆動・公的 | 浅い | 280-2000字 | 1-2/日 |

### hooks.md: チャネル別フックパターン

各チャネルの特性に合わせたフック：

| チャネル | 効果的なフック |
|---------|-------------|
| **Discord** | "新しい概念ページを拡充しました" / "〜の実装パターンを追加" |
| **Slack** | "📋 本日のWiki更新: [N]件" / "今週の重要トピック: [topic]" |
| **Telegram** | "AIが「目」を持つとはどういうことか" / "ほとんどの人が見落としている〜" |
| **X** | "prompt engineering is syntax. context engineering is infrastructure." |

## 実装ロードマップ

### Phase 1: Audience定義（今週）
- `agent-media/audience/` の4ファイル作成
- 各audienceの情報ニーズ、トーン期待値、チャネル選好を定義

### Phase 2: コマンドセンター（来週）
- `agent-media/index.md` の作成
- wikiのIdentity、配信目的、チャネルマップ、実行指示
- 既存のDaily Report cron jobにaudience別分岐の実験

### Phase 3: チャネルプレイブック（2週間以内）
- Discord / Slack / Telegram / X のチャネル別ファイル作成
- 既存の配信パイプラインをチャネル別テンプレートに移行

### Phase 4: フィードバックループ（1ヶ月以内）
- 各チャネルでのエンゲージメント追跡
- どのaudienceにどの情報が響いたかの学習
- hooks.md と channel-tone.md の継続的改善

## 設計原則

1. **Rethinking, not Reformatting** (Ronin): 同じ知識をチャネルごとに再思考。再フォーマットではない
2. **Context tells WHY/WHAT, Channels tell HOW, Schedule tells WHEN/WHERE** (Khairallah): MCP統合パターンの応用
3. **Litmus Test**: 「全チャネルをフォローしている人が同じものを見てうんざりするか？」 Yes→再フォーマットに過ぎない
4. **Evolutionary Design** (Ronin): 週次で改善。パフォーマンスデータをファイルにエンコード
5. **Memory Evolution Ladder** (Khairallah): Manual → Structured KB → Vector DB+RAG → **Autoresearch Desk**

## 関連概念

- [[concepts/skill-graph]] — 相互接続MarkdownによるAIエージェントプレイブック
- [[concepts/harness-engineering/context-engineering]] — Context Engineering（実践者フレームワーク含む）
- [[entities/khairallah-al-awady]] — Khairallah AL-Awady: 4ファイルアーキテクチャ提唱者
- [[entities/ronin-deronin]] — Ronin: Skill Graphアーキテクチャ提唱者
- [[concepts/memory-systems-design-patterns]] — AIエージェントのメモリ設計パターン
