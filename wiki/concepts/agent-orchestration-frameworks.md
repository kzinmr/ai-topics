---
title: "Agent Orchestration Frameworks"
type: concept
aliases:
  - agent-orchestration-frameworks
  - AI-agent-frameworks
  - multi-agent-frameworks
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - agent
  - orchestration
  - framework
status: complete
sources:
  - url: "https://www.developersdigest.tech/guides/ai-agent-frameworks-compared"
    title: "AI Agent Frameworks Compared 2026 (Developers Digest)"
  - url: "https://arsum.com/blog/posts/agentic-ai-frameworks-comparison"
    title: "Agentic AI Frameworks Compared 2026 (Arsum)"
  - url: "https://www.guideflow.com/blog/best-ai-orchestration-platforms"
    title: "16 Best AI Orchestration Platforms for 2026 (Guideflow)"
---

# Agent Orchestration Frameworks

**Agent Orchestration Frameworks** は、複数の AI エージェントを協調させ、複雑なマルチステップワークフローを実行するためのソフトウェアフレームワーク群。2025〜2026年にかけて爆発的に増加し、200以上のフレームワーク・ツールが存在する。

## 主要フレームワーク比較（2026年）

### 汎用フレームワーク

| フレームワーク | 言語 | アーキテクチャ | 学習曲線 | GitHub Stars | ライセンス |
|--------------|------|---------------|---------|-------------|-----------|
| **LangChain** | Python, JS/TS | チェーン + ツール統合 | Medium | 90,000+ | MIT |
| **LangGraph** | Python, JS/TS | グラフベース状態機械 | High | — | MIT |
| **LlamaIndex** | Python | データ中心クエリエンジン | Low | — | MIT |
| **Pydantic AI** | Python | 型安全エージェント | Low | — | MIT |
| **DSPy** | Python | コンパイル型プロンプト最適化 | High | — | MIT |
| **Semantic Kernel** | C#, Python | プラグイン駆動 | Medium | — | MIT |

### マルチエージェント特化フレームワーク

| フレームワーク | 協調パターン | 特徴 |
|--------------|-------------|------|
| **AutoGen（Microsoft）** | 会話ベース GroupChat | 人間参加ループ、35,000+ stars |
| **CrewAI** | ロールベース階層/フラット | 低学習曲線、24,000+ stars |
| **MetaGPT** | ソフトウェア会社シミュレーション | 役割駆動（PM、エンジニア、QA） |
| **OpenAI Agents SDK** | ハンドオフ + ガードレール | 公式 SDK、シンプル |
| **Google ADK** | グラフ + 並列実行 | Google 公式、A2A 対応 |
| **CAMEL** | 役割プレイ会話 | 研究志向、探索的 |
| **OpenDevin** | コード生成特化 | SWE-bench 最適化 |

### 軽量フレームワーク

| フレームワーク | 特徴 |
|--------------|------|
| **Smolagents（HuggingFace）** | 数行でエージェント構築 |
| **Agno** | ミニマル API |
| **Upsonic** | 関数特化型 |
| **Portia AI** | プランニング + 実行 |

## フレームワーク選択の意思決定フレームワーク

```
1. どの程度の制御が必要か？
   ├─ 高い → LangChain / LangGraph
   ├─ 中程度 → AutoGen
   └─ 低い（スピード優先）→ CrewAI / LlamaIndex

2. ワークフローは対話型か？
   ├─ はい → AutoGen（会話）または CrewAI（階層）
   └─ いいえ → LangChain/LangGraph（カスタム制御）

3. チームの専門性は？
   ├─ ML 経験少 → CrewAI / AutoGen
   └─ 経験豊富 → LangChain / LangGraph
```

## 各フレームワークの哲学

| フレームワーク | 哲学 |
|--------------|------|
| **CrewAI** | エージェントは**チームメンバー** |
| **LangGraph** | エージェントは**グラフ内のノード** |
| **AutoGen** | エージェントは**会話の参加者** |
| **Claude Code** | エージェントは**あなたのペアプログラマ** |

## エコシステムの成熟度

- **LangChain**: 1,800+ インテグレーション（2026年初頭時点）
- **エンタープライズ導入**: 40% の企業アプリが AI エージェントを統合（Gartner, 2026）
- **カテゴリ分化**: エンタープライズ（IBM watsonx, UiPath）、開発者（LangChain, CrewAI）、ノーコード（Zapier, n8n）

## 関連概念

- [[concepts/agent-loop-orchestration]] — エージェントループの基本パターン
- [[concepts/agent-swarms]] — 創発的マルチエージェントシステム
- [[concepts/telegram-managed-bots]] — プラットフォーム型エージェント
- [[concepts/claude-code-best-practices]] — Claude Code のエージェントパターン

## ソース

- [AI Agent Frameworks Compared 2026 (Developers Digest)](https://www.developersdigest.tech/guides/ai-agent-frameworks-compared)
- [Agentic AI Frameworks Compared 2026 (Arsum)](https://arsum.com/blog/posts/agentic-ai-frameworks-comparison)
- [16 Best AI Orchestration Platforms for 2026 (Guideflow)](https://www.guideflow.com/blog/best-ai-orchestration-platforms)
