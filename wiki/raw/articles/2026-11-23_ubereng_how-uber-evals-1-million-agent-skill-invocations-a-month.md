---
title: "How Uber Evals 1 Million Agent Skill Invocations a Month"
author: Uber Engineering (@UberEng; post authors @Mager, @JasonVarbedian, @udaykiran)
date: 2026-11-23
type: x_article
source_url: https://x.com/ubereng/status/2125008806249930999
canonical_url: https://www.uber.com/us/en/blog/optimizing-ubers-agent-skills/
ingested: 2026-11-26
engagement_at_ingest:
  bookmarks: 21507
  likes: 7055
  retweets: 948
  impressions: 2350203
tags: [raw, source]
---

# How Uber Evals 1 Million Agent Skill Invocations a Month

**Source**: [Uber Engineering on X](https://x.com/ubereng/status/2125008806249930999) (X Article, published 2026-11-23)
**Canonical blog**: https://www.uber.com/us/en/blog/optimizing-ubers-agent-skills/
**Related**: [Efficient Software Factory](https://www.uber.com/us/en/blog/efficient-software-factory/), [Cloudflare Code Mode](https://blog.cloudflare.com/code-mode/), [Agent Skills spec](https://agentskills.io/)

Post author: @Mager, @JasonVarbedian, @udaykiran

## Full article text (article.plain_text)

Skills at Enterprise Scale

A skill is a Markdown file that teaches an AI agent to do one job well, such as creating a pull request, querying a metrics store, or outlining a weekly sales presentation. Skills are one of the building blocks of Uber's software factory. Uber's shared skills marketplace grew from 1 skill in October 2025 to more than 5,000 in just one year. Thousands of people have written a skill, and agents invoked skills more than 1 million times in just one month.

At enterprise scale, skill management, quality, efficiency, and distribution raise many challenges and opportunities. This post is for teams that are rolling out agents across a company. We share how to improve AI enablement and how to use agents to help.

### What Is a Skill

A skill is a workflow, and "the atomic unit of the enterprise is the workflow."[1] A skill packages one workflow: a runbook, a team's process, or a task an expert does by hand. It can be as short as editing a Linear® issue or as long as a full root-cause analysis.

On disk, a skill is a directory. Its SKILL.md file has a name, a description, and a body of instructions. The directory can also hold scripts and reference files. An agent loads it in three stages, so thousands of skills cost only a short description each:

- Always loaded: the name and description, about 100 tokens. The agent uses the description to decide whether the skill applies.
- Loaded when the skill runs: the body, kept under 500 lines.
- Loaded on demand: scripts and references, read only by the step that needs them.

The Agent Skills specification describes the open format in detail.

### Distributing Skills

We created one place for everyone to put skills, where they load easily wherever people use agents. The best place turned out to be a Git® repository, because version control already gives each skill an owner, a review, and a history.

### Organizing the Madness: Always-On, Core, and Domain

The goal is to make it easy for teams to write skills while providing them with a curated set of skills by default. To enable fast but high quality development, we separate the marketplace into three tiers, and the expectations for quality and efficiency rise as a skill graduates. To graduate a skill, we run our eval system and have a set of quality and usefulness checks.

- Domain. Any team can start its own area. Each area names its reviewers, so a team publishes after one peer approval and a CI check, without waiting for a central group.
- Core. Skills that are widely used move here. They are recommended, tested, and maintained by a team, and the platform team reviews every change.
- Always-on. About 100 broadly useful skills are on for everyone, so a new employee has skills on the first run. They cover pull requests, code review, tool access, data analysis, and chat.

### One Install for Every Agent

Supporting many different agents is part of our strategy. It is an opportunity, because people pick the agent that suits the task. It is also a challenge, because each agent defines and installs skills differently.

We made a CLI called aifx for starting each type of agent and storing configuration. We expanded it to include skill management, MCP calls, observability, and more advanced configurations. aifx handles the differences in skill definition and install on each platform. A person or an agent runs `aifx plugin add data-analyst` to install a group of skills, called a plugin, or `aifx skill add analyze` to install one skill. aifx records the choice in one configuration file and applies it to whichever agent starts next. An engineer who switches among Claude Code™, Codex™, and OpenCode™ keeps the same skills.

aifx merges configuration in layers: the company defaults, a team or program, the repository, the working directory, the user, and a local override. Later layers add plugins and never remove them, so a repository can declare the plugins that everyone working in it needs.

aifx manages personas for engineers, data scientists, and other roles. It sets the default skills and configurations.

### Skill Discovery

With thousands of skills, helping users find the right skill for a workflow is essential. We have a find-skills skill that can find and download a quality skill and run it within a specific workflow. To support discovery, we have classified and ranked skills with evals and run counts, and we create a skill quality score.

Using our internal context graph, any employee can ask, "Give me the skills my peers are using that I'm not."

### Measuring Skill Usage

We collect usage statistics from agents with OpenTelemetry in hooks. The hooks send events such as a session start or a tool call, so we can record skill use and its context. When the tool is a skill, the event records the skill, its version, and whether the agent chose it or the user typed its command. Events carry no prompt text and no file contents.

From these events we compute 12 measures for each skill, among them its users, retention, cost, latency, and errors. Authors see them on the skill's page in Skill Workshop, our authoring tool.

### The Never-Ending Battle for Skill Quality

Skills create agent workflows that present different challenges than agents do. They are expected to work in many different contexts, in domains where a right answer requires human judgment, and in many different agent environments. We created Skill Workshop, a plugin and web app, to help skill authors and users improve skills through science, systematic evaluation, and user feedback.

#### Skill Workshop

A skill has a lifecycle. An author writes it, tests it, and ships it through the marketplace. Then the author improves it from what its real runs show, until a better model makes it unnecessary and it retires. Skill Workshop has workflows for each stage, and a page for each skill that shows its usage, cost, and quality.

A skill starts with a well-defined spec. Models and harnesses change fast, and we want skills to keep working while we iterate on the implementation. The spec keeps the intent of the skill: its goal, its outputs, the tool actions that are required or forbidden, and the agents and models it targets. Skill Workshop compiles the SKILL.md and its test prompts from the spec, and recompiles them when a model or an agent changes.

#### Skill Code Smell Distilled Into a Linter

We distilled what made good skills, what caused problems, research papers, and model prompting guides into a linter with pass-or-fail checks. Here are some of the most useful:

- Steps are numbered, and each has one objective, with some way to at least soft verify it.
- Each step gives a concrete command and checks its result before the next step.
- The skill has an error recovery section: a table of failures and their fixes. "Try again" doesn't count.

#### Evals

We needed to move past manual user feedback on skill quality. We created several systems for evaluating skills on our many agent surfaces. We created hand-annotated prompts and runtime environments to test them in. Our guidance for an eval suite is about 5% golden cases with a fixed input and an expected output with tool mocks, 80% real prompts graded on trajectory, and 15% judged by the author. Trajectory means whether the agent used the right skills and tools in the right order.

We run the evals in three places: Minion, our background agent platform; AES, our managed agent sandbox; and devpods, our remote development machines. The clean room catches dependencies on the author's laptop. Just like every developer who says "it works on my machine," forcing a remote setup found many issues. Some skills expected certain file paths, cached documents, or certain OS tooling to work.

Evals are still part art and part science when working with non-deterministic LLMs. In our experience, evals that pass 70%-90% of runs can be more useful than those that pass 100%. Answers vary, and judges can too. A 100% pass rate may mean an eval is missing meaningful changes in the answer.

Deciding whether an eval run passes means deciding what matters. Does the wording need to match exactly? What can change without changing the meaning? Agents may not make these distinctions consistently on their own. They can focus on irrelevant details or miss a significant hallucination when the answer otherwise follows the expected format.

LLM-as-judge works best if it has a human-annotated set. Skill authors must create these, collect them from users, and grade them repeatedly. That's why we separate eval suites into golden sets, real prompts, and author-created cases.

Trajectory eval looks at what the agent tried to do and why. It doesn't look at the outcome. Did the agent use the MCPs or flows as expected? Did it query the table, read the Google Doc, check the context graph? Did it check its error recovery instructions? We use the outcome and trajectory scores to evaluate changes to our skills and workflows.

#### Less Is Sometimes More: Ablation

We test removing words and entire skills from workflows, with the same input prompts in an isolated evaluation environment. For a whole skill, we replay real prompts once with the skill and once without, and a blind judge picks the better answer. We tested heavily used skills with real prompts, trying with and without the skills and with only parts of the skill. As models get better, more words can reduce performance, so we also test removing words from skills.

In a majority of the cases, skills made the session more successful and cost less. The biggest wins came from skills that give the agent something it couldn't easily find or understand, such as access to internal documents or a way to run warehouse queries.

### Skill Efficiency

A skill allows us to measure the cost of a task, so we move more sessions to using skills. A session that doesn't use the skill might try many things, find wrong answers and wrong tables, and mess up how it uses tools. With the skill, the probability of getting a right answer, and getting it efficiently, goes up. In our ablation test of a skill that runs warehouse queries, sessions without the skill made 13% more tool calls, had six times as many tool errors, and took 31% longer, and the answer with the skill won 87% of the comparisons.

A skill that improves the answer also has a cost. Its instructions, its tool calls, and their results enter the agent's context, and every later turn in the session pays for that context again. We measure what each skill costs and reduce the cost with a few levers.

#### How We Measure the Cost of a Skill

Agents keep a running total of what a session has cost so far, and our telemetry reports that total in periodic snapshots. When an agent invokes a skill, we take the last total reported before the call and the first total reported after it, and subtract. The difference is the cost of that call. We add up the calls for each skill per day and divide by the number of calls to get the skill's cost per invocation.

The number includes the model reading the skill, the turns that follow, and any other tool calls in that window. We use the number to see where the cost goes and to compare a skill before and after a change.

#### The Levers We've Used to Reduce the Cost of a Skill

A central team goes after efficiency in all the most used skills, and platform owners treat skill ownership like they do UI or software ownership. They set up KPIs for quality and efficiency.

- Use code over LLMs. Steps that never vary run in scripts, so the model doesn't read every tool definition and every result. This is Code Mode, described below.
- Run the skill in a worker on a cheaper model. The skill dispatches one subagent, and the caller picks its model: a small model for lookups, the most capable one for correlating results. The large tool result stays in the worker's context and only a bounded summary returns, so later turns don't pay for it again. In a before-and-after comparison, the cost per invocation of a tracing skill fell 46%. A deployment skill showed no drop in its first week, so we measure each skill after its change.
- Run the script when the skill loads. When the result is small and always needed, the skill runs its script at load time and puts the output into the prompt, which removes a model turn. One search skill went from four turns to three, and its mean cost fell 32%.
- Move polling out of the main session. In our 20 highest-spend sessions, notification turns were about a third of the spend. In September we moved the polling of our pull request monitoring skill to a background agent on a cheaper model.

### Code Mode: Use Code Over LLMs When You Can

Code is cheaper, easier to test, and has better outcomes for deterministic work than LLMs. We saw that many tokens went to the same tool calls: run a query and read the response, read and send a Slack® message, search remote code, read and send email. The agent wanted only the result, but it had to load and run everything through the LLM and its context window, which was slow and expensive.

The default MCP install in an LLM client made this worse, because it loads every tool's full description into every call. With more than 100 tools, those definitions took 50,000 to 70,000 tokens before the user typed anything.

Inspired by Cloudflare's Code Mode, we moved these flows into utility scripts that call tools through our gateway. In our configuration, this avoided preloading those tool definitions, and the agent read only the parts of each result that it needed. The scripts improved the success rate, the latency, and the cost of our most-used flows.

The code mode skills became packages that the rest of the company's skills reference by name, which lets them depend on high-quality implementations for their flows. We also block .mcp.json files, which install tool servers, in skills and plugins.

### Continuous Improvement and Agents Filing Their Own Bugs

A skill can stop working for a thousand reasons. A model upgrade changes how the agent reads instructions, a tool changes its flags, or an agent harness changes how it runs the skill.

Agents know when a skill, a tool, or a flow isn't working. An agent is aware when it's struggling to do what it was told and has spent 100 turns fighting some weird error. It sees a flag that the help text lists and the tool rejects, a command that exits 0 on an error, or a query that returns nothing when it should match.

Agents can sometimes find a workaround, but they waste a bunch of tokens and precious context doing it. We found that adding an always-available skill that files what the agent sees as friction or bugs lets us create a powerful flywheel of improvement.

#### Problem Discovery

We call each report a papercut. The agent files it with log-papercut, an always-on skill, so every agent can see the skill and file a report without being asked. This improves future sessions and also the session where the bug happened, because the agent knows that sometimes things are messed up and that it should recognize when it is struggling. It can even look up what others did to get around that problem.

The report states what the agent tried, what it expected, what happened, and what would fix it. All reports go to one dashboard, grouped by skill.

#### Problem Resolution

A papercut is grouped, triaged, analyzed for its root cause, fixed, evaluated, and approved. Once the fix is in the wild, it's measured and checked for regressions before the ticket closes.

Agents filed thousands of papercuts in just three months. Hundreds have been fixed, and the fixes have improved workflows and made them much more token efficient. Here are some interesting fixes:

- The pull request skill wrote the commit message to a shared temporary file, so two concurrent sessions changed each other's pull requests.
- A deployment skill told the agent to pass epoch seconds where the API expects milliseconds.
- A configuration lookup skill returned a different property, with no error, when the requested key did not exist.
- A pull request skill waited for CI checks on a repository that has none, and repeated the same 404 until it timed out.

### Human Signals

Independent of what an agent thinks, we have human graders on agent sessions. In Fawkes, Uber's automatic software maintenance factory, we have code maintenance skills that open pull requests. If a pull request gets comments and iterations, or is not accepted, we use those signals to improve the skills that created it. The blocked pull requests become part of the eval set. We use this same pattern across many domains and agent platforms.

### Conclusion

Skills have turned words into actions and results. As usage grows and models improve, our focus moves from writing skills to skill quality and evaluation. The open problem is evaluating workflows that run rarely, matter a lot, and are hard to judge. As we invest, we're experimenting with trajectory and trace analysis, structured human annotation, and skill routing.

### TL;DR

- One format and one repository for every agent. The same skill runs in Claude Code™, OpenAI Codex™, OpenCode™, and SpaceXSI Cursor® on a laptop, and in all of our hosted agents. Our command-line tool, aifx, serves every agent surface for identity, skill distribution, and MCP connections.
- Skills are for everyone, not just engineers. Engineers use them for everything, like root-cause analysis and experiment readouts. Other teams use them to retrieve metrics, prepare draft documentation for review, and help account managers answer merchant support questions.
- Write the spec first. A spec.md records what a skill must produce and which agents and models it supports. Skill Workshop, our authoring tool, compiles the SKILL.md and its test prompts from it, so the skill keeps working as models and agents change.
- Less is sometimes more. We replay real prompts with and without a skill, and a blind judge picks the better answer. As models get better, some skills need to change or retire.
- Improve skills from traces. An author reads where a skill's real runs went wrong in their own sessions and turns each failure into a test case.
- Agents file their own bugs. When an agent hits a broken flag, a wrong doc, or a silent error, it files a structured report called a papercut, and an owner gets it.

### What's Next?

- A/B testing skills. We want to A/B test what's in skills to evaluate them at large. It will let us canary changes to important skills.
- Skill compiling per model. As models drift in prompting guides and recommendations, we find that different phrasing and lengths of SKILL.md files work better in different model families.
- Collecting and processing traces of skill runs. We will index sessions by eval, recording what the user wanted to do, what happened, whether it hit any trouble, and whether it was successful.
- Skill recommendations. We will tell users which skills they should be using.
- A task router. For everything a user wants to do, they can ask one place, which will route it to the right agent, skills, and context.

### Acknowledgments

This work spans the AIFX, Developer Platform, Michelangelo, uReview, Fawkes, Minion, Cortana, Agentic XP, and Conan AI teams, and the hundreds of engineers across Uber who wrote and maintain skills in the marketplace.

### References

[1] Shyam Sankar, interview with Ben Thompson, Stratechery, October 29, 2026.
