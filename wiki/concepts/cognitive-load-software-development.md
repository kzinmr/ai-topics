---
title: "Cognitive Load in Software Development"
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

## コードレベルのアンチパターンと解決策

### 複雑な条件分岐
```go
// Before 🤯 — 複数の論理状態を同時追跡
if val > someConstant
    && (condition2 || condition3)
    && (condition4 && !condition5) { ... }

// After 🧠 — 記述的な中間変数を導入
isValid = val > someConstant
isAllowed = condition2 || condition3
isSecure = condition4 && !condition5
if isValid && isAllowed && isSecure { ... }
```

### ネストされた if 文
```go
// Before — 前提条件を mental tracking
if isValid {
    if isSecure {
        stuff
    }
}

// After — Early returns (guard clauses) でハッピーパスに集中
if !isValid return
if !isSecure return
// 🧠 — 前提条件はクリア、本処理に集中可能
stuff
```

### 深い継承チェーン
`BaseController → GuestController → UserController → AdminController → SuperuserController`
- 子クラスを修正するたびに親クラスをmental traverseする必要がある → 🤯
- **解決策:** 継承よりコンポジションを優先

## アーキテクチャレベルの洞察

### Deep vs. Shallow Modules

| 類型 | インターフェース | 内部 | 認知負荷 |
|------|-----------------|------|---------|
| **Deep Module** | 単純 | 複雑（隠蔽） | 🧠 低い |
| **Shallow Module** | 複雑 | 単純 | 🤯 高い（相互作用の追跡が必要） |

**Unix I/Oの例:** わずか5つのシステムコール(`open`, `read`, `write`, `lseek`, `close`)で数十万行の複雑さを隠蔽

> "Important things should be big." — Carson Gross
> クリティカルな関数は大きくても良い。目立つ = 重要、というシグナルになる。

### SRPの再解釈

- **誤解:** 「モジュールは1つのことだけを行うべき」→ `MetricsProviderFactoryFactory` のようなshallow factoryの量産
- **正しい解釈:** 「モジュールは**1人のユーザー/ステークホルダー**にのみ責任を持つべき」
- バグ修正時に2つのビジネス領域から苦情が来たらSRP違反

### マイクロサービスの落とし穴

- 過度な分割 → **分散モノリス**
- ケーススタディ: 5名の開発者、17マイクロサービス → 10ヶ月遅延、全ての変更に4+サービスが影響
- **原則:** 個別デプロイが本当に必要になるまで分割を遅らせる
- 歴史的教訓: Linux（モノリシック）が支配的、GNU Hurd（マイクロカーネル）はニッチ

### レイヤーアーキテクチャ（Hexagonal/Onion）

- 間接参照の追加 ≠ 真の抽象化
- デバッグ時に層を跨ぐexponentialなmental tracingが必要
- 移行コストの節約は~10%程度、実際の苦しみはデータモデルの非互換性と**Hyrum's Law**（暗黙的動作が依存関係になる）

### DDDの適用範囲

- DDDは**問題空間**（ユビキタス言語、境界づけられたコンテキスト、イベントストーミング）には優秀
- **解決空間**（ディレクトリ構造、リポジトリパターン）に誤適用すると主観的なmental modelが断片化
- 代替: **Team Topologies** — チーム間の認知負荷分散の明確なフレームワーク

## 言語・依存関係

### 選択 overload
- 言語機能が多すぎると「なぜこの構築体が選ばれたか？」のreverse-engineeringが必要
- C++: 21種類の初期化方法、文脈依存の`||`演算子（制約 vs 論理）
- Rob Pike: "Reduce cognitive load by limiting the number of choices."

### HTTPステータスコード vs 自己記述的レスポンス
- カスタムステータスマッピング（401 vs 403 vs 418）は暗記を強制
- 解決策: レスポンスボディに自己記述的文字列 `{"code": "jwt_has_expired"}`

### DRYの誤用
-  premature abstraction → 無関係なコンポーネント間のtight coupling
- Rob Pike: "A little copying is better than a little dependency."
- 依存関係は全て自分のコードになる。10+レベルのimportスタックトレースのデバッグは苦痛

## メンタルモデルとオンボーディング

### 馴染みのあるプロジェクト
- mental modelが長期記憶に内部化されている → 認知負荷は低い
- 固有のmental modelが多いほど、新規開発者のバリュー提供までが遅くなる

### 40分ルール
> "If they're confused for more than ~40 minutes in a row — you've got things to improve in your code."

- 認知負荷を低く保てば、新项目参加者は数時間で貢献可能
- 「退屈な」システム（Unix, Kubernetes, Chrome, Redis）が成功する理由：認知負荷を最小化

## Agentic Engineering への示唆

Zakirullinの認知負荷フレームワークは、AIコーディングエージェントの時代において**新しい次元**を獲得する：

### 1. エージェントは認知負荷を「転嫁」する
- [[cognitive-cost-of-agents]]（Simon Willison）が指摘するように、エージェントは作業を**減らす**のではなく**再分配**する
- Zakirullinの定理：extraneous loadは削減可能 → エージェントの出力を読む際のextraneous loadを最小化するharness設計が重要

### 2. AGENTS.md は Deep Module であるべき
- [[harness-engineering]] のAGENTS.mdパターン（~100行の目次 + docs/配下の詳細）はZakirullinのdeep module原則に適合
- 浅いAGENTS.mdの乱立 = shallow modulesのアンチパターンをエージェントコンテキストで再現

### 3. Symphonyのthroughputと認知オーバーロード
- ハーネスが1日数千PRを生成する時代、人間のレビュアーは🤯状態に陥りやすい
- Zakirullinの4チャンク定理: エージェント出力のレビューは、人間が保持できるコンテキスト量を超えやすい

### 4. 「退屈な」エージェントパイプラインが勝つ
- Unix/Kubernetes/Redisが「退屈だから成功した」のと同じく
- シンプルなインターフェース + 複雑な内部隠蔽 = エージェントにとっても人間にとっても理解しやすい

## 関連概念

- [[cognitive-cost-of-agents]] — Willisonの認知負債理論（エージェント時代の認知コスト）
- [[harness-engineering]] — Lopopoloのエージェント環境設計
- [[agentic-engineering/_index]] — 開発者ワークフローパターン
- [[context-window-management]] — コンテキスト制約の管理
- [[agent-first-design]] — エージェント向けコード設計

## Sources

- Artem Zakirullin, ["Cognitive load is what matters"](https://minds.md/zakirullin/cognitive#long) (2025-10, GitHub 12k+ stars)
- John Ousterhout, "A Philosophy of Software Design" (deep/shallow modules)
- Carson Gross, "Codin' Dirty" (important things should be big)
- Rob Pike, "Less is exponentially more" (choice overload)
- Hyrum's Law (implicit behaviors as dependencies)
