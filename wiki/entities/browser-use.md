---
title: "browser-use"
aliases:
  - browseruse
  - browser-use-oss
created: 2026-04-13
updated: 2026-04-13
tags:
  - entity
  - technology
  - browser-agent
  - open-source
  - dom-based
status: active
sources:
  - "https://github.com/browser-use/browser-use"
  - "https://browser-use.com"
  - "https://www.fastaijobs.com/companies/browser-use"
---

# browser-use

**browser-use**は、ETH Zurich出身者によって開発されたオープンソースのブラウザ自動化フレームワーク。AIエージェントがPlaywright経由でWebサイトを操作できるようにする。「Make websites accessible for AI agents」をミッションに掲げる。

## 概要

| 項目 | 内容 |
|---|---|
| 創設 | 2024年10月（GitHub） |
| 創設者 | ETH Zurich alumni（MagMuellerら） |
| 本社 | チューリッヒ / サンフランシスコ |
| ライセンス | MIT |
| GitHub Stars | 87,300+ |
| 資金調達 | $17M（Seed） |
| チームサイズ | 1-10名 |
| コントリビューター | 310名 |
| リリース | v0.12.6（2026年4月） |

## 技術スタック

### Python版（メイン）
```python
from browser_use import Agent, Browser, ChatBrowserUse

browser = Browser()  # または use_cloud=True でクラウド版
agent = Agent(
    task="ブラウザでタスクを実行",
    llm=ChatBrowserUse(),  # 最適化済みモデル
    browser=browser,
)
await agent.run()
```

### TypeScript版（npm）
- 2026年2月より提供（v0.6.0）
- Playwrightベース、Node.js >= 18
- 10+ LLMプロバイダー対応（OpenAI, Anthropic, Google Gemini, Azure, AWS Bedrock, Groq, Ollama, DeepSeek, OpenRouter）

### 主要機能
- **act / extract / observe**: 自然言語でのブラウザ操作
- **Cloud版**: ステルスブラウザ、プロキシローテーション、スケーラブル実行
- **Claude Codeスキル**: `~/.claude/skills/browser-use/SKILL.md`で直接統合
- **MCPサーバー**: `npx browser-use --mcp`でClaude Desktopから操作
- **ワークフロー**: `workflow-use`でRPA 2.0パターン
- **macOS-use**: MacアプリのAI操作対応

### ベンチマーク（自社）
- ChatBrowserUse()は平均3-5倍高速（他モデル比）
- 100実世界タスクでのオープンベンチマーク公開

## エコシステム

| リポジトリ | 説明 | Stars |
|---|---|---|
| browser-use | コアPythonライブラリ | 86,454 |
| web-ui | ブラウザ内でAIエージェント実行 | 15,818 |
| workflow-use | RPA 2.0ワークフロー | 3,936 |
| macOS-use | Macアプリ操作 | 1,884 |
| awesome-prompts | プロンプト集 | 904 |
| vibetest-use | 自動QAテスト | 785 |

## DOMベースアプローチの意義

Anthropic/OpenAIのスクリーンショットベースとは対照的に、**DOM構造を直接理解**して操作:
- ✅ 高速、再現性が高い
- ✅ 座標精度が高い
- ❌ 動的UI、Canvas、SPAに弱い
- ❌ CAPTCHA/ログイン壁でブロック

→ 2026年のトレンドは**ハイブリッド**（DOM優先 + ビジョンフォールバック）

## 関連エンティティ

- [[anthropic-computer-use]] — スクリーンショットベースアプローチ
- [[openai-cua]] — OpenAIのComputer-Using Agent
- [[browserbase]] — 信頼性の高いブラウザ自動化インフラ
- [[death-of-browser]] — ブラウザの脱人間化潮流
- [[webmcp]] — 標準化されたエージェント-ブラウザ対話

## Sources

- [GitHub: browser-use/browser-use](https://github.com/browser-use/browser-use)
- [browser-use.com](https://browser-use.com)
- [Browser Use Company Profile](https://www.fastaijobs.com/companies/browser-use)
