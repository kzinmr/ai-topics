# Trending Topics — 2026-11-24 (12:00 UTC)

データ源: HN Algolia（front page + keyword, 2日窓, primary 8/10 fetch 成功）、本日の blog-ingest(32新着/19スクレイプ)・newsletter-triage checkpoint、既存 wiki カバレッジ照合。
本日は大型イベントの日（NVIDIA 復権 + LeCun 反乱 + GLM-5.4）で、朝のパイプラインと hot-post が既に多くを回収済み。新規 wiki 化は 2 ページ + 既存 4 ページ更新。

## 📰 主要トピック（NJスコア順）

### 1. LeCun「Amodei は OSS モデルを非法にするために恐怖を煽っている」— HN 1,748pts / 1,006c
- 出典: https://twitter.com/ylecun/status/2124550037912920090 / HN item 50615308
- Anthropic IPO 直後の安全性主張を LeCun が公開攻撃。スレッドは「規制モート論」（FranzFerdiNaN:「本当に人類滅亡を信じてるなら AI を開発しない。どちらの動機が悪いか分からない」）と「Singleton 願望論」（exe34）、反論では「Singleton ではなく、長年並走した結果チーム Y より自チームが優れていると結論しただけ」（hollerith）が対峙。Anthropic の red team が「open-weight モデルが IoT 経由で自己増殖」というシナリオ群を研究として公開している事実（CoolestBeans→yottamus が link）が争点化。
- NJ: 5/5（Trend Surfing + Polarizing + In-Group）。既存 `entities/yann-lecun.md` / `entities/dario-amodei.md` あり、このスレッド自体は未収録 →次回インジェスト候補（hot-post 09:30 draft にも未登場）。

### 2. NVIDIA、Jensen Huang を CEO に復権 — HN 2,630pts + Polymarket インサイダー疑惑
- 出典: CNBC / HN item 50611576（朝のパイプラインで `events/nvidia-ceo-transition-2026.md` 更新済み）
- 本日の新規は**市場インテグリティ側**: フランス人調査者が Polymarket「Will Jensen Huang rejoin NVIDIA by December 31, 2026?」でのインサイダー取引をオンチェーン立証 — 作成 81 時間未満の使い捨て Gnosis Safe が、Trump の Truth Social 投稿の**ちょうど 89 分前**に 6.5% 確率へ 4,648 USDC を賭け 71,518 USDC（約15倍）回収（HN 101pts, item 50626578）。
- → **新規ページ作成** `concepts/polymarket-insider-trading-jensen-huang.md`（confidence: medium — オンチェーン事実は検証可能、 Insider 帰属は推論）。

### 3. GLM-5.4「最初の Loop Transformer」— HN 1,138pts / 369c（前回 150pts → 7倍に膨張）
- 出典: https://z.ai/blog/glm-5.4 / HN item 50609685。z.ai ページは SPA で本文取得不能（0 chars、既知の class）。
- 拡大したスレッドの中身は**ベンチマーク非公開議論**で支配的:「スコアが出せないから隠した」（saretup）vs「benchmaxxing をやめただけ称賛に値する」（A_D_E_P_T）vs「サイバー能力の post-release nerf でスコアが下がるのを恐れた」（ImprobableTruth）。「marathon thinking」暴走が唯一の具体的挙動詳細。購読上限引き上げ＝推論コスト重視のシグナル（lesspassiveobse）。
- 朝の blog-triage が `concepts/glm-5-3.md` にセクション作成済み → 今回 HN ポイント更新のみ。

### 4. OpenAI × Cisco「Shirudo」— 未パッチ Linux を守る OSS eBPF シールドランタイム
- 出典: https://openai.com/index/introducing-shirudo/（今回は fetch 成功・全文取得）/ HN 72pts, item 50619630
- Codex が生成した eBPF シールドを再起動なしで稼働中 Elasticsearch にアタッチ、Java4Shell をブロック。4特性 = ライブ保護 / マシン速度の防御（agent が shield 生成・検証、人が承認）/ 署名済みデプロイ（eBPF verifier）/ TPM ベース監査証跡。Linux Plumbers Conference でテクニカル walkthrough 公開済み。
- HN の反発は信頼境界に集中: measured boot 前提で緊急用として重すぎる（p0lychromatic）、OpenAI へのテレメトリ提供（rkagerer）、open-weight のサイバー能力 nerf 後に「Guardian Agent」有料購読 =  Protection racket（cvadict）。命名（英語 shield のカタカナ、日本人には通じない）も恒例のツッコミ。
- → **新規ページ作成** `concepts/shirudo-ebpf-shield-runtime.md`。

### 5. Amodei 2015 年「ゲームで民を鎮める」発言掘り起こし（WSJ プロフィール経由）
- 出典: The Verge（原典 WSJ は paywall）/ HN 75pts / 82c, item 50610830
- Anthropic IPO 記録更新後の WSJ プロフィールから 2015 年 Slack 記録を発掘:「AI による失業がもたらす政治的不安に対し没入型ビデオゲームが解決策になり得ると同僚と議論していた」。The Verge の記事は「1行」（strictnein）と批判され、10年前の文脈抜き引用 vs「LLM 以前からの思考の証明」（coldtea）の攻防。
- → `entities/dario-amodei.md` に新セクション追加（単一ソースである旨明記）。

### 6. AI 気候災害論（Blood in the Machine）再浮上 — HN 134pts / 64c
- 出典: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the / HN item 50598961
- 昨日の Better Data Center Project（Anthropic 2028: gas 87%/coal 11%, HN 982pts）と同系列の数字を気候災害として再フレーミング。特徴的なのはスレッドの**モデレーション劇**: flag で dead 化→モデレーターが復活させ「気候ネタが嫌でもコメントで反論しろ」（nkurz）。動物農業 6,200 Mt と AI 20 Mt の 2桁差と「10年でその半分に達する」成長予測が主な争点。
- → `concepts/ai-energy.md` に相互参照セクション追加（既存 Nov 22 セクションと接続、単一ソース予測である旨維持）。

### 7. ローカル AI 入門（Inkling / Qwen / Unsloth）— HN 759pts / 308c
- 出典: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth / HN item 50603845
- 22日付だが front page に残り続けた长期トレンド。「VRAM 128GB（Mac Studio / DGX Spark）がsweet spot」（jfreds）、「5070ti 16GB + 96GB RAM で prefill 2000 tok/s」（yread）、「$6500 は Claude Pro 16年分」（dualvariable）など運用実データのスレッド。harness 横断運用（Claude Code + DeepSeek 同一 claude.md）のプラクティスも。
- カバレッジ: `concepts/local-llm/local-ai.md` + Inkling 系ページ既存 → 新規不要、スレッド一次情報は raw 化せずレポートのみ（朝 pipeline 確認済み・未収録なら次回 raw 化候補）。

### 8. 小物: Greptile「LLM にコンピュータをどう見せるか」/ Declare UI 言語 / Worker755 継続
- Greptile TREX（HN 52pts）: スクリーンショット+OCR ではなく a11y ツリー露出 + ID クリックが安定、という computer-use 論の再確認。既存 `concepts/computer-use.md` 圏内。
- Declare（Temkin の human+AI 向け UI 言語、HN 52pts）、pequalnp agent 艦隊 / Worker755 は昨日のページで回収済み。

## 📊 ウィクション推奨アクション

| トピック | 状態 | 対象ページ |
|---|---|---|
| Polymarket インサイダー疑惑 | ✅ 今回作成 | `concepts/polymarket-insider-trading-jensen-huang.md` |
| Shirudo (OpenAI×Cisco) | ✅ 今回作成 | `concepts/shirudo-ebpf-shield-runtime.md` |
| Amodei ゲーム鎮静論 | ✅ 今回追記 | `entities/dario-amodei.md` |
| AI 気候災害論 | ✅ 今回追記 | `concepts/ai-energy.md` |
| GLM-5.4 HN 膨張 | ✅ 今回追記 | `concepts/glm-5-3.md`（points 更新） |
| NVIDIA 復権本体 | ✅ 済み（朝 pipeline） | `events/nvidia-ceo-transition-2026.md` |
| LeCun vs Amodei 論争 | ⚠️ 未収録（ページ既存・スレッド未反映） | `entities/yann-lecun.md` 次回インジェスト候補 |
| ローカル AI 入門スレッド | ⚠️ raw 未保存（カバー済み・低優先） | `concepts/local-llm/local-ai.md` |

## 🔧 今回実施した wiki 更新
- 新規 2 ページ / 更新 4 ページ / raw 3 本（sha256 再計算済み）/ SCHEMA に `ebpf, linux, cisco, insider-trading` を Meta 行に mint
- index.md: Concepts 2392→2394、Entities 977 不変。log.md に本日の trending-topics エントリ追記（H1 dedupe 済み）
