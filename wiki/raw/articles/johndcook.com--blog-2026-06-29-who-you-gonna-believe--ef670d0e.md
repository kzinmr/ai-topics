---
title: "Who you gonna believe: Grok or the docs?"
url: "https://www.johndcook.com/blog/2026/06/29/who-you-gonna-believe/"
fetched_at: 2026-06-30T07:01:00.656699+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Who you gonna believe: Grok or the docs?

Source: https://www.johndcook.com/blog/2026/06/29/who-you-gonna-believe/

The calculator utility
bc
has a minimal math library. For example, there’s no tangent function because you’re expected take the ratio of sine and cosine. (The Gnu version of
bc
does have a function for tangent, but the POSIX version does not.) And yet
bc
includes support for Bessel functions
J
(
x
).
The
bc
function
j
takes two arguments. Is the first argument
n
or
x
? Grok said the function arguments are
j(n,x)
. I thought I should run
man bc
just to make sure, and it said
j(x, n) Returns the bessel integer order n (truncated) of x.
So Grok says
j(n,x)
and the documentation that ships with the software says
j(x,n)
. Which one should you believe? Neither! You should run a little test.
~$ bc -l
>>> j(1, 0)
0
>>> j(0, 1)
.76519768655796655144
Now
J
1
(0) = 0, so apparently the first argument is the order
n
. Grok was right and the man page was wrong.
As further confirmation, let’s see which argument is truncated.
>>> j(1.2, 3.4)
.17922585168150711099
>>> j(1, 3.4)
.17922585168150711099
>>> j(1.2, 3)
.33905895852593645892
The first argument is truncated to an integer value, so that’s the order
n
.
Turns out there’s a bug in the man page. The man page text above comes from running
man bc
on my Macbook. On my Linux box, the documentation is correct. It says
j(n,x) The Bessel function of integer order n of x.
The software produces the same results on both computers. It’s just a documentation bug.
The version running on my Macbook is the version that ships with the OS. It’s not the Gnu version, though the documentation says “This bc is compatible with both the GNU bc and the POSIX bc spec.” It has a function
t
for tangent, for example, which a POSIX version does not. But if you run
bc --standard -l
attempting to call
t
produces an error.
