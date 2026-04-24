---
title: Gold Diff Distillation
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
- concept
- training
- distillation
- reinforcement-learning
- coding-agents
related:
- model-distillation
- trl-fine-tuning
- ai-coding-reliability
- evaluation-flywheel
sources: []
---

# Gold Diff Distillation

コーディング製品企業が開発した新しいRLトレーニング手法。ユーザーの最終的な「望ましい状態」をRLターゲットとして利用する。

## Core Concept

従来のモデル蒸留（distillation）が教師モデルの出力を直接模倣するのに対し、Gold Diff Distillationは：

- **ユーザーの最終収束状態**を正解として扱う
- ユーザーが拒否・編集した中間出力をペナルティ対象とする
- 10回以上のAPIターンを経て到達した「真に有用な出力」を学習ターゲットにする

## Mechanism

```
User Request → Model Output v1 → User Edit/Reject → Model Output v2 → ... → Final Accepted State
                                                                        ↑
                                                        これが「Gold Diff」（正解差分）
```

### RLターゲット設定
- **報酬**: ユーザーが最終的に受け入れた出力に近い生成
- **ペナルティ**: �ーザーが拒否・編集した中間出力パターン
- **利点**: 人間の実際の選好を直接反映できる

## Strategic Implications

### Distillationの阻止可能性
Dwarkesh Patelの分析によれば：
1. **Chain-of-Thought隠蔽は失敗する**: モデルはプロンプトで思考を省略・外部化可能
2. **RLVRでCoT再構築可能**: 隠してもトレーニングターゲットとして再構築できる
3. **真のモータはツール使用**: ローカル実行されるコード・bashツール使用は隠蔽困難

### Gold Diffの優位性
蒸留されたモデルは元のAPIモデルを**上回る可能性**がある：
- ユーザーの実際のワークフローから学習
- 中間試行錯誤の「負のサンプル」も活用
- 製品利用データという独占的データソース

## Economic Context

- Frontierモデル蒸留コスト: ~$25M（1T tokens @ Opus 4.6の$25/MTok）
- コーディング製品企業はこのコストを正当化できるROIを持つ
- ユーザー行動データという他社が入手できない「モータ」を保有

## Sources

- [Dwarkesh Patel: What I learned this week](https://www.dwarkesh.com/p/what-i-learned-april-15)
- AI Index Report 2026（コーディングエージェント採用データ）

## See Also

- [[concepts/_index.md]]
- [[concepts/local-llm/model-distillation.md]]
