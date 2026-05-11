---
title: "Skill Graph — 相互接続MarkdownファイルによるAIエージェントプレイブック"
type: concept
aliases:
  - skill-graph
  - content-skill-graph
  - スキルグラフ
created: 2026-05-11
updated: 2026-05-11
tags:
  - concept
  - skill-graph
  - content-engine
  - context-engineering
  - agent-media
status: active
sources:
  - "Ronin (@DeRonin_) — How To Build Own Content Engine? (FULL COURSE), April 2026"
  - "Linas Beliūnas — Skill Graphs: Fix Your AI Agent's Context Problem (Substack)"
---

# Skill Graph

相互接続されたMarkdownファイルのフォルダをAIエージェントの「プレイブック」として機能させるアーキテクチャ。各ファイルは1つの「知識ノード」であり、`[[wikilinks]]`で相互参照される。AIエージェントはエントリポイント（index.md）からリンクを辿って必要な知識ノードだけをコンテキストウィンドウにロードし、完全な理解を構築してからタスクを実行する。

## 核心理論

> "One flat .md file gives you a TOOL. A graph gives you a TEAM." — Ronin

> "The bigger the context, the worse the reasoning. Skill graphs solve this: most knowledge stays on disk. Only what matters enters the context window." — Linas Beliūnas

### 従来のプロンプト vs スキルグラフ

| アプローチ | 動作 | 結果 |
|-----------|------|------|
| **単一プロンプト** | 1つの指示、ゼロコンテキスト | 毎回「記憶喪失の天才」を雇うようなもの |
| **フラットファイル** | 1つの大きなリファレンス文書 | TOOL（単純な参照先） |
| **スキルグラフ** | 30+の相互接続.mdファイル | TEAM（プラットフォーム専門家、トーン適応、オーディエンス別対応） |

## アーキテクチャ

### 標準フォルダ構造（Roninの17ファイルモデル）

```
/content-skill-graph
├── index.md                  # コマンドセンター（エントリポイント）
├── platforms/                # プラットフォーム別プレイブック
│   ├── x.md                  # X/Twitter: 短形式、フック駆動、カジュアル小文字
│   ├── linkedin.md           # LinkedIn: 個人的ナラティブ、プロフェッショナル
│   ├── instagram.md          # Instagram: ビジュアル優先、カルーセル
│   ├── tiktok.md             # TikTok: 生の画面収録、2秒フック
│   ├── youtube.md            # YouTube: 深いチュートリアル、8-12分
│   ├── threads.md            # Threads: 会話的、意見駆動
│   ├── facebook.md           # Facebook: コミュニティ議論
│   └── newsletter.md         # Newsletter: 最も個人的、舞台裏
├── voice/                    # ブランドボイスDNA
│   ├── brand-voice.md        # 全プラットフォーム共通の核的人格
│   └── platform-tone.md      # プラットフォーム別のトーン適応
├── engine/                   # 運用エンジン
│   ├── hooks.md              # フックパターン（パフォーマンスの80%）
│   ├── repurpose.md          # 1アイデア→10プラットフォーム変換チェーン
│   ├── scheduling.md         # コンテンツカレンダー
│   └── content-types.md      # 形式定義（スレッド/カルーセル/動画/長文）
└── audience/                 # オーディエンスセグメント
    ├── builders.md           # 技術者向け
    └── casual.md             # 一般向け
```

### コアコンポーネント

#### index.md（コマンドセンター）
目次ではない。**ブリーフィング**である。以下を含む：
- **Identity**: 誰で、何をしているか（ニッチの具体性が最重要）
- **System Purpose**: このグラフが生成するもの
- **Node Map with Context**: `[[x]] — short-form, hook-driven, 280 chars max` のような文脈付きリンク
- **Execution Instructions**: ステップバイステップの実行手順

#### platform-tone.md（DNA適応層）
同じ人格を各プラットフォームの文化に適応させる「橋」。パーティーでの話し方 vs ビジネスディナー vs ポッドキャスト面接のような違い。

#### repurpose.md（変換チェーン）
**1つのアイデアが入り、10のプラットフォームネイティブ投稿が出る。再フォーマットではない、再思考である。**
チェーン順序: X → LinkedIn → Instagram → TikTok → YouTube → Newsletter → Threads → Facebook

**リトマス試験**:
> "If someone followed me on ALL platforms, would they be annoyed seeing the same thing everywhere?"
> If yes → reformatting. If no → 8 unique pieces from one idea.

## 運用方法

### Method 1: Claude Projects（推奨）
1. Projectを作成 → 全ファイルをアップロード
2. トピックを与える
3. Claudeがindex.mdを読み、wikilinksを辿り、接続ノードを読み、8つのプラットフォームネイティブ投稿を出力

### Method 2: コンテキスト貼り付け
- index.mdの内容を任意のAIチャットに貼り付け
- 実行指示を追加
- トピックを与える

### Method 3: Cursor / Claude Code（最も強力）
- グラフをローカルファイルシステムに保持
- エージェントが直接ファイルを読み取り・更新
- グラフ自体が時間とともに進化（hooks.mdの更新、platform-tone.mdの調整）

## 設計原則

| 原則 | 説明 |
|------|------|
| **Graph > Flat File** | 1つのフラット.md = TOOL。グラフ = TEAM |
| **Wikilinks as Navigation** | `[[wikilinks]]` でAIが研究者のように引用を辿る |
| **Platform-Native Repurposing** | 再フォーマットではなく再思考 |
| **Evolutionary Design** | 毎週hooks.mdを更新、パフォーマンスに基づいて改善 |
| **Compound Interest** | 学びをファイルにエンコードすることでシステムが賢くなる |

## Context Engineeringとの関係

スキルグラフはContext Engineering（[[concepts/harness-engineering/context-engineering]]）の**応用実装**である：

| Context Engineering概念 | スキルグラフでの対応 |
|------------------------|-------------------|
| 動的コンテキストローディング | Wikilinksによる選択的ノード読み込み |
| Attention Budget | 必要なノードだけをコンテキストにロード（大部分はディスク上） |
| 4ファイルアーキテクチャ（Khairallah） | voice/ + audience/ フォルダに展開 |
| JITコンテキスト | index.md→wikilinks→必要なノードの段階的発見 |
| 構造化メモ（Anthropic） | フォルダ構造そのものが永続的メモリシステム |

## Autoresearch Desk への応用

既存のwikiは既にスキルグラフである（構造化.md + `[[wikilinks]]`）が、**キュレーション用に最適化**されており、**配信用に最適化されていない**。

Autoresearch Desk化に必要な追加：
1. **index.mdの作成**: wikiの「コマンドセンター」 — エージェントが配信タスクを理解するためのブリーフィング
2. **platforms/フォルダ**: Discord / Slack / Telegram / X の各チャネル別プレイブック
3. **engine/repurpose.md**: wiki知識→マルチチャネル変換チェーン
4. **audience/フォルダ**: 技術実践者 / AI研究者 / プロダクトビルダー / 知識労働者

→ 詳細: [[concepts/agent-media]]

## 関連概念

- [[concepts/harness-engineering/context-engineering]] — Context Engineeringの技術的基盤
- [[concepts/agent-media]] — Autoresearch Desk: Wikiからマルチチャネル配信エンジンへ
- [[entities/ronin-deronin]] — Ronin: スキルグラフアーキテクチャの提唱者
- [[entities/khairallah-al-awady]] — Khairallah: 4ファイルアーキテクチャによる実践者フレームワーク
