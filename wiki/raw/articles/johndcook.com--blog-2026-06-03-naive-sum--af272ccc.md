---
title: "Naively summing an alternating series"
url: "https://www.johndcook.com/blog/2026/06/03/naive-sum/"
fetched_at: 2026-06-04T07:01:37.846156+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Naively summing an alternating series

Source: https://www.johndcook.com/blog/2026/06/03/naive-sum/

Suppose you run across the power series for the exponential function and decide to code it up. Good idea: you’ll probably learn something, though maybe not what you expect.
Maybe you decide a tolerance of 10
−12
is good enough, and so you sum the terms until the next term to add is below the tolerance.
from math import factorial, exp

def naive_exp(x):
    tolerance = 1e-12
    s = 0
    n = 0
    while True:
        delta = x**n / factorial(n)
        s += delta
        if abs(delta) < tolerance:
            return s
        n += 1
You want to try your program out, so you compute
e
by calling the function at 1. If you compare this to calling
exp(1)
you find that you got all the digits correct.
Now you try computing exp(-20). Calling
naive_exp(-20)
gives
5.47893091802112e-10
but calling
exp(-20)
gives
2.061153622438558e-09
Don’t brush things like this as flukes or compiler bugs [1]. This is your golden opportunity to learn something.
Maybe you add a print statement to see the intermediate values of the sum stored in the variable
s
. If you do, you’ll see that the partial sums oscillate wildly before settling down.
Maybe that seems wrong, but then you look more carefully at the series. The
n
th term is
x
n
/
n
!. Since
x
is negative, the terms alternate in sign. And the absolute values of the term get bigger before they get smaller. When
x
= −20, each numerator is 20 times larger than the previous, and each denominator is
n
times larger than the previous. So the terms will get bigger until
n
> 20. So the wild oscillations are real, not a bug.
The largest partial sum is 21822593.77927747 in absolute value. You know that exp(−20) is a very small number, so there’s going to have to be a lot of cancellation before the partial sums settle down to a small number. Maybe you’ve heard that cancellation is where numerical calculations lose precision. If not, now you know!
Look again at the largest partial sum. There are eight figures to the right of the decimal point. The code is printing out results to as much precision as it has, so the error at this point is on the order of 10
−8
. We’re trying to compute a number on the order of 10
−9
, and if
any
digits in our result are correct, it would be a coincidence.
If you go back and try your code on
x
= −22, the result is even worse, giving a negative result for a quantity that for theoretical reasons cannot be negative. But you can see why: you’re asking the code to compute a number that is closer to zero than the accuracy of the code.
Computers don’t represent numbers in base 10 internally, but the argument above is sufficient in this case. If you want to dig deeper, look into the
anatomy of a floating point number
.
There is a simple way around the problem above, but discovering it sooner would short-circuit the learning process. You could calculate exp(−20) as 1/exp(20) and avoid all the cancellation because the series for exp(20) does not alternate.
[1] Compilers do have bugs occasionally, but it’s orders of magnitude more likely that something is wrong with your code.
