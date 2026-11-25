---
title: "Memorable 12-digit primes"
url: "https://www.johndcook.com/blog/2026/11/24/memorable-12-digit-primes/"
fetched_at: 2026-11-25T10:00:48.585496+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Memorable 12-digit primes

Source: https://www.johndcook.com/blog/2026/11/24/memorable-12-digit-primes/

There’s an old joke about having to enter a 12-digit prime number to continue using a program. I wrote about this
years ago
, on how to use Python to come up with a 12-digit prime. But suppose you do this often, and so you’d like memorize a 12-digit prime so you could enter it without having to run a Python script.
Here’s an easy one: 999999999989. The following code verifies that this number is prime.
>>> from sympy import isprime
>>> isprime(999999999989)
True
Major system encoding
Maybe that’s too easy, so you’d like to first find a 12-digit prime, then memorize it using the
Major memory system
.
>>> import random
>>> while True:
...     candidate = random.randint(10**11, 10**12 - 1)
...     if isprime(candidate):
...         print(candidate)
...         break
...
298412857819
To encode 298412857819, you might come up with “knob o’ fire, tin foil, cave tuba.” These things look ridiculous when written down, but they actually work, especially when you come up with them yourself: it’s hard to reuse someone else’s mnemonics.
Working backward
To come up with a mnemonic that looks reasonable in writing, you might approach the problem the other way around: generate memorable phrases until one happens to encode as a 12-digit prime. I asked Grok to do this, and it came up with “A young man sits near the lake” which decodes to 273201024157.
>>> isprime(273201024157)
True
I read a book on memory tricks one time, and the chapter on the Major system began by stating some ordinary sentence and the corresponding number, then asked which you’d rather memorize. This was highly misleading. The author came up with the mnemonic first then calculated the number.
Mnemonics in practice
In practice the number comes first: you construct a mnemonic for a number; you don’t start with a mnemonic and search for a number it fits. And you are
far
more likely to come up with nonsensical streams like “knob o’ fire, tin foil, cave tuba” than prose like “A young man sits near the lake.” The system works, with practice, but it doesn’t
look
like it would work when you write down the mnemonics. The fact that the series of words is nonsensical may help you form durable mental images.
If you try to remember “A young man sits near the lake” you have to remember a sequence of
words
, not a sequence of
images
. “A young man sits near the lake” and “A young man sitting near a lake” correspond to the same mental image, but they’re different sequences of words and decode to different numbers. A sequence of words might be easier to remember in the short term, but a sequence of vivid mental images sticks better over time.
To be fair, “knob o’ fire” is also fragile, since “o” could easily become “of”. But this goes back to what works in practice versus what looks like it would work in writing. I chose “knob o’ fire” because it looked better in writing than some other alternatives I came up with.
In practice people who use the Major system to remember words often use
pegs
, fixed encodings of sequences of digits, rather than improvising encodings. This eliminates ambiguities. For example, suppose one of your pegs is “rover” for 484 and you imagine a Mars rover. Then when recalling a number, there’s no ambiguity whether “Mars rover” should decode to 340 (for Mars) or 484 (for rover), assuming you have a different peg for 340, such as Morse code.
