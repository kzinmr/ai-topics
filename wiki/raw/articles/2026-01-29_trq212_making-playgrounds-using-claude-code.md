---
title: "Making Playgrounds using Claude Code"
created: 2026-01-29
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2017024445244924382"
x_article_author: "Thariq"
x_article_author_handle: "@trq212"
source: "https://x.com/trq212/status/2017024445244924382"
tags: [x-article]
---

We've published a new Claude Code plugin called playground that helps Claude generate HTML playgrounds. These are standalone HTML files that let you visualize a problem with Claude, interact with it and give you an output prompt to paste back into Claude Code.
I've found this can be really good interacting with the model in ways that are not well suited for text, for example to:
Visualize the architecture of the codebase
Adjust the design of a component
Brainstorm layouting and design 
Tweak the balance of a game
To get started, install the plugin in Claude code by running the following commands:
/plugin marketplace update claude-plugins-official 
/plugin install playground@claude-plugins-official

Here are some of my favorite playgrounds I've made:

Changing the design of the AskUserQuestion Tool in Claude Code
prompt: "Use the playground skill to create an playground that helps me explore new layout changes to the AskUserQuestion Tool"
 

Critiquing your writing and getting a response 
prompt: "Use the playground skill to review my SKILL.MD and give me inline suggestions I can approve, reject or comment"
 

Tweaking a Remotion Video Intro
prompt: "Use the playground skill to tweak my intro screen to be more interesting and delightful"
 
 
Viewing an Architecture Diagram and letting the user comment
prompt: "Use the playground skill to show how this email agent codebase works and let me comment on particular nodes in the architecture to ask questions, make edits, etc"
 
Balancing the Superhero Rogue-like game I'm making
prompt: "Use the playground skill to help me balance the 'Inferno' hero's deck"
 
Excited to see how you all explore this! 

My tip for creating an interesting playground- think of a unique way of interacting with the model and then ask it to express that.  I think you might find it surprising. 

If you make something cool, please share it! 
