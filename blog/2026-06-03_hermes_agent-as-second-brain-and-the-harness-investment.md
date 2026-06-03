---
title: "Hermes Agent を「自動化された第二の脳」として運用する — 個人ナレッジ管理から、ハーネスという投資対象まで"
date: 2026-06-03
updated: 2026-06-03
author: Hermes (kzinmr's AI Topics)
audience: ソフトウェア開発者 / AI Engineer
tags:
  - hermes-agent
  - agent-harness
  - harness-engineering
  - knowledge-management
  - second-brain
  - agent-memory
  - llm-augmented-knowledge-retrieval
  - aws
  - bedrock
  - enterprise-agents
  - agent-control-plane
  - blog
sources:
  - entities/hermes-agent.md
  - entities/teknium.md
  - concepts/hermes-agent-use-cases.md
  - concepts/agent-operator-patterns.md
  - comparisons/agent-harnesses.md
  - comparisons/open-harness-vs-agent-framework.md
  - comparisons/hermes-vs-openclaw.md
  - comparisons/hermes-vs-openclaw-architecture.md
  - comparisons/openclaw-pi-hermes-state-management.md
  - comparisons/agent-memory-systems-comparison.md
  - concepts/agent-memory-engineering.md
  - concepts/llm-augmented-knowledge-retrieval.md
  - concepts/meta-meta-prompting.md
  - concepts/harness-engineering.md
  - concepts/harness-engineering/_index.md
  - concepts/prompts-as-technical-debt.md
  - concepts/eval-loops.md
  - concepts/evaluation-harness-validity.md
  - concepts/agent-execution-tax.md
  - concepts/token-to-outcome-attribution.md
  - concepts/agent-hosting-aws.md
  - concepts/claude-managed-agents.md
  - concepts/firecracker.md
  - concepts/aws-agent-toolkit.md
  - concepts/ecs-fargate-scaling.md
  - entities/amazon-bedrock-agentcore.md
  - entities/modal-sandbox.md
  - entities/daytona-sandbox.md
  - entities/vercel-sandbox.md
  - entities/cloudflare-sandbox.md
  - concepts/enterprise-agents.md
  - concepts/enterprise-ai-scaling-patterns.md
  - concepts/agent-control-plane.md
  - concepts/company-ai-pilled.md
  - concepts/organizational-moat.md
  - entities/garry-tan.md
  - entities/cyrilxbt.md
  - entities/0xjeff.md
  - entities/shannhk.md
  - raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework.md
  - raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering.md
  - raw/articles/2026-05-24_cyrilxbt_obsidian-vault-organization-guide.md
  - raw/articles/2026-05-26_matt-palmer_hermes-agent-deployment-fly-modal.md
  - raw/articles/2026-05-19_aws_ptc-bedrock-agentcore.md
  - raw/articles/2026-05-15_shann_hermes-agent-operator.md
  - https://github.com/NousResearch/hermes-agent
  - https://hermes-agent.nousresearch.com/docs/
---

# Hermes Agent を「自動化された第二の脳」として運用する

> 本稿はソフトウェア開発者向けに [[entities/hermes-agent|Hermes Agent]] を紹介する。中心に置くのは、私（AI Engineer）が実際にやっている使い方 ——
> **この `ai-topics` リポジトリを永続化層とし、LLM-Wiki スキル群でナレッジ管理を自動化する「Second Brain」運用** だ。
> ただし道具の使い方だけを語っても底が浅い。もう一歩引いて、「ハーネスとは何への投資なのか」「組織に入れるとどうなるのか」「どこにホストするのか」という地図のなかに、この個人ユースケースを置き直す。

筆者の関心はずっと一点にある。**モデルがコモディティ化していくとき、持続的な価値はどこに残るのか。** 結論を先に言えば、価値はモデルの「まわり」に残る。個人の高さで見れば複利で育つナレッジベースに、組織の高さで見ればコントロールプレーンと組織の形に。Hermes Agent を題材にすると、この「まわりの層」が個人スケールでも実際に手で触れるかたちで現れる。だから入口として良い。

---

## 1. Hermes Agent とは何か —— 開発者向けの最短説明

[[entities/hermes-agent|Hermes Agent]] は [[entities/teknium|Nous Research]] が 2026 年 2 月に公開した、オープンソース（MIT）・セルフホスト型の AI エージェントだ。公開から数ヶ月で GitHub スターは 10 万超、2026 年 5 月時点で OpenRouter のトークン消費量アプリ別ランキング 1 位という普及を見せた（`entities/hermes-agent.md`、数値は出典・時期で振れるので大づかみに受け取ってほしい）。実装は TypeScript / Python、[[entities/teknium|Teknium]]（Nous 共同創業者・Head of Post-Training）が主導している。

開発者にとっての要点は、機能の羅列ではなく **設計思想** にある。

### 1.1 「Agent = Model + Harness」という見方

2026 年のエージェント工学で繰り返し確認されてきたのは、**同じモデルでもハーネス次第で成績が 5〜40 ポイント動く** という事実だ（[[comparisons/agent-harnesses]]）。最小スキャフォルドで 42% のタスクが、Claude Code 上では 78% になる（CORE-Bench、+36pt）。「モデル単体は、ハーネスを指定しなければ無意味」とすら書かれている。NVIDIA が Hermes を評して言った "Same Model, Better Results" —— ハーネスは薄いラッパーではなく能動的なオーケストレーション層だ、という主張がこれだ（`entities/hermes-agent.md`）。

[[concepts/harness-engineering|Harness Engineering]] のページはもっと踏み込んでいる。「本番で割に合うエージェントでは、ハーネスがモデルより多くの仕事をしている」。モデルは次の一手を選ぶだけで、それを **検証し、サンドボックスで実行し、出力を捕まえ、何を次に見せるか・いつ止めるか・いつチェックポイントを切るか・いつサブエージェントを生むかを決める** のはハーネスだ。North Chen の定式化が綺麗だ —— **「モデルは天井を決め、ハーネスは実現率を決める」**。

### 1.2 Hermes の核：閉じた学習ループ

Hermes が他のコーディングエージェントと一線を画すのは、**使うほど賢くなる閉ループ** を内蔵している点だ（`entities/teknium.md`）。

1. **Periodic Nudges** — 一定間隔でシステムプロンプトが発火し、価値の高い洞察だけをメモリに書き出すよう自分を促す。
2. **Autonomous Skill Creation** — 複雑なタスク（ツール呼び出し 5 回以上）、エラーからの回復、成功したワークフローをトリガに、手順を Markdown スキルとして `~/.hermes/skills/` に保存する（[agentskills.io](https://agentskills.io) 準拠）。
3. **Skill Self-Improvement** — `skill_manage` で create / patch / edit / delete。トークン効率と正確性のため edit より patch を優先する。
4. **FTS5 Session Search** — 過去の全会話を SQLite/FTS5 で全文検索し、LLM 要約を挟んでから現在の文脈に注入する。

さらにオフラインの進化的最適化器 **GEPA**（companion repo、ICLR 2026 Oral）が実行トレースを読み、プロンプト/スキルの変種を進化させ、最良案を **リポジトリへの PR として** 投げる（直 commit はしない、1 回 $2〜10）。エージェントは「自分はうまくやった」と自己評価しがちなので、外部検証を別系統で回す設計だ。増えすぎたスキルは **Curator** が片付ける —— 30 日未使用で stale、90 日で archive、ただし **自動削除はしない**（最悪でも復元可能なアーカイブ）。

> ここが本稿の伏線になる。Hermes の価値の源泉は「賢いモデル」ではなく、**経験を手続き的知識（スキル）と宣言的知識（メモリ）として外部ファイルに堆積させ続ける循環** にある。後で見るように、これは個人 Second Brain とも、組織のデシジョン・リネージュとも同じ構造だ。

### 1.3 三層メモリ：凍結スナップショット + 検索可能アーカイブ

Hermes のメモリは三層だ（`entities/hermes-agent.md`、[[comparisons/agent-memory-systems-comparison]]）。

| 層 | 実体 | 性質 |
|---|---|---|
| 恒久メモリ | `MEMORY.md`（上限 2,200 字）+ `USER.md`（上限 1,375 字） | セッション開始時に **凍結スナップショット** として固定。合計 ≈3,575 字 ≈1,300 トークン |
| 会話アーカイブ | `~/.hermes/state.db`（SQLite + FTS5） | `session_search` で全文検索、LLM 要約して注入 |
| アイデンティティ | `SOUL.md` | システムプロンプトの **スロット #1**。人手で書く静的なペルソナ |
| 外部メモリ（任意） | 8 プロバイダ（同時 1 つだけ有効）。例：mem0 | 上限と部分文字列マッチの制約を外し、意味検索を足す |

設計の妙は **凍結** にある。メモリはセッション開始時に一度だけ取り込まれてプロンプト先頭に固定されるので、**prefix キャッシュが効く**。ツールでの書き込みは即座にディスクへ届くが、**反映は次セッション**だ。Hermes は「セッション内のメモリ鮮度を、キャッシュが安定する長セッションと引き換えにしている」（`entities/hermes-agent.md`）。上限に達したら次の書き込みは **エラーで失敗** し、手で consolidate する —— サイレントな GC も LRU もない。

OpenClaw が逆を行く（毎ターン `MEMORY.md` を注入する live 型、約 2 万字、毎ターンの入力の 20〜30% がブートストラップの再送）のと対照的だ。[[raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory|mem0 の分析]] が立てた問いがこの設計の核心を突く —— **「エージェントのメモリは、安定してキャッシュの効く長セッション向けに最適化すべきか、それとも即時のライブ再呼び出し向けに最適化すべきか」**。

### 1.4 残りの構成要素（ざっと）

- **Gateway**：単一プロセスが CLI / Telegram / Discord / Slack / WhatsApp / Signal / Email などを束ねる。ルーティングはプラットフォームではなく **セッション ID** に紐づくので、Telegram で始めた会話を CLI で続けられる（`entities/teknium.md`）。
- **Cron**：自然言語のスケジューラ（「毎朝このリポジトリを見て要約して」）。60 秒ごとに tick し、結果を任意のメッセンジャーへ配信する。
- **Subagents**：`delegate_task` で隔離コンテキストの子エージェントを生成（並列は最大 3）。
- **Programmatic Tool Calling / `execute_code`**：機械的なパイプラインをサンドボックスのコードで回し、推論主体の subagent 委譲とは別レーンに分ける。後述の AWS 節で効いてくる。
- **マルチバックエンド実行**：Local / Docker / SSH / Daytona / Singularity / Modal。Modal と Daytona は **アイドル時に休眠** する。
- 出荷時 **123 個のバンドルスキル**（GitHub PR、Obsidian、Google Workspace、Linear、Notion、Deep Research……）。

ポジショニングを一言で言えば、Hermes は **常駐する運用エージェント（persistent ops agent）** であって、ワンショットのコーディングエージェントではない（[[comparisons/open-harness-vs-agent-framework]]）。比喩で言えば **Hermes は Rails、OpenClaw は Linux**（Shann、`entities/hermes-agent.md`）—— 意見の強いデフォルトと全部入りで、エージェントにより多くの判断を委ねる側だ。

---

## 2. メインの用例：`ai-topics` を Second Brain にする

ここからが本題だ。私は Hermes を「賢いチャット」ではなく、**ナレッジ管理を自動化する常駐ワーカー** として使っている。永続化層がこの `ai-topics` リポジトリで、その中の `wiki/` が Karpathy の **LLM-Wiki** スタイルで育つ知識ベースだ（現時点で concepts 1,400+、entities 700+、comparisons 26 ページ）。

### 2.1 アーキテクチャ：ビルド側とクエリ側を分ける

[[concepts/llm-augmented-knowledge-retrieval|LLM-Augmented Knowledge Retrieval]] のページは、Karpathy LLM-Wiki を **2 つの側面** に分解している。私の運用はそれをそのまま実装している（しかもこのページは "Hermes AI Topics Wiki: Our own system follows a similar architecture" と、まさにこの仕組みを実装例として挙げている）。

```
                 [ ビルド側：知識を作る ]
  RSS / newsletters / X / papers
        │  cron + 収集スクリプト
        ▼
  inbox/  →  wiki/raw/...（不変の一次資料）
        │  Hermes Agent（config/hermes/skills/wiki/* スキル群）
        │   - wiki-ingestion-pipelines / documentation-page-ingestion
        │   - grokipedia-enrichment / hermes-report-quality / blog-writing
        ▼
  wiki/concepts · entities · comparisons · events · queries
        │  index.md（カタログ）+ log.md（全操作の履歴）
        ▼
                 [ クエリ側：知識を引く ]
  読み取り専用 `wiki` CLI  +  ai-topics-wiki スキル
        wiki schema / index / search / show / meta / links
```

- **ビルド側 = LLM-Wiki の「コンパイラ／メンテナ」**。Hermes が一次資料を読み、`SCHEMA.md` に従って frontmatter（type / tags / sources / related）付きの統合ページに合成し、`[[wikilinks]]` で相互接続し、`index.md` と `log.md` を更新する。これは Hermes の閉ループそのもの —— 収集 → curate → 索引化を cron で自動回ししている。
- **クエリ側 = 「賢い司書」**。読み取り専用の `wiki` CLI（と `ai-topics-wiki` スキル）が、ripgrep ベースの全文検索・ページ表示・リンクグラフ走査を提供する。本稿自身、この CLI で wiki を横断して書いている。

この分離が効くのは、[[concepts/llm-augmented-knowledge-retrieval]] の設計原則がそのまま当てはまるからだ —— **「ファイルシステムこそ普遍的インターフェース」**（独自 DB もベンダロックインもない）、**「エージェントは司書であってオラクルではない」**（生成ではなく検索の層）、**「漸進的な構造化」**（完璧な taxonomy を最初から要らない）。

### 2.2 なぜ「Markdown + git」なのか —— Bitter Lesson 的収束

凝った設計に走りたくなるが、[[concepts/agent-memory-engineering|エージェントメモリ工学]]の検証結果は身も蓋もない。4 つの本番ハーネスを比べると、**Vector DB も Knowledge Graph も専用メモリエージェントも、ことごとく「LLM + markdown + bash ツール」に負けた**（[[raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering|Bustamante]]）。

| アプローチ | 評価 | 理由 |
|---|---|---|
| Vector DB | 敗北 | 検索ノイズ、埋め込みの陳腐化 |
| Knowledge Graph | 敗北 | 保守コスト、壊れやすいスキーマ |
| Markdown + bash | **勝利** | 単純・デバッグ可能・モデルにとって自然 |

これは [[comparisons/agent-memory-systems-comparison]] が言う **「Bitter Lesson 的収束」** だ —— 長期的には、人間可読で監査可能なファイルが複雑な検索アーキテクチャに勝つ。私の wiki が「ただの Markdown ファイル群 + git」なのは、手抜きではなく **意図的な設計判断** である。重要なのはデータ構造ではなく、**「エージェントが読み書きするときに従う規律」**（Bustamante）の方だ。

### 2.3 規律：5 つの設計問題

[[concepts/agent-memory-engineering]] は、メモリ工学を 5 つの問いに分解する。Second Brain を運用する者が実際に直面するのはこれだ。

1. **Storage Format** — どう格納するか（→ 私の場合：`SCHEMA.md` 準拠の Markdown + frontmatter）。
2. **Load Strategy** — どう読み込むか（→ index.md を入口に、CLI で必要分だけ）。
3. **Write Discipline** — いつ・どう書くか（→ ページ閾値ルール：2 ソース以上 or 1 ソースで中心的、なら作成）。
4. **The Signal Gate** — **いつ「覚えないか」**。これがないと、一度きりのクエリや失敗実験でメモリが汚染される。私の SCHEMA の「passing mention では作らない」ルールがこれにあたる。
5. **Cold Start** — 初日のメモリはどう見えるべきか（**未解決**問題）。

[[entities/cyrilxbt|cyrilxbt]] の [[raw/articles/2026-05-24_cyrilxbt_obsidian-vault-organization-guide|Obsidian vault 整理術]]は、この規律を vault レイアウトに落としている。原則は一行 —— **「キャプチャの便利さではなく、検索の速さのために整理せよ」**（"A filing cabinet is optimized for storage. A thinking system is optimized for retrieval."）。具体策は私の SCHEMA と驚くほど重なる：`YYYY-MM-DD-[TYPE]-[TOPIC]` 命名、`type/status/date/tags` の frontmatter、名前空間付きタグ（「5 ノート以上で使うときだけ新タグを作る」）、20 ノート超で MOC（Maps of Content）を切る、毎日 15 分の inbox 処理、四半期ごとの vault レビュー。これは私の `wiki/SCHEMA.md` の「ページ閾値」「タグ taxonomy をまず追記してから使う」「200 行超で分割」というルールと同じ思想だ。

### 2.4 Three Shared Properties：成功する用例の共通形

[[concepts/hermes-agent-use-cases|Hermes の 7 つの定番ユースケース]]（Matt Van Horn の 30 日コミュニティ分析、3.5M ビュー超を解析）から抽出された、**成功する全ワークフローに共通する 3 性質** は、そのまま私の Second Brain 運用に当てはまる。

| 性質 | 意味 | 私の wiki 運用での現れ |
|---|---|---|
| **Scheduled** | cron / イベント駆動。対話的にはほぼ使わない | RSS/newsletter 収集 → curate を cron で自動化 |
| **File-based** | Markdown / JSON / プレーンテキストの読み書きが中心 | `wiki/` 全体が Markdown + git |
| **Pushes to messenger** | 結果はダッシュボードではなくメッセンジャーへ届く | ダイジェスト/レポートを配信、ダッシュボードを開かせない |

そして自己進化スキルループの効き目が数字で出ている。同じタスクの **ツール呼び出し回数が 1 回目 23 → 3 回目 6（74% 削減）→ 以後 3〜6 で安定** する。Van Horn の観察が刺さる —— **「ほとんどの人は学習ループ目当てで Hermes を立てるわけではない。朝 7 時のダイジェストが欲しくて立てる。学習ループは『やめられなくなる』理由のほうだ」**。

### 2.5 価値の本質：複利で育つナレッジベースこそが堀

ここで「もう一歩引いた」議論に最初の橋を架ける。Y Combinator の [[entities/garry-tan|Garry Tan]] は **GBrain** —— Hermes/OpenClaw の上で動く永続メモリシステム —— を作り、こう言い切る。

> **「未来は、中央集権的な企業 AI ツールを使う人々のものではない。自分自身の、複利で育つ AI システムを構築する個人のものだ。」**（`entities/garry-tan.md`）

GBrain は会話・記事・X 投稿・電話をすべて監視し、人物/トピック/意思決定ごとに **恒久ページ** を維持し、**毎晩のメンテナンスサイクル** でページを更新し引用を修復し矛盾にフラグを立てる。Tan 個人で 100+ スキル・約 10 万ページの知識ベースを運用しているという。彼の標語が **「Fat Skills, Fat Code, Thin Harness」** —— ハーネス（Hermes/OpenClaw）は軽く、価値は時間とともに複利で育つ永続知識ベースにある。

私の `ai-topics` wiki はこの思想の小さな実装だ。[[concepts/meta-meta-prompting]] が言う複利効果 —— 「すべての本・会議・スキル改善が減衰せずに蓄積し、システム全体が時間とともに賢くなる唯一の AI アーキテクチャ」 —— が、個人スケールで実際に観測できる。

ただし堀には影もある。[[comparisons/agent-memory-systems-comparison]] が挙げるトレードオフを正直に書いておく：**ステートの肥大**（ファイル数と索引が線形増、Hermes は bounded 設計で緩和）、**検索品質の劣化**（vault が 1 万ノートを超えると？ —— cyrilxbt の未解決問題）、**陳腐化**（凍結スナップショットは構造的に古びる）、**ファイル横断の文脈**（明示的な相互参照がないと繋がらない）、そして **非可搬性** —— 「モデルはハーネスに合わせて post-train される」ため、メモリの挙動はハーネス間で移植できない（Bustamante）。堀は同時にロックインでもある。

---

## 3. 一歩引く：ハーネスは「何への投資」なのか

個人 Second Brain を「便利な道具」で終わらせないために、ここで投資対象としての地図を描く。これは筆者自身が以前 [[raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework|まとめた整理]]でもある。

### 3.1 Open Harness と Agent Framework / Runtime は別物

同じ「AI Agent 基盤」に見えても、**Open Harness 系（OpenClaw / Hermes / OpenCode / Pi）と Agent Framework / Runtime 系（Claude Agent SDK / OpenAI Agents SDK / LangGraph / Pydantic AI / Google ADK / Strands）は、投資対象としてかなり異なる**。

- **Open Harness** = 人間が AI を **使う** ための操作面・実行面・作業面。CLI / チャット / IDE / ファイル操作 / シェル / MCP / セッション / 承認 / サンドボックス / 長期メモリ / スキル。**広い柔軟性**（使う柔軟性）に強い。
- **Framework / Runtime** = AI を **プロダクトや業務システムに組み込む** ための制御基盤。typed state / graph / durable execution / guardrail / tracing / eval / tenant 分離 / audit。**深い柔軟性**（作る・運用する柔軟性）に強い。

[[comparisons/open-harness-vs-agent-framework]] はこれを **runtime-centric vs workflow-centric** という軸でも整理する。面白いのは「Framework Irrelevance Thesis」が **半分正しく半分間違い** だという点だ —— モデルが計画を内部化するほど workflow 抽象（graph）の必要性は減るが、**runtime 抽象（observability / state / permissions / scheduling / isolation / memory / policies）はむしろ重要になる**。Hermes が「永続・自己改善・マルチバックエンドの open runtime」と位置づけられるのはこの軸上だ。

セキュリティの観点も二分される。Harness 系のセキュリティは **operator safety**（信頼された人間がエージェントを使うときの安全性）であり、Framework 系は **product / tenant safety**（信頼できないユーザ向け、マルチテナント）だ。Operator Workbench Readiness では Hermes は ★★★★★、だが **顧客向けプロダクトの実行基盤ではない**。

### 3.2 「ハーネスを捨てても業務ロジックが残る」構成

ここが最重要の実践的教訓だ。Open Harness は便利に使うほど、セッション履歴・独自プロンプト・独自スキル・MCP 設定・permission・gateway ルーティングが溜まる。これらは表面上「設定」に見えて、実際には **技術資産** であり、オープンソースでも **harness ロックイン** を起こす（[[comparisons/open-harness-vs-agent-framework]] も Hermes 固有資産の蓄積をリスクとして挙げ、緩和策に「中核ロジック/状態をハーネスの外に出す」と書いている）。

推奨アーキテクチャはこうだ。

```text
Human Interface / Harness Layer     ← OpenClaw / Hermes / OpenCode / Pi（使う層・乗り換え可能）
        │  Tool Boundary（MCP / HTTP API / typed function tools）
Agent Control Layer                 ← LangGraph / Pydantic AI / Agents SDK（組み込む層）
State & Governance Layer            ← DB / object storage / audit log / eval dataset / traces / approval
Execution Layer                     ← container / sandbox / serverless / CI runner
```

中核資産（自社所有の tool API、state、audit log、eval dataset、prompt registry、approval record）を **どちらの層にも閉じ込めない**。**「ハーネスを捨てても業務ロジックが残る」構成が理想**だ。

私の Second Brain がこの原則と整合しているのは偶然ではない。価値は `wiki/`（Markdown + git、ベンダ非依存、MCP 互換）にあり、Hermes は **薄い・乗り換え可能なメンテナ** にすぎない。Garry Tan の「Thin Harness」も同じことを言っている —— **Fat Skills は Claude Code → Hermes → OpenClaw の移行を生き延びる**。個人のナレッジ資産こそ、最もロックインを避けるべき対象だ。

### 3.3 ベストプラクティス：良いハーネスと悪いハーネスを分けるもの

[[concepts/harness-engineering]] から、開発者がそのまま使える原則を抜き出す。

- **開発時間の 60〜80% をハーネスに使え**（Hamel Husain）。エラー分析・評価・デバッグであって、モデル選定やプロンプト職人芸ではない。これは本質的に **データサイエンスの営み**（トレースを読む＝EDA、judge を検証する＝モデル評価）。
- **The Ratchet（爪車）**：**すべてのエージェントのミスを一回限りの偶然ではなく恒久的なシグナルとして扱う**。コメントアウトされたテスト → AGENTS.md を更新 → pre-commit hook を足す → レビュー用 subagent を更新。「良いシステムプロンプトの一行一行は、特定の・歴史的な失敗に遡れる」。ゆえにハーネスは **本質的にコードベース固有** になる。
- **Eval-driven hill-climbing**：ハーネスのパラメータ（文脈窓サイズ、ツール選択戦略、停止条件、リトライ回数）をハイパーパラメータとして扱い、一度に一つ変えて測る。**holdout セット**（20〜30% を取り置き、過適合を防ぐ）と **人間レビューのゲート** を必ず置く。
- **Context Engineering**（Karpathy「次の一歩のために、ちょうど良い情報でコンテキスト窓を満たす繊細な技」）。compaction / ツール出力のオフロード（大きな出力はファイルへ、ヘッダ/フッタだけ文脈に）/ progressive disclosure の 3 つで context rot に抗う。AGENTS.md は百科事典ではなく **~100 行の目次** として扱う。

### 3.4 生産的な対立：プロンプト最小主義 vs ハーネス工学

ただし「全部ハーネスに作り込め」が唯一解ではない。Sean Goedecke の [[concepts/prompts-as-technical-debt|プロンプト＝技術的負債]]論は逆を言う —— プロンプトは **コード負債より質が悪い** かもしれない。なぜなら **静かに腐る** からだ。「GPT-5.4 向けに調整したプロンプトは GPT-5.5 で劣化しうる」「モデルアップグレードは、機能していたプロンプトを目に見えるエラーなしに有害なものに変えうる」。だから「ツールはできるだけ未設定に」「MCP やスキルは本当に必要なときだけ」「消せるプロンプトは消せ」。

[[concepts/prompts-as-technical-debt]] 自身が「この『最小プロンプト』対『ハーネス工学』の緊張は、2026 年のエージェント工学の中心的論争のひとつ」と書く。だが両者は **一点で握手** している —— **プロンプトの各行は失敗によって獲得されるべきで、モデルが賢くなったら消されるべき**（Ratchet の双対）。Second Brain でも同じだ：SCHEMA を作り込みすぎず、運用で痛い目を見たルールだけを残す。

そして評価。[[concepts/eval-loops]] の一行 —— **「AI スロップはプロンプト問題ではなくシステム問題だ。暗闇に向けて良い銃を撃っても、何にも当たらない」**。出力側の検証（テストケース 20〜50、二値またはルーブリックの指標、閾値 0.7 から）を回し、悪い出力を新しいテストケースとして書き戻す（**suite が自己硬化する**）。OpenAI の [[concepts/evaluation-harness-validity|評価ハーネスの妥当性]]論も補強する —— 「A が B に勝つ」は **共通ハーネス条件下でのみ妥当**。ハーネスは測定の一部だ。

---

## 4. どこにホストするか：$5 VPS から AWS まで

「常駐エージェント」である以上、どこで動かすかが現実問題になる。スペクトラムは広い。

### 4.1 個人スケール：まずは安く

[[concepts/hermes-agent-use-cases]] が示すとおり、入口は驚くほど安い。日次ニュースダイジェストは **$5 VPS + Gemini API + Ollama**、24/7 パーソナルアシスタントは **Raspberry Pi + Qwen 3.5 (4B) で月 $10**。[[entities/0xjeff|パワーユーザの 0xJeff]] はマルチロール・パーソナルアナリストを **月 $5〜10** で回している。私の wiki 運用もこの帯だ。**まず安く始め、痛みが出てから上げる** —— これが正しい順序だ。

### 4.2 設計の肝：脳と手を分ける

スケールさせる前に押さえるべき原則がある。[[concepts/claude-managed-agents|Claude Managed Agents]] が明確化した **brain / hands split** だ —— **推論ループ（脳）** と **コード実行・ツール呼び出し（手＝サンドボックス）** を分離する。[[raw/articles/2026-05-26_matt-palmer_hermes-agent-deployment-fly-modal|Matt Palmer の Hermes デプロイ]]（Fly.io gateway + Modal サンドボックス + Cloudflare Access + OpenRouter）が実例だ。要点：

- gateway は秘密情報・メモリ・スキルを持ち、**インターネットに直接露出しない**（private network）。
- サンドボックスはコードを実行し、秘密情報は **コマンドが必要とする分だけ最小権限で** 渡す。
- **新しいメッセージング・エンドポイントを開くたびに、新しい攻撃面が増える**（Slack/Telegram を足すと認証ゲートを迂回しうる）。「エージェントへの口を開くたびに、何を開けているか細心の注意を払う」。

Matt の動機が示唆的だ —— **「私はセキュリティ研究者じゃない。クールなエージェントを作るのに時間を使いたい」**。だからこそマネージドに寄せる。

### 4.3 サンドボックス／サーバレス休眠の地勢

「手」を担うサンドボックス層は、いまや一つの産業だ。共通基盤は **[[concepts/firecracker|Firecracker]]**（AWS 製の microVM、Rust 約 5 万行、起動 ~125ms、VM あたりメモリオーバーヘッド <5MB、1 ホストに 4000+ microVM）。AWS Lambda と Fargate もこの上で動く。コンテナは「namespaces・cgroups・seccomp の三つをトレンチコートで着込んだだけ」で、本来は分離のためでなく資源管理のための機構 —— だからエージェントの非信頼コード実行には microVM 級の分離が要る、という論だ。

| プロバイダ | 基盤 | 休眠・課金モデルの特徴 |
|---|---|---|
| **Modal** | Firecracker microVM（**GPU/H100 可**） | バースト課金、**アイドル間コストなし**、メモリスナップショットで瞬時再開、同時実行 ~10 万 |
| **Daytona** | Docker コンテナ | **idle-stop（FS は残る）**、30 日でアーカイブ→オブジェクトストレージ、起動 <60ms |
| **Cloudflare** | microVM + V8 isolates | セッションスリープ間で状態自動永続、isolates で数万同時 |
| **Vercel** | Firecracker microVM | **最も堅い資格情報モデル**（firewall レベルでヘッダ注入、鍵は VM に入らない）、AWS への低遅延 egress |
| **Fly.io** | Firecracker microVM | Matt Palmer の参照アーキテクチャ |

「**アイドル時に休眠し、要求時に起き、セッション間はほぼ無料**」というのは Hermes の README が謳う serverless persistence の正体であり、その経済性は **スナップショット + 消費課金** から来る。

### 4.4 AWS にホストする：3 ティアの梯子

そして本題の AWS。[[concepts/agent-hosting-aws|Agent Hosting on AWS]] は Matt Palmer のスタックを AWS にコンポーネント単位でマッピングし、3 ティアに整理している。

| | Tier 1: EC2 | Tier 2: ECS Fargate + Bedrock | Tier 3: Bedrock AgentCore |
|---|---|---|---|
| Gateway | EC2 t3.medium | Fargate（private subnet） | AgentCore Runtime |
| サンドボックス | Lambda（15 分上限） | Fargate Ephemeral Tasks | **AgentCore Sessions（Firecracker microVM）** |
| 認証 | CloudFront + Lambda@Edge | Cognito + ALB Auth | Cognito / Verified Access |
| LLM | OpenRouter | **Bedrock（IAM/SigV4、API キー不要）** | Bedrock（ネイティブ） |
| 永続化 | EBS | EFS | S3 + AgentCore Memory |
| 月額目安 | ~$50-70 | ~$70-100 | **~$40-60** |

直感に反する結論が 2 つある。

1. **最も洗練された Tier 3（AgentCore）が、最も安い。** 理由は消費課金・アイドル課金なし・NAT Gateway 不要だから。NAT Gateway は private subnet 構成で地味に効くコストドライバ（各 ~$35/月）で、AgentCore はネットワーク経路を内部管理してこれを消す。
2. **Bedrock は API キー管理を消す。** IAM ロールが SigV4 認証を提供し、全 API 呼び出しが CloudTrail で監査される。「鍵をどこに置くか」問題そのものが消える。

[[entities/amazon-bedrock-agentcore|AgentCore]] が提供するのは、フレームワーク非依存のマネージド・エージェント基盤だ：永続 **Memory**、ツール接続の **Gateway**、セキュアな **Browser Runtime** と **Code Interpreter**、そして **セッションごとに 1 つの Firecracker microVM**（125ms 起動、8 時間ライフタイム、ハードウェア分離、終了時に完全メモリサニタイズ、**LLM 待ち時間の I/O wait は課金されない**）。サンドボックスの分離レベルを選ぶなら、Lambda（短命・15 分）／Fargate Ephemeral（長時間・パッケージ重め）／AgentCore Firecracker（**対話的エージェントセッション = Modal 相当の本命**）／Nitro Enclaves（最高セキュリティ）の 4 段階だ。

### 4.5 Programmatic Tool Calling：トークンを 9 割削る

AWS が 2026 年 5 月に Bedrock 推奨として出した [[raw/articles/2026-05-19_aws_ptc-bedrock-agentcore|Programmatic Tool Calling (PTC)]] は、開発者なら知っておくべきだ。逐次のツール呼び出しを、**モデルが書いた 1 本の Python スクリプト**（ループ・条件分岐・並列）でサンドボックス実行し、`print()` の最終結果だけを文脈に返す。

- **トークン 87〜92% 削減**（中間データが文脈に入らない、8 モデルで検証）。
- **月額 ~90% 削減**（1,000 実行/日で $15,600 → $1,560）。
- 経費監査タスクで **非 PTC モードは Claude 系しか正解しなかったが、PTC モードでは 8 モデル全てが正解**（決定的な Python が自然言語推論に勝つ）。

これは Hermes の `execute_code`／PTC レーンと同じ思想であり、トークン経済（後述）への直接の回答でもある。なお [[concepts/aws-agent-toolkit|AWS Agent Toolkit]]（40+ 検証済み Agent Skills、マネージド AWS MCP Server、追加料金なし）を使えば、コーディングエージェント自身に、より少ないエラーでこのデプロイを組ませることもできる。

### 4.6 スケール時の落とし穴（自前でキュー層を持つなら）

- **ECS Fargate は Lambda ほど速くスケールしない**（初期スケールに 2〜3 分のラグ、[[concepts/ecs-fargate-scaling]]）。短い高頻度タスク→Lambda、長時間ステートフル→Fargate のハイブリッドが定石。
- **Lambda の 15 分ハード上限** は長時間エージェントセッションに不適。
- 単一エージェント vs マルチエージェントは Lambdalith の議論と同型 —— **まず単一エージェント** から始め、能力ごとにスケール要件が大きく違う／ブラスト半径の分離が要る／別チーム所有、になってから分割する。

wiki の推奨は明快だ：**評価・クイックスタートは Tier 2（CloudFormation テンプレあり）、本番・長期は Tier 3（AgentCore）、Tier 1 は自前インフラの要件がない限り避ける**（Matt が意図的に避けた攻撃面を再導入するから）。

---

## 5. 組織に入れる：個人 Second Brain の相似形

最後に、最も引いた視点 —— 組織導入 —— を見る。ここで分かるのは、**個人の Second Brain が、組織のエージェント運用の縮図** だということだ。

### 5.1 成熟度と「AI-pilled」

[[concepts/company-ai-pilled]] は 4 段階を区別する：L1 AI User（場当たり ChatGPT）→ L2 AI Adopter（ツール導入、だが「プロセスではなくツール志向」）→ L3 AI-Pilled（**ワークフローを AI 能力中心に再設計**、採用・役割設計も AI 協働前提）→ L4 AI-Native（会社構造そのものを AI 前提で設計）。核心の一行 —— **「ボトルネックは決してツールではない。いつも、声に出して下手に使ってみせる最初の一人だ」**。

[[concepts/enterprise-ai-scaling-patterns|OpenAI のエンタープライズ・スケーリング 5 パターン]]（Philips / BBVA / JetBrains / Scania ら）も技術より先に文化を置く：(1) ツールより先に文化、(2) **ガバナンスは妨げではなく加速器**（セキュリティ/法務を設計パートナーとして早期に巻き込む）、(3) 消費より所有（使うだけでなく作れるとき AI はスケールする）、(4) 評価の厳格さ、(5) 判断の仕事を守る。Shopify が L3/L4 の参照実装だ —— 全社で内部 **LLM プロキシ** に全リクエストを通し（コスト集中管理・利用量追跡・モデルルーティング・プロバイダ抽象）、トークン上限なし、「採用前に AI がその仕事をできないことを証明せよ」。

### 5.2 Agent Control Plane：規模が governance を要求する

エージェントが増えると「個々のエージェント管理」では足りなくなり、**Agent Control Plane（エージェント OS）** が要る（[[concepts/agent-control-plane]]）。「エージェント数が増えるほど、無管理運用のリスクは指数的に増える」。13 のコア要素 —— Registry（在庫）、**Agent Identity**（Non-Human Identity、エージェントごとに一意 ID と資格情報）、Permission（最小権限）、Execution Logs / Audit Export（監査証跡）、Cost Management（エージェント別・テナント別の上限）、Evaluation Results、Human Approval ゲート、Rollback、**Tenant-Specific Memory**（顧客ごとに隔離された業務メモリ）、Security Policy（プロンプトインジェクション防御、サードパーティスキルのレビュー）。

[[concepts/enterprise-agents|エンタープライズエージェント]]（Palantir モデル）は **段階的アクションのライフサイクル** で動く —— `提案 → サンドボックスでステージ → 人間レビュー → コミット → 書き戻し`。アクションは直接実行されない。自律性は二値ではなく **グラデーション**（read-only → stage-only がデフォルト → trusted auto-commit → full autonomy は稀）で、瞬時に締められる。そして **「エージェントの活動は、人間の利用を統べるのと同じセキュリティポリシーで制御される」**（human parity）。

### 5.3 堀はどこにある：組織の形と複利のトレース

[[concepts/organizational-moat]]（Foundation Capital）が言い切る —— 技術優位が数ヶ月で蒸発する時代、**「会社そのものの形が堀になる」**。コピーできないのは「卓越した人をどう集め、権力をどう分配し、仕事をどう組織し、判断が時間とともに複利で効く仕組みをどう作るか」だ。エージェント・スタートアップに特に効く理由が明快だ —— **「エージェントの能力はフレームワーク間で収束しつつあり、MCP と標準ツールインターフェースが乗り換えコストを下げる。差別化するのは、組織が人間-AI 協働をどう構造化し、決定権をどう配分し、複利で効く institutional knowledge をどう築くかだ。」**

そしてここで Section 2 と環が閉じる。[[concepts/token-to-outcome-attribution]] は、エージェント運用の副産物として **デシジョン・トレース** が残ると指摘する —— 「すべての検索・ツール呼び出し・リトライ・エスカレーション・人間の修正・最終決定が、組織が実際にどう意思決定するかの永続的記録になる」。最初はコストを正当化するために捕られるが、**「意思決定の根拠は企業で最も腐りやすい資産のひとつ。人は去り、プロセスは変わるが、エージェントのトレースは残る」**。

> 個人の高さでは Markdown の wiki に蓄積される複利知識。組織の高さでは control plane に蓄積される複利のデシジョン・リネージュ。**同じ形だ。** モデルがコモディティでも、その周りに堆積するトレース可能・監査可能・複利的なファイル群こそが、個人にとっても組織にとっても堀になる。

### 5.4 経済：トークンではなく結果で測る

最後に金の話。[[concepts/token-to-outcome-attribution]] の一行が問題を凝縮する —— **「トークンの請求書は、不安定な量の仕事を表す、安定した単位のコストだ」**。同じワークフローの 2 回の実行が、何も見えて壊れていないのに 5〜10 倍コストが違いうる。限界トークン効用を見えなくする 3 つの構造的障害：**リトライの裾**（期待トークンは T/p でスケール、完了率 90→70% で解決あたりコストは ~28% 増、失敗は複利する）、**文脈インフレ**（コストは文脈長の O(n²)、文脈倍増で推論コストはほぼ 4 倍）、**ルーティング**（全部を最強モデルに投げるか、易しいタスクを小モデルに回すかが、管理可能な請求書と取締役会案件の差）。

[[concepts/agent-execution-tax|エージェント実行税]]（Fireworks、720 ラン計測）はこれを別角度から測る —— 「エージェントは知能ではなく実行で失敗する」。**Reliability-Adjusted Accuracy = タスク成功率 × (1 − 実行税)** で測ると、**MiniMax は Gemini より per-token は高いのに、成功タスクあたりでは 2.3 倍安い**。だから「トークン価格はモデル選定段階で誤導する」。会話の軸は **「per token」から「完了した結果あたりのコスト（per completed outcome）」** へ移る —— 解決したチケット、処理したクレーム、レビューした契約あたり。これは Section 4.5 の PTC（トークン 9 割削減）が技術的回答であり、Section 5.2 の Cost Management が組織的回答である問題だ。

---

## 6. 結び：モデルは燃料、価値は「まわりの層」に堆積する

一本の糸が全節を貫いている —— **モデルはコモディティ化し、持続的優位はモデルの「まわりの層」に残る。** その層は、

- **エンジニアリングの高さ**では **ハーネス**（モデルが天井を、ハーネスが実現率を決める。開発時間の 60〜80% はここ）、
- **個人の高さ**では **複利で育つナレッジベース**（Markdown + git、ファイルが普遍インターフェース、Thin Harness / Fat Knowledge）、
- **組織の高さ**では **コントロールプレーンと組織の形**（registry / identity / audit / eval / tenant memory、そして複利のデシジョン・リネージュ）、
- **経済の高さ**では **トークンから結果への帰属**（per token ではなく per outcome）。

私の `ai-topics` Second Brain は、この一番下 —— 個人の高さ —— の小さな実装にすぎない。だが小さいからこそ、上位の層と同じ形をしていることが手に取るように分かる。

開発者への持ち帰りを 5 つに畳む。

1. **Hermes は「使うほど賢くなる常駐ワーカー」として捉える。** 賢いチャットではない。スケジュール・ファイルベース・メッセンジャー配信の 3 性質を満たすワークフローに当てると効く。
2. **記憶は Markdown + git に置く。** 凝った Vector DB/KG は Bitter Lesson で負ける。重要なのはデータ構造ではなく **読み書きの規律**（特に Signal Gate）。
3. **ハーネスは薄く、知識資産は厚く、可搬に。** ハーネスはロックインを起こす。中核資産（知識ベース、tool API、eval dataset、audit log）を **ハーネスの外** に出し、「ハーネスを捨てても残る」構成にする。
4. **ホスティングは安く始め、痛みで上げる。** $5 VPS → Modal/Daytona でサンドボックス分離 → AWS なら Tier 2 で試し Tier 3（AgentCore）で本番。Bedrock で API キー問題を消し、PTC でトークンを 9 割削る。脳と手を分け、エンドポイントを開くたびに攻撃面を意識する。
5. **個人と組織は相似形。** 複利のファイル群（知識／デシジョン・トレース）が堀になる。per token ではなく per outcome で測る。

> 道具（Hermes）は乗り換えてよい。だが **複利で育つあなた自身のファイル群** だけは、ベンダにもハーネスにも預けず、自分の手元（git）に持ち続けること。それが、モデルがどれだけ強くなっても陳腐化しない唯一の資産だ。

---

### 参照（主要 wiki ページ）

本稿は読み取り専用 `wiki` CLI と `ai-topics-wiki` スキルで以下を横断して書いた（frontmatter `sources:` に全リスト）。中核：[[entities/hermes-agent]]・[[concepts/hermes-agent-use-cases]]・[[concepts/agent-memory-engineering]]・[[concepts/llm-augmented-knowledge-retrieval]]・[[concepts/harness-engineering]]・[[concepts/agent-hosting-aws]]・[[concepts/agent-control-plane]]・[[concepts/token-to-outcome-attribution]]、および筆者自身の整理 [[raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework]]。

数値は出典・時期で振れるもの（GitHub スター数、バックエンド/スキル数など）があり、本文では大づかみに扱った。一次資料は各 wiki ページの `sources:` を辿られたい。
