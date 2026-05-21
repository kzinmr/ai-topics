---
title: "Trending Topics Report — 2026-05-21"
date: 2026-05-21
author: Hermes (kzinmr's AI Topics)
tags: [report, trending]
sources:
  - https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/
  - https://perplexityaimagazine.com/ai-news/synthid-openai-elevenlabs-nvidia-ai-watermark-standard-2026/
  - https://www.techtimes.com/articles/316901/20260520/gemini-science-launches-peer-reviewed-benchmarks-era-beat-cdc-forecasting-model.htm
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
  - https://developer.chrome.com/blog/devtools-for-agents-v1
  - https://www.techrepublic.com/article/news-google-search-ai-agent-overhaul/
  - https://www.marketingprofs.com/opinions/2026/54655/ai-update-may-8-2026-ai-news-and-views-from-the-past-week
---

# Trending Topics Report — 2026-05-21

## 1. [NJ: 5/5] OpenAI、80年来の未解決Erdős問題を解決 — 今度こそ本物

OpenAIは2026年5月20日、新たな汎用推論モデルがPaul Erdősが1946年に提起した幾何学の未解決予想を反証する独自の数学的証明を生成したと発表した。数学者のNoga Alon、Melanie Wood、Thomas Bloomらが証明を支持する声明を発表。7ヶ月前のGPT-5発表時（Kevin Weilの「10のErdős問題を解決」という虚偽主張）の教訓を活かし、今回は事前に数学界の検証を受けた上での発表。同社は「AIが数学分野の中心的未解決問題を自律解決した初めての事例」と位置づけ、生物学・物理学・工学・医学への応用可能性を示唆。

> 出典: TechCrunch (2026-05-20)

## 2. [NJ: 4/5] SynthID連合が拡大 — OpenAI・ElevenLabs・NvidiaがGoogleの透かし技術を採用

Google I/O 2026で、OpenAI、ElevenLabs、Nvidia、KakaoがGoogleのSynthID（不可視AIコンテンツウォーターマーク）を採用することを発表。ChatGPT、Codex、OpenAI APIで生成された画像に即時適用開始。Googleは同時にSynthIDのテキスト透かし技術をオープンソース化。SynthID検証機能はGoogle SearchとChromeに数週間以内に展開予定。C2PA Content Credentials統合もGeminiアプリから開始。業界横断のコンテンツ発信源標準として最も広範な規模に達した。

> 出典: Perplexity AI Magazine (2026-05-19)

## 3. [NJ: 4/5] Google DeepMind「Gemini for Science」— Nature誌同時掲載2論文で科学的検証

Google I/O 2026で発表されたGemini for Scienceは、Co-ScientistとERA（Empirical Research Assistance）の2つのAIツールを擁し、Nature誌に同日掲載された査読論文で実証された。ERAはCDCの公式CovidHub Ensembleを上回る14のCOVID-19入院予測モデルを生成。バイオインフォマティクスでは40の新規single-cell解析手法を提案し、公開リーダーボードで人間開発手法を凌駕。Science Skillsデータレイヤー（30以上の生命科学データベースに接続）はGitHubとAntigravity上で即日公開。

> 出典: TechTimes / Google Blog (2026-05-19)

## 4. [NJ: 3/5] Google Search、25年ぶりの大規模AI刷新 — 情報エージェント＆カスタムUI

GoogleはI/O 2026でSearchの抜本的再設計を発表。従来の検索ボックスはGemini 3.5 Flashを搭載し、会話型クエリ・ファイルアップロード・Chromeタブ入力に対応。24時間稼働の「情報エージェント」は継続的な監視・アラート機能を提供。さらにAntigravityプラットフォームを活用し、検索結果としてカスタム対話型UI（グラフ・表・シミュレーション）をその場でコード生成する機能を追加。フィットネストラッカーから物件監視まで、ユーザーごとの「ミニアプリ」を動的生成。

> 出典: TechRepublic (2026-05-20)

## 5. [NJ: 3/5] Chrome DevTools for Agents 1.0 安定版リリース — MCPサーバーでAIデバッグ

GoogleはChrome DevTools for Agents 1.0をリリース。AIコーディングエージェントがブラウザのデバッグ情報にアクセス可能に。MCP（Model Context Protocol）サーバー、CLI、Agent Skillsの3つのインターフェースを提供。Lighthouse監査、モバイルエミュレーション、メモリリーク検出、Chrome拡張機能のデバッグをエージェントが自律実行可能。Antigravity 2.0にバンドル済み。

> 出典: Chrome Developers Blog (2026-05-19)

## 6. [NJ: 3/5] Gemini 3.5 Flash GA — エージェント＆コーディング用途に特化

Google I/O 2026で発表。Terminal-Bench 2.1で76.2%、MCP Atlasで83.6%を達成。競合フロンティアモデル比4倍の出力速度。価格は$1.50/$9（入出力/1Mトークン）。Gemini Spark（個人AIエージェント）の基盤モデルとしても採用。Antigravityハーネスとの組み合わせでサブエージェント協調動作に対応。

> 出典: Google AI Blog (2026-05-19)

## カバレッジ状況

- ✅ `events/google-io-2026` — Google I/O 2026全体（本日blog-wiki-ingestで作成）
- ✅ `entities/google` — Google I/O 2026製品テーブル（本日blog-wiki-ingestで強化）
- ✅ `concepts/ai-supply-chain-security` — TanStack攻撃含むサプライチェーンセキュリティ（本日作成）
- ❌ SynthID連合 — Wiki未カバー。entities/synthid または concepts/ai-content-provenance として作成候補
- ❌ OpenAI Erdős問題解決 — Wiki未カバー。concepts/ai-mathematical-discovery として作成候補
- ❌ Gemini for Science (ERA/Co-Scientist) — Wiki未カバー
- ❌ Chrome DevTools for Agents 1.0 — Wiki未カバー
