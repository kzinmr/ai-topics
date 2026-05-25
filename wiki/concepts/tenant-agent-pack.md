---
title: "Tenant Agent Pack"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - ai-agents
  - multi-tenancy
  - saas
  - enterprise-ai
  - agent-infrastructure
  - fde
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
related:
  - concepts/saas-agent-era
  - concepts/agent-control-plane
  - concepts/forward-deployed-engineering
  - concepts/enterprise-ai
---

# Tenant Agent Pack

**Tenant Agent Pack** とは、テナント（顧客）ごとの差異を**コード分岐ではなくAgent構成アーティファクト**として管理する、AI Agent時代のSaaSマルチテナンシー手法である。

## 定義

Tenant Agent Pack は、コア製品コードを一切変更せずに、特定顧客向けのAI Agentの振る舞いを定義する**顧客別アーティファクトの集合体**である。

## 背景：旧SaaS原則からの転換

従来のSaaSの鉄則は「顧客ごとの機能は作らない」だった（保守性・スケーラビリティのため）。しかしAI Agent時代では、顧客ごとの業務・データ・権限・例外処理の差異を**完全に回避することは不可能**である。そこで、コードではなく**差異を置くレイヤーを変える**のが Tenant Agent Pack の核心思想となる。

## Tenant Agent Pack に含まれるもの

典型的な Tenant Agent Pack は以下のアーティファクトから構成される：

| カテゴリ | 内容 |
|----------|------|
| 目的定義 | その顧客におけるAgentの業務目的・目標 |
| 役割定義 | Agentのロール定義 |
| ツール許可 | 利用可能なツールのallowlist |
| ツール禁止 | 利用禁止ツールのblocklist |
| 承認設定 | 人間の承認が必要な操作一覧 |
| データ接続 | アクセス可能なデータソース |
| 用語集 | 顧客固有の専門用語・グロッサリー |
| 例外処理 | 例外発生時の処理ルール |
| 評価データセット | その顧客にとっての「良い振る舞い」の評価基準 |
| 成功指標 | KPI・成功メトリクス |
| エスカレーション先 | 通知・エスカレーション対象（誰に・いつ） |
| コスト上限 | 実行コストの上限・予算 |
| ロールバック手順 | 障害時の復旧手順 |
| プロンプト | システム指示・プロンプト群 |
| ログ保持 | 実行ログの保持ポリシー |
| エスカレーションルール | 人間へのエスカレーション条件 |

## 設計原則

> **コードを顧客別にforkするな。運用アーティファクトを顧客別にforkせよ。**

コアのAgentエンジンは全顧客で共有し、顧客差分は Tenant Agent Pack に閉じ込める。これにより、製品の保守性を損なわずに深い顧客適応を実現する。

## [[forward-deployed-engineering|FDE]]との関係

[[forward-deployed-engineering|Forward Deployed Engineer]] は顧客現場で業務固有のニーズを発見する。その役割は、発見した知見を Tenant Agent Pack として**バージョン管理・テスト・再利用可能な形**で符号化することである。

## [[agent-control-plane|Agent Control Plane]]との関係

[[agent-control-plane|Agent Control Plane]] は、全テナントの Tenant Agent Pack を横断管理するレイヤーである。バージョニング、デプロイ、監視、監査を集中管理する。

## 旧SaaSとの比較

| 観点 | 旧来SaaS | Tenant Agent Pack |
|------|----------|-------------------|
| カスタマイズ | 管理画面・設定項目 | Agent運用アーティファクト |
| 顧客別コード | 原則禁止 | 原則禁止（別レイヤーで吸収） |
| アップグレード | フィーチャーフラグ・設定 | Packのバージョニング |
| 再利用性 | 共通機能セット | 業界別Packテンプレート |

## 関連項目

- [[saas-agent-era|SaaS Agent時代]] — Agent時代のSaaS構造変化の全体像
- [[agent-control-plane|Agent Control Plane]] — Tenant Agent Pack を横断管理する統治レイヤー
- [[forward-deployed-engineering|Forward Deployed Engineering]] — Packを生み出す現場知見の源泉
- [[enterprise-ai|Enterprise AI]] — エンタープライズAI導入の文脈
