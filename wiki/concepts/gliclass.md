---
title: "GLiClass"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags: [zero-shot-classification, text-classification, encoder-only, efficiency, open-source, multilingual, knowledgator]
aliases: ["GLiClass-V3", "GLiClass-Instruct", "GLiClass-Multilang", "gliclass"]
sources:
  - https://arxiv.org/abs/2508.07662
  - https://huggingface.co/collections/knowledgator/gliclass-v3
  - https://huggingface.co/collections/knowledgator/gliclass-instruct
  - https://huggingface.co/collections/knowledgator/gliclass-multilang
  - https://github.com/Knowledgator/GLiClass
  - https://medium.com/@knowledgrator/pushing-zero-shot-classification-to-the-limit-696a2403032f
status: L3
---

# GLiClass

**GLiClass** (Generalist Lightweight Model for Sequence Classification) は、[Knowledgator](https://knowledgator.com) Engineering が開発したエンコーダ専用ゼロショットテキスト分類モデルファミリー。GLiNER（Generalist Lightweight Named Entity Recognition）アーキテクチャを分類タスクに応用し、Cross-Encoder と同等以上の精度を維持しながら **最大50倍高速**な推論を実現する。

基盤論文：[arXiv:2508.07662](https://arxiv.org/abs/2508.07662)（2025年8月公開）、ライセンス：Apache-2.0。

## アーキテクチャの核心

### 単一フォワードパス分類

従来の Cross-Encoder（NLI ベース）分類では、ラベル数 N に対して N 回のフォワードパスが必要だった。GLiClass はこれを **単一フォワードパス** で処理する：

1. ラベルを `<<LABEL>>` 特殊トークンでマークし、入力テキストと連結
2. 双方向 Transformer（DeBERTa / ModernBERT / Ettin）でラベル間、テキスト-ラベル間の相互作用を同時処理
3. プーリング機構（CLS / 平均 / 最大など）で各ラベルのスコアを計算
4. ドット積またはニューラルネットベースのスコアラでテキストとラベルの整合性を評価

### 3つのアーキテクチャタイプ

- **uni-encoder**（デフォルト）: テキストとラベルを同一エンコーダで処理、最高効率
- **bi-encoder**: テキストとラベルを別々のエンコーダで処理
- **bi-encoder-fused**: bi-encoder にラベル埋め込みをテキスト側に融合
- **encoder-decoder**: 系列変換タスク用

### スコアラとプーリング戦略

| コンポーネント | オプション |
|---|---|
| スコアラ | `simple`（ドット積）, `weighted-dot`, `mlp`, `hopfield` |
| プーリング | `first`（CLS）, `avg`, `max`, `last`, `sum`, `rms`, `abs_max`, `abs_avg` |
| Flash Attention | FlashDeBERTa（DeBERTa v2）、TurboT5（T5/mT5）対応 |

## モデルファミリー概要

GLiClass は3つのサブファミリーで構成される：

### 1. GLiClass-V3（V3.0 シリーズ）

コアバリアント。DeBERTa-v3 / ModernBERT / Ettin をバックボーンにゼロショット分類に特化。**2025年8月リリース**。

| モデル | パラメータ | サイズ | Avg F1 | 推論速度 (ex/s) | バックボーン |
|---|---|---|---|---|---|
| **gliclass-edge-v3.0** | 32.7M | 131 MB | 0.4873 | 97.29 | Ettin |
| gliclass-modern-base-v3.0 | 151M | 606 MB | 0.5571 | 54.46 | ModernBERT |
| gliclass-modern-large-v3.0 | 399M | 1.6 GB | 0.6082 | 43.80 | ModernBERT |
| **gliclass-base-v3.0** | 187M | 746 MB | **0.6556** | 51.61 | DeBERTa-v3 |
| **gliclass-large-v3.0** | 439M | 1.75 GB | **0.7001** | 25.22 | DeBERTa-v3 |
| gliclass-x-base | 0.3B | — | 0.5778 (EN) / 0.418 (多言語) | — | mDeBERTa-v3 |

**推論速度の特性**: Cross-Encoder がラベル数増加に伴い線形に減速する（DeBERTa-v3-Large: 128ラベルで0.25 ex/s）のに対し、GLiClass-V3 はラベル数に関わらずほぼ一定の速度を維持（base-v3.0: 128ラベルで45.94 ex/s）。

### 2. GLiClass-Instruct（V1.0 シリーズ）

マルチタスク指示追従に特化したバリアント。**2026年2月リリース**。V3 と同じ高度な機能（階層ラベル、Few-Shot例、ラベル記述、タスクプロンプト）を備え、instruction-following に最適化。

| モデル | パラメータ | Avg F1 | 特徴 |
|---|---|---|---|
| gliclass-instruct-edge-v1.0 | 32.7M | 0.4922 | エッジ向け最軽量 |
| gliclass-instruct-base-v1.0 | 0.2B | 0.6525 | 速度と精度のバランス |
| **gliclass-instruct-large-v1.0** | **0.4B** | **0.7199** | 最高精度 |

**主要ベンチマーク（large-v1.0、ゼロショットF1）**:
| データセット | large-v1.0 | base-v1.0 | edge-v1.0 |
|---|---|---|---|
| IMDB | 0.9397 | 0.9364 | 0.8159 |
| SST2 | 0.9154 | 0.9198 | 0.7577 |
| CR | 0.9066 | 0.8922 | 0.7933 |
| Spam | 0.9790 | 0.9380 | 0.7609 |
| Snips | 0.8509 | 0.6515 | 0.5461 |
| **AVERAGE** | **0.7199** | **0.6525** | **0.4922** |

### 3. GLiClass-Multilang（多言語シリーズ）

**20言語**をネイティブサポートする多言語バリアント。**2026年4月リリース**。新開発の **CrossAttn Scorer**（Flash-Attention + unpadding による効率的なラベル単位プーリング）を採用。**言語横断分類**（例：フランス語の文章を英語ラベルで分類）が可能。

| モデル | パラメータ | English Avg F1 | Multilingual Avg F1 | スループット (samp/s) |
|---|---|---|---|---|
| gliclass-multilang-edge | ~140M | 0.6196 | 0.3959 | 553.6 |
| **gliclass-multilang-mini** | **~288M** | **0.6827** | **0.5378** | **513.4** |
| **gliclass-multilang-ultra** | **~720M** | **0.7212** | **0.5599** | **200.7** |

**サポート言語**: Swedish, Norwegian, Czech, Polish, Spanish, German, French, Ukrainian, Hindi, Chinese, Arabic, Hebrew, 他。

**Cross-Encoder 比較**（スループット vs ラベル数）:
| モデル | 1 Labels | 8 Labels | 64 Labels | 256 Labels |
|---|---|---|---|---|
| multilang-ultra | 308.2 | 266.3 | 125.2 | 31.5 |
| bge-m3-zeroshot | 940.0 | 112.9 | 14.4 | 3.7 |

## V3 新機能（全ファミリー共通）

GLiClass V3 世代で導入された高度な制御機能：

### 階層ラベル（Hierarchical Labels）
```python
hierarchical_labels = {
    "science": ["space", "biology", "physics"],
    "society": ["politics", "economics", "culture"]
}
# → results: science.space => 0.95
```

### Few-Shot 学習
```python
examples = [
    {"text": "Wake me up at 6:30.", "labels": ["set_alarm"]},
    {"text": "Play some jazz.", "labels": ["play_music"]},
]
results = pipeline(text, labels, examples=examples, threshold=0.5)[0]
```

### ラベル記述（Label Descriptions）
自然言語でラベルの意味を定義し、精度向上。例：`"spam": "Unsolicited commercial messages"`。

### タスクプロンプト（Task Prompts）
プリペンドするカスタム指示。例：`"Classify the sentiment of this review:"`。

### 長文書チャンキング
`ZeroShotClassificationWithChunkingPipeline` で最大 8K トークンの長文書を自動チャンク処理。

## 訓練手法

### LoRA ファインチューニング
- **V3 Base/Large**: LoRA r=384, α=768, target modules = query_proj, key_proj, value_proj, dense, linear_1, linear_2, mlp 層
- **Modern Large V3.0**: LoRA r=768, α=1536
- **Focus Loss**: α=0.7

### 訓練データセット
- `tau/commonsense_qa`
- `knowledgator/gliclass-v3-logic-dataset`
- `BioMike/formal-logic-reasoning-gliclass-2k`

### マルチラベル PPO
論文の重要な貢献の一つ：**Proximal Policy Optimization（PPO）** をマルチラベルテキスト分類に初めて適応。データ不足下でも効果的な訓練と、人間の嗜好／論理的制約の反映が可能。

## Retrieval-Augmented Classification（RAC）

RAG に触発された推論時拡張手法。GLiClass パイプラインの**追加機能**（必須ではない）：

### 仕組み
1. Sentence Transformer（paraphrase-MiniLM-L6-v2）で `gliclass-v2.0` データセットをエンコード
2. HNSW データベースにインデックス
3. 推論時に cosine similarity > 0.5 の類似例を 1–3 件検索
4. `<<EXAMPLE>>` / `<<TRUE_LABEL>>` / `<<FALSE_LABEL>>` トークンでフォーマット
5. 訓練時は 30% ノイズ注入（無関係テキストに置換）でロバストネス向上

### 効果
- **1例で F1 0.3090 → 0.4275**（+38%）、極端なケースでは 0.2594 → 0.6249（+141%）
- **2例で F1 0.4707**（8例 Few-Shot の 0.4838 に迫る）
- ラベル付きデータなしで Few-Shot に迫る性能を実現

## 比較：GLiClass vs 従来手法

| 側面 | GLiClass | Cross-Encoders | LLM | Embedding モデル |
|---|---|---|---|---|
| **ラベル数対応** | 非線形（1→128ラベルで7-20%減） | 線形減衰（50x 減速） | プロンプト長増加 | 定数時間（高速） |
| **ゼロショット能力** | Strong (F1 0.49–0.72) | Strong | Strong だが不安定 | Moderate |
| **単一パス** | ✅ 1パス | ❌ Nパス | ❌ 生成型 | ✅ エンコードのみ |
| **推論費用** | 低（GPU不要で動作可） | 中-高 | 高 | 低 |
| **階層ラベル** | ✅ ネイティブ | ❌ | プロンプト依存 | ❌ |

GLiNER2（2025年7月論文）による評価でも、GLiClass はオープンソースモデルとして競争力のある精度を示しており、特に Banking77（意図分類）などで DeBERTa-v3 を上回るケースが確認されている。

## ユースケース

1. **RAG パイプラインのリランカー**: Cross-Encoder の代替としてレイテンシ削減
2. **コンテンツフィルタリング**: 大規模テキストの一次フィルタリング（話題・感情・スパム）
3. **意図分類**: チャットボットやエージェントのルーティング
4. **NLI**: 含意関係判定
5. **幻覚検出**: コンテキスト＋質問＋回答の連接を入力に hallucinated/correct 分類
6. **LLM 安全性分類**: プロンプトインジェクション、ジェイルブレイク、有害コンテンツの検出
7. **ルール遵守検証**: ガイドラインに従っているかの自動チェック
8. **エッジデバイス / オンデバイス NLP**: 32.7M パラメータの edge モデルでプライバシーセーフ

## 関連リソース

- **GitHub**: [Knowledgator/GLiClass](https://github.com/Knowledgator/GLiClass)
- **ドキュメント**: [docs.knowledgator.com/docs/frameworks/gliclass/](https://docs.knowledgator.com/docs/frameworks/gliclass/)
- **デモ**: [GLiClass SandBox](https://huggingface.co/spaces/knowledgator/GLiClass_SandBox)
- **Discord**: [knowledgator Discord](https://discord.gg/dkyeAgs9DG)
- **ブログ**: [Pushing Zero-Shot Classification to the Limit](https://medium.com/@knowledgrator/pushing-zero-shot-classification-to-the-limit-696a2403032f)
- **Colab**: [ファインチューニングノートブック](https://colab.research.google.com/github/Knowledgator/GLiClass/blob/main/finetuning.ipynb)
- **インストール**: `pip install gliclass`

## 関連コンセプト
- [[concepts/rag-retrieval-augmented-generation]]
- [[entities/gm8xx8]] — キュレーター
- [[concepts/named-entity-recognition]] — GLiNER との関係
