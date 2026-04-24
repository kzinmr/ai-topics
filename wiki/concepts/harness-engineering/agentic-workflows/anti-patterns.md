---
title: "Anti-patterns in Agentic Engineering"
type: concept
aliases:
  - anti-patterns
  - agentic-anti-patterns
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - anti-pattern
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/"
---

# Anti-patterns in Agentic Engineering

Simon Willisonが警告する**コーディングエージェント使用時のアンチパターン**。特に「レビューされていないコードを他者に押し付ける」行為は深刻な問題。

## 最大のアンチパターン: Unreviewed Code Infliction

> "Don't file pull requests with code you haven't reviewed yourself."

エージェントが生成した数百〜数千行のコードを**自分で検証せずにPRに出す**行為。これは実質的に「実際の作業を他者に委譲している」に等しい。

### 問題の本質
- レビュアーがエージェントの代わりに検証作業を強いられる
- 開発者としての付加価値がゼロになる
- チームの信頼とモラルを損なう

## 良いPRの条件

Willisonが定義する**良いアジェンティックエンジニアリングのPR**の特徴:

### 1. 動作確実性
> "The code works, and you are confident that it works."

- コードが実際に動作することを自分で確認
- 自信を持って「動きます」と言える状態

### 2. 適切な変更サイズ
> "Several small PRs beats one big one."

- 小さな変更に分割
- レビュアーの認知負荷を考慮
- エージェントにGit操作を任せて分割コミット

### 3. 十分な文脈提供
> "Agents write convincing looking pull request descriptions. You need to review these too!"

- 変更の高レベルな目的を説明
- 関連するIssueや仕様書へのリンク
- エージェントが書いたPR説明文も自分で検証

### 4. 検証証拠の提示
> "Notes on how you manually tested it, comments on specific implementation choices or even screenshots and video of the feature working go a long way."

- 手動テストの方法と結果
- 特定の実装選択に関するコメント
- 動作確認のスクリーンショットや動画

## 認知負債との関係

アンチパターンは即座に**認知負債**を蓄積させる:
- 理解していないコードがマージされる
- 将来の保守・修正が困難になる
- チーム全体の生産性が低下する

## 予防策

### 開発者の責任
1. **必ず自分でコードを読む** - エージェントの出力を盲信しない
2. **テストを実行する** - 動作確認を省略しない
3. **小さな変更にする** - 一度に大量のコードを変更しない
4. **文脈を記録する** - なぜこの変更が必要か説明する

### レビュアーの権利
- 検証されていないコードのレビューを拒否する権利
- 動作確認の証拠を要求する権利
- 小さく分割されたPRを要求する権利

## 関連概念

- [[cognitive-debt]] — 未検証コードの蓄積が認知負債になる
- [[red-green-tdd]] — テスト駆動で品質を確保するアンチパターン回避策
- [[agentic-manual-testing]] — 手動テストの重要性
- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents.md]] — 小さなコミットに分割する技術

## 参照

- [[simon-willison]] — 概念提唱者
- [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
