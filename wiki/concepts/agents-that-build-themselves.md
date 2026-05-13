---
title: "Agents That Build Themselves"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - self-improving
  - agent-harness
  - agent-architecture
  - coding-agents
  - harness-engineering
  - ai-agents
sources:
  - raw/articles/2026-02-28_substack_agents-that-build-themselves.md
  - raw/articles/2026-02-28_youtube_openclaw-from-scratch-workshop.md
aliases: [self-extending-agents, self-building-agents, self-writing-tools, software-building-software]
---

# Agents That Build Themselves

**自己拡張エージェント** — エージェントが自身のツールを書き、それをホットリロードし、実行時に能力を拡張していくパラダイム。Hugo Bowne-Anderson と Ivan Leo（ex-Manus, Google DeepMind）による2026年2月のワークショップで体系化された。

> *"ソフトウェアがソフトウェアを構築する。エージェントが自分のハーネスを改造する。"*

## Core Concept

従来のエージェント開発では、開発者がツールを定義し、エージェントはそれを使うだけだった。**Agents That Build Themselves** はこれを逆転させる：

```
User: "I need a tool that generates files with Notion-style timestamps"
  → Agent reads agent_tools.py（自身のツール定義ファイル）
  → Agent writes a new tool class (NotionFileCreator) following the factory pattern
  → Runtime detects file modification via st_mtime
  → importlib.reload() — new tool is registered instantly
  → Agent calls the tool IT JUST WROTE to complete the request
```

このループは **双方向** に働く：エージェントはツールを**作成**できるだけでなく、**削除**もできる。ワークショップではエージェントが自身の bash ツールをコードから削除し、ランタイムがそれを検知してレジストリから除去するデモも行われた。

## The Three Enablers

### 1. Factory Pattern（ツールファクトリー）

ツール定義をクラスとして分離し、実行ロジックとスキーマ生成を切り離す：

```python
class AgentTool(BaseModel):
    """Base class for all tools. Define parameters → auto-generate schema."""
    name: str
    description: str
    
    async def execute(self, ctx: AgentContext) -> ToolResult:
        raise NotImplementedError

class ReadFile(AgentTool):
    path: str
    name = "read_file"
    description = "Read contents of a file"
    
    async def execute(self, ctx: AgentContext) -> ToolResult:
        content = await aiofiles.read(self.path)
        return ToolResult(output=content)
```

**利点**:
- 新しいツール = 新しいクラスを `agent_tools.py` に追加するだけ
- Pydantic が型ヒントから自動で function calling スキーマを生成
- `execute()` メソッドは LLM なしで独立してテスト可能
- ランタイムとエージェントループは**一切変更不要**

> *"All you need to implement a new tool is define the parameters you want. These are automatically converted into a schema. And you can test your execute function independently of your model being called."* — Ivan Leo

### 2. Hot Reload（ホットリロード）

標準的な Python ランタイムはモジュールを一度だけロードする。エージェントが新しいツールを書いても、サーバー再起動が必要になる。ホットリロードがこれを解決する：

```python
class AgentRuntime:
    def __init__(self):
        self._tools_mtime = os.path.getmtime("agent_tools.py")
        self._load_tools()
    
    def _check_reload(self):
        current_mtime = os.path.getmtime("agent_tools.py")
        if current_mtime > self._tools_mtime:
            importlib.reload(agent_tools)
            self._load_tools()
            self._tools_mtime = current_mtime
```

`get_tools()` または `execute_tool()` が呼ばれる**毎回**、ファイルの変更をチェック。変更があれば `importlib.reload()` で新しいツールを即座に登録する。

> *"Because our tools are defined in another file we can just check when the file was last modified. All the tools — they're not concrete things. They're just definitions."*

### 3. Hooks Architecture（フックシステム）

自己拡張を実用的にするには、エージェントのアクションに対して副作用を合成可能にする必要がある：

```python
class Agent:
    def __init__(self):
        self._hooks = {
            "on_model_response": [],
            "on_tool_call": [],
            "on_tool_result": [],
        }
    
    async def emit(self, event: str, **kwargs):
        for handler in self._hooks[event]:
            await handler(**kwargs)
```

- **Telegram 連携**もフックの一種 — `on_model_response` に Telegram 送信ハンドラを登録するだけで、コアループは一切変更不要
- **Pretty output** — Rich ライブラリを使った構文ハイライトやビジュアル diff もフックで実装
- **Logging/observability** — Logfire への記録もフックとして追加

> *"Literally all we had to do to get the Telegram bot working wasn't any complex functionality — just define on_model_response and on_tool_result Telegram hooks. Everything works out of the box because you have very good primitives."*

## Memory: Markdown Compaction（Markdownメモリ圧縮）

自己拡張エージェントが長期運用で有用であり続けるには、メモリが必要。OpenClaw のアプローチは**ベクトルDBも埋め込みも使わない**：

1. 会話が閾値を超えたら、別の LLM コールで要約
2. タイムスタンプ付き Markdown ファイルとして `memory/` フォルダに追記
3. エージェントは起動時や必要に応じてこのファイルを読み返す

> *"People are so surprised that something simple like appending summaries to a markdown file works so well for memories. A lot of the love that OpenClaw has is just because the model can see the raw chats and the model can see the summaries."*

## The Full Architecture

```
┌─────────────────────────────────────────────────┐
│                  Agent Loop                       │
│  while True:                                     │
│    response = model.generate(contents, tools)     │
│    if response.is_text: return response           │
│    if response.is_tool_call:                      │
│      emit("on_tool_call", ...)    ← hooks         │
│      result = runtime.execute(name, args)         │
│      emit("on_tool_result", ...)  ← hooks         │
│      contents.append(result)                      │
│    runtime._check_reload()        ← hot reload    │
├─────────────────────────────────────────────────┤
│  AgentRuntime (factory + hot reload)              │
│  ┌─────────────────────────────────────────────┐ │
│  │ agent_tools.py (watched for changes)         │ │
│  │   class ReadFile(AgentTool): ...             │ │
│  │   class WriteFile(AgentTool): ...            │ │
│  │   class BashTool(AgentTool): ...             │ │
│  │   class NotionFileCreator(AgentTool): ... ←  │ │
│  │        ↑ agent writes this itself!           │ │
│  └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────┤
│  Hooks (composable side effects)                  │
│  ├── on_model_response → Telegram send            │
│  ├── on_tool_call → Rich terminal diff            │
│  └── on_tool_result → Logfire observability       │
├─────────────────────────────────────────────────┤
│  Memory (markdown compaction)                     │
│  └── memory/2026-02-28.md ← timestamped summaries │
├─────────────────────────────────────────────────┤
│  Deployment (Modal sandbox)                       │
│  ├── FastAPI webhook server                       │
│  ├── modal.Queue (per-chat-id)                    │
│  └── modal.Sandbox (isolated execution)           │
└─────────────────────────────────────────────────┘
```

## Progressive Disclosure（段階的開示）

自己拡張の裏にある重要な設計原則：**ツールが多いほど高性能とは限らない**。

> *"Imagine if someone gave you 200 tools to choose from every time you had to make a decision. You wouldn't even be able to finish reading all of the tools before you had to give a response."* — Hugo Bowne-Anderson

Pi/OpenClaw の哲学：4つの基本ツール（read/write/edit/bash）から始め、必要に応じてエージェント自身がツールを追加していく。これにより：
- コンテキストウィンドウの圧迫を避ける
- モデルが「ツール選択の麻痺」に陥らない
- 必要になった時にだけ能力を拡張する

## Safety: Runaway Loop Prevention

自己拡張エージェントのリスクとして、ツール呼び出しの無限ループがある。OpenClaw の対策：

```python
# Per-turn tool-call budget
TOOL_CALL_BUDGET = 5
calls_since_user_message = 0

# When budget exceeded:
# - Remove all tools from the API call
# - Inject guardrail instruction: "Summarize and respond to the user"
# - Model is FORCED to stop and produce a text response
```

## Relationship to Pi and OpenClaw

| Aspect | Pi | OpenClaw | This Workshop |
|--------|----|---------|---------------|
| Language | TypeScript | Python wrapper | **Pure Python** |
| Core tools | read/write/edit/bash | read/write/edit/bash | read/write/edit/bash |
| Extensions | TypeScript SDK + npm | Pi SDK + hooks | Factory pattern + hot reload |
| Memory | Claimed unnecessary | Markdown compaction | Markdown compaction |
| Deployment | CLI / RPC / SDK | Modal sandbox | Modal sandbox |
| Self-extension | Skills/packages | Skills + MCP | Agent writes own tool classes |

このワークショップは **PiとOpenClawの設計思想を Pure Python で再構築** したもの。TypeScript や npm の依存なしに、同じ原則を実装できることを示している。

## Key Insights

1. **ツールをクラスにするだけで、エージェントは自分でツールを書ける** — ファクトリーパターンはシンプルだが、自己拡張の扉を開く
2. **`execute()` は初日から async に** — 実世界のエージェントはネットワークI/O待ちが大半を占める
3. **フックがエージェントを合成可能にする** — Telegram連携もロギングも、コアループに一切手を加えずに追加できる
4. **Markdown追記で十分なメモリになる** — ベクトルDBや埋め込みは不要
5. **モデルへの「共感」が設計を変える** — 200個のツールを一度に渡すのではなく、段階的に開示する

## Armin Ronacher's Perspective: Agents Built for Agents Building Agents

Armin Ronacher（Flask作者、[[entities/pi|Pi]] の主要ユーザー・推進者）による Pi の設計哲学の解説（[2026年1月](https://lucumr.pocoo.org/2026/1/31/pi/)）は、Hugo+Ivan のワークショップが実装した原則の**前提となる世界観**を提示している：

> *"Agents Built for Agents Building Agents — software that is malleable like clay. The agent maintains its own functionality."*

### Session Trees（セッションツリー）

Pi のセッションは**ツリー構造**を持ち、ブランチとナビゲーションが可能：

```
Main session (building feature X)
  ├── Branch: fix broken extension tool (side-quest)
  │   └── Agent rewrites tool → test → rewind to main
  └── Branch: code review context (fresh, isolated)
```

- サイドクエストのためにメインセッションのコンテキストを**浪費しない**
- ツール修正後、メインセッションに戻ると Pi がブランチでの変更を要約
- Hugo+Ivan の `RunState` 分離とは異なるアプローチだが、同じ「コンテキスト汚染の防止」という目標

### Extension State in Sessions（セッション内拡張状態）

Pi の AI SDK は、モデルメッセージに加えて**カスタムメッセージ**をセッションファイルに保持する：

- 拡張機能が状態を永続化（モデルには送信されない）
- 複数プロバイダ間のセッション可搬性を維持（特定プロバイダの機能に依存しない）
- Hugo+Ivan の `AgentContext`（外部依存注入）と `RunState`（可変状態）の分離に通じる設計

### No MCP — By Philosophy, Not Laziness

> *"Pi's entire idea is that if you want the agent to do something that it doesn't do yet, you don't go and download an extension or a skill. You ask the agent to extend itself."*

- MCP は意図的な**非搭載** — 怠惰ではなく哲学
- エージェントが自分でツールを書くことを**祝福**する設計
- ダウンロードした拡張ではなく、エージェントに「あの拡張を見て、こう変更して」と指示する

### Software Building Software — The Lived Experience

> *"None of this was written by me, it was created by the agent to my specifications. I told Pi to make an extension and it did. There is no MCP, there are no community skills, nothing. They are hand-crafted by my clanker."*

Armin の全拡張（ブラウザ自動化、コードレビュー、TODO管理、コミットメッセージ整形）は**エージェント自身が作成**したもの。この「ソフトウェアがソフトウェアを構築する」体験が、Pi への没頭を生んだ。

### The Pipeline: Write → Reload → Test → Loop

Pi のホットリロードは Hugo+Ivan の `importlib.reload()` と同じパターンだが、**テスト駆動**の要素が加わる：

```
Agent writes extension code → hot reload → agent tests it → fails → rewrites → reloads → passes
```

これにより、エージェントが「動くまで繰り返す」自律的な改善ループが成立する。Hugo+Ivan のワークショップ（Step 5のフック + Step 6のエージェントループ）と補完的。

## References

- [Building Agents That Build Themselves (Substack)](https://hugobowne.substack.com/p/building-agents-that-build-themselves) — Hugo Bowne-Anderson, Feb 2026
- [Build Your Own AI Assistant (GitHub)](https://github.com/hugobowne/build-your-own-ai-assistant) — Companion code repo
- [Workshop Livestream (YouTube, 96min)](https://www.youtube.com/watch?v=dDQ4rKXeHRw) — Full live build session
- [[concepts/self-evolving-agents]] — Related concept
- [[concepts/agent-harness]] — Agent harness fundamentals
- [[entities/pi]] — Pi coding agent (Mario Zechner)
- [[entities/openclaw]] — OpenClaw (Peter Steinberger)
- [[concepts/hermes-agent-architecture]] — Hermes Agent architecture (capability accumulation, self-generating skills)
- [[entities/hugo-bowne-anderson]] — Hugo Bowne-Anderson
- [[entities/ivan-leo]] — Ivan Leo
