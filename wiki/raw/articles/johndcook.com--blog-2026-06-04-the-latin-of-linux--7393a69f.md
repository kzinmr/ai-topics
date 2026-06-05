---
title: "Common patterns in Linux tools that go back to ed(1)"
url: "https://www.johndcook.com/blog/2026/06/04/the-latin-of-linux/"
fetched_at: 2026-06-05T07:01:41.183537+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Common patterns in Linux tools that go back to ed(1)

Source: https://www.johndcook.com/blog/2026/06/04/the-latin-of-linux/

One reason people study Latin is that it is the ancestor of many modern languages. English derives from West Germanic languages, not from Latin, but much of English vocabulary, perhaps as much as 60%, derives from Latin, either directly or indirectly through French.
Knowing a bit of Latin makes sense of many things that would otherwise seem completely arbitrary, such as why the symbols for gold, silver, and lead are Au, Ag, and Pb respectively.
Similarly, ed(1) is the Latin of Linux [1]. Many conventions in command line utilities follow conventions that go back to the ed(1) line editor. They may go back even further. Just as Latin didn’t come out of nowhere, neither did ed(1), but you can’t go back indefinitely. It’s convenient to start history somewhere, and this post will start with ed(1) just as much discussion of Western linguistics starts with Latin.
The following are features of ed(1) that live on in sed, awk, grep, vi, perl, bash, etc.
Using slashes to delimit regular expressions
Using $ to indicate the end of a line or the end of a file
The pattern of specifying address + action or address range + action
Using regular expressions as address ranges
Using \1, \2, etc to refer to regex captures
Using & to refer to the entire matched text
The g/regexp/command pattern
Using p for printing lines, as in g/re/p
The commands a, c, d, i, j, l, p, q, r, and w in vi
! for shell escape
[1] Because the name “ed” is so short, and looks so much like the name Ed, it’s convenient to use its full Unix name ed(1). The parenthesized number is used to disambiguate different things that have the same name, such as the user command kill(1) and the system call kill(2). There is no ed(2) or any other higher-numbered ed. The number is there to make the name stand out, not to disambiguate anything.
