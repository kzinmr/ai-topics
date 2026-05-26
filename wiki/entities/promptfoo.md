---
title: "Promptfoo"
type: entity
created: 2026-05-25
updated: 2026-05-26
tags:
  - promptfoo
  - evaluation
  - agent-evaluation
  - tool
  - testing
  - security
  - open-source
sources:
  - https://www.promptfoo.dev/
  - https://www.promptfoo.dev/docs/intro/
  - https://github.com/promptfoo/promptfoo
  - https://www.promptfoo.dev/blog/promptfoo-joining-openai/
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
related:
  - macro-evals-for-agentic-systems
  - evals-for-ai-agents
  - evals-skills
---

# Promptfoo

**Promptfoo** is an open-source CLI and library for evaluating and red-teaming LLM applications. Founded by **Ian Webster** and **Michael D'Angelo** in 2024, it was acquired by OpenAI in 2026 and remains MIT-licensed. With 350K+ developers, 130K monthly active users, and adoption by 25%+ of the Fortune 500, it is the most widely used AI evaluation and security testing platform.

## 概要

Promptfooは、LLMアプリケーションの**評価（Evaluation）**と**レッドチーミング（Red Teaming）**を統合した、開発者向けのオープンソースツール。従来の「プロンプトエンジニアリングの試行錯誤」に代わり、**テスト駆動型LLM開発（Test-Driven LLM Development）**を実現する。

| 側面 | 詳細 |
|------|------|
| **製作者** | Ian Webster (typpo) & Michael D'Angelo |
| **言語** | TypeScript (96.7%), Python SDK |
| **ライセンス** | MIT |
| **GitHub Stars** | 19.6K |
| **Contributors** | 260 |
| **npm Weekly DL** | 302.7K |
| **初回リリース** | 2023-05-03 |
| **最新版** | v0.121.12 (2026-05-21) |
| **リリース数** | 410+ |
| **企業導入** | 156 of Fortune 500 |

## OpenAIによる買収

2026年、PromptfooはOpenAIに買収された。条件は非公開だが、**MITオープンソースは継続**され、全プロバイダー・全モデルをサポートし続けることが明言されている。

- **買収前規模**: 23名（エンジニアリング・GTM・オペレーション）
- **投資家**: Insight Partners (Ganesh Bell), a16z (Zane Lackey)
- **買収後の位置づけ**: OpenAIのモデル/インフラ層に統合され、セキュリティ・評価機能を強化
- **開発継続**: 単独製品としてもオープンソースとしても存続

## 主要機能

### 1. LLM評価（Evaluations）

YAMLベースの宣言的設定で、プロンプト・モデル・RAGパイプラインの自動評価を実行：

```yaml
prompts:
  - "Translate to French: {{input}}"
  - "You are a translator. Output: {{input}}"

providers:
  - openai:gpt-4o
  - anthropic:claude-sonnet-4

tests:
  - vars:
      input: "Hello world"
    assert:
      - type: contains
        value: "Bonjour"
```

- **マルチプロバイダー比較**: OpenAI, Anthropic, Azure, Google, AWS Bedrock, Ollama, HuggingFace, カスタムAPI
- **自動スコアリング**: ルーブリック定義によるPass/Fail判定
- **キャッシュ・並行処理**: 高速な実行エンジン
- **ライブリロード**: 開発中の即時フィードバック
- **Web UI**: マトリックスビューによる結果比較・共有

### 2. レッドチーミング（Red Teaming）

AIアプリケーションのセキュリティ脆弱性を自動スキャン：

- **プロンプトインジェクション**（直接的・間接的）
- **ジェイルブレイク**（ガードレール回避）
- **データ漏洩・PII漏洩**
- **ビジネスルール違反**
- **エージェントの安全でないツール使用**
- **有害コンテンツ生成**
- **50+の脆弱性タイプ**をカバー

```bash
npx promptfoo@latest redteam setup
```

カスタム攻撃ベクトルを自動生成し、CI/CDパイプラインで継続的にテスト。

### 3. CI/CD統合

- GitHub Actions, GitLab CI, Jenkins とのネイティブ統合
- **PR内でのセキュリティフィードバック**: コードスキャン結果をプルリクエストに直接表示
- **継続的モニタリング**: 本番環境でのセキュリティ監視

### 4. MCP（Model Context Protocol）対応

MCPサーバー・エージェントフレームワークとの統合をサポート。

## アーキテクチャ

```
┌──────────────────────────────────────┐
│          CLI / Library API            │
│   (npx promptfoo, Node.js, Python)   │
└────────┬─────────────────────────────┘
         │
┌────────▼─────────────────────────────┐
│        Evaluation Engine              │
│   Caching · Concurrency · Matrix     │
└──┬──────────┬───────────┬────────────┘
   ▼          ▼           ▼
┌──────┐ ┌──────────┐ ┌──────────┐
│Evals │ │Red Team  │ │Code Scan │
│Bench │ │Attack Gen│ │Static    │
└──────┘ └──────────┘ └──────────┘
         │
┌────────▼─────────────────────────────┐
│          Provider Layer               │
│ OpenAI · Anthropic · Azure · Google   │
│ Bedrock · Ollama · HF · Custom API    │
└──────────────────────────────────────┘
```

## OpenAI Macro Evals での使用

[[concepts/macro-evals-for-agentic-systems]] Cookbookでは、5つのlower-levelルーブリック（`final_decision_quality`, `policy_compliance_correctness`, `routing_specialist_activation`, `market_drift_awareness`, `review_appropriateness`）をPromptfooで実装し、1000件の合成トレースに対してpass/failを生成。これらのlower-levelシグナルがBERTopicスタイルのマクロ発見パイプラインへの入力となる。

## 競合・関連ツール

| ツール | 主な違い |
|--------|---------|
| **LangSmith** | LangChainエコシステム内の評価・トレーシング。より高レベルなオブザーバビリティ |
| **Weights & Biases** | ML実験管理が中心。プロンプト評価は二次的 |
| **DeepEval** | Pythonネイティブの評価フレームワーク。CI/CD統合に特化 |
| **Arize AI** | 本番環境モニタリングに特化。開発時評価はPromptfooがリード |
| **Custom evaluation scripts** | 手動実装より10倍高速なフィードバックループ |

## 製作者

**Ian Webster** (@typpo) — Promptfoo共同創業者兼CEO。元Google、元Twitterのエンジニアリングリーダー。

**Michael D'Angelo** — Promptfoo共同創業者。技術・製品リーダーシップを担当。

## コミュニティ

- **Web**: [promptfoo.dev](https://www.promptfoo.dev/)
- **GitHub**: [github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- **npm**: [npmjs.com/package/promptfoo](https://www.npmjs.com/package/promptfoo)
- **Discord**: Promptfoo Discordサーバー
- **ライセンス**: MIT

## See Also

- [[concepts/macro-evals-for-agentic-systems]]
- [[concepts/evals-for-ai-agents]]
- [[comparisons/evals-skills]]
