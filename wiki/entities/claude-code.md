---
title: Claude Code
created: 2026-04-24
updated: 2026-04-24
tags:
  - product
  - coding-agent
  - anthropic
  - openai
aliases:
  - Claude Code CLI
  - Anthropic Coding Agent
---

# Claude Code

AnthropicのAIコーディングエージェントCLI。Boris Chernyによって開発され、AnthropicからOpenAIへ移管された。SWE-bench Verifiedで72.7%を達成し、OpenAI Codex (69.1%)を上回る。

## Overview

Claude CodeはAnthropicが開発したターミナルベースのAIコーディングエージェント。CLIとして動作し、ファイルの読み書き、コマンド実行、テスト実行などを自律的に行う。Anthropicのエンジニアリングチームでdogfoodingされ、2025年5月にGAリリースされた。

## Key Metrics

| Metric | Value |
|--------|-------|
| SWE-bench Verified | 72.7% (vs Codex 69.1%) |
| PR throughput improvement | 67% |
| Active user growth (mid-2025) | 300%+ |
| Run-rate revenue expansion | 5.5x |
| Claude usage that is coding | 36% of total |
| Claude Code interactions with automation | 79% |

## Development History

### Origins (Sep 2024)
Boris ChernyがAnthropicに入社し、Claude 3.6モデルでプロトタイピングを開始。最初のプロトタイプはAppleScript経由で音楽を特定・変更するCLIツールだった。以前のAnthropic研究プロジェクト「Clide」の影響を受けていたが、Clideの非効率性（遅い起動時間、重いインデックス要件）から学んで改善した。

### Internal Dogfooding (Nov 2024)
- **20%のエンジニア**が初日に採用
- **5日間以内に50%が採用**
- 1日60-100回の内部リリース
- 70-80%の技術スタッフが毎日使用

### General Availability (May 2025)
- チームは約10人のエンジニアに拡大
- 2025年7月時点ですでに高い成長率を記録

### OpenAI移管 (Jul 2025)
AnthropicからOpenAIへ移管され、Boris ChernyがHead of Claude Codeとして開発を継続。

## Architecture (arXiv:2604.14228v1, Apr 2026)

2026年4月の論文による設計分析：

### 7-Component Flow
`User → Interfaces → Agent Loop → Permission System → Tools → State & Persistence → Execution Environment`

### 5-Layer Decomposition
1. **Surface**: エントリポイントとレンダリング（CLI, SDK, IDE）
2. **Core**: エージェントループと5層コンパクションパイプライン
3. **Safety/Action**: パーミッションシステム、フック、拡張性、サンドボックス、サブエージェント
4. **State**: コンテキストアセンブリ、ランタイムステート、追記型JSONL永続化、CLAUDE.mdメモリ
5. **Backend**: シェル実行、MCPクライアント、リモートツール

### Infrastructure Dominance
- **~1.6%** のコードベースのみがAI判断ロジック
- **~98.4%** が決定論的運用インフラ（パーミッション、コンテキスト管理、リカバリ、ツールルーティング）

### Core Loop
シンプルな `while-true` 非同期ジェネレータ (`queryLoop()`) がモデルを呼び出し、ツールをディスパッチし、繰り返す。**ReActパターン**に従う。

## Source Code Leak Incident (Mar 31, 2026)

### What Happened
セキュリティ研究者Chaofan Shouが、Claude Codeのnpmパッケージに含まれるsourcemapファイルを通じて、難読化されていないTypeScriptの全ソースコードへの参照を発見。この参照はAnthropicのCloudflare R2ストレージバケット上のzipアーカイブを指しており、ダウンロード・解凍が可能だった。

### Impact
- GitHubにソースコードのバックアップがアップロードされ、**41,500回以上フォーク**された
- npmパッケージのsourcemapファイルが原因
- sourcemapファイルは本番環境のバンダルコードを元のソースにマッピングするために存在するが、 Anthropicのビルドチェーンが未難読化のTypeScriptソースを参照していた

### Significance
この漏洩により、Claude Codeの内部設計が完全に公開された状態となり、AIコーディングエージェントのアーキテクチャ理解に大きな影響を与えた。

## Core Workflow Patterns

### Parallel Agent Execution
Boris Chernyの最も影響力のある洞察：
> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

- 1つのエージェントがログを読みクエリを実行（分析用ワークツリー）
- 複数のエージェントが並行して機能を実装（機能用ワークツリー）
- 人間はコーディネーター兼承認者として機能

### Plan Mode → Auto-Accept
1. **Plan Modeで開始** (`Shift+Tab` 2回) — Claudeがアプローチを概説
2. **レビューと改善** — 計画が堅固になるまでClaudeと対話
3. **Auto-acceptに切り替え** — Claudeが計画を実行、通常は一発で成功
4. **検証** — Claudeがテストを実行またはブラウザ拡張機能で確認

> "Don't keep pushing when a plan fails — stop, re-plan, then execute."

### CLAUDE.md as Team Memory
- チームで共有するファイルをgitで管理
- 間違いのたびにCLAUDE.mdを更新
- PRで`@claude`を使用してガイドラインを更新

## Key Features

### NO_FLICKER Renderer
`CLAUDE_CODE_NO_FLICKER=1` 実験的レンダラー：
- 会話の成長に伴う画面のちらつき/ジャンプを解消
- 会話の長さに関係なく一定のメモリ/CPUを維持
- マウスサポート（クリックでカーソル配置、クリック可能なUI要素）
- テキスト選択動作の改善

### Subagents
> "Append 'use subagents' to any request where you want more compute."

- バックグラウンド分析タスク
- 複数ワークツリーでの並行コード探索
- 長時間実行クエリやデータ処理
- メインセッションのコンテキストを集中させたまま、サブエージェントがサイドタスクを処理

### MCP Integration
- **BigQuery**: チームはBigQueryスキルをコードベースにチェックイン。「Borisは数ヶ月SQLを書いていない」
- **Slack**: ClaudeがMCPサーバー経由でSlackにアクセス
- **Sentry**: Claudeが直接エラーログを読み取る
- 設定は`.mcp.json`でリポジトリにチェックイン

### Slash Commands
> "If you do something more than once a day, turn it into a skill."

- `/simplify` — PR shepherdingの自動化
- `/batch` — 並行コードマイグレーション
- `/commit-push-pr` — PR最終処理の自動化
- `/techdebt` — セッション終了時にコードベースのスキャン
- `/sync-context` — 7日間のSlack、GDrive、Asana、GitHubアクティビティをコンテキストとしてダンプ

## Terminal Environment

### Recommended Setup
- **Ghostty**: チームが推奨（同期レンダリング、24-bitカラー、Unicodeサポート）
- **tmux**: ワークツリーごとにタブをカラーコード/命名
- シェルエイリアス（za, zb, zc）で瞬時のワークツリー切り替え
- ターミナルタブを1-5に番号付け、システム通知を有効化

### PostToolUse Hooks
Claudeのコード出力後、自動的にフォーマットを実行するフック。ツール使用パイプラインの一部として実行され、バージョン管理に至る前にフォーマット問題を捕捉。

## Model Choice

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

- 思考モードにより複雑な問題への対応能力が向上
- トークンあたりのレイテンシは高いが、修正サイクルが減少
- 計画への投資が総時間を短縮

## Related

- [[boris-cherny]] — Creator
- [[anthropic]] — Original developer
- [[openai]] — Current owner (since Jul 2025)
- [[claude-opus-4.7]] — Latest model used
- [[claude-mythos]] — Withheld model
- [[project-glasswing]] — Safety initiative
- [[harness-engineering]]
- [[concepts/agentic-engineering.md]]

## Sources

- [arXiv:2604.14228v1 — "Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems"](https://arxiv.org/html/2604.14228v1) (Apr 2026)
- [The Register — "Anthropic accidentally exposes Claude Code source code"](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) (Mar 31, 2026)
- [Kuber Studio — "Claude Code's Entire Source Code Got Leaked via a Sourcemap"](https://kuber.studio/blog/AI/Claude-Code's-Entire-Source-Code-Got-Leaked-via-a-Sourcemap-in-npm,-Let's-Talk-About-it) (Apr 2026)
- [Claude Code Camp — "How the Claude Code team really works"](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) (Feb 5, 2026)
- [Boris Cherny — "I'm Boris and I created Claude Code"](https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/) (Jan 2, 2026)
- [ChernyCode Repository](https://github.com/meleantonio/ChernyCode) — Curated config files
- [Peterman Podcast — Boris Cherny interview](https://paddo.dev/blog/how-boris-uses-claude-code/) (Dec 2025)
