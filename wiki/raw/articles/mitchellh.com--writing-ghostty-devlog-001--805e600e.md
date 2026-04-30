---
title: "Ghostty Devlog 001"
url: "https://mitchellh.com/writing/ghostty-devlog-001"
fetched_at: 2026-04-30T07:01:54.140702+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty Devlog 001

Source: https://mitchellh.com/writing/ghostty-devlog-001

An inaugural devlog for
Ghostty
👻! Ghostty is the
terminal emulator I've been working on as a side project since 2021.
I recently
shared that Ghostty exists
and since then there's been a ton of interest in it!
I'm not ready to open it to the public (but I promise I plan to, fully FOSS),
but for historical reasons I wanted to start a devlog to share details about
the terminal and progress reports about how its all going. I think there
are generally interesting engineering things to share and I hope people
enjoy this and maybe learn a thing or two (or, reach out and teach me
a thing or two).
These devlogs are all going to be written in a very casual, almost
conversational tone. They aren't going to be on any specific cadence.
They'll cover anything related to the terminal: features, weird bugs,
my own ignorance, etc.
Tech Stack
As this is the first devlog ever, let's talk about the tech stack behind
Ghostty. Ghostty is a cross-platform (macOS and Linux today, but written
in a way that Windows support will come later), GPU-accelerated
terminal emulator.
Written in
Zig
Libxev
event loop (written and extracted specifically from Ghostty)
OpenGL on Linux, Metal on macOS
Fontconfig,
Freetype
,
Harfbuzz
for font rendering on Linux
CoreText
and
Harfbuzz
for font rendering on macOS
SwiftUI
frontend on macOS,
GTK
on Linux, also a
GLFW
option
Almost everything else is fully custom written in Zig
I'm not going to talk about the "why" for any of this. I'm just laying
out the tech stack as-is for people who are interested. Take it as you
will.
Automatic Shell Integration Injection (#191)
Let's talk about our first feature!
Did you know that modern terminal emulators can communicate with shells
(when properly configured) to enable
a lot
of nice to have features?
Talking to at least my close circle of developer friends, most people
do not know this
and
do not have this enabled
or
do not use
a terminal emulator that supports it
. 😢
Shell integration with the terminal
does a lot of stuff (see Kitty)
.
There are a few base features with shell integration that requires zero
workflow knowledge that really improve quality of life:
Complex prompt redrawing on resize. This makes resizing your
terminal way less glitchy with modern, complex prompts.
Working directory reporting. This allows new tabs, splits, etc.
to inherit the working directory of the previously focused terminal.
Active process detection. This can be used to safely close the
terminal without asking the user for confirmation if the terminal
emulator knows the user is sitting at an idle shell prompt.
I love demos, so let's look at one example:
complex prompt redrawing.
The video below
is not Ghostty
, it is some other popular terminal emulator
on macOS. This shows resizing my fish prompt without shell integration.
Notice the prompt becomes garbage.
The terminal emulator is not doing
anything wrong here. It is reflowing text but because the shell doesn't
(and can't, today) know that it reflowed the prompt onto multiple lines,
it gets redrawn on the bottom new line and duplicates a bunch.
Next is Ghostty, with shell integration configured.
Much better! The shell can communicate to the terminal that it can redraw
the prompt on resize. On resize, Ghostty clears the terminal line
(you can see the flashing -- I want to improve that later). This prevents
the text reflow which prevents new lines and results in perfect reflow
on resize.
Okay, but how do you configure this?
This requires shell-specific
(zsh code for zsh, fish code for fish, garbage for bash, etc.) configuration
to make work. Prior to #191, I just documented how users can set this
up manually.
But now, Ghostty does this 🪄 automagically 🪄 (for fish and zsh so far).
This can be disabled, but the way this works is that it does a simple
basename on your shell and if its "fish" it assumes its fish" and if its
"zsh" it assumes its "zsh", and sets the correct environment variables
so that some embedded configuration files are loaded with your shell
and set all this up automatically.
Since Ghostty isn't public at the time of writing this, the terminal
with the best shell integration today is
Kitty
. Kitty also does automatic
shell integration. If you want features like
this today, use Kitty. Other terminal emulators also support some of
these features, too!
Auto-Italicize Fonts (#179)
This fixes one bug, and adds one feature.
The basics: regular, bold, italic, and bold italic are different
font faces
. If you have a font
MyAwesomeFont.ttf
-- it is just a single
face (regular,  probably). I'm doing a lot of hand-waving here but
this is generally the case.
When a user says they want to use
MyAwesomeFont
, Ghostty has to
not only find this font, but find
all the faces
associated with this
font. A lot of programming fonts do not have italic or bold faces.
(Aside, the process of finding a font and all associatd faces is usually
called the problem of
font discovery
. This is a more general problem:
if a user doesn't specify a font, what font do you use by default? etc.)
First, The Bug
Another important bit of background: fonts often do not have every
possible glyph (a single drawable character). For example, a standard
monospace programming font probably doesn't have Chinese characters
(i.e., grass = 草 if that rendered for you).
If a program tries to draw a character that isn't in your configured
font, Ghostty
tries to find any other font that has it
. This is
usually
better behavior than just rendering a box and forcing your font file
to have every glyph in existence. There are some complexities about
drawing this glyph in a way that matches your configured font but
this isn't about that -- just know those problems exist and figuring
out the solution personally feels like some form of self-harm.
The bug was this: previously, if a character didn't exist in the given
style
in your font, Ghostty would search for any font that had that
character in that style. This resulted in... really ugly rendering because
if a monospace font didn't have a character, Ghostty would find a
non-monospace font and it'd end up looking like this:
Oh no.
The bug fix: if a character doesn't exist in the given style,
and the style is not "regular", try regular first. The result is that
the style is ignored, but it renders correctly. Cool.
Note that Ghostty would already try to search monospace fonts first.
It may seem reasonable to
never
choose to use a non-monospace
(proportional) font, but characters such as Chinese characters tend to
work just fine from proportional fonts so I don't think this limitation
is necessary.
Better, Make Italics Programmatically
For italics in particular, we can do better. If a font doesn't provide
an italic font, we can
skew
the regular font to create fake italics.
It won't look as good because it wasn't artisanally designed while sipping
a single-origin pour-over but it'll... pass.
So that's what Ghostty now does. If an italicized character is requested
and the font in use doesn't support italics, we rasterize the regular
glyph with a skew and make fake italics:
The font above doesn't support italics. The italics are fake. They look
alright! And they definitely look better than just rendering no italics
at all.
If you're curious about the internals of this works: font rasterization
libraries such as FreeType or CoreText allow callers to provide a
transformation matrix. For CoreText, the transformation matrix
can be provided when
initializing the font with
CTFontCreateCopyWithAttributes
.
For Ghostty, we just have a hardcoded 15 degree skew (see below), but you
can see how you could customize this to skew a glyph any way you want.
pub
const
italic_skew
:
macos
.
graphics
.
AffineTransform
=
.
{
.
a
=
1
,
.
b
=
0
,
.
c
=
0.267949
,
// approx. tan(15)
.
d
=
1
,
.
tx
=
0
,
.
ty
=
0
,
}
;
Fin
That concludes the first ever Ghostty devlog. I hope you learned a
thing or two or found this interesting. Given its the first one, there
were
so many more things
I could've covered but I'll save them
for future devlogs (though, I'll try to focus on newer developments).
If you want to keep up to date, follow me on Twitter or Mastodon
(links in footer). This blog also has an
RSS feed
.
Boo. 👻
