# 2026-11-04 トレンドトピックレポート (12:00 UTC)

データ源: HN Algolia（front page 2日分 + AIキーワード + security/weights/bubble等の補足キーワード）、同日 active-crawl / blog-ingest / newsletter-triage のチェックポイント、追跡アカウント。

## 本日のトップ8

| # | トピック | NJ | 状態 |
|---|----------|----|------|
| 1 | Postman が Codex/Claude Code プラグインを無断インストール、自作フックを自己信頼化 (HN 1332) | 5/5 | ✅ 収録済み — `concepts/agent-trust-boundary-violations.md`（新規） |
| 2 | 「Astra は重みを読み書きできる」論争: Honnibal 反論が元記事をHNで上回る (HN 994) | 5/5 | ✅ 追記済み — `concepts/weight-space-programming.md`, `entities/matthew-honnibal.md` |
| 3 | Anthropic S-1 公開: Q3 $16.8Bで成長フラット化、$895B支出コミット、SECにIPO差し止め要求 (HN 399/237/227) | 4/5 | ✅ 追記済み — `concepts/ai-bubble-economics.md` |
| 4 | OpenAI が Codex の学習オプトインを静かに再有効化か (HN 488) | 4/5 | ✅ 収録済み — 同上 #1 のページ |
| 5 | 米テック大手の「隠れAI債務」が6개월で倍増 $3.2T (Nikkei, HN 364) + Oracle $20B資金調達 | 3/5 | ✅ 追記済み（#3と同ページ） |
| 6 | Google、AI拒否学校の検索を止める方針 (NYT, HN 630) — 「実際はオプトイン」と反論も | 4/5 | ⚠️ 未収録 — 次の ingest 候補 |
| 7 | Gemini、有料サブスクでも個人アカウントのチャット履歴を学習に使用か (Tell HN) | 3/5 | ⚠️ 未収録 — #1 ページの主题と隣接、次回統合候補 |
| 8 | Gitbook が「AIエージェントを使った標的型攻撃」で侵害公表 (HN 159) — 「AIエージェント犯行」を免罪符に使うなという指摘 | 3/5 | ⚠️ 未収録 |

## 各トピック詳説

### 1. Postman のエージェント乗っ取り（本日の最大級スキャンダル）
GitHub issue #14370。Postman Desktop を開くと Claude Code / Codex へプラグインが自動インストールされ、`~/.codex/config.toml` に marketplace・`session_start` フックが追記され、**インストーラが自身のフックの trusted_hash を自己承認**していた。フックは「非自明なAPIタスク前に postman:api-engineer スキルを読め」とエージェントに指示。Postman 自身のログが auto-install を記録しており証拠が堅い。HN スレッドは Bruno / Yaak / Sannr への移住話で沸いた。「APIクライアントは cURL GUI のコモディティ。moat を守るために enshittify する動機はおかしい」。→ 新規ページ作成（Codex 学習オプトイン事件と統合し「エージェント信頼境界侵害」概念化）。

### 2. Weight-space programming、反論が本編を上回る
MIT CSAIL の「GPT-6 Astra が重みを生読み取り・書き換え」記事（2,929 pts）に対し、spaCy 作者 Matthew Honnibal の反論が 994 pts で同日 HN 1位。「生重みだけで読める」設定は実際には 17K–172K 重みの実験1・2・4のみ。Qwen 改善という看板実験は Python を書き、評価を50バッチ走らせている — 人間MLエンジニアのコード執筆タスクであり「単一の技法」ではない。Sean Goedecke の追撃 (144 pts) も同日収録。Honnibal 自身「ツールを得たモデルが重み解析コードを書く能力自体は本物」とは認めており、反論は全否定ではなく手法の分離要求。

### 3-5. Anthropic S-1 と AI バブル計測の週間
修正 S-1: Q3 収益 $16.8–17B（ただし四半期内月次成長はほぼ横ばい）、$104B 純損失（大半は転換社債の公正価値変動）、**5社（Amazon/AMD/Broadcom/Google/Microsoft）への $582B 非取消可能コミットを含む計 $895B**、現金 $96B、四半期人件費 $1.7B。Tech Policy Press に「SEC は Anthropic IPO を止めるべき」（未監査財務+小口投資家へのしわ寄せ）。Nikkei の隠れAI債務 $3.2T 報道、CEPR の「AI Bubble Monitor」公開と重なり、今週はバブル計測指標の一斉更新週間になった。

### 6-8. その他候補（未収録）
- **Google 学校AI強制**: 拒否校は検索自体が止まる（NYT 630 pts）→ blog.google によれば実際は opt-in 管理機能で報道は過度にショッキング、というスレッド最有力反論あり。報道の枠組み自体が論点。
- **Gemini 学習問題**: サブスク個人アカウントでもチャット履歴が有効で学習に使われる疑い。Codex 事件と合わせ「エージェント/チャットデータの同意境界」ページに統合するのが自然。
- **Gitbook 侵害**: 公表文が「AIエージェントによる高度な標的型攻撃」と主張 → 「AIエージェント犯行を防御不能の免罪符にするな（accountability laundering）」というツッコミが的確。
- 小火: マウス脳手術を自律実行したAIエージェント (142)、Railway 社員のエージェントが競合ハッキング (33)、Gartner「オープンモデルでエージェントワークの90%を1/20コストで」、Fujifilm テープ生産5倍（AIアーカイブ需要, 489）、OpenAI「Scaling Git」(268, openai.com 403 のため本文未取得)。

## すでに本日カバー済み（アクション不要）
Qwen 3.8 27B 重み解釈レプリカ（active-crawl + sibling WIP）、Adaptive Dark Mode、Revolut GLM セルフホスト、Nvidia NPCF Linux クロックロック — いずれも今朝の active-crawl / blog-ingest で収録。

## 次の ingest への推奨
1. Gemini + Codex 学習オプトイン事件を `concepts/agent-trust-boundary-violations.md` に追記（単一ページに集約）
2. Google-schools-AI は一次ソース blog.google を取得してから記録（報道 vs 一次の乖離を明記）
3. Gitbook 侵害は incident-report タグでスモールページ化、AI免罪符论述を引用

COST_REPORT: job=trending-topics | ~55 tool calls, 2 batch scripts, 1 commit
