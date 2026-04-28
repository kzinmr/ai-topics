---
title: "Ghostty Devlog 003"
url: "https://mitchellh.com/writing/ghostty-devlog-003"
fetched_at: 2026-04-28T07:02:41.048234+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty Devlog 003

Source: https://mitchellh.com/writing/ghostty-devlog-003

Hello! Welcome to the third official devlog for
Ghostty
👻!
I'm excited to share that we now have a
public Discord server
!
Anyone is welcome to join, ask questions about Ghostty, talk about
terminal emulators, talk about systems programming, GPU programming,
etc. We're also using the discord as a way to expand the beta program,
so if you're interested in joining the beta, please join the Discord server
and be somewhat active.
Next, I'll be giving a talk on Ghostty for
Zig Showtime
on September 5th. Please keep an eye on the Zig showtime website, twitter,
masto, etc. for updates on exact times and links. The talk is still being
developed but the general topic will be a whirlwind tour of the implementation
of Ghostty while highlighting a few interesting spots. It is
Zig
showtime
after all so I will focus more on the Zig aspects of Ghostty.
Keyboard Input Handling Hates You (#282)
1
I'm just a dumb US citizen typing on a dumb US-standard keyboard layout.
On a US-standard keyboard, you type
a
and you get "a", you type
'
(apostrophe) and you get "'". You type
shift+a
and you get "A". Easy,
easy.
You sit on a throne of lies.
The first hint of trouble are non-standard but English-centric keyboard layouts
such as Dvorak or Colemak. On US-standard physical keyboards, a Dvorak user
types
s
and expects "o" and presses
ctrl+i
and expects
ctrl+c
behavior.
The second hint of trouble are unicode sequences. On Mac, on a US-standard
layout,
alt+a
produces
å
. The latest beta group added a Norwegian user
who noted this is particularly important because they prefer the US-standard
layout but use the alt-sequences to type Norwegian words.
The third hint of trouble are non-standard keyboard layouts. Do you know
what a
dead key sequence
is? I
didn't (because I'm just a dumb US-standard user, remember). On US-standard
layouts, we're used to all keyboard presses being stateless. To uppercase
a character, you type
shift+A
at the same time
. With a dead key sequence
you'd type
shift
, let go, then type
a
, and then you'd see
A
(this
isn't a real world dead key sequence, but an example of what a dead key
sequence acts like). A real dead key sequence, on US international layouts:
type
'
, let go, then type
a
, and you get
á
.
When a person types a key on their keyboard, a few things happen. The
keyboard sends a
physical scancode
. Software keyboard layout handling
(i.e. using the Dvorak layout on a QWERTY keyboard) translates this
scancode to an alternate scancode ("i" acts like "c" with Dvorak). The
combination of modifiers (ctrl, alt, etc.) and other keys (i.e. letters)
may or may not
then produce
one or more
characters (i.e.
alt+p
on
macOS produces "π", but the same on Dvorak on a US physical keyboard
is
alt+r
).
Finally, not all modifiers may be consumed, and that is relevant
for keybindings. For example, if you bind
ctrl+=
on a US layout, that
would be
ctrl+shift+0
on a Norwegian layout, you have to know that
shift+0
produced
=
but
did not consume
ctrl
, so the final input
is
ctrl+=
. But if the user also bound
ctrl+shift+0
, which do you
use? 🤔
These explanations are
all very hand-wavy and lack detail.
I plan on writing an entire blog post dedicated to the eldritch horror
that is keyboard layouts, input handling, terminal keyboard "protocols",
and OS-level APIs so I'm going to skip the details in this devlog. Stay
tuned for that!
Ghostty not only has to handle these use cases (because it turns out
non US-standard keyboard users
exist
) but Ghostty must also do this
cross-platform
because Ghostty works on macOS and Linux already with
aspirations to also work on Windows. 😰 Well, Ghostty
now does
.
The only visual thing that can be shown is dead key state handling,
which is now rendered with the last pending dead key. You'll just have
to trust me that the rest now works.
In addition to the above, Ghostty now supports optional explicit
physical key mapping
. If you specify a keybinding as
ctrl+physical:0
(note the
physical:
prefix), then only the
physical
0
key will
trigger that binding. On some keyboard layouts, this may make the
keybinding impossible. By default, keybindings are based on logical (translated)
keys.
Kitty Keyboard Protocol and Others (#292, #295)
If you're tired of learning about keyboard input, just skip this section.
Beyond mapping keyboard keys to character input, keyboard events must also
be mapped to
escape sequences
so that running programs in the terminal
know what key you pressed.
The original terminal protocols sent the characters produced by keyboard
keys as-is. You type "a", you get "a", you type "A" (shift+A), you get "A".
This has
a lot of limitations
.
For example, terminal programs could not react to modifiers such as
ctrl-i
and
ctrl-shift-i
since they produced the same data.
Many additional keyboard protocols were developed to address these shortcomings.
xterm developed the
modified keys
sequences, Paul Evans developed the
fixterms
protocol, and Kovid Goyal (of Kitty) developed the
Kitty Keyboard Protocol
.
The gist of these protocols is that they simply define what the terminal
sends to the running program when keys are pressed.
These aren't hypothetical problems. These protocols are implemented by
tmux
,
neovim
, and other major programs and let you bind many hundreds
more keybindings than you would would otherwise.
Ghostty now implements all of these
.
As far as I know, Ghostty is one of only a handful of terminals that
implements
all of these
. I believe only iTerm, Foot, and maybe WezTerm
implement xterm modified keys
and
Kitty. I think only those plus Kitty
implement the Kitty protocol at all. Most terminals (Terminal.app,
Windows Terminal, Alacritty, Warp) implement
none
of the keyboard protocols.
2
Here is a video showing the Kitty keyboard protocol working:
And here is a video showing the xterm modified keys protocol working:
The Year of Desktop Linux (GTK)
The last batch of beta users increased our full-time Linux user
count from just a couple to around 5 or 6, and with it came
many
improvements
in the Linux experience.
First,
GTK single instance mode
(#247) is now enabled and supported.
For GTK, Ghostty now runs a single process. Launching Ghostty a second time
opens a new window in the existing Ghostty process. This plays nicely with
standard graphical desktop environments and also makes launching Ghostty
super fast
after the first launch.
Next, Ghostty now has
primary (selection) clipboard support
(#266).
Linux desktops have multiple clipboards. The "primary" (or "selection")
keyboard is where text is automatically copied for text selections, and
pasting is usually done via the middle mouse button. This is a
separate
clipboard
from where
ctrl+shift+c
and
ctrl+shift+v
go, so you can have
multiple items on your clipboard. This feature is sometimes controversial,
so don't worry, you can disable it with the
copy-on-select
configuration.
You can see this work in the video below. Note that I'm
not
pressing any
keyboard bindings; this is only using the selection clipboard.
Linux now supports
automatic shell integration
(#245). I talked about
shell integration in Devlog 001
.
Previously, Linux users had to set an environment variable to point to
Ghostty's
share
directory. The Linux application now searches up from
the
ghostty
executable for a
share
directory with the proper folder
structure. If you install Ghostty using a standard
FHS directory layout
(the standard layout Ghostty packages up in), then Ghostty will automatically
find and configure your shell.
And a lot more, the Ghostty app icon shows up properly (#251), the
GTK application handles non-US keyboard layouts (#271), the GTK
application supports semi-transparent window backgrounds (#264), and more.
I really want Ghostty to be a top-tier GTK-based Linux terminal. I don't
use GTK full time so I am really dependent on testers to provide feedback
to make this experience great. I'm really happy to report that Ghostty
is feeling really good on GTK now! The GTK application is still lagging
behind the macOS experience but I'm looking forward to bringing it up to
parity!
Fin
The most recent round of beta testers have been
so amazing
. I want to
thank
@hovsater
for exposing all the glaring
keyboard layout and mapping issues and pushing me to fix them all.
@cryptocode
exposed a dozen or so bugs
around edge cases with wide characters, multi-codepoint graphemes, and
their interaction with selection and soft-wrapping. And there are a number
of new testers worthy of thanks for the Linux improvements. Thank you!
If you want to keep up to date, follow me on Twitter or Mastodon
(links in footer). This blog also has an
RSS feed
.
Boo. 👻
