---
title: "My Least Favorite Example in Software Engineering"
url: "https://buttondown.com/hillelwayne/archive/my-least-favorite-example-in-software-engineering/"
fetched_at: 2026-11-20T10:01:14.224768+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# My Least Favorite Example in Software Engineering

Source: https://buttondown.com/hillelwayne/archive/my-least-favorite-example-in-software-engineering/

I'm doing a lightning talk at
Brooklyn Web Workers
on 11/30! If you're in the area, come check it out. If you're not in the area (like 99.90% of the world), you can just read this newsletter instead.
As you probably know, I am obsessed with examples.
Really
,
really
,
really
obsessed with examples. The best examples should at least:
Be simple enough to understand
Clearly showcase the topic under discussion
Actually correspond to how the topic manifests in the real world
Give some rough idea on how to find other examples in the same vein
Basically, the example needs to both help the student understand the topic and also why the topic matters. If not to them, at least to someone they know.
A good example of a good example is demonstrating type safety with option types, which ensure that you always handle nulls in your program. It's intuitive, clear, and simple, and it shows why and how this would be useful in practice.
But I'm not here to talk about good examples.
I'm here to talk about bad examples
Specifically my
least favorite
example.
Property-Based Testing
is a testing approach where we generate random inputs to a program and check the outputs all satisfy some property. And like half the PBT introductions online use this same example:
test reverse-reverse:
    l = random_list()
    reverse(reverse(l)) == l
I hate this example because 1) I see it every-freakin'-where, and 2) it fails the "this topic matters" criteria
hard
. It gives you some idea of what property-based testing is, but doesn't give you any way to relate it to actual real-world testing. I mean, who writes list reversal algorithms for their job?
And sure, common examples of regular testing like
add(1, 2) == 3
are also useless, but 1) regular testing is mundane and you can probably figure out more useful tests from that 2) most people can give you better examples than that! PBT, on the other hand, is quite exotic for most people and they need a lot of guidance on how to go from "learning about the concept of properties and generators" to "testing real software". It's dying for really good example, but double-reversal and similar are all ya get.
I blame John Hughes for this
Why do we use this example in the first place? I propose two reasons.
It's a really easy example to remember and share, unlike more useful and interesting examples, which often add complexity. It's also language agnostic, which should really be a separate reason but is logically kinda the same as "easy".
The first guy to talk about PBT used it and everybody followed his example.
The first guy in this case is John Hughes and
Quickcheck
. He opened his paper with reversing a list twice and the rest is history.
(He had some other examples but they quickly got into the weeds of example generation and domain-specific properties. See reason one for why double-reversing is popular.)
I shouldn't blame John Hughes for this
That's the useful part of the lightning talk. There's one more thing I want to try covering if I have time, though: While John Hughes was the guy who introduced PBT, he was not the first guy to use the double-reverse example! Zohar Manna used the example in
Inductive Methods for Proving Properties of Programs
and Boyer and Moore (yes,
that
Boyer and Moore
) used it in
Proving Theorems about LISP Functions
. Richard Bird and Philip Wadler also used the example in their book
Introduction to Functional Programming
(pg 68). So it was probably already a standard example that John Hughes took.
I'll observe that Manna/Boyer/Moore/Bird/Wadler used double-reverse as an example of
how to prove things
, while Hughes used it as a
property to test
. An example can be good in one context and bad in another.
I'll also note that Hughes did a lot of work on
efficient functional representations of lists
, so verifying double-reverse was a useful application to
his
context. It's not his fault everybody else in PBT ran with it.
And to be absolutely clear, he didn't have any kind of ethical responsibility to "pick a better example". It
does
demonstrate what PBT is. It's just not a
useful
example, and I really value usefulness in my teaching examples. Prolly more than most people tbh.
Anyway, that's roughly what I'm going to be talking about. If you've read this, you've probably seen most of the talk. I'm just going to be a bit rantier when I give it. Happy Thanksgiving to those of you who celebrate it!
Donation Drive
Still time to get
Logic for Programmers
for $20 off
! All proceeds go to the
Greater Chicago Food Depository
Update 2026-11-19
I've gotten a couple of emails asking what a
good
PBT example looks like. The one I'm probably going to use for the talk is "no interaction with the web app should cause a 500 Internal Server Error". For the Antithesis webinar last month I demoed
preserving data model invariants across API calls
, which seemed to go over pretty well. I think generally state-based properties are more intuitive and useful than pure function properties, though a little more fiddly to actually PBT.
If you want to stick with pure function properties, I think roundtrips (
to_json(from_json(x)) == x
) and oracles (
f(x) == crazy_optimized_f(x)
) are both pretty good. Those also happen to be two of the most common applications of stateless PBT.
