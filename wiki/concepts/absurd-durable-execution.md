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

## 参考文献

- [Absurd Workflows: Durable Execution With Just Postgres](https://lucumr.pocoo.org/2025/11/3/absurd-workflows/) — Armin Ronacher (2025-11-03) — 初回発表記事（[[raw/articles/2025-11-03_absurd-workflows-armin-ronacher]]）
- [Absurd In Production](https://lucumr.pocoo.org/2026/4/4/absurd-in-production/) — Armin Ronacher (2026-04-04) — 5ヶ月の本番運用レポート（[[raw/articles/2026-04-04_absurd-in-production-armin-ronacher]]）
- [Absurd 公式ドキュメント](https://earendil-works.github.io/absurd/) — Quickstart, Concepts, Patterns, SDKs
- [Absurd GitHub Repository](https://github.com/earendil-works/absurd) — ソースコード、SDK、比較ドキュメント
- [[entities/armin-ronacher]] — 製作者（Armin Ronacher / @mitsuhiko）のエンティティページ
- [[entities/pi-coding-agent]] — Pi Agent SDK（Absurdとの統合パターンあり）
