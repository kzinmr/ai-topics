---
title: "Project Mariner — Google DeepMind's Web Browsing Agent"
created: "2026-05-06"
updated: "2026-05-06"
type: entity
tags: [ai-agents, google, product, agentic-browsing]
sources: [raw/articles/2026-05-06_wired-google-project-mariner-shakeup.md]
---

# Project Mariner — Google DeepMind's Web Browsing Agent

**Project Mariner** is a research prototype developed by [[entities/google|Google DeepMind]] that explores human-agent interactions within web browsers. It automates tasks such as online shopping, information retrieval, and form-filling.

## Timeline

| Date | Event |
|------|-------|
| December 2024 | Initial research prototype unveiled |
| May 2025 | Released to Google AI Ultra subscribers (US) |
| 2026 | Team reorganization; capabilities folded into broader Google agent strategy |

## Technical Architecture

- **Engine**: Gemini 2.0 / Gemini 2.5 / Gemini 3
- **Platform**: Chrome extension + cloud-based VMs
- **Capabilities**: Screen understanding, multi-step reasoning, cursor manipulation, form-filling
- **Safety**: Single active tab only, user-visible actions, user can intervene at any time
- **Benchmark**: 83.5% on WebVoyager (May 2026); handles 10 concurrent tasks on cloud VMs

## Integration into Google's Agent Strategy

As of mid-2026, Mariner's computer use capabilities are being incorporated into Google's broader agent strategy:
- **Gemini Agent** — built on insights from Project Mariner, powered by Gemini 3's advanced reasoning
- **Gemini Enterprise Agent Platform** (rebranded from Vertex AI at Cloud Next 2026) — includes Mariner's web browsing capabilities
- **Roadmap**: Mariner Studio (Q2 2026), cross-device sync (Q3 2026), agent marketplace (Q4 2026)

## Team Reorganization

WIRED reported that Google is shaking up the Project Mariner team, with some Google Labs staffers who worked on the research prototype moving to higher-priority projects. This reflects the broader industry shift toward **coding agents** (Claude Code, Cursor, Codex) over browser agents.

## Related

- [[entities/google]] — parent organization
- [[concepts/agentic-browsing]] — web browsing agent paradigm
- [[entities/gemini-enterprise-agent-platform]] — Google's enterprise agent platform incorporating Mariner capabilities
- [[concepts/agent-sandboxing-patterns]] — sandboxing for agent execution
