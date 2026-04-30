---
title: "Two kinds of AI users are emerging. The gap between them is astonishing."
url: "https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-30T07:01:57.261380+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Two kinds of AI users are emerging. The gap between them is astonishing.

Source: https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/?utm_source=rss&utm_medium=rss&utm_campaign=feed

It still shocks me how much difference there is between AI users. I think it explains a lot about the often confusing (to me) coverage in the media about AI and its productivity impact.
I think it's clear there are two types of users to me now, and by extension, the organisations they work for.
First, you have the "power users", who are all in on adopting new AI technology - Claude Code, MCPs, skills, etc. Surprisingly, these people are often
not very technical
. I've seen far more non-technical people than I'd expect using Claude Code in terminal, using it for dozens of non-SWE tasks. Finance roles seem to be getting enormous value out of it (unsurprisingly, as Excel on the finance side is remarkably limiting when you start getting used to the power of a full programming ecosystem like Python).
Secondly, you have the people who are generally only chatting to ChatGPT or similar.
So many
people I wouldn't expect are still in this camp.
M365 Copilot has a lot to answer for
One extremely jarring realisation was just how poor Microsoft Copilot is. It has
enormous
market share in enterprise as it is bundled in with various Office 365 subscriptions, yet feels like a poorly cloned version of the (already not great) ChatGPT interface. The "agent" feature is absolutely laughable compared to what a CLI coding agent (including Microsoft's own GitHub confusingly-named-Copilot CLI).
To really underline this, Microsoft itself is rolling out Claude Code to internal teams, despite (obviously) having access to Copilot at near zero cost, and significant ownership of OpenAI. I think this sums up quite how far behind they are
The problem is that in enterprise Copilot is often the only allowed AI tool, so that's all you can use without either potentially losing your job or spending a lot of effort trying to procure and use another AI tool. It's slow, the code execution tool in it doesn't work properly and fails horribly with large(ish) files, seemingly due to very very aggressive memory and CPU limitations.
This is becoming an existential risk for many enterprises. Senior decision makers are no doubt using these tools with such poor results and are therefore writing off AI, and/or spending a fortune with various large consulting and management consultancy outfits to get not very far.
Why enterprise is so at risk
Enterprise corporate IT policy results in a completely disastrous combination of limitations that basically ensure that people cannot successfully use more 'cutting edge' AI tooling.
Firstly, they tend to have extremely locked down environments, with no ability to run even a basic script interpreter locally (VBA if you are lucky, but even that may be limited by various Group Policies). Secondly, they're locked into legacy software with no real "internal facing" APIs on their core workflows, which means agents have nothing to connect to even if you could run them.
Finally, they tend to have extremely siloed engineering departments (which may be completely outsourced), so there's nobody internally who could build the infrastructure to run safely sandboxed agents even if they wanted to.
The security concerns are real. You definitely do not want people YOLOing coding agents over production databases with no control, and
as I've covered
, sandboxing agents is
difficult
.
However, this does cause a real problem in so much that you don't have an engineering team that can help build the infrastructure to run safely sandboxed agents against your datasets.
The gap
I've also spoken to many smaller companies that don't have all this baggage and are
absolutely flying
with AI. The gap is so obvious when you can see both sides of it.
On one hand, you have Microsoft's (awful) Copilot integration for Excel (in fairness, the Gemini integration in Google Sheets is also bad). So you can imagine financial directors trying to use it and it making a complete mess of the most simple tasks and never touching it again.
On the other you have a non-technical executive who's got his head round Claude Code and can run e.g. Python locally. I helped one recently almost one-shot converting a 30 sheet mind numbingly complicated Excel financial model to Python with Claude Code.
Once the model is in Python, you effectively have a data science team in your pocket with Claude Code. You can easily run Monte Carlo simulations, pull external data sources as inputs, build web dashboards and have Claude Code work with you to really integrate weaknesses in your model (or business). It's a pretty magical experience watching someone realise they have so much power at their fingertips, without having to grind away for hours/days in Excel.
This effectively leads to a situation where smaller company employees are able to be
so much
more productive than the equivalent at an enterprise. It often used to be that people at small companies really envied the resources & teams that their larger competitors had access to - but increasingly I think the pendulum is swinging the other way.
The future
I'm starting to get a feel for what the future of work looks like. The first observation is that (often) the real leaps are being made organically by employees, not from a top down AI strategy. Where I see the real productivity gains are small teams deciding to try and build an AI assisted workflow for a process, and as they are the ones that know that process inside out they can get very good results - unlike an often outsourced software engineering team who have absolutely zero experience doing the process that they are helping automate. I think this is the opposite of what most 'digital transformation' projects looked like in enterprise.
Secondly, companies that have some sort of APIs for
internal
systems are going to be able to do far more than those that don't. This might be as simple as a readonly data warehouse employees can connect to and run queries on behalf of users, or it could be as far as many complex core business processes being completely APId.
Thirdly, this all needs to be wrapped up in some sort of secure mechanism, but I actually think a hosted VM running some sort of code agent with well thought through network restrictions would work well, at least for read only reporting. For creating and editing data I don't think we quite have the model for non technical users (especially) to be able to use agents safely (yet).
Finally, legacy enterprise SaaS players either have enormous lock in, or are extremely vulnerable depending on how you look at it. Most are not "API-first" products, and the APIs they have tend to be really for developer usage - not optimised for thousands of employees to ping in weird and wonderful inefficient ways. But if they are the source of truth for the company, they are going to be very difficult to migrate away from
and
bottleneck a lot of productivity gains.
Again, smaller companies tend to use newer products which have far better thought through APIs (simply because they weren't often originally created many decades ago with various interfaces grafted on over time).
The user prompts, the agent synthesises - connecting to APIs and producing outputs on demand.
What I've come to realise is that the power of having a
bash sandbox
with a programming language and API access to systems, combined with an agentic harness, results in outrageously good results for non technical users. It can effectively replace nearly every standard productivity app out there - both classic Microsoft Office style ones - and also web apps. It can build any report you ask for - and export it however you like. To me this seems like the future of knowledge work.
The bifurcation is real and seems to be, if anything, speeding up dramatically. I don't think there's ever been a time in history where a tiny team can outcompete a company one thousand times its size so easily.
