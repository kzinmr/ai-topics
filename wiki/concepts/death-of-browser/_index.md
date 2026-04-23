---
title: "Death of Browser — ブラウザの脱人間化"
aliases:
  - post-browser-era
  - agentic-browser
  - ai-native-browser
  - browser-agent-trends
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - front-page
  - browser-agent
  - synthesis
status: active
---

# Death of Browser — ブラウザの脱人間化

**「ブラウザは人間のUIだった。これからはエージェントのUIになる。」**

30年間、ブラウザは人間がウェブを操作するための唯一のインターフェースだった。しかし2024年後半から2026年にかけて、**ブラウザが「人間向けのウィンドウ」から「AIエージェントの実行環境」へ**とパラダイムシフトしている。この概念ページは、関連プレイヤー、技術アプローチ、トレンドを体系的にまとめたフロントページ。

## パラダイムシフトの3段階

```
Stage 1 (2024)     Stage 2 (2025)         Stage 3 (2026)
─────────────      ──────────────         ──────────────
人間が操作   →    AIが補助   →     AIが代行
（クリック）      （チャット+提案）    （自律実行）
```

| フェーズ | 説明 | 代表例 |
|---|---|---|
| **Human-operated** | 人間がマウス/キーボードで操作 | 従来ブラウザ |
| **AI-assisted** | AIが提案、人間が確認 | Copilot, Arc Max |
| **AI-delegated** | AIが自律的にタスク実行 | Operator, Comet, Manus |

## 主要プレイヤーマップ

### 🏢 ビッグテック

| プレイヤー | 製品 | アプローチ | ステータス |
|---|---|---|---|
| **Anthropic** | Computer Use | スクリーンショット + ビジョン | Claude Sonnet 4.6で大幅改善 |
| **OpenAI** | CUA / Operator | スクリーンショット + RL | ChatGPTエージェント統合 |
| **Google** | WebMCP (Chrome) | 構造化API標準 | Chrome 146で早期プレビュー |
| **Microsoft** | WebMCP (Edge) | 構造化API標準 | W3C共同開発 |
| **Perplexity** | Comet | 検索統合AIブラウザ | 4プラットフォーム対応 |
| **Meta** | Manus（買収） | ローカルブラウザ拡張 | 2026年に買収完了 |

### 🔧 オープンソース・インフラ

| プレイヤー | 製品 | 説明 | GitHub Stars |
|---|---|---|---|
| **browser-use** | browser-use | Python/TS製LLMブラウザ自動化 | 87,300+ |
| **Browserbase** | Stagehand | ホストブラウザインフラ | $300M評価 |
| **Browserless** | BaaS | セキュアブラウザインフラ | 業界レポート公開 |

### 🏢 エンタープライズ

| プレイヤー | 製品 | 焦点 |
|---|---|---|
| **Kahana** | Oasis | 企業向けAIブラウザ（Zero Trust + DLP） |
| **VeloFill** | - | エンタープライズ自動化 |
| **LayerX Security** | - | ブラウザエージェントセキュリティ |

## 技術アプローチの分類

### 1. スクリーンショットベース（Vision-First）
**代表: Anthropic Computer Use, OpenAI CUA**

```
タスク → スクリーンショット → ビジョンモデル解析 → 
座標クリック/入力 → 次のスクリーンショット
```

| 長所 | 短所 |
|---|---|
| 全てのUIに対応可能 | 遅い（画像送信） |
| 動的UIに強い | トークン消費大 |
| 新規サイトでも動作 | 座標精度に課題 |

### 2. DOMベース（Structure-First）
**代表: browser-use, Playwright, Puppeteer**

```
タスク → DOM解析 → 要素特定 → アクション実行
```

| 長所 | 短所 |
|---|---|
| 高速、正確 | 動的UIに弱い |
| トークン消費小 | シャドーDOM/iframeで困難 |
| デバッグ容易 | セレクター維持コスト |

### 3. 構造化プロトコル（Declarative）
**代表: WebMCP, Stagehand**

```
タスク → ツール発見 → 構造化呼び出し → 結果受信
```

| 長所 | 短所 |
|---|---|
| 最も信頼性が高い | ウェブサイト側の実装が必要 |
| 89%トークン削減 | 標準化途上 |
| セキュリティ組み込み | 採用には時間がかかる |

### 4. ハイブリッド（The 2026 Standard）
**代表: ChatGPT Agent, Browserbase Stagehand v3**

```
タスク → DOM優先 → ビジョンフォールバック → 構造化API（利用可能なら）
```

> "The future of browser agents lies not in vision or structure alone, but in orchestrating both intelligently."
> — InfoWorld, November 2025

## 重要トレンド（2026年）

### 1. ブラウザエージェントの標準化
- **WebMCP**: W3Cコミュニティグループ標準、Chrome 146でプレビュー
- **MCP-B**: 非標準ブラウザ向けポリフィル実装
- AnthropicのMCP（サーバー間）とWebMCP（ブラウザ内）は補完関係

### 2. セキュリティ課題の顕在化
- **CometJacking**: AIエージェントへのプロンプトインジェクション
- ブラウザエージェント固有の攻撃ベクターが増加
- Zero Trustアーキテクチャの必要性（Kahana Oasisのアプローチ）

### 3. エンタープライズ導入の加速
- 2026年末までに業務Webトラフィックの25-35%がエージェント生成と予測
- RPAからの移行（RPA 2.0）
- 監査証跡、コンプライアンス要件

### 4. ローカルブラウザ統合
- Manus Browser Operator: ユーザーの認証セッションを活用
- 有料ツール（CRM, SEO, 金融データ）へのアクセスが可能に
- クラウドサンドボックスの限界を克服

### 5. オープンソースエコシステムの成熟
- browser-use: 87k+ stars、310コントリビューター
- TypeScript/Python/Java/Go/Rubyマルチ言語対応
- Claude Codeスキル統合

## 技術比較マトリックス

| 技術 | アプローチ | OSWorld | WebArena | セキュリティ | 標準化 |
|---|---|---|---|---|---|
| Anthropic CU | スクリーンショット | 22.0%+ | 58.1% | ASL-2 | 独自 |
| OpenAI CUA | スクリーンショット + RL | 38.1% | 58.1% | 3層セーフガード | 独自 |
| browser-use | DOM + LLM | N/A | N/A | クラウド/ローカル | OSS |
| WebMCP | 構造化API | N/A | N/A | ブラウザネイティブ | W3C |
| Stagehand | 自然言語コマンド | N/A | N/A | Inspector | OSS |
| Manus | ハイブリッド | N/A | N/A | ローカル認証 | 独自 |
| Comet | 検索統合 | N/A | N/A | CometJacking修正 | 独自 |

## 市場予測

| 指標 | 2025 | 2026予測 |
|---|---|---|
| AIブラウザ市場成長率 | - | 65% YoY |
| エージェント生成トラフィック | <5% | 25-35% |
| browser-use GitHub Stars | 40k | 87k+ |
| WebMCP対応ブラウザ | 1（Chrome Canary） | 2+（Edge追加予定） |

## 定点ウォッチ対象

### 四半期チェック項目
1. **ベンチマーク進化**: OSWorld, WebArena, WebVoyagerスコア
2. **標準化進捗**: WebMCP仕様、W3Cトラック移行、Firefox/Safariシグナル
3. **セキュリティ**: 新規攻撃ベクター、修正パッチ
4. **エコシステム**: オープンソースプロジェクトの成長、M&A動向
5. **エンタープライズ**: 導入事例、コンプライアンスフレームワーク

### 要監視プレイヤー
- **Anthropic**: Computer Use APIの改善、Claude Code統合
- **OpenAI**: CUAモデルのAPI公開範囲、ChatGPT Agent進化
- **Google**: Chrome WebMCP実装、Firefox/Safariの対応状況
- **Microsoft**: Edge WebMCP実装、MCP-Bエコシステム
- **browser-use**: 新機能リリース、クラウド版の成長
- **Perplexity**: Cometの新機能、セキュリティ対応
- **Meta (Manus)**: 買収後の統合、Browser Operatorの進化
- **Kahana Oasis**: エンタープライズブラウザ市場の開拓

## 関連コンセプト

- [[harness-engineering]] — エージェント環境設計
- [[concepts/agentic-engineering.md]] — エージェントを活用したソフトウェア開発
- [[managed-agents-architecture]] — マネージドエージェントアーキテクチャ
- [[concepts/model-context-protocol-mcp.md]] — Model Context Protocol

## 関連エンティティ

- [[anthropic-computer-use]]
- [[openai-cua]]
- [[browser-use]]
- [[browserbase]]
- [[webmcp]]
- [[manus]]
- [[perplexity-comet]]

## Sources

- [When will browser agents do real work? (InfoWorld, Nov 2025)](https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html)
- [AI Browser Agents: The New Automation Layer (Fordel Studios, Mar 2026)](https://fordelstudios.com/research/ai-browser-agents-new-automation-layer-2026)
- [The State of AI & Browser Automation in 2026 (Browserless)](https://www.browserless.io/blog/state-of-ai-browser-automation-2026)
- [Agentic Browsers 101 (Kahana, 2026)](https://kahana.co/blog/agentic-browsers-101-hands-free-web-automation-2026)
- [The Rise of Personal AI Agents and the Death of the Browser (TigerTracks, Feb 2026)](https://tigertracks.ai/insights/the-rise-of-personal-ai-agents-and-the-death-of-the-browser-a-performance-marketing-shift/)
- [Perplexity Comet Analysis (Till Freitag)](https://till-freitag.com/en/blog/perplexity-comet-ai-browser)
