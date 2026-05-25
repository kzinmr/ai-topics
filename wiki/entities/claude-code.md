     1|---
     2|title: Claude Code
     3|type: entity
     4|created: 2026-04-24
     5|updated: 2026-05-25
     6|tags:
     7|  - product
     8|  - coding-agent
     9|  - anthropic
    10|  - economics
    11|aliases:
    12|  - Claude Code CLI
    13|  - Anthropic Coding Agent
    14|  - Claude Code Desktop
    15|sources:
    16|  - https://x.com/ClaudeDevs/status/2054610152817619388
    17|  - https://www.latent.space/p/ainews-codex-rises-claude-meters
    18|  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
    19|  - https://code.claude.com/en/whats-new/2026-w15
    20|  - https://code.claude.com/en/whats-new/2026-w14
    21|  - https://code.claude.com/en/changelog
    22|  - https://www.getaiperks.com/en/articles/claude-code-updates
    23|  - https://arxiv.org/html/2604.14228v1
    24|  - https://claude.com/blog/introducing-routines-in-claude-code
    25|  - "[[raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions]]"
  - "[[raw/articles/2026-05-25_sairahul1_claude-code-software-factory-7-agents]]"
    26|---
    27|
    28|# Claude Code
    29|
    30|AnthropicのAIコーディングエージェント。CLI、デスクトップアプリ、VS Code/JetBrains拡張、Web、iOS、Slackマルチサーフェスで動作。[[entities/boris-cherny]]によって開発された。
    31|
    32|SWE-bench Verifiedで72.7%を達成。2026年4月現在、7.6倍のデプロイ頻度向上、89%のAI採用率を記録する業界トップのコーディングエージェント。
    33|
    34|## 基本情報
    35|
    36|| 項目 | 内容 |
    37||------|------|
    38|| 開発元 | Anthropic |
    39|| 開発者 | Boris Cherny |
    40|| 初回リリース | 2025年5月（GA） |
    41|| 最新メジャー | v2.1.119（2026年4月23日） |
    42|| 標準モデル | Opus 4.7, Sonnet 4.6, Haiku 4.5 |
    43|| 対応環境 | CLI, Desktop, VS Code, JetBrains, Web, iOS, Slack |
    44|
    45|## Sub-Pages
    46|
    47|- **[[claude-code--capabilities]]** — Key metrics, latest features (Ultraplan, Monitor, Auto Mode, Routines, CLI Computer Use, Fast Mode), and key capabilities (Subagents, MCP Integration, Slash Commands, Checkpointing, Skills System)
    48|- **[[claude-code--architecture]]** — 5-layer decomposition, 7-component flow, core loop, infrastructure dominance (98.4% deterministic infra)
    49|- **[[claude-code--history]]** — Origins, internal dogfooding, GA, Agent Teams GA, and the source code leak incident
    50|
    51|## Key Metrics (2026)
    52|
    53|| Metric | Value |
    54||--------|-------|
    55|| SWE-bench Verified | 72.7% (vs Codex 69.1%) |
    56|| Deployment frequency increase | **7.6x** |
    57|| AI adoption across employees | **89%** |
    58|| Feature delivery speed | **2x faster** |
    59|| Incident investigation speed | **80% faster** |
    60|
    61|## Comparisons
    62|
    63|- **Cursor** — Competitor
    64|- **OpenAI Codex** — Competitor (SWE-bench: 69.1% vs Claude Code 72.7%)
    65|
    66|## Related
    67|
    68|- [[entities/boris-cherny]] — Creator
    69|- [[entities/anthropic]] — Developer
    70|- [[entities/claude-mythos]] — Withheld high-security model
    71|- [[concepts/project-glasswing]] — Safety initiative
    72|- [[concepts/harness-engineering]]
    73|
    74|## Sources
    75|
    76|- [Claude Code What's New — Week 15 (Ultraplan, Monitor)](https://code.claude.com/en/whats-new/2026-w15) (Apr 2026)
    77|- [Claude Code What's New — Week 14 (CLI Computer Use)](https://code.claude.com/en/whats-new/2026-w14) (Apr 2026)
    78|- [Claude Code Changelog](https://code.claude.com/en/changelog)
    79|- [Introducing Routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) (Apr 14, 2026)
    80|- [Auto Mode Blog](https://claude.com/blog/auto-mode) (Mar 24, 2026)
    81|- [GetAI Perks — Claude Code Updates 2026](https://www.getaiperks.com/en/articles/claude-code-updates) (Mar 26, 2026)
    82|- [arXiv:2604.14228v1 — Dive into Claude Code Architecture](https://arxiv.org/html/2604.14228v1) (Apr 2026)
    83|- [Claude Code Camp — How the team really works](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) (Feb 5, 2026)
    84|- [The Register — Claude Code source code leak](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) (Mar 31, 2026)
    85|- [Anthropic — Measuring Agent Autonomy](https://www.anthropic.com/news/measuring-agent-autonomy) (Feb 2026)
    86|- [Kuber Studio — Claude Code Source Code Leak Analysis](https://kuber.studio/blog/AI/Claude-Code's-Entire-Source-Code-Got-Leaked-via-a-Sourcemap-in-npm,-Let's-Talk-About-it) (Apr 2026)
    87|
    88|
    89|
    90|### Agent View — Unified Session Management (Research Preview, May 2026)
    91|
    92|Claude Code introduced **Agent View**, a research preview feature providing a unified list of all active Claude Code sessions:
    93|
    94|| Feature | Detail |
    95||---------|--------|
    96|| **Functionality** | Unified dashboard showing all active agent sessions |
    97|| **Status** | Research preview |
    98|| **Use case** | Monitor and manage multiple concurrent Claude Code sessions from a single interface |
    99|
   100|**Related session control commands** (Claude Code team thread, May 2026):
   101|- **`/goal`** — Define a high-level objective for the agent to work toward autonomously
   102|- **`/loop`** — Run a task in a continuous improvement loop
   103|- **`/schedule`** — Schedule recurring agent runs at specified intervals
   104|
   105|**Significance**: Agent View addresses the growing need for multi-agent session management as developers increasingly run multiple Claude Code sessions in parallel (per Boris Cherny's parallel worktree pattern). Combined with `/goal`, `/loop`, and `/schedule`, these represent a shift from interactive coding agent to persistent, managed agent workforce.
   106|
   107|Source: Aakash's Clicky newsletter (May 2026)
   108|
   109|## References
   110|
   111|- 2026-04-16-vivek-trivedy-harness-memory-context-fragments
   112|- 2026-04-28_x-article-the-harness-is-the-backend
   113|- 2026-04-30_willccbb-analysis-rl-harness-lifecycle
   114|- 2026-04-30_willccbb-rl-harness-lifecycle
   115|- 2026-04-viv-harness-memory-context-fragments-bitter-lesson
   116|- 2039441705586602134_The-Trillion-Dollar-Loop-B2B-Never-Had
   117|- 2042660310851449223_Latent-Briefing-Efficient-Memory-Sharing
   118|- crawl-2026-04-23-build-harness-not-code
   119|- crawl-2026-04-23-harness-engineering-discipline
   120|
   121|- 2026-01-02_boris-cherny---my-claude-code-setup-(jan-2026)
   122|- 2026-01-31_boris-cherny---10-tips-from-the-claude-code-team-(feb-2026)
   123|- 2026-02-11_chernycode---boris-cherny's-claude-code-config-files
   124|- 2026-03-19-claude-agents-disagree-experiment
   125|- 2026-04-09-claude-managed-agents-guide
   126|- 2026-04-26-claude-code-openclaw-harness-practice
   127|- 2026-keep-your-claude-code-context-clean-with-subagents
   128|- 2041927992986009773_Launching-Claude-Managed-Agents
   129|- 2047720067107033525_Memory-in-Claude-Managed-Agents
   130|- boris-cherny-im-boris-i-created-claude-code
   131|- crawl-2026-04-23-claude-code-design-space
   132|- how-claude-code-team-really-works
   133|
   134|## Usage & Workflows
   135|
   136|#### 7-Agent Software Factory Workflow (May 2026)
   137|
   138|@sairahul1（[[entities/sairahul1|Rahul]]）による Claude Code を7つの特化エージェントに分割するパイプライン手法。vibe coding の限界を克服し、構造化されたソフトウェア開発を実現する：
   139|
   140|```
   141|Researcher → Story Writer → Spec Writer → Backend Builder → Frontend Builder → Test Verifier → Validator
   142|  (Read)       (Read)         (Read)      (Backend only)    (Frontend only)    (Test files)        (Read)
   143|```
   144|
   145|**3 human checkpoints**: ストーリー承認 → 設計書承認 → PRレビュー。それ以外は完全自動。
   146|
   147|**CLAUDE.md の中心性**: 100-300行のリポジトリルートMarkdownが全エージェントの共有知識ベース。AIが間違えるたびに追記し、チームの集合記憶として進化させる。
   148|
   149|See: [[concepts/dark-factory-software-factory]] for full case study and StrongDM comparison.
   150|
   151|Source: [[raw/articles/2026-05-25_sairahul1_claude-code-software-factory-7-agents]]
   152|
   153|### Core Workflow Patterns
   154|
   155|#### Parallel Agent Execution
   156|Boris Chernyの最も影響力のある洞察:
   157|> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."
   158|
   159|- 1つのエージェントがログを読みクエリを実行（分析用ワークツリー）
   160|- 複数のエージェントが並行して機能を実装（機能用ワークツリー）
   161|- 人間はコーディネーター兼承認者として機能
   162|
   163|#### Plan Mode → Auto-Accept
   164|1. **Plan Modeで開始** (`Shift+Tab` 2回) — Claudeがアプローチを概説
   165|2. **レビューと改善** — 計画が堅固になるまでClaudeと対話
   166|3. **Auto-acceptに切り替え** — Claudeが計画を実行、通常は一発で成功
   167|4. **検証** — Claudeがテストを実行またはブラウザ拡張機能で確認
   168|
   169|#### CLAUDE.md as Team Memory
   170|- チームで共有するファイルをgitで管理
   171|- 間違いのたびにCLAUDE.mdを更新
   172|- PRで`@claude`を使用してガイドラインを更新
   173|
   174|### Terminal Environment
   175|
   176|#### Recommended Setup
   177|- **Ghostty**: チームが推奨（同期レンダリング、24-bitカラー、Unicodeサポート）
   178|- **tmux**: ワークツリーごとにタブをカラーコード/命名
   179|- シェルエイリアス（za, zb, zc）で瞬時のワークツリー切り替え
   180|- ターミナルタブを1-5に番号付け、システム通知を有効化
   181|
   182|#### Mobile-to-Desktop Workflow (2026)
   183|iOSからタスクを開始し、デスクトップにルーティングして実行、PRとして仕上げる「Phone to PR」ワークフローに対応。
   184|
   185|### Claude Design Integration
   186|
   187|Claude Design (April 2026) creates a direct handoff pipeline to Claude Code. When a design is complete, Claude Design packages everything into a handoff bundle that Claude Code can receive with a single instruction.
   188|
   189|### Pricing (April 2026)
   190|
   191|| Plan | Price | Details |
   192||
   193|
   194|### Programmatic Usage Metering (May 2026)
   195|
   196|On May 13, 2026, Anthropic announced a major pricing change via [@ClaudeDevs](https://x.com/ClaudeDevs/status/2054610152817619388), effective June 15, 2026:
   197|
   198|- **Every paid Claude subscription now includes a dedicated monthly credit for programmatic usage**, equal to the dollar amount of the plan (e.g., $200/mo plan = $200 API credits)
   199|- **Programmatic usage** covers: Claude Agent SDK, `claude -p`, Claude Code GitHub Actions, and third-party apps built on the Agent SDK
   200|- **Interactive usage** (Claude.ai, Claude Code CLI/Desktop) retains its own limits separate from the API credit pool
   201|- Previously, programmatic usage via OpenClaw, OpenCode, and other third-party harnesses was effectively subsidized at 70-90% below API pricing — this change formalizes and meters it
   202|
   203|The announcement was met with mixed reactions: framed as a "rug pull" by some users who relied on the historical subsidy, but viewed by Anthropic as rationalizing a pricing model that was never sustainable for third-party harness usage. OpenClaw and OpenCode had already been selectively targeted; the new policy makes metering universal and transparent.
   204|
   205|**Context**: This coincides with OpenAI's launch of an [enterprise switch promo](https://x.com/OpenAIDevs/status/2054586214112780518) the same day. Anthropic is consolidating its most favorable pricing behind its own tools (Claude Code, Claude.ai) now that its brand is established, while OpenAI Codex as the challenger maintains more liberal usage policies. See [[concepts/mandate-equinox]] for the broader competitive cycle.
   206|
   207|Sources: [@ClaudeDevs — May 13, 2026](https://x.com/ClaudeDevs/status/2054610152817619388), [AINews: Codex Rises, Claude Meters Programmatic Usage](https://www.latent.space/p/ainews-codex-rises-claude-meters)------|-------|---------|
   208|| **Pro** | $17/mo annual or $20/mo monthly | Claude Code included; Sonnet 4.6 + Opus 4.7 |
   209|| **Max 5x** | $100/mo | Larger codebases, more usage |
   210|| **Max 20x** | $200/mo | Maximum access, power users |
   211|| **Team** | $20/seat/mo (5–150 seats) | Self-serve seat management |
   212|| **Enterprise** | Contact sales | Advanced security, data management |
   213|| **API** | Pay-as-you-go | No per-seat fee, unlimited developers |
   214|
   215|---
   216|
   217|## Prompt Caching Architecture (April 2026)
   218|
   219|Claude Code is built around prompt caching from day one. The team runs alerts on cache hit rate and declares SEVs if it's too low. Key architectural decisions:
   220|
   221|- **Static-first layout**: System prompt → Claude.MD → Session context → Messages. Any change anywhere in the prefix invalidates everything after it.
   222|- **Messages over prompt edits**: When information becomes stale, `<system-reminder>` tags in messages preserve the cache.
   223|- **No mid-session model switching**: Cache is per-model. Switching mid-conversation is more expensive than continuing.
   224|- **Tool state via tools, not tool set changes**: Plan Mode uses `EnterPlanMode`/`ExitPlanMode` as tools rather than swapping tool definitions.
   225|- **Deferred tool loading**: Lightweight stubs (`defer_loading: true`) with `ToolSearch` for discovery keep the prefix stable.
   226|- **Cache-safe compaction**: Context compaction reuses the parent's exact system prompt, tools, and history to get cache hits.
   227|
   228|**April 2026 Regression**: Shipped a 47% performance regression caught by user community before internal monitoring — a widely-cited lesson on immature production agent eval practices even at the leaders.
   229|
   230|Sources: "Lessons from Building Claude Code: Prompt Caching Is Everything" (April 2026), "Prompt auto-caching with Claude" (@RLanceMartin)
   231|
   232|See also: [[concepts/prompt-caching]], [[concepts/context-engineering]]
   233|
   234|## Session Management (Agent SDK)
   235|
   236|Claude Code Agent SDKは、Context Engineering の抽象概念を**型付きAPIプリミティブ**として実装している。セッション管理（[Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)）は、MartinのWrite/Select/Compress/IsolateフレームワークのSDKレベルでの具現化である。
   237|
   238|### セッションの基本構造
   239|
   240|セッションは「プロンプト + 全ツール呼び出し + 全ツール結果 + 全応答」を含む完全な会話履歴。`~/.claude/projects/<encoded-cwd>/*.jsonl` に自動永続化される。セッションは**会話**を永続化し、**ファイルシステム変更**はFile Checkpointingが別途管理する（関心の分離）。
   241|
   242|### 3つの操作: Continue / Resume / Fork
   243|
   244|| 操作 | API | 機能 | Context Engineering 対応 |
   245||------|-----|------|------------------------|
   246|| **Continue** | Python: `ClaudeSDKClient` / TS: `continue: true` | カレントディレクトリの最新セッションを自動検出・追記 | **Write + Select** — 透過的なコンテキスト永続化と復元 |
   247|| **Resume** | `resume=<session_id>` | 指定IDのセッションを復元。全過去コンテキストにアクセス | **Select** — 精密なコンテキスト検索。プロセス再起動・マルチユーザー対応 |
   248|| **Fork** | `resume=<id>, fork_session=True` | 元セッションをコピーした新規セッション。元は不変 | **Isolate** — 会話履歴の分岐。別アプローチの安全な試行 |
   249|
   250|### Context Engineering フレームワークとのアーキテクチャ対応
   251|
   252|```
   253|Context Engineering 抽象          Claude Code SDK 実装
   254|─────────────────────────        ──────────────────────
   255|Write（外部保存）               自動セッション永続化（JSONL）
   256|Select（選択的取り込み）         Resume by session_id
   257|Compress（圧縮）                auto-compact（95%しきい値）
   258|Isolate（分離）                 Fork + Sub-agents（独立セッション）
   259|Offload（ファイルシステム分離）   File Checkpointing（会話状態 ≠ ファイル状態）
   260|```
   261|
   262|**クロスホスト**: JSONLファイルの移動または `SessionStore` アダプターでCI/サーバーレス環境間のセッション復元が可能。セッションの列挙・リネーム・タグ付け用ユーティリティ（`list_sessions()`, `tag_session()` 等）も提供。
   263|
   264|### 設計上の含意
   265|
   266|Context Engineeringはアドホックなプロンプト設計から、**SDKの型付きAPIとして標準化**されつつある。MartinのBitter Lesson — 「モデル改善に伴いハーネスは削ぎ落とされる」 — の対極として、セッション管理のような**基盤プリミティブ**はSDKに吸収される方向に進化している。
   267|
   268|Source: [[raw/articles/2026-05-13_anthropic_claude-code-agent-sdk-sessions]]
   269|
   270|