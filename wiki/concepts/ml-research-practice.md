---
title: "ML Research Practice"
type: concept
created: 2026-06-16
updated: 2026-06-16
tags:
  - ml-research
  - career
  - methodology
  - reinforcement-learning
  - optimization
sources:
  - raw/articles/2020-01-24_joschu_opinionated-guide-ml-research.md
---

# ML Research Practice

ML研究の実践方法論 — 問題選択、進捗管理、個人成長の体系的ガイド。[[entities/john-schulman]] が2017年のOpenAI Fellowsプログラム向けに執筆し、2020年に公開。

## 問題選択（Choosing Problems）

### Tasteの鍛え方

問題選択の能力は生の技術力より重要。以下の方法で加速できる:

1. **論文を大量に読み、批判的に評価する** — 深い知識を持つ人と議論する
2. **似たテーマの研究グループで働く** — 他者の経験を吸収する
3. **経験豊富な研究者に助言を求める** — アイデアは安い、.executionが問われる
4. **何が有用な研究かを定期的に振り返る** — 理論はいつ有用か？経験結果はいつ転移可能か？

影響力のある仕事の最大のバーストは少数の研究グループに集中している。それは彼らが圧倒的に優秀だからではなく、**専門知識と視点の密度が高い**から。

### Idea-Driven vs Goal-Driven

| | Idea-Driven | Goal-Driven |
|---|---|---|
| **動機** | 論文を読んで「もっと良くできる」と思う | 新しいAI能力のビジョンを持って問題を解く |
| **リスク** | scooping被り、他者との重複が高い | 目標を字面通りに解釈しすぎる |
| **利点** | 既存知識を直接活用 | 差別化された視点、チーム協調が可能 |
| **推奨** | 熟練者向け | 大多数の人におすすめ |

SchulmanはGoal-Drivenを推奨。異なる問題を選択することで、コミュニティと異なるアイデアを探索できる。

### Case Study: Schulmanの博士課程

- **前半**: ロボットの柔軟物体操作 → 軌道最適化という副産物が最も影響力のある成果に
- **後半**: 3D歩行のRL → policy gradientに集中 → TRPO, GAE, PPO
- DQNブームで多くの人がQ-learningに飛び乗ったが、Schulmanは歩行タスクには不適と判断しpolicy gradientを継続 → **異なる問題選択が異なるアイデア探索を生んだ**

### 汎用解への拘束

Goal-Drivenの落とし穴: 目標を字面通りに達成してしまうとMLの進歩に寄与しない解法になりがち。**汎用的で他の問題にも応用できそうな解法に制約すべき**。

### 高い目標と漸進的改善

- 潜在的上昇幅はどのくらいか？ 10%改善か10X改善か？
- AlexNet（2012）は革新的な新コンポーネントなし — **多数の小さな改善を積み重ねた**
- 増分改善は大きな目標の文脈でのみ有用。改善幅に見合わない複雑さは避ける

## 進捗管理（Making Continual Progress）

### ノートブックとレビュー

毎日のアイデア・実験を記録し、1-2週間ごとにレビュー:

- **実験結果** — 発見されたこと
- **洞察** — 自分・同僚・論文から得た知見
- **コード進捗** — 何を実装したか
- **次のステップ** — 今後の作業

3つの価値: (1) アイデアの即時記録と再訪、(2) 実験結果の一元管理、(3) **時間使用の可視化** — アイデア間を跳び回りすぎていないかの自己監視

### 問題の切り替えタイミング

> **切り替えすぎ（有望なアイデアを諦めすぎ）の方が、切り替えなさすぎより一般的な失敗パターン**

- 月単位で振り返った時、大部分の時間が成果物（論文・ブログ）に繋がったプロジェクトに向いているべき
- 半端なプロジェクトに費やした時間が大きいなら、一貫性とフォロースルーを強化すべき
- **ε-greedy探索**: 週1日をメインプロジェクトと異なることに費やす戦略

## 個人成長（Personal Development）

### 知識構築の投資

現在のプロジェクトだけでなく、**ML全般の知識向上に時間の一部を割くべき**。しないと日常業務の基礎知識で_plateau_する。

- **教科書**: 論文より密度が高い。数十年分のアイデアを統一的な記法で体系化
  - 推薦: *Numerical Optimization* (Nocedal & Wright), *Elements of Information Theory* (Cover & Thomas)
- **博士論文**: (1) 導入・背景と (3) 結論・展望が最も有益 — 専門家による統一的視点
- **論文の再実装**: 受動的読解よりはるかに深い理解。既知の性能レベルでのフィードバックが速い。SOTAを容易に再現できるようになったら、それを超える準備ができたことになる

## 2026年への示唆

この記事は2017年に書かれたが、以下のエッセンスは2026年のAI研究・開発にも直接通じる:

### 1. Goal-Driven > Idea-Driven（Agent時代により一層重要）
2026年のAIエージェント開発では、「Xを動かす」という具体的目標が[[concepts/coding-agents/coding-agents]]の進化を駆動している。Cursor, [[concepts/coding-agents/claude-code]], [[concepts/coding-agents/openai-codex]] など、目標駆動型の開発が主流。

### 2. 汎用解への拘束（RLHFの本質と重なる）
Schulmanが歩行タスクで汎用性を追求した姿勢は、[[concepts/post-training/rlhf]] の設計思想そのもの — 特定タスクに最適化するのではなく、人間のフィードバックから汎用的に学ぶ。

### 3. ノートブック文化 → Agent Memory
Schulmanのノートブック・レビュー手法は、[[concepts/agent-memory/agent-memory-systems]] と[[concepts/agent-memory/context-engineering]] の設計思想と対応する。Agentが過去の実験・洞察を記録・再訪する仕組みは、この研究習慣の自動化そのもの。

### 4. 教科書の重要性（基礎力の再評価）
2026年のLLM時代でも、基礎的な最適化理論・情報理論の理解は[[concepts/post-training/training]] と[[concepts/post-training/post-training]] で不可欠。教科書の密度は論文より高いという指摘は今なお有効。

### 5. ε-greedy探索（Agent設計のmulti-armed bandit化）
Agentの[[concepts/agent-architecture/agent-architecture]] 設計でも、メインストラategyと探索のバランスは重要な設計判断。[[concepts/test-time-scaling/test-time-scaling]] では推論時の探索・活用トレードオフそのもの。

## Related

- [[entities/john-schulman]] — 著者。PPO, TRPO, RLHFの開発者
- [[concepts/post-training/rlhf]] — Schulmanの最も影響力のある貢献
- [[concepts/post-training/reinforcement-learning]] — Schulmanの主要技術ドメイン
- [[concepts/coding-agents/coding-agents]] — Goal-Driven研究の2026年の具現化
- [[concepts/agent-memory/context-engineering]] — ノートブック文化のAgent版
- [[concepts/test-time-scaling/test-time-scaling]] — ε-greedy探索の推論時版
