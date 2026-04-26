---
title: "OpenClaw Philosophy — Primitives Over Defaults"
type: concept
aliases:
  - openclaw-philosophy
  - primitives-over-defaults
  - openclaw-design-philosophy
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - philosophy
  - agent-design
  - primitives
related:
  - concepts/openclaw/_index
  - concepts/skill-architecture-patterns
  - entities/peter-steinberger
sources:
  - "elvis analysis (April 2026) — 9-hour side-by-side source code study"
  - "OpenClaw VISION.md"
  - "https://steipete.me/"
---

# OpenClaw Philosophy — Primitives Over Defaults

OpenClawの設計哲学の中核は**「Primitives over Defaults」**（デフォルトではなくプリミティブを提供する）。これはLinuxカーネルやKubernetesの設計思想に近い。

## 核心原則

### 1. Explicit > Implicit（明示的 > 暗黙的）
> "Tool activation correctness is better on OpenClaw than Hermes for tasks where the agent has to pick the right CLI/API from ~50 options." — elvis

エージェントが「どのスキルをロードすべきか」を実行時に推測させるのではなく、**優先度ルールをシステムプロンプトに明示的に記述する**。

**実装例:** Five-Tier Skill Precedence（5階層スキル優先度モデル）

### 2. Guarantees > Defaults（デフォルトではなく保証）
> "You're not getting defaults, you're getting guarantees. OpenClaw does exactly what you told it to do, nothing more, nothing less. Boring in the best way." — elvis

- デフォルトで何百ものスキルがバンドルされているわけではない
- 最小限のベースラインスキルのみ
- あとはユーザーが明示的に追加

### 3. Legibility > Autonomy（自律性より可読性）
> "When something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered." — elvis

Hermesのself-authoringスキルは「魔法のように」新しいスキルを生成するが、**何が起きているかの追跡が困難**。OpenClawは「魔法」を排除し、grepで追える決定論的動作を優先する。

### 4. Bounded Growth > Organic Growth（制限付き成長 > 有機的成長）

| | OpenClaw (Bounded) | Hermes (Organic) |
|---|---|---|
| スキル追加 | ClawHub経由、明示的承認 | エージェントが自律作成 |
| 上限 | Byte caps, candidate caps | 無し |
| セキュリティ | Symlink拒否、検証済みファイルのみ | プロンプト経由 |
| コーパス劣化 | 防げない（意図が必要） | 発生する（Skill Explosion Problem） |

## Rails vs Linux/Kubernetes アナロジー

elvisの分析による製品ポジショニングフレーム：

| | Hermes = Rails | OpenClaw = Linux/K8s |
|---|---|---|
| 価値 | 「意見のあるデフォルト」 | 「最小限のプリミティブ」 |
| 哲学 | happy path が最初から用意されている | 必要なものを自分で組み立てる |
| トレードオフ | 初期生産性が高いが、カスタマイズが複雑 | 初期設定が必要だが、完全に制御可能 |
| ターゲット | 「Day Oneから100+のことを知っているエージェント」 | 「指示されたことだけ、それ以上でも以下でもない」 |

## Ship Beats Perfect

> "I don't read code anymore. I weave it." — Steinberger

Steinbergerの開発哲学：
- コードを一行一行読むのではなく、「織る」（weave）
- 完璧さより出荷速度
- 検証可能ならそれで良い（コンパイル→実行→テスト）
- 美的判断（spacing, naming）より機能的判断（does it work?）

## Closed Loop Principle

> "Code works well with AI because it's verifiable. You can compile it, run it, test it. That's the loop. You have to close the loop." — Steinberger

AIエージェントが効果的に動作するためには：
1. **検証可能な出力**を生成する構造にする
2. CLIテストランナーを準備する
3. 合成的ユーザーフローを定義する
4. エージェントが自己検証できるようにする

## Polyagentmorous Development

> "Powered by Vienna coffee culture" — steipete GitHub bio

Steinbergerは**5-10のAIエージェントを並列にオーケストレーション**する：
- Claude Code
- OpenAI Codex
- カスタムMCPサーバー
- 各エージェントはスペシャリスト（ファイル操作、Webスクレイピング、ターミナル自動化、スクリーンショット分析）
- 彼はコーダーではなく「指揮者」

## ローカルファーストとの関係

OpenClawの哲学は[[concepts/local-first-software]]運動と深く関連：
- ローカル推論（Ollama, LM Studio, llama.cpp）
- ローカルファイルシステムアクセス
- ローカルMCPサーバー
- プラットフォーム依存の最小化

## 関連

- [[concepts/openclaw]] — OpenClawコンセプト集約
- [[concepts/openclaw/five-tier-precedence]] — Five-Tier Skill Precedence
- [[concepts/skill-architecture-patterns]] — Hermesとの比較
- [[concepts/local-first-software]] — ローカルファーストソフトウェア
- [[peter-steinberger]] — 設計者
- [[comparisons/hermes-vs-openclaw-architecture]] — 詳細アーキテクチャ比較
