---
title: "System One models like Jev can train their own replacements"
url: "https://seangoedecke.com/system-one-models-can-train-their-own-replacements/"
fetched_at: 2026-09-21T10:02:06.863421+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# System One models like Jev can train their own replacements

Source: https://seangoedecke.com/system-one-models-can-train-their-own-replacements/

“System One” models like
Jev
are fast general classifiers. Classifiers have existed since
1958
, but they have to be trained for specific tasks: if you build a classifier to identify images of dogs, it can’t be used to tell you if a streetlight is red, or if a letter is urgent. Like a LLM, Jev can be prompted for a wide variety of tasks, from
sorting email
to
playing Doom
.
I think models like this are going to be important. There are many tasks that a LLM
could
do in theory but are too slow and expensive in practice (for instance, reading each new message in Slack
and deciding whether to notify you or not). While you could train a specific classifier for these tasks, there are two main problems with that:
Despite being a well-understood ML problem, training a bespoke classifier is outside of the skillset of most ordinary engineering teams
Training a classifier requires assembling a large dataset
Jev obviously solves the first problem. Any engineering team can plug in a System One model with a prompt like “Based on {list of criteria}, should the user be notified about this message?” But I think it solves the second problem too.
For serious work, a specific hand-built classifier will always be cheaper and faster than Jev. Generic classifiers have to encode knowledge of all kinds of irrelevant things in their weights, so they can address lots of different tasks. That makes them larger, slower, and more expensive to run. Fortunately,
it is going to be surprisingly easy to replace a Jev instance with a hand-built classifier.
Once you’re satisfied with how your Jev classifier is performing — presumably you’ve spent days tweaking the prompt — you can trivially collect its input and output data. In the Slack notifier case, that’d be the Slack message (plus any context) and the ultimate decision to notify or not. Once you’ve saved enough data, you’ll be able to train your own classifier on that data
.
It won’t be a general classifier like Jev, but it should do well on the specific task and be much faster. Of course it’ll require some ML expertise, but it should be easier to develop (or rent) that expertise once you’ve validated that the feature is worth building.
In other words, because Jev has to be prompted for specific tasks, it should be easy to
distil
any successful Jev usage into a specific classifier. If System One models take off — and I hope they do — I expect this to be a common pattern.
Here's a preview of a related post that shares tags with this one.
Two techniques for working with System One models
I recently wrote about
Jev
, a new “System One” language model that only outputs
decisions
: the answers to a set of user-provided multiple-choice questions. This means it’s nowhere near as flexible as a traditional LLM like ChatGPT, but in return it’s consistently fast.
We don’t know exactly how Jev works. I’ve seen people say diffusion, or various tweaks to the Transformer architecture, or some entirely new type of model. But that doesn’t matter. Like I argued
here
, it isn’t hard to turn any LLM into a System One model. By batching prompts that generate a single token with structured output, you get a consistently fast general-purpose classifier. I vibed up a basic version to play with
here
in ~150 lines of Python (most of which is error handling).
Continue reading...
