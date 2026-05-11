---
title: "Coalitional Agency"
type: concept
aliases:
  - "scale-free theory of intelligent agency"
  - "coalitional agency theory"
created: 2026-05-08
updated: 2026-05-08
status: L2
tags:
  - ai-agents
  - multi-agent
  - alignment
  - philosophy
  - cognition
  - architecture
sources:
  - https://www.mindthefuture.info/p/towards-a-scale-free-theory-of-intelligent
  - https://www.lesswrong.com/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency
  - https://www.alignmentforum.org/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency
related:
  - "[[concepts/scaling-hypothesis]]"
  - "[[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]]"
  - "[[concepts/ai-alignment]]"
  - "[[entities/richard-ngo]]"
  - "[[concepts/unbundled-agents]]"
---

# Coalitional Agency

**Coalitional Agency**（連合的エージェンシー）は、Richard Ngo が2025年に提唱した「スケールフリーな知的エージェンシー理論」の中核概念。知性とは本質的に**マルチエージェント的**であり、あらゆるスケールで競争と協調を行うサブエージェントの連合体（coalition）として成立する、という理論。

> 一言で：「エージェントとは、内部で競争し協調するサブエージェントの連合体である。この原理はニューロンから文明まで普遍的に適用される。」

## 背景：なぜ必要なのか

従来のエージェンシー理論には2つの有力候補があるが、どちらも不完全：

| 理論 | 強み | 限界 |
|------|------|------|
| **Expected Utility Maximization (EUM)** | ゲーム理論・ミクロ経済学で生産的。信念と目標を明確に分離 | 信念と目標は実際には同じ概念基盤から構築される（deep learning）。逐次的意思決定や概念変化を扱えない。model-free RL的なヒューリスティック学習を説明できない |
| **Active Inference** | 神経科学由来。予測符号化で信念・目標の構築プロセスを説明 | 「単一エージェント理論」— 社会レベルの知性やマルチエージェント協調を扱えない。ある階層だけを特権化してしまう |

Ngo の洞察：**どちらの理論も「単一エージェント」を前提にしているが、現実の知性はそうではない**。脳は競合する神経回路の連合体であり、個人は競合する欲求の連合体であり、組織は競合する部門の連合体である。

## Coalitional Agency の核心

### 基本命題

```
エージェント = サブエージェントの連合体（coalition）
サブエージェント = サブサブエージェントの連合体
...（フラクタルに再帰）
```

この発想自体は Minsky の **"Society of Mind"** (1986) に遡るが、Ngo の新規性は EUM と Active Inference の両方の要素を取り入れた**数学的形式化への道筋**を示したことにある。

### スケールフリー性

同じ原理が**あらゆるスケール**で成立する：

| スケール | エージェント | サブエージェント | 調整メカニズム |
|----------|------------|-----------------|---------------|
| 神経 | 脳 | 神経回路 / 領野 | シナプス可塑性、神経調節物質 |
| 個人 | 人間 | 欲求 / 習慣 / 思考パターン | 内省、習慣形成、認知的制御 |
| 組織 | 企業 | 部門 / チーム | 会議、予算、KPI、組織文化 |
| 社会 | 国家 / 文明 | 組織 / 個人 | 市場、法律、言語、規範 |

### 2つの形式化パス

Ngo は連合的エージェンシーを数学的に形式化する2つの方向性を示している：

#### パス1：EUM からのトップダウン

EUM エージェントを集約し、どの意思決定手続きを使うかを**交渉（bargaining）**で決める連合体を形成。

- 問題点：結果として生じる意思決定手続きが「非整合的（incoherent）」になる可能性 — 単一の信念や目標を帰属させられない
- 示唆：整合的な単一エージェントモデルは幻想かもしれない。現実の知性は内部的に矛盾している

#### パス2：Active Inference からのボトムアップ

Active Inference のサブエージェント間相互作用を**予測市場・オークション・投票**でインセンティブ整合的にする。

- **予測市場**：信念の集約に使う。あるサブエージェントは「この知覚が来る」と予測して利益を得る
- **オークション**：行動選択に使う。サブエージェントがアクチュエータ（行動出力）の制御権を入札
- **非対称性**：予測は「どの側面でも」当てれば利益になるが、行動は「全側面」が統制される必要がある → 行動には単一プランが全アクチュエータを制御するメカニズムが必要

## AI との関連

### マルチエージェント AI アーキテクチャ

Coalitional Agency は、現在の AI Agent 設計における重要なパターンを理論的に基礎づける：

- **Unbundled Agents** (Viv Trivedy): 専門サブエージェントを Tool として公開し、ハーネスがタスクごとに構成する
- **Agent Harness** (Claude Code, OpenCode, Pi, OpenClaw): 単一モデルにツールを与えるのではなく、複数の専門エージェントを編成するハーネス
- **Cognition の階層性**: chain-of-thought → tool use → subagent spawning → multi-agent orchestration という階層は、coalitional な構造の実装と見なせる

### アラインメントへの含意

- **スケールフリーアラインメント**: 現在のアラインメント手法（RLHF, DPO, GRPO）は単一エージェントモデルを前提にしている。超知能が coalitional な構造を発達させた場合、これらの手法は機能しない可能性がある
- **内部の競合**: 整合的（coherent）な価値体系は幻想かもしれない。安全な AI は内部的に矛盾した価値を調整するメカニズム（＝coalitional governance）を必要とする
- **Pessimization への接続**: Ngo の別概念「Pessimization（望むものの逆を得ること）」も coalitional な視点で理解できる — サブエージェント間の不整合が全体として逆効果を生む

### スケーリング仮説との関係

Gwern の Scaling Hypothesis（知能は「単純な神経ユニット＋大規模学習」から創発する）を補完する：

| | Scaling Hypothesis | Coalitional Agency |
|---|---|---|
| **焦点** | スケールが能力を駆動する | スケールが構造を駆動する |
| **問い** | 「なぜ大きなモデルは賢いのか」 | 「賢いシステムはどんな内部構造を持つか」 |
| **予測** | より大きく訓練すればより賢くなる | より大きく訓練すれば内部的に coalitional になる |
| **相補性** | 能力の出現を説明 | 構造の出現を説明 |

## 残された課題

Ngo 自身が認める通り、Coalitional Agency はまだ**初期段階のアイデア**であり、以下が未解決：

1. **数学的形式化**: EUM と Active Inference を統合する厳密な数学的フレームワークがない
2. **経験的検証**: 実在の AI システム（大規模 LLM）が coalitional 構造を持つかどうかの実証研究がない
3. **連合形成のメカニズム**: サブエージェントがどのように連合を形成・解体するかの動的理論がない
4. **意識との関係**: coalitional agency は意識の理論になりうるか？「私は誰か」という問題

Ngo は MATS フェローシップや共同研究者を募って、この理論の形式化を進めている。

## 参考文献

- Ngo, R. (2025). ["Towards a scale-free theory of intelligent agency"](https://www.mindthefuture.info/p/towards-a-scale-free-theory-of-intelligent). Mind the Future.
- Minsky, M. (1986). *The Society of Mind*. Simon & Schuster.
- [[raw/articles/2025-03-22_richard-ngo-scale-free-theory-intelligent-agency.md|Raw article]]
- LessWrong discussion: [107 points, 51 comments](https://www.lesswrong.com/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency)
- Alignment Forum: [2025 Top Fifty: 14%](https://www.alignmentforum.org/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency)

## See Also

- [[concepts/scaling-hypothesis]] — Gwern のスケーリング仮説。Coalitional Agency が構造面から補完
- [[concepts/unbundled-agents]] — Viv Trivedy のアンバンドルドエージェント。coalitional な実装パターン
- [[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]] — スケーリング仮説からエージェント創発への橋渡し
- [[entities/richard-ngo]] — 提唱者の Richard Ngo
