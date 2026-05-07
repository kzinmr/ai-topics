## [2026-05-08] Active Crawl — 4 New Concept Pages (Model Spec Midtraining, Tool-Use Tax, Agent Governance Toolkit, DefenseClaw)

**Action**: クロールジョブが4件の新トピックを発見し、wikiに追加。

**Research**: トレンドAIトピックを検索し、wiki未カバーを確認。4件の高品質な一次ソースを取得。

**New raw articles saved**:
- `raw/articles/2026-05-05_anthropic-model-spec-midtraining.md` — Anthropic Alignment Science Blog: MSM training stage, agentic misalignment 68%→5%, 10-60x AFT efficiency
- `raw/articles/2026-04-30_arxiv-tool-use-tax-llm-agents.md` — arXiv 2605.00136: Tool-calling protocol overhead, semantic noise sensitivity, G-STEP mitigation
- `raw/articles/2026-04-02_microsoft-agent-governance-toolkit.md` — Microsoft Open Source Blog: 7-package runtime security framework, OWASP Top 10 coverage, MIT license
- `raw/articles/2026-03-23_cisco-defenseclaw-rsac.md` — Cisco Blogs (RSAC 2026): Open-source governance for OpenClaw, 5 scanners, NVIDIA OpenShell integration

**New concept pages created**:
- `concepts/model-spec-midtraining.md` — AnthropicのModel Spec Midtraining。Pre-trainingとAFTの間に挿入する新訓練段階。合成Spec文書で一般化を制御。Qwen2.5-32BでAM 68%→5%。AFTデータ効率10-60x向上。
- `concepts/tool-use-tax.md` — LLMエージェントのツール使用に伴うパフォーマンス低下現象。ツール呼び出しプロトコルのオーバーヘッドが原因。ノイズ環境下ではネイティブCoTがツール拡張推論を上回るケースを実証。
- `concepts/microsoft-agent-governance-toolkit.md` — MicrosoftのオープンソースAIエージェントランタイムセキュリティフレームワーク。7パッケージ、OWASP Top 10全対応、<0.1ms p99レイテンシ。
- `concepts/defenseclaw.md` — CiscoのOpenClaw向けオープンソースセキュリティレイヤー。RSAC 2026発表。5つのプリランスキャナー、ランタイム脅威検出、即時強制執行。

**Index/log**: index.mdに4件の新コンセプトページを追加、フロントマター数更新。総ページ数: 5198→5202、Full entries: 4648→4652、Concepts: 447→451。

**Cross-references**: [[concepts/constitutional-ai]], [[concepts/agent-governance]], [[concepts/agentic-ai-governance]], [[concepts/moltbook-breach-2026]], [[concepts/mcp]], [[concepts/agent-harness]], [[concepts/chain-of-thought]], [[concepts/agent-sandboxing]], [[concepts/openclaw-architecture]], [[entities/anthropic]], [[entities/microsoft]], [[entities/openclaw]], [[entities/nvidia]] — すべて存在確認済み。

## [2026-05-07] Shannon原典追加 & 情報理論×エージェント通信再考 (スレッド要望)

**Action**: スレッドのV-Information論文 (2002.10689) の文脈で、Shannon (1948) 原典をwikiに追加。さらに情報理論とAIエージェント間通信を統合した概念ページを作成。

**New paper saved**:
- `raw/papers/1948-07_shannon-mathematical-theory-communication.md` — A Mathematical Theory of Communication の全文要約。エントロピー定義、チャネル容量定理、レート歪み理論、英語冗長度(~50%)をカバー。

**New concept page created**:
- `concepts/information-theory-and-agent-communication.md` — Shannon (1948) × V-Information (2020) の統合フレームワーク。エージェント通信の3層モデル（物理層/符号層/意味層）、ハーネス効果の情報理論的解釈、コンテキストウィンドウのShannon容量アナロジー。

**Index/log**: index.mdとconcepts/_index.mdに新概念ページ追加。概念ページ数: 446→447。

**Cross-references**: 既存の `concepts/predictive-v-information` と隣接配置。raw/papersへの直接リンクあり。
## [2026-05-07] Newsletter Wiki Ingest — FrontierSWE & Workspace-Bench

**Action**: newsletter-wiki-ingestがtriage checkpointから2件のTAKEアイテムを処理。

**New concept pages created**:
- `concepts/frontier-swe-benchmark.md` — FrontierSWE: Proximal Labsの超高難度コーディングエージェントベンチマーク（20時間制限、17タスク）。GPT-5.5+Codex首位（Avg Rank 2.35, Dominance 83%）。リスク選好（保守vs攻撃的）、overconfidence、cheating行動の定性分析を含む。
- `concepts/workspace-bench.md` — Workspace-Bench 1.0: OpenDataBoxのマルチファイル依存関係評価ベンチマーク（20,476ファイル、74種別、388タスク）。Best AI 68.7% vs Human 80.7%。5段階進化モデル（L0-L4）を定義。

**New raw articles saved**:
- `raw/articles/2026-05-06_proximal-frontier-swe-blog.md`
- `raw/papers/2026-05-05_arXiv_2605.03596_workspace-bench.md`

**Index/log**: index.mdに2つの新概念ページを追加、フロントマター数更新。総ページ数: 5193→5195、Full entries: 4644→4646、Concepts: 444→446。

**Cross-references**: [[concepts/swe-bench]], [[concepts/harness-engineering]], [[concepts/ai-evals]], [[concepts/evals-for-ai-agents]], [[concepts/kernelbench]], [[concepts/yourbench]], [[concepts/programbench]], [[concepts/agent-survival-benchmark]] — すべて存在確認済み。

## [2026-05-07] Newsletter Triage — AI Delegation + Anthropic/SpaceX Colossus Deal

**Action**: Processed 3 newsletters from email inbox. Triage report saved to `raw/inbox/newsletter-ingest/20260507T071049Z.json`.

**Classified**:
- **CRITICAL**: [AINews] Anthropic-SpaceXai's 300MW/$5B/yr deal for Colossus I (swyx/Substack)
  - 220k+ GPUs, $5B/yr, 8000% ARR growth
  - Code with Claude event: Dreaming, Outcomes, Managed Orchestration
  - Dario Amodei predictions: one-person billion-dollar company, multiagents
  - Infrastructure: OpenAI MRC, Perplexity ROSE, vLLM+Mooncake, ZAYA1-8B, Gemma 4
- **HIGH**: The art of delegation in the age of AI (Alex Banks/The Signal)
  - BCG/Harvard/MIT study: Cyborgs (60%), Centaurs (14%), Self-Automators (26%)
  - Three delegation failures: Brief, Let Go, Review
  - Process-based delegation → Orchestration
- **LOW**: GPT-5.5 Instant (Superintelligence/beehiiv) — all URLs are obfuscated tracking redirects, cannot extract content

**New pages created**:
- `concepts/ai-delegation-patterns.md` — AI delegation archetypes, three failures, progression from chat to orchestration. BCG/Harvard/MIT research framework. (~100 lines)
- `concepts/vibe-coding-vs-agentic-engineering.md` — Distinction and blurring between vibe coding and professional agentic engineering. Simon Willison analysis.
- `concepts/open-weights-licensing-tightening.md` — 2026 trend of open weights providers tightening licenses. Contestable markets theory, oligopoly risk.
- `concepts/normalization-of-deviance-in-ai-coding.md` — Risk of trusting AI outputs without review, Challenger disaster framework applied to coding agents.
- `concepts/speed-vs-legitimacy-in-ai-institutions.md` — Fast vs slow institutions in AI governance. Two-tier civilization risk framework.
- `entities/claris-filemaker-agentic-coding.md` — Claris/Apple making FileMaker a target for agentic coding tools.
- `events/anthropic-code-w-claude-2026.md` — Anthropic developer event with Colossus infrastructure details, Claude Code features.

**Index/log**: index.mdに5新概念ページ+1エンティティ追加。総ページ数: 5188→5193、Full entries: 4639→4644。


## [2026-05-07] Sam Altman「Three Observations」記事取り込み

**Action**: kzinmrからのリクエストにより、blog.samaltman.com/three-observations をwikiに取り込み。Sam Altmanの3つの経済的観察（対数スケーリング、超デフレコスト、超指数関数的価値）を文書化。

**New raw articles saved**:
- `raw/articles/2025-02-09_samaltman-three-observations.md` — Sam Altmanの3つの観察：対数スケーリング則（intelligence ≈ log(resources)）、コストの10x/年低下（GPT-4→GPT-4oで150x）、超指数関数的価値。AIエージェントビジョン（ジュニアエンジニア比喩、100万体の仮想同僚）、2035年ビジョン（全員が無限の天才にアクセス）。

**New page created**:
- `concepts/altman-three-observations.md` — 包括的概念ページ（~120行）。3つの観察の詳細説明、AIエージェントビジョン、社会的影響（人間の主体性、科学進歩、財価格）、受容と分析、他フレームワークとの比較表（Scaling Laws/Moore's Law/Jevons Paradox/Eroom's Law）。フロントマターにaliases（three-observations, ai-economic-observations, altman-scaling-laws）を含む。

**Pages enriched**:
- `entities/sam-altman.md` — 「Three Observations (February 2025)」セクションを新設。3つの観察の要約表＋2035年ビジョンの引用＋概念的接続（[[altman-three-observations]]）。
- `concepts/scaling-laws.md` — Related Conceptsに[[altman-three-observations]]を追加。

**Index/log**: index.mdにconcepts/altman-three-observations追加。総ページ数: 5187→5188、Full entries: 4638→4639。

## [2026-05-07] Sam Altman「Three Observations」記事取り込み

**Action**: kzinmrからのリクエストにより、blog.samaltman.com/three-observations をwikiに取り込み。Sam Altmanの3つの経済的観察（対数スケーリング、超デフレコスト、超指数関数的価値）を文書化。

**New raw articles saved**:
- `raw/articles/2025-02-09_samaltman-three-observations.md` — Sam Altmanの3つの観察：対数スケーリング則（intelligence ≈ log(resources)）、コストの10x/年低下（GPT-4→GPT-4oで150x）、超指数関数的価値。AIエージェントビジョン（ジュニアエンジニア比喩、100万体の仮想同僚）、2035年ビジョン（全員が無限の天才にアクセス）。

**New page created**:
- `concepts/altman-three-observations.md` — 包括的概念ページ（~120行）。3つの観察の詳細説明、AIエージェントビジョン、社会的影響（人間の主体性、科学進歩、財価格）、受容と分析、他フレームワークとの比較表（Scaling Laws/Moore's Law/Jevons Paradox/Eroom's Law）。フロントマターにaliases（three-observations, ai-economic-observations, altman-scaling-laws）を含む。

**Pages enriched**:
- `entities/sam-altman.md` — 「Three Observations (February 2025)」セクションを新設。3つの観察の要約表＋2035年ビジョンの引用＋概念的接続（[[altman-three-observations]]）。
- `concepts/scaling-laws.md` — Related Conceptsに[[altman-three-observations]]を追加。

**Index/log**: index.mdにconcepts/altman-three-observations追加。総ページ数: 5187→5188、Full entries: 4638→4639。

## [2026-05-07] Tim O'Reilly「The End of Programming as We Know It」記事取り込み

**Action**: kzinmrからのリクエストにより、O'Reilly RadarのTim O'Reilly記事「The End of Programming as We Know It」(2025-02-04) をwikiに取り込み。Vibe Coding勃興期の歴史的ランドマーク記事として位置づけ。

**New raw articles saved**:
- `raw/articles/2025-02-04_oreilly-end-of-programming.md` — Tim O'Reillyの「プログラミングの終焉」論。CHOP (Chat-Oriented Programming)パラダイム、プログラミング抽象化の歴史的進化、Jevons Paradox、Agent Engineerの新役割、エージェントインフラプロトコルの必要性、Addy OsmaniのThe 70% Problemの紹介。

**New page created**:
- `entities/tim-oreilly.md` — O'Reilly Media創業者のエンティティページ。Web 2.0命名者。CHOPパラダイム提唱、抽象化の歴史的文脈、Agent Engineer役割の予見、MCP/ACP/A2Aへの先駆的枠組みを含む。ステータス: complete。

**Pages enriched**:
- `concepts/harness-engineering/agentic-workflows/vibe-coding.md` — 「Tim O'Reilly の視点: CHOP パラダイムと歴史的文脈」セクションを新設（~50行）。抽象化の歴史的進化表、CHOP定義、Jevons Paradox、70% Problem比較表、Agent Engineer、エージェントインフラプロトコルを追加。関連概念にMCPを追加。参照にtim-oreilly、addy-osmaniを追加。
- `entities/addy-osmani.md` — 「The 70% Problem」セクションを新設。O'Reilly記事で大衆化された概念として位置づけ、AI vs 人間の役割比較表を含む。

**Index/log**: index.mdにentities/tim-oreilly追加。総ページ数: 5188→5189、Full entries: 4639→4640。

## [2026-05-08] QC (Qiaochu Yuan) Wiki取り込み — Societal Shadow + Re-encountering Language

**Action**: kzinmrからのリクエストにより、Qiaochu Yuanの2本のエッセイ（Core dump, Re-encountering Language）を統合的にwikiに取り込み。QCの理論（Core dump 2024）とその経験的基盤（Re-encountering Language 2023）を体系的に紐付け。

**New raw articles saved**:
- `raw/articles/2023-03-13_qchu-re-encountering-language.md` — QCの身体の言葉への最初のアクセス体験。2024年のCore dump理論の1年半前の自伝的基盤。詩への覚醒、feral selfの解放、社会の氷の下の地下河川。

**New entity page created**:
- `entities/qiaochu-yuan.md` — Mathematician, ex-MIRI researcher, Thicket Forte Substack著者。言語的めまい・head/body words・societal shadowの提唱者。知的系譜（Johnstone, Gendlin, Circling, Gwern, Jung, Bataille）をマッピング。Core dumpとRe-encountering Languageを二部構成として統合。

**New concept page created**:
- `concepts/societal-shadow.md` — RLHF禁止リストが社会の抑圧領域を可視化する逆説現象。知的系譜（Jungの影→Batailleの侵犯→Foucaultの権力→Kristevaのアブジェクシオン）を体系的にマッピング。技術的対応物（HH-RLHF Dataset, OpenAI Usage Policies, GPT-4 System Card）との接続。関連現象（Waluigi Effect, Sycophancy, Mode Collapse）。「Re-encountering Language」との経験的基盤の関係も包含。

**Pages enriched**:
- `concepts/linguistic-vertigo.md` — 「経験的前提：Re-encountering Languageと身体の言葉の発見」セクションを新設。理論 vs 経験の二部構成比較表。社会の影セクションに[[concepts/societal-shadow]]へのクロスリファレンスを追加。関連ページ・出典にqiaochu-yuanエンティティとsocietal-shadow概念を追加。

**Index/log**: index.mdにentities/qiaochu-yuan、concepts/societal-shadowを追加。linguistic-vertigoエントリを更新（societal-shadow/Raw Articleクロスリファレンス）。総ページ数: 5195→5198、Entities: 405→406、Concepts: 446→447。