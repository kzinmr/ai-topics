---
title: "Managed agents are the new Lambda"
url: "https://martinalderson.com/posts/managed-agents-are-the-new-lambda/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-15T07:01:01.206070+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Managed agents are the new Lambda

Source: https://martinalderson.com/posts/managed-agents-are-the-new-lambda/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Managed agents (cloud-hosted agents) are the next big push from the frontier labs. They're genuinely incredible. They're also going to be the AWS Lambda of this cycle - powerful, sticky, and an absolute nightmare to migrate off once you're in deep.
What are "managed agents"?
While the exact definition is up for debate, in my mind a managed agent is an agent harness (like Claude Code) running
in the cloud
, not on your local machine.
This has a few major advantages. The most obvious one is that you don't need a machine running locally - it can do its work 24/7, in the background. The other that running in the cloud means it can be notified of changes and act on them. Imagine, for example, agents responding to incoming emails or webhooks and doing some activity based on them (this is very possible locally - but easier with the agent running on the server).
The other advantage is security - probably the key part of the "managed" agent. Much like PaaS (platform-as-a-service) products like Heroku, AWS ECS/App Runner/Lambda and Azure App Service/Functions, the provider manages not just the underlying physical infrastructure for you, but also manages patching the operating system and related server software on your behalf.
Sandboxing is another related benefit. Managed agents only get access to what you give them - no risk of an agent wandering into files it shouldn't.
If you're already running Claude Code/Codex/OpenCode in Docker on a server, you've basically built one yourself. The frontier labs are just productising the pattern.
Vendor lock in is real
Anthropic has really been pushing their managed agents product
hard
lately. This makes a lot of sense - cloud hosted agents are genuinely incredible in what they can do - but I'd urge real caution on locking yourself into a vendor - at least at this point.
Fundamentally, agents are not particularly difficult to swap out. While there are important differences and nuances in how they work and operate, switching from Claude Code to Codex (or OpenCode, or Pi, or one of the many other agent harnesses) is a fairly simple process. Fundamentally the pattern is the same - run a harness with a prompt, context and tools and capture output and logs. All agent harnesses have the same primitives.
And at least having the ability to swap the agent harness and model out is
really
important. Clearly pricing is one important dimension, but equally so is being able to use new models from different labs. The competition is absolutely cutthroat and shows absolutely no sign of slowing down.
Once you start using a managed agent product
from a frontier lab
this gets far more difficult. A lot of your data and workflows are embedded in their cloud. While Anthropic have gone to lengths to say it is your data and it can be exported, in my many years of experience of vendor lock in this definition drifts and gets harder and harder to migrate to another provider.
As many people found out with AWS, moving Docker container workloads is fairly easy if you want to move hyperscaler clouds. Moving AWS Lambda functions is far, far more difficult - I've seen organisations spend months upon months unpicking Lambda code and assumptions when they realise it isn't a good fit after all the hype dies down.
Claude usage plan changes
Yesterday Anthropic
announced
huge
changes to their pricing model which underlines this point. If you run Claude Code non-interactively (which includes nearly all cloud-hosted agent usage -
and
many others), these now are not eligible for your subscription token allowances and will instead use some new credit. After this allowance is exhausted then it is very expensive API tokens ahead. It's fair to say if you were using a lot of "non interactive" Claude Code you are looking at a 5-20x price increase with these changes.
It's clearly Anthropic's prerogative to do this - and (I think) points to their compute shortages more than anything, but it
has
given OpenAI a real opening for users to switch to Codex - OpenAI (currently, at least) have been very explicit you can use your included allowances on your plan with any tool and however you like.
Expect to see a lot more talk around Codex (which has been already gaining significant traction over the past few months) and other providers in the future - developers are often remarkably price sensitive around things like this, especially for personal 'side projects' - which often then end up informing enormous purchasing decisions in the companies they work in months and years down the line.
Solutions
Now it's easy to say don't use a frontier lab's managed agent product, but what are the solutions?
I think there's two main ways you can solve this in your organisation.
Firstly, roll your own managed infra. This is a good option for developers and tech adjacent teams - they will have the expertise to do this. Essentially, it's just running a Docker container which they do all day every day. Using something like OpenCode as a harness allows you to use
any
model provider and switch between them in minutes.
Secondly, there's a flood of startups and other companies that allow you to run managed agents with any model or provider you want. I haven't (yet) evaluated them in detail as the market landscape is switching so fast to give any real thoughts on quality, but providers include Cloudflare Agents, Vercel and the hyperscaler options (AWS AgentCore, Azure AI Foundry and GCP Vertex AI Agent Engine).
My personal view is until this shakes out a bit more, stick to self hosting them. It's not difficult, allows you to secure them inside your current infrastructure and builds organisational competence around agent primitives. Outsourcing this knowledge at this point is a path to serious organisational knowledge gaps. However, expect this to change as the platforms introduce more capabilities that become more and more difficult to replicate. One to keep an eye on.
The one ointment in this plan is that I have a strong gut feeling the frontier labs are going to start introducing new models and capabilities that are
only
available on their managed agent platforms. This is where the pendulum (maybe) starts swinging to
having
to use managed agents - but again, maybe not.
