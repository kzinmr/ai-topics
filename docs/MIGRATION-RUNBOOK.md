# Hermes AI Topic Manager — Migration Runbook

別の exe.dev VM（または同等環境）への完全移行手順書。

> **前提**: 新マシンは Ubuntu 24.04 相当の exe.dev VM を想定。exe.dev 外への移行でも大部分は適用可能だが、メール受信・HTTPS プロキシ部分は exe.dev 固有機能。

---

## 目次

1. [現行環境の全体像](#1-現行環境の全体像)
2. [移行前の準備（旧マシン）](#2-移行前の準備旧マシン)
3. [新マシンのセットアップ](#3-新マシンのセットアップ)
4. [Hermes Agent インストール](#4-hermes-agent-インストール)
5. [ai-topics リポジトリのクローン](#5-ai-topics-リポジトリのクローン)
6. [シンボリックリンクの作成](#6-シンボリックリンクの作成)
7. [Hermes 設定ファイルの復元](#7-hermes-設定ファイルの復元)
8. [blogwatcher-cli のインストール](#8-blogwatcher-cli-のインストール)
9. [Maildir の構築とメール受信設定](#9-maildir-の構築とメール受信設定)
10. [systemd サービスの設定](#10-systemd-サービスの設定)
11. [systemd タイマーの設定](#11-systemd-タイマーの設定)
12. [Shelley スキル・AGENTS.md の設定](#12-shelley-スキルagentsmd-の設定)
13. [動作確認チェックリスト](#13-動作確認チェックリスト)
14. [旧マシンの停止・クリーンアップ](#14-旧マシンの停止クリーンアップ)
15. [トラブルシューティング](#15-トラブルシューティング)
16. [付録: ファイル一覧と設定値リファレンス](#16-付録-ファイル一覧と設定値リファレンス)

---

## 1. 現行環境の全体像

### サービス構成

| サービス | systemd unit | タイプ | ポート | 役割 |
|----------|-------------|--------|--------|------|
| Hermes Gateway | `hermes-gateway.service` | simple (常駐) | — | Discord bot (Hermes Agent) |
| Hermes Dashboard | `hermes-dashboard.service` | simple (常駐) | 8000 | Web ダッシュボード |
| Email Watcher | `email-watcher.service` | simple (常駐) | — | Maildir 監視→newsletter 自動処理 |
| Shelley Agent | `shelley.service` | exec (常駐) | — | exe.dev コーディングエージェント |

### スケジュールジョブ（systemd timer）

| タイマー | スケジュール | 役割 |
|----------|-------------|------|
| `shelley-trending-topics.timer` | 毎日 10:00 UTC | トレンドトピック検出 |
| `shelley-active-crawl.timer` | 毎日 11:00 UTC | 能動的知識クローリング |
| `shelley-wiki-health.timer` | 毎週月曜 09:00 UTC | Wiki ヘルスチェック |
| `shelley-wiki-graph.timer` | 毎週木曜 09:00 UTC | Wiki グラフ分析 |

### ディレクトリ構成

```
/home/exedev/
├── ai-topics/                    # メインリポジトリ (GitHub: kzinmr/ai-topics)
│   ├── wiki/                     # LLM Wiki 知識ベース (~721 .md files, ~11MB)
│   ├── inbox/                    # 受信データ
│   ├── config/
│   │   ├── feeds/                # blogs.opml, x-accounts.yaml
│   │   ├── hermes/               # SOUL.md, skills/
│   │   └── hot-topics.yaml       # アクティブクローリング対象
│   ├── scripts/                  # 自動化スクリプト群
│   ├── systemd/                  # systemd unit ファイル
│   ├── docs/                     # ドキュメント
│   └── blogwatcher.db            # blogwatcher-cli SQLite DB
│
├── .hermes/
│   ├── hermes-agent/             # Hermes Agent ソース (NousResearch/hermes-agent)
│   │   └── venv/                 # Python 仮想環境
│   ├── config.yaml               # Hermes 設定
│   ├── .env                      # API キー・シークレット
│   └── SOUL.md → ai-topics/config/hermes/SOUL.md
│
├── bin/
│   └── blogwatcher-cli           # Go バイナリ (v0.1.1)
│
├── Maildir/                      # メール受信ディレクトリ
│   ├── new/
│   ├── cur/
│   ├── processed/
│   └── tmp/
│
├── wiki → ai-topics/wiki/        # シンボリックリンク
├── scripts/                      # シンボリックリンク群
├── node/                         # Node.js v22.16.0
└── .config/shelley/              # Shelley エージェント設定
```

### 依存ソフトウェア

| ソフトウェア | バージョン | 用途 |
|-------------|-----------|------|
| Python | 3.12.3 | スクリプト実行 |
| Node.js | 22.16.0 | Playwright ブラウザ自動化 |
| Hermes Agent | v0.9.0 | AI エージェント |
| blogwatcher-cli | v0.1.1 | RSS フィード監視 (Go バイナリ) |
| Shelley | — | exe.dev エージェント |
| inotify-tools | 3.22.6.0 | Maildir 監視 |

---

## 2. 移行前の準備（旧マシン）

### 2.1 データの最新化とバックアップ

```bash
# ai-topics リポジトリを最新にpush
cd ~/ai-topics
git add -A
git commit -m "pre-migration: snapshot all changes"
git push

# .env ファイルのバックアップ（最重要シークレット）
cp ~/.hermes/.env ~/ai-topics-env-backup.txt
# ⚠️ このファイルにはAPIキー・トークンが含まれる。安全に転送すること。

# Hermes config.yaml のバックアップ
cp ~/.hermes/config.yaml ~/hermes-config-backup.yaml

# blogwatcher DB のバックアップ（gitignore されている）
cp ~/ai-topics/blogwatcher.db ~/blogwatcher-db-backup.sqlite

# Maildir に未処理メールが無いか確認
ls ~/Maildir/new/
ls ~/Maildir/processed/ | wc -l
```

### 2.2 旧マシンで停止すべきもの（移行完了後）

移行完了まで旧マシンは稼働させたまま。Section 14 参照。

---

## 3. 新マシンのセットアップ

### 3.1 基本パッケージのインストール

```bash
sudo apt-get update
sudo apt-get install -y \
  git \
  python3 python3-pip python3-venv \
  inotify-tools \
  curl wget \
  jq
```

### 3.2 Node.js のインストール

```bash
# Node.js v22 LTS
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# もしくは exe.dev の場合: shelley が自動インストール可能
# ~/node/ にインストールされるパターンの場合:
curl -fsSL https://nodejs.org/dist/v22.16.0/node-v22.16.0-linux-x64.tar.xz | tar -xJf - -C ~
mv ~/node-v22.16.0-linux-x64 ~/node
export PATH="$HOME/node/bin:$PATH"
echo 'export PATH="$HOME/node/bin:$PATH"' >> ~/.bashrc
```

### 3.3 Playwright のインストール（Hermes ブラウザツール用）

```bash
npx playwright install --with-deps chromium
```

---

## 4. Hermes Agent インストール

### 4.1 リポジトリのクローンとセットアップ

```bash
mkdir -p ~/.hermes
cd ~/.hermes
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# Python 仮想環境の作成とインストール
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install playwright beautifulsoup4 feedparser lxml requests
deactivate

# hermes コマンドへのシンボリックリンク
mkdir -p ~/.local/bin
ln -sf ~/.hermes/hermes-agent/venv/bin/hermes ~/.local/bin/hermes
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# バージョン確認
hermes --version
# 期待値: Hermes Agent v0.9.0 以上
```

---

## 5. ai-topics リポジトリのクローン

```bash
cd ~
git clone https://github.com/kzinmr/ai-topics.git
cd ai-topics

# git 設定
git config user.name "Hermes Agent"
git config user.email "hermes@<新VM名>.exe.xyz"
```

> **Note**: GitHub への push 権限が必要。SSH キーまたは Personal Access Token を設定すること。
>
> ```bash
> # SSH キーの場合
> ssh-keygen -t ed25519 -C "hermes@<新VM名>.exe.xyz"
> cat ~/.ssh/id_ed25519.pub
> # → GitHub Settings > SSH keys に追加
> git remote set-url origin git@github.com:kzinmr/ai-topics.git
>
> # PAT の場合
> git remote set-url origin https://<PAT>@github.com/kzinmr/ai-topics.git
> ```

---

## 6. シンボリックリンクの作成

多くのスクリプトと設定が旧パスを参照するため、互換シンボリックリンクを作成する。

```bash
# Wiki
ln -sf ~/ai-topics/wiki ~/wiki

# Scripts (個別リンク)
mkdir -p ~/scripts
for script in build_blog_wiki.py build_x_wiki.py check_mail.sh check_new_skills.py \
             email_watcher.sh process_email.py wiki_server.py; do
  ln -sf ~/ai-topics/scripts/$script ~/scripts/$script
done

# Config feeds
ln -sf ~/ai-topics/config/feeds/blogs.opml ~/hn-popular-blogs-2025.opml
ln -sf ~/ai-topics/config/feeds/x-accounts.yaml ~/x-accounts.yaml

# Docs
ln -sf ~/ai-topics/docs/SETUP.md ~/SETUP.md

# SOUL.md
ln -sf ~/ai-topics/config/hermes/SOUL.md ~/.hermes/SOUL.md
```

---

## 7. Hermes 設定ファイルの復元

### 7.1 .env ファイル

旧マシンからバックアップした `.env` を復元する。

```bash
# 安全な方法で転送（scp, 手動コピーなど）
# scp oldvm:~/ai-topics-env-backup.txt ~/.hermes/.env
vi ~/.hermes/.env
```

**必須の環境変数:**

| 変数 | 用途 | 取得元 |
|------|------|--------|
| `OPENAI_API_KEY` + `OPENAI_BASE_URL` | LLM プロバイダー (Fireworks) | Fireworks AI コンソール |
| `EXA_API_KEY` | Web 検索 | https://exa.ai |
| `DISCORD_BOT_TOKEN` | Discord bot | Discord Developer Portal |
| `DISCORD_ALLOWED_USERS` | 許可ユーザー ID | Discord |
| `DISCORD_HOME_CHANNEL` | 通知チャンネル | Discord |
| `BROWSERBASE_PROJECT_ID` | ブラウザ自動化 | https://browserbase.com |
| `BROWSERBASE_API_KEY` | ブラウザ自動化 | https://browserbase.com |
| `HONCHO_API_KEY` | ユーザーモデリング | https://app.honcho.dev |

> **⚠️ セキュリティ**: `.env` には全 API キーが含まれる。git に絶対コミットしない。転送後はバックアップファイルを削除。

### 7.2 config.yaml

```bash
cp ~/hermes-config-backup.yaml ~/.hermes/config.yaml
```

**config.yaml の重要設定:**

```yaml
model:
  default: accounts/fireworks/models/qwen3p6-plus
  provider: custom
  base_url: https://api.fireworks.ai/inference/v1

skills:
  external_dirs:
    - ~/ai-topics/config/hermes/skills   # カスタムスキル

memory:
  memory_enabled: true

compression:
  enabled: true
  summary_model: google/gemini-3-flash-preview

agent:
  max_turns: 60
  gateway_timeout: 1800

discord:
  require_mention: true
  auto_thread: true
```

### 7.3 blogwatcher.db の復元

```bash
# 旧マシンから転送
# scp oldvm:~/blogwatcher-db-backup.sqlite ~/ai-topics/blogwatcher.db
```

---

## 8. blogwatcher-cli のインストール

```bash
mkdir -p ~/bin

# Go バイナリのコピーまたは再ビルド
# 方法 A: 旧マシンからコピー
# scp oldvm:~/bin/blogwatcher-cli ~/bin/blogwatcher-cli

# 方法 B: ソースからビルド（Go 環境が必要）
# go install github.com/<repo>/blogwatcher-cli@latest
# cp $(go env GOPATH)/bin/blogwatcher-cli ~/bin/

chmod +x ~/bin/blogwatcher-cli
export PATH="$HOME/bin:$PATH"
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc

# 動作確認
blogwatcher-cli --version
# 期待値: 0.1.1
```

---

## 9. Maildir の構築とメール受信設定

### 9.1 Maildir ディレクトリの作成

```bash
mkdir -p ~/Maildir/{new,cur,tmp,processed}
```

### 9.2 exe.dev メール受信の有効化

**ローカルマシンから実行** (exe.dev CLI):

```bash
# 旧マシンのメール受信を無効化
ssh exe.dev share receive-email <旧VM名> off

# 新マシンのメール受信を有効化
ssh exe.dev share receive-email <新VM名> on
```

メールアドレスは `*@<新VM名>.exe.xyz` のワイルドカード。
ニュースレターの購読先アドレスを変更する必要がある場合は、各サービスで再登録。

> **⚠️ 重要**: `~/Maildir/new/` に 1000 ファイル以上溜まるとメール受信が自動停止される。

---

## 10. systemd サービスの設定

### 10.1 Email Watcher

```bash
sudo tee /etc/systemd/system/email-watcher.service << 'EOF'
[Unit]
Description=Newsletter Email Watcher
After=network-online.target

[Service]
Type=simple
User=exedev
ExecStart=/home/exedev/scripts/email_watcher.sh
Restart=always
RestartSec=10
Environment=PATH=/home/exedev/.local/bin:/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=multi-user.target
EOF
```

### 10.2 Hermes Gateway (Discord)

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway (Discord)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=exedev
WorkingDirectory=/home/exedev/.hermes/hermes-agent
ExecStart=/home/exedev/.local/bin/hermes gateway run
Restart=always
RestartSec=10
EnvironmentFile=/home/exedev/.hermes/.env

[Install]
WantedBy=multi-user.target
EOF
```

### 10.3 Hermes Dashboard

```bash
sudo tee /etc/systemd/system/hermes-dashboard.service << 'EOF'
[Unit]
Description=Hermes Agent Web Dashboard
After=network.target

[Service]
Type=simple
User=exedev
ExecStart=/home/exedev/.local/bin/hermes dashboard --port 8000 --host 0.0.0.0 --no-open
Restart=on-failure
RestartSec=5
Environment=HOME=/home/exedev
Environment=PATH=/home/exedev/.local/bin:/home/exedev/node/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
WorkingDirectory=/home/exedev

[Install]
WantedBy=multi-user.target
EOF
```

### 10.4 サービスの有効化と起動

```bash
sudo systemctl daemon-reload

# 各サービスを有効化して起動
sudo systemctl enable --now email-watcher.service
sudo systemctl enable --now hermes-gateway.service
sudo systemctl enable --now hermes-dashboard.service

# ステータス確認
sudo systemctl status email-watcher hermes-gateway hermes-dashboard
```

---

## 11. systemd タイマーの設定

### 11.1 Trending Topics Detection（毎日 10:00 UTC）

```bash
sudo tee /etc/systemd/system/shelley-trending-topics.service << 'SERVICEEOF'
[Unit]
Description=Shelley Trending Topics Detection (daily)
After=network.target

[Service]
Type=oneshot
User=exedev
WorkingDirectory=/home/exedev/ai-topics
ExecStart=/usr/bin/shelley client chat -p 'Daily Trending Topics notification.\n\nStep 1: Run `python3 ~/ai-topics/scripts/trending_topics.py --days 3` and present the report to the user IN JAPANESE. Focus on: (1) New Page Recommended — trending topics with no wiki page yet, (2) Hot Topics with 4+ sources, (3) Cross-Source Topics — highest signal items appearing across RSS, newsletters, and raw articles. Suggest which topics Hermes should prioritize for wiki page creation or updates.\n\nStep 2: Hot Topics クローリング候補提案。`cat ~/ai-topics/config/hot-topics.yaml` を読み、Step 1 の「New Page Recommended」のトピック群と照合する。以下の条件を満たすトピックがあれば、hot-topics.yaml への追加候補として提案する:\n- source_count が 3 以上で、hot-topics.yaml にまだ登録されていない\n- SCHEMA.md のドメイン(LLM/AI Agent技術)に合致する\n- 既存トピックのサブトピックではなく、独立したトピックとして管理する価値がある\n\n提案フォーマット(YAMLスニペットとしてそのまま貼れる形)で出力。候補がない場合は「該当なし」と明記。' -cwd '/home/exedev/ai-topics'
TimeoutStartSec=180

[Install]
WantedBy=multi-user.target
SERVICEEOF

sudo tee /etc/systemd/system/shelley-trending-topics.timer << 'TIMEREOF'
[Unit]
Description=Daily Trending Topics Detection

[Timer]
OnCalendar=*-*-* 10:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
TIMEREOF
```

### 11.2 Active Knowledge Crawl（毎日 11:00 UTC）

```bash
sudo tee /etc/systemd/system/shelley-active-crawl.service << 'SERVICEEOF'
[Unit]
Description=Shelley Active Knowledge Crawl (daily)
After=network.target

[Service]
Type=oneshot
User=exedev
WorkingDirectory=/home/exedev/ai-topics
ExecStart=/usr/bin/shelley client chat -p 'Daily Active Knowledge Crawl. あなたの目的: config/hot-topics.yaml に登録されたホットトピックに関連する「まだ取り込まれていない重要概念」を能動的に調査し、知識ベースに取り込むこと。\n\n手順:\n1. `cat ~/ai-topics/config/hot-topics.yaml` を読み、crawl_policy が prerequisites/laterals/deepdive かつ last_crawled が3日以上前(またはnull)のトピックを抽出\n2. priority: high から last_crawled が最も古い順に最大2つ、priority: medium から最大1つ、合計最大3トピックを選択\n3. 各トピックについて crawl_policy に応じた動作を実行\n4. 各概念についてWeb検索でソースを発見し、wiki に取り込み\n5. hot-topics.yaml の last_crawled を更新\n6. git commit & push\n7. 結果を日本語で報告' -cwd '/home/exedev/ai-topics'
TimeoutStartSec=300

[Install]
WantedBy=multi-user.target
SERVICEEOF

sudo tee /etc/systemd/system/shelley-active-crawl.timer << 'TIMEREOF'
[Unit]
Description=Daily Active Knowledge Crawl

[Timer]
OnCalendar=*-*-* 11:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
TIMEREOF
```

### 11.3 Wiki Health Digest（毎週月曜 09:00 UTC）

```bash
sudo tee /etc/systemd/system/shelley-wiki-health.service << 'SERVICEEOF'
[Unit]
Description=Shelley Wiki Health Digest (weekly)
After=network.target

[Service]
Type=oneshot
User=exedev
WorkingDirectory=/home/exedev/ai-topics
ExecStart=/usr/bin/shelley client chat -p 'Weekly Wiki Health Digest. Run `python3 ~/ai-topics/scripts/wiki_health.py` and present the full report to the user IN JAPANESE. Highlight notable findings: skeleton entities needing enrichment, stale pages (>30d), orphan pages not in index.md, and unprocessed raw articles. Suggest 2-3 concrete next actions.' -cwd '/home/exedev/ai-topics'
TimeoutStartSec=180

[Install]
WantedBy=multi-user.target
SERVICEEOF

sudo tee /etc/systemd/system/shelley-wiki-health.timer << 'TIMEREOF'
[Unit]
Description=Weekly Wiki Health Digest

[Timer]
OnCalendar=Mon 09:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
TIMEREOF
```

### 11.4 Wiki Graph Analysis（毎週木曜 09:00 UTC）

```bash
sudo tee /etc/systemd/system/shelley-wiki-graph.service << 'SERVICEEOF'
[Unit]
Description=Shelley Wiki Graph Analysis (weekly)
After=network.target

[Service]
Type=oneshot
User=exedev
WorkingDirectory=/home/exedev/ai-topics
ExecStart=/usr/bin/shelley client chat -p 'Weekly Wiki Graph Analysis. Run `python3 ~/ai-topics/scripts/wiki_graph.py` and present the report to the user IN JAPANESE. Focus on: (1) Intellectual clusters — top 10 person pairs with high similarity but no wiki link, (2) Cross-reference gap recommendations — top 10 links Hermes should add during entity enrichment, (3) Bridge concepts connecting many opinion leaders. Keep the summary concise.' -cwd '/home/exedev/ai-topics'
TimeoutStartSec=180

[Install]
WantedBy=multi-user.target
SERVICEEOF

sudo tee /etc/systemd/system/shelley-wiki-graph.timer << 'TIMEREOF'
[Unit]
Description=Weekly Wiki Graph Analysis (cross-reference gaps)

[Timer]
OnCalendar=Thu 09:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
TIMEREOF
```

### 11.5 タイマーの有効化

```bash
sudo systemctl daemon-reload

sudo systemctl enable --now shelley-trending-topics.timer
sudo systemctl enable --now shelley-active-crawl.timer
sudo systemctl enable --now shelley-wiki-health.timer
sudo systemctl enable --now shelley-wiki-graph.timer

# 確認
systemctl list-timers --no-pager
```

---

## 12. Shelley スキル・AGENTS.md の設定

exe.dev VM の場合、Shelley は自動的にプリインストールされている (`/usr/local/bin/shelley`)。

### 12.1 AGENTS.md

`~/.config/shelley/AGENTS.md` がプロジェクトの慣習を定義する。必要に応じて編集:

```bash
mkdir -p ~/.config/shelley
cat > ~/.config/shelley/AGENTS.md << 'EOF'
You are running in an exe.dev VM.

https://exe.dev/docs/proxy.md has details about the exe.dev HTTPS proxy.

Only use documented exe.dev features (see https://exe.dev/docs.md). Undocumented local endpoints are internal infrastructure—unstable and unsupported.
EOF
```

### 12.2 Shelley スキル

スキルは `ai-topics/config/hermes/skills/` に格納されており、リポジトリクローンで自動復元される。
`~/.hermes/config.yaml` の `skills.external_dirs` で参照:

```yaml
skills:
  external_dirs:
    - ~/ai-topics/config/hermes/skills
```

現行のカスタムスキル:
- `productivity/exe-dev-email-check` — メールチェック
- `research/semantic-article-grouping` — 記事グルーピング
- `research/blogwatcher-db` — blogwatcher DB クエリ
- `research/blog-author-thought-analysis` — ブログ著者分析
- `research/opinion-leader-depth-analysis` — オピニオンリーダー分析
- `wiki/x-account-enrichment` — X アカウントエンリッチ
- `wiki/cross-leader-synthesis` — クロスリーダー統合
- `wiki/wiki-entity-upgrade` — エンティティアップグレード
- `wiki/grokipedia-enrichment` — Grokipedia エンリッチ

---

## 13. 動作確認チェックリスト

以下を順番に確認する。全項目 ✅ で移行完了。

### 基本

- [ ] `hermes --version` → v0.9.0 以上
- [ ] `blogwatcher-cli --version` → 0.1.1
- [ ] `python3 --version` → 3.12+
- [ ] `node --version` → v22+
- [ ] `which inotifywait` → `/usr/bin/inotifywait`

### リポジトリ

- [ ] `cd ~/ai-topics && git status` → クリーン
- [ ] `git pull` → 成功
- [ ] `git push` → 成功（権限テスト）
- [ ] `ls ~/wiki/SCHEMA.md` → 存在する
- [ ] `ls ~/wiki/index.md` → 存在する

### シンボリックリンク

- [ ] `ls -la ~/wiki` → `~/ai-topics/wiki`
- [ ] `ls -la ~/scripts/process_email.py` → `~/ai-topics/scripts/process_email.py`
- [ ] `ls -la ~/.hermes/SOUL.md` → `~/ai-topics/config/hermes/SOUL.md`
- [ ] `ls -la ~/hn-popular-blogs-2025.opml` → `~/ai-topics/config/feeds/blogs.opml`
- [ ] `ls -la ~/x-accounts.yaml` → `~/ai-topics/config/feeds/x-accounts.yaml`

### Hermes Agent

- [ ] `hermes chat -p 'say hello'` → 正常応答
- [ ] `hermes skill list` → カスタムスキルが表示される

### systemd サービス

- [ ] `systemctl status email-watcher` → active (running)
- [ ] `systemctl status hermes-gateway` → active (running)
- [ ] `systemctl status hermes-dashboard` → active (running)
- [ ] `curl -s http://localhost:8000/` → ダッシュボード HTML

### systemd タイマー

- [ ] `systemctl list-timers --no-pager` → 4 つのタイマーが表示
- [ ] `sudo systemctl start shelley-trending-topics.service` → 手動実行成功

### メール

- [ ] `ls ~/Maildir/new/` → ディレクトリ存在
- [ ] テストメール送信 → `~/Maildir/new/` に到着
- [ ] Email watcher が処理 → `journalctl -u email-watcher -f` で確認

### Discord Bot

- [ ] Discord で `@Hermes hello` → 応答あり
- [ ] Discord で `@Hermes wiki status` → wiki 情報が返る

### Web アクセス (exe.dev)

- [ ] `https://<新VM名>.exe.xyz:8000/` → ダッシュボードが表示

---

## 14. 旧マシンの停止・クリーンアップ

新マシンでの動作確認が完了したら:

```bash
# 旧マシンで実行

# 1. サービス停止
sudo systemctl stop hermes-gateway email-watcher hermes-dashboard
sudo systemctl disable hermes-gateway email-watcher hermes-dashboard

# 2. タイマー停止
sudo systemctl stop shelley-trending-topics.timer shelley-active-crawl.timer \
  shelley-wiki-health.timer shelley-wiki-graph.timer
sudo systemctl disable shelley-trending-topics.timer shelley-active-crawl.timer \
  shelley-wiki-health.timer shelley-wiki-graph.timer

# 3. メール受信の無効化（ローカルマシンから）
# ssh exe.dev share receive-email <旧VM名> off

# 4. バックアップの .env ファイルを安全に削除
rm -f ~/ai-topics-env-backup.txt ~/hermes-config-backup.yaml ~/blogwatcher-db-backup.sqlite
```

---

## 15. トラブルシューティング

### Hermes Gateway が起動しない

```bash
journalctl -u hermes-gateway -n 50 --no-pager
# よくある原因:
# - .env の DISCORD_BOT_TOKEN が無効
# - Python venv のパスが間違っている
# - model.base_url への接続エラー
```

### Email Watcher が動かない

```bash
journalctl -u email-watcher -n 50 --no-pager
# よくある原因:
# - inotifywait がインストールされていない
# - ~/Maildir/new/ が存在しない
# - process_email.py の Python パスが間違っている
```

### タイマーが発火しない

```bash
systemctl list-timers --all --no-pager
journalctl -u shelley-trending-topics -n 20 --no-pager
# 手動トリガーでテスト:
sudo systemctl start shelley-trending-topics.service
journalctl -u shelley-trending-topics -f
```

### git push が失敗する

```bash
# SSH キー確認
ssh -T git@github.com
# credential helper 確認
git config --global credential.helper
```

### Wiki Server / Dashboard に外部からアクセスできない

- exe.dev の場合: ポート 3000-9999 のみプロキシされる
- `--host 0.0.0.0` でバインドしているか確認
- `curl http://localhost:8000/` でローカルアクセスを先に確認

---

## 16. 付録: ファイル一覧と設定値リファレンス

### 転送が必要なファイル（git に含まれないもの）

| ファイル | 必須 | 説明 |
|---------|------|------|
| `~/.hermes/.env` | ✅ 必須 | 全 API キー・トークン |
| `~/.hermes/config.yaml` | ✅ 必須 | Hermes 設定 |
| `~/ai-topics/blogwatcher.db` | 推奨 | RSS スキャン履歴 (無ければ再スキャンで再構築) |
| `~/Maildir/processed/*` | 任意 | 処理済みメール (不要なら移行不要) |

### git に含まれるもの（クローンで自動復元）

- `ai-topics/wiki/` — 全 wiki ページ (~721 files)
- `ai-topics/inbox/` — ニュースレターダイジェスト、RSS スキャンレポート
- `ai-topics/config/` — feeds, hermes skills, hot-topics.yaml, SOUL.md
- `ai-topics/scripts/` — 全自動化スクリプト
- `ai-topics/systemd/` — systemd unit ファイル（参考用コピー）
- `ai-topics/docs/` — ドキュメント

### ポート使用

| ポート | サービス | 公開 |
|--------|---------|------|
| 8000 | Hermes Dashboard | `https://<VM名>.exe.xyz:8000/` |

### 環境変数一覧 (.env)

```
# LLM
OPENAI_API_KEY=...           # Fireworks API key
OPENAI_BASE_URL=...          # https://api.fireworks.ai/inference/v1

# Tool APIs
EXA_API_KEY=...              # Web search
BROWSERBASE_PROJECT_ID=...   # Browser automation
BROWSERBASE_API_KEY=...      # Browser automation
HONCHO_API_KEY=...           # User modeling

# Discord
DISCORD_BOT_TOKEN=...        # Bot token
DISCORD_ALLOWED_USERS=...    # Comma-separated user IDs
DISCORD_HOME_CHANNEL=...     # Notification channel ID

# Telegram (optional)
TELEGRAM_BOT_TOKEN=...       # Bot token

# Slack (optional)
SLACK_BOT_TOKEN=...          # Bot token
SLACK_APP_TOKEN=...          # App token
```

---

## 変更履歴

| 日付 | 内容 |
|------|------|
| 2026-04-17 | 初版作成 |
