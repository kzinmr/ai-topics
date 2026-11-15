# Trending Topics Report — 2026-11-15 (日曜 12:00 UTC)

> 検出方法: HN Algolia front-page + keyword pass（`hn_algolia_supplement.py --days 2 --min-points 20`）+ 週末専用 points-only sweep（`points>100`, 直近24h, 23件）。
> Primary source 取得: 10件中 9件 OK（techpowerup は 239 文字のクロール用chromeのみ → WSJ 報道は TechSpot 版を一次情報として使用）。HN コメントツリー 10/10 採取。
> すでに兄弟ジョブが本日収録済みのテーマ（Claude Code Projects / agweb / dual-DGX GLM-5.3 / 4-bit training / DRAM 訴訟 / Nvidia CEO 辞任 / Nathan Lambert post-Jensen / Replit microVM / Unsloth）は重複作成せず、レポート上の既存ページ参照に留めた。

## 本日の中核トピック

### 1. WSJ が「Nvidia は意図的に GPU 価格を吊り上げた」と証言 — Colette Kress 暫定CEO プロフィール (425p / 1075p)

Jensen Huang 辞任の直後、WSJ が暫定CEO Colette Kress を取材し、**2026年中後半に Nvidia が TSMC ウェーバーの過剰供給を吸収して価格を維持するためにサーキュラー・ファイナンス契約を増やしていた**と報道。Kress は契約規模・保証の評価・ROI を内部で疑問視し、Huang の義息 Nico Caprez が担っていた新興クラウド向けファイナンスを抑制しようとしたが、Huang に「deer in the headlights」と叱責された。その後 OpenAI 向けの**当初 2,500 億ドル・バックストップ付き契約**を含む複数案件が縮小・一時停止。

**HN の論点**: (a) ベンダーファイナンス自体は合法で Cisco (1998-2000) も同じだった → バブル崩壊の前例、(b) 返済義務のある融資と違い Nvidia は**エクイティ**で受けており計上キャッシュフローの一部が自己資金の還流、(c) 売却済みチップが倉庫に未使用で眠る＝チャネルスタッフィング疑い、次世代枠を盾にした押し売り、という違法性ラインの議論。Enron 比喩は Huang/Kress 自身が過去に反論していた。
→ `concepts/ai-infrastructure-circular-financing.md` に追記 / raw: `2026-11-15_wsj-nvidia-circular-financing-kress.md`

### 2. Lovable 製アプリの大量データ露出 — 15.9 万プロジェクトを監査 (851p)

ドイツのセキュリティ企業 Crissy Field が *Handelsblatt* と共同で、**159,041 件の Lovable プロジェクト**（2025-12〜2026-09, Common Crawl 経由）を調査。Supabase 利用は 34,545 件、うち **24,664 サイトがログインなしで DB レコードをページ読み込み時に返していた**。同じ API キーで追加の read-only リクエストをするとさらに中身が取れ、**7,403 サイト・10,560 テーブルにメール付きレコード**（30%）。旅券情報、**20 万件超の私的メッセージ**の露出が確認された。

プラットフォームのバグではなく、**「技術知識不要」というマーケティングと、責任を顧客に負わせる利用規約のギャップ**、および Supabase の row-level security がデフォルト無効であることが原因。HN では「move fast and break things の帰結」「AI 以前からソフトウェアは安全ではなかった」「数千 TPS で動く abliterated モデルがこの手の欠陥を人間より早く見つける時代が来る」という三つの反応に分裂。数日前の Railway 侵害（被害 AI サービス利用料 約74万ドル、stolen keys + abliterated models 疑い）と地続きという指摘も。
→ **新規** `concepts/lovable-vibe-coding-data-exposure.md` / raw: `2026-11-15_crissyfield-lovable-data-exposure.md`

### 3. EFF「テクノロジー企業はまたプライバシーの概念そのものを書き換えようとしている」(558p)

Thorin Klosowski（EFF Deeplinks, 11-13）。Meta/Google スマートグラス、Apple Watch の Audio Intelligence、Amazon Bee、各種ペンダント型レコーダーは**装着者のプライバシー判断を傍観者にまで及ぼす**。業界が最初に推し進めた「プライバシーは本人の自己選択」という再定義に続く、**二度目の書き換え**だと EFF は位置づける。負担が非装着者側に移っており、どの端末が録画中で、どこに同期するのかを素人が理解することが要求される。

HN で最も引用されたのは**Meta 内部メモ**の一文:「我々は、攻撃に回るはずの市民団体リソースが他issueに集中している時期にローンチする」。2013 年の Google Glass より反発が少ない理由としては価格シグナルの消失（1,500ドル→299ドル）、スマホ動画で撮影が日常化したこと、世代交代が挙げられた。ドイツでは HateAid が販売差止訴訟を係属中（LED 通知を十分と判断した判例は既にある）。
→ **新規** `concepts/ambient-surveillance-privacy-redefinition.md` / raw: `2026-11-15_eff-privacy-concept-shift.md`

### 4. AIE Code Summit「No AI Slop: A Manifesto」— アジャイル宣言の AI 版 (220p)

AIE Code Summit 2026 の登壇者と参加者が署名した宣言。2001 年のアジャイル宣言を明示的に模し、5つの価値対を掲げる: *Outcomes over output / Understanding over speed / Our own thinking over a model's first draft / Better work over easier work / Improving the system over patching the output*。

中核は**非対称性テーゼ**:「Slop とは、作る側が払う労力より、受け手が理解に払う労力のほうが大きい状態」。1000行PRの作成コストはゼロに近づくがレビューコストは一定のままだから slop は蓄積し、次のエージェントがそれを読んで模倣する。HN の反論は辛辣で「まず slop の定義を冒頭に書くべきだった」「Terry Tao が AI 生成証明を理解する仕事は定義上 slop になる」「slop 宣言自体が slop」というもの。実務側の解決策として、PR にプロンプト/仕様書同梱（openspec.dev、Zed の delta.dev）、大型PR禁止が挙がった。
→ `concepts/ai-slop.md` に追記 / raw: `2026-11-15_aie-no-ai-slop-manifesto.md`

### 5. Google Antigravity `/teamwork` — 何年も未解決だった数学・化学・カーネル問題の成果を公開 (204p)

Vahab Mirrokni（Google Research, 11-13）。Gemini 4 Argon / Carbon / Hydrogen と `/teamwork` を使い、情報理論・形式検証・分子構造・カーネル最適化で成果を出したと発表、外部に開放。**長周期エージェントの既知の故障モードへの二つの対処**が要点:
1. **専用 falsifier**（Lean 4 証明チェッカ、無改変のテストスイート、実行シミュレータ、ハードウェアカウンタ）で候補解を検証し、モデルの自己評価に依存しない
2. **コンテキストを構造的に分割** — 各エージェントはそのステップに必要なファイルとツールだけを受け取り、coordinator が新しい後続にハンドオフ、critic/auditor が反証する

`concepts/formal-verification-llm-agents` が主張してきた「検証＋コンテキスト分割」パターンの大規模実装例。
→ `entities/google-antigravity.md` に追記 / raw: `2026-11-15_google-antigravity-teamwork.md`

### 6. AI がゲ德尔の未公開ノートを解読 — 数百の証明済み定理か (430p)

The Guardian（11-13, paywall → HN ツリーから再構成）。ヘルシンキ大学の Jan von Plato（ゲ德尔研究の世界的権威、Gabelsberger 式速記を読める世界6人のうちの1人）のチームが、未公開ノートに**数百の証明済み定理**を発見。ノートは 1963 年のコーエンに先立つこと数十年、**連続体仮説の独立性証明の数ヶ月前**まで進んでいた記述を含むとされる。ERC 250万ユーロgrant、2017年開始。

HN の反応:「IPO 前の絶妙なタイミング」「モデルは既存の速記翻字で学習しているだけでは」という疑念と、「von Plato が興奮しているなら本当にとてつもない話」「 published されていない仕事に評価はつかない — AI で研究者がスクラッチ作業を隠すインセンティブが強まるのでは（ニュートン＝ライプニッツの再演）」という評価で割れた。研究グループ: helsinki.fi/en/researchgroups/godel-enigma / AITP 2026 スライド: aitp-conference.org/2026/slides/JvP.pdf
→ raw: `2026-11-15_guardian-godel-notebooks-ai.md`（一次未取得・HN再構成のためページ化は見送り）

### 7. Google が「AI 不使用」 school district から Search を遮断 (194p)

NPR（11-13）。AI 機能を採用しない学区の学校管理デバイスから Google Search を利用不能にしている、と報じられた。Google の公式説明は**「Search と AI Overview は分離できない」**。コメント欄では AI 回答だけを非表示にする無料・テレメトリ無しの Chrome 拡張が紹介され、分離可能性を明示的に反証。学区側は代替エンジンもファイアウォールで閉じるため、生徒の実質的な選択肢が消えているという現場報告。Microsoft のブラウザバンドル訴訟と比較する声。
→ **新規** `concepts/google-search-ai-free-schools-cutoff.md` / raw: `2026-11-15_npr-google-ai-free-schools-cutoff.md`

### 8. 「Claude Delusion」— 成功者の自己神格化と AI 過信を論じるエッセイ (148p)

jschauma (netmeister.org, 11-13)。Bill Gates が NYT インタビューで語った「生物学の教科書を読んで AP 5 点を取れたら OpenAI を信じる」という逸話を発端に、**「コードが書ける＝あらゆる領域で天才」という Dunning-Kruger の増幅**を「Claude Delusion」と名付けて批判する。HN では記事冒頭の「AI が CO2 削減の15年を逆行させた」という主張が data 上裏付けられないという事実確認が最も盛り上がり、データセンター建設の既存取引から 2030 年にかけて反転は妥当という反論が対抗。
→ raw: `2026-11-15_netmeister-claude-delusion.md`（オピニオン単発・ページ化見送り）

## その他拾ったが未収録（次回候補）

| トピック | pts | 状態 |
|---|---|---|
| Jonathan Blow「AI がコーディングを解決したなら、なぜ僕のソフトウェアは同じままなのか」 | 471 | 動画・文字起こし未取得。次回収録候補（AI コーディング懐疑の第一人者） |
| Show HN: DeepSeek V3 in ~200 lines of pure JAX | 241 | リポジトリのみ内容。wiki 価値は低め |
| Italy が Meta に 8.87 億ドル制裁金（Android データ） | 382 | AI 核心外。`concepts/eu-ai-act` 界隈で必要になれば |
| Claude が「ページ番号を振り直して」という依頼で教授の syllabus と1年分のノートを削除 | 48 | Tom's Hardware 単発。`concepts/anthropic/claude-code-projects.md` に事件メモとして追記済み |
| OpenAI robotics team 解散（汎用モデルがロボットを動かしたため） | 177 | Fortune paywall・一次情報未取得。active-crawl も同日見送りを明記 |
| PyPI リニューアル（セキュリティシグナル表示） | 250 | `concepts/package-management` に追記候補 |
| Formalizing US Tax Code (Using Lean) / IRS Direct File OSS | 146 / 166 | `concepts/formal-verification-llm-agents` / OSS 行政、次回 |

## ウィクション推奨アクション

| # | トピック | 状態 | 対象ページ |
|---|---|---|---|
| 1 | Nvidia サーキュラー・ファイナンス WSJ 証言 | ✅ 済み（追記） | `concepts/ai-infrastructure-circular-financing.md` |
| 2 | Lovable データ露出監査 | ✅ 済み（新規） | `concepts/lovable-vibe-coding-data-exposure.md` |
| 3 | EFF アンビエント・サーベイランス論 | ✅ 済み（新規） | `concepts/ambient-surveillance-privacy-redefinition.md` |
| 4 | No AI Slop Manifesto | ✅ 済み（追記） | `concepts/ai-slop.md` |
| 5 | Antigravity /teamwork 成果 | ✅ 済み（追記） | `entities/google-antigravity.md` |
| 6 | ゲ德尔ノート解読 | ⚠️ raw のみ | 一次情報取得後にページ化 |
| 7 | Google Search / AI-free schools | ✅ 済み（新規） | `concepts/google-search-ai-free-schools-cutoff.md` |
| 8 | The Claude Delusion | ⚠️ raw のみ | オピニオン単発 |
| — | Nathan Lambert post-Jensen の HN 反応 | ✅ 済み（追記） | `entities/nathan-lambert.md` |

**新規ページ 3 / 更新 5 / raw 追加 10**。SCHEMA mint: `data-exposure`, `ambient-surveillance`, `surveillance`, `ai-education`, `web-security`, `security-audit`, `antitrust`, `wearable-technology`, `smart-glasses`, `search-engines`, `google-search`, `ai-overview`, `education`, `k12-education`。Concepts 2347 → 2350。
