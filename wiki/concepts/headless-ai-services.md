---
title: "Headless AI Services"
type: concept
created: 2026-04-20
updated: 2026-04-30
tags: [concept, ai-agents, api-first, saas, agentic-engineering]
related: [agentic-engineering, api-first-development, mcp, headless-saas]
sources: []
---

# Headless AI Services

Matt Webbが提唱した概念で、**personal AIが直接API経由でSaaSサービスを操作**し、GUIベースの操作（bot-controlled mouse）を排除するアプローチ。

## 背景

2026年4月、Marc Benioff（Salesforce CEO）が**Salesforce Headless 360**を発表：

> "Welcome Salesforce Headless 360: No Browser Required! Our API is the UI. Entire Salesforce & Agentforce & Slack platforms are now exposed as APIs, MCP, & CLI."

## 中心的な主張

- **Personal AIはGUIよりAPI経由の方が高速で確実**
- 人間向けUI ≠ AIエージェント向けUI
- API-firstがSaaSの差別化要因になる

## Brandur Leachによる「Second Wave of API-first Economy」

2010年代の「Every online service was launching APIs」に続き、第2波が来ている：

> "Suddenly, an API is no longer liability, but a major saleable vector to give users what they want: a way into the services they use and pay for so that an agent can carry out work on their behalf."

## 料金構造への影響

API-firstモデルが主流になると、**per-head SaaS pricing schemes**が壊れる可能性がある。エージェントは人間とは異なる利用パターンを持ち、1つの企業で数十〜数百のエージェントがAPIを叩くようになるため、従来のper-seat課金は成立しなくなる。

## Headless SaaS との関係

[[concepts/headless-saas]]（Ivan Burazinが提唱）はHeadless AI Servicesをさらに発展させた概念。両者の違い：

| 側面 | Headless AI Services (Webb) | Headless SaaS (Burazin) |
|------|---|---|
| フォーカス | 既存SaaSをAIがAPI経由で操作 | SaaS自体をエージェント向けに再構築 |
| インターフェース | 人間向けUIの上にAPI層 | APIが**唯一**のインターフェース（GUIなし） |
| ビジネスモデル | 既存SaaSの料金構造が課題 | 消費量ベースの新しいモデル |

## 関連項目

- [Agentic Engineering](../agentic-engineering.md)
- [Model Context Protocol (MCP)](../model-context-protocol-mcp.md)
- [API-first Development](../cli-over-mcp-pattern.md)

## See Also

- [[concepts/_index]]
- [[concepts/neurosymbolic-ai]]
- [[concepts/ai-coding-reliability]]
- [[concepts/ai-agent-memory-middleware]]
- [[concepts/ai-digital-nato]]
