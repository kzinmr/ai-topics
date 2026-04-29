---
title: "Solution-space Taste"
url: "https://grantslatton.com/solution-space-taste"
fetched_at: 2026-04-29T07:02:16.005438+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Solution-space Taste

Source: https://grantslatton.com/solution-space-taste

Solution-space taste
There's a visual analogy I've been drawing on whiteboards for years to explain a key element of taste in software design.
Imagine the problem domain as a 2D field of obstacles you're trying to get across:
In this analogy, a path represents a solution. Suppose you're trying to get from the center of the bottom to the center of the top.
A common failure mode of junior engineers is only considering what obstacle is directly front of them. They'll tend to produce solutions like this:
That is, junior engineers will tend to just keep grinding through obstacles as long as they feel like they are making some progress. They may actually get to a solution, but it's often really overcooked.
Coincidentally (or perhaps not), LLM coding agents like claude-code, Windsurf, et al have a similar junior engineer taste failure mode. The meme is they'll get some react.js error and decide the next logical step must be to change the source code of react, instead of stepping back and thinking about new paths.
After developing more taste, an experienced software developer learns to "feel" when the local solution space they find themselves in is unexpectedly complex, and this is a strong heuristic to backtrack.
They'll produce solutions more like:
That is, at each place they find themselves, they'll do a little local exploration to "feel in the dark" where things are going, and pretty aggressively backtrack if they find complexity.
I previously wrote about
an extreme form of this
someone described to me in which you only allow yourself 1 day to implement the whole feature, and if it takes longer than a day, that's a signal you don't understand the space well enough yet and should start over.
As you get even better, and you find yourself in familiar spaces that you have experience when and know pretty well, you can get even better results by exploring parts of the space out of order to act as an even stronger heuristic.
Once you've done this "initial scouting", you can often connect the sketched pieces even faster than just doing it from start to finish, because you know the general direction you're heading, and have a good intuition you'll be able to connect them because you've explored this space or a similar one before.
Obviously, anyone can draw lines on a map and say it's better to take the short path than the long path. This is a
super
rough analogy. In practice, the spaces you find yourself in are way more complicated than 2 dimensions. And the choices you make affect what walls will be present later on.
The analogy is just an intuition pump about how you should be thinking about navigating problem spaces. You really want to cultivate your sense of taste for what solutions are likely overcomplicated, and which are beautifully clean. You want to be able to
feel
when you've wandered into a space that's probably more complex than it needs to be.
The main way to develop this sense of taste is to write a lot of code. Explore a lot of spaces. If you're a junior engineer, you need to get your first 100K lines of code written as fast as possible. There might be other ways, but I don't know them.
In addition to writing 100K lines of code, it helps
a lot
to get feedback on that code by better programmers than yourself.
What you might have perceived to be a wall standing in the way of a beautiful solution might actually be a door that just needs a little trick to open. It's possible to find these tricks yourself — after all, someone invented them — but it's a lot faster to be shown by a trusted mentor.
Worse than direct feedback, but better than nothing, is reading code written by great programmers. You can pick up a few tricks this way if you read
very carefully
, but they may not be obvious to you because you're less specifically motivated than you are when solving your own problems.
Hopefully this intuition pump is useful to you, and that you start to think about your own search heuristics through the solution space.
