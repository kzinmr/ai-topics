---
title: "Designing for Agents"
created: 
author_id: ""
tweet_id: "2047312986696454584"
source: x_article
---

# Designing for Agents

If you spend time in the same corner of X as I do, scrolling past the "How I built a second brain with Obsidian" and "Anthropic just KILLED [insert industry] FOREVER" posts, you've probably also seen the take that UI is dead. And unless a product can be used by agents via an MCP, API, CLI, or something in between, it won't survive.
The trend is real at Ramp. Over the past three months, weekly active users on our MCP have grown 10x as more customers reach into the product through Claude, ChatGPT, and other agents.
Last week, Salesforce became one of the first incumbents to lean into this thesis.
From VentureBeat:
Salesforce on Wednesday unveiled the most ambitious architectural transformation in its 27-year history, introducing "Headless 360" — a sweeping initiative that exposes every capability in its platform as an API, MCP tool, or CLI command so AI agents can operate the entire system without ever opening a browser.
The announcement, made at the company's annual TDX developer conference in San Francisco, ships more than 100 new tools and skills immediately available to developers. It marks a decisive response to the existential question hanging over enterprise software: In a world where AI agents can reason, plan, and execute, does a company still need a CRM with a graphical interface?
Salesforce's answer: No — and that's exactly the point.
This is a smart move by Salesforce, and one that I can't imagine was easy to make. Ask most salespeople, and they'll tell you how much they dislike using Salesforce. But the product is pervasive because of the familiarity of its UX. Sales leaders aren't interested in ramping up their teams on new technology, and consistency frequently trumps functionality.
Benioff and team are accepting that this moat is eroding and leaning into the reality that a majority of usage will be driven through agents like Claude, ChatGPT, and other background processes that users never see.
I don't think UI is dying. Humans still want to point and click, see their configurations, and verify completed work. But the 80/20 has flipped: the new 80% of interaction with software will be through agents. That changes not only what you need to build, but how you build it.
The new interaction pattern
For the past twenty years, the primary way people have interacted with software has been:
User → Interface → Database
You open a product, click around, get things done. The interface is how you experience the software. For most people, the interface is the product.
As agents take on more of the work, a new layer has emerged:
User → User's Agent (e.g. Claude) → Database
The agent acts on the user's behalf. It reads, writes, and navigates the product so they don't have to. And suddenly the interface is gone. The agent is talking directly to the system underneath.
But even this is rapidly changing. Software companies are (and should be) designing their own agents and capabilities. So the new pattern looks more like this:
User → User's Agent → Software's Agent → Database
In this model, the software's agent handles complexity on behalf of the user's agent: applying business logic, enforcing rules, pulling in context the latter doesn't have. Two LLMs working together to drive toward an outcome.
Teach agents how to succeed
I do a majority of my brainstorming, writing, and ideating with LLMs. When a draft is ready to share, I push it to Notion through their MCP server. I was a Google Docs loyalist for years; Notion's MCP flipped me.
One thing I appreciate as a Notion MCP user is how every time I ask an agent to write something, it nails it. Tables, bullets, italics, lists, you name it — the agent never fails.
This is by design.
The notion-create-pages tool's description opens with: "For the complete Markdown specification, always first fetch the MCP resource at notion://docs/enhanced-markdown-spec. Do NOT guess or hallucinate Markdown syntax." When I ask my agent to write to a page, that's the first thing it does. It fetches the spec, then writes. Every Notion-specific assumption gets explicitly called out against the general model's defaults.
In an old world, that spec would've lived in API docs, and a developer integrating with Notion would read it, internalize it, and write a transformation layer. Now Notion hands the spec directly to the agent, at the moment it's needed.
If you've ever used the Slack MCP, you've probably experienced the inverse of this. Your agent assumes standard markdown and doesn't adhere to Slack's specific formatting. You end up spending more time editing the formatting than you would have writing the message:
 
Sure, the formatting guidelines are online and you could save them somewhere and teach your agent how to use them. But that's annoying, and it shouldn't be necessary.
Think about what your agent's callers need to know to succeed, and give it to them proactively. Don't make them figure it out.
Build feedback loops
When we first launched our MCP at Ramp, observability was our largest problem. We could see tool call volume, but we couldn't see the surrounding chat context that produced those calls. Volume alone didn't tell us what was working, what was breaking, or what people were actually trying to accomplish.
We've addressed this in a few ways:
Require a 'rationale' on every tool call. Every MCP or CLI tool call requires the agent to include a rationale parameter explaining why it's making the request. We can't see the chat, but the rationale reconstructs intent. Patterns in the rationales tell us what people are actually trying to do.
A feedback tool. We shipped a standalone tool the agent can call when it gets blocked or runs into a pattern that isn't working. The agent submits what it was trying to do, what it tried, and where it got stuck.
Tool-specific seeds. We add purpose-built parameters to individual tools to capture context we'd want later: things the agent has access to that we'd otherwise have to infer.
Imagine you're building a customer support platform, and you offer tools for customers to fetch tickets. Over time, you start noticing the same phrase in rationale logs: "building an incident report," "drafting incident summary," "gathering tickets for an outage postmortem."
That's a new product feature! A build-incident-report tool could identify related tickets, score severity, pull the affected customer segment, and draft a summary in a strongly opinionated format.
Once that's live, you might start receiving feedback on the tool: "the report pulled in tickets from three days ago that weren't part of this incident" or "it keeps including tickets from free-tier users who don't belong in postmortems." All of a sudden you've got agents telling your agents exactly what to build. Agents hallucinate, sure. But they're also more specific and more consistent in their feedback than most humans you'd ever ship to.
If the report pulls irrelevant tickets, you add a date range parameter. If it shouldn't include free-tier customers, you add a segment filter. Each feedback loop becomes a new way for the product to improve.
Mind the context gap
In any agent interaction, your system has context the calling agent doesn't have, and the calling agent has context your system doesn't have. When designing these interactions, you should have an opinion about where each has a leg up.
Let's say Diego goes on a business trip. Diego's AI chief of staff picks up a Slack nudge from the expense management system's agent: he has incomplete expenses from his recent trip. Two agents are now pointed at the same outcome: submit these expenses correctly.
These two agents bring their own context.
What Diego's chief of staff brings:
Diego's calendar: knows which meetings happened, when, and with whom
Diego's email: has the hotel and flight confirmation as attachments
Diego's Slack: can correlate the Kokkari dinner to a thread where he invited the Acme team
Diego's receipts (pulled from email attachments and photo library)
What the expense management system brings:
The raw transaction data (e.g., merchant, time of transaction)
The company's policies around submission
The company's GL accounts
The company's historical coding patterns
A traditional API would dump the problem back on the user. "Here is a transaction that needs a GL code. Use this endpoint to fetch the 150 GL code options, and pick one."
A well-designed agent interaction flips this — it doesn't ask for a GL code. It asks for context: was this a client meal, a team meal, or personal travel? The chief of staff agent pulls the answer from a calendar entry or a Slack thread. The EM system applies the correct code based on the context it was missing.
Diego and his agent never need to know what the GL codes are, and the finance team gets accurate categorization. Each side contributes what it knows, and delivers an outcome that is better for Diego — and his accountant.
As you design these agent-to-agent interactions, be mindful of the context gap. It's ok to admit where your agent falls short — you're both serving the same user.
 
The interface used to sit between Diego and his expense system. Now it sits between his agent and yours.
That shift reframes the product team's job. You used to design for a human who wanted to move fast, avoid mistakes, and see their work. Now you're designing for that same person through an intermediary whose instincts, context, and limitations are different from theirs. Teaching agents how to succeed, building feedback loops, and minding the context gap all ask the same underlying question: what does your agent's caller need to do its job well, and are you giving it to them?
Most companies will ship an MCP, check the box, and move on. Their usage will grow for a few quarters, then stall. Over time, customers will route toward products that sweated the details and around the ones that didn't.
Build for the agent with the same care you spent on the human. Before you know it, it'll be the one writing the check.
