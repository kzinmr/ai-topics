---
title: "Explanation of my Code Guessing entry (round 6)"
url: "https://iczelia.net/posts/cg-explanation/"
fetched_at: 2026-05-05T07:01:23.036371+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Explanation of my Code Guessing entry (round 6)

Source: https://iczelia.net/posts/cg-explanation/

For the unfamiliar - What is code guessing?
⌗
Code guessing
is a game played on one of my Discord servers. Participants write programs that solve a specific problem. The solutions (usually written in C or Python) are published on my website and the participants try to guess who made each of the solutions. After the guessing phase ends, the points are calculated. Being guessed costs one point, guessing someone correctly grants one point. The person with the most points is declared the winner and picks the next challenge (and supported languages).
This round of code guessing required the participants to write the following program:
Make a function that takes a natural number
i
i
i
and returns or prints a series of unique numbers
a
1
a_1
a
1
​
to
a
n
a_n
a
n
​
, where
∑
k
=
1
n
f
(
a
k
)
=
i
\sum_{k = 1}^{n} f(a_k) = i
∑
k
=
1
n
​
f
(
a
k
​
)
=
i
and
f
(
x
)
=
f
i
b
(
x
)
f(x) = fib(x)
f
(
x
)
=
f
ib
(
x
)
for
x
≥
0
x \geq 0
x
≥
0
, and
f
(
x
)
=
−
f
i
b
(
x
)
f(x) = -fib(x)
f
(
x
)
=
−
f
ib
(
x
)
otherwise.
For example,
i
=
1070
i = 1070
i
=
1070
should yield
-1 -5 11 16
, because:
1070
=
987
+
89
−
5
−
1
1070 = 987 + 89 - 5 - 1
1070
=
987
+
89
−
5
−
1
and
987
=
f
i
b
(
16
)
987 = fib(16)
987
=
f
ib
(
16
)
,
89
=
f
i
b
(
11
)
89 = fib(11)
89
=
f
ib
(
11
)
,
5
=
f
i
b
(
5
)
5 = fib(5)
5
=
f
ib
(
5
)
and
1
=
f
i
b
(
1
)
1 = fib(1)
1
=
f
ib
(
1
)
Meaning that
1070
=
f
i
b
(
16
)
+
f
i
b
(
11
)
−
f
i
b
(
5
)
−
f
i
b
(
1
)
=
f
(
16
)
+
f
(
11
)
+
f
(
−
5
)
+
f
(
−
1
)
1070 = fib(16) + fib(11) - fib(5) - fib(1) = f(16) + f(11) + f(-5) + f(-1)
1070
=
f
ib
(
16
)
+
f
ib
(
11
)
−
f
ib
(
5
)
−
f
ib
(
1
)
=
f
(
16
)
+
f
(
11
)
+
f
(
−
5
)
+
f
(
−
1
)
Because addition is commutative, the output vector can be given in any order.
My entry
⌗
My entry to the 6th round follows:
Preliminaries
⌗
That’s a lot to unpack, so let’s try it step by step. The first step is passing the code through the C preprocessor:
At this point, I dropped the code into clang-format. Unfortunately, it looks even scarier than before (presumably because its volume increased). My entry uses a technique described in my
previous blog post
about non-alphanumeric code. So let’s fold the constants then:
'`' - '!'
is
63
'$' - '$'
is
0
'>' - '='
,
'@' - '?'
,
'^' - ']'
,
'&' - ~~'%'
,
')' - '('
and
';' - ':'
are
1
':' - ';'
is
-1
The transformed code follows:
At this point, it’s a good idea to test if the code still works. I did so by tacking the following function at the bottom of it:
The program prints
40 23 12 -8 -5 -2
, so it’s still valid. The next step is merging constant values into the code. I also renamed the identifiers now so they’re easier to tell apart.
Diving into the code
⌗
At this point, the code starts looking more and more bearable. Let’s take on the smallest functions first:
g
returns truncated
n
if
n
doesn’t have a decimal part. Otherwise, it returns truncated
n + 1
, meaning that
g
is a ceiling function.
h
reinterprets a
long
as a
float
. Scary.
What’s
f
then? Let’s see:
Looking at where
f
is called, we deduce that
a
is the
fib
array from
main
. When we look at it’s initialisation code, it’s fairly obvious that this array is a cache of fibonacci numbers:
What about
b
and
c
?
b
doesn’t seem to be altered across recursive calls and it might be a good idea to turn the recursive function into something that uses iteration:
While the current fibonacci number (starting from
c
) is greater than… something, we keep decreasing it, until it’s smaller or equal to it.
What’s this bit trickery anyways?
b + (b >> 63)
will add the highest bit of this number to itself. Obviously, this has two possible outcomes - it yields either
b - 1
or
b
.
Ans ^ (b >> 63)
ends up being either
(b - 1) ^ -1
, or
b ^ 0
.
b ^ 0
is obviously
b
, while
(b - 1) ^ -1
is more interesting. Looking at the
xor
truth table, we learn that xoring a binary digit by
1
negates it, so our expression could be rewritten as
~(b - 1)
. For a signed integer,
~
acts
fairly similar
to absolute value, except it’s off by one
, so the
- 1
part fixes it:
This way, we’ve established that
((b + (b >> 63)) ^ (b >> 63))
is
abs(b)
. Let’s use this in the code:
f
returns the largest fibonacci number lesser or equal to
abs(b)
(because
c
, judging by all calls of
f
, is the size of the fibonacci number cache).
The Q function
⌗
Let’s take on
q
now. We apply the same absolute value transformation on it:
Our familiar pattern occurs in the code once more - we take the absolute value of
abs(h) - b[d]
and
abs(h) - b[d + 1]
:
Let’s break this ugly
return
statement down and ponder a little about
1 | (h >> 63)
. We already know that
h >> 63
is either
-1
if
h
is negative or
0
otherwise. Because
-1
is just all ones,
1 | 0xFFFFFFFFFFFFFFFF
simply yields
0xFFFFFFFFFFFFFFFF
. In the
0
case,
0 | 1
becomes
1
, so
1 | (h >> 63)
yields us the sign of the number. After applying the transformations, the
e
parameter is no longer needed, so it has been removed.
A few things can be done about the code in this shape, starting with removing the negation from
g
.
Now, we can turn the tail call into a
for
loop:
We know that
f()
returns the index in
fibs
,
d
is the length of the fibonacci numbers array as perceived by
f
, and
h
is our input (judging by the call to
q
in
main
). Let’s introduce meaningful names to our code now.
a
seems to be meaningless, so we remove it:
Let’s describe the algorithm now:
Compute the sign of input.
Find the largest fibonacci number which is lesser or equal to the input.
If it’s
worth
it, increment the index (so we subtract a larger fibonacci number). The operation is considered to be worth it if the absolute value after subtracting the larger fibonacci number is smaller than the absolute value after subtracting the smaller fibonacci number.
Add the fibonacci index to the output vector. Make sure it has the correct sign.
Subtract the fibonacci number from our input
Set a new boundary on fibonacci number cache size passed to
f
(to make the scan a little more efficient).
Explaining the I function
⌗
Now that we’ve figured out the actual solution part, paradoxically, we’re heading into the most tangled areas of the code.
Like with most eldritch horrors like this, I like to plug a few numbers into the function to see what’s going on:
The results look oddly similar to what we’d get from
log
⁡
10
n
\log_{10} n
lo
g
10
​
n
, except the domain of our function is presumably
<
1
,
∞
>
<1, \infty>
<
1
,
∞
>
.
The constant
0xff800000
should already alert someone familiar with floating point trickery. Assuming IEEE-754, this snippet extracts the exponent and the sign from a floating point number -
0xFF800000
is 9 ones followed by a trail of zeroes, since an IEEE-754 number consists of the sign bit, exponent (8 bits) and the mantissa. Intuition aside, let’s try to methodically untangle this function:
Let’s focus on the declarations.
x
is of course the IEEE-754 representation of our input number.
0x3f2aaaab
is the binary representation of
0.
(
6
)
0.(6)
0.
(
6
)
in IEEE-754 and it’s used to reduce the mantissa range to
<
2
3
,
4
3
>
<\frac{2}{3}, \frac{4}{3}>
<
3
2
​
,
3
4
​
>
. We extract the sign and exponent of it as
v
. Subtracting the exponent from the input naturally gives us the mantissa (in
u
). Subtracting
1
from the mantissa gives us a
<
−
1
3
,
1
3
>
<-\frac{1}{3}, \frac{1}{3}>
<
−
3
1
​
,
3
1
​
>
range of
m
.
So what actually happened here? We separated our input
n
n
n
into the exponent and mantissa, where
n
=
m
∗
2
e
n = m * 2^e
n
=
m
∗
2
e
, so
log
⁡
n
=
e
∗
log
⁡
2
+
log
⁡
m
\log n = e * \log 2 + \log m
lo
g
n
=
e
∗
lo
g
2
+
lo
g
m
. Finally, if we limit the range of
m
m
m
enough, we can compute
log1p(u)
which is approximately
log
⁡
n
\log n
lo
g
n
, so what we’re striving for is limiting
m
m
m
into a range so that the argument to
log1p
is in a small, uniform range. And that’s what the declarations did.
The following computation oddly resembles something involving a
Chebyshev polynomial
, which I’m already familiar with (I used it for approximating trigonometric functions). Regarding the algorithm for approximating functions in a Chebyshev space (e.g. the subspace of
n
n
n
-th order Chebyshev Polynomials in the space of real continuous functions in an interval), I used the
Remez exchange algorithm
.
Finally,
2.302585092994045f
is approximately
log
⁡
10
\log 10
lo
g
10
. Having computed
log
⁡
n
\log n
lo
g
n
, we turn it into
log
⁡
10
n
\log_{10} n
lo
g
10
​
n
using the change-of-base logarithm theorem.
The entry function
⌗
The last piece of the puzzle is the
entry
function:
Having read the
q
function, we can easily identify the obvious parts - guarding against the zero case, setting the results, pregenerating the fibonacci cache and calling the solver, so let’s ignore these parts for now:
Having analysed the
q
function, it’s fairly easy to guess that the block of code between initialisation of
m
and the first
/* SNIP */
is simply counting the amount of fibonacci numbers in the decomposition of input - it wasn’t really needed, but I did it only to precalculate the amount of space required in the result vector. Hopefully it added a little quirkiness to the code.
Given
k
k
k
, the decomposition of it is simply a pair of multisets
P
+
P_{+}
P
+
​
and
P
−
P_{-}
P
−
​
for which the following holds:
∑
i
∈
P
+
f
i
b
i
−
∑
i
∈
P
−
f
i
b
i
=
k
\sum_{i \in P_{+}}^{} fib_{i} - \sum_{i \in P_{-}}^{} fib_{i} = k
i
∈
P
+
​
∑
​
f
i
b
i
​
−
i
∈
P
−
​
∑
​
f
i
b
i
​
=
k
To justify my solution, I’m providing a few theorems that back it, but the proofs of them have been left as an exercise to the reader.
Assuming
A
=
P
−
∪
P
+
A = P_{-} \cup P_{+}
A
=
P
−
​
∪
P
+
​
and
m
m
m
as the multiplicity function, the multiset pair isn’t optimal if:
∃
i
i
∈
P
−
∧
i
∈
P
+
∃
n
∈
A
m
A
(
n
)
>
2
∃
i
∈
N
+
(
i
∈
P
+
∧
i
+
1
∈
P
+
)
∨
(
i
∈
P
+
∧
i
+
1
∈
P
−
)
∨
(
i
∈
P
−
∧
i
+
1
∈
P
+
)
∃
i
∈
N
+
i
∈
P
−
∧
i
+
2
∈
P
+
\mathop{\exists}\limits_{i}^{} i \in P_{-} \wedge i \in P_{+} \\
\mathop{\exists}\limits_{n \in A}^{} m_A (n) > 2 \\
\mathop{\exists}\limits_{i \in N_{+}}^{} \left(i \in P_{+} \wedge i + 1 \in P_{+}\right) \vee \left(i \in P_{+} \wedge i + 1 \in P_{-}\right) \vee \left(i \in P_{-} \wedge i + 1 \in P_{+}\right) \\
\mathop{\exists}\limits_{i \in N_{+}}^{} i \in P_{-} \wedge i + 2 \in P_{+}
i
∃
​
i
∈
P
−
​
∧
i
∈
P
+
​
n
∈
A
∃
​
m
A
​
(
n
)
>
2
i
∈
N
+
​
∃
​
(
i
∈
P
+
​
∧
i
+
1
∈
P
+
​
)
∨
(
i
∈
P
+
​
∧
i
+
1
∈
P
−
​
)
∨
(
i
∈
P
−
​
∧
i
+
1
∈
P
+
​
)
i
∈
N
+
​
∃
​
i
∈
P
−
​
∧
i
+
2
∈
P
+
​
It is known that:
∀
n
∈
N
+
∃
P
−
,
P
+
(
∑
i
∈
P
+
f
i
b
i
−
∑
i
∈
P
−
f
i
b
i
=
n
)
∧
(
∀
i
∈
A
m
A
(
i
)
=
1
)
f
i
b
n
≤
k
≤
f
i
b
n
+
1
⟹
∃
P
−
,
P
+
∀
m
∈
A
m
≤
n
+
1
f
i
b
n
≤
k
≤
f
i
b
n
+
1
⟹
∃
P
−
,
P
+
(
∑
i
∈
P
+
f
i
b
i
−
∑
i
∈
P
−
f
i
b
i
=
n
)
∧
n
∈
P
+
∧
n
+
1
∈
P
+
f
i
b
n
≤
k
≤
f
i
b
n
+
1
∧
k
−
f
i
b
n
≤
f
i
b
n
+
1
−
k
⟹
∃
P
−
,
P
+
(
∑
i
∈
P
+
f
i
b
i
−
∑
i
∈
P
−
f
i
b
i
=
n
)
∧
n
∈
P
+
f
i
b
n
≤
k
≤
f
i
b
n
+
1
∧
k
−
f
i
b
n
>
f
i
b
n
+
1
−
k
⟹
∃
P
−
,
P
+
(
∑
i
∈
P
+
f
i
b
i
−
∑
i
∈
P
−
f
i
b
i
=
n
)
∧
n
+
1
∈
P
+
\mathop{\forall}\limits_{n \in N_{+}}^{} \mathop{\exists}\limits_{P_{-}, P_{+}}^{} \left( \sum_{i \in P_{+}}^{} fib_{i} - \sum_{i \in P_{-}}^{} fib_{i} = n \right) \wedge \left(\mathop{\forall}\limits_{i \in A}^{} m_A (i) = 1\right) \\
fib_n \leq k \le fib_{n+1} \implies \mathop{\exists}\limits_{P_{-}, P_{+}}^{} \mathop{\forall}\limits_{m \in A}^{} m \leq n + 1 \\
fib_n \leq k \le fib_{n+1} \implies \mathop{\exists}\limits_{P_{-}, P_{+}}^{} \left( \sum_{i \in P_{+}}^{} fib_{i} - \sum_{i \in P_{-}}^{} fib_{i} = n \right) \wedge n \in P_{+} \wedge n + 1 \in P_{+} \\
fib_n \leq k \le fib_{n+1} \wedge k - fib_n \leq fib_{n+1} - k \implies \mathop{\exists}\limits_{P_{-}, P_{+}}^{} \left( \sum_{i \in P_{+}}^{} fib_{i} - \sum_{i \in P_{-}}^{} fib_{i} = n \right) \wedge n \in P_{+} \\
fib_n \leq k \le fib_{n+1} \wedge k - fib_n \gt fib_{n+1} - k \implies \mathop{\exists}\limits_{P_{-}, P_{+}}^{} \left( \sum_{i \in P_{+}}^{} fib_{i} - \sum_{i \in P_{-}}^{} fib_{i} = n \right) \wedge n + 1 \in P_{+}
n
∈
N
+
​
∀
​
P
−
​
,
P
+
​
∃
​
​
i
∈
P
+
​
∑
​
f
i
b
i
​
−
i
∈
P
−
​
∑
​
f
i
b
i
​
=
n
​
∧
(
i
∈
A
∀
​
m
A
​
(
i
)
=
1
)
f
i
b
n
​
≤
k
≤
f
i
b
n
+
1
​
⟹
P
−
​
,
P
+
​
∃
​
m
∈
A
∀
​
m
≤
n
+
1
f
i
b
n
​
≤
k
≤
f
i
b
n
+
1
​
⟹
P
−
​
,
P
+
​
∃
​
​
i
∈
P
+
​
∑
​
f
i
b
i
​
−
i
∈
P
−
​
∑
​
f
i
b
i
​
=
n
​
∧
n
∈
P
+
​
∧
n
+
1
∈
P
+
​
f
i
b
n
​
≤
k
≤
f
i
b
n
+
1
​
∧
k
−
f
i
b
n
​
≤
f
i
b
n
+
1
​
−
k
⟹
P
−
​
,
P
+
​
∃
​
​
i
∈
P
+
​
∑
​
f
i
b
i
​
−
i
∈
P
−
​
∑
​
f
i
b
i
​
=
n
​
∧
n
∈
P
+
​
f
i
b
n
​
≤
k
≤
f
i
b
n
+
1
​
∧
k
−
f
i
b
n
​
>
f
i
b
n
+
1
​
−
k
⟹
P
−
​
,
P
+
​
∃
​
​
i
∈
P
+
​
∑
​
f
i
b
i
​
−
i
∈
P
−
​
∑
​
f
i
b
i
​
=
n
​
∧
n
+
1
∈
P
+
​
These theorems allow us to define the computational complexity of the decomposition length checking function as
O
(
log
⁡
n
)
O(\log n)
O
(
lo
g
n
)
.
The final part of the code that begs for an analysis follows:
We notice that
m
is the size of the fibonacci cache, so this formula must determine the count of fibonacci numbers smaller or equal to
input
. Let’s use meaningful function names here:
Let’s start with Binet’s formula, and then try to find the formula for the index of a given fibonacci number.
F
n
=
ϕ
n
−
(
−
ϕ
)
−
n
5
n
=
log
⁡
ϕ
(
5
(
y
+
1
2
)
)
n
=
log
⁡
10
(
5
(
y
+
1
2
)
)
log
⁡
10
ϕ
n
=
log
⁡
10
5
+
log
⁡
10
(
y
+
1
2
)
log
⁡
10
ϕ
n
≈
0.34948500216
+
log
⁡
10
(
y
+
1
2
)
0.20898764025
F_{n} = \frac{\phi^n - {(-\phi)}^{-n}}{\sqrt{5}} \\
n = \log_{\phi} (\sqrt{5} (y + \frac{1}{2})) \\
n = \frac{\log_{10} (\sqrt{5} (y + \frac{1}{2}))}{\log_{10} \phi} \\
n = \frac{\log_{10} \sqrt{5} + \log_{10} (y + \frac{1}{2})}{\log_{10} \phi} \\
n \approx \frac{0.34948500216 + \log_{10} (y + \frac{1}{2})}{0.20898764025} \\
F
n
​
=
5
​
ϕ
n
−
(
−
ϕ
)
−
n
​
n
=
lo
g
ϕ
​
(
5
​
(
y
+
2
1
​
))
n
=
lo
g
10
​
ϕ
lo
g
10
​
(
5
​
(
y
+
2
1
​
))
​
n
=
lo
g
10
​
ϕ
lo
g
10
​
5
​
+
lo
g
10
​
(
y
+
2
1
​
)
​
n
≈
0.20898764025
0.34948500216
+
lo
g
10
​
(
y
+
2
1
​
)
​
Obviously,
input
might not be a fibonacci number in our case, but I’ve performed tests that show that this approximation coupled with rounding up the result are good enough to work without problems.
Having seen how this formula was made provokes a thought that in the end, I could have just let the logarithm function be
log
⁡
n
\log n
lo
g
n
instead of
log
⁡
10
n
\log_{10} n
lo
g
10
​
n
, and then used base
e
e
e
throughout my Binet’s formula transformation. Since the contest was
code guessing
, I wanted to make my code as obfuscated as possible, and I figured out that
log
⁡
10
n
\log_{10} n
lo
g
10
​
n
could be trickier to figure out. Also it introduced a new, menacing constant, so it was good enough.
