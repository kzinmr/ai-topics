---
title: "OpenClaw vs Hermes — Architecture Comparison"
aliases:
  - openclaw-hermes-architecture
  - hermes-openclaw-comparison
  - skill-explosion-problem
  - product-positioning-framework
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - hermes-agent
  - architecture
  - comparison
  - skill-management
related:
  - concepts/openclaw/_index
  - concepts/openclaw/five-tier-precedence
  - concepts/openclaw/philosophy
  - concepts/skill-architecture-patterns
  - comparisons/hermes-vs-openclaw-architecture
  - entities/peter-steinberger
  - entities/hermes-agent
sources:
  - "elvis analysis (April 2026) — 9-hour side-by-side source code study"
  - "OpenClaw VISION.md"
  - "Hermes Agent documentation"
---

# OpenClaw vs Hermes — Architecture Comparison

## 概要

elvis（@elvis_）が2026年4月に行った**9時間のHermes Agent vs OpenClawの並列ソースコード研究**に基づくアーキテクチャ比較分析。

> *"@steipete gave the world a new layer in the stack and put a claw in everyone's hand. That's foundational work."* — elvis

## 二つのアプローチ

| 次元 | OpenClaw (Steinberger) | Hermes Agent (Nous Research) |
|------|----------------------|------------------------------|
| **哲学** | Primitives First, Linux/K8sスタイル | Batteries-included, Railsスタイル |
| **スキル管理** | 明示的、ユーザー統治（Governed） | 自己作成（Self-authoring） |
| **デフォルト** | ベースラインのみ | 123+ バンドルSKILL.md |
| **成長モデル** | 制限付き（ClawHub経由） | 有機的（エージェントが自律作成） |
| **デバッグ** | `grep`一発で追跡可能 | 複数スキル横断調査が必要 |
| **ツール起動精度** | 高い（明示的ルーティング） | 低い（実行時推測） |
| **Day-One生産性** | 設定が必要 | 即座に生産的 |

## Five-Tier Skill Precedence vs Self-Authored Skills

### OpenClaw: 決定論的階層モデル
```
1. Workspace skills     （最優先）
2. User global skills
3. Managed skills
4. Bundled skills       （ベースラインのみ）
5. Extra skills         （最低優先度）
```

**利点:** 「何か壊れた時、grep一発で追える。どのスキルがトリガーされたか推測する必要がない。」

### Hermes: Self-Authored Skills
```
1. Prompt Nudge → スキル保存を検討
2. Background Review → タスク完了後にスキャン
3. Pre-Compression Flush → コンテキスト圧縮前に保存
4. Blunt Rule → 既存スキルがあれば修正、なければ新規作成
```

**利点:** エージェントが「こんなスキルがあったのか」と自律的に発見する

## Skill Explosion Problem

Hermesの有機的成長モデルが抱える根本的問題：

> *"Real example: the agent wanted to read an image from my desktop. Tried browser read and vision skill, nothing worked. So it wrote a third `read-local-image` skill lol."* — elvis

### 問題の構造
1. エージェントは「これをスキル化すべき」を特定するのは得意
2. 「これは既に別のフォルダにある」を特定するのは苦手
3. コーパスが統合速度よりも速く成長する
4. 結果：素晴らしいスキル、重複スキル、誰も存在を覚えていないスキル

### OpenClawの解決策
- バイト数キャップ
- 候補数キャップ
- シンボリックリンク拒否
- 検証済みファイルオープンのみ
- 資格チェック ≠ 発見（異なるエージェントが異なるサブセットを見る）

## Product Positioning Framework

elvisによる競争分析フレームワーク：

### カテゴリ定義者への対抗は失敗する
> *"OpenClaw had the audience. The mindshare, the GitHub stars, the 'it's basically the standard now' energy. Look at what happened to everyone who tried to fight that fight head-on — nanoclaw, nullclaw, picoclaw, zeroclaw. All trying to out-OpenClaw OpenClaw. None got Hermes's traction."*

### 新しいゲームを作る方が成功する
- **Hermesの勝ち手**: OpenClawのボードで戦わない
- Self-authoring vs governed
- Bundled-by-default vs primitives-only
- Tool Gateway as ecosystem lock-in
- 「We are not the minimalist primitives company」

### Rails vs Linux/Kubernetes アナロジー

| | Hermes = Rails | OpenClaw = Linux/K8s |
|---|---|---|
| 価値 | 意見のあるデフォルト | 最小限のプリミティブ |
| 哲学 | happy path が最初から用意されている | 必要なものを自分で組み立てる |
| トレードオフ | 初期生産性が高いが、カスタマイズが複雑 | 初期設定が必要だが、完全に制御可能 |

## AGENTS.md Optimization Pattern

elvisがOpenClawのTOOLS.md + VercelのAGENTS.mdを組み合わせ：

> *"Tool activation correctness is better on OpenClaw than Hermes for tasks where the agent has to pick the right CLI/API from ~50 options."*

**原則:** Explicit > Implicit

## 実践的意思決定フレームワーク

| ユーザープロファイル | 推奨 | 理由 |
|---------------------|------|------|
| とにかく早く始めたい | **Hermes** | 意見のあるデフォルト = Day Oneで生産的 |
| 100%のコントロールが必要 | **OpenClaw** | 可読性とスコープ制御が最重要 |
| カスタムエージェントを構築 | **両方** | OpenClawから統治を、Hermesから自己改善を学ぶ |

## 主要な洞察

> *"Both harnesses will do everything you want. Pick either, you'll be fine. But the more interesting question isn't which to pick — it's what you can learn from each."* — elvis

> *"You don't even need to use OpenClaw to benefit from OpenClaw — the patterns will show up in everything downstream for years."* — elvis

## 関連

- [[openclaw/_index]] — OpenClawコンセプト集約
- [[openclaw/five-tier-precedence]] — 5階層スキル優先度モデル
- [[openclaw/philosophy]] — Primitives First哲学
- [[skill-architecture-patterns]] — スキルアーキテクチャの比較分析
- [[comparisons/hermes-vs-openclaw-architecture]] — 詳細なアーキテクチャ比較
- [[peter-steinberger]] — OpenClaw創設者
- [[hermes-agent]] — Hermes Agent
