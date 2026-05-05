---
title: "Fizz Buzz Through Monoids"
url: "https://entropicthoughts.com/fizzbuzz-through-monoids"
fetched_at: 2026-05-05T07:00:57.027761+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Fizz Buzz Through Monoids

Source: https://entropicthoughts.com/fizzbuzz-through-monoids

We have previously seen
the guard-sequence pattern
which sits at the core of
this implementation. The expression
In[3]:
"fizz"
<$
guard (rem i 3
==
0)
will evaluate to
Just "fizz"
whenever
i
is divisible by three, and in all
other cases it evaluates to
Nothing
. Thus, if a number is not divisible by any
of 3, 5, or 7, the list will evaluate to
In[4]:
[
Nothing
,
Nothing
,
Nothing
]
If a number is divisible by only 5, but not 3 or 7, the list will be
In[5]:
[
Nothing
,
Just
"buzz"
,
Nothing
]
And if a number is divisible by, say, 3 and 7, but not 5, the list
will be
In[6]:
[
Just
"fizz"
,
Nothing
,
Just
"zork"
]
These are smushed together by
mconcat
from the
Monoid
interface, which
applies the generic smushing operation
<>
over the list. This operation
behaves as expected for our strings-that-might-not-exist: it concatenates them
together if they do exist, otherwise it returns
Nothing
.
Whatever we get out of
mconcat
, we pass it to
fromMaybe (show i)
, which
replaces any
Nothing
values with the string representation of the number
coming into the function, but passes through any actual values it receives
intact. That is the full
fizzbuzz
function that converts a number to the
correct textual representation.
To make it an actual program, we loop through all numbers
[1..100]
, convert
them with
fizzbuzz
, and print the result.
