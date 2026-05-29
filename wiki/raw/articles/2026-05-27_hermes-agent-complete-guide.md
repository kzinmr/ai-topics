---
type: x_article
x_article_title: "HERMES AGENT: THE COMPLETE GUIDE. From Zero to Self-Improving AI Employee"
x_article_author: "@IBuzovskyi"
x_article_id: "2059639716417273860"
getxapi: false
date: 2026-05-27
source: https://x.com/i/article/2059639716417273860
tags:
  - hermes-agent
  - ai-agents
  - self-improvement
  - multi-agent
---

# HERMES AGENT: THE COMPLETE GUIDE

Comprehensive guide to Hermes Agent by Nous Research. Covers installation, model selection, messaging platforms, dashboard, use cases, self-improvement loop, and security.

## Key Highlights

- **Memory**: Everything lives in markdown files on your computer — not in the cloud
- **Self-improvement**: Reviews every completed task and edits its own skills
- **Session recall**: FTS5 full-text search + LLM summarization across entire conversation history
- **Multi-agent via Kanban**: Agents claim tasks from a board, work in parallel
- **20+ messaging platforms**: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams
- **Self-improvement loop**: Execute → Review → Save as skill → Reuse next time
- **Security stack**: Bitwarden Secrets Manager + iron-proxy egress firewall for production deployments

## Model Recommendations

| Tier | Model | Best For |
|------|-------|---------|
| Expensive | claude-opus-4 / claude-sonnet-4 | Complex reasoning, nuanced writing, business advisor |
| Moderate | GPT-5.5 | Coding, prototyping, budget daily driver ($20/mo) |
| Affordable | Qwen 3.7 Max | Long-horizon autonomous tasks (35h, 1000+ tool calls) |

## The Self-Improvement Loop

1. User gives task
2. Hermes executes
3. After completion: reviews what worked, what didn't, optimal path
4. Saves as skill in `~/.hermes/skills/`
5. Next time: uses that skill directly
6. User corrects once → never makes that mistake again

## Security for Production

- **Layer 1 — Bitwarden Secrets Manager**: One bootstrap token in .env, real credentials in Bitwarden. Rotate in web app, all instances pick up on restart.
- **Layer 2 — iron-proxy egress firewall**: Agent gets opaque proxy tokens, not real credentials. Proxy swaps at network boundary. Sandbox compromise → attacker gets tokens that only work behind the proxy.
