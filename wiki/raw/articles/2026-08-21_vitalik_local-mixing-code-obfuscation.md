---
title: "Obfuscation (Part III): Local Mixing"
author: "Vitalik Buterin"
source: "vitalik.eth.limo"
url: "https://vitalik.eth.limo/general/2026/08/21/obfuscation_part_iii_local_mixing.html"
date: "2026-08-21"
fetched_at: "2026-08-24"
type: raw_article
tags:
  - cryptography
  - white-box
  - code-obfuscation
  - llm-code-comprehension
---

# Obfuscation (Part III): Local Mixing

Vitalik Buterin, "Obfuscation (Part III): Local Mixing", published 2026-08-21 on vitalik.eth.limo. Special thanks to Nicholas Ho, Ran Canetti and Janmajaya Mall for feedback and review.

## Summary (raw note)

Third installment of Buterin's 3-part series on cryptographic obfuscation (indistinguishability obfuscation, iO). Parts I–II covered (1) the mainstream conservative iO line built on near-standard assumptions with "galactic overhead" and (2) "diamond iO" (lattice-based, much lower overhead but still not viable to run). This post covers the third major family: **local mixing**, described as "a totally different way of doing cryptography" — no elliptic curves, no prime factorization, no lattices; the closest regular-crypto analogue is symmetric cryptography (encryption/hash function design) and secure hardware design.

## The threat model

Motivation: stop LLMs from comprehending source code (code obfuscation against AI code understanding — see Part I/II of the series; HN discussion notes AI can "read" code better than humans, making classical obfuscation insufficient). Goal of local mixing: take a circuit C (XOR/AND/NOT gates) and apply transformations such that the result computes the same function but no detectable relationships remain between executions of the obfuscated circuit and the original.

## Pipeline (six stages)

Original circuit → adding reversibility → hardening → gadgetization → mixing → final compression (fcompress).

1. **Adding reversibility** — convert to reversible gates (e.g. Toffoli-style; T blocks behave the same forwards and backwards) so the circuit can be shuffled.
2. **Hardening** — introduces must-be-zero / must-be-one helper wires and the u_delta flip trick to make inputs "hot".
3. **Gadgetization** — replace gates with nonlinear gadget representations (secretshare14 etc., stacked constructions) to defeat exact linear attacks on the whole trace.
4. **Mixing** — "repeatedly making transformations to a small part of the circuit at a time. Each transformation preserves functionality while destroying (or rather, confusing and diffusing) some amount of visible information about structure." Sub-techniques:
   - *Generation mixing*: giant table of all small circuits with the same functionality; grab gate sets, look up the equivalence class, replace with a random other circuit from the same class, then move it to a random legal position. Production version takes groups of ~7–10 gates; the "rainbow table" is in the hundreds of gigabytes (plus a smaller curated table); canonicalization + polynomial-form conversion make storage fast.
   - *Splitting*: broaden the gate set and split gates (e.g. r57 gate decomposed into two-gate forms) to create conditions for shuffling.
   - *Crossing walk*: gates move through the circuit leaving "residues" for each gate crossed.
   - *Final compression (fcompress)*: shrink the result.
5. **Sandwiching** (S' step) — overhead ≈2x instead of ≈4x, no extra u_delta wire; operates on random permutations with no must-be-zero ancillas.

## Security analysis

- Targeted attacks: exact linear matches (Gaussian elimination, O(|Obf(C)|)^≈2.8), exact degree-k matches, correlations with weight-k linear/nonlinear functions (sparse LPN / MOS algorithm O(|Obf(C)|)^≈0.7k).
- Complementarity: gadgetization converts circuits into representations that avoid these attackers; mixing forces attackers to search all of Obf(C) rather than an identifiable subset.
- "Big key cryptography" regime: each gate is part of the noise protecting every other gate (unlike FHE where each ciphertext is independently attackable).
- Conservative parameter example: terabyte (2^43 bits) obfuscated circuit trace takes minutes on consumer hardware; Gaussian elimination needs 2^129 steps (≈2^122 with Strassen), and ≈10^25 bytes to store the matrix — within cryptographically-secure bounds.
- Random bit flip attacks: three layers of defense; bit flips land in junk wires, gadgets, or sandwich layers.
- Epistemology: "completely alien" compared to reduction-based cryptography — heuristic grab-bag like symmetric cryptography (confusion & diffusion tradition) and secure hardware design; sits "on a graveyard of failed attempts at white-box cryptography".

## Raw article body (full text below)

# Obfuscation (Part III): Local Mixing 

 2026 Aug 21 
See all posts

 
 

 Obfuscation (Part III): Local Mixing 

Special thanks to Nicholas Ho, Ran Canetti and Janmajaya Mall for
feedback and review

In the last
two parts
of this series, we have gone through two of the major families of
cryptographic obfuscation (iO) protocols: the mainstream and
conservative line that tries to build it from somewhat-close-to-standard
cryptographic assumptions, but at the cost of galactic overhead, and
diamond iO, which adds more novel lattice-based assumptions, and reduces
the overhead massively - but still not by enough to make it viable to
run. In this post, we will go through the third major family being
worked on today, called "local mixing".

The first thing to note about local mixing is that this is a
totally different way of doing cryptography. There are no
elliptic curves, no prime factorization and no lattices anywhere here.
In fact, the closest thing that "regular" cryptography has to what is
going on here is symmetric cryptography - encryption
and hash function design.

In symmetric encryption and hash function design, there are no clean
reductions to well-structured mathematical problems like "if you can
crack this, that would imply you can quickly factor very large numbers".
Instead, there is a fifty-year-long tradition of people attempting to
create functions that are pseudorandom, mathematicians attacking them,
and people figuring out design tricks that protect against those
attacks, until the whole thing stabilized and we have secure hashes like
SHA and BLAKE today. The goal of local-mixing is to take that
tradition, and apply its ideas to circuits - achieving the
properties that symmetric cryptographers have learned that their core
building blocks need to achieve - while being
functionality-preserving.

This is a wild and risky bet; it sits on a graveyard of failed
attempts at white-box
cryptography. The local mixing authors' hope is that if we push even
more effort into this direction, and are smarter about it, including
using AI to speed-run the three decades that hash functions took to
stabilize and get to equal maturity in a few years, and at the same time
we accept higher overhead, then we could make something that works.

## How does local mixing work?

The goal of local mixing is to take a circuit \(C\) (made
up of logic gates, eg. XOR, AND, NOT), and then apply a series of
transformations to it, which preserve the functionality of \(C\), but
progressively remove any ability to see its internal logic.

The obfuscation pipeline

Six
coloured boxes joined left to right: original circuit, adding
reversibility, hardening, gadgetization, mixing, obfuscated
circuit.

original
circuit

- 

adding
reversibility

- 

hardening

- 

gadget-
ization

- 

mixing

- 

Obf(C)

- 
- 
- generation
mixingsplitting
andcrossing
walkfinal
compression

At a high level, the most important idea is exactly what you might
guess from the name "local mixing": add a whole bunch of junk gates,
shuffle everything around, and repeatedly replace small portions of the
circuit with different sets of gates that have the same
functionality.

But as you can see, that is only one step in the pipeline - the
mixing step. The bulk of the cleverness is in the other steps in the
pipeline - the steps that set up for circuit to be friendly to mixing,
and that are optimized to remove some information leakage in the
underlying circuit that is difficult for mixing to fully address.

Let us go through these steps one by one. We will start off with
adding reversibility, because that step is necessary to set the stage
for mixing, and then sandwiching. Then, we will talk about how mixing
works. After that, we will talk about the limits of mixing as it stands
today, and describe the major helper that was added to compensate:
gadgetization.

## Adding reversibility

As our example, we will use the same circuit that you may have
already seen earlier in this series: the two-bit adder.

The first step is to convert the circuit \(C\) into a reversible
circuit: a circuit that can be run backwards as well as forwards.

The main reason why this is done is that reversible circuits are far
more friendly to mixing. A single reversible gate can be replaced with
an arbitrarily large number of other reversible gates that all add up to
having the same functionality as the original gate. Doing that with eg.
AND and OR is much more difficult.

A key reason why is that irreversible computation
collapses entropy: AND collapses 00, 01 and 10 into
the same output, and likewise with OR and 01, 10 and 11. And so, long
chains of irreversible gates will by default destroy huge amounts of
information, proportional to the length of the circuit. A big-enough
random reversible circuit is plausibly a secure cryptographic
permutation, a big-enough random irreversible circuit degenerates into
having only a few possible outputs.

There are ways to generate big irreversible circuits that
don't have this property. For example, if the two-bit adder above
returned both \(a+b\) and \(b\) itself,
and avoided returning the x100 digit of \(a+b\) (so the addition becomes
wraparound), then it would be a reversible circuit made out of
irreversible gates: every output would have a single valid corresponding
input. But such techniques basically end up reinventing reversible
circuits, and so it's easier to just use reversible circuits as the base
medium directly.

The choice to go with reversible circuits echoes time-worn wisdom
from symmetric cryptography: even in irreversible applications like hash
functions, the core underlying building block is a reversible
permutation, and the irreversibility comes from a thin layer on top,
precisely in order to make sure that for as long as possible, the full
"state space" of the circuit is actually reachable.

In the case of our two-bit adder, making it reversible looks like
this:

Two-bit adder built entirely from r57 gates

Fourteen
horizontal wires: four input bits, a wire pinned to one, a wire pinned
to zero, and eight ancilla wires starting at zero. Sixteen r57 gates are
grouped into eight dotted boxes of two gates each, one box per gate of
the original adder. The bottom three wires carry the three sum
bits.

XOR
AND
XOR
OR
AND
XOR
AND
OR

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 
a
[x1]
a
[x10]
b
[x1]
b
[x10]
1
0
0
0
0
0
0
0
0
0

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

a
[x1]
a
[x10]
b
[x1]
b
[x10]
1
0
a₁∧b₁
a₁₀⊕b₁₀
a₁₀∨b₁₀
a₁₀∧b₁₀
c₁∧(a₁₀∨b₁₀)
a+b
[x1]
a+b
[x10]
a+b
[x100]
positive
controlnegative
controlactive
pin
Flips
the active pin if either the positive control is 1 or the negative
control is 0.
Dotted
box = one gate of the original adder, now two r57 gates.

Notice a few things here:

- The new circuit is made out of many copies of an "r57"
gate, which has three inputs and three outputs. The core logic
is: flip wire C unless wire A equals 0 and wire B equals 1. The outputs
on wire A and B stay the same. Each "standard" two-input-one-output gate
can be implemented with two r57 gates.

- We now draw the circuit in a style that is easier to reason about
mathematically. There is a well-defined "state" at each point in the
execution - drawing a vertical line through the circuit, it's the values
on each wire as they intersect that vertical line. Gates are arranged in
sequence from left to right. Each gate has three coordinates that
represents the positions of the three wires that it acts on.

- The circuit needs a whole bunch of extra "junk" inputs, of which one
is expected to be 1 and the rest are expected to be 0. Two of these junk
inputs (the topmost 0 and 1) assist the construction of "standard" gates
through r57 gates. Others hold the result of intermediate computation.
And the ones at the bottom are the space onto which the output is
written.

You now have a two-bit adder that you can run forwards or backwards -
sort of. If you try to just put 101 into the output position and zeroes
in the other positions, and walk through the gates right to left, you
won't wind up with 010 + 011 in the input positions, or 100 + 001,
you'll wind up with total junk. The ability to actually run the
original computation backwards depends on having not just the
final output, but also the final values on each intermediate wire on the
circuit.

The main thing that we have gained in this step is that we have an
object that does the same thing as \(C\), but in a format that is
naturally much more friendly to mixing.

## Hardening

The next step is a hardening step. We take a reversible circuit \(C\) as a
starting point - either the output of the previous reversibilization
step, or some "natively reversible" circuit. The goal is to transform it
in such a way that, without manipulating the gates, there is no way to
use the circuit that does anything other than executing \(C\) on some
input and getting the output.

There are two ways in which this condition gets violated:

- Reversibilization often (as above) creates helper wires (often
called "ancillas"), that must be zero. If the ancillas are set to
nonzero, it risks leaking internal behavior of \(C\) in
arbitrary ways.

- The reversibilized version of \(C\) can, well, be run in reverse. We
don't actually want this. We want to use reversible circuits as a
medium, but we don't want \(C\) to be runnable in reverse.

The main technique to deal with this is called the hardened
Toffoli technique, and works as follows.

We add two new sets of wires:

- One extra ancilla wire, called \(u_{\delta}\), as well as its
helpers \(u_1 ...
u_j\). The construction does not assume anything
about \(u_{\delta}\)'s value - it can come
in as 0 or 1, and it comes out with the same value that it came in.
\(u_1 ... u_j\)
can come in as any values, and leave unchanged.

- Output wires, new wires \(y_1 ... y_k\)
that the output gets copied to. Again, the construction assumes nothing
about these wires' contents: it simply xors \(C(inputs)\) into this position, so
if they come in as \(y_1 ... y_k = X\) they come out as
\(y_1 ...
y_k = X \oplus C(inputs)\)

Here is what the gates look like:

- Run \(C\)

- If \(u_{\delta} = 0\), set \(y_1 ...
y_k\ {\oplus}{=}\ C(inputs)\)

- Run \(C\)
backwards, clearing all helper wires of \(C\)

- If all must-be-zero helper wires are zero (and all must-be-one
helper wires are one), flip \(u_{\delta}\), otherwise keep it as
is

- Repeat the above four steps again

Or, in diagram form:

We can walk through its behavior in both the normal case, and each of
the "unusual" cases:

- 
Normal case:

- \(u_{\delta}\) comes in as either 0 or
1.

- If all of the helper wires have their correct values, it gets
flipped in the middle.

- Hence, in one of the two \(S'\) blocks, \(C(inputs)\)
gets xor'd into the output wires, in the other, nothing happens.

- In each \(S'\) block, first \(C(inputs)\)
gets computed, then (in one of the two runs) it gets xor'd into the
output wires, then it gets "un-computed", which sets all wires except
the output wires back to their original values, allowing the middle
block to faithfully check them.

- 
Some helper has an incorrect value:

- \(u_{\delta}\) does not get flipped in
the middle, and so it's either 0 twice or 1 twice

- Hence, \(C(inputs)\) - or rather, the mangled
execution of \(C(inputs)\) with some helper wire(s)
flipped - either never gets xor'd into the output wires, or it gets
xor'd in twice, in which case the copies cancel each other out

- 
Run in reverse:

- 
The full circuit run backwards just does the exact same thing as
running it forwards!

- Each \(S'\) block
is a perfect palindrome

- Each \(T\) block
is not a palindrome in its gate arrangement, but it is designed to
behave the same run forwards and backwards

- The fact that when you run in reverse the second \(T\) block
is run before the \(S'\) doesn't matter, because that
just flips \(u_{\delta}\), which we've
established does not change the final outcome (it just flips which of
the two \(S'\) blocks
fires)

The authors' 2026 work
includes a different approach, called sandwiching. You
can think of sandwiching as a form of hardened Toffoli optimized for the
use case where there is no reversibilization step, and it's directly
obfuscating a random permutation (the most immediate use case is
building public-key encryption).

A random permutation wrapped in a sliced sandwich

Twenty-eight wires in two halves. The top half carries the free
input x, acted on by a random permutation C interleaved with slice
gates, then by an independent random circuit D interleaved with more
slice gates. Between them, fourteen CNOTs copy the top half into the
bottom half, which is the slice register pinned to zero.

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 
x₀
x₁
x₂
x₃
x₄
x₅
x₆
x₇
x₈
x₉
x₁₀
x₁₁
x₁₂
x₁₃
0
0
0
0
0
0
0
0
0
0
0
0
0
0

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 
 

- 
 

- 

 

- 
 

- 
 

- 
 

- 
 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 

 

- 
 

- 
 

- 

 

- 
 

- 
 

- 
 

- 
 C interleaved
with S₁ N: y
⊕= x D
interleaved with S₂

junk

C(x)
Top half: x, the
free input to the random permutation C. Every wire is a real input
— there are
no pinned ancillas. Bottom half: y, the slice register, pinned to
0.
positive
controlnegative
control
active
pin (flip if ≥1 control
holds)
- active
pin (flip if 2 controls hold)

Sandwiching has overhead \(\approx 2x\) instead of \(\approx
4x\) and does not require the extra \(u_{\delta}\) wire - it only does an
\(S'\)-like
step once. It does not need to defend against nonzero ancillas on the
input, because it's intended to operate on random permutations that have
no must-be-zero ancillas. It does defend against nonzero inputs on
the output wires, but for that it uses a simpler trick: a set of
random "slice" gates ensures that if those wires come in nonzero, the
input gets completely mangled. The "compute \(C\) backwards" step is also replaced
with an arbitrary random circuit \(D\).

## Mixing

Mixing is conceptually very easy to understand: it's repeatedly
making transformations to a small part of the circuit at a time. Each
transformation preserves functionality while destroying (or rather, confusing
and diffusing) some amount of visible information about structure.
After many millions of rounds of transformation, each gate in the
original circuit will have undergone mixing steps hundreds of times.

In the current code, mixing is done through a combination of several
techniques, which we will describe in turn.

### Generation mixing

Generation mixing works as follows:

- Make a giant table of all small circuits that have the same
functionality (note: this will inevitably include "small circuits" that
include pairs of sub-blocks that don't interact with each other at
all)

- Repeatedly grab sets of gates from the circuit that are either
contiguous, or don't have any gates in between that interfere with their
functionality

- Check the table what "class" the set of gates you picked is in, and
replace it with a random other small circuit from the same class

- Figure out the range of legal positions that the new sub-circuit is
allowed to be in, before it moves so far that functionality breaks (eg.
an input moves to before the output wire that last updated it). Move
that gate to a random position in that range.

- Repeat

A large amount of the work in the local mixing repo is about
optimizing this procedure: there's a canonicalization step which uses a
few tricks to automatically identify small circuits that are the same
even before the table, then conversion to a polynomial form, and then a
"rainbow table" mechanism to store everything space-efficiently and make
querying fast.

Here is a simplified diagram of how generation mixing works (the
production version takes groups of ~7-10 gates, and the rainbow table is
in the hundreds of gigabytes, though a much smaller "curated table" is
also available):

Rainbow-table replacement of a four-gate window

Five layers: raw four-gate circuits, canonical classes, polynomial
states sorted into buckets, the rainbow-table entries for the matched
bucket, and the spliced replacement. The chosen path is blue; sibling
paths converging on the same class or bucket are bluish grey.

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

· ·
·
331
776 in all

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

·
· ·
12
123 classes in all

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

bucket
0
x0'=1+x0+x1
x1'=x0+x1+x2
x2'=x1+x2+x3

bucket
1
x2'=x0+x1+x2
x3'=x0+x1+x3
x1'=x0+x1+x3

bucket
2
x0'=1+x0+x2+x1x2
x2'=1+x1+x2+x0x1
x3'=x1+x2+x3
x2'=x0+x2+x3

bucket
3
x0'=x0+x2
x0'=x0+x2x3
x3'=x0+x2+x3

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 
·
· ·

key
x0'=1+x0+x2+x1x2 · x2'=1+x1+x2+x0x1

- 

- 

- 

- 

- 

- 

- 

- 

the
window

- 

- 

- 

- 

- 

- 

- 

- 

key
x3'=x1+x2+x3

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

key
x2'=x0+x2+x3

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 
three
of the four gates change, and so does which wires get written
neither
spelling contains a cancelling pair — this is not a reordering

1 · raw
four-gate circuits on up to four wires

2 ·
canonicalise

3 ·
evaluate to the polynomial state, hash, sort into buckets

4 ·
rainbow table — the entries stored for that bucket

5 ·
splice — same functionality, different gates

Generation mixing is the most powerful step in the pipeline. It's
able to change around the ways in which values inside a window are
represented wholesale. This makes it the most effective step for
introducing nonlinearities - getting to a point where any value \(x\) in the
original circuit is represented only by a nonlinear function of the
values in the obfuscated circuit. Generation mixing can also potentially
"glue together" two pieces of the circuit that are far away in the
original computation graph, replacing a sub-circuit that is a
combination of those two pieces with one that interleaves them - and
then further generations of mixing would make the interleaving hard to
detect and reverse.

The pipeline does a huge number of rounds of generation mixing, with
the goal of covering each gate in the circuit many times. It also does
it in multiple phases: one which biases toward expanding the circuit,
and the other which biases toward keeping the size the same, and at the
end eventually shrinking it back down slightly.

## Splitting

Splitting replaces r57 gates with a broader set of one and
two-control gates. There is a bundle of techniques here.

(\(\oplus\) means xor,
\(\lor\)
means or, \(\land\) means and,
\(\neg\)
means not)

First, you can replace \(a\ {\oplus}{=}\ b \lor
\neg c\) with either \(a\
{\oplus}{=}\ b;\ a\ {\oplus}{=}\ \neg b \land \neg c\) or
\(a\
{\oplus}{=}\ \neg c;\ a\ {\oplus}{=}\ b \land c\).

Splitting one r57 gate two ways

A
single r57 gate on three wires at the left, with arrows to its two
equivalent two-gate decompositions above and below right, and a truth
table at the right showing that the two halves of each split fire on
disjoint rows.

- 

- 

- 
a
b
c

- 

a
⊕= b ∨ ¬c
fires
unless b=0, c=1

split
1
a
⊕= b  then  a ⊕= ¬b ∧ ¬c

- 

- 

- 
a
b
c

- 

- 

- 

- 

split
2
a
⊕= ¬c  then  a ⊕= b ∧ c

- 

- 

- 
a
b
c

- 

- 

- 

- 

b
c
r57
split
1
split
2

- 
0
01–
✓✓
–
0
10–
––
–
1
01✓
–✓
–
1
11✓
––
✓
positive
controlnegative
controlflip
if ≥1 control
holds
- flip
if all controls hold

Second, for any wire, you can do the following:

- Pick two positions A and B at which the wire gets modified

- At positions A and B, flip the wire - replace the gate modifying the
wire with a gate that modifies that wire in the exact opposite set of
circumstances

- In between A and B, negate that wire's role in any case where it's
being read in a gate - if it was a positive control, make it a negative
control, and vice versa

A distant join along one wire

The
same eight-wire circuit drawn twice. Above, wire w is written and read
by many gates. Below, two bracket gates targeting w are negated by
flipping both their pin type and all their control polarities, and every
control reading w between them is inverted. Gates that write w inside
the span need no change.
before

- 

- 

- 

- 

- 

- 

- 

- 
0
1
2
w
4
5
6
7

- 

- 
- 

- 
- 

- 

- 

- 
- 

- 
- 

- 

- 

- 
- 

after
negate
the two bracket gates, invert every control that reads w between
them

- 

- 

- 

- 

- 

- 

- 

- 
0
1
2
w
4
5
6
7

- 
- 

- 
- 

- 
- 

- 
- 

- 

- 
- 

- 

- 

- 
- 

- 
- 

bracket
bracket
writes
w — unchanged
positive
controlnegative
control
active
pin (flip if ≥1 control
holds)
- active
pin (flip if 2 controls hold)

Splitting helps to destroy a particular type of visible information
about the meaning of individual wires and gates: after enough
rounds, it would not be practical to tell where some wire represents "x"
and where it represents "not-x".

By broadening the set of gates being used, splitting also creates the
conditions that are necessary to implement the next step, which allows
us to shift around the order of gates with much fewer restrictions.

## The crossing walk

Two gates that do not "collide" with each other, in the sense of one
gate writing a value that the other reads, can be freely reordered. But
two gates that do collide each other can also be reordered - as
long as you add a new gate to compensate for the read and write
switching places.

Here's how this works, split into three cases:

The three crossing rules

Three
panels, each showing a two-gate collision on the left and its exact
three-gate rewrite on the right. R1 splits the mover, R2 splits the
collider, R3 has a more complicated effect.

R1
· the collider writes a control of the mover — the mover splits

- 

- 

- 

- 

- 
x₀
x₁
x₂
x₃
x₄

- 
- 

- 
- 

- 

- 

- 

- 

- 

- 

- 
- 

- 
- 

- 
- 

x₀
⊕= x₁x₄ becomes
x₁x₄
⊕ x₂x₃x₄, since
x₁
→ x₁ ⊕ x₂x₃ 
R2
· the mover writes a control of the collider — the collider
splits

- 

- 

- 

- 

- 
x₀
x₁
x₂
x₃
x₄

- 
- 

- 
- 

- 

- 

- 

- 

- 

- 

- 
- 

- 
- 

- 
- 

x₂
⊕= x₁x₃ becomes
x₁x₃
⊕ x₀x₃x₄, since
x₁
→ x₁ ⊕ x₀x₄ 
R3
· each reads the other's target — the mover transforms and splits

- 

- 

- 

- 

- 
x₀
x₁
x₂
x₃
x₄

- 
- 

- 
- 

- 

- 

- 

- 

- 

- 

- 
- 

- 
- 

- 
- 

x₄=0
· green and orange
are
both no-ops, so purple
is
free to cross
x₄=1
· green does what
purple
used to do, and
purple
is now a no-op 

- 
purple
the moving
fragment  ·  orange
the
collider  ·  green
the piece created by the crossing
positive
controlnegative
control
- active
pin (flip if all controls hold)

In principle, you can move a gate as far as you want, leaving behind
"residues" for each gate that it crosses through.

Notice that this step takes gates with \(k\) controls (the above diagram
shows \(k = 2\),
but \(k \ge 3\)
is also supported) and outputs gates with up to \(2k-1\)
controls.

This is not a serious problem for the crossing walk itself. It just
means that after many rounds of it, you might get gates with many
controls. Additionally, at higher control counts, multiple "residue"
gates may need to be created per crossing.

However, it is a problem if we decide to do crossing walks
during generation mixing, rather than just after it as is the
case now, because the current rainbow table only contains r57 gates. One
could make a rainbow table that contains higher-control-count
gates, but this risks exponentially increasing the rainbow table in size
for the same level of coverage. The easiest solution would be to reduce
each 3+ control gate back into a series of two-control gates.

## fcompress

This step simplifies down a series of gates that modify a wire before
it gets read.

This is primarily done not to do more hiding, but to shrink the
program. The argument is that if we did not do this, the attacker could
do it themselves anyway to have a smaller object to work with, so we
might as well give the same efficiency gain to legitimate users.

Here are some of the simplifications:

And that's it for mixing!

One final thing worth mentioning here is gadgetization
swaps. The gadgetization phase, which we will talk about later,
includes a "role swapping" mechanism where two wires get their values
and their roles swapped at some position in the circuit. The swaps that
affect the output wires are undone at the end in a single step that
extracts the right output wire to the right position. Even though it's
done during the gadgetization phase, I still think of it as being a type
of mixing. It allows wires to move "vertically", complementing the
"horizontal" movement done by the crossing walk phase.

You can think of the different families of mixing as making
"sudoku-like" transformations on the circuit that nicely complement each
other:

The four families of mixing on one grid

A
single nine by nine grid with time along the horizontal axis and wires
down the vertical. A full column, a three by three window, a full row
and a single cell are shaded to show the region each family of moves can
reach. 

time
→
wires
↓

- 

- 

- 

- 

- 

- 

- 

- 

splitting
rewrite
wire values in-place 

gadgetization
swaps
values
move across wires 

generation
mixing
fully
replace a small window 

crossing
walk · fcompress
gates
move across time 

## Gadgetization: why do we need
it?

To understand the need for this next phase, we should ask the
question: what are some data leakages that inserting junk gates,
shuffling and mixing are either bad at addressing, or fundamentally
cannot address at all?

Here's one simple answer (it's not strictly correct, but for
the moment, assume it is): each "wire" in \(C\), at each point in time,
is still instantiated in the obfuscated circuit \(Obf(C)\)
somewhere.

If an attacker has the original circuit \(C\) and the obfuscated circuit \(Obf(C)\),
they can run the original circuit many times, see which wires in the
obfuscated circuit are perfectly correlated with wires in the original
circuit, and use that to determine the mapping from one to the
other.

Of course, in real-world applications, the attacker does not have
access to \(C\). But in
many real-world applications, they almost do. Almost all of
\(C\) is
public, the only thing secret is some "embedded secret key" that \(Obf(C)\) is
trying to hide. Even if the attacker has no access to \(C\) at all,
they can do something like this:

- The attacker starts off knowing which input wires to \(Obf(C)\)
correspond to which input wires to \(C\)

- Suppose you have an oracle that, given a gate in \(C\), finds
which gate(s) and wire(s) in \(Obf(C)\) correspond to it (eg. this
might be the correlation-based detector we described above)

- Enumerate all possible wires that we already know about, and all
possible options for the next gate in the circuit. For each
option, run the oracle. If it successfully finds the feature in \(Obf(C)\)
that maps to that gate, then the gate must exist in \(C\)

- Keep going, using this attack to expose more gates further and
further down \(C\), until you've exposed the whole
thing

Adding junk gates does not affect this at all. Shuffling the gates
does not affect this at all.

Mixing can affect this, in principle. For example, imagine
you have a sub-circuit that does:

\(x\
{\oplus}{=}\ a \land b\)

You could replace that with:

\(x \
{\oplus}{=}\ y \oplus z \\ y\ {\oplus}{=}\ a \lor b \\ z\ {\oplus}{=}\ a
\oplus b \\ x \ {\oplus}{=}\ y \oplus z \\ y\ {\oplus}{=}\ a \lor b \\
z\ {\oplus}{=}\ a \oplus b\)

The behavior is exactly the same: \(x\) gets flipped only if \(a\) and
\(b\) are
both 1. But in the replacement sub-circuit, the expression \(a \land b\)
never gets instantiated.

What is going on is:

- \(a \land
b\) gets replaced with \((a \lor b) \oplus (a
\oplus b)\) (this is an algebraic identity)

- \(a \lor b\)
and \(a
\oplus b\) get applied separately, through \(y\) and
\(z\) (wires
that are borrowed and then put back in their place), so even these two
components of \(a \land
b\) are a few steps removed from each other.

In principle, this kind of transformation can be done by local
mixing. Even more complex transformations can be done by local mixing.
In principle, you could mix enough times that something like this just
ends up happening to every wire many times over by random chance.

That was the authors' hope. But, so far, mixing has not
proved to be good enough. There ended up being too many correlations
between values in \(C\) and values in the obfuscation
that remained. The authors visualize these correlations through
heatmaps:

Gadgetization emerges as a way to more deterministically make sure
that these kinds of correlations do not exist, even before any mixing
starts. We take the problem "each wire in \(C\) must never be explicitly
instantiated", and we explicitly solve for it.

## Gadgetization: how does it
work?

We replace each gate in the circuit with a "gadgetized gate". For
example, here is the simplest possible gadgetization of an r57 gate:

In this design, we represent each wire \(w_i\) as two wires, \(s_i\) and
\(r_i\), that
satisfy \(w_i =
s_i \oplus r_i\). The construction in the above diagram
allows us to replicate the desired behavior over
representations - flipping the representation of \(w_a\) only
if either \(w_b =
1\) or \(w_c =
0\) - without ever explicitly instantiating \(w_a\),
\(w_b\) or
\(w_c\).

The construction here borrows ideas from multi-party computation,
where the goal is identical: the participants start with a
secret-sharing of the inputs and get to a secret-sharing of the outputs,
without ever exposing any value in the computation (input, output or
intermediate) to any single machine. The construction here is the
simplest two-party case. Another source of inspiration is the secure
hardware literature, eg. this
work. In secure hardware design, a common model is the d-probing
model: assume the adversary can read up to \(d\) wires,
and mathematically guarantee that under this constraint they can learn
nothing.

If we implement this kind of gadget, then we are guaranteed to get no
single wire in the gadgetized output representing any specific wire of
\(C\) -
unless we get really unlucky and the mixing step undoes a
gadgetization by sheer blind luck, which is currently very rare and
mixing can be optimized to protect against further.

Now let's look at the full pipeline that makes gadgetization
possible.

The linear gadgetizer with every phase boxed and swaps expanded

Ten
wires in two halves. The junk fill and refill each sweep the auxiliary
half repeatedly, hitting several wires more than once. Every carrier is
masked and unmasked. The gadgetized section holds one gadgetized r57 and
one wire swap; the route section holds another swap. A bold orange line
follows value two's carrier as it moves to the band half and
back.

junk
fill
mask
gadgetized
gates
unmask
route
refill

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 
x₁
x₂
x₃
x₄
x₅
⋮
z₁
z₂
z₃
z₄
z₅
⋮

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

⋯
⋯
⋯
⋯
⋯
⋯
⋯
⋯
⋯
gadgetized
r57
swap
swap

out

junk
Bold
orange tracks value 2's carrier: the swap moves it to z₄, the route
brings it back.
Each
gadgetized r57 is six r57 gates on six wires (three pairs);
Each
swap is six r57 gates on three wires (in, out, helper).
positive
controlnegative
controlactive
pin (flip if ≥1 control
holds)⋯
omitted gates

(Note: to simplify exposition, this description is mixing the
secret-share gadget, which is from an older design, with a gadgetization
pipeline that is as-of-today current)

The gadgetized gates that we discussed above go into the third phase,
and they get interspersed with the swaps we mentioned
earlier, which switch the role of two wires. The remaining phases are
there to provide the scaffolding the makes the whole pipeline
correct:

- The junk fill phase covers the newly added wires
(\(z_1 ... z_5\)
in the diagram) with junk, which is a high-degree function of the
inputs. The high-degreeness is accomplished because the controls of each
gate can come from either the \(x\) portion or the \(z\)
portion, so the degree of each \(z\) wire keeps going up as it
incorporates both \(x\)'s and other \(z\)'s

- The mask phase replaces \((value,
junk)\) with \((value \oplus junk,
junk)\). This brings the inputs into the correct form
needed for the gadgetized gates. Once the mask phase is complete, there
is no single wire in the gadgetized circuit that directly represents a
wire in \(C\) - that
responsibility is now shared between the two wires whose xor
together equals the wire in \(C\).

- The gadgetized gates phase, as described above,
contains a gadgetized gate for each of the actual gates from the
reversibilized-and-hardened circuit, plus extra swaps thrown in

- The unmask phase brings \((value
\oplus junk, junk)\) back to \((value, junk)\) so we can read off
the outputs

- The route phase moves the outputs back to the
positions that they are supposed to be at. You can think of it as
"undoing all the swaps", though we only care about the wires
representing outputs to \(C\).

- The refill phase adds more junk to all the junk
wires. This is an extra precaution to make it harder for an adversary to
see what the junk values are, making it harder to invert the
masking.

Now, we have removed any direct one-to-one correspondences between
wires in \(G\) (the
gadgetized output) and wires in the original \(C\). We
have even removed correlation: \(a \oplus b\) has zero correlation
with \(a\) and
with \(b\) - at
least, as long as \(a\) and \(b\) are themselves independent with
each other, which is approximately true with a high-quality junk-filling
phase.

But there is still a major type of attack that remains.

## Linear algebra attacks

We still have one type of relationship between the pre-gadgetized
circuit \(C\) and the
gadgetized circuit \(G\) that is discoverable: a
linear (or more precisely, affine) relationship. Each
wire \(w_i\) in
\(C\), at
some specific position in execution, corresponds to some \(g_j \oplus
g_k\) in \(G\). And you can discover all such
relationships, even if we expanded the gadgetization so there are eg.
ten masks going into the xor, by using linear algebra
attacks.

Here is how a linear algebra attack works. Consider \(c_{\{i,w\}}\), wire \(w\) in the
state of \(C\) after
executing the first \(i\) gates. Then take \(g_j\), the
state of \(G\) after
executing the first \(j\) gates. The goal will be to find
linear relationships between \(c_{\{i,w\}}\) and \(g_j\)
(mathematically, these are both vectors over \(F_2\)).

Do many executions of \(C\) and \(G\), so you have a vector of \(c_{\{i,w\}}\) values and a matrix of
\(G\) states,
\(G_j\).
Append an extra column of all-ones to \(G_j\) to let us find dependencies
that are offset-by-a-constant. Then, use Gaussian elimination (or, at
very high dimension, slightly more efficient algorithms based on faster
matmul eg. Strassen) to
solve the system of linear equations:

\(G_j * v
= c_{\{i,w\}}\)

Either this system has no solutions, or it has a solution. If it has
a solution, then take even more executions of \(C\) and
\(G\), and
see for how many of these new executions it correctly predicts \(c_{\{w,i\}}\). If the number is very
close to 0.5, then you've probably identified a spurious correlation, an
accident. If the number is significantly above 0.5, then you've
discovered at least a partially effective predictor of \(c_{\{w,i\}}\). For clear linear
relationships like the two-value (or any multi-value) xor, it will
return a correlation of 1.

This attack takes far longer than more naive attacks: Gaussian
elimination is \(O(N^3)\), and Strassen-based
approaches are \(O(N^{2.8})\) whereas finding perfect
correlations between activations can be \(O(N*log(N))\) or even faster. But
that's still not good enough.

And so the solution is to make the gadget represent \(w_i\)
nonlinearly.

## Nonlinear gadgetization

Instead of storing wires as \((s_i, r_i)\) satisfying \(w_i =
s_i \oplus r_i\), we store them with a "carrier" wire
\(c_i\)
satisfying \(w_i =
c_i \oplus B_{i1} \oplus B_{i2} \oplus ...\), where each
"band product" \(B_{ij}\) is itself a product of some
pseudorandomly generated "band values". Instead of the mask being
linear, the mask is highly nonlinear.

When the value of a wire changes, it's always the carrier that
changes: an xor to the carrier xors the underlying value. To apply a
gate \(w_k\ {\oplus}{=}\ w_i
\land w_j\), the goal is to apply a series of xors to the
carrier of the output wire, which sum up to \(w_i
\land w_j = c_i \land c_j \oplus c_i \land M_j \oplus M_i \land c_j
\oplus M_i \land M_j\), where \(M_i\) and \(M_j\) are
the two band products. However, we want to do this without ever
instantiating this product or even any of its four cross-terms. The
solution is a mechanism called Gray folding:

How the Gray fold cancellation works

A square whose four corners are the four accumulator states. Each
corner shows the expansion of u times z at that state. Terms appearing
an even number of times across the four corners are shown in matching
muted colours; the single surviving term P times Q is circled in the
bottom-right corner.

 Two dirty
wires u, z
hold unknown u₀,
z₀. Goal:
add P·Q to the
target, never
forming P or
Q alone.
START HERE

u₀
· z₀
=
u₀z₀

(u₀⊕P)
· z₀
=
u₀z₀
⊕
Pz₀

(u₀⊕P)
· (z₀⊕Q)
=
u₀z₀
⊕
Pz₀
⊕
u₀Q
⊕
PQ

Only value
that does
not cancel
out across
the four
steps

u₀
· (z₀⊕Q)
=
u₀z₀
⊕
u₀Q

- 

- 

- 

- 
gather
P gather
Q
strip
P
strip
Q

- 

- 

- 

- 
XOR
u·z into
target
at each step

Gray folding is very flexible: it can be naturally extended to cover
higher-degree monomials or expressions where different terms have a
mixture of different degrees.

Here is one single gadget that uses this mechanism:

This gadget is now much more complex than the secret-sharing gadget
we saw before. It accomplishes the goal of immunity to exact linear
attacks on rows of G, which you can see by comparing heatmaps (this
time, heatmaps that check for linear attacks, and not just
value-to-value correlations):

Left: secretshare14 gadget
(the secret share above plus some re-mixing), right:
bandproduct92 (the 92-gate
nonlinear-band-product gadget)

But as it turns out, even this approach is not perfect: it's still
vulnerable to exact linear attacks on the whole trace of G.

The reason is fundamental: the series of xors applied to the carrier
has to ultimately sum up to the actual output value of the gate, and no
matter how much you try to put shuffles or other things into those xors,
you can solve a system of linear equations to find the exact set of
wires that sum up to the output value.

Here are the heatmaps against the trace of G:

Could you remove this vulnerability too? As it turns out, yes, but
you have to do some extreme trickery: the value \(w_i\) has
to be stored in multiple carriers in a nonlinear way. One winning
equation is \(w_i =
c_1(i) \land c_2(i) \oplus c_1(i) \land c_3(i) \oplus c_2(i) \land
c_3(i) \oplus c_4(i) \oplus c_5(i)\).

The evaluation of a gate also has to be done in a way that avoids
ever instantiating values any subset of which sum up to \(w_i\).
Instead, we take the whole expression \(C_{\{c,out\}} = encode(gate(decode(C_a),
decode(C_b), decode(C_{\{c,in\}})))\) (here each \(C\) stands
in for five values), break it up into monomials, and then do
Gray-coding-like tricks to apply each monomial to its target.

Here is one implementation, which I call
nonlinear291. It uses 291 gates per gadget representing
a single underlying gate.

It is fully immune to:

- Any exact linear attacks between \(C\) and the rows or trace
of \(G\)

- Any correlations between \(C\) and individual values, or
weight-2 expressions (xor, or, and, a-and-not-b) in the rows or trace of
\(G\)

The simplest relationship between \(C\) and \(G\) that it does have is a
0.5 correlation between a wire value in \(C\) and an expression of
three values in \(G\).

If you want to go full crazy, you can go even further, by stacking
these constructions on top of each other. Here is a secretshare14
gadget, with each individual gate replaced by a full
nonlinear291. I call this monster
behemoth1415:

It's not feasible to exhaustively check this, but there is a
reasonable argument to believe that it does not have any correlations
against weight <= 5 expressions.

Well, okay, if you want to really go full crazy, you can
make a nonlinear291 with each individual gate replaced by a nonlinear
291 (some gates have one control so they might be simpler).

This would have a blowup of about eighty thousand gates in \(G\) per
gate in \(C\) - a
ratio that sounds monstrous, until you remember that garbled
circuits replace each gate with a computation including a hash,
which is also around tens of thousands of gates, and fully homomorphic
encryption can have a blowup in the billions or trillions.

What does "behemoth80000" get you? There's good reason to conjecture
that it has no correlations against weight <= 8 expressions, and no
exact match to linear or degree <= 3 expressions in \(G\). If
\(G\) is
large enough (eg. a gigabyte, or even megabytes), this already gets you
to the point where the best known algorithms for finding matches to
\(C\)
(whether a linear attack on the fourth tensor power of \(G\), or
exhaustive search, or learning
parity with noise algorithms, or "junta
learning") all take cryptographically long amounts of time.

However, before we get too excited about behemoth gadget
constructions, it's important to keep in mind two facts:

- 
Gadgetization alone buys you no security against attackers that
just pattern-match: they know what kind of gadget corresponds to which
underlying gate. So you have to do serious mixing after gadgetization
anyway.

- 
The authors of the local mixing proposal are convinced that if
they keep improving mixing, then mixing itself should be able to remove
exact linear attacks and small-weight correlations. They believe that
theoretically, with a good enough mixing pipeline, no gadgetization step
should be needed at all.

The main weakness of mixing so far is that it is stochastic, and so
empirically it often leaves many correlations and linear attacks not
sufficiently removed. The rainbow-table-based generation mixing, even
with canonicalization and a heavily curated table, is currently only
able to reorder very small portions of the circuit at a time.

So it feels like gadgetization and mixing have complementary
roles:

- Gadgetization can achieve some nonlinearity and
minimum-correlation-weight properties in a way that is guaranteed for
each gate, but it's fundamentally dependent on a strong mixing step to
force the attacker to search for the correlations and higher-degree
expressions that inevitably remain by looking over all of \(G\), and
not a small subset where everything related to each gate is clumped
together

- Mixing can destroy structural leakage very well, but it's
less robust at destroying algebraic leakage

That said, there is also quite a bit of overlap in their potential
roles, and so a better version of one takes some pressure off the other.
This is one of the major axes of uncertainty in the project: exactly how
much of the task is done by gadgets, and how much by mixing?

## What
low-level security properties are we going after?

The goal is to ensure a lack of detectable relationships between
executions of the obfuscated circuit and executions of the original
circuit. Let's re-summarize the specific attacks:

Relation
Attacker
Complexity

Exact linear matches of any weight
Gaussian elimination or more advanced matrix inversion
\(O(|Obf(C)|)^{\approx 2.8}\)

Exact degree-k matches of any weight
Gaussian elimination or more advanced matrix inversion on k'th
tensor power of \(Obf(C)\)
\(O(|Obf(C)|)^{\approx 2.8}\)

Correlations with weight-k linear functions
Sparse learning parity with noise (LPN); MOS
algorithm
\(O(|Obf(C)|)^{\approx 0.7k}\)

Correlations with weight-k nonlinear functions
Exhaustive search, junta learning; MOS
algorithm
\(O(|Obf(C)|)^{\approx 0.7k}\)

Theoretically optimal matrix multiplication algorithms are
at \(O(N^{\approx 2.37})\), but even
at the very large sizes we're working at, anything more
asymptotically-efficient than Strassen
is not efficient in practice.

This once again shows the natural complementarity between
gadgetization and mixing. An effective task for gadgetization is to
convert circuits into representations that avoid all of these attackers.
An effective task for mixing, in addition to doing even more smudging
stochastically, is to force attackers attempting any of the above
attacks to actually search through all of \(Obf(C)\) and not just an
identifiable subset of it to target each individual gate.

One interesting fact to notice here is that we are naturally in a
"big key cryptography" regime. With "normal" cryptography, each
individual cryptographic object stands by itself: to attack an FHE
ciphertext, you can attack any individual value at any point in the
execution of a circuit. Here, each gate in the circuit is part of
the noise protecting every other gate.

If we are really conservative on parameters - say, the
obfuscated circuit's trace is a terabyte (\(2^{43}\) bits) in size (which should
take a few minutes to run on consumer hardware) - then even a linear
attack is not fatal. A Gaussian elimination requires \(2^{129}\)
steps, at best optimizable to perhaps \(2^{\approx 122}\) with Strassen,
which is within bounds of what is considered cryptographically secure
(not to mention that you would need \(\approx 10^{25}\) bytes to store the
matrix)! If we are okay with degree-2 attackers, then (assuming perfect
mixing), megabyte-sized obfuscated circuits become sufficient - though
in practice, we will want lots of headroom to account for imperfections
in mixing.

## Random bit flip attacks

There is one other attack worth worrying about: random bit
flip attacks. Here, the goal is not to learn anything about the
circuit directly. Instead, it's to randomly flip the evaluations of
wires inside of the circuit during an execution, without knowing what
you're flipping, with the goal of extracting outputs that you would
otherwise not be able to extract.

Here is one example. Consider a program \(P(C, \pi)\) that takes two inputs:
an FHE ciphertext \(C\), and a STARK \(\pi\).

- If \(\pi\) is a
valid proof that \(C\) was the result of executing some
"correct" circuit, it decrypts the output with an embedded FHE
decryption key

- If it is not, it just returns zero or pseudorandom noise

This is the classic "obfuscation bootstrapping" program: given an
obfuscation that can handle the single specific task of "verify a STARK
and decrypt FHE", it lets you obfuscate arbitrarily complex circuits,
with FHE * STARK overhead - still very high, but within reach of
viability.

Now, suppose you have a local mixing obfuscation that uses the
mechanisms described above, including very strong gadgetization and good
mixing. It's still vulnerable to the following attack.

An attacker puts in:

- A \(C\)
produced using the wrong circuit - perhaps a circuit that just
outputs some embedded secret key in the FHE-encrypted program

- A fake and invalid proof \(\pi\)

They then run the obfuscated \(Obf(P)\) many times. During each
execution, they keep randomly flipping a bit some time during the
execution.

Even though there is no observable relationship between \(Obf(P)\)
and \(P\), there
is still the fact that on average, flipping a bit in the execution of
\(Obf(P)\)
has a \(\ge
50\%\) chance of flipping one bit in \(P\). The
attacker's goal: just keep doing this until the bit they flip is the
"was the STARK correct?" bit. After a number of tries roughly equal to
the size of the circuit, they succeed, and out pops the secret key.

There are actually many possible bit flips in the circuit that would
help the attacker. For example, if there is some bit that flips the FHE
noise to zero or otherwise turns off the rounding during decryption,
they could learn an exact relation \(s * C\), and out of that recover the
embedded secret \(s\). For this reason, it's worth
addressing this systematically.

What we've seen so far seems to suggest two ways to solve this
problem: at mixing layer and at gadgetization
layer:

- Mixing layer solution: make sure that each wire is
being used regularly as an ancilla (a "helper wire") for many other
gadgets. The classic ancilla use is some version of: read \(x\), apply
\(x\
{\oplus}{=}\ y\), read \(x\) again, then un-apply \(x\ {\oplus}{=}\
y\). If you flip \(x\) in between the two reads, you
are breaking the ancilla's functionality. If each wire is simultaneously
an ancilla for many other gadgets at the same time, then flipping it at
any point will correspond to many flips in the gadgetized circuit.
Ideally, there would be an avalanche of cascading pseudo-random flips to
much of the remaining execution.

- Gadgetization layer solution: instead of all
representations of each gadgetized gate representing either 0 or 1,
adjust the gadgetization so that most representations are "junk", and
only a few represent 0 or 1. It should take at least a few bit flips to
go from a representation of 0 to a representation of 1. This would be
yet another expansion to the gadgetization, of similar complexity to the
shift from secret-share to nonlinear. Tamper-resilient circuit
literature contains
ideas on how concretely to do this. You would then rely on mixing
and \(Obf(C)\)
being big to make it infeasible for an attacker to find the combination
of bit flips that corresponds to one single gadget. You can add further
security against potential copy-paste attacks by making the
valid encodings depend on band values derived from the input.

In the next section, we will also see a third line of
defense, at a layer wrapping the obfuscation scheme we have built so
far.

## Getting
to (sort of) provable indistinguishability obfuscation

All of this work is early stage and unproven, and the local mixing
authors acknowledge this. And so right now, they are focusing on using
the above pipeline for one specific narrow use case: obfuscating
random circuits. There are two already-known concrete uses for
this.

First of all, obfuscation for random circuits immediately
implies public key encryption (assuming the obfuscation scheme
meets the RIO and SCP properties, which we will describe later).
Generate a reversible random circuit \(R\), with width \(2w\). Keep
\(R\) for
yourself, and publish \(Obf(R)\) (the obfuscation should use
sandwiching, so it can only be used to compute \(R\)
forwards and not backwards). Anyone can encrypt a width \(w\) message
\(m\) by
generating randomness \(r\) and computing \(c = Obf(R)(m,
r)\). Because \(R\) itself is reversible, given such
a \(c\) you can
decrypt it via \(R^{-1}(c )[{:}w]\).

The reason to add a random pad when encrypting (and trim the pad
after decrypting) is to avoid situations where an attacker can decrypt
encrypted messages by encrypting all possible options and seeing which
one matches.

This alone is very valuable: it gives us a totally different
family of plausibly quantum-resistant public-key encryption
algorithms. In an era when quantum computers are about to take
away RSA and elliptic curves, and there are serious (though so far
unsuccessful) attempts at even attacking lattices, having a new and
totally-different form of cryptography to fall back on is a valuable
insurance policy.

Because this style of public-key encryption only uses classical
symmetric-cryptography-style operations during decryption, it has
extremely impressive performance properties:

- Ciphertexts can be 48 bytes, compared to over a thousand for almost
anything else plausibly quantum-resistant

- Very fast to decrypt; slower than AES and the like because it's a
random permutation that does not benefit from vectorization or hardware
acceleration, but faster than anything else plausibly
quantum-resistant

- Though with the cost that public keys are many megabytes in
size.

But the authors also have a second use case in mind: they
have found a way to (sort of) provably construct indistinguishability
obfuscation (iO) of arbitrary circuits from obfuscation of random
circuits.

Here is (one version of) the technique:

- 
Walk through the whole circuit from left to right

- 
For each gate \(g\) in the circuit:

- Generate a random circuit \(R\)

- Make two obfuscations of \(R\), \(Obf_1(R)\) and \(Obf_2(R)\)

- Reverse \(R\). \(Obf_1(R)\ |\
Obf_2(R)^{-1}\) is an obfuscated identity

- Rotate this obfuscated identity (ie. move the first \(k\) gates
to the end) so that the first gate's control function (eg. or, xor,
a-and-not-b) is the same as in \(g\)

- Swap the indices in it so that the wires read and written by the
first gate are the same as the indices written by \(g\)

- Remove \(g\) from
the start. Call the result \(\Gamma\). This whole set of gates
has the same functionality as \(g\)

- Swap \(g\) in
place (in the circuit) with \(\Gamma\)

- Take the last few gates in the circuit before that point (this will
be the tail of the previous round's \(\Gamma\)),
and the first few gates of \(\Gamma\). Swap that bundle in-place
with an obfuscation of itself.

In diagram form:

The authors have a proof that this achieves the formal definition of
iO: if two reversible circuits \(A\) and \(B\) have the same behavior on all
inputs, given \(Obf(A)\) and \(Obf(B)\)
you should not be able to tell which is which. To extend this to
irreversible circuits, one need only convert the irreversible
to reversible using the hardened Toffoli construction, which does the
conversion in a way that structurally guarantees that it introduces no
new data leakage.

Their proof depends on two assumptions:

- RIO ("random input and output obfuscation")
for random circuits. RIO is a significantly weaker
property than regular iO: it only requires obfuscation for random
circuits, and the distinguisher that it is defending against is assumed
to not have access to the plaintext program.

- The "Split Circuit Pseudorandomness" conjecture:
roughly, you cannot tell the difference between \(Obf(C_1\ |\ R)\ |\
Obf(R^{-1}\ |\ C_2)\) and \(Obf(C_1\ |\ C_2)\). This assumption
lets us attach together separate obfuscated circuits.

Here, the methodology becomes more recognizably similar to the other
strands of obfuscation research: there is a core assumption that they
attempt to minimize, and then a complex and high-overhead protocol built
on top to make the whole thing "provable".

The main difference from most other cryptography is that here, they
are not reducing to well-understood assumptions many people have worked
with, rather they are simultaneously designing a new protocol and a new
assumption that it's based on. It's still worthwhile, because the new
assumption is considerably "smaller" and easier to analyze than just
saying "we assert this whole protocol is secure", but this is a downside
inherent to doing pioneering work with a wholly new family of
constructions.

More heuristically, notice that this pipeline opens up a
third avenue of defense to random bit flip
attacks: any bit you flip will be somewhere in the middle of an
obfuscation, and so it will likely propagate into a lot of junk.

The last step in the above pipeline, replacing \(head\ |\
tail\) with an obfuscation of itself, ends up essential
here: if that step were not there, then if your bit flip lands right
after the last gate of a \(\Gamma\), you would actually have an
effect equivalent to flipping a gate in \(C\). But with that step in there,
any bit flip you make ends up deep inside of a sub-obfuscation.
The same machinery that was constructed to protect against distingushing
attacks to ensure the iO property also protects against bit flip
attacks.

## What
"cryptography tradition" is local mixing even in?

Compared to basically all cryptography that I've written about so
far, the epistemology of why local mixing obfuscation might be secure is
completely alien.

In most cryptography, you try to create mathematical proofs that
reduce the security of a protocol to a well-understood math problem -
"if you can break this encryption algorithm, then you can factor a
semiprime \(N\) into
its two factors \(p*q\)".

The design here is not like that at all. There is an outer wrapping
layer that sort of does this at the end, but at every layer below that
it's much more heuristic, combining together a grab bag of ideas that we
think hide structure, together with some mathematical reasoning about
specific properties that we care about avoiding.

The only other tradition in cryptography that is like this is
symmetric cryptography, which is behind symmetric encryption
algorithms and hash functions. The closest second is secure hardware
design, which adopts very similar principles, though it tends to
focus on linear attacks less because, well, you can't multiply a
physical circuit by a matrix the same way you can a virtual one.

Symmetric cryptography has developed a grab bag of tricks to use, and
attacks to watch out for. For example:

- Confusion
and diffusion as properties to target

- Substitution-permutation
networks, and more generally the idea of interleaving global linear
functions that destroy locality and local nonlinear functions that
destroy linearity

- Doing all internal work using reversible steps, and then only
applying irreversibility at the end

- Making sure the function is high degree

- Linear
cryptanalysis: analyzing complex functions by looking for exact
matches or correlations to linear functions

- Differential
cryptanalysis: analyzing complex functions by looking for changes to
the output that are more likely to arise from specific changes to the
input: where \(f(x) \oplus f(x \oplus
e)\) , for some fixed \(e\) but varying \(x\), takes
on some specific value \(g\) more often than would be
expected by random chance

But despite having what might be viewed as a lower level of rigor,
many cryptographers think that hash-based cryptography is the one type
of cryptography that will survive if all other cryptography gets
destroyed by advances in mathematics.

The high-level reason why is: hashes have no
structure, they're intentional chaos. It's much easier
to believe that something intended to have no structure will continue to
have no structure, than to believe that something intended to have one
or two types of structure will not have some other form of
structure discovered later that enables attacks.

The way that the authors of local mixing see it, they are trying to
make that tradition work: to obfuscate circuits through a
series of steps that destroy all structure, except by being
functionality-preserving.

But there is also a different way to see the primitive being
constructed here, which actually views it as an attempt to
introduce a new member to the "pantheon" of cryptographic
gadgets that we use as building blocks, along with structures
like lattices and elliptic curves. Roughly, you can see the
correspondence like this:

Object
Where it's hiding plaintext
How you compute on it

Elliptic curves
Discrete log wrt a standardized point \(G\): \(P = G * k\) hides \(k\)
Linear homomorphism of elliptic curve addition: if \(P = Gk\)
and \(Q = Gj\),
then \(R = P +
Q\) hides \(G * (j+k)\)

RSA
k'th root modulo \(N =
pq\)
Homomorphism on multiplication: encryption is \(x \rightarrow
x^k\) mod \(N\), so \(enc(a) * enc(b) = a^k *
b^k = (ab)^k\) mod \(N\)

Lattices
Approximate linear equations: \(C * s + e = m\)
Approximate linear equations preserve ring properties (up to error
bound), eg. in GSW if \(C_1\) maps \(s\) to
\(\approx
m_1 * s\) and \(C_2\) maps \(s\) to
\(\approx
m_2 * s\) then \(C_1 *
G^{-1}(C_2)\) maps \(s\) to \(\approx m_1 * m_2 *
s\), same for addition

Local mixing gadgetization
Low-degree low-weight (but not too low degree or weight)
polynomial functions of \(G\)
Walk a "path" going from \(P_1(x)\), \(P_2(y)\),\(P_3(z)\) to
\(P_3(Gate(x,y,z))\) that avoids
coming anywhere close to explicitly instantiating \(x\), \(y\) or
\(z\)

To me, this is the most impressive aspect of this whole project. This
is not just a construction aimed at achieving a specific goal. This is a
serious attempt at actually inventing a new base cryptographic primitive
- and, conveniently, one whose most "natural" functionality is exactly
the functionality that we do not yet have: obfuscation.

But this ambition is also the reason why it's appropriate to make a
warning. Typically, it takes decades for new cryptographic
primitives to mature. There is a whole pipeline that needs to happen, of
searching for and ruling out fatal attacks that would kill the whole
program, searching for non-fatal but still serious attacks, learning the
tricks that get around those attacks, and refining everything to the
point where it stabilizes.

This is also why the authors are focusing short-term on a less
ambitious target: obfuscation of random circuits. Fortunately, as we've
seen, even obfuscation of random circuits is very meaningful: if you can
achieve it, then you have a new form of public key cryptography, and you
even get general-purpose obfuscation, though possibly with higher
overhead than necessary (each gate in \(C\) gets replaced with a full
obfuscated circuit, so we're back to terabytes).

One major hope here is that with AI-accelerated research, we
can greatly accelerate this whole pipeline. Speed-running the
cryptanalysis and verification that would before take decades could be
done within a few years, so inventing new cryptographic building blocks
might become a much more viable idea in general.

Obfuscation is the final frontier of cryptography: any other
primitive can be built from obfuscation (plus one-way functions), and
there are many protocols that are most naturally expressed as obfuscated
circuits. Local mixing is potentially not only much more efficient than
lattice-based obfuscation (even diamond iO), but it even has a route to
be competitive in runtime with FHE protocols. Additionally, because it
doesn't build on a tower of already-known building blocks, and instead
is a much more "start-from-fundamentals" project, it is much easier for
cryptographers without decades of experience to come in and contribute.
So I am very excited that this totally different, new and unproven and
somewhat alien thread of cryptographic research is happening.

## HN Discussion

HN front page 2026-08-21/22: "Code Obfuscation via Local Mixing" — 34 points, 17 comments (objectID 49389339).
