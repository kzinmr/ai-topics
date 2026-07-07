# 🔥 トレンドトピックレポート — 2026-06-04

> **分析期間:** 2026-06-01 → 2026-06-04
> **ソース:** blogwatcher DB 120記事 + raw articles 129件 + RSSスキャン

---

## 1️⃣ 🏗️ **Microsoft MAI: 1Tパラメータ完全スクラッチモデルの衝撃**

**関連ソース:** Simon Willison (simonwillison.net), Elie Bakouch (X megathread 1.5K likes), LWN.net

Microsoftが**MAIシリーズ**の詳細なtech reportを公開。1Tパラメータ・35B activeの超大規模モデルながら、**ゼロ合成データ・ゼロ蒸留**で完全スクラッチから学習された点が最大の特徴。推論能力・エージェント的行動・ツール使用をすべてpost-trainingで獲得しており、フロンティアラボとしての本気度を示している。

主要設計選択:
- Dense層とMoE層の**交互配置**（Llama 4以来の手法、Shared Expertを不要に）
- Local/Global Sliding Window Attention（window size 512、5:1比）
- LatentMoE採用
- 33.5Tトークンで学習（30T pre-training + 3.55T mid-training）
- 全学習イテレーションのMFUを公開する異例の透明性

> Simon Willison: "Microsoft's new MAI models" — https://simonwillison.net/2026/Jun/2/microsofts-new-models/
> Elie Bakouch deep dive: https://x.com/eliebakouch/status/2061965825037254947

**Wikiアクション:** Microsoft MAIのエンティティページ作成または `entities/microsoft.md` 更新。モデル設計の革新（Dense/MoE交互配置）は `concepts/moe.md` にも反映。

---

## 2️⃣ 🧬 **OpenAI GPT-Rosalind 新機能 + ライフサイエンスAIの本格展開**

**関連ソース:** OpenAI Blog, Simon Willison

OpenAIがGPT-Rosalindシリーズに**3つの新機能**を追加:
1. **LifeSciBench** — 外部専門家評価によるエンドツーエンド生命科学研究ベンチマーク（エビデンス処理、分析、分子設計、科学的推論、実験室検証、成果伝達の6領域）
2. **MedChemBench** — GPT-Rosalind 27.5% vs GPT-5.5 25.1%（7%少ないトークンで上回る）
3. **LabWorkBench** — 実際のウェットラボ実験プロトコル評価で63.2% vs 55.8%

加えて、**Life Sciences Research / NGS Analysis** の2つのCodexプラグインを発表。Novo Nordiskとの提携やRosalind Biodefenseプログラムにより、バイオセキュリティ分野への応用も加速。

> OpenAI: "Introducing new capabilities to GPT-Rosalind" — https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind

**Wikiアクション:** `entities/gpt-rosalind.md` 作成（既存の `entities/openai.md` からの参照も）

---

## 3️⃣ 🛠️ **Codex for Every Role: ロール別プラグイン+ Sites機能**

**関連ソース:** OpenAI Blog, Merge Blog, Augment Code Blog

OpenAIがCodexに**6つのロール特化プラグイン**を投入（データ分析、クリエイティブプロダクション、プロダクトデザイン、営業、株式投資、投資銀行）。62のアプリ連携と110のスキルをバンドル。さらに**Sites機能**（インタラクティブなWebアプリをCodex内で生成・共有）もプレビュー開始。

同時期にMerge Devは**Google Slides/Sheets/DriveのMCP+Codex連携ガイド**を3本立て続けに公開。エンタープライズでのCodex+MCP活用が急速に標準化しつつある。

> OpenAI: "Codex for Every Role, Tool, and Workflow" — https://openai.com/index/codex-for-every-role-tool-workflow/
> Merge Blog: "How to connect a Google Slides MCP with Codex" — https://www.merge.dev/blog/google-slides-mcp-codex

**Wikiアクション:** `entities/codex.md` 更新（最新プラグイン情報）、`concepts/mcp.md` にMerge連携事例を追加

---

## 4️⃣ 🔀 **Devin Desktop（Windsurfリブランド）+ ACPによるAgent-Neutral革命**

**関連ソース:** Cognition AI Blog, Devin Docs, X (@windsurf)

Cognition AIが2025年7月に$250Mで買収したWindsurfを**Devin Desktop**にリブランド。最大の革新は**ACP（Agent Client Protocol）** 対応によるAgent-Neutralハーネススワッピング — Devin, Claude Code, カスタムエージェントを同一UIから利用可能に。

「エージェントコマンドセンター」として、マルチエージェントセッション管理、リアルタイムモニタリング（ターミナル/ファイル変更/ブラウザ活動/コード差分）、永続的Spaces（共有コンテキスト＋メモリ＋タスク履歴）、かんばんビューによるワークフロー管理を提供。

> Devin Blog: "Windsurf is now Devin Desktop" — https://devin.ai/blog/windsurf-is-now-devin-desktop
> ACP docs: https://docs.devin.ai/desktop/acp

**Wikiアクション:** `entities/windsurf.md` 作成完了（本日時点で未作成なら即時）、`entities/cognition.md` 更新。ACPプロトコルは `concepts/agent-communication-protocols.md` と比較ページ要。

---

## 5️⃣ 🔄 **動的ワークフローの台頭: Claude Code Workflows + LangChain Rubrics**

**関連ソース:** trq212 (X Article), LangChain Blog, Claude Code Docs

Anthropic Claude Codeの**Dynamic Workflows**（エージェントが実行ハーネスをタスクに応じて動的に生成）と、LangChain Deep Agentsの**RubricMiddleware**（エージェント自己評価・反復改善ループ）が同時期に登場。

trq212の解説記事が示すユースケースの幅広さが注目を集めている: フレーキーテストの自動再現、過去セッションからのルールマイニング、Slackインシデント分析、履歴書ランキング、CLIツール名のトーナメント選定など。

LangChain RubricMiddlewareは専用graderサブエージェントが出力を評価、基準未達の場合はフィードバックを注入して再実行。Claude Codeの `/goal` やCodexと類似するが、より柔軟な評価機構を持つ。

> trq212: "A harness for every task" — https://x.com/trq212/status/2061907337154367865
> LangChain: "Introducing Rubrics" — https://x.com/i/article/2061868304654864384

**Wikiアクション:** `entities/claude-code--capabilities.md` 更新（Dynamic Workflowsセクション追加）、`entities/langchain.md` 更新（Deep Agents + RubricMiddleware）

---

## 6️⃣ 🔍 **Perplexity Search as Code (SaC): 検索をコード生成として再定義**

**関連ソース:** Perplexity Research Blog

Perplexityが**Search as Code (SaC)** を発表 — モノリシックな検索APIを、SDKとして露出された合成可能なプリミティブに分解。エージェントがPythonコードを生成して検索・ランキング・フィルタリング・ファンアウト・集約を直接制御する。

ベンチマーク結果: DSQA 0.871, BrowseComp 0.805, WideSearch 0.651, WANDR 0.386（全ベンチマーク4/5でSOTA、WANDRでは次点の2.5倍）。CVEベンダー勧告タスクではトークン消費が288.7K→42.9Kに削減（85.1%減）。

従来のfixed search()関数呼び出しを、コード生成による直接制御に置き換えることで、関数呼び出しのオーバーヘッドを排除し、非同期制御フロー（ファンアウト、並列フェッチ、重複除去）を単一推論ターン内で実現。

> Perplexity: "Rethinking Search as Code Generation" — https://research.perplexity.ai/articles/rethinking-search-as-code-generation

**Wikiアクション:** `entities/perplexity.md` 更新（SaCセクション追加）、`concepts/agentic-search.md` または新規 `concepts/search-as-code.md` 作成を検討

---

## 7️⃣ 🚀 **Augment Code Cosmos: IDEを超えた「AIネイティブ開発チーム」OS**

**関連ソース:** Augment Code Blog

Augment Codeが**Cosmos**を発表 — 従来のIDE型コード補完から、**SDLC全体をエージェント化するプラットフォーム**へと大胆に転換。エージェントチームによる協調作業、共有ファイルシステム＋メモリ、MCP・Webhook統合、マルチ環境実行（クラウド/セルフホスト/ローカル）を特徴とする。

「エージェントのためのエージェント」というメタ設計もユニーク — Cosmos自身がCosmos上で動作し、ユーザーが自然言語で新しい自動化を記述すると自動的にワークフローを構築する。

> Augment Code: "Hello, Cosmos" — https://augmentcode.com/blog/cosmos-the-platform-for-ai-native-engineering-teams

**Wikiアクション:** `entities/augment-code.md` 作成（現時点で未作成の場合）

---

## 8️⃣ 📚 **エージェントエンジニアリング実践知の急増 — コミュニティ知の爆発的蓄積**

**関連ソース:** mvanhorn (X Article), Sean Goedecke, Harvey AI, Merge Blog, LangChain

以下のような実践的知見の「総合格闘技」的な蓄積が顕著:

- **mvanhorn**「Every Agentic Engineering Hack I Know」— 913Kビューを記録した先月の投稿の続編。Compound Engineeringプラグインによる `/ce-plan` / `/ce-work` ワークフロー、plan.md駆動開発の実践ルール
- **Sean Goedecke**「Weird projects I shipped with AI」「Anti-AI nostalgia and the cult of the past」— AIツールで実際に出荷したプロダクト経験談
- **Harvey AI**「Why we built our own cloud agent infrastructure」— 法律AI企業による自前エージェント基盤構築の理由
- **Merge Dev**のMCP+Codex連携シリーズ（Slides/Sheets/Drive）×3本

> mvanhorn: "Every Agentic Engineering Hack I Know" — https://x.com/i/article/2061440101411102721
> Sean Goedecke: "Weird projects I shipped with AI" — https://seangoedecke.com/weird-projects-i-shipped-with-ai/

**Wikiアクション:** `concepts/agentic-engineering.md` 更新（mvanhornの実践知、Compound Engineering）、`entities/mvanhorn.md` 作成

---

## 📊 ウィクション推奨アクション

| トピック | 強度 | アクション |
|---------|------|-----------|
| Microsoft MAI 1Tモデル | ★★★★★ | `entities/microsoft.md` 更新 → MAIモデルセクション追加 |
| GPT-Rosalind新機能 | ★★★★★ | `entities/gpt-rosalind.md` 新規作成 |
| Codexロール別プラグイン | ★★★★ | `entities/codex.md` 更新（プラグイン一覧+Sites機能） |
| Devin Desktop + ACP | ★★★★ | `entities/windsurf.md` 作成 or `entities/cognition.md` 更新 |
| Claude Code Dynamic Workflows | ★★★★ | `entities/claude-code--capabilities.md` 更新 |
| Search as Code (SaC) | ★★★★ | `concepts/search-as-code.md` 新規作成 or `entities/perplexity.md` 更新 |
| Augment Code Cosmos | ★★★ | `entities/augment-code.md` 新規作成 |
| Agentic Engineering実践知 | ★★★ | `concepts/agentic-engineering.md` 更新 + `entities/mvanhorn.md` 作成 |

---

*生成: Hermes Trending Topics Agent | 2026-06-04 12:00 UTC*
