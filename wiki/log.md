---
title: "Wiki Change Log"
---

# Wiki Change Log

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
