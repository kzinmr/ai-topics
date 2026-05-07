---
title: "Hermes Agent Architecture"
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - agentic-engineering
  - architecture
  - harness-engineering
  - ai-agents
  - multi-agent
  - orchestration
  - context-engineering
  - memory-systems
  - coding-agents
sources:
  - raw/articles/2026-05-07_chatgpt-hermes-agent-architecture-deep-dive.md
---

# Hermes Agent Architecture

> **核心定義:** Hermes Agent（v0.9.0）は、`AIAgent` を中心核とし、memory・session search・compression・skill 管理を束ねる **agent-core-first** アーキテクチャを採用する。CLIを単なるインターフェースの一つとして扱い、エージェントランタイムそのものが設計の中心にある。対照的に [[concepts/openclaw-architecture]] は長寿命 Gateway を control plane とする gateway-first 設計をとる。

## 1. Overview — アーキテクチャの位置づけ

Hermes Agent は Nous Research が開発したオープンソースの自己ホスト型 AI エージェントである。アーキテクチャ上の最大の特徴は、**AIAgent クラスが単一の中心核（central core）** として全サブシステムを統合する点にある。これは「ツールを呼べる CLI」ではなく、「持続的に稼働し自己改善するエージェントランタイム」として設計されていることを意味する。

アーキテクチャ哲学を一言で表すなら **capability accumulation system（能力蓄積システム）** である。エージェントは使用されるほどに手続き的知識（skills）と環境記憶（memory）を蓄積し、時間とともに強くなる。これは scope-controlled assistant control plane を志向する OpenClaw とは根本的に異なる設計思想である。詳細な比較は [[comparisons/hermes-vs-openclaw-architecture]] を参照。

公開ドキュメントとソースコード分析（elvis による9時間の並列研究、2026年4月）から、Hermes は built-in learning loop を掲げ、agent-managed skills、pre-compression memory flush、bounded curated memory の3層構造を持つことが確認されている。

## 2. Core Architecture — AIAgent 中心設計

Hermes のアーキテクチャは `AIAgent` クラスを中心核として、以下のサブシステムが放射状に統合される：

```
                    ┌──────────────────┐
                    │   Gateway Layer   │
                    │  (14+ platforms)  │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼────────┐ ┌──▼───┐ ┌───────▼──────┐
     │  Prompt Assembly │ │AIAgent│ │ Provider     │
     │  (cached+ephem.) │ │ CORE │ │ Runtime      │
     └────────┬────────┘ │      │ └──────┬───────┘
              │          └──┬───┘        │
     ┌────────▼────────┐    │    ┌───────▼──────┐
     │  Persistent      │    │    │  Tool         │
     │  State (SQLite)  │    │    │  Runtime      │
     └─────────────────┘    │    └──────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼────────┐ ┌──▼──────┐ ┌─────▼───────┐
     │  Subagent        │ │Skills   │ │ Extension   │
     │  Delegation      │ │Registry │ │ Model       │
     └─────────────────┘ └────────┘ └─────────────┘
```

**3つの API 実行モード:**
- **対話モード（Interactive）:** ユーザーとのリアルタイム対話。Gateway 経由でメッセージを受信し、AIAgent が応答を生成。
- **Cron モード（Scheduled）:** natural-language cron による定期実行。毎朝の GitHub スキャン要約など、無監視での自律実行。
- **Watchdog モード（Reactive）:** 外部イベントや他エージェントの障害を検知して自動介入。例：OpenClaw の監視に Hermes を配置し、障害検知→15秒以内に自動復旧。

**コールバックサーフェス** は各サブシステムが AIAgent コアにイベントを通知する仕組みで構成され、tool execution completion、skill creation trigger、memory flush signal、gateway message arrival などのライフサイクルイベントを処理する。

## 3. Agent Loop — ターンライフサイクル

Hermes のエージェントループは [[concepts/agent-loop-orchestration|標準的なReActパターン]] を拡張し、以下の特徴を持つ：

**ターンライフサイクル:**
1. **コンテキスト収集:** キャッシュ済みシステムプロンプト + エフェメラルレイヤー（最新メッセージ、ツール結果）を組み立て
2. **推論:** LLM が次のアクション（テキスト応答 or tool_call）を決定
3. **ツール実行:** 最大並列度で複数ツールを同時実行可能
4. **結果評価:** ツール出力をコンテキストに追加し、継続 or 停止を判定
5. **反復:** イテレーション予算（デフォルト上限）内でループ

**割り込み可能な呼び出し（Interruptible Calls）:** 長時間実行ツールは Gateway 経由のユーザー介入（approve/reject/abort）で中断可能。cron モードでは事前承認ポリシーに従う。

**ツール実行並列性:** 独立したツール呼び出し（例：複数ファイルの同時読み取り、並列 Web 検索）は単一ターン内で並列実行され、レイテンシを最小化する。

**イテレーション予算:** 無限ループ防止のため、1タスクあたりの最大ツール呼び出し回数に上限が設定される。複雑なタスク（5+ tool calls）完了時には自動スキル生成トリガーが発火する。

## 4. Prompt Assembly — キャッシュとエフェメラルレイヤー

プロンプト組み立ては **キャッシュ対応設計（cache-aware design）** を採用し、トークンコストを最小化する：

**アセンブリ順序（上から下へ）:**
1. **キャッシュ層（Cached / Deterministic）:**
   - `SOUL.md` — エージェントのペルソナ・行動指針（ほぼ不変）
   - System prompt コア — ツール定義、基本指示（バージョン間で安定）
2. **セッション固定層（Session-stable）:**
   - `MEMORY.md` — 環境事実、規約、蓄積された経験
   - `USER.md` — ユーザー設定、通信スタイル、期待値
   - Project context files — プロジェクト固有のコンテキスト
3. **エフェメラル層（Ephemeral / Turn-variable）:**
   - 直近の会話履歴（bounded window）
   - 最新ツール実行結果
   - アクティブな skill 本文（progressive disclosure: 必要な時のみ全本文をロード）

**キャッシュ設計の要点:** キャッシュ層とセッション固定層はプロバイダAPIのプロンプトキャッシュ機能を活用し、ターン間で再送信コストを削減する。エフェメラル層のみが毎ターン変化する。skill 本文は基本的に name/description のみがプロンプトに入り、全文は `read` ツールで必要時に取得する（progressive disclosure）。

## 5. Persistent State — セッションDB と JSONL トランスクリプト

Hermes の永続状態管理は **bounded memory** 哲学に基づく：

**セッションデータベース（SQLite + FTS5）:**
- 全会話履歴をローカル SQLite に保存
- FTS5（Full-Text Search 5）による全文検索が可能
- 過去の会話を検索・要約・取得して現在のコンテキストに注入可能

**JSONL トランスクリプト:**
- 人間可読・機械可読なトランスクリプトを JSONL 形式で併記
- デバッグ・監査・外部ツール連携に使用

**Bounded Memory の設計:**
- `MEMORY.md` と `USER.md` の2つのコアメモリファイルが全セッションで frozen snapshot としてロードされる
- メモリは無制限に膨張せず、pre-compression flush によって重要な情報のみが保持される
- コンテキスト圧縮時にメモリがフラッシュされ、新たなスキル生成やメモリ更新のトリガーとなる

**外部メモリプロバイダ:**
- Honcho integration（オプション）による拡張メモリバックエンド
- プラグイン機構を通じて追加の memory/context provider を接続可能

[[concepts/ai-memory-systems|AIメモリシステムの設計哲学比較]]も参照。

## 6. Tool Runtime — 自己登録型レジストリ

**ツールレジストリ:**
- 自己登録型（self-registering）: ツール定義が宣言されると自動的にレジストリに登録される
- MCP（Model Context Protocol）サポートにより外部ツールサーバーと統合
- ツールセット管理: アクティブなツールセットをセッション/プロファイルごとに切り替え可能

**承認フロー（Approval Flow）:**
- 破壊的操作（ファイル削除、外部API呼び出し、コード実行）はユーザー承認が必要
- Gateway 経由で approve/reject/always-approve の3択を提示
- cron モードでは事前定義された承認ポリシーに従う

**ターミナルバックエンド:**
- 永続的なマシンアクセス（persistent machine access）
- 複数のターミナルセッションを並行管理
- サブエージェントごとに独立したターミナル環境

## 7. Subagent Delegation vs execute_code

Hermes は2つの異なる実行プリミティブを提供する：

**Subagent Delegation（サブエージェント委任）:**
- メインエージェントが独立した子エージェント（child agents）を起動
- 各サブエージェントは隔離されたコンテキストとターミナルセッションを持つ
- 複数サブエージェントの並列実行が可能
- 親エージェントは結果を集約して統合
- 用途: 大規模タスクの分解、独立した調査、並列コード生成

**execute_code:**
- 単一のコードブロックを現在のセッションコンテキストで直接実行
- サブエージェント起動のオーバーヘッドなし
- 用途: 小規模な計算、データ変換、クイックスクリプト

**選択基準:**
| 特性 | Subagent | execute_code |
|------|----------|-------------|
| コンテキスト | 隔離（blank-slate） | 親セッション共有 |
| 並列性 | マルチエージェント並列 | 単一実行 |
| オーバーヘッド | 高い | 低い |
| 適するタスク | 複雑・独立・大規模 | 単純・依存的・小規模 |

## 8. Gateway Layer — ロングランニングプロセス

**Gateway の役割:**
Hermes は単一の長寿命 Gateway プロセスを通じて外部と通信する。このプロセスは 24/7 で稼働し、複数プラットフォームからのメッセージを統一的に処理する。

**14+ プラットフォーム統合:**
- Telegram, Discord, Slack, WhatsApp, Signal, Email
- Web UI, CLI, HTTP API
- その他 5+ プラットフォーム

**メッセージフロー:**
```
[User on Telegram] → Gateway → AIAgent Loop → Tool Execution → Gateway → [Response to Telegram]
                                   ↓
                            [Cron Trigger] → Gateway → AIAgent Loop → ...
```

**2レベルガード（Two-Level Guard）:**
1. **Gateway レベル:** メッセージ認証、レート制限、プラットフォーム固有の検証
2. **AIAgent レベル:** ツール実行前の承認チェック、破壊的操作のガード

この2層構造により、プラットフォームレベルのセキュリティとエージェントレベルのアクション制御が分離される。

## 9. Provider Runtime — 共有リゾルバとフォールバック

**共有リゾルバ（Shared Resolver）:**
- 複数のLLMプロバイダ（OpenAI, Anthropic, Google, ローカルモデル等）を統一的に扱う抽象化レイヤー
- プロバイダ固有のAPI差異を吸収

**Auxiliary Task Model Routing（補助タスクモデルルーティング）:**
- メインタスク（複雑な推論・コード生成）には高能力モデルを使用
- 補助タスク（要約、分類、軽量な判定）には軽量モデルにルーティング
- コスト最適化とレイテンシ低減が目的

**フォールバック機構:**
- プライマリプロバイダ障害時に自動フォールバック
- プロバイダごとのレート制限・クォータ管理
- ローカルモデル（Ollama 経由）へのフォールバックもサポート

## 10. Extension Model — プラグイン・フック・プロバイダ

**プラグイン機構:**
- `~/.hermes/` ディレクトリ下の設定で拡張を管理
- サードパーティ製プラグインのインストールが可能

**フック（Hooks）:**
- エージェントライフサイクルの各段階にフック可能
- 主なフックポイント: pre-prompt assembly, post-tool execution, pre-memory flush, post-skill creation

**Memory/Context Providers:**
- 外部メモリバックエンド（Honcho 等）を接続するプロバイダインターフェース
- カスタムコンテキストプロバイダによる追加コンテキスト注入
- [[concepts/context-engineering|コンテキストエンジニアリング]] の拡張ポイント

## 11. Key Architectural Characteristics — 4つの定義的特性

**1. Agent-Core-First（エージェントコア優先）:**
AIAgent が設計の中心。CLI はインターフェースの一つに過ぎない。Gateway-first の OpenClaw とは対照的。

**2. Capability Accumulation（能力蓄積）:**
使用されるほど強くなるシステム。タスク成功後に自動スキル生成、エラー回復後に手続き的知識を patch-in-place、ユーザー修正を学習。静的ツールセットではなく、成長する手続き的記憶。

**3. Bundled-by-Default（初期装備充実）:**
123+ の bundled/optional skills catalog。blank framework ではなく、最初からかなり完成したエージェント。Rails スタイルの「opinionated defaults」。

**4. Self-Improving Loop（自己改善ループ）:**
プロンプトナッジ（N tool calls ごとにスキル保存を促す）→ バックグラウンドレビュー（タスク完了後にスキャン）→ pre-compression flush（コンテキスト圧縮前に保存）→ blunt rule（既存スキルがあれば修正、なければ新規作成）の4段階。

## 12. Trade-offs — アーキテクチャ上のトレードオフ

**コア複雑性（Core Complexity）:**
AIAgent 中心設計はすべてのサブシステムがコアに依存する密結合構造を生む。OpenClaw の Gateway を中心とした疎結合設計と比較して、内部の依存関係が複雑になりやすい。

**メモリ即時性 vs 一貫性（Memory Immediacy vs Consistency）:**
bounded memory（`MEMORY.md` + `USER.md`）は即座に利用可能だが、更新には pre-compression flush を待つ必要がある。リアルタイムのメモリ更新と一貫性のトレードオフが存在する。

**サブエージェント blank-slate 問題:**
サブエージェントは隔離されたコンテキストで起動するため、親の記憶や学習したスキルを引き継がない。これは意図的な設計（独立性の保証）だが、知識の伝達には追加のオーバーヘッドが生じる。

**Skill Explosion 問題:**
[[concepts/openclaw-architecture]] と異なり、Hermes の自己生成スキルは `~/.hermes/skills/` に蓄積され続ける。長期運用では taxonomy・dedupe・メトリクスが必要になる構造的課題を抱える。もっとも、progressive disclosure によりフルスキル本文は必要な時のみ読み込まれるため、即座にプロンプトトークンが破綻するわけではない。これは **discoverability と corpus governance の問題** である。

## 13. Code Reading Order — 推奨探索パス

Hermes Agent のコードベースを理解するための推奨探索順序（v0.9.0 時点）：

1. **`AIAgent` クラス（エントリポイント）:** コアの初期化と全サブシステムのワイヤリングを把握
2. **Agent Loop（`loop/` or `agent/loop`）:** ターンライフサイクル、ツール実行、イテレーション制御
3. **Prompt Assembly（`prompt/` or `context/`）:** キャッシュ戦略、レイヤー構造、プログレッシブディスクロージャー
4. **Persistent State（`memory/` or `session/`）:** SQLite+FTS5 スキーマ、JSONL トランスクリプト、メモリフラッシュ
5. **Tool Runtime（`tools/`）:** 自己登録レジストリ、MCP 統合、承認フロー
6. **Skills System（`skills/`）:** スキル生成・更新・削除のライフサイクル、フォールバック/要求機構
7. **Gateway Layer（`gateway/`）:** マルチプラットフォームメッセージルーティング、2レベルガード
8. **Provider Runtime（`providers/`）:** 共有リゾルバ、モデルルーティング、フォールバック
9. **Subagent / Sandbox（`subagents/` or `exec/`）:** サブエージェント委任とコード実行の分離
10. **Extensions（`plugins/` or `hooks/`）:** 拡張ポイントと外部プロバイダ統合

## 14. References

- [Hermes Agent — Agent Loop Internals (公式ドキュメント)](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)
- [Hermes Agent — Skills System (公式ドキュメント)](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [GitHub — NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
- [[entities/hermes-agent]] — Hermes Agent エンティティページ（機能・使用例・3層モデル）
- [[comparisons/hermes-vs-openclaw-architecture]] — Hermes vs OpenClaw アーキテクチャ比較
- [[concepts/openclaw-architecture]] — OpenClaw アーキテクチャ詳細（Hermes の agent-core-first との対比）
- [[concepts/openclaw/_index]] — OpenClaw コンセプトクラスターインデックス
- [[concepts/agent-loop-orchestration]] — エージェントループオーケストレーションの一般的パターン
- [[concepts/agent-harness-primitives]] — エージェントハーネスの6つの基本プリミティブ
- [[concepts/ai-memory-systems]] — AIメモリシステムの設計哲学比較（OpenAI/Anthropic/Cognition）
- [[concepts/context-engineering]] — コンテキストエンジニアリングの体系的アプローチ
