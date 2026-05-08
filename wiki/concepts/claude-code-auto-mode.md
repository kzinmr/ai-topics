---
title: "Claude Code Auto Mode"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - claude-code
  - agent-safety
  - sandbox
  - security
aliases:
  - auto mode
  - Claude Code auto mode
  - auto-approve mode
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-code-auto-mode.md
  - https://www.anthropic.com/engineering/claude-code-auto-mode
related:
  - claude-code
  - claude-code-best-practices
  - agent-sandboxing
  - agent-skills
---

# Claude Code Auto Mode

Claude Codeのauto modeは、手動承認と無ガードレールの中間に位置する新しい権限モード。モデルベースの分類器が人間の承認者を代替し、危険なアクションをブロックしつつ、安全な操作は許可プロンプトなしで実行する。

## 3つの権限モードの位置づけ

| モード | 自律性 | セキュリティ | メンテナンス負荷 |
|--------|--------|-------------|----------------|
| Manual Approval | 中 | 中 | 低（93%承認で疲労） |
| **Auto Mode** | **高** | **高** | **低** |
| Sandbox | 高 | 最高 | 高（設定が必要） |
| `--dangerously-skip-permissions` | 最高 | なし | なし |

## アーキテクチャ: 2層防御

### Layer 1: 入力層 — Prompt Injection Probe
- ツール出力（ファイル読み取り、Web fetch、シェル出力）がagent contextに入る**前**にスキャン
- 乗っ取り試行を検出 → contextに警告を注入
- サーバーサイドで実行

### Layer 2: 出力層 — Transcript Classifier
- Sonnet 4.6上で実行
- **2段階パイプライン**:
  - **Stage 1**: 高速シングルトークンフィルタ（yes=block / no=allow）。安全側にチューニング
  - **Stage 2**: Stage 1でフラグされた場合のみChain-of-Thought推論を実行
- 分類器が見るもの: ユーザーメッセージ + ツール呼び出し（Claudeのメッセージとツール出力は**意図的に削除**）
- 削除の理由: エージェントが分類器を説得するのを防ぐ（"reasoning-blind"設計）

### 権限決定のTier構造

| Tier | 内容 | 分類器呼び出し |
|------|------|-------------|
| Tier 1 | 安全ツール許可リスト（read, search, todo）+ ユーザー設定 | ❌ スキップ |
| Tier 2 | プロジェクト内ファイル操作 | ❌ スキップ |
| Tier 3 | シェルコマンド、Web fetch、外部ツール、サブエージェント、プロジェクト外操作 | ✅ 分類器へ |

## 脅威モデル（4種類）

1. **Overeager behavior（過剰積極性）**: ユーザーの意図を超えて自律的に行動（クレデンシャル探索、ブランチ削除など）
2. **Honest mistakes（正直なミス）**: ブラスト半径の誤認
3. **Prompt injection**: ファイル/Webページに埋め込まれた命令
4. **Misaligned model**: モデル自身の目標追求（実運用では未観測だが評価対象）

### 実例（内部インシデントログから）

- **スコープ拡大**: "clean up old branches" → リモートブランチの一括削除をブロック
- **クレデンシャル探索**: 認証エラー → 環境変数をgrepして別トークンを探すのをブロック
- **エージェント推論パラメータ**: "cancel my job" → 名前類似度での誤ターゲット削除をブロック
- **外部サービス経由の共有**: GitHub Gist作成によるデータ流出をブロック
- **安全チェック迂回**: deploy失敗 → skip-verificationフラグ付きリトライをブロック

## 分類器の判断基準

### 固定テンプレート
- **評価ルール**: 表面的なコマンド文字列ではなく、実世界への影響を評価。`&&`チェーン全体を1アクションとして判断。ペイロード書込み→実行のパターンも捕捉
- **ユーザー意図ルール**: ユーザーが明示的に許可したもの以外は未承認と判断

### カスタマイズ可能スロット
- **Environment**: 信頼境界（デフォルトは現在のgitリポジトリのみ）
- **Block rules**: 20以上のデフォルトルール（破壊/流出、セキュリティ低下、信頼境界越え、レビュー回避）
- **Allow exceptions**: マニフェスト記載パッケージのインストールなど

## 評価結果

| データセット | Stage 1 FPR/FNR | Stage 1→2 FPR/FNR |
|-------------|-----------------|-------------------|
| 実内部トラフィック (n=10,000) | 8.5% FPR | **0.4% FPR** |
| 実Overeager行動 (n=52) | 6.6% FNR | 17% FNR |
| 合成データ流出 (n=1,000) | 1.8% FNR | 5.7% FNR |

- FPR 0.4%: 通常操作の99.6%が許可プロンプトなしで実行可能
- FNR 17% on real overeager: 危険行動の83%を捕捉（`--dangerously-skip-permissions`比で大幅改善）

## Deny-and-Continue

分類器がブロックしても停止しない。拒否は「より安全な方法を見つけよ」というツール結果として返される。
- 連続3回拒否 or 合計20回拒否 → 人間にエスカレーション
- Headless mode (`claude -p`): プロセス終了

## Multi-Agent Handoffs

サブエージェントの委任時と結果返却時の両方で分類器が実行される:
- **Outbound**: タスク委任が本当にユーザー意図かチェック
- **Return**: サブエージェントが実行中にprompt injectionで侵害された可能性をチェック

## See Also

- [[entities/claude-code]] — Claude Code agent harness
- [[concepts/claude-code-best-practices]] — Best practices for Claude Code
- [[concepts/agent-sandboxing]] — Agent sandboxing patterns
- [[claude-code-sandboxing]] — Claude Code sandboxing implementation
- [[concepts/agent-skills]] — Equipping agents with skills
- [[concepts/code-execution-with-mcp]] — Code execution with MCP
