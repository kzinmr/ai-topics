---
title: "Human-AI partnerships are for alignment, not capability"
url: "https://seangoedecke.com/human-ai-partnerships-are-for-alignment-not-capability/"
fetched_at: 2026-09-27T10:01:13.947643+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Human-AI partnerships are for alignment, not capability

Source: https://seangoedecke.com/human-ai-partnerships-are-for-alignment-not-capability/

It’s common to compare the current AI takeover of software engineering to the rise of AI in chess. Chess AIs went from much weaker than serious players to much stronger than even the strongest humans. Between those points, there was a middle period dominated by “centaurs”: human-AI partnerships that were stronger than unassisted AIs or humans. Lots of people think that we’re currently in a world of software engineering centaurs. According to them, coding AIs are not yet capable enough to replace engineers, but AI-assisted engineers are better at programming than both AIs and humans.
This is partialy correct, but the wrong way to think about it. AI-assisted engineers are better, but unlike with chess centaurs, they’re not actually better at
programming
. When I ask agents to write code, they make fewer mistakes than I do
and are orders of magnitude faster. The code that they write always compiles, rarely has race conditions or other concurrency errors, works on mobile browsers, and so on.
That doesn’t mean I can leave the AI alone. Purely vibe-coding at work produces awful outputs. But they’re not awful because they’re bad
code
, they’re awful because they’re in
bad taste
: code that is not maintainable, that trades off important requirements in order to satisfy made-up ones, that contradicts the long-term strategy for a feature or service, and so on.
In other words, my primary value is not that I help the AI write better code, it’s that I
align
the AI with the values of my organization.
Human-AI partnerships are for alignment, not capability.
Frontier models are misaligned to the working programmer. They are obsessed with a set of behaviors that presumably satisfy their RL
grader
: writing enormous block comments above functions, producing hundreds of useless unit tests, adding little bits of text all over websites they design, and so on. Working with agents is about noticing and wrestling with those behaviors. That’s why
my prompting advice
is to explicitly talk about your high-level values: it’s an attempt to head off obvious misalignment.
This is great news for software engineers. It’s well-understood how to train more capable models: bigger models, more and better data, better
RL
environments, and so on. However, it’s not well-understood how to
align
models better. There are plenty of very capable models that exhibit behavior that is
badly misaligned
with human values. Indeed, it’s one of the main pillars of the
AI doomer
position that alignment is much harder to solve than capability, and we might thus end up with dangerous super-capable but poorly-aligned AI models.
Alignment is also more context-dependent than capability. Working code is working code, no matter what (which is partially why it’s comparatively easy to train for). But aligning to a company’s technical values is different from company to company, as any software engineer who’s switched companies knows. It can almost feel like relearning the job. So training an aligned coding model doesn’t just require hitting the exact right set of values, it requires creating a model that can adapt on the fly to a wide range of possible values.
Vibecoding maximalists like
DHH
argue that AI models are (or soon will be) so much more capable than human programmers that we ought to stop reading the code. Eventually there will be no such thing as programmers at all. If it were just about capability, they might be right. But — fortunately for software engineers — good code also has to be aligned to the technical values of the system and organization it’s embedded in. AI models are great at writing code, but not very good at doing that, and it’s unclear that they’re going to get good at it anytime soon. We might all
keep our jobs for a little while yet.
Here's a preview of a related post that shares tags with this one.
