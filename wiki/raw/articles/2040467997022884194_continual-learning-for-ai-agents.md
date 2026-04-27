# Continual learning for AI agents

## Source

- X Native Article by @hwchase17
- Tweet ID: 2040467997022884194
- Article URL: https://x.com/i/article/2040467997022884194
- Tweet URL: https://x.com/hwchase17/status/2040467997022884194

## Article

Most discussions of continual learning in AI focus on one thing: updating model weights. But for AI agents, learning can happen at three distinct layers: the model, the harness, and the context. Understanding the difference changes how you think about building systems that improve over time.
The three main layers of agentic systems are:
Model: the model weights themselves.
Harness: the harness around the model that powers all instances of the agent. This refers to the code that drives the agent, as well as any instructions or tools that are always part of the harness.
Context: additional context (instructions, skills) that lives outside the harness, and can be used to configure it.
 
Example #1: Mapping this a coding agent like Claude Code:
Model: claude-sonnet, etc
Harness: Claude Code
User context: CLAUDE.md, /skills, mcp.json
Example #2: Mapping this to OpenClaw:
Model: many
Harness: Pi + some other scaffolding
Agent context: SOUL.md, skills from clawhub
When we talk about continual learning, most people jump immediately to the model. But in reality - an AI system can learn at all three of these levels.
Continual learning at the model layer
When most people talk about continual learning, this is what they most commonly refer to: updating the model weights.
Techniques to update this include SFT, RL (e.g. GRPO), etc.
A central challenge here is catastrophic forgetting — when a model is updated on new data or tasks, it tends to degrade on things it previously knew. This is an open research problem.
When people do train models for a specific agentic system (e.g. you could view the OpenAI codex models as being trained for their Codex agent) they largely do this for the agentic system as a whole. In theory, you could do this at a more granular level (e.g. you could have a LORA per user) but in practice this is mostly done at the agent level.
Continual learning at the harness layer
As defined earlier, the harness refers to the code that drives the agent, as well as any instructions or tools that are always part of the harness.
As harnesses have become more popular, there have been several papers that talk about how to optimize harnesses.
A recent one is **Meta-Harness: End-to-End Optimization of Model Harnesses.**
The core idea is that the agent is running in a loop. You first run it over a bunch of tasks, and then evaluate them. You then store all these logs into a filesystem. You then run a coding agent to look at these traces, and suggest changes to the harness code.
 
Similar to continual learning for models, this is usually done at the agent level. You could in theory do this at a more granular level (e.g. learn a different code harness per user).
Continual learning at the context layer
“Context” sits outside the harness and can be used to configure it. Context consists of things like instructions, skills, even tools. This is also commonly referred to as memory.
This same type of context exists inside the harness as well (e.g. the harness may have base system prompt, skills). The distinction is whether it is part of the harness or part of the configuration.
Learning context can be done at several different levels.
Learning context can be done at the agent level - the agent has a persistent “memory” and updates its own configuration over time. A great example is OpenClaw which has its own SOUL.md that gets updated over time.
Learning context is more commonly done at the tenant level (user, org, team, etc). In this case each tenant gets their own context that is updated over time. Examples include Hex’s Context Studio, Decagon’s Duet, Sierra’s Explorer.
You can also mix and match! So you could have an agent with agent level context updates, user level context updates, AND org level context updates.
These updates can be done in two ways:
After the fact in an offline job. Similar to harness updates - run over a bunch of recent traces to extract insights and update context. This is what OpenClaw calls “dreaming”.
In the hot path as the agent is running. The agent can decided to (or the user can prompt it to) update its memory as it is working on the core task.
 
Another dimension to consider here is how explicit the memory update is. Is the user prompting the agent to remember, or is the agent remembering based on core instructions in the harness itself?
Comparison
 
Traces are the core
All of these flows are powered by traces - the full execution path of what an agent did. LangSmith is our platform that (among other things) helps collect traces.
You can then use these traces in a variety of different ways.
If you want to update the model, you can collect traces and then work with someone like Prime Intellect to train your own model.
If you want to improve the harness, you can use LangSmith CLI and LangSmith Skills to give a coding agent access to these traces. This pattern is how we improved Deep Agents (our open source, model agnostic, general purpose base harness) on terminal bench.
If you want to learn context over time (either at the agent, user, or org level) - then your agent harness needs to support this. Deep Agents - our harness of choice - supports this in a production ready way. See the documentation there for examples of how to do user-level memory, background learning, and more.
Thank you to @sydneyrunkle @Vtrivedy10 @nfcampos for review and feedback on this article
