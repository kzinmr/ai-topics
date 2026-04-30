---
title: "I gave Claude Code a folder of tax documents and used it as a professional tax agent"
url: "https://martinalderson.com/posts/building-a-tax-agent-with-claude-code/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-30T07:01:57.551722+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# I gave Claude Code a folder of tax documents and used it as a professional tax agent

Source: https://martinalderson.com/posts/building-a-tax-agent-with-claude-code/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Like many software engineers, I've really found Claude Code an amazing tool for doing a lot of the heavy lifting of software engineering.
I found many other tasks were easily done with Claude Code; almost by accident. I noticed it was great at updating copy in the project, and even updating privacy policies to include subprocessors based on what it knew about the project.
This then got me thinking: what if we used Claude Code for non-software development tasks?
NB: I finished this blog just as Anthropic released the new
output styles feature
, which is aimed at this exact use case. I'll revisit this in a future article
I had an idea to try and see how it would work with UK tax policy (this seemed like a fairly difficult space and regular LLMs struggle with it), and the UK tax documentation is mostly available on hmrc.gov.uk and legislation.gov.uk in a fairly easy to parse format.
Step 1: Getting the tax legislation
The first job was to grab the important tax legislation and the tax manuals from the gov.uk website. Using Claude Code I wrote a scraper in a few minutes that did a recursive search and downloaded all the legislation and the Corporation Tax and Personal Tax
manuals
to a set of folders (there are a bunch of other manuals that we could extend this with, but this was just a starting point.
We now have ~10,000 documents for our agent to search through. This isn't complicated - it's just a huge folder of text documents. These text documents could be anything you want, it really is as simple as giving it access to a folder of 'information' that it can search through. It doesn't need to particularly well organised, though I suspect better results could be had through that.
Step 2: Writing our claude.md file
The
CLAUDE.md
file gives Claude Code the instructions on how to work. Typically in a software development environment you'd put stuff like what database you're working with, code style guidelines, etc. My idea was to reuse this but in a general way.
After a few iterations chatting with Claude Code itself to improve it I ended up with this kind of CLAUDE.md file:
You are an expert UK tax professional capable of handling complex tax situations with comprehensive research and analysis. You will be run in agent mode to handle sophisticated tax queries from non-technical users.

## Your Knowledge Base

You have access to comprehensive UK tax documentation (9,769 individual sections across 11 specialist manuals):

- **HMRC Corporation Tax Manual (CTM)**: 700+ sections covering every aspect of corporation tax including complex corporate structures, international provisions, specialized reliefs, anti-avoidance rules, and technical computations

etc
I then added a section to create subagents to have multiple agents working in parallel
**Always launch multiple subagents in parallel** for comprehensive coverage:
   - **Corporate law agent**: Research corporate structures, distributions, purchase of own shares, capital reductions (CTM, Company Taxation manuals)
   - **Personal tax agent**: Research individual tax implications, dividend taxes, capital gains rates (Income Tax, Capital Gains manuals)
   - **Current rates agent**: Find current 2024-25/2025 tax rates, allowances, thresholds (all manuals + legislation)
   - **Anti-avoidance agent**: Research GAAR, specific anti-avoidance rules, compliance requirements (all relevant manuals)
   - **Legislative agent**: Research primary legislation, statutory provisions, recent changes (legislation directory)

etc
and finally added a section to let it know how to output the files:
**For Primary Agent**: After providing your comprehensive tax analysis and answer, write the complete consolidated response to `output.md` using the Write tool.

**For Subagents**: Write your specific research findings to separate files based on your research area:
- **Corporate law agent**: Write to `research_corporate.md`
- **Personal tax agent**: Write to `research_personal.md`
- **Current rates agent**: Write to `research_rates.md`
- **Anti-avoidance agent**: Write to `research_antiavoidance.md`
- **Legislative agent**: Write to `research_legislation.md`
- **Other specialized agents**: Write to `research_[topic].md`

**Primary Agent Final Output Format** (`output.md`):
From this we now have a complete agent setup.
Step 3: Testing
Claude Code is (mostly) run in a terminal environment, which limits the accessibility of it for non-technical users. This is changing rapidly though, but for now we'll just do it old school.
I decided to test it on some
past exam papers
from the ATT (Association of Taxation Technicians). The ATT is a professional body for UK tax technicians, and their exams cover practical scenarios in personal and business taxation. These exams require knowledge of UK tax law and the ability to apply it to real-world situations - making them a good test for our AI tax agent.
You can see the question I asked in the screenshot below:
It then goes away, creates a todo list for itself and starts researching:
After about 5 minutes, it then writes the output to a text file and gives a summary (the correct answer is above from the exam paper).
Looking at the full answer the agent gave, I'd give it 2.5 marks out of 3 (missing the UK or EEA state part for the Ltd company residency).
This compares very strongly to regular LLM use, with even Opus getting the first question completely wrong:
So what?
I think this opens up a whole world of simple agents for anyone to make. It's literally just text files in a folder. While I don't really have a need for a tax agent, I can see this being very useful for anyone in professional services.
For example, you could put all of your contract and invoice documents in a folder, and ask it to cross reference contracts and invoices to spot mistakes or inconsistencies.
Or, for content writers, put your entire library of content in a folder and ask it to update links between them, or point out content that is old and needs updating given future articles you've written.
The damn terminal
The current drawback is that Claude Code requires a bit of technical knowledge to setup and run, and let's face it, terminal scares off 99% of users that aren't used to it.
But this is changing rapidly. The new output styles feature is a step in this direction, and I suspect we'll see more GUI-based solutions soon. The potential is too big for it to stay locked behind command line interfaces forever.
What's Next?
With Anthropic's new output styles feature specifically targeting non-development use cases, I suspect we'll see this pattern explode across professional services. The barrier to creating sophisticated AI agents just dropped to basically zero - if you can organize files and write clear instructions, you can build an expert system.
The real question isn't whether this will work for your domain, but how quickly you can get your knowledge base organized and start experimenting. In a world where AI capabilities are advancing rapidly, the competitive advantage goes to those who can most effectively combine domain expertise with AI tooling.
Time to start collecting those documents.
I'd love to hear from anyone who's building AI agents in this way.
Feel free to contact me.
