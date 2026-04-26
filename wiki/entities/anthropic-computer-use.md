---
title: Anthropic Computer Use
type: entity
aliases:
- claude-computer-use
- anthropic-cu
- claude-cowork
- vercept-acquisition
created: 2026-04-13
updated: 2026-04-13
tags:
- entity
- technology
- computer-use
- browser-agent
- anthropic
status: active
sources:
- https://www.anthropic.com/news/claude-sonnet-4-6
- https://www.anthropic.com/news/acquires-vercept
- https://techcrunch.com/2026/02/25/anthropic-acquires-vercept-ai-startup-agents-computer-use-founders-investors/
---

# Anthropic Computer Use

**Anthropic Computer Use**は、Claudeモデルがスクリーンショットを見てGUIを直接操作する機能。2024年10月に研究プレビューとして公開され、スクリーン座標へのクリック、キー入力、スクロールなど、人間と同じ方法でコンピュータを操作できる。2026年2月のVercept買収とClaude Sonnet 4.6リリースにより、OSWorldスコアが15%未満から72.5%に飛躍した。

## 概要

| 項目 | 内容 |
|---|---|
| 初回リリース | 2024年10月（研究プレビュー） |
| ベースモデル | Claude Sonnet / Opus |
| アプローチ | スクリーンショットベースのビジョン認識 + 推論 |
| 提供形態 | API + Claude App（Cowork） |
| OSWorldスコア | 14.9% → 72.5%（Sonnet 4.6、2026年2月） |
| WebArenaスコア | 58.1% |
| セキュリティ | ASL-2プロンプトインジェクション耐性 |

## 技術アーキテクチャ

### 認識-行動ループ（Perception-Action Loop）
```
タスク指示 → スクリーンショット取得 → ビジョンモデルがUI要素認識 →
アクション計画（クリック/入力/スクロール） → 実行 →
次のスクリーンショットで状態確認 → 自己修正 → 繰り返し
```

### Claude Sonnet 4.6の改善（2026年2月）
- OSWorld: 15%未満 → **72.5%**（人類レベルに接近）
- 1Mトークンコンテキスト対応
- アダプティブ思考 + 拡張思考（Extended Thinking）
- コンテキスト圧縮（Compaction）ベータ
- Web検索/fetchツールのコード自動生成

### Vercept買収の影響（2026年2月）
AnthropicはSeattleのAIスタートアップ**Vercept**を買収:
- **共同創設者**: Kiana Ehsani（CEO）、Luca Weihs、Ross Girshick
- **Vy製品**: クラウド上のコンピュータ使用エージェント（リモートMacBook操作）
- **専門性**: ビジョンベースのコンピュータ認識と自動化
- **資金調達**: 合計$50M（Fifty YearsのSeth Bannon主導）
- **エンジェル投資家**: Eric Schmidt（元Google CEO）、Demis Hassabis（Google DeepMind CEO）
- **Allen Institute for AI (AI2)**出身
- 買収後、Anthropicのコンピュータ使用研究グループに統合
- 外部製品Vyは2026年3月25日に終了

### セーフガード
- **ASL-2（Anthropic Safety Level 2）**: プロンプトインジェクション耐性
- Sonnet 4.6はSonnet 4.5と比較して大幅改善、Opus 4.6と同レベル
- マルチステップタスクでのエラー修正能力向上

## タイムライン

| 日付 | マイルストーン |
|---|---|
| 2024年10月 | Computer Use研究プレビュー公開 |
| 2025年7月 | OSWorld-Verifiedベンチマークリリース |
| 2026年1月 | Claude Cowork研究プレビュー（コンピュータ使用統合） |
| 2026年2月17日 | Claude Sonnet 4.6リリース（OSWorld 72.5%） |
| 2026年2月25日 | Vercept買収発表 |
| 2026年3月25日 | Vercept Vy製品終了、Anthropicに統合 |

## 得意領域

1. **レガシーソフトウェア**: APIが存在しない専門システムの操作
2. **複数タブ横断タスク**: ブラウザタブ間をまたぐワークフロー
3. **複雑なフォーム入力**: Webフォーム、スプレッドシート操作
4. **自動化不可能なツール**: モダンAPIコネクタがないツールの操作

## 制限と課題

1. **速度**: スクリーンショットの送受信でレイテンシが発生
2. **トークン消費**: 画像ベースのためAPIコストが高い
3. **精密操作**: ドラッグ&ドロップ、複雑なマルチステップフォーム
4. **動的UI**: 頻繁に変更されるインターフェースでの安定性

## OpenAI CUAとの比較

| 次元 | Anthropic Computer Use | OpenAI CUA |
|---|---|---|
| ベースモデル | Claude Sonnet/Opus | GPT-4o + RL |
| OSWorldスコア | **72.5%**（Sonnet 4.6） | 38.1% |
| WebArenaスコア | 58.1% | 58.1% |
| トレーニング | ビジョン認識 + 推論 | 教師あり + 強化学習 |
| セーフガード | ASL-2（プロンプト耐性） | 3層（97%有害拒否） |
| 提供形態 | API + Claude Cowork | ChatGPTエージェント統合 |
| 最新開発 | Vercept買収（2026年2月） | API公開拡大 |

## 関連エンティティ

- [[openai-cua]] — OpenAIのComputer-Using Agent
- [[concepts/death-of-browser]] — ブラウザの脱人間化潮流
- [[browser-use]] — オープンソースDOMベース自動化
- [[concepts/harness-engineering]] — エージェント環境設計
- [[webmcp]] — 標準化プロトコル

## Sources

- [Introducing Claude Sonnet 4.6 (Anthropic, 2026-02-17)](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Anthropic acquires Vercept (Anthropic, 2026-02-25)](https://www.anthropic.com/news/acquires-vercept)
- [Anthropic acquires computer-use AI startup Vercept (TechCrunch)](https://techcrunch.com/2026/02/25/anthropic-acquires-vercept-ai-startup-agents-computer-use-founders-investors/)
- [Claude AI Computer Use: Near-Human Performance (SuperClaude)](https://superclaude.app/en/blog/claude-ai-computer-use-vercept-near-human-performance)
