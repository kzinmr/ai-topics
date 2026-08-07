---
title: "Calculating log(1000!)"
url: "https://www.johndcook.com/blog/2026/08/06/log1000/"
fetched_at: 2026-08-07T10:19:27.468410+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Calculating log(1000!)

Source: https://www.johndcook.com/blog/2026/08/06/log1000/

The
previous post
pointed out that the following code such as the following unexpectedly works.
>>> from math import log, factorial
>>> log(factorial(1000))
5912.128178488163
If you don’t find this unexpected, note that if you replace
math.log
with
numpy.log
the code will fail [1]. Functions like natural logarithm operate on real numbers. Real numbers are represented as floating point numbers in programming languages, and 1000! factorial is too large to represent as a standard floating point number. (More on that
here
.)
In this post I’d like to look at how you might calculate log(1000!) with less capable software, and even without software.
One approach would be to sum the logarithms of the numbers 1 through 1000. This will give essentially the same result as above, with a little difference in the last couple decimal places due to rounding error.
If you have a way to calculate 1000! but not a way to cast it to a floating point number, you could do this manually.
>>> s = str(factorial(1000))
>>> s[:16]
'4023872600770937'
>>> len(s)
2568
This tells us 1000! = 4.023872600770937 × 10
2567
. Therefore
log(1000!) = log(4.023872600770937) + 2567 log(10)
which only requires working with numbers of modest size.
Calculating by hand
Now suppose it’s 1964. You don’t have a computer, or even a calculator, but you do have a copy of the recently published Handbook of Mathematical Functions by Abramowitz and Stegun (A&S). You turn to Table 6.6 “Factorials for large arguments.” This has values of factorial for 100, 200, 300, …, 1000, so you can simply look up your answer to 20 decimal places.
That was too easy; I didn’t expect that to be there when I started writing this post. If you wanted to compute log(950!), for example, you’d have to work harder. You could find A&S equation 6.1.41 (Stirling’s series) which says
So how would you use this formula to calculate log(1000!)? Since
n
! = Γ(
n
+ 1), you set
z
= 1001.
You’d need to decide how many terms you need to use. Assuming the error is on the order of the first term you leave out, you’d reason that you could probably stop with the 1/12
z
term because the next term is between 10
−11
and 10
−12
.
You find Table 4.2 has natural logarithms, but not for 1001. You can look up log(1.001), however, and at the bottom of the same page is log(10) to 16 decimal places, and you can find log(10) to 24 decimal places in Table 1.1. So you calculate
log(1001) = log(1.001 × 10³) = log(1.001) + 3 log(10).
You can find log(2) and log(π) in Table 1.1, and average them to find ½ log(2π).
Here’s Python code to simulate the hand calculations.
log2     = 0.6931_47180_55994_53094_172321 # Table 1.1
log10    = 2.3025_85092_99404_56840_179915 # Table 1.1
logpi    = 1.1447_29885_84940_01741_43427  # Table 1.1
log1_001 = 0.00099_95003_330835            # Table 4.2

z = 1001
logz = log1_001 + 3*log10
s = (z - 0.5)*logz - z + (log2 + logpi)/2 + 1/(12*z)

print(s)
This result differs from the one at the top of the post only in the last decimal place.
Related posts
Doing calculations with tables is not as simple as “just look it up.” It takes a bit of skill.
[1] The code will also fail if you replace
math.log
with
math.cos
. Both logarithm and cosine return moderate sized real numbers when given enormous inputs like 1000!, so representing the output as a float is not the problem. But logarithms of huge numbers can be computed with ordinary precision functions, as above. But computing the cosine of a huge number requires extended precision.
