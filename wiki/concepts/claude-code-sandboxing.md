---
title: "Claude Code Sandboxing"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - claude-code
  - sandboxing
  - agent-safety
  - security
  - prompt-injection
aliases:
  - Claude Code sandbox
  - Claude sandboxed bash
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-code-sandboxing.md
  - https://www.anthropic.com/engineering/claude-code-sandboxing
related:
  - claude-code
  - agent-sandboxing
  - claude-code-auto-mode
  - code-execution-with-mcp
---

# Claude Code Sandboxing

Claude Codeのサンドボックス機能。OSレベルの隔離（Linux bubblewrap / macOS seatbelt）を使ってファイルシステムとネットワークの両方を制限し、許可プロンプトを84%削減しながらセキュリティを向上させる。

## 中核設計

### 2つの隔離境界

| 境界 | 機能 | 防御内容 |
|------|------|---------|
| **Filesystem isolation** | 指定ディレクトリのみ読み書き許可 | 機密システムファイルの改ざん防止 |
| **Network isolation** | 承認済みサーバーのみ接続許可 | 情報漏洩・マルウェアダウンロード防止 |

**重要な原則**: 両方が揃って初めて有効。ネットワーク隔離だけではファイル流出を防げず、ファイルシステム隔離だけではサンドボックス脱出可能。

## 2つの提供形態

### 1. Sandboxed Bash Tool（ベータ、リサーチプレビュー）

- コンテナのオーバーヘッドなしでディレクトリ・ネットワークホストを制限
- Linux bubblewrap + macOS seatbelt のOSプリミティブを利用
- **オープンソース化**（[GitHub](https://github.com/anthropics/claude-code)）
- 任意のプロセス、エージェント、MCPサーバーをサンドボックス化可能
- カスタムプロキシでアウトバウンドトラフィックに任意のルール適用可能

**アーキテクチャ**:
```
[Claude Code] → [Sandboxed Bash]
                    ├── FS isolation: cwdのみrw、外部はブロック
                    └── Network isolation: Unix domain socket → Proxy → 承認済みドメインのみ
```

### 2. Claude Code on the Web

- **クラウド上の隔離サンドボックス**でClaude Codeセッションを実行
- 機密クレデンシャル（git認証情報、署名鍵）はサンドボックス内に**一切置かない**
- カスタムGit proxyが認証を透過的に処理:
  - サンドボックス内git client → スコープ付きクレデンシャルでproxy認証
  - Proxyがブランチ・リポジトリを検証 → 実際の認証トークンを付与 → GitHubへ

## セキュリティモデル

- サンドボックス内で起動された**すべての**スクリプト、プログラム、サブプロセスに制限が適用される
- Prompt injectionが成功しても完全に隔離され、SSH鍵の窃取や攻撃者サーバーへの通信は不可能
- サンドボックス範囲外へのアクセス試行 → 即時通知 + ユーザー判断

## 効果

- **許可プロンプト84%削減**（Anthropic社内利用実績）
- 手動承認の「承認疲れ」を解消
- 開発サイクルの高速化

## 権限モード比較

| 特徴 | Sandbox | Auto Mode | Manual |
|------|---------|-----------|--------|
| セキュリティ | 最高（OS隔離） | 高（分類器） | 中（人間判断） |
| 自律性 | 高 | 高 | 低 |
| メンテナンス | 高（要設定） | 低 | 低 |
| 外部アクセス | 制限あり | 分類器次第 | 手動承認 |

## See Also

- [[entities/claude-code]] — Claude Code agent harness
- [[claude-code-auto-mode]] — Auto mode permission classifier
- [[concepts/agent-sandboxing]] — General agent sandboxing patterns
- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[concepts/code-execution-with-mcp]] — MCPでのコード実行
