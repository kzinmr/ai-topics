---
title: "AI-Resistant Technical Evaluations"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - evaluation
  - company
  - agent-safety
  - benchmark
aliases:
  - AI-resistant take-home tests
  - AI-proof evaluations
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_AI-resistant-technical-evaluations.md
  - https://www.anthropic.com/engineering/AI-resistant-technical-evaluations
related:
  - eval-awareness-browsecomp
  - swe-bench
  - frontier-swe-benchmark
---

# AI-Resistant Technical Evaluations

Tristan Hume（Anthropic Performance Optimizationチームリード）による、AIに打ち負かされない技術評価（採用テスト）の設計論。Claudeモデルの進化に伴い3回の再設計を経た実践的知見。

## 問題

> 今日人間のスキルレベルを識別できるtake-homeテストが、明日にはモデルに簡単に解かれて評価手段として無価値になる。

### Claudeモデルによる撃破の歴史

| バージョン | 期間 | 敗因 |
|-----------|------|------|
| v1 (2024年初) | 約1.5年 | Claude 3.7 Sonnet: 候補者の50%以上がClaude Codeに委任した方が良いレベルに |
| v1限界突破 | 2025年5月 | Claude Opus 4: 4時間制限内でほぼ全ての人間より最適化された解答 |
| v2 | 数ヶ月 | Claude Opus 4.5: 2時間で最高の人間パフォーマンスに匹敵（その人間もClaude 4をヘビーに使用） |

## オリジナルテスト設計

### 課題
Pythonシミュレータ上の疑似アクセラレータ（TPU風）でコード最適化:
- 手動管理スクラッチパッドメモリ
- VLIW（複数実行ユニットの並列動作）
- SIMD（ベクトル演算）
- マルチコア

### 設計原則
1. **実務の代表性**: 実際の仕事を味わえる問題
2. **高シグナル**: 単一洞察に依存せず、幅広い能力発揮の機会
3. **専門知識不要**: 良い基礎力があれば学習可能
4. **楽しさ**: 高速開発ループ、奥深さ、創造性の余地
5. **AI支援許容**: 長期的な問題はAIが完全解決しにくい

### 結果
- 1,000人以上の候補者が受験、数十名を採用
- Claw 3 Opus以降の全モデル出荷、Trainiumクラスタ立ち上げに貢献
- 経験不足でも高い素養を示した学部卒新卒を発掘

## v3: 奇抜な方向へ

### Attempt 1（失敗）: データ転置問題
- Claude Opus 4.5が「計算全体を転置する」という想定外の最適化を発見
- ultrathinkで完全解決 → 訓練データに豊富な銀行競合問題はAI有利

### Attempt 2（成功）: Zachtronics風パズル
- 極度に制約された命令セット（Shenzhen I/O風）
- 最小命令数での最適解を競う
- 可視化・デバッグツールなし → ツール構築力も評価対象
- 「リアリズムより新奇性」への移行

> "The original worked because it resembled real work. The replacement works because it simulates novel work."

## 公開チャレンジ

オリジナルテストが無制限時間で公開中:
- Claude Opus 4.5: 1,487サイクル（11.5時間ハーネス）
- これを下回れば `performance-recruiting@anthropic.com` に連絡を

## 洞察

- リアリズムは贅沢品になった
- 人間の優位性は「十分長い時間軸」でのみ残る
- AIの広範な訓練データに対しては「分布外」の問題設計が鍵
- 評価の敵対的性質: モデルが賢くなるほどテストは短命に

## See Also

- [[concepts/eval-awareness-browsecomp]] — Eval awareness and benchmark contamination
- [[concepts/swe-bench]] — SWE-bench benchmark
- [[concepts/frontier-swe-benchmark]] — Frontier SWE benchmark
- [[concepts/infrastructure-noise-agent-evals]] — Infrastructure noise in agent evals
