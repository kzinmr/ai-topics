---
title: "Claude Opus 4.7"
type: concept
aliases:
  - claude-opus-4-7
  - opus-4-7
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - anthropic
  - model
status: complete
sources:
  - url: "https://www.anthropic.com/news/claude-opus-4-7"
    title: "Introducing Claude Opus 4.7 (Anthropic Official, 2026-04-16)"
  - url: "https://www.anthropic.com/claude/opus"
    title: "Claude Opus 4.7 Product Page"
  - url: "https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available"
    title: "Claude Opus 4.7 on GitHub Copilot"
  - url: "https://www.anthropic.com/claude-opus-4-7-system-card"
    title: "Claude Opus 4.7 System Card"
---

# Claude Opus 4.7

**Claude Opus 4.7** は、Anthropic が **2026年4月16日** にリリースしたフロンティア LLM。Opus 4.6 の後継であり、高度なソフトウェアエンジニアリング、視覚認識、長期的なマルチステップタスク実行において大幅な改善を実現している。

## リリース情報

- **リリース日**: 2026年4月16日
- **コンテキストウィンドウ**: **100万トークン**
- **API 提供**: Anthropic API、GitHub Copilot、Claude.ai
- **Model Card**: [公開済み](https://www.anthropic.com/claude-opus-4-7-system-card)

## 主要な改善点

### 1. ソフトウェアエンジニアリング
- 最も難しいコーディングタスクで顕著な改善
- 「これまで監督が必要だった作業」を **自信を持って任せられる** レベルに
- 複雑な長時間タスクを **厳密かつ一貫して** 処理
- 指示への **精密な注意** と **自己検証** 能力

### 2. ビジョン能力
- **高解像度画像認識** — より詳細な視覚情報を処理
- XBOW の視覚精度ベンチマーク: **98.5%**（Opus 4.6 は 54.5%）
- プロフェッショナルタスクでの **センスと創造性** が向上
- UI、スライド、ドキュメントの品質が改善

### 3. エージェント機能
- **堅牢なマルチステップ実行** — GitHub Copilot でも評価
- **長期的推論** と **ツール依存ワークフロー** での改善
- コード実行前に **証明/検証** を行う新しい行動パターン（Vercel 報告）

## ベンチマーク改善

| 領域 | Opus 4.6 | Opus 4.7 | 改善 |
|------|---------|---------|------|
| 視覚精度（XBOW） | 54.5% | **98.5%** | +44% |
| ワンショットコーディング | ベースライン | **顕著に向上** | — |
| 自己限界認識 | 中程度 | **顕著に正直に** | — |

## トークナイザーの変更点

Opus 4.7 は更新されたトークナイザーを使用：
- 同じ入力が **1.0〜1.35倍** のトークンにマッピングされる可能性あり
- 高努力レベルでの思考量増加（特にエージェント設定での後半ターン）
- 信頼性向上と引き換えの出力トークン増加

## セキュリティとガバナンス

- **Mythos へのステップ**: Opus 4.7 は Mythos クラスモデルの **安全テストベッド**
- **Project Glasswing**: サイバーセキュリティリスク・ベネフィットの評価
- **サイバーセーフガード**: 禁止/高リスクのサイバーセキュリティ使用を自動検出・ブロック
- **Mythos との関係**: Mythos Preview ほど広範な能力は持たないが、Opus 4.6 を全てのベンチマークで上回る

## 実績（ユーザー報告）

- **Vercel（Joe Haddad）**: 「Opus 4.6 からの退行なし。ワンショットコーディングタスクで驚異的。より正確かつ完全。自身の限界について顕著に正直。」
- **XBOW（Oege de Moor）**: 「コンピューター使用作業でステップチェンジ。Opus 4.6 の最大の不満点が事実上解消。」
- ユーザーがゲーム、Webサイト、アニメーション、CAD デザインを **数分で** 構築

## 関連概念

- [[concepts/claude-code-best-practices]] — Claude Code のベストプラクティス
- [[concepts/claude-perfect-memory]] — Claude Code の永続メモリ

## ソース

- [Introducing Claude Opus 4.7 (Anthropic Official)](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude Opus 4.7 Product Page](https://www.anthropic.com/claude/opus)
- [GitHub Copilot Changelog](https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available)
- [Claude Opus 4.7 System Card](https://www.anthropic.com/claude-opus-4-7-system-card)
