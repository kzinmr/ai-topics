---
title: "Coding Agents & Complexity Budgets"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [agentic-engineering, coding-agents, developer-tooling, workflow, software-engineering, ai-native]
sources:
  - "[[raw/articles/2025-12-01_leerob_coding-agents-complexity-budgets]]"
related:
  - "[[concepts/ai-native-development]]"
  - "[[concepts/agentic-engineering]]"
  - "[[entities/cursor]]"
---

# Coding Agents & Complexity Budgets

Lee Robinson（Cursor, 元Vercel）が提唱する、AIコーディングエージェント時代の**抽象化コスト**と**複雑性バジェット**の概念。

## 核心的主張

**AIとコーディングエージェントの時代において、抽象化のコストは過去最大になっている。**

従来は非開発者（マーケター、ライター）がGUIで編集できるようにCMSを導入するのが標準だった。しかし、エージェントがコードを直接操作できる現在、中間抽象化レイヤー（CMS、i18nフレームワーク、プレビューシステム）はエージェントの生産性を阻害する。

## 実証: cursor.comのCMS→コード移行

- **期間**: 推定2週間 → 実際3日間
- **コスト**: $260のトークン（数百エージェントを使用）
- **手法**: Cursorで移行計画を生成 → エージェントが実装 → 人間がレビュー

### 削除された複雑性

1. **ユーザー管理の二重化**: CMS側とGitHub側の両方でアカウント管理
2. **プレビューの複雑性**: 静的サイト + CMSのドラフトモード → Vercel認証が必要
3. **国際化（i18n）**: CMSベースの翻訳ワークフロー → コードベースで管理
4. **コンテンツ移行**: CMS APIからのデータエクスポート + フォーマット変換

## 複雑性バジェット（Complexity Budget）

ソフトウェアシステムには「複雑性の許容量」があり、抽象化はそこから消費する:

- CMS導入前: 複雑性バジェットの30%消費 → 残り70%で機能開発
- CMS導入後: 複雑性バジェットの60%消費 → 残り40%
- AIエージェント時代: **エージェントがコードを直接扱えるなら抽象化不要** → 複雑性バジェットを機能に全振り

## 実践的含意

| Before (AI以前) | After (AIエージェント時代) |
|-----------------|--------------------------|
| 非開発者用GUIが必要 | チャットボットで十分（マーケターもGitHubでPR） |
| 抽象化で複雑性を隠蔽 | 抽象化自体が複雑性を追加 |
| 静的サイト生成 + CMS | 静的サイト生成 + Markdown |
| 専用i18nフレームワーク | ファイルベースの翻訳 |

## 参照

- [Coding Agents & Complexity Budgets — Lee Robinson](https://leerob.com/agents) (2025-12)
- [cursor.com](https://cursor.com) — この移行の対象サイト
