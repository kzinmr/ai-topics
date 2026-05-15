---
title: "Claude Code Skills — 機序と役割パターン"
created: 2026-05-15
updated: 2026-05-15
type: concept
tags:
  - claude-code
  - agent-skills
  - harness-engineering
  - ai-agent-engineering
  - skill-graph
  - developer-tooling
sources:
  - raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md
  - https://x.com/trq212/status/2033949937936085378
related:
  - agent-skills
  - skill-architecture-patterns
  - claude-code-best-practices
  - agent-harness
  - mcp
status: active
---

# Claude Code Skills — 機序と役割パターン

Claude Code TeamのThariq Shihipar（[[entities/thariq-shihipar]]）がAnthropic社内で数百のSkillsを運用して得た実践知に基づく、Skillsの**機序**（仕組み）の本質と、**9つの役割パターン**への分類。

> "Skills have become one of the most used extension points in Claude Code. They're flexible, easy to make, and simple to distribute."

## 機序（Mechanism）：Skillsの本質

### Skills ≠ Markdownファイル

最も重要な誤解の解消。Skillsは単なる`.md`ファイルではない:

- **フォルダである**: スクリプト、アセット、データ、設定ファイルを含むディレクトリ構造
- **エージェントが発見・探索・操作できる**: Claudeが必要に応じてファイルを読み取り、スクリプトを実行し、データを参照する
- **動的Hooksの登録**: PreToolUse/PostToolUseフックにより、Skill呼び出し時に限定された行動制約を課せる

### ファイルシステム = コンテキストエンジニアリングの媒体

```
skill-name/
├── SKILL.md              # 必須: YAML frontmatter + 指示本体
├── references/           # オプション: 詳細リファレンス（progressive disclosure）
│   └── api.md            # → 必要なときだけClaudeが読み取り
├── scripts/              # オプション: 実行可能コード
│   └── fetch_data.py     # → Claudeが実行、結果だけコンテキストに取り込む
├── assets/               # オプション: テンプレート・画像など
│   └── template.md       # → 出力フォーマットの雛形
└── config.json           # オプション: セットアップ状態の永続化
```

**Progressive Disclosure（段階的開示）**:
1. **L1**: `name` + `description` → セッション開始時に全Skill一覧として常時注入
2. **L2**: `SKILL.md`本文 → 関連タスク時にClaudeが自力で読み取り
3. **L3+**: `references/`以下のファイル → 必要に応じてClaudeが判断して読み取り

> "Tell Claude what files are in your skill, and it will read them at appropriate times."

### コード実行による決定論的操作

Scriptsフォルダ内のコードは、トークン生成より決定論的で効率的:
- ソート・データ処理・フォーム抽出など、コード実行の方が正確
- Claudeはスクリプト自体をコンテキストに読み込まず、実行結果だけを受け取る
- 一貫性・再現性の保証

### オンデマンドHooks

Skill呼び出し時にのみ発動し、セッション中継続する動的行動制約:

| Hook | 機能 | ユースケース |
|------|------|-------------|
| `/careful` | `rm -rf`, `DROP TABLE`, `force-push`, `kubectl delete`をブロック | 本番環境操作時のみ有効化（常時ONは煩わしい） |
| `/freeze` | 特定ディレクトリ外のEdit/Writeをブロック | 「ログを追加したいのに無関係な箇所を"修正"してしまう」デバッグ時 |

### メモリとデータ永続化

Skillsは自己の状態をファイルシステムに保存可能:
- **append-onlyログ**: `standups.log`に過去の投稿履歴 → 次回実行時に差分把握
- **JSON/SQLite**: 構造化データの保存
- **`${CLAUDE_PLUGIN_DATA}`**: Skillアップグレード時も消えない安定ストレージパス

## 役割パターン（9 Types of Skills）

Anthropic社内の全Skillをカタログ化した結果、9つの再利用パターンに収束。各Skillは1つの型にきれいに収まるのが理想で、複数にまたがるものは混乱を招く。

### Type 1: Library & API Reference（ライブラリ・API参照）

**目的**: 特定ライブラリ・CLI・SDKの正しい使い方をClaudeに教える。

**特徴**:
- 内部ライブラリのエッジケース・フットガン集
- リファレンスコードスニペット
- Claudeが間違えやすいポイントのGotchasセクション

**例**:
- `billing-lib` — 社内課金ライブラリのエッジケース・落とし穴
- `internal-platform-cli` — 社内CLIの全サブコマンドと使用タイミング
- `frontend-design` — デザインシステムに沿ったUI生成

### Type 2: Product Verification（製品検証）

**目的**: コードが正しく動作しているかの検証方法を定義。

**特徴**:
- Playwright/tmux等の外部ツールと連携
- プログラムによる状態アサーション
- 「エンジニアが1週間かけて検証Skillを磨く価値がある」最重要Skillタイプの1つ
- 動画出力による検証結果の可視化も有効

**例**:
- `signup-flow-driver` — サインアップ→メール認証→オンボーディングをヘッドレスブラウザで実行、各ステップで状態アサーション
- `checkout-verifier` — Stripeテストカードで決済UIを操作、請求書が正しい状態かを検証
- `tmux-cli-driver` — TTYが必要な対話型CLIのテスト

### Type 3: Data Fetching & Analysis（データ取得・分析）

**目的**: データスタック・監視スタックへの接続と分析ワークフローを提供。

**特徴**:
- 認証情報・ダッシュボードID・クエリパターンを含む
- 複雑なジョインや集計の定型パターンをカプセル化

**例**:
- `funnel-query` — 「サインアップ→アクティベーション→課金」のイベント結合方法と正規化user_idテーブル
- `cohort-compare` — 2コホートのリテンション/コンバージョン比較、統計的有意差フラグ
- `grafana` — データソースUID、クラスタ名、問題→ダッシュボード対応表

### Type 4: Business Process & Team Automation（業務プロセス・チーム自動化）

**目的**: 繰り返しワークフローを1コマンドに集約。

**特徴**:
- 比較的シンプルな指示だが、他SkillやMCPへの依存あり
- **過去実行結果のログ保存**が一貫性維持の鍵 — Claudeが自身の履歴を読み取り差分を把握
- チケットシステム・Slack・GitHub間の連携を定型化

**例**:
- `standup-post` — チケットトラッカー + GitHub + Slack履歴からデイリースタンドアップを自動生成
- `create-<ticket>-ticket` — スキーマ強制（有効なenum値・必須フィールド）+ 作成後フロー（レビュワー通知・Slackリンク）
- `weekly-recap` — マージ済PR + クローズチケット + デプロイ → 整形レポート

### Type 5: Code Scaffolding & Templates（コードスキャフォールディング）

**目的**: フレームワーク固有のボイラープレート生成。

**特徴**:
- 自然言語の要件を含む足場生成（コードだけでは表現できない）
- スクリプトとの合成で柔軟性向上

**例**:
- `new-<framework>-workflow` — アノテーション付きの新規サービス/ハンドラ生成
- `new-migration` — マイグレーションファイルのテンプレート + 共通の落とし穴
- `create-app` — 認証・ログ・デプロイ設定がプリワイヤされた新規アプリ

### Type 6: Code Quality & Review（コード品質・レビュー）

**目的**: 組織のコード品質基準の強制とレビュー支援。

**特徴**:
- 決定論的スクリプト/ツールで堅牢性を最大化
- HooksやGitHub Actionでの自動実行にも適する
- Claudeがデフォルトで苦手なコードスタイルの強制

**例**:
- `adversarial-review` — フレッシュなサブエージェントが批判的レビュー→修正実施→指摘が瑣末になるまで繰り返し
- `code-style` — Claudeがデフォルトで苦手なコードスタイルの強制
- `testing-practices` — テストの書き方・何をテストすべきかの指示

### Type 7: CI/CD & Deployment（CI/CD・デプロイ）

**目的**: コードの取得・プッシュ・デプロイの自動化。

**特徴**:
- 他Skillと連携してデータ収集することも
- 段階的ロールアウト、自動ロールバック、コンフリクト解決

**例**:
- `babysit-pr` — PR監視→フレーキーCI再試行→マージコンフリクト解決→自動マージ
- `deploy-<service>` — ビルド→スモークテスト→段階的トラフィックロールアウト+エラーレート比較→自動ロールバック
- `cherry-pick-prod` — 分離worktree→チェリーピック→コンフリクト解決→テンプレート付きPR

### Type 8: Runbooks（ラン�ック）

**目的**: 症状（Slack通知・アラート・エラーシグネチャ）からマルチツール調査を経て構造化レポートを生成。

**特徴**:
- 症状→ツール→クエリパターンの対応表
- オンコールフローの定型化

**例**:
- `<service>-debugging` — 症状→ツール→クエリパターンの対応表（高トラフィックサービス用）
- `oncall-runner` — アラート取得→通常の容疑者チェック→所見整形
- `log-correlator` — リクエストIDから全関連システムのログを横断取得

### Type 9: Infrastructure Operations（インフラ運用）

**目的**: 破壊的操作を含むルーチンメンテナンスのガードレール付き自動化。

**特徴**:
- オーファンリソースの安全な特定と段階的クリーンアップ
- コスト調査の定型クエリパターン
- エンジニアがベストプラクティスに従いやすくする

**例**:
- `<resource>-orphans` — 孤立Pod/Volumeの検出→Slack通知→浸透期間→ユーザー確認→連鎖クリーンアップ
- `dependency-management` — 組織の依存関係承認ワークフロー
- `cost-investigation` — 「ストレージ/エグレス料金が急騰した理由」の調査クエリパターン

## 9パターンの全体像

| # | 型 | 焦点 | 自動化度 | 外部依存 | メモリ利用 |
|---|-----|------|---------|---------|-----------|
| 1 | Library & API Reference | 知識注入 | 低 | 低（静的ファイル） | 不要 |
| 2 | Product Verification | 品質保証 | 高 | 高（Playwright/tmux） | 中（動画出力） |
| 3 | Data Fetching & Analysis | データ接続 | 中 | 高（認証・DB） | 中（クエリ結果） |
| 4 | Business Process | ワークフロー | 高 | 高（チケット・Slack・GitHub） | 高（ログ履歴） |
| 5 | Code Scaffolding | コード生成 | 中 | 中（フレームワーク） | 不要 |
| 6 | Code Quality & Review | 品質強制 | 中〜高 | 低（静的解析） | 低 |
| 7 | CI/CD & Deployment | デプロイ自動化 | 高 | 中（CI/Git） | 中（デプロイ履歴） |
| 8 | Runbooks | 障害対応 | 中 | 高（監視・ログ） | 中（調査レポート） |
| 9 | Infrastructure Operations | インフラ保守 | 中 | 中（クラウドAPI） | 高（クリーンアップ履歴） |

## 設計原則（Tips for Making Skills）

### 1. 自明なことを書かない（Don't State the Obvious）

Claude Codeはコードベースをよく知っており、Claudeはコーディングのデフォルト意見を持っている。Skillは**Claudeを通常の思考パターンから押し出す情報**に集中する。

> "The frontend design skill was built by iterating with customers on improving Claude's design taste, avoiding classic patterns like the Inter font and purple gradients."

### 2. Gotchasセクションが最も高シグナル

「Claudeが実際に遭遇した失敗ポイント」を蓄積したGotchasセクションが、Skillの情報価値の大部分を占める。**時間をかけて継続的に更新する**のが理想。

### 3. ファイルシステムによるProgressive Disclosure

> "A skill is a folder, not just a markdown file."

- 詳細な関数シグネチャを `references/api.md` に分離 → 必要なときだけClaudeが読み取る
- 出力がMarkdownならテンプレートを `assets/` に配置 → コピーして使用
- Claudeに「どんなファイルがあるか」を伝えれば、適切なタイミングで読み取る

### 4. Claudeをレールに嵌めすぎない（Avoid Railroading）

Skillsは再利用性が高いため、**指示を具体的にしすぎない**。Claudeに必要な情報を与えるが、状況に応じて適応する柔軟性を残す。

### 5. セットアップ設計（Think through the Setup）

ユーザー固有の設定が必要なSkill（例: Slackのどのチャンネルに投稿するか）は、`config.json`に保存するパターンが有効:
- 未設定ならClaudeがユーザーに質問
- 設定後は再利用

### 6. Descriptionフィールドはモデル向け

Claude Codeは起動時に全Skillのdescription一覧を構築し、「このリクエストに使えるSkillはあるか」をスキャンする。つまり description は**要約ではなく、トリガー条件の記述**。

### 7. メモリとデータ永続化

- `standups.log`に過去の全投稿をappend → 次回実行時に差分把握
- `${CLAUDE_PLUGIN_DATA}` はSkillアップグレード時も消えない安定パス
- シンプルなログファイルからSQLiteまで、複雑さは任意

### 8. スクリプト提供とコード生成

> "One of the most powerful tools you can give Claude is code."

- データ取得のヘルパー関数群を提供 → Claudeはそれらを合成して高度な分析を実行
- 「火曜日に何が起きた？」というプロンプトに対し、Claudeがその場でスクリプトを生成・実行

### 9. オンデマンドHooks

常時ONだと煩わしいが、時には極めて有用な制約:
- `/careful` — 本番環境操作時のみ危険コマンドをブロック
- `/freeze` — デバッグ中、特定ディレクトリ外の編集をブロック

## 配布パターン（Distributing Skills）

| 方法 | 適する規模 | トレードオフ |
|------|-----------|-------------|
| **リポジトリチェックイン** (`./.claude/skills/`) | 小規模チーム・少数リポジトリ | Skillが増えると全員のコンテキストを圧迫 |
| **Pluginマーケットプレイス** | 大規模組織 | 各開発者が必要なSkillだけインストール可能 |

### マーケットプレイス運用

- **中央集権的な選定チームは置かない**: 最も有用なSkillを有機的に発見
- **Sandbox→トラクション→PR→マーケットプレイス**: まずGitHubのsandboxフォルダにアップロードしSlack等で共有。十分なトラクションが得られたらマーケットプレイスへのPR
- **キュレーションは必須**: 質の低い重複Skillが容易に作れてしまうため、リリース前の審査プロセスが重要

### Skillsの合成（Composing Skills）

依存関係のネイティブ管理はまだないが、他のSkillを名前で参照すればモデルがインストール済みSkillを呼び出す:
- 「CSV生成Skill」が「ファイルアップロードSkill」を参照
- モデルが自律的に連鎖実行

### Skillsの計測

PreToolUseフックでSkill使用状況をログ:
- 人気Skillの発見
- 期待より発動が少ない（undertriggering）Skillの特定

## See Also

- [[concepts/agent-skills-overview]] — Agent Skills 概念クラスターマップ（親ページ）
- [[concepts/agent-skills]] — Agent Skills オープン標準（Anthropic Engineering）
- [[concepts/skill-architecture-patterns]] — Self-Authored vs Governed（Hermes Agent vs OpenClaw）
- [[concepts/agent-harness]] — Agent Harness全体像
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/claude-code-best-practices]] — Claude Code運用のベストプラクティス
- [[entities/thariq-shihipar]] — 著者
- [[concepts/skill-graph]] — Skill Graphアーキテクチャ
