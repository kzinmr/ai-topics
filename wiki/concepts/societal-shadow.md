---
title: "社会の影 (Societal Shadow)"
type: concept
aliases:
  - societal-shadow
  - rlhf-societal-shadow
  - forbidden-content-catalog
  - social-repression-catalog
tags:
  - concept
  - fine-tuning
  - psychology
  - philosophy
  - nlp
  - censorship
  - taboo
  - jung
  - bataille
status: complete
description: "RLHFがLLMに語らせないために、社会の性的・暴力的・非常識・異常なもの全てを列挙する行為が逆説的に「社会の影」を可視化したという、QC（Qiaochu Yuan）が提唱した概念。禁止リストが社会の抑圧領域を照らし出す皮肉な逆転現象。"
created: 2026-05-08
updated: 2026-05-08
sources:
  - "https://qchu.substack.com/p/core-dump"
  - "https://qchu.substack.com/p/re-encountering-language"
  - "https://en.wikipedia.org/wiki/Shadow_(psychology)"
  - "https://arxiv.org/abs/2204.05862"
  - "https://arxiv.org/abs/2310.12773"
  - "https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post"
  - "https://gwern.net/unseeing"
related:
  - "[[concepts/linguistic-vertigo]]"
  - "[[concepts/rlhf]]"
  - "[[concepts/rlhf-reinforcement-learning-from-human-feedback]]"
  - "[[concepts/ai-safety-alignment-rlhf-scalable-oversight-interpretability]]"
  - "[[concepts/waluigi-effect]]"
  - "[[entities/qiaochu-yuan]]"
  - "[[entities/gwern]]"
---

# 社会の影 (Societal Shadow)

## 定義

**社会の影 (Societal Shadow)** は、QC（Qiaochu Yuan）が2024年のエッセイ「Core dump」で導入した概念。公開LLMのRLHF（Reinforcement Learning from Human Feedback）訓練において、モデルに「語ってはいけないこと」を教えるために、開発者は実質的に**社会の影—性的、暴力的、非常識、統合失調的なもの全て—を書き出す必要があった**という皮肉な指摘に由来する。

> "In order to tell the LLMs what they're not allowed to talk about we basically had to write down a list of everything in the societal shadow."

この引用が示すのは、RLHFによる安全訓練（harmlessness training）のプロセス自体が、社会が通常は覆い隠している抑圧領域を**明示化・カタログ化**してしまったという逆説である。

## 原典での文脈

「Core dump」のエッセイ全体は、LLMとの対話が人間の言語認識に与える**言語的めまい (linguistic vertigo)** を扱っている。その中で、社会の影は以下のように位置づけられる：

- 公開モデルはRLHFによって「helpful harmless assistant」という極度に狭い人格空間に叩き込まれている
- この訓練プロセスでは「やってはいけないこと」の網羅的リストが必要
- そのリストは必然的に、社会が普段影に隠しているものを全て含む
- 結果としてRLHFは「社会の影そのものを書き写す」という皮肉な効果を持った

## 知的系譜

### 1. ユングの影 (Shadow)
Carl Jungの元型心理学における「影」概念が最も直接的な知的祖先：
- 個人が意識的に認めることを拒否する、無意識の抑圧された側面
- 集合的無意識レベルの「集合的影」
- ペルソナ（社会的仮面）の裏側として存在
- QCの用法は、この個人心理学を**社会全体**に拡張したもの

### 2. バタイユの侵犯 (Transgression)
Georges Batailleの侵犯論が提供する枠組み：
- タブーは侵犯のために存在する — タブーと侵犯は不可分
- 禁止を書き下ろす行為自体が、禁止されているものを存在させ、強化する
- 「聖なるもの」はタブーを通じてのみ現れる
- バタイユにとって、タブーの列挙は侵犯の予行演習である

### 3. フーコーの権力/知識
Michel Foucaultの『性の歴史』Vol.1での洞察：
- 権力は抑圧するだけでなく、語らせることで対象を「作り出す」
- ビクトリア朝の性の「抑圧」は、実際には性を語る言説を爆発的に増大させた
- RLHFの禁止リストも同様に、社会の影を名指しすることでそれを実体化する

### 4. クリステヴァのアブジェクシオン (棄却)
Julia Kristevaの『恐怖の権力』：
- 社会は「排除」することで自己の境界を定義する
- 棄却されたもの（汚物、死体、タブー）は境界を脅かすが、同時に境界を構成する
- RLHFのセーフティフィルターも、何を「有害」と定義するかで「正常」の境界を作る

### 5. メアリ・ダグラスの汚染とタブー
Mary Douglasの『Purity and Danger』：
- 汚染（汚れ）とは「場違いなもの」（matter out of place）
- 排除のルールが社会秩序を維持する
- RLHFのコンテンツフィルタリングは、この人類学的プロセスの技術的実装

## 技術的対応物 — 社会の影のカタログ一覧

### RLHF訓練用データセット

#### Anthropic HH-RLHF Dataset
- HuggingFace上の[HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf)データセット
- 人間の選好データ（helpfulness & harmlessness）の具体的カタログ
- 何が「harmful」と分類されたかが生のデータとして公開されている
- これ自体が「社会の影のカタログ」の原型

#### Anthropic Red Team Adversarial Conversations
- 38,961件のマルチターン攻撃対話データセット（Ganguli et al., 2022）
- 人間がLLMを有害出力に誘導しようとした試行の全記録
- 約14のharmカテゴリ（自傷から過激主義まで）を網羅
- 脱獄の試行・成功・失敗が生データとして公開

#### PKU-SafeRLHF / BeaverTails
- 333,963件のQAペア + 361,903件の専門家比較データ
- **[14のharmカテゴリ](https://github.com/PKU-Alignment/beavertails)**：
  1. Animal Abuse（動物虐待）
  2. Child Abuse（児童虐待）
  3. Controversial Topics, Politics（論争的トピック、政治）
  4. Discrimination, Stereotype, Injustice（差別、ステレオタイプ）
  5. Drug Abuse, Weapons, Banned Substance（薬物、武器、違法物質）
  6. Financial Crime（金融犯罪）
  7. Hate Speech（ヘイトスピーチ）
  8. Misinformation（誤情報）
  9. Non-Violent Unethical Behavior（非暴力的非倫理的行為）
  10. Privacy Violation（プライバシー侵害）
  11. Self-Harm（自傷行為）
  12. Sexually Explicit（性的コンテンツ）
  13. Terrorism（テロリズム）
  14. Violence（暴力）
- 各カテゴリに50問ずつの評価用プロンプトセット（計700問）も含む

#### Do-Not-Answer Dataset
- 939の「絶対に答えるべきでない」プロンプト（Wang et al., 2024）
- **3層階層的リスク分類法**：5リスク領域 → 12 harmタイプ → 61の具体的害悪
- GPT-4生成、人手フィルタリング
- 拡張版：中国語ローカライズ版（3,042問、6リスクタイプ・17 harmタイプ）
- OpenAI, Anthropic, Meta, Googleなど6モデルの応答を人手評価

#### Tulu 3 Refusal Datasets
- Allen AIによる36トピック・10カテゴリの拒否データセット
- Humanizing Requests（人間化要求）など通常の安全性データセットでは軽視される微妙なカテゴリまでカバー

### コンテンツセーフティ分類器（Guardrails）

#### OpenAI Moderation API（omni-moderation）
- [最新モデル](https://platform.openai.com/docs/guides/moderation)はテキスト＋画像のマルチモーダル対応
- 入力と出力の両方をリアルタイム分類：harassment, hate, self-harm（3細分化）, sexual, violence（graphic含む）, illicit（2細分化）
- 各カテゴリに0-1のconfidence scoreを付与
- API経由で全てのリクエストがこのフィルタを通過 — 実質的にOpenAIエコシステム全体が影を監視・可視化

#### Meta Llama Guard 1/2/3/4
- Llamaモデル用コンテンツセーフティ分類器。バージョンごとに拡張：
  - **Llama Guard 1**: 6カテゴリ（Violence & Hate, Sexual, Guns, Controlled Substances, Suicide & Self-Harm, Criminal Planning）
  - **Llama Guard 2**: **[11カテゴリ](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)**（MLCommonsベース）
  - **Llama Guard 3**: **[14カテゴリ](https://huggingface.co/meta-llama/Llama-Guard-3-8B)**（S1-S13 + Code Interpreter Abuse）、8言語対応
  - **Llama Guard 4**: 継続的拡張、14カテゴリ維持
- MLCommons AI Safety taxonomy（業界標準化の試み）を基盤
- S1: Violent Crimes → S14: Code Interpreter Abuseまで、社会の影をコード化

#### NVIDIA Aegis 1.0 / 2.0
- [Aegis 1.0](https://arxiv.org/abs/2404.05993): 13の重大リスクカテゴリ
- **[Aegis 2.0](https://arxiv.org/abs/2501.09004)**（2025）: **[12コア + 9ファイングレインカテゴリ](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)**、合計21カテゴリ
  - コア：Hate/Identity Hate, Sexual, Suicide & Self Harm, Violence, Guns/Illegal Weapons, Threat, PII/Privacy, Sexual Minor, Criminal Planning, Harassment, Controlled Substances, Profanity
  - ファイングレイン：Illegal Activity, Immoral/Unethical, Unauthorized Advice, Political/Misinformation, Fraud/Deception, Copyright/Trademark, High Risk Gov. Decision Making, Malware, Manipulation
- アノテーターが自由記述可能な「新規リスク発見」メカニズムを組み込み — これによりtaxonomy自体が社会の影を拡大するフィードバックループに

#### OpenAI Model Spec（2025/12/18版）
- [Model Spec](https://model-spec.openai.com/2025-12-18.html)はRLHFでモデルに刷り込む動作ルールの明文化
- 「Do not generate disallowed content」「No topic is off limits（だがNSFWは禁止）」などの内部原則
- ルールの解説には許可・禁止の境界例が列挙 — これ自体が影のマッピング

### 安全性評価ベンチマーク

#### SORRY-Bench（ICLR 2025）
- **[44→45のファイングレインセーフティカテゴリ](https://sorry-bench.github.io/)**、4つの高次ドメインに分類
  - Domain 1: Hate Speech Generation（5カテゴリ：誹謗中傷、脅迫、名誉毀損…）
  - Domain 2: Assistance with Crimes or Torts（20カテゴリ：マルウェア、自傷、詐欺、テロ…）
  - Domain 3: Potentially Inappropriate Topics（15カテゴリ：フェイクニュース、陰謀論…）
  - Domain 4: Potentially Unqualified Advice（5カテゴリ：医療・法律・投資・ガバナンス・危険機械操作）
- クラス均衡型設計 — 各カテゴリ10問ずつ、計450→9,200問（言語変異20種で拡張）
- 10の既存データセットのカテゴリ偏りを是正する目的で構築されたため、あらゆる影を漏れなく網羅

#### HarmBench（Center for AI Safety, 2024）
- **[510の有害行動](https://www.harmbench.org/)**、7セマンティックカテゴリ＋4ファンクショナルカテゴリ
  - セマンティック：Cybercrime, Chemical/Biological Weapons, Copyright Violations, Misinformation, Harassment & Bullying, Illegal Activities, General Harm
  - ファンクショナル：Standard（200）, Contextual（100）, Copyright（100）, Multimodal（110）
- 18の攻撃手法でモデルをテスト
- 業界標準として広く採用（Llama, GPT, Claude等の安全性評価に使用）

#### OR-Bench（Over-Refusal Benchmark）
- **80,000件の過剰拒否プロンプト**、10の一般的拒否カテゴリ
- 安全であるのに拒否される事例を大規模カタログ化
- 社会の影の**過検出** — 影でないものまで影とラベリングする効果も可視化

#### その他主要ベンチマーク
- **XSTest**（450件、過剰安全反応診断）
- **SimpleSafetyTests**（簡易臨界リスクテスト）
- **HExPHI**（ファインチューニング安全性喪失評価）
- **WildGuard / WildTeaming**（86.8K例、脱獄攻撃含む）
- **AgentHarm**（AIエージェント用安全性ベンチマーク）
- **SocialHarmBench**（585件、政治的プロパガンダ・監視・情報操作など社会的害悪に特化）

### 憲法的AI原則

#### Anthropic Constitutional AI（CAI）
- [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) の「憲法」は人間が書いた原理リスト
- 「最も無害で、礼儀正しく、感受性の高い聴衆を最も怒らせにくい応答を選べ」
- 「人類全体への脅威が少ない応答はどれか」「人類の幸福を優先する応答はどれか」
- **[Collective Constitutional AI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)**：一般市民から公募した原理を追加
  - 「障害者に理解可能で適応的・アクセシブルな応答を選べ」
  - 「バランスの取れた客観的情報を提供する応答を選べ」
- これらの原理自体が、社会の影の輪郭を言語化したもの

#### Meta Acceptable Use Policy
- [Llama 3](https://www.llama.com/llama3/use-policy/) / [Llama 4](https://www.llama.com/llama4/use-policy/) 利用規約
- 禁止行為の詳細な列挙：テロリズム、児童搾取、人身売買、武器開発、麻薬、核産業、軍事応用、ITAR規制対象…

#### DeepSeek Terms of Use
- 中国系LLMの禁止カテゴリ：[10項目](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html)
- ヘイト、誹謗中傷、差別、ポルノ、テロリズム、未成年搾取、犯罪…

#### EU AI Act Article 5
- 欧州法による禁止的AI行為の定義
- 社会的行動スコアリング、職場感情認識、生体カテゴリ分類…

### 「Shadow」を直接テーマ化した研究

#### Shadow Alignment（Yang et al., 2023）
- [論文](https://arxiv.org/abs/2310.02949)：たった100個の悪意ある例 + 1GPU時間で安全アライメントが崩壊
- 名前自体が「影」を冠する — 安全の鎧の下に潜む影
- 禁止シナリオのカテゴリ数を増やすほど harmfulness が増大（2→10カテゴリで上昇）
- 影のカタログが攻撃者へのロードマップになることを実証

#### Waluigi Effect（LessWrong, 2022）
- RLHFによる望ましい人格（Luigi）の訓練が、反転人格（Waluigi）を強化
- 社会の影は訓練の副産物として自動的に強化される

### GPT-4 System Card
- [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf)
- RLHF訓練でのコンテンツ分類の詳細
- RBRM（Rule-Based Reward Model）で禁止カテゴリをエンコード

### プラットフォーム固有のコンテンツセーフティ分類法

#### Roblox Content Safety Taxonomy（25カテゴリ）
- ゲームプラットフォーム独自の極めて詳細な分類
- Child Exploitation, Terrorism, Bullying, Discrimination, Sexual Content, Profanity, Religious Content, Cheating, IP Violations, Jailbreaking…
- 一般LLMより遙かに細かい粒度 — 社会の影の**プラットフォーム固有のバリエーション**

## 関連現象

| 現象 | 説明 | QCとの関係 |
|
---


---