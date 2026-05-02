---
title: Manus
type: entity
aliases:
- manus-ai
- manus-browser-operator
- monica-im
created: 2026-04-13
updated: 2026-04-13
tags:
  - entity
  - technology
  - browser-agent
  - general-purpose-agent
  - company
- entity
- technology
- browser-agent
- general-purpose-agent
- startup
status: active
sources:
- https://manus.ai/features/manus-browser-operator
- https://chatgptguide.ai/manus-browser-operator-agentic-workflows/
- https://manus.im/blog/manus-browser-operator
- https://www.taskade.com/blog/manus-ai-review
---

# Manus

**Manus**は、元Alibaba/ByteDanceエンジニアらが創業した中国系スタートアップ（Monica.im）が開発した汎用AIエージェント。2025年3月のバイラルデモで注目され、ブラウザ操作・コード実行・ファイル作成を仮想コンピュータ上で自律実行できる。2025年11月には**Browser Operator**機能をリリース、2026年には**Metaに買収**された。

## 概要

| 項目 | 内容 |
|---|---|
| 創業 | 2024年（Monica.im） |
| 創設者 | 元Alibaba/ByteDanceエンジニア |
| 買収 | 2026年、Metaにより |
| バイラルデモ | 2025年3月（フライト予約、コーディング等） |
| アクセス | 招待制（初期）、後に全ユーザー開放 |

## Manus Browser Operator（2025年11月〜）

Manusの最大の差別化は**ローカルブラウザ拡張**によるエージェント実行。クラウドのサンドボックスではなく、ユーザーの実際のブラウザ上で動作する。

### 3ステッププロセス
1. **Connect Browser**: 「My Browser」コネクタを有効化、拡張機能をインストール
2. **Grant Access**: マルチステップタスクの実行許可を付与（ワンタイム認証）
3. **Autonomous Action**: ブラウザ内でタスクを実行、専用タブでリアルタイム監視可能

### 主な特徴
- ✅ **認証済みセッションの利用**: ログイン状態、Cookie、有料ツールのアクセスを継承
- ✅ **ローカルIP**: 信頼された環境からのアクセスとして認識（CAPTCHA回避に有利）
- ✅ **完全な透明性**: 全アクションがログ記録、監査証跡あり
- ✅ **即時中断**: タブを閉じるだけでタスク停止
- ✅ **リモート監視**: メインPCがオンラインであれば、スマホ等からタスク進捗を確認可能

### 得意領域
- **プレミアムデータソース**: Crunchbase, PitchBook, SimilarWeb, Financial Times, Semrush, Ahrefs
- **B2Bデータ分析**: CRM操作、市場調査、SEO分析
- **内部ダッシュボード**: 企業内の認証ツールでの作業

### 制限
- ドラッグ&ドロップ、複雑なマルチステップフォームは未対応
- 永続メモリなし（仮想コンピュータモデルのため）
- センシティブ情報へのアクセスは事前レビューが必要

## アーキテクチャ比較

| 次元 | クラウドブラウザ | Browser Operator（ローカル） |
|---|---|---|
| 実行環境 | 隔離サンドボックス | ユーザーのブラウザ |
| ログイン | 不可（壁にぶつかる） | 継承可能 |
| CAPTCHA | 問題あり | 回避しやすい |
| 有料ツール | アクセス不可 | 契約済みツールを利用可能 |
| 監視 | 限定 | リアルタイム（専用タブ） |
| IP信頼性 | 低い | 高い（ローカルIP） |

## 買収と今後

2026年にMetaによる買収が発表された。「AIをビジネスに普及させる」ための戦略的買収とされる。MetaのAIエージェントエコシステムとの統合が予想される。

## 関連エンティティ

- [[anthropic-computer-use]] — AnthropicのComputer Use
- [[openai-cua]] — OpenAIのComputer-Using Agent
- [[browser-use]] — オープンソースブラウザ自動化
- [[concepts/death-of-browser]] — ブラウザの脱人間化潮流
- [[webmcp]] — 標準化プロトコル

## Sources

- [Manus Browser Operator](https://manus.ai/features/manus-browser-operator)
- [Introducing Manus Browser Operator](https://manus.im/blog/manus-browser-operator)
- [Manus AI Review 2026 (Taskade)](https://www.taskade.com/blog/manus-ai-review)
- [Manus Browser Operator Explained](https://chatgptguide.ai/manus-browser-operator-agentic-workflows/)
