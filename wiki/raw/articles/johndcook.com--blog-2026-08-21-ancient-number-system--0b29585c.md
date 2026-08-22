---
title: "How would you know whether an ancient culture had zero?"
url: "https://www.johndcook.com/blog/2026/08/21/ancient-number-system/"
fetched_at: 2026-08-22T10:01:32.949679+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# How would you know whether an ancient culture had zero?

Source: https://www.johndcook.com/blog/2026/08/21/ancient-number-system/

A few weeks ago
I wrote about the number system used in labeling spreadsheet columns. Labels run from A through Z, then AA through AZ, etc. This looks a lot like base 26, but it’s not quite the same. It has no analog of zero. If Z were like zero, Y would be followed by AZ. The Excel labeling system is not base 26, but what’s called bijective base 26.
If you found fragments of writing from an ancient culture and inferred that five symbols were used as digits, how could you distinguish base 5 from bijective base 5? Suppose you believe these five symbols were digits
★ ☂︎ ☘︎ ☗ ☢︎
but you don’t know in what order. You just see sequences like ☂︎☘︎☢︎ and ★★☂︎ and believe they’re numbers.
If you noticed that numbers often contain ☘︎, but ☘︎ never appears at the beginning of a number, you might infer that ☘︎ is a zero. But this would take a fairly large sample. If you found only 20 numbers, for example, you could hardly conclude ☘︎ never appears at the beginning of a number just because it doesn’t come at the beginning of any number you’ve seen.
Now suppose you’ve found writing with more number symbols. Say you’ve found 17 numeric symbols. You might infer that the writing used a base 20 system, because it would be hard to imagine a human culture using base 17. Now imagine you find more fragments and confirmed that indeed there are 20 numeric symbols. Approached as a purely statistical problem, you’d need a very large sample to infer what the digits correspond to and whether they use a base 20 or bijective base 20 system (or some other system).
You’re best hope is to find numbers in some context where you know what number is being represented. If you knew somehow that some symbol corresponds to 20, then you’d know they didn’t use base 20 because base
b
doesn’t have a single symbol for
b
.
If you had a huge collection of numbers but no context, which is highly unlikely, you could use
Benford’s law
to infer the meaning of the number symbols: the most common leading digit is probably 1, the next most common is probably 2, etc. This is interesting to think about, but it seems much more realistic that a number system would be decoded by finding context, such as a list of consecutive numbers or numbers with known meaning.
