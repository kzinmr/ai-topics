---
title: "Are we in a GPT-4-style leap that evals can't see?"
url: "https://martinalderson.com/posts/are-we-in-a-gpt4-style-leap-that-evals-cant-see/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-01T07:02:07.090658+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Are we in a GPT-4-style leap that evals can't see?

Source: https://martinalderson.com/posts/are-we-in-a-gpt4-style-leap-that-evals-cant-see/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I feel like we've just had another GPT4 moment (after everyone being sure that scaling laws were collapsing and progress was stalled). It's more subtle than GPT4, but I think it has huge implications for many industries and potentially the economy as a whole.
Chat is a terrible eval
I've come to the conclusion that we've (mostly) maxxed out ad hoc chat as a way to evaluate models. I think everyone got very used to this being the defacto way to test LLMs - GPT4 was clearly
so much better
at answering (any) question than 3.5 that it was so obviously a big step forward.
Lately that definitely hasn't been happening, and I think most people have got to a point (especially with the hype) that each model release is a bit of a disappointment.
Over the last year or so I've found that I highly prefer speed of response to "quality" for day to day "ad hoc" usage of LLMs for answering questions in their respective UIs. I probably came to this conclusion when Gemini 2.5 Pro Preview came out (which feels like a lifetime ago, but is less than a year ago!). While it was a very impressive model, the thinking step was so slow for chatting to it that I switched back to Sonnet 3.5, which probably wasn't as good, but was vastly faster.
As such I've sort of resigned myself to the fact that my usual way of ranking models by asking them various niche questions in my industry is not a good way to get a feel for them. Speed also hugely matters to how good I think a model is, and how much I'll use it. Tl;dr, I am terrible at evaluating the quality of models based on chatting with them.
Gemini 3 Pro Preview is incredible at design
Gemini 3 has probably been the model I've been most excited about for a while. I think many people who follow LLM developments closely probably felt the same.
When it was released I started playing around with it, and while it seemed to be good I was again hitting the point where it's very difficult for me to really tell the difference between models.
However... there is one thing it is incredible at doing which I just haven't seen another model do. It's genuinely good at designing things. If you ask it to design a website or a landing page, the results that come back (mostly) look great.
This really does change things. I've been using it
so much
to build prototypes that look somewhere between passable and genuinely impressive. It genuinely feels like having a fairly good designer sitting next to you, that can come back with iterations in a couple of minutes.
But I can build prototypes with any model?!
Yes you can, but they all end up having what I call "bootstrap emoji chic", where everything looks pretty plain and absolutely inundated with emojis.
The issue with this when I've been building prototypes is that they tend to all look the same regardless of the project you're working on. With a bit more visual fidelity I find it much easier to get excited about a concept or idea (or not).
It's also far better at adhering to screenshots to give a flavour of what the existing UI/branding looks like - a very quick screenshot and a prompt will get you very far in terms of a prototype that matches branding. And if you can give it a design system (or ask it to extract one from a "real" CSS file) you can get stuff that is very much on brand, to my non-professional-designer eyes.
It's really best to try this yourself, with your own organisations branding and product. My (poor) attempts to illustrate this for this article don't really capture the "magic". This is my suggested approach to doing this is the following:
Grab your CSS file(s) for your product. Minified is fine - upload it to a new Gemini chat system and ask it to pull out a design system and an HTML example of it with the canvas tool enabled. Ask it to focus on typography, colours, elements, etc.
Open a new chat, paste in the code output from the canvas tool in the above step with a screenshot of your product (or two). Ask it to make a HTML prototype of whatever new feature you think would be cool. I strongly suspect you'll be blown away with the results visually.
You can then start creating landing pages for your new feature, and even play around with ad creative for it. It feels like you can really go a lot further on prototyping an idea from concept to actual "go to market" which for me at least is really exciting - often we get totally stuck in the code part.
I don't think any of the standard evals for LLMs test this kind of 'design taste', but it's a huge part of software/product development and it feels like Gemini 3 Pro finally crossed a line in terms of quality.
Opus 4.5?
Of course Anthropic then released Opus 4.5 a few days after - the pace is relentless.
However, the real magic of Opus 4.5 isn't for design, it's for software engineering itself (of course). I still think Claude Code is far ahead of the competition here - Codex and Gemini CLI regardless of model still just don't click for me the same way Claude Code does, and I was a bit confused at the launch of Google Antigravity, which is the 3rd (or 4th?) coding "agent" attempt from Google.
At first I noticed absolutely no difference between Sonnet 4.5 and Opus 4.5. But it does actually seem genuinely far better at not going horribly off piste. I can seemingly go for an hour or more without me having to stop and correct it going horribly wrong. It's not perfect, but when I'm interacting with it I tend to be doing minor adjustments rather than asking why on earth it's decided to install a completely new web framework out of the blue.
Again, this is hard to explain until you've used it for a while and you start realising that you are not constantly interrupting it. I've had it run some complex tasks (running analysis and building dashboards on a huge, complex, Clickhouse dataset, for example) over the past week which I'd have to babysit Sonnet 4.5, whereas Opus 4.5 has just done it. I've expected to see loads of mistakes when I've reviewed it, but it just works 95% of the time.
Between these two facts - "midlevel designer" ability, and being able to go what feels like 5x as long with an agent before things falling apart badly - it actually feels like LLMs are now capable of an order of magnitude more of a product development lifecycle.
Before it felt like we had some pretty good (if forgetful) software engineers we were managing as agents. It now starts to feel like you're managing a whole cross functional squad, with Gemini doing UX/UI/graphic design, and Opus 4.5 feeling like a far less annoying software engineer.
Are we just benchmarking everything wrong?
I think the really interesting conclusion to this is that both the things I've been so impressed with are
not
obvious knowledge retrieval, which is mentally how the industry seems to be sizing up LLMs.
The Gemini 3 design breakthrough is really a matter of taste, and I don't know of any benchmarks that test for this. It feels definitely possible - a great one would be to have a panel of designers rank screenshots of product outputs for a prompt - but instead we get endless math, science and SWE benchmarks that don't really cover this.
The second part - requiring less babysitting - I also expect most (all?) benchmarks don't test for. As far as I'm aware, benchmarks (by their nature) run a totally isolated environment with examples passing or failing. This doesn't actually really capture how at least I use coding agents. I don't just put it in yolo mode and have a very simple pass/fail for the task.
Instead it's a much more iterative process - making a plan, watching its output, interrupting it when I can see something that's not right.
I really hope the industry starts adding more benchmarks like this. We're evaluating them like STEM students at a university exam. The world doesn't work like that - we need a bit more qualitative 'taste' style benchmarking too for other roles.
This has been a
subtle
GPT-4 moment for me. I feel like I've got a whole new dimension of things I can build to an acceptable standard (design), and far more headspace to do it without constantly interrupting Claude.
And this is where I think we start seeing the broader economic impacts of this. There's been a big disconnect between benchmark scores and hypothetical GDP growth when it comes to LLMs which has had a lot of people puzzled and has given a lot of ammunition to AI being a giant hype bubble. I (highly) suspect that the link is there, but we've just been doing the wrong benchmarks.
