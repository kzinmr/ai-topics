---
title: "Akira (@realmcore_) / Random Labs"
handle: "@realmcore_"
name: "Akira (Random Labs)"
created: 2026-04-13
updated: 2026-04-13
tags: [person, coding-agents, swarm-orchestration, thread-weaving, rlm, slate]
aliases: ["Random Labs", "Akira (RL)", "realmcore"]
status: complete
---

# Akira (@realmcore_) — Random Labs / Slate

| | |
|---|---|
| **X** | [@realmcore_](https://x.com/realmcore_) |
| **GitHub** | [github.com/random-labs](https://github.com/random-labs) |
| **Blog** | [randomlabs.ai/blog](https://randomlabs.ai/blog) |
| **Company** | Random Labs (YC S24, founded 2024 by Kiran & Mihir Chintawar) |
| **Known for** | Slate: Thread Weaving, Episodic Memory, Swarm Orchestration, Skill Chaining |
| **Bio** | Random LabsのAIエンジニアリングチーム。Slateの開発をリード。「RLM for coding」を提唱し、ReActとRLMを超える第3のアーキテクチャを構築。 |

## Overview

Akira (@realmcore_) は Random Labs のAIエンジニアリングチームの中心的な声。同社は2024年設立、YC S24バッチのスタートアップで、創設者は **Kiran** と **Mihir Chintawar**。

Random Labsは「ソフトウェア開発の次の2000万人のエンジニアをオンラインにする」ことをミッションとし、Slateをそのためのプラットフォームとして開発している。

## Core Ideas

### 1. Thread Weaving — エピソード記憶を持つSwarmアーキテクチャ

Slateの核心は**Thread Weaving**。OSのカーネルがプロセスを管理するように、LLMオーケストレーターがスレッドを管理する。

> "Instead of letting RAM fill until the process crashes, each thread return is a natural opportunity to decide what gets retained, what gets compressed, and what gets discarded."

**スレッド**: 一度に1アクションを実行する汎用作業員。永続的なサブエージェントとは異なり、スレッドは一時停止して制御をオーケストレーターに戻す。コンテキストは**共有・合成可能**で、メッセージパッシングによる隔離ではない。

**エピソード**: スレッドの完了したアクションシーケンスの圧縮表現。**真のエピソード記憶**として機能し、自然な圧縮境界となる。

**スレッド・ウィービング**: オーケストレーターがスレッドをディスパッチ → スレッド実行 → エピソード返却 → エピソードが後続スレッドの入力となる。静的な計画ではなく、**暗黙的で適応的なタスク分解**を可能にする。

### 2. RLM for Coding — RLMの実践的適用と批判的改良

Alex ZhangのRLM (Recursive Language Models) をコーディングエージェントに適用しつつ、その限界も認識している。

> "We built RLM for coding. And it F*cking rocks. Swarm native agents are here to stay."

**RLMの限界認識**:
- RLM: 「Blind N-step execution」— 中間フィードバックなしでフルシーケンスをコミット
- Slate: Thread Weavingで**中間状態の保持**を実現

**Random Labsの批判的立場** (Agent Wars 2026-03-13):
> "Random Labs says coding agents are patching over a problem they should be solving... both paradigms [RLM and ReAct] treat context management as an afterthought. RLMs externalize data into a Python REPL and hand analysis off to sub-LLMs. ReAct agents interleave reasoning traces with action steps. Random Labs argues that neither was built for the multi-hour, multi-file sessions that real software engineering demands."

### 3. Three Foundational Problems

Random Labsが特定した現代のエージェントの3つの根本問題:

| 問題 | 説明 | 洞察 |
|---|---|---|
| **Long-Horizon Tasks** | パス依存のタスク（例: 複数ファイルに跨る変更） | 動的ワーキングメモリ、戦略的計画、中間適応が必要 |
| **Working Memory & "Dumb Zone"** | コンテキストウィンドウが埋まるにつれLLMの注意力が非一様に劣化 | 「右端のDumb Zone — ウィンドウが埋まるほど注意力の質が劣化」全てのフロンティアモデルが suffer |
| **Strategy vs. Tactics** | 戦略 = オープンエンドな計画 vs 戦術 = 局所実行シーケンス | ソフトウェア工学はこのスペクトラム全体をカバー: `bashコマンド実行`(戦術) vs `後方互換性のあるスキーマ設計`(戦略) |

### 4. Prior Approaches & Critical Failure Modes

| アプローチ | メカニズム | 致命的な失敗モード |
|---|---|---|
| **Compaction** | 定期的にコンテキストをドロップ/要約 | **Lossy & unpredictable.** クリティカルな状態をドロップするリスク (Claude Code, Ralph Wiggum loop, Amp handoffs) |
| **Subagents** | コンテキストを別エージェントインスタンスに隔離 | **Poor cross-context transfer.** レスポンスメッセージのみ返却; 中間状態の共有に失敗 |
| **Markdown Planning** | 構造化ファイルによる事前計画の強制 | **3つの失敗モード:** 仕様不足の計画、不完全な実行、適応/更新の失敗。「knowledge overhang」に制限 |
| **Task Trees (Direct Decomposition)** | リジッドなゲート付きステップ実行グラフ | **低表現力 & 非柔軟。** 新しい情報に適応不可; 自然言語の柔軟性を構造的硬直性とトレード |
| **RLM (Recursive LM)** | Python REPLでの反復的・再帰的実行 | **Blind N-step execution.** 中間フィードバックなし; モデルがフルシーケンスを事前にコミット |
| **Multi-Agent (Devin/Manus/Altera/Codex)** | 戦略化 → 委任 → 圧縮 → 同期 | **同期のボトルネック。** Sync = 遅い; Async = 調整の問題。圧縮境界がクリティカルな状態をドロップ |

### 5. Knowledge Overhang — 潜在知識の解放

> "The gap between what an LLM *knows* and what it *chooses* to do."

モデルが持つ潜在的な知能を、適切なコンテキスト管理とルーティングで引き出すアプローチ。Skillsは**プログレッシブ・ディスクロージャー**でアクティブ化/非アクティブ化され、限られたコンテキストスペース(200kトークン未満)を保護する。

### 6. Skill Chaining — 動的スキル定義

従来の「静的プロンプト」としてのスキル定義を批判:
> "A skill should be something the agent does not something the agent reads."

**Orchestration Skills**: ユーザーがアクティブ化するスキルが、他のスキルを参照して条件付きアクティベーションシーケンスを定義。プログラム的な自動化ワークフローを実現。

**Context Forking**:
- インタラクティブスキル → **Fork** (ブロッキング、UI乗っ取り)
- 自律スキル → **Thread** (バックグラウンド実行、分離コンテキスト)

⚠️ **Status**: As of April 1, 2026, forking is in **ALPHA** (信頼性確保のため延期)

## Slate Architecture: OS Analogy (Karpathy's LLM OS Framing)

| OS Component | Slate Equivalent |
|---|---|
| Kernel | Orchestration LLM |
| RAM | Context Window (scarce, actively managed) |
| Processes | Threads |
| Return Values | Episodes (compressed state) |
| Peripherals | Files, Terminal, Web, APIs |

## Architecture Comparison

| Aspect | ReAct | Markdown Plan | Task Trees | RLM | Multi-Agent (Devin/Codex) | **Slate** |
|---|---|---|---|---|---|---|
| **Planning** | Implicit | File-based | Explicit | REPL-driven | Planning Agent | **Implicit** |
| **Decomposition** | None | None | Direct Tree | REPL Functions | Task-based | **Implicit** |
| **Synchronization** | Single-thread | Single-thread | Gated Steps | REPL Return | Reduce/Message | **Episodes** |
| **Context** | Lossy | Static | Rigid | REPL Externalized | Compressed | **Episodic** |
| **Memory** | None | None | None | None | Lossy compaction | **True episodic** |

## Key Work

### Slate V1 (March 12, 2026)
- **Terminal Bench**: make-mips-interpreter taskで2/3テスト合格 (変化する環境での安定性実証)
- **実世界タスク**: オープンソースライブラリのTypeScript移植を$58.32で完了
- **インストール**: `npm i -g @randomlabs/slate`
- **Config**: `slate.json` でモデルスロット、権限、MCPサーバー、カスタムコマンドを定義

### RLM for Coding
- Alex ZhangのRLMアーキテクチャをコーディングエージェントに適用・改良
- Thread WeavingでRLMの中間フィードバック欠如を解決

### Skill Chaining (April 1, 2026)
- スキルを動的にチェーンし、条件付き実行シーケンスを定義
- Orchestration Skillsによる自動化ワークフロー
- Context Forking (Alpha)

## Connection to Harness Engineering & Agentic Engineering

AkiraのSlateは[[Harness Engineering]]の文脈で重要な位置を占める:

1. **Slate as a Meta-Harness**: Slate自体が大規模なharness — モデル間のルーティング、コンテキスト管理、権限制御を統合
2. **Thread Weaving as Harness Pattern**: 各スレッドが独立したharnessインスタンスとして機能し、エピソードで結果を合成
3. **Skill Chaining as Dynamic Harness**: 静的なharness定義ではなく、条件付きでスキルをチェーンする動的アプローチ
4. **Knowledge Overhang as Harness Insight**: 「モデルが知っていること」と「モデルが実際に使うこと」のギャップを埋めるのがharnessの役割

> "Slate is not merely a wrapper or a chatbot with file access; it is an implementation of a 'hive mind' philosophy designed to scale agentic work with the complexity of a human organization."

Slateは[[Agentic Engineering]]における「swarm orchestration」パラダイムの先駆的実装。DevinやCodexのような単一エージェントモデルから、複数モデルの並列協調への移行を体現している。

## Related People

| Person | Relationship | Wiki Link |
|---|---|---|
| [[Kiran (Random Labs)]] | Random Labs co-founder | — |
| [[Mihir Chintawar]] | Random Labs co-founder, CTO | — |
| [[Alex L. Zhang]](@a1zhang) | RLM開発者。SlateはRLMを改良して適用 | [[alex-zhang]] |
| [[Andrej Karpathy]] | LLM OS concept — SlateのOSアナロジーの源流 | [[andrej-karpathy]] |
| [[Peter Steinberger]](@steipete) | OpenClaw開発者。並列エージェントアプローチで関連 | [[peter-steinberger]] |
| [[Nader Dabit]](@dabit3) | Cloud agents / agent fleet — 長時間実行エージェントの文脈で関連 | — |

## X Activity Themes

| Theme | Content |
|---|---|
| **Thread Weaving** | Slateのアーキテクチャ解説、OS analogy、エピソード記憶 |
| **RLM for Coding** | RLMの実践的適用と限界の認識 |
| **Swarm Orchestration** | マルチモデル並列実行、hive mind哲学 |
| **Knowledge Overhang** | モデルの潜在知識の解放、コンテキスト管理の重要性 |
| **Skill Chaining** | 動的スキル定義、Orchestration Skills |
| **Critique of Existing Agents** | ReAct/RLMの限界、コンテキスト管理の重要性 |

## Sources

- [Random Labs Blog: Slate](https://randomlabs.ai/blog/slate)
- [Random Labs Blog: Skill Chaining](https://randomlabs.ai/blog/skill-chaining)
- [Agent Wars: Moving Beyond RLM and ReAct](https://agent-wars.com/news/2026-03-13-moving-beyond-rlm-and-react-based-coding-agents)
- [VentureBeat: YC-backed Random Labs launches Slate V1](https://venturebeat.com/orchestration/y-combinator-backed-random-labs-launches-slate-v1-claiming-the-first-swarm)
- [Podcast: Slate: An Agent Architecture - Vinh Nguyen](https://www.youtube.com/watch?v=zTXWPdsiv9c)
- [Slate Documentation](https://docs.randomlabs.ai/)
