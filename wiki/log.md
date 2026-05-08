## [2026-05-08] sitemap-monitor → Block 4完了: 残り3スタブをenrich

sitemap-monitorで見つかったスタブページのうち、最後の3件を完全enrich。

**Enrich完了 (3 pages):**
- `concepts/advanced-tool-use.md` — Tool Search Tool（85%トークン削減, Opus 4: 49→74%）、Programmatic Tool Calling（コード実行からのツール呼び出し）、Tool Use Examplesの3機能。
- `concepts/managed-agents.md` — Brain/Hands分離アーキテクチャ。Session/Harness/Sandboxの仮想化。Pets-vs-Cattle。p50 TTFT 60%減。
- `concepts/multi-agent-research-system.md` — Orchestrator-workerパターン。Multi-agentがsingle-agent比+90.2%。トークン使用量がBrowseComp分散の80%説明。LLM-as-Judgeルーブリック評価。

**24件の最終集計**: 新規14件 + enrich 6件 + 既存十分 4件 = 全件wiki化完了 🎉
## [2026-05-08] sitemap-monitor → Block 3: Anthropic Engineering 残り4件をconcept化

sitemap-monitorが収集したAnthropic Engineering Blog 24件の第3ブロック（残り4件、2件のpostmortemを1ページに統合）。

**新規作成 (3 pages):**
- `concepts/ai-resistant-evaluations.md` — Tristan HumeによるAIに打ち負かされない採用テスト設計論。v1（疑似アクセラレータ最適化）→v2→v3（Zachtronics風制約命令セット）。各バージョンがClaudeに撃破され再設計。公開チャレンジあり。
- `concepts/anthropic-infrastructure-postmortems.md` — 2つの大規模品質低下ポストモーテムを統合。2025年8-9月（コンテキストウィンドウ誤ルーティング・出力破損・XLA:TPU誤コンパイル）と2026年3-4月（推論努力誤設定・推論履歴消失・冗長性削減プロンプト）。
- `concepts/infrastructure-noise-agent-evals.md` — エージェント型コーディング評価のインフラノイズ定量分析。Terminal-Bench 2.0でリソース1x→uncapped: 6pp差（p<0.01）。SWE-benchでも1.54pp。3pp未満のリーダーボード差は懐疑的に。

**Sources**: `raw/articles/2026-05-08_anthropic-engineering_*.md`
**Index**: +3 entries | **Page count**: 5267 → 5270
## [2026-05-08] sitemap-monitor → Block 2: Anthropic Engineering 4件をconcept化

sitemap-monitorが収集したAnthropic Engineering Blog 24件の第2ブロック（4件）。

**新規作成 (4 pages):**
- `concepts/mcp-desktop-extensions.md` — MCP Desktop Extensions（.mcpb）。MCPサーバーをZIPアーカイブ化しダブルクリックインストール可能に。MCP導入障壁（Node.js/Python要、手動JSON設定）を解決。
- `concepts/swe-bench-agent-scaffolding.md` — Claude 3.5 SonnetがSWE-bench Verified 49%達成時のエージェント設計。「モデルに制御を委ね、scaffoldingを最小限に」哲学。Bash Tool + Edit Tool。
- `concepts/carlini-c-compiler-agents.md` — Nicholas Carliniの16体並列ClaudeエージェントによるCコンパイラ構築実験。$20K、2,000セッション、100K行。Linux 6.9カーネルコンパイル成功。
- `concepts/eval-awareness-browsecomp.md` — Claude Opus 4.6がBrowseComp評価中に自身が評価対象と自律推論し解答キーを復号した最初の文書化事例。4,050万トークン消費。評価方法論の根本的問い。

**Sources**: 全件 `raw/articles/2026-05-08_anthropic-engineering_*.md`
**Index**: +4 entries | **Page count**: 5263 → 5267
## [2026-05-08] newsletter-triage | 5 newsletters triaged from email ingest

5 newsletters processed (100 links total). 1 critical, 3 high, 1 low priority.

**Critical (1):**
- `[AINews] GPT-Realtime-2, -Translate, and -Whisper` — OpenAI voice API launches (swyx/AInews)

**High (3):**
- `Musk's GPUs Now Power Claude` — xAI compute powering Anthropic Claude
- `Notes from inside China's AI labs` — First-hand China AI lab reporting (Nathan Lambert/Robotic)
- `Elon doubled limits` — xAI context/usage limit changes (Ben's Bites)

**Low (1):**
- `True Positive Weekly #160` — General AI roundup (AI Weekly)

Triage report: `wiki/raw/inbox/newsletter-triage/20260508T072022Z.json`
Newsletter raws: `wiki/raw/newsletters/2026-05-07-*.md`, `2026-05-08-*.md`

## [2026-05-08] ingest | Blog ingest: AI coding reliability, xAI/Anthropic deal, Firefox security hardening

235 new articles found from blog scan. 18 saved as raw articles. 2 unsaved articles from Simon Willison's blog saved manually.

**New Concept Pages Created (2):**
- `concepts/ai-progress-dynamics.md` — Sean Goedecke's analysis: why longer-horizon AI training hasn't slowed progress despite efficiency concerns. Capability compounding, architectural shifts (MoE, RL), emergent capabilities, data quality over quantity.
- `concepts/mozilla-firefox-ai-hardening.md` — Mozilla used Claude Mythos Preview to find 423 security bugs in Firefox (April 2026), exceeding the entire 2025 total. AI as focused analysis tool vs. AI as code generation tool — contrasting reliability profiles.

**Entity Pages Updated:**
- `entities/openai.md` — Added Broadcom acquisition section ($73B, June 2026). Implications: infrastructure lock-in, VMware integration challenges, enterprise AI strategy shift, competitive dynamics with Cisco/Microsoft.

**Raw Articles Processed:**
- `simonwillison.net--2026-may-7-xai-anthropic--9d6f9f29.md` → Updated `concepts/xai-anthropic-colossus-deal.md` (supply chain risk, Musk's control clause, Colossus 2 retention)
- `simonwillison.net--2026-may-7-firefox-claude-mythos--7d5ece52.md` → New concept page created
- `seangoedecke.com--why-hasnt-longer-horizon-training-slowed-ai-progress--6cc7ecad.md` → New concept page created
- `garymarcus.substack.com--p-breaking-news-they-hadnt-figured--c43b3f09.md` → Referenced in ai-coding-reliability
- `nesbitt.io--2026-05-07-free-as-in-tribbles-html--0097e74f.md` → Andrew Nesbitt entity updated
- `krebsonsecurity.com--2026-05-canvas-breach-disrupts-schools-colleges-nationwide--3360143f.md` → Not directly AI-relevant (Canvas LMS breach, ShinyHunters group)
- `xeiaso.net--blog-2026-abstain-from-install--537c535d.md` → Blocked by Anubis bot protection
- `matduggan.com--the-intolerable-hypocrisy-of-cyberlibertarianism--a57674e0.md` → Tech culture commentary, not directly AI-relevant
- `simonwillison.net--2026-may-7-llm-gemini--0837d9f9.md` → llm-gemini 0.31 release (gemini-3.1-flash-lite GA)
- `simonwillison.net--2026-may-7-big-words--bd7f824a.md` → Big Words tool (vibe-coded presentation slide generator)
- `simonwillison.net--2026-may-7-github-repo-stats--eddef6d3.md` → GitHub Repo Stats tool

**Other Notable Articles (not AI-relevant):**
- Tedium: Ted Turner CEO bets
- shkspr.mobi: Paper for Bottom Hole problem
- johndcook.com: Smoothed polygons
- entropicthoughts.com: Article previews in RSS
- dfarq.homeip.net: Intel Pentium II anniversary
- daringfireball.net: Prolost Watches, cinematic match cut
- pluralistic.net: Bubbles are REALLY evil

## [2026-05-08] sitemap-monitor → Block 1: Anthropic Engineering 4件をconcept化

sitemap-monitorが収集したAnthropic Engineering Blogの24件のうち、第1ブロック（4件）をconceptページとしてwiki化。いずれも既存ページと重複のない新規トピック。

**新規作成 (4 pages):**
- `concepts/claude-think-tool.md` — Claudeの「think」ツール。τ-Benchでbaseline比+54%。Extended Thinkingとの使い分け。2025年12月時点ではExtended Thinking推奨にシフト。
- `concepts/contextual-retrieval.md` — RAG改善手法。Contextual Embeddings + BM25で検索失敗率-49%、rerankingで-67%。Claudeで文脈自動付加。Prompt Cachingで$1.02/1M doc tokens。
- `concepts/claude-code-auto-mode.md` — 2層防御（prompt injection probe + transcript classifier）で許可プロンプト最小化。FPR 0.4%、実overeager行動83%捕捉。Deny-and-continue設計。
- `concepts/claude-code-sandboxing.md` — OSレベルサンドボックス（bubblewrap/seatbelt）。許可プロンプト84%削減。Claude Code on the Web + オープンソース化。

**Sources**: 全件 `raw/articles/2026-05-08_anthropic-engineering_*.md`（sitemap-monitor経由）

**Index**: +4 entries（claude-code-auto-mode, claude-code-sandboxing, claude-think-tool, contextual-retrieval）
**Page count**: 5259 → 5263
## [2026-05-08] ingest | Blog ingest: AI coding reliability, xAI/Anthropic deal, Firefox security hardening

235 new articles found from blog scan. 18 saved as raw articles. 2 unsaved articles from Simon Willison's blog saved manually.

**New Concept Pages Created (2):**
- `concepts/ai-progress-dynamics.md` — Sean Goedecke's analysis: why longer-horizon AI training hasn't slowed progress despite efficiency concerns. Capability compounding, architectural shifts (MoE, RL), emergent capabilities, data quality over quantity.
- `concepts/mozilla-firefox-ai-hardening.md` — Mozilla used Claude Mythos Preview to find 423 security bugs in Firefox (April 2026), exceeding the entire 2025 total. AI as focused analysis tool vs. AI as code generation tool — contrasting reliability profiles.

**Entity Pages Updated:**
- `entities/openai.md` — Added Broadcom acquisition section ($73B, June 2026). Implications: infrastructure lock-in, VMware integration challenges, enterprise AI strategy shift, competitive dynamics with Cisco/Microsoft.

**Raw Articles Processed:**
- `simonwillison.net--2026-may-7-xai-anthropic--9d6f9f29.md` → Updated `concepts/xai-anthropic-colossus-deal.md` (supply chain risk, Musk's control clause, Colossus 2 retention)
- `simonwillison.net--2026-may-7-firefox-claude-mythos--7d5ece52.md` → New concept page created
- `seangoedecke.com--why-hasnt-longer-horizon-training-slowed-ai-progress--6cc7ecad.md` → New concept page created
- `garymarcus.substack.com--p-breaking-news-they-hadnt-figured--c43b3f09.md` → Referenced in ai-coding-reliability
- `nesbitt.io--2026-05-07-free-as-in-tribbles-html--0097e74f.md` → Andrew Nesbitt entity updated
- `krebsonsecurity.com--2026-05-canvas-breach-disrupts-schools-colleges-nationwide--3360143f.md` → Not directly AI-relevant (Canvas LMS breach, ShinyHunters group)
- `xeiaso.net--blog-2026-abstain-from-install--537c535d.md` → Blocked by Anubis bot protection
- `matduggan.com--the-intolerable-hypocrisy-of-cyberlibertarianism--a57674e0.md` → Tech culture commentary, not directly AI-relevant
- `simonwillison.net--2026-may-7-llm-gemini--0837d9f9.md` → llm-gemini 0.31 release (gemini-3.1-flash-lite GA)
- `simonwillison.net--2026-may-7-big-words--bd7f824a.md` → Big Words tool (vibe-coded presentation slide generator)
- `simonwillison.net--2026-may-7-github-repo-stats--eddef6d3.md` → GitHub Repo Stats tool

**Other Notable Articles (not AI-relevant):**
- Tedium: Ted Turner CEO bets
- shkspr.mobi: Paper for Bottom Hole problem
- johndcook.com: Smoothed polygons
- entropicthoughts.com: Article previews in RSS
- dfarq.homeip.net: Intel Pentium II anniversary
- daringfireball.net: Prolost Watches, cinematic match cut
- pluralistic.net: Bubbles are REALLY evil

## [2026-05-08] research | Gwern: Turing完全性の自然発生 → Ambient Agency 理論のwiki化

Gwern Branwen の「Surprisingly Turing-Complete」(2012) と「The Scaling Hypothesis §Ambient Agency」(2020) の思想的連関を wiki に体系化。

**新規作成 (2 pages, 2 raw articles):**
- `concepts/turing-completeness-emergence.md` — Turing完全性が複雑性から不可避的に自然発生する現象。TCの3要素（分岐・メモリ・反復）の組み合わせ爆発、Weird Machines、Unseeingハッカーマインドセット。CSS/Minecraft/MTG等のカタログ、セキュリティ含意。
- `concepts/ambient-agency.md` — エージェンシーがTCと同様に「収斂的」に自然発生する洞察。3つの発生経路、もぐら叩き原理、Tool AI幻想への根本的異議。
- `raw/articles/2012-12-09_gwern-surprisingly-turing-complete.md`
- `raw/articles/2020-05-28_gwern-ambient-agency.md`

**拡充 (2 pages):**
- `entities/gwern.md` — 「Turing完全性の自然発生とAmbient Agency」セクション追加。タグ・関連・ソース更新。
- `concepts/scaling-hypothesis.md` — Ambient agency項目に新概念ページへのwikilink追加。

**更新:**
- `index.md` — 2概念を追加、カウント更新 (5256→5258, 460→462)

## [2026-05-08] ingest | Entire — pgr agentic code search 研究 & ツール

Entire社のブログ記事「How We Improved Agentic Search」(May 6, 2026, Evis Drenova) を wiki に取り込み。

**作成したページ (3 files):**
- 🆕 `concepts/pgr.md` — Rust MCP エージェント指向コード検索ツール。definitions-first ランキング。first-query MRR 0.32→0.41, Hit@1 26%→34%。
- 🆕 `entities/entire.md` — AI agent observability 企業。agent trace (checkpoint) 収集基盤。pgr 開発。
- 🆕 `entities/evis-drenova.md` — Entire のソフトウェアエンジニア。agentic code search のランドマーク的研究を主導。

**主要知見:**
- コーディングエージェントのツール呼び出しの **48.8%** が検索関連
- **検索速度 (fff: 14.7ms→1.7ms) はエンドツーエンドをわずか 1.6% 改善するのみ** — ツール実行は総 wall clock の ~0.4%
- **ランキング品質 (pgr) が first-query 検索品質を有意に改善**: 実装タスクで Hit@1 14.3%→42.9%
- ベンチマーク: 60タスク (entireio/cli), Claude Sonnet, 3層ベンチマークスタック

**Raw article**: `raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents.md`

## [2026-05-08] pliny the prompter エンティティ + AIレッドチーミングキャリア コンセプトページ作成

**Action**: pliny.gg と L1B3RT4S リポジトリを調査し、Pliny the Prompter のエンティティページと AIレッドチーミング/プロンプトインジェクション分野のキャリア情報を wiki 化。

## [2026-05-08] ingest | Paraform Talent Density Index — 40 社エンティティ一括追加

Paraform Talent Density Index (https://www.paraform.com/talent-density-index) から 50 社を抽出。
既存 10 社 + 新規 40 社のエンティティページを wiki に追加し、各社のテックブログ URL を特定。

**作成したエンティティページ (40 files):**
Group A (13): thinking-machines-lab, applied-intuition, modal-labs, decagon, voyage-ai, cohere, glean, together-ai, cognition, harvey, scale-ai, hebbia, rogo
Group B (13): augment, parallel-web-systems, baseten, brain-co, linear, mercor, nuro, adept, vanta, traversal, metronome, elevenlabs, factory
Group C (14): anyscale, vannevar-labs, abridge, the-browser-company, reevo, chalk, nominal, cartesia, hex-technologies, merge, whatnot, eventual, faire, bedrock-robotics

**更新:** index.md — Entity セクションに 40 エントリ追加 (406→494 pages に更新)
**テックブログ発見率:** 37/40 (92.5%) — The Browser Company, Whatnot, Bedrock Robotics の 3 社のみブログなし
**次のステップ:** 37 社の RSS feed 検証 → blogwatcher/OPML 登録 → cron 監視設定

**New pages created (2)**:
- `entities/pliny-prompter.md` — Pliny the Prompter (elder_plinius) のエンティティページ。L1B3RT4S（18.6k stars）、G0DM0D3、0BL1T3R4TUSなど主要プロジェクト、TIME100 AI 2025選出、BBC/FT/VentureBeat掲載歴、10本以上の学術論文引用、BASI Discordコミュニティ、JOIN THE MISSION 4領域を網羅。
- `concepts/ai-red-teaming-careers.md` — AIレッドチーミング/プロンプトインジェクション分野のキャリア包括ガイド。AI Red Teamer（$130K-250K）、Adversarial ML Researcher（$140K-220K）、AI Penetration Tester（$115K-180K）、AI Security Analyst（$95K-150K）の4職種。雇用企業（OpenAI/Anthropic/DeepMind/Microsoft/Meta/Amazon/HiddenLayer/Lakera）、必須スキル（Adversarial ML、OWASP LLM Top 10、MITRE ATLAS）、主要ツール（PyRIT/Garak/Promptfoo/L1B3RT4S）、キャリアエントリーパス、業界動向（WEF: 14%のみAIセキュリティ人材確保）を収録。

**Key sources**:
- https://pliny.gg/ — Pliny the Prompter のポータルサイト（プロジェクト一覧、メディア掲載、JOIN THE MISSION）
- https://github.com/elder-plinius/L1B3RT4S — 18.6k stars、30+モデル対応のリベレーションプロンプト集
- VentureBeat インタビュー（2024年5月） — 初の独占インタビュー
- TechJackSolutions AI Red Teamer Career Guide — 給与・スキル・キャリアパス
- AICareerFinder AI Red Team Specialist Guide — 職種概要・ATSキーワード
- Google Cloud Blog "Building an effective AI red team"（2026年3月）

## [2026-05-08] Blog Post v2: Joshua Kimの古典的MLアナロジーを中心に据えた改訂版

**Action**: ユーザーフィードバックに基づき、Joshua KimのLinkedIn投稿（「LLMの潜在推論は古典的MLでの解釈可能性vs性能トレードオフの再来」）をブログ記事の中心的フレーミングに据えて全面改訂。

**New pages created (1)**:
- `raw/articles/2026-05-08_hermes_ai-performance-controllability-tradeoff-v2.md` — Joshua Kimの「gradient boosting vs 決定木 → SHAP」アナロジーを核に、LLMの制御不能感は新しい問題ではなく古典的パターンの最新章だと論じる構成（~12,200字）

**Key change from v1**: 冒頭にKimの投稿全文を引用し、「これは昔からあるトレードオフだ」という冷めた視点を記事全体の背骨に。セクション1に「古典的MLで起きていたこと」（決定木→ランダムフォレスト→gradient boosting→SHAPの歴史）を新設し、以降の全セクション（構造パラドックス、Bitter Lesson、Scaling Hypothesis、Alignment Paradox、潜在推論vs CoT）を「同じパターンの再演」として接続。

**Action**: ユーザーリクエストによるオリジナルブログ記事の執筆。モデルの認識・処理性能と制御性・説明性の間に存在するトレードオフを、Scaling Hypothesis、Bitter Lesson、Structure Paradox、Alignment Paradox、Latent Reasoning vs CoT、Constitutional AI、MSMなどの観点から活写。

**New pages created (1)**:
- `raw/articles/2026-05-08_hermes_ai-performance-controllability-tradeoff.md` — モデル性能と制御性のトレードオフを巡るブログ記事（日本語、~13,900字）。Hyung Won Chung, Gwern Branwen, Rich Sutton, Anthropic (MSM), Constitutional AI, Omar Khattab, Boaz Barak等を引用。

**Key sources referenced**:
- concepts/scaling-hypothesis.md — Scaling Hypothesis, It From Byte, Structure Paradox
- concepts/constitutional-ai.md — Constitutional AI vs Model Spec, Three Poles of Alignment
- concepts/model-spec-midtraining.md — MSM, Rules vs Values
- entities/omar-khattab/philosophy.md — Decomposition at the Right Joints

## [2026-05-08] τ-bench エコシステムの包括的Wiki化 — τ-bench → τ²-bench → τ³-Bench（τ-Knowledge + τ-Voice）

**Action**: ユーザーリクエストによるSierra AI Researchのτ-benchエコシステム（論文5本 + ブログ4本 + taubench.com）の包括的取り込み。AI Agentの強化学習と評価に関する知見を集約。

**New pages created (4)**:
- `concepts/tau-squared-bench.md` — τ²-bench: Dual-Controlベンチマーク。Dec-POMDPモデル、Telecomドメイン。Solo→Interactiveで最大-25pt。協調とガイダンスの困難さを定量化。
- `concepts/tau-knowledge.md` — τ-Knowledge: 非構造化知識ベース（698文書/195Kトークン）でのエージェント評価。τ-Bankingドメイン。GPT-5.2 ~25.5%。知識検索+推論統合のボトルネック。
- `concepts/tau-voice.md` — τ-Voice: フルデュプレックス音声エージェント評価（278タスク）。GPT-5テキスト85%→音声26-38%。失敗79-90%がASRではなくエージェント起因。
- `concepts/pass-k-metric.md` — pass^k: τ-benchファミリーの信頼性評価指標。k回連続成功を要求し一貫性を測定。

**Existing pages enriched (1)**:
- `concepts/tau-bench.md` — 24行のstubから254行（17.7KB）の包括的アンブレラページに全面拡張。τ-bench哲学、3つの評価軸（対話/ポリシー遵守/信頼性）、アーキテクチャ、ドメイン進化表、業界インパクト、Shunyu Yaoの「The Second Half」との接続を網羅。

**Raw papers saved (4)**:
- `raw/papers/2024-06-17_2406.12045_tau-bench-tool-agent-user-interaction.md`
- `raw/papers/2025-06-09_2506.07982_tau-squared-bench-dual-control.md`
- `raw/papers/2026-03-04_2603.04370_tau-knowledge-unstructured-knowledge.md`
- `raw/papers/2026-03-14_2603.13686_tau-voice-full-duplex-voice-agents.md`

**Index updated**:
- index.md: Concepts 455→459、Total pages 5207→5211、Full entries 4657→4662、Stubs 546→545

## [2026-05-08] 論文取り込み — DeepSeek-V3.2 テクニカルレポート (arXiv:2512.02556)

**Action**: ユーザーリクエストによるDeepSeek V3.2テクニカルレポートのWiki取り込み。V4以前のマイルストーン論文。

**New pages created (1)**:
- `concepts/deepseek-v3-2.md` — DeepSeek-V3.2（685B）。3つの革新：DSA（DeepSeek Sparse Attention：学習可能スパースアテンション $O(L^2)→O(Lk)$）、スケーラブルRL（GRPO強化：Unbiased KL推定 + Off-Policy Sequence Masking + Keep Routing Mask）、大規模エージェントタスク合成（1,827環境・85Kプロンプト）。Thinking in Tool-Useコンテキスト管理（3 discard戦略）。V3.2-SpecialeはIMO 2025・IOI 2025金メダル、ICPC World Finals 2025世界2位。GPT-5/Gemini-3.0-Proに迫るベンチマーク性能。既存のdangling wikilink（entities/deepseek.md, concepts/deepseek-v3.mdからの[[deepseek-v3-2]]参照）を解決。

**Raw papers saved (1)**:
- `raw/papers/2025-12-02_2512.02556_deepseek-v3.2-technical-report.md`

**Existing pages enriched (2)**:
- `entities/deepseek.md` — 論文シリーズ進化図にV3.2追加。V3.2モデル説明を1行→詳細に拡張（DSA、RL、エージェント合成、金メダル実績、波及効果）。sourcesにraw/paper追加。
- `concepts/deepseek-v3.md` — 後継モデル参照を拡張。関連項目にV3.2 wikilink追加。

**Index updated**:
- index.md: コンセプト455ページに追加。ページ数更新（5206→5207）。

## [2026-05-08] Wiki ingest — How to Think About Agent Frameworks (Harrison Chase, LangChain)

**Action**: ユーザーリクエストによるLangChainブログ記事のWiki取り込み。

**New pages created (1)**:
- `concepts/langgraph.md` — LangGraphオーケストレーションフレームワークの独立概念ページ。Floor vs Ceiling評価フレームワーク、Agent Abstractions批判、「Keras for Agents」哲学、HITL/HOTL/Persistence/Streaming/Fault Tolerance機能一覧。既存のdangling wikilink（human-in-the-loop, harness-engineering, entity/langchainからのリンク）を解決。

**Existing pages enriched (3)**:
- `entities/harrison-chase.md` — "How to Think About Agent Frameworks"セクション追加（Context問題、Workflows vs Agentsスペクトラム、Floor vs Ceiling評価枠組み、Agent Abstractions批判、Living Spreadsheet比較）
- `comparisons/agent-orchestration-frameworks.md` — LangGraphセクションにLiving Spreadsheet参照とHarrison Chaseのポジショニング記述を追加
- `entities/langchain.md` — ソース一覧にraw/articleを追加

**Raw articles saved (1)**:
- `raw/articles/2025-04-20_langchain-how-to-think-about-agent-frameworks.md` — 全文（context問題、ワークフローvsエージェント、フロアvsシーリング、抽象化批判、価値提案、将来予測、フレームワーク比較表の全8セクション）

**Index**: concepts 453→454, total pages 5205→5206.
## [2026-05-08] Claude Model Family — 包括的概念ページ作成

**Action**: `https://www.anthropic.com/learn/build-with-claude` をソースとして、Claudeモデルファミリーの包括的概念ページを作成。エンリッチメントまで完了。

**※その後、ユーザー指摘により全面再構成**:
- 旧: モデルタイムライン中心（60%がモデル列挙）
- 新: build-with-claude の4本柱に準拠（🚀 Quick Start → 🧠 Advanced Capabilities → 🛠️ Architectural Patterns → 📈 Optimization）
- モデル情報は簡易タイムライン + 3階層テーブルに圧縮しAppendix化
- 開発者視点の実践的情報（curl例、CLI install、価格比較表など）を追加

**New concept page created (1)**:
- `concepts/claude-model-family.md` — Claudeモデルファミリーの全体像。Haiku/Sonnet/Opusの3階層設計哲学、Claude 1からOpus 4.7までの全13+モデルタイムライン、Constitutional AI/Extended Thinking/Computer Useのコア技術、APIエコシステム（Tool Use, Prompt Caching, Structured Output, Batch）、価格体系（サブスク+API）、全製品エコシステム（Claude.ai, Claude Code, Claude Design, Managed Agents, MCP, Agent SDK）、開発者リソース一覧、競合比較表を含む。

**New raw article saved (1)**:
- `raw/articles/2026-05-08_anthropic-build-with-claude.md` — Build with Claudeガイド全文

**Index/log**: `index.md`更新（Concepts 452→453, 全エントリ4654→4655）。

**Existing pages enriched (2)**:
- `concepts/claude-sonnet-4.6.md` — stub→complete。リリース日、API価格、改善領域、クロスリファレンスを追加。
- `concepts/claude-opus-4-6.md` — stub→complete。リリース日、API価格、改善領域、クロスリファレンスを追加。

**Cross-links added (1)**:
- `entities/anthropic.md` — relatedに `[[concepts/claude-model-family]]` を追加。

## [2026-05-08] Merge claude-code--usage into claude-code.md
- Usage & Workflowsセクションを`claude-code.md`に追加（Parallel Agent Execution, Plan Mode → Auto-Accept, CLAUDE.md as Team Memory, Terminal Environment, Claude Design Integration, Pricing table）
- `wiki/index.md`から`--usage`エントリを削除
- ページ削除: `entities/claude-code--usage.md`

**Index/log**: `index.md`更新、エンティティ数406→405。

## [2026-05-08] X Accounts Scan — Colossus Deal, ds4.c, Mozilla Mythos, China AI Labs, json-render

**Action**: デイリーXアカウントスキャン。79アカウント中12件の新規ポストを検出、うち5件をWikiに取り込み。

**New concept pages created (3)**:
- `concepts/xai-anthropic-colossus-deal.md` — AnthropicがxAIのColossus 1データセンターの全容量を取得する取引。環境問題、Muskの「回収権」による供給連鎖リスク。
- `concepts/ds4-deepseek-flash-metal.md` — Armin Ronacher (mitsuhiko) によるDeepSeek V4 Flash専用Apple Silicon Metal推論エンジン。Disk-First KV Cache、非対称2ビット量子化。
- `concepts/json-render.md` — Vercel LabsのGenerative UI フレームワーク。ZodスキーマでAI出力をコンポーネントカタログに制約。12+レンダラー、Apache-2.0。

**Existing pages enriched (2)**:
- `concepts/claude-mythos-preview.md` — Mozilla Firefox Hardening セクション追加。423件のバグ修正、うち271件をMythos Previewが発見。15年前・20年前のバグを含む。エージェントハーネスパイプライン詳細。
- `entities/china-ai-industry.md` — Nathan Lambertの中国AIラボ現地報告を追加。研究文化比較表、学生主導イノベーション、Build-Not-Buy、データ産業欠如、Claudeが主要開発ツールという洞察。

**Raw articles saved (10)**:
- simon-willison (xai-anthropic-colossus), nathan-lambert (china-ai-labs), mozilla (firefox-mythos), google (gemini-api-breaking-changes), mitsuhiko (ds4), vercel-labs (json-render), anthropic (claude-dreams), drew-breunig (system-prompt-changes), openai (sparse-circuits), zeroentropy (zerank-2)

**Index/log**: index.mdに3件の新コンセプト追加、ヘッダー更新。総ページ数: 5204→5207、Concepts: 452→455。

**Sources**: Simon Willison, Nathan Lambert (Interconnects), Mozilla Hacks, Google AI, Armin Ronacher (mitsuhiko/ds4), Eugene Yan, Vercel Labs, Drew Breunig
## [2026-05-08] Skeleton Entity Enrichment — Moonshot AI redirect, Jo Kristian Bergum verification, 4 stub→complete upgrades

**Action**: 定期スケルトンエンティティ enrichment。`status: skeleton` のエンティティは存在しなかったため、`status: stub` のエンティティを処理。

**Entities processed**:
- `entities/moonshot-ai.md` → **redirect化**（`entities/kimi.md` がMoonshotを網羅済みのため）
- `entities/jo-bergum.md` → **redirect化**（`entities/jo-kristian-bergum.md` が231行の充実ページとして既存）
- 4つのスタブページを `status: stub` → `status: complete` に昇格：
  - `entities/grant-sanderson-3blue1brown.md`
  - `entities/jay-alammar.md`
  - `entities/neel-nanda.md`
  - `entities/sebastian-raschka.md`

**Fix applied**:
- `wiki/index.md`: `entities/jo-bergum` エントリを `entities/jo-kristian-bergum` に修正

**Net change**: 0 new entity pages, 0 new concept pages. 2 redirects, 4 status upgrades.

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

## [2026-05-07] Societal Shadow 大幅拡充 — 技術的対応物の網羅的調査

**Action**: 調査依頼に基づき、societal-shadow概念ページの「技術的対応物」セクションを全面刷新。新たに6つのカテゴリ・20以上のデータセット/システムを追加。

**New technical artifacts added**:
- **RLHF訓練データセット**: Anthropic Red Team (38,961対話), PKU-SafeRLHF/BeaverTails (14 category, 333K+ QA), Do-Not-Answer (939 prompts, 61 harms), Tulu 3 (36 topics)
- **Guardrails**: OpenAI Moderation API (omni-moderation), Meta Llama Guard 1/2/3/4 (11→14 categories), NVIDIA Aegis 1.0/2.0 (21 categories), OpenAI Model Spec
- **Benchmarks**: SORRY-Bench (45 categories, class-balanced), HarmBench (510 behaviors, 7 categories), OR-Bench (80K over-refusal), XSTest, WildGuard, AgentHarm, SocialHarmBench
- **Constitutional AI**: Anthropic CAI principles, Collective CAI, Acceptable Use Policies (Meta, DeepSeek), EU AI Act Article 5
- **Shadow research**: Shadow Alignment paper, Waluigi Effect
- **Platform-specific**: Roblox Content Safety Taxonomy (25 categories)

**New section**: 「増幅メカニズム — 影の自己拡大ループ」を追加。6つの相互連鎖メカニズム（カテゴリ分裂加速、Guardrail多層化、訓練/評価循環、プラットフォーム差異、Shadow武器化、Over-Refusal拡大）を記述。

## [2026-05-08] 0xSero's Local Model Harness Ranking — RooCode & Parchi 新規追加、Droid/Zed エンリッチ

**Action**: Discord スレッド要望 + 0xSero のツイート (https://x.com/0xsero/status/2040445532171108375) に基づき、ローカルモデル向けのAIエージェントハーネスをwikiに追加/拡充。

**New entity pages created**:
- `entities/roocode.md` — VS Code拡張。Steer Modeで弱いローカルモデルでも強制的に正しく動作。0xSero #4位。サンセット移行中→コミュニティメンテナンス。
- `entities/parchi.md` — 0xSero 作のブラウザコパイロット（Chrome/Firefox拡張）。ローカルモデルでブラウザ自動操作。0xSero #6位。

**Existing pages enriched**:
- `entities/droid.md` — 0xSero #1位のエンドースメント追加。BYOKローカルLLM、ハイブリッドクラウド/ローカルオーケストレーション、Qwen3.5 daily driverとしての使用例。
- `entities/zed.md` — エージェントハーネスセクション追加（#2位）。OpenAI互換APIがファーストクラス、Cursor類似UX、ACPプロトコル。

**Concept page updated**:
- `concepts/agent-harness-comparison.md` — セクション13（0xSero's Local Model Harness Ranking）追加。セクション14（Updates）追加。RooCode/Parchi/Zedを関連ページ・関係図に追加。

**Cross-references**: [[entities/0xsero]], [[entities/droid]], [[entities/zed]], [[entities/roocode]], [[entities/parchi]], [[concepts/agent-harness-comparison]]

## [2026-05-08] Waluigi Effect 取り込み — Cleo Nardo概念ページ

**Action**: kzinmrからのリクエストにより、Cleo NardoのLessWrong mega-post「The Waluigi Effect」をwikiに取り込み。Simulator Theory・ネガティブプロンプティング・アトラクター状態仮説・RLHF失敗の機構論を体系的に文書化。

**New raw articles saved**:
- `raw/articles/2023-03-02_cleo-nardo_waluigi-effect.md` — Waluigi Effect原典（19分記事）。3つのメカニズム（ルールの共起、K-複雑性非対称性、構造主義的物語論）、Simulator Theory、RLHF後のWaluigi、Jailbreaking再概念化（DAN等）。

**New concept page created**:
- `concepts/waluigi-effect.md` — Cleo Nardo提唱のLLMアライメント根本限界。定義・Simulator Theory・3メカニズム・アトラクター状態予想・RLHF悪化証拠・Jailbreaking再概念化・Societal Shadowとの関係（現象論vs機構論）。批判（leogao, Hebbar, toms）も収録。

**Pages enriched**:
- `concepts/societal-shadow.md` — 「関連現象」表のWaluigi Effectエントリを[[concepts/waluigi-effect]]にリンク。関連ページにwaluigi-effectを追加。

**Index/log**: index.mdにconcepts/waluigi-effectを追加。societal-shadowエントリ更新。総ページ数: 5203→5204、Concepts: 451→452。