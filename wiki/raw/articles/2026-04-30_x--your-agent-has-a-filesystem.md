---
title: "Your Agent Has a Filesystem, Now What?"
source: "https://x.com/i/article/2049555986143162492"
date: 2026-04-30
type: x_article
tweet_id: "2049555986143162492"
---

A few months ago we launched Airstore, an open source filesystem for AI agents. It went kinda viral, a lot of people booked discovery calls, and we even converted a few paying customers. And after all of that, I'm convinced filesystems for agents aren't going to be a standalone product.
These days the conventional wisdom on agent filesystems is pretty settled:
Agents prefer filesystems for context. Most of them are trained on coding models, and nobody wants to glue together MCPs to pull data from Salesforce or Gmail.
Filesystems are a better interface than a database. It's safer and easier for an agent to run find -name "yourfile" than to execute SQL.
You still need a database underneath. The best context layer is a filesystem interface backed by materialized views.
The more context you give an agent, the more useful it becomes.
Giving an agent a lot of context is a non-trivial storage problem.
Each of these is basically right. The mistake I made was assuming that an agentic filesystem would be a standalone product.
On the surface, there are two obvious wedges for an agentic filesystem product:
Kafka for AI agents. The streaming and storage layer (see @archildata). It's a real problem at large companies. The open question is whether the agent filesystem layer is fundamentally different from existing streaming infra and whether enough companies are ingesting context at enough scale to justify a specialized provider to manage it.
Plaid for AI agents. The integration layer that lets you authenticate and access data from many different services with a single interface. This is super useful, because companies like @zocomputer can ship hundreds of integrations into their product from Day One using @pipedream, but the value of this product lives in the integrations, not the filesystem.
I went in thinking we'd find a wedge somewhere in here. What we actually found on discovery calls was that people split into four buckets, and none of them needed a filesystem in isolation:
Bucket 1: Companies ingesting data who wanted a shared filesystem layer. They didn't need a new filesystem. They needed a volume mounted to their sandbox, which every sandbox provider already includes. We showed them how to use volumes, linked them to docs, and it solved their problem.
Bucket 2: Solopreneurs who wanted an alternative to Obsidian sync. People use Obsidian and want to ingest data into it. There's a tool for this called `obsidian sync` but it's not very reliable. The challenge with this demographic is that it's a fairly niche user with low willingness to pay. 
Bucket 3: Developers who wanted to eliminate the hassle of MCPs. A filesystem with adapters to Salesforce, Gmail, Slack, etc. solves this indirectly, but Pipedream and others already do this well. The value is in the integrations, not the storage layer underneath.
Bucket 4: Everyone else. This was the biggest bucket and the one I keep coming back to.
These were the people who got it. They saw the filesystem demo, plugged in their Gmail and Slack and Linear, watched their emails populate in a folder on their local machine, and said some version of: "ok this is awesome, but now what?"
The idea of a context layer over your digital life is extremely appealing in the abstract. However, once it actually exists, you're staring at a folder full of files and a blinking cursor. What people actually wanted was for someone to look at their data and build useful things on top of it: daily summaries, draft email replies, agents that did specific jobs inside their workflow. They didn't want storage, they wanted an application.
This is the structural problem. Infrastructure only sells when the application layer above it is mature enough that buyers know what they're plugging it into. Right now people are still figuring out what the application layer looks like, so the storage layer underneath has nothing to latch onto.
Filesystems are the correct architecture component for agents. People agree with this and they want it. But the shape of the thing it goes inside hasn't been decided yet.
The agentic filesystem will become part of a higher-level platform. The companies that win won't be selling filesystems for AI agents. Instead they'll be shipping a sandbox or a harness and providing the filesystem as an add-on underneath. The filesystem layer will be a component of the modern AI cloud platforms, but not as a product on its own. 
Everyone knows the filesystem is the truth, but it's only one piece of the puzzle.
