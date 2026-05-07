---
title: "Coding Agent Harnesses Comparison"
created: 2026-05-01
updated: 2026-05-07
type: comparison
tags: [comparison, coding-agents, harness, harness-engineering, ai-agents]
sources:
  - "https://thoughts.jock.pl/p/ai-coding-harness-agents-2026"
  - "https://grigio.org/opencode-vs-pi-which-ai-coding-agent-should-you-use/"
  - "https://github.com/disler/pi-vs-claude-code"
  - "https://developers.openai.com/codex/cli/features"
  - "https://medium.com/superagentic-ai/codex-cli-running-gpt-oss-and-local-coding-models-with-ollama-lm-studio-and-mlx-4b796e39404b"
  - "https://github.com/openai/codex"
  - "https://pi.dev"
  - "https://opencode.ai"
  - "https://github.com/badlogic/pi-mono"
---

# Coding Agent Harnesses Comparison

**Date:** May 7, 2026 (Kilo追加)
**Related:** [[concepts/agent-harness-comparison]] — 更新版9ハーネス比較ポータル, [[hermes-vs-openclaw-architecture]], [[concepts/harness-engineering]], [[concepts/coding-agents]], [[concepts/agent-harness-primitives]]

> **注意:** 本ページは推論サーバー（vLLM/llama.cpp等）ではなく、**コーディングエージェントハーネス**（Claude Code, OpenCode, Pi, Codex CLI, Cursor, OpenClaw, Hermes Agent）を比較する。Aiderは対象外。

---

## The "Harness Effect" — 最重要概念

ハーネス（エージェントフレームワーク）の品質は、モデルそのものと同等以上に重要である。

同一モデルでもハーネスによって性能が**5〜40ポイント**変動することが複数の独立研究で確認されている：

| 比較 | スコア | 差 | 要因 |
|------|:-----:|:--:|------|
| Claude Opus in **Claude Code** | 77% | → | |
| Claude Opus in **Cursor** | **93%** | **+16pt** | プロンプト設計・ツール実装の差 |
| Claude Opus in **最小スキャフォールド** | 42% | → | |
| Claude Opus in **Claude Code（フル）** | **78%** | **+36pt** | ハーネス品質の影響 |

> 出典: Matt Mayer独立テスト、CORE-Bench — ハーネス効果はタスクとモデルにより5〜40ポイント範囲

---

## 1. アーキテクチャ比較

| 次元 | Claude Code | OpenCode | Pi | Codex CLI | Cursor |
|------|------------|----------|-----|-----------|--------|
| **哲学** | フルオーケストレーター | "バッテリー同梱" OSS代替 | 最小プリミティブ | 軽量ユニバーサルエージェント | IDEエージェント |
| **開発元** | Anthropic → OpenAI | AnomalyCo/SST | Mario Zechner | **OpenAI** | Cursor Inc. |
| **言語** | TypeScript | TypeScript | TypeScript (Rust移植中) | **Rust** (96.2%) | TypeScript |
| **ライセンス** | ❌ Proprietary | ✅ MIT | ✅ MIT | **✅ Apache-2.0** | ❌ Proprietary |
| **GitHub Stars** | — | **140K+** | ~15K | **79.3K** | — |
| **ツール数** | 多数（サブエージェント含む） | 多数（Build/Planデュアル） | **4** (read/write/edit/bash) | 多数（内蔵+プラグイン） | IDE統合 |
| **システムプロンプト** | 数千トークン | ~10,000トークン超 | **<1,000トークン** | 効率的 | 高度に最適化 |
| **モデル選択** | **Anthropicのみ** | **75+プロバイダ** | **~20プロバイダ** | **OpenAI + カスタム + OSS** | Claude/GPT/カスタム |
| **MCP対応** | ✅ | ✅（標準搭載） | ✅（拡張で） | **✅（双方向）** | ✅ |
| **サブエージェント** | ✅ Agent Teams | ✅（Plan/Build切替） | ✅（拡張で） | **✅（config.toml設定）** | ✅（クラウド） |
| **LSP統合** | ❌ | ✅ | ❌ | ❌ | ✅ |
| **マルチモーダル** | ✅ | ✅ | ✅ | **✅（画像添付+生成）** | ✅ |
| **Web検索** | ✅ (Computer Use) | ✅ | ❌（拡張） | **✅（キャッシュ+Livemode）** | ❌ |
| **デスクトップ/TUI** | CLI + Desktop + Web | CLI + Desktop + TUI | CLI + TUI | **CLI + IDE拡張 + Desktop App** | IDE拡張 |
| **オープンソース** | ❌ | ✅ | ✅ | **✅** | ❌ |
| **プレイグラウンド** | ✅（Managed Agents） | ❌ | ❌ | **✅（Codex Web）** | ❌ |

---

## 2. Codex CLI 詳細ファクトシート（修正版）

Codex CLIに関する情報は初版に誤りがあったため、以下に正確な情報をまとめる：

### 基本情報
- **GitHub:** [github.com/openai/codex](https://github.com/openai/codex) — 79.3K stars, Apache-2.0
- **インストール:** `npm i -g @openai/codex` または `brew install --cask codex`
- **言語:** Rust (96.2%) + Python (2.8%) + TypeScript (0.3%)
- **サブスクリプション:** ChatGPT Plus/Pro/Team/Enterpriseに含まれる（APIキーも可）

### モデルサポート（対応プロバイダ）
- **OpenAIネイティブ:** gpt-5.5（推奨）, gpt-5.4, GPT-5.3-Codex-Spark（Pro専用）
- **OSSローカル:** `--oss` フラグでGPT-OSS-20B / GPT-OSS-120B（Ollama経由）
- **カスタムプロバイダ:** `config.toml` で `[model_providers]` を追加 → **DeepSeek, Qwen, Gemma等の任意モデルに対応**
- **ローカルエンジン:** Ollama / LM Studio / MLX対応
- **ミッドセッション切替:** `/model` コマンド対応

### 主要機能
- **SWE-bench Pro:** GPT-5.3 Codex = 56.8%, GPT-5.5 = 58.6%
- **MCP:** 双方向対応（MCPサーバー接続 + 自らがMCPサーバーとして動作）
- **サブエージェント:** `[agents]` セクションで設定可能
- **リモートTUI:** `codex app-server` + `codex --remote` でリモート実行
- **コードレビュー:** `/review` コマンド（ベースブランチ/未コミット/特定SHA）
- **画像生成:** `$imagegen` または自然言語でgpt-image-2を呼出
- **セッション永続化:** ローカルに保存、`codex resume` で復元
- **パーミッションモード:** Auto / Read-only / Full Access の3段階

### 誤っていた点（初版からの訂正）
| 項目 | 初版（誤） | 訂正（正） |
|------|----------|----------|
| モデルサポート | GPT-5.4のみ | ✅ gpt-5.5/gpt-5.4/Codex-Spark + カスタム + OSS |
| ライセンス | ❌クローズド | ✅ **Apache-2.0 オープンソース** |
| 言語 | TypeScript | ✅ **Rust** (96.2%) |
| MCP | ❌非対応 | ✅ **双方向対応** |
| サブエージェント | ❌非対応 | ✅ **config.tomlで設定可能** |
| 価格 | API課金のみ | ✅ **ChatGPT Plus/Pro/Team/Enterpriseに含まれる** |

---

## 3. モデル×ハーネス 相性マトリックス

### 🥇 各ハーネスのベストモデル

| ハーネス | 🥇 Best Match | 次点 | ローカル | 相性評価 |
|---------|:------------:|:----:|:-------:|---------|
| **Claude Code** | **Claude Opus 4.7** | Sonnet 4.6 | ❌ | 唯一の公式選択肢。サブスク$20/月で全機能 |
| **OpenCode** | **Claude Opus**（最高性能） | GPT-5, Gemini, Grok, Qwen, DeepSeek, GLM | ✅ Ollama/LM Studio | 75+プロバイダ対応だが、Claude Max課金は**二重取り**問題あり |
| **Pi** | **GPT-5系** or **Qwen 3.5 Coder 32B** | Claude, Gemma 4, DeepSeek, GLM | ✅ MLX/GGUF最適 | 最小プロンプトで**ローカル最速**、OpenClawの基盤 |
| **Codex CLI** | **GPT-5.5 / GPT-5.3 Codex**（ネイティブ） | カスタム (DeepSeek/Qwen) + OSS (GPT-OSS) | ✅ Ollama/LM Studio/MLX | ChatGPTサブスクに含まれる+OSS+カスタム対応 |
| **Cursor** | **Claude Opus**（**93%** 最高スコア） | GPT-5, カスタム | ❌ | 人間がキーボード前にいる前提、プロンプト職人の結晶 |

### モデル視点でのハーネス相性

| モデル | 最適ハーネス | 理由 |
|-------|------------|------|
| **Claude Opus 4.7** | Cursor (93%) → Claude Code (77%) → Pi/OpenCode (サブスク二重取り注意) | ハーネス効果が最大。Cursorのプロンプト最適化がOpus性能を最大限引き出す |
| **GPT-5.5** | **Codex CLI**（ネイティブ最適化） → Pi / OpenCode | Codex CLIはGPT-5.5が推奨モデル、ChatGPTサブスク込み |
| **GPT-5.3 Codex** | **Codex CLI**（専用設計） | Codex CLIに最適化されたコーディング特化モデル。SWE-bench Pro 56.8% |
| **GPT-OSS-20B/120B** | **Codex CLI**（`--oss`フラグ） | OpenAI謹製OSSモデルをCodex CLIから直接ローカル実行 |
| **Gemma 4 26B A4B** | **Pi**（<1Kプロンプト + LM Studio） | ローカルMoEモデル。Piの軽量さがVRAM制約下で効果を発揮 |
| **DeepSeek V3/V4** | **Codex CLI**（カスタムProvider）→ Pi / OpenCode | コスパ最強。Codex CLIのconfig.tomlで簡単設定可 |
| **Qwen 3.5 Coder 32B** | **Pi**（MLX最適）or **Codex CLI**（LM Studio経由） | ローカルコーディング特化。両ハーネスで動作可能 |
| **Gemini 2.5系** | **OpenCode** or **Pi** | Google系APIとの相性良好 |
| **GLM-5.1**（OSS） | **OpenCode** or **Codex CLI**（カスタムProvider） | SWE-bench Pro 58.4%の強力OSSモデル、OpenCodeが無難 |
| **中小ローカルモデル**（7B〜14B） | **Pi**（超軽量プロンプト） | OpenCodeの10Kプロンプトではローカルモデルの推論能力を使い切る前にオーバーヘッド |

---

## 4. アンソロポリックの「壁」とOpenAIの優位性

### Anthropic — サードパーティハーネスでのClaude二重課金

Anthropicは**PiやOpenCode等のサードパーティハーネスがClaude Maxサブスクリプションクレジットを使うことを許可していない**。Pi/OpenCodeでClaude Opusを使う場合、サブスク＋API従量課金の二重払いになる。

> **「Anthropicがこのポリシーを変えれば、PiはClaudeユーザーにとって第一の選択肢になる。」** — thoughts.jock.pl

### OpenAI — ChatGPTサブスクでCodex CLIがカバーされる

OpenAIは**ChatGPT Plus/Pro/Team/EnterpriseサブスクリプションでCodex CLIの全機能が利用可能**。課金は一本化されており、Pi/OpenCodeのような二重取り問題は発生しない。

これが**Codex CLIの最大の競争優位性**：サブスク料金だけでGPT-5.5クラスのエージェントコーディングを使える。

---

## 5. 決定フレームワーク

### 「放置して寝てる間に動かしたい」
→ **Claude Code**（唯一の「夜通し動かせる」ハーネス）
- モデル: Claude Opus 4.7 一択
- Auto Mode + Agent Teams で複数ファイル/複数タスクを並列
- SWE-bench Verified 72.7%

### 「ChatGPTサブスクに入ってるからそのまま使いたい」
→ **Codex CLI**（ChatGPT Plus/Proに含まれる）
- モデル: GPT-5.5（推奨）/ GPT-5.3 Codex
- 追加費用ゼロ、Rust製で軽量
- MCP・サブエージェント・リモートTUI・画像生成・Web検索まで網羅
- `--oss` でローカルモデルにも対応、カスタムプロバイダ設定も可

### 「全部入りのプラットフォームが欲しい」
→ **Kilo**（OpenCode fork、500+モデル、CLI/IDE/KiloClaw）
- OpenCodeをベースにVS Code + JetBrains拡張 + Kilo CLI + ホステッドOpenClaw
- 500+モデルをKilo Gateway経由でゼロマークアップ
- インライン補完、Cloud Agents、Teams/SSO、コードレビュー
- Apache-2.0、無料枠あり

### 「いろんなモデルを試したい / 乗り換えたい」
→ **OpenCode**（75+プロバイダ、140K GitHub Stars）
- Claude → GPT → Gemini → Qwen → DeepSeek を同一ワークフローで切替
- LSP統合、Plan/Buildデュアルエージェント
- Oh-my-opencodeでSisyphus/Prometheus拡張

### 「ローカルモデルで最速」
→ **Pi**（<1Kシステムプロンプト、MLX/GGUF最適）
- 同モデルでも2-3倍高速（OpenCode比）
- Qwen 3.5 Coder 32B / Gemma 4 26B / DeepSeek との相性抜群
- OpenClawでTelegram常時稼働ボットにもできる
- RPCモードでサブプロセス埋め込み可能

### 「OSSモデルをOpenAIのCLIで使いたい」
→ **Codex CLI + `--oss`**（GPT-OSS ローカル実行）
- `codex --oss` だけでOllama経由GPT-OSSモデル起動
- LM Studio / MLX 設定もconfig.tomlで簡単
- カスタムProviderでDeepSeek/Qwen等の設定も可

### 「IDEの中で最高品質」
→ **Cursor + Claude Opus**（スコア93%=業界最高）
- ただし人間操作前提。無人実行には不向き

### 「24時間動く自律エージェントが欲しい」
- **Telegram + 常時稼働** → **OpenClaw**（Piベース）
- **マルチプラットフォーム + Self-improving** → **Hermes Agent**

---

## 6. 主観的まとめ

1. **モデルよりハーネスが重要** — 同じOpusで77% vs 93%（+16pt）
2. **Codex CLIは最も過小評価されている** — オープンソース（Apache-2.0）、ChatGPTサブスク込み、GPT-5.5ネイティブ、MCP対応、カスタムProvider対応、OSSローカル実行。事実上「万能ハーネス」
3. **Piはローカルの王者** — 最も軽量なシステムプロンプトはローカルモデルで最大の効果
4. **OpenCodeは実験の王者** — 75+プロバイダでモデル比較/乗り換えを容易にする。コミュニティ最大
5. **Claude Codeは無人実行の王者** — Auto Mode + Agent Teamsで唯一の「夜通し動作」可能
6. **Anthropicの壁** — これが崩れればPiがClaudeユーザーの第一選択肢に

---

## Related

- [[comparisons/hermes-vs-openclaw-architecture]]
- [[comparisons/ai-agent-platforms]]
- [[concepts/harness-engineering]]
- [[concepts/agent-harness-primitives]]
- [[concepts/coding-agents]]
- [[entities/claude-code]]
- [[entities/pi]]
- [[entities/opencode]]
- [[entities/kilo]]
- [[entities/hermes-agent]]
- [[entities/openclaw]]

## Sources

- thoughts.jock.pl — "Claude Code vs Codex vs Aider vs OpenCode vs Pi 2026"
- grigio.org — "OpenCode vs Pi: Which AI Coding Agent Should You Use?"
- disler/pi-vs-claude-code (GitHub) — Pi vs OpenCode architecture comparison
- OpenAI Codex CLI Docs — https://developers.openai.com/codex/cli/features
- Medium/Superagentic AI — "Codex CLI: Running GPT-OSS and Local Coding Models"
- GitHub openai/codex — Apache-2.0, 79.3K stars, Rust (96.2%)
- pi.dev — Pi Coding Agent official
- opencode.ai — OpenCode official
- SWE-bench Pro Leaderboard — benchlm.ai (Apr 29, 2026)
