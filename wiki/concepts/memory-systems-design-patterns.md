---
title: "Memory Systems Design Patterns — Anthropic vs OpenAI vs Cognition"
status: draft
created: 2026-04-13
updated: 2026-04-13
sources:
  - "https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - "https://www.shloked.com/writing/chatgpt-memory-bitter-lesson"
  - "https://www.shloked.com/writing/claude-memory"
  - "https://www.shloked.com/writing/claude-memory-tool"
  - "https://www.shloked.com/writing/claude-code-source-patterns"
  - "https://www.shloked.com/writing/vajra"
tags: [memory-systems, context-engineering, design-patterns, multi-agent, file-based-memory, competitive-analysis]
related: [claude-memory, chatgpt-memory-bitter-lesson, context-engineering, harness-design-long-running-apps, claude-code-source-patterns, vajra-background-agent]
---

# Memory Systems Design Patterns — Anthropic vs OpenAI vs Cognition

AIエージェントのメモリシステム設計における**3つのアプローチ**と、業界が収束しつつあるパターンを整理。

## 1. メモリ設計の3大アプローチ

| 次元 | **Anthropic (Claude)** | **OpenAI (ChatGPT)** | **Cognition (Devin)** |
|------|------------------------|----------------------|------------------------|
| **メモリ形式** | ファイルベース（CLAUDE.md, .agent/） | 独自データベース | ファイルベース（Anthropicをコピー） |
| **セッション** | ステートレス（毎回全コンテキスト） | ステートフル（メモリ永続化） | ステートフル→ステートレスへ移行中 |
| **検索戦略** | JIT（必要時に取得） | 事前ロード（メモリから復元） | ハイブリッド |
| **バージョン管理** | Git統合（天然） | 手動バックアップ必要 | Git統合予定 |
| **透明性** | 高い（人間が読めるファイル） | 低い（内部データベース） | 中間 |
| **スケーラビリティ** | ファイルシステムに依存 | データベーススキーマに制限 | ファイルシステムへ移行 |

## 2. Anthropicのメモリ設計原則（Engineering Blog 2記事から抽出）

### Principle 1: Context is a Finite Budget
> "Every new token introduced depletes this budget by some amount."

- **Context Rot**は性能勾配（ハードな崖ではない）
- Transformerアーキテクチャの根本的制約（n² attention）
- **対策**: 最小限の高信号トークンのみを選択

### Principle 2: File System IS the Memory
- CLAUDE.md + .agent/ + Git = 完全なメモリシステム
- 外部データベース不要
- **Anthropic Harness**: スプリントコントラクトをファイルで保存
- **Claude Code**: Forkプリミティブでコンテキスト分岐

### Principle 3: JIT > Pre-Load
- 事前に全データをロードするのではなく、**必要なときに必要なだけ取得**
- 人間の認知モデルに近い（索引に依存、暗記しない）
- `glob`/`grep`/`read`で動的取得

### Principle 4: Context Reset > Compaction
- 会話内要約（compaction）より**新規エージェント起動**を推奨
- ハンドオフ成果物に十分な状態を含める
- クリーンスレートでコヒーレンスを維持

### Principle 5: Evaluator Isolation
- 生成と評価を分離することで自己評価バイアスを回避
- **GAN-inspiredループ**: Generator ↔ Evaluator
- Evaluatorはタスクがモデル能力を超える場合のみ使用

## 3. Shlok Khemaniの「Bitter Lesson」分析との接続

Rich Suttonの**Bitter Lesson**（計算量を活用する一般的方法が最終的に勝つ）をメモリシステムに適用：

| Bitter Lessonの教訓 | メモリシステムへの適用 |
|---------------------|----------------------|
| 計算量を活用せよ | 大きなコンテキストウィンドウ = より良い想起 |
| 人間のバイアスを排除 | ファイルベース = 透明、再現可能 |
| 一般的方法が特殊方法に勝る | JIT検索 = 普遍的パターン |

**Khemeniの核心主張**:
> "The best way to build agent memory is not to build one at all."
> "Stateless agents that receive full context every time are more reliable than stateful agents that try to remember."

## 4. 業界の収束パターン

### 収束している設計
| パターン | Anthropic | OpenAI | Cognition | Vajra |
|---------|-----------|--------|-----------|-------|
| **ファイルベースメモリ** | ✅ CLAUDE.md | ❌ DB | ✅ コピー中 | ✅ .vajra/ |
| **JITコンテキスト** | ✅ glob/grep | ❌ 事前ロード | ⚠️ 移行中 | ✅ SKILL.md |
| **Git統合** | ✅ 天然 | ❌ proprietary | ✅ 予定 | ✅ 天然 |
| **ステートレスセッション** | ✅ | ❌ ステートフル | ⚠️ 移行中 | ✅ |
| **Context Reset** | ✅ 推奨 | ❌ Compaction | ⚠️ 調査中 | ✅ 分離ワークスペース |
| **Evaluator分離** | ✅ GANループ | ❌ 自己評価 | ⚠️ 計画中 | ✅ Plan Review + Code Review |

### 収束していない設計
| 次元 | Anthropic | OpenAI |
|------|-----------|--------|
| **メモリ永続化** | ファイル（CLAUDE.md） | データベース（Memory機能） |
| **セッション管理** | Context Reset（新規エージェント） | Compaction（会話内要約） |
| **評価戦略** | Evaluator分離（GAN） | 自己評価（単一エージェント） |

## 5. Coding Agent（Codex vs Claude Code）への影響

メモリ設計の差異が**エージェントの特色**に直結：

| 特色 | Claude Code | Codex |
|------|-------------|-------|
| **メモリ形式** | CLAUDE.md（ファイル） | 内部状態（データベース） |
| **セッション** | ステートレス（毎回全コンテキスト） | ステートフル（メモリ永続化） |
| **Fork** | ✅ 独立的コンテキスト分岐 | ❌ 単一スレッド |
| **Cache** | ✅ プロンプトキャッシュ最優先 | ⚠️ 部分的 |
| **Transparency** | ✅ 人間が読めるファイル | ❌ 内部状態 |

**Shlokの洞察**:
> "Cognition is copying Claude's memory approach" — Anthropicの設計が業界標準になりつつある

## 6. 実践的メモリ設計チェックリスト

エージェントメモリシステムを設計する際の評価項目：

- [ ] **ファイルベースか？** — 透明性、Git統合、可搬性
- [ ] **JIT検索か？** — 最小限の事前ロード、動的取得
- [ ] **ステートレスセッションか？** — 再現性、Context Reset対応
- [ ] **Evaluator分離か？** — 自己評価バイアスの回避
- [ ] **Context Rot対策か？** — 注意力バジェットの管理
- [ ] **Cache最適化か？** — プロンプトキャッシュの有効活用
- [ ] **Fork/ブランチ対応か？** — 独立したコンテキスト探索

## Sources

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic Engineering, Sep 2025
- [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) — Prithvi Rajasekaran, Anthropic Labs, Mar 2026
- [ChatGPT's Memory Problem](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson) — Shlok Khemani, Apr 2026
- [Claude's Memory](https://www.shloked.com/writing/claude-memory) — Shlok Khemani, Apr 2026
- [Why Cognition is Copying Claude's Memory](https://www.shloked.com/writing/claude-memory-tool) — Shlok Khemani, Apr 2026
- [Claude Code Source Patterns](https://www.shloked.com/writing/claude-code-source-patterns) — Shlok Khemani, Apr 2026
- [Vajra: Background Coding Agent](https://www.shloked.com/writing/vajra) — Shlok Khemani, Apr 2026

## See Also

- [[concepts/_index.md]]
- [[concepts/claude-memory-tool.md]]
- [[concepts/ai-agent-memory-middleware.md]]
- [[concepts/knowledge-graph-memory-agents.md]]
- [[concepts/ai-agent-memory-two-camps.md]]
