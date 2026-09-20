---
title: "Finding Bugs"
url: "https://matklad.github.io/2026/09/19/finding-bugs.html"
fetched_at: 2026-09-20T10:01:20.123514+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Finding Bugs

Source: https://matklad.github.io/2026/09/19/finding-bugs.html

Finding Bugs
Sep 19, 2026
Are generative (randomized) tests significantly more effective than example-based
unit-tests at discovering bugs? There’s
an interesting discussion about this on lobste.rs
.
One argument in favor of unit tests is, paraphrasing
My generic fuzzer wasn’t able to find
this tricky bug
in Rust
regex
crate.
To me, it seems that generative testing should shake out that particular
creature, so I wrote
a lil fuzzer
of my own, and it indeed discovered
another
bug in that version of
regex
,
and then the one I was after. I didn’t find anything in the latest version. I
like to do a write up about the process, as it is a good case study for how one
approaches a problem like this.
I want to be extra clear that my argument is very weak here, as I know exactly
the bug I am after, and I even know that fuzzers can find it. My primary goal is
to teach you the techniques, leaving it to your judgment just how effective they
are. That being said, I think finding a
second
bug validates the approach
somewhat.
I also want to emphasize that writing fuzzers to find known bugs is far from an
idle amusement. While I believe that generative testing is very powerful,
relative to its cost, it’s always a question whether a particular test is
throughout enough. And it never is, you
will
find more bugs elsewhere (that’s
why defense in depth and
runtime
mitigations are critical). And, whenever you
have a pest that dodged your fuzzers, your first order of business is to treat
this event as a bug in the
fuzzer
, and change it so that it can find this and
related bugs. Only then you are allowed to add a fix and a unit test!
For
".abb|b"
regex and
"zabb"
input, an older version of
regex
crate
returned
b
as the first match, which is incorrect, because the entire
zabb
matches:
use
regex;
fn
main
() {
let
r
= regex::Regex::
new
(
".abb|b"
).
unwrap
();
let
m
= r.
find
(
"zabb"
).
unwrap
();
assert_eq!
(m.
as_str
(),
"zabb"
)
}
How do we find this, or something
like
this?
Regular expression engines are one of the easiest things to apply generative
testing to, they are pure algorithms. While few large systems are
just
an
algorithm, algorithms are everywhere inside components of interesting systems,
so this is a hands-on knowledge.
And by far the most important technique for testing algorithms is to compare
with the known right answer, with an oracle. Implement both
O(N log N)
and
O(N^2)
versions of the algorithm, and match the answers.
To be fair, the original comment mentioned that the their fuzzer didn’t find the
issue because they didn’t have access to an oracle. However, if you are
designing a reliable system, it’s part of your job to ensure it has an oracle!
One of the first things we did for our
Jepsen test
at TigerBeetle was to
expose internal timestamps
via API, to make it easier for Jepsen to find bugs (TigerBeetle is
co-designed
with
its internal simulator
VOPR
which naturally has access to timestamps and anything else). And for, a regex
engine, coming up with an oracle shouldn’t be hard, as they typically already
come with multiple specialized implementations under a single facade, and the
implementations can be cross-checked against each other.
But the
regex
case is even simpler (which makes it an excellent case study).
There’s
regex_lite
crate that provides the same API.
So here’s a plan: generate a regular expression, an input text, and check that
regex
and
regex_lite
give identical answers.
I’ll start with code that generates a random string, as it is simpler, but still
shows some non-trivial ideas. First, we’ll need a random number generator:
use
fastrand::Rng;
There are fancier techniques, which can give you
test-case minimization
,
exhaustive search
, or
coverage guided exploration
, but the
insight is that even a humble PRNG is brutally effective, if you put it to good use.
When you start with randomized testing, the instinct is to generate something
big, no, HUGE! Surely regex will choke on 5 GiBs of input? This is usually a
wrong call. Bugs
usually
involve small, but tricky examples, weaponizing
interactions between a few features. A string where all characters are the same
is more likely to trigger a bug than a purely random string where every
character is unique.
So my default approach to generating strings is this.
First
, I fix the
alphabet of possible characters. A nice way to get one is to
sort | unique
all
the unit tests. Then, for each particular string, I pick a
subset
of that
alphabet. I want strings that use all the characters, but I also want long
strings with only
a
and
b
! Then I generate a string using the given subset
of the alphabet, where the length of the string is also picked at random.
To make fuzzing efficient, I want to keep each iteration as fast as possible, so
I make sure to re-use the memory across iterations,
static allocation
in the small:
use
fastrand::Rng;
fn
main
() {
let
mut
rng
= Rng::
new
();
let
mut
text_alphabet
:
Vec
<
u8
> =
vec!
[];
let
mut
text
:
Vec
<
u8
> =
vec!
[];
for
_
in
0
..
1_000_000
{
alphabet_swarm
(&
mut
rng,
b"abcdef"
, &
mut
text_alphabet);
let
text
=
gen_string
(&
mut
rng, &text_alphabet, &
mut
text);
}
}
fn
alphabet_swarm
<
'a
>(
rng: &
mut
Rng,
all: &[
u8
],
pick: &
'a
mut
Vec
<
u8
>,
) {
pick.
clear
();
pick.
extend
(all);
rng.
shuffle
(pick);
let
count
= rng.
usize
(
1
..=pick.
len
());
pick.
truncate
(count);
}
fn
gen_string
<
'a
>(
rng: &
mut
Rng,
alphabet: &[
u8
],
result: &
'a
mut
Vec
<
u8
>,
)
->
&
'a
str
{
result.
clear
();
let
count
= rng.
usize
(
0
..
8
);
for
_
in
0
..count {
result.
push
(alphabet[rng.
usize
(
0
..alphabet.
len
())]);
}
str
::
from_utf8
(result).
unwrap
()
}
There’s a nice way to think about this two step process, generating alphabet
first, and then generating a string. To generate a string, you need a
distribution of characters. You
can
use the same distribution for each of the
million iterations. But an easy way to spice things up is to make the
distribution
itself
random. I file this “randomize distributions themselves” idea under
swarm testing
.
Let’s apply the same tricks when generating a regex:
pick a subset of active regex features,
pick size at random,
re-use memory.
Let’s start with the first one:
#[derive(Default, Debug)]
struct
ReOptions
{
alt:
u16
,
rep:
u16
,
any:
u16
,
lit:
u16
,
sum:
u16
,
alphabet:
Vec
<
u8
>,
}
Regexes have alternation
r1|r2
, repetition
r*
, wildcard
.
, and literals
a
. Rather then binary enabling or disabling a particular feature, I assign
each feature a weight between 0 and 100, which is a bit more general. The
sum
is the total of all weights. To select a feature at random, we need to generate
a number in
0..sum
and find which segment it falls into.
In anything more serious, I’d introduce explicit types for probabilities and
distributions, but just a two-digit number is perfectly serviceable in the
small.
This is how I generate
ReOptions
, making sure that literals always have
non-zero weight, and also selecting an alphabet for them:
impl
ReOptions
{
fn
swarm
(&
mut
self
, rng: &
mut
Rng, alphabet_full: &[
u8
]) {
self
.alt =
if
rng.
bool
() {
0
}
else
{ rng.
u16
(
0
..
100
) };
self
.rep =
if
rng.
bool
() {
0
}
else
{ rng.
u16
(
0
..
100
) };
self
.any =
if
rng.
bool
() {
0
}
else
{ rng.
u16
(
0
..
100
) };
self
.lit = rng.
u16
(
1
..
100
);
self
.sum =
self
.alt +
self
.rep +
self
.any +
self
.lit;
assert!
(
self
.sum >
0
);
alphabet_swarm
(rng, alphabet_full, &
mut
self
.alphabet);
}
}
So now we can generate a regular expression. This is convenient to do
recursively. To avoid allocations, an output buffer is passed through. To
control regex length, a
size
parameter is also threaded, and “branching”
recursive invocations divide the
size
between the children:
fn
gen_re
(
rng: &
mut
Rng,
options: &ReOptions,
result: &
mut
Vec
<
u8
>,
) {
result.
clear
();
let
size
= rng.
u8
(
0
..
8
);
gen_re_rec
(rng, options, result, size);
}
fn
gen_re_rec
(
rng: &
mut
Rng,
options: &ReOptions,
result: &
mut
Vec
<
u8
>,
size:
u8
,
) {
if
size ==
0
{
return
;
}
let
mut
p
= rng.
u16
(
0
..options.sum);
if
p < options.alt {
let
size_left
= rng.
u8
(
0
..=size -
1
);
let
size_right
= size - size_left -
1
;
assert!
(size == size_left +
1
+ size_right);
result.
push
(
b'('
);
gen_re_rec
(rng, options, result, size_left);
result.
extend
(
b")|("
);
gen_re_rec
(rng, options, result, size_right);
result.
push
(
b')'
);
return
;
}
p -= options.alt;
if
p < options.rep {
result.
push
(
b'('
);
gen_re_rec
(rng, options, result, size -
1
);
result.
extend
(
b")*"
);
return
;
}
p -= options.rep;
if
p < options.any {
gen_re_rec
(rng, options, result, size -
1
);
result.
push
(
b'.'
);
return
;
}
p -= options.any;
if
p < options.lit {
gen_re_rec
(rng, options, result, size -
1
);
let
index
= rng.
usize
(
0
..options.alphabet.
len
());
let
lit
= options.alphabet[index];
result.
push
(lit);
return
;
}
unreachable!
();
}
Given that compiling regular expressions is somewhat slow, it seems like a good
idea to try multiple strings for the same pair of regular expressions, which
gives the following code:
fn
main
() {
let
mut
rng
= Rng::
new
();
let
mut
options
= ReOptions::
default
();
let
mut
text_alphabet
:
Vec
<
u8
> =
vec!
[];
let
mut
text
:
Vec
<
u8
> =
vec!
[];
let
mut
re
:
Vec
<
u8
> =
vec!
[];
let
mut
test_count
:
u32
=
0
;
for
_
in
0
..
1_000_000
{
options.
swarm
(&
mut
rng,
b"abcdef"
);
alphabet_swarm
(&
mut
rng,
b"abcdefx"
, &
mut
text_alphabet);
gen_re
(&
mut
rng, &options, &
mut
re);
let
re
=
str
::
from_utf8
(&re).
unwrap
();
let
r1
= regex::Regex::
new
(re).
unwrap
();
let
r2
= regex_lite::Regex::
new
(re).
unwrap
();
for
_
in
0
..
1000
{
test_count +=
1
;
let
text
=
gen_string
(&
mut
rng, &text_alphabet, &
mut
text);
let
m1
= r1.
find
(text)
.
map_or
(
"not found"
, |it| it.
as_str
());
let
m2
= r2.
find
(text)
.
map_or
(
"not found"
, |it| it.
as_str
());
if
m1 != m2 {
eprintln!(
"err re={re} text={text} m1={m1} m2={m2}"
);
return
;
}
if
test_count %
500_000
==
0
{
eprintln!(
"ok  re={re} text={text}"
);
}
}
}
}
It produces examples similar to those in the issue, with a common suffix:
err re=(e)|(fee) text=xxfee
but also examples which somewhat different, without the shared suffix:
err re=(f..)*.d text=xfcbdd
All together:
use
fastrand::Rng;
fn
main
() {
let
mut
rng
= Rng::
new
();
let
mut
options
= ReOptions::
default
();
let
mut
text_alphabet
:
Vec
<
u8
> =
vec!
[];
let
mut
text
:
Vec
<
u8
> =
vec!
[];
let
mut
re
:
Vec
<
u8
> =
vec!
[];
let
mut
test_count
:
u32
=
0
;
for
_
in
0
..
1_000_000
{
options.
swarm
(&
mut
rng,
b"abcdef"
);
alphabet_swarm
(&
mut
rng,
b"abcdefx"
, &
mut
text_alphabet);
gen_re
(&
mut
rng, &options, &
mut
re);
let
re
=
str
::
from_utf8
(&re).
unwrap
();
let
r1
= regex::Regex::
new
(re).
unwrap
();
let
r2
= regex_lite::Regex::
new
(re).
unwrap
();
for
_
in
0
..
1000
{
test_count +=
1
;
let
text
=
gen_string
(&
mut
rng, &text_alphabet, &
mut
text);
let
m1
= r1.
find
(text)
.
map_or
(
"not found"
, |it| it.
as_str
());
let
m2
= r2.
find
(text)
.
map_or
(
"not found"
, |it| it.
as_str
());
if
m1 != m2 {
eprintln!(
"err re={re} text={text} m1={m1} m2={m2}"
);
return
;
}
if
test_count %
500_000
==
0
{
eprintln!(
"ok  re={re} text={text}"
);
}
}
}
}
fn
alphabet_swarm
<
'a
>(
rng: &
mut
Rng,
all: &[
u8
],
pick: &
'a
mut
Vec
<
u8
>,
) {
pick.
clear
();
pick.
extend
(all);
rng.
shuffle
(pick);
let
count
= rng.
usize
(
1
..=pick.
len
());
pick.
truncate
(count);
}
fn
gen_string
<
'a
>(
rng: &
mut
Rng,
alphabet: &[
u8
],
result: &
'a
mut
Vec
<
u8
>,
)
->
&
'a
str
{
result.
clear
();
let
count
= rng.
usize
(
0
..
8
);
for
_
in
0
..count {
result.
push
(alphabet[rng.
usize
(
0
..alphabet.
len
())]);
}
str
::
from_utf8
(result).
unwrap
()
}
#[derive(Default, Debug)]
struct
ReOptions
{
alt:
u16
,
rep:
u16
,
any:
u16
,
lit:
u16
,
sum:
u16
,
alphabet:
Vec
<
u8
>,
}
impl
ReOptions
{
fn
swarm
(&
mut
self
, rng: &
mut
Rng, alphabet_full: &[
u8
]) {
self
.alt =
if
rng.
bool
() {
0
}
else
{ rng.
u16
(
0
..
100
) };
self
.rep =
if
rng.
bool
() {
0
}
else
{ rng.
u16
(
0
..
100
) };
self
.any =
if
rng.
bool
() {
0
}
else
{ rng.
u16
(
0
..
100
) };
self
.lit = rng.
u16
(
1
..
100
);
self
.sum =
self
.alt +
self
.rep +
self
.any +
self
.lit;
assert!
(
self
.sum >
0
);
alphabet_swarm
(rng, alphabet_full, &
mut
self
.alphabet);
}
}
fn
gen_re
(
rng: &
mut
Rng,
options: &ReOptions,
result: &
mut
Vec
<
u8
>,
) {
result.
clear
();
let
size
= rng.
u8
(
0
..
8
);
gen_re_rec
(rng, options, result, size);
}
fn
gen_re_rec
(
rng: &
mut
Rng,
options: &ReOptions,
result: &
mut
Vec
<
u8
>,
size:
u8
,
) {
if
size ==
0
{
return
;
}
let
mut
p
= rng.
u16
(
0
..options.sum);
if
p < options.alt {
let
size_left
= rng.
u8
(
0
..=size -
1
);
let
size_right
= size - size_left -
1
;
assert!
(size == size_left +
1
+ size_right);
result.
push
(
b'('
);
gen_re_rec
(rng, options, result, size_left);
result.
extend
(
b")|("
);
gen_re_rec
(rng, options, result, size_right);
result.
push
(
b')'
);
return
;
}
p -= options.alt;
if
p < options.rep {
result.
push
(
b'('
);
gen_re_rec
(rng, options, result, size -
1
);
result.
extend
(
b")*"
);
return
;
}
p -= options.rep;
if
p < options.any {
gen_re_rec
(rng, options, result, size -
1
);
result.
push
(
b'.'
);
return
;
}
p -= options.any;
if
p < options.lit {
gen_re_rec
(rng, options, result, size -
1
);
let
index
= rng.
usize
(
0
..options.alphabet.
len
());
let
lit
= options.alphabet[index];
result.
push
(lit);
return
;
}
unreachable!
();
}
https://github.com/matklad/regex-fuzz
Takeaways:
Fuzzing against an oracle is effective, which is a strong motivation to build
an oracle!
Go for small, tricky examples, rather than large uniform ones.
Real fuzzers are cool, but, if you know something, even xoroshiro can be dangerous.
Black box testing is cool, but co-designing system and its testing harness is
a point of leverage (build an oracle!).
This stuff is not rocket science, you don’t need a Haskell PhD to apply these
ideas.
