---
title: "Claude Code — Capabilities & Features"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-04-28
tags:
  - product
  - capabilities
  - features
sources:
  - https://code.claude.com/en/whats-new/2026-w15
  - https://code.claude.com/en/whats-new/2026-w14
  - https://code.claude.com/en/changelog
  - https://www.getaiperks.com/en/articles/claude-code-updates
  - https://claude.com/blog/auto-mode
---

# Claude Code: Capabilities & Features

Back to main profile: [[claude-code]]

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
