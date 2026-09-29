---
title: Kyle Corbitt
type: entity
aliases:
  - Kyle Corbett
  - corbtt
created: 2026-06-10
updated: 2026-09-29
tags:
  - person
  - reinforcement-learning
  - ai-agents
  - coding-agents
sources:
  - https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
  - https://openpipe.ai/
  - raw/articles/corbt.com--codex-file-my-taxes-make-no-mistakes--2026-09-29.md
---

# Kyle Corbitt

| | |
|---|---|
| **Company** | [OpenPipe](https://openpipe.ai/) (CTO) |
| **Focus** | RL post-training for custom agent models |
| **Background** | Y Combinator, Google |
| **X/Twitter** | [@corbtt](https://x.com/corbtt) |

## Overview

Kyle Corbitt is the **CTO of OpenPipe**, an RL post-training company that helps organizations train custom models optimized for their specific agentic tasks. OpenPipe's approach enables companies to move beyond generic API calls to task-specialized models that outperform frontier models on domain-specific workloads.

Before OpenPipe, Corbitt gained ML experience at **Y Combinator** and **Google**, giving him a unique perspective bridging startup velocity with large-scale ML infrastructure.

## Key Work

### OpenPipe
OpenPipe provides RL post-training as a service — enabling companies of all sizes to train custom models optimized for their specific tasks. The company's core thesis is that most AI companies will eventually want post-training models focused on their particular workflows, rather than relying solely on generic frontier model APIs.

### Production-Ready Agent Engineering Course (Maven)
In 2026, Corbitt co-created and co-teaches **"Production-Ready Agent Engineering: From MCP to RL"** with [[entities/will-brown]] on Maven. The course covers the full stack of production agent engineering — from tool design via MCP to RL optimization with GRPO.

See [[concepts/agents-mcp-rl-course]] for full course details.

### Codex vs Accountant: Filing Taxes Autonomously (Sep 2026)

In **"Codex, File My Taxes. Make No Mistakes."** (corbt.com, 2026-09-29), Corbitt tested his 2025 prediction that "the best coding agent of early 2026 would be able to file my taxes autonomously" — in parallel with a $2,000+ human accountant, after selling OpenPipe-coreweave made his return unusually complex (7 income sources, four K-1s, WA capital gains, three compensation types).

Workflow: dictated a 10-minute unstructured braindump via Handy; Codex (GPT-5.3-Codex at the time — chosen over Claude because "Opus is slightly more likely to quietly cut corners on hard problems") built fact-finding question lists, researched IRS guidance interactively, kept a running `taxes/2025/README.md` checklist, and gathered forms from email/institution websites (Playwright MCP; Claude was unusable here since it blocks banking sites). When Codex initially refused to write a tax engine from scratch, Corbitt pushed anyway — ~30 minutes later it produced a Python engine that ingested his forms and filled the actual 1040 packets.

**Result: Codex caught a $20,000 error the accountant missed** — a deferred "adjustment escrow" payment buried in 214 pages of acquisition documents that the accountant had omitted; re-running the engine with the payment excluded matched the accountant's estimate within dollars. Cost comparison: accountant $2,000+ / 2–3-day turnaround / made a $20k mistake; Codex $20/mo / immediate interactive research / caught the mistake. He open-sourced the engine ([github.com/corbt/2025-tax-engine](https://github.com/corbt/2025-tax-engine), explicitly unreviewed) and predicts a high-quality open-source tax engine by 2027.

Raw: [[raw/articles/corbt.com--codex-file-my-taxes-make-no-mistakes--2026-09-29]]

## Related

- [[entities/will-brown]] — Co-instructor, Research Lead at Prime Intellect
- [[concepts/agents-mcp-rl-course]] — Their joint Maven course
- [[entities/openpipe]] — Corbitt's company (RL post-training)
- [[concepts/agentic-rl]] — Core topic of the course
- [[concepts/post-training/grpo-rl-training]] — Key RL algorithm taught
- [[entities/prime-intellect]] — Partner organization providing GPU credits

## Sources

- [Maven Course Page](https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl)
- [OpenPipe](https://openpipe.ai/)
