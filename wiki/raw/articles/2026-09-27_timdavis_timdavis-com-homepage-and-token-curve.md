---
title: "Tim Davis — homepage bio, essay list, and The Token Curve / GPU-loan essays"
source: "timdavis.com (via Jina Reader)"
date: 2026-09-27
scraped: 2026-09-27
type: web-snapshot
url: https://www.timdavis.com/
authors: ["Tim Davis"]
tags: [ai-infrastructure, gpu-financing, token-economics, agentic-engineering, career]
---

# Tim Davis — homepage bio, essay list, and two 2026 essays

**Scraped**: 2026-09-27 via `r.jina.ai` (homepage, The Token Curve, Every GPU loan is really a software loan)

## Homepage bio (verbatim, 2026-09-27)

- Tim Davis co-founded [Modular](https://www.modular.com/), whose mission is to create an AI hardware abstraction layer for the world. Modular was [acquired by Qualcomm in July 2026](https://www.qualcomm.com/news/releases/2026/07/qualcomm-completes-acquisition-of-modular). He is now a **SVP & GM of Modular at Qualcomm**.
- Previously he served as a PM at Google, helping to create & scale AI systems inside Google Brain including infrastructure like TensorFlow, on-device AI & large model infrastructure.
- Tim studied Engineering, Finance and Law in Australia and the US, and now resides in California. He is an active angel investor in AI startups.

## Essay bibliography (from blog index, 2026-09-27)

### Essays
- **The Token Curve** (2026-08-17)
- **Every GPU loan is really a software loan** (2026-07-26)
- **Probabilistic engineering and the 24-7 employee** (2026-04-16) — already ingested: [[raw/articles/2026-04-16_timdavis_probabilistic-engineering-24-7-employee.md]]
- **What we owe the minds we create** (2025-10-13)
- **Scale or Surrender: When watts determine freedom** (2025-06-06)
- **AI Regulation: step with care, and great tact** (2023-09-26)
- **The career opportunity matrix** (2019-10-12)

### Interviews (selected)
- **EE Times: Why Qualcomm Bought An Open AI Software Stack** (2026-07-30)
- **Australian entrepreneur sells AI start-up Modular for $4B+** (2026-06-25)
- **Qualcomm Buys Buzzy Chip Startup Modular** (2026-06-24)
- **The "Android Moment" for AI: Why Modular Raised $250M to Break GPU Lock-In** (2025-11-26)
- **The Aussie conquering Silicon Valley** (2023-09-22)

### Short posts (funding timeline)
- Founding Modular & raising $30M (2022-01-04)
- Modular raised $100M to fix AI infrastructure (2023-08-24)
- Modular raised $250M to scale AI's Unified Compute Layer (2025-09-24)
- MLIR — Open Source Infrastructure for the world (2020-08-24)

## The Token Curve (2026-08-17) — key content

Core thesis: **financing terms set the cost floor for every token served, and heterogeneous compute will materially reprice the long-contracted GPU market.**

- Portability does not create heterogeneous compute — it turns heterogeneous capacity that already exists into supply the market can actually use. Once enough of it is production-ready at scale, it resets the marginal cost of inference and reprices fixed GPU commitments.
- Three measurements of "demand" growing at different rates:
  1. **Usage volume** (tokens actually served) — compounding on one of the fastest adoption curves recorded
  2. **Inference revenue** — volume × falling realized prices, grows much slower than volume
  3. **Infrastructure investment (capex)** — a forward capital commitment against forecasts of both; the least direct proxy of demand
- Token cost equation: `required token cost = (capital recovery + power + operations) ÷ effective tokens produced`. Competition, not financing terms, sets market price.
- Data: Google served 9.7T tokens/month (May 2024) → ~480T (May 2025) → 3.2 quadrillion+ (May 2026). Alphabet capex $52.5B (2024) → $91.4B (2025) → ~$200B guided (2026). Result: capex per million tokens served fell ~$451 → $16 → $5 — a ~90x fall in capex intensity in two years while capex nearly quadrupled, because the demand denominator grew ~330x.
- Constant-capability price envelope anchored at GPT-4-class output ≈ $60/M tokens (Mar 2023), falling ~10x/year (same slope a16z documents for GPT-3-class; task-level rates vary 9x–900x per Epoch).
- Two curves: the **market token curve** (price of a standardized task, moved most by open-model competition) vs the **portable cost curve** (break-even cost of a fixed checkpoint across whatever qualified hardware is cheapest, moved by silicon portability). The "Token Curve" is the gap between what the market pays and what it costs to produce.
- References BIS (Bank for International Settlements) measuring the financing gap between arriving inference revenue and committed capital.

## Every GPU loan is really a software loan (2026-07-26) — key content

Core thesis: **a GPU loan is only as good as the next operator's ability to run the software stack** — what a lender repossesses is worth far less than the silicon unless software portability lets a new owner put the machines back to work.

- Not a bubble essay; an essay about what makes compute *financeable* at all. Takeaway: it's mostly software, not silicon.
- "Portability" defined in three senses:
  1. **Workload portability** — a model can move across different silicon with bounded cost in performance, correctness, engineering effort
  2. **Operational transferability** — a qualified third party can take over a running cluster and keep it earning
  3. **Asset liquidity** — the hardware can find a new operator or buyer at an observable price
- Frame: the flow of funds is where underlying risk is forced into a price; debt-market underwriting of AI hardware reveals the real fungibility of compute.
