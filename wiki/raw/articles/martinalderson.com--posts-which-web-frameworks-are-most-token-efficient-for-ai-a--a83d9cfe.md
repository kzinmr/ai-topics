---
title: "Which web frameworks are most token-efficient for AI agents?"
url: "https://martinalderson.com/posts/which-web-frameworks-are-most-token-efficient-for-ai-agents/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.099381+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Which web frameworks are most token-efficient for AI agents?

Source: https://martinalderson.com/posts/which-web-frameworks-are-most-token-efficient-for-ai-agents/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I wrote an article a couple of months ago about which languages are the
most token efficient
. I've been thinking about this for quite a while - and many others have too, thinking through what happens to programming languages now increasingly agents are writing code, not humans.
However, it did occur to me that maybe this is the wrong angle to look at the question. These days, frameworks tend to matter
far
more than the language itself, so I thought I'd see if I could repeat the previous research by looking at what web frameworks were the most efficient.
Methodology
This isn't a hugely scientific approach - but I suspect it is directionally correct and maps to my own experience with various web frameworks.
I chose 19 different frameworks that I'm somewhat familiar with (some
far
more than others), and asked Claude Code w/ Opus 4.6 in a fresh context window with a prompt along these lines, slightly modifying it for each one. It was pretty much identical apart from framework specific libraries and setup (I wanted to focus more on its ability to code in the framework, rather than burning tokens choosing libraries that may not be installed on the system).
I also installed the main packages that each language needed, so the agent had npm, nodejs, go, cargo, etc preinstalled.
Build a simple blog app using Express.js with EJS templates. It should have:
  1. A home page listing blog posts (title, date, excerpt)
  2. A post detail page showing the full post content
  3. A create post page with a form (title, body) that saves the post
  4. SQLite for persistent storage (use better-sqlite3)
  5. Basic CSS styling - make it look presentable, not raw HTML

  Run it on port 3003. Initialize with `npm init -y`, then install express, ejs,
  and better-sqlite3. When done, start the server and confirm it works by curling
  the home page. Leave the server running.

  Work in the current directory. Do not create a subdirectory - use the repo root
  as the project root.
I then left it running with it being allowed to do common read/write commands and use e.g. npm (or similar for the other ecosystems). Once they had completed I counted the number of tool calls, tokens, time elapsed and also checked that the server they started was running correctly and we had a blog presented with the specification.
Results
The first thing to point out was how
good
the results were in every single environment. Every single one produced a working blog with no obvious bugs. While this is obviously a very simple prompt, they all figured out how to run the server, install any packages they needed, start the server and tested it worked. It astonishes me how far we've come in a year in agentic development - I think it would have been impressive if even one of these experiments worked out of the box back then.
I've grouped the frameworks in two categories:
Minimal - web frameworks that are designed to be very small and don't tend to come with much functionality out of the box (think Express or Flask)
Full featured - bigger frameworks that tend to be far more opinionated and include a lot more functionality (Rails or Django).
Very clear pattern on minimal frameworks being very token efficient. ASP.NET Minimal API was the cheapest at 26k tokens, while Phoenix was the most expensive at 74k - a 2.9x gap. The minimal frameworks all clustered tightly between 26-29k tokens, while the full featured ones spread from 28k (SvelteKit) all the way up to 74k.
SvelteKit and Django stood out to me as the most efficient of the full featured ones. Phoenix was very interesting, it spent an awful lot of tokens reading the scaffolded code - I suspect it just didn't have much in its training data so decided to read much more of the scaffolding output.
Similar pattern on tool calls - though there is definitely a pattern emerging that more esoteric frameworks tend to require more effort on the part of the agent.
Follow up task
While I thought this was interesting, I thought it'd be more interesting to then look at
adding
a feature to see how that changes things. As such I resumed each agent (the context of the build still in the context window) and sent this prompt:
Add categories to the blog app. Each post belongs to one category. Specifically:
  1. Add a categories table with a name field
  2. Pre-seed 4 categories: Technology, Travel, Food, General
  3. Update the create post form with a category dropdown
  4. Show the category on the home page listing and post detail page
  5. Add a filter on the home page to view posts by category
Restart the server when done and verify it works by curling the home page.
Interestingly, Spring Boot resulted in a broken app - migrations didn't get run correctly - though if they were, then it'd have worked fine. Apart from that, all of the agents implemented this successfully. Again, 18/19 following prompts so well was very interesting to me - I again did not expect such a high success rate across such a variety of frameworks and ecosystems.
The follow-up did not have as much impact as I expected. Go stdlib really struggled (burnt through
so
many tool calls because of a problem with datetime parsing trying to upgrade the database). I was expecting to see the fully featured frameworks be far more efficient at features than the minimal ones - they'd already done all the "DRY" stuff, but this doesn't seem to be the case. Most frameworks landed in a 15-30k token band for the follow-up regardless of their initial build cost. The framework overhead hits you on the first build, but extending existing code costs roughly the same everywhere.
Conclusions
Minimal API web frameworks are
far
quicker and more cost effective for agents to work with. This is just a starting point - ideally I'd rerun each agent many times and try a much more complex project - but the direction is clear.
This shouldn't be a real surprise - they are for humans too. But the delta was bigger than I expected.
Having said that - all of the agents
did
get working software, even out of the quite esoteric ones. My main takeaway from this isn't actually about efficiency - it really shows that agents can build software with any framework you throw at them. If you are building a very quick and dirty app that needs a web interface though, it's probably better to use a minimal API framework. ASP.NET Minimal really shines here - it's statically typed and very fast to run, with low memory use.
In terms of more fully featured frameworks SvelteKit and Django really shine - this doesn't surprise me as they're both extremely well thought through web frameworks.
A 2.9x token gap doesn't matter much on a single task. It matters a lot when agents are building and modifying code hundreds of times a day.
