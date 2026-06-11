---
title: Manus
type: entity
aliases:
- manus-ai
- manus-browser-operator
- monica-im
created: 2026-04-13
updated: 2026-05-06
tags:
  - entity
  - developer-tooling
  - browser-agent
  - company
status: active
sources:
- https://manus.ai/features/manus-browser-operator
- https://chatgptguide.ai/manus-browser-operator-agentic-workflows/
- https://manus.im/blog/manus-browser-operator
- https://www.taskade.com/blog/manus-ai-review
---

# Manus

**Manus** is a general-purpose AI agent developed by Chinese startup Monica.im, founded by former Alibaba/ByteDance engineers. It gained attention through a viral demo in March 2025, capable of autonomously executing browser operations, code execution, and file creation on a virtual computer. In November 2025 it released the **Browser Operator** feature, and was **acquired by Meta** in 2026.

## Overview

| Field | Details |
|---|---|
| Founded | 2024 (Monica.im) |
| Founder | Former Alibaba/ByteDance engineers |
| Acquisition | 2026, by Meta |
| Viral demo | March 2025 (flight booking, coding, etc.) |
| Access | Invite-only (initial), later opened to all users |

## Manus Cloud Computer (May 2026)

Manus launched an **always-on cloud machine** that keeps bots, scripts, and agents running even when the user's local computer is offline:

- **Always-on execution**: Agents continue running on cloud infrastructure regardless of local machine state
- **Use cases**: Scheduled jobs, long-running agent tasks, background automation
- **Significance**: Removes the local-computer dependency from agent execution — a step toward persistent autonomous agent infrastructure
- **Ecosystem context**: See [[entities/flue]] for TypeScript agent frameworks; [[entities/vercel]] for cloud-native agent deployment

## Manus Browser Operator (November 2025~)

Manus's key differentiator is agent execution through a **local browser extension**. Rather than running in a cloud sandbox, it operates on the user's actual browser.

### 3-Step Process
1. **Connect Browser**: Enable "My Browser" connector, install extension
2. **Grant Access**: Grant permission for multi-step task execution (one-time auth)
3. **Autonomous Action**: Execute tasks in browser, real-time monitoring via dedicated tab

### Key Features
- ✅ **Authenticated sessions**: Inherits login state, cookies, access to paid tools
- ✅ **Local IP**: Recognized as trusted environment access (advantageous for CAPTCHA avoidance)
- ✅ **Full transparency**: All actions logged with audit trail
- ✅ **Instant abort**: Close the tab to stop the task
- ✅ **Remote monitoring**: Check task progress from phone when main PC is online

### Strengths
- **Premium data sources**: Crunchbase, PitchBook, SimilarWeb, Financial Times, Semrush, Ahrefs
- **B2B data analysis**: CRM operations, market research, SEO analysis
- **Internal dashboards**: Working with enterprise authenticated tools

### Limitations
- Drag-and-drop and complex multi-step forms not yet supported
- No persistent memory (due to virtual computer model)
- Access to sensitive information requires prior review

## Architecture Comparison

| Dimension | Cloud Browser | Browser Operator (Local) |
|---|---|---|
| Execution environment | Isolated sandbox | User browser |
| Login | Not possible (hits paywalls) | Can inherit |
| CAPTCHA | Problematic | Easier to avoid |
| Paid tools | No access | Can use subscribed tools |
| Monitoring | Limited | Real-time (dedicated tab) |
| IP trust | Low | High (local IP) |

## Acquisition and Future

Meta announced the acquisition in 2026, described as a strategic move to "democratize AI for business." Integration with Meta's AI agent ecosystem is expected.

## Related Entities

- [[entities/anthropic-computer-use]] — Anthropic Computer Use
- [[entities/openai-cua]] — OpenAI Computer-Using Agent
- [[entities/browser-use]] — Open-source browser automation
- [[concepts/browser-agent/death-of-browser]] — The de-humanization of the browser
- [[entities/webmcp]] — Standardization protocol

## Sources

- [Manus Browser Operator](https://manus.ai/features/manus-browser-operator)
- [Introducing Manus Browser Operator](https://manus.im/blog/manus-browser-operator)
- [Manus AI Review 2026 (Taskade)](https://www.taskade.com/blog/manus-ai-review)
- [Manus Browser Operator Explained](https://chatgptguide.ai/manus-browser-operator-agentic-workflows/)
