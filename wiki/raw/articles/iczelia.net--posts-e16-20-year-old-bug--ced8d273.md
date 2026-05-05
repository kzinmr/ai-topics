---
title: "Fixing a 20-year-old bug in Enlightenment E16."
url: "https://iczelia.net/posts/e16-20-year-old-bug/"
fetched_at: 2026-05-05T07:01:18.171526+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Fixing a 20-year-old bug in Enlightenment E16.

Source: https://iczelia.net/posts/e16-20-year-old-bug/

The editor in chief of this blog was born in 2004. She uses the 1997 window manager,
Enlightenment E16
, daily. In this article, I describe the process of fixing a show-stopping, rare bug that dates back to 2006 in the codebase. Surprisingly, the issue has roots in a faulty implementation of Newton’s algorithm.
Introduction
⌗
Some may find it weird, but I actually greatly enjoy using Enlightenment E16 as my window manager. It’s themable, hackable, lightweight (24MB peak RSS!), amenable to heavy keyboard users like myself, and most importantly - it looks goregous:
E16 first came to be in 1997, thanks to Carsten Haitzler, and it has been in development ever since. Most have moved to E17 and other newer versions; a community of hardcore enthusiasts still uses E16, and I am one of them. The codebase is quite old, and it has accumulated a lot of technical debt over the years.
Bugs always come out of the woodworks in a time scramble and this one likely sensed a prime opportunity: I was doing a lot of last-minute work on a couple of slides for a course that I will be teaching. I had a couple of PDFs with lecture slides and an exercise sheet typeset in LaTeX. At some point, I opened one of them in Atril, and the entire desktop froze.
The bug
⌗
I killed the X11 session from a TTY. Sadly, the hang was deterministic: every time I opened that specific PDF.
Attaching gdb to the live process showed every sample parked in imlib2’s
font cache, under the same e16 caller:
#0  __strcmp_evex ()
#1  __imlib_hash_find (hash=0x55bc9c111420, key="\001\001\001\001\001")     object.c:172
#2  __imlib_font_cache_glyph_get (fn=..., index=0)                          font_draw.c:30
#3  __imlib_font_get_next_glyph (... utf8="Kickoff.pdf — Introduction...")  font_main.c:218
#4  __imlib_font_query_advance (...)                                        font_query.c:89
#5  imlib_get_text_advance (...)                                            api_text.c:231
#6  Efont_extents (...)                                                     text_ift.c:87
#7  _ift_TextSize (...)                                                     text_ift.c:156
#8  TextstateTextFitMB (ts=..., textwidth_limit=291)                        text.c:350
#9  TextstateTextFit (...)                                                  text.c:559
#10 TextstateTextDraw (... text="Kickoff.pdf — Introduction...")            text.c:638
#11 ITApply (...)                                                           iclass.c:930
#12 ITApply (...)                                                           iclass.c:884
#13 _BorderWinpartITclassApply (ewin=..., i=2, force=1)                     borders.c:179
#14 EwinBorderUpdateInfo (ewin=...)                                         borders.c:300
#15 EwinChangesProcess (...)                                                ewins.c:2141
#16 EwinEventPropertyNotify (ewin=..., ev=...)                              ewins.c:1438
...
#21 main (...)                                                              main.c:320
Re-attaching repeatedly showed the program was not
deadlocked
.
__imlib_font_cache_glyph_get
was being called with different glyph indices (0, 20, 73, 81, 82, 87, 88, …) each time. So the inner font-measurement was making progress; the loop was somewhere outside it.
After some fudging, I found out that Frame 8 (
TextstateTextFitMB
at
text.c:350
) was the constant. That’s a
ts->ops->TextSize(ts, new_line, 0, pw, &hh, &ascent);
call inside the middle-ellipsis truncation loop that tries to fit a string into
textwidth_limit = 291
pixels by nuking characters out of the middle - used when rendering the title of the PDF, that happened to also be the title of the window, too long for the decoration to contain.
Dumping the frame’s locals across many samples revealed a clean two-state oscillation:
nuke_count = 8   nc2 = 36   wc_len = 81   len_n = 76
nuke_count = 11  nc2 = 35   wc_len = 81   len_n = 73
nuke_count = 8   nc2 = 36   wc_len = 81   len_n = 76
...
I always saw two trial truncations, forever, same text each time.
The problematic function
⌗
We start at the lowest common denominator - there is likely a logic bug here.
The loop is of paticular interest to us. Abridged:
This is a Newton-style search that estimates how many more/fewer wchars to nuke based on how far off
width
is from
textwidth_limit
, using
cw = width / len_n
as the derivative (average pixels per char). Seeing clever and crafty solutions like this is delightful. But to anyone who has ever implemented Newton’s method, this code screams something obvious:
“Where is your iteration limit?!”
. Newton’s method can fail to converge, and it can also overshoot and diverge - all depending on the starting point, the nature of the function, and the quality of the derivative estimate. In this case, the method was oscillating between two points forever.
To make matters worse, the exit tolerance (
ε
\varepsilon
ε
) is tight - accept only
nc2
between
[0, 3*cw)
. This also explains why ordinary short titles never tripped it - on shorter strings or with wider
cw
, the
<= 2*cw
branch kicks in and the step becomes 1, which converges.
The fix
⌗
I have made three defensive changes, applied symmetrically to both the multi-byte and ASCII loops:
Capped iteration counts at 32. Past the cap, if the current trial fits
nc2 >= 0
we just accept it; otherwise bump
nuke_count
by 1 and retry. This guarantees termination in bounded time and picks the first fitting trial once the Newton step has been shown to oscillate.
We now floor
nuke_count
at 1 inside the loop, so a negative correction can never produce the degenerate tail-overlaps-head string.
Floor
cw
at 1, so a pathological zero-width measurement cannot turn the step formulas into a divide-by-zero.
Patch (against e16 1.0.30)
⌗
Reproducer
⌗
Any window whose WM_NAME is long enough that the middle-ellipsis search falls into the overshoot regime reproduces this. The one in the wild:
Kickoff.pdf — Introduction to Information Theory Session 1: kickoff & first topic
(81 wide chars including the em-dash, a ~291px border title slot, font roughly 3px/char average.)
A philosophical detour that nobody asked for.
⌗
Newer is not necessarily better. Fresh software carries brand new bugs for you and the maintainers to enjoy, now empowered by the barrier to contribute being much lower thanks to Large Language Models. But sometimes stable maintainers do absurdly dumb things too:
On the
3rd of April 2026, I remarked
that
fgetxattr(54321, NULL, NULL, 0);
apparently crashes yesterday’s 6.6.y lts kernel. A call that should just return
-1
and set
errno
to
EINVAL
because the path is invalid, but a stable maintainer
patched it out wholesale
.
Then, the awful commit
was reverted
, on the 8th of April. No CVE has been assigned despite an obvious Denial-Of-Service attack vector being introduced.
If this is what happens by mistake on a daily basis
, what happens when the supply chain is compromised and a malicious actor intentionally introduces a bug? The mind boggles. Back when the
XZ backdoor
was introduced, I was scrolling through news on my Debian Sid laptop with some code compiling in the background. I learned of a backdoor in XZ Utils, potentially introduced by a state actor in version v5.6.0. Thinking back to the fact that I do, indeed, run a bleeding edge distro and update often, I immediately ran
apt list --upgradable | grep xz-utils
. Sure enough, the stains on my laptop from the coffee I spat out through the nose
were pretty tough to deal with.
On the other hand, the amount of bugs in private checkouts of crusty old software maintained by competent developers will monotonically decrease. If I need a feature, I will implement it. If there is a problem, I only have myself to blame. There is no supply chain to compromise, and if a determined, targetted state actor wants
sudo
privileges on my machine - they will find a way to get it anyway. Oh, also, eI probably wasn’t going to use whatever features that my XFWM updates (the WM I used to use before!) were going to bring.
