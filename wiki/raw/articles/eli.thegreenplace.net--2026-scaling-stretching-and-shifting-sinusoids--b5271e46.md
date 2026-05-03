---
title: "Scaling, stretching and shifting sinusoids"
url: "https://eli.thegreenplace.net/2026/scaling-stretching-and-shifting-sinusoids/"
fetched_at: 2026-05-03T07:01:02.662962+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Scaling, stretching and shifting sinusoids

Source: https://eli.thegreenplace.net/2026/scaling-stretching-and-shifting-sinusoids/

May 02, 2026 at 07:17
Tags
Math
This is a brief and simple  explanation of how to adjust the
standard sinusoid
sin(x)
to change its amplitude, frequency and
phase shift. More precisely, given the general function:
\[s(x)=A\cdot sin(w\cdot x+\theta)\]
We’ll see how adjusting the parameters
,
and
affect the shape of
s(x)
. Each section below
covers one of these aspects mathematically, and you can use the demo at
the bottom to experiment with the topic visually.
Scaling
Scaling is conceptually the simplest change; we adjust
to
increase or decrease the amplitude (maximal height) of
s(x)
. Setting
A=2
will make the
value twice as large (in both the positive
and negative direction) as the original function.
Stretching
Stretching changes the frequency of
sin(x)
, which is inverse
proportional to its period. The baseline function
sin(x)
has a
period of
2\pi
, meaning it repeats every
2\pi
. In other
words,
sin(x)=sin(x+2\pi)
for any
.
If we set
w=2
, we get
sin(2x)
. This function repeats
itself twice as fast as
sin(x)
, because
is multiplied
by 2 before being fed into the sinusoid. If
changes by
\pi
, the sinusoid’s input changes by
2\pi
.
Therefore, the period of
sin(2x)
is
\pi
, the period of
sin(4x)
is
\frac{\pi}{2}
and so on.
More generally, the period of
sin(wx)
is
\frac{2\pi}{w}
.
Play with the demo below to see this in action, by changing
and observing how the waveform changes.
If we know the period
p
we want, we can easily calculate the
that gives us this period:
\[p=\frac{2\pi}{w} \implies w=\frac{2\pi}{p}\]
Shifting
The final parameter we discuss is
; it’s called the
phase
of the sinusoid. In the baseline
sin(x)
,
. The sinusoid is 0 at
x=0
, achieves its
positive peak at
x=\frac{\pi}{2}
, crosses 0 again at
x=\pi
, negative peak at
x=\frac{3\pi}{2}
and returns to
its original position at
x=2\pi
where the repetition begins.
By adding a non-zero
, we don’t affect the sinusoid’s
amplitude or frequency, but we do shift it right or left along the
axis. For example, suppose we use the function
sin(x+\theta)
with
\theta=\frac{\pi}{2}
. Then when
x=0
, we have
sin(\frac{\pi}{2})
, so the sinusoid is
already at its positive peak; at
x=\frac{\pi}{2}
, the sinusoid
crosses 0 into the negatives, etc. Everything happens earlier (by
exactly the value of
\theta=\frac{\pi}{2}
) than in the baseline
sinusoid. In other words, we’ve shifted the function
left
by
\frac{\pi}{2}
. Similarly, when
is negative,
everything happens later, and the function is shifted
right
.
Putting it all together
We’ve now gone over all the parameters for the function:
\[s(x)=A\cdot sin(w\cdot x+\theta)\]
controls the scaling factor (amplitude).
is the frequency and controls the repetition period
controls the phase - how much the sinusoid is shifted
left or right
Use the demo below to adjust these parameters and observe their effect on
the sinusoid:
Your browser does not support the HTML5 canvas tag.
