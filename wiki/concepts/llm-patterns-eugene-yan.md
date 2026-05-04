---
title: "LLM Patterns (Eugene Yan)"
type: concept
created: 2026-05-04
updated: 2026-05-04
tags:
  - concept
  - llm-patterns
  - evals
  - rag
  - fine-tuning
  - production-llm
aliases:
  - "7 patterns for building LLM systems"
  - "yan-llm-patterns"
  - "llm-based-systems-patterns"
sources:
  - https://eugeneyan.com/writing/llm-patterns/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/
  - raw/articles/2023-07-30_eugeneyan-llm-patterns.md
  - raw/articles/2024-05-28_oreilly-applied-llms-part1.md
  - raw/articles/2024-05-31_oreilly-applied-llms-part2.md
  - raw/articles/2024-06-06_oreilly-applied-llms-part3.md
status: Level2
---

# LLM Patterns (Eugene Yan's Framework)

**Eugene Yan** が提唱する、LLMをプロダクションシステムに統合するための7つの実践的パターン。2023年7月の記事「[Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/)」で初めて体系的に整理され、その後O'Reilly共著「[What We've Learned From a Year of Building with LLMs](https://oreilly.com)」で発展・改訂された。

このフレームワークは、LLMアプリケーション開発における「評価なき開発は盲目」という哲学に基づき、データ中心の改善からユーザー向け設計までをカバーする。

---

## フレームワークの全体像

7つのパターンは **データ中心 → インフラ → ユーザー対面** のスペクトラムを形成する：

```
データ/内部        インフラ            ユーザー対面
  Evals     RAG     Caching      Guardrails      Defensive UX
  ↓         ↓         ↓             ↓                ↓
  Fine-tuning       (Infrastructure)          User Feedback
```

| パターン | 目標 | 焦点 | カテゴリ |
|---------|------|------|---------|
| **Evals** | パフォーマンスの測定 | データ/内部 | 🔵 評価基盤 |
| **RAG** | 外部知識の注入 | データ/内部 | 🔵 知識拡張 |
| **Fine-tuning** | タスク特化 | データ/内部 | 🔵 モデル適応 |
| **Caching** | レイテンシ・コスト削減 | インフラ | 🟢 効率化 |
| **Guardrails** | 品質・安全性の確保 | インフラ | 🟢 品質保証 |
| **Defensive UX** | エラーの優雅な処理 | ユーザー対面 | 🟡 UX設計 |
| **User Feedback** | 改善のためのデータ循環 | ユーザー対面 | 🟡 フィードバック |

**Evalsはすべての基盤** — 測定なしに改善は不可能。

---

## 各パターンの詳細

### 1. Evals — パフォーマンス測定

LLMエンジニアリングの基盤。評価なしに「飛び回る」ことになる。

**主要指標:**
- **BLEU/ROUGE** — n-gramベースの精度/再現率。創造的タスクでは人間の判断と相関が低い
- **BERTScore/MoverScore** — 埋め込みを使って同義語や意味的類似性を考慮
- **LLM-as-a-Judge (G-Eval)** — 強力なモデル（GPT-4）で他モデルを評価。GPT-4は人間評価者と~85%一致

**実装のヒント:**
- **Eval Driven Development (EDD)** — エンジニアリングの前にタスク固有のプロンプトと「正解」参照を収集
- **LLMバイアスの緩和:** LLMは最初の回答（Position bias）、長い回答（Verbosity bias）、自身の出力（Self-enhancement bias）を好む。評価時に回答順序を入れ替えてPosition biasを対策

**関連Wikiページ:**
- [[concepts/evals-for-ai-agents]] — AIエージェント向け評価（要拡充）
- [[eugene-yan--core-ideas]] — Eugene YanのEDD哲学とAlignEval

#### NLI-based Hallucination Detection (OOD Finetuning)

Yanの実証研究（[Out-of-Domain Finetuning to Bootstrap Hallucination Detection](https://eugeneyan.com/writing/finetuning/)）では、ハルシネーション検出を **NLI（Natural Language Inference）タスク**として定式化。BARTモデルをMNLIでファインチューニングし、原文（Premise）と要約（Hypothesis）の矛盾（Contradiction）を検出する。

**OODブートストラッピングの手法:**
1. **事前ファインチューニング（ドメイン外）:** Wikipediaデータセット（USB）で3エポック学習。単体ではスコア向上しない
2. **本ファインチューニング（対象ドメイン）:** Newsデータセット（FIB）で10エポック。事前学習が「隠れた基盤」として機能

**結果（FIB検証セット、@0.8閾値）:**

| 訓練段階 | PR AUC | Recall | Precision |
|---------|--------|--------|-----------|
| 非ファインチューン | 0.56 | Low | Low |
| FIBのみ（10 epoch） | 0.69 | 0.02 | 0.67 |
| USB（3 epoch）→ FIB（10 epoch） | **0.85** | **0.50** | **0.91** |

- **25倍のRecall向上:** USB事前学習によりRecallが0.02→0.50に
- **Hidden Learning:** ドメイン外データ単体では効果が見えなくても、本学習の準備として機能
- **実用化閾値が可能に:** ブートストラップ後の確率分布分離が明瞭になり、実用的な分類閾値（0.8）が設定可能
- **使用技術:** QLoRAで効率的なファインチューニング

> **教訓:** 「対象タスクに完全に関連するデータがなくても、オープンソースの関連データセットで事前学習すれば、収集すべきファインチューニングデータを減らせる可能性がある」

---

### 2. RAG (Retrieval-Augmented Generation) — 外部知識の注入

モデルを外部の最新データに基づかせ、幻覚（ハルシネーション）とコストを削減。

**主要概念:**
- **Dense Passage Retrieval (DPR)** — クエリと文書を同じベクトル空間にマッピングするデュアルエンコーダ
- **Hybrid Search** — キーワード検索（BM25）+ 意味検索（Embeddings）の組み合わせ。単独より優れる
- **HyDE (Hypothetical Document Embeddings)** — クエリに対してLLMが仮想的な文書を生成し、その埋め込みで検索

**ベクトルインデックス:**
- **FAISS** — 数十億ベクトルに対して効率的なメモリ使用
- **HNSW** — 高速な階層的検索のためのグラフ構造
- **ScaNN** — Googleのアプローチ。最高の再現率-レイテンシトレードオフ

**関連Wikiページ:**
- [[concepts/agentic-rag]] — エージェント型RAGの進化系
- [[concepts/modern-retrieval-toolkit]] — 最新の検索ツールキット

---

### 3. Fine-tuning — タスク特化

パフォーマンス向上、制御、モジュール化（小さな専門モデルの使用）のために。

**主要手法:**
- **LoRA (Low-Rank Adaptation)** — 学習可能な低ランク分解行列を注入し、少数のパラメータのみ更新
- **QLoRA** — 4ビット量子化モデルをファインチューニング。65Bモデルを48GB GPU 1台で調整可能
- **Instruction Fine-tuning** — (指示, 出力) ペアでベースモデルを学習し、役立つアシスタントに

**関連Wikiページ:**
- [[concepts/fine-tuning/peft-lora-qlora]] — LoRA/QLoRAの詳細
- [[concepts/fine-tuning/instruction-fine-tuning]] — 指示チューニング
- [[concepts/fine-tuning/axolotl]] — ファインチューニングフレームワーク
- [[concepts/fine-tuning/unsloth]] — 高速ファインチューニング

---

### 4. Caching — レイテンシ・コスト削減

以前計算したLLM応答をキャッシュし、将来の同一・類似リクエストに再利用。

**戦略:**
- **Semantic Caching** — 入力の埋め込みをキャッシュキーにする
- **Safe Caching** — 自然言語ではなくItem IDや制約付き入力（ドロップダウン選択など）を使用。誤った「類似」回答を防ぐ
- **Pre-computation** — 人気クエリの応答をオフラインで事前生成。レイテンシを秒からミリ秒に

---

### 5. Guardrails — 品質保証

LLMの出力を構文、安全性、事実正確性の観点から検証。

**ツールと方法:**
- **Structural Guidance** — 定型表現（Guidance、Outlinesなど）を使ってモデルに特定の文法（JSONなど）を強制
- **統語的/意味的チェック:**
  - *統語的:* SQLコードが実行可能か、値が定義済みリストに含まれるか
  - *意味的:* LLMで要約がソーステキストと矛盾していないか確認（SelfCheckGPT）
- **Input Guardrails** — 敵対的・NSFWプロンプトがモデルに到達する前にブロック

**関連Wikiページ:**
- [[concepts/structured-outputs]] — 構造化出力の手法
- [[concepts/ai-coding-reliability]] — AIコーディングの信頼性

---

### 6. Defensive UX — エラーの優雅な処理

LLMが失敗することを前提とし、インターフェースを優雅に設計。

**核となる原則:**
- **期待値の設定:** 「AIは不正確な情報を生成する可能性があります」という注意書きで信頼を調整
- **効率的な却下:** 提案を無視しやすくする（GitHub Copilotのゴーストテキストなど）
- **帰属性の提供:** 引用や「社会的証明」を含めてユーザーが情報を検証できるように
- **親しみやすいUI:** すべてをチャットボックスに詰め込むのではなく、標準的なUI要素（ボタン、リスト）を使用

---

### 7. User Feedback — データフライホイール

フィードバックはLLMプロダクトの主要な「堀（moat）」であり、将来の評価とファインチューニングを促進。

- **明示的フィードバック:** いいね/よくない、「再生成」ボタン、星評価
- **暗黙的フィードバック:**
  - *Copilot:* ユーザーがTabを押してコードを受け入れたか？
  - *Midjourney:* ユーザーが画像をアップスケール・ダウンロードしたか？
  - *検索:* 結果をクリックしたか、クエリを修正したか？

---

## フレームワークの進化

Yanの7パターンはコミュニティとの共進化により複数バージョンが存在する：

| バージョン | 出典 | パターン | 違い |
|-----------|------|---------|------|
| **v1 (2023.07)** | eugeneyan.com | Evals, RAG, Fine-tuning, Caching, Guardrails, Defensive UX, User Feedback | オリジナル版。Caching/Guerdrails/Defensive UX/User Feedbackを含む |
| **v2 (2024.06)** | O'Reilly共著「Applied LLMs」 | Part I (Tactical): Prompting, RAG, Flow Engineering, Evals<br>Part II (Operations): Data, Models, Product, Team<br>Part III (Strategy): Resource Allocation, System Moat, Human-Centered AI, Economics | 3部構成に拡張。戦術→運用→戦略の階層構造。6人の共著。 |

**O'Reilly版 (Applied LLMs Guide) の3層構造:**

```mermaid
Part I: Tactical (How?)
  Prompting Tactics → RAG → Flow Engineering → Evaluation
        ↓
Part II: Operations (Who? With what?)
  Data Ops → Model Management → Product Design → Team/Roles
        ↓
Part III: Strategy (Why? What's next?)
  Resource Allocation → Competitive Advantage → Product Strategy → Economics
```

The O'Reilly guide (通称「Applied LLMs」) は [applied-llms.org](https://applied-llms.org/) で公開され、6人の共著者（Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, Shreya Shankar）により執筆された。コミュニティの事実上の標準リファレンス。

---

## O'Reilly Applied LLMs Guide — 詳細内容

### Part I: Tactical — How to Build

#### 1. Prompting Tactics
- **N-Shot Prompts:** 5例以上を提供。分布を代表する例を選ぶ
- **Chain-of-Thought:** 単なる「step-by-step」ではなく具体的な手順を指示（「1. sketchpadで意思決定、2. 一貫性チェック、3. 統合」）
- **構造化入出力:** Instructor（API向け）、Outlines（セルフホスト向け）。ClaudeはXML、GPTはMarkdown/JSONを好む
- **God Prompt アンチパターン:** 2000トークンの巨大プロンプトを避け、小さなパイプラインに分割
- **Claude応答のPre-filling:** assistantロールで応答を先書きして誘導

#### 2. RAG (Retrieval-Augmented Generation)
- **品質の3要素:** 関連性（MRR/NDCG測定）、情報密度、メタデータの充実
- **Hybrid Searchが標準:** 「ベクトル埋め込みは検索を魔法のように解決しない」— Aravind Srinivas。BM25（名前/頭字語/ID）+ Embeddings（同義語/マルチモーダル）
- **Long ContextがRAGを殺さない理由:** コスト線形増加、超長文脈でも「distractor」にモデルが圧倒される

#### 3. Flow Engineering（ワークフロー最適化）
- 単一プロンプト→フローへの移行で精度が劇的向上（AlphaCodium: GPT-4 19%→44%）
- **決定論優先:** エージェントが計画（DAG）を生成し、決定論的に実行してデバッグ容易に
- **多様性確保:** Temperature以外に、入力順シャッフル、プロンプト言い換え、「最近の出力リスト」で回避指示
- **Caching:** 静的コンテンツには一意IDでキャッシュ、レイテンシ/コストゼロに

#### 4. Evaluation & Monitoring
- **Intern Test:** 大学生のインターンが10分でできないタスクはLLMも失敗する
- **LLM-as-Judgeのベストプラクティス:** ペアワイズ比較、評価順スワップ（Position bias対策）、同値判定を許可
- **アサーションベーステスト:** 実プロダクションサンプルから単体テスト。コード生成なら実行まで検証
- **幻覚問題:** ベースライン5-10%、最適化後でも2%以下は困難。下流でFactual Inconsistency Guardrails

---

### Part II: Operations — Who Builds and With What

#### 1. Data Operations（データ運用）
- **開発-プロダクションスキュー:** 構造的skew（フォーマット不一致）、意味的skew（トピック/意図の変化）。埋め込みクラスタで検出
- **Daily Vibe Check:** 毎日入出力サンプルを目視確認。失敗を見つけたら即座にコードアサーションまたは評価を書く
- **Criteria Drift:** データを見れば見るほど「良い/悪い」の判断基準が変化する。運用プロセスとして組み込む

#### 2. Working with Models（モデル運用）
- **Postelの法則のLLM版:** 「入力では自由な自然言語を許容し、出力では型付けされた機械可読オブジェクトを返せ」
- **モデルピンニング:** 常に特定バージョン（gpt-4-turbo-1106）を固定。同ファミリ内アップグレードでも~10%性能低下を想定
- **Shadow Pipelines:** 新旧モデルを並行運用し、安定確認後に切替
- **モデル選択:** 最小のモデルでジョブを完了。Claude Haiku + 10-shot > GPT-4 zero-shot。分類ではDistilBERTがLLMの<5%コストで0.84 ROC-AUC

#### 3. Product Design（プロダクト設計）
- **Suggestion Pattern:** 完全自動化ではなく、LLMが提案→人間が検証/編集
- **暗黙的フィードバック:** 提案受け入れ=強い肯定、再生成=強い否定
- **Hierarchy of Needs:** 信頼性と無害性を最優先。有用性とコストは初期から完璧を求めない

#### 4. Team and Roles（チーム構成）
- **役割の進化:** AI Engineer（試作/UX）→ Data/Platform Engineer（計装/データ）→ ML Engineer（最適化）。MLEの早期採用はリソースの無駄
- **EvalGen原則:** ドメイン固有テストを定義、人間の判断とアライン、変化に応じてテストを反復
- **文化:** 全チームにプロンプトエンジニアリングを教育、ハッカソンで革新的UXを発見

---

### Part III: Strategy — Why Build and What's Next

#### 1. Resource Allocation（リソース配分）
- **"No GPUs Before PMF":** PMF達成前にトレーニングインフラに投資するな
- **ゼロからの学習は気晴らし:** BloombergGPTすら1年でGPT-4に凌駕された
- **Build vs. Buy:** APIで検証→セルフホストはスケール/プライバシーが必要な場合のみ（BuzzFeedはファインチューニングでコスト80%削減）

#### 2. Competitive Advantage（競争優位）
- **「システムの堀」に投資:** 評価基盤、Guardrails、Caching、データフライホイール — これらはモデル交換後も持続する
- **戦略的先送り:** モデルプロバイダーが自分で解決する必要がある機能（関数呼び出しのバリデーションなど）は自前で作らない

#### 3. Human-Centered AI（人間中心のAI）
- **Centaur Paradigm:** 有能な人間 + LLMツールの組み合わせ。完全代替ではなく協調
- **Scopeの狭化:** 汎用「chat with your data」は浅い。ドメイン固有フォーマットに特化
- **"Sparkle" Features回避:** コモディティ化しつつあるバニティ機能（ドキュメントチャットボット）にリソースを割かない

#### 4. Economics of "Low-Cost Cognition"（低コスト認知の経済学）
- **6ヶ月で半減:** text-davinci-003相当の性能が$20→$0.20/100万トークンへ（18ヶ月で1/100）
- **戦略的予測:** 今日高コストなアプリケーション（$60/hourのゲームNPC）は12-24ヶ月で経済圏に
- **洞察:** 「今日の非現実的なデモは数年後にはプレミアム機能、さらにその後はコモディティになる」

#### 5. From Demos to Products（デモからプロダクトへ）
- 「初のニューラルネット駆動自動車は1988年…プロトタイプから商用製品まで35年かかった」
- 0→1（デモ）から1→N（スケーラブルな製品）への移行こそが本当の課題

---

## 関連Wikiページ

- [[entities/eugene-yan]] — フレームワークの提唱者、Applied LLMs Guideの主著者
- [[entities/eugene-yan--core-ideas]] — Yanのコアアイデアとフレームワーク一覧
- [[entities/bryan-bischof]] — Applied LLMs Guide共著者
- [[entities/charles-frye]] — Applied LLMs Guide共著者
- [[entities/hamel-husain]] — Applied LLMs Guide共著者
- [[entities/jason-liu]] — Applied LLMs Guide共著者（Instructorライブラリ作者）
- [[entities/shreya-shankar]] — Applied LLMs Guide共著者
- [[concepts/evals-for-ai-agents]] — AIエージェント評価（要拡充）
- [[concepts/agentic-rag]] — RAGのエージェント型進化
- [[concepts/fine-tuning/peft-lora-qlora]] — PEFT/LoRA/QLoRA
- [[concepts/fine-tuning/instruction-fine-tuning]] — 指示チューニング
- [[concepts/structured-outputs]] — 構造化出力
- [[concepts/ai-coding-reliability]] — AIコーディングの信頼性とガードレール
