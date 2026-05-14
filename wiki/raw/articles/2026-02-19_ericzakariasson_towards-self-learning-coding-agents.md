---
title: "Towards self-learning coding agents"
created: 2026-02-19
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2024535665333956960"
x_article_author: "eric zakariasson"
x_article_author_handle: "@ericzakariasson"
source: "https://x.com/ericzakariasson/status/2024535665333956960"
tags: [x-article]
---

So often, you work with coding agents when its making mistakes and you ask why don't you remember this? A human would have remembered many of the small details and feedback it'd have given. With coding agents, this doesn't come by default and they need to store this information somewhere.
You also dont wan't to manage this manually, as its a quite tedious and involved process. To solve this, we've built an experimental plugin for self learning:
https://cursor.com/marketplace/cursor/continual-learning
 
This will read existing chats, extract learnings, preferences and other relevant workspace information and then store it in AGENTS.md in a simple bulleted format.
 
Last year, we both shipped and unshipped memories. They built on a sidecar approach where a smaller model would monitor chats and extract the same information when it found something useful. We found this approach to be clunky, require more technical hoops, but most importantly not provide good memory suggestions. And that is why we unshipped it.
However, a need for long term persisted memory has not gone away. Agents have gotten better, and we have started adapting Cursor harness to be more file first focused: Dynamic context discovery
As chat transcripts are just text stored in files, agent can access them with two tools it already has access to:
Search (grep + semsearch)
Read file
One challenge becomes formatting the transcripts in way that its flexible for rendering and easy to query. Fortunately, agents are good at retrieving and reasoning over what is relevant information given the task at hand, and that has enabled a plugin like this to exist
 
Building truly continual learning on a deeper level is something that'll take time, but is something we're working towards!
Try out the plugin and let me know what you think!
