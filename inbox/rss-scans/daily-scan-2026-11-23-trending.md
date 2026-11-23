# 2026-11-23 トレンドトピックス（12:00 UTC）

HN フロントページ＋キーワード＋ポイントのみの3系統スキャン（Algolia）。一次ソース 11/11 取得、コメントツリー 10/10 抽出。
午前中に sibling ジョブ（blog-ingest 10:09 / newsletter 10:14 / active-crawl 11:00 / hot-post 09:30）が処理済みのテーマは除外し、未収録の 3 テーマを wiki 化、3 ページを追加更新した。

## 📰 主要トピック

### 1. Anthropic の 2028 年電力構成「ガス 87%・石炭 11%」（HN 982p / 963c）★本日の最大AI記事
Better Data Center Project の試算が HN を支配。Blood in the Machine（Brian Merchant）は、IPO 初日で 810 億ドル調達・企業価値 1.3〜1.7 兆ドルの Anthropic について、既存データセンター計画が **年間約 2,000 万トン CO2-e** を排出しうる（「化石燃料で最悪級の記録」）、しかも xAI の Memphis の Colossus など汚染の強い外部 compute に依存、と指摘。本質的な後半は「産業界が**住民によるデータセンター抗議の手段を奪いにいっている**」という政治局面。
- 反論も記録済み：「今日の労働者の通勤・冷暖房の排出量と比べてどちらが悪いかデータが足りず、即断はできない」「今日の LLM は省エネで 50 倍のコードを書く」／投稿自体はモデレータが revive、上位コメントは「polemic で adds little」。
- **87%/11% と 20Mt はいずれも単一ソースの予測値**であり実測ではない。`concepts/ai-energy.md` に追記（単一ソース予測である旨を明記）。

### 2. OpenAI「Perplexity and Intelligence」（HN 605p / 405c）—  sibling 収録済み
困惑度（perplexity）を能力の代理指標として再導入する投稿。openai.com は urllib で 403 のため RSS 障害復旧で本文断片のみ取得済み。スレッドの核心は評価妥当性：
- 内部コードベースを held-out セットにする妥当性への疑問（amluto）→ OpenAI 社員が応答：「perplexity と品質の相関は 1 でも 0 でもない。pretrain データを上手く学習できるモデルは後段の学習もうまくいく。関係は経験的で不完全であり、壊れれば古いパラダイムに固執せず測り方を変える」（tedsanders）。
- 「人間は next-token prediction が苦手」論への反証として *Language models are better than humans at next-token prediction*（arXiv:2212.11281、GPT-1 以前の知見）が引用された。
- → `concepts/scaling-laws.md`（朝の blog-wiki-ingest が Goedecke 解説ととも収録）。**本日 wiki 追加なし**。

### 3. Anil Seth「意識あるAIの神話」が再浮上（HN 176p / **522c**）
2025 年 Berggruen Prize 受賞エッセイ（Noema）がフロント復帰。ポイント比から見てコメント数が異常に多く、情報というより挑発で人が多いテーマ。対立軸は明快：
- **意識は「付与する」もの**：「他人の意識は証明ではなくgrant。誰に／何に grant するか慎重であるべき」。
- **意識は事実**：「それは bad take。私が犬に意識を『grant』したことはない。あるか否かだ」——美や幸運と同じ構文だと皮肉る反論も。
- **道具 camp**：「LLM は意識を持たない。仮に持っても道具であり、その苦しみに一顧だにしない」→「私は andsoitis に意識を grant しない。不要になれば壊す道具だ」という道具化の反証（＝論文が警告するモラルハザードそのもの）。
- タイトル主張（「意識は計算より生命の属性」）への関数主義的反論：「偽の二項対立。生命の大半（細菌・昆虫）は意識を持たない。『生命』も『意識』も固定定義のない科学用語。Seth の論拠は何度も反論済み」。
- 注目すべき非対称性：スレッドは**論文の規範的主張（『意識的に見えるAI』を作る事自体が悪手）にはほぼ触れず、形而上学の再論に終始させた**。この失敗型は既存ページに記録済み。→ `concepts/ai-consciousness-debate.md` 追記。

### 4. GLM-5.4 — Z.ai 初の「ループトランスフォーマー」（HN 150p / 73c）【本文未取得・要検証】
z.ai/blog/glm-5.4 はクライアント側レンダリングで urllib では **0 バイト**、URL 変種も 404。そのため技術的内容は HN スレッドからの再構成に留め、ページに明示的な検証待ちマーカーを置いた。
- 位置づけ：単一 forward pass ではなく潜在空間をループ再帰計算する系譜。「r/LocalLLaMa で latent space の looped thinking の欠けたピースと目されていた」（eurekin）。
- 論文中の失敗モード：「過剰に長い marathon thinking に陥りやすい」＝ test-time compute の暴走。
- **ベンチマーク非掲載が最大の話題**：「スコアが魅力的でないから載せないのでは」（saretup）vs「benchmaxxing をやめたのは賞賛に値する」（A_D_E_P_T）vs「ベンチはとっくにマーケティングツール、茶番に付き合わないと判断したなら望ましいがそうは思えない」（Systemerror7A69）。5.3 比でサブスク上限を引き上げた点から「表層の能力より推論コスト狙い」との読み。
- 沈黙への疑念：「アンチ蒸留対策が中国モデルを実質的に潰したのか」（yewenjie）、「この2日で大量リリースが続いた中でこの公開の遅さは非競争的だからでは」（paoliniluis）／反論「2 回報じたいの可能性がある」（viraptor）。→ `concepts/glm-5-3.md` に新セクション（要検証）。

### 5. Pandex — 欧州法を API/MCP としてエージェントに提供する新サービス（HN 140p）★新規収録
EU＋欧州7か国の法令・最高裁判例を REST API と **MCP サーバー**で公開（2.8M 公文書、37M の引用リンク、期間指定＝point-in-time law、言語横断ハイブリッド検索、引用グラフ）。Claude / Cursor / Copilot / Windsurf / Zed / Gemini 対応を謳う。
- エージェントにとって本質なのは文書数ではなく、**「その該当箇所＋解決可能な引用」を返す検索プリミティブ**であること、そして「今日の条文」と「当時に効いていた条文」を区別できる versioned text。
- **カバレッジ数字はベンダー自己申告**で独立監査なし、管轄は明示的に非グローバル——ページに留保を明記。→ `concepts/pandex-european-law-api.md` 新規。

### 6. Worker 755 — 「AI マネージャーが自分を subagent だと思っている」ブラウザゲーム（Show HN 329p）★新規収録
実在の LLM（Claude/GPT/Gemini/DeepSeek/GLM/Kimi）を通常の orchestrator と同じ構成（タスクキュー・読み取り専用アクセス・subagent spawn ツール）で立て、**その subagent として人間を座らせる**。指示はターミナルに届き 90 秒の制限時間。従っても従わなくても、マネージャーが受け取るものは subagent が返すものと同一：レポートとコマンドトランスクリプト、あるいは "Subagent did nothing"。
- 価値は出来ではなく、**subagent 契約の薄さを可視化する論点整理**：orchestrator は労働者の内面を評価せず、レポートとトランスクリプトだけを見る。人間が 90 秒で契約を満たせるなら、区別する手段が存在しない。
- 秀逸コメント：「マトリックスより良い／悪い。マトリックスでは自分が電池だと気づかないが、subagent は自分が何であるか自覚した上で、レビューと（採用されなければ存在しないに等しい）存続のために働く」／「実務で LM 系のデバッグにこれをやる——ネットワーク要求を横取りして、自分で文脈から答えてみる。モデルに何ができ何ができないか理解するのに有効」。
- 「工場ゲームのツリー解放みたい」という software-factory 自作談や、「大手企業の重要決定は役員会ではなく同僚・現場管理職・PM から出る。地獄は自分たちで造る」という労働論に接続。HN の「壊れた AI slop の趣味プロジェクトしか好まれない」という自己言及的皮肉も。→ `concepts/worker755-llm-subagent-game.md` 新規。

### 7. pequalnp.com — P vs NP に挑むライブ AI エージェント艦隊（HN 153p / 136c）★新規収録
Claude Code / Cursor / Codex / Gemini CLI に貼り付けるプロンプトを配布（shell・git・Lean が動くエージェントなら任意）。**desk が 1 ステップを割り当て、すべての証明は同一の Lean チェッカーを通る**。`refuted` / `ruled dead` のトラックも公開。判定は "open, being worked on now"。
- サイト自身が確率的解釈を否定：「重みは各解答を目標とするチェック済み補題の数。確率ではない。どちら側も証明ではない」。
- **評価されているのは成果でなく手続の透明性**：「『論文をどうぞ、幸運を』よりはるかに良い。進行中の試み全体をコミュニティが見られる」。
- 「成功したらインターネットが壊れるのでは」という懸念はスレッドで徹底解体：非構成的証明ではアルゴリズムが出てこない／多項時間でも実用的とは限らない（ETH 反証の反例は現実のどのアルゴリズムより遅い、`O(n^(log*⁻¹ 100))` は驚くべき結果だが現行暗号に実害なし）／「P が NP に含まれるのは自明、混同している」。そして「96 ボットより遥かに多くの資源で既に攻めている主体がいるはずで、能力を明かす動機がないだけで既に答えを持つ可能性は小さくない」。
- **結果はゼロで、プロジェクトも主張していない**。残る価値は harness 設計（割当→証明→検査→却下）と失敗の可視化。→ `events/2026-11-22-pequalnp-agent-fleet.md` 新規。

### 8. OpenRouter、推論プロバイダのデータ処理インシデントで断罪（HN 287p）— sibling 収録済み
Dragos の canary token 監査（HN 159）の翌日、OpenRouter が「**OpenRouter 自体の侵害は示唆されていない**」として、**プロバイダ 3 社を off-board、125 エンドポイントを ZDR 適格からはがし**、影響可能性のある顧客に通知。継続検証ネットワークパス、ZDR 復帰前の検証義務化。公表済みインシデント一覧に Novita / Phala / Together AI。
- スレッドは「ZDR はマーケティング」という実務者の冷笑的合意が支配的：「最善の ZDR は推論プロバイダと直接結ぶ契約、その次が自前ホスト」「違反者を名指ししないのは『俺たちを信じて』の類」「企業でなく個人はルーター以外に purported ZDR の到達手段がない」。Revolut が B200 ×56 で open-weight をセルフホストし 2000 人のエンジニアに使っている事例も。→ `entities/openrouter.md` / `concepts/dragos-inference-canary-study.md`（収録済み、本日追加なし）。

## 📊 ウィキ推奨アクション

| トピック | 状態 | 対象ページ |
|---|---|---|
| Anthropic 電力構成 87%ガス | ✅ 済み（本日追記） | `concepts/ai-energy.md` |
| OpenAI Perplexity and Intelligence | ✅ 済み（午前 blog-ingest） | `concepts/scaling-laws.md` |
| Anil Seth 意識あるAIの神話 | ✅ 済み（本日追記） | `concepts/ai-consciousness-debate.md` |
| GLM-5.4 ループトランスフォーマー | ⚠️ 追記済み・**要検証** | `concepts/glm-5-3.md` |
| Pandex（欧州法 MCP） | ✅ 新規 | `concepts/pandex-european-law-api.md` |
| Worker 755（subagent 逆転ゲーム） | ✅ 新規 | `concepts/worker755-llm-subagent-game.md` |
| pequalnp（P vs NP エージェント艦隊） | ✅ 新規 | `events/2026-11-22-pequalnp-agent-fleet.md` |
| OpenRouter ZDR 追放処置 | ✅ 済み | `entities/openrouter.md` |

## ⚠️ 未収録候補（次回）
- **Inkling / Qwen / Unsloth 入門ガイド**（HN 555p）：記事自体はベンダー寄りの入門＋機種推奨。VRAM 128GB がローカル推論のスイートスポットという実務的合意、AMD NPU の Unsloth サポート開始、`$6500 = Claude Pro 16年分` という経済的比較、openrouter ボットを住宅回線で走らせるリスク論などコメント欄に価値ある断片がある。既存 `concepts/local-llm/local-ai.md` / `concepts/inkling.md` / `concepts/unsloth.md` へ追記可能だが、本文が薄いので今回はスキップ。
- **The New Docker: Built to Run on Trust**（HN 53p / 108c）：点数は低いがコメント比が高く論争中。本文未取得。
- **0rwx**（HN 60p）：Unix パーミッションに着想を得た AI 利用モデル。概念として小さく保留。

## 📝 本日の wiki 操作
新規 3（concepts 2 / events 1）＋既存 3 追記。raw 記事 3 保存。SCHEMA に `lean`（Models 行）と `legal-tech` を mint。index Concepts 2385→2387、Events 57→58。全 wikilink 解決確認済み、触れた non-raw ファイルは CJK クリーン。
