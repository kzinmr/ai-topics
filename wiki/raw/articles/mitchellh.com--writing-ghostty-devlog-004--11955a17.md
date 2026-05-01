---
title: "Ghostty Devlog 004"
url: "https://mitchellh.com/writing/ghostty-devlog-004"
fetched_at: 2026-05-01T07:02:03.325241+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty Devlog 004

Source: https://mitchellh.com/writing/ghostty-devlog-004

Hello! Welcome to the fourth official devlog for
Ghostty
👻!
Last week, I shared our
public Discord server
and I also
gave a talk on Ghostty and Zig
.
If you missed either of those, please check it out. I distribute new beta
invites through the Discord community. Also, our Discord community has grown to
over 600 people. Wow!
Since the last Ghostty devlog, the closed beta has grown from around 30 people
to about 100 people. Early in the project each new beta wave would be only
a few people, but as Ghostty has become more stable, we've been able to
comfortably grow the closed beta by 15 to 20 people per wave now. I'm taking
this as a great sign!
Pretty GUIs
Before diving into the deep end of terminal internals and archaic
technologies, let's talk about GUI improvements and look at some
eye candy.
If you're looking for deeply technical content, later sections
really go into some weeds.
The native GUIs on both macOS and Linux have made some big leaps.
On Linux, Ghostty now has a headerbar menu, wide tabs (configurable),
an About window, and more. Side by side with Gnome Terminal and
other GTK-based terminals, Ghostty fits right in:
Also for Linux, we now have multiple beta testers using Wayland via
Sway, Hyprland, and other compositors. We fixed a number of issues
and
Ghostty now works great with Wayland.
On macOS, we added a
window-theme
setting so you can permanently
set your Ghostty instance in dark or light mode instead of just following
your system. I personally run macOS in light mode but my terminal is
perpetually dark so I can force it dark. We also made it so unfocused
splits are faded (this can be configured). It all looks beautiful:
One of Ghostty's stated goals is to have native experiences that make
it feel like Ghostty was purpose-built for the platform you're on.
We take GUI improvements very seriously and ensure Ghostty follows
idiomatic designs for the platform it is running on. The improvements
above showcase our progress on these ideals.
We Found a Vim Bug! And Other Naughty Programs.
For most of its life, Ghostty has been advertising itself as
TERM=xterm-ghostty
. The
xterm-
prefix is because a lot of naughty
programs do string matching on
TERM
to determine if a terminal supports
some set of functionality. This is wrong and
very naughty
, do not do this!
The correct approach is to
query the terminfo database
.
Terminfo is an extremely interesting (primarily because it is so cursed)
topic on its own. I hope to write a dedicated blog post on terminfo one
day. This devlog will not go into detail about terminfo. If you care to
get a glimpse of this archaic beast, run
infocmp
in your terminal.
For the last month, we've been trying to rid ourselves of the
xterm-
prefix
and simply become
TERM=ghostty
. In the process, we've found a lot of bugs
with our own terminfo database as well as upstream issues. We've been fixing
both as we go.
Most recently, we've become blocked by a
vim bug
.
Vim 9.0 supports Kitty Keyboard Protocol, but hardcodes the list of terminals
that support it and doesn't properly respect the terminfo database. This is
a bug, and a Ghostty community member amazingly has opened a pull request to
fix it. This issue does not affect Neovim.
Vim is just a little bit important
1
, so until that bug is fixed and downstream
distributions are broadly updated, we've unfortunately had to revert to
being
TERM=xterm-ghostty
. Still, I'm proud of the progress we made and
I'm optimistic we can yield our xterm shackles soon.
We found other upstream bugs, and I'm proud that Ghostty community have been
not only reporting issues, but
also providing fixes
. Tim made a PR to
the popular Go library tcell
to fix a particularly bad issue. This is an important library since it is
used by popular TUI applications such as
lazygit
,
lazydocker
, etc. Without
this fix, all of those programs spew garbage unless you run them explicitly
with
TERM=xterm-256color
. I hope this can be accepted soon!
None of these bugs or fixes are Ghostty specific, and all should serve to
make programs more robust in the face of all unfamiliar terminal emulators.
This work was primarily driven by
Tim Culverhouse
and I'm deeply appreciative of everything he's done here.
XTGETTCAP (#563)
One of the big problems with
terminfo
is that it relies on a
local file
that the
running program
must inspect.
This means that if you SSH into a remote host and the remote host doesn't
have your terminal's terminfo, the program won't be able to determine what
your terminal is capable of and may behave incorrectly or suboptimally.
XTGETTCAP
is a feature of terminals that allows querying the terminfo
database for a terminal through VT escape sequences rather than reading
a local file. This has a couple benefits: programs don't need to know how
to parse the binary format or lookup the file path, and programs can query
terminfo even if they're running remotely.
XTGETTCAP
looks like this:
# Query for stylized underline support (key "Smulx")
ESC
P
+
q
536D756C78
ESC
\
# Response from the terminal (Smulx=\E[4:%p1%dm)
ESC
P
1
+
r
536D756C78=5C45343A25703125646D
ESC
\
Totally obvious, yeah? Really its not too bad. A program sends the text
ESC P + q <key> ESC \
where
<key>
is a hex-encoded string. In the
example above, we hex-encoded "Smulx". And the response has the key and value
of that terminfo entry, also hex-encoded.
A particularly cool thing about our implementation is that we used
Zig's comptime
capability
to generate all possible requests and responses at compile-time. This is
generated from the same source file that generates our actual terminfo file,
so our terminfo and XTGETTCAP are always perfectly in sync.
XTGETTCAP performance doesn't really matter at all, but our XTGETTCAP
implementation is
stupid fast
because it is a compile-time optimized lookup
table. We don't have to perform any allocations, string formatting, etc.
We do a simple lookup, find a stable character pointer, and write that
directly to the pty. Very cool.
Take a look at
the Zig snippet that generates this
.
I love Zig comptime.
Variable Fonts (#345)
Most fonts supply a set of fixed styles, such as "Bold", "Heavy",
"Medium", "Italic", etc.
Variable fonts
on the other hand provide a single font face that makes various axes
such as weight, slant, etc. configurable with a continuous value in
some range. Ghostty now supports variable fonts and configuring
variation axes.
First, let's take a look at what a variable font looks like.
Inconsolata has a variable font version and you can
see the video below where I can finely control character width
and weight.
Here is what Ghostty looks like by default with Inconsolata,
with no font variation axes set:
And here is a configuration where we slightly modify the weight.
The difference is subtle but you can see it. The configuration
first followed by a screenshot.
font-family = Inconsolata
font-variation-bold = wght=500
Why
wght
above and not
weight
? The key of the variation is determined
by the font and font variations must be four characters. These aren't
standardized so we can't safely convert
weight
to
wght
. The Ghostty
config uses the literal variation key and users can use any font inspection
program (such as
FontDrop
) to determine valid
keys.
Support for variable fonts is relatively rare amongst terminal
emulators, so I'm proud we support this (and cross-platform!).
These types of features really let you fine tune your terminal
to be exactly how you want it and make it feel
just right
.
Fin
Thanks again to our most recent round of beta testers. Each round
always brings in really incredible people who have certain specialized
depths of knowledge or exercise the terminal in new, unique ways to
find issues.
If you want to keep up to date, follow me on Twitter or Mastodon
(links in footer). This blog also has an
RSS feed
.
Boo. 👻
