---
title: "Death of the Browser"
created: 2026-04-13
updated: 2026-04-26
type: concept
tags: [browser-automation, agent, web-infrastructure, cross-cutting]
sources: [raw/articles/crawl-2026-04-26-browser-landscape-2026.md]
---

# Death of the Browser

> "The browser is not going to disappear overnight, but its dominance as the primary interface for the internet is ending."

**概念概要**: ブラウザが人間の視覚的インターフェースから、AIエージェントのアクション実行プラットフォームへと変遷する潮流。Webサイトは「人間に読まれる」ものから「エージェントに操作される」ものへシフトしている。

## Core Thesis

### ブラウザの3つの役割の転換

| 従来のブラウザ | 次世代ブラウザ |
|---|---|
| 人間がWebページを閲覧する窓 | AIエージェントがタスクを実行するランタイム |
| HTML/CSSをレンダリング | DOM理解 + ビジュアル認識 + 構造化ツール |
| ユーザーがクリック・スクロール | エージェントが自律的に対話・操作 |

### なぜ「Death」なのか

1. **認知負荷の限界**: 人間は多数のタブ、ポップアップ、SEOスパムに疲弊
2. **エージェントの台頭**: AIが直接Webを操作できるようになり、人間の仲介が不要に
3. **新しいインタラクションモデル**: 自然言語でタスクを依頼 → エージェントが実行
4. **GEOの登場**: SEOに代わりGenerative Engine Optimization（エージェント向け最適化）が重要に

## Timeline: The Rise of Agentic Browsers

| Date | Milestone | Player |
|---|---|---|
| Oct 2024 | Anthropic Computer Use public beta | Anthropic |
| Nov 2024 | Model Context Protocol (MCP) release | Anthropic |
| Dec 2024 | Project Mariner research prototype | Google |
| Jan 2025 | OpenAI Operator (CUA) launch | OpenAI |
| Jan 2025 | browser-use open source (66.5k+ stars) | ETH Zurich duo |
| Mar 2025 | Nova Act browser automation SDK | Amazon |
| Mar 2025 | Playwright MCP release | Microsoft |
| Apr 2025 | Copilot Studio Computer Use | Microsoft |
| May 2025 | Genspark AI browser (on-device models) | Genspark |
| Jun 2025 | The Browser Company launches Dia | The Browser Company |
| Sep 2025 | Opera Neon agentic browser | Opera |
| Sep 2025 | Atlassian acquires The Browser Company | Atlassian |
| Oct 2025 | OpenAI Atlas browser | OpenAI |
| Nov 2025 | Manus Browser Operator (local browser) | Manus (Meta) |
| Jan 2026 | Chrome Gemini auto browse (all users) | Google |
| Feb 2026 | WebMCP early preview in Chrome 146 | Google + Microsoft (W3C) |
| Mar 2026 | Claude Computer Use Agent (research preview) | Anthropic |
| Feb 2026 | Zero-API-Key Browser Agents (WebGPU + WebLLM) | Open-source community |
| Jan 2026 | Browser Use BU-2.0 (bu-2-0 model) | Browser Use |
| Mar 2026 | Perplexity Comet AI browser | Perplexity |
| Apr 2026 | ChatGPT Atlas (autonomous browsing) | OpenAI |

## 2026年重点ツール

### Browser Use BU-2.0 (Jan 2026)
- **モデル**: `bu-2-0`（`ChatBrowserUse`）
- **特徴**: 構造化出力に特化したエージェント向けブラウザ操作フレームワーク
- **APIキー**: `cloud.browser-use.com` から取得
- **用途**: Webスクレイピング、フォーム操作、ナビゲーション自動化

### Perplexity Comet (Mar 2026)
- **概要**: AI駆動の検索統合ブラウザ。検索結果を直接解釈し、要約を生成
- **特徴**: 従来の検索結果リストを介さず、エージェントが直接コンテンツを処理
- **競合**: ChatGPT Atlas、Google AI Overviews

### ChatGPT Atlas (Apr 2026)
- **概要**: OpenAIの自律型ブラウザエージェント。自然言語で指示 → 直接Web操作
- **特徴**: ChatGPTの会話インターフェースに統合、エージェントが複数ページを横断して情報収集
- **技術**: 複数のAIモデルを協調させてタスクを実行

## 主要プレイヤーと技術スタック

### 1. Vision-Based Computer Use（スクリーン認識型）
- **Anthropic Computer Use**: Claudeがスクリーンショットを見てマウス/キーボード操作
- **OpenAI CUA**: GPT-4oのビジョン + 強化学習によるGUI操作
- 特徴: 既存UIをそのまま利用、セットアップ不要、ただしレイアウト変化に脆弱

### 2. DOM-Based Browser Automation（構造理解型）
- **browser-use**: AIエージェントがDOMを理解してブラウザ操作（66.5k+ GitHub stars）
- **Browserbase/Stagehand**: 信頼性の高いDOMパース + AIアクション
- 特徴: 構造的に正確、再現性が高い、ただし動的UIに弱い

### 3. Hybrid Approach（ハイブリッド型）
- **ChatGPT Agent Mode**: DOM + ビジュアルの組み合わせ
- **Manus Browser Operator**: ローカルブラウザの認証セッションを活用
- 特徴: 両方の長所を組み合わせ、2026年の主流アプローチ

### 4. Protocol Layer（標準化レイヤー）
- **WebMCP (Google + Microsoft, W3C)**: ブラウザが構造化ツールをエージェントに公開
- **Anthropic MCP**: サーバーサイドのツール接続標準
- 特徴: スクレイピング不要、構造化されたエージェント-Web対話

## 技術的課題

### 信頼性
> "Computer-use models are still too slow and unreliable for production at enterprise scale. Even a 1% failure rate is unacceptable." — InfoWorld, 2025

- ビジョンモデル: レンダリング差異、レイテンシ、複雑なレイアウトの解釈に課題
- DOMベース: 動的UI、Canvas、SPAに脆弱
- **解決策**: ハイブリッドアプローチ（DOM優先、ビジョンフォールバック）

### セキュリティ
- エージェントが認証情報にアクセスするリスク
- プロンプトインジェクションの脆弱性
- **解決策**: サンドボックス環境、Human-in-the-loop、ドメイン許可リスト

### 測定と帰属
> "The collapse of cookie-based tracking creates an attribution vacuum." — TigerTracks

- 従来のSEO/トラッキングが機能しない
- エージェント向けコンテンツ最適化（GEO）の必要性
- **解決策**: 機械可読なメタデータ、構造化データの充実

## 未来予測

### 2026年後半
- Chrome/Edgeの標準機能としてエージェント操作が組み込み
- WebMCPがW3C標準化プロセスを進行
- オンデバイスLLM（WebGPU + WebLLM）によるプライバシー重視のブラウザエージェント普及

### 2027年以降
- 「エージェントファースト」なWebサイト設計が標準化
- 構造化ツール公開が「モバイルフレンドリー」に次ぐWeb要件に
- ブラウザとAIアシスタントの境界が完全に消失

## Related Concepts

- [[harness-engineering]] — エージェント環境設計
- [[webmcp]] — ブラウザネイティブのMCP標準
- [[anthropic-computer-use]] — AnthropicのComputer Use API
- [[openai-cua]] — OpenAIのComputer-Using Agent
- [[browser-use]] — オープンソースブラウザ自動化
- [[browserbase]] — 信頼性の高いブラウザ自動化インフラ
- [[manus]] — ローカルブラウザ統合型エージェント

## Sources

- [The Agentic Browser Landscape in 2026](https://nohacks.co/blog/agentic-browser-landscape-2026)
- [When will browser agents do real work? (InfoWorld)](https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html)
- [Zero-API-Key Browser Agents](https://www.agentvsai.com/zero-api-key-browser-agents/)
- [The Rise of Personal AI Agents and the Death of the Browser](https://tigertracks.ai/insights/the-rise-of-personal-ai-agents-and-the-death-of-the-browser-a-performance-marketing-shift/)
- [The browser Is dead, long live the AI Agent (Promethean AI)](https://www.promethean-ai.com/post/the-browser-is-dead-long-live-the-ai-agent)
