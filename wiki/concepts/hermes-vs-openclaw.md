---
title: "Hermes Agent vs OpenClaw — アーキテクチャ比較"
created: 2026-05-07
updated: 2026-05-07
type: comparison
tags:
  - comparison
  - agentic-engineering
  - architecture
  - ai-agents
  - openclaw
  - harness-engineering
  - skills
  - context-engineering
  - memory-systems
  - gateway
sources:
  - raw/articles/2026-05-07_chatgpt-hermes-vs-openclaw-comparison.md
  - raw/articles/2026-05-07_chatgpt-openclaw-architecture-deep-dive.md
---

# Hermes Agent vs OpenClaw — アーキテクチャ比較

## 概要

Hermes Agent と OpenClaw は、どちらも自律型 AI エージェントを永続実行するオープンソースプラットフォームだが、その設計哲学は根本的に異なる。Hermes は **エージェントコア中心主義**（`AIAgent` に全 orchestration を集約）をとり、OpenClaw は **ゲートウェイ中心主義**（長寿命 Gateway を制御面とし、agent runtime はその中に埋め込まれる）をとる。

両者の分岐点を一言で言えば、**Hermes = 能力蓄積型システム（capability accumulation）、OpenClaw = スコープ制御型制御面（scope-controlled control plane）** である。この違いは、スキル管理、プロンプト設計、サブエージェント実行、拡張モデル、セキュリティ前提のすべてに波及している。

Hermes（v0.9.0、2026年4月13日公開）は `run_agent.py` の `AIAgent` クラスを中心に、prompt assembly、provider resolution、tool execution、compression、fallback を単一のコアに集約する。OpenClaw（2026年3月〜4月時点）は Gateway daemon を中心に、typed WebSocket protocol、embedded pi agent runtime、sandbox/approvals、nodes、plugins を束ねる「assistant control plane」として設計されている。

この比較は、両者の公式ドキュメントとアーキテクチャ詳細分析（2026年5月）に基づく。Hermes は Nous Research（Teknium 率いる）が開発し、OpenClaw は Peter Steinberger（@steipete、元 PSPDFKit CEO）が開発した。

## コア設計哲学

| 次元 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| **設計重心** | `AIAgent`（エージェントコア）| Gateway（制御面） |
| **哲学** | 能力蓄積 — デフォルトで多くをバンドルし、エージェント自身が拡張する | スコープ制御 — 最小限のプリミティブから、ユーザーが意図的に構築する |
| **比喩** | Rails（フルスタック、設定より規約）| Linux/Kubernetes（プリミティブ、明示的制御） |
| **デフォルト状態** | 123+ バンドルスキル、300+ ツールゲートウェイ | ベースラインスキルのみ、新スキルは ClawHub へ |
| **ターゲットユーザー** | 即日生産性重視。最小セットアップで使い始めたい | プロダクションチーム。100% 制御と予測可能性を要求 |
| **アーキテクチャスタイル** | コア集約型（prompt/tool/session/compression/fallback を1つの `AIAgent` に）| 制御面分散型（Gateway → WS protocol → embedded agent → sandbox/nodes） |

Hermes は「設定より規約」で強力なデフォルトパスを提供し、OpenClaw は「プリミティブよりデフォルトなし」で保証を提供する。Hermes の強力なオピニオンが leverage を生む場面では大きな生産性を発揮し、OpenClaw の明示性は「午前3時に障害が起きても grep 一発で原因特定できる」予測可能性をもたらす。

## アーキテクチャ比較表

| 次元 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| **コア** | `run_agent.py` の `AIAgent` — 単一クラスに prompt assembly、provider resolution、tool execution、compression、fallback を集約 | Gateway（長寿命 daemon）+ 埋め込み pi agent runtime — Gateway が state の source of truth |
| **状態管理** | SQLite + FTS5 (`state.db`) + JSONL transcripts。session ID、platform、user、model、token counts、親 session ID を保持 | `sessions.json`（軽量 registry）+ `<sessionId>.jsonl`（append-only transcript tree） |
| **メモリ** | 三層: bounded `MEMORY.md`/`USER.md` + FTS5 検索可能 session archive + optional external memory provider（Honcho/RetainDB/ByteRover）| ファイル駆動: workspace 内の `MEMORY.md`（prompt 常駐）+ `memory/*.md` daily files（tool 経由 on-demand） |
| **プロンプト組立** | cached system prompt（SOUL→tool guidance→Honcho→MEMORY snapshot→USER snapshot→skills index→context files→timestamp→platform hint）+ ephemeral layer 分離 | OpenClaw-owned system prompt（Tooling/Safety/Skills/Self-Update/Workspace/Sandbox の固定セクション）+ provider plugin による部分差し替え |
| **プロンプトキャッシュ戦略** | stable prefix 重視。frozen memory snapshot、mid-session 不変。Anthropic native で system prompt + 直近3 non-system messages を cache（TTL 5分）| cache boundary を意識した stable prefix + dynamic suffix。provider plugin が `interaction_style`/`tool_call_style`/`execution_bias` を差し替え |
| **ツール実行** | self-registering registry（`registry.register()` auto-discovery）+ MCP tools + plugin tools。toolset 単位の管理、`check_fn` による availability 判定 | sandbox / tool policy / elevated の三者分離。`host=auto|sandbox|gateway|node`、`security=deny|allowlist|full`、`ask=off|on-miss|always` |
| **サブエージェント** | `delegate_task`（child `AIAgent`、fresh conversation、separate terminal、最大3並列）+ `execute_code`（sandboxed Python executor、RPC tool call）の二種 | background task として spawn。独自 session `agent:<agentId>:subagent:<uuid>`。`maxSpawnDepth` 制御、tool policy は depth で変化 |
| **ゲートウェイ** | 14+ messaging platform 対応の常駐 `GatewayRunner`。two-level message guard、interrupt/queue、slash command dispatch | Gateway 自体が製品の中核。WS protocol、device identity + pairing、typed JSON Schema、queue（session lane + global lane、`collect`/`steer`/`interrupt` mode） |
| **セキュリティモデル** | terminal tool の `DANGEROUS_PATTERNS` + approval flow（CLI/gateway 承認、session 単位、永続 allowlist、smart approval）| personal assistant trust model（単一 trust boundary）。sandbox + tool policy + elevated + channel allowlists + prompt 非依存の hard stop |
| **拡張** | Python plugins（general/memory provider/context engine）+ hooks（`pre_tool_call`/`post_tool_call`/`pre_llm_call`/`post_llm_call`/`on_session_start`/`on_session_end`）| 4層 plugin architecture（Manifest+discovery→Enablement+validation→Runtime loading→Surface consumption）。native plugins は Gateway と同一プロセス、unsandboxed |
| **ノード/分散** | terminal backend（local/docker/ssh/singularity/modal/daytona）| WS 接続 nodes（`role: node`）。device identity + pairing + capability 広告（`canvas.*`/`camera.*`/`screen.record`/`location.get`）。per-agent allowlist |
| **通信プロトコル** | callback surface（`tool_progress_callback`/`thinking_callback`/`stream_delta_callback`）— 複数 front-end が共有 | typed WebSocket protocol（`connect`→`req/res`+`event`→TypeBox→JSON Schema→Swift models）。live control channel、replay なし |
| **実行モード** | 3 API execution mode（`chat_completions`/`codex_responses`/`anthropic_messages`）+ auxiliary task 用の独立 provider routing | 単一埋め込み `runEmbeddedPiAgent()`。`promptMode=minimal` で sub-agent 用軽量モード |
| **状態即時性** | frozen snapshot 方式 — mid-session の memory 変更は prompt に即時反映されず、次 session から有効 | Gateway が source of truth — UI は Gateway に問い合わせ。remote mode では local machine の状態は無意味 |
| **割り込み/キュー** | interruptible call 標準装備。CLI/gateway とも実行中に新規入力で停止可能。複数 tool call は interactive 逐次 + non-interactive 並列 | 多段階キューイング（session lane + global lane）。`collect`/`followup`/`steer`/`steer-backlog`/`interrupt` モード。tool boundary 実行中注入 |
| **プロバイダ解決** | 全 feature 共有の resolver（明示指定 > config.yaml > env var > provider defaults/auto）。auxiliary task は main と独立 routing | provider plugin として抽象化。Gateway が generic agent loop・failover・transcript handling を持ち、provider 固有差分のみ hook surface で渡す |
| **永続性/圧縮** | middle turns を要約圧縮。親 session ID 保持で「軽量現役 session + 検索可能祖先履歴」を両立。compression 後 session lineage 分岐 | `sessions.json`（軽量 registry）+ append-only JSONL transcript（id/parentId tree 構造）。compaction と history limiting を Gateway 側で制御 |

## スキルシステム詳細比較

スキル管理は両プラットフォームの設計哲学の違いが最も鮮明に現れる領域である。

### Hermes: 自己生成・増殖型（Capability Accumulation）

Hermes のスキルシステムは **エージェント自身がスキルを作成・拡張する能力蓄積モデル** である。公式 docs では `skills` toolset として位置づけられ、skills hub からロード・管理される。

- **生成**: 自律的 — プロンプトナッジ + バックグラウンドレビューでエージェントが `SKILL.md` を自己生成
- **発見**: 全スキルが全エージェントから可視。スキルインデックスは常に system prompt（cached system prompt の7番目の要素）に注入される
- **重複排除**: 「既存スキルがカバーしていればパッチする」という粗いルールのみ
- **増殖制御**: 現状なし（これがスキル爆発問題を引き起こす）
- **コーパス健全性**: 統合より生成が速い。放置すると腐敗リスク
- **バンドル数**: 123+ のバンドルスキル（GitHub PR, Obsidian, Google Workspace, Linear, Notion, Typefully, Perplexity, deep research, Minecraft 等）

**構造**: バンドルスキルがデフォルトで全エージェントにロードされ、prompt 内の skills index を通じて常時発見可能。新スキルは自律生成され、コーパスに蓄積されていく。この「デフォルトで全部入り」アプローチは即日生産性に直結する。

### OpenClaw: 索引注入・許可リスト型（Supply-Chain Governance）

OpenClaw のスキルシステムは **供給連鎖（supply-chain）アプローチ** である。AgentSkills 互換の `SKILL.md` フォルダを複数ソースからロードする。

- **生成**: 明示的 — ユーザーの意図が必要。コアスキル追加は「稀であるべきで、強い製品上またはセキュリティ上の理由が必要」（VISION.md より）
- **発見**: 適格性チェックが発見とは分離。system prompt にはスキル本体ではなく **name/description/location のコンパクトリスト** のみ注入。model は必要時に `read` で `SKILL.md` を demand-load
- **重複排除**: 5段階優先順位システム（workspace > user global > managed > bundled > extra）
- **増殖制御**: Byte caps、candidate caps、symlink 拒否。許可リスト方式による決定論的制御
- **コーパス健全性**: 意図なしに何も追加されないため腐敗しない
- **バンドル数**: ベースラインのみ（managed / workspace / ClawHub 経由で拡張）

**構造**: bundled（ベースライン）+ managed + workspace + extra の4層ソースからロード。全スキル本文を prompt に常駐させない token 効率設計。deterministic overhead を docs が明示的に説明しており、context pressure を強く意識している。

### 設計トレードオフ比較

| 評価軸 | Hermes（能力蓄積）| OpenClaw（供給連鎖）|
|--------|----------------|-------------------|
| 初期生産性 | ★★★★★ — 123+ スキルがデフォルト | ★★★ — 必要なものを明示的に追加 |
| 長期健全性 | ★★ — 増殖 > 統合のリスク | ★★★★★ — 原理的に腐敗しない |
| デバッグ容易性 | ★★ — どのスキルがトリガーされたか不明瞭 | ★★★★★ — grep 一発で特定可能 |
| Token 効率 | ★★★ — スキルインデックスは常駐 | ★★★★★ — メタデータのみ常駐、本文 demand-load |
| 適応速度 | ★★★★★ — 自律生成で即時適応 | ★★★ — ユーザーの意図を待つ |

### スキル爆発問題（Hermes 固有）

**観測された挙動**: エージェントは「これをボトルに詰めるべき（将来再利用可能）」という発見（creation trigger）には優れるが、「すでに3フォルダ隣にボトルがある」という発見（deduplication trigger）には弱い。結果として、同じ概念ドメインに複数の冗長スキルが生成される。

**実例**: デスクトップから画像を読むタスク → `browser_read` スキル試行 → `vision` スキル試行 → どちらも失敗 → 3つ目の `read-local-image` スキルを作成。同一ドメインに3スキルが乱立。

**根本原因**: Hermes のエージェントは自律的なスキル生成能力を持つが、スキル間の横断的重複検出の仕組みが粗い（「既存スキルがカバーしていればパッチする」ルールのみ）。これにより、時間とともにスキルコーパスが統合より速く増殖する「エントロピー増大」が発生する。

**構造的課題**: この問題は Hermes の能力蓄積モデルに内在する。自律生成能力とコーパス健全性はトレードオフであり、生成を止めれば適応速度が落ち、生成を許せば重複が蓄積する。

**想定される解決**:
1. 呼び出しメトリクスに基づく統合パス（使用頻度の低いスキルを自動アーカイブ・統合）
2. スキル作成時のより強い重複排除（ベクトル類似度や機能シグネチャ比較）
3. 定期的な「スキルコーパス健全性チェック」エージェントの実行
4. 利用統計に基づくスキルライフサイクル管理（作成→利用→統合→アーカイブ）

**OpenClaw の対処法**: 5段階優先順位システムにより、どのスキルがいつトリガーされるかが決定論的にデバッグ可能。許可リスト方式（byte caps, candidate caps, symlink 拒否）のため、意図しないスキル増殖が原理的に発生しない。VISION.md が「コアスキル追加は稀であるべき」と明文化していることも、組織的なガバナンスとして機能する。

## プロンプトアーキテクチャ

両者とも prompt-cache-aware な設計だが、戦略は異なる。

### Hermes: Stable Prefix + Frozen Snapshot

- **cached system prompt** と **ephemeral additions** を明確に分離
- 組み立て順は固定的: SOUL → tool guidance → Honcho → MEMORY snapshot → USER snapshot → skills index → context files → timestamp → platform hint
- memory も context files も **mid-session では基本的に固定**（cache stability のため）
- Anthropic native では system prompt + 直近3 non-system messages を cache、TTL 5分
- context compression と併用し、stable prefix をなるべく不変に保つ

### OpenClaw: Platform-Owned Prompt + Provider Hooks

- system prompt は **OpenClaw-owned**（pi-coding-agent default prompt を使わない）
- Tooling、Safety、Skills、Self-Update、Workspace、Sandbox、Time、Reply Tags、Heartbeats、Runtime、Reasoning の固定セクション
- prompt は persona 文というより **runtime の操作マニュアル兼 policy hint**
- provider plugin は `interaction_style`、`tool_call_style`、`execution_bias` を部分差し替え
- sub-agent 用 `promptMode=minimal` では Skills、Memory Recall、Self-Update、User Identity、Messaging、Heartbeats を削除
- workspace bootstrap files（`AGENTS.md`/`SOUL.md`/`TOOLS.md` 等）が毎ターン trimmed/truncated 注入

**分岐点**: Hermes は prompt を「人格・規律・記憶・スキル索引・プロジェクト文脈・プラットフォーム表現を合成した構造体」として扱い、OpenClaw は「runtime 操作マニュアル + policy enforcement 文書」として扱う。

## キーインサイト：Rails vs Linux

この比較から浮かび上がる最も重要な洞察は、両者が AI エージェントプラットフォームの**異なるゲーム**をプレイしていることである。

| | Hermes Agent（Rails）| OpenClaw（Linux） |
|---|---|---|
| **提供するもの** | 強力なデフォルト | 保証されたプリミティブ |
| **価値命題** | 「設定より規約」— デフォルトパスがハッピーパス | 「言ったことだけを、それ以上は何もしない」 |
| **拡張モデル** | 能力蓄積 — エージェントが自ら学び、スキルを増やす | スコープ制御 — ユーザーが明示的に構築・許可する |
| **リスク** | スキル爆発、コア実装の複雑性集中 | Gateway が trust bottleneck、設定負荷が高い |
| **最適な用途** | 個人の生産性最大化、高速な立ち上げ | プロダクション信頼性、チーム運用、決定論的デバッグ |

Hermes の戦略的優位は「OpenClaw のコピーにならない」ことにある。自己生成・バンドルデフォルト・ツールゲートウェイロックインという異なるゲームを創出した。OpenClaw の戦略的優位は、ガバナンスパターン・優先順位モデル・明示的ツールルーティングといった**業界標準になりつつある基盤パターン**を定義したことにある。

## 相互学習 — 各プラットフォームが相手から学べること

### Hermes が OpenClaw から学べること

1. **スキルガバナンス**: 5段階優先順位システムと許可リスト方式の導入により、スキル爆発問題を構造的に解決できる
2. **決定論的デバッグ**: 「grep 一発で原因特定」の予測可能性。スキルトリガーの明示性を高める設計
3. **実行安全性の分離**: sandbox / tool policy / elevated の三者分離は、prompt ベースの safety より堅牢
4. **ノードアーキテクチャ**: device identity + pairing + capability 広告の仕組みは、マルチデバイス展開に有効
5. **キューイング制御**: `collect`/`steer`/`interrupt` モードによる実行中入力の整合性管理

### OpenClaw が Hermes から学べること

1. **能力蓄積ループ**: エージェントの自己改善・スキル自己生成は、ユーザーの設定負荷を劇的に下げる
2. **バンドルデフォルトの力**: 123+ スキルをデフォルトで持つことは、ユーザー獲得の強力なレバレッジ
3. **三層メモリ**: bounded memory + searchable archive + external provider の分離は、長寿命エージェントの記憶管理として優れている
4. **複数実行プリミティブ**: `delegate_task` と `execute_code` の使い分け（判断重視 vs 機械的パイプライン）は token 効率に寄与
5. **auxiliary task routing**: main model とは独立した provider/model 選択は、コスト最適化の余地を広げる

## 総括比較表

| 評価軸 | Hermes Agent | OpenClaw | 優位 |
|--------|-------------|----------|------|
| 即日生産性 | ★★★★★ | ★★★ | Hermes |
| プロダクション信頼性 | ★★★ | ★★★★★ | OpenClaw |
| スキル管理の健全性 | ★★ | ★★★★★ | OpenClaw |
| 自己改善能力 | ★★★★★ | ★★ | Hermes |
| 決定論的デバッグ | ★★★ | ★★★★★ | OpenClaw |
| メモリ/文脈管理 | ★★★★★ | ★★★ | Hermes |
| マルチデバイス展開 | ★★★ | ★★★★★ | OpenClaw |
| セットアップ容易性 | ★★★★★ | ★★★ | Hermes |
| 実行時安全性 | ★★★★ | ★★★★★ | OpenClaw |
| 拡張性（plugin/ecosystem）| ★★★★ | ★★★★★ | OpenClaw |

## 関連ページ

- [[concepts/hermes-agent-architecture]] — Hermes Agent のアーキテクチャ詳細
- [[concepts/openclaw-architecture]] — OpenClaw のアーキテクチャ詳細
- [[concepts/openclaw-philosophy-primitives-over-defaults]] — OpenClaw のプリミティブ哲学
- [[concepts/openclaw-ecosystem]] — OpenClaw エコシステム
- [[concepts/hermes-models]] — Hermes モデルファミリー
- [[entities/hermes-agent]] — Hermes Agent エンティティページ
- [[entities/openclaw]] — OpenClaw エンティティページ
