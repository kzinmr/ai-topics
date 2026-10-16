---
source_url: https://openai.com/index/third-moment-research
ingested: 2026-10-15
sha256: 2d68e37c4a3a00d60d84fd9a087dc3af1a71e9b665269ea19262b8a12419f9ea
---

Every company has its own workflows, tools, edge cases, and definitions of success.[⁠(opens in a new window)](https://thirdmomentresearch.com/)[Third Moment Research⁠(opens in a new window)](https://thirdmomentresearch.com/) believes the best agents should be really good at that specific work and should improve their capabilities the more they’re used.

The company is building a self-improving AI system around that idea, using OpenAI’s latest models to understand agent behavior, identify recurring weaknesses, and automatically create thousands of synthetic scenarios around those problems. The team uses those scenarios to improve agents, repeating the process as new issues emerge.

Codex, GPT‑6 Astra, GPT‑6 Sol, and GPT‑6.1 Sol support the system’s research and computational work, enabling Third Moment to run 10,000 agents at once on investigations lasting 36-48 hours. The company also uses Daybreak to test the security of the environments where agents work.

> “In a single session, GPT-6.1 Sol is able to maintain a coherent thread of computational research across days of compute without losing the plot.”

—Adam Khakhar, Co-founder, Third Moment Research

## Reducing runtime and token waste with Codex

One of Third Moment’s early applications is in the field of quantitative finance given the clear measure of success. This domain provides a concrete setting to study how agents work and where they struggle. The team uses Codex to find and address problems in the research environment.

In one instance, it used Codex with GPT‑5.6, the latest GPT model at the time, to analyze thousands of recorded simulation trajectories (the agents’ actions and the environment’s responses) alongside timestamps and the codebase.

Codex uncovered a bottleneck: backtesting a trading strategy across a year of order-level US equity data took several hours. While waiting, agents repeatedly polled for completion, wasting tokens and filling their context with status checks.

After profiling the backtest and analyzing its inputs and usage, Codex identified a caching optimization and a memory-packing technique. It experimented with solutions and deployed the fix to production, reducing the backtest from approximately 3 hours to approximately 3 to 5 minutes. This reduced token use and context pollution, freeing more of the agents’ token budget for further experiments.

## Keeping agents on task with Codex and GPT‑6

Third Moment gives each agent the tools, information, and environment it needs for a specific job. For quantitative research, the team runs the default Codex harness inside a Dockerized environment. Agents receive a terabyte of data, documentation, and a research repository with modules for feature engineering, GPU-supported model training, trading strategies, and simulation.

GPT‑6 Astra, GPT‑6 Sol, and GPT‑6.1 Sol provide the reasoning, while the Codex harness gives agents tools to act, create plans, set objectives, spawn subagents, and compact context as work continues.

To address agents that stop before completing a task, Third Moment treats Codex as a subagent within an outer harness powered by GPT‑6 Sol or GPT‑6.1 Sol. The outer harness examines the trajectory when a task is left unfinished and determines whether to retry, terminate the job, or escalate to human review.

> “The Codex harness is extremely versatile, and it enables use across many different domains.”

—Adam Khakhar, Co-founder, Third Moment Research

In that research environment, agents work to improve a baseline trading system built by Third Moment’s engineers. They test trading strategies on historical data, assess whether an improvement is meaningful or noise, and use each result to choose the next experiment. According to Adam, their work has improved the baseline trading system.

## Sustaining longer research with greater token efficiency

Before GPT‑5.5, Adam says models could only execute experiments prescribed by a user. With GPT‑5.5 and GPT‑5.6, models working with the Codex harness could use results to design follow-up experiments. Now with GPT‑6 Astra, GPT‑6 Sol, and GPT‑6.1 Sol, agents can investigate root causes through hundreds of experiments running in parallel with subagents.

That progression has helped agents explore research directions the team hadn’t anticipated. In one session, GPT‑6.1 Sol identified the impact of non-displayed trades on an exchange where those trades accounted for an unexpectedly large share of volume. “This was an unobvious result that our research team did not initially consider,” says Adam.

Third Moment evaluates models across optimization, machine learning systems, and quantitative research. It tests frontier releases at their highest reasoning settings, assessing their ability to navigate repositories, write efficient code, and sustain an investigation. Current testing also includes GPT‑6 Luna.

> “GPT-6.1 Sol is currently our most-used model given its token efficiency. It completes tasks with the fewest tokens while delivering performance similar to GPT-6 Astra.”

—Jeffrey Yan, Co-founder, Third Moment Research

One benchmark asks agents to reduce a live scoreboard service’s update latency while preserving its outputs. The team measures speedup by dividing the average runtime of an expert-crafted solution by that of the model’s solution on the same hardware, subject to correctness. GPT‑6 Astra delivered the biggest speedup, according to Adam.

For targeted work, including checks for specific security weaknesses in the simulation system, the team uses more efficient models like GPT‑5.6 Terra. For deep research, Adam believes stronger reasoning can justify higher cost: “In the space of quantitative finance, the value of finding some interesting signal is extremely high.”

## Automating security testing with Daybreak

With 10,000 agents running autonomously, Third Moment needs a way to test the security of its research environments at scale. The team uses the Daybreak cybersecurity platform to automate that testing before simulations launch.

The tests check whether an agent could break out of its research environment and access the wider network. “By using Daybreak, we’re able to have agents themselves do penetration testing on the simulation and test the infrastructure and security of it,” says Adam.

> “Without Daybreak, we would not be able to autonomously test this at scale.”

—Adam Khakhar, Co-founder, Third Moment Research

## Moving toward hundreds of thousands of collaborating agents

Third Moment’s ambition extends to the specialized work companies do every day. For a retailer, that could mean making better supply chain decisions when inventory is short or a supplier is delayed. For an engineering team, it could mean finding performance bottlenecks in a large codebase. For a document-heavy business, it could mean identifying where commitments in one document don’t match outcomes recorded in another.

Building on the reasoning capabilities of GPT‑6 Astra, GPT‑6 Sol, and GPT‑6.1 Sol, Third Moment plans to expand from individual investigations to hundreds of thousands of collaborating subagents. Its roadmap calls for trillions of tokens supporting chains of dozens of dependent experiments, with the goal of using that research to autonomously improve agents as new challenges arise.

For Adam, this would give people more capacity to shape how agents learn and work: “Humans can be in a much more leveraged position, where they can think about how to do research and optimize the research itself instead of actually doing the research.”
