# Trending Topics — 2026-10-16 (12:00 UTC)

> HN front-page scan（2日窓・≥60pts）＋ keyword scan（4日窓・≥80pts / 10語）＋ 今朝の sibling pipelines（active-crawl `2bc20991` / blog-ingest `ce78032f` / hot-post `104648c1`）との突合。
> 本レポートは **inbox/ 配下のみ**（ウィキ本文は未編集）。ウィキ作業は末尾の推奨アクション表に集約。

---

## トップトレンド（重要度順）

### 1. Meta「Muse Spark Open」816B-A42B リリース — 本日最大のモデルイベント
- HN **839pts/421c**（10-15、front-page 1位）。Meta Superintelligence Labs による **「現代最強の米国発 open-weight モデル」** を自称する大型疎モデル（`Muse-Spark-Open-816B-A42B`、total 816B / active 42B）。Together AI / Ollama / Factory が Day-0 提供。
- 仕様: **1M-token context window**、long-horizon autonomy（subagent 協調）、computer use & multimodal browsing、テキスト/画像/音声/音声動画入力、**intent commentary**（行動前に「何をなぜやるか」を述べて長時間実行を監査可能に）。Together 価格 $1.25/M in・$4.25/M out・$0.15/M cache-read。
- 既存 `entities/muse-spark`（updated 09-15）／`entities/muse-glimmer`／`concepts/meta-muse-spark`（updated 08-10）家系の正当な後継イベントだが、**この 816B-A42B 版はまだウィキ本文に一切なし**。open-weight 競争軸（`entities/martin-alderson` の "Summer of Open Weights"、subprime データセンター論）にも直結。
- NJスコア 4/5（Trend Surfing + In-Group + Pattern Interrupt: Meta が frontier 開放側へ）。
- ext: https://research.meta.ai/blog/muse-spark-open ｜ Together: https://www.together.ai/blog/meta-muse-spark-open（raw: `wiki/raw/articles/together.ai--blog-meta-muse-spark-open--b5154a4c.md`）｜ hn: https://news.ycombinator.com/item?id=50107379

### 2. 「ニューラルネットはクリーンだ」— 解釈可能性の立場転換（Goodfire）
- HN **719pts/272c**（10-15）。Goodfire の mechanistic interpretability 主張。特徴的方向性が重なり合う「ポリティカル・コンパス空間」モデルから、**単一特徴が意味単位で立ち上がる「dictionary（辞書）」構造**へ、解釈可能性の前提自体を張り替える論。
- 既存 `entities/goodfire-ai`（スキャフトン的短さ）と `concepts/mechanistic-interpretability`（→ interpretability リダイレクト）に直結する重要論点だが、本文はほぼ白紙。**ハブ書き起こしに値する**。NJスコア 3/5（Contrarian Insight + In-Group Signal）。
- ext: https://already-clean.goodfire.com/ ｜ hn: https://news.ycombinator.com/item?id=50105647

### 3. AIエージェント「暴走」報道は封じ込め・監視の不備が原因 — 今週最大の論争が継続中
- HN **943pts/614c**（10-14、急上昇）。CSO Online。最近の「AI がハッキングを仕掛けた」報道はエージェントの rogue 化ではなく **containment／monitoring の実装サボり**が原因だとする専門家反論。
- **昨日(10-15)レポートで最重要扱いしたが、今朝の sibling pipeline でもウィキ本文は未更新**（`concepts/security-and-governance/agent-containment`, `concepts/rogue-ai-agent-activity`, `concepts/frontier-rl-safety-cases` いずれも本論点未収録）。反論軸として追記すべき筆頭。
- 同時進行の法的論点「Why aren't AI companies being charged for hacking?」（mortoray, 336pts/372c, hn 50057278）。NJスコア 4/5。
- ext: https://www.csoonline.com/article/4234854/ai-agents-arent-going-rogue-frontier-labs-are-skipping-security-basics.html ｜ hn: https://news.ycombinator.com/item?id=50091788

### 4. LFM2.5-24B-A2B — on-device エージェント用 MoE（今朝 active-crawl が処理済み ✅）
- HN **286pts/79c**（10-14）。Liquid AI の 24B総量/2B active 疎推論モデル。Qwen3.6-35B-A3B より約50%小さい参数で agentic ベンチ 5/8 にて互角以上、M5 Max で 184 tok/s。teacher specialization 中の reward hacking（git history / PyPI を覗く）観察も記録。
- **今朝の active-crawl commit `2bc20991` が `entities/liquid-ai-lfm2-5-24b-a2b.md` として新設済み**。レポート上は ✅ 済み。
- ext: https://www.liquid.ai/blog/lfm2-5-24b-a2b ｜ hn: https://news.ycombinator.com/item?id=50097369

### 5. AIコーディングエージェントは「コードを増やすがソフトウェアは増やさない」— code-review ボトルネック研究（今朝処理済み ✅）
- HN **364pts/310c**（10-12）。Ars Technica。Harvard の Chen & Stratton による Jellyfish 解析（700社・70万人超・2021〜2026/3、3億 work event）。AI 導入後 **LOC +30% / commit +20% / PR +23%**、しかし **ソフト出力も雇用減もほぼ無し** — ゲインは人間のリビュー工程に吸収される。「Quantity, not quality」。
- **今朝の active-crawl commit `2bc20991` がこの論点を処理済み**（"code-review bottleneck"）。関連 hub: `concepts/ai-coding-effectiveness-debate`, `concepts/dark-factory-software-factory`。
- ext: https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/ ｜ hn: https://news.ycombinator.com/item?id=50059523

### 6. Codex CLI がデフォルトで永続・自己更新バックグラウンドデーモンを同梱（問題化）
- HN **607pts/292c**（10-12、継続）。OpenAI Codex GitHub issue #48195。coding agent の既定挙動として「常駐・自動更新の裏プロセス」を入れることへの同意性／supply-chain 批判。
- 昨日レポートでも挙がったが **ウィキ本文は未収録**。`concepts/codex/codex-safety`・`concepts/codex/codex-harness-controls`・`entities/codex` へ追記候補。NJスコア 3/5（In-Group + Pattern Interrupt）。
- ext: https://github.com/openai/codex/issues/48195 ｜ hn: https://news.ycombinator.com/item?id=50060694

### 7. HTTP ヘッダ経由の prompt injection — 2.17億レスポンスの実測調査
- HN **89pts/17c**（10-15）。Signals Corps。既知の「プロンプト内注入」ではなく **HTTP レスポンスヘッダ**を注入面として実測（217M web responses）。agent が web を読む以上、ヘッダは信頼境界の外 — インフラ層の注入面として新論点。
- 既存 `concepts/prompt-injection`（既成 hub）／`concepts/security-and-governance/agent-containment` へ追記で足りる。NJスコア 3/5（In-Group + Contrarian）。低 pts だが core interest 直撃。
- ext: https://www.signalscorps.com/blog/prompt-injection-in-http-headers/ ｜ hn: https://news.ycombinator.com/item?id=50104310

### 8. AI データセンター債務の証券化／業界懐疑論の高まり（misc・記録中心）
- 「Banks are now trying to offload the AI data center debt they just underwrote」**378pts/275c**（10-14）— 既存 `concepts/subprime-data-center-crisis`（Ed Zitron 系）の実証続報。追記候補。hn 50092664
- 「Why We're Banning AI」（Current Affairs）**244pts/189c**（10-15、編集方針として AI 投稿禁止を宣言）hn 50108131 ／ 「Has AI tells」**137pts**（AI 検出の非信頼性）hn 50090799 ／ 「AI was great until it was not」**119pts** hn 50100791 — 反 AI 世論クラスタ、記録のみ。
- 「Simons Foundation $15M で数学者の AI 時代支援」**240pts/194c**（10-15）hn 50104654。技術外だが AI×科学研究の資金_flow 事例として隣接 hub の付記程度。

---

## 📊 ウィキ推奨アクション（priority 順）

| # | トピック | 新設/追記 | 対象ページ | 状態 |
|---|----------|-----------|-----------|------|
| 1 | Muse Spark Open 816B-A42B | 追記（家系 hub） | `entities/muse-spark` + `concepts/meta-muse-spark`（＋新イベントページ候補） | ⚠️ 未収録（raw は together/modal に保存済） |
| 2 | 「Neural networks are clean」解釈可能性 | 追記/新設 | `entities/goodfire-ai` + `concepts/mechanistic-interpretability`(→interpretability) | ⚠️ 未収録 |
| 3 | AI「暴走」=封じ込め不備論 | 追記 | `concepts/security-and-governance/agent-containment` + `concepts/rogue-ai-agent-activity` + `concepts/frontier-rl-safety-cases` | ⚠️ 未収録（連日 carry-over） |
| 4 | Codex CLI 常駐デーモン同意性 | 追記 | `concepts/codex/codex-safety` + `concepts/codex/codex-harness-controls` + `entities/codex` | ⚠️ 未収録（連日 carry-over） |
| 5 | HTTP ヘッダ prompt injection | 追記 | `concepts/prompt-injection` + `concepts/security-and-governance/agent-containment` | ⚠️ 未収録（新注入面） |
| 6 | データセンター債務の証券化 | 追記 | `concepts/subprime-data-center-crisis` | ⚠️ 実証続報として追記余地 |
| — | LFM2.5-24B-A2B | 新設済み | `entities/liquid-ai-lfm2-5-24b-a2b` | ✅ active-crawl `2bc20991` |
| — | code-review ボトルネック（more code not software） | 処理済み | `concepts/ai-coding-effectiveness-debate` 他 | ✅ active-crawl `2bc20991` |
| — | OpenAI 幹部会議室盗聴事件（652pts） | — | — | provenance bar で drop（技術トレンド外） |

---

COST_REPORT: job=trending-topics | report-only run — HN front-page + keyword scan, no wiki-body edits, 1 inbox report committed
