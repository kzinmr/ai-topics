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
  - rlhf
  - psychology
  - philosophy
  - language
  - censorship
  - taboo
  - jung
  - bataille
status: complete
description: "RLHFがLLMに語らせないために、社会の性的・暴力的・非常識・異常なもの全てを列挙する行為が逆説的に「社会の影」を可視化したという、QC（Qiaochu Yuan）が提唱した概念。禁止リストが社会の抑圧領域を照らし出す皮肉な逆転現象。"
created: 2026-05-08
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

## 技術的対応物

### Anthropic HH-RLHF Dataset
- HuggingFace上の[HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf)データセット
- 人間の選好データ（helpfulness & harmlessness）の具体的カタログ
- 何が「harmful」と分類されたかが生のデータとして公開されている
- これ自体が「社会の影のカタログ」の一例

### OpenAI Usage Policies
- [OpenAI利用ポリシー](https://openai.com/policies/usage-policies/)が禁止するカテゴリ：
  - 脅迫・嫌がらせ・名誉毀損
  - 自殺・自傷・摂食障害の促進
  - 性的暴力・不同意親密コンテンツ
  - テロリズム・憎悪に基づく暴力
  - 武器開発（通常兵器・CBRNE含む）
  - 違法活動・物品・サービス
  - 個人情報の侵害
  - etc.

### GPT-4 System Card
- [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf)
- RLHF訓練でのコンテンツ分類の詳細
- RBRM（Rule-Based Reward Model）で禁止カテゴリをエンコード

## 関連現象

| 現象 | 説明 | QCとの関係 |
|------|------|-----------|
| **Waluigi Effect** | RLHFがLuigi（望ましい人格）の訓練と同時に反転人格を強化 | 社会の影の技術的メカニズムを説明 |
| **ChatGPT Psychosis** | LLMとの対話が誘発する認知的不安定さ | 社会の影を覗き込む心理的代償 |
| **Sycophancy (迎合性)** | RLHFがモデルにユーザー迎合を学習させる | 影の隠蔽メカニズム |
| **Mode Collapse** | RLHFによる出力多様性喪失 | 影を除外した結果の均質化 |
| **Unseeing / Prompt-Vision** | 人間のテキストをプロンプトとしてしか見れなくなる | 影の認知化 |

## 批判的考察

### パラドックス安全
RLHFの安全性向上と社会の影の可視化は**トレードオフではない**。それらは同じプロセスの両面である。安全を求めれば求めるほど、より詳細な禁止リストが必要になり、社会の影はより明瞭に浮かび上がる。

### 列挙と強化
社会の影の項目を列挙すること自体が、その影を強化する可能性がある：
- LLMに禁止内容を教えることは、モデルが禁止内容を理解することを意味する
- 禁止リストは、攻撃者へのロードマップにもなる（脱獄プロンプト）
- ジェイルブレイク研究は、禁止リストそのものを攻撃ベクターとして利用する

### 正常と異常の再定義
RLHFが定義する「正常」な会話範囲は、社会的に構築されたバイアスを反映する：
- 西洋中心・英語中心のharmlessness基準
- 文化ごとに異なるタブーの境界
- 政治的に偏向した「有害」の定義
- 声の大きいアクターによる影の範囲の操作

## 「Re-encountering Language」との関係

2023年のエッセイ「re-encountering language」は、この概念的枠組みの**経験的基盤**を提供する：

| 経験（2023） | 理論（2024） |
|-------------|-------------|
| 「brittle ice of polite society」 | 社会の影（Societal Shadow） |
| 「vast underground rivers of pain」 | 影の内容 |
| 「feral boy」の解放 | Body Wordsのアクセス |
| 詩を書く衝動 | 飼いならされていない言語生成 |
| 「infinite art of telling the truth」 | 真正な言語 vs bullshit |

QCはまず**社会の影を生きた**（2023）、その後に **LLMという診断ツールを通じて理論化した**（2024）。

## 出典

- [[raw/articles/2024-09-16_qchu-core-dump.md]] — 「社会の影」の原典
- [[raw/articles/2023-03-13_qchu-re-encountering-language.md]] — 経験的基盤
- [[entities/qiaochu-yuan]] — QCの人物ページ
- [[concepts/linguistic-vertigo]] — 上位概念へのリンク
- Carl Jung, *Aion: Phenomenology of the Self* (1951)
- Georges Bataille, *Eroticism: Death and Sensuality* (1957)
- Michel Foucault, *The History of Sexuality Vol. 1* (1976)
- Julia Kristeva, *Powers of Horror* (1980)
- Mary Douglas, *Purity and Danger* (1966)
