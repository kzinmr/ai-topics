---
title: "OpenClaw — Concepts Index"
aliases:
  - openclaw-concepts
  - openclaw-index
  - open-claw-concepts
created: 2026-04-18
updated: 2026-04-19
tags:
  - concept
  - index
  - openclaw
  - ai-agents
  - personal-agents
  - peter-steinberger
status: active
---

# OpenClaw — コンセプト集約

**OpenClaw** は Peter Steinberger（@steipete）が開発したオープンソースの常駐型パーソナルAIエージェントフレームワーク。135,000以上の実行インスタンスを記録し、Anthropicによるサブスクリプション制限の中心となった。NVIDIA NemoClawのアップストリームプロジェクト。

## コア哲学（[[concepts/openclaw/philosophy]]）

| 原則 | 説明 |
|------|------|
| **Primitives First** | デフォルトではなく保証を提供 |
| **Always-On Agent** | セッションバウンドではなく常駐・自律動作 |
| **Explicit > Implicit** | ルーティングルールはシステムプロンプトに明記 |
| **Ship Beats Perfect** | コードは読まない。「織る」（weave） |
| **Closed Loop Principle** | コンパイル→実行→テストの自己検証構造 |
| **Local-First** | ローカル推論、ローカルファイル、ローカルMCP |

## 設計パターン

### Five-Tier Skill Precedence（[[concepts/openclaw/five-tier-precedence]]）
```
1. Workspace skills     （最優先）
2. User global skills
3. Managed skills
4. Bundled skills       （ベースラインのみ）
5. Extra skills         （最低優先度）
```
> 「何か壊れた時、grep一発で追える。どのスキルがトリガーされたか推測する必要がない。」

### Anti-Bloat Policy
- バンドルスキルはベースラインのみ
- 新規スキルはまずClawHubへ
- コアへの追加は「製品またはセキュリティ上の強い理由」が必要
- バイトキャップ、候補キャップ、symlink拒否、検証済みファイルオープンのみ

### AGENTS.md Optimization Pattern
OpenClawのTOOLS.md + VercelのAGENTS.mdパターンを組み合わせ:
> 「約50のCLI/APIから正しいものを選ぶタスクにおいて、ツール起動の正確性はOpenClawの方がHermesより優れていた。」 — elvis

## アーキテクチャ比較（[[concepts/openclaw/architecture-comparison]]）

| 次元 | OpenClaw | Hermes Agent |
|------|----------|--------------|
| **哲学** | Primitives First, Linux/K8s | Batteries-included, Rails |
| **スキル管理** | 明示的、ユーザー統治 | 自己作成（Self-authoring） |
| **デフォルト** | ベースラインのみ | 123+ バンドルSKILL.md |
| **デバッグ** | `grep`一発 | 複数スキル横断調査 |
| **成長モデル** | 制限付き（ClawHub） | 有機的（Skill Explosion Problem） |

## Anthropic-OpenClaw Conflict（[[concepts/openclaw/anthropic-conflict]]）

2026年4月、Anthropicがサードパーティエージェントをサブスクリプションから排除。OpenClawインスタンスは$109.55/日（Opus）の消費に対し、一般開発者は$6/日。135,000インスタンス稼働中。

## エコシステムツール（[[concepts/openclaw/ecosystem-tools]]）

| ツール | 説明 | Stars |
|--------|------|-------|
| **VibeTunnel** (vt.sh) | 任意のブラウザをターミナル化 | — |
| **CodexBar** | OpenAI Codex/Claude Code使用統計 | 9.9k |
| **Peekaboo** | macOS CLI + MCPスクリーンショット | 3.1k |
| **mcporter** | MCPをTypeScriptでCLI化 | 3.8k |
| **gogcli** | Google Suite CLI | 6.7k |
| **agent-rules** | Claude Code/Cursor用ルール | 5.7k |
| **tokentally** | LLMトークン/コスト計算 | — |
| **Terminator MCP** | ターミナル出力返却MCP | — |

## 関連エンティティ

| エンティティ | 説明 |
|-------------|------|
| [[entities/peter-steinberger]] | OpenClaw作者。元PSPDFKit CEO。OpenAIでパーソナルエージェント開発 |
| [[entities/openclaw]] | OpenClawフレームワーク詳細 |
| [[entities/nvidia-nemoclaw]] | NVIDIAのエンタープライズ版OpenClawラッパー |

## 製品ポジショニングフレーム

> *"OpenClaw had the audience. The mindshare, the GitHub stars... nanoclaw, nullclaw, picoclaw, zeroclaw. All trying to out-OpenClaw OpenClaw. None got Hermes's traction."* — elvis

Hermesの勝ち手: **カテゴリ定義者のボードで戦わず、新しいゲームを作る**

## 意思決定フレームワーク

| ユーザープロファイル | 推奨 | 理由 |
|---------------------|------|------|
| とにかく早く始めたい | **Hermes** | 意見のあるデフォルト = Day Oneで生産的 |
| 100%のコントロールが必要 | **OpenClaw** | 可読性とスコープ制御が最重要 |
| カスタムエージェントを構築 | **両方** | OpenClawから統治を、Hermesから自己改善を学ぶ |

## 主要引用

> *"With one command, anyone can run always-on, self-evolving agents anywhere."* — OpenClaw

> *"First they copy some popular features into their closed harness, then they lock out open source."* — Steinberger on Anthropic

> *"@steipete gave the world a new layer in the stack and put a claw in everyone's hand. That's foundational work."* — elvis

> *"You don't even need to use OpenClaw to benefit from OpenClaw — the patterns will show up in everything downstream for years."* — elvis

## See Also

- [[concepts/harness-engineering]] — Harness Engineering（横断概念）
- [[concepts/harness-engineering/agentic-workflows/_index]] — Agentic Engineering Patterns
- [[concepts/local-first-software]] — ローカルファーストソフトウェア運動
- [[concepts/personal-superintelligence]] — パーソナルスーパーインテリジェンス
- [[concepts/open-source-ai-destruction]] — オープンソースAI破壊の議論
- [[comparisons/hermes-vs-openclaw-architecture]] — 詳細アーキテクチャ比較
- [[concepts/skill-architecture-patterns]] — スキルアーキテクチャ比較分析
