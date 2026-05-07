---
source: x.com
url: https://x.com/vtrivedy10/status/2052100726608781363
author: Viv Trivedy (@Vtrivedy10)
published: 2026-05-06T18:58:34Z
type: x_note_tweet
tags: [agent-harness, harness-engineering, evals, unbundled-agents, general-purpose-agents, open-models, context-window]
---

# Strong Opinions, Loosely Held on Agent + Harness Engineering

By Viv Trivedy (@Vtrivedy10), May 6, 2026

## The 8 Points

1. **Harness over model**: You can outperform any default harness+model (including Codex & Claude Code) on pretty much any Task by engineering the harness around it. Using the exact same model, curate prompts, tools, skills, hooks for that Task. This harness optimization process is becoming much more agent driven with humans reviewing and curating evals/rewards to hill climb on. "Just say what you want".

2. **"General purpose" doesn't really exist**: It's a tradeoff between time spent on customizing the agent and performance (cost, latency, accuracy) on a Task. Who decides what's general and what's not?

3. **If it did exist**: A general purpose agent/harness would look like a good coding agent.

4. **Convergence on Skills**: Building a Task specific harness will most likely converge to good prompt & tool design (probably packaged up as a Skill) as models become smarter and better at in-context learning.

5. **Evals are a moat**: Data to produce evals is a moat. Especially true for vertical agent companies. Agents can fit to most Eval sets today. If Evals measurably encode all the good behavior your agent needs to do, then this signal can be hill climbed to improve your agent.

6. **Frontier closed models too expensive**: Far too expensive for the large majority of tasks the world needs to do. As teams start mapping costs to ROI, Open Model Harness Engineering will take off even more. It is almost always worth the investment to at least try to get a potential 20x+ cost reduction.

7. **Context window drives architecture**: A large chunk of design decisions around Task decomposition and context engineering exist solely because our usable context window is 50-100k. Agents that become excellent at breaking down tasks, applying compaction appropriately, and orchestrating subagents as sub-task workers will be the most delightful products.

8. **Age of Unbundled (& Rebundled) Agents**: Subagents exposed as Tools do domain-specific work on behalf of an orchestrator agent. The Harness becomes a box populated with the exact set of tools, skills, and subagents needed. Examples: WarpGrep (search), Chroma Context-1 (search), Nemotron 3 Omni (small multimodal), and software-as-tools via Skills (Remotion, Blender).

## Key Insights

- The "Harness Effect" — same model, different harness = dramatically different performance
- Skills as the packaging format for harness optimization
- Evals → data → moat flywheel for vertical agents
- Open model cost advantage (20x+) driving harness engineering investment
- Subagent-as-tool architecture as the emerging paradigm
