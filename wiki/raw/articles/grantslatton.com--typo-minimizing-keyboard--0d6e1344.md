---
title: "Typo Minimizing Keyboard"
url: "https://grantslatton.com/typo-minimizing-keyboard"
fetched_at: 2026-04-29T07:02:15.989800+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Typo Minimizing Keyboard

Source: https://grantslatton.com/typo-minimizing-keyboard

Typo Minimizing Keyboard
I'm always frustrated when I make a typo, but the typo is of another valid word, so a spellchecker can't easily catch it.
For instance, "love" and "live" are easy to typo — 'o' and 'i' are adjacent on a QWERTY keyboard. There's a ton of these words. Precious and previous. Funding and Finding.
All these words differ in 1 letter
and
those letters are adjacent on the keyboard.
A little question I'd always wanted to answer but never got around to until now: what is the keyboard layout that minimizes the number of "valid typos".
I loaded a
word frequency dataset
and told o1-pro what to do. Below is the result. It uses
simulated annealing
to slowly optimize the layout.
There are 668 words in the dataset that have at least one valid typo. The optimizer below has found solutions that have as low as 102. There are a lot of local optima, so just restart if you get stuck for too long. I haven't tuned the algo too much.
Iteration
0
Score
0
Restart
Notes
There are a lot of ways this can be improved. Feel free to right click → view-source and chuck the source code into your favorite LLM to make modifications.
Some ideas:
This code assumes all typos are equally likely. This is definitely not true. My pinky and ring fingers probably typo 10x more often than my index fingers. Could take that into account.
This code also only considers single-typos which I guess account for the vast majority. If you do the most robust probabilistic model of different fingers being different probabilities, you can also model the whole distribution of possible typo counts — two typos in a word, three, etc.
This code also doesn't do any kind of optimization for typing speed. It would be fun to find a layout that is optimized for comfort or speed (like
Dvorak
& friends) but also typo-minimization. You could create a Pareto frontier of both variables.
I'd be interested to try with a larger dataset. The top 5000 words is probably enough that the end-result is the same, but 10K or 20K would be a tiny bit more accurate.
Send me an email or DM if you wind up improving it and I'll link your improvement or post it here.
