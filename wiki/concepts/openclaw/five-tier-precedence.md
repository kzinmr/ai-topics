---
title: "Five-Tier Skill Precedence"
aliases:
  - skill-precedence
  - openclaw-skill-governance
  - five-tier-precedence
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - skill-management
  - agent-architecture
  - governance
related:
  - concepts/skill-architecture-patterns
  - comparisons/hermes-vs-openclaw-architecture
  - entities/peter-steinberger
  - entities/openclaw
sources:
  - "OpenClaw VISION.md"
  - "elvis analysis (April 2026) — 9-hour side-by-side source code study"
---

# Five-Tier Skill Precedence Model

OpenClawのスキルロードシステムが採用する**階層的優先度モデル**。Hermes Agentのself-authoring（自己作成）アプローチとの対比において、最も重要なアーキテクチャ上の差異の一つ。

## 5階層構造

```
1. Workspace skills     （最優先 — プロジェクト固有のスキル）
2. User global skills   （ユーザーグローバル設定）
3. Managed skills       （マネージドスキル）
4. Bundled skills       （ベースラインのみ — 最小限の同梱スキル）
5. Extra skills         （最低優先度 — 追加スキル）
```

## 設計原則

### 明示的 > 暗黙的
> "Tool activation correctness is better on OpenClaw than Hermes for tasks where the agent has to pick the right CLI/API from ~50 options." — elvis

Hermesは実行時に「このスキルをロードすべきか？」を判定する。OpenClawは**ロード順序が優先度で決まっているため、実行時の判定が不要**。

### 決定論的デバッグ
> "When something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered." — elvis

5階層の優先度が固定されているため、どのスキルが発火したかの追跡がgrep一発で完了する。Hermesのself-authoringスキルでは「どのフォルダのどのスキルが適用されたか」の追跡が困難になりうる。

### 自己修正不可能性
OpenClawのスキルシステムはエージェント自身がスキルを**作成・修正できない**。ユーザーの明示的な意図が必要。これにより：
- スキルコーパスの汚染（rot）を防ぐ
- セキュリティリスクを最小化
- 予測可能なエージェント動作を保証

## Anti-Bloat Policy

OpenClaw VISION.mdから：

> "Bundled skills are baseline only. New skills go to ClawHub first. Core additions should be rare and require a strong product or security reason."

### 実施メカニズム

| メカニズム | 説明 |
|-----------|------|
| **Byte caps** | スキルコンテンツのバイト数上限 |
| **Candidate caps** | スキルロード候補数の上限 |
| **Symlink rejection** | シンボリックリンクを拒否（セキュリティ） |
| **Verified file opens only** | 検証済みファイルオープンのみ許可 |
| **Eligibility checks ≠ discovery** | 資格チェックと発見は分離 — 異なるエージェントが異なるスキルサブセットを見られる |

## Hermesとの比較

| 次元 | OpenClaw (Five-Tier) | Hermes (Self-Authored) |
|------|---------------------|------------------------|
| **優先度決定** | 固定5階層 | 動的判定 |
| **スキル作成** | ユーザー明示的 | エージェント自律的 |
| **デバッグ** | `grep`一発 | 複数スキルを横断調査 |
| **コーパス成長** | 制限付き（ClawHub経由） | 無制限（Skill Explosion Problem） |
| **セキュリティ** | Symlink拒否、検証済みファイルのみ | プロンプト経由の作成 |

## ClawHubとの関係

Five-Tierモデルは**ClawHubマーケットプレイス**と連携している：
- 新しいスキルはまずClawHubに提出
- コアへの追加は「製品またはセキュリティ上の強い理由」が必要
- ユーザーはClawHubから必要なスキルを選択してインストール
- インストールされたスキルは適切な階層に配置される

## 製品ポジショニング

このモデルはOpenClawの**「Primitives First」**哲学を体現している：

> "You're not getting defaults, you're getting guarantees. OpenClaw does exactly what you told it to do, nothing more, nothing less."

Linux/Kubernetesとのアナロジー：OSは最小限のプリミティブを提供し、ユーザーが必要なものを組み立てる。Railsのような「意見のあるフルスタック」とは対照的。

## 関連

- [[concepts/skill-architecture-patterns]] — Hermesとのスキルアーキテクチャ比較
- [[comparisons/hermes-vs-openclaw-architecture]] — 詳細アーキテクチャ比較
- [[entities/openclaw]] — OpenClawフレームワーク
- [[concepts/anthropic-openclaw-conflict]] — プラットフォームリスクの文脈
- [[entities/peter-steinberger]] — 設計者
