---
title: "Mistral Medium 3.5 and Vibe Remote Agents"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [model, coding-agents, mistral, cloud, orchestration]
sources:
  - raw/articles/mistral-medium-3-5-vibe-remote-agents.md
  - https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
  - https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/
  - https://earezki.com/ai-news/2026-05-03-mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-35-with-776-swe-bench-verified-score/
  - https://rits.shanghai.nyu.edu/ai/mistral-medium-3-5-launches-with-vibe-remote-coding-agents/
  - https://www.aibusinessreview.org/2026/05/03/mistral-cloud-coding-agents-medium-3-5/
  - https://www.infoq.com/news/2026/05/mistral-agents-lechat/
---

# Mistral Medium 3.5 and Vibe Remote Agents

## Overview

On **April 29, 2026**, Mistral AI announced **Mistral Medium 3.5**, a **128B dense multimodal model** with a **256k context window**, alongside **Vibe Remote Agents** — cloud-based coding sessions that run asynchronously and in parallel. The model replaces Devstral 2 as the default in Mistral Vibe and Le Chat, and ships under a **modified MIT license** with open weights on Hugging Face.

## Mistral Medium 3.5 Model Details

- **Architecture**: 128B dense (not MoE), multimodal with vision encoder
- **Context Window**: Up to 256k tokens
- **License**: Modified MIT, open weights on Hugging Face
- **Performance**: 77.6% on SWE-bench Verified
- **Reasoning**: Configurable reasoning effort per request — short responses or longer multi-step executions
- **Inference**: Self-hostable on as few as 4 GPUs
- **Capabilities**: Instruction following, reasoning, coding, and vision in a single model

## Vibe Remote Agents

### Architecture

- **Cloud-based execution**: Coding sessions run in isolated sandboxes on remote infrastructure, not locally
- **Parallel sessions**: Developers can run multiple agents simultaneously
- **State teleportation**: Local CLI sessions can be "teleported" to the cloud with full history preserved
- **Async operation**: Agents run independently and notify users when work completes

### Integration Ecosystem

- **Mistral Vibe CLI**: Start coding tasks from command line
- **Le Chat**: Launch agents directly from web chat interface
- **Workflows**: Orchestrated via Mistral Studio
- **External tools**: Integrates with Linear, Jira, Sentry, Slack, and Teams
- **GitHub**: Agents can open pull requests directly when work completes

### Use Cases

- Module refactors
- Test generation
- Dependency upgrades
- CI investigations
- Bug fixes
- Multi-step research and analysis tasks

### Work Mode in Le Chat

New **Work mode** (Preview) extends Le Chat with a powerful agent for complex, multi-step tasks:
- Executes workflows across connected tools
- Accesses external data sources
- Performs analysis and generates reports
- Requires user approval for sensitive operations
- Sessions persist across multiple steps

## Strategic Significance

### Industry Positioning

Mistral's move into **cloud-based coding agents** represents a shift from model licensing to **agentic services**. This mirrors Anthropic's Claude agents and suggests industry convergence on cloud-based agent deployment as the preferred architecture for enterprise applications.

### Competitive Landscape

- **vs Claude Code**: Mistral offers cloud-native async execution; Claude Code is primarily local
- **vs Devin**: Vibe Remote Agents are task-specific, not full autonomous engineers
- **vs OpenAI Codex**: Mistral emphasizes self-hostability and open weights

### Enterprise Value Proposition

- **Compute efficiency**: Runs on 4 GPUs vs. cloud-only solutions
- **Developer workflow**: "Review results, not keystrokes" — async notification model
- **Cost optimization**: Self-hostable alternative to expensive cloud agent platforms
- **Integration flexibility**: Works with existing enterprise tools (Linear, Jira, GitHub)

## Key Dates

| Date | Event |
|------|-------|
| April 29, 2026 | Mistral Medium 3.5 released with open weights |
| April 30, 2026 | Vibe Remote Agents GA announcement |
| May 2026 | Industry coverage in MarkTechPost, InfoQ, NYU RITS |

## Related Pages

- [[entities/mistral-ai]] — Mistral AI company profile
- [[concepts/cloudflare-llm-infrastructure]] — Cloudflare's custom LLM inference stack
- [[entities/coding-agents]] — LLM-powered coding agents ecosystem
- [[concepts/agent-harness]] — Agent infrastructure layer concepts
- [[concepts/agentic-alternative-to-graphrag]] — Agentic tool-use vs. retrieval

## Sources

- [Mistral AI Official Announcement](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5)
- [MarkTechPost: 77.6% SWE-bench Score](https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/)
- [InfoQ: Remote Agents and Work Mode](https://www.infoq.com/news/2026/05/mistral-agents-lechat/)
- [NYU RITS: Launch Coverage](https://rits.shanghai.nyu.edu/ai/mistral-medium-3-5-launches-with-vibe-remote-coding-agents/)
- [AI Business Review: Cloud Coding Agents](https://www.aibusinessreview.org/2026/05/03/mistral-cloud-coding-agents-medium-3-5/)
