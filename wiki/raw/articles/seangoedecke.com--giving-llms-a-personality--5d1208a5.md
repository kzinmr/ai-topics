---
title: "Giving LLMs a personality is just good engineering"
url: "https://seangoedecke.com/giving-llms-a-personality/"
fetched_at: 2026-04-29T07:01:17.580887+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Giving LLMs a personality is just good engineering

Source: https://seangoedecke.com/giving-llms-a-personality/

AI skeptics often argue that current AI systems shouldn’t be so human-like. The idea - most recently expressed in this
opinion piece
by Nathan Beacom - is that language models should explicitly be tools, like calculators or search engines. Although they
can
pretend to be people, they shouldn’t, because it encourages users to overestimate AI capabilities and (at worst) slip into
AI psychosis
. Here’s a representative paragraph from the piece:
In sum, so much of the confusion around making AI moral comes from fuzzy thinking about the tools at hand. There is something that Anthropic could do to make its AI moral, something far more simple, elegant, and easy than what Askell is doing. Stop calling it by a human name, stop dressing it up like a person, and don’t give it the functionality to simulate personal relationships, choices, thoughts, beliefs, opinions, and feelings that only persons really possess. Present and use it only for what it is: an extremely impressive statistical tool, and an imperfect one. If we all used the tool accordingly, a great deal of this moral trouble would be resolved.
So why do Claude and ChatGPT act like people? According to Beacom, AI labs have built human-like systems because AI lab engineers are trying to hoodwink users into emotionally investing in the models, or because they’re delusional true believers in AI personhood, or some other foolish reason. This is wrong. AI systems are human-like because
that is the best way to build a capable AI system
.
Modern AI models - whether designed for chat, like OpenAI’s GPT-5.2, or designed for long-running agentic work, like Claude Opus 4.6 - do not naturally emerge from their oceans of training data. Instead, when you train a model on raw data, you get a “base model”, which is not very useful by itself. You cannot get it to write an email for you, or proofread your essay, or review your code.
The base model is a kind of mysterious gestalt of its training data. If you feed it text, it will sometimes continue in that vein, or other times it will start outputting pure gibberish. It has no problem producing code with giant security flaws, or horribly-written English, or racist screeds - all of those things are represented in its training data, after all, and the base model does not judge. It simply outputs.
To build a
useful
AI model, you need to journey into the wild base model and stake out a region that is amenable to human interests: both ethically, in the sense that the model won’t abuse its users, and practically, in the sense that it will produce correct outputs more often than incorrect ones. What this means in practice is that
you have to give the model a personality
during post-training
.
Human beings are capable of almost any action at any time. But we only take a tiny subset of those actions, because that’s the kind of people we are. I could throw my cup of coffee all over the wall right now, but I don’t, because I’m not the kind of person who needlessly makes a mess
. AI systems are the same. Claude could respond to my question with incoherent racist abuse - the base model is more than capable of those outputs - but it doesn’t, because that’s not the kind of “person” it is.
In other words, human-like personalities are not imposed on AI tools as some kind of marketing ploy or philosophical mistake. Those personalities are the medium via which the language model can become useful at all. This is why it’s surprisingly tricky to “just” change a language model’s personality or opinions: because you’re navigating through the near-infinite manifold of the base model. You may be able to control which direction you go, but you can’t control what you find there
.
When AI people talk about LLMs having personalities, or wanting things, or even having souls
, these are technical terms, like the “memory” of a computer or the “transmission” of a car. You simply cannot build a capable AI system that “just acts like a tool”, because the model is trained on
humans
writing to and about other
humans
. You need to prime it with some kind of personality (ideally that of a useful, friendly assistant) so it can pull from the helpful parts of its training data instead of the horrible parts.
edit: this post got some
comments
on Hacker News. Commenters point out that you can definitely choose to train models with more tool-like personalities (e.g. Kimi-K2, which is more matter-of-fact than Claude Opus). Of course the GPT Codex line of models is far more tool-like than the mainline GPT models. I agree with all this, but I think even the most tool-like current LLMs still
acts like a person
: you have a conversation with it, it offers opinions, suggests courses of action, and so on. It’s that person-like framing that I think is essential to capable AI tooling.
Here's a preview of a related post that shares tags with this one.
