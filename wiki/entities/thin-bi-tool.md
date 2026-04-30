---
title: thin-bi-tool
description: "薄くなるBIツール — The trend of BI tools transitioning from comprehensive analysis platforms to lightweight, visualization-focused tools that rely on cloud DWH and semantic layers"
url: https://note.com/ikki_mz/n/n3382a648c6c5
type: entity
created: 2026-04-25
updated: 2026-04-30
tags:
  - entity
  - bi
  - data-visualization
  - data-engineering
  - dwh
aliases:
  - 薄くなるBIツール
  - Thin BI Tool
  - Light BI
sources:
  - https://note.com/ikki_mz/n/n3382a648c6c5
  - https://stable.co.jp/blog/introduction-lightdash
  - https://stable.co.jp/blog/introduction-steep
---

# 薄くなるBIツール (Thin BI Tool)

**薄くなるBIツール (Thinning BI Tools)** とは、従来の「総合分析プラットフォーム」型BIツールから、DWHネイティブで可視化特化型の軽量BIツールへのトレンドを指す概念。2026年3月にstable株式会社の代表・ikki氏がnoteで発表した考察が基点となっている。

## 著者

**ikki** — stable株式会社 代表。企業向けデータエンジニアリング領域の支援（データ活用・基盤整備のハンズオン支援）を手がける。

## 従来のBIツール: 総合分析プラットフォーム

2004年頃のTableau登場時、クラウドDWH（BigQueryは2010年リリース）は普及しておらず、BIツールには「総合分析プラットフォーム」としての役割が期待されていた。

### 3つの役割
1. **データ取り込み** — Excel、CSV、オンプレDBなど散在するデータをBIツールに取り込む
2. **データ加工** — JOIN、カスタムSQL、ディメンション・メジャー定義など
3. **データ可視化** — ダッシュボード・レポート作成

## 最近のトレンド: 可視化特化型BIツール

新世代のBIツール（Lightdash, Steepなど）は従来と対照的に**機能が少なくシンプル**：

### 変化のポイント
1. **データ取り込みの消失** — BIツールにインポートするのではなく、DWHにクエリを発行してデータを呼び出す
2. **データ加工の最小化** — dbtのセマンティックレイヤーから定義済みデータをそのまま取得
3. **可視化への特化** — BIツールは純粋な可視化レイヤーとして機能

### この変化の要因
1. **クラウドDWHの普及** — BigQuery, Snowflake, Redshiftなどがデータの集約・加工・管理を担う
2. **dbtの普及** — dbtモデルでセマンティックレイヤー（ディメンション・メトリクス定義）をコード管理

### dbt Semantic Layer統合のメリット
- 指標の定義をコードベースで一元管理
- BIツール側の処理を最小化（定義済みデータを選択するだけ）
- エンジニアリングチームとアナリストチームの共通言語として機能

## 代表的なThin BIツール

### Lightdash
- dbtモデルの定義をそのままセマンティックレイヤーとして利用
- yamlファイルでディメンション・メトリクスを定義
- オープンソース、セルフホスト可能

### Steep
- デザインが美しいモダンなBIツール
- dbt Semantic Layerとの統合をサポート
- シンプルな操作性が特徴

## DWHネイティブ可視化の未来

DWH自体（BigQueryなどのクエリ結果を直接可視化する機能）が進化すれば、BIツール単体の価値はさらに薄れる可能性がある。コスト削減、権限管理の一元化などのメリットが期待される。

## Related Concepts
- [[concepts/business-intelligence]] — BIの基礎概念
- [[concepts/dbt]] — データ変換とセマンティックレイヤー管理
- [[concepts/cloud-data-warehouse]] — クラウドDWHアーキテクチャ
- [[concepts/semantic-layer]] — セマンティックレイヤー設計

## Related Entities
- [[entities/lightdash]] — Lightdash BIツール
- [[entities/dbt-labs]] — dbtを開発する企業
- [[entities/tableau]] — 従来型総合BIの代表例

## References
- [薄くなるBIツール — note (ikki / stable株式会社)](https://note.com/ikki_mz/n/n3382a648c6c5)
- [Lightdash紹介 — stable株式会社](https://stable.co.jp/blog/introduction-lightdash)
- [Steep紹介 — stable株式会社](https://stable.co.jp/blog/introduction-steep)
