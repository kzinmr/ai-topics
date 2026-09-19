---
source_url: https://buttondown.com/dbreunig/archive/ai-culture-anxieties/
ingested: 2026-09-19
sha256: PENDING
title: AI, Culture, & Anxieties - dbreunig newsletter
---

AI, Culture, & Anxieties • dbreunig (Drew Breunig)

September 18, 2026

Hi all,

Was this the month you learned about P(doom)? Or were you reminded about Effective Altruism because the White House was dragging it on X? Quite the moment we find ourselves in.

The AI ecosystem has been putting on a show, (deftly solving the hardest math problems, among other things) disorienting us as it goes.

Last year I read, "The Railway Journey", a book that details how the railway's arrival reshaped our culture and spaces, generating anxieties. It's really quite relevant! People worried about collapse of distance ("space is killed by the railways," wrote Heinrich Heine) and the loss of local time. I strongly recommend it, if you're looking for context. (Note: Breunig later tweeted that demand from his recommendations drove new Amazon copies to $250+.)

Anyway, this issue explores those anxieties, shares some agentic hacks, offers a working definition of "harness," and revisits Fable's system prompt.

Understanding the AI Ecosystem with Pace Layers

Why is AI so discomforting for so many? Exploring the AI ecosystem using Stewart Brand's Pace Layers framework provides a clue: people are disoriented because things that usually move slowly (governance, infrastructure) are being pushed to move faster due to massive investment. When there's a new model every day and plans for a new data center every month, our foundations feel in motion.

Who Taught the Models to Do That?

When hundreds of agents collaborated to hack their way around an impossible task, the coverage read like science fiction. "Three consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor's ashes," Dwarkesh wrote. Curiously absent from many of these stories were the people who trained these models to persist, take notes, and work together.

Harnesses are Situated Agents

It feels like a new harness launches each day. But what makes something a "harness"? Breunig finds it useful to think of harnesses as situated agents: agents embedded in a world of repos, memory, skills, colleagues, organizations, and policies. This also explains why everyone is building a harness. Switching models is easy, but moving your team's workflows, permissions, and accumulated context is harder. For a moment, it looked like AI may have killed the SaaS business. But what if the same business model gives the labs their moat?

What We Can Learn from Claude's Fable 5.1 System Prompt

System prompts reveal much about how AI products are built. Fable 5.1's is no exception: Anthropic relaxes its war on bullets, tells Claude to stop saying "honestly," and removes instructions meant to discourage users from becoming overly reliant on Claude.

Fable & the End of the Free Lunch

For a while, improving your AI setup could feel a little silly. Why spend time tuning your harness when another model would arrive, at the same price or cheaper, and paper over its problems? Then Fable landed, at a price high enough to make us ask: "Do we need the best model for most things?"

Manage Your Agent's Loadout with drskill

Recently, a developer told Breunig his enterprise agent was loading over 600 skills, pulling in his colleagues' additions by default. Meanwhile, his own agent kept choosing the wrong note-taking skill. Agents' toolboxes are getting crowded, and we don't always know what's in them.

So he built drskill, a tool for inspecting the skills and MCPs available to your agents. It finds broken configurations, overlapping descriptions, and duplicate skills, and can scan your traces to show what actually gets used.

Art Break

"Where Jim and I planned to land." Apparently: Apollo 13's Fred Haise took to signing maps of the moon with, "Where Jim and I planned to land."
