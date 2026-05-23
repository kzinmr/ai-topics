---
title: OpenAI Codex
type: entity
created: 2026-05-12
updated: 2026-05-23
tags:
  - product
  - coding-agent
  - openai
  - coding-agents
  - harness-engineering
  - ai-agents
  - data-science
  - bizops
  - human-in-the-loop
  - workflow
  - voice-ai
aliases:
  - Codex CLI
  - codex-cli
  - GPT-5.3 Codex
  - gpt-5.3-codex
  - Codex for Work
sources:
  - raw/articles/2026-01-14_openai-codex-prompting-guide.md
  - raw/articles/openai.com--academy-codex-for-work-how-data-science-teams-use-codex--afc8cde3.md
  - raw/articles/2026-05-20_jxnlco_getting-the-most-out-of-codex.md
  - https://github.com/openai/codex
  - https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08
  - https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
---

# OpenAI Codex

OpenAIのAIコーディングエージェント。CLI ベースの完全OSSエージェント（[GitHub](https://github.com/openai/codex)）として提供され、API経由でのカスタム統合も可能。モデルは `gpt-5.3-codex`。

コード生成・編集・コードベース探索・テスト・デプロイまで自律的に実行。コンパクション（会話圧縮）により数時間の自律実行が可能。

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | OpenAI |
| モデル | gpt-5.3-codex |
| 提供形態 | CLI（OSS）+ SDK + API |
| 特徴 | 自律実行、コンパクション、Windows/PowerShell対応 |
| 推論努力量 | medium（推奨）/ high / xhigh |

## 主要機能

- **長時間自律実行**: 数時間の自律タスク実行が可能。high/xhigh reasoning effort で最高難度タスクに対応
- **ファーストクラスコンパクション**: 会話履歴を圧縮し、コンテキスト制限を回避。長時間セッションでも新規チャット開始不要
- **Windows/PowerShell対応**: PowerShell環境での動作が大幅に改善
- **高速・トークン効率**: thinking tokens が削減され、medium reasoning effort でインタラクティブなコーディングに最適なバランスを実現

## アーキテクチャの特徴

- **apply_patch ツール**: ファジーマッチによるファイル編集。厳密な文字列置換ではなく、前後のコンテキストを考慮したマッチングを行う
- **バックグラウンドターミナル実行**: 長時間ビルドやテストをバックグラウンドで実行し、完了を通知
- **ツール並列化**: 独立したツール呼び出しを並列実行
- **ブラウザツール**: ドキュメント検索とUIの視覚的検証に使用

## Codex for Work — チーム向けユースケース（2026年5月）

OpenAIは2026年5月、「Codex for Work」としてチーム別ユースケースのドキュメントを公開。エンジニアだけでなく、データサイエンス、ビジネスオペレーション、営業チームのワークフローにもCodexを適用するガイド。

### データサイエンスチーム向け

データサイエンスの成果物は「クエリ」ではなく「誰かが読み、検証し、行動できる成果物」。Codexはダッシュボード、指標定義、エクスポート、実験ノート、ビジネスコンテキストから**レビュー可能な初稿**を生成する。

| ユースケース | 入力 | 出力 |
|-------------|------|------|
| **KPI根本原因分析** | 指標定義、ダッシュボード、セグメントデータ、ビジネス状況 | 原因分析ブリーフ（確認済み要因と仮説を分離）、チャート、推奨アクション |
| **ビジネスインパクトレポート** | 実験計画、成功指標、コホートデータ、顧客シグナル | リフト分析、ガードレール確認、スケール/変更/中止の判断付きレポート |
| **分析リクエストエージェント** | 曖昧なステークホルダー依頼、利用可能データ | スコープ分析計画、初回分析、ステークホルダー向け回答 |
| **エグゼクティブKPIメモ** | 最新KPI、過去レビュー、オーナーノート、計画コンテキスト | 重要な変化・異常・リスク・オーナーフォローアップ付きメモ |
| **ダッシュボード構築・監視** | ワークフロー、戦略、指標、ソースデータ | ダッシュボード仕様書または初回計画 |

**ワークフローパターン**: Codexが初稿を生成 → 人間が検証、注意点のストレステスト、推奨の精緻化。Codexは**確認済みの事実と仮説を明確に分離**し、データ品質の問題や前提条件を明示する。

**対応プラグイン**: Google Drive, Spreadsheets, Slack, Gmail, Documents, Presentations

### ビジネスオペレーションチーム向け

レポート生成、データ照合、会議準備、プロセス文書化などの運用ワークフローを自動化。

### 営業チーム向け

アカウント調査、提案書作成、CRMデータ分析、競合情報ブリーフィング。


### Codex Thursday No. 6 — Appshots, /goal improvements, annotation mode (May 2026)

OpenAI's sixth weekly Codex Thursday release introduced:

| Feature | Description |
|---------|-------------|
| **Appshots** | Interactive app previews within Codex — see rendered UI without leaving the CLI |
| **/goal improvements** | Better specification understanding for complex multi-step goals |
| **Remote computer use** | Codex can control remote computers (including while locked/away) |
| **Annotation mode** | Markup on rendered output — draw on web pages, highlight UI elements, annotate screenshots |
| **Plugin sharing** | Share custom plugins with team members |
| **Analytics dashboard** | Usage monitoring, task completion tracking, bottleneck identification |

**User reports**: Practitioners report abandoning traditional IDEs entirely for Codex, with the annotation mode and Appshots filling the last gaps that required visual verification in a browser.

**Context**: Thursday No.6 continues the rapid weekly cadence that demonstrates OpenAI's commitment to agent platform iteration — consistent with the [[concepts/model-labs-to-agent-labs]] thesis.

**See also**: [[concepts/model-labs-to-agent-labs]] — Model Labs to Agent Labs industry thesis.

## Codex App: Human-in-the-Loop Capabilities（2026年5月）

Jason Liu（[@jxnlco](https://x.com/jxnlco)、CodexチームDXエンジニア）の包括的ガイドに基づく、Codexのコードエージェントから**「コンピュータ作業全般のシステム」**への進化を支えるアプリ機能群。

### 制御モデル

| 機能 | 説明 | 用途 |
|------|------|------|
| **Steering（操縦）** | 実行中のタスクを中断し、現在のステップ完了前に修正指示 | 「この要素を小さく」「このコピーが間違っている」 |
| **Queuing（キューイング）** | 現在のタスクを中断せず、次のタスクを追加 | 「完了したらSlackでレビュワーにプレビューリンクを送って」 |
| **Voice input（音声入力）** | 洗練前のラフな思考やミーティング議事録をそのまま入力 | 「誰かがSlackでBenって言ってた気がする。詳細忘れた。調べて。」 |

Steering は「今」を変え、Queuing は「次」を変える。両方とも、作業が展開されている間ユーザーを作業の近くに保つ。

### リーチレイヤー（ツール階層）

```
$browser（サイドパネル内ブラウザ：検証・注釈）
  ↓
@chrome（サインイン済みChrome状態でのワークフロー）
  ↓
@computer（デスクトップGUI経由でしか存在しない作業）
```

- **$browser**: サイドパネルでのWebサーフェスレビュー・注釈
- **@chrome**: ユーザーのChromeコンテキストに依存するワークフロー
- **@computer**: デスクトップGUI経由でのみ可能な操作
- **MCPサーバー＋コネクター**: Slack, Gmail, Calendar — タスクはコードになる前にメッセージや受信トレイ項目として現れる
- **Skills**: 実証済みワークフローを再利用可能パッケージとして保存

### 長時間実行と自律性

| 機能 | 説明 |
|------|------|
| **Durable threads** | セッションを跨いでコンテキストを保持する永続スレッド。Command-1~9でピン留めスレッドに即ジャンプ。Chief of Staff, リリース, ドキュメントレビューなどの定常ワークフロー向け |
| **Thread automations** | 同じスレッドにスケジュールで戻るハートビート型の定期的ウェイクアップ。30分毎にSlack/Gmailの未返信メッセージをチェック→優先順位付け→下書き（送信せず） |
| **Goals** | 検証可能なゴールラインを持つ長期間タスク。テストスイート・ベンチマーク・E2Eワークフローを検証器（verifier）として使用。「野心は大事だが、検証なしでは願望に過ぎない」 |

### サイドパネル（成果物レビュー）

会話の横に成果物を保持。コードだけでなく、デッキ・PDF・ブラウザページ・テーブルもその場でレビュー可能。以下の4つの役割に特に有効：

1. **成果物の検査** — Markdown、スプレッドシート、ドキュメント、スライドをその場で
2. **修正箇所の注釈** — 変更が必要な箇所を直接マークアップ
3. **Webサーフェスの操作** — レンダリングされたページをCodexが検査・制御・注釈対応
4. **変更のレビュー** — コンテキストスイッチなしで成果物を洗練

特に効果的なサーフェス: `index.html`（軽量静的アーティファクト）、Storybook（UIレビュー）、Remotion Studio（プログラマティックアニメーション）、ブラウザベースのスライドデッキ、データ分析アプリ。

### 共有メモリ（Shared Memory）

長期スレッドは会話外でメモリを共有することでさらに有用になる。Jason Liuが推奨する耐久パターン：

- **Obsidian vault**: プレーンファイルベースの永続コンテキスト。`TODO.md`, `people/`, `projects/`, `agent/`, `notes/` の構造
- **AGENTS.md**: トップレベルでCodexが何を・いつ・どのように保存すべきか定義
- **Codex Memories**（Settings > Personalization > Memories）: 好み・定常ワークフロー・既知の落とし穴のローカルリコール層
- **Chronicle**: 最近の画面コンテキストからCodexがメモリを構築

> 重要なコンテキストは会話トランスクリプトの中だけに存在すべきではない。次のスレッドが拾い上げられる場所に書き留めよ。

### モバイル（Work from Anywhere）

Codexモバイルアプリにより、Macで開始したタスクを外出先のスマートフォンから継続可能。ローカル環境（ファイル、権限、セットアップ）はMac上に残り、ユーザーは外出先で次のステップを承認・方向転換できる。



### Codex Mobile (May 2026)

Codex expanded to the **ChatGPT mobile app** in preview:

| Feature | Detail |
|---------|--------|
| **Platform** | ChatGPT mobile app (iOS/Android) |
| **Functionality** | Start, steer, and review Codex tasks from phone |
| **Status** | Preview |
| **Significance** | Expands Codex beyond desktop to mobile form factor for task management on the go |

**Use case**: Start a complex coding task on desktop, then monitor progress, approve steps, or redirect the agent from your phone while commuting. The local environment (files, permissions, setup) remains on the desktop — the mobile app provides remote control and oversight.

Source: Jason Liu X article (May 2026), Aakash's Clicky newsletter

## プロンプト設計の特徴

[[concepts/codex-prompting]] 参照。主な特徴：

- **計画の明示的な出力を禁止**: モデルは内部的に計画するが、書き出させると早期停止の原因になる
- **確認不要の自律性**: エラー解決不能時以外はユーザー確認を待たない
- **簡潔なコミュニケーション**: preamble（前置き）やステータス更新を削除し、行動優先
- **メタプロンプティング**: モデル自身に過去の会話を分析させ、システムプロンプトの改善案を生成させる

## 成長指標（Growth Metrics）

| 日付 | WAU | ソース |
|------|-----|--------|
| 2026年3月中旬 | 200万 | Thibault Sottiaux（Codex責任者） |
| 2026年4月8日 | **300万** | Sam Altman 発表。Codex責任者Thibault Sottiauxが「1ヶ月弱前の200万から」と確認 |
| 2026年4月22日 | **400万** | WSJ報道。2週間で100万増加 |

2026年4月8日、Sam AltmanはCodexが週間アクティブユーザー300万人を突破したと発表し、利用制限のリセットを実施。さらに1,000万人に達するまで100万人増加ごとにリセットを繰り返す計画を表明した。Codex責任者Thibault Sottiauxは「1ヶ月弱前には200万人だった」と急成長を確認。

GPT-5.5ローンチ（2026年4月）以降、Codexの勢いは加速。4月22日にはWSJが400万WAU到達を報じ、2週間で100万人の純増を記録した。OpenAIはAccenture、Capgemini、PwCなどのコンサルティングファームと提携し、企業向けCodex販売を本格化。

Sources: [Business Today — Codex 3M WAU](https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08), [WSJ — OpenAI Working With Consultants to Sell Codex](https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9), [Gradually AI — Codex Statistics 2026](https://www.gradually.ai/en/codex-statistics/)


## 競合との比較

| 項目 | Codex | [[entities/claude-code]] | [[entities/cursor]] |
|------|-------|--------------------------|---------------------|
| モデル | gpt-5.3-codex | Opus 4.7 / Sonnet 4.6 | マルチモデル |
| OSS | ✅ 完全OSS | ❌ プロプライエタリ | ❌ |
| 自律性 | 高（数時間） | 高（Auto Mode） | 中 |
| コンパクション | ✅ ファーストクラス | — | — |

## 関連トピック

- [[entities/jason-liu]] — Jason Liu（CodexチームDXエンジニア、本記事著者）
- [[concepts/codex-prompting]] — Codexプロンプト設計パターン
- [[concepts/codex-goal]] — Codex Goalsの設計と運用
- [[concepts/agent-harness]] — エージェントハーネス設計
- [[concepts/metaprompting]] — メタプロンプティング（自己改善プロンプト）
- [[entities/openai]] — OpenAI
- [[concepts/coding-agents]] — コーディングエージェント全般
