---
title: "Context Repositories (Git-based Agent Memory)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [context-management, context-engineering, memory-systems, coding-agents, git, filesystem, subagents]
sources:
  - "[[raw/articles/2026-02-12_letta_context-repositories]]"
related:
  - "[[concepts/agent-memory]]"
  - "[[concepts/letta-code]]"
  - "[[concepts/progressive-disclosure]]"
  - "[[concepts/context-engineering]]"
---

# Context Repositories (Git-based Agent Memory)

Context Repositories（コンテキストリポジトリ）は、Lettaが提唱する**Gitベースのエージェントメモリ管理**アーキテクチャ。エージェントのコンテキストをローカルファイルシステムに保存し、Gitでバージョン管理することで、プログラム可能なメモリ操作とマルチサブエージェントの並行作業を可能にする。

## 背景

従来のエージェントメモリ（MemGPT、メモリツール）の限界:
- エージェントがメモリ操作に**専用ツール**を使う必要がある → 表現力が制限される
- 複数サブエージェントの**同時メモリ書き込み**に非対応
- バージョン管理不在 → 巻き戻し不可

## アーキテクチャ

### 基本原則

```
メモリ = ローカルファイルシステム上のファイル
操作 = ターミナルコマンド + スクリプト（bash, Python）
バージョン管理 = Git
```

Unix哲学に従い、エージェントは標準ツール（`grep`, `find`, `cat`, `for` loops）でメモリを操作できる。

### プログレッシブ開示 (Progressive Disclosure)

```
context-repo/
├── system/           ← 常にシステムプロンプトに全読み込み
│   ├── identity.md
│   └── rules.md
├── memory/           ← ファイルツリー構造のみプロンプトに表示
│   ├── user-prefs.md  (frontmatter: description="ユーザー設定")
│   └── project-x.md   (frontmatter: description="Project Xの学び")
```

- ファイル階層とファイル名が**ナビゲーションシグナル**として機能
- 各ファイルのYAML frontmatterに**説明文**
- `system/` ディレクトリ内のファイルのみ全読み込み
- エージェント自身がファイルの移動・整理を管理

### マルチエージェントメモリスワーム

- 各サブエージェントに**独立したGitワークツリー**
- 並行してメモリ処理 → Gitマージで解決
- 分割統治: 複数サブエージェントが異なる側面から学習
- 例: `/init` ツールがClaude Code/Codexの履歴から学習

## 比較: Context Repositories vs 従来手法

| 側面 | Context Repositories | 従来メモリツール | 仮想ファイルシステム |
|------|---------------------|-----------------|-------------------|
| 操作手段 | ターミナル + スクリプト | 専用ツール呼び出し | FS操作ツール |
| 並行性 | Gitマージ | 非対応 | 非対応 |
| バージョン管理 | ✅ Gitコミット | ❌ | ❌ |
| プログレッシブ開示 | ファイル階層 + frontmatter | ツール依存 | ディレクトリ構造のみ |
| プログラム可能性 | 全スクリプト言語 | ツールの範囲内 | ファイル操作の範囲内 |

## 応用

- **トークン空間学習 (Token-Space Learning)**: 過去のエージェント軌跡を再処理して抽象化
- **継続的学習**: セッションを超えて知識を蓄積
- **チームメモリ**: 複数開発者のエージェントが知識を共有

## 参照

- [Introducing Context Repositories — Letta Blog](https://www.letta.com/blog/context-repositories) (2026-02-12)
- [Effective Context Engineering for AI Agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
