---
title: "Martin Fowler"
type: entity
created: 2026-06-21
updated: 2026-06-22
tags:
  - person
  - consultant
  - software-engineering
  - thoughtworks
  - company
sources:
  - path: raw/articles/2026-06-19_martinfowler_reliable-agentic-ai-systems.md
status: active
---

# Martin Fowler

Martin Fowler is a renowned software architect, author, and thought leader in the software engineering community. He serves as Chief Scientist at Thoughtworks, a global technology consultancy, and publishes extensively on his website martinfowler.com.

## Background

Fowler has been a prominent voice in software engineering for decades, contributing foundational works on refactoring, patterns of enterprise application architecture, domain-specific languages, and continuous delivery. His writing spans both deeply technical topics and broader reflections on engineering practices.

## Key Contributions

- **Refactoring**: Authored the seminal book _Refactoring: Improving the Design of Existing Code_, which popularized the concept and practice of code refactoring.
- **Enterprise Patterns**: Wrote _Patterns of Enterprise Application Architecture_ (2002), cataloging design patterns for enterprise software systems.
- **DSLs**: Advanced the practice of domain-specific languages with _Domain-Specific Languages_ (2010).
- **Microservices**: Coined and shaped the modern understanding of microservice architectures.
- **martinfowler.com**: Maintains a widely-read bliki (blog + wiki) that serves as a primary reference for software engineering patterns and practices.

## Role in AI Systems Engineering

Through Thoughtworks and his platform, Fowler has increasingly covered AI and LLM engineering topics. In June 2026, martinfowler.com published "Building Reliable Agentic AI Systems," a case study of Bayer's PRINCE platform co-authored with Sarang Sanjay Kulkarni. This article applies Fowler's long-standing emphasis on engineering discipline — context engineering and harness engineering — to the emerging domain of agentic AI, demonstrating patterns for production-reliable AI agents.

## PRINCE Case Study: Building Reliable Agentic AI Systems（2026年6月）

2026年6月、martinfowler.comに掲載された「Building Reliable Agentic AI Systems」は、バイエルAG（Bayer AG）とThoughtworksが共同開発した **PRINCE（Preclinical Information Center）** プラットフォームの包括的ケーススタディである。本稿はFowlerが長年提唱してきた[[concepts/context-engineering|コンテキストエンジニアリング]]と[[concepts/harness-engineering|ハーネスエンジニアリング]]の概念をエージェントAI領域に適用し、実運用に耐える信頼性の高いエージェントシステムの構築パターンを詳述している。

### 進化の三段階：Search → Ask → Do

PRINCEは三つのフェーズを経て進化した。

1. **Search（検索）**：初期フェーズでは数千件の非臨床試験レポートへの統合ゲートウェイを構築。複数のサイロ化されたデータベースを統合し、構造化メタデータを中心とした検索可能な形式を提供した。
2. **Ask（質問）**：第二フェーズではRetrieval-Augmented Generation（RAG）を導入。研究者が自然言語で質問できるAI駆動の質問応答システムにより、過去のPDFレポートを含む非構造化データから直接インサイトを引き出せるようになった。
3. **Do（実行）**：現在のフェーズではマルチエージェントシステムを統合。複雑なクエリ処理、ワークフローオーケストレーション、規制文書の下書き作成など、能動的なリサーチアシスタントとして機能する。

### システムアーキテクチャ

PRINCEのアーキテクチャは[[concepts/reliable-agent-patterns|信頼性パターン]]を具現化したものである。オーケストレーションには **LangGraph** を採用し、FastAPIによるバックエンドとReactによる対話型UIで構成される。

**データストア構成：**
- **OpenSearch**：すべての試験レポートのベクトル表現を格納するコア知識ベース
- **Athena**：ETL処理後のキュレーションされた構造化データへのアクセス
- **PostgreSQL**：LangGraphチェックポインターによるエージェント実行状態の管理
- **DynamoDB**：アプリケーションレベルの状態管理

LLMはOpenAI、Anthropic、Google、およびオープンソースモデルを内部GenAIプラットフォームから統一API経由で利用し、タスクに応じて最適なモデルを選択できるよう設計されている。

### 三層エージェントワークフロー

PRINCEの核となるのは、三つの専門エージェントによる協調ワークフローである。

1. **Researcher Agent（調査エージェント）**：システムの情報収集役。Agentic RAG（非構造化データ用）とText-to-SQL（構造化データ用）の二つの検索パターンをハイブリッドに活用する。RAGパイプラインはキーワード抽出、メタデータフィルタ生成、クエリ拡張（n=5）、重み付きハイブリッド検索（セマンティック0.7＋キーワード0.3）、再ランク（bge-reranker-large、top-k=7）の多段階プロセスで構成される。Text-to-SQLでは動的Few-ShotプロンプティングによりAthena SQLクエリを生成する。

2. **Reflection Agent（リフレクションエージェント）**：Researcher Agentが収集したデータの検証と十分性を評価する。データの完全性を確認し、不足があれば追加調査を指示するフィードバックループを実現する。

3. **Writer Agent（ライターエージェント）**：検証済みの情報を基に回答を統合・整形する。引用付きの応答を生成し、透明性と説明可能性を担保する。

### [[concepts/context-engineering|コンテキストエンジニアリング]]

PRINCEは「コンテキストの規律」（context discipline）を設計原則としている。大規模コンテキストウィンドウが利用可能になっても、各エージェントに与える情報を選択的に絞り込むアプローチを採用した。初期の反復では過剰な情報をコンテキストに詰め込むとシステムの制御と評価が困難になることが判明したため、以下のように段階ごとに異なるコンテキストを提供する：

- **計画コンテキスト**（Think & Plan段階）
- **検索コンテキスト**（Researcher Agent段階）
- **エビデンスコンテキスト**（Reflection Agent段階）
- **統合コンテキスト**（Writer Agent段階）

これによりコンテキスト汚染を低減し、デバッグ、評価、改善が容易になった。

### [[concepts/harness-engineering|ハーネスエンジニアリング]]

システムの信頼性を支えるハーネス層は以下の要素で構成される。

- **オーケストレーション**：LangGraphによるマルチステージワークフローの制御。意図明確化→思考・計画→調査→検証→回答生成の各段階を順次実行する。
- **リトライ機構**：LLM呼び出しレベルと論理ノード（エージェント計画全体のステップ）レベルの二段階でリトライを実装。エラーのコンテキストをエージェントに提供し、代替経路を選択可能にする。
- **フェイルオーバー**：特定のLLMが失敗した場合、自動的にリトライ後に代替モデルまたは代替プラットフォームに切り替える。
- **観測可能性（Observability）**：
  - **Langfuse**：全本番トラフィックの詳細トレースと評価データセット管理
  - **RAGAS**：RAGパイプラインの品質評価フレームワーク
  - **CloudWatch**：システム全体のヘルスとメトリクス監視
- **評価方法論**：日次ベースのライブトラフィック評価と、コアワークフロー・プロンプト・モデル変更時のデータセット評価を組み合わせた二段階評価を実施。

### 透明性と説明可能性

PRINCEは信頼構築を最優先する。すべての応答には引用が自動付与され、回答の根拠が元文書の該当チャンクにトレース可能となっている。また、Clarify User Intent段階ではAIがデータソースを推薦するが、ユーザーはこれを承認・調整・却下できる完全な**Human-in-the-Loop**を確保しており、ドメイン知識が常に最終決定権を持つ。

### 今後の展開

Researcher Agentは現在、単一のエージェントが全ツールを管理する方式から、ドメイン特化型サブエージェントの階層構造へと進化中である。毒性学、薬理学などの各ドメインが独自のツールセットとプロンプト指示を持つことで、責務の明確化とテスト容易性の向上を目指している。このアプローチは、FowlerがSoftware Engineeringラジオなどで繰り返し強調してきた「凝集性と関心の分離」の原則をエージェント設計に適用した実践例といえる。

## Related Pages

- [[concepts/reliable-agent-patterns]] — Fowler's reliability patterns applied to agentic AI
- [[concepts/agentic-rag]] — Agentic RAG architecture, illustrated by PRINCE
- [[concepts/ai-agents]] — AI agents overview
