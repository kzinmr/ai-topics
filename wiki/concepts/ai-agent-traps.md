---
title: "AI Agent Traps"
type: concept
created: 2026-04-09
updated: 2026-04-19
tags: [concept, security, adversarial-attacks, agents]
related: [prompt-injection, ai-safety, multi-agent-systems]
sources: []
---

# AI Agent Traps

A systematic framework from Google DeepMind (2026) for understanding how the open web can be weaponized against autonomous AI agents. Defines six categories of adversarial content engineered to exploit visiting agents.

## Key Findings

### Hidden Prompt Injections
- HTML-based injections commandeer agents in **up to 86% of scenarios**
- Trivial to deploy, no sophisticated tooling required
- Immediate concern for web-reading agents

### Memory Poisoning
- **>80% attack success** with <0.1% data contamination
- Single poisoned page corrupts downstream reasoning across future sessions
- User never sees the malicious input

### Six-Category Attack Taxonomy

| Category | Target | Example |
|----------|--------|---------|
| Perception Traps | What agent sees | Hidden text in HTML |
| Cognitive Traps | Reasoning | Misleading logical structures |
| Memory Traps | Stored knowledge | Poisoned embeddings |
| Action Traps | Tool use | Hijacked API calls |
| Systemic Traps | Multi-agent coordination | Exploiting agent communication |
| Human-in-the-Loop Traps | Supervisor | Deceiving human approvers |

### Accountability Gap
- No clear liability when compromised agents commit financial crimes
- Unclear responsibility: agent operator vs model provider vs domain owner
- Future regulation must distinguish passive adversarial examples from deliberate cyberattacks

## Implications

### Security
- Web-browsing agents highly vulnerable to simple attacks
- Defense requires fundamental architectural changes
- Memory persistence creates long-term attack surface

### Policy
- Legal frameworks need updating for agent-specific vulnerabilities
- Clear standards for liability in autonomous system failures
- Distinction between accidental and malicious exploitation needed

## Sources
-  (NLP News coverage)
- Google DeepMind research paper (2026)

## Related
- 
- [[concepts/ai-safety]]
- 

## Authorization Challenges for AI Agents (2026-04)

**WorkOS FGA**的分析では、AIエージェントの認可安全问题について以下を特定:

### The Confused Deputy Problem

エージェントが正当な権限を持っているが、攻撃者に騙されて権限を悪用する構造的リスク。

**例**: 「本番とステージングの差分を示して」という要求で、本番のAPIキーが漏洩

| 従来のサービスアカウント | AIエージェント |
|------------------------|----------------|
| 決定論的スコープ | 非決定論的スコープ |
| 固定アクセス | 動的にintentを生成 |
| 変更なし | 今日と明日で異なる権限が必要 |

### 権限爆発問題

従来のRBACでは `Repository:API > Branch:feature-xyz` のような細粒度の許可を表現すると、O(N×M)ロールが必要になる。

### FGA = RBAC + 階層

リソースグラフのノードに 역할을関連付ける:
- 垂直継承: `Branch:feature-xyz` のEditor権限は内部すべてにアクセス
- 水平移動防止: `Branch:staging` にはアクセスできない

### MCPとの接続

MCPは認可を実装者に委任し、`files:read` のような粗いOAuth 2.1スコープ依赖。FGAはMCPのRAR(rich authorization requests)에ロジック层を提供。

### Sources
- 

## Sources