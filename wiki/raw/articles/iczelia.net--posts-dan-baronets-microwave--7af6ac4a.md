---
title: "Dan Baronet's Microwave :: Kamila Szewczyk"
url: "https://iczelia.net/posts/dan-baronets-microwave/"
fetched_at: 2026-05-05T07:01:20.444801+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Dan Baronet's Microwave :: Kamila Szewczyk

Source: https://iczelia.net/posts/dan-baronets-microwave/

The story
⌗
Dan Baronet
(6 May 1956 -
1 Nov 2016
) was an APL programmer at
Dyalog Ltd.
. He gained recognition for his unconventional and ingenious utilization of APL primitive functions, Dyalog’s Simple APL Library Toolkit (SALT) and others. Several employees at Dyalog have shared intriguing anecdotes about him:
Dan was a bit of a prankster and loved to see what tales he could get away with.  He would say things looking completely serious and wait for you to catch on that it was just a ruse.  Fortunately, I knew the telltale signs (most of the time) when he did this.
When Dan would stay with us, we occasionally took him to social events here in Rochester.  If there were kids present at the event, Dan delighted in chatting and kidding around with them and showing them magic tricks.  He was comfortable and friendly around everyone – young or old.
Fiona made mention of the “chicken broth incident”.  Dan had made chicken broth and stored it in a used milk container.  After pouring (a small amount of) broth on my corn flakes, I asked Dan if he was going to reuse milk containers like that, could he please label them so I knew they weren’t milk.  Next morning, I opened the refrigerator and there on the container was a Post-It note labeled “Not Milk”.  And yes, I did eat the corn flakes.
Dan and I would cook when we stayed in Basingstoke together.  He loved making French fries and had a very liberal interpretation of what spaghetti sauce consisted of.
Dan left a trail of forgotten and/or broken tech behind him. I have absolutely no idea how he managed to work for as long as he did on a laptop with a screen cracked from one corner to the other. The cleaners at the Dyalog house seemed genuinely concerned when he was staying because he apparently made so much work for them. His lunches in the office were legendary, consisting principally of leftovers and food well past its use-by date. In the end, it wasn’t the dodgy reheated food which took Dan from us, though I sometimes jokingly said it would be.
One such anecdote, shared with me by
Adám Brudzewsky
, inspired this code golf challenge.
Dan had remarkable microwave habits: he would input 55s instead of 1 minute, 111s for 2 minutes, and so forth. Presumably, this practice was more convenient due to reduced effort and hand movement, given that monodigital entries are quicker to enter.
The challenge posed is to write a program that, given a number of seconds, calculates the time Dan Baronet would have entered into the microwave - the nearest monodigital number (i.e., a number consisting of a single digit) based on the absolute difference (
∣
a
−
b
∣
|a-b|
∣
a
−
b
∣
).
The code
⌗
The approach starts by recognizing that the resulting number could have a smaller, larger, or equal most significant digit. Additionally, the number of digits in the result will always be less than or equal to the number of digits in the input. For instance, numbers like 980, 990, and 995 would round up to 999, but 1000 should round down to 999.
Based on this intuition, the naive solution follows:
Or, golfed:
The biggest leap in the size improvements comes from noticing the similarities in the code that computes
l
and
h
:
The line
z←(0 ¯1+≢d)∘.⍴¯1 1+⊃d
generates all combinations between
[length(in), length(in) - 1]
and
[leading_digit - 1, leading_digit + 1]
. The rest of the process remains the same as before. Although this approach involves checking more possibilities, it’s not a practical concern. Additionally, recognizing that the leading digit falls between 1 and 9 allows us to simplify the process further: Trying all these digits eliminates the need to obtain all the individual digits of the number. The focus shifts to determining the quantity of digits, which can be easily calculated using an integer logarithm.
The following golfed solution is the embodiment of all these observations:
How does APL help C programmers?
⌗
A conventional approach from a C or C++ programmer (or anyone primarily accustomed to imperative languages) would typically involve a lengthy ladder of if-else statements to address various scenarios. In contrast, the solution derived by translating the APL code directly is significantly less complex while maintaining the same computational efficiency, making it remarkably concise:
