---
title: "Contextual Retrieval"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - rag
  - retrieval
  - embeddings
  - search
  - anthropic
aliases:
  - Contextual Embeddings
  - Contextual BM25
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_contextual-retrieval.md
  - https://www.anthropic.com/engineering/contextual-retrieval
related:
  - rag-systems
  - retrieval-augmented-generation
  - context-engineering
---

# Contextual Retrieval

Contextual Retrieval（文脈検索）は、RAGシステムの検索精度を劇的に向上させる前処理手法。チャンクをembedding/BM25インデックス化する**前に**、各チャンクに文書全体の文脈を付加する。

**コアアイデア**: チャンク単体では失われる文脈（「どの会社の」「いつの」データか）を、Claudeを使って自動補完する。

## 手法

### 2つのサブ技術

1. **Contextual Embeddings**: チャンクに文脈を前置してからembedding化
2. **Contextual BM25**: 同じ文脈付きチャンクでBM25インデックスを作成

### 変換例

```
# Before
original_chunk = "The company's revenue grew by 3% over the previous quarter."

# After
contextualized_chunk = "This chunk is from an SEC filing on ACME corp's 
performance in Q2 2023; the previous quarter's revenue was $314 million. 
The company's revenue grew by 3% over the previous quarter."
```

### 文脈生成プロンプト

```xml
<document>{{WHOLE_DOCUMENT}}</document>
Here is the chunk we want to situate within the whole document
<chunk>{{CHUNK_CONTENT}}</chunk>
Please give a short succinct context to situate this chunk within the
overall document for the purposes of improving search retrieval of the chunk.
```

生成される文脈は通常50-100トークン。Claude 3 Haikuで処理。

## 性能改善

| 手法 | 検索失敗率削減 | Top-20失敗率 |
|------|--------------|-------------|
| Baseline (標準RAG) | — | 5.7% |
| Contextual Embeddingsのみ | **-35%** | 3.7% |
| Contextual Embeddings + Contextual BM25 | **-49%** | 2.9% |
| + Reranking (Cohere) | **-67%** | 1.9% |

- **全embeddingモデルで改善**（Gemini Text 004, Voyageが特に効果的）
- 複数ドメイン（コードベース、フィクション、arXiv論文、科学論文）で検証

## コスト

Prompt Cachingを活用した場合、**100万ドキュメントトークンあたり$1.02**の一度限りのコスト（800トークンチャンク、8kトークン文書、50トークン文脈指示、100トークン文脈/チャンクの仮定）。

## 実装上の考慮点

- **チャンク境界**: サイズ・境界・オーバーラップの選択が検索性能に影響
- **Embeddingモデル**: GeminiとVoyageが特に効果的
- **カスタム文脈化プロンプト**: ドメイン固有の用語集を含めるとさらに改善
- **チャンク数**: Top-20がTop-10/Top-5より効果的（ただし情報過多に注意）
- **Reranking**: レイテンシとコストのトレードオフあり

## 従来手法との比較

Anthropicは以下の既存手法も評価したが、Contextual Retrievalほどの効果はなかった：
- ドキュメント要約のチャンク付加 → 限定的な改善
- Hypothetical Document Embedding (HyDE)
- Summary-based indexing

## See Also

- [[rag-systems]] — RAG systems overview
- [[retrieval-augmented-generation]] — RAG fundamentals
- [[context-engineering]] — Context engineering for AI agents
- [[contextual-retrieval]] — (self)
