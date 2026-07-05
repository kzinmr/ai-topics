---
title: "Polymarket Trading Agents"
type: concept
aliases:
  - polymarket-bots
  - prediction-market-agents
  - weather-trading-bots
tags:
  - concept
  - ai-agents
  - automation
status: complete
description: "AI agents used for automated trading on Polymarket prediction markets — weather, crypto, sports. Self-learning bots that operate 24/7 with no emotions."
created: 2026-04-27
updated: 2026-05-27
sources:
  - "https://x.com/i/article/2045080054917476451"
related:
  - "[[concepts/harness-engineering]]"
  - "[[entities/hermes-agent]]"
  - "[[concepts/self-learning-agents]]"
---

# Polymarket Trading Agents

> **Definition:** Polymarket is a prediction market platform where AI agents autonomously trade in weather, cryptocurrency, and sports markets. Agents operate 24/7, have no emotions, and remember everything.

## Notable Agent Examples

| Agent | Market | Results |
|-------------|------|------|
| ColdMath | Weather | $300 → $219K (3 months) |
| Sharky6999 | Crypto | $819K PnL, 99.3% win-rate |
| RN1 | Sports | $1.2K → $7.3M |

## Agent Advantages
- No sleep, no emotions, remembers everything
- The right algorithm and execution speed are everything
- Automated self-learning AI agents have a strong edge

## Building a Weather Trading Bot (with Hermes Agent)

### Prerequisites
- Hermes Agent (built by Nous Research, released February 25, 2026)
- VPS (Hetzner recommended)
- Polymarket wallet (Polygon network)
- Weather API (VisualCrossing free API)

### Build Steps
1. **Clone & Setup** — Clone the open-source bot by AlterEgo
2. **Create Wallet** — Set up a dedicated wallet
3. **Fund** — $ USDC.e (trading capital) + $ POL (gas fees)
4. **Approve Polymarket Contracts** — Allow bot to use funds
5. **Connect Weather API** — Set up VisualCrossing API key
6. **Test Scan** — Test in paper-trading mode
7. **Start Real Trading** — Self-learning weather trading bot goes live

### How It Works
- Scans 20 cities across 4 continents
- Integrates 3 forecast sources with Expected Value and Kelly Criterion position sizing
- Self-improves with each trade (not a fixed script)

## Sources
- [Hermes Agent + Polymarket - how i built self-learning weather trading bot $100 → $5,000](https://x.com/i/article/2045080054917476451) (2026-04-25, X article)
