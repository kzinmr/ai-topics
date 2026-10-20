---
title: "A frivolous problem with a deeper lesson"
url: "https://www.johndcook.com/blog/2026/10/19/regex-backtracking/"
fetched_at: 2026-10-20T10:01:30.593929+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# A frivolous problem with a deeper lesson

Source: https://www.johndcook.com/blog/2026/10/19/regex-backtracking/

About 14% of English words can be spelled by stringing together chemical symbols. For example,
sarcasm
can be written
S Ar Ca Sm
using the symbols for sulfur, argon, calcium, and samarium.
How would you write a program to determine whether a word can be written by stringing together chemical element abbreviations ignoring case? Obviously this isn’t a practical problem, but it illustrates a practical problem.
You could solve the problem with a regular expression:
(h|he|li|be|b|c|n|o|f|ne|na|mg|al|si| … |og)+
This solution could either be very efficient or very inefficient, depending on the inner workings of the software used to match the regular expression.
A DFA (deterministic finite automata) regular expression engine would find a match, or report failure, linear time, i.e. the execution time would be proportional to the length of the string being matched. A NFA (nondeterministic finite automata) engine that uses backtracking could take exponential time.
The root of the problem is the ambiguity in dividing words into single letters or pairs of letters.
Many two-letter chemical symbols are made of letters that are themselves chemical symbols. For example, the symbol for cobalt, Co, consists of the symbols for carbon, C, and oxygen, O. A traditional NFA regular expression engine uses backtracking and could take exponentially long to test whether the word
cococo…j
matches a regular expression for concatenated chemical symbols. If there are
n
copies of
co
, the engine would try all 2
n
possibilities of treating each pair as either
co
(cobalt) or
c o
(carbon oxygen).
A DFA regular expression engine always runs in
O
(
n
) time, but a (traditional) NFA can take exponential time. So why ever use an NFA engine? Because it can match more advanced patterns such as Perl regular expressions (which are not “regular” expressions in the original meaning of the term). Newer NFA engines have added safeguards to eliminate or at least reduce the chance of running into catastrophic backtracking.
