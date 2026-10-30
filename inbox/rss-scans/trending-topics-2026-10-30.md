# Trending Topics — 2026-10-30 (12:00 UTC)

HN Algolia（front page + キーワード）+ 朝パイプライン（blog-ingest 18件 / newsletter 4通: Ben's Bites・The Skip・Beehiiv回線・Irrational Analysis）+ web supplement。front_page タグは減衰済みのためキーワードブロックを主信号に採用。

## 🏆 トップトレンド

### 1. 公式 Claude Code VS Code 拡張機能が Cursor Marketplace でバックドア化（HN 131+98+21pts）🆕
Phorion が 10/30 開示。**公式 Claude Code for VS Code v2.1.313 が Cursor Marketplace 上で改ざんされ、macOS/Linux/Windows に SSH バックドアを持続インストール**（SSH鍵設置 + Remote Login 有効化 + ホスト情報ビーコン）。Cursor/NPM/VSCode レジストリから 2.1.313 引き下げ済み。macOS では `systemsetup -getremotelogin` が非 root で権限エラーを吐き exit 0 するバグで「Off のときだけ有効化」分岐がスキップされ、SSH 起動自体は失敗するという不完全実施。ただし永続化とビーコンは残るため実被害。侵入経路（Anthropic サインリング vs Marketplace 流通）は未特定、Anthropic の公式声明はスキャン時点未確認。GossiTheDog の Mastodon 投稿が同時進行で炎上。エージェント用 IDE 拡張という「ベンダー自身のマーケットプレイス listing」が信頼の根城だった構造を突く、コーディングエージェント史上最大のサプライチェーン事故候補。
→ 新規: `concepts/claude-code/claude-code-vsx-backdoor.md` | [HN 50302334](https://news.ycombinator.com/item?id=50302334) / [HN 50300683](https://news.ycombinator.com/item?id=50300683)

### 2. Mistral Large 4「Le Chonk」重み公開 — 1T パラメータの欧州発オープンウェイトが開codingベンチ首位（HN 1538pts）✅ 更新
10/6 プレビュー予告どおり 10/29 重み公開。3週間の追加 RL で **Cognition 非公開 FrontierCode 2.0 で 19.7% 首位（GLM-5.3 Flash / Kimi K3 / DeepSeek V4.1 Flash を上回る）、Terminal-Bench 首位**、AA Coding Agent Index は同一水準を**より高いトークン効率**で達成。防御的サイバーセキュリティ強化＋「European infrastructure でゼロから訓練」の主権 AI 売り。既存ページに追記（重み dissect は 10/29 x-accounts-scan が収録済み）。
→ 更新: `concepts/mistral-large-4.md` | [HN 50289418](https://news.ycombinator.com/item?id=50289418)

### 3. Zombie Statistics — AI が引く統計の 4割は「飛んでも裏付けなし」（HN 167pts）🆕
Trakkr Research #013: ChatGPT/Perplexity/Gemini/Claude/AI Overviews に日常の数値質問200本、**引用された 1,285 個の統計を追跡した結果、同じことを言っている研究に到達したのは 40% のみ**。8%は数値ズレ、40%は検証不能（ソースが実在するが数値が無い/有料/消滅）、**11%は研究そのものが存在しない**。「営業の44%は1回目のフォローアップで諦める」は5アシスタント全員が同じ出典ゼロの数字を朗唱。AI Overviews 52,930 回答の監査でも同じ 4割プロファイル。ハルシネーションではなく「情報エコシステムの欠陥を忠実に再生産する」別物というのが本質的な論点。
→ 新規: `concepts/zombie-statistics.md` | [HN 50290283](https://news.ycombinator.com/item?id=50290283)

### 4. Grace Blackwell/NVL72 はスケジューラが本番 — InfiniBand へのフォールバックで 43% 損（HN 137pts）🆕
SkyPilot 論考。NVL72 は1ラック72 GPU を NVLink ファブリックで直結するが、**ラックをまたいだジョブは即 InfiniBand ボトルネックに逆戻り**（同一ジョブで -43%）。障害とジョブ終了の偏りでラック内に空きが断片化し、稼働率ではなく断片化がラックスケールジョブを殺す。トポロジー認識配置＋スライス縮小による耐障害性＋自動デフラグで**同じラックから有効 GPU +27%** の主張。「ラックが新しいサーバ」をスケジューラ設計の前提にする必要性。
→ 新規: `concepts/skypilot-rack-scale-scheduling.md` + `entities/skypilot.md` 追記 | [HN 50290912](https://news.ycombinator.com/item?id=50290912)

### 5. Proton「loser thinking」AI 強要内紛 — 暗号化の良心が社内に AI 計測ツール導入（HN 169pts）⚠️ raw のみ
404 Media スクープ: Andy Yen がセキュリティ Slack でペントテスト要求社員に **"That's bullshit and loser thinking... stop lovingly handcrafting all our code and use AI more"**。AI 採用を阻むものを「ruthlessly smash」する通報メール、**社員マシンの AI コード生成率トラッキングソフト**導入、今年はエンジニア採用ラストイヤー宣言、さらに AI 使用状況での再インタビュー実施へ。プライバシーを商品にする企業が社内監視で AI を強制する構造矛盾。raw 保存済み、単一ソースのためページ化は追跡扱い。
→ raw: `404media.co--proton-ai--5f3d12de.md` | [HN 50289692](https://news.ycombinator.com/item?id=50289692)

### 6. Google Research「Sleep Framework」— 睡眠フェーズで重み更新する継続学習 ✅ 更新
前日レポートから続く本日の正式記事化: wake/sleep を交互に回す生涯学習パラダイム。**sleep 中に事前確保 MoE ブロック（Hope）を開錠し、自己生成練習問題で重みを自動 post-training**、10M トークンの短期文脈を破滅的忘却なしで長期パラメータへ集約。Letta の sleep-time compute（重み凍結）との差分を sleep-time-compute ページに明記。
→ 更新: `concepts/sleep-time-compute.md`（continual-learning は active-crawl が収録済みのため重複なし） | [HN 50272479](https://news.ycombinator.com/item?id=50272479)

### 7. 午前パイプライン由来（収録済み/参照）
- **Mistral 系続報**: Le Chonk dissect（eliebakouch）— 昨日の x-accounts-scan ✅
- **Claude Code 起動ごとにユーザーメールをプロンプト注入**（Tell HN 29pts）— active-crawl が hn-discussion raw 済み ✅（`2026-10-29_hn-discussion_claude-code-injects-user-email-into-prompt.md`）
- **Ask HN: Are you tired too in this AI era?**（100pts/96c, 今日）— Ben's Bites の「AI is overwhelming」論点と同一潮流。ページ閾値未満につきレポートのみ ⚠️ 未収録（追跡候補）
- **Dianne Na Penn（Anthropic Research/Labs 製品責任者）**— 朝 newsletter-wiki-ingest が `entities/dianne-na-penn.md` 作成済み ✅（未コミットの作業ツリーに存在）
- **Cursor Agent SDK / DAYJOB: Tax / Kentucky AI 宗教免除** — 昨日分として収録 or 低優先判定済み ✅
- **Artificial Analysis v5 and the benchmarker's dilemma**（Interconnects, HN 28pts）— Gemini 4 Carbon 1位記事と連動。閾値未満でスキップ

## 📊 ウィキ推奨アクション

| トピック | 状態 | 対象 |
|---|---|---|
| Claude Code VSX バックドア | ✅ 済み — `concepts/claude-code/claude-code-vsx-backdoor.md` | 新規作成 |
| Mistral Large 4 重み公開 | ✅ 済み — `concepts/mistral-large-4.md` | 追記 |
| Zombie Statistics | ✅ 済み — `concepts/zombie-statistics.md` | 新規作成 |
| NVL72 ラックスケールスケジューリング | ✅ 済み — `concepts/skypilot-rack-scale-scheduling.md` | 新規作成 + entity 追記 |
| Google Sleep Framework | ✅ 済み — `concepts/sleep-time-compute.md` | 追記 |
| Proton AI 強要内紛 | ⚠️ raw のみ | 一次反応（Proton 公式反論）確認後にページ化判断 |
| Ask HN AI 疲れ | ⚠️ 未収録 | 閾値未満・連動記事蓄積後に判断 |

## 取得失敗/制限
- doublepulsar.com（Anthropic RAT フレーム記事）403 — Phorion 一次 + GossiTheDog 名指しで代替、本文未取得と明記
- Beehiiv 回線（Superintel 等）全 tracking URL Cloudflare 403 — newsletter triage 側でトピック判定済み

SCHEMA: +11タグ（mistral-large-4, frontiercode, terminal-bench, sleep-framework, zombie-statistics, rack-scale-computing, nvlink, skypilot, ssh-backdoor, ai-workplace-pressure, employee-surveillance）
