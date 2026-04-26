---
title: "Claude 4.7 Tokenizer Change"
type: concept
created: 2026-04-20
updated: 2026-04-20
tags: [concept, anthropic, claude, tokenizer, cost-analysis]
related: [context-window-management, context-compaction, claude-opus]
sources: []
---

# Claude 4.7 Tokenizer Change

2026年4月16日にClaude Opus 4.7がリリースされ、**初めてトークナイザーが変更**された。この変更により、同じ入力テキストが40%多いトークンにマッピングされる。

## 主要な変更点

### トークン乗数（Opus 4.6 → 4.7）

| コンテンツタイプ | 乗数 |
|----------------|------|
| システムプロンプト（生テキスト） | **1.46x** |
| 高解像度画像（3456×2234, 3.7MB） | **3.01x** |
| 小画像（682×318） | ~1.01x（無視できる） |
| テキストheavyPDF（15MB, 30ページ） | 1.08x |

### テスト結果詳細

**システムプロンプト:**
- Opus 4.7: 7,335トークン
- Opus 4.6: 5,039トークン
- 乗数: 1.46x

**大容量画像（3456×2234, 3.7MB PNG）:**
- Opus 4.7: 4,744トークン
- Opus 4.6: 1,578トークン
- 乗数: 3.01x

**PDFテスト（15MB, 30ページ）:**
- Opus 4.7: 60,934トークン
- Opus 4.6: 56,482トークン
- 乗数: 1.08x

## 料金への影響

Opus 4.7はOpus 4.6と同様の料金を維持：

| トークンタイプ | 100万トークンあたりの料金 |
|---------------|-------------------------|
| 入力 | $5.00 |
| 出力 | $25.00 |

**結果**: 典型的なテキストコンテンツで**約40%のコスト増**。

## 高解像度画像対応の改善

> "Opus 4.7はより高解像度画像への対応が向上：長い辺的最大2,576ピクセル（约3.75メガピクセル）をサポートし、これまでのClaudeモデルの3倍以上"

大容量画像の3倍トークン増加は**すべてより高解像度サポートのため**であり、非効率性ではない。

## 意味

1. **テキストheavyコンテンツ**: Opus 4.7で~1.1-1.5xのトークン増加を見込む
2. **高解像度画像**: 3xトークン増加だが、より大きな画像を入力可能に
3. **コスト影響**: 典型的なテキスト使用で~40%高コスト
4. **小画像**: バージョン間で大きな差なし

## 関連項目

- [Context Window Management](../context-window-management.md)
- [Context Compaction](../context-compaction.md)
- [Claude Opus](../entities/claude-opus.md)

## See Also

- [[concepts/_index]]
- [[concepts/claude-memory-tool]]
- [[concepts/claude-code-source-patterns]]
- [[concepts/claude-mythos-preview]]
- [[concepts/claude-code-leak]]
