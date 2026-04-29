---
title: "AI is destroying Open Source, and it's not even good yet"
url: "https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/"
fetched_at: 2026-04-29T07:02:13.999146+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# AI is destroying Open Source, and it's not even good yet

Source: https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/

Over the weekend Ars Technica
retracted an article
because the AI a writer used
hallucinated quotes
from an open source library maintainer.
The irony here is the maintainer in question, Scott Shambaugh, was
harassed by someone's AI agent
over not merging its AI slop code.
It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.
Video
This blog post is a lightly-edited transcript of the video I published to YouTube today. Scroll past the video embed if you're like me, and you'd rather read the text :)
Impacts on Open Source
Last month, even before OpenClaw's release, curl maintainer Daniel Stenberg
dropped bug bounties
because AI slop resulted in actual
useful
vulnerability reports going from 15% of all submissions down to 5%.
And that's not the worst of it—the authors of these bug reports seem to have a more entitled attitude:
These "helpers" try too hard to twist whatever they find into something horribly bad and a critical vulnerability, but they rarely actively contribute to actually improve curl. They can go to extreme efforts to argue and insist on their specific current finding, but not to write a fix or work with the team on improving curl long-term etc. I don't think we need more of that.
These agentic AI users don't care about curl. They don't care about Daniel or other open source maintainers. They just want to grab quick cash bounties using their private AI army.
I manage
over 300 open source projects
, and while many are more niche than curl or matplotlib, I've seen my own increase in AI slop PRs.
It's gotten
so
bad, GitHub added a feature to
disable Pull Requests entirely
. Pull Requests are the fundamental thing that made GitHub popular. And now we'll see that feature closed off in more and more repos.
AI slop generation is getting easier, but it's not getting smarter. From what I've seen, models have
hit a plateau
where code generation is
pretty good
...
But it's not improving like it did the past few years. The problem is the humans who
review
the code—who are responsible for the useful software that keeps our systems going—don't have infinite resources (unlike AI companies).
Some people suggest AI could take over code review too, but that's not the answer.
If you're running a personal weather dashboard or building a toy server for your Homelab, fine. But I wouldn't run my production apps—that actually make money or could cause harm if they break—on unreviewed AI code.
If this was a problem already, OpenClaw's release, and this hiring by OpenAI to democratize agentic AI further, will only make it worse. Right now the AI craze feels the same as the
crypto and NFT boom
, with the same signs of insane behavior and reckless optimism.
The difference is there's more useful purposes for LLMs and machine learning, so scammers can point to those uses as they bring down everything good in the name of their AI god.
Since my video
The RAM Shortage Comes for Us All
in December, we have
hard drives
as the next looming AI-related shortage, as
Western Digital just announced
they're already sold through their inventory for 2026.
Some believe the AI bubble isn't a bubble, but those people are misguided, just like the AI that hallucinated the quotes in that Ars Technica article.
And they say
"this time it's different"
, but it's not. The same signs are there from other crashes. The big question I have is, how many other things will AI companies destroy before they have to pay their dues.
