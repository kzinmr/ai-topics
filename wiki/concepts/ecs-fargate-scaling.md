---
title: "ECS Fargate Scaling"
type: concept
created: "2026-04-16"
updated: "2026-04-16"
tags: [aws, ecs, fargate, lambda, scaling, container-orchestration]
aliases: ["ECS scaling", "Fargate auto-scaling", "Container scaling"]
sources: ["https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/"]
status: "draft"
---

# ECS Fargate Scaling

AWS ECS FargateをLambdaのようにスケーリングさせる実験的検証。SQSワークロードでのバーストハンドリング性能を最適化する。

## 背景

Lambdaはスケーリングにおいて最適だが、すべてのワークロードをLambdaで実行できるわけではない。ECS FargateでLambdaに近いスケーリング性能を達成する方法を探る。

## 実験シナリオ

- **トラフィックパターン:** 月間~1億リクエスト（平均40 RPS）、バースト時に10分で30万リクエスト（~500 RPS）
- **ワークロード:** 各メッセージ200msスリープ（処理模擬）
- **成功基準:** 最古メッセージ年齢≈0、可視メッセージ≈0、総処理時間≈エンキュー時間

## 実験結果比較

| メトリクス | Lambda | ECS Custom Metric |
|---|---|---|
| 初回スケール時間 | 数秒 | 2分 |
| 最古メッセージ年齢 | 0秒 | 27秒 |
| 最大可視メッセージ数 | 1 | 13,800 |
| 総バースト処理時間 | 7分 | 7分 |

## 主要ボトルネック

### 内在的遅延
- CloudWatch公開遅延（~1分）+ SQS結果整合性（~1分）= スケーリングトリガーまで~2分
- タスクプロビジョニング時間: イメージPull、コンテナ起動、LB/キュー登録に時間必要

### カスタムメトリクスアプローチ
専用Lambdaで15秒ごとに詳細メトリクスを公開し、CloudWatch/SQSの遅延を回避。メンテナンス負担は増えるが、スケーリング遅延を1分短縮。

## AI Agent設計への示唆

### コンピューティングプール
- ECS FargateはAI Agentの長時間実行コンテナプールとして有用
- Lambdaとの2-3分の初期スケールラグは、Agentのウォームスタート戦略に影響
- カスタムメトリクスによる積極的スケーリングで性能向上可能

### コスト最適化
- 過剰プロビジョニングはECSの経済的優位性を損なう
- 本番環境では少ないベースラインタスクをプロビジョニングし、若干長いバースト処理時間を許容
- Lambdaと比較したコストメリットを維持しつつ、必要なスケーリング性能を確保

### ハイブリッドアーキテクチャ
- 短時間・高頻度タスク → Lambda
- 長時間・状態保持タスク → ECS Fargate
- カスタムメトリクスによる統合監視

## 出典
- [Scaling ECS Fargate like Lambda](https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/)

## See Also

- [[concepts/_index]]
- [[concepts/scaling-without-slop]]
- [[concepts/compute-scaling-bottlenecks]]
- [[concepts/sqs-lambda-esm-scaling]]
