---
type: article
date: 2026-03-31
source: https://hugobowne.substack.com/p/top-questions-about-ai-assisted-software
title: "Top Questions About AI-Assisted Software Development"
author: Hugo Bowne-Anderson
tags: [ai-assisted-coding, agent, coding-agent]
---

## Top Questions About AI-Assisted Software Development

## Effective AI-Assisted Coding

Hugo Bowne-Anderson and Eleanor Berger Mar 31, 2026 14 1 3 Share In a recent conversation , I had the pleasure of hosting Eleanor Berger and Isaac Flath, the creators of the “Elite AI Assisted Coding” course , to discuss Agent Skills, Async Agents, and all the ins and outs of Effective AI-Assisted Coding.

Many questions came up that were similar to the questions that surface the most in their course. Not benchmark gossip or model tribalism, but the practical ones: how to make AI reliable in real codebases, how to delegate safely, where it fits into the software development lifecycle, and how to tell whether it is actually helping a team.

We reviewed the course FAQs, guides, and discussions and consolidated the recurring patterns into ten broad questions. You can also find many more guides, talks, FAQs, and tips on the course Substack at elite-ai-assisted-coding.dev . Each question below starts with a short answer and then a more practical explanation, linking to relevant resources and time-stamps in the podcast.

The top 10 questions were:

- Why do AI coding demos look magical while real projects feel much harder?

- How do I make AI reliable on real software projects?

- How much context does an agent need, and how should I package it?

- What makes a good AI coding specification?

- Which AI mode, tool, or model should I use for a given task?

- How do I delegate to AI without losing control of quality or direction?

- How can AI help across the whole software development lifecycle, not just writing code?

- How do async and parallel agents change the workflow?

- How do I keep AI-assisted development secure?

- How do I know whether AI is actually helping my team, and how do we turn that into repeatable practice?

👉 Eleanor & Mitja are teaching their next cohort of their Elite AI Assisted Coding course starting April 20 . They’re kindly giving readers of Vanishing Gradients 25% off. Use this link .👈

Our flagship course Building AI Applications just wrapped its final cohort but we’re cooking up something new. If you want to be first to hear about it (and help shape what we build), drop your thoughts here .

Vanishing Gradients is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

## Q1: Why do AI coding demos look magical while real projects feel much harder?

Because demos usually happen in low-constraint environments, while real projects are dense with hidden context, operational constraints, and accumulated risk.

## In practice

Why demos look so good. AI tends to shine in greenfield settings where there are many acceptable answers. A small prototype, a throwaway script, or a standalone feature leaves the model plenty of room to be approximately right. If the code compiles, looks plausible, and does something useful, the demo is already a success.

Why production feels different. Real systems carry architecture, naming conventions, historical decisions, security requirements, deployment processes, and tests that encode years of accumulated intent. Much of that is obvious to someone steeped in the codebase and completely invisible to a model unless you surface it explicitly.

The common misdiagnosis. People often assume the model has suddenly become bad or that the demos were fake. The more common explanation is simpler: the task has become far more constrained, but the briefing has not. The model is still doing what models do - filling in gaps with plausible guesses.

What works better. The more a task looks like “understand the system, define the boundaries, surface the important context, implement in bounded steps, verify as you go”, the more dependable the results become. In other words, the path out of disappointment is not less AI. It is more engineering.

A better operating pattern.

- Start with a smaller slice than you think you need.

- Provide the relevant context and non-goals up front.

- Ask for a plan before you ask for implementation.

- Review after each meaningful step.

- Let tests and tooling arbitrate, not vibes.

Bottom line. The demos are not fake. They are simply operating under kinder conditions than most production software.

See also:

- Everyone says agentic coding builds whole projects. Why doesn’t it work for me?

- Using AI For Real Projects and Decisions

- Vibe Coding a Real Mobile App: We Put ‘Vibe Code’ to the Test

-

## Q2: How do I make AI reliable on real software projects?

Reliability comes from engineering discipline, not from hoping the model will infer what you meant. Specificity, context, constraints, and verification are the real levers.

## In practice

Start with the two strongest levers. There are two key principles: be specific, and curate context. Vague prompts produce plausible guesses. Models rarely stop to say “I do not have enough information”. They usually improvise, which feels helpful until it quietly isn’t.

Define success before asking for output. Reliable runs usually have clear goals, constraints, acceptance criteria, and non-goals. They point to the right files, the right documentation, and the right conventions. They tell the model what good looks like and, just as importantly, what it must not do.

Constrain the scope of change. Reliability improves dramatically when you stop asking for huge, fuzzy transformations and instead work in smaller loops. Multi-file refactor? Fine. Entire subsystem redesign with unclear boundaries? Less fine. AI is strongest when the task is well-bounded enough that you can verify it without squinting.

Verify outside the model. Reliability is not the same thing as deterministic output. It is process reliability. That means tests, linters, static analysis, code review, CI, and manual inspection where it matters. If the work cannot survive external validation, it was never reliable in the first place.

Treat failures as specification bugs. This is one of the most useful mindset shifts: When the result is wrong, the first question should not be “why is the model stupid?” but “what did the instructions fail to make clear?” That framing gives you something actionable to improve.

A simple reliability loop.

Write down the goal, scope, constraints, and acceptance criteria.

- Provide the relevant project context and references.

- Keep the task small enough to verify confidently.

- Run tests, checks, and review after each meaningful step.

- Feed failures back into the spec or context, not just into your frustration.

Common failure modes.

- Asking for too much at once

- Assuming the model will infer local conventions

- Providing requirements but no acceptance criteria

- Letting the agent run without checkpoints

- Confusing a polished draft with a verified result

Bottom line. AI becomes reliable when you stop treating it as magic and start treating it as a system that needs inputs, boundaries, and feedback.

See also:

- I’ve configured instructions in AGENTS.md, but the agent isn’t following them. What should I do?

- Guide AI Agents Through Test-Driven Development

- Break Down Complex AI-Generated Code into Atomic Functions

- How to Build an AI Agent with AI-Assisted Coding

-

## Q3: How much context does an agent need, and how should I package it?

Enough context to behave like a competent collaborator, packaged so that the important parts are easy to load, maintain, validate, and evolve.

## In practice

Think in layers, not in one giant file. We like to frame this as a portable context stack. At the top are global rules and personal preferences. Then comes repository and project-level context. Then external documentation for the tools and libraries you depend on. Finally, there is living documentation: plans, specifications, architectural notes, data access, and other project artefacts that evolve over time.

Starting from zero still needs context. In an empty repository, one of the best first moves is to write down the basics in Markdown: what the product is for, who it serves, which libraries or services you expect to use, and any standing rules for the agent. That can live in AGENTS.md, a short project brief, or both. A quick voice-dictated brain dump is often enough to give the model something real to organise.

Use the right delivery mechanism for the right kind of context. Rules files such as AGENTS.md are useful for always-on constraints. Skills are excellent for reusable procedural knowledge. llms.txt is useful for third-party guidance. MCP resources are useful when context needs to be dynamic or live. In-repo documentation remains essential because it is the part you own and can version with the code.

Source context in tiers. Generic context is quick: public docs, default skills, web search. Curated context is better: the best docs, distilled references, selected examples, tuned workflows. Project-specific context is best when you need precision: conventions, constraints, architecture, and patterns written specifically for your codebase.

Capture intent, not just instructions. Good context is not only a list of rules. It also preserves the “why” behind decisions: why a database was chosen, which alternatives were rejected, what trade-offs were accepted. A lot of that intent first appears in chat logs. Promoting the important parts into notes, ADRs, or specs creates useful archaeology for both humans and agents.

Validate the context, do not just admire it. Ask the agent questions it could only answer if it had truly loaded your materials. For larger teams, write checks that demonstrate the agent actually follows the documented conventions. If you do not validate the context, you are effectively testing it in production.

Manage the context window deliberately. Long conversations are not free. As the context window fills up, quality degrades and compaction becomes lossy. Short, focused threads usually perform better and cost less. If a conversation starts drifting, it is often wiser to stop, sharpen the spec, and restart than to pay for a long chain of increasingly muddy context. Persist important artefacts to files, start new conversations before things get muddy, and treat the live chat as working memory, not as permanent storage.

On teams, context becomes infrastructure. Once AI is part of the workflow, shared context stops being a convenience and becomes a strategic asset. It captures conventions, decisions, and successful patterns. Over time it becomes living organisational memory - provided someone curates it. The useful trick is to treat context files as living documentation: if a new rule or design decision emerges in chat, update the shared instructions instead of leaving it buried in conversational history.

A practical context stack.

Global rules and preferences

- Project and repository conventions

- External docs and reference material

- Living project artefacts: plans, ADRs, specs, data notes

- Validation checks proving the context actually works

Bottom line. The right amount of context is “enough to remove guessing”, and the right structure is whatever lets you maintain that without drowning in token soup.

See also:

- Watch: Starting a new AI-assisted coding project

- Watch: The importance of capturing and sharing intent

- Watch: The importance of living documentation

- What are the best strategies for managing “exploding” context in large enterprise codebases for AI agents?

- In a multi-repo setup, what are good patterns for providing an AI agent with context from other internal repositories?

- Does including AGENTS.md cause context overflow?

-

## Q4: What makes a good AI coding specification?

A good spec explains the goal, the scope, the constraints, how success will be judged, and what artefacts should come out the other end.

## In practice

A spec is the contract. For a small task, that contract might just be a careful prompt. For larger work, it should usually become a proper Markdown artefact: a plan, a PRD, an implementation brief, or some equivalent. The format matters less than the clarity and the fact that it is reviewable.

Spec-driven development is mostly about sequence. You think through the problem before you ask the model to improvise a solution. That might mean user stories, a planning note, a rough list of constraints, a pro-and-con sketch, or a more formal PRD. The format can vary. The discipline of defining success up front is the point.

The strongest specs answer the same basic questions. What are we trying to achieve, and why? What is in scope, and what is not? Which files, systems, or inputs matter? Which constraints must be respected? What tests or checks must pass? What output should the agent produce: code changes, docs, a PR, an issue comment, a report?

Good specs are calibrated, not maximal. Under-specified tasks give the model too much freedom and invite misalignment. Over-specified tasks can be almost as bad: they trap the agent inside irrelevant implementation detail and stop it from finding simpler solutions. The sweet spot is precise incompleteness - enough detail to define the target and the boundaries, enough freedom to let the model solve the problem.

AI lowers the cost of spec-driven development. One of the biggest changes in practice is that you can now use an interactive agent to help write the specification for a background agent. Ask the first agent to analyse the codebase, identify affected files, draft a plan, and sharpen the constraints. Then hand that refined spec to the second agent to execute.

That also hints at where things may go next. As agents improve, the durable artefact may increasingly be the specification and the recorded intent around it, with more code generated or regenerated just in time for a task. That will not replace carefully maintained software everywhere, but it does make good specs more valuable, not less.

Common specification bugs recur.

Ambiguous scope: the agent changes more than intended

- Implicit assumptions: domain knowledge was obvious to you but written nowhere

- Under-constrained style: the output works but does not fit the project

- Missing exit conditions: the agent keeps going past the intended stopping point

- Insufficient context: it reinvents things that already exist

A practical spec template.

- Goal and why it matters

- Scope and explicit non-goals

- Relevant inputs, files, or references

- Constraints and acceptance criteria

- Tests and checks to run

- Expected output artefacts

Bottom line. A good spec is what turns AI from an improviser into a collaborator with a map.

See also:

- Watch: Spec-driven development

- Watch: Where AI-assisted coding may be heading

- Spec-First Development For API -> MCP

- Make Dictation Your Prompting Superpower

- Product Thinking for Agentic Development

- Thanks for reading Vanishing Gradients! This post is public so feel free to share it.

Share

## Q5: Which AI mode, tool, or model should I use for a given task?

Choose the mode that matches the task. Tool choice matters, but usually less than workflow fit, context quality, and how well you review the results.

## In practice

Separate the decisions. People often ask “which tool should I use?” as if that were the whole question. In practice there are at least four decisions hiding inside it: which modality fits the task, which execution environment you want, which model you want, and which commercial trade-offs you are willing to accept.

Start with modality. We encourage everyone to work with a spectrum: completion, inline editing, chat Q&A, chat-driven editing, interactive agentic coding, and background async agents. Completion is excellent for flow and boilerplate. Chat is great for debugging and discovery. Interactive agents are strong for bounded multi-step work. Async agents are right when the task is fully specifiable and you want a clean, reviewable result later.

Then choose the environment. IDE agents are convenient and great for interactive work. CLI agents offer more explicit control and easier integration with scripts and tooling. Hosted background agents are polished and easy to dispatch. CLI agents in CI give you maximum control over models, environments, and integration points, though with more setup.

Prefer simple tooling until complexity earns its keep. In many day-to-day workflows, plain CLI tools and agent skills are enough. They are easy to inspect, easy to version, and easy for the agent to use. MCP still has legitimate uses, especially when you need richer state or a more structured interface, but it should usually be justified rather than treated as the default. The growing standardisation around agent skills makes them especially useful as a reusable customisation layer across tools.

Then choose the model. Benchmarks are useful, but personal test tasks are more useful. Keep a small suite of tasks that matter to you and run new models against them. In many real workflows it makes sense to split by phase: use a stronger, slower model for analysis and planning, and a faster, cheaper model for routine implementation or iteration.

Costs are part of the decision too. Sensible model selection and shorter, cleaner threads usually save more money than elaborate prompt hacks. Use cheaper, faster models for routine work, and reserve the expensive ones for analysis, difficult reasoning, or multimodal tasks. Subscription products can be convenient and often good value, but pay-per-token models have the advantage of transparency and predictability.

Do not overfit to one vendor. We are intentionally vendor-agnostic because the core skills transfer. Context engineering, specification, review, and workflow design matter across products. It is usually better to know one setup deeply and understand the others broadly than to keep jumping between tools looking for salvation.

A small model portfolio usually beats loyalty. One model may be better for long context or multimodal input, another for dense technical reasoning, another for quick drafting. Some of that is hard capability, some of it is simply learned fit. You do not need to master all of them at once. Learn one strong setup well, then expand deliberately.

A simple decision sequence.

What kind of task is this?

- Which modality fits that task?

- Does this need interactive steering or background execution?

- What model is best for this phase?

- Which tool makes that combination easy?

Common mistake. Picking a tool first and then forcing every problem through it.

Bottom line. Choose the mode for the task, the model for the phase, and the tool for the workflow.

See also:

- Watch: Choosing between CLI tools, agent skills, and MCP

- Watch: Managing token costs

- Watch: Subscription versus pay-per-token pricing

- Watch: Using different models for different tasks

- Watch: The rise of agent skills

- How can I compare and identify the best AI models for my agentic tasks?

- A Straightforward Answer to “What Tool Should I Use?”

-

## Q6: How do I delegate to AI without losing control of quality or direction?

Delegation works when you control scope, checkpoints, and review. The goal is not maximal autonomy. It is effective autonomy.

## In practice

Think in terms of a control spectrum. Some tasks are safe to hand over with minimal supervision. Others need tight steering. The skill is not to maximise autonomy for its own sake, but to choose the right point on the spectrum for the stakes, ambiguity, and reversibility of the work.

Control starts with scope. Before you begin, decide whether this is a tiny edit, a multi-file refactor, a new feature, or an end-to-end background job. The larger the scope, the more important version control, checkpoints, and explicit verification become. When in doubt, start smaller.

Use boring safety nets. Topic branches, git worktrees, checkpoints, and small commits are not glamorous, but they are what keep the process reviewable. If the agent goes sideways, you want a clean rollback point and a clear history of what happened.

Review incrementally, not only at the end. A strong loop is: let the agent complete a bounded step, review the output, verify alignment, run the relevant checks, then continue. This catches drift while the design is still flexible. If you wait until the end of a huge run, you often discover too late that the agent was solving the wrong problem beautifully.

Keep humans where they matter most. For async or operational workflows, human-after-the-loop is often the right pattern. Let the agent produce a PR, a report, or a proposed fix. Let a human decide whether it should be merged or promoted. For higher-risk changes, add stricter gates. For lower-risk work, allow more speed.

Trust is always conditional. “Trust, but verify” is the right operating principle. The level of review should scale with the damage a mistake could cause, and accountability never leaves the human who approves or deploys the result. The agent can assist. It cannot own the consequences.

Do not outsource the thinking you still want to own. The best posture is not “please replace my brain”. It is “help me explore, implement, critique, and verify”. That keeps you in control and avoids the passive habit of accepting polished nonsense because it arrived quickly.

A practical delegation pattern.

Choose the right scope

- Write a clear spec

- Isolate the work on a branch or worktree

- Review and verify in short loops

- Gate higher-risk changes with stronger human review

Bottom line. Delegation works best when the work is bounded, the artefacts are reviewable, and the human stays responsible for judgement.

See also:

- Watch: Trusting AI agents

- How can I use AI without losing my core problem-solving skills?

- Use Git for Automated Checkpointing

-

## Q7: How can AI help across the whole software development lifecycle, not just writing code?

Because writing new code is only a small slice of software work. Much of the leverage sits in planning, review, operations, documentation, and all the repetitive tasks around coding.

## In practice

Planning and discovery. AI is useful long before implementation starts. It can help explore a codebase, compare architectural options, draft plans, refine specs, and turn fuzzy ideas into something reviewable. This is especially valuable when the real bottleneck is not typing but understanding.

Implementation and refactoring. This is the most familiar use case, but even here the best results come when AI is treated as part of a broader loop. Completion, inline edits, chat-driven edits, and full agents each have their place.

Review and collaboration. Reading code is far more common than writing new code. AI can perform first-pass review, flag inconsistencies, catch common bugs, summarise diffs, and help reviewers focus on architecture, intent, and impact rather than routine mechanical checks.

Quality assurance can be continuous as well as local. When reviewing AI-generated code, it is often better to verify the outcome than to fetishise line-by-line reading. Strong tests matter more than aesthetic reassurance. On larger codebases, scheduled AI jobs can also scan for duplication, missing coverage, or architectural drift and open issues for humans to triage.

Operational work. One of the strongest themes is AI-assisted operations: writing commit messages, opening pull requests, watching CI, parsing logs, proposing fixes, keeping release hygiene under control, and handling other repeatable tasks that otherwise consume attention.

Maintenance and quality work. AI is also useful for documentation refreshes, release notes, issue triage, dependency updates, code health reports, and other jobs that are often neglected because they are tedious rather than unimportant. In practice this can raise quality more than code generation alone, because work that used to be too expensive to do consistently becomes sustainable.

The real shift. The point is not that AI writes code. The point is that it can reduce bottlenecks throughout the SDLC. Once that happens, it stops being a novelty and starts being part of how the team ships software.

A useful mental model.

Use humans for judgement, priorities, and trade-offs

- Use AI for scale, consistency, and repetitive analysis

- Put the two together through reviewable artefacts and workflow integration

Bottom line. The biggest gains usually come when AI spreads into the whole software lifecycle, not when it is confined to code generation.

See also:

- Watch: AI code reviews and quality assurance

- Adventures in Continuous AI

- How can we use a “Continuous AI” pattern to integrate AI into CI/CD

- Legible AI Collaboration: Workflows for Reviewing AI-Generated Code

-

## Q8: How do async and parallel agents change the workflow?

They shift AI from a tool you babysit to a system that can take complete tasks, run in parallel, and return reviewable outputs later. That changes both the economics and the discipline of the work.

## In practice

Why async matters. A background agent can take a complete, well-defined task and run remotely without you hovering over it. When it finishes, it returns a PR, a patch, a report, or some other artefact you can review. That changes AI from something that augments your keystrokes into something that can automate entire workflows.

The practical benefit is wonderfully unglamorous. Background agents are ideal for the small, clearly bounded jobs that do not deserve your full attention: tweak copy, adjust a component, clean up a test, refresh a doc. You hand off the task, get on with something harder, and review the result later.

Why this is powerful. Async agents as a major productivity multiplier because they enable true parallelism, fit naturally into SDLC workflows, and force discipline. Since you cannot intervene mid-run, you are pushed to define the environment, the context, the specification, and the expected outputs properly.

Local versus remote parallelism. On a single machine, you can run multiple CLI agents across worktrees. That is useful, but limited by local resources and attention. Remote agents go further: cloud systems and CI runners can execute many jobs at once, in clean containerised environments, with outputs visible to the whole team through PRs, issues, or CI comments.

This is where Continuous AI enters. Once a job is predictable enough, it can be triggered by a schedule, a pull request, a release, or an issue label. Documentation refreshes, dependency updates, code health checks, release notes, AI reviews, and issue triage all fit naturally into this model.

A reusable async job pattern.

Trigger: a schedule, repo event, or issue activity

- Environment: container, tools, network policy, secrets

- Context: shared project instructions and docs

- Specification: the job definition

- Execution: the agent run with captured logs

- Output handling: usually a PR or reviewable report

The two big mistakes. Under-specifying the job and hiding the outputs. Async work only helps when the result is reviewable and the run itself is observable.

Bottom line. Async and parallel agents become transformative when they are treated as disciplined, reviewable automation rather than as distant cousins of chat.

See also:

- Watch: Asynchronous and background agents

- Working with Asynchronous Coding Agents

- Asynchronous CLI Agents in GitHub Actions

- Louis Knight-Webb on Vibe Kanban

-

## Q9: How do I keep AI-assisted development secure?

By treating security as architecture and workflow design, not as a prompt-writing problem. The real danger is the combination of private data, untrusted input, and external communication.

## In practice

Start with the real threat model. Be aware of Simon Willison’s “lethal trifecta”: access to private data, exposure to untrusted content, and the ability to communicate externally. If an agent has all three, you have a serious exfiltration risk. There is no magic prompt that makes this safe.

The immediate, practical danger is indirect prompt injection. An agent reads something untrusted - a web page, an issue comment, a ticket, a pasted log - and treats hidden instructions as if they were part of the job. That is exactly why sandboxing, network restriction, and output review matter so much.

Design by removing or restricting one leg. If the agent cannot access secrets, the blast radius shrinks. If it cannot fetch arbitrary untrusted content, the injection surface shrinks. If it cannot send data out, exfiltration becomes much harder. The most reliable mitigation is architectural, not rhetorical.

Apply restrictions at several layers. Network policies matter: allowlists, read-only access, no uploads where possible. Filesystem policies matter: sandbox the project, keep home directories and secret stores unreachable. Execution policies matter: require approval for risky actions, especially scripts, migrations, infrastructure changes, or broad filesystem writes.

Use familiar security tools and habits. Containers, codespaces, approval modes, least-privilege credentials, short-lived tokens, audit logs, dependency pinning, and sensible monitoring all matter here. This is largely ordinary security engineering, applied to a more dynamic actor.

Be aware of approval fatigue. Human approval can help, but only if it is meaningful. If the system nags you constantly, you will eventually rubber-stamp actions you do not actually understand. Better to combine selective approvals with environment restrictions and logging than to pretend that endless clicking is a security model.

A practical safeguard checklist.

Sandbox the filesystem

- Keep secrets out of reach

- Scope credentials narrowly

- Allowlist network access where possible

- Require approval for high-risk actions

- Log prompts, actions, and outputs

- Treat model output and external content as untrusted

Bottom line. Safe AI use comes from layered controls, least privilege, and healthy scepticism - not from telling the model to “please be careful”.

See also:

- Watch: Security concerns with AI agents

- How do you handle agent sandboxing?

- How can I defend against prompt-injection attacks in AI-assisted software developent?

- Sandboxing for AI Coding with GitHub Codespaces

-

## Q10: How do I know whether AI is actually helping my team, and how do we turn that into repeatable practice?

If you do not measure and learn, you only have anecdotes. The teams getting durable value treat AI adoption as an experiment and shared practice, not as a collection of isolated wins.

## In practice

Distinguish personal speed from team efficacy. A developer feeling faster is mildly encouraging. A team shipping more reliably, with less toil and better quality, is what actually matters. One of the strongest themes in the later course material is the move from individual productivity to organisational efficacy.

Measure against a baseline. AI adoption works best when treated as an engineering experiment. Define a hypothesis, choose a baseline, decide what success would look like, and then measure. Without that, you are mostly measuring excitement.

Use frameworks as vocabulary, not doctrine. DORA is useful for delivery performance: deployment frequency, lead time, change failure rate, and time to restore. SPACE is useful for the human side: satisfaction, communication, efficiency, and the rest. Both are helpful starting points. Neither should be treated as a religion.

Measure what AI delegates, not just what it augments. The biggest gains often come from work that used to be manual and is now automated: documentation updates, dependency maintenance, issue triage, routine review work, release notes, code health checks. These are often easier to measure than vague “developer productivity”.

Choose a few actionable metrics. If a metric cannot change a decision, it is probably vanity. Start with two or three things that matter to your team right now: review churn, first-pass yield, escaped defects, documentation freshness, time spent on repetitive work, or CI babysitting burden.

Build a learning loop. Capture useful artefacts: transcripts, specs, logs, PRs, failures, successful patterns. Review them regularly. Feed what works back into shared context, tools, and specifications. Learn from failure modes systematically rather than emotionally.

Team adoption changes the social side of engineering too. AI makes implicit hallway knowledge less viable. Standards, design decisions, and operating rules need to be written down clearly enough for both colleagues and agents to follow. That is less romantic than intuition and lore, but much more scalable.

Give context an owner. This is one of the most interesting team-scale ideas in the ecosystem. Once AI matters to the organisation, shared context becomes infrastructure. If nobody curates it, it drifts. If someone owns it, it can improve continuously and become living organisational memory.

A few habits travel especially well. Give agents richer context than feels strictly necessary, keep experimenting with prompts and workflows, and automate the small boring tasks first. Those early wins usually teach a team more than grand transformation programmes. A beginner’s mind helps too: what felt impossible a month ago may already be routine.

A simple team playbook.

Pick a baseline

- Choose 2-3 actionable metrics

- Run AI in a few repeatable workflows

- Capture outputs and failures

- Feed the lessons back into shared context and specs

- Make someone responsible for that loop continuing

Bottom line. Teams get durable value from AI when they measure what matters, codify what works, and treat shared context as an asset rather than an accident.

See also:

- Watch: Collaborative AI-assisted coding in teams

- Watch: Three takeaways for effective AI-assisted coding

- How can we credibly measure if AI coding assistants improve developer productivity?

The common thread across all ten questions is simple: the teams getting real value from AI are not treating it as magic. They are treating it as engineering.

That means context that is curated, specifications that are precise, delegation that is reviewable, automation that fits the SDLC, security that is designed in, and feedback loops that compound learning over time.

It may be slightly less glamorous than the louder stories on social media. It is also a much better way to ship software.

👉If you want to go deeper on these ideas, join the spring cohort of Elite AI Assisted Coding , which starts on April 20. It is a practical, vendor-agnostic course on using AI to build real software with context engineering, spec-first workflows, async agents, security, and team-scale adoption. Eleanor & Mitja are kindly giving readers of Vanishing Gradients readers 25% discount . Use this link . 👈

Our flagship course Building AI Applications just wrapped its final cohort but we’re cooking up something new. If you want to be first to hear about it (and help shape what we build), drop your thoughts here .

Vanishing Gradients is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe 14 1 3 Share A guest post by Eleanor Berger intellectronica.net ・ agentic-ventures.com ・ okigu.com Subscribe to Eleanor