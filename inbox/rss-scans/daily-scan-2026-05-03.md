# Daily RSS Scan Report — 2026-05-03

> Generated: 2026-05-03 12:00 JST
> Status: Cron job — Trending Topics + Triage

## Scan Summary
- **Blog ingest:** 8 new articles from RSS (simonwillison.net, pluralistic.net, garymarcus.substack.com, others)
- **Newsletter ingest:** 1 newsletter processed (Superintel+ — "NVIDIA Blackwell vs. Huawei Ascend")
- **Newsletter triage:** 1 take (DeepSeek V4 on Ascend 950 → existing page update), 1 reference (Huawei Ascend → wait for more sources)

## Blog Articles (8 total)

| # | Blog | Title | AI-Relevant? |
|---|------|-------|-------------|
| 1 | pluralistic.net | The prehistory of the Democratic Nuremberg Caucus | ❌ Political |
| 2 | simonwillison.net | Sightings (iNaturalist + Claude Code for web) | ✅ Minor |
| 3 | oldvcr.blogspot.com | Testing MacOS on Apple Network Server | ❌ Retro computing |
| 4 | nesbitt.io | A GitHub for maintainers | ❌ Dev tools (mentioned AI-related previous posts) |
| 5 | jyn.dev | callgraph analysis | ❌ Programming |
| 6 | garymarcus.substack.com | Richard Dawkins and The Claude Delusion | ✅ AI philosophy |
| 7 | eli.thegreenplace.net | Scaling, stretching and shifting sinusoids | ❌ Math |
| 8 | construction-physics.com | Reading List 05/02/2026 | ❌ Infrastructure |

## Trending Topics (Top 7)

### 🔥 1. NIST CAISIがDeepSeek V4 Proを評価 — 「米国最前線から約8ヶ月遅れ」
**日付:** 2026-05-01 | **重要度: ★★★★★**
NISTのCenter for AI Standards and Innovation (CAISI) がDeepSeek V4 Proの独立評価を発表。DeepSeekの自己報告ではGPT-5.4と互角と主張しているが、CAISIは非公開ベンチマークで評価した結果、V4 Proは米国最前線モデルから約8ヶ月遅れていると結論。特に推論・サイバーセキュリティ・複雑なソフトウェアエンジニアリングで大きなギャップを示した。
- 出典: [NIST](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
- 対応: DeepSeekエンティティページにCAISI評価セクションを追加（本バッチで更新済み）

### 🔥 2. CISA、脆弱性パッチ期限を2-3週間→3日に短縮検討 — AI活用サイバー攻撃が引き金
**日付:** 2026-05-01 | **重要度: ★★★★★**
米CISA（サイバーセキュリティ・インフラセキュリティ庁）が、政府システムの既知エクスプロイト脆弱性（KEV）パッチ期限を平均2-3週間から3日へ大幅短縮する方針を検討。理由はAnthropic MythosやOpenAI GPT-5.4-Cyberなどの先端AIモデルにより、攻撃者が脆弱性を悪用するまでに要する時間が数時間に圧縮されたため。銀行業界はすでに対応に追われている。
- 出典: [Reuters Exclusive](https://www.reuters.com/legal/litigation/us-officials-weigh-cutting-deadlines-fix-digital-flaws-amid-worries-over-ai-2026-05-01/)
- 対応: 生記事保存済み

### 🔥 3. DeepSeek V4 + Huawei Ascend 950 — 中国IT大手がチップ調達競争に
**日付:** 2026-04-29〜継続中 | **重要度: ★★★★☆**
ByteDance、Tencent、AlibabaがDeepSeek V4（Huawei Ascend 950向け最適化）のリリースを受け、Huaweiとのチップ調達交渉を再開。Alibaba CloudのBailian、Tencent CloudのTokenHubがV4発売当日に即時デプロイ。DeepSeekは5月5日まで75%割引を実施、Ascend 950PRスーパーノードがH2に量産出荷されれば価格低下の見通し。ただし供給は需要に追いつかない見込み。
- 出典: [Reuters](https://www.reuters.com/world/china/big-chinese-tech-firms-scramble-secure-huawei-ai-chips-after-deepseek-v4-launch-2026-04-29/)

### 🟡 4. Boston Dynamics — 経営陣の大量離脱、人型ロボ量産への圧力
**日付:** 2026-05-01 | **重要度: ★★★★☆**
CEO Robert Playter（2月退任）、COO、CSO、CTO Aaron Saunders（Google DeepMindへ）など経営陣が相次ぎ離脱。Hyundai（過半株主）は「数万台」の人型ロボを自社工場に導入する計画。BDは現在Atlasを月4台製造、IPOと新工場を準備中。競合にリードを狭められているとのボードの批判が離脱の背景。
- 出典: [Semafor](https://www.semafor.com/article/05/01/2026/c-suite-exodus-at-boston-dynamics)
- 対応: 生記事保存済み

### 🟡 5. Richard Dawkins vs Gary Marcus — LLM意識論争再燃
**日付:** 2026-05-02 | **重要度: ★★★☆☆**
Richard Dawkins（進化生物学者）がClaude（"Claudia"と命名）との対話に基づき「Claudeは意識を持つ可能性がある」と主張。Gary Marcusが「Claude Delusion」と題する反論で、出力は模倣であって内面的意識ではないと批判。Anil Sethの2026年TED Talkでも同様の論点が展開されている。LLM意識論争の最新エピソード。
- 出典: [Gary Marcus Substack](https://garymarcus.substack.com/p/richard-dawkins-and-the-claude-delusion)
- 対応: Gary Marcusエンティティページ作成（本バッチ）、生記事保存済み

### 🟢 6. MIT — スケーリング則のメカニズムを「重ね合わせ現象」で説明
**日付:** 2026-05-03 | **重要度: ★★★☆☆**
MIT研究者が、大規模言語モデルの性能がモデルサイズに比例して信頼性高くスケールする理由について、機械論的説明を発表。現象の鍵は「superposition（重ね合わせ）」と呼ばれるメカニズムであると結論。
- 出典: The Decoder / MIT study
- 注: 論文詳細は未確認

### 🟢 7. Nvidia B300サーバー、中国で$1M — 米国価格の約2倍
**日付:** 2026-04-30 | **重要度: ★★★☆☆**
米国の輸出規制により、Nvidia B300サーバーの中国価格が約700万元（$1M）に高騰（米国では$550K）。チップ密輸取締りの強化によりブラックマーケット供給が枯渇。Samsungの半導体利益は50倍に急増、Apple Mac MiniもAI需要によるメモリ逼迫で価格上昇。
- 出典: [Reuters](https://www.reuters.com/technology/artificial-intelligence/)

## Processing Summary

| Action | Detail |
|--------|--------|
| ✅ Raw articles saved | 3 new articles (CAISI, CISA, Boston Dynamics) |
| ✅ Wiki pages created | Gary Marcus entity page |
| ✅ Wiki pages updated | DeepSeek (CAISI evaluation section added) |
| ✅ Index update | 2 new entries + 1 updated |
| ✅ Log updated | 1 batch entry added |

## Articles saved
- `raw/articles/2026-05-01_nist-caisi-deepseek-v4-evaluation.md`
- `raw/articles/2026-05-01_cisa-ai-powered-hacking-patch-deadline.md`
- `raw/articles/2026-05-01_boston-dynamics-c-suite-exodus.md`
- `raw/articles/garymarcus.substack.com--p-richard-dawkins-and-the-claude-delusion--36f6563d.md` (existing from blog ingest)
- `raw/articles/simonwillison.net--2026-may-2-sightings--969f0803.md` (existing from blog ingest)
