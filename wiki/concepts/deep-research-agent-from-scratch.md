---
title: "Deep Research Agent from Scratch"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - deep-research
  - ai-agents
  - planning-agent
  - agent-loop
  - architecture
  - research-agent
aliases: [build-your-own-deep-research-agent, deep-research-from-scratch, research-agent-pipeline]
sources:
  - raw/articles/2026-03-28_youtube_deep-research-agent-workshop.md
  - raw/articles/2026-03-28_github_deep-research-agent-readme.md
---

# Deep Research Agent from Scratch

**深層リサーチエージェントをゼロから構築する10ステップのパイプライン**。Ivan Leo（Google DeepMind, ex-Manus）と Hugo Bowne-Anderson による2026年3月のワークショップで体系化。生の Gemini API 呼び出しから始まり、明確化質問 → リサーチプラン生成 → 動的サブエージェント並列起動（Exa検索）→ 引用付きレポート合成までを一気通貫で構築する。

## The 10-Step Build Pipeline

```
Step 1: Raw API Call      → Gemini function call を観察するだけ
Step 2: Single Tool        → read_file を実際に実行、結果を返す
Step 3: Tool Runtime       → Tool データクラス + AgentRuntime（名前でディスパッチ）
Step 4: State & Context    → RunConfig, RunState, AgentContext の分離
Step 5: Hooks              → .on() イベントシステムでレンダリングを分離
Step 6: Agent Loop         → run_until_idle() — モデルがツール呼び出しを止めるまでループ
Step 7: Subagents          → 子 Agent インスタンスを並列生成、Exa 検索を委譲
Step 8: Beautiful Outputs  → フック経由でリッチレンダリング（diff, syntax highlight）
Step 9: Plan Generation    → plan/execute モード切替 + generate_plan ツール
Step 10: OpenTelemetry     → Logfire でフルトレース可視化
```

## Core Architecture

### Phase Swapping: Plan → Execute

このアーキテクチャの核心は **モード切替（phase swapping）** にある：

```python
class RunState:
    mode: Literal["plan", "execute"] = "plan"
    todos: list[Todo] = []
```

**Plan モード**:
- 利用可能なツールは `generate_plan` のみ
- ユーザーの曖昧な質問に対して、エージェントが**明確化質問**を生成
- 回答を受けてリサーチプラン（Todo リスト）を作成
- プランが完了したら `mode = "execute"` に切り替え

**Execute モード**:
- 全ツール（read, write, search, bash）が利用可能に
- Todo リストに沿ってサブエージェントを並列起動
- 各サブエージェントが Exa で Web 検索を実行
- 結果を合成して引用付きレポートを生成

> *"Phase swapping is how the agent moves from planning to execution — it's not two separate agents, it's one agent with two modes."*

### Deterministic Guardrails（決定論的ガードレール）

エージェントが Todo を完了せずに終了するのを防ぐ：

```python
def run_until_idle(self) -> str:
    while True:
        response = self._run_one_turn()
        if response.is_text:
            if self.state.is_incomplete():
                # Nudge: "You have unfinished todos. Complete them before responding."
                self.contents.append(nudge_message)
                continue  # Force another turn
            return response.text
```

- `state.is_incomplete()` は未完了の Todo をチェック
- 未完了があればヌッジメッセージを注入し、強制的に次のターンへ
- **モデルが「終わった」と言っても、ハーネスが許さない**

### Dynamic Subagent Spawning（動的サブエージェント生成）

```python
class Agent:
    def spawn_subagent(self, prompt: str, tools: list[str]) -> Agent:
        child = Agent(
            config=RunConfig(model=self.config.model, max_iterations=5),
            state=RunState(todos=[], mode="execute"),
            tools=[t for t in self.tools if t.name in tools],
        )
        return child
```

- 親エージェントが必要に応じて**任意の数**の子エージェントを生成
- 各子エージェントは独立した RunState, イテレーション予算, ツールセットを持つ
- 検索クエリは `asyncio.gather()` で並列実行
- Exa API を使った Web 検索を各サブエージェントが担当

## Design Decisions & Trade-offs

### Build Your Own vs. Provider SDKs

ワークショップで Ivan Leo が語った重要な洞察 — Manus が独自ランタイムを構築せざるを得なかった理由：

| Aspect | Provider SDK (e.g. Claude Agent SDK) | Build Your Own |
|--------|--------------------------------------|----------------|
| 学習曲線 | 低い | 高い |
| 制御粒度 | SDK の抽象化に依存 | **完全な制御** |
| デバッグ | ブラックボックス化しやすい | 全レイヤーが可視 |
| プロダクション | SDK の更新に依存 | 自己管理 |
| Manus の選択 | ❌ | ✅ 5回の再アーキテクチャを経て到達 |

> *"Manus had no choice but to build their own runtime. When you're shipping to millions of users, you need control over every layer — retry logic, error handling, context management. Provider SDKs abstract too much away."* — Ivan Leo

### Why Tool Calling Beats Parsing Text Output

- テキスト出力のパースは壊れやすい（JSON の微細なフォーマット違いで破綻）
- Function calling は**型契約**を強制する — モデルが呼び出す関数の引数スキーマが事前定義されている
- 不正な引数や未知のツール呼び出しに対する防御的コードが書きやすい

### Start With the Best Model, Then Optimize Down

- まず Gemini 2.5 Pro（最高性能）でタスクが**実際に達成可能か**を確認
- 達成可能なら、Flash やより安価なモデルにダウングレードして最適化
- コスト最適化は**検証後** — 最初から安いモデルで始めて「できない」と諦めるのが最悪のパターン

## Key Design Patterns

### 1. State Separation（状態の分離）

```python
@dataclass
class RunConfig:       # 不変の設定
    model: str
    max_iterations: int
    user_confirmation: bool

@dataclass  
class RunState:        # 可変の実行状態
    iteration: int = 0
    mode: str = "plan"
    todos: list[Todo] = field(default_factory=list)

@dataclass
class AgentContext:    # 外部依存の注入
    api_keys: dict
    working_dir: Path
```

**Config（不変）/ State（可変）/ Context（外部依存）の明確な分離**により、テスト容易性とサブエージェントの独立起動が可能になる。

### 2. Todo-Driven Execution

エージェントは自分自身の Todo リストを管理する：

```
User: "Research the impact of AI on software engineering"
  → Plan mode: Agent generates clarifying questions
  → User answers
  → Agent creates Todo list:
      1. [pending] Search: AI coding assistant adoption rates
      2. [pending] Search: developer productivity studies
      3. [pending] Search: job market impact of AI tools
      4. [pending] Synthesize findings into report
  → Execute mode: Spawns 3 subagents (parallel), then synthesizes
```

### 3. Hooks for Lifecycle Events

コアループからレンダリングを分離（[[concepts/agents-that-build-themselves]] と同じパターン）：

```python
agent.on("message", lambda msg: print(f"[{msg.role}]: {msg.content}"))
agent.on("llm_tool_call", lambda call: print(f"🔧 Calling {call.name}..."))
agent.on("tool_result", lambda result: print(f"✅ {result.name} done"))
```

### 4. Don't Break Your Cache

Ivan Leo のプロダクション教訓：

- ツールの `description` フィールドを変更すると、モデルのツール選択パターンが壊れる
- キャッシュされた function calling スキーマが無効化される
- プロダクションではツール定義の**後方互換性**が重要

## When Deep Research Makes Sense

| ✅ 適している | ❌ 適していない |
|---|---|
| 複数ソースの横断検索が必要 | 単一の事実確認 |
| 探索中に検索パスが変化する | 既知の情報の要約 |
| 競合分析、技術調査、文献レビュー | 定型的な情報取得 |
| 矛盾する情報源の統合が必要 | 計算や変換 |

> *"Deep research is not the right tool for everything. Sometimes a single web search is faster and better. Know when to use what."* — Hugo Bowne-Anderson

## Production Observability (Step 10)

OpenTelemetry + Logfire によるフルトレース：

```
┌─ Turn Span (per agent run) ──────────────────────┐
│  model: gemini-2.5-pro                            │
│  tokens: 4,200 input / 850 output                 │
│  ├─ tool_call span: search_exa("AI adoption...")  │
│  │  └─ tool_executed span: 5 results, 1.2s        │
│  ├─ tool_call span: search_exa("developer...")    │
│  │  └─ tool_executed span: 3 results, 0.9s        │
│  └─ subagent span: delegated_search               │
│     └─ (child agent's own turn spans)             │
└──────────────────────────────────────────────────┘
```

[Logfire公開トレース](https://logfire-us.pydantic.dev/public-trace/eb9a4dec-edd0-439e-941e-0ce43dcc8c48?spanId=47d016809c9b61f0)

## Sample Output

Step 10 エージェントの出力例 → [`airpods_report.md`](https://github.com/hugobowne/build-your-own-deep-research-agent/blob/main/airpods_report.md) — 調査クエリに対して構造化された引用付きレポートを生成。

## Related Concepts

- [[concepts/agents-that-build-themselves]] — 同じ Hugo + Ivan Leo の前回ワークショップ。ツールファクトリー・ホットリロード・フック
- [[concepts/subagents]] — サブエージェント並列委譲パターン
- [[concepts/research-agent-fundamentals]] — Anthropic Claude Agent SDK の research agent
- [[concepts/agentic-loop]] — エージェントループの基本
- [[concepts/pi-autoresearch]] — Pi の autoresearch 機能
- [[concepts/karpathy-rl-agents-agentic-research-loop]] — Karpathy の RL エージェント + リサーチループ

## References

- [Build Your Own Deep Research Agent (YouTube, 89min)](https://www.youtube.com/watch?v=LUfqQgz1-Os) — Full live build session
- [GitHub: build-your-own-deep-research-agent](https://github.com/hugobowne/build-your-own-deep-research-agent) — 10-step companion code
- [[entities/hugo-bowne-anderson]] — Host, Vanishing Gradients
- [[entities/ivan-leo]] — Co-host, Google DeepMind (ex-Manus)
