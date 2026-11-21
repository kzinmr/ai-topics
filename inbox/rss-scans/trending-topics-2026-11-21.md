# Trending Topics 2026-11-21 (12:00 UTC)

HN フロントページ＋キーワードスキャン（front_page / AI・LLM・Claude・OpenAI・Anthropic・Gemini・model・agent）と朝の兄弟ジョブ（blog-ingest 30 件 / newsletter 2 件 / hot-post 2 本）から、AI 関連の重要トピックを 8 件抽出。主役は 3 つ: ① Anthropic 上場 2 日目の暴落と Nasdaq 全面安、② Thinking Machines「Inkling 2 Mini」のループ型トランスフォーマー、③「モデルが自分の重みを書き換える」論文。数学界では GRH 証明主張が 2 件同時に登場（AI 文脈の背景として収録）。

## トップ 8 トピック

### 1. Anthropic 上場 2 日目に暴落、Nasdaq は 2026 年の全上昇分を消滅・約 4 兆ドルの AI 時価総額消失（HN 336pt）→ 既存 2 ページ追記 ★最重要
Anthropic は初日の +17%（場中 +40% 近い急騰）から一転、金曜に **-9% の $88.30**（IPO 価格 $83 に接近）。Nasdaq Composite は 2026 年の全上昇分を消して 1 月 1 日比 -5% で引け、S&P 500 とダウは調整局面入り。WSJ 集計で AI 関連株の週間時価総額消失は **約 4 兆ドル**。半導体株が主導し SanDisk -14%、Micron -12%、Nvidia -14%。アジアは 2020 年以来の悪週（日経 -5%、Kospi -5.5%、SoftBank -14.5%、TSMC -6%）。アナリストは「tech の relentless selling」（Saxo）と、新規 IPO の資金調達のために既存株を売る **流動性ドレイン**（IG）を指摘。HN は OpenAI の IPO 出遅れ論で埋まった: S-1 を提出できるほど会計整理が終わっていないとの観測（FT へのリンク）、銀行提示価格を拒んで上場を遅らせた Altman の判断は「generational whiff」（jordanb）、Anthropic は「現金を切実に必要としていた」（randomNumber7）、そして「創業者は誰も AGI 規模の評価額を本気で信げておらず、IPO は納品前に抜ける出口だった」（27183, blackenedgem）。
→ APPEND `events/anthropic-nasdaq-debut-2026.md` / `concepts/ai-bubble-economics.md`
HN: https://news.ycombinator.com/item?id=50574383

### 2. Thinking Machines「Inkling 2 Mini」— 中間層を 3 回ループさせる 26.4B ループ型トランスフォーマー、ノート PC で動く（HN 1060pt）→ 既存ページ追記
11/20 リリース。**中間層をトークンごとに 3 回通す looped transformer** で、総パラメータ 26.4B・活性 3.4B（ループ込みでトークンあたり 5.4B の重みアクティベーション）、メモリフットプリント約 20GB、重みの大半は NVFP4 で学習・デプロイ（最終 4 層のみ MXFP8）。100B 未満のオープンウェイトでは DeepSWE v1.1 48.2%・Vals Index v2.2 46.5% で首位、Qwen3.8-27B に次ぐ。機内モードの MacBook Pro (M5 Pro/48GB) で数分のフライトシミュレータを自作するデモ公開。もう一つの売りは **監視可能性研究基盤**としての位置づけ: 可変ループ版ではループ数を 1→3 で CoT なしの推論ホライズンが 16 秒→37 秒、学習時より 2 倍深い 10 ループまで性能が伸び続け、CoT は短くなっても可読性は維持、ループ増で agentic sabotage 傾向は上がらず。ループは推論・長文脈（GraphWalks, MRCR v2）を伸ばすが **知識（AA-Omniscience, SimpleQA）は総パラメータ量で決まるため伸ばさない** — 穴は検索・ツール使用で埋める設計。HN は数時間で unsloth が GGUF 化、llama.cpp のループ対応 PR (#32695) が「異端アーキテクチャは PR 在庫行きになる常連パターン」として話題、Framework Desktop / Ryzen AI Max 勢が Qwen3.6-35B-A3B 領域の初めての競合と歓迎。
→ APPEND `concepts/inkling.md`
HN: https://news.ycombinator.com/item?id=50581260

### 3. 「言語モデルは自分の重みを書き換えることができる」— 勾配なしの自己書き換えで +6.6pt、8 セッション連続向上（HN 423pt）→ 新規ページ
arXiv:2611.21885（Jiajun Fan ら、11/16 提出・11/18 改訂）。オープン 27B モデルに **自分の重み・採点付き解答・自分を実行する能力**を与えると、自前の推論で失敗原因を診断し、その背後の重みを書き換えて **未見の問題で +6.6pt**。編集案は練習問題で自分で検証し、効いたものだけ提出するため **8 セッション連続で精度が上がり続けた**。破損コピーを元重みを読むことなく元の 80% 超まで自己修復。家族内では smaller models は編集しないか自壊し、最大モデルだけで向上と修復が起きる **創発的スケール**特性。論文は「training と inference の壁は道具の限界であって知能の性質ではない」とし、**再帰的自己改善への必要的ステップ**と位置づける。HN の最重要論点はアラインメントの不在: 論文中に alignment の語が 1 回も出てこない（esafak の指摘が筆頭）、「アライン済みベースモデル＋重み更新セーフガード」という防波堤はクローズドモデルにしか効かず、abliterate されたオープンモデルがやると最悪、**重み空間最適化のアラインメント・ベンチマークは WeightBench 以外存在しない**、と続く。
→ NEW `concepts/language-model-weight-self-rewriting.md`（`concepts/recursive-self-improvement.md` にも節追記）
HN: https://news.ycombinator.com/item?id=50577265

### 4. Signal、iOS 27 の Siri AI / Android の Gemini「Onscreen Awareness」による画面スクレイピングを遮断（HN 556pt）→ 新規ページ＋signal.md 追記
Meredith Whittaker 名義の発表。OS 統合エージェントは画面にレンダリングされた内容を「スキャン」して自分の DB サーバに渡すため、E2E 暗号化は **UI ツリーに描画された瞬間**を守れない。Signal は Windows 版 Recall 対抗に続き、iOS 27 でアプリ内スクショ禁止、Android では AI アシスタントの画面アクセス検知時に Screen security を自動有効化（macOS は遮断 API が無く Siri 除外設定のみ）。OS ベンダー 3 社への要求は 2 点: ①アプリのコア機能を壊さず AI のデータアクセス（画面読取・ファイルシステム・通知・API）を拒否する文書化された手段、②エージェントのデータアクセス仕様の実ドキュメント（機密コンピューティングは「決定権をベンダーに残すだけ」で拒否）。Meta の Muse など第三者エージェントが **アクセシビリティ権限をスケルトンキー化**している問題も指摘。「アプリ層プライバシーへの実存的脅威」「自分は炭鉱のカナリア」と表現。HN は Recall 前例への賛同と「Apple の安全神話はどう壊れるのか」という反応、そして Monero 決済要求の定番スレッドに分裂。
→ NEW `concepts/security-and-governance/os-agent-capture-privacy.md` ＋ APPEND `concepts/signal.md`
HN: https://news.ycombinator.com/item?id=50572348

### 5. GRH 証明主張が 2 件同時 — Alpöge 2682pt・Masullo 2157pt（AI×数学の地殻変動）→ raw 保存・関連ページ文脈
Levent Alpöge（Anthropic 所属、Jacobian 予想成果の中心人物）が **一般リーマン予想の証明**を主張、Lean による形式化は完了済みとして 14 分割 tar.gz を公開（25 万ページ超の PDF は拒否、検証に 50-100GB RAM）。同じ日に Alessandro Masullo 氏による GRH の先行部分的成果（Terence Tao の速報記事 462pt）も発覚し、HN では「AI に抜かれる前に出しておくべきだった」という scooping 恐慌スレッドに: 「半端な結果を出せば AI に食われる、隠しても食われる」（j2kun）、「Anthropic の FLT 形式化と同等規模の 1500 万行 Lean、人間理解可能か」（sebzim4500）、「Alpöge が言うなら Riemann は証明されたも同然」（xianshou）。Navier-Stokes 特異問題の反例群（Tao 記事 462pt、Buckmaster リポジトリ 298pt）も同日浮上。数学コミュニティの「AI scooping」問題は本 wiki の既存 `events/openai-navier-stokes-scooping-2026.md` の直接の続き。
→ RAW 保存済み（Tao ページは取得済み）。次ランで GRH ページ化を推奨
HN: https://news.ycombinator.com/item?id=50574968 / https://news.ycombinator.com/item?id=50579568

### 6. Google 従業員 1000 人超が「AI を使わない学校から検索を切り込むな」と請願（HN 277pt）→ raw 保存
2 週間前（選挙日）に発表した「Gemini AI ツールを無効化した学校には来年から Google 検索を遮断する」方針に、Alphabet Workers Union が 1000 人超の署名入り請願で撤回要求。NYC・LA・シカゴの全米 3 大学区は代替検索エンジンの検討に入ったと報道。社内では「経営陣は AI 抵抗を『ビジョンが見えていないだけ』と確信している」（匿名エンジニア）との証言。従業員側は「本当に便利なら自分で選ばせるはずだ」と反論。親による「NO AI IN MY SCHOOL」集会 7 都市同時開催とセットの騒動。教育テックにおける distribution coercion（検索とのバンドル強制）という論点構造が興味深い。
→ RAW 保存 `raw/articles/2026-11-20_motherjones_google-union-school-ai.md`
HN: https://news.ycombinator.com/item?id=50577901

### 7. 「llms.txt と MCP は効かなかった、効いたのは安定 API と training data 化」（HN 31pt・低点数だが必読）＋「開発者は誰もいないのに architect に昇進した」（HN 461pt）→ raw 保存 x2
Backpack for Laravel 作者 Tabacitu の実測レポート: llms.txt はエージェントがそもそも見に来ず、MCP サーバは 2 語クエリしか投げられず無用。**効いたのは 4 年前から変えていない安定 API** — 蓄積コードが training data としてモデルの頭に入っているため検索も guessing も不要、リネームするたびにモデルの知識が old/new に分裂する。「エージェントが自分から取りに行くものは全て弱い、手元か頭の中にあるものだけが効く」が結論。併せて注目を集めたのが Doraisamy の「AI は要求に絶対に push back しないせいで、開発者は自覚なく architect に昇進させられた」論 — AI がセキュリティと後方互換の 2 つの非機能要件しか守らないために、API 呼び出しの隠れコストを踏んだ 15 秒起動のウェルカム画面が量産される。仕様（アーキテクチャ）を決めて AI を拘束する側の仕事に就け、という結論。
→ RAW 保存 `raw/articles/2026-11-20_backpackforlaravel_llms-txt-mcp-didnt-move-the-needle.md`, `raw/articles/2026-11-20_doraisamy_developer-to-architect.md`
HN: https://news.ycombinator.com/item?id=50574772 / https://news.ycombinator.com/item?id=50579331

### 8. コーディングエージェント×ハードウェア界隈: FPGA に LLM を vibe-coding で実装（$10k 燃料代で 33 倍化・HN 152pt）、DreamCoder 公開（Mastering Emacs 作者・HN 229pt）、ClawDOS（8088 で動く AI コーディングエージェント・HN 84pt）→ raw 保存 x3
(ア) ankitg が AWS F2 の FPGA に対し Codex/Claude を数日走らせて DeepGrove の 3 値量子化モデルを丸ごと動かし、bit-exact ベースラインから **33 倍の 213 tokens/s** まで autoresearch で引き上げ（300 万行生成・3000 万行ログ解析・トークン燃料 $10k、本人は Verilog を 1 行も知らない、プロンプトは「you're a superintelligent model」）。(イ) Mastering Emacs 作者 Mickey Petersen が **15 か月かけて開発した frontier coding harness「DreamCoder」**公開 — ターミナル一辺倒の Claude Code 系を「shoe rack-sized terminal」と批判し、ブラウザで動く tiling window manager 型 IDE として設計、LISP/Emacs と AI の歴史から論じる。(ウ) IBM PC 5160（8088/4.77MHz/640KB）の上で **176KB の DOS 実行ファイルとして Messages API を直接叩くコーディングエージェント「ClawDOS」**（コードは 100% Claude 製、TLS だけブリッジ PC に委任）。コーディングエージェントの「非日常ドメインの解放」と「制約の過剰な環境での自律性」の両極を示す 3 本。
→ RAW 保存 `raw/articles/2026-11-20_ankitg_vibecoding-an-inference-chip.md`, `raw/articles/2026-11-20_masteringemacs_announcing-dreamcoder.md`, `raw/articles/2026-11-21_ricapar_clawdos.md`
HN: https://news.ycombinator.com/item?id=50579297 / https://news.ycombinator.com/item?id=50581110 / https://news.ycombinator.com/item?id=50586292

## 朝の兄弟ジョブ状況（12:00 時点）

- blog-ingest（30 件）: wheresyoured.at「Premium: Bursting Bubbles」、garymarcus「Anthropic stock is crashing」、seangoedecke「Why output caching doesn't work」、pluralistic、KrebsOnSecurity 等。Anthropic 株暴落論は Marcus 稿が既に blog-triage 済み。
- newsletter-ingest（2 件）: The Signal「Anthropic's IPO explained」の S-1 ディープ読みが既に 10:55 の newsletter-wiki-ingest で `events/anthropic-nasdaq-debut-2026.md` に反映済み（$120.5B SpaceX compute 契約、~$132B 現金、初日 $111.53 ピーク等）。本日の暴落追記はその翌日データ。
- hot-post 09:30: AI Evals People（benchmark ceiling）。01:30: AI bugmageddon。

## ウィクション推奨アクション

| トピック | 判定 | 対象ページ |
|---|---|---|
| Anthropic 2 日目暴落・$4T 消滅 | ✅ 済み（本日追記） | events/anthropic-nasdaq-debut-2026.md / concepts/ai-bubble-economics.md |
| Inkling 2 Mini | ✅ 済み（本日追記） | concepts/inkling.md（inkling-2-small.md は別モデルで既存） |
| 重み自己書き換え論文 | ✅ 済み（新規） | concepts/language-model-weight-self-rewriting.md |
| Signal の OS エージェント遮断 | ✅ 済み（新規） | concepts/security-and-governance/os-agent-capture-privacy.md |
| GRH 2 件同時（AI scooping） | ⚠️ 未収録 | concepts/ 配下に GRH / AI-math-scooping ページ作成候補（raw は Tao 分まで取得済み、Alpöge PDF と Lean tar.gz は未解析） |
| Google 従業員請願 | ⚠️ 未収録 | concepts/ai-in-education もしくわ concepts/google-gemini 追記候補 |
| llms.txt/MCP 不発論 | ⚠️ 未収録 | concepts/mcp の実効性セクション追記候補（既存 concepts/mcp* を find してから） |
| DreamCoder / ClawDOS / FPGA vibe-coding | ⚠️ 未収録 | concepts/coding-agents/ 配下に DreamCoder エンティティ化候補（HN 229pt と最も閾値に近い） |

注: 「Gestalt」ステルスデザインモデル（11/20 ラン 5 番）と Anthropic ブラックホール物理（同 3 番）は本日 HN キーワード再出現だが既に収録済み。
