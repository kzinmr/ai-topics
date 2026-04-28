---
title: "Ghostty Devlog 002"
url: "https://mitchellh.com/writing/ghostty-devlog-002"
fetched_at: 2026-04-28T07:02:40.861130+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty Devlog 002

Source: https://mitchellh.com/writing/ghostty-devlog-002

Hello! Welcome to the second official devlog for
Ghostty
👻!
We'll dive into the tech stuff in just a second, but I want to highlight
some updates on the non-tech side since there are a few really exciting
things to share!
First, I gave my first "talk" talking
about Ghostty in the public for
Handmade Boston
.
You can find the
Twitch VOD here (starts at 2:45:30)
.
The talk is more of a discussion around terminals in general, and doesn't
cover Ghostty specifically too much, but if you want to hear my philosophy
on terminals and why I started and continue to work on Ghostty, check it out.
Next, a couple community members have began working on a Ghostty website,
a public Discord (even if you're not in the beta), and a waitlist for joining
the beta. This is early times but all are going to be an important item
on the road to releasing this project. And, would be cool to meet and chat
with some of you until then!
As far as beta access... I'll have more to share maybe in the next devlog.
We're working on it. "We" because the Ghostty community is growing and
some community members are helping me prep to bring in more and more people.
Fun!
I've also been getting regularly asked what my plan is for releasing
Ghostty: will it be free, open source, etc.? Yes, yes yes! Ghostty will
be free and open source (both free as in free speech and free as in beer).
We haven't settled on a license yet, but I'm allowing the beta group to
make suggestions. We're leaning towards GPLv3 but haven't settled on anything
yet.
Non-Native Fullscreen on macOS (#215)
This feature was contributed by
Thorsten Ball
.
There is a feature amongst other macOS terminal emulators that is commonly
called "non-native fullscreen." This is easiest to demo visually. Below
is
native or traditional macOS fullscreen
:
And then here is the
new, non-native fullscreen
:
Both approaches have their own pros and cons, so this is a configurable
option in Ghostty. In particular, the non-native fullscreen is very fast,
allows other programs to be floated on top, and doesn't create a new
"Desktop." However, you can't access tabs (only splits) while in fullscreen
(until we write a custom tab bar controller, help wanted!).
It turns out implementing this was a doozy.
On the surface,
it really is very simple: you programmatically modify some window attributes.
If you Google around, the code samples to make this behavior happen are a
dozen lines or so. But the Ghostty PR was
+802/-239
. What?
If you've been following Ghostty, I very proudly talk about how
Ghostty
is written in Zig but uses SwiftUI for macOS GUI
.
Ghostty was 100% SwiftUI (for the GUI): the main entrypoint for
Ghostty.app
was a SwiftUI
App
object. The issue is that non-native fullscreen requires
subclassing
NSWindow
and with SwiftUI you just can't (or, nobody has publicly figured out how).
So, in order to make non-native fullscreen work, we had to rip out the
SwiftUI app and window lifecycle management and rewrite it ourselves using
plain old
AppKit
. Note:
we still use SwiftUI for the
views
, just not the window/app lifecycle
management.
This includes startup, multi-window creation, tab bars,
menu bar, etc.
If we just wanted non-native fullscreen, this probably wouldn't be worth it.
But, we already had some other bugs or missing features looming because
of SwiftUI and this gives us a path to fix all of them, so we decided it was
worth it. I'll share more on those improvements later, but let's just say
that Thorsten was able to delete a file named
CursedMenuManager.swift
and that's a good hint into the broader reason this was a good change.
So we have non-native fullscreen now! Cool! But we also have a much more
robust framework for building new macOS functionality, so this was a much
bigger win than it all seems on the surface. Thanks Thorsten!
Oh also, the
+802/-239
was 97% Swift. I respect that there's a lot
of people out there who really like Swift, but I'd much prefer
to be working in Zig. And Xcode is not great. Thorsten agrees. So
this feature was also not super fun for that reason, but we do the
things we do because we want the native macOS experience to be awesome.
Blurry Linux Fonts, Box Artifacts (#178, #204)
Almost 6 months ago, one of the earliest Ghostty testers reported
that they were seeing slightly blurry fonts and artifacts on Linux:
Note the above screenshot has two issues. First, the fonts are blurry. But
second, there should not be any blank lines under the box glyphs in the
NixOS logo. See my screenshot below for what it looked like on my machine
that didn't exhibit these issues.
I
use Linux heavily
and wasn't seeing any blurriness at all. I installed multiple distros
on multiple hardware devices and couldn't reproduce the issue. I even
got the exact OS config of the issue reporter and ran it as-is and couldn't reproduce this issue.
I noted that I had a suspicion this was a DPI issue but dropped it there.
I revisited the issue a few times over the following months but never quite
figured it out.
But then we got it.
Specifically,
Thorsten
figured it out. Sit around the campfire friends, because this is a very
important software engineering lesson on the insidious nature of float math
and float/int conversions.
DPI
handling in modern software
is a pain. For decades, displays had only a handful of possible DPIs and
everything was rendered without scaling ("1x"). Today, displays have highly
varying DPIs and they're so high that UIs are usually rendered with
scaling applied ("2x"). To make matters more complicated, fractional scaling
("1.25x") is also very common, nowadays.
Due to this, portable software usually asks for size configurations
(font, padding, etc.) in
points
.
Points
are generally 1/72 of an
inch
. DPI is
dots per inch
. GPU rendering works
in
pixels
. To convert points to pixels, we need to do some math:
pixels = (points * 72) / dpi
.
As it turns out, I had this hunch (earlier screenshot) months prior and I
audited all my DPI-based calculations and concluded they were all right. And,
they
almost were
. All of the calculations I did with font sizes and GPU (shader)
parameters were all correct: I handled rounding, precision, and integer
conversion (if necessary) correctly.
But there was one more feature that used points that I forgot to audit:
window padding. And the window padding calculation was wrong. And this wrong
answer would lead to padding being off by zero or one pixels (never more).
If it was off by even one pixel, you'd get blurriness. Oh. My. God.
Let's look at how it was wrong. Here is the previous padding calculation
(width only, the height calculation was the same but with
y
):
const
padding_x
:
f32
=
(config
.
@"window-padding-x"
*
x_dpi)
/
72
;
const
screen_width
:
u32
=
self
.
width
-|
@as
(
u32
,
@intFromFloat
(padding_x
*
2
))
;
Do you see it? Let me show you the solution, and maybe you'll see it:
const
padding_x
:
u32
=
@intFromFloat
(
@floor
(config
.
@"window-padding-x"
*
x_dpi
/
72
))
;
const
screen_width
:
u32
=
self
.
width
-|
(padding_x
*
2
)
;
The problem sequence:
The padding was computed as a float. If you had a DPI that didn't cleanly
divide by 72, you'd get a fractional padding. For example, if your DPI
is 125 and you used a padding of 2, you'd get a final pixel value of
3.333...
The screen width calculation converted the float to an int without
an opinion on rounding. This led to flooring, so following our
example you'd get
width - 3
. Note that 0.333... padding is missing now.
The screen width and padding are both sent to the GPU for rendering.
GPUs work in floating point values, so it honored the fractional pixel
value of 3.333... for the padding.
Of course, that has to be mapped to real pixels which aren't fractional
and the GPU would round
up
because it didn't want to lose any of your data.
But now the render is 1 pixel wider (0.3 rounded to 1) than the screen,
so it would apply a downscale operation.
Downscaling introduces anti-aliasing, which by definition blurs edges.
Hence, blurry fonts.
By instead rounding the padding down and simply using integral types throughout,
we never arrive at this scenario, avoid the anti-aliasing, and get pixel-perfect
rendering. 😅 Here is a super zoomed in before (left) and after (right):
This ultimately led to an audit of the entire codebase wherever we use the
@intFromFloat
built-in, and we did actually find one more scenario that had
a rounding error causing slight artifacts. Hard lesson learned.
In theory, this didn't only affect Linux users. In practice, Linux hardware
is more diverse and testers more regularly had DPIs that didn't cleanly
divide with the padding. But a macOS user who tweaked the padding settings
just right could've seen this behavior too.
The original "fix" was a 2-line change to add the
@floor
to padding
calculations. After thoroughly understanding the problem sequence as
described above, we decided that the
correct
solution was to change
all of our size data structures to use integers instead of floats, and
only convert integers to floats for the GPU, thus ensuring that only
non-fractional values are used. Screen sizes aren't fractional, padding
isn't fractional, grid dimensions aren't fractional, etc. So this is
also a lesson in using the right data type. Thorsten wrote about this
experience in a
newsletter entry on the value of truly understanding a bug
.
Fin
This concludes Ghostty devlog 002. This devlog was the
Thorsten
show! And I am so happy and thankful! Even though the beta group is still
only a couple dozen people, I'm really excited to see the Ghostty community
grow.
If you want to keep up to date, follow me on Twitter or Mastodon
(links in footer). This blog also has an
RSS feed
.
Boo. 👻
