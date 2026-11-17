# Trending Topics Report — 2026-11-17 (12:00 UTC)

> 対象: 過去24〜48時間の HN / RSS / ニュースレター。front_page タグは減衰済みのためキーワード検索＋ポイントスイープ併用。
> 本日の sibling ジョブ（blog-ingest / newsletter-ingest / active-crawl / hot-post）が大部分を既に wiki 化済み。以下は統合サマリ。

## 🏆 トップ トピック

### 1. Claude Mythos、AMD GPU オンボーディングを約3日に短縮 — CUDA の堀が侵食か（新規収録 ✅）
Anthropic が IPO 投資家に説明したところによると、Claude Mythos Preview が AMD MI355X 上のモデル稼働に必要なカーネルの「ほぼ100%」を人間の介入なしで記述、従来6〜12ヶ月かかっていた作業が約3日に。Tom Brown は「数十人のエンジニア」チームとの比較を提示。AMD側も「Claude は HIPify より優れた変換ツール」と公言済み。
- HN の懐疑: IPO 直前・Nvidia 不安局面での「都合のよい発表」論、パブリックモデルではカーネル開発が禁止トピックである非対称性（_lab と巨大企業だけが使える）、CUDA の20年の重力は消えない、という反論。
- 収録: `concepts/cuda-moat.md` に新セクション、raw: `raw/articles/2026-11-17_tomshardware_claude-mythos-amd-gpu-onboarding.md`
- [HN 50526264](https://news.ycombinator.com/item?id=50526264) / [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat)

### 2. Qwen4-Max 公開、ベンチは期待外れ（✅ 済み — concepts/qwen-4-max.md）
11/16 に Alibaba がフラッグシップ Qwen4-Max をリリース（HN 594pts/250c）。公式ブログが CSR で取得不能なため community-reported 扱い。午前 pipeline が `concepts/qwen-4-max.md` + `entities/qwen.md` に収録済み。newsletter triage でも critical 判定。

### 3. OpenCode Browse — エージェントが「本物のローカルブラウザ」を操る（新規収録 ✅、281pts）
Chrome/Edge/Brave/Arc など実ブラウザを MCP 経由で制御。Playwright MCP との重複、接続の不安定さ（browse pair 再実行問題）、週3本ペースの雑なリリースとセキュリティ軽視という常連批判がコメント欄に。エージェントに専属ブラウザを持たせるべき、という意見も。
- 収録: `entities/opencode.md` に新セクション、raw: `raw/articles/2026-11-17_opencode_opencode-browse.md`
- [HN 50523459](https://news.ycombinator.com/item?id=50523459)

### 4. Windows 11 がコーディングエージェント/開発ツールの利用を実際に telemetry 収集（✅ 済み — active-crawl 収録）
xusheng.dev の調査（HN 634pts/488c）が本物だと確認され Microsoft が認める展開。active-crawl が `raw/articles/2026-11-16_xusheng_windows-coding-agent-telemetry.md` として収録済み。

### 5. FBI、OSS の AI 攻撃ツール「Artex」が3時間未満でネットワーク侵入に使用されたと警告
TechCrunch 報道（HN 46pts）。GitGuardian によればフォーク120超・同種ツール群40ファミリー以上。「ガードレールの弱いモデルに "go hack it" と言うだけで RCE を含む15脆弱見つかった」というコメントも——ツールよりモデル自体がボトルネック解除された、という論点。未収録（小トピックとして追跡）。
- [HN 50520796](https://news.ycombinator.com/item?id=50520796)

### 6. OpenAI「embedded assessments」第1フェーズ — 安全性評価の外部委託モデル
自社モデルの安全性評価を外部（政府・学術含む）に開放する枠組み。HN では「Hugging Face インシデント後の safetyism 化」「Anthropic との逆転現象」の議論。元記事は 403 で本文未取得（HN ツリーから要旨取得）。
- [HN 50519153](https://news.ycombinator.com/item?id=50519153)

### 7. Claude Code チームの「検証」論 — コードの90%を Claude が書き、レビューも自動化（42pts、claude.dev 公式）
「誰も全変更は読めないから、失敗を人の審査の基準にする」「flaky テストは sleep/retry 禁止、原因が特定できなければ削除して理由を書く」。コメント欄は「$2k/月で数エージェントが限界なのに何十並列も無理」「プロトタイピングには最適だが平文コードで焼く必要がある」とコスト論に集中。午前 hot-post の Anthropic dreaming 記事（13%→48%）と対で読むと面白い。未収録（候補）。
- [HN 50529612](https://news.ycombinator.com/item?id=50529612)

### 8. 「Who is Hiring?」が12年ぶりの低水準 — AI 求人占比50%超（94pts）
hntrends.com の集計。ただしコメント欄は「2022年の利上げと Section 174 の方が説明力がある」「HN への投稿数=市場ではない」とモティブ reasoning 批判が強く、楽観/悲観両論入り混じる。統計の読み方に注意。未収録（追跡候補）。
- [HN 50512950](https://news.ycombinator.com/item?id=50512950)

## 📰 本日の sibling job カバレッジ
- blog-ingest: geohot「My Empire of Dirt」singularity 怒涛、dwarkesh × Paul Christiano（12ヶ月以内の takeover 論）、micahflee オープンウェイト私密ガイド、llm 0.37.3、Gary Marcus ×2、dragas、Apple macOS 27.3 全ディスクアクセス問題
- newsletter: Import AI 481（critical）、Qwen4-Max 落胆（critical）、How I AI Fable 5.2 レビュー（high）、Claude Sheets（high）
- active-crawl: エージェント credential leasing、Windows telemetry、ソフトの崩壊 system論、ChatGPT Wallet、JEPA/LeWM

## 📊 ウィキ推奨アクション
| トピック | 状態 | 対象 |
|---|---|---|
| Claude Mythos / AMD / CUDA moat | ✅ 済み — concepts/cuda-moat.md（本日） | 新規セクション |
| OpenCode Browse | ✅ 済み — entities/opencode.md（本日） | 新セクション |
| Qwen4-Max | ✅ 済み — concepts/qwen-4-max.md | 確認のみ |
| Windows エージェント telemetry 収集 | ✅ 済み — active-crawl raw | 概念ページ化は次ラン候補 |
| Artex AI 攻撃ツール | ⚠️ 未収録 | concepts/ai-agent-safety-incidents.md に追記候補 |
| Claude Code 検証論 | ⚠️ 未収録 | concepts/coding-agents/ 配下が候補 |
| Fed・AI エージェントによるバンクラン（26pts） | ⚠️ 低優先 | スキップ |

## 備考
- OpenAI 公式 2 本（embedded assessments / child safety）は 403、TechCrunch 1 本は 404 — HN ツリーから要旨取得済み。
- Import AI 481 / dwarkesh × Paul Christiano 回などは午前 pipeline が処理済み、重複作成せず。
