---
title: "Agent Skills"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - architecture
  - mcp
  - developer-tooling
  - claude-code
aliases:
  - Agent Skills open standard
created: 2026-04-25
updated: 2026-05-22
sources:
  - raw/articles/2026-05-08_anthropic-engineering_equipping-agents-for-the-real-world-with-agent-skills.md
  - raw/articles/2026-05-18_browse-sh-browserbase_agent-skills-catalog.md
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
related:
  - building-effective-agents
  - effective-harnesses-for-long-running-agents
  - mcp
  - claude-code-best-practices
---

# Agent Skills

Anthropicが公開した、エージェントにドメイン固有の専門知識を動的に付与するための**オープン標準**（2025年12月18日公開）。

> "Building a skill for an agent is like putting together an onboarding guide for a new hire."

## コアコンセプト

Skills = 命令・スクリプト・リソースを格納した**ディレクトリ**。エージェントが動的に発見・ロードして特定タスクの性能を向上させる。

## 構造

```
skill-name/
├── SKILL.md          # 必須: YAML frontmatter + 指示本体
├── references/       # オプション: 追加参照ファイル
├── scripts/          # オプション: 実行可能コード
└── templates/        # オプション: テンプレート
```

### SKILL.md

```yaml
---
name: pdf
description: PDF document editing and form filling capabilities
---
# PDF Skill

Instructions for editing PDFs and filling forms...
```

## Progressive Disclosure（段階的開示） — 3層設計

| レベル | 内容 | コンテキスト消費 |
|--------|------|----------------|
| **L1** | `name` + `description` | 常時（システムプロンプトに注入） |
| **L2** | `SKILL.md` 本文 | 関連タスク時のみ（Bash toolで読み取り） |
| **L3+** | リンクされた追加ファイル | 必要時のみ（エージェントが判断して読み取り） |

**設計原理**: 「よく整理されたマニュアルのようなもの — 目次→章→付録の順に必要なときだけ読む」

## コード実行

Skillsは実行可能コードも含められる:
- ソートのような決定論的操作はトークン生成よりコード実行の方が効率的
- PDFフォームフィールド抽出スクリプト → ClaudeはスクリプトもPDFもコンテキストに読み込まず実行可能
- コードは決定論的 → 一貫性・再現性

## 開発ガイドライン

1. **評価から始める**: 代表的なタスクでエージェントの苦手領域を特定 → そこからSkillを段階的に構築
2. **スケールのための構造化**: SKILL.mdが肥大化したらファイル分割＋参照
3. **相互排他的・低頻度の文脈は分離**: トークン使用量削減
4. **コードは実行可能ツールとしてもドキュメントとしても機能**: どちらで使うべきか明確に

## 実例: PDF Skill

Claudeの文書編集機能を支えるSkill:
- `SKILL.md` — PDF操作の基本指示
- `forms.md` — フォーム入力専用指示（フォーム入力時のみ読み取り）
- `fill_form.py` — フォームフィールド抽出・入力スクリプト

## See Also

- [[entities/browse-sh]] — Browse.sh: 100+ curated browser skills catalog by Browserbase
- [[concepts/agent-skills-overview]] — Agent Skills 概念クラスターマップ（親ページ）
- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[concepts/mcp]] — Model Context Protocol
- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[agent-skills-skillmd]] — SKILL.md format details
