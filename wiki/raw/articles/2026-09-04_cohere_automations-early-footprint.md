---
title: "Automation’s Early Footprint: The ATE Dataset"
source: "Cohere Blog"
url: "https://cohere.com/blog/automations-early-footprint"
scraped: "2026-09-04T06:00:46.194860+00:00"
lastmod: "2026-09-03"
type: "sitemap"
---

# Automation’s Early Footprint: The ATE Dataset

**Source**: [https://cohere.com/blog/automations-early-footprint](https://cohere.com/blog/automations-early-footprint)

Key takeaways
We aggregated seven public directories of AI tools into a new dataset: the
Agentic Task Ecosystem (ATE)
, a corpus of roughly
696,000 published tools across 123,000 MCP servers
, the largest open dataset of its kind.
Under a strict test that asks whether a tool can actually
carry out
an occupational task rather than merely inform someone doing it, only
2.6%
of tools clear the bar.
Automation of recognized work is a small slice of a very large ecosystem
. Among those that group into recognizable categories, three patterns dominate:
existing work represented at a finer grain than occupational databases record, infrastructure for running agents themselves, and a small amount of genuinely new work, most of it the work of managing agents.
Nearly half of U.S. occupations have no agentic tools represented.
Of 923 occupations, 419 show no agentic tool activity of any kind.
What gets built follows what can be built
. Expert judgments of technical feasibility predict which occupations receive tools; workers' own preferences about what they would like automated predict nothing.
The question that decides labor market outcomes isn't how much of an occupation is exposed to automation, but which parts
. Across 178 occupations, we ranked required work tasks from most routine to most specialized. In healthcare and computing, we find agentic tools exist for tasks toward the specialized end of the occupation, leaving humans the more routine remainder. In legal, production, and sales occupations, tools stay at the routine edges, leaving the specialized core with humans.
Specialized work resists automation when it is physical or interpersonal, and gives way when it is already conducted through software.
Hundreds of thousands of tools have been published to let AI systems take action on our behalf: write code, query databases, update records, schedule meetings, move information between applications. But what does this rapidly growing layer of agentic AI infrastructure actually add up to? What work are we building AI to automate?
Most of what we know about AI and work comes from one of two vantage points. Some studies estimate what AI could theoretically do, calculating
exposure
based on the percent of occupational tasks an AI system could plausibly handle. Others look at what people ask AI to do, analyzing millions of conversations to see which tasks users bring to a chatbot [
AI Observatory, 2026
;
Handa et al., 2025
;
Iscenko et al., 2026
;
OpenAI, 2026
;
Tomlinson et al., 2025
]. Both represent distinct pieces in the larger puzzle of how AI is impacting work, however, they do not represent the full picture on their own. At Cohere Labs, we are committed to helping assemble this puzzle, and our research presents new evidence from a third, complementary vantage:
the agentic-task ecosystem
.
We collected nearly 700k tools from 123k public MCP servers to create the
Agentic Task Ecosystem (ATE)
dataset and ask,
what tools have developers built to enable AI agents to fully automate certain work tasks?
What we found complicates the idea that agents are simply swallowing occupations one task at a time.
What is a MCP tool?
In the past two years, AI systems have moved from generating text to taking autonomous actions. A model that once only answered inside a chat window can now query a database, edit a file, open a pull request, schedule a meeting, or run a sequence of these tasks in order.
The
Model Context Protocol
(MCP) is an open standard for connecting AI systems to external software and data. One server might let a model work with GitHub, another might give it access to a calendar, a spreadsheet, a payment system, or a company's internal documents. In practice, a developer writes an MCP server that consists of a set of tools, each with a short description of what it does.
MCP tools as a record of what we are automating
Economists studying automation usually weigh
three variables
against each other: (1) what work humans do, (2) what work gets handed to machines, and (3) what genuinely new work appears for both. Automation displaces workers from tasks machines can perform whereas genuinely new tasks that emerge, where humans hold the advantage, reinstate them. Whichever effect is larger determines whether a technology
raises or lowers demand
for human work overall.
The first variable in this equation is relatively well documented –
occupational databases such as O*NET
break down and describe human work at the task-level (at least in an American context). The second and third variables are much harder to measure, which is why ATE is a valuable signal alongside usage and exposure data.
Every published MCP tool is a small, dated, public record of a task deemed fully automatable. A developer or builder looked at a piece of work, judged it concrete and reliable enough to hand to a machine, and packaged it as something a machine can call. That does not mean the tool is widely used, able to automate
long-horizon tasks
, or reliable enough for every workplace. As a supply-side signal measuring what has been made available rather than what is used,
ATE tells us something unique about the future of work puzzle –
where developers judge automation to be ready,
ahead
of any evidence about whether anyone has adopted it.
Building ATE
We collected 696,291 tools from 123,069 public MCP server listings across seven directories in May 2026. For each server, we recorded all listed tools’ names and descriptions, and deduplicated so that a server republished in several places is only counted once.
Public MCP corpora have been assembled before, mostly to study whether the infrastructure itself is sound and secure [
Guo et al., 2025
;
Lin et al., 2025
;
Wu et al., 2025
]. The largest of these, MCPZoo, holds 56,053 distinct servers; we hold 85% of those, plus roughly 66,000 it does not. The closest to our own question is
Stein (2026)
, which analyses 177,436 tools across 19,388 servers drawn from GitHub and the Smithery registry – asking whether a tool lets an agent perceive, reason, or act, and how consequential the affected occupation is. They report that 67% of tools and 90% of downloads are software and IT work, a concentration we see as well: among the tools in our corpus that map to any occupation, computing accounts for the majority.
For each tool, we found the closest existing O*NET task statement and asked a language model whether the tool executes that task. The protocol deliberately filters out tools that inform a user, or that handle one step of a process a person still coordinates, so what remains are tools that perform the task a statement names rather than helping someone else perform it.
Under that standard,
about one tool in forty
– 2.6% – performs a recorded work task from end to end.
One limitation is that we observe public directories only. Companies build MCP servers against their own systems and never publish them, and that missing tier is plausibly weighted toward the types of back-office processes that occupational databases describe. Vendor-published enterprise servers are included here; it is the bespoke internal tier that is absent. This bias runs against our headline since our count can only miss tools, not overcount them, therefore 2.6% is best read as a floor.
What the 2% of matched tools tells us
Where tools do match to existing work, they land unevenly. Matched tools attach to 1,380 distinct task statements, about 15% of the software-performable work O*NET records, and the occupations with the most coverage are those where a large share of the job is already conducted through software – graphic designers, for instance, have tools matching 11 of their 15 software-performable tasks. Coverage is also concentrated within occupations as well as across them. Over a thousand of the tools matched to graphic design attach to a single task statement, “Use computer software to generate new images,” which is the kind of broadly worded task that a great many general-purpose tools can genuinely perform.
Zooming out
, 419 of 923 occupations represented in O*NET have no agentic tool activity at all
. For anyone asking which jobs agentic AI is coming for, the honest answer from the supply side is that for a great many of them, no one is building anything yet.
What about the other 98% of unmatched tools
Grouping the unmatched tools by similarity produces 1,136 categories that describe work of some kind. Sorting through them, we made three distinct observations:
1) Most of it is existing work, seen at the wrong grain.
We found that 693 of the categories are what we call
subatomic
: recognizable work broken into smaller units than occupational databases use. Where a task statement says "maintain configuration control," ATE holds dozens of tools for individual components of that task. Another 411 categories of MCPs run the other way, spanning several recorded tasks or bundling them into a workflow that no single task statement names: meeting-transcript management, for instance, collects, organizes, and analyzes transcripts across what O*NET records as separate tasks. Neither kind falls outside the world of recognized work, the subatomic tools simply do not complete the whole process of what a task statement describes, and the composite ones stitch together several tasks.
2) Infrastructure for running agents.
A substantial share of the corpus consists of tools that exist so that agents can operate: registering agents, discovering other agents, managing sessions, handling identity between them. This is genuinely unprecedented work, but it is better described as the operating overhead of automation than as a new kind of output.
3) A small amount of genuinely new work, mostly about managing agents.
From early explorations into the types of work which are neither subatomic nor composite, nor infrastructure, there does appear to be a small amount of human work that is genuinely new. Only 35 categories, about 3% describe work with no plausible counterpart in the occupational record, and most of them are work that exists because agents do: selecting synthetic voices, developing and switching AI personas, assessing whether an agent can be trusted.To check that this classification held up, we hand-labelled a blind sample of 120 categories without sight of the model’s answers; the human labels point the same way, if anything finding slightly fewer genuinely new categories.
What theory gets right, and what it misses
We compared the most widely used
exposure scores
with what has actually been built. The scores, from
Eloundou et al.
, rate every O*NET task statement on whether a language model, with complementary software, could cut the time to complete it by at least half without losing quality. We find a connection between what occupations are theoretically exposed and the number of MCP tools available.
Across 178 occupations, theoretical exposure and realized MCP coverage correlate at 0.54 – a strong relationship for two measures built from entirely different evidence. On the question of
how much
of an occupation is reachable, exposure scores hold up well.
However, what exposure does not tell you is which part of a job the tooling reaches. Its correlation with where matched tasks sit inside an occupation's own mix of work is indistinguishable from zero.
The same is true of coverage depth. How much tooling an occupation has says nothing about whether that tooling touches its routine edges or its specialized core – the two are statistically independent. A heavily tooled occupation is
not
thereby one under pressure at its core.Worker preferences fare no better as a predictor. For 65 occupations,
WORKBank
surveyed both which tasks workers would like automated and how capable experts judge AI of performing them – what has actually been built tracks the expert judgments while bearing no relationship to the kinds of tasks workers actually want to be automated.
So what are the implications of automation which targets the routine edges of an occupation versus the specialized core?
Where automation lands inside a job matters
Two occupations can have similar overall exposure to a given technology and still experience very different outcomes of automation. During the computerization era, for example, accounting clerks and inventory clerks had nearly equal shares of their work exposed to automation, yet
wages rose for accounting clerks and fell for inventory clerks
. The difference was not how much work technology reached, but which types of work tasks remained after exposure.
If relatively routine tasks are delegated to AI systems while leaving specialized work to people, it could concentrate human effort on the parts of a job that require the most expertise. Economists call this
expertise-raising automation
. If AI instead performs specialized tasks that distinguish experts from everyone else, the effect could run in the opposite direction. In short, the expertise framework gives us a way to distinguish forms of automation that may have very different consequences for workers, even when the overall amount of automation looks similar.
We use this framework to conduct the first analysis on the ATE dataset. Specifically, we asked
: where do MCP tools match to each occupation’s expertise requirements, relative to that occupation's own mix of tasks
?
Where we see expertise in ATE
Across all of the 178 occupations with enough coverage to measure, on average, tools land almost exactly at the midpoint of a job’s own range of work – neither notably on the routine side nor notably on the specialized side.
But that average conceals opposite patterns. In healthcare and computing occupations the tools that exist reach toward the specialized end of the job leaving humans the more routine remainder, or what economists call,
expertise-lowering automation
. In production and legal occupations the tools stay at the routine edges, leaving the specialized core to humans and raising the barrier to entry:
expertise-raising automation
. To put a number on this, we score each occupation by how the average expertise of its remaining work would change if the matched tasks were handed to AI tools, a measure adapted from
Autor and Thompson (2025)
and shown as ΔExpertise in the chart below (positive when what remains demands more of a worker, negative when it demands less).
The chart spreads occupations by how many matched tools they have, and the flatness across that axis is itself a finding:
how much tooling a job attracts tells you nothing about which end of the job the tools reach
. Heavily tooled occupations are no more likely than lightly tooled ones to see their specialized work affected.What the groups on the specialized side share is the kinds of work they do with information. Across all 178 occupations, tools reach furthest into specialized work in roles whose core function is structuring, analyzing or managing information, and least far in roles that deliver a field’s primary service. Information work tied to a specific professional field sits highest of all: Clinical Data Managers and Biostatisticians are the clearest cases, each with 143 and 82 respectively matched tools. Even after accounting for the high number of tools available for these occupations, the pattern holds.
Computing is among the groups where tools reach furthest into specialized work, and it is the best-evidenced case in the sample, resting on thirty occupations. Healthcare practitioners are the only occupation group that sit further in the same direction, though on only five occupations.
One explanation for interpreting the findings within technical work is that developers build first for themselves. This is likely part of the story – MCP grew out of the software world and its public directories are weighted toward developer tools, which makes technical occupations unusually visible here.
But the large presence of tools matched within healthcare contexts suggests this is not the only reason. Both healthcare and computing are fields where a great deal of expert judgment is already exercised inside software. The reading we would offer is that specialized work is not uniformly hard to automate – it is hard to automate where it is physical or interpersonal, and comparatively tractable where it is already conducted through software.
Measuring a transition while it happens
ATE data tells us what kinds of tasks developers have built open-source agentic capabilities for. On its own, it does not tell us whether companies deploy those tools, or whether workers use them. Combined with
recent evidence
demonstrating a clear spike in agentic usage in enterprise contexts, it does appear that working with AI will increasingly mean deploying agentic capabilities. ATE is a measure of supply, not adoption nor economic impact: a tool’s presence tells us only that a developer judged the task concrete enough to hand to a machine, while its absence tells us that nobody has made that judgment yet. For questioning the trajectory of AI automation, the 419 occupations with nothing built for them matter as much as those with hundreds of tools. Because supply sits earlier in the chain than adoption, it can help researchers monitor, and developers build with intention, before downstream effects become visible in employment or wage data.
Our expertise analysis connects this early signal with a tangible framework to understand the expected impacts on the labor market. Averaged across occupations, tooling shows no systematic direction, but that average conceals healthcare and computing, where tools reach the specialized core and leave people the routine remainder, and legal, production and sales, where tools stay at the edges and the specialized work remains with people.
However, this raises a new question about the true outcomes of expertise-raising or expertise-lowering automation for workers. It’s not as simple as weighing one outcome as positive and the other as negative – for one, the effects on wages and employment don't move together. Automation which raises the required expertise may increase the wages of those workers, but limit the pool of qualified applicants. Automation which lowers the barrier to entry for an occupation can be viewed as
democratizing expertise
, but this doesn’t account for how skills and expertise are shaped by experience. Entry-level
workers often learn
through the routine tasks experienced colleagues and mentors hand-off. It’s already been observed that the hiring of young, entry-level workers in highly AI-exposed occupations
has fallen
well behind their peers’, and this gap has only widened over the past year. If that work is increasingly done by machines, how people become experts strikes us as one of the more important open questions about AI and work.
We are releasing the ATE dataset so that others can continue to ask their own questions of it. The public agent landscape is vast, fragmented, and changing quickly. ATE is our attempt to make that change measurable – to track not just what AI becomes capable of doing, but which capabilities developers actually turn into tools, which parts of human work those tools reach, and eventually how those choices compare with what workers want and use. If the goal is only to create capable technology that outperforms humans at most economically valuable work,
core job roles are at stake
. If one person’s substitute is always another’s complement, the true impacts of the technology on wealth and power
cannot be calculated by simply classifying technology augmenting versus automating
. Futures in which machine capabilities expand human opportunities and raise the value of labor are possible, but require early and meaningful interventions. By observing early trends, developers can build tools with intention and purpose, and decision makers can prepare for downstream impacts. The future of work will not be determined by AI capability alone.
Contributors
By
Thomas Euyang
Blog
Written By
Zanele Munyikwa
Research Fellow
Campbell Lund
Research Scholar
Marzieh Fadaee
Head of Cohere Labs
Aidan Peppin
Senior Global Public Policy Specialist
Tags
Research
Open Science
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
