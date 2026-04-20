---
title: "Claude Code Best Practices"
aliases:
  - claude-code-best-practices
  - claude-code-patterns
  - agentic-coding-patterns
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - claude-code
status: draft
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
---

# Claude Code Best Practices

Anthropic公式のClaude Code（エージェント型コーディングツール）使用ベストプラクティス。

## 核心哲学

> "Agentic Environment: Claude Code reads files, runs commands, makes changes, and works autonomously. Shift from 'write & review' to 'describe & verify'."

> "Context window fills fast, and performance degrades as it fills. Every message, file read, and command output consumes tokens. Managing context is the #1 priority."

**エージェント環境では「書いてレビュー」から「記述して検証」へのシフトが必要。コンテキスト管理が最優先事項。**

## 検証とワークフロー

### Claudeに作業を検証させる方法（最高レバレッジ）

> "Give Claude a way to verify its work. Without clear success criteria, you become the only feedback loop."

| 戦略 | 前 | 後 |
|---|---|---|
| **検証基準の提供** | `「メールアドレスを検証する関数を実装して」` | `「validateEmail関数を書いて。テストケース: user@example.comはtrue、invalidはfalse、user@.comはfalse。実装後にテストを実行して」` |
| **UI変更の視覚的検証** | `「ダッシュボードを良くして」` | `「[スクリーンショットを貼付] このデザインを実装して。結果のスクリーンショットを撮ってオリジナルと比較して。違いをリストアップして修正して」` |
| **根本原因の対処** | `「ビルドが失敗してる」` | `「ビルドがこのエラーで失敗: [エラーを貼付]。修正してビルドが成功することを検証して。根本原因に対処して、エラーを抑制しないで」` |

- **検証に投資**: テストスイート、リンター、Bashコマンド。`「検証を堅牢にするのに投資しよう」`
- **Claude Chrome拡張** をUI反復に使用

### Explore → Plan → Implement → Commit

調査と実行を分離し、間違った問題を解決するのを避ける。

1. **Explore**: `read /src/auth and understand how we handle sessions and login...`
2. **Plan**: `I want to add Google OAuth. What files need to change? Create a plan.` → `Ctrl+G` でエディタで計画を編集
3. **Implement**: `implement the OAuth flow from your plan. write tests... run the test suite and fix any failures.`
4. **Commit**: `commit with a descriptive message and open a PR`

複雑/不確実なタスクには**Plan Mode**を使用。簡単な修正はスキップ。

## プロンプティングとコミュニケーション

### 具体的なコンテキストの提供
- **スコープタスク**: ファイル、シナリオ、テスト設定を指定
- **ソースへのポインタ**: `「ExecutionFactoryのgit履歴を見て、APIがどう進化したか要約して」`
- **パターンの参照**: `「既存のウィジェットの実装を見て... HotDogWidget.phpが良い例。パターンに従って...」`
- **症状の説明**: `「ユーザーがセッションタイムアウト後にログインに失敗すると報告。src/auth/の認証フローをチェックして...問題を再現する失敗するテストを書いて、修正して」`

### Claudeにインタビューさせる
大規模機能の場合:
```text
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.
Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs.
Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```
**クリーンなコンテキストで新しいセッションを開始**して仕様を実装。

## CLAUDE.md（永続コンテキスト）

- `/init` でスターターファイルを生成。**短く人間可読に**保つ
- **✅ 含める**: Claudeが推測できないBashコマンド、非標準コードスタイル、テスト設定、リポジトリエチケット、アーキテクチャ決定、環境の癖、一般的な落とし穴
- **❌ 除外**: Claudeが推測可能なもの、標準規約、詳細なAPIドキュメント、頻繁に変わる情報、長いチュートリアル、ファイルごとの説明、自明なルール
- **インポート構文**: `See @README.md... Git workflow: @docs/git-instructions.md`
- **場所**: `~/.claude/CLAUDE.md`（グローバル）、`./CLAUDE.md`（プロジェクト）、`./CLAUDE.local.md`（個人、`.gitignore`）、親/子ディレクトリ（自動ロード）

> "If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long." Prune ruthlessly.

## コンテキスト管理

> "Managing context is the #1 priority."

**コンテキストは有限リソース**。コンテキストを浪費するものはパフォーマンスを劣化させる。

- **ファイル読み込みを制限**: Claudeが必要とする正確なファイルのみを読み込む。推測可能なものは読み込ませない
- **出力を最小化**: 長いコマンド出力はファイルにリダイレクト。必要な部分のみを表示
- **段階的アプローチ**: 大きなタスクを小さなステップに分解。各ステップで検証
- **外部メモリ**: Claude Codeのメモリファイル（`memory.md`等）を活用

## LSP Hooks for Code Navigation

Community-developed hooks (April 2026) force Claude Code to use LSP (Language Server Protocol) instead of grep for code navigation, saving ~80% tokens:

```bash
# Example hook configuration
# Forces semantic-aware navigation instead of text search
```

- **Token savings**: ~80% reduction in navigation-related token usage
- **Accuracy improvement**: LSP understands symbol definitions, references, and types — grep only does text matching
- **Setup**: Configure hooks in Claude Code to intercept file search commands and route through LSP
- **Source**: Reddit r/LocalLLaMA community (April 14, 2026)

## 関連概念

- [[_index]] — 上位インデックス
- [[context-engineering]] — コンテキストエンジニアリング
- [[building-effective-agents]] — エージェント構築の基本原理
- [[using-git-with-agents]] — エージェントとのGit使用
