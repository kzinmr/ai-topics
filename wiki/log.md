---
title: "Wiki Change Log"
---

# Wiki Change Log

## 2026-04-13

### Entity Page Enrichments (skeleton → L2/L3)

#### Scott Wu (skeleton → L3)
- **Bio**: CEO & Co-Founder, Cognition AI. 3× IOI Gold Medalist. Harvard dropout. Forbes 30 Under 30 (2019, Lunchclub).
- **Core Ideas**: "AI should augment human engineers, not replace them." Extreme performance culture. Closing the agent loop (Write→Catch→Fix→Merge autonomously). Single-threaded agent philosophy with context continuity.
- **Contributions**: Devin 1.0 (13.86% SWE-bench unassisted, vs 1.96% previous SOTA). Cognition grown from 10-person team to $10B+ valuation. Enterprise adoption at Goldman Sachs, Citi (40K+ developers), NASA, Ramp, Stripe (1K+ PRs/week).
- **Philosophy**: "Eventually, the future comes." — closing the agent loop, no human needed for PR reviews. Competitive programming background (10 IOI gold medals across founding team) gives unique edge in algorithmic AI development.
- **Timeline**: Mathcounts champion → IOI Gold → Addepar → Harvard (dropout) → Lunchclub (2019) → Cognition AI (2023) → Devin 1.0 (Mar 2024) → $400M raise at $10B+ (2025) → Devin GA (2026)
- **Sources**: cognition.ai/blog/introducing-devin, cognition.ai/blog/devin-2-2, SF Standard (Mar 2026), American Optimist Podcast

#### Nader Dabit (skeleton → L3)
- **Bio**: Growth Engineer at Cognition AI (Feb 2026–). AWS (2018–2021) → Aave Labs (2022–2024) → Eigen Labs (2024–2026). React Native Training founder (2016–2021).
- **Core Ideas**: **Cloud Agent Thesis** — "Cloud agents are a different category from local agents, and the differences compound." **Agents That Never Sleep** — 70/30 human→agent trigger ratio inverting to 10/90. Prerequisites: unit tests, documentation, reproducible dev environments, rich system context.
- **Key Publications**: "Engineering for Agents That Never Sleep" (Mar 2026), "How Cognition Uses Devin to Build Devin" (Feb 2026), "How to Run a Fleet of Cloud Agents" (Mar 2026), "The Cloud Agent Thesis" (Feb 2026). Substack: 1.7K+ subscribers.
- **Philosophy**: "That scaffolding is the difference between an agent that opens a PR and an agent that closes an incident at 3am." "Local agents make developers faster. Cloud agents make engineering orgs more capable."
- **Key Metrics**: Cognition internal: 154→659 Devin PRs/week. Industry: Stripe 1K+ agent-written PRs/week, 1.2M merged PRs across hundreds of orgs.
- **Sources**: nader.substack.com, nader.codes, LinkedIn, X (@dabit3)

#### Walden Yan (skeleton → L3)
- **Bio**: Co-Founder & CPO, Cognition AI. IOI 2020 Gold Medalist (19/343, 505.38/600). MIT PRIMES researcher (cryptography, ML). Harvard CS & Economics (2020–2024).
- **Core Ideas**: **Context Engineering** — "Share full agent traces, not just individual messages." "Actions carry implicit decisions, and conflicting decisions carry bad results." **Don't Build Multi-Agents** — current multi-agent frameworks are fragile; single-threaded agents with context continuity are more reliable.
- **Background**: DeepReason (Co-Founder & CEO, 2022–2023, security systems) → Anysphere/Cursor (Early Engineer, Jun–Aug 2023) → Inverted Agency (Managing Partner, 2020–2021). Early exposure to AI-powered coding at Cursor directly informed Devin's architecture.
- **Philosophy**: "We're still playing with raw HTML & CSS" — current agent development lacks standardization. Advocates for intellectual humility: "Our theories are likely not perfect, and we expect things to change."
- **Key Publications**: "Don't Build Multi-Agents" (Jun 2025, Cognition Blog) — most cited article on context engineering. Maven Course: "Why Devin Does Not Use Multi-Agents."
- **Sources**: cognition.ai/blog/dont-build-multi-agents, LinkedIn, Product Hunt, waldenyan.com, IOI 2020 Statistics

#### Ali Farhadi (skeleton → L2)
- **Bio**: YOLO co-creator, Xnor.ai founder (→Apple $200M), Ai2 CEO (2023-2026) → Microsoft (Mustafa Suleyman's AI team)
- **Core Ideas**: Open-source AI as default ("Open source is how we drive progress"), financial reality of frontier AI, real-time object detection philosophy, multimodal AI grounding
- **Contributions**: YOLO (80K+ citations), OLMo (#1 open model on HF Heatmap), Molmo, Dolma (5.9T tokens), OlmoTrace
- **Philosophy**: Simplicity over complexity, transparency as prerequisite for progress, real-world applicability
- **Sources**: homes.cs.washington.edu/~ali/, GeekWire articles on Ai2/Microsoft moves

#### Peter Steinberger (skeleton → L3)
- **Bio**: Austrian developer, PSPDFKit founder (1B+ device deployments, exited 2020), OpenClaw creator (135K+ instances), joined OpenAI Feb 2026
- **Core Ideas**: "Ship beats perfect" philosophy, "I don't read code anymore, I weave it", closed loop principle (compile→run→test), PRs = "Prompt Requests", polyagentmorous development (5-10 parallel agents)
- **Tooling Ecosystem**: OpenClaw, VibeTunnel, CodexBar, Peekaboo, mcporter, gogcli, agent-rules, Aspects (8.4K stars)
- **Anthropic-OpenClaw Conflict**: April 2026 policy dispute over third-party tools; account suspended then restored
- **Philosophy**: Agent-first design, CLI over MCP, cache-first engineering, main-branch development
- **Sources**: steipete.me, thewantrepreneurshow.com interview, GitHub (@steipete, 46K+ followers)

#### Shlok Khemani (skeleton → L2)
- **Bio**: Writer/programmer in Gurgaon, India. Researching personal AI and memory systems. Previously at Decentralised.co (crypto products)
- **Core Ideas**: Bitter Lesson applied to AI memory (ChatGPT's context-only approach), filesystem-first memory (Claude's CLAUDE.md vs ChatGPT's hidden profiles), personality ≠ execution separation (OpenPoke), cache-first engineering
- **Contributions**: OpenPoke (465 stars, multi-agent Poke replica), Claude Memory Tools (53 stars), Vajra (background coding agent), ChatFerry, Conjure
- **Writing**: ChatGPT Memory reverse-engineering (widely cited), Anthropic Memory Bet analysis, Claude Code source analysis
- **Philosophy**: Personality ≠ Execution, Filesystem over Database, Cache-First Design, Background Execution, Transparency over Opacity
- **Sources**: shloked.com, GitHub (@shlokkhemani)

### Concept Pages Added (from entity enrichments)
- `concepts/open-claw-ecosystem` — Peter Steinberger's OpenClaw framework
- `concepts/chatgpt-memory-bitter-lesson` — Shlok Khemani's ChatGPT memory analysis
- `concepts/claude-memory` — Claude's file-based memory architecture
- `concepts/claude-memory-tool` — Cognition copying Claude's memory approach
- `concepts/claude-code-source-patterns` — Leaked Claude Code source analysis
- `concepts/vajra-background-agent` — Vajra open-source background coding agent
- `concepts/olmo-open-language-model` — Ali Farhadi's OLMo project at Ai2

### Updated Files
- `wiki/entities/ali-farhadi.md` — skeleton → L2 (7KB)
- `wiki/entities/peter-steinberger.md` — skeleton → L3 (7.4KB)
- `wiki/entities/shlok-khemani.md` — skeleton → L2 (9.6KB)
- `wiki/index.md` — entity count 46→49, People section descriptions updated, AI Research & Computer Vision section added
- `wiki/log.md` — This entry

## 2026-04-13

### Anthropic Cookbooks — Claude Agent SDK & Managed Agents (4件)
Anthropic Cookbookから実用的なエージェント設計パターンを抽出し、概念ページとして整理。特にClaude Codeの検証済みユースケースをサーバーサイド自動化フローに転用する設計に焦点。
- **claude-agent-sdk-sre-patterns.md** — MCPサブプロセス統合、3層安全ガードレール（ディレクトリ制限/コマンドAllowlist/PreToolUseフック）、自律的インシデント対応ワークフロー
- **managed-agents-sre-incident-response.md** — Webhook駆動セッション開始、Skillsによるプログレッシブディスクロージャー、カスタムツール経由HITL承認（Slackボタン→PRマージ）
- **chief-of-staff-agent-patterns.md** — CLAUDE.md永続メモリ、Planモード（`permission_mode="plan"`）、Output Styles、カスタムスラッシュコマンド、Hooks（PreToolUse/PostToolUse）、サブエージェント委任
- **research-agent-fundamentals.md** — ステートレス(`query()`) vs ステートフル(`ClaudeSDKClient`)、バッファ管理(`max_buffer_size`)、システムプロンプトによる引用強制
- **Sources**: https://platform.claude.com/cookbook/ (56 cookbooks中10件をスキャン、優先4件をwiki化)

### OpenAI Cookbook — 方法論コンセプト追加 (6件)
OpenAI Cookbookからベンダー中立な方法論を抽出し、概念ページとして整理。
- **evaluation-flywheel.md** — 評価→分析→改善→データ収集の継続的フィードバックループ。Golden Dataset構築、Multi-Metric Evaluation、Regression Detection
- **agentic-scaffolding.md** — エージェントの安全な動作のための多層ガードレール設計。Input Validation → Execution Constraints → Output Verification → Human Oversight
- **exec-plans.md** — 計画と実行の分離パターン。事前Plan生成→レビュー→実行→検証のフロー。透明性・デバッグ性・再利用性向上
- **self-evolving-agents.md** — 自己改善するエージェント設計。4レベル（Parameter Tuning → Strategy Adaptation → Capability Expansion → Architectural Evolution）
- **resilient-prompt-engineering.md** — プロンプトをコードとして扱う設計。バージョン管理、テスト、レビュー、A/Bテスト、構造化プロンプティング
- **context-engineering.md** — コンテキストウィンドウ最適化技術。Compression、Ordering、Dynamic Management、Chunking（Anthropic版のConceptual Context Engineeringと区別）
- **Sources**: https://github.com/openai/openai-cookbook

### Steipete 過去1年投稿 — 追加Concept Pages
- **New concept pages (5件)**:
  - `direct-prompting-philosophy.md` — 「Just Talk To It」哲学。RAG/サブエージェント/カスタムフック等の過剰工学を拒否し、直接的な会話的インタラクションでAIを操るアプローチ。パラレルターミナルウィンドウパターン、コンテキストポイズン警告、直感的ディレクション開発
  - `cli-over-mcp-pattern.md` — MCPサーバーより標準CLIツールを優先する設計原則。コンテキストウィンドウ効率、モデル familiarly、デバッグ容易性の観点からCLIsが勝る。MCPが有効なユースケース（Webスクレイピング、DB探索、デザイン-to-コード）も記載
  - `ai-addiction-burnout.md` — AIコーディングエージェントによる「スロットマシン効果」、Black Eye Club現象、80時間労働週の正常化リスク。バーンアウトサイクル（発見→執着→消耗→回復）と緩和戦略
  - `self-hosting-ai-development.md` — Claude Max利用制限後のセルフホスティング検討。8xH200 vs APIコスト分析、ツール評価（opencode, charm, Cline, Gemini CLI）、Qwen3-Coder-480B vLLMデプロイガイド。「商業的にはトークン課金が経済的に健全」
  - `main-branch-development.md` — feature branch/worktreeを避けmainで直接開発するパターン。アトミックコミット、Gitをセーフティネットとして活用、Arena機能1時間構築ケーススタディ
- **Updated existing pages**:
  - `index.md` — 5新概念エントリ追加、Last updated更新
- **Sources**: steipete.me 過去1年分13投稿を抽出・分析（2025-07 〜 2026-02）

## 2026-04-13

### Cognition AI Data Analyst — Devinをデータ分析エージェントにする設計
- **New concept page**:
  - `concepts/cognition-ai-data-analyst.md` — Cognitionのデータ分析エージェント設計パターン。MCP+Knowledgeアーキテクチャ、SQL専用ツールとの違い、Knowledge設定テンプレート、実践的ワークフロー
- **Key insights**:
  - AIソフトウェアエンジニアをデータ分析に使う理由: コードベースの文脈理解+完全なデータ系譜の把握
  - MCPをセキュアなデータアクセスブリッジとして活用（Google MCP Toolbox, Metabase MCP Server 80+ツール）
  - Knowledge設定（Purpose/Guidelines/Output Format/Macro）がエージェントの精度を決定
  - Verifiable Outputs: 最終SQL+可視化+Metabaseリンクで人間が検証可能
  - 150+時間/月 → 数分の効率化
- **Sources**:
  - [Build Your Own AI Data Analyst (Part 1)](https://devin.ai/ai-data-analyst-1)
  - [Build Your Own AI Data Analyst (Part 2)](https://devin.ai/ai-data-analyst-2)

### Cognition/Devin Philosophy — Agentic Coding at Scale
- **Enhanced entity pages**:
  - `entities/scott-wu.md` — X/Twitter activity追加（"Eventually, the future comes" Devin 2.2リリース）。100x capability growth metrics（週154→659 PRs、METR結果）、technical insights（Don't Build Multi-Agents、Managed Devins転換、Context Anxiety発見、Closing the Agent Loop）
  - `entities/nader-dabit.md` — X/Twitter activity追加（Agentic Slack, Agents From Anywhere）。ターミナル/IDEの限界→Slackをエージェントインターフェースに。非同期fire-and-forget、マルチプレイヤー化
- **Enhanced concept page**:
  - `concepts/cognition-devin-philosophy.md` — Scott Wu X投稿メトリクス、Nader Dabit Agentic Slack/Agents From Anywhere詳細追加。sourcesにXリンク追加
- **Updated index.md**:
  - PeopleセクションにScott Wu, Nader Dabit, Walden Yan追加
  - Cognition/Devin Philosophyセクション新規追加（4概念ページ）
- **Removed duplicate**: `concepts/cognition-devin-agentic-coding.md`（cognition-devin-philosophy.mdに統合）
- **Sources**:
  - [Scott Wu — Eventually, the future comes](https://x.com/scottwu46/status/2026350958213787903)
  - [Nader Dabit — Agentic Slack](https://x.com/dabit3/status/2026385925593510302)
  - [Nader Dabit — Agents From Anywhere](https://x.com/dabit3/status/2025936695661826481)
  - [Cognition — Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents)
  - [Cognition — Devin Can Now Manage Devins](https://cognition.ai/blog/devin-can-now-manage-devins)
  - [Nader Dabit — Engineering for Agents That Never Sleep](https://nader.substack.com/p/engineering-for-agents-that-never)

## 2026-04-13

### Sankalp & Steipete Articles — Core Concept Extraction
- **New top-level concept pages**:
  - `inference-speed-development.md` — 推論速度で出荷する開発パラダイム (Steipete): 従来の日単位→分単位の開発サイクル、テスト駆動AI開発、UI開発パイプライン、50回試行パターン、人間の役割変化（Writer→Reviewer/Director）
  - `claude-code-best-practices.md` — Claude Code実践パターン集 (Sankalp): MCP Server活用、サブエージェント委任（--max-turns）、CLAUDE.md戦略、セッションハイジーン、アンチパターン（無限セッション、過委任、盲目的信頼、プロンプト肥大）
  - `context-window-management.md` — コンテキスト管理の一般パターン（両記事統合）: セッション分割、圧縮（`<analysis>→<summary>`）、フォークパターン、トークンエコノミクス、キャッシュ最優先エンジニアリング
- **Updated existing pages**:
  - `agentic-engineering.md` — Further ReadingにSankalp/Steipete記事追加、Related concepts拡張
  - `index.md` — 3新概念エントリ追加、Last updated更新
- **Sources**:
  - [Sankalp — My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
  - [Peter Steinberger (@steipete) — Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)

## 2026-04-13

### Sankalp & Steipete — Coding Agent Practical Patterns
- **New concept pages**:
  - `agentic-engineering/agent-first-design.md` — 「人間向け」ではなく「エージェント向け」コード設計哲学 (Steipete)
  - `agentic-engineering/cli-first-development.md` — CLI起点開発でフィードバックループ高速化 (Steipete, Sankalp)
  - `agentic-engineering/throw-away-draft-pattern.md` — 捨て台本→比較→反復サイクル (Sankalp)
- **Enhanced existing pages**:
  - `agentic-engineering/context-window-management.md` — コンテキスト60%ルール、モデル別有効限界表を追加 (Sankalp)
  - `agentic-engineering/how-agents-work.md` — Plan Mode不要論、Task Toolアーキテクチャ、Exploreエージェント制約を追加 (Steipete, Sankalp)
  - `agentic-engineering/subagents.md` — サブエージェント要約のlossiness、使い分け指針を追加 (Sankalp)
  - `agentic-engineering/_index.md` — Sankalp/Steipeteセクション追加、リーダー表拡張
- **Sources**:
  - [Sankalp — A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
  - [Steipete — Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)

## 2026-04-13

### Shlok Khemani — Memory Systems & Agent Architecture Analysis (5 articles)
- **New concept pages**:
  - `chatgpt-memory-bitter-lesson.md` — ChatGPTメモリ問題と「The Bitter Lesson」。ステートフルメモリ vs ステートレスコンテキストウィンドウ
  - `claude-memory.md` — Claudeのファイルベースメモリ（CLAUDE.md、.agent/、Git統合）
  - `claude-memory-tool.md` — CognitionがClaudeのメモリをコピーしている理由と競争力学
  - `claude-code-source-patterns.md` — Claude Code漏洩ソースの分析（プロンプト合成、キャッシュ最優先、Forkプリミティブ、Scratchpad圧縮）
  - `vajra-background-agent.md` — Vajraオープンソースバックグラウンドコーディングエージェント（Graphviz DOT、Linear統合、ファイルシステム専用アーキテクチャ）
- **New entity page**: `shlok-khemani.md` — Shlok Khemani (@shloked)
- **Sources**: shloked.com 5記事（April 2026）

### Simon Willison — Agentic Engineering Patterns Guide (L3 Enrichment)
- **simon-willison.md**: L3 Thought Analysisレベルにアップグレード
  - Added: Hoarding（知識の蓄積）哲学 — "productive kind of hoarding"
  - Added: Compound Engineering Loop — Write→Review→Improve→Save→Repeat
  - Added: Git統合の具体的プラクティス — 小さく頻繁なコミット、人間向けのメッセージ
  - Added: Writing Code is Cheap — 新しい習慣の必要性
  - Updated sources: Agentic Engineering Patterns Guideリンクを追加
- **New concept pages**:
  - `agentic-engineering/compound-engineering-loop.md` — 複合エンジニアリングループ
  - `agentic-engineering/code-hoarding.md` — 知識の蓄積と再利用パターン
- **index.md**: Updated with new concept entries


### Agent Team / Swarm Directory Created
- Created `agent-team-swarm/_index.md` — フロントページ: 5レベルモデル（Spicy Autocomplete → Dark Factory）、主要実装比較表
- Enriched `anthropic-managed-agents.md` — 公式ブログ3件（Claude Blog + Engineering Blog + Platform Docs）の情報を反映。Brain/Hands/Session分離アーキテクチャ、Multi-Agent Coordination、Pricing、Enterprise Adoption事例を追加
- New `openai-symphony.md` — WORKFLOW.md駆動のタスクオーケストレーター。SPEC.md解析、アーキテクチャコンポーネント、Symphony Go等のエコシステム、HN議論の洞察
- New `dark-factory-software-factory.md` — Simon Willison + Dan Shapiroの5レベルモデル、StrongDM実践事例、Attractor/CXB、Digital Twin Universe

## 2026-04-12

### Concept Taxonomy Restructure
- **Split `agentic-engineering/` into two directories:**
  - `agentic-engineering/` — Willisonの開発パターン (13 files remain)
  - `ai-agent-engineering/` — Anthropicのシステム構築パターン (11 files moved)
- Created `agentic-engineering/_index.md` (Willison-centric refactor)
- Created `ai-agent-engineering/_index.md` (Anthropic Engineering index)
- Updated tags in 11 moved files: `agentic-engineering` → `ai-agent-engineering`
- Updated `wiki/index.md` with new taxonomy
- **Concept**: Agentic Engineering (開発者ワークフロー) vs AI Agent Engineering (システムアーキテクチャ) vs Harness Engineering (環境設計・共通概念)

### Entity Pages
- Simon Willison entity page enriched with Agentic Engineering guide content
  - Sources: https://simonwillison.net/guides/agentic-engineering-patterns/
  - Added: 7 core patterns, 4 principles, 4 tool references, 4 related concepts
  - Expanded: Cognitive Debt theory, Context Window Management, Multi-agent patterns

### New Concept Pages (from Agentic Engineering guide)
- **context-window-management.md** — コンテキストウィンドウの戦略的管理（圧縮、構造化、優先順位付け）
- **rodney.md** — ブラウザ自動化CLIツール（エージェント向け設計、Showboat連携）
- **subagents.md** — 並列AIエージェント委任パターン（独立性、自己完結性、バッチモード）

### New Concept Pages (from OpenAI Responses API article)
- **agent-loop-orchestration.md** — エージェント実行ループ（モデル提案→シェル実行→結果フィードバック、並列実行、出力キャップ）
- **context-compaction.md** — コンテキスト圧縮（サーバーサイド自動、/compact手動、Codexによる自己改善）
- **container-context.md** — ホスト型コンテナ（永続ファイルシステム、SQLite、サイドカーエグレスプロキシ）
- **agent-skills.md** — SKILL.mdバンドル（再利用可能ワークフロー、バージョン管理、段階的探索）
- **agent-security-patterns.md** — エージェントセキュリティ（エグレスプロキシ、ドメインスコープシークレットインジェクション、許可リスト）

### Enriched
- **ai-agent-engineering/_index.md** — OpenAI Responses API 5概念を追加（エージェント実行基盤、セキュリティセクション新設）
- **wiki/index.md** — AI Agent Engineeringセクションを「Anthropic + OpenAI」に拡張

### Enriched Concept Pages
- **cognitive-debt.md** (1.5KB → 3.5KB): Vibe Coding vs Agentic Engineering対比表、認知負債のメカニズム、返済サイクル図を追加

### 2026-04-13 — Anthropic-OpenClaw Conflict & Illusion of Thinking Research

### New Concept Pages (2件)
- **anthropic-openclaw-conflict.md** — 2026年4月のAnthropicによるサードパーティAIエージェントツール（OpenClaw等）のサブアクセス遮断。135,000+インスタンス、~300xトークン格差、Peter SteinbergerのOpenAI移籍との関連性、競争力学の分析
- **illusion-of-thinking.md** — Apple (2025) + Tufts (2026)の研究。LLMがTower of Hanoiで「推論しているように見えるが実際はパターンマッチ」であることを実証。ニューロシンボリックモデルはVLA比で95% vs 34%（3ブロック）、78% vs 0%（未知4ブロック）、エネルギー効率~100x

### Entity Updates
- **entities/gary-marcus.md** — "Even more good news for the future of neurosymbolic AI" (4/12)追加。Apple+Tufts研究の分析

### New Entity Page (1件)
- **entities/peter-steinberger.md** — OpenClaw創設者、2026年2月にOpenAI入社。"Agent-first design"提唱者（status: skeleton）

### Raw Articles Saved (2件)
- `wiki/raw/articles/2026-04-12-gary-marcus-even-more-good-news-neurosymbolic.md`
- `wiki/raw/articles/2026-04-12-anthropic-openclaw-subscription-ban.md`

### Updated Files
- `wiki/index.md` — Last updated, Entity count 45→46, Anthropic-OpenClaw Conflict / Illusion of Thinking sections, Peter Steinberger in People
- `wiki/log.md` — This entry

- **Sources**:
  - https://garymarcus.substack.com/p/even-more-good-news-for-the-future
  - https://thenextweb.com/news/anthropic-openclaw-claude-subscription-ban-cost
  - https://www.breezyscroll.com/technology-news/anthropic-blocks-openclaw-founder-from-claude-what-happened/
  - https://danilchenko.dev/posts/2026-04-04-anthropic-cuts-claude-subscriptions-openclaw-third-party-tools/

## 2026-04-13 — Auto-triage ingest
- Updated: `entities/antirez-com.md` (added LLM sampling research from "First Token Cutoff LLM sampling" article)

## 2026-04-13 — 4/11-12 Inbox Triage (Neurosymbolic AI, Open-Source Philosophy, Consortium)

### New Concept Pages (3件)
- **neurosymbolic-ai.md** — ニューラルネットワーク（パターン認識）とシンボリック推論（ルールベース論理）の組み合わせアーキテクチャ。Claude Codeのprint.ts漏洩を証拠に、Gary Marcusが「LLM以降最大のAI進化はニューロシンボリック」と論じる
- **ai-coding-agent-criticism.md** — AIコーディングエージェント論争における「Center Has a Bias」論文（Armin Ronacher）。批判の対称性分析：直接体験派 vs 抽象批判派、エンゲージメントバイアスの構造的説明
- **open-model-consortium.md** — オープンモデルコンソーシアムの必然性（Nathan Lambert）。NVIDIA Nemotron Coalition、Stanford Marin、Arcee AIの動向。オープンモデルが公共財としての性格を持つことの論証

### Entity Updates
- **entities/gary-marcus.md** — Updated `updated` date, added "The biggest advance in AI since the LLM" to recent posts
- **entities/geohot-github-io.md** — Added Apr 2026 "OpenAI is nothing without its people" and Mar 2026 posts (neofeudalism, 69 agents, Two Worlds)
- **entities/armin-ronacher.md** — Added 4/11 "The Center Has a Bias" to timeline and sources, added `ai-coding-agent-criticism` cross-reference
- **entities/nathan-lambert.md** — Added to index.md People section (Open Source AI & Consortium)

### Raw Articles Saved (4件)
- `wiki/raw/articles/2026-04-11-gary-marcus-biggest-advance-ai-llm.md`
- `wiki/raw/articles/2026-04-11-geohot-openai-nothing-without-people.md`
- `wiki/raw/articles/2026-04-11-armin-ronacher-center-has-a-bias.md`
- `wiki/raw/articles/2026-04-12-nathan-lambert-open-model-consortium.md`

### Updated Files
- `wiki/index.md` — Last updated, Neurosymbolic AI section, Open Source AI & Consortium section, People additions
- `wiki/log.md` — This entry

- **Sources**:
  - https://garymarcus.substack.com/p/the-biggest-advance-in-ai-since-the
  - https://geohot.github.io//blog/jekyll/update/2026/04/11/openai-people.html
  - https://lucumr.pocoo.org/2026/4/11/the-center-has-a-bias/
  - https://www.interconnects.ai/p/the-inevitable-need-for-an-open-model
