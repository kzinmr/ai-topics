---
title: "Prism-Reranker: 関連性スコアリングを超えたエージェント検索"
created: 2026-04-28
updated: 2026-04-28
type: summary
tags: [rag, ai-agents, inference, benchmark, tool]
sources: [raw/articles/prism-reranker-agentic-retrieval-2026-04-28.md]
---

# Prism-Reranker: Beyond Relevance Scoring

## 概要
Inflection by Gradientが提案した、エージェント向け検索のための再ランクモデル。従来のスカラー関連性スコアだけでなく、文書の貢献要約とノイズ除去済みエビデンスパスを単一のフォワードパスで同時出力する。

## 主要イノベーション
- **3つの同時出力**: 関連性スコア + 貢献ステートメント + エビデンスパス
- **効率的判断**: 「no」の verdict の場合は即時停止、生成コストを Relevant な文書にのみ投入
- **ハイブリッド訓練**: ポイント蒸留 + SFT の組み合わせ損失
- **LLM-as-Judge**: 5モデルの多数決でラベル生成（DeepSeek-V3.2, Qwen3.5-397B, Gemini-3-Flash, Claude-Haiku-4.5, GPT-5.4-mini）

## 実験結果
- **BEIR-QA NDCG@10**: Prism-Reranker-4B-exp が 58.87%（既存モデルを+1.54改善）
- **エンティティ忠実度**: 全サイズで>0.968
- **圧縮率**: 中央値~0.5（最長・ノイズの多いWebページで最大の削減効果）
- **形式遵守率**: >0.995

## 実装詳細
- **バックボーン**: Qwen3.5（Causal LM）
- **コンテキスト長**: 最大10,240トークン
- **訓練ハードウェア**: 0.8B〜4Bモデルを単一RTX 4090（24GB）で訓練
- **CoTは不使用**: 研究によりCoTがスコアを二極化させ、ランキングのホリスティックパターンマッチングを阻害することが判明

## 今後の課題
- SFTのみのモデルでは短文からの幻覚が稀に発生
- RLによるエンティティレベルの幻覚ペナルティと簡潔性の報酬を提案中
