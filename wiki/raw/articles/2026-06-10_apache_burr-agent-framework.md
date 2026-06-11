---
title: "Apache Burr: Build Reliable AI Agents and Applications"
url: https://burr.apache.org/
fetched_at: 2026-06-11T12:00:00Z
source: web
tags: [blog, raw]
note: "JS-rendered Next.js site. Text content extracted from HTML metadata, headings, code samples, features section, testimonials, and community links. Numbers (stars, downloads, members) rendered client-side as 0 in static HTML. GitHub API used as supplementary source."
---

# Apache Burr (Incubating) - Build Reliable AI Agents and Applications

## Source: https://burr.apache.org/

### Meta Description
Apache Burr (Incubating) makes it easy to develop applications that make decisions,
from simple chatbots to complex multi-agent systems. Pure Python, no magic.

### GitHub Stats (from GitHub API, 2026-06-11)
- **Stars**: 2,256
- **Forks**: 163
- **Language**: Python
- **License**: Apache-2.0
- **Topics**: ai, burr, chatbot-framework, dags, generative-ai, graphs, hacktoberfest, llmops, llms, mlops, persistent-data-structure, state-machine, state-management, visibility
- **Open Issues**: 102
- **Created**: 2024-01-29
- **Last Updated**: 2026-06-11

### Key Features (from website)

1. **Simple Python API** — Define your application as a set of actions and transitions. No DSL, no YAML — just Python functions and decorators.

2. **Built-in Observability** — The Burr UI lets you monitor, debug, and trace every step of your application in real time. See state changes as they happen.

3. **Persistence & State Management** — Automatically persist state and replay from any point. Debug production issues by replaying exact states.

### Code Example (from website)

```python
from burr.core import action, State, ApplicationBuilder

@action(reads=["messages"], writes=["messages"])
def chat(state: State, llm_client) -> State:
    response = llm_client.chat(state["messages"])
    return state.update(
        messages=[*state["messages"], response]
    )

app = (
    ApplicationBuilder()
    .with_actions(chat)
    .with_transitions(("chat", "chat"))
    .with_state(messages=[])
    .with_tracker("local")
    .build()
)

app.run(halt_after=["chat"], inputs={"llm_client": client})
```

### Status
- Apache Incubating project (sponsored by Apache Incubator)
- Listed integrations include multiple LLM providers and tools

### Companies Using Burr (from website)
- Peanut Robotics
- Watto.ai
- Paxton.ai
- Provectus
- TaskHuman

### Community Channels
- Discord: https://discord.gg/6Zy2DwP4f3
- GitHub: https://github.com/apache/burr
- Twitter/X: https://x.com/burr_framework
- YouTube: https://www.youtube.com/@DAGWorks-Inc

### Testimonials (from website)

> "I have been using Burr over the past few months, and compared to many agentic LLM platforms out there (e.g. LangChain, CrewAi, AutoGen, Agency Swarm, etc), Burr provides a more robust framework for designing complex behaviors."
> — **Hadi Nayebi**, Co-founder, CognitiveGraphs

> "Moving from LangChain to Burr was a game-changer! It took me just a few hours to get started with Burr, compared to the days and weeks I spent trying to navigate LangChain. I pitched Burr to my teammates, and we pivoted our entire codebase to it."
> — **Aditya K.**, DS Architect, TaskHuman

> "Of course, you can use it [LangChain], but whether it's really production-ready and improves the time from code-to-prod, we've been doing LLM apps for two years, and the answer is no. Honestly, take a look at Burr. Thank me later."
> — **Reddit User**, r/LocalLlama

---

## Source: HN Discussion (June 10, 2026) — 227 points

### Context
Apache Burr was featured on Hacker News on June 10, 2026. The discussion centered on whether agent frameworks are necessary and Burr's positioning in the ecosystem.

### Key HN Comments

**On building without frameworks:**
> "I just created an MVP chatbot for a client... took the route of no frameworks. Claude/codex wrote the agent loop."
— A developer argued that an agent is fundamentally "context building, making an LLM call, executing requested tool calls" — not THAT complicated.

**On Apache incubation:**
> "First time I hear about Burr, curious why it was incubated in Apache."
— Several commenters were unfamiliar with Burr and questioned the Apache incubation pathway.

**Comparisons raised:**
- Comparison to StrandsAgents
- Comparison to Bedrock + Serverless Agent Core
- Debate on whether agent frameworks are necessary at all

### Naming
- Named after Aaron Burr, referencing the musical *Hamilton*
- The framework builds on Hamilton, another DagWorks project (a micro-framework for defining dataflows)
- The naming pattern: Hamilton → Burr (both characters from the musical)

### Key Takeaway
The HN community showed significant interest (227 points) but also healthy skepticism about whether agent frameworks add value or just add complexity to what is fundamentally a simple loop.
