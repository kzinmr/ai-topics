---
title: "Coding Agent Harnesses Comparison"
created: 2026-05-01
updated: 2026-05-01
type: comparison
tags: [comparison, coding-agents, harness, harne-engineering, ai-agents]
sources:
  - "https://thoughts.jock.pl/p/ai-coding-harness-agents-2026"
  - "https://grigio.org/opencode-vs-pi-which-ai-coding-agent-should-you-use/"
  - "https://pub.towardsai.net/i-tested-ollama-vs-vllm-vs-llama-cpp-the-easiest-one-collapses-at-5-concurrent-users-d4f8e0e84886"
  - "https://www.sitepoint.com/ollama-vs-vllm-performance-benchmark-2026"
  - "https://macgpu.com/en/blog/2026-mac-inference-framework-vllm-mlx-ollama-llamacpp-benchmark.html"
  - "https://github.com/disler/pi-vs-claude-code"
---

# Coding Agent Harnesses Comparison

**Date:** May 1, 2026
**Related:** [[hermes-vs-openclaw-architecture]], [[concepts/harness-engineering]], [[concepts/coding-agents]], [[concepts/agent-harness-primitives]]

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

| 次元 | Claude Code | OpenCode | Pi | Aider | Codex CLI | Cursor |
|------|------------|----------|-----|-------|-----------|--------|
| **哲学** | フルオーケストレーター | "バッテリー同梱" OSS代替 | 最小プリミティブ | Gitファースト | クラウドコンテナ | IDEエージェント |
| **言語** | TypeScript | TypeScript | TypeScript (Rust移植中) | Python | TypeScript | TypeScript |
| **ツール数** | 多数（サブエージェント含む） | 多数（Build/Planデュアル） | **4** (read/write/edit/bash) | Git + ファイル操作 | クラウド操作 | IDE統合 |
| **システムプロンプト** | 数千トークン | ~10,000トークン超 | **<1,000トークン** | 効率的 | 効率的 | 高度に最適化 |
| **プロバイダ** | Anthropicのみ | **75+** | ~20（主要） | 任意(BYOM) | GPT-5.4のみ | Claude/GPT/カスタム |
| **サブエージェント** | ✅ Agent Teams | ✅（Plan/Build切替） | ✅（拡張で） | ❌ | ❌ | ✅（クラウド） |
| **MCP対応** | ✅ | ✅（標準搭載） | ✅（拡張で） | ❌ | ❌ | ✅ |
| **プラン/承認モード** | Ultraplan / Auto | ビルトイン | ❌（拡張で追加） | 確認モード | /goal コマンド | Design Mode |
| **git連携** | 標準 | 標準 | 標準 | ✅ 全編集を自動コミット | クラウド管理 | 標準 |
| **LSP統合** | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ |
| **デスクトップ/TUI** | CLI + Desktop + Web | CLI + Desktop + TUI | CLI + TUI | CLI | CLI | IDE拡張 |
| **オープンソース** | ❌（OpenAI管理） | ✅ MIT | ✅ MIT | ✅ Apache-2.0 | ❌ | ❌ |

---

## 2. モデル×ハーネス 相性マトリックス

### 🥇 各ハーネスのベストモデル

| ハーネス | 🥇 Best Match | 次点 | ローカル | 相性評価 |
|---------|:------------:|:----:|:-------:|---------|
| **Claude Code** | **Claude Opus 4.7** | Sonnet 4.6 | ❌ | 唯一の公式選択肢。サブスク$20/月で全機能 |
| **OpenCode** | **Claude Opus**（最高性能） | GPT-5, Gemini, Grok, Qwen, DeepSeek, GLM | ✅ Ollama/LM Studio | 75+プロバイダ対応だが、Claude Max課金は**二重取り**問題あり |
| **Pi** | **GPT-5系** or **Qwen 3.5 Coder 32B** | Claude, Gemma 4, DeepSeek, GLM | ✅ MLX/GGUF最適 | システムプロンプト最小で**ローカル最速**。OpenClawの基盤 |
| **Aider** | **DeepSeek** or **Sonnet**（費用対効果） | 任意モデル | ✅ | トークン消費Claude Code比 **1/4.2**、最強の費用対効果 |
| **Codex CLI** | **GPT-5.4**（専用） | ❌ 他不可 | ❌ | アプリ雛形生成とUIロジックが得意。$20/月 |
| **Cursor** | **Claude Opus**（**93%** 最高スコア） | GPT-5, カスタム | ❌ | 人間がキーボード前にいる前提、プロンプト職人の結晶 |

### モデル視点でのハーネス相性

| モデル | 最適ハーネス | 理由 |
|-------|------------|------|
| **Claude Opus 4.7** | Cursor (93%) → Claude Code (77%) | ハーネス効果が最大。Cursorのプロンプト最適化がOpusの性能を最大限引き出す |
| **GPT-5.4** | Codex CLI (ネイティブ) → Pi / OpenCode | CodexはGPT-5.4専用設計。Piでも安定動作 |
| **Gemma 4 26B A4B** | **Pi**（<1Kプロンプト + LM Studio） | ローカルMoEモデル。Piの軽量さがVRAM制約下で効果を発揮 |
| **DeepSeek V3/V4** | **Aider** or **Pi** | コスパ最強。Aiderのトークン効率とDeepSeekの安さの組み合わせが最高 |
| **Qwen 3.5 Coder 32B** | **Pi**（MLX最適） | ローカルコーディング特化。PiのGGUF/MLX対応で高速動作 |
| **Gemini 2.5系** | **OpenCode** or **Pi** | Google系APIとの相性良好 |
| **中小ローカルモデル**（7B〜14B） | **Pi**（超軽量プロンプト） | OpenCodeの10Kプロンプトではローカルモデルの推論能力を使い切る前にオーバーヘッド |

---

## 3. 実測ベンチマーク

### Claude Code vs OpenCode vs Pi — 実タスク比較

| ベンチマーク | Claude Code | OpenCode | Pi | 備考 |
|:----------:|:-----------:|:--------:|:--:|------|
| **SWE-bench Verified** | **72.7%** | ~65-70%（モデル依存） | ~65-70%（モデル依存） | Claude Codeが最高。Pi+Opusも同等程度 |
| **Terminal-Bench 2.0** | **92.1%** | — | — | マルチステップシェル操作 |
| **Token効率** | 3-4x Codex | 中程度 | **最小** | PiはClaude Code比で状況により2-3倍効率的 |
| **コーディングタスク（Opus同モデル）** | 77% | — | — | **Cursorで同じOpus→93%**（ハーネス効果） |
| **Localモデル速度（Qwen 14B）** | ❌ 不可 | ~10 t/s | **~25 t/s** | Piの軽量プロンプトが2-3倍高速 |

### トークン消費の比較（実測）

> 出典: 複数ユーザーレポート（2026年4月）

| ハーネス | 1タスクあたりの推定トークン | 月間推定コスト（ヘビーユーザー） |
|---------|:------------------------:|:-----------------------------:|
| **Aider + DeepSeek** | 最小（〜Claude Code比1/4） | **$5-15/月** |
| **Pi + GPT-5** | 低（〜1/2-1/3 of CC） | $20-40/月（API） |
| **OpenCode + Sonnet** | 中 | $30-80/月（API） |
| **Claude Code** | 高（3-4x Codex） | $20（サブスク）+ 追加API費用 |
| **Codex CLI** | 低（GPT-5.4最適化） | $20/月（ChatGPT Plus/Pro） |

---

## 4. アンソロポリック/OpenAIのハーネス制限

### Anthropicの「壁」— サードパーティハーネスでのClaude

Anthropicは**PiやOpenCode等のサードパーティハーネスがClaude Maxサブスクリプションクレジットを使うことを許可していない**。Pi/OpenCodeでClaude Opusを使う場合：
- Anthropic APIを通じて課金（サブスクとは別）
- サブスク＋API従量課金の**二重払い**になる
- 月$20（サブスク）＋API費用

> **「Anthropicがこのポリシーを変えれば、PiはClaudeユーザーにとって第一の選択肢になる。」** — thoughts.jock.pl

### OpenAI Codexのクローズドな制約

Codex CLIは**GPT-5.4のみ**で動作。他モデルへの切り替え不可。ただしChatGPT Plus/Proサブスク内で動作するため追加費用なし。

---

## 5. 機能マトリックス

| 機能 | Claude Code | OpenCode | Pi | Aider | Codex CLI | Cursor |
|------|:---------:|:--------:|:--:|:-----:|:---------:|:------:|
| **マルチファイル編集** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **自動テスト実行** | ✅ | ✅ | ✅（拡張） | ✅（自動） | ✅ | ✅ |
| **Web検索** | ✅ (Computer Use) | ✅ | ❌（拡張） | ❌ | ❌ | ❌ |
| **マルチモーダル** | ✅（画像理解） | ✅ | ✅ | ❌ | ❌ | ✅ |
| **自動コンパクション** | ✅ | ✅ | ✅（拡張可能） | ❌ | ✅ | ✅ |
| **Checkpointing** | ✅ | ✅ | — | ✅（git） | ✅ | ✅ |
| **スキル/ルーティン** | ✅ Routines | ✅（Oh-my-opencode） | ✅ Skills | — | — | — |
| **スワップモデルミッドセッション** | ❌（キャッシュ維持不可） | ✅ | ✅ (`/model`+Ctrl+L) | ✅ | ❌ | ❌ |
| **ヘッドレス/無人実行** | ✅（Auto Mode） | ✅ | ✅（RPC Mode） | ✅ | ✅ | ❌ |
| **RPC/SDK埋め込み** | ❌ | ❌ | ✅（RPC/SDK/MCP） | ❌ | ❌ | ❌ |
| **sandbox実行** | ❌（任） | ❌ | ✅（cco拡張） | ❌ | ✅（Cloud Container） | ✅（Cloud VM） |

---

## 6. 決定フレームワーク

### 「放置して寝てる間に動かしたい」
→ **Claude Code**（唯一の「夜通し動かせる」ハーネス）
- モデル: Claude Opus 4.7 一択
- Auto Mode + Agent Teams で複数ファイル/複数タスクを並列

### 「コスパ最優先、リファクタリング大量」
→ **Aider + DeepSeek or Sonnet**
- トークン消費 Claude Code比 **1/4**
- 全編集をgit自動コミット、完璧な監査証跡
- DeepSeekはAPI費用が圧倒的に安い

### 「いろんなモデルを試したい / 乗り換えたい」
→ **OpenCode**（75+プロバイダ）
- Claude → GPT → Gemini → Qwen → DeepSeek を同一ワークフローで切替
- LSP統合、Plan/Buildデュアルエージェント
- Oh-my-opencodeでSisyphus（オーケストレーション）/ Prometheus（プランニング）拡張

### 「ローカルモデルで最速」
→ **Pi**（<1Kシステムプロンプト、MLX/GGUF最適）
- 同モデルでも2-3倍高速（OpenCode比）
- Qwen 3.5 Coder 32B / Gemma 4 26B / DeepSeek との相性抜群
- OpenClawでTelegram常時稼働ボットにもできる
- RPCモードでサブプロセス埋め込み可能

### 「IDEの中で最高品質」
→ **Cursor + Claude Opus**（スコア93%=業界最高）
- ただし人間操作前提。無人実行には不向き

### 「クラウドネイティブ/CI/CD統合」
→ **Codex CLI**
- GPT-5.4専用でコスト一貫
- /goal で高レベル指示→勝手に実装
- Cloud Containerで切断しても継続実行

---

## 7. まとめ：ハーネス選びの黄金則

1. **モデルよりハーネスが重要** — 同じOpusで77% vs 93%（+16pt）。ハーネスの品質/プロンプト設計が結果を分ける
2. **Piはローカルの王者** — 最も軽量なシステムプロンプトはローカルモデルで最大の効果を発揮
3. **OpenCodeは実験の王者** — 75+プロバイダでモデル比較/乗り換えを容易にする
4. **Claude Codeは無人実行の王者** — Auto Mode + Agent Teamsで唯一の「夜通し動作」可能
5. **Anthropicの壁はいつか崩れる** — ポリシー変更があればPiがClaudeユーザーの第一選択肢になる可能性

---

## Related

- [[comparisons/hermes-vs-openclaw-architecture]] — Hermes vs OpenClawのアーキテクチャ比較
- [[comparisons/ai-agent-platforms]] — Claude Code vs Codexのプラットフォーム比較
- [[concepts/harness-engineering]] — ハーネスエンジニアリングの概念
- [[concepts/agent-harness-primitives]] — ハーネスプリミティブ
- [[entities/claude-code]] — Claude Code詳細
- [[entities/pi-coding-agent]] — Piコーディングエージェント詳細
- [[entities/opencode]] — OpenCode詳細
- [[entities/hermes-agent]] — Hermes Agent詳細
- [[entities/openclaw]] — OpenClaw詳細

## Sources

- thoughts.jock.pl — "Claude Code vs Codex vs Aider vs OpenCode vs Pi 2026"（ハーネス効果の実測データ）
- grigio.org — "OpenCode vs Pi: Which AI Coding Agent Should You Use?"（同モデル・異ハーネスの性能差）
- disler/pi-vs-claude-code (GitHub) — Pi vs OpenCodeのアーキテクチャ徹底比較
- Simon Shine — "Learning about AutoAgents by benchmarking Claude Code vs OpenCode"
- Terminal Trove — 43のコーディングエージェント比較テーブル
- reddit r/GithubCopilot — "Which terminal coding agent wins in 2026"（実ユーザーの議論）
