---
title: "Expert Beginners and Lone Wolves will dominate this early LLM era"
url: "https://www.jeffgeerling.com/blog/2026/expert-beginners-and-lone-wolves-dominate-llm-era/"
fetched_at: 2026-04-29T07:02:13.951916+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Expert Beginners and Lone Wolves will dominate this early LLM era

Source: https://www.jeffgeerling.com/blog/2026/expert-beginners-and-lone-wolves-dominate-llm-era/

After migrating this blog
from a static site generator into Drupal in 2009
, I noted:
As a sad side-effect, all the blog comments are gone. Forever. Wiped out. But have no fear, we can start new discussions on many new posts! I archived all the comments from the old 'Thingamablog' version of the blog, but can't repost them here (at least, not with my time constraints... it would just take a nice import script, but I don't have the time for that now).
That would've been the case this year, when I
migrated back from Drupal to a static site
—except I wanted to test local LLMs to assist with the migration. I'd label myself an 'AI skeptic', but I admit it's impressive how well LLMs achieve certain tasks, especially if you treat them like junior devs on a small team, break down work into reasonable-sized tasks, review the work in stages (checking in code in a VCS)—as you would if you were a technical architect.
I've had experience working with a number of teams, and I'd say the two models I was using on my Mac (GPT-OSS 20B and Qwen3 Coder 30B, via Ollama) are on the lower-to-midrange end of dev teams I've worked with. "Frontier" models might be better than that, but they still don't solve all the issues prevalent in computer science!
Nota bene
: not one word of this blog post (nor any post on this blog, either in the past or in the future) was written by, or with the assistance of an LLM—and yes, I use em-dashes, which are easy to type on a Mac (⇧ + ⌥ +
-
).
Sosumi
!
When I worked full-time as a technical architect, I encountered:
Missed requirements
: Sometimes this was my own fault, but often it was a sign of a feature that was missing something important. The code would implement a feature, but lack one or two of the important bits required to get it across the line for stakeholder approval. Sometimes it was something nobody considered, but was obvious in hindsight.
Working, but suboptimal implementations
: After building at least a few hundred Drupal sites, I learned design patterns that lead to either unmaintainable disasters or efficient, maintainable sites. The more junior the developer, the more often I'd spend time with them trying to guide approaches down the less rocky path.
Premature optimizations
: The paradoxical flip-side is spending
too much
time perfecting a feature. Sometimes code will only be run one time in a migration, and it'll be irrelevant beyond that. So don't spend hours optimizing its
Big O
to shave 3 minutes off a 7 hour process!
Burnout
: Seeing patterns that lead to burnout both for myself and other devs, I tried to help project managers lighten a load or go easier on devs in the thick of it. Sometimes it was just a matter of taking a task off that developer's back, other times pulling a feature and reworking the requirements.
The LLMs I enlisted for help hit all four problems at various times (yes, even 'burnout', as their context windows would grow too large for my meager Mac mini, and I'd reset and start anew).
The big difference? I could supply a small set of requirements
, and
within 1-2 minutes, I would have code that runs
. Maybe not code that
works
, but it would be in close proximity to the code that meets all my requirements.
If I were assigning the same tasks to a small dev team, I wouldn't expect the first code back for review for at
least
a day. Maybe two. And probably a full sprint (e.g. 2 weeks) before we'd have a solution ready for QA testing.
With some initial success in getting the code I needed (coding was only about half this project), I was a little troubled:
I was able to finish this entire comment migration in a few evenings.
Being able to do that felt great, sure. But the fact 'senior' developers can be similarly productive,
without the useful work of mentoring junior devs through this process
, worries me.
AI/LLMs—even the best 'frontier' models—cannot and I believe
will never
be good at the other 80% of work involved in a task like content migration.
The best projects—the ones that don't go over budget and timeline—require technical and project management from people who ran the gauntlet as beginners.
We need people who've brought down the entire site with a bad query or migration step. We need people who've had to withstand the ire of an angry sysadmin on a weekend night their Friday deployment wiped out a database...
You don't get that for free.
With AI/LLMs, and without the mentorship aspect, you end up with two types of developers:
Expert beginners
: Junior devs who feel like they can achieve
anything
with AI coding tools. (But they don't see the enormous footguns lurking in their code.)
Lone Wolf Developers
: Devs who
did
go through the ringer earlier in the pre-AI era, and have the tools to play LLMs like an orchestra, building decent software
fast
—and
alone
. And who now have no excuse to work on teams with junior devs and be the curmudgeons
they were meant to be.
There's less of a path from #1 to #2 now. And that's even assuming you should strive to become a #2. I'd argue we need 'middle class' developers: devs who want to earn a living, clock in and clock out, and build software that helps the world run.
These developers also benefit from the mentorship (and sometimes consternation) they'd traditionally get early in their careers.
Sycophant LLMs are not a substitute for senior devs.
And they're also about the exact
opposite
of what you'd want for QA
.
I reposted this excerpt from
Migrating 13,000 Comments from Drupal to Hugo
as a standalone blog post, since the topic of how LLMs change the role of 'programmer' is something I'll write about more in the future.
