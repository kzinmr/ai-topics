---
title: GLiNER Model Family
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [model, encoder-model, small-language-model, named-entity-recognition, open-source, inference, content-moderation, pii-detection, information-retrieval]
sources:
  - https://pioneer.ai/blog/gliner-modern-named-entity-recognition
  - https://pioneer.ai/blog/gliner2
  - https://pioneer.ai/blog/gliguard-16x-faster-safety-moderation-with-a-small-language-model
  - https://pioneer.ai/blog/gliner2-pii-open-source-privacy-filtering-with-pii-detection
  - https://arxiv.org/abs/2311.08526
  - https://arxiv.org/abs/2507.18546
  - https://arxiv.org/abs/2605.07982
  - https://arxiv.org/abs/2605.09973
---

# GLiNER Model Family

**GLiNER**（Generalist Language model for Named Entity Recognition）は、[[entities/fastino-labs]] が開発する **双方向エンコーダベースのSmall Language Modelファミリー**。ゼロショットNamed Entity Recognition（NER）を皮切りに、情報抽出、セーフティモデレーション、PII検出へと拡張されている。

## アーキテクチャの革新

GLiNERの核心的イノベーションは、**NERを生成タスクではなくマッチングタスクとして再定義**したこと。

### 従来のアプローチ（デコーダモデル）

GPT-5やClaudeなどの大規模生成モデルは、NERを自己回帰的なトークン生成として処理:
- 入力テキストを1トークンずつ順次処理
- 遅延・高コスト・API依存
- 分類問題をテキスト生成で解決するオーバーヘッド

### GLiNERのアプローチ（双方向エンコーダ）

- **双方向処理**: 各トークンの前後両方のコンテキストを使用して表現を構築
- **マッチングパラダイム**: 入力テキストとターゲットラベルを共有潜在空間に射影し、類似度スコアを計算
- **ゼロショット**: 新しいエンティティクラスを追加学習なしで認識可能
- **1パス処理**: 全タスクを単一のフォワードパスで並列実行

> "GLiNER's innovation lies in both its return to a bidirectional encoder architecture and its treatment of NER as a matching algorithm."

## モデルファミリー

### GLiNER (v1) — ゼロショットNER

| 項目 | 内容 |
|---|---|
| **論文** | arXiv:2311.08526（2023年11月） |
| **パラメータ** | 50M（Small）〜 205M（Large） |
| **アーキテクチャ** | BERTベース双方向エンコーダ |
| **主要機能** | ゼロショットNER |
| **GitHub** | https://github.com/urchade/GLiNER |

**ベンチマーク結果:**
- GLiNER-Medium (90M): UniNER-13Bと同等性能（**140x 小さい**）
- GLiNER-Small (50M): ChatGPT、Vicuna、InstructUIE-11BをゼロショットNERで凌駕
- 英語のみで学習した多言語変換でも、ChatGPTを多くの言語で上回る

**スケーリング法則の否定:**
> "GLiNER directly contradicts [scaling laws] by matching and even outperforming models many times larger."

### GLiNER2 — 多タスク情報抽出

| 項目 | 内容 |
|---|---|
| **論文** | arXiv:2507.18546（2025年） |
| **パラメータ** | 205M |
| **アーキテクチャ** | 双方向エンコーダ + スキーマ駆動インターフェース |
| **主要機能** | NER, 関係抽出, JSON抽出, テキスト分類（4タスクを1パスで） |
| **GitHub** | https://github.com/fastinoai/GLiNER2 |

**GLiNERからの拡張:**

GLiNER v1はNERのみだったが、GLiNER2はエージェント時代の要求に応えて4タスクに拡張:

1. **NER（Named Entity Recognition）**: 人名、場所、組織などエンティティの識別・分類
2. **関係抽出（Relation Extraction）**: エンティティ間の意味的接続・依存関係の識別
3. **構造化データ抽出（JSON Extraction）**: テキストをスキーマに基づいたJSON形式に変換
4. **テキスト分類**: テキストセグメントへのカテゴリ/ラベル付与

**アーキテクチャ的優位性:**
- **スキーマ駆動**: 宣言的スキーマインターフェースで4タスクを同時実行
- **確定的精度**: 生成モデルではないためハルシネーションなし
- **信頼性の高い構造化出力**: 出力形式はスキーマで事前定義
- **CPU-first**: GPU不要、100ms未満の推論

**ファインチューニング特性:**
- **10例の追加データで3分以内にファインチューニング可能**
- ドメイン特化が容易で、プライバシー要件の高いデータもローカルで処理

**活用場面:**
- プロンプトハック検出
- ハルシネーション検出
- ガードレール
- モデルルーティング（タスクの複雑さに基づくモデル選別）

### GLiGuard — セーフティモデレーション

| 項目 | 内容 |
|---|---|
| **論文** | arXiv:2605.07982（2026年5月） |
| **パラメータ** | 300M |
| **ベース** | GLiNER2-base-v1 のフルファインチューニング |
| **主要機能** | 4種のセーフティタスクを1パスで同時評価 |
| **ライセンス** | Apache 2.0 |
| **HuggingFace** | https://huggingface.co/fastino/gliguard-LLMGuardrails-300M |

**4つのセーフティタスク:**

1. **Safety Classification**（safe/unsafe）: ユーザー入力とモデル出力両方に対して適用
2. **Jailbreak Strategy Detection**（11戦略）: プロンプトインジェクション、ロールプレイバイパス、指示上書き、ソーシャルエンジニアリングなど
3. **Harm Category Detection**（14カテゴリ）: 暴力、性的コンテンツ、ヘイトスピーチ、PII露出、誤情報、児童安全、著作権侵害など
4. **Refusal Detection**（compliance/refusal）: モデルがリクエストを拒否したか従ったかを追跡（過剰拒否の検出にも活用）

**ベンチマーク結果:**

| 指標 | 結果 |
|---|---|
| プロンプト分類 平均F1 | 87.7（最高はPolyGuard-Qwen 89.4） |
| レスポンス分類 平均F1 | 82.7（最高はQwen3Guard-8B 84.1） |
| スループット | 現SOTA比 **最大16.2x 高速**（133 vs 8.2 samples/s） |
| レイテンシ | 現SOTA比 **最大16.6x 低レイテンシ**（26ms vs 426ms） |

**比較対象モデル（全てGLiGuardより23-90x 大きい）:**
- LlamaGuard4 (12B)
- WildGuard (7B)
- ShieldGemma (27B)
- NemoGuard (8B)
- PolyGuard (7B)
- Qwen3Guard (8B)

**学習データ:**
- WildGuardTrain（87,000人のアノテーション済み例）
- GPT-4.1によるラベル生成（unsafe samples）
- Pioneerによるエッジケースの合成データ補完

### GLiNER2-PII — PII検出・プライバシーフィルタリング

| 項目 | 内容 |
|---|---|
| **論文** | arXiv:2605.09973（2026年5月） |
| **パラメータ** | 300M |
| **ベース** | GLiNER2 のファインチューニング |
| **主要機能** | 42 PIIエンティティタイプの検出・マスキング |
| **ライセンス** | Apache 2.0 |
| **HuggingFace** | https://huggingface.co/fastino/gliner2-privacy-filter-PII-multi |

**42 PIIエンティティタイプ（7カテゴリ）:**

| カテゴリ | エンティティ例 |
|---|---|
| 個人識別 | person, full name, date of birth |
| 連絡先・所在地 | email, phone, address, postal code |
| 政府・税ID | passport number, driver's license, tax ID |
| 銀行・決済 | bank account, IBAN, card number, CVV |
| デジタルID | username, IP address, account ID |
| 秘密情報・認証情報 | password, API key, access token |
| 機密日付 | sensitive date, expiration date |

**SPYベンチマーク結果:**

| モデル | 平均F1 | Recall (法律) | Recall (医療) |
|---|---|---|---|
| **GLiNER2-PII** | **0.471** | **0.722** | **0.681** |
| NVIDIA GLiNER PII | 0.391 | — | — |
| urchade | 0.384 | — | — |
| OpenAI Privacy Filter | 0.373 | 0.640 | 0.671 |
| Knowledgator | 0.368 | — | — |

**OpenAI Privacy Filterとの比較:**
- OpenAI: 1.5Bパラメータデコーダ、8エンティティタイプ固定、スキーマ変更不可
- GLiNER2-PII: 300Mパラメータエンコーダ、42タイプ、推論時スキーマカスタマイズ可能
- **5x以上のラベルカバレッジ**をメモリフットプリントの一部で実現

**学習データの革新:**
- 実PIIデータは収集・共有・アノテーションが本質的に不可能
- Pioneerの合成データ生成パイプラインで **4,910件の高品質アノテーション済み例** を生成
- 7言語、多様なドキュメント形式（チャットログ、サポートチケット、CRMメモ、KYCフォーム、請求書、医療記録）
- 合成データのみで学習したにもかかわらず、未見の自然テキストに汎化

## GLiNERのエコシステム

GLiNERアーキテクチャはFastino Labs以外にも影響を与え、複数の派生モデルが開発されている:

### GLiClass（Knowledgator） — 分類特化派生
→ 詳細は [[concepts/gliclass]] を参照

**Knowledgator** がGLiNERアーキテクチャを分類タスクに転用して開発したモデルファミリー。NERの「マッチング」パラダイムをテキスト分類に応用し、Cross-Encoder比で最大50x高速な推論を実現。

| モデル | パラメータ | 主要用途 |
|---|---|---|
| GLiClass-V3 | 32M-439M | ゼロショット分類（DeBERTa/ModernBERT/Ettin） |
| GLiClass-Instruct | 32M-400M | マルチタスク指示追従型分類 |
| GLiClass-Multilang | 140M-720M | 20言語対応、クロスリンガル分類 |

**GLiNER2との関係**: GLiClassとGLiNER2は、GLiNER (v1) を起点とした **並列進化**。GLiNER2はFastinoがNER+関係抽出+JSON+分類の統合を目指したのに対し、GLiClassはKnowledgatorが分類タスクに特化し、階層ラベル・few-shot学習・マルチリンガル対応を深めた。両者は「双方向エンコーダで分類問題を解決」という思想を共有しつつ、異なる最適化方向に進化している。

### その他のコミュニティ派生

| プロジェクト | 開発者 | 用途 |
|---|---|---|
| [GLiNER-PII](https://huggingface.co/nvidia/gliner-PII) | NVIDIA | PII検出 |
| [Gretel GLiNER](https://huggingface.co/gretelai/gretel-gliner-bi-large-v1.0) | Gretel AI | PII検出 |
| [GLiNER-BioMed](https://huggingface.co/collections/knowledgator/gliner-biomed) | Knowledgator | バイオメディカルエンティティ抽出 |
| GLiNER-Multi-PII | urchade | 多言語PII検出 |

## 生産環境での活用パターン

GLiNERモデルは [[entities/pioneer-ai]] プラットフォーム経由で推論可能。以下のようなエージェントアーキテクチャでの利用を想定:

```
ユーザー入力
    ↓
[GLiGuard] ── セーフティチェック（safe/unsafe, jailbreak検出）
    ↓
[GLiNER2-PII] ── PII検出・マスキング
    ↓
[GLiNER2] ── 意図分類・ルーティング
    ↓
[フロンティアLLM] ── 複合推論・計画（必要な場合のみ）
    ↓
[GLiNER2] ── 出力の構造化・検証
```

## 技術的意義

GLiNERファミリーは、AI業界の以下のトレンドを体現している:

1. **スケーリング法則の相対化**: 専用アーキテクチャ + タスク特化で、数百倍大きなモデルに匹敵する性能
2. **SLM優位の時代**: プロダクションAIの主要ビルディングブロックはフロンティアLLMではなく特化型SLM
3. **エンコーダの復権**: 生成モデル万能論への対抗として、理解・分類タスクに特化した双方向エンコーダ
4. **合成データの効用**: 実データが制約されるドメイン（PII、セーフティ）での合成データ活用

## 関連ページ

- [[entities/fastino-labs]] — 開発元
- [[entities/pioneer-ai]] — ファインチューニング＆推論プラットフォーム
- [[concepts/gliclass]] — GLiNERアーキテクチャの分類特化派生（Knowledgator開発）
- [[concepts/continual-learning]] — 継続学習（Adaptive Inferenceの理論的基盤）
