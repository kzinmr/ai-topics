---
title: "Phone words"
url: "https://www.johndcook.com/blog/2026/09/17/phone-words/"
fetched_at: 2026-09-18T10:00:52.182637+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Phone words

Source: https://www.johndcook.com/blog/2026/09/17/phone-words/

I recently bought a copy of Los Alamos Rolodex, a book displaying business cards from Los Alamos Nation Labs from 1967 to 1978. You can find some examples of the cards
here
.
One of the cards in the book is for Eugene Frank, President of B & F Instruments. His card lists his phone number as
(215) MErcury 9-7100
At first glance I thought the “E” in “MErcury” had been accidentally capitalized. Then I realized the intention was that someone would dial ME (i.e. 63) and ingore “rcury”. So the phone number would be (215) 639-7100.
This card was from 1968, the height of the space race. Presumably the card was alluding to the Project Mercury or the planet Mercury, or both.
The telephone keypad mapping (ITU E.161 standard) is a poor attempt at making phone numbers more memorable. For starters, there’s no way to encode 0 or 1 [1]. It’s unlikely a phone number will correspond to anything memorable unless you come up with the word first and then try to obtain the phone number, such as 800 FLOWERS.
Inserting extra letters, as Mr. Frank did, greatly increases the chances of encoding a phone number as a word. But then you need to denote which letters count and which ones are filler, so there’s not much advantage. Still, I wanted to play around with it for fun. I found 109 words [1] containing the letters from a telephone encoding of 4228646. (I’m using the file
/usr/share/dict/words
on my laptop as my list of words.)
Here are some of the more interesting hits.
semicatholicism
heartburning
gladiatorism
diabetogenic
galactogenetic
xanthocreatinine
There are over 30,000 words containing an encoding of the area code 832. One of these is
traditional
, and so I could write my phone number as
TraDitionAl semICAThOlIcisM
.
Another choice for 832 is
intercosmic
, so
inTErCosmic GAlaCTOGeNetic
is another possibility.
Galactogentic
can refer to the production of milk by the mammary glands or to the formation of galaxies (e.g. the Milky Way). Here
intercosmic
fits with the later sense.
I got greedy and tried to find a word containing the full phone number, 8324228646, but didn’t find anything.
Here’s my business card in the style of the Los Alamos Rolodex cards, created by Grok, using (832) GlAdiATOrIsM as the phone number.
Now suppose you remembered “gladiatorism” but not which letters were capitalized. Then you’d have to try up to 792, i.e. 12 choose 7, possible numbers, so this really isn’t a practical mnemonic. If you remembered “traditional semicatholicism” without capitalization it would be worse, with over a million possibilities (11 choose 3 times 15 choose 7). Some possibilities are counted twice, since different ways of selecting letters can lead to the same phone number, but still there are too many possibilities to try.
Related posts
[1] Not only are there no letters for 0 and 1, the letters O and I represent digits. At one point in time the first digit of an exchange (the middle three digits) could not be a 0 or 1, but these digits could appear anywhere else.
[2] I initially found a list of 185 words, but some of these were duplicates: a word can represent a phone number in more than one way.
