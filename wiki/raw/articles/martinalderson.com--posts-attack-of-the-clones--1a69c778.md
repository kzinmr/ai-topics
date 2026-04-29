---
title: "Attack of the SaaS clones"
url: "https://martinalderson.com/posts/attack-of-the-clones/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.131983+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Attack of the SaaS clones

Source: https://martinalderson.com/posts/attack-of-the-clones/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I cloned most of Linear's core functionality in 20 prompts using Claude Code. It took a couple of evenings and a few million tokens. Here's what I think that means for the future of SaaS economics.
A quick recap
In my previous two posts,
AI agents are starting to eat SaaS
and a more recent one about the
sharp decline in software company valuations
, I've covered some of the risks to existing SaaS businesses now agentic coding capabilities have increased so much (and perhaps more importantly, continued to improve so quickly, with no real slowdown in sight).
In these essays I argued that there are two emergent challenges to software businesses. Firstly, organisations will increasingly look to build their own "internal" versions of SaaS rather than procure external vendors.
Secondly, agents are increasingly replacing SaaS entirely. Take design - agents
can build
pretty great looking reports and slide decks without an intermediary Google Slides, Figma or Prezi step. A lot of productivity and analytics software is at risk from being completely eaten by agents.
And even the threat of this will allow organisations to push back much harder on price increases from SaaS vendors. Given so much of SaaS is now owned by PE, who have borrowed money against future (growing) revenue streams, this is a significant problem.
But do people really want to manage internal SaaS?
A (very) fair critique of a lot of the "build your own SaaS" narrative is that while people
can
build their own internal versions of SaaS, it's one thing building it and quite another managing it, updating it and running the infrastructure for it. It's hard to disagree with this - though I think it oversimplifies some of the competitive advantages companies can have from having bespoke line of business software that is perfectly aligned to their business goals.
But clearly, it's not a great idea for a company to be spending all their time building and managing tools that distract them from their main business. Adam Smith's pin factory still very much stands.
However, this overlooks that while the end
users
themselves may not want this headache of management, there
are
many people who would happily build competing platforms, manage it and sell it on for a fraction of the cost of existing SaaS vendors.
And this is where I think software companies are perhaps the most exposed.
Building a Linear alternative in 20 prompts
Please note that this was built purely for research purposes and I have no intention to release this code nor commercialise this in any way. I'm not intending to infringe on anyone's brand, copyright or other intellectual property. I'm a huge fan of Linear and think it is a brilliant piece of design and software.
To test this theory out (and to use the awesome new
Teams
feature in Claude Code), I went about seeing how possible it would be for a coding agent to replicate Linear. Linear is an excellent project management tool, which I chose to look at simply because I've read
so many
comments in reply to my article(s) saying that while building a simple SaaS clone is possible, it wouldn't be possible to build a Linear clone.
I followed a pretty simple process. Firstly, I opened my web browser with DevTools open, and browsed the platform, collecting all the network traces.
I interacted with a few features in the app so it'd have a trace of most of the software's functionality in this.
I then exported this as a HAR file (the rightmost icon above the search bar), which is an archive file of every network request. This produced an
enormous
HAR file with thousands of CSS and minified JS files.
HAR to software
I then set Claude Code off to use multiple subagents to understand all the functionality and the design of the software.
It did an
incredible
job at this, reverse engineering everything in the archive to a very high level of fidelity.
From this I used the new Teams feature in Claude Code to spin up multiple agents to start working on the front and backend of the product. This was very hands off; the first iteration was incredibly buggy, so I had to insist it start adding unit and integration tests. The quality dramatically improved after I did this.
I estimate I did 20 prompts, asking it to find placeholder content and replace it with actual functionality a few times.
A few million tokens later - which was more than covered by my $200/month Claude Max subscription - and I got a pretty faithful clone of Linear, with most key pieces of functionality working, persisting to a SQLite database.
Built entirely from reverse-engineering network traces. No source code required.
Now it's certainly not perfect and it's missing a lot of important pieces of functionality.
My point here isn't that people can copy an existing project in 20 prompts and get it
perfect
. It's that I managed with Claude Code to do this in a couple of evenings while paying very little attention. I suspect a couple of motivated engineers could get a production quality version ready in a few weeks/months. Linear has had nearly a decade of some of the best designers and developers in the industry working extremely hard on it (and it shows) - it's renowned for its impeccable design and polish. Most SaaS isn't anywhere near that level. If an agent can produce a passable clone of Linear, it can probably do a
very
good job on the vast amount of SaaS out there that is, frankly,
barely
functional.
What does this mean?
I think all SaaS is vulnerable to this to some level. Software that has significant network effects or proprietary datasets, or specialised infrastructure requirements are much more defensible, however. I expect you could even just paste the public API docs of many projects in and get a pretty workable version of the software back - the API docs usually expose a
lot
of the inherent business logic in it.
In a way this isn't anything the industry hasn't seen before - indeed the PC itself was a clone of the original IBM PC. And we've had many people build compatible implementations of many APIs - the AWS S3 object storage API, the Java APIs and even ironically the OpenAI inference API standard itself have all become de-facto industry standards. Microsoft itself famously built most of its initial marketshare by doing exactly this - building affordable "alternatives" of existing software (MS-DOS, Windows, Excel and Word were all
extremely
inspired by their contemporaries in the market).
But now I think we have the ability of a handful of people to reimplement hundreds (or thousands) of developer-years of effort in a
very
compressed timescale. And I think this will become a pervasive risk for SaaS going forward. Much like Rocket Internet in the early 2010s cloned every popular American platform going for the European market, I think we are going to see some very high quality alternatives to every major SaaS vertical - but without requiring billions of dollars of VC money to do so.
And even if these platforms
don't
get marketshare for whatever reason - they again put downwards pressure on the software pricing equations. And most importantly, it doesn't require users to manage this themselves - they can get a familiar tool at a far lower cost.
Of course, the product is only one part of the equation. Sales, marketing, customer support, compliance certifications - these are all things that existing SaaS vendors have spent years and millions building out. But I think these are increasingly solvable with very small teams now too. AI is compressing the effort required across
all
of these functions, not just engineering. A handful of people can now credibly stand up a competing product
and
the business around it.
Can SaaS companies fight back?
I'm not a lawyer, but my rough understanding is that functionality itself cannot be copyrighted. While software patents may apply, I suspect unlike a lot of other technology companies SaaS companies are very patent light - it's very hard to patent a lot of the "CRUD" workflows that SaaS is famous at helping automate.
This puts them in a difficult place legally to enforce this. While they can certainly enforce their brand and trademarks, it's much more difficult for them to send C&Ds if competitors are careful to not infringe that. Reverse engineering like this could certainly be against Terms of Service, but exactly how enforceable this is given they
ship
these files publicly is not clear to me - it's not "hacking" into their backends which is far more clear cut. And most SaaS contracts cap liability at fees paid, so even if a vendor successfully enforced a ToS breach, the damages from a $20/month subscription aren't exactly a deterrent.
They can however make it
much
harder to get your existing data out of their systems, and we are already starting to see a
lot
of API price changes in the SaaS marketplace. For example, the popular accounting platform (outside of the US),
Xero
has announced brutal API charges, which cost far more than the underlying SaaS fees in most cases. I'm not sure how related this is, but putting up tolls to get your data out is one option.
The issue though is that these APIs are just what people need to "legitimately" build agentic workflows against these products, so by making this expensive, you also reduce the utility of your product for new agentic workflows and make it more compelling for people to switch off.
Perhaps the most durable moat SaaS companies have is one that's rarely discussed:
liability
. Established vendors can take on contractual liability for data breaches, offer indemnification clauses, carry millions in cyber insurance, and back it all up with SOC2 audits and compliance certifications. Enterprise buyers are paying for more than software - they're paying for someone to be legally and financially on the hook when things go wrong. A two-person clone shop simply can't offer that. Maybe this, more than any technical moat, is what ultimately protects incumbent SaaS.
I certainly didn't have agents being able to take a HAR file and build a passable clone on my 2026 bingo card. I hope the industry finds a way to protect the incentives to build great software like Linear in the future. Because right now, I'm not sure what that looks like.
