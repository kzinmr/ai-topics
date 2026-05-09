---
title: "Claude Diary (Agent Continual Learning)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [memory-systems, coding-agents, context-engineering, claude-code]
sources:
  - "[[raw/articles/2025-12-01_rlancemartin_claude-diary]]"
related:
  - "[[concepts/agent-memory]]"
  - "[[concepts/continual-learning]]"
  - "[[concepts/context-engineering]]"
  - "[[entities/rlancemartin-github-io]]"
---

# Claude Diary (Agent Continual Learning)

Claude Diaryは、R. Lance Martinが開発したClaude Codeプラグイン。エージェントが**自身の経験から学習**し、永続的なメモリ（`CLAUDE.md`）を自動更新する。

## 動機

多くのAIエージェントは継続的学習能力を欠いている。CoALA論文（Sumers et al., 2023）が提唱する「手続き記憶（procedural memory）」と「エピソード記憶（episodic memory）」の区別に基づき、セッションログから持続的なルールを抽出する仕組みを実装。

## アーキテクチャ

### メモリパイプライン

```
セッション → /diary コマンド → diary entries → /reflect コマンド → CLAUDE.md更新
```

### 主要コンポーネント

| コンポーネント | 保存先 | 役割 |
|---------------|--------|------|
| Diary Entry | `~/.claude/memory/diary/YYYY-MM-DD-session-N.md` | セッションの達成事項・設計判断・課題・ユーザー好み・PRフィードバックを記録 |
| Reflection | `~/.claude/memory/reflections/YYYY-MM-reflection-N.md` | Diary entriesを分析し、パターンを抽出・CLAUDE.md提案 |
| Processed Log | `~/.claude/memory/reflections/processed.log` | 重複処理防止 |

### 作成タイミング

- **手動**: `/diary` スラッシュコマンド
- **自動**: PreCompact フック — 長いセッションでコンパクション時に自動生成
- **リフレクション**: 手動（`CLAUDE.md` 直接更新のため、人間が確認）

### 学習の種類

1. **PRレビューフィードバック**: PRコメントからコード品質ルールを学習
2. **Gitワークフロー**: アトミックコミット、ブランチ命名規則、コミットメッセージ形式
3. **テスト手法**: 標的テスト→包括テストの順序、特殊なテストランナー設定
4. **ユーザー好み**: 明示的に言及されない暗黙のワークフロー選好

## 理論的背景

- **CoALA** (Sumers et al., 2023): エージェントメモリの「手続き記憶」と「エピソード記憶」
- **Generative Agents** (Park et al., 2023): リフレクションによる経験の抽象化
- **Grow & Refine** (Zhang et al., 2025): 軌跡→教訓抽出→構造化更新のパイプライン

## Anthropic内部での類似実践

Cat Wu（Claude Codeプロダクトリード）のインタビューによると、Anthropicスタッフも同様のパターンを使用: Claude Codeセッションから日記エントリを作成し、リフレクションでパターンを特定。

## 参照

- [Claude Diary — Lance Martin's Blog](http://rlancemartin.github.io/2025/12/01/claude_diary/) (2025-12-01)
- [Claude Diary GitHub](https://github.com/rlancemartin/claude-diary)
- [CoALA Paper](https://arxiv.org/pdf/2309.02427) (Sumers et al., 2023)
