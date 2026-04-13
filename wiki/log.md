## 2026-04-13

- **[New]** [[concepts/dspy]] — 15KB comprehensive DSPy concept page: declarative LM programming philosophy, Signature/Module/Teleprompter architecture, Assertions, Fine-tuning integration, paradigm comparison vs LangChain/LlamaIndex/RLMs/GEPA
- **[New]** [[comparisons/llm-integration-patterns]] — 12KB comparative taxonomy of 5 LLM integration paradigms (Orchestration, Declarative, Recursive, Agentic, Genetic), paradigm evolution map, Khattab research lineage, practical selection guide
- **[New]** [[entities/omar-khattab]] — 11KB comprehensive profile (RLM co-author, DSPy creator, GEPA, ColBERT, "LMs as modules" philosophy, research phases, relationships, impact metrics)
- **[Updated]** [[entities/alex-zhang]] — Expanded with RLM deep analysis (OOLONG, BrowseComp-Plus, Qwen3-8B recipe), philosophical context-centric decomposition analysis, additional quotes
- **[Updated]** [[entities/omar-khattab]] — 13KB → RLM section expanded: Khattab X quote on context-as-data, RLM benchmarks, Yao×Khattab convergence analysis, DSPy v3.1.2+ RLM integration, 3-phase research arc table
- **[New]** [[entities/shunyu-yao]] — 15KB full profile (ReAct, ToT, Reflexion, SWE-bench, "The Second Half", Yao×Zhang convergence on environment-first design)
- **[New]** [[concepts/rlm-recursive-language-models]] — 8KB RLM concept page (Inspect→Decompose→Recurse→Aggregate pattern, REPL integration, benchmarks, Harness Engineering relationship)
- **[Updated]** [[wiki/index.md]] — Added shunyu-yao, updated Khattab entry to reflect RLM enrichment

     1|---
     2|title: "Wiki Change Log"
     3|---
     4|
     5|# Wiki Change Log
     6|
     7|## 2026-04-13
     8|
     9|### Entity Page Enrichments (skeleton → L2/L3)
    10|
    11|#### Scott Wu (skeleton → L3)
    12|- **Bio**: CEO & Co-Founder, Cognition AI. 3× IOI Gold Medalist. Harvard dropout. Forbes 30 Under 30 (2019, Lunchclub).
    13|- **Core Ideas**: "AI should augment human engineers, not replace them." Extreme performance culture. Closing the agent loop (Write→Catch→Fix→Merge autonomously). Single-threaded agent philosophy with context continuity.
    14|- **Contributions**: Devin 1.0 (13.86% SWE-bench unassisted, vs 1.96% previous SOTA). Cognition grown from 10-person team to $10B+ valuation. Enterprise adoption at Goldman Sachs, Citi (40K+ developers), NASA, Ramp, Stripe (1K+ PRs/week).
    15|- **Philosophy**: "Eventually, the future comes." — closing the agent loop, no human needed for PR reviews. Competitive programming background (10 IOI gold medals across founding team) gives unique edge in algorithmic AI development.
    16|- **Timeline**: Mathcounts champion → IOI Gold → Addepar → Harvard (dropout) → Lunchclub (2019) → Cognition AI (2023) → Devin 1.0 (Mar 2024) → $400M raise at $10B+ (2025) → Devin GA (2026)
    17|- **Sources**: cognition.ai/blog/introducing-devin, cognition.ai/blog/devin-2-2, SF Standard (Mar 2026), American Optimist Podcast
    18|
    19|#### Nader Dabit (skeleton → L3)
    20|- **Bio**: Growth Engineer at Cognition AI (Feb 2026–). AWS (2018–2021) → Aave Labs (2022–2024) → Eigen Labs (2024–2026). React Native Training founder (2016–2021).
    21|- **Core Ideas**: **Cloud Agent Thesis** — "Cloud agents are a different category from local agents, and the differences compound." **Agents That Never Sleep** — 70/30 human→agent trigger ratio inverting to 10/90. Prerequisites: unit tests, documentation, reproducible dev environments, rich system context.
    22|- **Key Publications**: "Engineering for Agents That Never Sleep" (Mar 2026), "How Cognition Uses Devin to Build Devin" (Feb 2026), "How to Run a Fleet of Cloud Agents" (Mar 2026), "The Cloud Agent Thesis" (Feb 2026). Substack: 1.7K+ subscribers.
    23|- **Philosophy**: "That scaffolding is the difference between an agent that opens a PR and an agent that closes an incident at 3am." "Local agents make developers faster. Cloud agents make engineering orgs more capable."
    24|- **Key Metrics**: Cognition internal: 154→659 Devin PRs/week. Industry: Stripe 1K+ agent-written PRs/week, 1.2M merged PRs across hundreds of orgs.
    25|- **Sources**: nader.substack.com, nader.codes, LinkedIn, X (@dabit3)
    26|
    27|#### Walden Yan (skeleton → L3)
    28|- **Bio**: Co-Founder & CPO, Cognition AI. IOI 2020 Gold Medalist (19/343, 505.38/600). MIT PRIMES researcher (cryptography, ML). Harvard CS & Economics (2020–2024).
    29|- **Core Ideas**: **Context Engineering** — "Share full agent traces, not just individual messages." "Actions carry implicit decisions, and conflicting decisions carry bad results." **Don't Build Multi-Agents** — current multi-agent frameworks are fragile; single-threaded agents with context continuity are more reliable.
    30|- **Background**: DeepReason (Co-Founder & CEO, 2022–2023, security systems) → Anysphere/Cursor (Early Engineer, Jun–Aug 2023) → Inverted Agency (Managing Partner, 2020–2021). Early exposure to AI-powered coding at Cursor directly informed Devin's architecture.
    31|- **Philosophy**: "We're still playing with raw HTML & CSS" — current agent development lacks standardization. Advocates for intellectual humility: "Our theories are likely not perfect, and we expect things to change."
    32|- **Key Publications**: "Don't Build Multi-Agents" (Jun 2025, Cognition Blog) — most cited article on context engineering. Maven Course: "Why Devin Does Not Use Multi-Agents."
    33|- **Sources**: cognition.ai/blog/dont-build-multi-agents, LinkedIn, Product Hunt, waldenyan.com, IOI 2020 Statistics
    34|
    35|#### Ali Farhadi (skeleton → L2)
    36|- **Bio**: YOLO co-creator, Xnor.ai founder (→Apple $200M), Ai2 CEO (2023-2026) → Microsoft (Mustafa Suleyman's AI team)
    37|- **Core Ideas**: Open-source AI as default ("Open source is how we drive progress"), financial reality of frontier AI, real-time object detection philosophy, multimodal AI grounding
    38|- **Contributions**: YOLO (80K+ citations), OLMo (#1 open model on HF Heatmap), Molmo, Dolma (5.9T tokens), OlmoTrace
    39|- **Philosophy**: Simplicity over complexity, transparency as prerequisite for progress, real-world applicability
    40|- **Sources**: homes.cs.washington.edu/~ali/, GeekWire articles on Ai2/Microsoft moves
    41|
    42|#### Peter Steinberger (skeleton → L3)
    43|- **Bio**: Austrian developer, PSPDFKit founder (1B+ device deployments, exited 2020), OpenClaw creator (135K+ instances), joined OpenAI Feb 2026
    44|- **Core Ideas**: "Ship beats perfect" philosophy, "I don't read code anymore, I weave it", closed loop principle (compile→run→test), PRs = "Prompt Requests", polyagentmorous development (5-10 parallel agents)
    45|- **Tooling Ecosystem**: OpenClaw, VibeTunnel, CodexBar, Peekaboo, mcporter, gogcli, agent-rules, Aspects (8.4K stars)
    46|- **Anthropic-OpenClaw Conflict**: April 2026 policy dispute over third-party tools; account suspended then restored
    47|- **Philosophy**: Agent-first design, CLI over MCP, cache-first engineering, main-branch development
    48|- **Sources**: steipete.me, thewantrepreneurshow.com interview, GitHub (@steipete, 46K+ followers)
    49|
    50|#### Shlok Khemani (skeleton → L2)
    51|- **Bio**: Writer/programmer in Gurgaon, India. Researching personal AI and memory systems. Previously at Decentralised.co (crypto products)
    52|- **Core Ideas**: Bitter Lesson applied to AI memory (ChatGPT's context-only approach), filesystem-first memory (Claude's CLAUDE.md vs ChatGPT's hidden profiles), personality ≠ execution separation (OpenPoke), cache-first engineering
    53|- **Contributions**: OpenPoke (465 stars, multi-agent Poke replica), Claude Memory Tools (53 stars), Vajra (background coding agent), ChatFerry, Conjure
    54|- **Writing**: ChatGPT Memory reverse-engineering (widely cited), Anthropic Memory Bet analysis, Claude Code source analysis
    55|- **Philosophy**: Personality ≠ Execution, Filesystem over Database, Cache-First Design, Background Execution, Transparency over Opacity
    56|- **Sources**: shloked.com, GitHub (@shlokkhemani)
    57|
    58|### Concept Pages Added (from entity enrichments)
    59|- `concepts/open-claw-ecosystem` — Peter Steinberger's OpenClaw framework
    60|- `concepts/chatgpt-memory-bitter-lesson` — Shlok Khemani's ChatGPT memory analysis
    61|- `concepts/claude-memory` — Claude's file-based memory architecture
    62|- `concepts/claude-memory-tool` — Cognition copying Claude's memory approach
    63|- `concepts/claude-code-source-patterns` — Leaked Claude Code source analysis
    64|- `concepts/vajra-background-agent` — Vajra open-source background coding agent
    65|- `concepts/olmo-open-language-model` — Ali Farhadi's OLMo project at Ai2
    66|
    67|### Updated Files
    68|- `wiki/entities/ali-farhadi.md` — skeleton → L2 (7KB)
    69|- `wiki/entities/peter-steinberger.md` — skeleton → L3 (7.4KB)
    70|- `wiki/entities/shlok-khemani.md` — skeleton → L2 (9.6KB)
    71|- `wiki/index.md` — entity count 46→49, People section descriptions updated, AI Research & Computer Vision section added
    72|- `wiki/log.md` — This entry
    73|
    74|## 2026-04-13
    75|
    76|### Anthropic Cookbooks — Claude Agent SDK & Managed Agents (4件)
    77|Anthropic Cookbookから実用的なエージェント設計パターンを抽出し、概念ページとして整理。特にClaude Codeの検証済みユースケースをサーバーサイド自動化フローに転用する設計に焦点。
    78|- **claude-agent-sdk-sre-patterns.md** — MCPサブプロセス統合、3層安全ガードレール（ディレクトリ制限/コマンドAllowlist/PreToolUseフック）、自律的インシデント対応ワークフロー
    79|- **managed-agents-sre-incident-response.md** — Webhook駆動セッション開始、Skillsによるプログレッシブディスクロージャー、カスタムツール経由HITL承認（Slackボタン→PRマージ）
    80|- **chief-of-staff-agent-patterns.md** — CLAUDE.md永続メモリ、Planモード（`permission_mode="plan"`）、Output Styles、カスタムスラッシュコマンド、Hooks（PreToolUse/PostToolUse）、サブエージェント委任
    81|- **research-agent-fundamentals.md** — ステートレス(`query()`) vs ステートフル(`ClaudeSDKClient`)、バッファ管理(`max_buffer_size`)、システムプロンプトによる引用強制
    82|- **Sources**: https://platform.claude.com/cookbook/ (56 cookbooks中10件をスキャン、優先4件をwiki化)
    83|
    84|### OpenAI Cookbook — 方法論コンセプト追加 (6件)
    85|OpenAI Cookbookからベンダー中立な方法論を抽出し、概念ページとして整理。
    86|- **evaluation-flywheel.md** — 評価→分析→改善→データ収集の継続的フィードバックループ。Golden Dataset構築、Multi-Metric Evaluation、Regression Detection
    87|- **agentic-scaffolding.md** — エージェントの安全な動作のための多層ガードレール設計。Input Validation → Execution Constraints → Output Verification → Human Oversight
    88|- **exec-plans.md** — 計画と実行の分離パターン。事前Plan生成→レビュー→実行→検証のフロー。透明性・デバッグ性・再利用性向上
    89|- **self-evolving-agents.md** — 自己改善するエージェント設計。4レベル（Parameter Tuning → Strategy Adaptation → Capability Expansion → Architectural Evolution）
    90|- **resilient-prompt-engineering.md** — プロンプトをコードとして扱う設計。バージョン管理、テスト、レビュー、A/Bテスト、構造化プロンプティング
    91|- **context-engineering.md** — コンテキストウィンドウ最適化技術。Compression、Ordering、Dynamic Management、Chunking（Anthropic版のConceptual Context Engineeringと区別）
    92|- **Sources**: https://github.com/openai/openai-cookbook
    93|
    94|### Steipete 過去1年投稿 — 追加Concept Pages
    95|- **New concept pages (5件)**:
    96|  - `direct-prompting-philosophy.md` — 「Just Talk To It」哲学。RAG/サブエージェント/カスタムフック等の過剰工学を拒否し、直接的な会話的インタラクションでAIを操るアプローチ。パラレルターミナルウィンドウパターン、コンテキストポイズン警告、直感的ディレクション開発
    97|  - `cli-over-mcp-pattern.md` — MCPサーバーより標準CLIツールを優先する設計原則。コンテキストウィンドウ効率、モデル familiarly、デバッグ容易性の観点からCLIsが勝る。MCPが有効なユースケース（Webスクレイピング、DB探索、デザイン-to-コード）も記載
    98|  - `ai-addiction-burnout.md` — AIコーディングエージェントによる「スロットマシン効果」、Black Eye Club現象、80時間労働週の正常化リスク。バーンアウトサイクル（発見→執着→消耗→回復）と緩和戦略
    99|  - `self-hosting-ai-development.md` — Claude Max利用制限後のセルフホスティング検討。8xH200 vs APIコスト分析、ツール評価（opencode, charm, Cline, Gemini CLI）、Qwen3-Coder-480B vLLMデプロイガイド。「商業的にはトークン課金が経済的に健全」
   100|  - `main-branch-development.md` — feature branch/worktreeを避けmainで直接開発するパターン。アトミックコミット、Gitをセーフティネットとして活用、Arena機能1時間構築ケーススタディ
   101|- **Updated existing pages**:
   102|  - `index.md` — 5新概念エントリ追加、Last updated更新
   103|- **Sources**: steipete.me 過去1年分13投稿を抽出・分析（2025-07 〜 2026-02）
   104|
   105|## 2026-04-13
   106|
   107|### Cognition AI Data Analyst — Devinをデータ分析エージェントにする設計
   108|- **New concept page**:
   109|  - `concepts/cognition-ai-data-analyst.md` — Cognitionのデータ分析エージェント設計パターン。MCP+Knowledgeアーキテクチャ、SQL専用ツールとの違い、Knowledge設定テンプレート、実践的ワークフロー
   110|- **Key insights**:
   111|  - AIソフトウェアエンジニアをデータ分析に使う理由: コードベースの文脈理解+完全なデータ系譜の把握
   112|  - MCPをセキュアなデータアクセスブリッジとして活用（Google MCP Toolbox, Metabase MCP Server 80+ツール）
   113|  - Knowledge設定（Purpose/Guidelines/Output Format/Macro）がエージェントの精度を決定
   114|  - Verifiable Outputs: 最終SQL+可視化+Metabaseリンクで人間が検証可能
   115|  - 150+時間/月 → 数分の効率化
   116|- **Sources**:
   117|  - [Build Your Own AI Data Analyst (Part 1)](https://devin.ai/ai-data-analyst-1)
   118|  - [Build Your Own AI Data Analyst (Part 2)](https://devin.ai/ai-data-analyst-2)
   119|
   120|### Cognition/Devin Philosophy — Agentic Coding at Scale
   121|- **Enhanced entity pages**:
   122|  - `entities/scott-wu.md` — X/Twitter activity追加（"Eventually, the future comes" Devin 2.2リリース）。100x capability growth metrics（週154→659 PRs、METR結果）、technical insights（Don't Build Multi-Agents、Managed Devins転換、Context Anxiety発見、Closing the Agent Loop）
   123|  - `entities/nader-dabit.md` — X/Twitter activity追加（Agentic Slack, Agents From Anywhere）。ターミナル/IDEの限界→Slackをエージェントインターフェースに。非同期fire-and-forget、マルチプレイヤー化
   124|- **Enhanced concept page**:
   125|  - `concepts/cognition-devin-philosophy.md` — Scott Wu X投稿メトリクス、Nader Dabit Agentic Slack/Agents From Anywhere詳細追加。sourcesにXリンク追加
   126|- **Updated index.md**:
   127|  - PeopleセクションにScott Wu, Nader Dabit, Walden Yan追加
   128|  - Cognition/Devin Philosophyセクション新規追加（4概念ページ）
   129|- **Removed duplicate**: `concepts/cognition-devin-agentic-coding.md`（cognition-devin-philosophy.mdに統合）
   130|- **Sources**:
   131|  - [Scott Wu — Eventually, the future comes](https://x.com/scottwu46/status/2026350958213787903)
   132|  - [Nader Dabit — Agentic Slack](https://x.com/dabit3/status/2026385925593510302)
   133|  - [Nader Dabit — Agents From Anywhere](https://x.com/dabit3/status/2025936695661826481)
   134|  - [Cognition — Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents)
   135|  - [Cognition — Devin Can Now Manage Devins](https://cognition.ai/blog/devin-can-now-manage-devins)
   136|  - [Nader Dabit — Engineering for Agents That Never Sleep](https://nader.substack.com/p/engineering-for-agents-that-never)
   137|
   138|## 2026-04-13
   139|
   140|### Sankalp & Steipete Articles — Core Concept Extraction
   141|- **New top-level concept pages**:
   142|  - `inference-speed-development.md` — 推論速度で出荷する開発パラダイム (Steipete): 従来の日単位→分単位の開発サイクル、テスト駆動AI開発、UI開発パイプライン、50回試行パターン、人間の役割変化（Writer→Reviewer/Director）
   143|  - `claude-code-best-practices.md` — Claude Code実践パターン集 (Sankalp): MCP Server活用、サブエージェント委任（--max-turns）、CLAUDE.md戦略、セッションハイジーン、アンチパターン（無限セッション、過委任、盲目的信頼、プロンプト肥大）
   144|  - `context-window-management.md` — コンテキスト管理の一般パターン（両記事統合）: セッション分割、圧縮（`<analysis>→<summary>`）、フォークパターン、トークンエコノミクス、キャッシュ最優先エンジニアリング
   145|- **Updated existing pages**:
   146|  - `agentic-engineering.md` — Further ReadingにSankalp/Steipete記事追加、Related concepts拡張
   147|  - `index.md` — 3新概念エントリ追加、Last updated更新
   148|- **Sources**:
   149|  - [Sankalp — My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
   150|  - [Peter Steinberger (@steipete) — Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
   151|
   152|## 2026-04-13
   153|
   154|### Sankalp & Steipete — Coding Agent Practical Patterns
   155|- **New concept pages**:
   156|  - `agentic-engineering/agent-first-design.md` — 「人間向け」ではなく「エージェント向け」コード設計哲学 (Steipete)
   157|  - `agentic-engineering/cli-first-development.md` — CLI起点開発でフィードバックループ高速化 (Steipete, Sankalp)
   158|  - `agentic-engineering/throw-away-draft-pattern.md` — 捨て台本→比較→反復サイクル (Sankalp)
   159|- **Enhanced existing pages**:
   160|  - `agentic-engineering/context-window-management.md` — コンテキスト60%ルール、モデル別有効限界表を追加 (Sankalp)
   161|  - `agentic-engineering/how-agents-work.md` — Plan Mode不要論、Task Toolアーキテクチャ、Exploreエージェント制約を追加 (Steipete, Sankalp)
   162|  - `agentic-engineering/subagents.md` — サブエージェント要約のlossiness、使い分け指針を追加 (Sankalp)
   163|  - `agentic-engineering/_index.md` — Sankalp/Steipeteセクション追加、リーダー表拡張
   164|- **Sources**:
   165|  - [Sankalp — A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
   166|  - [Steipete — Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
   167|
   168|## 2026-04-13
   169|
   170|### Shlok Khemani — Memory Systems & Agent Architecture Analysis (5 articles)
   171|- **New concept pages**:
   172|  - `chatgpt-memory-bitter-lesson.md` — ChatGPTメモリ問題と「The Bitter Lesson」。ステートフルメモリ vs ステートレスコンテキストウィンドウ
   173|  - `claude-memory.md` — Claudeのファイルベースメモリ（CLAUDE.md、.agent/、Git統合）
   174|  - `claude-memory-tool.md` — CognitionがClaudeのメモリをコピーしている理由と競争力学
   175|  - `claude-code-source-patterns.md` — Claude Code漏洩ソースの分析（プロンプト合成、キャッシュ最優先、Forkプリミティブ、Scratchpad圧縮）
   176|  - `vajra-background-agent.md` — Vajraオープンソースバックグラウンドコーディングエージェント（Graphviz DOT、Linear統合、ファイルシステム専用アーキテクチャ）
   177|- **New entity page**: `shlok-khemani.md` — Shlok Khemani (@shloked)
   178|- **Sources**: shloked.com 5記事（April 2026）
   179|
   180|### Simon Willison — Agentic Engineering Patterns Guide (L3 Enrichment)
   181|- **simon-willison.md**: L3 Thought Analysisレベルにアップグレード
   182|  - Added: Hoarding（知識の蓄積）哲学 — "productive kind of hoarding"
   183|  - Added: Compound Engineering Loop — Write→Review→Improve→Save→Repeat
   184|  - Added: Git統合の具体的プラクティス — 小さく頻繁なコミット、人間向けのメッセージ
   185|  - Added: Writing Code is Cheap — 新しい習慣の必要性
   186|  - Updated sources: Agentic Engineering Patterns Guideリンクを追加
   187|- **New concept pages**:
   188|  - `agentic-engineering/compound-engineering-loop.md` — 複合エンジニアリングループ
   189|  - `agentic-engineering/code-hoarding.md` — 知識の蓄積と再利用パターン
   190|- **index.md**: Updated with new concept entries
   191|
   192|
   193|### Agent Team / Swarm Directory Created
   194|- Created `agent-team-swarm/_index.md` — フロントページ: 5レベルモデル（Spicy Autocomplete → Dark Factory）、主要実装比較表
   195|- Enriched `anthropic-managed-agents.md` — 公式ブログ3件（Claude Blog + Engineering Blog + Platform Docs）の情報を反映。Brain/Hands/Session分離アーキテクチャ、Multi-Agent Coordination、Pricing、Enterprise Adoption事例を追加
   196|- New `openai-symphony.md` — WORKFLOW.md駆動のタスクオーケストレーター。SPEC.md解析、アーキテクチャコンポーネント、Symphony Go等のエコシステム、HN議論の洞察
   197|- New `dark-factory-software-factory.md` — Simon Willison + Dan Shapiroの5レベルモデル、StrongDM実践事例、Attractor/CXB、Digital Twin Universe
   198|
   199|## 2026-04-12
   200|
   201|### Concept Taxonomy Restructure
   202|- **Split `agentic-engineering/` into two directories:**
   203|  - `agentic-engineering/` — Willisonの開発パターン (13 files remain)
   204|  - `ai-agent-engineering/` — Anthropicのシステム構築パターン (11 files moved)
   205|- Created `agentic-engineering/_index.md` (Willison-centric refactor)
   206|- Created `ai-agent-engineering/_index.md` (Anthropic Engineering index)
   207|- Updated tags in 11 moved files: `agentic-engineering` → `ai-agent-engineering`
   208|- Updated `wiki/index.md` with new taxonomy
   209|- **Concept**: Agentic Engineering (開発者ワークフロー) vs AI Agent Engineering (システムアーキテクチャ) vs Harness Engineering (環境設計・共通概念)
   210|
   211|### Entity Pages
   212|- Simon Willison entity page enriched with Agentic Engineering guide content
   213|  - Sources: https://simonwillison.net/guides/agentic-engineering-patterns/
   214|  - Added: 7 core patterns, 4 principles, 4 tool references, 4 related concepts
   215|  - Expanded: Cognitive Debt theory, Context Window Management, Multi-agent patterns
   216|
   217|### New Concept Pages (from Agentic Engineering guide)
   218|- **context-window-management.md** — コンテキストウィンドウの戦略的管理（圧縮、構造化、優先順位付け）
   219|- **rodney.md** — ブラウザ自動化CLIツール（エージェント向け設計、Showboat連携）
   220|- **subagents.md** — 並列AIエージェント委任パターン（独立性、自己完結性、バッチモード）
   221|
   222|### New Concept Pages (from OpenAI Responses API article)
   223|- **agent-loop-orchestration.md** — エージェント実行ループ（モデル提案→シェル実行→結果フィードバック、並列実行、出力キャップ）
   224|- **context-compaction.md** — コンテキスト圧縮（サーバーサイド自動、/compact手動、Codexによる自己改善）
   225|- **container-context.md** — ホスト型コンテナ（永続ファイルシステム、SQLite、サイドカーエグレスプロキシ）
   226|- **agent-skills.md** — SKILL.mdバンドル（再利用可能ワークフロー、バージョン管理、段階的探索）
   227|- **agent-security-patterns.md** — エージェントセキュリティ（エグレスプロキシ、ドメインスコープシークレットインジェクション、許可リスト）
   228|
   229|### Enriched
   230|- **ai-agent-engineering/_index.md** — OpenAI Responses API 5概念を追加（エージェント実行基盤、セキュリティセクション新設）
   231|- **wiki/index.md** — AI Agent Engineeringセクションを「Anthropic + OpenAI」に拡張
   232|
   233|### Enriched Concept Pages
   234|- **cognitive-debt.md** (1.5KB → 3.5KB): Vibe Coding vs Agentic Engineering対比表、認知負債のメカニズム、返済サイクル図を追加
   235|
   236|### 2026-04-13 — Anthropic-OpenClaw Conflict & Illusion of Thinking Research
   237|
   238|### New Concept Pages (2件)
   239|- **anthropic-openclaw-conflict.md** — 2026年4月のAnthropicによるサードパーティAIエージェントツール（OpenClaw等）のサブアクセス遮断。135,000+インスタンス、~300xトークン格差、Peter SteinbergerのOpenAI移籍との関連性、競争力学の分析
   240|- **illusion-of-thinking.md** — Apple (2025) + Tufts (2026)の研究。LLMがTower of Hanoiで「推論しているように見えるが実際はパターンマッチ」であることを実証。ニューロシンボリックモデルはVLA比で95% vs 34%（3ブロック）、78% vs 0%（未知4ブロック）、エネルギー効率~100x
   241|
   242|### Entity Updates
   243|- **entities/gary-marcus.md** — "Even more good news for the future of neurosymbolic AI" (4/12)追加。Apple+Tufts研究の分析
   244|
   245|### New Entity Page (1件)
   246|- **entities/peter-steinberger.md** — OpenClaw創設者、2026年2月にOpenAI入社。"Agent-first design"提唱者（status: skeleton）
   247|
   248|### Raw Articles Saved (2件)
   249|- `wiki/raw/articles/2026-04-12-gary-marcus-even-more-good-news-neurosymbolic.md`
   250|- `wiki/raw/articles/2026-04-12-anthropic-openclaw-subscription-ban.md`
   251|
   252|### Updated Files
   253|- `wiki/index.md` — Last updated, Entity count 45→46, Anthropic-OpenClaw Conflict / Illusion of Thinking sections, Peter Steinberger in People
   254|- `wiki/log.md` — This entry
   255|
   256|- **Sources**:
   257|  - https://garymarcus.substack.com/p/even-more-good-news-for-the-future
   258|  - https://thenextweb.com/news/anthropic-openclaw-claude-subscription-ban-cost
   259|  - https://www.breezyscroll.com/technology-news/anthropic-blocks-openclaw-founder-from-claude-what-happened/
   260|  - https://danilchenko.dev/posts/2026-04-04-anthropic-cuts-claude-subscriptions-openclaw-third-party-tools/
   261|
   262|## 2026-04-13 — Auto-triage ingest
   263|- Updated: `entities/antirez-com.md` (added LLM sampling research from "First Token Cutoff LLM sampling" article)
   264|
   265|## 2026-04-13 — 4/11-12 Inbox Triage (Neurosymbolic AI, Open-Source Philosophy, Consortium)
   266|
   267|### New Concept Pages (3件)
   268|- **neurosymbolic-ai.md** — ニューラルネットワーク（パターン認識）とシンボリック推論（ルールベース論理）の組み合わせアーキテクチャ。Claude Codeのprint.ts漏洩を証拠に、Gary Marcusが「LLM以降最大のAI進化はニューロシンボリック」と論じる
   269|- **ai-coding-agent-criticism.md** — AIコーディングエージェント論争における「Center Has a Bias」論文（Armin Ronacher）。批判の対称性分析：直接体験派 vs 抽象批判派、エンゲージメントバイアスの構造的説明
   270|- **open-model-consortium.md** — オープンモデルコンソーシアムの必然性（Nathan Lambert）。NVIDIA Nemotron Coalition、Stanford Marin、Arcee AIの動向。オープンモデルが公共財としての性格を持つことの論証
   271|
   272|### Entity Updates
   273|- **entities/gary-marcus.md** — Updated `updated` date, added "The biggest advance in AI since the LLM" to recent posts
   274|- **entities/geohot-github-io.md** — Added Apr 2026 "OpenAI is nothing without its people" and Mar 2026 posts (neofeudalism, 69 agents, Two Worlds)
   275|- **entities/armin-ronacher.md** — Added 4/11 "The Center Has a Bias" to timeline and sources, added `ai-coding-agent-criticism` cross-reference
   276|- **entities/nathan-lambert.md** — Added to index.md People section (Open Source AI & Consortium)
   277|
   278|### Raw Articles Saved (4件)
   279|- `wiki/raw/articles/2026-04-11-gary-marcus-biggest-advance-ai-llm.md`
   280|- `wiki/raw/articles/2026-04-11-geohot-openai-nothing-without-people.md`
   281|- `wiki/raw/articles/2026-04-11-armin-ronacher-center-has-a-bias.md`
   282|- `wiki/raw/articles/2026-04-12-nathan-lambert-open-model-consortium.md`
   283|
   284|### Updated Files
   285|- `wiki/index.md` — Last updated, Neurosymbolic AI section, Open Source AI & Consortium section, People additions
   286|- `wiki/log.md` — This entry
   287|
   288||- **Sources**:
   289|  - https://garymarcus.substack.com/p/the-biggest-advance-in-ai-since-the
   290|  - https://geohot.github.io//blog/jekyll/update/2026/04/11/openai-people.html
   291|  - https://lucumr.pocoo.org/2026/4/11/the-center-has-a-bias/
   292|  - https://www.interconnects.ai/p/the-inevitable-need-for-an-open-model
   293|
   294|---
   295|
   296|## 2026-04-13
   297|
   298|### Entity Page Enrichment (new → L3)
   299|
   300|#### Alex L. Zhang (@a1zhang) — MIT CSAIL PhD, RLM creator
   301|- **Bio**: MIT CSAIL PhD student (advisors: Omar Khattab, Tim Kraska). Princeton CS top graduate. GPU MODE core team.
   302|- **Core Ideas**: **Recursive Language Models (RLMs)** — LMs that recursively call themselves via REPL environments to handle unbounded context. "Language models will be scaffolds." Context rot is a training distribution problem, not a model capacity problem. The line between "language model" and "scaffold" is blurring.
   303|- **Key Contributions**: RLM paper (arXiv:2512.24601), RLM library (3.3k+ ⭐), KernelBench (ICML 2025 Best Paper), GPU MODE community, KernelBot platform, Neo-1 (Sakana AI), KernelLLM-8B.
   304|- **RLM Results**: RLM(GPT-5-mini) outperforms GPT-5 by >34pts on OOLONG (132k context). RLM-Qwen3-8B beats base Qwen3-8B by 28.3%. BrowseComp-Plus: perfect performance at 1000 docs.
   305|- **Philosophy**: RLMs ≠ agents, ≠ summarization. RLMs are a task-agnostic scaffold where the LM decides how to decompose problems. "RLMs trained explicitly to recursively reason are likely to represent the next milestone in general-purpose inference-time scaling after CoT-style reasoning models and ReAct-style agent models."
   306|- **Connection to Harness Engineering**: RLMs as universal, task-agnostic scaffolds vs. task-specific harnesses. Harness engineering = human-designed scaffolds; RLM = model-designed scaffolds.
   307|- **Sources**: alexzhang13.github.io/blog/2025/rlm/, alexzhang13.github.io/blog/2026/scaffold/, arXiv:2512.24601, github.com/alexzhang13/rlm
   308|
   309|### Updated Files
   310|- `wiki/entities/alex-zhang.md` — New entity page (~12KB)
   311|- `wiki/index.md` — Added ML Systems & Inference Scaling section
   312|- `wiki/log.md` — This entry
   313|