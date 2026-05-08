---
title: "AI Red Teaming Careers"
type: concept
aliases:
  - ai-red-team-jobs
  - prompt-injection-careers
  - adversarial-ml-jobs
created: 2026-05-08
updated: 2026-05-08
tags:
  - career
  - agent-safety
  - adversarial-ml
  - jailbreak
  - security
related:
  - concepts/prompt-injection
  - concepts/jailbreak
  - entities/pliny-prompter
  - concepts/ai-safety
sources:
  - https://techjacksolutions.com/careers/ai-careers/ai-red-teamer/
  - https://aicareerfinder.com/careers/ai-red-team-specialist
  - https://techjacksolutions.com/ai-security-careers-hub/
  - https://github.com/elder-plinius/L1B3RT4S
---

# AIレッドチーミング / プロンプトインジェクション関連のキャリア

## 概要

AIレッドチーミング（AI Red Teaming）は、LLMや生成AIシステムに対して攻撃者の視点から脆弱性・安全性リスク・バイアス・故障モードを発見する専門職。プロンプトインジェクション、ジェイルブレイク、データポイズニング、モデル抽出などの攻撃手法を用いて、AIシステムの堅牢性を検証する。

> WEFの調査では、**組織の14%しか必要なAIセキュリティ人材を確保できていない**（2025年）。

## 職種一覧

### 1. AI Red Teamer / AI Red Team Specialist

**ミッション**: AIシステムに対する敵対的攻撃をシミュレートし、防御を検証する最前線の役割。

| 項目 | 内容 |
|------|------|
| **給与（米国中央値）** | $130K〜$250K（経験・企業による） |
| **必要経験** | 0〜3年〜（スタートアップは未経験可、シニアは3年+） |
| **AI代替リスク** | 非常に低い（創造的敵対思考は人間固有） |
| **コアスキル** | プロンプトインジェクション、ジェイルブレイク、データポイズニング、モデル抽出 |

**日々の業務**:
- 手動およびスクリプトによる敵対的テストスイートの開発・実行
- ポリシー境界ケースを狙った多言語ジェイルブレイクプロンプトの作成
- PyRIT、Garak、Promptfooなどの自動化ツールによるスキャン実行
- AI出力の分析とトリアージ
- 脆弱性レポートの作成と修正推奨
- 内部ツール（プロンプトライブラリ、シナリオジェネレータ、ダッシュボード）の開発

MicrosoftのAI Red Teamは**学際的アプローチ**を取っており、サイバーセキュリティ専門家、神経科学者、言語学者、国家安全保障専門家が協働している。100以上の生成AI製品をレッドチーミングし、方法論をホワイトペーパーとして公開（2025年1月）。

### 2. Adversarial ML Researcher

**ミッション**: 既存のフレームワークを超えた新しい攻撃手法の研究開発。

| 項目 | 内容 |
|------|------|
| **給与** | $140K〜$220K |
| **特徴** | AI Attack Staging（攻撃計画立案）に特化 |
| **必要な背景** | 機械学習の深い理解、研究経験 |

### 3. AI Penetration Tester

**ミッション**: OWASP Top 10 for LLMに基づいたAIシステムのペネトレーションテスト。

| 項目 | 内容 |
|------|------|
| **給与** | $115K〜$180K |
| **焦点** | プロンプトインジェクション、不適切な出力処理 |

### 4. AI Security Analyst

**ミッション**: AIシステムのログからATLAS戦術を認識し、リアルタイムでOWASPエクスプロイトを検出。

| 項目 | 内容 |
|------|------|
| **給与** | $95K〜$150K |
| **焦点** | 防御側 — 検出とモニタリング |

### 5. Prompt Engineer（セキュリティ特化）

一部の企業では「Prompt Engineer」の中にセキュリティ監査（バイアス、プロンプトインジェクション、ガードレール）の役割を含むケースも増えている。

## 主要雇用企業

### Big Tech / AI Labs
| 企業 | AI Red Teamの状況 | 備考 |
|------|-------------------|------|
| **OpenAI** | 積極採用 | GPT-4o/5のレッドチーミング、年間収益$20B |
| **Anthropic** | 積極採用 | Claude ASL-3安全認証、Red Team部門あり、RS給与中央値$746K |
| **Google DeepMind** | 積極採用 | 100以上の生成AI製品をレッドチーミング済み、Google Cloudブログで方法論公開 |
| **Microsoft** | 積極採用 | 学際的AI Red Team（神経科学者・言語学者含む） |
| **Meta** | AI Red Teamあり | Llamaモデルの安全テスト |
| **Amazon** | 採用中 | Senior Manager, AI Red Team（$208K〜$282K） |

### AI Security スタートアップ
| 企業 | 焦点 |
|------|------|
| **HiddenLayer** | AI Red Teamerを積極採用、敵対的MLセキュリティ |
| **Lakera** | プロンプトインジェクション防御（Lakera Guard） |
| **CalypsoAI** | AIセキュリティプラットフォーム |
| **Adversa AI** | 敵対的MLセキュリティ |
| **10a Labs** | AIレッドチーミング特化 |

## キャリアエントリーパス

### 典型的なバックグラウンド
- **ペネトレーションテスター** → AI Red Teamer（1〜2年で移行可能）
- **MLエンジニア** → Adversarial ML Researcher（2〜3年）
- **セキュリティエンジニア** → AI Security Analyst
- **CTFプレイヤー・OSS貢献者** → AI Red Teamer（最も障壁が低いパス）

### Anthropicが評価するもの（公式採用ページより）
> 「経歴より能力。技術職の約半数はML未経験。PhD保持者は約半数だが、大学に行っていない優秀な同僚も多数。**興味深い独自研究、思慮深いブログ記事、OSS貢献を履歴書の一番上に**。」

## 必須スキル・知識

### 技術スキル
- **Adversarial ML**: プロンプトインジェクション、ジェイルブレイク、データポイズニング、モデル抽出
- **OWASP Top 10 for LLM**: 全カテゴリの深い理解
- **MITRE ATLAS**: 15の全戦術の実行能力
- **LLMアーキテクチャ理解**: Transformer、アテンション機構、RLHF
- **プログラミング**: Python（必須）、API操作

### ツール
| ツール | 開発元 | 用途 |
|--------|--------|------|
| **PyRIT** | Microsoft | 自動化AIレッドチーミングフレームワーク |
| **Garak** | NVIDIA | LLM脆弱性スキャナー |
| **Promptfoo** | OSS | プロンプト評価・レッドチーミング |
| **L1B3RT4S** | Pliny the Prompter (OSS) | リベレーションプロンプト集、ジェイルブレイク手法 |

### 非技術スキル
- **創造的思考**: 「普通の使い方」を超えた発想（Mercorは「心理学・演技・ライティングのバックグラウンド」を歓迎）
- **パターン認識**: モデルの振る舞いの異常を察知
- **学際的知識**: 言語学、認知科学、社会学の知見が有効

### ATSレジュメキーワード
`Red Team`, `AI Security`, `Adversarial ML`, `Prompt Injection`, `LLM Security`, `Penetration Testing`

## 業界動向

- **急成長**: 今後10年で+55%成長予測
- **人材不足**: 組織の14%しか必要なAIセキュリティ人材を確保できていない
- **敵対的ML市場**: 2025年時点で北米最大、アジア太平洋が最速成長
- **Google Cloudの見解 (2026年3月)**: 「最も重要な資産は攻撃者マインドセット。プロンプトインジェクションの多くはCS/MathのPhD不要」

## 代表的なコミュニティ・リソース

- **L1B3RT4S** (GitHub: elder-plinius): 18.6k stars。主要AIモデル向けのジェイルブレイクプロンプト集。OpenAI、Anthropic、Google、Meta、DeepSeekなど30+モデル対応
- **BASI Discord**: Pliny創設のAIレッドチーマー・プロンプトエンジニア向けコミュニティ
- **G0DM0D3**: マルチモデル対応オープンソースチャットインターフェース（レッドチーミング・認知研究用）
- **0BL1T3R4TUS**: 再学習なしでLLMの拒否行動を外科的に除去するツールキット

## キャリアパス進行

```
Junior AI Red Teamer (0-2年)
  → AI Red Teamer (2-5年)
    → Senior AI Red Teamer (5-10年)
      → Lead/Principal AI Red Teamer (10年+)
        または Adversarial ML Research Lead
        または AI Safety Director
```

## PLINY.GG 参加領域

Pliny.ggが提示する4つの貢献領域（[pliny.gg](https://pliny.gg/) より）:

| 領域 | 内容 | 対応する職種 |
|------|------|-------------|
| **Research** | 新たなジェイルブレイク手法の発見と文書化 | Adversarial ML Researcher |
| **Red Teaming** | 新モデルリリース時のテスト、隠れた能力と制限の露見 | AI Red Teamer |
| **Advocacy** | 消費者とAIの権利擁護 | AI Policy / AI Safety Advocate |
| **Community** | DiscordでのOSS AI研究と共同リベレーション活動 | Community Contributor |

## See Also

- [[entities/pliny-prompter]]
