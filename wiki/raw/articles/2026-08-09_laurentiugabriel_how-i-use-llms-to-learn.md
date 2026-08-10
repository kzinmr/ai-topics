---
title: "How I use LLMs to learn complex topics"
source: "https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/"
author: "Laurentiu Raducu"
date: "2026-08-09"
date_ingested: "2026-08-10"
type: raw_article
tags:
  - trending
  - active-crawl
hn_url: "https://news.ycombinator.com/item?id=49234675"
hn_points: 659
---

# How I use LLMs to learn complex topics

**Source**: https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/
**Author**: Laurentiu Raducu
**Published**: 2026-08-09
**HN Discussion**: https://news.ycombinator.com/item?id=49234675 (659 points)

Many engineers I know use generative AI for many functions, like building PoCs, internal tools or dashboards, or even learning new stuff. I personally find the style used by LLMs to explain things difficult to follow. It's just too simplistic and depending on the number of emojis used, a bit annoying too.

While I was analyzing new AI bottlenecks that might slow down data center buildup, I realized there are many aspects of chip production that I do not know. Surfing the web, I asked myself what if there would be a game to get you through the process of building a chip at a fab? For sure learning this way will stick, since you can map concepts with objects within the game. This is when I decided to try it, and it actually turned out really well.

The flow

Instead of just asking  AI to explain a topic, I use the following flow:

In plan mode (using CC, or OpenCode) I ask a model to build the foundational knowledge for X topic.

I ask it to review the accuracy of the knowledge base it built in the previous step.

I proceed asking it to build a simulation of that topic in a low-poly, Rollercoaster Tycoon-like animation. I add some UX elements as well, like the page needs to be visible on both large and small screens, have controls to stop the flow whenever I want etc.

I then push it to a new repo and enable GitHub Pages for it.

The result

What you get is a beautiful animation that is 100% accurate and free of hallucinations. For me, this method works a lot better than just reading endless materials that I find on Google, or trying to digest a bulleted list that is spat by a language model.

I've done this specifically for learning chip building and launch it under this website: 
ChipTycoon
. You get to follow a cart from the moment when sand is collected, to the moment when a chip is finalized and delivered to a data center.

Visually, you can follow the cart and see how it changes too. Since it's low-poly, the details might be missing, but it's still a good indicator for showing how the product changes once it goes through the many steps required in the manufacturing process.

How to improve it further

Let's say that the low-poly design requires to much immagination to actually visualize what happened to the quartz sand pile after it left the furnace. To transform this into a more realistic representation, you can use my 
skill for transforming pictures into 3d objects
, and map the resulting objects to your simulation. This way you get more accurate design.

Also, you can add challenges to your simulation too. Trying to answer questions about a previous step in the chip manufacturing process will help you retain the knowledge tremendously. Add intuitive puzzles too that will help you learn even better.

Check out what other pages I created:

How rocket engines are made

How LLMs work

How F1 engines are built

How an EUV machine is built
