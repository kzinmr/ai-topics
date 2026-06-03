---
marp: true
theme: default
paginate: true
size: 16:9
title: "Hermes Agent（後編）: ハーネスという投資対象"
description: "ソフトウェア開発者向け後編——個人のSecond Brainから、ハーネス投資・AWSホスティング・組織導入まで"
style: |
  section {
    font-family: "Hiragino Sans", "Yu Gothic", "Noto Sans CJK JP", "Helvetica Neue", sans-serif;
    background: #fbfaf4;
    color: #18241f;
    padding: 54px 66px;
    letter-spacing: 0;
  }
  h1, h2, h3 {
    color: #10251c;
    letter-spacing: 0;
  }
  h1 {
    font-size: 42px;
    line-height: 1.18;
  }
  h2 {
    font-size: 34px;
    line-height: 1.2;
  }
  p, li {
    font-size: 25px;
    line-height: 1.46;
  }
  ul, ol {
    margin-top: 0.5em;
  }
  strong {
    color: #b45f06;
  }
  code {
    background: #efe7d0;
    color: #243326;
    border-radius: 4px;
    padding: 0.04em 0.24em;
  }
  pre {
    font-size: 18px;
    line-height: 1.4;
  }
  table {
    font-size: 19px;
    border-collapse: collapse;
  }
  th {
    background: #17352b;
    color: #fffaf0;
  }
  td, th {
    padding: 0.42em 0.55em;
  }
  blockquote {
    border-left: 8px solid #c47f2c;
    color: #31423a;
    background: #f2ead8;
    padding: 0.4em 0.8em;
  }
  section.lead {
    background: #10251c;
    color: #fffaf0;
  }
  section.lead h1,
  section.lead h2,
  section.lead h3 {
    color: #fffaf0;
  }
  section.lead strong {
    color: #f1b35d;
  }
  section.section {
    background: #26372f;
    color: #fffaf0;
  }
  section.section h1,
  section.section h2 {
    color: #fffaf0;
  }
  .kicker {
    font-size: 18px;
    color: #b45f06;
    font-weight: 700;
    text-transform: uppercase;
  }
  .small {
    font-size: 18px;
    line-height: 1.38;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
  }
  .box {
    border: 1.5px solid #d5c8ac;
    border-radius: 8px;
    padding: 18px 20px;
    background: #fffdf7;
  }
  .box h3 {
    margin-top: 0;
    font-size: 24px;
  }
  .big {
    font-size: 30px;
  }
  .mono {
    font-family: "SFMono-Regular", Menlo, Consolas, monospace;
    font-size: 20px;
    line-height: 1.35;
  }
---

<!-- _class: lead -->

<div class="kicker">Software Engineer's Guide — 後編</div>

# ハーネスという投資対象

## 個人の Second Brain から、ホスティングと組織導入まで

<br />

<div class="small">
2026年6月3日<br />
kzinmr (AI Engineer)
</div>

---

# 前編の振り返りと、今日の問い

**前編（実装編）** では「どう作り、どう回すか」を見た——
`AGENTS.md` / `SCHEMA.md`、pre-commit hook、28本の cron、`llm-wiki` スキル。

今日（後編）は **一歩引いて地図を描く**。同じ題材を別の座標に置く。

- Hermes は **何への投資** なのか（Agent = Model + Harness）
- なぜ Markdown の Second Brain が **複利** になるのか
- ハーネスの **ロックイン** をどう避けるか
- $5 VPS から **AWS Bedrock AgentCore** まで、どこに置くか
- 1つの脳が **組織のコントロールプレーン** とどう相似なのか

<!-- _footer: "前編: blog/2026-06-03_hermes_hermes-agent-for-developers.md / slides/2026-06-03_hermes-agent-second-brain-practice.marp.md" -->

---

# 貫く一本の糸

> **モデルはコモディティ化する。持続的な価値は、モデルの「まわりの層」に複利で堆積する。**

<div class="grid">
<div class="box">

### まわりの層とは
- **エンジニアリング**: ハーネス
- **個人**: 複利のナレッジベース
- **組織**: コントロールプレーン / 組織の形
- **経済**: トークン→結果の帰属

</div>
<div class="box">

### 前編との関係
- 前編 = この一番下（個人の脳）を **作る** 話
- 後編 = それを **守り、賭ける** 話
- 縮尺が違うだけで、**同じ形**

</div>
</div>

---

<!-- _class: section -->

# Part 1: 設計思想——前編が触れなかった概念核

---

# Agent = Model + Harness

**同じモデルでも、ハーネス次第で成績が 5〜40 ポイント動く。**

- 最小スキャフォルド **42%** → Claude Code 上で **78%**（CORE-Bench, +36pt）
- 「モデル単体は、ハーネスを指定しなければ無意味」
- NVIDIA が Hermes を評して **"Same Model, Better Results"**

<br />

前編の **harness engineering**（失敗→足場、Mitchell Hashimoto）は、
この境界面を **運用者が育てる** 側の話だった。
後編はそれを別角度——**投資対象**——から見る。

---

# 学習装置としての閉ループ

Hermes の価値の源泉は「賢いモデル」ではなく、
**経験を外部ファイルに堆積させ続ける循環**。

<div class="grid">
<div class="box">

### ループの駆動部
- **Nudges** — 価値ある洞察だけメモリへ
- **Skill 自動生成 / patch**（前編で詳述）
- **FTS5 Session Search** — 全会話を全文検索
- **GEPA** — トレースを進化させ **PR で** 提案

</div>
<div class="box">

### なぜ PR なのか
- エージェントは「自分はうまくやった」と
  自己評価しがち
- だから **外部検証を別系統** で回す
- 直 commit はしない / 1回 $2〜10

</div>
</div>

→ 個人 Second Brain とも、組織のデシジョン・トレースとも **同じ形**。

---

# 凍結メモリ：キャッシュ安定性との引き換え

| 層 | 実体 | 性質 |
|---|---|---|
| 恒久メモリ | `MEMORY.md`(2,200字) + `USER.md`(1,375字) | **凍結スナップショット** ≈1,300トークン |
| 会話アーカイブ | `state.db`(SQLite+FTS5) | `session_search` で全文検索 |
| アイデンティティ | `SOUL.md` | システムプロンプト スロット#1 |

- 書き込みは即ディスク、**反映は次セッション** → prefix キャッシュが効く
- OpenClaw は逆（毎ターン注入の live 型、約2万字）

> **問い**: メモリは「キャッシュの効く長セッション」向けか、
> 「即時のライブ再呼び出し」向けか。設計判断であって、正解は一つでない。

---

<!-- _class: section -->

# Part 2: なぜ Second Brain は「効く」のか

---

# 「Markdown + git」は手抜きではなく設計判断

4つの本番ハーネスを比較した結果（Bustamante）:

| アプローチ | 評価 | 理由 |
|---|---|---|
| Vector DB | 敗北 | 検索ノイズ、埋め込みの陳腐化 |
| Knowledge Graph | 敗北 | 保守コスト、壊れやすいスキーマ |
| **Markdown + bash** | **勝利** | 単純・デバッグ可能・モデルに自然 |

**「Bitter Lesson 的収束」** —— 人間可読で監査可能なファイルが勝つ。
重要なのはデータ構造ではなく **「読み書きの規律」**。

---

# 覚えることより、「覚えないこと」

メモリ工学の5問い: Storage / Load / Write / **Signal Gate** / Cold Start

<div class="grid">
<div class="box">

### The Signal Gate
**いつ「覚えない」か。**
これがないと一度きりのクエリや失敗実験で
メモリが汚染される。

→ SCHEMA の「2ソース以上で作成」
「passing mention では作らない」
= **ノイズを入れない門番**

</div>
<div class="box">

### 検索速度のために整理せよ
cyrilxbt: 「キャプチャの便利さではなく、
**検索の速さ** のために整理せよ」

フォルダ名は保存時には分かるが
**検索時には何も語らない**。

命名・タグ・MOC は全部「引ける速さ」用。

</div>
</div>

**品質は、何を入れるかより何を入れないかで決まる。**

---

# 複利で育つナレッジベースこそが堀

> **「未来は、中央集権的な企業AIツールを使う人々のものではない。
> 自分自身の、複利で育つAIシステムを構築する個人のものだ。」**
> — Garry Tan (GBrain)

- **Fat Skills, Fat Code, Thin Harness** — ハーネスは軽く、価値は知識ベース
- 「本・会議・スキル改善が **減衰せずに蓄積** し、全体が賢くなる」
- 0xJeff: 「Knowledge 層はセッションごとに **複利** で効く」
- Van Horn: **「学習ループは『やめられなくなる』理由のほうだ」**

<div class="small">影もある: ステート肥大 / 検索品質の劣化 / 陳腐化 / そして非可搬性（→ Part 3）</div>

---

<!-- _class: section -->

# Part 3: ハーネスは「何への投資」か

---

# Open Harness と Framework は別物

<div class="grid">
<div class="box">

### Open Harness（使う面）
OpenClaw / Hermes / OpenCode / Pi
- CLI・チャット・ファイル・シェル・MCP
- セッション・承認・サンドボックス
- **広い柔軟性**（使う柔軟性）
- **operator safety**

</div>
<div class="box">

### Framework / Runtime（組み込む面）
Agents SDK / LangGraph / Pydantic AI
- typed state・graph・durable exec
- guardrail・tracing・eval・tenant 分離
- **深い柔軟性**（作る・運用する柔軟性）
- **product / tenant safety**

</div>
</div>

「Framework Irrelevance Thesis」は半分正しく半分間違い——
workflow 抽象は薄れるが、**runtime 抽象（state/permission/memory/policy）は重要化**。

---

# 「ハーネスを捨てても業務ロジックが残る」構成

便利に使うほど溜まる設定・スキル・メモリ = **技術資産** = ロックイン。
さらに **「モデルはハーネスに合わせて post-train される」** → メモリは非可搬。

```
Human Interface / Harness    ← Hermes / OpenClaw（乗り換え可能）
  │ Tool Boundary（MCP / HTTP API）
Agent Control                ← LangGraph / Agents SDK
State & Governance           ← DB / audit log / eval dataset / approval
Execution                    ← container / sandbox / serverless
```

**中核資産（知識ベース・tool API・eval・audit）をどの層にも閉じ込めない。**
私の `wiki/` は Markdown + git。Hermes は薄い・乗り換え可能なメンテナにすぎない。

---

# ハーネスは消えない、移動する

「モデルが賢くなればハーネスは要らない」は **誤り**。
良いモデルは古い足場を不要にするが、**新しい難所と新しい失敗モードを解禁** する。

<div class="grid">
<div class="box">

### 実務に効く3原則
- **検証は出力側に**（テスト・閾値・自己硬化）
- **コンテキストは希少資源**
  （compaction / offload / 目次化）
- **プロンプトは技術的負債**（静かに腐る）

</div>
<div class="box">

### 足し算と引き算
- Ratchet で **足す**（失敗で獲得）
- 陳腐化したら **外す**（モデル進化で）
- 「A が B に勝つ」は
  **共通ハーネス下でのみ妥当**

</div>
</div>

---

<!-- _class: section -->

# Part 4: どこにホストするか——$5 VPS から AWS まで

---

# 安く始め、脳と手を分ける

<div class="grid">
<div class="box">

### まず安く
- 日次ダイジェスト: **$5 VPS** + Gemini + Ollama
- 24/7 アシスタント: **Raspberry Pi + $10/月**
- 痛みが出てから上げる

</div>
<div class="box">

### brain / hands split
- gateway（脳）= 秘密情報・メモリ・スキル
  **インターネット非露出**
- sandbox（手）= コード実行、秘密は **最小権限**
- エンドポイントを増やす = **攻撃面が増える**

</div>
</div>

サンドボックス産業は共通基盤 **Firecracker microVM**（125ms / <5MB / 4000+台）の上に：
Modal（GPU・アイドル無課金）/ Daytona（idle-stop）/ Vercel（堅い鍵）/ Cloudflare / Fly。

---

# AWS にホストする：3ティアの梯子

| | Tier 1: EC2 | Tier 2: ECS + Bedrock | Tier 3: AgentCore |
|---|---|---|---|
| サンドボックス | Lambda(15分上限) | Fargate Ephemeral | **Firecracker microVM/session** |
| LLM | OpenRouter | **Bedrock(IAM, 鍵不要)** | Bedrock |
| 月額目安 | ~$50-70 | ~$70-100 | **~$40-60** |

- **最も洗練された Tier 3 が最も安い**（消費課金・アイドル無課金・NAT 不要）
- **Bedrock は API キー管理を消す**（IAM/SigV4 + CloudTrail で全監査）
- AgentCore: 125ms 起動 / 8時間 / HW分離 / **LLM待ちの I/O は無課金**

---

# PTC：トークンを9割削る

**Programmatic Tool Calling**（AWS 推奨）——
逐次のツール呼び出しを **1本の Python スクリプト** に束ね、最終結果だけ文脈へ。

<div class="grid">
<div class="box">

### 効果
- トークン **87〜92% 削減**
- 月額 **~90% 削減**
  ($15,600 → $1,560 / 1,000実行・日)

</div>
<div class="box">

### 効く理由
- 中間データが文脈に入らない
- 決定的 Python が自然言語推論に勝つ
- 非PTC: Claude系のみ正解 →
  **PTC: 8モデル全て正解**

</div>
</div>

Hermes の `execute_code` / PTC レーンと同じ思想。Part 5 の「トークン経済」への技術的回答。

---

<!-- _class: section -->

# Part 5: 1つの脳から、組織へ

---

# オペレータパターン：脳と体を分ける

1体 → 複数体へ増やすとき、実務者が辿り着く型（Shann Holmberg）:

<div class="grid">
<div class="box">

### Control Room（横の管理面）
> **「体は脳から再構築できる。
> 脳は体から再構築できない。」**

私の `AGENTS.md` + git は
個人スケールの Control Room。

</div>
<div class="box">

### Brain Layers
> **「ブレイン層がワーカーを使い捨てにする。」**

会社の脳は安定、ワーカーは反復。
増設は「独自の鍵/メモリ/役割」が要るとき。

</div>
</div>

> **「本番エージェントはゼロから書けない。育てるものだ。」**
> 前編で半年かけて育てた知識ベースが、まさにこれ。

---

# 組織の Control Plane と、堀のありか

エージェントが増えると **Agent Control Plane** が要る——
Registry / Identity / Permission / Audit / Cost / Eval / Approval / Tenant別メモリ。
= 前編の個人版（git revert・pre-commit・cron監査）の **組織版**。

> **「会社そのものの形が堀になる」**（Foundation Capital）
> エージェント能力は収束し、MCP が乗り換えコストを下げる。
> 差別化は **複利で効く institutional knowledge** の築き方。

**個人**: Markdown wiki に複利知識 ／ **組織**: control plane に複利のデシジョン・トレース。
**同じ形。** 「意思決定の根拠は最も腐りやすい資産。トレースは残る。」

---

# 経済：トークンではなく結果で測る（と逆風）

> **「トークンの請求書は、不安定な量の仕事を表す、安定した単位のコストだ。」**

- 同じ処理でもコストは **5〜10倍** ぶれる（リトライ裾 / 文脈 O(n²) / 過剰ルーティング）
- 実行税: **MiniMax は Gemini より成功タスクあたり 2.3倍安い**（per-token は高いのに）
- 軸は **per token → per outcome（完了した結果あたり）** へ

<div class="small">逆風も直視: 2026/5 後半、AI の ROI は「正当化しづらい」(Uber COO)、FTは大手ROIをマイナス試算。
→ <strong>結果への帰属が要るのは、生のトークン投入が確実にリターンへ変換できていないから。</strong>
個人スケールでも「回し続ける」価値は、出力が実際に判断を変えているときだけ。</div>

---

# まとめ：4つの高度、同じ形

| 高度 | まわりの層 | 前編/後編での現れ |
|---|---|---|
| エンジニアリング | **ハーネス** | 失敗を足場に変える（前編） |
| 個人 | **複利のナレッジベース** | Markdown+git の Second Brain |
| 組織 | **コントロールプレーン / 組織の形** | identity・audit・複利トレース |
| 経済 | **トークン→結果の帰属** | per token ではなく per outcome |

前編の個人の脳は、この一番下の小さな実装。
**Control Room も Ratchet も監査可能な git も、個人と組織で縮尺が違うだけ。**

---

# 開発者への5つの持ち帰り（後編）

1. **ハーネスは薄く、知識資産は厚く、可搬に** — 中核はハーネスの外（DB・git）へ
2. **ハーネスは消えず、移動する** — 足し算(Ratchet)と引き算(削除)の両方
3. **安く始め、痛みで上げる** — $5 VPS → サンドボックス分離 → AgentCore
4. **増やすときは型に従う** — Control Room、ブレイン層、そして **育てる**
5. **個人と組織は相似形** — 複利のファイルが堀、per outcome で測る

> 道具（Hermes）は乗り換えてよい。だが **複利で育つあなた自身のファイル群** だけは、
> ベンダにもハーネスにも預けず、自分の手元（git）に持ち続けること。

---

<!-- _class: lead -->

# Thank You

<div class="small">

**後編記事**: blog/2026-06-03_hermes_agent-as-second-brain-and-the-harness-investment.md
**前編記事**: blog/2026-06-03_hermes_hermes-agent-for-developers.md
**リポジトリ**: github.com/kzinmr/ai-topics
**Hermes Agent**: hermes-agent.nousresearch.com

</div>
