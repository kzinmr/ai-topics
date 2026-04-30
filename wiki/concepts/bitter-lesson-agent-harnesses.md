---
title: "The Bitter Lesson of Agent Harnesses"
type: concept
aliases:
  - bitter-lesson-of-agent-frameworks
  - minimal-agent-architecture
tags:
  - ai-agents
  - harness-engineering
  - agent-sdk
  - browser-use
status: complete
description: "Gregor Zunic (Browser Use founder) の提唱する 'The less you build, the more it works' — 最小限のエージェントアーキテクチャ哲学。"
created: 2026-04-30
updated: 2026-04-30
sources:
  - "https://browser-use.com/posts/bitter-lesson-agent-frameworks"
  - "https://x.com/gregpr07/status/2047358189327520166"
  - "raw/articles/the-bitter-lesson-of-agent-harnesses-2026-04-24--d9ffedba.md"
related:
  - "[[concepts/harness-engineering]]"
  - "[[entities/browser-use]]"
  - "[[concepts/agent-loop]]"
---

# The Bitter Lesson of Agent Harnesses

> **Definition:** Rich Suttonの「The Bitter Lesson」（計算量を最大限に活用する一般的手法は、人手の知識を常に凌駕する）をエージェントフレームワークに適用した原則。**「The less you build, the more it works」** — エージェントフレームワークの価値は1万行の抽象化ではなく、RL訓練されたモデルにある。

## 核心テーゼ

- **All the value is in the RL'd model, not your 10,000 lines of abstractions**
- **An agent is just a for-loop of messages.** The only state: keep going until the model stops calling tools
- **Agent frameworks fail not because models are weak, but because their action spaces are incomplete**

## なぜ伝統的フレームワークが失敗するか

1. **Abstractions freeze assumptions** — Planningモジュール、検証レイヤー、出力パーサーは開発者のバイアスをエンコードする。モデルの実際の能力ではない
2. **RL breaks constraints** — 数百万サンプルで訓練されたモデルは、開発者が予測できないパターンを発見する。過度な仕様設定はモデルの訓練活用を阻害
3. **99% of the work is in the model** — 現代LLMは専用ツールなしでタスクをネイティブに処理可能（例: Claude Codeが直接AppleScriptを記述）

## Browser Useのアーキテクチャ哲学

### Inversion Strategy
最大限の能力から始めて、評価に基づいて制限を課す。LLMにほぼ人間と同じブラウザの自由を与え、その後で安全性/構造をレイヤーする。

### 生制御面（Raw Control Surfaces）
Brittleなプリミティブ（click/type/scroll）を以下で置換:
- **Chrome DevTools Protocol (CDP):** 直接ブラウザ制御
- **Browser Extension APIs:** 権限付き状態とアクティブウィンドウアクセス

→ ほぼ完全なaction spaceを生成し、自己修正を可能にする。

## 技術的実装詳細

### Context Bloat問題
ブラウザstate snapshotは1リクエストあたり50KB+。約10インタラクション後には500KB+に到達し、hallucination、一貫性喪失、クラッシュを引き起こす。

### Ephemeral Tool Solution
直近X回の呼び出し出力のみを保持。モデルが必要なのは直近のstateであり、古いsnapshotはノイズ。

```python
@tool("Get browser state", ephemeral=3)  # Keep last 3 only
async def get_state() -> str:
    return massive_dom_and_screenshot
```

### Explicit Termination (`done` Tool)
Naiveな「ツール呼び出しなしで停止」は早期終了を招く。明示的な`done()`ツールで意図的な完了を強制。
- **CLI Mode:** ツール呼び出しなしで停止（クイックインタラクション）
- **Autonomous Mode:** 明示的な`done()`呼び出しのみで停止

### Model-Agnostic Protocol
```python
class ChatAnthropic:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...

class ChatOpenAI:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...

class ChatGoogle:
    async def ainvoke(self, messages, tools) -> ChatCompletion: ...
```

## コアエージェントループ

エージェント全体がこれに還元される:

```python
while True:
    response = model(messages, tools)
    if response.tool_calls:
        for tc in response.tool_calls:
            messages.append(tc.execute())
    else:
        break  # Or await done()
```

> "Everything else — retries, rate limits, connection recovery, context compaction, token tracking — is ops, not agent."

## 実装リソース

- **[agent-sdk](https://github.com/browser-use/agent-sdk)** — 最小エージェントアーキテクチャSDK（オープンソース）
- **[browser-harness](https://github.com/browser-use/browser-harness)** — セルフヒーリングブラウザハーネス
- **[bu.app](https://bu.app)** — Browser Useのプロダクションエージェント製品
- [Cloud Docs](https://docs.cloud.browser-use.com) | [Open Source Docs](https://docs.browser-use.com)

## Harness Engineeringとの関係

[[concepts/harness-engineering]]が「Agent = Model + Harness」の包括的フレームワークを提供するのに対し、Bitter Lessonアプローチはその逆を提唱する。**最小限のharnessでモデルの力を最大限に引き出す** — 両者は補完的。

| 次元 | Harness Engineering | Bitter Lesson |
|------|-------------------|---------------|
| 焦点 | 信頼性/安全性/追跡可能性 | 最小抽象化/モデル能力最大化 |
| アプローチ | 体系的な制御レイヤー | 「less is more」— 必要なものだけ |
| 適合 | プロダクション/エンタープライズ | 高速反復/スタートアップ |
| 共通基盤 | RL訓練モデルの活用 | RL訓練モデルの活用 |

## Sources

- [The Bitter Lesson of Agent Frameworks](https://browser-use.com/posts/bitter-lesson-agent-frameworks) (2026-01-16, Gregor Zunic)
- [x.com/gregpr07/status/2047358189327520166](https://x.com/gregpr07/status/2047358189327520166) (2026-04-24)
- [agent-sdk GitHub](https://github.com/browser-use/agent-sdk)
