---
title: "Agentic Code Quality"
author: Addy Osmani (@addyosmani)
date: 2026-08-12
type: x_article
source: "https://x.com/addyosmani/status/2087427868343373919"
url: "https://x.com/i/article/2087205551038230528"
engagement:
  bookmarks: 1067
  likes: 584
  retweets: 73
  impressions: 220993
tags:
  - code-quality
  - agentic-engineering
  - harness-engineering
  - quality-gates
  - coding-agents
  - verification
  - back-pressure
  - agent-harness
---

# Agentic Code Quality

**Author:** Addy Osmani ([@addyosmani](https://x.com/addyosmani))
**Published:** 2026-08-12 (X Article)
**Source tweet:** https://x.com/addyosmani/status/2087427868343373919
**Full article:** https://x.com/i/article/2087205551038230528

---

For much of human history, we've evaluated code quality via code review: someone reads what you wrote and makes sure it's clean, thoughtful, fast, understandable, and tests well. For agents, that approach doesn't scale well; there's just too much code for anyone to read. As a result, more and more of our quality checks have to happen in the harness, environment, and operating system around the agent. I still read and review code, but am very intentional about where I am comfortable with constraints as the check.

**Software quality now depends on the constraints you set around your agents.**

Constraints define what the system is allowed to do by throwing tests and deterministic constraints at an agent's proposals. It's by setting and maintaining these constraints that we build loops that reliably deliver high-quality production software, even when agents are creating hundreds of thousands or millions of changes every single day.

We call these constraints **quality gates**, and they take many forms.

They include conventional unit tests, property tests, and acceptance tests. They include mutation testing, where we generate variations of code, run it against the same tests, and make sure that people aren't sneaking bugs in that we're missing. They're metrics around code quality, such as cyclomatic complexity and line length, that help keep things readable.

Constraints also play an important role in what proposals the system will accept and apply as code changes. By the time a change proposal moves from the interpreter running the agent to the agent controller and out to production, we've done enough checks on it to be confident that it's safe to ship and the impact of its change is well within the scope of the agent.

> An agent can propose anything. Your constraints decide whether a proposal is safe enough, correct, scoped, and useful, for you and your team to ship.

This model offers a lot, but also leaves out many pieces, and those omissions are worth thinking about today. One issue is autonomy; agents might apply their intentions well, but may fail when there's missing information or when what they try to do is ambiguous. That applies both to the task itself and to how it's parameterized by the harness, environment, and other components.

Many of the reasons that humans fail to ship great code are shared with what agents might do: brittle environments that don't hold up under script-driven stress, nondeterministic builds, missing permissions, and weak tests. This motivates a better environment that gives agents trustworthy feedback, allows for low-damage failure modes, and makes it easier to progressively build up success.

> The environment we're after is one where an agent can do real work, get feedback it can trust, and fail without doing much damage.

The other important issue is trust. We can't credulously hand off intent to something even as smart and robust as a modern agent without checking for correctness. We start with trust, but it has to be hard-earned.

Some constraints shape work before it begins. Others give feedback while the agent is working. Others decide whether its output can cross the production boundary at all.

There are a bunch of ways to model how we put a verification structure around a system. In my experience it helps to have a broader, but intentionally chosen, set of checks for your constraints instead of solely relying on unit tests. The idea is that each check has a distinct responsibility and that can range from type safety and performance to late-stage security scanning. Folks can define their own constraints too, including architecture rules that linting tools like ESLint can enforce. Many of these tools have built-in hooks that can be used to pull in agents, or humans, when things break.

For now, much of the difference between useful agent output and slop still comes down to the skill of the team operating the loop.

AI gives us high volume code generation and velocity, but this can also mean it gets harder for humans to review every single change. You have to instead be intentional with where their attention is going. If you put a human check into a system that otherwise moves at machine speed, don't be surprised if that impacts productivity. Human attention is scarce and valuable so we should proactively direct it to those most nuanced problems that require our judgment. Downstream humans should only be pulled in when the automated guardrails for constraints break.

> Human "code review" in the future is going to look very different.

Correctness is one important dimension, but you may care about others as well, like maintainability, performance, security, efficiency, and comprehensibility. Just as correctness decomposes into many signal types, so does the rest of quality. And while it matters how many constraints we have in place, it matters more whether they're challenging enough to meet our bar for quality and production readiness.

> Software quality isn't a single metric. Think of it as a collection of signals of varying importance to you and your team.

Back-pressure can be implemented through many tools: compilers rejecting invalid code, tests failing, security policies blocking bad practices, CI declining to deploy. Ideally it exists throughout the loop, not as a single review at the very end of all the work.

> Constraints and back-pressure let agents catch bad work before it's a problem.

What happens if we can't apply the constraint because the volume of changes is higher than our tools can consume? We end up building a queue and relying on a verification system that moves at human speed. To scale, we want to push as much as we can into the verification loop throughout and not wait until the end. If we can scale within our automated checks, we can increase the speed and throughput of our entire delivery system. If we run out of room in the verification loop, we need to do one of several things.

First, we can scale our verification system and create more capacity to constrain and push back on changes that come in. Second, we can reduce the rate at which agents generate new changes so that verification can catch up to the volume of work. Third, we can lower our quality bar so that verification doesn't push back as hard as it otherwise might. From a scaling perspective, we need to be ready to do all of these things. At the same time, we should not stop short of realizing that we could actually get more done by un-constraining in some directions. Maybe we can increase the speed of agent-generated changes by providing swarms of agent developers or automated software factories to create changes without waiting for us to review each of them.

And in some places we might want to give them more freedom as long as we keep tighter constraints in others. By providing tighter constraints where we care the most, we can maximize our throughput without sacrificing quality. Throughout these decisions there are many options. Most obviously, we have to trade between different dimensions of quality. As we've emphasized, security is very important, but we've also had to trade between delivering security and delivering a product on time. There is a spectrum from innovation-focused at one end to quality-focused at the other. Somewhere along the way, we have to make choices about where we want to be on that spectrum.

We want to send clear feedback from the environment and the system back to our agents or teams, so that people can focus on the more subjective concerns of taste, intent, and architecture. If we can help humans stay inside the safe range of constraints, we can avoid the need for them to work hard trying to figure out where things went wrong.

Software quality includes more than just correctness. Software quality also means maintainability, good performance, security, efficiency, and being easy to understand. All the constraints that help us meet these standards and keep our production flowing create back-pressure in our delivery pipeline.

We need to make deliberate decisions about where to apply strong constraints and where to remove or relax them. Apply strong constraints where they're serving both of these goals. Don't support them if they're not serving one or both. Be ready to raise or lower standards as the case may require. And remember these constraints at different points in the software system are what make software quality enforceable.

We should apply strong constraints where they'll serve this dual purpose best and consider removing or relaxing constraints that aren't serving either purpose well. We should also be ready to shift quality bars up or down as needed. In effect, these constraints at various points in our software system are what give quality its teeth. In many cases, we can create more back-pressure and more constraints by deploying new tools or strengthening tools that are already in place. All of these things can be used to push back on most change requests. We want to build them throughout the pipeline.

We don't want to wait until the end of the pipeline when our CI system will simply tell us that we're not allowed to deploy without fixing problems. We want to use these signals as early as we possibly can, through every possible pathway. The ultimate constraint in this system is the one we place on ourselves to stand behind the decisions and actions we've taken to build the system and to operate it. But like all other constraints, we need to make thoughtful trade-offs about how much we want our own judgment to restrain, to back-pressure, and to act as a final check.

Quality is in the constraints that we place around our agents. So as you're thinking about quality for your own apps, take this problem statement and come up with your own constraint-driven plan.

---

*Speaking of quality, agents are writing your code. Sonar gives you the quality gates to make it shippable.* (sponsored segment)

*This article was rated 100% human written by Pangram 4.*
