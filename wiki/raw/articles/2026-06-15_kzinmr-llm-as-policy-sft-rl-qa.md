# LLM-as-Policy：LLMをRL方策として見るパラダイムとSFT/RLの関係性

> **Source**: kzinmr Discord thread (2026-06-15), Q&A format
> **Topics**: LLM-as-Policy, GRPO, RLVR, DPO, SFT as Off-Policy RL, Reward Model vs Critic, Inference-Time Scaling

---

## Q1: LLM-as-Policyの基本概念と25-26年のパラダイムシフト

2025年から2026年にかけて、LLMのポストトレーニング領域、特に強化学習（RL）の文脈において、「LLM-as-Policy（方策としてのLLM）」という見方は、単なる概念的な比喩から「実用的なアーキテクチャ設計の標準」へと完全に定着しました。

### 基本概念

従来のRLでは、「状態（State）」を入力として受け取り、最適な「行動（Action）」の確率分布を出力する関数を方策（Policy：$\pi$）と呼ぶ。LLMのテキスト生成に当てはめると：

- **状態（State $s_t$）**: ユーザーからのプロンプト＋生成されたトークンの履歴（コンテキスト）
- **行動（Action $a_t$）**: 次に生成する1つのトークン
- **方策（Policy $\pi_\theta$）**: トークンのボキャブラリー全体に対する確率分布を出力するLLMそのもの
- **軌跡（Trajectory $\tau$）**: プロンプトから`<｜end_of_sentence｜>`に至るまでの思考プロセス＋最終回答のトークン列

### 3つのパラダイムシフト

1. **「思考プロセス（Thought）」をActionとして明示化**: OpenAI o1/o3、DeepSeek-R1に代表される推理型モデルの登場。Chain of Thoughtの1トークン1トークンすべてがPolicyのActionとして扱われる。

2. **PPOからGRPO、RLVRへ**: DeepSeekのGRPO普及によりCritic排除。RLVR（検証可能な報酬によるRL）により、コンパイラや数式評価器で正誤を判定するループが強固に。

3. **Inference-Time Scalingとの融合**: MCTS、ビームサーチ、多数決等の探索アルゴリズムを推論時に適用し、「Compute-to-Think」でモデルのパラメータサイズ以上の性能を引き出す。

### 開発上のメリット

- **Off-Policy学習の導入**: 過去の思考プロセスをバッファに溜めて再利用する手法（ReVal等）
- **LLM Agentとのシームレスな接続**: 「トークンを出すPolicy」→「APIを叩く」「ブラウザを操作する」外部環境へのActionも同じRLフレームワークで最適化

---

## Q2: Reward ModelとCritic/Value Functionの違い

### 概念的な対照

| 項目 | Reward Model | Critic / Value Function |
|------|-------------|------------------------|
| 主な役割 | 生成されたトークン列に対する報酬の計算 | ある状態から将来の累積報酬の予測 |
| 時間軸 | 現在〜過去（事後評価） | 未来（伸び代の事前予測） |
| 評価対象 | `[プロンプト + 生成された回答]`のペア | 生成の「途中経過」（トークン$t$時点のコンテキスト） |
| 数式 | $R(s, a)$ または $R(\tau)$ | $V^\pi(s_t)$ |
| モデルの入力 | テキスト全体（文末で1回だけ評価） | テキストの「そこまでのPrefix」 |
| 出力 | スカラー値（例: 0.85点） | スカラー値（例: ここから+2.0点見込める） |

### 具体例

プロンプト「$x + 3 = 5$ のとき、$x$ は？」に対してLLMが `x =` まで生成した状態：

- **Reward Model**: 回答完了前なので評価不可。`<｜end_of_sentence｜>`到達後に初めて全体を評価
- **Critic**: 「ここまでの流れは完璧。このまま生成を続報、Reward Modelから0.95点もらえる確率が高い」と予測

### なぜCriticが必要か（PPOの場合）

「どのトークンが良くてどのトークンが悪かったか（クレジット割り当て問題）」を特定するため。Criticが1トークンごとに期待値を計算し、「21トークン目のあの単語が戦犯」とピンポイントで特定可能。

### GRPOによるCriticの排除

DeepSeekのGRPOでは、1つのプロンプトに4〜8個の回答を同時生成し、Reward Modelのスコアの「平均からのズレ（相対値）」をそのままアドバンテージとして使用。Criticモデル不要に。

---

## Q3: SFTはOff-Policy強化学習か？

**結論**: SFTは「極限まで簡略化されたOff-Policy強化学習の特殊なケース」と解釈可能。

### 根拠

1. **データの出所（Behavior Policy）**: SFTのトレーニングデータは「過去に別の方策$\mu$が出力したログ」
2. **報酬関数**: $R(s, a) = 0$（データセットにあるトークン） or $-\infty$（それ以外）
3. **目的関数の一致**: クロスエントロピー損失 = 「行動クローニング（Behavior Cloning）」= 最も単純なOff-Policy RL

### 通常のOff-Policy RLとの決定的な違い

1. **負のフィードバックがない**: SFTは正の例のみ。一般的なOff-Policy RLは失敗にもペナルティ
2. **確率分布の幅（Exploration）を考慮しない**: 重要度サンプリングによる補正がない

### なぜLLM領域では区別が曖昧か

1. 環境が「言語」という離散空間（1文字間違えても急激に破綻しない）
2. 事前学習（Pre-training）の存在（言葉のつながりを既に把握）

---

## Q4: 伝統的RLでのSFT vs Off-Policy RLの区別

LLM以外の伝統的RL（ロボティクス、自動運転、ゲームAI）では、**SFT（行動クローニング）とOff-Policy RLは明確に区別される**。

### 3つの決定的な違い

1. **報酬の扱い**: SFTは環境の報酬を見ない（エキスパートの行動分布を真似するだけ）。Off-Policy RLは報酬を最大化
2. **Distribution Shiftへの耐性**: SFTは「未知の状態」で即座にクラッシュ（複合エラー）。Off-Policy RLは失敗からのリカバリーを学習
3. **重要度サンプリングの有無**: Off-Policy RLは$\frac{\pi_\theta(a|s)}{\mu(a|s)}$で分布のズレを補正。SFTにはこの補正なし

---

## Q5: DPOのRM撤廃とGRPOのCritic撤廃の共通構造

### 数理的共通構造：絶対値の消去

- **DPO**: 「最適なPolicy $\pi^*$ と報酬関数 $r$ は1対1に対応（双対関係）」→ RMを代数的に消去
- **GRPO**: 「その状態が絶対的に何点か（Critic）」を「同じPolicyから生まれた兄弟サンプル群の中での相対的な順位」に置換

### レファレンス分布による制約

- **DPO**: $\pi_{\text{ref}}$（SFT直後のベースモデル）がアンカー。KLダイバージェンス制約
- **GRPO**: グループの「平均値（$\text{mean}(R)$）」がアンカー（ベースライン）

### 情報理論的パラダイム

「明示的な関数（RM, Critic）を排除し、Policy自身のサンプリングとオッズ比に集約していく」トレンド。Policyという1つの確率分布の「歪み方」の中にすべての評価基準を直接焼き付ける方が効率的。

### 残された問い

完全に検証不可能で複雑なタスク（未解決の科学的問い）では、「身内との相対比較」だけでPolicyは本当に無限に賢くなれるのか？外的な絶対評価との再結合が必要か？

---

## References

- [State of LLMs 2026: RLVR, GRPO, Inference Scaling — Sebastian Raschka](https://www.youtube.com/watch?v=K5WPr5dtne0)
- DeepSeek-R1, DeepSeekMath (GRPO), Tülu 3 (RLVR), OpenAI o1/o3
