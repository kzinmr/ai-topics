---
title: "DeerFlow"
created: 2026-06-22
updated: 2026-06-22
type: concept
tags:
  - deer-flow
  - bytedance
  - harness-engineering
  - agent-runtime
  - multi-agent
  - sandbox
  - open-source
  - coding-agents
  - china
  - hn-popular
  - deep-research
  - skill-graph
sources:
  - raw/articles/2026-06-22_bytedance-deerflow-superagent-harness.md
  - https://github.com/bytedance/deer-flow
  - https://x.com/RituWithAI/status/2068918767430869368
---

# DeerFlow

**DeerFlow** (Deep Exploration and Efficient Research Flow) is ByteDance's open-source SuperAgent harness that orchestrates sub-agents, memory, and sandboxes to handle complex, long-horizon tasks ranging from minutes to hours. Version 2.0 is a ground-up rewrite sharing no code with v1. Claimed #1 on GitHub Trending on February 28, 2026.

## Architecture

DeerFlow v2.0 is a backend (Python 3.12+) + frontend (Node.js 22+) system deployable via Docker, released under the MIT license. As of June 2026, the project has accumulated 72,935 GitHub stars and 9,867 forks.

Core architectural components:

- **Sub-agents**: Task decomposition with both parallel and sequential execution. The harness spawns specialized sub-agents that each operate within their own sandboxed environment.
- **Sandboxed Agent Computers**: Each agent receives a real filesystem, bash terminal, package installation capability, and code execution environment. This is a distinguishing feature — agents aren't limited to tool-calling APIs but operate in full-fledged OS environments.
- **Memory**: Long-term and short-term memory systems for maintaining context across extended task execution.
- **Skills**: Extensible, progressively loaded skill files. Only the skills needed for the current task are loaded, reducing context overhead.
- **Message Gateway**: Central routing layer for inter-agent communication.
- **Multi-model Support**: Recommends Doubao-Seed-2.0-Code and DeepSeek v3 for coding workflows, with additional support for Kimi 2.5, OpenAI models, and Gemini.

## The "Agent Gets Its Own Computer" Model

DeerFlow's most distinctive design choice is giving each agent a complete computer environment rather than a narrow tool API. This includes:

- **Real filesystem**: Agents read and write files as a human developer would
- **Bash terminal**: Full shell access for running build tools, tests, and system commands
- **Package installation**: Agents can install dependencies (pip, npm, apt) as needed
- **Code execution**: Execute and debug code in the native environment

This design philosophy contrasts with lighter-weight agent harnesses (see [[concepts/agent-harnesses]]) that favor minimal abstraction. DeerFlow instead provides a "batteries-included" runtime that trades simplicity for comprehensive capability — a different point on the harness spectrum from the [[concepts/bitter-lesson-agent-harnesses|minimal agent architecture]] approach.

## Agent Orchestration Model

DeerFlow implements a planning-then-execution model:

1. **Plan**: The harness reasons through task complexity and generates a plan with sub-tasks
2. **Orchestrate**: Sub-agents are spawned with appropriate skills, memory context, and sandbox environments
3. **Execute**: Tasks run sequentially or in parallel, with persistent sandbox state maintained between steps
4. **Integrate**: Results from sub-agents are collected and synthesized

This model handles tasks spanning minutes to hours, making it suitable for deep research, multi-file code generation, and complex data analysis workflows.

## Version History

- **v1**: Original release (now superseded)
- **v2.0** (February 2026): Ground-up rewrite with no shared code. Introduced the sandboxed agent computers model, skills architecture, and message gateway. Immediately claimed #1 GitHub Trending.
- Partnership with BytePlus/Volcengine for cloud deployment infrastructure
- Official site: [deerflow.tech](https://deerflow.tech) — with live demos

## Position in the Agent Harness Landscape

DeerFlow occupies a distinct niche in the agent harness ecosystem:

| Dimension | DeerFlow | [[concepts/agent-harnesses|Minimal Harnesses]] | [[concepts/deep-agents-runtime|Deep Agents]] |
|---|---|---|---|---|
| Abstraction level | High (batteries included) | Minimal (just a loop) | Medium (runtime primitives) |
| Sandbox model | Full OS per agent | Usually none or Docker | Managed sandboxed execution |
| Sub-agent model | First-class with own computers | Model-driven delegation | Managed sub-agent spawning |
| Target tasks | Minutes to hours | Variable | Production long-running |
| Origin | ByteDance (China) | Various (Browser Use, etc.) | LangChain/Anthropic |

This represents a broader trend of Chinese tech companies entering the agent infrastructure space with substantial, well-engineered open-source contributions — complementing efforts from [[entities/deepseek|DeepSeek]], [[concepts/qwen|Alibaba (Qwen)]], and [[entities/xiaomi|Xiaomi (MiMo)]].

## Related Pages

- [[entities/bytedance]] — ByteDance, parent company and creator of DeerFlow
- [[concepts/sandbox]] — Agent sandboxing and isolation techniques
- [[concepts/agent-harnesses]] — The broader agent harness philosophy and spectrum
- [[concepts/deep-agents-runtime]] — Production agent runtime primitives
- [[concepts/deerflow]] — Earlier DeerFlow entry (v1 era coverage)
- [[entities/deepseek]] — DeepSeek v3, recommended coding model for DeerFlow
