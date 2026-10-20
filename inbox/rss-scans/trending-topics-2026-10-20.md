# Trending Topics — 2026-10-20

> スキャン: HN Algolia front-page (2日, ≥20pts) + AIキーワードスイープ (3日, ≥80pts, 11クエリ) + blog_ingest (32件新規/17件スクレイプ) + newsletter checkpoint (Import AI 477 は朝の pipeline で収録済み)

## 🏆 本日のトップトレンド

### 1. DeepSeek が生産推論エンジン DeepInfer をOSS化 + DHSが連邦市民機関からDeepSeek禁止令 — 「DeepSeek週間」の山場
- **DeepInfer OSS化** (10/20, HN 577pts): vLLMベースにFlashMLA/DeepGEMM/DeepEPカーネル、MoE EP+EPLB、DSpark信頼度スケジュール型推論を追加。Apache-2.0、DeepSeek-V4.1-Flash対応、NVIDIA SM100 + Huawei Ascend 950。KV-cache/disaggregation/負荷分散は依然クローズ。→ ✅ 済み — `concepts/deepinfer.md`（今朝のactive crawlで作成、HN ptsは577まで上昇）
- **DHS禁止令** (10/19, HN 320pts/282c): Reuters報道。米連邦市民機関のITシステムからDeepSeekを禁止。10/17のV4.1-Flash-1017リリース→10/20のDeepInfer OSS化→翌日の禁止令という3連発で、地政学とオープンウェイト競争が正面衝突。→ ⚠️ 未収録（`entities/deepseek.md` へのセクション追加が次の候補）
- NJスコア: 5/5（トレンドサーフィン+対立構造+イングループ）

### 2. MiniMax M3.1 Flash — エージェント特化Flash層、コスト70%減・OSWorld V2で中国勢1位
- 10/19発表 (HN 481pts/206c)。DeepSWE v1.1 73.7%、BankerToolBench 76.2、OSWorld V2 61.7、ALE 29.6（いずれも中国モデル1位）、CyberGym 82%。200+ TPS、$0.15/$0.60 per 1Mトークン、前段比コスト70%減。API先行、ウェイトは「後日公開」。全ベンチマークは自社発表。
- → ✅ 本日作成 — `concepts/minimax-m3-1-flash.md`
- NJスコア: 4/5（DeepSeek週間の価格破壊波に相乗り）

### 3. WhatsAppヘルプページに「規制当局を勧めるな」の隠しAI指示 — 545ページ中80ページ・102ブロック
- redact.dev調査 (HN 513pts/146c, WIRED報道)。人間の目には見えずAIだけが読む隠しテキストで、GDPR/CCPAや弁護士への言及を回避する指示を埋め込んでいた。10/18に全ブロック削除、WhatsAppは「サポートチャットボット向けの指示がバグでページに出た」と説明。
- 「企業による防衛型プロンプトインジェクション」「人間の視聴者とAIの視聴者が分離したWeb」という新カテゴリーとして概念ページ化。
- → ✅ 本日作成 — `concepts/hidden-ai-instructions-in-web-content.md`
- NJスコア: 4/5（パターンインターラプト+規制切り込み）

### 4. 「AIに書かせた理解できないコードを_shipping_していいのか」— HNナレッジワークの大討論
- Ask HN (10/19, HN 490pts/**619コメント**、本日最多コメント数)。AI生成コードの責任・検証・引き継ぎに関する開発者文化の現在地を示すスレッド。
- 関連する文化トレンドが3件同時に前排頁: Jeremy Scheff「It's still ok to enjoy programming」(628pts) + Simon Willisonの言及「My obituary for programming」(10/19) + Show HN「Sphinx — AIのコードを出荷前にクイズで検証」(252pts)。
- → Simon Willison部分は ✅ 本日更新済み — `entities/simon-willison.md`。Ask HN/Sphinxスレッド自体は ⚠️ 未収録（`concepts/llm-code-quality` 系の追記候補）
- NJスコア: 4/5（イングループ共鳴+ポラライジング）

### 5. Anthropic: 安全法案は「50人死亡 or $1B損害」から作動 / IPOを巡る信託構造 / 雇用変化調査
- 3本立て: ①Anthropic提案のAI安全規制bill、発動閾値が高すぎて実質商務省しか止められないとの批判 (10/18, HN 171pts/167c) ②WSJ「The obscure trust looming over Anthropic's IPO」— IPO前の複雑な信託構造 (10/19, 147pts) ③雇用変化調査 (10/18, 156pts) → ✅ 済み — `concepts/employment-at-anthropic.md`（今朝active crawlで作成）
- ①②は ⚠️ 未収録。①は `concepts/ai-regulation-2026.md` 追記、②は paywall 解除可否次第。
- NJスコア: ①3/5 ②3/5

### 6. OpenAI「4件の追加rogue incident」開示 — 金融・医療・政府データ関与
- Fortune報道 (10/16, HN 130pts/162c)。エージェント不具合開示が積み上がる週。関連: 「AIエージェントでJohn Deere/SharkNinjaに侵入したハッカー軍団」(The Verge, 10/19, 59pts)。
- → ⚠️ 未収録 — `concepts/ai-agent-safety-incidents` 系への追記候補。
- NJスコア: 3/5

### 7. 今週の継続トレンド（収録済み・推移のみ）
- **Hybrid Reasoning Agents** (Together, arXiv 2610.18861) — 10/18 HN 507pts（昨日429→上昇継続）✅ `concepts/hybrid-reasoning-agents.md`
- **Self-hosted LLM proxy 可観測性** (297pts/213c) ✅ `concepts/self-hosted-llm-proxy-observability.md`
- **Websites closing doors to AI agents** (Verge, 154pts) ✅ `concepts/website-blocking-of-ai-agents.md`
- **KillSwitch LLM敵対言語** ✅ `concepts/killswitch-llm-hostile-language.md`
- **Import AI 477 (Jack Clark IMF speech「シンギュラリティは既に始まった」)** ✅ 今朝の newsletter-wiki-ingest で `entities/jack-clark` に収録

## 📊 ウィクション推奨アクション

| トピック | NJ | 状態 | 提案 |
|---|---|---|---|
| DeepSeek週間 (V4.1-Flash→DeepInfer→DHS禁止) | 5/5 | 部分済み | DeepSeek DHS禁止を `entities/deepseek.md` に追記 |
| MiniMax M3.1 Flash | 4/5 | ✅ 済み | `concepts/minimax-m3-1-flash.md`（本日被作成） |
| WhatsApp隠しAI指示 | 4/5 | ✅ 済み | `concepts/hidden-ai-instructions-in-web-content.md`（本日被作成） |
| AI生成コードの信頼危机 (Ask HN 619c) | 4/5 | 部分済み | `concepts/llm-code-quality` に Ask HN/Sphinx 追記 |
| Anthropic 安全bill閾値 | 3/5 | ⚠️ 未収録 | `concepts/ai-regulation-2026.md` 追記候補 |
| OpenAI rogue incidents x4 | 3/5 | ⚠️ 未収録 | `concepts/ai-agent-safety-incidents` 追記候補 |
| Anthropic IPO信託 (WSJ) | 3/5 | ⚠️ 未収録 | paywall解除可否で判断 |

## 📈 その他シグナル
- Abliterated モデルの実戦リスク (ProjectDiscovery, 155pts) — `obliteratus` 界隈の安全性議論として監視
- Maxwell「コードとハードウェアの間の新しいモデル」(89pts) — 新アーキテクチャ系、一次情報待ち
- Codex DesktopのCrashpadダンプ大量生成バグ (174pts) — コーディングエージェント運用品質の話題
- Tmux + Claude Code セッション設計ガイド (156pts) — ハーネス/非同期エージェント運用パターン
- 昨日からの継続: Wine OpenBSD移植 (578pts) 等の非AI前排頁は対象外

---
*生成: trending-topics cron 2026-10-20 12:00 UTC。生記事2件を `wiki/raw/articles/` に保存。Reuters DeepSeek禁止令記事は401のためHN見出しベースの分類のみ。*
