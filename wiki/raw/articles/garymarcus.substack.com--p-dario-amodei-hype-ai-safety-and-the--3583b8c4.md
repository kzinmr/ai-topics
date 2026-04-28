---
title: "Dario Amodei, hype, AI safety, and the explosion of vibe-coded AI disasters"
url: "https://garymarcus.substack.com/p/dario-amodei-hype-ai-safety-and-the"
fetched_at: 2026-04-28T07:01:30.945289+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# Dario Amodei, hype, AI safety, and the explosion of vibe-coded AI disasters

Source: https://garymarcus.substack.com/p/dario-amodei-hype-ai-safety-and-the

AI coding tools are genuinely revolutionizing the software industry, but more than almost anything I have ever seen, they fall into the category of things you maybe shouldn’t try at home without significant prior experience:
Ujjwal Chadha
@ujjwalscript
Stories of vibe coded disasters piling up on Reddit

Unless YOU intervene and build out a structure for AI, it is going to push slop.
7:03 AM · Apr 26, 2026
·
167K Views
247 Replies
·
147 Reposts
·
1.58K Likes
And, see especially
this long, thoughtful report of another case
, which has gone completely viral.
Excerpt from a long essay worth reading.
Such a total failure was, of course, totally predictable (as I noted on X
in a tweet with around 2 million views
), and unsurprising in a system that mimics data without truly understanding what was asked of it.
And I am sure we will see many more catastrophic failures soon enough, involving things like privacy, security and data loss. Already there have been many.
But what does this have to do with Anthropic’s CEO Dario Amodei? And who is to blame? And what does it all mean?
§
I’ll get to the latter two questions in a moment. Perhaps the most important point, one that goes well beyond coding, is at the end.
But, first, the reason that I bring up Amodei is his steady hype for AI coding, and especially this, from a couple day ago:
Anthropic CEO (Dario Amodei):

"Coding is going away first, then all of software engineering."

What do you think about this?
8:00 PM · Apr 25, 2026
·
1.92M Views
323 Replies
·
52 Reposts
·
753 Likes
I don’t know if this is a case of pump and dump prior to the upcoming IPO or he if really believes what he said.
But what he is saying is that we can  eliminate not just line coders but the people who architect and maintain systems. That seems to me to be vastly overhyping what autonomous AI is currently in a position to do.
And I am far from alone.  For example, software architecture legend Grady Booch called out Amodei harshly on X, writing
“
I think that @DarioAmodei does not understand software engineering and  that he is working feverishly to pump up the valuation of his company in anticipation of its forthcoming IPO.
”
The influential software engineer Gergely Orosz was equally critical, writing that “
The only people who believe any of [what Amodei said] are non-coders
” and clarifying that the tools only work in a fully trustworthy way when they are supervised in domains in which the user already has experience.
Absurd
remarks like Amodei’s
hype
the idea that coding agents are all we need. They are not.
§
When disaster strikes, a lot of people want to blame the user.
And there is some merit to that. The user
should
have had separate offsite backups (and do many many other things. For sure, every experienced programmer should know this.
But we just created a whole generation of vibe coders who don’t.
And we now have a legion of synthetic coding agents (like Cursor) that also apparently don’t always follow these kinds of basic principles (e.g., always keep independent backups), either.
𝗪𝗵𝗶𝗰𝗵 𝗶𝘀 *𝗲𝘅𝗮𝗰𝘁𝗹𝘆* 𝘄𝗵𝘆 𝘄𝗲 𝘀𝗵𝗼𝘂𝗹𝗱 𝗻𝗼𝘁 𝘁𝗿𝘂𝘀𝘁 𝗰𝗼𝗱𝗶𝗻𝗴 𝗮𝗴𝗲𝗻𝘁𝘀.
§
People keep blaming the users for the growing number of vibe-coded fiascos. Doing so is *half* right.
Users
are
screwing up - by letting vibe coded stuff access their files, without proper backups, without proper monitoring, without adequate sysadmin, etc.
But that’s
exactly why
we still need software engineers — and why what Amodei recently said about software engineers disappearing is so absurd.
Skilled coders can use vibe-coded tools, with careful oversight.
But amateurs using vibe-coding tools are asking for trouble.
Using them without a strong prior working knowledge in coding and software maintenance and sysadmin *is* the mistake.
§
Another thread on X is about why some coders are starting to write code by hand again, after their initial infatuation with coding agents.
All the best programmers I know are starting to write code by hand again
7:15 PM · Apr 25, 2026
·
1.38M Views
659 Replies
·
330 Reposts
·
6.6K Likes
What’s the answer? Part of it is (as the above author notes in his thread), because with AI it’s “too easy to slopify a codebase” – which means after you write the code, it’s hard to maintain it. (For example, people sometimes wind up with multiple copies of data, which can wind up causing hard-to-diagnose downstream problems). Maintainability is yet another serious issue beyond the recurring issues of data loss, privacy leaks, and security breaches. In the long run, it may be the most serious.
§
Now here’s the interesting thing. Tools like Claude Code
can actually
be very useful. (As noted in a previous essay, they are neurosymbolic, not pure LLMs, but that’s a story for a different day.)
But you have to know what tweets like these mean, and how to act on them, to use them safely:
Chen Avnery
@MindTheGapMTG
We run 12 AI agents in production. Zero slop. The difference is constraint files that define what the agent is NOT allowed to do. Scope boundaries, permission gates, naming conventions. AI without guardrails is just a very fast intern with no supervision.
1:52 PM · Apr 26, 2026
·
3.12K Views
5 Replies
·
5 Reposts
·
71 Likes
And most people don’t.
In the hands of very skilled practitioners
who pay a lot of attention, and treat the outputs with considerable scrutiny,
coding agents can be astonishing. But that kind of expert knowledge, which coding agents can’t be counted on for, is exactly why we need to keep software engineers in the loop. And it is why most of us who are in the know have such a hard time taking Amodei’s hype about getting rid of software engineers (who look at the whole problem, and not just isolated bits of code) seriously.
§
But I have one more lesson, it’s the most important one, relevant even if you aren’t a coder and never plan on using these tools. And it is this:
AI agents are wildly premature technology that is being rolled out way too fast. The deepest lesson about the vibe coded AI agent disaster story that is running around is NOT about losing your data.
𝗜𝘁’𝘀 𝗮𝗯𝗼𝘂𝘁 𝗔𝗜 𝘀𝗮𝗳𝗲𝘁𝘆.
The user in the lost data situation wasn’t (totally) naive. He thought (and makes explicit in his essay linked above)
system prompts
(hidden prompts that are built in by the AI companies) and guardrails would save him.
They didn’t.
What the user known as @lifeof_jer discovered was, in his own words, that system prompts—the basis for much of the mediocre work that passes as technical work in “AI safety” these days – were merely “advisory, not enforcing”, things the system often follows, but not always.
In other words, coding agents, and by extension most of generative AI, can’t reliably follow rules. A system that can’t be trusted to follow its own rules can’t be trusted. Period.
In this case the user just lost data. Eventually people will lose lives.
Gary Marcus
had a cameo on Last Week Tonight, last night
.
[Unfortunately, because of licensing arrangements, the link works only in some geographic regions.]
Thanks for reading Marcus on AI!  Please consider sharing this post!
Share
