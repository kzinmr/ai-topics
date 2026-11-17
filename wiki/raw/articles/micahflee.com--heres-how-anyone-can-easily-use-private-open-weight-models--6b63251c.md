---
title: "Here's how anyone can easily use private, open weight models"
url: "https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/"
fetched_at: 2026-11-17T10:00:44.675167+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# Here's how anyone can easily use private, open weight models

Source: https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

It's impossible to deny that, despite all the slop/data centers/environmental destruction/theft, LLMs are incredibly useful and powerful.
It's also impossible to deny that
OpenAI and Anthropic suck
and you can't trust them with your data.
Luckily, you don't need them.
You also don't need a prohibitively expensive computer with lots of GPUs and RAM, and you don't need to be an expert on LLMs.
Because of the AI bubble, when most people think about LLMs, they assume that OpenAI and Anthropic are the only good options. In reality, there are tons of models and providers and a diverse ecosystem of open source tools that you can use with them.
💡
Models can be completely closed and proprietary, like OpenAI's GPT models or Anthropic's Claude models. If you want to use these, you have no choice but to go through OpenAI or Anthropic. Or they can be "open weight," which means anyone can download and host them. Unlike closed models, it's possible to run open weight models privately.
Unless the frontier labs decide to allow it, it's not possible to run your own closed models, or to use them without sharing your data with the companies that make them. The most powerful open weight models are from Chinese companies, but some are also from US companies and from around the world.
The nice thing about using something like Claude is that there's no learning curve: You sign up, install the software, and just start using it. You don't have to know what a model is, or understand inference, harnesses, or anything else. You just tell Claude what you want it to do. (And, of course, send a copy of whatever private data you're working with to Anthropic, and pay them money – both things that would be nice to avoid.)
So, in an effort to help people switch to open weight models as easily as possible, this blog post shows you how to use
Maple AI
just as easily, with no learning curve required.
There are lots of other ways of doing similar things. I like software like OpenCode and Pi, and there are other good providers too. Everything, including what models are available, changes constantly.
I'm writing about Maple because they have a nice, mature, and user-friendly product that just works. I don't get money from them or anything like that. Maple is an LLM provider that runs open weight models in TEEs, which basically just means that, unlike OpenAI and Anthropic, they can't spy on your conversations.
💡
Maple lets you choose between popular open weight models. At the time of writing, this includes: DeepSeek V4.1 Flash, GLM-5.3 Flash, GLM 5.3, Kimi K3.1 Pro, and others.
It also includes
DeepSeek V4.1 Flash Uncensored
, a version of DeepSeek V4.1 with all cyber safeguards removed from the weights. Basically, this means
you can use it for security research and it won't constantly tell you no
.
Though, in my experience, the open weight models rarely block you anyway. Claude and ChatGPT have a
cop looking over your shoulder
, after all.
Sign up for Maple AI
Check out Maple's
pricing page
. Maple has a free plan, but I'm going to sign up for the $20/month Pro plan because it lets you use its nice desktop app and gives you API access.
When you're ready, create an account and pay for the Pro plan.
💡
It's outside the scope of this post, but Maple also accepts Bitcoin. That means that if you don't make any OPSEC mistakes, and you can get your hands on some anonymous Bitcoin, you can use powerful open weight models privately and anonymously.
Try out the chatbot
The simplest thing to try first is the chat interface on Maple's website. It's basically just like using ChatGPT or Claude, except it's private.
For example, in the feature image of this post, I sent the prompt:
DDoSecrets recently published Icepick, an internal database with details about over 41k DHS employees: https://ddosecrets.org/article/icepick
Help me find all of the public projects online where people have visualized this data or made it searchable.
After doing a bunch of web searches and then inference, it responded with: "Here's what I found — note the ecosystem is shifting as domains get hit with takedown pressure, so treat this as a snapshot of what's up as of today," followed by a bunch of links to projects.
Install the desktop app
Chatbots can be useful, but they're nothing compared to agentic AI: software that runs on your computer, can write code, use tools, run scripts, etc.
💡
You have to be careful when you let a program like Maple Work (or Claude, or Codex) access your data and execute programs on your computer. While in might not be likely for many tasks, it could easily break things, delete things, share your data, or make your computer less secure.
The safest way to run agentic AI is to run it in its own isolated sandbox. For Mac, you can use a program called
GhostVM
to easily spin up new isolated macOS VMs, and then run Maple Work inside those, where it only has access to the data you give it access to.
So next, download and install
Maple Work
. Once you open it, log in to your Maple account. Maple Work looks a lot like the web app chatbot, but it's more powerful because it's running directly on your computer instead of in a browser. For each chat session, you can choose a project folder.
For example, using the default Maple workspace (
~/Documents/Maple/Workspace
on the Mac I'm using), I chose to use GLM 5.3 on "low" reasoning. I sent it this prompt based on a question someone asked me the other day:
in this 2025 blog post, Bluesky describes how trusted verifiers and verified accounts work:
https://bsky.social/about/blog/04-21-2025-verification
Is there a public list of trusted verifiers? If it's not human readable, is it in any of the Bluesky/atproto-related github repos? Or, can you write code to scour atproto data for it?
It did a bunch of research, figured out that it's nontrivial to get the list, and wrote a Python script for me that does it anyway.
The Maple Work desktop app, working on the Bluesky trusted verifier problem
You can use Maple Work the same way you would use the Claude or ChatGPT desktop apps:
You can do
agentic coding
, complete with agent skills.
You can give it a folder with Word documents and PDFs and get it to read them all for you and answer questions about them.
You can have it troubleshoot computer problems for you, or get it to
reverse-engineer
your internet-of-things tech and flash your own non-shit firmware onto it.
The biggest difference between doing this with Maple and doing it with Claude or ChatGPT is that:
It's private. You're not handing loads of data to Maple like you do when you use the frontier labs. All Maple can see is that you're burning tokens, not what you're doing with them.
You get to use powerful open weight models. The big ones are honestly about as good as the frontier models. Because they're open, it's possible for third-party providers like Maple to run them without vendor lock-in. (And maybe, if you someday get access to a powerful enough computer, you can run them yourself too.)
The biggest downside, IMO, is the cost.
Because there's an AI bubble and OpenAI and Anthropic are drowning in billions of dollars of cash, they're able to massively subsidize their products. If you use as many tokens as they give you access to in their $20/month plans, it will cost them many thousands of dollars. With their pricing structure, they're constantly losing money. But they can get away with this because, as long as the bubble hasn't popped, they don't care.
While the paid plans for Maple, OpenAI, and Anthropic all start at $20/month, you'll run out of tokens in Maple much quicker than running out in OpenAI or Anthropic. If you don't use a massive amount of tokens, this won't be a problem.
I hope this helps open people's eyes to how easy it is to start using open weight models! You really can use powerful AI without giving your money and data to Trump-aligned anti-competitive Silicon Valley tech oligarchs that insist on their right to spy on you.
