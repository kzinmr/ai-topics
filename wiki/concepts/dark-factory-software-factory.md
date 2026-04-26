---
title: "Dark Factory Software Factory"
type: concept
created: 2026-04-13
updated: 2026-04-13
tags: [concept, agent-team-swarm, automation, strongdm]
related: [agent-team-swarm, openai-symphony, anthropic-managed-agents]
sources:
  - https://simonwillison.net/2026/Feb/7/software-factory/
  - https://simonwillison.net/2026/Jan/28/
  - https://github.com/strongdm/attractor
  - https://github.com/strongdm/cxdb
---

# Dark Factory Software Factory

**Source:** Simon Willison's Weblog (2026-01-28, 2026-02-07)
**Practitioners:** StrongDM AI Team (Justin McCarthy, Jay Taylor, Navan Chauhan)
**Related:** [[agent-team-swarm]], [[openai-symphony]], [[anthropic-managed-agents]]

---

## Overview

「Dark Factory（暗黒工場）」とは、**人間がコードを一切書かず、レビューもしない**ソフトウェア開発の最高自動化レベル。Fanucの無人工場（ロボットが稼働する工場は照明が不要＝暗い）に由来する比喻。

Simon Willisonが2026年1月28日にDan Shapiroの「AI支援プログラミング5レベル」モデルとして紹介し、2月7日にStrongDMの実践例として詳細を公開した。

---

## Dan Shapiroの5レベルモデル

| レベル | 名称 | 説明 |
|---|---|---|
| **Level 1** | Spicy Autocomplete | GitHub Copilot初期版、コード補完 |
| **Level 2** | Chat-Assisted | ChatGPTに聞いてコピペ |
| **Level 3** | Agent-Assisted | Claude Code/Codexがタスクを実行（人間が監視） |
| **Level 4** | The Engineering Team | 仕様と計画を立て、Agentが実装。人間はマネージャー役 |
| **Level 5** | Dark Factory | **人間不要の完全自律開発** |

### Level 5の定義

> At level 5, it's not really a car any more. You're not really running anybody's software any more. And your software process isn't really a software process any more. It's a **black box that turns specs into software**.
>
> Why Dark? Maybe you've heard of the Fanuc Dark Factory, the robot factory staffed by robots. It's dark, because it's a place where **humans are neither needed nor welcome**.
> — Dan Shapiro

---

## StrongDMの実践

### チーム構成
- **3名**（Justin McCarthy, Jay Taylor, Navan Chauhan）
- 2025年7月結成、数ヶ月で動作デモを達成
- Claude 3.5 Sonnet（2024年10月改訂）の能力向上が触媒

### Key Characteristics

1. **Nobody reviews AI-produced code, ever.** 人間は生成されたコードを一切見ない
2. **The goal is to prove the system works.** 大量の作業をテスト/検証に投入
3. **Humans design the system.** Agentが効果的に働く新しいパターンを発見するのが人間の役割

### Digital Twin Universe

StrongDMの最も印象的な概念:

> [The Digital Twin Universe is] behavioral clones of the third-party services our software depends on. We built twins of Okta, Jira, Slack and more. How do you clone the important parts? **With coding agents!**

依存サービス（Okta, Jira, Slack等）の振る舞いをAgentでクローンし、完全なテスト環境を構築。これにより:
- 外部サービスに依存しないテスト実行
- 24時間自動テスト運用
- Agent生成コードの品質保証

---

## Attractor: 非インタラクティブ・コーディングAgent

StrongDMが公開したコアプロダクト:

- **[github.com/strongdm/attractor](https://github.com/strongdm/attractor)** — リポジトリにはコードがなく、仕様を記述したMarkdownファイルのみ
  - 「あなたの好きなコーディングAgentにこの仕様を読ませろ」
- **[github.com/strongdm/cxdb](https://github.com/strongdm/cxdb)** — AI Context Store
  - 16,000行のRust + 9,500行のGo + 6,700行のTypeScript
  - 会話履歴とツール出力を保存するシステム

### Open Source Ecosystem

Attractor公開1ヶ月で数百のオープンソース実装が出現:
- 言語別フォーク
- 独自harness実装
- プロパティテスト/フォールトインジェクション/ファズテスト統合

---

## Simon Willisonの観察

> "Honestly, six months ago, I thought that was crazy, and today, probably 95% of the code that I produce, I didn't type it myself."
> — Simon Willison, Lenny's Podcast (2026-04)

WillisonはDark Factoryを「未来の姿」として位置づけつつも、重要な注意点を持っている:

- 95%のコードを自分で書いていないが、**残り5%の設計判断が極めて重要**
- AIがコードを書くこと自体は容易になったが、「何を・なぜ作るか」の判断は人間の責任
- テスト/検証インフラの設計こそが、Dark Factory成功の鍵

---

## Dark Factory達成の条件

StrongDMとWillisonの観察から抽出:

| 条件 | 説明 |
|---|---|
| **強力なHarness** | Agentの実行環境・ツール統合・ガードレールが必須 |
| **自動テスト網** | プロパティテスト、フォールトインジェクション、E2Eテスト |
| **Digital Twin** | 依存サービスのクローン環境 |
| **Spec-Driven** | 詳細な仕様書がAgentへの唯一の入力 |
| **Proof of Work** | コード自体ではなく、テスト通過・CI成功で品質を証明 |
| **Human System Design** | 人間はシステム設計とパターン発見に集中 |

---

## 5レベルモデルとAgent Team/Swarmの関係

```
Level 1-2: 個人生産性ツール（Copilot, ChatGPT）
Level 3: Harness Engineering（単一Agent + 実行環境）
Level 4: Agent Team / Swarm（複数Agent協調、Symphony/Managed Agents）
Level 5: Dark Factory（完全自律、人間は設計のみ）
```

OpenAI SymphonyとAnthropic Managed AgentsはLevel 4のインフラを提供し、StrongDMの実践はLevel 5への道筋を示している。

---

## Related

- [[agent-team-swarm]] — 複数Agent協調の上位概念
- [[openai-symphony]] — Level 4を実現するオーケストレーター
- [[anthropic-managed-agents]] — Level 4のプラットフォーム基盤
- [[harness-engineering]] — 全レベルの基礎となる実行環境設計

---

## Sources

- [Simon Willison: The Five Levels](https://simonwillison.net/2026/Jan/28/) (2026-01-28)
- [Simon Willison: How StrongDM's AI team build serious software](https://simonwillison.net/2026/Feb/7/software-factory/) (2026-02-07)
- [StrongDM Attractor](https://github.com/strongdm/attractor)
- [StrongDM CXB](https://github.com/strongdm/cxdb)
- [Business Insider: Simon Willison says the 'dark factory' is the next big thing in AI](https://tech.yahoo.com/ai/articles/simon-willison-says-dark-factory-224709005.html) (2026-04-04)
