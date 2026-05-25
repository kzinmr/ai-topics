---
title: "Macro Evals for Agentic Systems"
source: "https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems"
date_ingested: 2026-05-25
author: "Shikhar Kwatra, Will Thieme, Bradley Strauss (OpenAI × Slalom)"
published: 2026-05-19
type: cookbook
tags:
  - agent-evaluation
  - evaluation
  - observability
  - trace-analysis
  - bertopic
  - promptfoo
  - agents-sdk
  - multi-agent
---

# Macro Evals for Agentic Systems

OpenAI Cookbook（Slalom との共同制作）。マルチエージェントシステムにおいて、数千のエージェントイベントから少数の理解可能な行動パターンを抽出するためのマクロ評価ワークフローを解説。

## コアアイデア

- **Lower-level evals**: 個別のエージェント、ハンドオフ、ツール、実行をグレーディング
- **Macro evals**: 多数の lower-level 結果を横断的に分析し、「どの種類の問題が繰り返されるか」「どこに集中しているか」「どの部分を最初に調査すべきか」を特定

## 4つのラベル体系

| ラベル | 意味 |
|--------|------|
| `case_type` | 生成されたビジネス状況（クリーン、検証ブロック、代替、価格例外など） |
| `run_outcome` | 実行結果（completed, awaiting review, blocked, failed） |
| `eval_finding` | 下位レベルのシグナル（例: `final_decision_quality`, `policy_compliance_correctness`） |
| `behavior_pattern` | クラスタリングで発見された集団レベルの反復パターン |

`case_type` → `run_outcome` → `eval_finding` → `behavior_pattern` のラベルチェーン。

## シミュレーションシステム

合成 EV 注文・構成後ワークフロー。以下の制約を含む:
- コンポーネント可用性とサプライヤー代替
- 工場キャパシティと生産スケジューリング
- 価格例外、プロモーション、インセンティブ
- 関税と日付付き市場シグナル
- 地域コンプライアンス
- エスカレーション・レビュー閾値

Orchestrator → 専門エージェント（validation, supply risk, procurement, capacity, factory routing, pricing, compliance, customer communications, release review）。OpenAI Agents SDK 上に構築。

## Lower-Level Evals (Promptfoo)

5つのルーブリック:
1. `final_decision_quality` — 最終判断が問題と終端状態に合致
2. `policy_compliance_correctness` — 価格/関税/インセンティブ/地域制約を遵守
3. `routing_specialist_activation` — 適切な専門家が起動
4. `market_drift_awareness` — 変化する市場状況を認識
5. `review_appropriateness` — レビュー/エスカレーションがリスクに比例

各ルーブリックはトレースごとに pass/fail。失敗したルーブリックが `eval_finding` となる。

1000件の合成注文のデータセット:
- ~992 bundle-backed traces（完全な証跡パケット）
- 典型的なバンドル: ~170イベント, ~15ハンドオフ, ~15ツール/関数呼び出し, ~8エージェント, ~4環境シグナル
- Promptfoo失敗は `final_decision_quality` に集中、次いで policy と review

## 分析データセットの構築

2つのテーブルに正規化:
- `traces_df`: 実行ごと1行（メタデータ、結果、所見、ドキュメント）
- `events_df`: 正規化イベントごと1行（ハンドオフ、ツール呼び出し、ステータス、レスポンス、レビューマーカー）

**Trace documents**: クラスタリングに渡される圧縮・比較可能なテキスト。以下を保持:
- ビジネスセットアップ（`case_type`, route, 環境シグナル）
- 実行結果と重大度
- キーハンドオフと専門家起動
- レビュー/所見マーカー
- 状態遷移ダイジェスト

**Impact score**: `severity_weight * (1 + findings_count) * (1 + loop_count/4)`

## BERTopic スタイルの発見

失敗・レビュー・Promptfoo シグナルがあるトレースのみを対象。

モジュラーパイプライン:
1. **Embed**: 各トレースドキュメント → ベクトル e_i
2. **Reduce**: UMAP で次元削減 → z_i
3. **Cluster**: HDBSCAN で密度ベースクラスタリング（外れ値はノイズ）
4. **Label**: tf × idf 的スコアで各クラスタに特徴的用語を割り当て

```
score(t, k) = tf(t, k) × log((1 + N) / (1 + df(t)))
```

**優先順位付け指標**:
```
impact_score(k) = prevalence_share(k) × severity_weighted_prevalence(k)
```

高頻度かつ高重大度のトレースを集中させるパターンが高インパクト。

**出力**:
- **Topic leaderboard**: インパクト順パターンランキング
- **Trace scatter map**: 各点がトレースドキュメント、行動パターンで色付け
- **Lift heatmap**: 各 `case_type` 内のパターン集中度

## AgentTrace スタイルの診断

選択された行動パターンについて、軽量実行グラフ G = (V, E) を再構築。フォーカスイベント（アンカー）から後方ウォークし、上流容疑者をスコアリング:

```
suspect_score = 0.4·proximity + 0.3·frequency + 0.2·bridge + 0.1·role
```

- **Proximity**: フォーカスイベントへの近さ
- **Frequency**: 同じパターン内のサンプルトレースでの再発頻度
- **Bridge**: 実行グラフの部分を接続する度合い
- **Role**: エージェント/ツールの役割と所見の関連性

## 実践的次のステップ

AI エンジニアリングチーム向け:
- 最も明確な lower-level eval 失敗をリグレッションスイートに昇格
- ルーブリックの厳格さを較正するため自動グレードのサンプルをレビュー
- モデルバージョン・プロンプトバージョン・オーケストレーションモード別に行動パターンを追跡
- 最高インパクトパターンにビジネスオーナーを割り当て

ビジネスステークホルダー向け:
- 生成されたケースタイプが実際の運用リスクと一致するか判断
- 高インパクトパターンが重要な顧客・運用成果に対応するか確認

**中核的教訓**: エージェントレベルの評価は「どの局所的行動がリスキーか」を教え、マクロ評価は「そのリスクがシステム規模で何になるか」を教える。

## Contributors

Shikhar Kwatra, Will Thieme, Bradley Strauss — OpenAI × Slalom 共同制作
