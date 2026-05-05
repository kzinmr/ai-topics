---
title: "Faster comparison modulo α-equivalence"
url: "https://purplesyringa.moe/blog/./faster-comparison-modulo-alpha-equivalence/"
fetched_at: 2026-05-05T07:02:09.162442+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# Faster comparison modulo α-equivalence

Source: https://purplesyringa.moe/blog/./faster-comparison-modulo-alpha-equivalence/

Faster comparison modulo α-equivalence
November 30, 2025
This article is a technical counterpart of my previous post
Finding duplicated code with tools from your CS course
. It is deliberately written in a terse manner, and I’m not going to hold your hand. Consider reading the previous post first and coming back here later.
Introduction
Given a
λ
-calculus term, suppose we want to find all of its
α
-equivalent subterms. Terms
t
1
and
t
2
are considered
α
-equivalent (denoted as
t
1
∼
t
2
in this article) if they are syntactically equal up to a bijection between their bound variables. For example,
t
1
=
λ
x
.
a
x
and
t
2
=
λ
y
.
a
y
are
α
-equivalent because the bijection
{
x
↦
y
}
translates
t
1
to
t
2
, and
t
1
=
λ
x
.
a
x
and
t
2
=
λ
x
.
b
x
are not
α
-equivalent because
a
and
b
are free in
t
1
and
t
2
respectively.
Terms are
α
-equivalent if and only if their
locally nameless
forms are syntactically equal. The locally nameless form of a term
t
represents variables free in
t
by name, and variables bound in
t
by de Bruijn index. For example,
λ
x
.
a
x
is represented as
λ
.
a
1
. While computing the locally nameless form of a single term is straightforward, efficiently computing forms of all subterms of a term is tricky, since whether a variable is free or bound depends on the term whose form is being computed.
This article describes:
A linear-time algorithm for computing hashes of subterms up to
α
-equivalence, i.e. hashes of their locally nameless forms. We prove a bound on the collision rate of non-
α
-equivalent subterms.
A linear-time algorithm for validating the resulting hashes for lack of collisions. Together with 1., this produces a reliable classification algorithm with expected linear runtime.
An algorithm for computing
α
-equivalence classes in
𝒪
(
n
log
⁡
n
)
guaranteed time, as a deterministic alternative to 1.+2.
Over the course of the article, we use Python-like pseudocode. A common pattern in the pseudocode is using
dict[...]
to associate temporary data with terms or variables. This should be read as using linear arrays addressed by unique term/variable indices, or alternatively ad-hoc fields in data types, as opposed to a hash table access.
Prior art
Our first algorithm is an adaptation of the algorithm developed in:
Krzysztof Maziarz, Tom Ellis, Alan Lawrence, Andrew Fitzgibbon, and Simon Peyton Jones. 2021.
Hashing modulo alpha-equivalence
. In Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation (PLDI 2021). Association for Computing Machinery, New York, NY, USA, 960–973.
https://doi.org/10.1145/3453483.3454088
Maziarz et al.'s algorithm has
𝒪
(
n
log
2
⁡
n
)
runtime, but can be straightforwardly adjusted to expected
𝒪
(
n
log
⁡
n
)
time by replacing binary trees with hash tables. Crucially, this algorithm allows hashes to be computed
incrementally
. It achieves this by producing
e-summaries
, which represent the entire contents of a term up to
α
-equivalence, and efficiently combining e-summaries in application terms. We believe this “purely functional” approach does not allow for faster algorithms, so our algorithm expects the entire expression to be provided upfront.
To the best of our knowledge, our algorithm for validating hashes is novel.
The third algorithm is an adaptation of:
Lasse Blaauwbroek, Miroslav Olšák, and Herman Geuvers. 2024.
Hashing Modulo Context-Sensitive α-Equivalence
. Proc. ACM Program. Lang. 8, PLDI, Article 229 (June 2024), 24 pages.
https://doi.org/10.1145/3656459
Our algorithm has the same asymptotic complexity as described in the paper, but is adjusted to non-context-sensitive
α
-equivalence and simplified, which hopefully leads to easier intuitive understanding and faster practical performance. To guarantee deterministic
𝒪
(
n
log
⁡
n
)
time, we replace hash consing with an approach similar to:
Michalis Christou, Maxime Crochemore, Tomáš Flouri, Costas S. Iliopoulos, Jan JanoušEk, BořIvoj Melichar, and Solon P. Pissis. 2012. Computing all subtree repeats in ordered trees. Inf. Process. Lett. 112, 24 (December, 2012), 958–962.
https://doi.org/10.1016/j.ipl.2012.09.001
Hashing
We start with a named form, where all variables are accessed by names. This ensures that the innermost terms are already in the locally nameless form. We then compute the locally nameless forms of other terms recursively:
repr
(
x
)
=
x
repr
(
t
1
t
2
)
=
repr
(
t
1
)
repr
(
t
2
)
repr
(
λ
x
.
t
)
=
λ
.
repr
(
t
)
[
x
:
=
0
]
[
x
:
=
0
]
denotes that the form of
λ
x
.
t
is computed from the form of
t
by replacing mentions of
x
with de Bruijn indices. This replacement is the crux of the problem: while it can be easily performed on strings, the (possibly very long) strings then need to be rehashed on each iteration, since we want to compute the hash of each term.
However, some string hashes, most commonly rolling hashes, allow the hash to be recomputed efficiently if part of the string is changed. Adjusting
repr
to return such a hash allows the rewrite
[
x
:
=
0
]
to be performed directly on the hash. Consider in particular the polynomial hash parameterized by a constant
b
, chosen randomly, and a prime number
p
:
hash
(
c
0
c
1
…
c
n
−
1
)
=
∑
i
c
i
b
i
mod
p
.
A character at index
i
can be changed from
x
to
y
by adding
(
y
−
x
)
b
i
to the hash value. The hash of
λ
.
repr
(
t
)
and the “patch” replacing each mention of
x
with a de Bruijn index can be computed separately and then merged at the abstraction, since the offset of a given variable mention within the corresponding abstraction can be calculated efficiently, and patches can be merged by adding them together.
An implementation of the algorithm is reproduced below. To avoid handling parentheses, we implicitly translate terms to postfix notation, denoting calls with
!
.
range_of_expr:
dict
[Expr,
tuple
[
int
,
int
]] = {}
variable_nesting:
dict
[VariableName,
int
] = {}
variable_accesses:
dict
[VariableName,
list
[
tuple
[
int
,
int
]]] = {}
current_location:
int
=
0
def
collect_locations
(
expr: Expr, nesting:
int
):
global
current_location
    start = current_location
match
expr:
case
Variable(x):
            
            current_location +=
1
variable_accesses[x].append((start, nesting - variable_nesting[x]))
case
Abstraction(x, body):
            
            variable_nesting[x] = nesting
            variable_accesses[x] = []
            collect_locations(body, nesting +
1
)
            current_location +=
1
case
Application(f, a):
            
            collect_locations(f, nesting)
            collect_locations(a, nesting)
            current_location +=
1
end = current_location
    range_of_expr[expr] = (start, end)

collect_locations(root,
0
)

powers_of_b:
list
[
int
] = [
1
]
def
shift
(
h:
int
, count:
int
) ->
int
:
while
len
(powers_of_b) <= count:
        powers_of_b.append(powers_of_b[-
1
] * b % p)
return
h * powers_of_b[count] % p
def
hash_lambda
() ->
int
:
return
1
def
hash_call
() ->
int
:
return
2
def
hash_variable_name
(
x: VariableName
) ->
int
:
return
x.int_id *
2
+
3
def
hash_de_bruijn_index
(
i:
int
) ->
int
:
return
i *
2
+
4
def
calculate_hashes
(
expr: Expr
) ->
int
:
    start, end = range_of_expr[expr]
match
expr:
case
Variable(x):
            h = hash_variable_name(x)
case
Abstraction(x, body):
            h = calculate_hashes(body) + shift(hash_lambda(), end - start -
1
)
for
location, de_bruijn_index
in
variable_accesses[x]:
                h += shift(
                    hash_de_bruijn_index(de_bruijn_index) - hash_variable_name(x),
                    location - start,
                )
                h %= p
case
Application(f, a):
            h = (
                calculate_hashes(f)
                + shift(calculate_hashes(a), range_of_expr[a][
0
] - start)
                + shift(hash_call(), end - start -
1
)
            )
    h %= p
print
(
"The hash of"
, expr,
"is"
, h)
return
h

calculate_hashes(root)
Expand
The probabilistic guarantees of this scheme depend entirely on the choice of the hash. The collision probability of rolling hashes typically scales linearly with the length of the input. In this case, the length of the input exactly matches the number of subterms
n
, and each element of the input is a
log
⁡
n
+
𝒪
(
1
)
-bit number (assuming binary logarithm from now on).
For polynomial hashes, the collision probability is
≤
n
−
1
p
, assuming
b
is chosen randomly. If
b
is instead fixed and
p
is chosen randomly, the probability is
≤
C
n
log
⁡
n
p
, where
C
depends on how wide the range
p
is chosen from is. For Rabin fingerprints, the probability is
≲
n
log
⁡
n
2
deg
⁡
p
(
x
)
.
Since there are
n
(
n
−
1
)
2
possibly colliding pairs of terms, the probability of at least one collision among all terms is, for polynomial hashes, bounded from above by:
Verification
To verify that the computed hashes don’t produce collisions, we group terms by their hashes and validate that in each group of size
≥
2
, all terms are
α
-equivalent. We first check that terms within each group have equal sizes (i.e. the number of subterms, denoted
|
t
|
), and then iterate over groups in order of increasing size. This ensures that while validating terms of size
n
, terms of sizes
m
<
n
can be compared for
α
-equivalence by hash.
We now introduce some terminology.
We call subterms with non-unique hashes (i.e. subterms that are not alone in their groups)
pivots
.
We say an optimized predicate for
α
-equivalence is
sound
if it implies
α
-equivalence, and
complete
if it is implied by
α
-equivalence.
For a term
t
and a subterm
u
, we define the
path
from
t
to
u
(written
t
⇝
u
) as a (possibly empty) string of characters
↓
,
↙
,
↘
, where
↓
means “proceed into the body of the abstraction” and
↙
/
↘
mean “proceed into the function/argument of the application” respectively. For fixed
t
, valid paths map bijectively to subterms of
t
.
For a term
t
and a subterm
u
, we denote by
repr
(
u
/
t
)
a representation of
u
that encodes variable mentions as follows:
Variables bound in
u
use de Bruijn indices.
Variables free in
t
use names.
Variables bound in
t
but free in
u
use paths from
t
to the declaring abstraction.
Note that
repr
(
t
/
t
)
=
repr
(
t
)
. The act of writing
u
/
t
implicitly states that
u
is a subterm of
t
akin to
x
y
implying
y
≠
0
in arithmetic.
We write
e
1
∼
e
2
, where each
e
i
is either
u
i
or
u
i
/
t
i
independently, if
repr
(
e
1
)
=
repr
(
e
2
)
. For example,
x
/
λ
x
.
x
∼
y
/
λ
y
.
y
even though
x
≁
y
.
We rely on the following propositions:
If
u
1
∼
u
2
and
|
t
1
|
=
|
t
2
|
are distinct terms, then
u
1
/
t
1
∼
u
2
/
t
2
. Indeed,
repr
(
u
1
)
differs from
repr
(
u
1
/
t
1
)
at mentions of variables that are free in
u
1
but bound in
t
1
. But since
t
1
and
t
2
have the same size, they don’t share subterms, so
u
1
∼
u
2
implies
u
1
doesn’t mention any variables bound in
t
1
but not
u
1
. Hence
u
1
/
t
1
∼
u
1
∼
u
2
∼
u
2
/
t
2
.
If
u
1
/
t
1
∼
u
2
/
t
2
and there is a
u
1
′
∼
u
1
that isn’t a subterm of
t
1
, then
u
1
∼
u
2
. Indeed,
u
1
′
cannot mention variables declared within
t
1
, so
u
1
can also only mention free variables declared outside
t
1
, hence
u
2
can also only mention free variables declared outside
t
2
; thus
u
1
∼
u
1
/
t
1
∼
u
2
/
t
2
∼
u
2
.
If
u
∼
u
′
, then
u
/
t
∼
u
′
/
t
. Indeed,
repr
(
u
)
differs from
repr
(
u
/
t
)
at variables that are free in
u
, but bound in
t
. Such variables are accessed by name in
repr
(
u
)
, so by
u
∼
u
′
they must be accessed by the same name in
repr
(
u
′
)
and correspond to the same declaring abstraction
a
. Since the same
t
is used in
u
/
t
and
u
′
/
t
, the same path
t
⇝
a
will be used in both
repr
(
u
/
t
)
and
repr
(
u
′
/
t
)
.
If
u
/
t
∼
u
′
/
t
, then
u
∼
u
′
. Indeed,
repr
(
u
)
differs from
repr
(
u
/
t
)
at variables that are free in
u
, but bound in
t
. Since such variables are accessed by path in
repr
(
u
)
, by
u
∼
u
′
they must be accessed by the same path in
repr
(
u
′
)
. Since the same
t
is used in
u
/
t
and
u
′
/
t
, this path denotes the same abstraction
a
in both cases, and so
repr
(
u
)
and
repr
(
u
′
)
will include the same name (namely, the name of
a
).
If
u
1
/
t
1
∼
u
2
/
t
2
,
u
1
∼
u
1
′
, and
u
2
∼
u
2
′
, then
u
1
′
/
t
1
∼
u
2
′
/
t
2
. Indeed, by proposition 3 we have
u
1
′
/
t
1
∼
u
1
/
t
1
and
u
2
/
t
2
∼
u
2
′
/
t
2
, from which the statement follows by transitivity.
If
u
1
/
t
1
∼
u
2
/
t
2
,
u
1
′
/
t
1
∼
u
2
′
/
t
2
, and
u
1
∼
u
1
′
, then
u
2
∼
u
2
′
. Indeed, by proposition 3 we have
u
1
/
t
1
∼
u
1
′
/
t
1
, thus
u
2
/
t
2
∼
u
1
/
t
1
∼
u
1
′
/
t
1
∼
u
2
′
/
t
2
, from which by proposition 4
u
2
∼
u
2
′
.
If
t
1
∼
t
2
and
(
t
1
⇝
u
1
)
=
(
t
2
⇝
u
2
)
, then
u
1
/
t
1
∼
u
2
/
t
2
. Indeed,
repr
(
u
1
/
t
1
)
and
repr
(
u
2
/
t
2
)
are identical substrings of the string
repr
(
t
1
)
=
repr
(
t
2
)
.
If
t
1
∼
t
2
and
u
1
is a subterm of
t
1
, there exists a subterm
u
2
of
t
2
such that
u
1
/
t
1
∼
u
2
/
t
2
. Indeed, by
t
1
∼
t
2
the terms
t
1
and
t
2
have identical tree structure, so the path
t
1
⇝
u
1
is valid in both
t
1
and
t
2
. Rerooting it at
t
2
, we obtain an identical path
t
2
⇝
u
2
, and by proposition 7
u
1
/
t
1
∼
u
2
/
t
2
.
If a path
t
⇝
p
does not contain any pivots except
t
and
p
,
p
′
∼
p
is a distinct term from
p
, and a path
t
⇝
u
⇝
p
′
exists, where
u
is a pivot, then
p
is not a subterm of
u
. Indeed,
p
cannot be a strict subterm of
u
because
t
⇝
p
would contain another pivot
u
.
p
=
u
is also impossible, since
p
′
∼
p
would have to be a strict subterm of
p
due to
p
≠
p
′
, but a term can never be
α
-equivalent to its strict subterm.
To verify
t
1
∼
t
2
, where
t
1
and
t
2
are from the same group, we set
u
1
=
t
1
,
u
2
=
t
2
and assert
u
1
/
t
1
∼
u
2
/
t
2
recursively. At each step, we repeatedly verify that
u
1
and
u
2
are subterms of the same “kind” (variable/abstraction/application) and recurse, adjusting
u
1
and
u
2
accordingly. We apply two optimizations to ensure the time complexity is subquadratic. For every step except the first, if
u
2
is a pivot:
If
u
2
has an
α
-equivalent copy outside
t
2
, we immediately assert
u
1
∼
u
2
by hash and don’t recurse into
u
1
/
t
1
∼
u
2
/
t
2
. This is sound by proposition 1 and complete by proposition 2.
Otherwise, we look for copies of
u
2
within
t
2
(there must be at least one more copy). If this is the first copy we’ve seen during the current comparison, we recurse into
u
1
/
t
1
∼
u
2
/
t
2
and record the mapping
u
2
↦
u
1
. If there is an earlier copy
u
2
′
mapping to
u
1
′
, we assert
u
1
∼
u
1
′
by hash and don’t recurse. This is sound by proposition 5 and complete by proposition 6.
Note that in the latter case, if
u
2
is entered, it’s guaranteed to be the first copy in DFS order not only among visited terms, but among all terms. Indeed, suppose the earliest copy
u
2
′
was skipped because some of its ancestor pivots
p
wasn’t visited. There could be two reasons for that:
p
has a copy
p
′
outside
t
2
. By proposition 8, there exists
u
2
′
′
in
p
′
such that
u
2
′
/
p
∼
u
2
′
′
/
p
′
. Since
u
2
′
∼
u
2
and
u
2
is not a subterm of
p
, by proposition 2
u
2
′
∼
u
2
′
′
. Since
u
2
′
′
is outside
t
2
and
u
2
∼
u
2
′
′
,
u
2
could not be entered.
p
has an earlier copy
p
′
inside
t
2
. Repeat the process from the previous paragraph, finding
u
2
′
′
∼
u
2
. This
u
2
′
′
is earlier than
u
2
′
, so
u
2
′
could not be the earliest copy of
u
2
.
An implementation of this algorithm follows.
def
compare
(
u1: Term, t1: Term, u2: Term, t2: Term, h21:
dict
[
int
,
int
]
) ->
bool
:
if
(u2
is
not
t2)
and
(u2
is
a pivot):
if
there
is
any
term alpha-equivalent to u2 outside t2:
return
hash
[u1] ==
hash
[u2]
if
hash
[u2]
in
h21:
return
h21[
hash
[u2]] ==
hash
[u1]
        h21[
hash
[u2]] =
hash
[u1]
match
(u1, u2):
case
(Variable(x1), Variable(x2)):
            x1 = (x1
as
de Bruijn index)
if
x1 defined within t1
else
(x1
as
name)
            x2 = (x2
as
de Bruijn index)
if
x2 defined within t2
else
(x2
as
name)
return
x1 == x2
case
(Application(u11, u12), Application(u21, u22)):
return
compare(u11, t1, u21, t2, h21)
and
compare(u12, t1, u22, t2, h21)
case
(Abstraction(_, v1), Abstraction(_, v2)):
return
compare(v1, t1, v2, t2, h21)
case
_:
return
False
def
verify_hashes
():
for
class_members
in
classes:
        t1 = class_members[
0
]
for
t2
in
class_members[
1
:]:
if
not
compare(t1, t1, t2, t2, {}):
return
False
return
True
It turns out that this algorithm takes linear time. We will now prove this.
The pair
(
u
2
,
t
2
)
uniquely determines a particular invocation of
compare
. Split such invocations into two categories depending on whether the path
t
2
⇝
u
2
contains any pivots except
t
2
and possibly
u
2
. For visited pairs without such pivots,
u
2
determines
t
2
almost uniquely: if
u
2
is not a pivot,
t
2
is the closest pivot ancestor; otherwise it’s either such an ancestor or
u
2
itself. This means that the number of visited pairs without pivots inbetween is
≤
2
n
=
𝒪
(
n
)
. We will now prove that the number of visited pairs with pivots is also linear with amortized analysis.
Consider any path
t
2
⇝
u
2
that does contain an additional pivot. Call the highest such pivot
p
, so that
t
2
⇝
p
is non-empty and pivot-free except for
t
2
and
p
, and
p
⇝
u
2
is non-empty. Since
p
⇝
u
2
is non-empty, the pivot
p
must have been recursed into, which only happens if
p
has no copies outside
t
2
and is the earliest copy within
t
2
. Call the immediately next copy in DFS order
p
′
. Since
p
′
∼
p
,
p
′
and
p
have the same tree structure and we can find
u
2
′
such that
(
p
′
⇝
u
2
′
)
=
(
p
⇝
u
2
)
. We “pay” for entering the pair
(
u
2
,
t
2
)
with
u
2
′
and will now demonstrate that all visited pairs pay with different terms, which implies linearity.
Suppose that there are two pairs that pay with the same
u
′
:
(
u
1
,
t
1
)
with highest pivot
p
1
with next copy
p
1
′
, and
(
u
2
,
t
2
)
with highest pivot
p
2
with next copy
p
2
′
.
u
′
is a subterm of all of
t
1
,
t
2
,
p
1
′
,
p
2
′
, so there is a linear order on these four terms. Without loss of generality, assume
t
1
is an ancestor of
t
2
. There are three linear orders matching
t
1
≺
t
2
,
t
1
≺
p
1
′
,
t
2
≺
p
2
′
(note that we aren’t assuming that all terms in this order are distinct):
t
1
≺
t
2
≺
p
1
′
≺
p
2
′
. By proposition 9,
p
2
is not a subterm of
p
1
′
. By proposition 8, there is
q
such that
p
2
′
/
p
1
′
∼
q
/
p
1
. Since
p
2
∼
p
2
′
and
p
2
is not a subterm of
p
1
′
, by proposition 2
q
∼
p
2
′
. By proposition 9,
p
1
is not a subterm of
t
2
, thus
q
is not a subterm of
t
2
. This means that
p
2
could not be entered from
t
2
, since it has a copy
q
outside
t
2
.
t
1
≺
t
2
≺
p
2
′
≺
p
1
′
. By proposition 9,
p
1
is not a subterm of
t
2
or
p
2
′
. Since
p
1
is earlier than
p
1
′
in DFS order,
p
1
is also earlier than
t
2
. By proposition 8, there is
q
such that
p
1
′
/
p
2
′
∼
q
/
p
2
. Since
p
1
∼
p
1
′
and
p
1
is not a subterm of
p
2
′
, by proposition 2
q
∼
p
1
′
. Since
q
is in
t
2
, it is also later than
p
1
in DFS order. Since
p
2
is earlier than
p
2
′
,
q
is earlier than
p
1
′
. Thus
q
∼
p
1
is between
p
1
and
p
1
′
in DFS order, so
p
1
′
cannot be the immediately next copy of
p
1
.
t
1
≺
p
1
′
≺
t
2
≺
p
2
′
. By proposition 8, there are
q
and
q
′
such that
p
2
/
p
1
′
∼
q
/
p
1
and
p
2
′
/
p
1
′
∼
q
′
/
p
1
. By proposition 6,
q
∼
q
′
. Since
p
2
is earlier than
p
2
′
in DFS order,
(
p
1
′
⇝
p
2
)
=
(
p
1
⇝
q
)
, and
(
p
1
′
⇝
p
2
′
)
=
(
p
1
⇝
q
′
)
,
q
is earlier than
q
′
in DFS order. Together with
q
∼
q
′
, this implies
q
′
could not be entered from
t
1
. However, the path
p
1
′
⇝
u
′
passes through
p
2
′
, so the rerooted path
p
1
⇝
u
1
passes through
q
′
, and thus
q
′
has to be entered for
u
1
to be reached.
This proves that the mapping
(
t
2
,
u
2
)
↦
u
′
is injective, and thus this part of the algorithm takes at most linear time, which proves the linear complexity of the entire algorithm.
Notes:
The algorithm is linear even under the presence of collisions. The mapping
(
t
2
,
u
2
)
↦
u
′
will be defined over a smaller set of pairs than with perfect hashes, since the algorithm will abort at some point, but will stay injective.
The arguments
u
1
,
t
1
to
compare
are not taken into consideration during the proof.
compare
can be transformed to
serialize
, which lists non-entered terms as either hash values or backrefs, followed by an assertion that the serialized strings of all terms within a group are equal. This still takes linear time because the total string length is linear. This algorithm can resolve hash collisions locally by splitting groups in expected linear time, but is more complex and requires more memory.
The only reason a
serialize
-based algorithm needs to be pre-fed with hashes is to determine which terms are pivots – the exact hashes or even collisions between pivots are inconsequential. Pivots mostly matter because of the assumption that the path
t
⇝
p
does not contain other pivots. Hashing is an overkill, but we are not aware of any algorithm for detecting pivots without it.
Classes
The high-level overview of our deterministic algorithm for computing equivalence classes is as follows.
We start with the root term
t
and generate an auxiliary forest
F
of terms, where some variable accesses use names and others use indices, such that for each non-unique subterm
u
of
t
(i.e. a subterm that has an
α
-equivalent copy in
t
), there is a subtree
u
′
within
F
that syntactically matches the locally nameless form of
u
. For example, for
t
=
(
λ
x
.
x
x
)
(
λ
y
.
y
y
)
,
F
might contain three root terms:
(
λ
.
1
1
)
(
λ
.
1
1
)
,
x
, and
y
. Two distinct terms
u
1
,
u
2
are
α
-equivalent if and only if they both have
u
1
′
,
u
2
′
, and the corresponding subtrees
u
1
′
,
u
2
′
are equal. After
F
is built, we apply a general-purpose algorithm to compute syntactic equivalence classes of subtrees of
F
, and then lift those classes back to
t
.
The algorithms we propose build
F
in
𝒪
(
n
log
⁡
n
)
time, ensure
F
has
𝒪
(
n
log
⁡
n
)
nodes, and compute syntactic equivalence classes in
𝒪
(
|
F
|
)
=
𝒪
(
n
log
⁡
n
)
.
Our algorithm for building
F
is recursive. It receives a term
t
in a locally nameless representation (initially just the root term) and guarantees that all of its non-unique subterms will have locally nameless forms in
F
on exit.
We start by adding an exact copy
t
′
of
t
to
F
. We map
u
↦
u
′
for all
locally closed
subterms
u
of
t
, i.e. subterms that only access variables free in
t
or bound in
u
; this includes
t
itself, mapping
t
↦
t
′
. Among non-locally-closed subterms, we recognize that “large” subterms of size
|
u
|
≥
1
2
|
t
|
are guaranteed to be unique and don’t have to be mapped, since their
α
-equivalent copies could only be located within
t
, but there isn’t enough space within
t
for another subterm of matching size. This leaves “small” non-locally-closed subterms. To cover them, we adjust variable mentions so that the top-level subterms of this kind are in the locally nameless representation and recurse.
size:
dict
[Term,
int
] = {}
max_index:
dict
[Term,
int
] = {}
forest:
list
[Term] = []
term_to_node:
dict
[Term, Term] = {}
def
build_forest
(
t: Term
) ->
int
:
    t_prime = deep_copy(t)
    forest.append(t_prime)
    compute_term_properties(t)
    recurse(t, t_prime, size[t])
def
compute_term_properties
(
t: Term
):
match
t:
case
Variable(x):
            size[t] =
1
if
x
is
a de Bruijn index:
                max_index[t] = x
else
:  
                max_index[t] = -
1
case
Abstraction(x, u):
            compute_term_properties(u)
            size[t] =
1
+ size[u]
            max_index[t] = max_index[u] -
1
case
Application(t1, t2):
            compute_term_properties(t1)
            compute_term_properties(t2)
            size[t] =
1
+ size[t1] + size[t2]
            max_index[t] =
max
(max_index[t1], max_index[t2])
def
recurse
(
t: Term, t_prime: Term, root_size:
int
):
if
max_index[t] <
0
:  
        term_to_node[t] = t_prime
else
:
if
2
* size[t] < root_size:  
            build_forest(t)
return
match
(t, t_prime):
case
(Abstraction(x, u), Abstraction(_, u_prime)):
            replace_mentions(x)  
            recurse(u, u_prime, root_size)
case
(Application(u1, u2), Application(u1_prime, u2_prime)):
            recurse(u1, u1_prime, root_size)
            recurse(u2, u2_prime, root_size)

build_forest(root_t)
Expand
Since
|
t
|
is at worst halved during each recursive invocation, there are at most
log
⁡
n
levels of recursion. Excluding recursion, each invocation of
build_forest
takes
𝒪
(
|
t
|
)
time, which can be amortized as
𝒪
(
1
)
per subterm
u
of
t
. Since each
u
only takes part in
𝒪
(
log
⁡
n
)
recursive invocations, the total time complexity is
𝒪
(
n
log
⁡
n
)
, implying
|
F
|
=
𝒪
(
n
log
⁡
n
)
.
To calculate syntactic equivalence classes of subterms of
F
, we partition subterms by subtree size and iterate over groups in order of increasing size. Within each group, the equivalence classes of direct descendants of terms are already known, so each term can be associated with a short finite vector, such that syntactically equal terms have equal vectors. Further partitioning terms within the group by vectors using a radix sort-like approach produces subgroups corresponding to equivalence classes.
Term classes can then be populated from node classes.
term_classes:
dict
[Term,
int
] = {}
def
populate_term_classes
(
t: Term
):
if
t
in
term_to_node:
        term_classes[t] = node_classes[term_to_node[t]]
else
:  
        term_classes[t] = next_class
        next_class +=
1
match
t:
case
Abstraction(_, u):
            populate_term_classes(u)
case
Application(t1, t2):
            populate_term_classes(t1)
            populate_term_classes(t2)

populate_term_classes(root_t)
