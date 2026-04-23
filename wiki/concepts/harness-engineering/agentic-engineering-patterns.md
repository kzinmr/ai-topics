---
title: Agentic Engineering Patterns
status: active
created: 2026-02-23
updated: 2026-04-12
related:
  - concepts/evals
  - concepts/harness-engineering
  - concepts/ai-agent-traps
  - entities/simon-willison
  - entities/andrej-karpathy
tags: [agentic-engineering, coding-agents, claude-code, codex, testing, git, patterns, simon-willison]
source: https://simonwillison.net/guides/agentic-engineering-patterns/
---

# Agentic Engineering Patterns

Simon Willisonが2026年2月23日に開始したガイドプロジェクト。コーディングエージェント（Claude Code、OpenAI Codex、Gemini CLI等）から最高の結果を得るための実践パターンを体系化したもの。

> "I use the term **agentic engineering** to describe the practice of developing software with the assistance of coding agents."
> — Simon Willison

元は2025年12月の「2025 in AI: The Year Everything Changed」で言及された用語が、2026年2月に独立的なガイドとして展開された。15章構成、6つのセクションに分類。

## 定義

**Coding Agent**: コードの生成と実行の両方ができるエージェント。Claude Code、OpenAI Codex、Gemini CLI等。

**Agent**: "Agents run tools in a loop to achieve a goal" — LLMにプロンプトとツール定義を渡し、LLMがリクエストしたツールを呼び出して結果をLLMに戻すループ。

**Agentic Engineering**: コーディングエージェントの支援を受けてソフトウェアを開発する実践。Vibe coding（Karpathyが2025年2月に造語）とは異なり、**レビュー済みの本番品質コード**を目指す。

---

## セクション1: Principles（原則）

### 1. What is agentic engineering?
- コードを書くことはソフトウェアエンジニアの唯一の活動ではない
- 本質は「**どのコードを書くか**」を判断すること
- 与えられた問題には常に複数の解決策があり、それぞれにトレードオフがある
- LLMは過去の間違いから学習しないが、**コーディングエージェントは学習できる** — 指示とツールハーネスを意図的に更新することで
- エージェントは人間の野心を拡大する手段

### 2. Writing code is cheap now
- コーディングコストがほぼ無料に近づいたが、「**良いコード**」には依然としてコストがかかる
- 良いコードの定義:
  - 正しく動作し、意図したことをバグなく実行する
  - 動作することが確認されている（テスト等）
  - 正しい問題を解決している
  - エラーケースを適切に処理（ハッピーパスだけでなく）
  - シンプルでミニマル（YAGNIの原則）
  - テストで保護されている
  - 適切に文書化されている
  - 将来の変更に耐える設計
  - 関連する「〜ility」（アクセシビリティ、テスト性、信頼性、セキュリティ、保守性、観測性、スケーラビリティ、ユーザビリティ）を満たす
- 新しいパーソナル・組織的習慣の構築が必要
- 「その時間をかける価値がない」という直感に従う前に、とりあえず非同期エージェントセッションでプロンプトを試す

### 3. Hoard things you know how to do
- 何が可能で何が不可能か、そしてそれをどう実現するかを知る
- 実行可能なコードによる実証が最強の資産
- Simonのアセット: ブログ、TIL、1000以上のGitHubリポジトリ、tools.simonwillison.net（HTMLツール集）、simonw/research
- **Recombining Pattern**: 既存の動作する例を2つ以上組み合わせて新しいものを構築
  - 例: PDF.js + Tesseract.js → ブラウザベースOCRツール
- コーディングエージェントはこのパターンをさらに強力にする

### 4. AI should help us produce better code
- AIは単に高速にコードを書くためではなく、**より良いコード**を生み出すために使う
- 技術的負債の回避
- コーディングエージェントに退屈な作業（テスト、ドキュメント、リファクタリング）を任せる
- AIツールにより、より多くのオプションを検討できる
- **Compound Engineering Loop**: プロトタイプ → テスト → リファクタリング → ドキュメント → 改善の循環

### 5. Anti-patterns
- **Inflicting unreviewed code on collaborators**: レビューされていないコードを共同作業者に押し付ける
- 品質基準の低下を防ぐ

---

## セクション2: Working with coding agents

### 1. How coding agents work
- **Large Language Models**: 基盤技術
- **Chat templated prompts**: プロンプトの構造化
- **Token caching**: コスト最適化
- **Calling tools**: ツール呼び出しのメカニズム
- **The system prompt**: エージェントの動作定義
- **Reasoning**: 推論能力の活用
- **LLM + system prompt + tools in a loop**: エージェントループの全体像

### 2. Using Git with coding agents
- **Git essentials**: エージェントとGitの連携
- **Core concepts and prompts**: エージェント向けのGitプロンプトパターン
- **Rewriting history**: 安全な履歴の書き換え

### 3. Subagents
- **Claude Code's Explore subagent**: 調査タスクの委任
- **Parallel subagents**: 並列実行による効率化
- **Specialist subagents**: 専門特化したエージェントの活用
- **Official documentation**: 各エージェントの公式ドキュメント参照

---

## セクション3: Testing and QA

### 1. Red/green TDD
テスト駆動開発をエージェントと共に行う。テストファーストアプローチにより、エージェントはより簡潔で信頼性の高いコードを書く。

### 2. First run the tests
既存のテストをまず実行し、ベースラインを確立してから変更を行う。

### 3. Agentic manual testing
- **Mechanisms for agentic manual testing**: エージェントによる手動テストの仕組み
- **Using browser automation for web UIs**: ブラウザ自動化を活用したUIテスト
- **Have them take notes with Showboat**: Showboatを使ったテスト結果の記録

---

## セクション4: Understanding code

### 1. Linear walkthroughs
コードの線形的な説明。ShowboatとPresentを使った実例。

### 2. Interactive explanations
対話的なコード説明。Word cloudsの理解例。

---

## セクション5: Annotated prompts

### GIF optimization tool using WebAssembly and Gifsicle
プロンプトの注釈付き実例。フォローアッププロンプトのパターンも含む。

---

## セクション6: Appendix

### Prompts I use
Simon Willisonが実際に使用しているプロンプト集:
- **Artifacts**: アーティファクト生成プロンプト
- **Proofreader**: 校正プロンプト
- **Alt text**: 代替テキスト生成プロンプト
- **Podcast highlights**: ポッドキャストハイライト抽出プロンプト

---

## Guide Format（ガイド形式）

Simonはこのプロジェクトのために新しいコンテンツタイプ「**Guide**」をDjangoサイトに実装した:
- Guideは章のコレクション
- 各章は事実上ブログ記事だが、日付が目立たない
- 時間の経過とともに**更新される**ことを意図（初回公開で固定されない）
- Guide/Chapter/ChapterChangeモデルとDjangoビューは**Claude Opus 4.6 + Claude Code for web**（iPhone経由）で書かれた

## 関連プロジェクト

- **simonw/research**: コーディングエージェントに問題を調査させ、動作するコードとレポートを作成させるリポジトリ
- **tools.simonwillison.net**: LLM支援ツールとプロトタイプのコレクション
- **HTML tools**: JavaScriptとCSSを埋め込んだ単一HTMLページで特定の問題を解決

## 参考文献

- [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [Writing about Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)
- [2025 in AI: The Year Everything Changed](https://simonwillison.net/2025/Dec/31/2025-in-ai/) — 用語の初出
- [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)

## See Also

- [[concepts/_index.md]]
- [[concepts/agentic-rag.md]]
- [[concepts/chaos-engineering.md]]
- [[concepts/memory-systems-design-patterns.md]]
- [[concepts/meta-harness.md]]
