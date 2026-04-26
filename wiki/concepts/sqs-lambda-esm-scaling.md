---
title: "SQS Lambda ESM Scaling"
type: concept
created: "2026-04-16"
updated: "2026-04-16"
tags: ["aws", "sqs", "lambda", "esm", "scaling", "backpressure", "task-queue"]
aliases: ["ESM scaling", "Lambda Event Source Mapping", "SQS scaling behavior"]
sources: ["https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/"]
status: "draft"
---

# SQS Lambda ESM Scaling

AWS LambdaのEvent Source Mapping (ESM)はSQSキューからメッセージをPullし、Lambda関数を自動起動する仕組み。Rehan van der Merweが100回以上の実験で得た知見をまとめる。

## 基本スケーリング動作

- **初期状態:** 5並列呼び出し（1バッチ/呼び出し）
- **スケールアップ:** メッセージが残っている場合、毎分+300並列呼び出し
- **上限:** ESMあたり最大1,250並列呼び出し
- **重要:** キュー深度はスケーリングのトリガーにならない

## 7つのスケーリング挙動

### 1. キュー深度はスケーリングを駆動しない
ESMはキュー深度をスケーリングシグナルとして使用しない。1Kメッセージでも1Mメッセージでも呼び出し・コールドスタート率は同一。

### 2. バッチサイズはコールドスタートに直接影響
バッチサイズを大きくするとコールドスタートは減少するが、呼び出し率はほぼ一定。

### 3. 急激なランプアップ後に急落
ESMは最初に可能な限り速く関数を呼び出し、その後定常状態に急落。短時間関数ほど変動が激しい。

### 4. 大規模デプロイはメトリクスのみのスパイク
大きなパッケージ(~30MB)や環境変数の変更は報告された並列数をスパイクさせるが、スループットには影響しない。

### 5. ESMは最大並列数を超えて呼び出すことがある
ESMは設定された最大並列数を超えて呼び出すことがある。Lambda並列数制限に達してもESMはメッセージをキューに戻さない。

### 6. ESMは必要な以上の並列数をプロビジョニングする
「バインドなし」並列数は定常スループットに必要な値より大幅に高い。

### 7. エラーはスループットに壊滅的影響
1%エラー率 → 20%スループット低下。10%エラー率 → 85%低下。

## AI Agent設計への示唆

### タスクキューパターン
- ESMの振る舞いはAI AgentのバックグラウンドタスクキューとしてSQS+Lambdaを使用する際に重要
- キュー深度がスケーリングのトリガーにならないため、Agentは明示的なバックプレッシャー制御が必要
- バッチサイズ調整によりコールドスタートを最小化できる

### 耐障害性設計
- エラー発生時に投げるのではなく、Batch Item Failureを使用
- べき等性は必須（at-least-onceデリバリー）
- 並列数制限はESM max + 5に設定

### スケーリング最適化
- 短時間処理関数はより高い並列数制限が必要
- 定常状態では必要な並列数の20-70%に設定可能
- エラー率は絶対数ではなく成功率で監視

## 出典
- [7 SQS Lambda ESM Scaling Behaviours](https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/)

## See Also

- [[concepts/_index]]
- [[ecs-fargate-scaling]]
- [[scaling-without-slop]]
- [[lambda-monolith-lambdalith]]
- [[compute-scaling-bottlenecks]]
