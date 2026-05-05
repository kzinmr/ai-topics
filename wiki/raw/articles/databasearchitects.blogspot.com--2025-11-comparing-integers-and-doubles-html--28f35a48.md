---
title: "Comparing Integers and Doubles"
url: "https://databasearchitects.blogspot.com/2025/11/comparing-integers-and-doubles.html"
fetched_at: 2026-05-05T07:01:27.967187+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Comparing Integers and Doubles

Source: https://databasearchitects.blogspot.com/2025/11/comparing-integers-and-doubles.html

During automated testing we stumbled upon a problem that boiled down to transitive comparisons: If a=b, and a=c, when we assumed that b=c. Unfortunately that is not always the case, at least not in all systems. Consider the following SQL query:
select
a
=
b,
a
=
c
,
b
=
c
from
(
values
(
1234567890123456789
.
0
::double
precision
,
1234567890123456788
::
bigint
,
1234567890123456789
::
bigint
))
s(a,b,
c
)
If you execute that in Postgres (or DuckDB, or SQL Server, or ...) the answer is (true, true, false). That is, the comparison is not transitive! Why does that happen? When these systems compare a bigint and a double, they promote the bigint to double and then compare. But a double has only 52 bits of mantissa, which means it will lose precision when promoting large integers to double, producing false positives in the comparison.
This behavior is highly undesirable, first because it confuses the optimizer, and second because (at least in
our system
) joins work very differently: Hash joins promote to the most restrictive type and discard all values that cannot be represented, as they will never produce a join partner for sure. For double/bigint joins that leads to observable differences between joins and plain comparisons, which is very bad.
How should we compare correctly? Conceptually the situation is clear, an IEEE 754 floating point with sign s, mantissa m, and exponent e represents the values (-1)^s*m*2^e, we just have to compare the integer with that value. But there is no easy way to do that, if we do a int/double comparison in, e.g., C++, the compiler does the same promotion to double, messing up the comparison.
We can get the logic right by doing two conversions: We first convert the int to double and compare that. If the values are not equal, the order is clear and we can use that. Otherwise, we convert the double back to an integer and check if the conversion rounded up or down, and handle the result. Plus some extra checks to avoid undefined behavior (the conversion of intmax64->double->int64 is not defined) and to handle non-finite values, and we get:
int
cmpDoubleInt64
(
double
a,
int64_t
b)
{
// handle intmax and nan
if
(
!
(a
<=
0x1.fffffffffffffp+62
))
return
1
;
// fast path comparison
double
bd
=
b;
if
(a
!=
bd)
return
(a
<
bd)
?
-1
:
1
;
// handle loss of precision
int64_t
ai
=
a;
if
(ai
!=
b)
return
(ai
<
b)
?
-1
:
1
;
return
0
;
}
Which is the logic that we now use. Who else does it correctly? Perhaps somewhat surprisingly,
Python
and
SQLLite
.  Other database systems (and programming languages) that we tested all lost precision during the comparison, leading to tons of problems. IMHO a proper int/double comparison should be available in every programming language, at least as library function. But in most languages (and DBMSes) it isn't. You can use that code above if you ever have this problem.
