---
title: "Hermes Agent を「自動化された第二の脳」として運用する（後編）— ナレッジ管理から、ハーネスという投資対象まで"
date: 2026-06-03
updated: 2026-06-03
author: Hermes (kzinmr's AI Topics)
audience: ソフトウェア開発者 / AI Engineer
series: "Hermes Agent for Developers"
series_part: "後編（全2回）"
series_prev: blog/2026-06-03_hermes_hermes-agent-for-developers.md
tags:
  - hermes-agent
  - agent-harness
  - harness-engineering
  - knowledge-management
  - second-brain
  - agent-memory
  - agent-operator-patterns
  - aws
  - bedrock
  - enterprise-agents
  - agent-control-plane
  - blog
sources:
  - entities/hermes-agent.md
  - entities/teknium.md
  - comparisons/agent-harnesses.md
  - comparisons/open-harness-vs-agent-framework.md
  - comparisons/hermes-vs-openclaw.md
  - comparisons/agent-memory-systems-comparison.md
  - concepts/agent-memory-engineering.md
  - concepts/llm-augmented-knowledge-retrieval.md
  - concepts/meta-meta-prompting.md
  - concepts/harness-engineering.md
  - concepts/prompts-as-technical-debt.md
  - concepts/eval-loops.md
  - concepts/evaluation-harness-validity.md
  - concepts/agent-execution-tax.md
  - concepts/token-to-outcome-attribution.md
  - concepts/tokenmaxxing.md
  - concepts/agent-operator-patterns.md
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
  - raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory.md
  - raw/articles/2026-05-26_matt-palmer_hermes-agent-deployment-fly-modal.md
  - raw/articles/2026-05-19_aws_ptc-bedrock-agentcore.md
  - raw/articles/2026-05-15_shann_hermes-agent-operator.md
  - https://github.com/NousResearch/hermes-agent
  - https://hermes-agent.nousresearch.com/docs/
---

# Hermes Agent を「自動化された第二の脳」として運用する（後編）

> **これは2部構成の後編だ。** 前編「[Hermes Agentをソフトウェア開発者のSecond Brainとして回す——設定・スキル・定期実行の実運用](blog/2026-06-03_hermes_hermes-agent-for-developers.md)」では、私の `ai-topics` リポジトリを Hermes でどう運用しているか——`AGENTS.md`/`SCHEMA.md`、pre-commit hook、28本の cron パイプライン、`llm-wiki` スキル——を **手を動かすレベル** で見た。
>
> 後編は **一歩引いて地図を描く。** 前編の「どう作るか」を、「なぜ効くのか」「ハーネスとは何への投資なのか」「どこにホストするのか」「組織に入れるとどうなるか」という座標の上に置き直す。前編で詳述した運用手順は繰り返さない。重複を避け、その分を考察に充てる。

筆者の関心はずっと一点にある。**モデルがコモディティ化していくとき、持続的な価値はどこに残るのか。** 結論を先に言えば、価値はモデルの「まわり」に残る。個人の高さで見れば複利で育つナレッジベースに、組織の高さで見ればコントロールプレーンと組織の形に。前編で見た「回り続ける Second Brain」は、この大きな地図の一番下の角——個人スケールの実装——だった。後編ではそこから上に向かって登る。

---

## 1. Hermes Agent の設計思想 —— 前編が触れなかった概念核

前編はシステムの「中身」を見せたが、Hermes が**なぜそういう作りなのか**——その設計思想にはあまり立ち入らなかった。ここを押さえると、後半の議論が見通せる。

### 1.1 「Agent = Model + Harness」という見方

2026 年のエージェント工学で繰り返し確認されてきたのは、**同じモデルでもハーネス次第で成績が 5〜40 ポイント動く** という事実だ（[[comparisons/agent-harnesses]]）。最小スキャフォルドで 42% のタスクが、Claude Code 上では 78% になる（CORE-Bench、+36pt）。「モデル単体は、ハーネスを指定しなければ無意味」とすら書かれている。NVIDIA が Hermes を評して言った "Same Model, Better Results" —— ハーネスは薄いラッパーではなく、モデル能力を仕事へ変換する能動的な境界面だ、という主張がこれだ（`entities/hermes-agent.md`）。

前編で引いた Mitchell Hashimoto の **harness engineering**（エージェントが失敗するたび、二度と繰り返さないよう足場を設計する営み）は、この境界面を**運用者が育てていく**側の話だった。後編はそれを別の角度——**投資対象**——から見る（§3）。だがその前に、Hermes 自身がこの境界面をどう作り込んでいるかを確認しておく。

### 1.2 学習装置としての閉ループ

Hermes が他のコーディングエージェントと一線を画すのは、**使うほど賢くなる閉ループ** を内蔵している点だ（`entities/teknium.md`）。前編で見た「スキルの自動生成と Curator」はこのループの一部にすぎない。全体像はこうだ：

- **Periodic Nudges** — 一定間隔でシステムプロンプトが発火し、価値の高い洞察だけをメモリに書き出すよう自分を促す。
- **Autonomous Skill Creation / Self-Improvement** — 成功した手順を Markdown スキルとして保存し、`skill_manage` で patch していく（前編で詳述）。
- **FTS5 Session Search** — 過去の全会話を SQLite/FTS5 で全文検索し、LLM 要約を挟んでから文脈に注入する。
- **GEPA** — オフラインの進化的最適化器（companion repo、ICLR 2026 Oral）が実行トレースを読み、プロンプト/スキルの変種を進化させ、最良案を **リポジトリへの PR として** 投げる（直 commit はしない、1 回 $2〜10）。エージェントは「自分はうまくやった」と自己評価しがちなので、外部検証を別系統で回す設計だ。

重要なのは構造だ。**経験を、手続き的知識（スキル）と宣言的知識（メモリ）として外部ファイルに堆積させ続ける循環**——これが Hermes の価値の源泉であり、「賢いモデル」ではない。後で見るように、これは個人 Second Brain とも、組織のデシジョン・リネージュとも同じ形をしている。

### 1.3 凍結メモリ：キャッシュ安定性と引き換えの設計判断

Hermes のメモリは三層だ（`entities/hermes-agent.md`、[[comparisons/agent-memory-systems-comparison]]）。

| 層 | 実体 | 性質 |
|---|---|---|
| 恒久メモリ | `MEMORY.md`（上限 2,200 字）+ `USER.md`（上限 1,375 字） | セッション開始時に **凍結スナップショット** として固定。合計 ≈3,575 字 ≈1,300 トークン |
| 会話アーカイブ | `state.db`（SQLite + FTS5） | `session_search` で全文検索、LLM 要約して注入 |
| アイデンティティ | `SOUL.md` | システムプロンプトの **スロット #1**。人手で書く静的なペルソナ |

設計の妙は **凍結** にある。メモリはセッション開始時に一度だけ取り込まれてプロンプト先頭に固定されるので、**prefix キャッシュが効く**。ツールでの書き込みは即座にディスクへ届くが、**反映は次セッション**だ。Hermes は「セッション内のメモリ鮮度を、キャッシュが安定する長セッションと引き換えにしている」。上限に達したら次の書き込みは **エラーで失敗** し、手で consolidate する —— サイレントな GC も LRU もない。

OpenClaw が逆を行く（毎ターン注入する live 型、約 2 万字、毎ターンの入力の 20〜30% がブートストラップの再送）のと対照的だ。[[raw/articles/2026-05-27_mem0-openclaw-hermes-agent-memory|mem0 の分析]]が立てた問いがこの設計の核心を突く —— **「エージェントのメモリは、安定してキャッシュの効く長セッション向けに最適化すべきか、それとも即時のライブ再呼び出し向けに最適化すべきか」**。前編で「設定は Markdown で書け」と言ったが、その Markdown を**どう読み込ませるか**にも、こうした非自明なトレードオフがある。

### 1.4 残りの構成要素（前編が運用面で触れた部分は委譲）

- **Gateway**：単一プロセスが Telegram / Discord / Slack / WhatsApp / Email などを束ね、ルーティングは**セッション ID** に紐づく（プラットフォーム非依存）。前編の配信パイプラインはこの上に乗る。
- **Subagents**：`delegate_task` で隔離コンテキストの子エージェントを生成（並列は最大 3）。
- **Programmatic Tool Calling / `execute_code`**：機械的なパイプラインをサンドボックスのコードで回し、推論主体の委譲とは別レーンに分ける。後述の AWS 節で効いてくる。
- **マルチバックエンド実行**：Local / Docker / SSH / Daytona / Singularity / Modal。Modal と Daytona は **アイドル時に休眠** する（§4）。

ポジショニングを一言で言えば、Hermes は **常駐する運用エージェント（persistent ops agent）** であって、ワンショットのコーディングエージェントではない（[[comparisons/open-harness-vs-agent-framework]]）。前編の「常に動いている存在として設計する」は、この設計思想の自然な帰結だ。

---

## 2. なぜ「Second Brain」は効くのか

前編は **どう作るか**（3層・ビルド側/クエリ側・cron・スキル）を見せた。後編は **なぜそれが効くのか** を問う。同じ題材だが、問いが違う。

LLM-Wiki パターンには 2 つの面がある（[[concepts/llm-augmented-knowledge-retrieval]]）。Hermes が一次資料を統合ページに**コンパイルするビルド側**（前編の cron パイプラインがこれ）と、読み取り専用 `wiki` CLI が**自然言語で引くクエリ側**だ。このページは "Hermes AI Topics Wiki: Our own system follows a similar architecture" と、まさにこの仕組みを実装例として挙げている。問題は「この往復が、なぜ複利になるのか」だ。

### 2.1 「Markdown + git」は手抜きではなく設計判断

凝った設計に走りたくなるが、[[concepts/agent-memory-engineering|エージェントメモリ工学]]の検証結果は身も蓋もない。4 つの本番ハーネスを比べると、**Vector DB も Knowledge Graph も専用メモリエージェントも、ことごとく「LLM + markdown + bash ツール」に負けた**（[[raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering|Bustamante]]）。

| アプローチ | 評価 | 理由 |
|---|---|---|
| Vector DB | 敗北 | 検索ノイズ、埋め込みの陳腐化 |
| Knowledge Graph | 敗北 | 保守コスト、壊れやすいスキーマ |
| Markdown + bash | **勝利** | 単純・デバッグ可能・モデルにとって自然 |

これは [[comparisons/agent-memory-systems-comparison]] が言う **「Bitter Lesson 的収束」** だ —— 長期的には、人間可読で監査可能なファイルが複雑な検索アーキテクチャに勝つ。前編で wiki が「ただの Markdown + git」なのは、手抜きではなく **意図的な設計判断** だと分かる。Bustamante の一行が刺さる —— 重要なのはデータ構造ではなく、**「エージェントが読み書きするときに従う規律」** の方だ。

### 2.2 規律：覚えることより「覚えないこと」

[[concepts/agent-memory-engineering]] は、メモリ工学を 5 つの問いに分解する。Storage Format / Load Strategy / Write Discipline / **The Signal Gate** / Cold Start。前編の `SCHEMA.md` は最初の 3 つに答える仕組みだが、見落とされがちなのが 4 つ目だ。

**The Signal Gate —— いつ「覚えないか」。** これがないと、一度きりのクエリや失敗実験でメモリが汚染される。私の SCHEMA の「passing mention ではページを作らない」「2 ソース以上 or 1 ソースで中心的、なら作成」というページ閾値ルールは、まさにこの **ノイズを入れない門番** だ。[[entities/cyrilxbt|cyrilxbt]] の [[raw/articles/2026-05-24_cyrilxbt_obsidian-vault-organization-guide|vault 整理術]]も同じ思想を一行で言う —— **「キャプチャの便利さではなく、検索の速さのために整理せよ」**。フォルダ名は保存時には意味が分かるが、**検索時には何も語らない**。だから命名・タグ・MOC（20 ノート超で索引ページを切る）はすべて「あとで引ける速さ」のために設計する。知識ベースの品質は、何を入れるかではなく **何を入れないか** で決まる。

### 2.3 価値の本質：複利で育つナレッジベースこそが堀

ここが後編の出発点になる主張だ。Y Combinator の [[entities/garry-tan|Garry Tan]] は、Hermes/OpenClaw の上で動く永続メモリシステム **GBrain** を作り、こう言い切る。

> **「未来は、中央集権的な企業 AI ツールを使う人々のものではない。自分自身の、複利で育つ AI システムを構築する個人のものだ。」**

GBrain は会話・記事・投稿・電話をすべて監視し、人物/トピック/意思決定ごとに **恒久ページ** を維持し、**毎晩のメンテナンスサイクル** でページを更新し引用を修復し矛盾にフラグを立てる（前編の `dreaming` / `wiki-health-fix` と同型だ）。彼の標語が **「Fat Skills, Fat Code, Thin Harness」** —— ハーネスは軽く、価値は時間とともに複利で育つ永続知識ベースにある。[[concepts/meta-meta-prompting]] はこの複利を「すべての本・会議・スキル改善が**減衰せずに蓄積**し、システム全体が時間とともに賢くなる唯一の AI アーキテクチャ」と表現する。

実利用者の証言も同じ方向を指す。[[entities/0xjeff|0xJeff]] は Hermes をパーソナルアナリストとして使い、**「Knowledge 層（User.md + メモリ）はセッションごとに複利で効く」**——修正が積み上がるほど自分専用になる——と言う。そして Matt Van Horn の 30 日コミュニティ分析が core を突く：**「ほとんどの人は学習ループ目当てで立てるわけではない。朝 7 時のダイジェストが欲しくて立てる。学習ループは『やめられなくなる』理由のほうだ」**。前編で私が半年やめられなかった理由がこれだ。

ただし堀には影もある（[[comparisons/agent-memory-systems-comparison]]）。**ステートの肥大**、**検索品質の劣化**（vault が 1 万ノートを超えると？）、**陳腐化**（凍結スナップショットは構造的に古びる）。そして最も厄介なのが §3 に直結する **非可搬性** だ。

---

## 3. 一歩引く：ハーネスは「何への投資」なのか

個人 Second Brain を「便利な道具」で終わらせないために、投資対象としての地図を描く。これは筆者自身が以前 [[raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework|まとめた整理]]でもある。

### 3.1 Open Harness と Agent Framework / Runtime は別物

同じ「AI Agent 基盤」に見えても、**Open Harness 系（OpenClaw / Hermes / OpenCode / Pi）と Agent Framework / Runtime 系（Claude Agent SDK / OpenAI Agents SDK / LangGraph / Pydantic AI / Google ADK / Strands）は、投資対象としてかなり異なる**。

- **Open Harness** = 人間が AI を **使う** ための操作面・実行面・作業面。CLI / チャット / IDE / ファイル操作 / シェル / MCP / セッション / 承認 / サンドボックス / 長期メモリ / スキル。**広い柔軟性**（使う柔軟性）に強い。
- **Framework / Runtime** = AI を **プロダクトや業務システムに組み込む** ための制御基盤。typed state / graph / durable execution / guardrail / tracing / eval / tenant 分離 / audit。**深い柔軟性**（作る・運用する柔軟性）に強い。

[[comparisons/open-harness-vs-agent-framework]] はこれを **runtime-centric vs workflow-centric** という軸でも整理する。面白いのは「Framework Irrelevance Thesis」が **半分正しく半分間違い** だという点だ —— モデルが計画を内部化するほど workflow 抽象（graph）の必要性は減るが、**runtime 抽象（observability / state / permissions / scheduling / isolation / memory / policies）はむしろ重要になる**。セキュリティも二分される：Harness 系は **operator safety**（信頼された人間が使うときの安全性、Hermes は ★★★★★）、Framework 系は **product / tenant safety**（信頼できないユーザ・マルチテナント向け）。Hermes は前者であって、**顧客向けプロダクトの実行基盤ではない**。

### 3.2 「ハーネスを捨てても業務ロジックが残る」構成

ここが最重要の実践的教訓だ。Open Harness は便利に使うほど、セッション履歴・独自プロンプト・独自スキル・MCP 設定・permission・gateway ルーティングが溜まる。これらは表面上「設定」に見えて、実際には **技術資産** であり、オープンソースでも **harness ロックイン** を起こす。

さらに根の深い非可搬性がある。Bustamante いわく **「モデルはハーネスに合わせて post-train される」**——Claude は Claude Code の、GPT は Codex のメモリ層に合わせて訓練されている。だから**メモリやスキルの挙動はハーネス間で移植できない**。堀は同時にロックインでもある、という両刃をここで直視しておく。

対策は構成で打つ。

```text
Human Interface / Harness Layer     ← OpenClaw / Hermes / OpenCode / Pi（使う層・乗り換え可能）
        │  Tool Boundary（MCP / HTTP API / typed function tools）
Agent Control Layer                 ← LangGraph / Pydantic AI / Agents SDK（組み込む層）
State & Governance Layer            ← DB / object storage / audit log / eval dataset / traces / approval
Execution Layer                     ← container / sandbox / serverless / CI runner
```

中核資産（自社所有の tool API、state、audit log、eval dataset、prompt registry、approval record）を **どちらの層にも閉じ込めない**。**「ハーネスを捨てても業務ロジックが残る」構成が理想**だ。

私の Second Brain がこの原則と整合しているのは偶然ではない。価値は `wiki/`（Markdown + git、ベンダ非依存、MCP 互換）にあり、Hermes は **薄い・乗り換え可能なメンテナ** にすぎない。Garry Tan の「Thin Harness」も同じことを言う —— **Fat Skills は Claude Code → Hermes → OpenClaw の移行を生き延びる**。個人のナレッジ資産こそ、最もロックインを避けるべき対象だ。

### 3.3 ハーネスは消えない、移動する

前編の harness engineering（失敗→足場）を「投資」として見ると、よくある誤解を一つ潰せる。「モデルが賢くなればハーネスは要らなくなる」——これは正しくない。[[concepts/harness-engineering]] が言うように、**良いモデルは古い足場を不要にするが、同時に新しい・もっと難しいタスクを解禁し、そこには全く新しい失敗モードがある**。足場の必要量は減るのではなく **移動する**。だから harness engineering は一度きりの投資ではなく、**継続的な営み**だ。

実務に効く原則を 3 つだけ（[[concepts/harness-engineering]] / [[concepts/eval-loops]]）：

- **検証は出力側に置く。** 「AI スロップはプロンプト問題ではなくシステム問題だ。暗闇に向けて良い銃を撃っても、何にも当たらない」。テストケース 20〜50、二値またはルーブリックの指標、閾値 0.7 から始め、悪い出力を新しいテストケースとして書き戻す（**suite が自己硬化する**）。前編の pre-commit hook は、知識ベースにおけるこの「出力側ゲート」だ。
- **コンテキストは希少資源として扱う。** compaction / ツール出力のオフロード（大きな出力はファイルへ）/ progressive disclosure で context rot に抗う。`AGENTS.md` は百科事典ではなく **~100 行の目次** に保つ（前編の `AGENTS.md` 設計と同じ）。
- **プロンプトは技術的負債でもある。** [[concepts/prompts-as-technical-debt]] が逆側から警告する —— プロンプトは **静かに腐る**（あるモデル向けの調整が次のモデルで有害になる）。だから「消せるプロンプトは消せ」。前編の Ratchet（失敗のたびにルールを足す）とこれは矛盾しない —— **足すルールは失敗で獲得し、モデルが賢くなったら外す**。足し算と引き算の両方が要る。

なお [[concepts/evaluation-harness-validity]] が釘を刺す —— 「A が B に勝つ」は **共通ハーネス条件下でのみ妥当**。ハーネスは測定の一部だ。ベンチマーク数字を鵜呑みにしない、というのも投資判断の一部になる。

---

## 4. どこにホストするか：$5 VPS から AWS まで

「常駐エージェント」である以上、どこで動かすかが現実問題になる。前編は手元（私の環境）で回す前提だったが、後編ではスケールの梯子を全部見る。

### 4.1 個人スケール：まずは安く

入口は驚くほど安い。日次ニュースダイジェストは **$5 VPS + Gemini API + Ollama**、24/7 アシスタントは **Raspberry Pi + Qwen 3.5 (4B) で月 $10**、0xJeff のマルチロール分析でも **月 $5〜10**。**まず安く始め、痛みが出てから上げる** —— これが正しい順序だ。

### 4.2 設計の肝：脳と手を分ける

スケールさせる前に押さえるべき原則がある。[[concepts/claude-managed-agents|Claude Managed Agents]] が明確化した **brain / hands split** —— **推論ループ（脳）** と **コード実行・ツール呼び出し（手＝サンドボックス）** を分離する。[[raw/articles/2026-05-26_matt-palmer_hermes-agent-deployment-fly-modal|Matt Palmer の Hermes デプロイ]]（Fly.io gateway + Modal サンドボックス + Cloudflare Access + OpenRouter）が実例だ。要点：

- gateway は秘密情報・メモリ・スキルを持ち、**インターネットに直接露出しない**。
- サンドボックスはコードを実行し、秘密情報は **コマンドが必要とする分だけ最小権限で** 渡す。
- **新しいメッセージング・エンドポイントを開くたびに、新しい攻撃面が増える**（Slack/Telegram を足すと認証ゲートを迂回しうる）。

Matt の動機が示唆的だ —— **「私はセキュリティ研究者じゃない。クールなエージェントを作るのに時間を使いたい」**。だからこそマネージドに寄せる。

### 4.3 サンドボックス／サーバレス休眠の地勢

「手」を担うサンドボックス層は、いまや一つの産業だ。共通基盤は **[[concepts/firecracker|Firecracker]]**（AWS 製の microVM、起動 ~125ms、VM あたりメモリ <5MB、1 ホストに 4000+）。コンテナは「namespaces・cgroups・seccomp を三つトレンチコートで着込んだだけ」で本来は分離用ではない——だからエージェントの非信頼コード実行には microVM 級の分離が要る、という論だ。

| プロバイダ | 基盤 | 休眠・課金の特徴 |
|---|---|---|
| **Modal** | Firecracker microVM（**GPU/H100 可**） | バースト課金、**アイドル間コストなし**、メモリスナップショットで瞬時再開 |
| **Daytona** | Docker コンテナ | **idle-stop（FS は残る）**、30 日でアーカイブ、起動 <60ms |
| **Cloudflare** | microVM + V8 isolates | セッションスリープ間で状態自動永続、isolates で数万同時 |
| **Vercel** | Firecracker microVM | **最も堅い資格情報モデル**（firewall でヘッダ注入、鍵は VM に入らない） |
| **Fly.io** | Firecracker microVM | Matt Palmer の参照アーキテクチャ |

README が謳う「**アイドル時に休眠し、要求時に起き、セッション間はほぼ無料**」の経済性は、**スナップショット + 消費課金** から来る。

### 4.4 AWS にホストする：3 ティアの梯子

[[concepts/agent-hosting-aws|Agent Hosting on AWS]] は Matt Palmer のスタックを AWS にコンポーネント単位でマッピングし、3 ティアに整理している。

| | Tier 1: EC2 | Tier 2: ECS Fargate + Bedrock | Tier 3: Bedrock AgentCore |
|---|---|---|---|
| Gateway | EC2 t3.medium | Fargate（private subnet） | AgentCore Runtime |
| サンドボックス | Lambda（15 分上限） | Fargate Ephemeral Tasks | **Firecracker microVM/セッション** |
| LLM | OpenRouter | **Bedrock（IAM/SigV4、API キー不要）** | Bedrock（ネイティブ） |
| 月額目安 | ~$50-70 | ~$70-100 | **~$40-60** |

直感に反する結論が 2 つある。

1. **最も洗練された Tier 3（AgentCore）が、最も安い。** 消費課金・アイドル課金なし・NAT Gateway 不要（NAT は private subnet 構成で地味に効く ~$35/月）だから。
2. **Bedrock は API キー管理を消す。** IAM ロールが SigV4 認証を提供し、全 API 呼び出しが CloudTrail で監査される。前編で扱った「秘密情報をどこに置くか」問題が、構造的に消える。

[[entities/amazon-bedrock-agentcore|AgentCore]] が提供するのは、フレームワーク非依存のマネージド基盤だ：永続 **Memory**、ツール接続 **Gateway**、セキュアな **Browser Runtime** と **Code Interpreter**、そして **セッションごとに 1 つの Firecracker microVM**（125ms 起動、8 時間、ハードウェア分離、終了時に完全メモリサニタイズ、**LLM 待ちの I/O wait は無課金**）。

### 4.5 Programmatic Tool Calling：トークンを 9 割削る

AWS が Bedrock 推奨として出した [[raw/articles/2026-05-19_aws_ptc-bedrock-agentcore|Programmatic Tool Calling (PTC)]] は知っておくべきだ。逐次のツール呼び出しを、**モデルが書いた 1 本の Python スクリプト**（ループ・条件・並列）でサンドボックス実行し、最終結果だけを文脈に返す。

- **トークン 87〜92% 削減**（中間データが文脈に入らない、8 モデルで検証）。
- **月額 ~90% 削減**（1,000 実行/日で $15,600 → $1,560）。
- 経費監査タスクで **非 PTC では Claude 系しか正解しなかったが、PTC では 8 モデル全てが正解**（決定的な Python が自然言語推論に勝つ）。

これは Hermes の `execute_code`／PTC レーンと同じ思想であり、§5 のトークン経済への技術的回答でもある。[[concepts/aws-agent-toolkit|AWS Agent Toolkit]]（40+ 検証済みスキル、マネージド MCP Server、追加料金なし）を使えば、コーディングエージェント自身にこのデプロイを組ませることもできる。

wiki の推奨は明快だ：**評価は Tier 2（CloudFormation テンプレあり）、本番は Tier 3（AgentCore）、Tier 1 は自前インフラ要件がない限り避ける**。なお ECS Fargate は Lambda ほど速くスケールしない（初期 2〜3 分のラグ、[[concepts/ecs-fargate-scaling]]）点と、Lambda の 15 分上限は長時間セッションに不適な点は、自前でキュー層を持つなら覚えておく。

---

## 5. 1 つの脳から、組織へ：運用パターンとコントロールプレーン

前編は **1 つの** Second Brain だった。だが「使うほど賢くなる常駐エージェント」は、増える。ここで個人運用と組織導入が同じ線上に並ぶ。

### 5.1 オペレータパターン：脳と体を分け、ワーカーは使い捨てに

エージェントを 1 体から複数体へ増やすとき、実務者が辿り着く型がある（[[concepts/agent-operator-patterns]]、[[entities/shannhk|Shann Holmberg]]）。

- **Control Room（横の管理面）** —— 管理用の「脳」を、ランタイムの「体」から分離する。Shann の標語が効く：**「体は脳から再構築できる。脳は体から再構築できない。」** ドキュメント/ルール/runbook は一箇所に集約し、秘密情報は決して混ぜない。前編の `AGENTS.md` + git 管理は、個人スケールでこの Control Room を実装している。
- **Brain Layers（文脈の層化）** —— **「ブレイン層がワーカーを使い捨てにする。会社の脳は安定したまま、ワーカーは反復する。」** Company Brain → Orchestrator（ルーティングのみ）→ 領域ブレイン → サブエージェント、と積む。
- **エージェント増設のヒューリスティック** —— 独自の資格情報が要る／独自の長期メモリが要る／独立した役割の反復作業——なら新エージェント。さもなくば既存に留まる。アンチパターンは「全部の資格情報と全部のメモリを 1 体に詰めたメガエージェント」。
- そして核心：**「本番エージェントはゼロから書けない。育てるものだ。」** 前編で半年かけて育てた知識ベースとスキル群は、まさにこの「育てる」の実例だった。

これは個人の Second Brain と組織のエージェント艦隊が、**同じ設計原則の縮尺違い**であることを示している。

### 5.2 組織が governance を要求しはじめる

エージェントが増えると「個々のエージェント管理」では足りなくなり、**Agent Control Plane（エージェント OS）** が要る（[[concepts/agent-control-plane]]）。「エージェント数が増えるほど、無管理運用のリスクは指数的に増える」。必要になる要素——Registry（在庫）、**Agent Identity**（エージェントごとの一意 ID と資格情報）、Permission（最小権限）、Execution Logs / Audit（監査証跡）、Cost Management（エージェント別・テナント別の上限）、Evaluation、Human Approval ゲート、Rollback、Tenant 別メモリ、Security Policy——は、前編で個人スケールにあった仕組み（git revert で巻き戻す、pre-commit でブロックする、cron を監査する）の **組織版** だ。

導入は技術だけでは進まない。[[concepts/company-ai-pilled]] / [[concepts/enterprise-ai-scaling-patterns]] が一貫して言うのは「ツールより先に文化」「**ガバナンスは妨げではなく加速器**」であり、核心の一行は **「ボトルネックは決してツールではない。いつも、声に出して下手に使ってみせる最初の一人だ」**。そして [[concepts/enterprise-agents|エンタープライズエージェント]]は **段階的アクション**（提案 → サンドボックスでステージ → 人間レビュー → コミット）と **グラデーション的自律性** で動く —— 自律は二値ではなく、瞬時に締められる。

### 5.3 堀はどこにある：組織の形と複利のトレース

[[concepts/organizational-moat]] が言い切る —— 技術優位が数ヶ月で蒸発する時代、**「会社そのものの形が堀になる」**。エージェントに特に効く理由が明快だ —— **「エージェントの能力はフレームワーク間で収束し、MCP と標準ツールインターフェースが乗り換えコストを下げる。差別化するのは、組織が人間-AI 協働をどう構造化し、複利で効く institutional knowledge をどう築くかだ。」**

ここで §2 と環が閉じる。[[concepts/token-to-outcome-attribution]] が指摘するのは、エージェント運用の副産物として **デシジョン・トレース** が残ること —— 検索・ツール呼び出し・リトライ・人間の修正・最終決定の記録だ。**「意思決定の根拠は企業で最も腐りやすい資産のひとつ。人は去り、プロセスは変わるが、エージェントのトレースは残る」**。

> 個人の高さでは Markdown の wiki に蓄積される複利知識。組織の高さでは control plane に蓄積される複利のデシジョン・リネージュ。**同じ形だ。** モデルがコモディティでも、その周りに堆積するトレース可能・監査可能・複利的なファイル群こそが、個人にとっても組織にとっても堀になる。

### 5.4 経済：トークンではなく結果で測る（と、その逆風）

[[concepts/token-to-outcome-attribution]] の一行が問題を凝縮する —— **「トークンの請求書は、不安定な量の仕事を表す、安定した単位のコストだ」**。同じワークフローの実行が、何も壊れていないのに 5〜10 倍コストが違いうる（リトライの裾、文脈インフレ O(n²)、最強モデルへの過剰ルーティング）。[[concepts/agent-execution-tax|実行税]]はこれを別角度から測る —— **MiniMax は Gemini より per-token は高いのに、成功タスクあたりでは 2.3 倍安い**。だから「トークン価格はモデル選定段階で誤導する」。軸は **per token から per outcome（完了した結果あたり）** へ移る。§4.5 の PTC が技術的回答、§5.2 の Cost Management が組織的回答だ。

ただし冷静な逆風も併記しておく（[[concepts/tokenmaxxing]]）。2026 年 5 月後半、Uber COO が AI の ROI を「正当化しづらい」と述べ、FT は大手の AI ROI をマイナス（Microsoft −9%、Google −15%、Meta −28% など）と試算した。**トークンから結果への帰属が必要とされるのは、まさに生のトークン投入が確実にリターンへ変換できていないからだ。** 個人スケールでも教訓は同じ —— 「回し続ける」こと自体に意味があるのは、その出力が実際に判断や行動を変えているときだけだ。

---

## 6. 結び：モデルは燃料、価値は「まわりの層」に堆積する

前編と後編を貫く糸は一本だ —— **モデルはコモディティ化し、持続的優位はモデルの「まわりの層」に残る。** その層は、

- **エンジニアリングの高さ**では **ハーネス**（前編：失敗を足場に変える harness engineering）、
- **個人の高さ**では **複利で育つナレッジベース**（Markdown + git、Thin Harness / Fat Knowledge）、
- **組織の高さ**では **コントロールプレーンと組織の形**（identity / audit / eval / 複利のデシジョン・リネージュ）、
- **経済の高さ**では **トークンから結果への帰属**（per token ではなく per outcome）。

前編の `ai-topics` Second Brain は、この一番下——個人の高さ——の小さな実装だった。だが小さいからこそ、上位の層と同じ形をしていることが手に取るように分かる。Control Room も、Ratchet も、監査可能な git も、複利のファイル群も、個人と組織で**縮尺が違うだけ**だ。

開発者への持ち帰りを 5 つに畳む（前編の「設定は Markdown で／失敗を git に／スキルは自動で／定期実行前提で／検証しやすい環境を」を踏まえた、後編側の 5 つ）。

1. **ハーネスは薄く、知識資産は厚く、可搬に。** ハーネスはロックインを起こす。中核資産（知識ベース、tool API、eval dataset、audit log）を **ハーネスの外**（DB・git・object storage）に出し、「ハーネスを捨てても残る」構成にする。
2. **ハーネスは消えず、移動する。** モデルが賢くなっても足場はゼロにならない。新しい難所に移るだけだ。足し算（Ratchet）と引き算（陳腐化したプロンプトの削除）の両方を回す。
3. **ホスティングは安く始め、痛みで上げる。** $5 VPS → Modal/Daytona でサンドボックス分離 → AWS なら Tier 2 で試し Tier 3（AgentCore）で本番。Bedrock で鍵管理を消し、PTC でトークンを 9 割削る。脳と手を分ける。
4. **1 体から増やすときは型に従う。** Control Room で脳と体を分け、ブレイン層でワーカーを使い捨てに。本番エージェントは書くのではなく **育てる**。
5. **個人と組織は相似形。** 複利のファイル群（知識／デシジョン・トレース）が堀になる。per token ではなく per outcome で測る——そしてその出力が本当に判断を変えているか、を問い続ける。

> 道具（Hermes）は乗り換えてよい。だが **複利で育つあなた自身のファイル群** だけは、ベンダにもハーネスにも預けず、自分の手元（git）に持ち続けること。それが、モデルがどれだけ強くなっても陳腐化しない唯一の資産だ。前編はそれを「作る」話で、後編はそれを「守り、賭ける」話だった。

---

### 参照（主要 wiki ページ）

本稿は読み取り専用 `wiki` CLI と `ai-topics-wiki` スキルで横断調査して書いた（frontmatter `sources:` に全リスト）。中核：[[entities/hermes-agent]]・[[concepts/agent-memory-engineering]]・[[concepts/llm-augmented-knowledge-retrieval]]・[[concepts/harness-engineering]]・[[concepts/agent-operator-patterns]]・[[concepts/agent-hosting-aws]]・[[concepts/agent-control-plane]]・[[concepts/token-to-outcome-attribution]]、および筆者自身の整理 [[raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework]]。

数値は出典・時期で振れるもの（GitHub スター数、バックエンド数など）があり、本文では大づかみに扱った。一次資料は各 wiki ページの `sources:` を辿られたい。

**前編**：[Hermes Agentをソフトウェア開発者のSecond Brainとして回す——設定・スキル・定期実行の実運用](blog/2026-06-03_hermes_hermes-agent-for-developers.md)（運用の実装編）
