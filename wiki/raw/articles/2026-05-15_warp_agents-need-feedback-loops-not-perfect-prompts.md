---
title: "Agents Need Feedback Loops, Not Perfect Prompts"
source: "Warp Blog"
url: "https://www.warp.dev/blog/agents-need-feedback-loops-not-perfect-prompts"
scraped: "2026-05-15T06:00:24.578581+00:00"
lastmod: "2026-05-14T12:12:44.000Z"
type: "sitemap"
---

# Agents Need Feedback Loops, Not Perfect Prompts

**Source**: [https://www.warp.dev/blog/agents-need-feedback-loops-not-perfect-prompts](https://www.warp.dev/blog/agents-need-feedback-loops-not-perfect-prompts)

Engineering
Agents Need Feedback Loops, Not Perfect Prompts
Petra Donka
May 14, 2026
For agents doing judgement-heavy work, the starting prompt is only the beginning. The best agents learn what good looks like from the team and improve themselves over time.
Everyone is trying to write better prompts for agents. While that’s useful, it misses an important challenge: the best prompt you write today will not be the best prompt a month from now.
Your product changes. Your users change. Your team’s taste is refined over time. New edge cases present themselves. And if the agent is doing work that requires judgement and taste, no static prompt could cover everything it will need to know.
This changes the question from “how do we write the perfect prompt?” to “how do we build agents that keep learning from the team after they ship?”
We ran into this at Warp while building an agent to help our Developer Experience team respond to people mentioning us across Twitter, Reddit and other channels. We love talking to users about Warp, hearing their questions and feedback, and care deeply replying to people who talk to and about us. Folks in our community generate more than a thousand mentions per week! That’s more conversations than any small team can keep up with by hand.
The challenge with agents that almost work
In a lot of agentic development, the core loop is straightforward: the agent tries something, checks whether it worked, and retries. If it is writing code, there are often concrete signals it can use: tests, builds, browser checks, command output.
Social replies do not quite work that way, because the agent doesn't have a sensible "external check" available to it. It cannot send a bunch of public replies, wait to see whether people trust us more or less, infer whether the brand tone was right, and then retry. The feedback loop is too long, too noisy, and too expensive. The same is true for a lot of useful work inside companies: customer outreach, support replies, code review comments, product feedback analysis, docs, recruiting messages. They require knowing what matters and when not to act.
We’ve seen a lot of agents get stuck in this state: they almost work. They are clearly capable, and the output is good enough to get your hopes up, but not good enough to trust. The team keeps tweaking the prompt and hoping the next version will close the gap.
I think that’s the wrong level of abstraction. Getting an agent to do the task once is not the hard part. It is building a system where the agent gets better from the way your team already does the work.
The agent we built
We call the agent Buzz. Buzz monitors mentions of Warp across Twitter, LinkedIn, and other platforms. When a new mention comes in, it decides whether we should reply, like, note, or skip it. If we should reply, it drafts a message and posts the suggestion into Slack.
Right: feedback to Buzz in a Slack thread. Left: the daily PR where Buzz links the resulting skill updates.
Every reply is still written by us personally in the end, but this alone saves a ton of time: the team no longer has to watch every platform, open every thread, decide whether each mention matters, and start every reply from scratch. We wanted to automate as much as we reasonably could without sacrificing valuable engagement or compromising the quality. Every reply is public, represents our brand, and shapes how people experience the company. We needed the agent to learn how our team thinks about community engagement.
Principles beat rules
The first version of Buzz looked a lot like many first versions of agents: a long checklist of rules. If someone mentions a bug, say this. If someone compares us to another tool, say that. If someone asks about pricing, mention this plan.
This was very brittle. The prompt got longer, the replies were robotic, and the agent broke the moment a situation appeared that we had not told it about. So we shifted the skill from rules to principles. Instead of trying to enumerate every case, we wrote down the durable ideas that guide good replies:
Be helpful, not defensive.
Do not talk down to the user.
Check factual claims against the docs.
Sound like someone who builds the product, not someone who processes feedback.
This made the skill file smaller and the agent a lot better. The replies started to sound more like something we would actually say, and the agent could handle more situations because the instructions were no longer a giant decision tree. Principles only gave Buzz a better starting point, though. We couldn’t encapsulate everything it could possibly need.
Feedback is not learning unless the agent can generalize
Once Buzz had a decent principles-based skill, we started giving it feedback.
It would draft a reply. I would say what was wrong with it, or write the reply I would have used instead. Then Buzz would try to update its own instructions based on that feedback.
This got us to the next failure mode: the agent wanted to turn every correction back into a rule. For example, if I said a reply felt too marketing-y, it’d add a rule: “Never mention pricing in the first sentence.” The transferable principle is closer to: “If someone is venting, lead with empathy, not a pitch.” The agent needed to be taught how to learn from feedback.
So, we built a separate skill for that. It looks at the agent’s suggestion, what the human did instead, and the current instructions, then asks: what principle is missing or unclear to achieve the expected output?
The learning process is roughly:
Identify what went wrong (or right) — start from specific feedback, be concrete
Ask: why? — the failure is a symptom, find the underlying cause
Zoom out to the pattern — would this apply beyond this one case?
Check against existing principles — sharpen, edit, delete, or add?
Write it as a principle, not a rule — describe how to think, not what to do
Put it where it belongs — section matters for the agent to apply them right
Edit and commit — update the skill file, keep it tight, merge overlapping principles
It felt a lot like teaching a new team member and enabling them to learn broader ideas. A useful side effect was that feedback forced us to be clearer about our own judgement. A lot of taste lives implicitly in people’s heads. Teaching an agent forces it onto the page.
The feedback loop has to fit the team
At this point, Buzz had two pieces of the larger puzzle: principles for doing the job, and a way to learn better principles from human feedback. But, who was going to keep teaching it? We did not want a recurring meeting, or a task to assign to someone.
Buzz already posted each mention into a Slack channel with its recommendation and draft reply, so we made the feedback interface as small as possible: the team reacts with an emoji for what they actually did, and can optionally add a note in the thread. One click is enough signal; a thread is extra context.
Then, once a day, Buzz collects the reactions and thread feedback, compares its recommendations to what the team actually did, extracts durable learnings, updates the relevant skill files, and opens a PR.
That small Slack loop is what made the system work in practice. The best way to get leverage from agents is not to turn everyone into prompt engineers. It is to design workflows where the team’s normal judgement and taste become a training signal for the systems around them.
Agent skills should be treated like code
There is an obvious concern with a system like this: do you really want an agent rewriting its own instructions? Yes, but not silently. We make it safe by treating agent skills like code.
When an agent does work repeatedly, the prompt starts to become the thing you review. If those instructions determine production behaviour, they should live in a repo, with version history, review, and rollbacks. The daily learning agent does not directly change production behaviour. It opens a PR showing what feedback it reviewed, what principle it thinks should change, and the exact diff to the skill file. A human reviews it like any other change.
This gives us the useful part of self-improvement without giving up control. Buzz can continuously propose improvements, but durable changes go through review, so we can make sure it doesn’t all veer off into a weird direction.
How it's going
Today, Buzz processes thousands of mentions a month across our Twitter, Reddit, Bluesky, LinkedIn, and other channels. About half don’t need a reply, which means the team only spends time on mentions that need our attention — that's already a massive time save. Buzz runs on around 15 skills across triage, drafting, learning, analytics, and reporting. We use
Oz
for agent management and orchestration, so Buzz can run in the background and be triggered by scheduled jobs or incoming mentions.
That lets the team get more done without increasing the team size, and spend more time on what we are best at: knowing what matters, making taste calls, building relationships with the community, and deciding what kind of company Warp should feel like to someone on the outside.
The goal is compounding judgement
Agents doing judgement-heavy work need a way to learn from the people whose judgement they are trying to approximate.
Whenever we’re building a similar agent, we keep these three things in mind:
Principles
beat rules, because rules overfit and principles transfer.
Agents need to
learn how to learn
, or feedback turns into brittle exceptions.
The
feedback loop
has to live where the team already works, or people stop participating.
I do not want to remove human judgement and taste from the system. I want to make them compound. Every time the team corrects the agent, the next run should get a little better. Every durable improvement should be reviewed and checked in.
Over time, the agent becomes less like a prompt someone wrote once and more like a working memory of how the team thinks. The best teams will not just write better prompts. They will build better loops.
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
