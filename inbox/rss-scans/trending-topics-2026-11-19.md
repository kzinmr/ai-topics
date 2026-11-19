# Trending Topics 2026-11-19 (12:00 UTC)

本日の HN 急上昇＋キーワードスキャンから、AI/LLM 関連の重要トピックを 8 件抽出。朝の兄弟ジョブ（active-crawl / hot-post / blog・newsletter ingest）が既に収録済みのものは既収録として相互リンクし、未収録の高信号トピックのみ新規ページ化・追記した。

## トップ 8 トピック

### 1. Gemini 4 Neon 公開（HN 866pt）→ 新規ページ
Google DeepMind が 11/18 に Gemini 4 ラインナップの高速・低価格帯 **Neon** を公開。Artificial Analysis Intelligence Index で **#3（スコア61、xhigh）**、Vals Index #2（70.9%）、Legal Research Bench / Tax Agent Bench / AutomationBench / Vending-Bench 2 で #1、Arena Agent Arena で #2（1336）。価格は **$3 / $15 per 1M**（キャッシュ入力 $0.15＝95% 割引）、**1M トークンコンテキスト**。サードパーティの micjm は OpenRouter 実測 **127 tok/s（Carbon の 46 tok/s 比）** から Agent Duel Elo を約 1,066 と試算し、Opus 5.5（1,078）に肉薄と予測。HN では命名の分かりにくさと Antigravity のアクセス権（学生/$20 プランで使えない）への不満が噴出。
→ NEW `concepts/gemini/gemini-4-neon.md` ＋ `concepts/gemini/index.md` 追記
HN: https://news.ycombinator.com/item?id=50552424

### 2. NGINX HTTP/2 で未認証 RCE（HN 1412pt・本日最大）→ 新規ページ
Wiz Research が **NGINX 自体**の 2 つのクリティカル RCE（CVE-2026-123633 / CVE-2026-123007、CVSS 4.0 9.2）を公開。全世界 2.25 億超サイトの「正面扉」を担う OSS で、アプリ側が安全でも HTTP/2 有効なら被弾しうる。CVE-2026-123007 は 2015 年の 1.9.5 まで遡及。Wiz / Ikotas / Metnir / Rapid7 / Xint の **5 チームが独立に発見**（「バグ衝突の記録では」と HN）。F5 に報告済み、パッチは開示 30 分以内に配布。スレッドは AI 支援脆弱性発見の加速（Java4Shell / Ruby2Shell と同週）と「C で人間の記述はもはや保たない」議論に接続。
→ NEW `concepts/nginx-http2-rce.md`（systemic-software-breakdown / ai-vulnerability-discovery と相互リンク）
HN: https://news.ycombinator.com/item?id=50547374

### 3. Microsoft Ignite 2026 — MAI 7 モデル一挙公開（HN 552pt）→ 既存追記
「エージェントを 24/7 回す」価格性能を掲げ 7 モデルをリリース（いずれもベンダー報告値）。MAI Cyber 2 Flash は CyberGym-E2E で GPT-6 Astra 超え・1 タスク 2% 未満、MAI Code 2 は GPT-6.1 Sol の 98% 品質・約 40% 価格（Opus 5.5 比 96%/5%）、MAI Image 2.7 は AA 画像編集 #1・1/5 価格、MAI Realtime 1 は $0.01/音声分、MAI Transcribe 2（Dragon Copilot で月 1,000 万件）、Decision 1.1 は GPT-6.1 Sol 比 50x 高速/79x 安価。第 2 世代アクセラレータ **Maia 200** も生産稼働（1.7x トークン）、自 Azure で動かせる **MAI Licensed Weights** も。HN は「数字はゲーム化」「オープンウェイト出さないと Windows Phone の二の舞」と評価割れ。
→ APPEND `concepts/microsoft-mai-models.md`
HN: https://news.ycombinator.com/item?id=50548021

### 4. KPMG UK — 100 体の AI エージェントが監査で人間より良い質問（HN 467pt）→ 未収録候補
FT 報道（Project Exponential）。無名の FTSE 250 企業の財務諸表を 100 超の AI エージェントが監査チームと並走し、所内で「人間監査チームより深く掘り、より良い質問をした」事例を確認（KPMG UK 監査責任者 Cath Burnet）。Big Four 監査のホワイトウォッシュ批判（Enron 等）や「AI は怠惰でないのが強み」「手続が固定された領域で AI は人間超え」という議論、韓国での AI 試験満点騒動まで拡散。
→ 候補: `concepts/` 新規（ai-audit / agentic-services 系ページ）。本日はレポートのみ。
HN: https://news.ycombinator.com/item?id=50547777

### 5. 「AI が All About Berlin を殺した」（HN 783pt）→ 関連既存あり・未収録候補
2017 年から運営されたベルリン移住ガイドサイトが **Google AI Overviews で 70–75% トラフィック減**。検索結果は広告 → AI 生成回答（自分のコンテンツで学習）→ 遅れて自分のリンク、という構造。2026 年 5 月の投稿の再浮上（HN でも「なぜ今」という声）。AI Overviews による創作者搾取の代表事例。
→ 既存 `concepts/google-ai-overviews-liability.md` / `concepts/ai-search-visibility.md` と統合候補。
HN: https://news.ycombinator.com/item?id=50542705

### 6. RadixArk の自社モデル DaisyRose-27B（HN 223pt）→ 既存追記
Qwen3.8-27B ベースに Miles で RL ポストトレーニング。**1,200 タスク・18 日・144 H200** という小規模計算で Terminal-Bench 4.1 pass@1 を **5.6% → 12.0%** に改善、全ベンチでベース超え。BF16/FP8/NVFP4 公開。SGLang + Miles スティックの実力証明。
→ APPEND `entities/radixark.md`
HN: https://news.ycombinator.com/item?id=50551046

### 7. Anthropic IPO 価格決定・安全性批判連合（HN 262pt / 134pt）→ 既存追記候補
11/18 に IPO 価格決定（前日のロードショー収録済み `events/anthropic-ipo-roadshow-2026.md`）。Amazon+Google が IPO 後 30% 弱を保有（TechCrunch）。並行して「Anthropic Is Not a Safe AI Company」と題した科学者・法学者・技術者の広範な連合が IPO 前に安全性ブランディングに異議を唱える声明。
→ `events/anthropic-ipo-roadshow-2026.md` 追記候補（次ラン）。
HN: https://news.ycombinator.com/item?id=50553843 / https://news.ycombinator.com/item?id=50548485

### 8. 各種（簡潔）
- **Ruby2Shell**（HN 179pt）: stock Rails の pre-auth RCE（1 バイトのヒープオーバーフロー、大文字化で 0x53 / 小文字化で 0x73 を出力バファ直後に書込）。PoC は 1 週間後に公開予定。Java4Shell / Nginx と並ぶ「centaur hacker」クラスタの一員 → `concepts/systemic-software-breakdown.md` 追記候補。https://news.ycombinator.com/item?id=50556287
- **DeepMind 社員がユニオン化**（HN 35pt, 新規）: gdmunion.co.uk。AI 大手の労働組合化の進展。
- **Genie 4 公開**（HN 265pt）: Google DeepMind のワールドモデルが一般利用可。
- **Black 高校生が AI 誤認（ドーナツ袋を銃と誤認）で提訴**（HN 98pt）: Lawyers' Committee。AI 誤認の法的帰結ケース。
- **Codex / LLM でコードレビューがボトルネック化**（Harvard, HN 321pt）: 収録済み `concepts/code-review-bottleneck.md` に追記候補。

## 📊 ウィキ推奨アクション

| # | テーマ | 状態 | 対象 |
|---|--------|------|------|
| 1 | Gemini 4 Neon | ✅ 済み（新規） | concepts/gemini/gemini-4-neon.md |
| 2 | NGINX HTTP/2 RCE | ✅ 済み（新規） | concepts/nginx-http2-rce.md |
| 3 | Microsoft MAI 7 モデル | ✅ 済み（追記） | concepts/microsoft-mai-models.md |
| 4 | KPMG AI 監査 | ⚠️ 未収録 — 新規 ai-audit ページ候補 | — |
| 5 | AI Overviews 殺し | ⚠️ 関連既存あり — 統合候補 | concepts/google-ai-overviews-liability.md |
| 6 | DaisyRose-27B | ✅ 済み（追記） | entities/radixark.md |
| 7 | Anthropic IPO 価格決定 | ⚠️ 既存追記候補 | events/anthropic-ipo-roadshow-2026.md |
| 8 | Ruby2Shell | ⚠️ systemic-software-breakdown 追記候補 | concepts/systemic-software-breakdown.md |

## その他スキャン所感
- 本日 AI 以外の大型は Deutsche Bank 内部告発（716pt）、Quad9 の仏 DNS 離脱（666pt）、Cambridge 辞書「human」を今年のことばに（283pt）— AI ウィキの範囲外につきスキャンのみ。
- MAI の「Decision 1.1」「gamed metrics」論争は、PostHog decision-model シリーズ（`concepts/decision-model-playbook.md`）と直結。次ランで相互リンクを検討。
- Gemini 4 ラインナップの XL/L/M/S 整理（HN WarmWash の整理表）は、`concepts/gemini/index.md` の常設セクション化に値する。

COST_REPORT: job=trending-topics | see below
