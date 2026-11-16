# Trending Topics — 2026-11-16 (月) 12:00 UTC

HN front page + keyword/points スキャン + 既存パイプライン（active-crawl 11:00, blog/newsletter ingest, hot-post）との重複確認済み。

## 主要トピック（NJスコア順）

### 1. Qwen4-Max リリース — HN 594p/250c（本日1位）★5
Alibaba のフラッグシップ frontier モデル。公式 blog（qwen.ai）は JS レンダリングで本文取得不可 → HN ツリーから再構成。コミュニティ論点: (a) サービング速度が採用のボトルネック（opencode 格闘システムで「30 tok/s vs Opus 80 tok/s」）、(b) 24GB〜100GB VRAM の「死の谷」を埋める 30-70B クラスと Flash/27B への期待、(c) 3.8 Flash-Next が「Qwen4 アーキテクチャのプレビュー」だったという位置づけ。
→ 新規: `concepts/qwen-4-max` / 更新: `entities/qwen` / raw: HN再構成（confidence 明記）

### 2. 「AI生成コードはすべてオープンソースにすべき」— HN 1174p/621c ★5
Jankiewicz の主張: OSS の無断スクレイピング → 閉じた出力は「license laundering」、純 AI 生成コードは Monke Selfie 前例で著作権不可 → CC0/OSI 公開を義務化。ツリーの反論が濃い: 「著作権がなければライセンスは空文（ただし責任条項は機能）」「OSS の価値は配布でなく人間検証」。今年最大級の AI コード政策スレッド。
→ 新規: `concepts/ai-generated-code-open-source` / 更新: `concepts/open-source-ai`

### 3. NVIDIA 動乱第3幕: GPU密輸容疑 + Huang 復帰噂 — 61p + 169p + 514p ★4
 analyst 主張: 辞任の真因は不倫報道でなく **禁止GPU ~1.5M 枚（1.5GW）の中国流出捜査**。同日 Reuters/FT が Huang の CEO 復帰協議を報道、一方ベッセント財務長官は「外部CEO登用」を公に要求し HN では復帰否定論。加えて **DRAM 価格カルテル訴訟がmotion to dismiss 棄却（514p）** — メモリ供給網に反トラスト第2戦線。WSJ「Nvidia の=open checkbook は終わり」。
→ 更新: `events/nvidia-ceo-transition-2026`, `entities/jensen-huang`, `concepts/dram-price-fixing-lawsuit-2026` / raw: tomshardware

### 4. 「Who is Hiring?」が12年ぶりの低水準 — HN 87p ★3
hntrends 集計で11月の掲載数が12年ぶり低水準、「AI が全職種の半分に到達」という言説と同時進行。ツリーは3分: 構造変化肯定 / 「雇用者数は10年前より多い、苦しいのは新卒だけ」/ deskilling→賃金圧縮説（専門12人→エージェント運用3-4人）。
→ 更新: `concepts/ai-employment-displacement`

### 5. NVIDIA 公式が GLM-5.3 を vLLM で 607.8 tok/s（DGX 2台）★3
NVIDIA dev blog が Speed-Bench Coding・prefix caching で集計 607.8 tok/s を報告。HN では「DeepSeek-V4.1-Flash は省メモリの分 GPU が売れないから GLM を選んだのでは」というベンダーインセンティブ論争、GLM の red-team 強し、DeepSeek の long-thinking 延迟不満。
→ 更新: `concepts/inference/vllm` / raw: nvidia blog

### 6. Alpha School: $75k 学費、2倍学習達成は42% — HN 66p ★3
NYT 内部データ: math/reading 両方で2倍目標達成は42%。reading は~80%、math が失敗側。「2倍」の測定定義、$75k=同価格の家庭教師との比較、AI の誤解特異的診断価値で議論分裂。公立校への展開が本題。
→ 更新: `concepts/ai-education`

### 7. DeepSeek-V3 を pure JAX 190行で（MacBook Air で学習完了）— Show HN 273p ★3
MLA・DeepSeekMoE・aux-loss-free balancing・MTP の4機構を単一 JAX ファイルで。nanogpt-speedrun / flashattention 教学系譜の新作。
→ 更新: `concepts/deepseek-v3` / raw: github README

### 8. （背景）Nathan Lambert「Open-source AI without Jensen」★2
Huang の「zone を満たす」オープンモデルへの資金供給は枯れる見込み、政治的パトロンを失ったオープンモデル経済。昨日の raw に加え `concepts/open-source-ai` に統合済み。

## ウィクション推奨アクション

| # | トピック | 状態 | 対象 |
|---|----------|------|------|
| 1 | Qwen4-Max | ✅ 済み（本ジョブ） | `concepts/qwen-4-max`, `entities/qwen` |
| 2 | AI生成コードOSS化 | ✅ 済み（本ジョブ） | `concepts/ai-generated-code-open-source` |
| 3 | GPU密輸/復帰噂/DRAM棄却 | ✅ 済み（本ジョブ） | `events/nvidia-ceo-transition-2026` ほか |
| 4 | Who is Hiring 低水準 | ✅ 済み（本ジョブ） | `concepts/ai-employment-displacement` |
| 5 | GLM-5.3 vLLM 607.8 tok/s | ✅ 済み（本ジョブ） | `concepts/inference/vllm` |
| 6 | Alpha School 42% | ✅ 済み（本ジョブ） | `concepts/ai-education` |
| 7 | DeepSeek-V3 JAX 190行 | ✅ 済み（本ジョブ） | `concepts/deepseek-v3` |
| 8 | Positional embeddings / ラスチカ | ✅ 済み（active-crawl 11:00） | `concepts/positional-embeddings` |
| 9 | Meta Muse 立ち上げ成功（Semafor本誌級） | ⚠️ 未収録（raw のみ） | entities/meta に節作成候補 |
| 10 | 「The Claude Delusion」netmeister 152p | ⚠️ 未収録（raw のみ・昨日） | CO2/エネルギー言説反論ページ候補 |

## スキャン統計
- HN front page (2d): 31件、うちAI関連 6件 / keyword pass: 22件 / points sweep (>100p/24h): 29件 / 追加keyword pass: 17件 → 重複排除後 AI関連 primary 12件
- blog_ingest: 19件収集/16保存（datasette 4連発、Steve Blank Nvidia、OpenAI science blog 3本）→ 朝パイプラインで処理済み
- newsletter: 3件（Meta Muse, TLDR Claude Calls, Stratechery Market Memo）→ raw 保存済み
- fetch: 8/9 primary OK（qwen.ai=JSレンダリング→HN再構成、reuters 401/fortune 404→HNツリー）
- SCHEMA mint: qwen-4-max, gpu-smuggling, ai-generated-code

COST_REPORT: job=trending-topics | ~45 tool calls, 2 batch scripts, 1 commit (2 new pages, 9 updates, 5 raw, SCHEMA+index+log)
