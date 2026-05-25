---
title: "Macro Evals for Agentic Systems"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - agent-evaluation
  - evaluation
  - trace-analysis
  - bertopic
  - clustering
  - promptfoo
  - observability
  - multi-agent
  - methodology
sources:
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
  - https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
related:
  - evals-for-ai-agents
  - infrastructure-noise-agent-evals
  - harness-engineering
  - ai-resistant-evaluations
status: active
---

# Macro Evals for Agentic Systems

マルチエージェントシステムの評価において、**個別トレースの低レベル評価（lower-level evals）から集団レベルの行動パターン（macro evals）を発見する**方法論。OpenAI × Slalom の共同 Cookbook として公開。

> エージェントレベルの評価は「どの局所的行動がリスキーか」を教え、マクロ評価は「そのリスクがシステム規模で何になるか」を教える。

## 2層アーキテクチャ

```
Lower-level evals（エージェント単位）
  ├─ 個別エージェント・ハンドオフ・ツール・実行をグレーディング
  └─ Promptfoo 等の eval ツールが pass/fail を生成
         ↓
Macro evals（集団横断）
  ├─ 多数の lower-level 所見を横断的に分析
  ├─ 反復パターンを発見（BERTopic スタイルのクラスタリング）
  ├─ インパクトスコアで優先順位付け
  └─ 上流原因を診断（AgentTrace スタイルの実行グラフ分析）
```

マルチエージェントシステムでは、最終回答は長いワークフローの最後のイベントに過ぎない。一見妥当に見えるリリース推奨も、トレースを見れば価格エージェントがインセンティブを無視していたり、供給エージェントが在庫切れを見逃していたり、Orchestrator が必要なレビューステップを迂回していたりする可能性がある。

## 4ラベルチェーン

個別トレースから集団パターンまでを結ぶラベル体系：

| ラベル | スコープ | 意味 |
|--------|----------|------|
| `case_type` | 入力 | 生成されたビジネス状況（clean, validation block, supplier substitution, pricing exception, ...） |
| `run_outcome` | 出力 | 実行結果（completed, awaiting review, blocked, failed） |
| `eval_finding` | 局所 | 下位レベル評価のシグナル（`final_decision_quality`, `policy_compliance_correctness`, ...） |
| `behavior_pattern` | 集団 | クラスタリングで発見された反復パターン |

> `case_type` はセットアップ、`run_outcome` は結末、`eval_finding` は局所症状、`behavior_pattern` は集団パターン。

## Lower-Level Evals: Promptfoo による 5 ルーブリック

| ルーブリック | 評価内容 |
|-------------|---------|
| `final_decision_quality` | 最終判断が特定された問題と終端状態に合致しているか |
| `policy_compliance_correctness` | 価格/関税/インセンティブ/地域制約が遵守されているか |
| `routing_specialist_activation` | ケースに対して適切な専門エージェントが起動されたか |
| `market_drift_awareness` | 変化する市場状況（関税、供給変動）を認識しているか |
| `review_appropriateness` | レビュー/エスカレーションがリスクに比例しているか |

各ルーブリックはトレースごとに pass/fail。失敗したルーブリックが `eval_finding` になる。

1000 件の合成データセットでは、典型的トレースは ~170 イベント、~15 ハンドオフ、~15 ツール呼び出し、~8 エージェント、~4 環境シグナルを含む。Promptfoo 失敗は `final_decision_quality` に集中。

## 分析データセットの構築

2 テーブルに正規化：

| テーブル | 粒度 | 内容 |
|---------|------|------|
| `traces_df` | 実行単位（1行/run） | メタデータ、結果、所見、trace document |
| `events_df` | イベント単位（1行/event） | ハンドオフ、ツール呼び出し、ステータス、レスポンス、レビューマーカー |

**Trace document**: クラスタリングに渡される圧縮テキスト。ビジネスセットアップ・実行結果・キーハンドオフ・所見マーカー・状態遷移ダイジェストを保持。

**インパクトスコア**（優先順位付け用）:
```
impact_score = severity_weight × (1 + findings_count) × (1 + loop_count / 4)
```

重大度マッピング：
| Outcome Group | Severity | Weight |
|--------------|----------|--------|
| successful_completion | low | 1.0 |
| review_escalation | medium | 2.0 |
| in_progress | medium | 1.5 |
| blocked | high | 2.5 |
| hard_failure | high | 3.0 |

## BERTopic スタイルのマクロ発見パイプライン

失敗・レビュー・Promptfoo シグナルがあるトレースのみを対象に、モジュラーパイプラインで実行：

```
Embed（ベクトル化）→ Reduce（UMAP次元削減）→ Cluster（HDBSCAN）→ Label（特徴的用語抽出）
```

**用語スコア**（クラスタ k における用語 t の特徴度）:
```
score(t, k) = tf(t, k) × log((1 + N) / (1 + df(t)))
```

**パターン優先順位付け**:
```
impact_score(k) = prevalence_share(k) × severity_weighted_prevalence(k)
```

高頻度かつ高重大度のトレースが集中するパターンが高インパクト。これは普遍的なリスク式ではなく、実用的なトリアージスコアである。

**3つの出力ビュー**:
1. **Topic leaderboard**: インパクト順のパターンランキング
2. **Trace scatter map**: UMAP 次元削減空間上の各トレースを行動パターンで色付け
3. **Lift heatmap**: 各 `case_type` における行動パターンの集中度（どのシナリオがどのパターンを引き起こすか）

## AgentTrace スタイルの根本原因診断

発見が「何が繰り返されるか」を教えるのに対し、診断は「どこを最初に調査すべきか」を問う。

選択された行動パターンについて、実行グラフ `G = (V, E)` を再構築。フォーカスイベント（アンカー）から後方ウォークし、上流容疑者を重み付きスコアリング：

```
suspect_score = 0.4·proximity + 0.3·frequency + 0.2·bridge + 0.1·role
```

| 要素 | 重み | 意味 |
|------|------|------|
| Proximity | 0.4 | フォーカスイベントへの近さ |
| Frequency | 0.3 | 同じ行動パターン内のサンプルトレースでの再発頻度 |
| Bridge | 0.2 | 実行グラフの部分間を接続する度合い |
| Role | 0.1 | エージェント/ツールの役割と所見の関連性 |

> これは因果関係の証明ではなく、「このパターンが重要」から「これらのエージェント、ツール、ハンドオフ、レビューポリシーを最初に調査せよ」への変換である。

## シミュレーション: EV 注文ワークフロー

OpenAI Agents SDK 上に構築された合成 EV 注文・構成後ワークフロー。実世界の制約を反映：

- コンポーネント可用性とサプライヤー代替
- 工場キャパシティと生産スケジューリング
- 価格例外・プロモーション・インセンティブ
- 関税と日付付き市場シグナル
- 地域コンプライアンス制約
- エスカレーション・レビュー閾値

Orchestrator → validation, supply risk, procurement, capacity, factory routing, pricing, compliance, customer communications, release review の専門エージェント群。ハンドオフ・関数ツール・ガードレール・構造化出力・トレースにより完全な証跡パケットを保持。

## 実践的適用ステップ

**AI エンジニアリングチーム向け**:
1. 最も明確な lower-level eval 失敗をリグレッションスイートに昇格
2. ルーブリック厳格さを較正するため自動グレードのサンプルをレビュー
3. モデルバージョン・プロンプトバージョン・オーケストレーションモード別に行動パターンを追跡
4. 最高インパクトパターンにビジネスオーナーを割り当て
5. 上位容疑者（エージェント・ツール・ハンドオフ）を調査してからシステム変更

**ビジネスステークホルダー向け**:
- 生成されたケースタイプが実際の運用リスクと一致するか判断
- 高インパクトパターンが重要な顧客・運用成果に対応するか確認
- レビュー閾値が意図したビジネス行動を生み出しているか検証
- Sankey・ヒートマップビューでポリシー・プロセス設計の優先順位付け

## 他の評価アプローチとの関係

| アプローチ | スコープ | 関係 |
|-----------|---------|------|
| [[evals-for-ai-agents]]（Anthropic） | エージェント評価の基本構造・落とし穴・採点手法 | 基礎。Macro evals はこの上に構築される集団層 |
| [[infrastructure-noise-agent-evals]] | インフラノイズがエージェント評価に与える影響 | 評価インフラの信頼性に関する補完的視点 |
| [[ai-resistant-evaluations]] | 評価自体の堅牢性設計 | 下位レベルの eval 設計原則 |
| [[comparisons/evals-skills]] | コーディングエージェント向け評価スキル | MCP + スキルによる評価自動化の異なるアプローチ |
| [[concepts/harness-engineering]] | OpenAI の AI 支援開発手法 | トレースを活用した自己検証の着想源 |

## ツールスタック

| ツール | 役割 |
|--------|------|
| **[[promptfoo]]** | エージェントレベルの lower-level eval（ルーブリック評価） |
| **OpenAI Agents SDK** | マルチエージェントシステム構築（ハンドオフ、ガードレール、構造化出力、トレース） |
| **BERTopic**（BERTopic ファミリー） | UMAP + HDBSCAN + c-TF-IDF によるトピックモデリング |
| **AgentTrace** | 実行グラフ後方ウォークによる根本原因診断 |
| **Plotly / Sankey** | ラベルチェーンの可視化、ヒートマップ、散布図 |

## 参考文献

- [Macro Evals for Agentic Systems — OpenAI Cookbook](https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems) — Shikhar Kwatra, Will Thieme, Bradley Strauss (OpenAI × Slalom)
- [BERTopic Documentation](https://maartengr.github.io/BERTopic/)
- [Promptfoo: OpenAI Agents Provider](https://www.promptfoo.dev/docs/providers/openai-agents/)
- [AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems](https://arxiv.org/abs/2505.12345)
