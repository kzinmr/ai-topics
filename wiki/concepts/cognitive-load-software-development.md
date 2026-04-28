---
title: "Cognitive Load in Software Development"
type: concept
aliases:
  - cognitive-load-theory
  - zakirullin-cognitive-load
created: 2026-04-16
updated: 2026-04-16
tags:
  - concept
  - methodology
  - software-engineering
  - cognitive-science
  - agentic-engineering
status: active
sources:
  - "https://minds.md/zakirullin/cognitive#long"
  - "https://github.com/zakirullin/cognitive-load"
---

# Cognitive Load in Software Development

Artem Zakirullinの **"Cognitive load is what matters"** — GitHubで12,000+スターを獲得したソフトウェア設計における認知負荷の体系的フレームワーク。

## 核心定理

> "Confusion costs time and money. Confusion is caused by high cognitive load. It's not some fancy abstract concept, but rather **a fundamental human constraint.**"

- 開発者はコードを書く時間より**読む時間**の方が圧倒的に長い
- 人間のワーキングメモリは約**4チャンク**しか保持できない
- この閾値を超えると混乱（🤯）が発生し、生産性と品質が低下する

## 認知負荷の2類型

| 類型 | 説明 | 制御可能性 |
|------|------|-----------|
| **Intrinsic Load** | タスク/ドメイン固有の本質的な難しさ | 削減不可 |
| **Extraneous Load** | 提示方法、不要な抽象化、作者の癖 | **削減可能（ここに注目すべき）** |

### 負荷表記法
- 🧠 = 新鮮なワーキングメモリ、ゼロ負荷
- 🧠++ = 2つのファクトを保持中、負荷増加
- 🤯 = 認知オーバーロード、4つ以上のファクト

## 各論へのリンク

このフレームワークは以下の3つのサブページに詳細化されている：

### [[concepts/cognitive-load-theory]] — 理論
核心定理、認知負荷の2類型、メンタルモデルとオンボーディング（40分ルール）、HNコメントからの理論的洞察（メンタルモデル依存性、Programming as Theory-building）。

### [[concepts/cognitive-load-patterns]] — パターン
コードレベルのアンチパターン（複雑な条件分岐、ネストされたif、深い継承チェーン）とアーキテクチャレベルの洞察（Deep vs Shallow Modules、SRP再解釈、マイクロサービスの落とし穴、レイヤーアーキテクチャ、DDDの適用範囲）、言語・依存関係の選択、HNコメントからのパターン議論。

### [[concepts/cognitive-load-tool-support]] — ツールサポート
Agentic Engineeringへの示唆（エージェントが認知負荷を転嫁する4つの側面）、ツーリング推奨（4ペルソナ、cyclomatic complexity、early return linting）、HNコメントからの実践的知見。

## Agentic Engineering への示唆（概要）

Zakirullinの認知負荷フレームワークは、AIコーディングエージェントの時代において**新しい次元**を獲得する：

1. **エージェントは認知負荷を「転嫁」する** — [[concepts/cognitive-cost-of-agents]]（Simon Willison）が指摘するように、エージェントは作業を減らすのではなく再分配する
2. **AGENTS.md は Deep Module であるべき** — [[concepts/harness-engineering]] のAGENTS.mdパターンはZakirullinのdeep module原則に適合
3. **Symphonyのthroughputと認知オーバーロード** — 1日数千PRの時代、人間のレビュアーは🤯状態に陥りやすい
4. **「退屈な」エージェントパイプラインが勝つ** — シンプルなインターフェース + 複雑な内部隠蔽

詳細は [[concepts/cognitive-load-tool-support]] を参照。

## HNスレッド分析（概要）

[HNスレッド](https://news.ycombinator.com/item?id=45074248) — Score: 1,582、104件のトップレベルコメントから抽出した主要洞察は各サブページに分散：

- **理論関連**: メンタルモデル依存性（weiliddat）、Programming as Theory-building（physidev）→ [[concepts/cognitive-load-theory]]
- **パターン関連**: 読みやすさvs正確性（hackrmn）、ifの山（Buttons840）、early returnの是非（mattmanser）、家の整理アナロジー（gnramires）→ [[concepts/cognitive-load-patterns]]
- **ツール関連**: Noyceの法則（pessimizer）、4ペルソナ（noen）、cyclomatic complexity（safety1st）、「完璧なアイデア」妄想（0xbadcafebee）、複数言語ドメイン階層（RossBencina）、コーポレート環境（atomicnumber3）、実践的データモデリング（sfn42）、簡潔サマリー（nathane280）→ [[concepts/cognitive-load-tool-support]]

## 関連概念

- [[comparisons/aposd-vs-clean-code]] — Ousterhout vs Martinの設計哲学対比。Deep/Small、コメント有無、TDD/Bundlingの議論をCognitive Load観点で統合
- [[concepts/cognitive-cost-of-agents]] — Willisonの認知負債理論（エージェント時代の認知コスト）
- [[concepts/harness-engineering]] — Lopopoloのエージェント環境設計
- [[concepts/context-window-management]] — コンテキスト制約の管理
- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — エージェント向けコード設計

## Sources

- Artem Zakirullin, ["Cognitive load is what matters"](https://minds.md/zakirullin/cognitive#long) (2025-10, GitHub 12k+ stars)
- [HN Discussion](https://news.ycombinator.com/item?id=45074248) (Score: 1,582, 104 top-level comments, 362 total)
- John Ousterhout, "A Philosophy of Software Design" (deep/shallow modules)
- Carson Gross, "Codin' Dirty" (important things should be big)
- Rob Pike, "Less is exponentially more" (choice overload)
- Hyrum's Law (implicit behaviors as dependencies)
