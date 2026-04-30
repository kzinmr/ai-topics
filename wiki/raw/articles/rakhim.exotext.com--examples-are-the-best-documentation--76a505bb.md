---
title: "Examples are the best documentation"
url: "https://rakhim.exotext.com/examples-are-the-best-documentation"
fetched_at: 2026-04-30T07:01:13.572646+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Examples are the best documentation

Source: https://rakhim.exotext.com/examples-are-the-best-documentation

When I'm searching for docs, 95% of the time a single example would suffice. Yet, 95% of the time I can't find one in any official source.
It seems that by default formal technical documentation is targeted towards someone who's deeply immersed in the ecosystem. But many developers have to juggle a lot of "worlds" in their heads daily. When jumping between projects, languages and frameworks, it takes a considerable amount of mental energy to restore the context and understand what is going on.
Consider this
example
from the Python 3 docs:
max(iterable, /, *, key=None)
Return the largest item in an iterable or the largest of two or more arguments....
[followed by 5 short paragraphs]
.
You need to know quite a bit about Python in order to understand this:
What
*
means in the function definition.
What
/
means in the function definition.
What's a "positional-only parameter separator"
What's an iterable.
What are keyword-only arguments.
What
key
usually means.
Then you have to read some text in order to understand what values you can pass and how to actually call the function.
Granted, these are important details that can't be omitted for brevity. But I bet a lot of developers looked at that page simply because they needed to quickly find out how to pass a custom sorting function. This example would've quickly helped them:
max
(
4
,
6
)
max
([
1
,
2
,
3
])
max
([
'x'
,
'y'
,
'abc'
],  key=
len
)
max
([])
max
([], default=
5
)
Easy, right?
One popular community-based project in the Clojure world is
clojuredocs.org
, a site where people contribute examples for built in functions. It's fantastic and, in my experience, indispensable in day-to-day coding. For example, check out the pages about
into
or
spit
or
map
. Note that examples often include related functions, not only those in question. This increases the real-world usefulness and practicality.
Since even major software projects rarely offer
4 distinct kinds of documentation
, I am often hesitant to click on a "Documentation" link. Chances are, it's a terse, difficult to read, automatically generated API reference. I often choose to find a tutorial, not because I need a walk-through, but because I need examples.
