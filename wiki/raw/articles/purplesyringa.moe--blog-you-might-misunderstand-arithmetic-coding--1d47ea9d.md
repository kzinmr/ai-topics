---
title: "You might misunderstand arithmetic coding"
url: "https://purplesyringa.moe/blog/./you-might-misunderstand-arithmetic-coding/"
fetched_at: 2026-05-05T07:02:08.484872+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# You might misunderstand arithmetic coding

Source: https://purplesyringa.moe/blog/./you-might-misunderstand-arithmetic-coding/

You might misunderstand arithmetic coding
May 3, 2026
This post assumes basic familiarity with
arithmetic coding
.
I’ve written an arithmetic coder, like, three times in my life, so the mistake I want to highlight is likely amateurish. But since I didn’t have a clue that my understanding was incomplete, I figured I needed to write a post about it.
If you search for a simple arithmetic coder, you might find something like this (pseudocode for terseness):
The encoder starts with an interval
[left; right]
covering the entire range of
u32
. It recursively divides it into two parts according to the probability of the current bit, and outputs the coordinate of a point within the final range – here
left
. The decoder receives this point and finds the sequence of intervals it’s present in, thus decoding bits. Predictable input recurses into long intervals, making the final point’s binary representation shorter, thus yielding high compression ratio. Entropy coding 101.
Since
u32
cannot represent small intervals, the encoder shifts out when the top byte becomes known, freeing up
8
bits for precision in low bits. The decoder uses the same condition as a clue that precision has increased and
x
needs to be updated.
This feels very intuitive, but this coder is actually suboptimal: its compression quality can degrade in edge cases, and the decoder is less efficient than it could be. This was surprising to learn for me, since I had assumed this was a textbook AC implementation. It turns out that’s not the case!
Issues
Before I explain the fix, we need to understand where the problems are coming from.
The output of an arithmetic coder has a length of approximately
∑
i
log
2
⁡
p
i
, where
p
i
represents the estimated probability that the
i
th bit has the correct value. Due to rounding, though, the effective
p
i
can significantly diverge from the intended
p
i
if the interval
[left; right]
gets too short.
We would
like
[left; right]
to always be, let’s say, at least
2
16
long to reduce these effects. But if the interval strafes a byte boundary, like
[
2
31
−
1
,
2
31
]
, the length can reach as low as
2
. This forces
p
i
=
1
2
, requiring the encoder to emit an entire bit, even if the input is very predictable.
So, for some reason, intervals of the same length behave differently wrt. precision, depending on their offset: an interval starting at
left = 0
never gets shorter than
2
24
, but one starting at a different position can. This asymmetry is not present in the infinitely precise formulation of AC – it’s purely an artifact of the practical coder.
This is not very noticeable in practice: strafing a byte boundary by chance is difficult when the probabilities are constantly changing, and maliciously attacking a compressor is as simple as encoding randomness anyway. But another consequence of this strangeness can bite you regardless of that.
Let’s look at the decoder:
let
mid
= left + ((right - left)
as
f32
* probability)
as
u32
;
if
x <= mid {
    right = mid;
    bit =
false
;
}
else
{
    left = mid +
1
;
    bit =
true
;
}
This snippet accesses three integer variables:
left
,
right
,
x
. But just two values –
right - left
and
x - left
– could encode the same information in less space, reducing register pressure and improving performance.
The only reason
left
and
right
need to be known separately is to figure out when to increase precision. Again: the
entire
reason for having three variables is the
while
condition. If we could make the precision increase offset-independent, relying only on the length of the interval, the decoder could become significantly simpler.
Philosophy
The solution to this problem is somewhat tricky, so I want to give a birds-eye view on the situation first.
You might interpret this line as rounding
mid
to an integer, and reason that the coder works because the encoder and the decoder do it the same way:
let
mid
= left + ((right - left)
as
f32
* probability)
as
u32
;
This is a bad way to look at it. A more prospective interpretation is that this tweaks the effective
probability
such that
mid
is an integer – even if that’s not what the code looks like. The idea behind this is that it allows a limited-precision decoder and a perfect encoder to be compatible if the probabilities are tweaked correctly, and vice versa. This decouples the encoding from decoding and lets us build a formal model.
Fixing decoder
So we’re going out on a limb and update the
while
condition in the decoder to the offset-independent
right - left < 1 << 24
:
let
mut
length
:
u64
=
u32
::MAX
as
u64
+
1
;
let
mut
x
:
u32
= ...;
fn
decode_bit
(probability:
f32
)
->
bool
{
assert!
(
0.0
< probability && probability <
1.0
);
let
bit
;
let
mid
= (length
as
f32
* probability)
as
u32
;
if
x <= mid {
        length = mid
as
u64
;
        bit =
false
;
    }
else
{
        length -= mid
as
u64
;
        x -= mid;
        bit =
true
;
    }
while
length <
1
<<
24
{
        length <<=
8
;
        x = (x <<
8
) | (bytes.
next
().
unwrap
()
as
u32
);
    }

    bit
}
This corresponds to
some
effective probabilities – an infinite-precision encoder can provide a compatible output if we adjust probabilities correctly at its input.
For now, we’ll assume that infinite precision exists, and reinterpret the decoder from this perspective.
x
,
length
,
mid
are all floating-point representation values with 32-bit significands, with the exponent adjusted when the top
8
bits of
length
are zero.
The line
x = (x << 8) | ...
is trickier than it looks:
x
has been updated by
x -= mid
by now, so it’s not clear that this is equivalent to an infinite-precision decoder, which would populate
x
with the entire input once at the beginning.
Luckily, since subtracting a number with trailing zeros from a number with a tail keeps the tail intact, this works out. Here’s a graphical interpretation of
x -= mid
:
x = 0 . x0 x1 ... x31 x32 ...
        mid = 0 . m0 m1 ... m31 0   ...
y = x - mid = 0 . y0 y1 ... y31 x32 ...
The decoder doesn’t have to load
x32 ...
into
x
at once because it knows that the tail can be included at a later time without errors.
These subtleties are an indicator of the fact that this decoder is an optimized implementation of an infinite-precision decoder, with just probabilities adjusted for practicality, rather than an ad lib. This will help us design the encoder.
Fixing encoder
The old encoder can’t handle the
right - left < 1 << 24
condition, because this permits
left >> 24 != right >> 24
, and thus off-by-one errors can occur if bytes that aren’t actually known are pushed.
But the fact that the decoder is effectively perfect allows us to design an encoder separately, comparing it to the model of an infinite-precision encoder without any consideration for the specifics of the decoder.
Let’s take a look at a perfect encoder:
let
mut
left
: real =
0.0
;
let
mut
length
: real =
1.0
;
fn
encode_bit
(bit:
bool
, probability:
f32
) {
assert!
(
0.0
< probability && probability <
1.0
);
let
mid
= ;
if
!bit {
        length = mid;
    }
else
{
        left -= mid;
        length -= mid;
    }
while
{
        
    }
}
Much like the decoder has an implicit global scale that
length * probability
is rounded to, the encoder has one as well. Let’s make it visible as
exponent
, and multiply
left
and
length
by
2^exponent
so that we can work in (still infinite!) integers.
let
mut
left
: int =
0
;
let
mut
length
: int =
1
<<
32
;
fn
encode_bit
(bit:
bool
, probability:
f32
) {
assert!
(
0.0
< probability && probability <
1.0
);
let
mid
= (length
as
f32
* probability)
as
u32
;
if
!bit {
        length = mid;
    }
else
{
        left += mid;
        length -= mid;
    }
while
length <
1
<<
24
{ 
        
        left <<=
8
;
        length <<=
8
;
    }
}
Since
length
is always at most
2
32
, it fits in
u64
, and we don’t need a long integer there.
left
, however, is constantly increasing, so we can’t apply the same optimization.
But looking closely at the specific operations applied to
left
reveals another approach:
left += mid
: add a 32-bit value to
left
.
left <<= 8
: shift
left
to the left by 8 bits.
The first operation can change the low 32 bits of
left
unpredictably, but the carry-out to higher bits can be at most 1. So we can introduce an auxiliary data structure and store
left
in two parts: the bottom 32 bits to benefit from fast native addition, and the rest of the bits, for which we’ll implement carry propagation by hand:
let
mut
left_bottom
:
u32
=
0
;
let
mut
left_rest
:
Vec
<
u8
> =
Vec
::
new
();
let
mut
length
: int =
1
<<
32
;
fn
encode_bit
(bit:
bool
, probability:
f32
) {
assert!
(
0.0
< probability && probability <
1.0
);
let
mid
= (length
as
f32
* probability)
as
u32
;
if
!bit {
        length = mid;
    }
else
{
let
mut
carry
;
        (left_bottom, carry) = left_bottom.
overflowing_add
(mid);
for
num
in
left_rest.
iter_mut
().
rev
() {
if
!carry {
break
;
            }
            (*num, carry) = num.
overflowing_add
(
1
);
        }

        length -= mid;
    }
while
length <
1
<<
24
{ 
        
        left_rest.
push
((left_bottom >>
24
)
as
u8
);
        left_bottom <<=
8
;

        length <<=
8
;
    }
}
Do you see some similarity with the previous encoder in the
while
loop?
left_rest
is what used to be
bytes
, and
left_bottom
is what used to be
left
. So pretty much the only difference between the two decoders (except for the
while
condition) is that the new one adjusts its output when a carry occurs, while the old one never had carries:
-left += mid;
+let mut carry;
+(left, carry) = left.overflowing_add(mid);
+// If the carry is present, propagate it to the rest of `left` by hand.
+for num in bytes.iter_mut().rev() {
+    if !carry {
+        break;
+    }
+    (*num, carry) = num.overflowing_add(1);
+}
In streaming encoders, you might see a slightly different data structure implementing the same operations, but that’s the gist of it.
If you care about
𝒪
(
1
)
space, you might also see carry propagation in finalization: if
left + (length - 1)
overflows, incrementing
bytes
and zeroing out
left
produces a point within in the correct interval without having to append anything to
bytes
.
Conclusion
Let’s look at this from a practical perspective.
Changing the
while
condition from
left >> 24 == right >> 24
to
right - left < 1 << 24
improves worst-case compression quality and simplifies the decoder by removing one variable. This reduces code size and improves performance.
In exchange, the encoder got a little more complex. It uses two variables just like before, but now it needs to mutate its output. It’s not too expensive, but streaming requires tracking carries in a different manner, which can be trickier.
This introduces asymmetry between the encoder and the decoder, so it’s not always worthwhile. However, if the data is compressed once and decoded multiple times, it may be reasonable, increasingly so if the encoder is already slow due to an LZ pass.
References
In case you want to learn more or this explanation wasn’t detailed enough for you, here’s a couple resources that helped me figure it out myself. They’re long, but if you have time, they’re a good investment.
