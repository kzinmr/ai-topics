# Agent Team / Swarm

**Agent Team (Swarm)** は、単一のAI Agentがタスクを遂行するのではなく、複数のAgentが協調・分担して複雑なワークフローを自律的に実行するアーキテクチャパターン。

従来の **Harness Engineering**（1つのAgent + ツール環境）を、複数のBrainとHandsにスケールアップしたもの。

## Taxonomy: Agent Team関連概念の整理

| 概念 | 提唱者/実装 | 焦点 | レベル |
|---|---|---|---|
| **Agentic Engineering** | Simon Willison他 | AI Agentを活用したソフトウェア開発手法全般 | レベル1: 個人開発者のワークフロー |
| **Harness Engineering** | Anthropic, Ryan Lopopolo | Agentの実行環境・ツール統合・ガードレール | レベル2: 単一Agentのインフラ |
| **Managed Agents** | Anthropic | AgentのBrain/Hands/Sessionを分離したプラットフォーム | レベル3: エンタープライズ基盤 |
| **Agent Team / Swarm** | OpenAI Symphony他 | 複数Agentの協調・オーケストレーション | レベル4: チームレベル自律化 |
| **Dark Factory** | Dan Shapiro, StrongDM | 人間がコードを一切書かず・レビューもしない完全自律 | レベル5: 完全自動化 |

## Dan Shapiroの「5レベル」モデル

Simon Willisonが紹介したDan Shapiroの分類:

1. **Level 1: Spicy Autocomplete** — GitHub Copilotの初期版、コード補完
2. **Level 2: Chat-assisted** — ChatGPTに聞いてコピペ
3. **Level 3: Agent-assisted** — Claude Code/Codexがタスクを実行
4. **Level 4: The Engineering Team** — 仕様と計画を立て、Agentが実装。人間はマネージャー役
5. **Level 5: Dark Factory** — Fanucの無人工場の如く、人間が不要な完全自律開発

StrongDMはこのLevel 5を実践し、Anthropic Managed AgentsとOpenAI SymphonyはLevel 4→5への架け橋となっている。

## 主要実装

### Anthropic Managed Agents
- **Brain（Claude + harness） / Hands（sandbox） / Session（event log）**を完全分離
- Multi-Agent Coordination（リサーチプレビュー）: Agentが他のAgentをspawn可能
- Self-Evaluation（リサーチプレビュー）: 成功基準を定義し自律的に評価・改善
- 詳細: [[anthropic-managed-agents]]

### OpenAI Symphony
- Linear等のタスクボードを監視し、Agentチームをspawnして実行
- SPEC.mdを提供 → 任意の言語で実装可能（参照実装はElixir）
- Coding Agentを「管理」するのではなく「仕事を管理」するパラダイム
- Ryan LopopoloがOpenAI Frontierで開発。3-5 PR/日 → 75 PR/週の実績
- 詳細: [[openai-symphony]], [[ryan-lopopolo]]

### StrongDM Attractor / Dark Factory
- 非インタラクティブ開発: 仕様 + シナリオ → Agentがコード作成 → テスト → 収束
- 人間はコードを一切見ない・レビューしない
- Digital Twin Universe: 依存サービスをAgentでクローン
- 詳細: [[dark-factory-software-factory]]

## 関連概念

- [[harness-engineering]] — 単一Agentの実行環境設計（基礎）
- [[multi-agent-autonomy-scale]] — 256Agentスケールの自律協調研究
- [[concepts/harness-engineering/agentic-engineering-patterns.md]] — Agentic Engineeringのパターン集
- [[ryan-lopopolo]] — Symphonyの作者、Harness Engineering提唱者
