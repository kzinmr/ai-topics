---
title: Claude Code
type: entity
created: 2026-04-24
updated: 2026-04-27
tags:
  - product
  - coding-agent
  - anthropic
aliases:
  - Claude Code CLI
  - Anthropic Coding Agent
  - Claude Code Desktop
sources:
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - https://code.claude.com/en/whats-new/2026-w15
  - https://code.claude.com/en/whats-new/2026-w14
  - https://code.claude.com/en/changelog
  - https://www.getaiperks.com/en/articles/claude-code-updates
  - https://arxiv.org/html/2604.14228v1
  - https://claude.com/blog/introducing-routines-in-claude-code
  - https://claude.com/blog/auto-mode
---

# Claude Code

AnthropicのAIコーディングエージェント。CLI、デスクトップアプリ、VS Code/JetBrains拡張、Web、iOS、Slackマルチサーフェスで動作。Boris Chernyによって開発され、2025年7月にAnthropicからOpenAIへ移管された。

SWE-bench Verifiedで72.7%を達成。2026年4月現在、7.6倍のデプロイ頻度向上、89%のAI採用率を記録する業界トップのコーディングエージェント。

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | Anthropic（オリジナル）→ OpenAI（2025年7月移管） |
| 開発者 | Boris Cherny |
| 初回リリース | 2025年5月（GA） |
| 最新メジャー | v2.1.119（2026年4月23日） |
| 標準モデル | Opus 4.7, Sonnet 4.6, Haiku 4.5 |
| 対応環境 | CLI, Desktop, VS Code, JetBrains, Web, iOS, Slack |

## Key Metrics (2026)

| Metric | Value |
|--------|-------|
| SWE-bench Verified | 72.7% (vs Codex 69.1%) |
| Deployment frequency increase | **7.6x** |
| Week-over-week deployment growth | **14%** |
| Incident investigation speed | **80% faster** |
| Feature delivery speed | **2x faster** |
| AI adoption across employees | **89%** |
| PR throughput improvement | 67% |
| Active user growth (mid-2025) | 300%+ |
| Claude usage that is coding | 36% of total |

## Latest Features (April 2026)

### Ultraplan (Week 15 — v2.1.92–v2.1.101, Apr 6–10)
Claude Codeの**クラウド計画機能**: CLIから計画をクラウドにドラフトし、Webエディタでレビュー・コメント、リモート実行またはローカルにPull可能。

- 初回実行時に自動でクラウド環境を作成
- Web上のインタラクティブエディタで計画を閲覧・編集
- チームメンバーと計画を共有し、コメントベースでレビュー
- 大規模リファクタリングや複雑なマルチステップタスクに最適

### Monitor Tool (v2.1.92+)
バックグラウンドイベントを会話にストリーミングする新しいツール。Claudeが**ログをテールし、リアルタイムに反応**できる。

- 長時間ジョブの進捗モニタリング
- エラーログの自動検出と対応
- デプロイ監視と自動ロールバック判断

### Auto Mode (Mar 24, 2026)
`--dangerously-skip-permissions` の安全な代替。分類器がパーミッションプロンプトを処理:

- 安全なアクション → 自動実行（中断なし）
- リスクのあるアクション → ブロック
- 手動承認と完全自動の間のバランスを提供
- 長時間実行タスクに最適化

### Routines (Apr 14, 2026)
一度設定したルーティンをスケジュール・APIコール・イベントトリガーで実行。

- 定期的なコードメンテナンスタスクの自動化
- CI/CDパイプラインとの統合
- イベント駆動型の自動修正ワークフロー

### Redesigned Desktop App (Apr 14, 2026)
複数のClaude Codeタスクを同時実行可能なデスクトップアプリに刷新。

- 並列タスク管理
- ビジュアルDiffの確認
- サーバープレビュー機能
- PRステータスの一元管理

### CLI Computer Use (Research Preview — Week 14, v2.1.86+)
CLIから直接**ネイティブアプリを操作**可能に:

- GUIでのみ確認可能なUI変更を自動検証
- アプリを開き、UIをクリック操作
- ヘッドレス環境でのE2Eテスト自動化

### Fast Mode (Research Preview)
Opus 4.6ベースで**2.5倍高速**な実行モード:

| モード | 速度 | 価格（入力/出力 百万トークンあたり） |
|--------|------|--------------------------------------|
| Standard (Opus 4.7) | 1x | $15/$75 |
| **Fast mode** (Opus 4.6) | **2.5x** | $30/$150 |

- 短いタスクや高速なイテレーションに最適
- 研究プレビュー段階

## Architecture (arXiv:2604.14228v1, Apr 2026)

### 7-Component Flow
```
User → Interfaces → Agent Loop → Permission System → Tools → State & Persistence → Execution Environment
```

### 5-Layer Decomposition
1. **Surface**: エントリポイントとレンダリング（CLI, SDK, IDE, Desktop, Web）
2. **Core**: エージェントループと5層コンパクションパイプライン
3. **Safety/Action**: パーミッションシステム、フック、拡張性、サンドボックス、サブエージェント
4. **State**: コンテキストアセンブリ、ランタイムステート、追記型JSONL永続化、CLAUDE.mdメモリ
5. **Backend**: シェル実行、MCPクライアント、リモートツール

### Infrastructure Dominance
- **~1.6%** のコードベースのみがAI判断ロジック
- **~98.4%** が決定論的運用インフラ（パーミッション、コンテキスト管理、リカバリ、ツールルーティング）

### Core Loop
シンプルな `while-true` 非同期ジェネレータ (`queryLoop()`) がモデルを呼び出し、ツールをディスパッチし、繰り返す。**ReActパターン**に従う。

## Development History

### Origins (Sep 2024)
Boris ChernyがAnthropicに入社し、Claude 3.6モデルでプロトタイピングを開始。最初のプロトタイプはAppleScript経由で音楽を特定・変更するCLIツールだった。

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

### Agent Teams GA (2026)
マルチエージェント協調機能がGeneral Availabilityに到達。複数のClaude Codeインスタンスが役割分担しながら並行作業を実行可能。

## Key Features

### NO_FLICKER Renderer
`CLAUDE_CODE_NO_FLICKER=1` 実験的レンダラー:
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
- **BigQuery**: チームはBigQueryスキルをコードベースにチェックイン
- **Slack**: ClaudeがMCPサーバー経由でSlackにアクセス
- **Sentry**: Claudeが直接エラーログを読み取る
- 設定は`.mcp.json`でリポジトリにチェックイン
- **MCP懒加载** (v2.1.76): 数百のツールを事前ロードせず、コンテキストに関連するツールのみアクティブ化 → 起動オーバーヘッド削減

### Slash Commands
- `/simplify` — PR shepherdingの自動化
- `/batch` — 並行コードマイグレーション
- `/commit-push-pr` — PR最終処理の自動化
- `/techdebt` — セッション終了時にコードベースのスキャン
- `/sync-context` — 7日間のSlack、GDrive、Asana、GitHubアクティビティをコンテキストとしてダンプ
- `/team-onboarding` (v2.1.92+) — セットアップを再生可能ガイドにパッケージ化
- `/autofix-pr` (v2.1.92+) — ターミナルからPR自動修正を有効化
- `/loop` (v2.1.92+) — 間隔省略時にセルフペーシング対応
- `/powerup` (v2.1.86+) — インタラクティブレッスン

### Checkpointing
ファイルレベルのリストアポイント。自律的マルチステップタスク用:

- セッション中のファイル変更を追跡
- 任意の以前の状態に復元可能
- gitと異なり**タスクレベル**で動作
- Python: `enable_file_checkpointing=True`, TypeScript: `enableFileCheckpointing: true`

### Hook System (v2.1.83+)
条件付き `if` フック: 特定の条件で自動アクションを実行。ツール使用後のフォーマット実行など。

### Cross-App Context Sharing (Mar 2026)
ExcelとPowerPointのClaudeアドイン間で会話コンテキストを共有。アクションが別アプリに引き継がれる。

### Custom Visualizations (Mar 12, 2026)
Claudeがコード内で直接チャート、図、ビジュアライゼーションを動的に生成。

### Skills System
- カスタムコマンドでClaude Codeを拡張
- `$ARGUMENTS`, `$ARGUMENTS[N]`, `${CLAUDE_SESSION_ID}` テンプレート変数
- 拡張バンドルスキルライブラリ
- ネストディレクトリからの自動発見

### PostToolUse Hooks
Claudeのコード出力後、自動的にフォーマットを実行するフック。ツール使用パイプラインの一部として実行され、バージョン管理に至る前にフォーマット問題を捕捉。

## Pricing (April 2026)

| Plan | Price | Details |
|------|-------|---------|
| **Pro** | $17/mo annual or $20/mo monthly | Claude Code included; Sonnet 4.6 + Opus 4.7 |
| **Max 5x** | $100/mo | Larger codebases, more usage |
| **Max 20x** | $200/mo | Maximum access, power users |
| **Team** | $20/seat/mo (5–150 seats) | Self-serve seat management |
| **Enterprise** | Contact sales | Advanced security, data management |
| **API** | Pay-as-you-go | No per-seat fee, unlimited developers |

## Source Code Leak Incident (Mar 31, 2026)

### What Happened
セキュリティ研究者Chaofan Shouが、Claude Codeのnpmパッケージに含まれるsourcemapファイルを通じて、難読化されていないTypeScriptの全ソースコードへの参照を発見。AnthropicのCloudflare R2ストレージ上のzipアーカイブがダウンロード可能だった。

### Impact
- GitHubにソースコードのバックアップが**41,500回以上フォーク**
- npmパッケージのsourcemapファイルが原因
- Anthropicのビルドチェーンが未難読化のTypeScriptソースを参照

### Significance
この漏洩により、Claude Codeの内部設計が完全に公開。AIコーディングエージェントのアーキテクチャ理解に大きな影響を与えた。

## Core Workflow Patterns

### Parallel Agent Execution
Boris Chernyの最も影響力のある洞察:
> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

- 1つのエージェントがログを読みクエリを実行（分析用ワークツリー）
- 複数のエージェントが並行して機能を実装（機能用ワークツリー）
- 人間はコーディネーター兼承認者として機能

### Plan Mode → Auto-Accept
1. **Plan Modeで開始** (`Shift+Tab` 2回) — Claudeがアプローチを概説
2. **レビューと改善** — 計画が堅固になるまでClaudeと対話
3. **Auto-acceptに切り替え** — Claudeが計画を実行、通常は一発で成功
4. **検証** — Claudeがテストを実行またはブラウザ拡張機能で確認

### CLAUDE.md as Team Memory
- チームで共有するファイルをgitで管理
- 間違いのたびにCLAUDE.mdを更新
- PRで`@claude`を使用してガイドラインを更新

## Terminal Environment

### Recommended Setup
- **Ghostty**: チームが推奨（同期レンダリング、24-bitカラー、Unicodeサポート）
- **tmux**: ワークツリーごとにタブをカラーコード/命名
- シェルエイリアス（za, zb, zc）で瞬時のワークツリー切り替え
- ターミナルタブを1-5に番号付け、システム通知を有効化

### Mobile-to-Desktop Workflow (2026)
iOSからタスクを開始し、デスクトップにルーティングして実行、PRとして仕上げる「Phone to PR」ワークフローに対応。

## Claude Design Integration

Claude Design (April 2026) creates a direct handoff pipeline to Claude Code. When a design is complete, Claude Design packages everything into a handoff bundle that Claude Code can receive with a single instruction.

## Related

- [[boris-cherny]] — Creator
- [[anthropic]] — Original developer
- [[openai]] — Current owner (since Jul 2025)
- [[claude-mythos]] — Withheld high-security model
- [[concepts/project-glasswing]] — Safety initiative
- [[concepts/harness-engineering]]
- [[entities/cursor]] — Competitor
- [[entities/openai-codex]] — Competitor

## Sources

- [Claude Code What's New — Week 15 (Ultraplan, Monitor)](https://code.claude.com/en/whats-new/2026-w15) (Apr 2026)
- [Claude Code What's New — Week 14 (CLI Computer Use)](https://code.claude.com/en/whats-new/2026-w14) (Apr 2026)
- [Claude Code Changelog](https://code.claude.com/en/changelog)
- [Introducing Routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) (Apr 14, 2026)
- [Auto Mode Blog](https://claude.com/blog/auto-mode) (Mar 24, 2026)
- [GetAI Perks — Claude Code Updates 2026](https://www.getaiperks.com/en/articles/claude-code-updates) (Mar 26, 2026)
- [arXiv:2604.14228v1 — Dive into Claude Code Architecture](https://arxiv.org/html/2604.14228v1) (Apr 2026)
- [Claude Code Camp — How the team really works](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) (Feb 5, 2026)
- [The Register — Claude Code source code leak](https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/) (Mar 31, 2026)
