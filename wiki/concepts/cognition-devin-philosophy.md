---
title: "Cognition/Devin Philosophy — Agentic Coding at Scale"
aliases:
  - cognition-philosophy
  - devin-approach
  - cognition-agentic-coding
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - cognition
  - devin
  - agentic-engineering
  - context-engineering
related:
  - "[[agentic-engineering-patterns]]"
  - "[[harness-engineering]]"
  - "[[context-engineering]]"
  - "[[agent-team-swarm/_index]]"
sources:
  - "https://cognition.ai/blog/dont-build-multi-agents"
  - "https://devin.ai/agents101"
  - "https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges"
  - "https://cognition.ai/blog/devin-review"
  - "https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments"
  - "https://cognition.ai/blog/introducing-devin-2-2"
  - "https://cognition.ai/blog/devin-can-now-manage-devins"
  - "https://nader.substack.com/p/engineering-for-agents-that-never"
---

# Cognition/Devin Philosophy — Agentic Coding at Scale

Cognition Labs（Devin開発元）が、コーディングエージェントの実運用を通じて得た実践的知見の体系。
Scott Wu（CEO）、Walden Yan、Nader Dabit（Growth Engineer）、Theodor Marcu（CTO）らが発信。

Anthropicの **"Building Effective Agents"** や Simon Willisonの **"Agentic Engineering"** と対比されつつ、
Cognitionは**「エージェントを実際にプロダクションで動かし続ける」**観点から独自の知見を蓄積している。

## 核心原則

### 1. Context Continuity（コンテキストの連続性）
> *"Share context, and share full agent traces, not just individual messages"*
> *"Actions carry implicit decisions, and conflicting decisions carry bad results"*
> — Walden Yan, "Don't Build Multi-Agents"

Cognitionが最も重視するのは**コンテキストの分断を防ぐ**こと。
- マルチエージェントはコンテキストが断片化し、暗黙の決定が共有されない
- 単一スレッドの線形エージェントが最も信頼性が高い
- コンテキストが溢れる場合のみ、圧縮レイヤーを追加する
- Claude Codeのサブエージェントが**逐次実行**に制限している理由と同じ

### 2. Agent as Junior Partner（エージェントはジュニアパートナー）
> *"Think of the agent as a junior coding partner whose decision-making can be unreliable."*
> — "Coding Agents 101"

- エージェントは「何をするか」だけでなく「どうするか」を指示する必要がある
- 防御的プロンプティング（新人インターンへの指示のように曖昧さを事前に潰す）
- **Checkpoint ワークフロー**: Plan → Implement → Test → Fix → Checkpoint → Next
- 人間の役割は最終的な正確性の保証（アーキテクチャ判断、エッジケースの検証）

### 3. The Agent Loop（Write → Catch → Fix → Merge）
> *"A coding agent is a tool. A coding agent paired with a review agent... that's a system. Systems compound. Tools don't."*
> — "Closing the Agent Loop"

Cognitionが到達した成熟パターン:
1. **Write** — エージェントがコードを書く（ドラフトPR）
2. **Catch** — レビューエージェントがバグを検出（Lint, CI, セキュリティスキャナー）
3. **Fix** — エージェントが自動的に修正（botトリガー）
4. **Merge** — 人間は判断のみ（アーキテクチャ、プロダクト方向性）

このループにより、「メカニカルな修正」から人間が解放される。

### 4. Context Anxiety & Token Economics
> *"the model consistently underestimates remaining tokens with high precision"*
> — "Rebuilding Devin for Claude Sonnet 4.5"

Sonnet 4.5で発見された新現象:
- **Context Anxiety**: モデルが自身のコンテキスト限界を「自覚」し、早期に要約を開始
- **1M Beta + 200k Cap Trick**: 1Mコンテキストを有効化し、200kで制限。モデルに「余裕がある」と錯覚させ、不安によるショートカットを防ぐ
- **Parallel Execution**: Sonnet 4.5は並列ツール呼び出しを最大化。コンテキストを速く消費するが、空コンテキストでは劇的に高速
- **Self-Verification**: テスト・スクリプト作成に積極的だが、根因対処よりworkaroundを選びがち

## Managed Devins（パラレルAgent協調）

> *"When one agent tries to handle too many things in a single session, context accumulates, focus degrades."*
> — "Devin Can Now Manage Devins"

Cognitionが「マルチエージェント」に慎重だった姿勢から転換した唯一のケース:
- メインDevinが**コーディネーター**として機能
- 各Managed Devinは**独立したVM**（独自のシェル、ブラウザ、テスト環境）
- コンテキスト分断を防ぐため、タスクを**スコープされた独立単位**に分割
- メインDevinは子エージェントの**完全なtrajectory**を読み、次のタスク分解に活かす
- 2026年3月時点でGA（全ユーザー利用可能）

これはAnthropicの「Don't Build Multi-Agents」の**例外**ではなく、**前提を満たした上での実装**:
- 各エージェントが完全なコンテキスト（独立VM）を持つ
- コーディネーターが一元管理（スコープ、モニタリング、コンフリクト解消）
- 並列実行は独立タスクに限定

## Engineering for Agents That Never Sleep（Nader Dabit）

> *"The prompt is the bottleneck. The alert, the failing test, the approved spec — any of these can kick off an agent directly."*
> — Nader Dabit, "Engineering for Agents That Never Sleep"

Cognitionの内部データ（2026年3月時点）:
- **70%** が人間による起動（Web/Slack/Linear）
- **30%** が自動起動（API/スケジューラ）
- 予測: 数ヶ月で30/70、1年で10/90に逆転

**前提となるスキャフォールディング:**
1. 包括的なユニットテスト（エージェントが自己検証可能）
2. 十分なドキュメント（エージェントが質問なしで文脈理解）
3. 再現可能な開発環境（カスタムセットアップ不要）
4. リッチなシステムコンテキスト（アーキテクチャ・規約・サービス間相互作用）

> *"Without it, you have agents that write code. With it, you have agents that ship software."*

## Cognition vs Anthropic vs Willison — 比較

| 次元 | Cognition (Devin) | Anthropic | Simon Willison |
|------|------------------|-----------|----------------|
| 焦点 | エージェント実運用 | エージェント構築 | 開発者ワークフロー |
| マルチエージェント | 慎重 → Managed Devins（条件付き） | 非推奨 | subagents（並列委任） |
| コンテキスト | 1M+cap trick, anxiety対策 | Context Engineering | Context Window Management |
| 品質保証 | Write→Catch→Fix→Merge | Evaluator-Optimizer | Red/Green TDD, First Run Tests |
| 自動化 | Botトリガー, autofix | Self-Evaluation | Cognitive Debt回避 |
| 人間役割 | アーキテクチャ判断のみ | Human-in-the-loop | オーケストレーター |

## 出典一覧

| 日付 | タイトル | 著者 | 主要トピック |
|------|---------|------|-------------|
| Jun 2025 | Don't Build Multi-Agents | Walden Yan | コンテキスト連続性、シングルエージェント推奨 |
| Jun 2025 | Coding Agents 101 | Cognition Team | 防御的プロンプティング、チェックポイント |
| Sep 2025 | Rebuilding Devin for Sonnet 4.5 | Cognition Team | Context Anxiety、1M+cap trick |
| Jan 2026 | Devin Review | Cognition Team | レビューボトルネック、AIバグ検出 |
| Feb 2026 | Closing the Agent Loop | Cognition Team | Autofix、botトリガー、Write→Catch→Fix→Merge |
| Feb 2026 | Devin 2.2 | Cognition Team | Computer use E2Eテスト、3x高速化 |
| Mar 2026 | Devin Can Manage Devins | Cognition Team | Managed Devins、コーディネーターパターン |
| Mar 2026 | Engineering for Agents That Never Sleep | Nader Dabit | 自動起動、スキャフォールディング |