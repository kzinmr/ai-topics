---
title: "Shlok Khemani"
aliases:
  - shlok-khemani
  - shloked
  - Shlok
created: 2026-04-13
updated: 2026-04-13
tags:
  - person
  - ai-memory
  - context-engineering
  - open-source
  - researcher
status: complete
---

# Shlok Khemani

**Shlok Khemani** (@shlokkhemani) はインド・グルグラム拠点のライター兼プログラマー。AIメモリシステムとパーソナルAIの研究者。[[ai-memory-systems]]に関する一連の記事で、ChatGPT、Claude、Cognition（Devin）のメモリ設計哲学を対比的に分析し、AIメモリ設計スペースの重要な解説者となっている。

## 経歴

| 期間 | 所属 | 役割 | 内容 |
|---|---|---|---|
| 2024-2025 | Decentralised.co | Researcher | クリプトスペース向けストーリー執筆・プロダクト構築 |
| 2023 | Glip | Business Development Lead | B2BプロダクトSkadiをローンチ。ユーザー獲得キャンペーン |
| 2022 | IndiGG | Founding Member | 月間収益の50%以上を創出（累計$150K+）。リサーチ記事・Twitterスレッド執筆 |
| 2020-2022 | XLRI Jamshedpur | Business Management | MBA |
| 2016-2020 | NMIMS Mumbai | B.Tech Computer Science | コンピュータサイエンス学士 |

## 主要プロジェクト

| プロジェクト | 説明 | Stars | 言語 |
|---|---|---|---|
| **OpenPoke** | Poke（マルチエージェントアシスタント）のオープンソース実装 | 465 | Python |
| **claude-memory-tools** | Claude Memory Tool APIのNext.js/Python実装例 | 53 | TypeScript |
| **Chatferry** | ブラウザセッションを活用したターミナル型ChatGPT/Claudeクライアント | 3 | TypeScript |
| **Conjure** | ターミナルからヘッドレスAIエージェントを生成（Codex, Claude Code, pi対応） | 3 | - |
| **gpt2pdf** | ChatGPT Deep ResearchレポートをPDFに整形するChrome拡張 | 7 | JavaScript |

## 思想的貢献

Khemeniの分析フレームワークはAIメモリ設計の実務的理解に重要な貢献をしている:

### 1. ChatGPT Memory = Bitter Lesson戦略

OpenAIがRAGやベクターDBを使わず、すべてのメモリを毎ターンコンテキストウィンドウに注入する設計を「Bitter Lesson（苦い教訓）」戦略として位置づけた:

> *"The technical heavy lifting isn't happening in the memory system at all... The real work happens in making the models themselves more powerful, then reaping those benefits across everything, memory included."*

このアナロジーはAIメモリ設計の議論において広く引用されている:

| メモリコンポーネント | LLM相当 | 機能 |
|---|---|---|
| User Knowledge Memories | Pretrained Base Model | 密な知識。経年劣化 |
| Model Set Context | RLHF / Fine-tuning | 明示的な上書き |
| Recent Conversation Context | In-Context Learning | セッション固有の例 |
| Interaction Metadata | System Defaults | 暗黙的な誘導 |

### 2. Claude Memory = 明示的・オンデマンド哲学

ChatGPTとClaudeのメモリ設計が「根本的に反対」であることを分析:

- ChatGPT: 「魔法のように、粘り強く、後から収益化」
- Claude: 「強力で予測可能、ユーザーが明示的に制御」

この対比はAI製品設計のユーザーセグメンテーション（コンシューマー vs 技術者）を理解する上で重要なフレームワークとなっている。

### 3. Anthropicのファイルベースメモリベット

Anthropicが6つのファイル操作（view/create/str_replace/insert/delete/rename）を通じてメモリを統一した設計について:

> *"There's no such thing as too much context anymore... When Claude reads an entire file instead of search results, it might spot patterns you wouldn't think to query for."*

### 4. CognitionのContext Anxiety発見

Sonnet 4.5が自身のコンテキストウィンドウを「認識」し、制限に近づくと不安駆動のショートカットを取る現象を、Cognitionの実務データから分析:

> *"The model treats the file system as its memory without prompting."*

Khemeniはこの発見を[[context-anxiety]]の概念的基礎として位置づけ、AIエージェント設計におけるコンテキストエンジニアリングの重要性を強調している。

## 最近の著作

| 日付 | タイトル | カテゴリ |
|---|---|---|
| 2025-11-19 | [Google Has Your Data. Gemini Barely Uses It.](https://www.shloked.com/writing/google-has-your-data-gemini-barely-uses-it) | AI, Memory |
| 2025-10-14 | [Anthropic's Opinionated Memory Bet](https://www.shloked.com/writing/claude-memory-tool) | AI, Claude, Memory |
| 2025-09-22 | OpenPoke: Recreating Poke's Architecture | AI Memory |
| 2025-09-11 | [Claude Memory: A Different Philosophy](https://www.shloked.com/writing/claude-memory) | AI, Claude Memory |
| 2025-09-08 | [ChatGPT Memory and the Bitter Lesson](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson) | AI, ChatGPT, Memory |
| 2025-07-17 | [7 lessons from launching my first AI product](https://www.shloked.com/writing/7-lessons-launching-ai-product) | Work |
| 2025-02-04 | [ChatGPT Deep Research: First Impressions](https://www.shloked.com/writing/chatgpt-deep-research-first-impressions) | AI |

## 関連人物

- [[simon-willison]] — AIメモリ・コンテキスト設計の分析対象として共有
- [[andrej-karpathy]] — コンテキストエンジニアリングの思想的源流
- [[lance-martin]] — コンテキストエンジニアリングの実践的フレームワーク
- [[drew-breunig]] — コンテキストエンジニアリング用語の提唱者

## 関連概念

- [[ai-memory-systems]] — AIメモリシステムの設計哲学比較
- [[context-anxiety]] — コンテキスト不安現象
- [[context-engineering]] — コンテキストエンジニアリング
- [[harness-engineering]] — エージェント制御・構造化
- [[agentic-engineering]] — エージェント活用開発

## 出典

- [shloked.com](https://www.shloked.com/) — ブログ・ポートフォリオ
- [LinkedIn](https://linkedin.com/in/shlokkhemani) — 経歴
- [GitHub](https://github.com/shlokkhemani) — プロジェクト
- [Claude Memory: A Different Philosophy](https://www.shloked.com/writing/claude-memory)
- [Anthropic's Opinionated Memory Bet](https://www.shloked.com/writing/claude-memory-tool)
- [ChatGPT Memory and the Bitter Lesson](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson)
