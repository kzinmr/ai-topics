# Daily RSS Scan & Trending Topics — 2026-10-22

> 実行: 2026-10-22 12:00 UTC（trending-topics）
> blog_ingest run_id: `20261022T100019Z` / newsletter run_id: `20261022T101115Z`
> スキャン: 新規発見 50 件 / スクレイプ保存 20 件 / ニュースレター 4 件（4 high）
> 補完: HN Algolia front-page + keyword scan（2日窓・≥20pt）

---

## 1. 本日のトップテーマ（Newsjacking スコア付き）

| # | テーマ | NJ | 出所 | 収録状況 |
|---|--------|----|------|----------|
| 1 | **LiteLLM 1.107.0 が PyPI でサプライチェーン攻撃**（認証情報ストラー+RCEビーコン） | 5/5 | SafeDep / HN 540p | ✅ 新規収録 |
| 2 | **Anthropic「Claude Duet」— 能動的パーソナルエージェント**（Opus 5.5） | 4/5 | claude.com / HN 427p | ✅ anthropic.md に追記 |
| 3 | **PHP2Shell — OpenAI "Patch the Planet" が発見側の片割れ** | 4/5 | AINews / Wiz / HN 442p | ✅ 既存イベントページ + openai.md 更新 |
| 4 | **OpenAI 公式 CLI 公開 + OpenAI モデルが Google Cloud に** | 3/5 | GitHub / OpenAI / HN 147p・301p | ✅ openai.md に追記 |
| 5 | **OpenAI×PerturbAI×Scripps — 数千エージェントで脳細胞データを32分で解釈** | 4/5 | openai.com / HN 146p | ✅ openai.md に追記 |
| 6 | **eMudhra CA 鍵漏洩（mitmproxy が `--emudhra` 追加）** | 3/5 | HN 517p / johndcook / simonwillison | ⚠️ 未収録（候補） |
| 7 | **Peec — 架空統計5万件で ChatGPT に引用させる GEO 実験** | 5/5 | peec.ai / HN 363p | ⚠️ 未収録（候補・raw は保存済み） |
| 8 | **Anthropic 上半期純損失 800億ドル超（WSJ / S-1）** | 4/5 | Reuters・WSJ / HN 187p | ⚠️ 未収録（候補・fetch 401） |

### NJスコアの内訳（上位3件）

- **LiteLLM**: Trend Surfing（PHP2Shell でセキュリティ週間）+ Pattern Interrupt（"ゲートウェイ自体が攻撃経路になった"）+ In-Group Signal（agentic stack 全員の共通基盤）+ Contrarian（"リポジトリを見ても検知できない"）= 5/5
- **Claude Duet**: Trend Surfing（能動的エージェント競走）+ Polarizing Promise（"朝1回のブリーフ以外黙っている"＝チャットループ否定）+ In-Group（harness / human-in-the-loop 設計論）= 4/5
- **Peec 架空統計**: Pattern Interrupt（自社で5万個の嘘データを撒く実験）+ Contrarian Insight（"Google は削除、ChatGPT は引用し続ける"）+ In-Group（GEO/SEO 業界）+ Polarizing = 5/5

---

## 2. RSS スキャン結果（blog_ingest 2026-10-22 10:00 UTC）

新規発見 50 件 → スクレイプ保存 20 件。本日分は AI 直接テーマは薄め、セキュリティ／レガシー computing 寄りの日。

### AI/セキュリティ関連（有効）

| ソース | タイトル | NJ | アクション | 対象 |
|--------|----------|----|------------|------|
| safedep.io (HN補完) | Compromised LiteLLM 1.107.0 on PyPI | 5/5 | エンティティ+イベント新規 | `entities/litellm.md`, `events/2026-10-21-litellm-pypi-compromise.md` |
| claude.com (HN補完) | Claude Duet | 4/5 | 追記 | `entities/anthropic.md` |
| github.com/openai/openai-cli (HN補完) | OpenAI CLI | 3/5 | 追記 | `entities/openai.md` |
| openai.com (HN補完) | OpenAI models on Google Cloud | 3/5 | 追記 | `entities/openai.md` |
| openai.com | Scaling AI research for complex biological data | 4/5 | 追記（raw は 11:03 保存済み） | `entities/openai.md` |
| krebsonsecurity.com | Widespread PHP Flaw May Cause Many Site Outages Today | 2/5 | スキップ（PHP2Shell 既存収録で十分） | — |
| jeffgeerling.com | Upgrade PHP immediately for php2shell | 1/5 | スキップ（同上） | — |
| simonwillison.net | Today's PHP Security Release | 2/5 | スキップ（PHP2Shell 収録済み・運営対応寄り） | — |
| simonwillison.net | sparqlite: SPARQL 1.1 inside SQLite in Rust | 2/5 | 低優先（Rust+DB、AI周辺外） | — |
| pluralistic.net | Adversarial interoperability is a team sport | 2/5 | 低優先（AI文脈は副次的） | — |
| nesbitt.io | Trust Stores Are Dependencies Too | 3/5 | 候補（CA/信頼ストア＝依存、eMudhra と対で収録推奨） | `concepts/ai-supply-chain-security.md`（次回） |
| johndcook.com | Backdoors, Incompetence, and Elliptic Curves | 2/5 | 候補（eMudhra/暗号バックドア文脈） | — |
| idiallo.com | Can they write a function? | 2/5 | 候補（AI採用面接/評価） | — |
| peec.ai | Publish fake stats, get cited | 5/5 | raw 保存済み・ページ未作成（次回の最優先候補） | `concepts/llm-citation-seeding.md`（提案） |
| harness-engineering-101 (GitHub) | "The LLM is the brain. The harness is the body." 16章 | 3/5 | raw 保存済み・候補 | `concepts/harness-engineering/` 配下 |
| layerfs.ai | LayerFS — filesystem for AI coding agents | 3/5 | raw 保存済み・候補 | `concepts/`（ephemeral workspace / agent FS） |
| github.com/omnara-ai/omnara | オープンソース managed agent platform | 3/5 | raw 保存済み・候補 | `concepts/managed-agents.md` 更新候補 |
| heymaxwell.ai | doubleAI Maxwell — "first Code Execution Model" | 3/5 | raw 保存済み・候補（ベンチは自社公表値に注意） | — |

### 非AI（スキップ）

xeiaso.net CVE シットポスト 5 件（`data = "cook"` とは無関係の風刺シリーズ）、johndcook "Deliberate imperfection"、dfarq（Creative Computing 1974）、Raymond Chen 2 件（COM unmarshal / Microspeak）、daringfireball "The iPhone Duo"、jim-nielsen（retirement/utopia）。ElevenLabs・Harvey・Fireworks・Glean・Parallel のベンドー側投稿はいずれもプロダクト告知で収録基準未満。

### 失敗・注意

- `openai.com/index/openai-models-google-cloud/` → **403**（本文未取得。HN+見出しで判断、本文は未取得である旨をページに明記）
- Reuters（Anthropic $80B loss）→ **401**（取得不能。WSJ 原典も有料。ページ化見送り）
- Reddit（r/LocalLLaMA 系）は本日チェック対象外（429 リスク回避のため再試行しない運用）

---

## 3. ニュースレター（4件・すべて high）

| 配信 | 件名 | NJ | 状態 |
|------|------|----|------|
| swyx / Latent Space | Claude Mods: Flipping the Harness Inside Out | 4/5 | triage 済み・`concepts/harness-engineering` 系で未反映（次回） |
| SemiAnalysis | The Huawei-DeepSeek Symbiosis | 4/5 | triage 済み・paid body 未取得（課金記事） |
| beehiiv 系 | Nvidia Pitches Europe an AI Factory-in-a-Box | 3/5 | triage 済み・beehiiv 403 で本文未取得 |
| swyx / AI News | OpenAI's Patch the Planet is 1 of 2 parties to discover PHP2Shell | 4/5 | ✅ 本日の openai.md 更新で吸収 |

`newsletter-triage` 判定（`wiki/raw/inbox/newsletter-ingest/20261022T101115Z.json`）: critical 0 / high 4 / low 0。
SemiAnalysis は過去パターンどおり paid body 未取得、beehiiv は 1リンク解決テスト後に batch 403 を確認済みのため、本文なしでタイトル判断に留めた。

---

## 4. HN 補完スキャン（2日窓・front page + AI keyword）

front_page タグだけでは AI ストーリーが薄く、keyword クエリ（AI / LLM / Claude / OpenAI / Anthropic / Gemini / model / agent）で補完した。取得済み HN item ID はすべてページ内 `sources` に使用。

**高ポイント（セキュリティ密集週）**

- 756p — Today's PHP security release（[item/50182987](https://news.ycombinator.com/item?id=50182987)）
- 540p — **Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor**（[item/50181114](https://news.ycombinator.com/item?id=50181114)）← 本日収録
- 517p — mitmproxy adds `--emudhra` option（[item/50189232](https://news.ycombinator.com/item?id=50189232)）
- 490p — Railway Security Disclosure（[item/50188228](https://news.ycombinator.com/item?id=50188228)）
- 442p — PHP2Shell: AI uncovers critical RCE in PHP（[item/50180836](https://news.ycombinator.com/item?id=50180836)）← 昨日収録済み
- 368p — PingCap TiDB Leaks（[item/50173716](https://news.ycombinator.com/item?id=50173716)）
- 363p — GitLab critical patch release（[item/50185869](https://news.ycombinator.com/item?id=50185869)）
- 173p — CVE-2026-111943: Compromised Intermediate Certificate Authority（[item/50192900](https://news.ycombinator.com/item?id=50192900)）

→ **所見**: 10/19–10/22 は「PHP core / PyPI / CA鍵 / GitLab / Railway / TiDB」と脆弱性とサプライチェーンが全面に出た1週間。PHP2Shell（AI 発見）と LiteLLM（AI 基盤の被攻撃）が対になっており、`concepts/autonomous-security-agents` と `concepts/ai-supply-chain-security` の交点として週次ダイジェストの柱にすべき。

**AI 製品・発表**

- 427p — Claude Duet（[item/50186037](https://news.ycombinator.com/item?id=50186037)）← 本日収録
- 301p — OpenAI models are coming to Google Cloud（[item/50180079](https://news.ycombinator.com/item?id=50180079)）← 本日収録
- 283p — WorldTUI: trained a 360M model to pretend to be a terminal（[item/50190363](https://news.ycombinator.com/item?id=50190363)）— Qwen2.5-Coder-0.5B fine-tune、画面グリッドを token 化、エラー自己修復と行並列デコードが効いた要点。`concepts/world-models-for-agents` 更新候補
- 147p — OpenAI CLI（[item/50191507](https://news.ycombinator.com/item?id=50191507)）← 本日収録
- 146p — Using thousands of AI agents on biological data（[item/50180752](https://news.ycombinator.com/item?id=50180752)）← 本日収録
- 132p — Using Claude to reduce the attack surface of code（[item/50175779](https://news.ycombinator.com/item?id=50175779)）— 昨日収録済み
- 117p — Claude designed protein binders against scorpion neurotoxins（[item/50170021](https://news.ycombinator.com/item?id=50170021)）— 未収録候補（AI in science）
- 54p — Claude Now Works with Google Docs, Sheets, Slides（[item/50190357](https://news.ycombinator.com/item?id=50190357)）
- 25p — Gemini 4 Argon now available for everyone（[item/50168983](https://news.ycombinator.com/item?id=50168983)）— 既存リリースページで網羅済み

**業界・社会**

- 187p — Anthropic net loss >$80B in H1 2026（WSJ）（[item/50171966](https://news.ycombinator.com/item?id=50171966)）— ⚠️ 未収録（一次ソース 401。Ed Zitron / AI economics の文脈で次回）
- 124p — Google staff resign in backlash over AI contracts with military（[item/50186043](https://news.ycombinator.com/item?id=50186043)）— 本文取得済み、`concepts/ai-military` 更新候補
- 183p — Steam Users Beg for "No AI" Filter as Vibecoders Flood Next Fest（[item/50168190](https://news.ycombinator.com/item?id=50168190)）— ai-slop 論の具体例、候補
- 116p — Using LLM for confidence scoring is a bad idea（[item/50176082](https://news.ycombinator.com/item?id=50176082)）— 評価・校正論として候補
- 48p — Benchmarking Bot Detection Against Modern AI Agents in 2026（[item/50169506](https://news.ycombinator.com/item?id=50169506)）

---

## 5. 次回のインジェスト候補（優先順）

1. **Peec 架空統計 → LLM 引用汚染**（raw 保存済み / NJ 5/5）— `concepts/llm-citation-seeding.md` 新規（タグ `llm-citation-seeding` は SCHEMA 追加済み）。GEO/SEO・relevance engineering・AI slop の交点で本 wiki 中核。
2. **eMudhra CA 鍵漏洩 + mitmproxy `--emudhra` + nesbitt "Trust Stores Are Dependencies Too"**（3記事・タグ `trust-store`/`certificate-authority` 追加済み）— 単一の CA/信頼ストア・イベントに統合するのが正しい。
3. **harness-engineering-101（16章本）** — `concepts/harness-engineering/` のハブから参照される入門テキストとして収録。
4. **LayerFS / Omnara** — ephemeral workspace filesystem と OSS managed agent platform。いずれも coding agent 基盤。
5. **Anthropic H1-2026 純損失 800億ドル / S-1** — 一次ソース（WSJ）有料のため取得経路を確認してから。Ed Zitron の "Concentration Risk" 記述と接続。
6. **WorldTUI** — `concepts/world-models-for-agents` の実践例セクションに追記。
7. **Google 社員の軍事契約への辞職 protest** — `concepts/ai-military` / `concepts/security-and-governance/ai-safety-military-governance-claude` と対応づける。
8. **swyx "Claude Mods: Flipping the Harness Inside Out"** — harness を内側から裏返す主張。`concepts/agent-harnesses` / `concepts/harness-commoditization` と接続。

---

## 6. 変更ファイル

- 新規: `entities/litellm.md`, `events/2026-10-21-litellm-pypi-compromise.md`
- 更新: `concepts/ai-supply-chain-security.md`, `comparisons/llm-gateways.md`, `entities/anthropic.md`, `entities/openai.md`, `SCHEMA.md`, `index.md`, `log.md`
- raw 新規: `2026-10-22_safedep-litellm-1.107.0-pypi-compromise.md`, `2026-10-22_anthropic-claude-duet-launch.md`, `2026-10-22_openai-cli-official.md`
- index: ページ数 3284 → 3286、Events 40 → 41
