---
title: "Character Prefix Conditioning · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/cpc"
scraped: "2026-05-10T01:19:50.742667+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Character Prefix Conditioning · Cursor

**Source**: [https://cursor.com/blog/cpc](https://cursor.com/blog/cpc)

Blog
/
product
Jan 6, 2025
·
product
Character Prefix Conditioning
Jacob Jackson
·
2 min read
The first in a series of problems that give a glimpse into the work we do at Cursor.
#
Setup
When using a language model for code completion, we typically want the model to produce a completion that begins with what the user has typed.
However, modern language models operate on sequences of tokens, not characters, so naively tokenizing the user's input and sending it to the model produces wrong results if the user's cursor doesn't happen to lie on a token boundary.
Instead, we need an algorithm that samples a sequence of tokens conditional on a prefix of
characters
, rather than the more typical case of sampling conditional on a prefix of tokens.
We call this
character prefix conditioning
, an algorithm for sampling a sequence of tokens conditioned on a character prefix.
We want to sample a sequence of tokens
s
=
t
1
​
,
t
2
​
,
…
,
t
n
​
from a distribution specified by an autoregressive model
p
(
s
)
given by
p
(
s
)
=
p
(
t
1
​
,
t
2
​
,
…
,
t
n
​
)
=
k
=
1
∏
n
​
p
(
t
k
​
∣
t
1
​
,
…
,
t
k
−
1
​
)
subject to the constraint that
s
starts with a character prefix
P
, i.e.
P
is a prefix of
repr
(
t
1
​
)
+
repr
(
t
2
​
)
+
⋯
+
repr
(
t
n
​
)
, where
+
means string concatenation and
repr
maps a token to the characters it represents.
We define
q
(
s
)
=
p
(
s
∣
s
starts with
P
)
. It's sufficient to find a way to sample autoregressively from
q
(
s
)
, that is, to sample from
q
(
t
k
​
∣
t
1
​
,
…
,
t
k
−
1
​
)
for each
k
.
#
Problem
Can you construct an efficient algorithm for sampling from
q
(
t
k
​
∣
t
1
​
,
…
,
t
k
−
1
​
)
, that minimizes calls to the original language model? A description of the algorithm is great. An actual implementation is excellent.
Feel free to email me your solutions at
problems@cursor.com
.
Filed under:
product
Author
:
Jacob Jackson
