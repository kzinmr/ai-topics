---
title: "Better Batteries"
url: "https://matklad.github.io/2026/08/20/better-batteries.html"
fetched_at: 2026-08-21T10:01:06.646146+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Better Batteries

Source: https://matklad.github.io/2026/08/20/better-batteries.html

Better Batteries
Aug 20, 2026
One of the eternal schisms in programming is over the question of whether the
standard library should be minimal or encompassing. This is the wrong question
to ask. The right one is:
Which social architecture creates a high-quality standard library?
Python is always brought up as example of leaky batteries exploding in slow
motion, but this has nothing to do with
size
. The problem with Python’s stdlib
is its, ahem, uneven quality. Some standard library modules don’t follow
language naming conventions! You know which
unittest
module I am talking about
:-)
But even that is not a mistake. It’s actually Python core’s advantage — that
it makes functionality available early, not thinking about the future too much.
That’s how we ended up with ossified cAPI which makes CPython the language, but
that is
also
how we ended up with Python powering data scientific revolution.
The Go standard library is similarly encompassing, but it is held in a high
regard. Go team has institutional capacity to deliver well-designed API for the
standard library, and then some:
https://pkg.go.dev/golang.org/x
Rust is an interesting case. The 1.0 standard library APIs are brilliant.
Collections and iterators are a work of art. But it also feels that, while the
current team has the capacity to preserve existing APIs and fill in
some
gaps,
the capacity to execute design decisions is limited. While
golang.org/x
captures excess capacity,
rust-lang-nursery
is a graveyard. Maybe I am
over-indexing on
my favorite hobby-horse
,
but it seems that the reason for Rust not having an API to get a stream of
random bytes from the OS in 2026 is that, while it is an easy technical problem,
it requires tricky organization architecture (including getting money in
peoples’ pockets, of course) to actually get solved in the high-stakes
environment of a world-wide coordination problem called a programming language.
