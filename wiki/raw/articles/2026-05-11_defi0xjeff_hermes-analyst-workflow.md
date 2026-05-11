---
title: "Hermes Analyst Workflow Essentials"
source: https://defi0xjeff.substack.com/p/hermes-analyst-workflow-essentials
author: 0xJeff
date: 2026-05-11
scraped: 2026-05-11
tags: [hermes-agent, agent-harness, workflow, personal-ai, analyst]
x_article_id: 2053753720693825536
x_author: "@0xJeff"
type: raw_article
---

# Hermes Analyst Workflow Essentials

**Author:** 0xJeff
**Date:** May 11, 2026
**Series:** Part V — Training Hermes as a Personal Analyst

Hermes recently achieved the #1 spot on OpenRouter global ranking. It's the best agent harness in the market. After extensive experimentation, 0xJeff shares what gives the best ROI.

## The Three-Layer Stack

**Layer 1 — Identity (Soul.md)**: Who the agent IS. Personality, voice, constraints, values, knowledge of the user. Takes 2-3 hours to write well and you'll revise it 5+ times. Highest ROI.

**Layer 2 — Knowledge (User.md + Memory)**: What the agent KNOWS about you. Portfolio, theses, preferred sign-offs, past mistakes. Compounds every session.

**Layer 3 — Tools (Config + Skills)**: What the agent CAN DO. API keys, cron jobs, browser access. Table stakes — makes the agent capable but not differentiated.

## Model Configuration

- Start with Opencode Go ($5/month, includes Kimi k2.6 & GLM5.1 for complex tasks, MiniMax 2.5-2.7 for basic tasks)
- Continue with DeepSeek (75% discount on v4 Pro in May, v4 Flash for basic tasks)
- Free OpenRouter models are unreliable (rate-limited, slow)
- Two critical files: config.yaml (model provider + API key) and .env (environment variables)

## Key Workflows

1. **Daily Briefing**: X Bookmark Briefing (Hermes queries bookmarks, scores, prioritizes) + Top 5 Daily Synthesis
2. **Deep Research**: Context-rich analysis across multiple sources
3. **Reporting**: Automated cron-based report generation
