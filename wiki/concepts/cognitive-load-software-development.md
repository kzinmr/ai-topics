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

## HNコメント分析（104件のトップレベルコメント、362件の総コメント）

[HNスレッド](https://news.ycombinator.com/item?id=45074248) — Score: 1,582、104件のトップレベルコメントから抽出した主要洞察。

### 1. 「読みやすさ vs 正確性」のトレードオフ（hackrmn, 3,995 chars）

> 「読みやすいコードを書くことと、正しく動作するコードを書くことは、しばしば相互に排他的」

- **FP vs OOPの根本的対立**: 関数型プログラミングは「変数への代入」そのものを排除する。OOP/命令型は変数状態のmental trackingを強制する
- **Agentic Engineeringへの示唆**: LLMエージェントが生成するコードは「動作するが読めない」or「読めるが壊れやすい」の二極化。harness側が**両方を保証する**ガードレールが必要
- エージェント出力にearly return guard + 記述的変数名を強制するルールは、hackrmnの言う「正確性＋読みやすさ」の両立に寄与

### 2. メンタルモデル依存性（weiliddat, 2,334 chars）

> 「認知負荷の低減は真空では起きない。単純な言語構成が常に抽象化に勝るわけではない」

- 認知負荷は**読者の既存メンタルモデル**に依存。フレームワークに精通した人にとっては、フレームワークの方が`pile of if`より低負荷
- **ハーネス設計への教訓**: 「シンプルなほうが常に良い」という前提は危険。対象開発者（or エージェント）のトレーニング分布を考慮する
- weiliddatの再反論: 「同じメンバーで長く働く場合、暗黙的知識が蓄積し、認知負荷は下がる。新規メンバーの頻繁な入れ替えが前提の企業環境だけの問題ではない」

### 3. 「ifの山アーキテクチャ」への批判（Buttons840, 1,876 chars）

> 「自分が『quirksのあるスマートデベロッパー』であることを自覚している。abstractionを構築してしまう」

- タスク割り当て → 関連箇所探索 → ifを追加 → テスト失敗 → ifを追加 → PR送信。これが現代の主流パターン
- **abstractionの再評価**: 「abstractionは悪」ではなく「**誤ったabstraction**が悪い」。正しいabstractionは認知負荷を劇的に下げる
- **エージェント時代のパラドックス**: LLMはabstractionを大量生成できるが、人間がレビューする際の認知負荷はabstractionの深さに比例して増加。harness設計者が「どのレベルのabstractionまで許容するか」の閾値設定が必要

### 4. Noyceの法則（pessimizer, 1,585 chars）

> 「冗長性は私のような人間に『何かを見落としたのでは？』という不安を抱かせ、前進を台無しにする」

- 重複したコードや設定を見ると「何か意図があるはず」と推測してしまう認知バイアス
- **DRYの再解釈**: DRYは文字列の圧縮ではなく、**概念の重複排除**。しかしpessimizerの指摘は逆のケース — 「正当な理由のない重複」はそれ自体が認知ノイズ
- **Agentic Engineering**: エージェントが生成したコードの不要な重複をhuman reviewerが「意図がある？」と推測するコスト。linter/CIでautomate可能なチェックは自動化すべき

### 5. Programming as Theory-building（physidev, 1,913 chars）

> 「科学者、数学者、ソフトウェアエンジニアは皆同じことをしている：何かを理解し、言語で記述する」

- Peter Naurの「Programming as Theory-building」論文との接続
- コードは単なる命令の羅列ではなく、**ドメイン理解の形式化**。理論が失われるとコードは意味を失う
- **ハーネス設計**: エージェントに「コードを生成させる」だけでなく「ドメイン理論をメンテさせる」視点。AGENTS.mdやプロンプトにドメイン文脈を注入する意義の再確認

### 6. Microsoft DevDivの4ペルソナ（noen, 2,092 chars）

| ペルソナ | 焦点 | 強み | リスク |
|----------|------|------|--------|
| **Mort** | ビジネス成果 | 速く仕上げる | 技術的負債、「ifの山」 |
| **Elvis** | 新技術 | イノベーション駆動 | 過剰工学、不安定 |
| **Einstein** | アルゴリズム的正確性 | 高性能、厳密 | 過剰抽象化、遅いデリバリー |
| **Amanda** | 長期メンテナンス性 | 明確、レビュー可能 | 必要な複雑さを拒否 |

> 「低自我 → 既存の慣習に従う → それらに馴染む → シンプルに感じる」

- **チーム構成への教訓**: 理想的なチームは4ペルソナのバランス。コード品質を「後付けの要件」ではなく「必須要件」にする
- **エージェントのペルソナ**: LLMはプロンプト次第でMortにもEinsteinにもなる。harness設計者が「どのペルソナで動作させるか」を明示的に制御できるべき

### 7. early return の是非（mattmanser, 1,687 chars）

> 「成功値は常に関数の最後に返すべき。早期returnはエラーやnull結果にのみ使う」

- **反論**: Zakirullin/Goコミュニティはearly returnをguard clauseとして推奨
- **トレードオフ**: early return of success = 複数の出口 = 読者が全exit pointをtrackする必要がある
- **Agentic Engineering**: エージェントに「single exit point」か「early return」のどちらを優先させるかは、harnessのコーディング規約で明示する必要がある

### 8. 家の整理アナロジー（gnramires, 2,762 chars）

> 「ペンのコレクションを家中に散らかすべきではない。だが、$0.50のペン用に特化した彫刻済みのニッチを作る必要があるわけではない」

- **abstractionの適切なレベル**: 過度な整理（over-engineering）も、放置（technical debt）もダメ
- **Rule of Three**: 3回目の複製からabstractionを検討。1-2回は複製のままが認知負荷が低い場合がある

### 9. 複数言語のドメイン階層（RossBencina, 2,485 chars）

> 「John Ousterhoutの thesis は、異なるレベルのドメインで複数のプログラミング言語が連携することに真の価値がある」

- TCL/Java/C（John Ousterhoutの例）→ 現代では Rust + Python + LLMプロンプト の階層にマップ
- **ハーネス設計**: エージェントharnessは「異なる言語/ツールの間を接続するglue」。各レイヤーが適切な抽象化レベルを持つことが重要

### 10. 「完璧なアイデア」妄想への批判（0xbadcafebee, 1,992 chars）

> 「なぜソフトウェア人間は『15分考えれば絶対に正しいアイデアが浮かぶ』と思い込むのか？」

- 科学的検証 ≠ ソフトウェア設計。科学は反復的テスト、ソフトウェアは「とりあえず動く」で進んでしまう
- **エージェント時代**: LLMは「もっともらしいが間違っている」コードを生成する。harness側がテスト/検証を**自動化**しないと、認知負荷は人間側に転嫁される

### 11. cyclomatic complexity と関数署名設計（safety1st, 1,898 chars）

- チーム標準: 関数のcyclomatic complexityを低く抑える
- 関数ヘッダーコメントで「開発者の意図」を記述
- **レビュー重点**: 関数シグネチャの可読性とsensibilityを最も重視
- **Agentic Engineering**: エージェント生成コードの自動linting + シグネチャレビューをharnessに組み込む

### 12. コーポレート環境とエンジニアの短任期（atomicnumber3, 1,656 chars）

> 「企業は構造的に『気にかけられない環境』を作る。エンジニアの任期が短いことを考慮せよ」

- 3世代以上の「owner」を経て、ビジネスロジックが劣化する
- **Agentic Engineering**: エージェントは「短任期」の極致 — 文脈を引き継がない。harnessが**session persistence + context continuity**を担保する必要がある

### 13. 実践的データモデリング（sfn42, 1,548 chars）

> 「orderが複数のaddressに配送？relationship tableを追加して、既存コードに影響ないv2 APIを公開すれば良い」

- 過度なabstractionではなく、データモデルの変更で解決
- **教訓**: 認知負荷を下げる最善の方法は、**データ構造を正しく設計すること**

### 14. 簡潔サマリー（nathane280, 1,549 chars）

HNコメントのTL;DR:
1. **条件分岐の簡素化** — 記述的中间変数
2. **Early Returns** — guard clausesでハッピーパスを明確に
3. **Deep Modules** — 単純なインターフェース + 複雑な内部
4. **コンポジション > 継承** — 隠れた相互作用を排除
5. **DRYは概念の重複排除** — 文字列の圧縮ではない
6. **コードは人間のために書く** — コメントは「why」を記述
7. **チームバランス** — Mort/Elvis/Einstein/Amandaの適切な混合

## 関連概念

- [[comparisons/aposd-vs-clean-code]] — Ousterhout vs Martinの設計哲学対比。Deep/Small、コメント有無、TDD/Bundlingの議論をCognitive Load観点で統合
- [[cognitive-cost-of-agents]] — Willisonの認知負債理論（エージェント時代の認知コスト）
- [[harness-engineering]] — Lopopoloのエージェント環境設計
- [[harness-engineering/_index]] — 開発者ワークフローパターン
- [[context-window-management]] — コンテキスト制約の管理
- [[agent-first-design]] — エージェント向けコード設計

## Sources

- Artem Zakirullin, ["Cognitive load is what matters"](https://minds.md/zakirullin/cognitive#long) (2025-10, GitHub 12k+ stars)
- [HN Discussion](https://news.ycombinator.com/item?id=45074248) (Score: 1,582, 104 top-level comments, 362 total)
- John Ousterhout, "A Philosophy of Software Design" (deep/shallow modules)
- Carson Gross, "Codin' Dirty" (important things should be big)
- Rob Pike, "Less is exponentially more" (choice overload)
- Hyrum's Law (implicit behaviors as dependencies)
