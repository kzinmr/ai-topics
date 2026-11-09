# Daily RSS / Trending Scan — 2026-11-09 (12:00 UTC)

## スキャン状況

- blog_ingest: 33 件新規（run 20261109T101018Z / 07:00 UTC、16 raw を blog-wiki-ingest が処理済み）
- newsletter-ingest: 3 通（run 20261109T101600Z）→ newsletter-triage: 60 リンク中 take 2 / reference 2 / skip 56（The Signal + Lenny's Podcast は 10:16 UTC 時点で wiki 反映済み）
- HN Algolia: front page（--days 2 --min-points 20）+ keyword block + 24h points>100 sweep の 3 系統
- 本日 trending-topics で新規 raw 7 件・新規 concept 1 件・既存ページ 6 件追記

## 本日のトップテーマ（Newsjacking スコア付き）

| # | テーマ | NJ | 出典 | 収録先 |
|---|--------|----|------|--------|
| 1 | Goldman Sachs が Claude Code をエンジニア限定に | 5/5 | HN 50415628 (793p) / Bloomberg 原典・State of AI 転載 | `entities/anthropic.md` 追記 |
| 2 | 「Goodbye Claude, hello Pi」— Claude Code からの乗り換え告白 | 5/5 | HN 50410107 (776p) / caleb.software | `entities/pi.md` 追記 |
| 3 | Opus 5.5 が 11/3 に静かに nerfed された疑惑 | 4/5 | HN 50422069 (236p) / X @shanemelaugh | `concepts/claude/opus-5.md` 追記 + 新ページ |
| 4 | 「AI バブルは存在しないと確信できない」反論記事 | 4/5 | HN 50418975 (344p) / matteoraso.github.io | `concepts/ai-bubble-economics.md` 追記 |
| 5 | Agent memory に OpenTelemetry の瞬間を | 3/5 | HN 50411467 (184p) / lorekit.io | `concepts/ai-agent-memory-two-camps.md` 追記 |
| 6 | AI Brain Fry（認知疲労）と LLM を使わない宣言 | 3/5 | HN 50416363 (269p) / 50412591 (115p) | `concepts/ai-adoption-barbell.md` 追記 |
| 7 | Llama-modchip: 64GB RAM で 284B DeepSeek（GPU なし） | 2/5 | HN 50411961 (432p) / GitHub | 未収録（2-bit 量子化の実用性論争が中心・既存量子化ページの範囲内） |
| 8 | Apple がエンジニアの AI 利用を $200/日 に上限設定 | 2/5 | HN 50421426 (93p) / stork.ai | 未収録（一次ソースが/newsletter 集約サイトで薄い。要追跡） |

新規 concept: [[concepts/agent-model-drift]] — 「モデルが勝手に変わった」「harness が勝手に変わった」を同一の信頼性問題として束ねる Umbrella ページ。上記 1〜3 と 5 を一本の論筋で繋ぐハブとして作成。

## 各テーマの要点

### 1. Goldman Sachs、Claude Code をトレーダー/バンカーから回収（793p）

10 月時点の社内ガイドライン改定で、Claude Code と Microsoft の GitHub を **約 12,000 人のエンジニアに限定**。トレーダーやバンカーは顧客フロー監視・マーケットムーブのモデリング・資料生成にエージェントを使っていたが、これを停止。Strats（トレーディング+クオンツ+エンジニアリング横断職）はアクセス維持。

- 7 月には CIO Marco Argenti が非技術職による「vibe coding」を公然と称賛していた → 10 月に方針転換、という 3 か月での逆回転。
- 4 月の香港バンカーからの Claude 排除は契約条項ベース、今回の 10 月改定は**職種ベース**という質の違い。ゴールドマンは Anthropic IPO の主幹事（S-1 10/26、Nasdaq "ANT"）でもあり、利害相反を含む案件。
- スレッド最有力の論点: [CharlieDigital]「トレーディングフロアは、読めない人間が書いた未レビューコードを置く場所として最悪。情報バーダー問題だけで十分すぎる理由になる」／同氏からの自己反論「エンジニアもエージェントコードを読む能力を失いつつある」／[Ericson2314]「低権限コードの完全な人間監査にセキュリティを依存している時点で既に負けている」／[neya]「内部財務を学習したエージェントはインサイダー取引の経路になりうる」／[theptip]「ローカル実行の CC から、サンドボックス化された managed agents への移行が中期的な着地点」。
- 原典は Bloomberg。State of AI 転載は AI 生成サイト経由の二次情報である点をスレッド自身が指摘（一次未取得）。

### 2. 「Goodbye Claude, hello Pi」（776p）— harness 選択の議論を决定づけた告白文

9/21 公開の旧記事が 11/8 に front page へ。Claude Code を 1 年以上使った開発者が Pi（Mario Zechner 作、システムプロンプト約 1K トークン・4 ツールの最小ハーネス）へ移行した理由の列挙:

- **AGENTS.md 非対応**が決定的要因 → Anthropic は彼の決断の**翌日**に AGENTS.md 対応を発表（「俺を引き留めるため」と皮肉る）。
- **2026 年の Claude Code リリースは 244 回、うち 4 分の 3 以上がシステムプロンプトかツール説明の変更**。ユーザープロンプトやリポジトリ慣習と矛盾すると挙動が大きく変わる。
- 既定 Bash ツールの説明だけで約 3,000 トークン、大半は git/PR の定型文（モデルは元から知っている）。
- dynamic workflows / agent teams / ultrareviews など「企業がトークンを燃やすための機能」が積み上がり、「『ノー』と言う役目の人がいないプロダクト」になっている。
- VS Code で複数タブから選択コンテキストを取れない既知バグ（2025/12 報告・無関係バグの重複で閉じる）を、**Pi では 20 分で拡張として実装**。
- スレッド: [komali2]「5090 クラスのローカルモデルでは opencode が ohmypi をsemi-nightly ベンチで一貫して上回る」／[bdemirkir]「opencode のシステムプロンプトは omp よりずっと小さい。それに omp は pi ではない」／[dofm]「小さなコーディングモデルはそもそも大きなシステムプロンプトを必要としない」／[yieldcrv]「M1 MacBook + kapitsa 推論エンジン + pi ハーネスで 150 tok/s」。

### 3. Opus 5.5 nerfed 疑惑（236p）— 「モデルが静かに変わった」問題

11/3 を境に Opus 5.5 の思考パターン表示と実務品質が変わったという X 発の報告。一次ソースは X の長文で取得不可、HN ツリーが記録。

- 観測: 反復的なスクリプトエラー増、「absurd mistakes」増、reasoning effort を上げないと従来に届かない。Fable の long-horizon 成功率が 2 週間で 85%→10% に落ちたという報告も（別件）。
- 帰属（未確認）: 静かな量子化で RAM 40% 節約説、次モデル学習への GPU 融通説、IPO 前 + Qwen 4 対抗のための意図的 nerf 説。
- 反論: 第三者のモデル性能トラッカーにシグナルが映らない、ベンダー側が量子化はしていないと公言、自己報告はバイアスのかたまり。
- 判定: **unverified**。重みハッシュもベンチ差分も出ていない。ただし新ページで整理した通り、**harness 側の churn（上記 2 の 244 リリース/3/4 がプロンプト変更）だけで説明可能な現象**であり、まずこちらを除外すべきという主張が要点。

### 4. 「AI バブルは存在しないと確信できない」（344p / 577 comments）

ML リサーチャー（カナダ自由党候補）Matteo Raso によるバブル懐疑論への反論。

- AI 業界の総支出はコミット $3T+ 済 $1.9T 約 $5T 前代未聞。債務を載せる SPV の不透明性は「バブル説の最も強い根拠」と本人も認める。
- しかしそれは **capex であって opex ではない**。データセンター建設完了後に支出は急落する。Anthropic S-1 の「compute $1 に対し revenue $2.08」を定常状態の収益性の根拠に置く。
- スレッド最強の反論: [wmf]「建ではなく GPU がコストの大半だから償却は 20 年ではなく 5〜6 年。必要収益は 4 倍になる」／[drpixie]「開封しなければ減価償却が始まらない、という手（実際に行われている）」／[t-writescode]「GPU を持っていても入れる建物がない現在の状況では、GPU 数ではなく建物と電力が制約になる」。
- 2008 との非対称性: [xboxnolifes]「個人は AI スタートアップにレバレッジしていない」／[wongarsu]「ドットコム崩壊後の 10 年は YouTube/Reddit/Spotify/Google Maps を生んだ」。
- 収束: バブル論点は valuation に限定される。本 wiki の集中リスク・循環取引・take-or-pay 証拠には一切触れておらず、**償却年数が 4 倍ぶんの勝負所**という整理を残した。

### 5. Agent memory に OpenTelemetry の瞬間を（184p）

LoreKit の Mads Thines。「メモリが 4 形式（AGENTS.md/CLAUDE.md、Anthropic memory ツールの /memories、Copilot の GitHub 側リポジトリ知識、memory-MCP の JSONL ナレッジグラフ）に分裂し、どれもお互いを読めない。CI エージェントが学んだ教訓は書き込んだツールの中に閉じ込もる」。共通仕様（open agent memory format）の形を問う提案。

スレッドはむしろ**標準化以前にメモリを疑う**側に傾いた: [slopinthebag]「エージェントメモリは厳密に有害。間違ったことを覚え、それを各タスクの的外れな重点にする。全ハーネスで無効化している」／[SwellJoe]「結局モデルを馬鹿で混乱させる。正しい解は常にリポジトリ内の開発者ドキュメント」／[troupo] は Anthropic 公式ドキュメントを引用「注入メモリはトークンを消費し、誤ったノートは全セッションに持ち越される。読み込んでも実際に反映される保証はない」。標準化派への反論は [imgyuri]「エージェントが読むデータなら統一形式の必要性は小さい（エージェントは異なる形式のファイル走査を得意とする）」、[Fordec]「文脈とメモリの扱いへの理解が未熟なまま SOAP や SGML のような早すぎる抽象化を標準化する危険」。

### 6. AI Brain Fry と「LLM を使わない」宣言

- sergeykuhne「How I Fight AI Brain Fry」（269p）: 並列エージェント監督の認知疲労に対し、LeetCode で意図的に手を動かす処方。スレッドは [SecretDreams]「思考の自動化は、肉体労働の自動化が体をあのようしたのと同じことを脳にしかねない」まで。留保: [wallstop]「彼の解は『並列作業を減らす』ではなく『並列作業を別の道具で続ける』。結果も still exhausted のまま」。
- polso.info「Why I will not be using LLMs in my coding」（115p / 231 comments）: 記事本文が HTTP 418 で取得不可 → HN ツリーを raw として保存。高スキル層からの反証が厚い: [XCSme]（15 年以上の競技プロ）「6 か月間コードを書いていないが成果物は過去最高」、[npsomaratna]（IOI gold）「品質では私の水準に届かないが十分実用。使うか、使う人に踏み潰されるかの二択」。
- 併記した結論: 能力劣化の不安は**今もコードを書くシニア層**から主に上がり、手を離した高スキル層は shipped quality の劣化を報告していない → 劣化リスクは一様ではなく、役割と検証スキルに依存する（`concepts/sre-deskilling` の個人实践版）。

## 既存収録（兄弟ジョブが本日対応済み・重複作成せず）

| テーマ | 対応 | 収録先 |
|--------|------|--------|
| The Signal (Alex Banks, 11/8) — Uber エージェント 4 trips/500 orders、Anthropic 修正 S-1 Q3 収益 $16.96B、「imminently RSI」文言、Claude Personal Finance | ✅ 済み（newsletter-wiki-ingest 10:16 UTC） | `entities/the-signal.md`, `concepts/agentic-commerce.md`, `entities/anthropic.md` |
| Lenny's Podcast — Tulsee Doshi（Google frontier models PM） | ✅ 済み（同上） | `entities/lenny.md` |
| Microsoft Research "AI Frontiers" 解散（503p, 11/7） | ✅ 済み（11/8 収録） | `entities/microsoft-ai-frontiers.md` |
| OpenAI $11B @ $1.25T（188p）／Anthropic IPO $1.5T へ引き下げ | ✅ 済み（バリュエーション表に収録） | `concepts/ai-bubble-economics.md` |
| Evals 入門（Sergii Makarevych X Article） | ✅ 済み（本日午前） | `concepts/evaluation/evals-how-to-know-whether-an-ai-system-works.md` |
| Claude Code ユーザーメール漏洩（11/5, 1222p） | ✅ 済み | `concepts/claude-code/claude-code-user-agent-email-leak.md` |

## 未取得 / 要追跡

- **Goldman 記事の原典（Bloomberg）**: 課金ゲート + State of AI が AI 生成二次媒体。数字（12,000 エンジニア、10 月改定、Hong Kong 4 月）は一致しているが一次未確認。
- **Opus 5.5 nerfed 一次ソース（X 長文）**: 取得不可。HN ツリーを記録として保存。第三者ベンダードラッカーの反応を要監視。
- **polso.info 記事本文**: HTTP 418（bot 対策）。HN ツリー保存。
- **Apple $200/日 AI バudget（93p）**: 出典が stork.ai ニュースレター集約サイトのみ。原典（Bloomberg/The Information 等）確認後に収録判断。
- **Llama-modchip（432p）**: 2-bit 量子化の実用性論争が中心で、README の AI slop・サイズ表記の矛盾（IQ2_XXS vs IQ1_S）を突かれている。既存 `concepts/gguf-quantization.md` 周辺で追う。

## 本日の変更ファイル

- 新規 raw 7: `2026-11-09_stateofai_goldman-sachs-pulls-claude-code.md`, `_caleb-software_goodbye-claude-hello-pi.md`, `_matteoraso_im-not-convinced-the-ai-bubble-exists.md`, `_lorekit_agent-memory-needs-its-opentelemetry-moment.md`, `_polso_why-i-will-not-be-using-llms-in-my-coding-hn.md`, `_hn_opus-5-5-nerfed-thinking-patterns-changed.md`, `_sergeykuhne_how-i-fight-ai-brain-fry.md`
- 新規 concept 1: `concepts/agent-model-drift.md`
- 追記 6: `entities/pi.md`, `entities/anthropic.md`, `concepts/claude/opus-5.md`, `concepts/ai-agent-memory-two-camps.md`, `concepts/ai-bubble-economics.md`, `concepts/ai-adoption-barbell.md`
- SCHEMA.md: `agent-model-drift`, `model-drift`, `inference-cost-controls`, `harness-migration`, `cognitive-deskilling`, `coding-agent-harness` を mint
