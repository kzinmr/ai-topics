---
title: "Agent Memory Systems Comparison — OpenClaw vs Claude Code vs Codex"
type: concept
aliases:
  - agent-memory-systems-comparison
  - harness-memory-comparison
created: 2026-05-17
updated: 2026-05-17
tags:
  - concept
  - memory-systems
  - agent-architecture
  - context-engineering
  - comparison
sources:
  - https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive
  - https://mem0.ai/blog/how-memory-works-in-codex-cli
  - https://ianlpaterson.com/blog/claude-code-memory-architecture/
  - https://www.buildfastwithai.com/blogs/claude-managed-agents-memory-2026
  - https://code.claude.com/docs/en/memory
---

# Agent Memory Systems Comparison — OpenClaw vs Claude Code vs Codex

3つの主要コーディングエージェントハーネスにおけるメモリ（記憶）システムのアーキテクチャ比較。全ハーネスが **Markdownファイルベース** のメモリ戦略を取っている点が最も重要な共通項だが、検索方式・埋め込み戦略・コンテキスト保持のアプローチは大きく異なる。

---

## 共通項: ファイルファースト哲学

3ハーネスすべてが「**ファイルこそが唯一の真実源（source of truth）**」という設計哲学を共有している:

| ハーネス | プライマリストレージ | 読み取り可能？ | バージョン管理可能？ |
|---|---|---|---|
| **OpenClaw** | `memory/*.md`, `MEMORY.md`, `sessions/*.md` | ✅ 人間可読Markdown | ✅ git管理可能 |
| **Claude Code** | `CLAUDE.md`, `MEMORY.md`, `.claude/rules/*.md`, auto-memory dir | ✅ 人間可読Markdown | ✅ git管理可能 |
| **Codex CLI** | `~/.codex/memories/*.md`, `AGENTS.md` | ✅ 人間可読Markdown | ✅ AGENTS.mdのみgit共有可能 |

この共通哲学は **AIエージェントメモリの「Bitter Lesson」的収束** を示唆する — 複雑な検索アーキテクチャより、シンプルで人間可読・監査可能なファイルの方が長期的に勝つ。

---

## アーキテクチャ比較

### メモリ階層

| 階層 | OpenClaw | Claude Code | Codex CLI |
|---|---|---|---|
| **静的指示** | なし（system promptで代替） | `CLAUDE.md` (Global → Project → `.claude/rules/*.md`) | `AGENTS.md` (Global → Project walk → Override, 最大32KiB) |
| **永続メモリ** | `MEMORY.md`（プライベートセッションのみ） | `MEMORY.md`（常時読み込み） + auto-memory dir | `~/.codex/memories/MEMORY.md` |
| **日次/一時メモリ** | `memory/YYYY-MM-DD.md`（今日+昨日読み込み） | なし（セッション内コンテキストのみ） | `rollout_summaries/<slug>.md`（セッションごと） |
| **会話履歴** | `sessions/YYYY-MM-DD-<slug>.md`（全文検索・インデックス可） | CLAUDE.md経由で間接参照 | `memory_summary.md`（要約のみ） |

### 検索・リコール方式

| 方式 | OpenClaw | Claude Code | Codex CLI |
|---|---|---|---|
| **ベクトル検索** | ✅ sqlite-vec + コサイン類似度 | ❌ | ❌ |
| **全文検索** | ✅ SQLite FTS5 (BM25) | ❌（ファイル直接読み込み） | ✅ `grep` ベース（MEMORY.mdをgrep） |
| **ハイブリッド** | ✅ BM25 + ベクトル（70:30重み付け） | ❌ | ❌ |
| **リコール方法** | `memory_search` ツール（~700文字スニペット + 関連度スコア） | ファイル全体読み込み | `memory_summary.md` 全体読み込み → 必要に応じて `grep` |

**最大の差異**: OpenClawだけがベクトル検索を実装している。Claude CodeとCodexはファイル自体をコンテキストに読み込むシンプルなアプローチ。OpenClawはより高度だが複雑。

### 埋め込み戦略

| 項目 | OpenClaw | Claude Code | Codex CLI |
|---|---|---|---|
| **埋め込み使用** | ✅ あり（検索用） | ❌ なし | ❌ なし |
| **プロバイダー** | Local → OpenAI → Gemini 自動フォールバック | N/A | N/A |
| **キャッシュ** | ✅ SHA-256ハッシュベース | N/A | N/A |
| **バッチ最適化** | ✅ OpenAI/Gemini Batch API（50%コスト削減） | N/A | N/A |

### メモリ生成・更新

| 項目 | OpenClaw | Claude Code | Codex CLI |
|---|---|---|---|
| **生成タイミング** | Pre-compaction flush（自動） + ユーザー指示 | ユーザー指示 / CLAUDE.md手動更新 | 非同期バックグラウンド（~6時間のアイドル後） |
| **生成モデル** | 実行中のエージェントモデル | 実行中のエージェントモデル | 専用の抽出モデル + 統合モデル（独立設定可） |
| **自動要約** | ✅ コンパクション時に自動発動 | ❌ 手動指示のみ | ✅ セッション要約 → 定期的統合 |
| **ロールアウト上限** | 制限なし（ファイルシステム容量依存） | 制限なし（ファイルシステム容量依存） | 256ロールアウト上限 / 30日未使用→削除 |
| **機密情報除去** | ❌ | ❌ | ✅ 組み込みクレデンシャルスクラビング |

### コンテキスト保持・コンパクション

| 項目 | OpenClaw | Claude Code | Codex CLI |
|---|---|---|---|
| **コンパクション前フラッシュ** | ✅ 自動（~80%コンテキスト使用時、サイレントターン） | ❌（5層コンパクションパイプラインだが事前フラッシュなし） | ❌（非同期生成のため直接関係なし） |
| **コンパクション方式** | Markdown要約を `memory/` に追記 | 5層パイプライン（段階的要約） | 抽出→統合の2フェーズパイプライン |
| **コンテキスト注入** | 今日+昨日の日次ログ + 検索結果 | CLAUDE.md + MEMORY.md を毎セッション注入 | `memory_summary.md` を毎セッション注入（トークン切り詰め） |

---

## 選択ガイド: どのメモリシステムを選ぶべきか

### OpenClaw が最適なケース

- **長期稼働エージェント**: 日次ログ + セッション履歴の自動蓄積で数ヶ月のプロジェクトに最適
- **高度な検索が必要**: ベクトル検索で概念マッチ、BM25で正確な用語検索
- **オフライン要件**: Local埋め込みプロバイダーで完全オフライン動作
- **マルチエージェント**: Per-agent isolation でエージェント間のメモリ汚染防止

### Claude Code が最適なケース

- **チーム開発**: CLAUDE.mdをgit管理し、チーム全体でメモリ共有
- **シンプルさ重視**: ファイル直接読み込みで複雑な検索インフラ不要
- **セッション単位の作業**: 長期間より単一タスクの集中実行に向く
- **エンタープライズ管理**: Managed Agentsのライフサイクル管理と統合

### Codex CLI が最適なケース

- **自動化されたメモリ管理**: 非同期生成で「設定したら忘れる」運用
- **スキルベースの記憶**: スキルごとに独立したメモリファイル
- **コスト管理**: レート制限認識、使用量に応じた統合抑制
- **プライバシー重視**: 組み込みクレデンシャルスクラビング + Geographic制約

---

## 設計思想の対比

| 軸 | OpenClaw | Claude Code | Codex CLI |
|---|---|---|---|
| **哲学** | 「ファイルが真実、検索が知性」 — ハイブリッド検索で記憶を活用 | 「シンプルさが力」 — 余計なインフラを排し、モデルの知性に任せる | 「自動化が鍵」 — 人間が設定し、エージェントが自律管理 |
| **複雑さ** | 高（ベクトルDB + FTS + プロバイダー管理） | 低（ファイルシステムのみ） | 中（非同期パイプライン + 専用モデル） |
| **運用負荷** | 中（SQLite管理必要） | 低（ファイル編集のみ） | 低（自動化、上限・プルーニングあり） |
| **スケーラビリティ** | 高い（検索で大規模メモリに対応） | 限定的（ファイル全体読み込みに依存） | 中（256ロールアウト上限、定期的プルーニング） |
| **移植性** | 高い（Markdownファイル + SQLite） | 高い（Markdownファイルのみ） | 中（`~/.codex/` に依存、クロスマシン同期なし） |

---

## 共通の限界

3ハーネスすべてに共通する制約:

1. **クロスファイルコンテキストの欠如**: 複数ファイルにまたがる概念は明示的なクロスリファレンスがないと接続されない
2. **埋め込みドリフト**: プロバイダー変更時に再インデックスが必要（OpenClawは追跡機構あり）
3. **ストレージ増大**: 長期間使用でファイル数・インデックスサイズが線形増加
4. **マルチマシン同期**: いずれも組み込みのクロスマシン同期機構を持たない（Codexは明示的に「なし」と表明）

---

## Related

- [[entities/openclaw]] — OpenClaw entity page（Memory System セクションあり）
- [[entities/claude-code]] — Claude Code entity page
- [[entities/claude-code--architecture]] — Claude Code 5層アーキテクチャ詳細
- [[concepts/claude-perfect-memory]] — Claude Codeのファイルベースメモリ設計哲学
- [[raw/articles/2026-05-08_mem0-how-memory-works-in-codex-cli]] — Codex CLI メモリ詳細
- [[raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive]] — OpenClaw メモリ詳細
- [[concepts/ai-memory-systems]] — ChatGPT vs Claude vs Cognition メモリ比較
- [[concepts/context-compaction]] — コンテキストコンパクション概念
- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — AIメモリシステム全体像
- [[concepts/agent-harness-comparison]] — 9ハーネス総合比較
