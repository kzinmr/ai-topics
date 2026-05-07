---
title: "Absurd (Postgres-Native Durable Execution)"
tags:
  - concept
  - ai-agent-pattern
  - async-processing
  - durable-execution
  - postgres
  - workflow-engine
created: 2026-05-07
updated: 2026-05-07
type: concept
related:
  - entities/armin-ronacher
  - entities/pi-coding-agent
  - concepts/automation-series
  - concepts/functional-core-imperative-shell
  - concepts/single-agent-ceiling
---

# Absurd: Postgres-Native Durable Execution for AI Agents

## 概要

**Absurd**は、Armin Ronacher (Earendil Inc.) によって開発された、**Postgresのみで動作する軽量Durable Executionワークフローシステム**。すべての状態管理と実行ロジックをPostgresのストアドプロシージャ（単一の `absurd.sql` スキーマ）に押し込み、SDKは言語バインディングとして極めて薄く保つ設計が特徴。

> *"... because it's absurd how much you can over-design such a simple thing."*

AI Agent文脈では、LLMループの各イテレーションを**チェックポイント付きステップ**としてモデル化し、プロセスクラッシュやネットワーク障害を透過的にリカバリする**非同期処理基盤の実装パターン**を提供する。

**プロジェクトURL:** https://github.com/earendil-works/absurd
**ドキュメント:** https://earendil-works.github.io/absurd/

---

## アーキテクチャ

### 核心理念

| 要素 | 説明 |
|:---|:---|
| **Postgres-Native** | すべての状態とロジックがデータベース内。追加のサービス、メッセージブローカー、調整レイヤー不要 |
| **Pull-Based Worker** | ワーカーがPostgresからタスクをPullする。Push（オーケストレーター主導）モデルは非対応 |
| **チェックポイント** | タスクはStepに分割され、各Step完了時に結果が永続化。障害時は最後のチェックポイントから再開 |
| **薄いSDK** | 複雑性はDBレイヤーが担当。SDKは各言語のエルゴノミクスを提供するだけ |

### SDKの重量比較（5ヶ月の本番運用実績）

| システム | Python SDK行数 | TypeScript SDK行数 |
|:---|:---:|:---:|
| **Absurd** | ~1,900 | ~1,400 |
| **Temporal** | ~170,000 | — |

この差が示すのは、複雑性をDBストアドプロシージャに移すことで、アプリケーションSDKを驚くほどシンプルに保てるという設計判断の正当性。

### 制約事項（2026年5月時点）

- **ビルトインスケジューラーなし**: Cron的な定期実行は手動ループ＋冪等性キーで実装必要
- **Pushモデルなし**: Webhookによるタスク起動は未サポート（別ライブラリとして提案中）
- **パーティショニング課題**: データクリーンアップのコストが高く、`DETACH PARTITION CONCURRENTLY` のトランザクション外実行が困難
- **MVCC Bloatリスク**: Postgresのキュー運用に固有のMVCCデッドタプルの蓄積リスク（[[raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale]]参照）。特に混合ワークロード下では、長時間クエリがMVCC Horizonを固定し、`autovacuum`が追いつかなくなる「死亡スパイラル」に陥る可能性がある。

---

## AI Agent文脈での実装パターン

### 1. LLM Agent LoopのDurable化（基本パターン）

Absurdの中核的な使い方は、LLMエージェントのループを**チェックポイント付きステップ**としてモデル化すること。各LLM呼び出しが `ctx.step()` でラップされ、障害時に最後の完了ステップから再開される。

```typescript
app.registerTask({ name: "my-agent" }, async (params, ctx) => {
  let messages = [{ role: "user", content: params.prompt }];
  let step = 0;
  while (step++ < 20) {
    const { newMessages, finishReason } = await ctx.step("iteration", async () => {
      return await singleStep(messages);
    });
    messages.push(...newMessages);
    if (finishReason !== "tool-calls") break;
  }
});
```

**ポイント:** 同じStep名（`"iteration"`）を繰り返し使うと、Absurdが自動的にインクリメントしてユニークなチェックポイントとする。これによりループ構造でも正しくリプレイ可能。

### 2. Pi AI Agent Durable Turns（具体的な統合パターン）

Absurdドキュメントには、Pi Agent SDKとの統合パターンが公式に記載されている。これはAI Agent文脈での最も具体的な非同期処理基盤の実装例。

**仕組み:**

1. 各 `message_end` イベントをStepログに追記
2. リトライ時にそのログからAgentコンテキストを再構築
3. 最後のメッセージが `assistant` でない場合、`runAgentLoopContinue()` で再開

```typescript
app.registerTask({ name: "run-agent" }, async (params: Params, ctx) => {
  let { messages, nextHandle } = await loadMessageLog(ctx);
  
  const context: AgentContext = {
    systemPrompt: params.systemPrompt,
    tools,
    messages,
  };

  const persistEvent = async (event: AgentEvent) => {
    if (event.type !== "message_end") return;
    await ctx.completeStep(nextHandle, { message: event.message });
    context.messages.push(event.message);
    nextHandle = await ctx.beginStep<MessageLogEntry>("message");
  };

  const last = context.messages.at(-1);
  if (!last) {
    // 初回: ユーザープロンプトを追加して継続
    const userPrompt = { role: "user", content: params.userMessage, timestamp: Date.now() };
    await ctx.completeStep(nextHandle, { message: userPrompt });
    context.messages.push(userPrompt);
    nextHandle = await ctx.beginStep<MessageLogEntry>("message");
  } else if (last.role === "assistant") {
    // 前回完了済み → 何もしない
    return;
  }

  await runAgentLoopContinue(context, config, persistEvent);
});
```

このパターンは以下を実現する:
- **Agentターンレベルの耐久性**: ターン内の各メッセージ交換がPostgresに永続化される
- **透過的リカバリ**: ワーカープロセスが死んでも、再起動後にメッセージログからコンテキストを完全再構築
- **進行中のターンの再開**: 前回の実行がassistant応答で終わっていなければ、ループを継続

### 3. イベント駆動型Agent間連携

SleepとEventメカニズムにより、複数エージェント間の非同期連携がPostgresのみで実現可能:

```typescript
// Agent A: 支払い処理後にイベント発行
await absurd.emitEvent(`payment.completed:${orderId}`, { 
  amount: 9999, currency: "USD" 
});

// Agent B: 支払い完了を待って出荷処理
const payment = await ctx.awaitEvent(`payment.completed:${orderId}`, { 
  timeout: 3600 
});
```

**Eventの特性:**
- Cacheされる（"first emit wins"）ため、競合状態が発生しない
- Timeout付きで待機可能（指定時間経過後は自動復帰）

---

## 競合比較

### Temporalとの違い

| 軸 | Absurd | Temporal |
|:---|:---|:---|
| **インフラ** | Postgresのみ | Temporal Server（独自サービス）必須 |
| **SDK重量** | ~1,400–1,900行 | ~170,000行（Python） |
| **リプレイモデル** | チェックポイントベース（Step境界のみ） | 決定論的リプレイ（全体の関数が決定論的である必要） |
| **非決定論的操作** | Step間では `Math.random()` 等が使用可能 | 厳密に禁止 |
| **セルフホスト** | 極めて簡単 | 複雑 |

### DBOSとの違い

DBOSもPostgres-NativeのDurable Executionシステムだが、SDKの重量が大きい（40k行 vs Absurdの2k行）。AbsurdはDBストアドプロシージャにロジックを集中させることで、SDKを極限まで薄く保つ。

### PGMQとの違い

PGMQはSQSライクなPostgresメッセージキュー。キュー＋状態ストアの組み合わせでDurable Executionを実現するAbsurdとは異なり、PGMQは純粋なトランスポートレイヤーであり、チェックポインティングやリトライの耐久性は含まれていない。

### Inngestとの違い

InngestはHTTPベースのPushモデル。AbsurdはPullベース。InngestはDebouncing、Throttling、Batchingなどの高レベルプリミティブを持つが、Absurdは意図的にこれらを排除している。また、InngestはSSPLライセンス（将来ライセンス変更条項あり）、AbsurdはApache 2.0。

---

## AI Agent基盤としての評価

### 適合するユースケース

1. **セルフホスト型AI Agent**: TemporalやInngestのような外部サービスに依存できない環境。Postgresさえあれば動作する。
2. **長時間実行Agent**: 数分〜数日かかるAgentワークフロー。Sleep/Eventで一時停止・再開可能。
3. **マルチステップAgent**: 各Tool CallやLLM呼び出しを独立的なチェックポイントとして管理したい場合。
4. **Agent間イベント連携**: Event機構を使った疎結合なAgent間通信。

### 注意点

1. **LLM呼び出しコスト**: Stepの再実行を防ぐ設計とはいえ、`ctx.step()` 内の処理が失敗するとコストのかかるLLM呼び出しが再発生する可能性がある。
2. **Push不在**: WebhookベースのAgent起動には別途アダプター実装が必要。
3. **データクリーンアップ**: 長期稼働でタスク・イベントデータが蓄積。定期的なRetentionポリシーの設定が運用上の必須項目。

---

## PG Queue運用の観点からの批判的レビュー

> 本セクションはPlanetScaleの記事「[[raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale|Keeping a Postgres Queue Healthy]]」の知見を基に、Absurdのアーキテクチャ上のリスクを評価する。

### 前提：Absurdが正しくやっていること

| Absurdの実装 | PG Queueのベストプラクティス | 評価 |
|:---|:---|:---:|
| `FOR UPDATE SKIP LOCKED` を使用 | PlanetScale: 「常にSKIP LOCKEDを使え」 | ✅ |
| パーティションストレージモードを提供 | 大規模テーブルの管理に有効 | ✅ |
| pg_cron経由の定期クリーンアップ関数（`cleanup_tasks`, `ensure_partitions`, `schedule_detach_jobs`） | PlanetScale: 「リソース制御を実装せよ」 | ✅ |
| 冪等性キー（`i_` テーブル） | PlanetScale: 「リトライを実装せよ」 | ✅ |
| Unpartitioned Modeの `fillfactor=70` | 更新頻度の高いテーブル向けの定石 | ✅ |

Absurdの作者はPG Queue運用の基本を理解しており、多くのベストプラクティスに従っている。しかし、Durable Executionというレイヤーが上乗せされることで、単純なキューでは発生しない複合的なリスクが生じる。

---

### 問題1：Checkpoint による増幅された書き込み負荷

通常のPGキューは「INSERT → READ → DELETE」の単一テーブルで完結する。Absurdは**1タスクあたり最大6テーブル**（`t_`=Tasks, `r_`=Runs, `c_`=Checkpoints, `e_`=Events, `w_`=Wait Registrations, `i_`=Idempotency Keys）に書き込む。

**試算：20ステップのLLM Agentループが3回リトライした場合**
```
1 task + 3 runs + 20 checkpoints + 1 event + 1 wait registration
= 26 rows created → cleanup実行まで26のdead tupleが蓄積
```

PlanetScaleの核心的な警告を再掲する：

> "A database is destined to fail if it cannot reclaim dead tuples faster than its workload creates them."

Absurdは単純なジョブキューより**数倍多くのdead tupleを生成する**。`fillfactor=70`（30%の空き領域を確保）という設計判断は、この問題への暗黙の認識と見なせる。ただしfillfactorは「B-Treeページ内の空き容量」を増やすだけで、**MVCC Horizonが固定された場合の抜本的な解決にはならない**。

---

### 問題2：「Just Postgres」がもたらす混合ワークロードの罠

Ronacherは「Just Postgres — no additional infrastructure」をAbsurdの最大のセールスポイントにしている。しかしPlanetScaleの記事は、**これが最大の危険信号**だと警告する。

特にAI Agentワークフローでは、以下の要因がMVCC Horizon固定のリスクを高める：

| シナリオ | MVCC Horizonへの影響 |
|:---|:---|
| LLM呼び出し待ちのSleep — `sleep(3600)` | 行は生存し続け、同じインスタンス上の分析クエリがHorizonを固定 |
| Agent思考ループ中の並行分析クエリ | PlanetScaleが「Staggered Query Trap」と呼ぶ状態 — クエリが20秒間隔で立ち上がり、Horizonが永久に進まない |
| Event待ちの長時間サスペンド — `awaitEvent(timeout: 86400)` | Wait Registration行が24時間生存 |

PlanetScaleの800 jobs/secベンチマークが示す通り、Absurd自体が高速に動作しても、**同じインスタンス上の他のワークロードがMVCC Horizonを固定すれば、Absurdのテーブルだけが異常肥大化する**。

---

### 問題3：Unpartitioned Mode の死亡スパイラル

AbsurdのデフォルトはUnpartitioned Mode。PlanetScaleのベンチマーク結果：

| 条件 | Queue Backlog | Lock Time | 結果 |
|:---|:---:|:---:|:---:|
| Queue単体（800 jobs/sec） | 0 | 2ms | ✅ 安定 |
| Queue + 重複分析クエリ | **155,000 jobs** | **300ms+** | ❌ 死亡スパイラル |

特に注意すべきは、Absurdの**Checkpointテーブル（`c_`）のB-Tree肥大化**。通常のキューと異なり、Checkpointはタスク完了後もクリーンアップTTLが来るまで削除されない。その間、以下の悪循環が発生する：

1. B-Treeが肥大化 → スキャンコスト増大
2. Lock Timeが増加 → ワーカーのスループット低下
3. 未処理タスクが滞留 → さらに多くのCheckpointが生成
4. `autovacuum`が追いつかない → B-Treeのbottom-up deletionも効果を発揮できない

PlanetScaleの記事は「Postgres v18になっても、天井は上がっていない」と結論づけている。

---

### 問題4：クリーンアップのタイミングミスマッチ

Absurdの `cleanup_tasks` はpg_cronで定期実行できる。しかし：

1. **頻度の問題**: デフォルトのcron式 `17 * * * *`（毎時17分）は、800 jobs/secの環境で生成されるdead tuple量に到底追いつかない
2. **DELETEの自己矛盾**: cleanup自身のDELETEが新たなdead tupleを生む。DELETEが空き領域をすぐに回収できるわけではない
3. **VACUUM不在**: AbsurdはDELETEを実行するが、`VACUUM`との連携戦略は提供していない。削除してもすぐに領域は返却されない
4. **監視の欠如**: PlanetScaleは「Creeping lock times = デッドタプル蓄積の先行指標」と指摘するが、Absurdはこのメトリクスを監視する仕組みを持たない。Habitatダッシュボードはタスク状態を表示するが、テーブルBloat率やLock待ち時間は見えない

---

### 問題5：イベントテーブルの無制限蓄積

Event機構は `e_` (Emitted Events) テーブルを使用する。「first emit wins」の設計は競合状態を排除する点で優れているが、**TTLが来るまでイベント行は削除されない**。

Agent間連携パターンで問題となるのは：
- `emitEvent('user-activated:alice', ...)` → 受信ワーカーは1度だけ消費
- しかしイベント行はcleanup TTLまで生存 → 全Agentの全イベントが蓄積
- イベント名のユニーク性が高いほど（`user-activated:{userId}`）、削除条件のマッチングが複雑になる

大量のイベントが蓄積すると、`awaitEvent()` の検索が `e_` テーブルのフルスキャンに近づく。

---

### 問題6：パーティションモードの限界

Absurdは週次レンジパーティション（UUIDv7ベース）を提供している。しかし：

1. **パーティション内のMVCC問題**: パーティションを切っても各パーティション内でのMVCC bloatは解決されない。単に「1つの大きなテーブル」が「複数の小さなテーブル」になるだけ
2. **DETACH PARTITIONの困難さ**: Ronacher自身がproduction retrospectiveで認めている通り、`DETACH PARTITION CONCURRENTLY` のトランザクション外実行はPostgresの制約上難しい
3. **パーティションプランナーのオーバーヘッド**: 多数のパーティションを持つテーブルに対するクエリは、パーティションプルーニングが効かないケースでかえって遅くなる

---

### 総評：適切なスコープと危険ゾーン

**Absurdが適切なシナリオ：**
- 低〜中スループット（< 100 tasks/sec）
- Postgres専用インスタンス（混合ワークロードなし）
- 短命タスク（分単位で完了）、Checkpoint数が少ない
- インフラを増やせない自己ホスト環境

**危険ゾーン：**
- 高スループット（> 500 tasks/sec）＋同一DBの分析クエリ → 死亡スパイラル確実
- 数時間〜数日かかるAgentワークフローの大量並行実行 → Sleep行の生存によるBloat
- 100+ Checkpointを持つAgentの大量実行 → `c_`テーブルの爆発的肥大化
- 複数サービスが同一Postgresインスタンスを共有する環境

**結論：** Absurdは「PostgresだけでDurable Execution」というアイデアのエレガントな実装だが、そのトレードオフはSDKの薄さ以上に深い。PG Queue運用の古典的問題（MVCC bloat、混合ワークロード分離）は、薄いSDKに複雑性を押し込まない代わりに、**運用者に完全に委ねられている**。Temporalが専用Server/SDKレイヤーでこれらの問題を吸収しているのに対し、Absurdは「Postgresさえ面倒見ればいい」という一見シンプルな運用を、高負荷下では**逆説的に複雑**にする。適切なスコープを見極めた上で採用すべきであり、「Just Postgres」の主張を額面通りに受け取るべきではない。

---

## 参考文献

- [Absurd Workflows: Durable Execution With Just Postgres](https://lucumr.pocoo.org/2025/11/3/absurd-workflows/) — Armin Ronacher (2025-11-03) — 初回発表記事（[[raw/articles/2025-11-03_absurd-workflows-armin-ronacher]]）
- [Absurd In Production](https://lucumr.pocoo.org/2026/4/4/absurd-in-production/) — Armin Ronacher (2026-04-04) — 5ヶ月の本番運用レポート（[[raw/articles/2026-04-04_absurd-in-production-armin-ronacher]]）
- [Absurd 公式ドキュメント](https://earendil-works.github.io/absurd/) — Quickstart, Concepts, Patterns, SDKs
- [Absurd GitHub Repository](https://github.com/earendil-works/absurd) — ソースコード、SDK、比較ドキュメント
- [Keeping a Postgres Queue Healthy](https://planetscale.com/blog/keeping-a-postgres-queue-healthy) — PlanetScale (2026-05-07) — PG Queue運用のベストプラクティスとMVCC Bloat分析（[[raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale]]）
- [[entities/armin-ronacher]] — 製作者（Armin Ronacher / @mitsuhiko）のエンティティページ
- [[entities/pi-coding-agent]] — Pi Agent SDK（Absurdとの統合パターンあり）
