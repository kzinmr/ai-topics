---
title: "Assumptions weaken properties"
url: "https://buttondown.com/hillelwayne/archive/assumptions-weaken-properties/"
fetched_at: 2026-05-21T07:01:28.996763+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# Assumptions weaken properties

Source: https://buttondown.com/hillelwayne/archive/assumptions-weaken-properties/

In
some tests are stronger than others
, I defined
STRONG => WEAK
to mean "any system passing test STRONG is also guaranteed to pass WEAK". This uses the logical implication operator, defined as
P => Q = !P || (P && Q)
.
Implication may be the most overworked operator in logic. Among other things, it's also used in formal specification, where
Spec => Prop
means "any system satisfying
Spec
has property
Prop
" and
ASSUME => Spec
means "The assumption
ASSUME
must hold in order for the system to satisfy
Spec
."
Now let's mush these all together and do some math. To start, "the system has property
Prop
" is the same as "the system passes the test that checks
Prop
", so test strength is also property strength. Now let "
ASSUME => Prop
" mean "the system passes
Prop
assuming
ASSUME
is true." In classic logic, if
P
is true, then obviously
!Q || P
is true. Further, that is equivalent (just draw the truth table!) to
!Q || (P && Q)
. So for
any
propositions
P
and
Q
,
P => (Q => P)
.
In other words,
Prop => (ASSUME => Prop)
. In other other words, "the system passes
Prop
" is a stronger property than "the system passes
Prop
whenever our assumptions hold."
In other other other words, any assumption added makes a property weaker.
This makes intuitive sense to me. A JSON parser that's only been verified with ASCII strings has the property "input only uses ASCII && is valid json => correctly parsed". A better JSON parser that works for all Unicode will have the property "is valid json => correctly parsed", which has fewer assumptions, meaning it's guaranteed to work in a strict superset of cases.
It also matches the intuition that "more assumptions means more likely to go wrong". We have a bug whenever
Prop
is false. The only way for
Spec => Prop
to be true and
Prop
be false is if
Spec
is false, eg our system doesn't satisfy the specification we intended to implement. On the other hand,
Spec => (ASSUME => Prop) && !Prop
is true whenever
Spec
and/or
ASSUME
is false, meaning a correctly-implemented system could still show a bug if a runtime assumption is false.
...Looking back the last two paragraphs have a lot of conceptual leaps. Does that all make sense to you? It all feels natural to me but that might just be my familiarity with the topic talking.
Regardless, a couple more notes on assumptions:
Why we have assumptions
Why not just build our systems to satisfy
ASSUME => Prop
when we can "just" build it to satisfy
Prop
? At least three reasons.
First
, sometimes
Prop
is simply impossible to satisfy and we need to add assumptions to make this property. We do this a lot in formal methods with
fairness
. The property "
mergesort
always returns a sorted list" is unsatisfiable because we can dropkick the computer before it returns. Instead, we have to verify a weaker property like "
mergesort
always returns => it returns a sorted list" or "
mergesort
always makes progress => it will eventually return a sorted list."
Another example is Rust. Rust
does not
guarantee the property "the program is memory safe". It guarantees the weaker property "all
unsafe
blocks are memory safe => the program is memory safe". Making the language satisfy the stronger property would rule out too many use cases of Rust. Note you also get memory safety if you don't use
unsafe
, but that still satisfies the assumption, as all
zero
blocks are safe!
Second
, sometimes the strong property is satisfiable, but it's simply not worth the extra cost. Like it's possible to make our software resistant against cosmic rays, but if your code isn't running in space, why bother? Just say "No cosmic bit flips => things work". Or if your plugin works Neovim
0.12
but not 0.11, you could put in the effort to make it run on older versions, or you could tell everybody that they need to upgrade to use your plugin. "Neovim version is at least 0.12 => the plugin works".
Third
, sometimes the strong property is satisfiable in the system but not easily
verifiable
. Say your algorithm makes a lot of API calls and you don't want to hit rate limits while testing. If you
mock out the API
you're testing the weaker property "The mock is accurate to the API => the algorithm is correct".
Assumptions are a second level of system effect
I notice that almost all of the examples in the last two sections are exoprogram factors:
The JSON parser assumptions are about user input
Fairness assumptions are about the OS/hardware/operating environment
Unsafe assumptions are about things the Rust compiler can't verify
Cosmic ray assumptions depend on the physical location of the hardware
The plugin assumptions are about the Neovim team's release schedule and social compatibility contract
The edge case is replacing a third party call with a mock. The assumption is intraprogram because the program could just hit the API during testing. We still have the assumption because of an exoprogram constraint. Maybe this is why mocks are considered an antipattern in Agile.
One consequence of this is that checking whether assumptions hold is a different problem from verifying that your code works given the assumptions. Like to make sure "all unsafe blocks are safe" can't use the rust compiler, you need a second tool like
Miri
. I wonder if checking assumptions is, in practice, generally more difficult than checking everything else.
