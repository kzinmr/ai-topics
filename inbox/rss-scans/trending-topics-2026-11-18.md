# Trending Topics — 2026-11-18 (12:00 UTC)

スキャン: HN Algolia front page + keyword（2日窓、≥20pt）+ 一次ソース9件フェッチ（8/9 OK）・コメントツリー10件。同日の blog-ingest / newsletter-ingest / active-crawl が処理済みのテーマは除外し、未収録テーマを wiki 化しました。

## 🏆 トップテーマ

### 1. Microsoft ONNX Runtime が GitHub から突然消滅（HN 350pt）⭐新規ページ化
`github.com/microsoft/onnxruntime` が事前告知なく 404。説明なし・退避Noticeなし。Phrack 73 の ORT パーサ欠陥記事（任意ファイルパス読み出し）や agent-framework PyPI 侵害が候補説明として浮上（未確認）。Intel フォークと SourceForge ミラーが一夜で生命线になり、「消えたリポジトリのミラーはマルウェア確率高」という一次被害も発生。
→ NEW `concepts/open-source-project-sudden-disappearance.md`（「障害中の一時的リポジトリステート」という OSS 運用規範の欠如を指摘）
→ 併記: `concepts/windows-coding-agent-telemetry.md` / `concepts/open-source-ai-destruction.md` に同一週の信頼崩壊クラスタ追記
HN: https://news.ycombinator.com/item?id=50539610

### 2. Java4Shell — OpenJDK Base64 デコーダのメモリ破損 RCE（HN 983pt）raw保存
Calif Research が CVE-2026-114938 を公開（CVSS 9.2）。AVX-512 VBMI 命令を使った高速 Base64 デコードの手書きアセンブリにバグ。`A×64 + =` だけでヒープ上書き、Heartbleed 型のメモリ読出し → 認証前 RCE。Keycloak / Jira / Confluence / Jenkins / PingFederate で pre-auth RCE を実証。回避は `-XX:UseAVX=2`（AVX-512 無効化）。PHP2Shell に続く「AI エージェントによるクラシック基盤バグ発見」シリーズ。
→ raw: `raw/articles/2026-11-18_calif_java4shell-openjdk-base64-rce.md`（クラスタページ化候補）
HN: https://news.ycombinator.com/item?id=50538240

### 3. Google AI Overviews で外部クリック 40%減 — ランダム化実験（HN 459pt）既存ページ追記
DataForSEO 2000万キーワードで Overview 表示率は 5.93%→61.43%（2年で）。Overview を一部ユーザーに非表示にする対照実験で外部サイトへのクリックが約40%減。GEO（生成エンジン最適化）に損失補填のエビデンスはなく、AI アシスタント経由流入は全体の 0.3%。個人サイト側の実例として All About Berlin（HN 429pt）の -75% が同日同時代で共鳴。
→ APPEND `concepts/ai-search-visibility.md`（需要側の定量データ）
HN: https://news.ycombinator.com/item?id=50540178 / https://news.ycombinator.com/item?id=50542705

### 4. Anthropic × METR「規制俘獲」告発スレッド（HN 140pt）⭐新規ページ化
投資家 Kevin Bass が「Anthropic は METR を評価系の経済的依存で俘獲した」と告発。HN は「終末カルトの IPO」派と「単純化しすぎ」派に割れ、「信じているが不可避と考える→儲けるだけ儲ける」という最も皮肉な解釈が上位。単発 X スレッドなので confidence: low、構造的関心として記録。
→ NEW `concepts/anthropic-metr-regulatory-capture.md`
HN: https://news.ycombinator.com/item?id=50530450

### 5. Claude はタンパク質配列で大規模学習している（HN 72pt）人物ページ追記
Xinming Tu らが「無名の細菌/古細菌タンパク質668個の次アミノ酸予測」で学習データ由来の知識を検出。Fable 5.2 はオープン系タンパク質 LM を全勝、Opus 5.5 は ProtGPT3-10B と同等。シャッフル制御で崩れる＝論文経由ではない。11/18 追補: 学習カットオフ後公開のタンパク質も予測、GPT-6.2 勢は痕跡なし。
→ APPEND `entities/xinming-tu.md`
HN: https://news.ycombinator.com/item?id=50541619

### 6. FrontierHarness Eval v1.1 — モデルごとに最適なハーネスが違う（HN 385pt）raw保存
Runta×Baseten、22ハーネス × 5モデル × 62タスク × 4試行 = 27,280ラン・83Bトークン。pass率/コストでモデルごとに最適ハーネスが異なり（Codex CLI は GLM-5.3 で1位 → Kimi-K3 で16位）、1モデルに複数ハーネス固定は損。創業者コメントが HN の AI 文房フラグで検証済み。ベンダー運営ランタイム上のベンチマークである点は留保。
→ raw: `raw/articles/2026-11-18_runta_frontierharness-eval-v1-1.md`
HN: https://news.ycombinator.com/item?id=50532191

### 7. Gemini 4 Carbon の遅さ問題（HN 126pt）既存ページ追記
kernel.dev が社内 eval で「Opus/Astra なら数分のタスクに Carbon は1時間近く」と報告。補助率（Opus 40x に対し Carbon 3x）も表で提示。「ベンチマーク最適化特化説」に拡散。
→ APPEND `concepts/gemini/gemini-4-carbon.md`
HN: https://news.ycombinator.com/item?id=50541790

### 8. Windows コーディングエージェントテレメトリ（HN 723pt・昨日の主役）— 関連付けのみ
MissionControlAggregator のエージェント名一致ログ問題は昨日収録済み（`concepts/windows-coding-agent-telemetry.md`）。今日は ONNX 消滅・Optimizely 供給網攻撃と「同一週の信頼崩壊クラスタ」として相互リンク追記。

## 📊 ウィキ推奨アクション

| # | テーマ | 状態 | 対象 |
|---|--------|------|------|
| 1 | ONNX Runtime 消滅 | ✅ 済み（新規） | concepts/open-source-project-sudden-disappearance.md |
| 2 | Java4Shell | ⚠️ raw保存のみ — 「centaur hacker」クラスタページ候補 | raw/articles/2026-11-18_calif_... |
| 3 | AI Overviews 40%減 | ✅ 済み（追記） | concepts/ai-search-visibility.md |
| 4 | Anthropic-METR 俘獲 | ✅ 済み（新規・low confidence） | concepts/anthropic-metr-regulatory-capture.md |
| 5 | Claude タンパク質学習 | ✅ 済み（追記） | entities/xinming-tu.md |
| 6 | FrontierHarness v1.1 | ⚠️ raw保存のみ — harness 評価ページ群と統合候補 | raw/articles/2026-11-18_runta_... |
| 7 | Gemini 4 Carbon 遅延 | ✅ 済み（追記） | concepts/gemini/gemini-4-carbon.md |
| 8 | Windows エージェントテレメトリ | ✅ 済み（昨日）＋クラスタ相互リンク | concepts/windows-coding-agent-telemetry.md |

## その他スキャン所感
- Bank CEOs/NSA が議会証言で「AI 駆動パッチが障害の一因」（Washington Sun, HN 79pt）— Marcus の「インフラ溶解」論と同系列。raw 取得済み、次ランで systemic-software-breakdown 統合候補。
- Baidu/Xiaomi CEO が「AI の熱狂とリターンの乖離」を公開警告（SCMP, 189pt）— ai-bubble 系ページに追記候補。
- 「Fed、AI エージェントのバンクラッシュ 誘発を懸念」（Gizmodo, 27pt）— agentic-commerce 側で後追い要。
- 未フェッチ: reuters/FT 系（Nvidia シンガポール販売非開示 570pt）はゲートクラス。FT 記事はシンガポール経由のチャネルサンギング疑惑 — NVIDIA バブル頁（events/nvidia-ceo-transition-2026 の Zitron 節）と統合候補。

COST_REPORT: job=trending-topics | see below
