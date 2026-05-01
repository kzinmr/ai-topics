---
title: "Why I created Ethereum Proof of Stake demo"
url: "https://timsh.org/why-i-created-ethereum-proof-of-stake-demo/"
fetched_at: 2026-05-01T07:01:01.479376+00:00
source: "timsh.org"
tags: [blog, raw]
---

# Why I created Ethereum Proof of Stake demo

Source: https://timsh.org/why-i-created-ethereum-proof-of-stake-demo/

Hi there!
My name is Tim, and I’ve recently completed a project called
ether-pos
, which aims to explain how Ethereum’s Proof of Stake (PoS) system really works. If you haven’t seen it yet, check it out here:
ether-pos
.
Let me share a bit about why I created it and what I learned along the way.
Some introduction
Two months ago, I decided to dive deeper into the technical side of crypto. I’d previously dabbled in crypto and learned the basics of Solidity and TON’s FunC, but I often felt gaps in my understanding — especially when reading technical threads or hack investigations on Twitter. I wanted to bridge that gap and understand blockchain technology beyond the surface level.
So, I put together a learning plan: I created a Kanban board in Notion, set daily goals, and discussed my approach with ChatGPT.
One of my first tasks was to read
Ethereum’s Mauve Paper
— a document that lays out the roadmap for Ethereum’s transition from Proof of Work to Proof of Stake.
Facing the Mauve Paper
The Mauve Paper is a short but dense document — six pages that outline the design of Ethereum 2.0 and its transition to PoS. It starts with a straightforward introduction, which I found easy to understand.
Mauve Paper Introduction
But once I reached the first technical section, “Minimal Proof of Stake,” I hit a wall. I read that part repeatedly for about 40 minutes and still understood only half of it.
Mauve Paper 1 page later…
At this point, I had two choices: set the paper aside until I gained more context, or dig into it until I fully understood it.
I chose the latter.
I copied the text into ChatGPT and asked it to break down each section. It wasn’t straightforward — GPT didn’t understand grasp some concepts, and I had to ask over 20 follow-up questions.
But eventually, after about six hours, I finished the paper.
The surprising part? There were no mind-boggling formulas or complex algorithms — just an elegant combination of simple principles that formed the sophisticated design of Ethereum 2.0.
Knowledge gap and why it annoys me
I’ve spent a long time self-educating myself — and what I noticed in almost every field that interested me was the
huge
gap
between popular resources and professional-level explanations in almost every field.
When you search for “What is Proof of Stake?” on YouTube, you’ll find countless 5–15 minute videos that provide a decent overview.
Some are well-made and engaging, but they never fully answer how PoS works under the hood.
On the other hand, reading the Mauve Paper or any serious whitepaper is like reading someone’s thesis — it requires a lot of context to even understand the terminology.
This gap left me frustrated. I wanted both:
An in-depth understanding
of what’s happening beneath the surface.
And I’m realistic about this: if there’s any complex differential equation, for example, I might not be able to get it, but at least I digged up until I reached a brick wall.
A good user experience
— like those animated YouTube videos.
I’m ready to watch 10 or 20 of them and spend more time, but I don’t want to read a paper from a scientific journal, where I can’t understand half of the words.
The combination of these features is, in my opinion, quite rare and is often placed behind a paywall.
Worse than that, since you don’t really know what happens between the paywall, you might spend money and find that there’s nothing more than you learned from those YouTube videos.
I’ve been there.
My attempted solution: ether-pos
I wanted to find a better way to understand complex concepts without having to wrestle through scientific papers or spend hours dissecting them with AI. That’s why I decided to create the
ether-pos
project.
The goal was to take the Mauve Paper — which is complex but ultimately based on simple concepts — and present it in a way that:
Could be understood in under an hour.
Allowed for active participation and examples.
Provided enough depth to feel confident about the topic.
I read through my entire chat with GPT, highlighted key moments where I reached understanding, and translated those into an interactive web application. I used React (which I barely knew) and didn’t write any code myself, just pieced it together with tools I had available.
The end result is a step-by-step journey through the Ethereum network — from becoming a validator to betting on finality. It mirrors the Mauve Paper’s sections but transforms them into digestible, interactive steps.
Some conclusion
Looking back, I spent over 50 hours on this project — much more than I expected. Now I understand why similar resources aren’t usually freely available online: it takes a lot of time to transform such content into something accessible.
I hope to optimize this process in the future, but even so, it was worth it.
Whether or not you were interested in Ethereum PoS before, I hope
ether-pos
helps you learn something new. Initially, I created this project just for myself, but after finishing and deploying it, I realized I’d love for it to reach others who also want to understand how crypto and PoS in particular works in depth.
This is my first open-source and educational project, and my first Medium post — so I don’t have big expectations. But if you find this interesting, please feel free to share it. I’ll definitely be creating more projects like this, diving into other topics, and sharing what I learn along the way.
It’s my first time doing something non-commercial, where I don’t need to think of eye-catching headers, texts filled with value and all other annoying commercial bullshit.
And you know what? It feels amazing!
Thank you for reading this.
Share it if you liked it and subscribe to see my future work.
