---
title: "Hierarchy to Intelligence — Blockの組織モデル変革"
aliases:
  - block-hierarchy-to-intelligence
  - jack-dorsey-org-model
  - ai-native-organization
created: 2026-04-13
updated: 2026-04-15
tags:
  - concept
  - organization
  - block
  - jack-dorsey
  - ai-native
  - ai-native-organization
status: draft
depth_tracking:
  target: 10KB+
  current: ~10KB
---

# Hierarchy to Intelligence — Blockの組織モデル変革

## 概要

Jack Dorseyが2024年にBlock（旧Square）で実践した**Hierarchy to Intelligence**モデル。従来のヒエラルキー型意思決定を廃し、**「文脈駆動の自律実行 + 透明性ベースの監視」**への移行を宣言。AIを単なる生産性向上ツールではなく、**「協調メカニズムそのものの再設計」**として捉える。

> *"Most companies are focused on AI as a productivity enhancer. Few are focused on the potential of AI to change how we work together."*

## AIの真のポテンシャル

Blockの主張: AIは既存ワークフローを効率化する「コパイロット」ではなく、**中間管理の情報をルーティングする機能を代替する協調メカニズム**として機能する。

## 階層の歴史 — なぜヒエラルキーが生まれたか

組織の階層構造は技術的制約の産物だった:

| 時代 | イノベーション | 中核機能 |
|------|--------------|---------|
| **ローマ軍** | 階層型編成 (`contubernium` → `century` → `cohort` → `legion`) | 限られた通信手段での遠距離協調 |
| **プロイセン (1806)** | 参謀本部 | 事前計算された決定、情報ルーティング、line vs staffの形式化 |
| **米国鉄道 (1850s)** | 最初の組織図 (Daniel McCallum) | 軍事階層の商業化。大規模衝突防止 |
| **テイラー主義** | 科学的管理法 | タスクの専門化・測定 → 機能別ピラミッド |
| **戦後** | マトリクス組織 & 7Sフレームワーク | 中央基準と地方の俊敏性のバランス |
| **テック時代** | スクワッド、ホラクラシー、フラット構造 | 大規模化で失敗。情報ルーティングの限界により階層に回帰 |

> *"The structure (8 → 80 → 480 → 5,000) was an information routing protocol built around a simple human limitation: a leader can effectively manage somewhere between three and eight people."*

> *"The question was never whether you needed layers. The question was whether humans were the only option for what those layers do. They aren't anymore."*

## Company World Model: AIによる情報ルーティングの代替

Blockが構築した2つのワールドモデル:

### 1. Company World Model (内部)
- リモートファースト、マシンリーダブルなアーティファクト（コード、決定、計画、進捗）で構築
- 何が構築され、何がブロックされ、何がリソースされているかを継続的に追跡
- **管理職のコンテキスト収集機能を代替**

### 2. Customer World Model (外部)
- 独自のプロプライエタリな双方向トランザクションデータ（Cash App購入者 + Square加盟店）
- 顧客/加盟店ごとの金融リアリティを作成。運用ごとに複利
- > *"People lie on surveys. They ignore ads. They abandon carts. But when they spend, save, send, borrow, or repay, that's the truth."*

## 4つのビルディングブロック

従来のプロダクトチームが事前に決められたロードマップを構築するのではなく:

| ブロック | 説明 | 例 |
|---------|------|-----|
| **1. Capabilities** | アトミックな金融プリミティブ（支払い、融資、銀行、給与、BNPL）。UIなし。規制・ネットワーク効果のモートで習得困難 | 決済処理エンジン、与信判断ロジック |
| **2. World Model** | 双方向の運用・顧客インテリジェンス。生トランザクションデータ → 因果・予測モデルへ進化 | 季節的なキャッシュフロー予測 |
| **3. Intelligence Layer** | Capabilitiesを文脈的なソリューションに**自律的に構成**。 failure signalが未来のロードマップ | 季節的落ち込みを検知 → 短期融資 + 返済_scheduleを自動提案 |
| **4. Interfaces** | 配信面（Square、Cash App、Afterpay、TIDAL、bitkey）。配布には重要だが、**価値創造はモデル&インテリジェンス層**に存在 | ユーザー向けアプリ、加盟店ダッシュボード |

> **ロードマップの根本的転換**: *"When the intelligence layer tries to compose a solution and can't because the capability doesn't exist, that failure signal is the future roadmap."* — 仮説駆動のPM計画から**現実駆動のバックログ生成**へ。

## AIネイティブ企業の3つのロール

階層を反転: インテリジェンスはシステムに存在。人間は**直観、倫理、新規問題解決が必要なエッジ**で動作。

### 1. Individual Contributors (ICs)
- システム層を構築・運用する専門技術者
- ワールドモデルが文脈を提供。**承認チェーンは不要**
- 深い専門性を活かしてCapabilityの実装・改善に集中

### 2. Directly Responsible Individuals (DRIs)
- 横断的な問題/成果を一時的に所有（例: 90日間の加盟店離脱防止イニシアチブ）
- capability、model、interfaceチームから**リソースをプルする権限**を持つ
- プロジェクト完了後は解散。次のDRIが別の課題を所有

### 3. Player-Coaches
- ハンズオンビルディングと人材育成を組み合わせ
- 技術的クラフトと成長を担当
- **アライメントと戦略はシステム&DRIsが自動化**

## 従来の階層モデルとの比較

| 次元 | 従来の階層 | Hierarchy to Intelligence |
|------|-----------|---------------------------|
| **意思決定** | 上意下達 | 文脈駆動・自律実行 |
| **情報フロー** | サイロ化・制限 | 透明・オープン |
| **管理の役割** | 指示・監視 | 文脈設計・ガードレール設定 |
| **AIの位置付け** | ツール・補助 | 自律実行エージェント |
| **スケーラビリティ** | 人头比に依存 | コンテキスト品質に依存 |
| **ロードマップ生成** | 仮説駆動PM | 現実駆動（failure signal） |

## AIと企業アイデンティティ

> *"If the answer is nothing, AI is just a cost optimization story... If the answer is deep, AI doesn't augment your company. It reveals what your company actually is."*

ブロックのモート: **エコノミックグラフ** — 数百万の加盟店/消費者にわたるリアルタイムの双方向トランザクションデータ。この理解はシステムが運用されるたびに複利で蓄積。

## 実行上の現実

移行は容易ではない。**「壊れてから動く」**状態を経験する。成功にはドメインに対する深い独自理解が必要。それがなければ、AIは短期的なコスト最適化ストーリーに終わる。

## 関連概念

- [[ai-org-context-as-moat]] — Proprietary ContextとFission-Fusion
- [[ai-org-solo-founder-and-super-ic]] — Solo FounderとSuper IC
- [[harness-engineering/agentic-engineering]] — 開発者のAI活用ワークフロー
- [[harness-engineering]] — エージェントの制御・構造化
- [[context-engineering]] — コンテキストエンジニアリング

## ソース

- [Block: From Hierarchy to Intelligence](https://block.xyz/inside/from-hierarchy-to-intelligence) — 2024
- [Jack Dorsey interviews on org design](https://block.xyz) — 2024-2025
