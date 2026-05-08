---
title: "Infrastructure Noise in Agentic Coding Evals"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - evaluation
  - infrastructure
  - benchmarking
  - coding-agents
aliases:
  - infra noise evals
  - resource allocation variance
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_infrastructure-noise.md
  - https://www.anthropic.com/engineering/infrastructure-noise
related:
  - swe-bench
  - frontier-swe-benchmark
  - ai-resistant-evaluations
---

# Infrastructure Noise in Agentic Coding Evals

エージェント型コーディングベンチマークにおいて、**インフラ設定の差異だけでスコアが有意に変動する**現象の定量分析。リソース割り当て・時間制限・クラスタ状態といった「隠れた変数」が、モデル能力の測定を歪める。

## 核心的発見

> Terminal-Bench 2.0で、最もリソース制約の厳しい設定と無制限設定の間で **6ppの差**（p < 0.01）。

リーダーボードの上位差はしばしば2-3ppであり、インフラ設定の差異がそれを上回る。

## 実験設定

Terminal-Bench 2.0を6段階のリソース設定で実行:
- **1x**: タスク指定値 = 保証割り当て = ハード上限（厳格強制）
- **3x**: 3倍のヘッドルーム
- **Uncapped**: 完全無制限

同一モデル（Claude）、同一ハーネス、同一タスクセットで比較。

## 結果

| 設定 | インフラエラー率 | 成功率 | 有意性 |
|------|---------------|--------|--------|
| 1x（厳格） | 5.8% | baseline | — |
| 3x | 2.1% | noise内 (+1.5pp) | p=0.40 |
| Uncapped | 0.5% | **+6pp** | p<0.01 |

### 2つのフェーズ

**Phase 1 (1x〜3x)**: インフラ信頼性の改善
- 一時的なリソーススパイクによる誤OOM-Killを防止
- スコアはノイズ範囲内（p=0.40）→ 評価を「容易に」はしていない

**Phase 2 (3x〜無制限)**: 評価の性質変化
- インフラエラー1.6pp減に対し成功率4pp増
- 大規模依存関係の pull、高負荷サブプロセス、メモリ集約テストが可能に
- 制約の緩い設定は「効率的戦略」より「リソースを活用できる戦略」を有利にする

## SWE-bench での再現

227タスク×10サンプルでRAM 1x〜5x:
- 同方向の効果、規模は小さい（+1.54pp at 5x）
- SWE-benchタスクはリソース集約度が低いため

## 他の隠れた変数

- **時刻**: APIレイテンシがトラフィックパターンで変動 → 合格率も変動（未定量化）
- **並列度**: 同時実行数
- **Egress帯域幅**: ネットワーク速度
- **ハードウェアスペック**: CPU・ディスクI/O

> 「エージェント型評価は構造的にエンドツーエンドのシステムテストであり、システムのどのコンポーネントも交絡因子になり得る」

## 推奨事項

### 評価実行者向け
- 保証割り当てとハード上限の**両方**をタスクごとに指定（単一値ではない）
- 上限をfloorのノイズ範囲内に校正（Terminal-Bench 2.0なら3x推奨）
- 複数時刻・複数日での実行でノイズ平均化

### ベンチマーク消費者向け
- **3pp未満のリーダーボード差は懐疑的に**（構成未公開なら特に）
- 単純な二項信頼区間（1-2pp）＋インフラ交絡（〜6pp）= 実効的不確実性は表示以上

## See Also

- [[concepts/swe-bench]] — SWE-bench benchmark
- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
- [[concepts/ai-resistant-evaluations]] — AI-resistant evaluation design
- [[concepts/eval-awareness-browsecomp]] — Eval awareness and contamination
- [[swe-bench-agent-scaffolding]] — Agent scaffolding for SWE-bench
