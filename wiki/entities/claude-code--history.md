---
title: "Claude Code — Development History"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-04-28
tags:
  - product
  - history
sources:
  - https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works
  - https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/
---

# Claude Code: Development History

Back to main profile: [[claude-code]]

## Origins (Sep 2024)
[[boris-cherny]]がAnthropicに入社し、Claude 3.6モデルでプロトタイピングを開始。最初のプロトタイプはAppleScript経由で音楽を特定・変更するCLIツールだった。

## Internal Dogfooding (Nov 2024)
- **20%のエンジニア**が初日に採用
- **5日間以内に50%が採用**
- 1日60-100回の内部リリース
- 70-80%の技術スタッフが毎日使用

## General Availability (May 2025)
- チームは約10人のエンジニアに拡大
- 2025年7月時点ですでに高い成長率を記録

## OpenAI移管 (Jul 2025)
[[anthropic]]から[[openai]]へ移管され、Boris ChernyがHead of Claude Codeとして開発を継続。

## Agent Teams GA (2026)
マルチエージェント協調機能がGeneral Availabilityに到達。複数のClaude Codeインスタンスが役割分担しながら並行作業を実行可能。

## Source Code Leak Incident (Mar 31, 2026)

### What Happened
セキュリティ研究者Chaofan Shouが、Claude Codeのnpmパッケージに含まれるsourcemapファイルを通じて、難読化されていないTypeScriptの全ソースコードへの参照を発見。AnthropicのCloudflare R2ストレージ上のzipアーカイブがダウンロード可能だった。

### Impact
- GitHubにソースコードのバックアップが**41,500回以上フォーク**
- npmパッケージのsourcemapファイルが原因
- Anthropicのビルドチェーンが未難読化のTypeScriptソースを参照

### Significance
この漏洩により、Claude Codeの内部設計が完全に公開。AIコーディングエージェントのアーキテクチャ理解に大きな影響を与えた。詳細は[[claude-code--architecture]]を参照。
