---
title: "Suffix BWT vs cyclic shift BWT, and fast computation"
url: "https://purplesyringa.moe/blog/./suffix-bwt-vs-cyclic-shift-bwt-and-fast-computation/"
fetched_at: 2026-07-04T07:01:39.850707+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# Suffix BWT vs cyclic shift BWT, and fast computation

Source: https://purplesyringa.moe/blog/./suffix-bwt-vs-cyclic-shift-bwt-and-fast-computation/

Suffix BWT vs cyclic shift BWT, and fast computation
July 3, 2026
Intended audience: data compression geeks.
The
Burrows-Wheeler transform
takes a string as an input and rearranges its characters, grouping them by context. It is invertible with
𝒪
(
1
)
additional input, and together these properties give it a place in data compression and genome alignment.
What Wikipedia doesn’t tell you is that there are actually two variants of BWT, with subtly different performance characteristics and simplicity. These differences seem to be largely undocumented, so this post is me trying to make sense of it.
Cyclic shift BWT
I’ll cover what I call “cyclic shift BWT” first.
Let’s start with the string
bcacaba
. We write down all cyclic shifts, or rotations of this string, along with their offsets:
bcacaba (0)
cacabab (1)
acababc (2)
cababca (3)
ababcac (4)
babcaca (5)
abcacab (6)
We then sort them lexicographically:
ababcac (4)
abcacab (6)
acababc (2)
babcaca (5)
bcacaba (0)
cababca (3)
cacabab (1)
The output of the BWT is the sequence of characters just before the start of each cyclic shift. For example, the first cyclic shift in the list starts at
4
, so we write down the character at offset
3
in the input, which is
c
. The final output is
cbcaaab
. (Note that this is the same as taking the last column of the table above.)
Two strings sorted next to each other are likely to have a long common prefix, and thus the symbol before them is also likely to match in realistic data. For example, if in a given text the string
ender
is always preceded by
g
,
b
, or a space, there’s going to be a long subsequence in the output composed entirely of these three symbols.
This algorithm is invertible: if you know the output of the BWT, you can recover the input up to a cyclic shift. Here’s how you can do this:
Preparation step: take the output of the BWT (
cbcaaab
) and sort its characters lexicographically. This reveals the first column of the table above:
aaabbcc
.
Now take the first character of the output,
c
. It was produced by taking the last character of some cyclic shift
t
‖
"
c
"
. We will now find the character before this
c
, i.e. the last character of
t
.
There are two
c
s in the text, so there are two cyclic shifts ending with
c
:
t
1
‖
"
c
"
and
t
2
‖
"
c
"
. Since we took the first
c
of the output, not the second one, it much be part of the lexicographically smaller shift
t
‖
"
c
"
=
t
1
‖
"
c
"
<
t
2
‖
"
c
"
(and
t
1
<
t
2
).
Now consider shifts
starting
with
c
. There are also two of them,
"
c
"
‖
t
1
and
"
c
"
‖
t
2
, and since
t
1
<
t
2
, they’re ordered in the same way:
"
c
"
‖
t
1
<
"
c
"
‖
t
2
.
The first column tells us these cyclic shifts are located at indices
5
and
6
in the sorted order. The smaller one is at index
5
, and according to the BWT output that shift (
"
c
"
‖
t
1
) ends with
a
. Hence the
c
at index
0
is preceded by the
a
at index
5
.
This process can now be repeated starting with this
a
: it terminates the third shift out of three shifts ending with
a
, so the character before it is last in the third shift out of three shifts starting with
a
, i.e.
c
at index
2
, etc. This recovers the characters of the input in reverse order.
In pseudocode, the decoder looks something like this:
pos_in_char = []
counts = [
0
] *
256
for
c
in
bwt:
    pos_in_char.append(counts[c])
    counts[c] +=
1
s =
""
i =
0
for
_
in
range
(
len
(bwt)):
    s =
chr
(bwt[i]) + s
    
    
    i =
sum
(counts[:bwt[i]]) + pos_in_char[i]
print
(s)
To recover the original string exactly, not just up to a cyclic shift, we have to start decoding from
i
representing the cyclic shift with offset
0
(so-called
primary index
). In this example, the encoder can communicate that it’s index
4
to the decoder.
Suffix BWT
Now that you hopefully understand how cyclic shift BWT works, let’s compare it to suffix BWT.
We start with the same string
bcacaba
, but this time we write down and sort suffixes instead of cyclic shifts:
empty   (7)
a       (6)
aba     (4)
acaba   (2)
ba      (5)
bcacaba (0)
caba    (3)
cacaba  (1)
Note that the order is different from cyclic shifts: whereas before, offset
4
(
ababcac
) was located before
6
(
abcacab
), now offset
4
(
aba
) is located after offset
6
(
a
). Such a flip can occur when one suffix is a prefix of another, since lexicographic comparison considers shorter strings smaller, all other things being equal.
Just like before, we construct the output out of characters preceding the suffixes:
abcca^ab
.
^
denotes the full suffix, which is not preceded by anything, and in practice we drop it:
abccaab
.
Decoding suffix BWT is a little subtle. Due to the empty suffix at the beginning, we have to bump up every computed index by one. And since the full suffix is dropped without a trace, we have to decrement every index after the position where the full suffix
would
be, if it was present in the BWT.
s =
""
i =
0
for
_
in
range
(
len
(bwt)):
    s =
chr
(bwt[i]) + s
    i =
sum
(counts[:bwt[i]]) + pos_in_char[i]
    i +=
1
if
i > where_full_suffix_would_be: 
        i -=
1
One would hope that dropping the empty suffix instead of the full suffix would cancel out these nuances:
# no empty suffix, no problem
# the character in [_] is the character preceding the suffix
[b] a       (6)
[c] aba     (4)
[c] acaba   (2)
[a] ba      (5)
[a] bcacaba (0) # retain the full suffix, say it's cyclically preceded by "a"
[a] caba    (3)
[b] cacaba  (1)
Assume that we blindly trust this algorithm and tell the decoder the BWT string is
bccaaab
and the full suffix is at index
4
. The decoder would correctly infer that the last character of the string is
a
, and then notice that it’s the second
a
out of three and thus jump to index
1
among
0
–
2
. But that corresponds to the suffix
aba
, not
a
! Oops!
Why did this happen? With this approach, suffixes preceded by
a
are
"ba" < "bcacaba" < "caba"
. Prepending
a
gives
"aba" < "abcacaba" < "acaba"
. But
abcacaba
is not a suffix, only
a
is, which is ordered differently wrt. other suffixes:
"a" < "aba" < "acaba"
. Ordering breaks at the
0
boundary, and there is no safe lie we can tell about which character precedes the full suffix.
Comparison
Given these nuances, you might reasonably assume that everyone uses cyclic shift BWT, and suffix BWT is a relic. But that’s not the case.
While suffix BWT is a little trickier and slower to decode, it’s much faster to encode. There are plenty of fast approaches to
sorting suffixes
, the most practical one being the linear-time
SA-IS
algorithm, but very few for cyclic shifts. Baby’s first
𝒪
(
n
log
⁡
n
)
suffix array implementation
works on cyclic shifts, sure, but I couldn’t find any linear-time algorithm focusing on cyclic shifts in the literature.
So that’s what most people do: import
libsais
, construct the suffix array, drop the full suffix and prepend the empty suffix, and construct suffix BWT via
s[sa[i] - 1]
. Or call the
libsais_bwt
function that does the same thing.
In many cases, that’s perfectly fine. You can often prepend a
^
character that compares less than every other character, so that the full suffix ends up at index
0
and you don’t need to adjust
i
. Or append a
$
character, so that suffix BWT and cyclic shift BWT coincide up to the position of
$
, which ends up doing almost the same thing.
Tricking SA-IS
But what if you do need cyclic shift BWT? Maybe your alphabet is full and implementing a real suffix BWT decoder is too expensive, or maybe your problem asks for it specifically. In this case, we can still use SA-IS with a few adjustments.
The easiest way to implement wrap-around semantics is to double the string. Two suffixes of the string
s
‖
s
starting at offsets
i
,
j
<
|
s
|
compare exactly like the corresponding cyclic shifts of
s
. So you can double
s
, compute the suffix array, drop indices
≥
|
s
|
, and compute cyclic BWT and the primary index from that list.
If you don’t want to pay double the price, there’s another approach.
Take the lexicographically smallest cyclic shift of
s
, say,
s
′
. For
s = "bcacaba"
, that would be
s' = "ababcac"
. Suffixes of
s
′
compare exactly like its cyclic shifts:
"c" < "cac"
and
"cababca" < "cacabab"
. This works because
s
′
plays the same role as the implicit
$
terminator for the purposes of lexicographic comparison at the cut-off point. Since cyclic BWT is indifferent to rotating the input, computing suffix BWT of
s
′
gives the correct result. I learned this from
Christoph Diegelmann’s SO answer
.
The smallest cyclic shift can be found by running
the Duval algorithm
on
s
‖
s
. It’s linear-time, but has a smaller constant than SA-IS, so that’s a great speed-up.
The only issue is that the primary index gets corrupted by rotating
s
. There are two ways to recover it. First, we can build the SA of
s
′
instead of jumping straight to BWT, and find where
s
is in that list. This works, but it’s somewhat costly.
Alternatively, we can compute the primary index by definition, as the number of cyclic shifts of
s
lexicographically smaller than
s
. The
Z-function
can find in linear time, for each suffix
(
s
‖
s
)
[
i
…
]
, the length of the common prefix of
(
s
‖
s
)
[
i
…
]
and
s
‖
s
, which is precisely the position that determines whether the cyclic shift at
i
is smaller than
s
. Or, depending on the data, it may be faster to use a quadratic algorithm instead.
Here is my implementation
.
Conclusion
So which one should you use? In most cases, suffix BWT is better: an efficient suffix BWT encoder is both simpler to implement and has higher top performance, while decoding is only a little slower, and only if the alphabet is full.
I think cyclic shift BWT shines specifically when you need a tiny decoder and don’t care much about the encoder size.
Demos
and size-coding in general come to mind. It also matters more in scripting languages, where decoding runtime is not dominated by pure memory accesses, and adjustments measurably slow down the process.
I hope I didn’t get anything wrong here! This is a topic I’m not too familiar with, so if I made a mistake, feel free to send me an e-mail.
