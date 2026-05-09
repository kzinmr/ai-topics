---
title: "OpenEnv (Agent Environments Standard)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [ai-agents, reinforcement-learning, sandbox, open-source, huggingface, agent-evaluation]
sources:
  - "[[raw/articles/2025-10-23_huggingface_openenv]]"
related:
  - "[[concepts/agent-environments]]"
  - "[[concepts/reinforcement-learning]]"
  - "[[concepts/grpo]]"
  - "[[entities/huggingface]]"
---

# OpenEnv (Agent Environments Standard)

Meta-PyTorch と Hugging Face が提携して立ち上げた、**オープンなエージェント環境（Agentic Environments）の標準規格とハブ**。

## 問題意識

LLMだけではエージェントタスクは実行できない。必要なのは:
- 適切なツールへのアクセス
- 安全なサンドボックス実行
- タスクの明確なセマンティクス

しかし、数百万のツールをモデルに直接露出するのは非現実的かつ危険。

## OpenEnvの解決策

**エージェント環境（Agentic Environment）**: タスクに必要なツール、API、認証情報、実行コンテキストだけを含む、安全で意味的に明確なサンドボックス。

```
OpenEnv Environment
├── ツール定義 (APIs, MCPs)
├── 認証情報
├── 実行コンテキスト (Docker, sandbox)
└── タスクセマンティクス
```

### コアAPI

```python
env.step(action)    # エージェントのアクションを実行 → 観測を返す
env.reset()         # 環境をリセット
env.close()         # クリーンアップ
```

### RFC

| RFC | 内容 |
|-----|------|
| RFC 001 | コアコンポーネント（Environment, Agent, Task）のアーキテクチャ |
| RFC 002 | 基本envインターフェース、パッケージング、分離、通信 |
| RFC 003 | MCPツールのカプセル化と分離境界 |

## ユースケース

| ユースケース | 説明 |
|-------------|------|
| **RL Post-Training** | TRL, TorchForge+Monarch, VeRLでエージェントを強化学習 |
| **環境作成** | 自作環境を共有、主要RLツールとの相互運用を保証 |
| **SOTA再現** | FAIRのCode World Modelなどの手法を再現 |
| **デプロイ** | 訓練と同じ環境で推論も実行（フルパイプライン） |

## 統合先

- **TorchForge** (Meta) — 新RLライブラリ
- **TRL** (Hugging Face)
- **verl** (Volcengine)
- **SkyRL**
- **Unsloth**

## エコシステム

Hugging Face上に [Environment Hub](https://huggingface.co/openenv) を開設:
- 開発者が環境をビルド・共有・探索
- Human Agentとして対話的にテスト可能
- モデルをタスク解決に使用可能
- 本格的なRL訓練の前に妥当性を高速に検証

## 参照

- [OpenEnv Blog — Hugging Face](https://huggingface.co/blog/openenv) (2025-10-23)
- [OpenEnv GitHub](https://github.com/meta-pytorch/OpenEnv)
- [OpenEnv Hub](https://huggingface.co/openenv)
