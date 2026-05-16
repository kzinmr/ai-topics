# 🔥 トレンドトピックレポート — 2026-05-16

> データ収集期間: 2026-05-14 ~ 2026-05-16
> Web検索 + ブログRSS + ニュースレター + raw articles 123件を横断分析
> スコアリング基準: 複数ソースでの言及頻度 + 業界インパクト + 新規性

---

## 📊 総評

今日のWiki運用では11:00のアクティブクロールで**SubQ・Baidu Ernie 5.1・IBM Think・DeployCo・ZAYA1-8B**を処理済み。07:40のニュースレターでは**Codex mobile・Apple契約紛争・Cerebras IPO**を更新。
これらに加え、本レポートでは**新たに特定したトレンドトピック8件**を報告する。

---

## 🏆 トップトレンド

### 1. 🥇 Grok Build CLI — xAI初のコーディングエージェント

**重要度: ⭐⭐⭐⭐⭐ | 日付: 2026-05-14 | ソース: xAI公式, Engadget, Bloomberg**

xAIがCLI型コーディングエージェント「Grok Build」のアーリーベータを発表。Claude Code / Codex CLIへの直接的競合製品。

**主要スペック:**
- SuperGrok Heavy購読者($300/月)限定ベータ
- `curl -fsSL https://x.ai/cli/install.sh | bash` でインストール
- **Plan Mode**: コード実行前に段階的プランを提示→承認→実行の3段階フロー
- **並列サブエージェント**: 大規模タスクを自動分割・並列処理
- **ACP (Agent Communication Protocol) 対応**: ボット構築・マルチエージェントオーケストレーション可能
- **Headless Mode** (`-p` フラグ): CI/CDパイプラインで使用可能
- AGENTS.md / plugins / hooks / Skills / MCP Servers と相互運用性あり

**コンテキスト**: 50名以上の研究者がSpaceXAI合併後に離脱したとの報道もある中でのリリース。xAIがコーディング分野での巻き返しを図る。

**→ Wiki未カバー。Grok Buildのエンティティページ作成推奨**

---

### 2. 🥈 Google I/O 2026 — 5/19目前、Gemini 4.0発表か

**重要度: ⭐⭐⭐⭐⭐ | 日付: 2026-05-19 (翌週) | ソース: Mashable, CNET, Android Authority**

**予想発表内容:**
- **Gemini 4.0**: 2M~10M token context window、ネイティブマルチモーダル（転写不要）
- **Android 17 "Adaptive Everywhere"**: Android + ChromeOS + XR 統合プラットフォーム。端末上Gemini Nano API (ModelManager.getModel) をサードパーティ開発者に解放
- **Google初のエージェンティックコーディングツール**: Claude Code / Codex の競合。Firebase Studio + Stitch + MCP ベース
- **Veo 3**: テキスト→ビデオ＋音声生成APIの一般提供
- **Aluminum OS**: AndroidベースデスクトップOS

**見どころ**: Gemini 4.0は「Claude Opus 4.7の議論好き問題」で不満を持つ開発者の奪取を狙う。Compliance Mode搭載の可能性。

---

### 3. 🥉 Notion AI Agent Platform — ワークスペースがエージェントハブに

**重要度: ⭐⭐⭐⭐ | 日付: 2026-05-13 | ソース: TechCrunch, InfoWorld, BetaNews**

Ivan Zhao (CEO) がライブ配信で発表。Notionの歴史的転換点。

**4つの新機能:**
1. **カスタムエージェント拡張**: 2月β公開のCustom Agentsの機能拡張（Rampだけで300+エージェント構築）
2. **外部エージェント連携**: MCP経由で任意の外部AIエージェントをNotionワークスペースに統合
3. **マルチステップ自動化**: 複数データベース横断のワークフロービルダー
4. **開発者プラットフォーム**: REST API + OAuth 2.0 + PAT認証

**成果**: 100万以上のCustom Agentsが顧客により構築済み。Zapier / Make / Airtable対抗。

---

### 4. Anthropic Claude Agent Meter — 全サブスクリプション横断の課金測定

**重要度: ⭐⭐⭐⭐ | 日付: 2026-05-14 | ソース: InfoWorld, Claude Platform**

Claude全サブスクリプション層（Pro/Max/Team/Enterprise）でエージェント使用量測定を開始。

**Claude Managed Agents 課金:**
- **トークン料金**: 標準API料金＋
- **セッション時間**: $0.08/セッション時間（稼働中のみ計測）
- **ツールオーバーヘッド**: bash tool 245 input tokens/コール、Text Editor tool 700 input tokens/コール

**→ WikiのClaude Code/Anthropicページ更新検討**

---

### 5. IBM Bob GA — エンタープライズSDLC全体をカバーするAI開発パートナー

**重要度: ⭐⭐⭐⭐ | 日付: 2026-04-28 (GA) / 5月に再注目 | ソース: IBM Newsroom, The New Stack**

IBMがフルSDLC対応AI開発パートナー「IBM Bob」をGA発表。既に80,000+ IBM従業員が利用中。

**主要機能:**
- **マルチモデルオーケストレーション**: タスクごとにAnthropic Claude/Mistral/IBM Graniteを自動ルーティング
- **Persona-based Agents**: アーキテクト/セキュリティエンジニア/DevOpsなど役割別エージェント
- **Pass-through pricing**: AIコストの可視化（独自仮想通貨「Bobcoins」）
- **成果例**: 30日かかっていたJavaアップグレードを3日で完了（160エンジニア時間削減）
- Neel Sundaresan (GM, GitHub Copilot創設エンジニア) がリーダーシップ

**→ IBMのエンティティページに追記推奨（Think 2026カバレッジにBob追記）**

---

### 6. Meta Avocado — 5月リリースウィンドウ閉塞、依然遅延中

**重要度: ⭐⭐⭐ | 日付: 2026-05-16 | ソース: NYT, TestingCatalog**

Metaの次世代基盤モデル「Avocado」は3月→5月に延期されたが、5月ウィンドウも閉塞しつつある模様。

**ステータス:**
- Avocado 9B / Avocado Mango Agent / Avocado Thinking 5.6 / Paricado など複数バリアント並行テスト中
- Gemini 3やGPT-5に数ヶ月遅れのパフォーマンス
- Alexandr Wang (CAIO) 指揮下でプロプライエタリモデルへの転換議論
- MetaはGeminiライセンスも検討中

**→ Wiki未カバー。Metaエンティティページに追記推奨**

---

### 7. AWS Bedrock Advanced Prompt Optimization — プロンプト最適化の自動化

**重要度: ⭐⭐⭐ | 日付: 2026-05-15 | ソース: InfoWorld, AWS Blog**

AWSがBedrockに Advanced Prompt Optimization ツールを追加。

**機能:**
- ユーザー定義データセットに対してプロンプトを自動評価・最適化
- 最大5つの推論モデルでベンチマーク
- 最適化前後の比較レポート自動生成
- 推論コスト削減と精度向上を同時達成

---

### 8. Spec-Driven Development Tools — Vibe Codingからの進化

**重要度: ⭐⭐⭐ | 日付: 2026-05-15 | ソース: InfoWorld (Martin Heller)**

**4つの最新ツール:**
- **Kiro**: 仕様からコード生成、検証まで
- **Spec Kit**: 型安全な仕様記述
- **Tessl**: テスト仕様駆動開発フレームワーク
- **Zenflow**: エージェント協調による仕様駆動パイプライン

Karpathyの"vibe coding"概念（2025年2月）から1年、業界は「仕様駆動開発」への揺り戻しフェーズ。

---

## 📋 未カバートピック — 今後のWiki作業候補

| トピック | 優先度 | アクション |
|---------|--------|-----------|
| Grok Build CLI (xAI) | 🔴 高 | 新規エンティティページ作成 |
| Notion AI Agent Platform | 🔴 高 | Notion既存ページに追記 or 新規コンセプトページ |
| Google I/O 2026 Preview | 🟡 中 | Googleエンティティ or イベントページ作成 |
| Meta Avocado | 🟡 中 | MetaエンティティにAvocadoセクション追加 |
| IBM Bob | 🟡 中 | IBMエンティティにBobセクション追加 |

---

## 📈 スクリーニングレポート

`scripts/trending_topics.py` 分析結果: 123 articles中27のトレンドトピックを検出

| カテゴリ | トレンド数 |
|---------|-----------|
| Entities | 12 |
| Concepts | 11 |
| People | 4 |

**ホットトピック（4+ソース）:** Claude (26), OpenAI (23), Google (22), Agentic Engineering (14), Simon Willison (13), Evals (13), Anthropic (12), Gemini (11), GPT (9), Coding Agents (9), OpenClaw (7), Sandboxing (7), MCP (6), Meta (5), Cory Doctorow (4), Long Context (4)

**→ これらのトピックにはWikiページが既に存在し、複数ソースで更新中**

---

## 🔗 主要ソース

- [xAI: Introducing Grok Build Early Beta](https://x.ai/news/grok-build-cli)
- [Engadget: xAI introduces its coding agent called Grok Build](https://www.engadget.com/2173482/xai-coding-agent-grok-build/)
- [Mashable: What to expect from Google I/O 2026](https://mashable.com/article/google-io-2026-what-to-expect)
- [InfoWorld: Anthropic puts Claude agents on a meter](https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html)
- [TechCrunch: Notion just turned its workspace into a hub for AI agents](https://techcrunch.com/2026/05/13/notion-just-turned-its-workspace-into-a-hub-for-ai-agents/)
- [BetaNews: Notion wants to be the place where your AI agents live and work](https://betanews.com/article/notion-developer-platform-ai-agents/)
- [IBM Newsroom: Introducing IBM Bob](https://newsroom.ibm.com/2026-04-28-introducing-ibm-bob-ai-development-partner)
- [MLQ AI: Meta postpones Avocado AI model launch](https://mlq.ai/news/meta-postpones-avocado-ai-model-launch-to-may-amid-performance-gaps-with-competitors/)
- [InfoWorld: AWS adds Advanced Prompt Optimization tool to Bedrock](https://www.infoworld.com/article/4171870/aws-adds-advanced-prompt-optimization-tool-to-bedrock.html)
- [InfoWorld: Four cutting-edge tools for spec-driven development](https://www.infoworld.com/article/4171332/four-cutting-edge-tools-for-spec-driven-development.html)

---

*Generated by `trending_topics.py` + web search at 12:00 UTC / 21:00 JST*
