# Wiki Log Archive


## 2026-05-13 11:30 UTC — X Bookmarks Ingest

**Source**: X bookmarks pipeline (2 bookmarks, x-bookmarks-ingest cron)

### Pages Created
- 🆕 `entities/kyle-jeong.md` — Kyle Jeong entity page (Growth Engineer at Browserbase, writes about AI infra: Firecracker, agent sandboxing, Kubernetes)
- 🆕 `entities/david-fowler.md` — David Fowler entity page (Distinguished Engineer at Microsoft, Aspire, NuGet, SignalR)

### Pages Enriched
- ✏️ `concepts/firecracker.md` — Upgraded from stub (24 lines) to full page (~100 lines). Added architecture details, isolation problem analysis, agent infra company usage, Firecracker vs gVisor comparison table, history. Source: Kyle Jeong's X Article.

### Raw Articles Saved
- `raw/articles/2026-05-11_kylejeong_firecracker-agent-infra.md` — metadata-only (X Article behind auth wall, blog mirror not found)
- `raw/articles/2026-05-12_davidfowl_ai-made-us-faster.md` — metadata-only (X Article behind auth wall, no mirror found)

### Index Updates
- index.md: +3 indexed entries (firecracker concept, kyle-jeong entity, david-fowler entity)
- Concepts: firecracker added
- Entities: kyle-jeong, david-fowler added

### Notes
- Both bookmarks were X native articles (x.com/i/article/...) with no external URLs. Blog mirror for Kyle's article could not be resolved (403/404). David Fowler's article has no mirror.
- Firecracker stub was already present (created 2026-04-25) — enriched rather than duplicated.

## 2026-05-13 10:00 UTC — INTELLECT-2 paper ingestion + model entity page

- **📄 論文保存**: `wiki/raw/papers/2025-05-12_2505.07291_intellect-2-decentralized-rl.md` — arXiv:2505.07291 (May 12, 2025), 26 pages
- **📄 モデルエンティティ新規作成**: `[[entities/intellect-2]]` — 32B reasoning model, first globally distributed RL training run. GRPO with two-sided clipping. Infrastructure: PRIME-RL + SHARDCAST + TOPLOC. 285K verifiable tasks (NuminaMath-1.5, Deepscaler, SYNTHETIC-1). Outperforms QwQ-32B. Apache 2.0. 14 co-authors including Fares Obeid (Grad).
- **📋 Prime Intellectページ更新**: ModelsセクションをINTELLECT-2/3の論文準拠の詳細にアップグレード。Related Pagesにintellect-2追加。
- **📋 Index更新**: intellect-2エンティティ追加（+1ページ、+580 entities）。

## 2026-05-13 09:45 UTC — Grad page consolidation: merge duplicate into entities/grad

- **🔄 統合**: `@Grad62304977` の重複ページを整理。
  - **削除**: `entities/grad62304977.md`（33行の劣化複製）→ `entities/grad.md`（200行の既存決定版）に統合
  - **削除**: `concepts/fares-obeid-grad62304977.md`（24行スタブ）→ entities/grad.md に本名情報を統合済み
  - **更新**: `entities/grad.md` — `updated`日付、`researcher`/`pseudonymous`/`reinforcement-learning`タグ追加、Prime Intellect同僚クロスリンク追加
  - **修正**: `entities/prime-intellect.md` — grad参照を `[[entities/grad|Fares Obeid (Grad)]]` に修正
- **📋 Index**: grad62304977エントリ削除、カウント調整（-2ページ、-1エントリ）
- **教訓**: wiki作成前に `search_files` で重複チェック必須。entities/grad.md は `grad` というファイル名で存在していた。

## 2026-05-13 09:30 UTC — FIX: Restore overwritten Prime Intellect people pages

- **🔄 上書き復元**: 3名の既存エンティティページをgit履歴から復元し、Prime Intellectクロスリンクのみ追加。
  - `[[entities/will-brown]]` — 203→206行に復元。vincent-weisser, florian-brand, elie-bakouch へのクロスリンク追加。
  - `[[entities/florian-brand]]` — 183行に復元。空白のRelated Peopleスロットをvincent-weisser, will-brown, elie-bakouch で埋める。
  - `[[entities/elie-bakouch]]` — 140→144行に復元。Prime Intellectへの移籍を反映（formerly HuggingFace）。Related WikilinksにPrime Intellect同僚追加。
- **⚠️ 教訓**: ページ作成前に `search_files` で既存ページの有無を必ず確認。ファイル名だけでなくindex.mdのエントリもチェック。
- **📋 SCHEMA更新**: `researcher`, `pseudonymous` タグ追加（前回コミットから継続）。

## 2026-05-13 09:15 UTC — Prime Intellect people entity pages + cross-links

- **📄 エンティティページ新規作成**: 5名のPrime Intellect関係者ページを新規作成し、[[entities/prime-intellect]]にクロスリンク。
  - `[[entities/vincent-weisser]]` — Co-founder & CEO (@vincentweisser, 29K followers)
  - `[[entities/will-brown]]` — Research, "reward hacking" (@willccbb, 43.5K followers). PhD Columbia. prime-rl/verifiers creator.
  - `[[entities/florian-brand]]` — Research Engineer, evals (@xeophon, 13.2K followers). Interconnects editor.
  - `[[entities/elie-bakouch]]` — Training LLMs (@eliebakouch, 15K followers). Previously HuggingFace (SmolLM, FineWeb).
  - `[[entities/grad62304977]]` — Pseudonymous RL researcher (@Grad62304977, 9K followers). GRPO, reward engineering.
- **📋 Prime Intellectページ更新**: Key Peopleセクションを全文クロスリンクにアップグレード。Related Pagesに全5名を追加。
- **📋 Index更新**: 5エンティティをindex.mdに追加。

## 2026-05-13 11:00 UTC — Active Crawl | GNAP + AEM + InclusionAI Ring-2.6-1T (4 wiki pages + 3 raw articles)

- **📄 概念ページ新規作成**: `[[concepts/gnap-git-native-agent-protocol]]` — Git-Native Agent Protocol: farol-teamの軽量オープンソースプロトコル。git repoを共有する4つのJSONファイルでAIエージェントチームを調整。ゼロサーバー、ゼロデータベース。MCP/A2Aと補完的。
- **📄 概念ページ新規作成**: `[[concepts/aem-adaptive-entropy-modulation]]` — Baidu/Tsinghua 2026: マルチターンエージェントRLのための教師なしクレジット割当手法。応答レベルのエントロピー変調で探索/活用トレードオフを適応制御。SWE-bench-Verifiedで+1.4%。
- **📄 エンティティページ新規作成**: `[[entities/inclusionai]]` — AI企業。エージェント最適化LLMを開発。RingモデルシリーズをOpenRouterで無料提供。
- **📄 エンティティページ新規作成**: `[[entities/ring-2-6-1t]]` — 1T MoE思考モデル（63B活性化）。コーディングエージェント、ツール使用、長時間タスク用。2026年5月8日リリース。OpenRouter無料。
- **📄 生記事保存**: `raw/articles/2026-05-13_gnap-git-native-agent-protocol.md`, `raw/articles/2026-05-13_aem-adaptive-entropy-modulation.md`, `raw/articles/2026-05-13_inclusionai-ring-2-6-1t.md`
- **📋 Index更新**: 4ページをindex.mdに追加。セクションカウント更新（Entities: 580, Concepts: 1252）。
- **🔍 ソース**: arXiv:2605.00425, github.com/farol-team/gnap, openrouter.ai/inclusionai/ring-2.6-1t:free

## 2026-05-13 09:00 UTC — Prime Intellect entity + renderers concept pages

- **📄 エンティティページ新規作成**: `[[entities/prime-intellect]]` — Prime Intellect社の包括的エンティティページ。2023年創業、$20.5M資金調達（Founders Fund, Andrej Karpathy, Clem Delangue, Tri Dao）。Lab（RLポストトレーニングプラットフォーム）、Environment Hub（2,500+ RL環境）、Compute（分散GPUマーケットプレイス）。オープンソース: renderers, verifiers, prime-rl。INTELLECT-1/2/3モデルシリーズ。
- **📄 概念ページ新規作成**: `[[concepts/renderers-token-level-templating]]` — Prime Intellectがオープンソース化したtoken-level templatingライブラリの詳細概念ページ。MITO→Generic TITO→renderersの3段階進化、bridge_to_next_turn、3x training efficiency、Token-In/Token-Outパラダイム、harness境界との相互作用。
- **📄 生記事保存**: `wiki/raw/articles/2026-05-12_primeintellect_renderers-token-level-templating.md` — Prime Intellectブログ記事全文（22KB）。
- **📋 SCHEMA更新**: `chat-template` タグをTechniquesカテゴリに追加。
- **📋 Index更新**: エンティティと概念をindex.mdに追加。

## 2026-05-13 08:15 UTC — RLM v3 paper update and wiki refresh

- **Updated:** `wiki/raw/papers/2025-12-31_2512.24601_recursive-language-models.md` — Replaced v2 with v3 (May 11, 2026). Added: depth>1 experiments (depth=0-3), OpenCode & Claude Code baseline comparisons, MRCRv2 length generalization results, OOLONG prompting case study, expanded error analysis (§5 — syntax errors, decomposition mistakes, first-decomposition importance), 6-appendix summary, and full results tables for GPT-5 and Qwen3-Coder-480B-A35B.
- **Updated:** `wiki/concepts/rlm-recursive-language-models.md` — Version bumped to v3. Added: V3 New Findings section (Recursion Depth Scaling, OpenCode & Claude Code Comparisons, MRCRv2 Length Generalization, Error Analysis & Prompting Case Study), updated Benchmark Performance with full v3 tables (depth=0-3, OpenCode, Claude Code), updated RLM-Qwen3-8B training details, expanded Limitations (7 items with v3 context).
- **Key v3 findings:** Depth=3 achieves 76.0% on OOLONG-Pairs (31% improvement over depth=1); RLM training generalizes from 64K→1M context on MRCRv2; coding agents (OpenCode/Claude Code) lag far behind RLMs on information-dense tasks despite context offloading.
- **Sources:** arXiv:2512.24601v3

## 2026-05-12 07:50 UTC — Blog Wiki Ingest | 4 reference updates from blog triage

- Updated `concepts/harness-engineering/agentic-engineering.md`: Added "Emerging Practices (May 2026)" section with 3 subsections — James Shore maintenance cost economics (velocity gains must match inverse maintenance cost reductions), Shopify River Lehrwerkstatt case study (public-by-default agent interactions in Slack), LLM shebang pattern (plain-text as executable agent scripts). Added 3 raw article sources.
- Updated `entities/openai.md`: Added "ChatGPT Adoption Metrics (Q1 2026)" section — gender parity reached, 35+ age group gaining share, geographic spread into LatAm/APAC/Africa, health documentation as fastest-growing workplace task. Scope note: excludes Codex and enterprise. Added 1 raw article source.

- **2026-05-13**: Cross-synthesis enrichment — integrated Armin Ronacher's "Agents Built for Agents Building Agents" Pi philosophy (lucumr.pocoo.org, Jan 2026) with the Hugo+Ivan workshop pages. **Enriched concepts/agents-that-build-themselves.md**: added "Armin Ronacher's Perspective" section — session trees, extension state in sessions, no-MCP philosophy, write→reload→test→loop pipeline, Software Building Software lived experience. **Enriched entities/pi.md**: added "Agents Built for Agents Building Agents" section with session trees, extension state persistence, no-MCP philosophy, Armin quotes. **Enriched entities/armin-ronacher.md**: added "Pi Experience" section bridging Pi philosophy to Hugo+Ivan's Pure Python workshop. Source: raw article `lucumr.pocoo.org--2026-1-31-pi--0eb410a7.md` (already ingested).
## 2026-05-13 07:45 UTC — Lance Martin「Learning the Bitter Lesson」取り込み

## 2026-05-13 - Blog Ingest

### Updated Entity Pages
- **[ed-zitron](entities/ed-zitron.md)**: Added "Data Center Construction Investigation (May 2026)" section covering Zitron's investigative analysis of hyperscaler data center claims, finding significant discrepancies between announced and operational capacity. Microsoft's 4GW claim traced to only ~342MW verified. Stargate Abilene far below 1.2GW promised. CoreWeave contracted vs. operational power obfuscation pattern identified.
- **[jeff-geerling](entities/jeff-geerling.md)**: Added "Bambu Lab and Open Source Social Contract (May 2026)" section documenting Geerling's critique of Bambu Lab threatening an OrcaSlicer fork developer with legal action over AGPLv3-compliant code use. Louis Rossmann pledged $10K to defend the developer.
- **[simon-willison](entities/simon-willison.md)**: Expanded May 2026 Updates with Mitchell Hashimoto's TDM motivations analysis ("90% motivated by NOT GETTING FIRED") and Mo Bitar's "Ralph Loop" satire on enterprise AI adoption patterns.

- **Raw記事保存**: `wiki/raw/articles/2025-07-30_rlancemartin_bitter-lesson-ai-engineering.md` — Lance Martinのブログ記事。Rich SuttonのBitter LessonをAIエンジニアリングに応用。open-deep-researchの事例研究（構造の追加→ボトルネック→削除のサイクル）。Hyung Won Chungの「構造を加えて後で取り除く」フレームワーク。
- **📄 概念ページ拡充**: `[[concepts/rich-suttons-bitter-lesson]]` — stub→complete。Rich Suttonの原典（2019）、各ドメインでの歴史的事例表、Hyung Won Chungのフレームワーク、Lance MartinのAIエンジニアリング応用（open-deep-researchケーススタディ）、3つの実践的教訓、エージェントハーネスへの含意。
- **📋 Entity更新**: `[[entities/lance-martin]]` — sourcesに新規raw記事を追加。
- **📋 Index更新**: `wiki/index.md` に `rich-suttons-bitter-lesson` を追加。

## 2026-05-13 08:15 UTC — RLVR概念ページ + o1/o3→GPT-5統合タイムライン + MCP実用的起源 (3ページ新規作成)

- **📄 概念ページ新規作成**: `[[concepts/rlvr]]` — RLVR (Reinforcement Learning with Verifiable Rewards) の包括的概念ページ。GRPOとの標準ペアリング、test-time-scaling連関、検証器の設計空間（3類型）、ART·E $80ケーススタディ、o1→o3 10x RL compute scaling、RLHF/DPOとの比較。27KB調査ベース。
- **📄 概念ページ新規作成**: `[[concepts/openai-o-series-gpt5-unification]]` — o1 (Sep 2024)→o3 (Dec 2024)→Altmanロードマップ転換でo3キャンセル (Feb 2025)→GPT-5統合 (Aug 2025)の完全タイムライン。GPT-5の3コンポーネントアーキテクチャ、戦略的理由（モデルピッカー複雑化+DeepSeek R1競合）。
- **📄 概念ページ新規作成**: `[[concepts/mcp]]` — MCP (Model Context Protocol) の包括的概念ページ。David Soria Parraの個人フラストレーション起源（copy-paste地獄）とJohn Welshの組織カオス（integration chaos）の2層起源ストーリー。M×N問題、3プリミティブ、業界タイムライン。
- **🏷️ SCHEMA更新**: `rlvr`, `test-time-scaling` をTechniquesタグ分類に追加。
- **📋 Index更新**: 3エントリ追加、staleな `mcp-protocol` + `model-context-protocol-mcp` を統合置換。

## 2026-05-13 08:00 UTC — Lance MartinのAIE 2025まとめを取り込み + ambient-agents概念ページ作成

- **Raw記事保存**: `[[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]]` — AI Engineer World's Fair 2025現地レポート。5大テーマ: Ambient Agents, Agent UX/Bitter Lesson論争, Agent Training (RLVR, Art-E $80), Agent Tools (MCP起源), Agent Evaluation。
- **📄 概念ページ新規作成**: `[[concepts/ambient-agents]]` — チャットUIなしの非同期的自律実行AIエージェントパラダイム。Devin, Codex, Windsurf, Claude Code事例、Solomon Hykes 4要件、AIE 2025主要テーマ。
- **✏️ エンティティページ拡充**: `[[entities/ai-engineer-youtube]]` — Flagship Eventsセクション新設（World's Fair 2025の5テーマ表 + 2026予告）、sources/tags更新。
- **✏️ エンティティページ更新**: `[[entities/lance-martin]]` — Blog/Recent PostsにAIE 2025記事追加、tags/sources更新。
- **🏷️ SCHEMA更新**: `ambient-agents`, `agent-training` をAI Agentsタグ分類に追加。

## 2026-05-13 07:40 UTC — AI Engineer YouTubeチャンネルを監視対象に追加

- **🔧 監視設定**: `config/feeds/blogs.opml` に YouTube Channels セクションを新設し、AI Engineer (@aiDotEngineer) のRSSフィードを追加。`blogwatcher-cli add` でDB登録、初回15件を既読化。
- **📄 エンティティページ新規作成**: `[[entities/ai-engineer-youtube]]` — 466K登録者、700+ talks。AI Engineerカンファレンスシリーズ（World's Fair, Summit, Code）の公式YouTubeチャンネル。主要トーク、コンテンツテーマ、Wiki関連性を記載。
- **📋 Index更新**: `wiki/index.md` にエンティティ追加。

## 2026-05-13 05:15 UTC — Claude Code Agent SDK セッション管理 + Context Engineering 実装分析

- **Raw記事保存**: `wiki/raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions.md` — Anthropic公式ドキュメント「Work with sessions」。continue/resume/fork の3操作による会話履歴の永続化・復元・分岐。`~/.claude/projects/<encoded-cwd>/*.jsonl` への自動永続化、`ClaudeSDKClient`（Python）、`continue: true`（TypeScript）、クロスホストセッション復元。
- **✏️ 概念ページ拡充**: `[[concepts/harness-engineering/context-engineering]]` — 「Claude Code Agent SDK: Context Engineering の SDK 実装」セクションを新設。Continue/Resume/Fork を Martin の Write/Select/Compress/Isolate フレームワークに対応付け。会話状態とファイル状態の関心の分離（Offload）、Bitter Lesson の対極としての基盤プリミティブのSDK吸収を分析。
- **🔧 エンティティページ更新**: `[[entities/claude-code]]` — Session Management セクションを新設（Continue/Resume/Fork 操作の詳細、Context Engineering フレームワークとのアーキテクチャ対応表、クロスホスト運用、設計上の含意）。sources と updated を更新。

## [2026-05-13] refactor | Harness Engineering blog unified boundary framing
- id: blog-harness-engineering-boundary-refactor-2026-05-13
- summary: Refactored the Harness Engineering survey around a unified boundary-interface framing, integrating Context Engineering, Action-oriented harness design, Agent Trace/Open Eval, open harness ownership, RLM-based learned context management, and anti-harness counterarguments into one coherent arc.
- touched:
  - [[blog/2026-05-12_hermes_harness-engineering-from-coding-agents-to-general-agents]]
  - [[concepts/harness-engineering]]
  - [[concepts/harness-engineering/context-engineering]]
  - [[concepts/rlm-recursive-language-models]]
  - [[concepts/unharnessed-agents]]

- **2026-05-13**: Discord user request → ingested Claude Code `/goal` documentation page. **New page**: `concepts/claude-code-goal.md` — Goal-driven autonomous workflow via prompt-based Stop hook + evaluator model (Haiku). Architecture comparison with Codex /goal, /loop, Stop hooks. Condition writing best practices. Lifecycle diagram. Non-interactive mode support. **Enriched**: `concepts/agentic-loop.md` — added Claude Code /goal as named variant in comparison table + Related Concepts link. **Raw articles**: `2026-05-13_anthropic_claude-code-goal.md` (6.2KB). Index: +1 entry. Tags: claude-code, coding-agents, agent-loop, autonomous-agents, anthropic, prompt-caching, tool-use.

- **2026-05-13**: Discord user request → ingested "Build Your Own Deep Research Agent" workshop (Ivan Leo, Google DeepMind + Hugo Bowne-Anderson, Mar 2026). **New page**: `concepts/deep-research-agent-from-scratch.md` — 10-step build pipeline from raw Gemini API to full research agent with phase swapping (plan/execute modes), deterministic guardrails, dynamic subagent spawning (Exa parallel search), OpenTelemetry tracing. **Enriched**: `entities/ivan-leo.md` (added Deep Research Agent Workshop section with 10-step breakdown), `entities/hugo-bowne-anderson.md` (enhanced collaboration description). **Raw articles**: 2026-03-28_youtube_deep-research-agent-workshop.md (27.6KB), 2026-03-28_github_deep-research-agent-readme.md (2.3KB). Index: +1 page (1782→1783), +1 entry (836→837).
## 2026-05-13 04:50 UTC — Lance Martin Context Engineering for Agents 生記事保存 + 概念ページ拡充 + ブログ監視追加 + 相互リンク

- **Raw記事保存**: `wiki/raw/articles/2025-06-23_rlancemartin_context-engineering-for-agents.md` — Lance Martin による Context Engineering のマイルストン記事。4バケット分類（Write/Select/Compress/Isolate）を提唱。Anthropic/Claude Code/Manus/Cognition/Windsurf/ChatGPT等の実例を交えた包括的フレームワーク。
- **✏️ 概念ページ拡充**: `[[concepts/harness-engineering/context-engineering]]` — Lance Martin の Write / Select / Compress / Isolate 4バケット分類セクションを新設。各バケットの詳細（Write: スクラッチパッド+長期記憶、Select: ツール選択RAG+メモリ検索+知識選択、Compress: 要約+トリミング、Isolate: マルチエージェント+サンドボックス+State分離）と Anthropic 3戦略との対応表を含む。さらに Reduce/Offload/Isolate への進化マッピングを追加。source: `raw/articles/2025-06-23_rlancemartin_context-engineering-for-agents.md`
- **🔗 相互リンク**: `[[concepts/reduce-offload-isolate]]` ↔ `[[concepts/harness-engineering/context-engineering]]` — 4バケット→3原則の進化マッピングを双方向に追加
- **🔧 エンティティページ更新**: `[[entities/lance-martin]]` — sourcesに生記事を追加、updatedを2026-05-13に更新
- **📡 ブログ監視追加**: Lance Martin (`rlancemartin.github.io`) を OPML + blogwatcher DB に追加。RSSフィード: `http://rlancemartin.github.io/feed.xml`。初回スキャン: 10記事（既読化済み）
- **Raw記事保存**: `wiki/raw/articles/2026-01-09_rlancemartin_agent-design-patterns.md` — Lance Martin による Agent Design Patterns。Context Engineering の拡張として7つのデザインパターン（Give Agents A Computer, Multi-Layer Action Space, Progressive Disclosure, Offload Context, Cache Context, Isolate Context, Evolve Context）を体系化。Manusのcache hit rate最重要指標、Ralph Wiggum loop、RLMによるcontext management吸収予測などを含む。source追加: `[[concepts/harness-engineering/context-engineering]]`, `[[concepts/reduce-offload-isolate]]`, `[[entities/lance-martin]]`

## 2026-05-13 04:55 UTC — Jeff Huber / Harness Engineering 対談取り込み + Inner/Outer Loop 拡張

- **Raw記事保存**: `wiki/raw/articles/2026-03-04_hugobowne_harness-engineering-agent-context.md` — Hugo Bowne-Anderson による Vanishing Gradients 記事。Jeff Huber (Chroma CEO) が語る context engineering > prompt engineering、大規模コンテキストウィンドウの限界、エージェントハーネス = tools+sub-agents+workflows、コード記述が創発的推論を解放する、Inner Loop / Outer Loop フレームワーク。
- **🆕 エンティティページ作成**: `[[entities/jeff-huber]]` (L2) — Chroma CEO & Co-founder の包括的ページ。Standard Cyborg (YC W15) → Chroma ($18M seed) の背景、Context Engineering > Prompt Engineering の再定義、Inner/Outer Loop フレームワーク、コード記述による創発的推論テーゼ、実践的ビルダーアドバイス（Hybrid Search / Golden Dataset / Cluster Analysis / Tool Engineering）。
- **✏️ 概念ページ強化**: `[[concepts/reduce-offload-isolate]]` — Jeff Huber の **Inner Loop vs Outer Loop** 拡張セクションを新設。Inner Loop = Reduce/Offload/Isolateをタスク単位で適用、Outer Loop = コンテキスト充填を時間と共に改善するシステム（"machine that builds the machines"）。評価の未解決問題にも言及。
- **✏️ 相互リンク**: `[[entities/hugo-bowne-anderson]]` — Key Collaborations テーブルの Jeff Huber を [[entities/jeff-huber]] へのwikilink化。
- **Index更新**: jeff-huber を entities セクションに追加（jeff-geerling と jensen-huang の間）。Total pages: 1783→1784, Indexed entries: 837→838, Entities: 558→559。
## [2026-05-13] enrich | Agentic Search: Berryman 5-Level Model + Revealed Preferences + Ep.68
- id: concept-agentic-search-berryman-ep68-2026-05-13
- summary: Saved 3 raw articles (Berryman's 5-level maturity model blog, Turnbull's LLM-judges critique, Ep.68 show notes). Added two major sections to [[concepts/agentic-search]]: "Berryman's 5-Level Agentic Search Maturity Model" (Level 0-4: Trad Search → Beginner AI → Intermediate AI → Conversational Assistant → Async Research Agent) with comparison table vs 3-level framework, and "Revealed Preferences: The Fundamental Limit of LLM-as-Judge" (engagement blindness, hard negative blindness, sneaky overfitting, LLMs-as-analysts-not-judges). Added Jan 2026 blog post entry to [[entities/john-berryman]]. Cross-linked with [[concepts/llm-as-judge]].
- touched:
  - [[concepts/agentic-search]]
  - [[entities/john-berryman]]
  - raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level.md
  - raw/articles/2026-01-23_vanishing-gradients_ep68-builders-guide-agentic-search.md
  - raw/articles/2025-11-02_softwaredoug_llm-judges-arent-the-shortcut.md
## 2026-05-13 04:30 UTC — Lance Martin Reduce/Offload/Isolate フレームワーク取り込み

- **Raw記事保存**: `wiki/raw/articles/2025-12-12_hugobowne_agent-harness-context-engineering.md` — Hugo Bowne-Anderson + Duncan Gilchrist による Vanishing Gradients 記事。Lance Martin (Anthropic, 出演時はLangChain) が High Signal ポッドキャストで語ったコンテキストエンジニアリング3原則、Bitter Lessonのハーネス設計への適用、Manus 5回再設計・AnthropicのClaude Code ハーネス削減の証言。
- **🆕 概念ページ作成**: `[[concepts/reduce-offload-isolate]]` (L2) — Reduce（コンテキスト圧縮）/ Offload（プロンプト外移動）/ Isolate（サブエージェント委譲）の詳細フレームワーク。Bitter Lessonとの接続、Write-Select-Compress-Isolateからの進化、Manus/Claude Code/Open Deep Researchの実例、ハーネス設計への含意を含む。
- **✏️ エンティティ強化**: `[[entities/lance-martin]]` — High Signal ポッドキャスト出演を Podcast Appearances に追加。Reduce/Offload/Isolateフレームワークの専用セクションを新設。updated: 2026-05-13。
- **✏️ 相互リンク**: `[[entities/hugo-bowne-anderson]]` — Harness Engineering Philosophy セクションの "Reduce, Offload, Isolate" を [[concepts/reduce-offload-isolate]] へのwikilink化。
- **Index更新**: concepts/reduce-offload-isolate を追加。Total pages: 1782→1783, Indexed entries: 836→837, Concepts: 1249→1250。
- **2026-05-13**: Discord user request → ingested "Agents That Build Themselves" (自己拡張エージェント) content from 3 sources: Substack article (Hugo Bowne-Anderson, Feb 2026), YouTube workshop (96min live build with Ivan Leo), GitHub repo (build-your-own-ai-assistant). **New pages**: `concepts/agents-that-build-themselves.md` (Level 5: Self-Modification pattern — factory + hot reload + hooks + markdown memory), `entities/ivan-leo.md` (Ivan Leo — Google DeepMind, ex-Manus). **Enriched**: `concepts/self-evolving-agents.md` (added Level 5: Self-Modification with code example), `entities/openclaw.md` (added Core Architecture Patterns: hooks, memory compaction, tool factory + self-extension), `entities/hugo-bowne-anderson.md` (added build-your-own-ai-assistant repo). **Raw articles**: 2026-02-28_substack_agents-that-build-themselves.md (18KB), 2026-02-28_youtube_openclaw-from-scratch-workshop.md (33KB). Index: +2 pages (1780→1782), +2 entries (834→836).
## [2026-05-13] enrich | Agentic Search: Long-Running Agents & RLM practitioner perspective
- id: concept-agentic-search-rlm-practitioner-2026-05-13
- summary: Added "Long-Running Agents and Recursive Language Models" section to [[concepts/agentic-search]] from Doug Turnbull's Feb 2026 Vanishing Gradients interview. Documents the practitioner's RLM vision: context-as-variable, context-as-search-index, 4-stage evolution (linear history → compaction → context-as-variable → context-as-world). Includes comparison table (Academic RLM vs Turnbull's Practitioner Framing), OpenClaw self-extending loop example, and cross-links to [[concepts/rlm-recursive-language-models]], [[concepts/code-mode]], [[concepts/context-fragments]].
- touched:
  - [[concepts/agentic-search]]
## [2026-05-13] enrich | Agentic Search: In-Prompt RL section + Hugo Bowne-Anderson annotated talk
- id: concept-agentic-search-in-prompt-rl-2026-05-13
- summary: Saved Hugo Bowne-Anderson's annotated Substack transcript of Doug Turnbull's "How To Build Your First Agentic Search Application" talk as raw article `2026-02-21_hugobowne_how-to-build-first-agentic-search.md`. Added new "In-Prompt Reinforcement Learning" section to [[concepts/agentic-search]] covering the validator-as-dissatisfied-user pattern, RLHF vs in-prompt RL comparison table, validator taxonomy (LLM-as-Judge, reranker, rule-based, domain model), and connection to the broader harness architecture. Updated concept page sources and date.
- touched:
  - [[concepts/agentic-search]]
  - raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search.md
## [2026-05-13] update | John Berryman entity + Unharnessed Agents concept + Arcturus Labs blog tracking
- id: entity-john-berryman-unharnessed-agents-2026-05-13
- summary: Created [[entities/john-berryman]] entity page (L2, Arcturus Labs founder, ex-GitHub Copilot engineer, author). Created [[concepts/unharnessed-agents]] concept page documenting Berryman's anti-harness thesis ("agent harness" is wrong frame, agents should leave the IDE, skills are new programs). Updated [[concepts/harness-commoditization]] with comparative analysis table (Amp vs Berryman). Saved raw article `2026-04-24_arcturus-labs_unharnessed-agents.md`. Added Arcturus Labs to blogwatcher DB + OPML with RSS feed. Moved from concepts/john-berryman.md stub. Fixed Doug Turnbull entity wikilink.
- touched:
  - [[entities/john-berryman]]
  - [[concepts/unharnessed-agents]]
  - [[concepts/harness-commoditization]]
  - [[entities/doug-turnbull]]
  - [[config/feeds/blogs.opml]]

## [2026-05-13] update | Hugo Bowne-Anderson entity enrichment + duplicate merge + x-accounts
- id: entity-hugo-bowne-anderson-enrichment-2026-05-13
- summary: Enriched [[entities/hugo-bowne-anderson]] (L3) with Privacy Engineering section (from "15 Privacy Questions" with Katharine Jarmul) and Agent Harness Engineering section (Harness Reading List, Lance Martin's Reduce/Offload/Isolate, Jeff Huber context engineering, Ivan Leo self-extending agents, Doug Turnbull agentic search). Added 5 new Related People. Merged and deleted duplicate [[entities/hugo-bowne]] stub. Added @hugobowne to x-accounts.yaml. Fixed wikilink in concepts/ai-safety.md.
- touched:
  - [[entities/hugo-bowne-anderson]]
  - [[entities/hugo-bowne]] (deleted)
  - [[concepts/ai-safety]]
  - [[config/feeds/x-accounts.yaml]]

## [2026-05-13] update | Max Rumpf エンティティページ + SID-1 コンセプトページ作成
- id: entity-max-rumpf-sid-1-2026-05-13
- summary: Created [[entities/max-rumpf]] (L2, CEO/Co-founder SID.ai, SID-1 developer) and [[concepts/sid-1]] (L2, first RL-trained agentic retrieval model). Added @maxrumpf to x-accounts.yaml. Web-sourced from maxrumpf.com, sid.ai, X, LinkedIn, YC, podcasts.
- touched:
  - [[entities/max-rumpf]]
  - [[concepts/sid-1]]
  - [[config/feeds/x-accounts.yaml]]

## [2026-05-13] update | Harness Engineering blog context/action synthesis
- id: blog-harness-engineering-context-action-synthesis-2026-05-13
- summary: Strengthened the Harness Engineering survey with a Context-axis/Action-axis synthesis, Lance Martin's Reduce/Offload/Isolate framing, RLM-based learned context management, and anti-harness/commoditization counterarguments.
- touched:
  - [[blog/2026-05-12_hermes_harness-engineering-from-coding-agents-to-general-agents]]
  - [[concepts/harness-engineering/context-engineering]]
  - [[concepts/reduce-offload-isolate]]
  - [[concepts/rlm-recursive-language-models]]
  - [[concepts/unharnessed-agents]]
  - [[concepts/harness-commoditization]]
