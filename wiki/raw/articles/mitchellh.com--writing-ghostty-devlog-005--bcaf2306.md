---
title: "Ghostty Devlog 005"
url: "https://mitchellh.com/writing/ghostty-devlog-005"
fetched_at: 2026-05-01T07:02:03.313637+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty Devlog 005

Source: https://mitchellh.com/writing/ghostty-devlog-005

Hello! Welcome to the official devlog for
Ghostty
👻!
It has been over two months since the last devlog, and there have been
a lot
of updates to Ghostty. I've been busy being a new dad and just generally focusing
more of my computer free time on improving Ghostty, so I've neglected the
devlog a bit. Sorry!
In the past two months, the beta testing group has grown from 100 people
to over 350 people! Whoa! Two months ago the beta was less than 50 people.
I'm so thankful for the interest in this terminal project and the beta testers
we have. This large and growing group of testers is really going to ensure that
Ghostty is a strong and stable project by the time we reach a public release.
The only reason I'm able to increase the beta group by so much for
each wave is because Ghostty is becoming so much more feature complete and
stable. Beta waves used to be 5 people and result in a dozen or more bugs or
feature requests. Now, we can invite 50 to get the same amount. And that
number is only going to increase. It is very satisfying to see this project
becoming very real and very stable.
If you're interested in joining the beta program,
join the Ghostty Discord
to be considered
for the next beta wave. At the time of writing this, about 20% of the
Discord community is part of the beta.
Terminal Inspector (#728)
A terminal is an application platform. I think the word "platform" is
thrown around way too much by people trying to believe their work is more
important than it actually is (or at least trying to make investors
believe its more important than it actually is), but a terminal is
actually
a plaform
for text-based interactivity
1
.
A terminal is not interesting without the applications that run in it.
Going further, a terminal is
pointless
without applications that run in it.
One way of increasing the quantity and quality of terminal applications is
to make it easier to build for the terminal.
If we look to the web, a quantum leap in ease of development for me
came with the introduction of
Firebug
,
now more commonly called a "web inspector" and similar functionality is
present in every major browser. I wanted to bring a similar experience to
the terminal, so Ghostty now has a
terminal inspector
.
The terminal inspector works similarly to a web inspector: it is a
per-terminal panel that contains live updating information about the
running terminal. You can see keyboard input (and how they encode),
terminal modes, font sizes, grid sizes, cell metadata, palette colors,
and much more.
The goal is for the terminal inspector to be an indispensable tool
for terminal developers to make it easier to develop and debug terminal
applications (that work in
any
terminal, not just Ghostty).
The terminal inspector is still very early and very experimental. It
is a purely read-only interface today but I plan to make it read-write
in the future so you can modify cells, terminal modes, create synthetic
input events, and more.
The original terminal inspector idea came from a member of the beta
community, and a small group within the beta community including me
quickly rallied to grow this into a very real idea. Thanks to everyone
involved!
Asian Language Input (#八百八十八)
In recent beta waves I've made an explicit effort to invite people
from a more diverse set of timezones. This has yielded many more testers
typing in languages such as Chinese, Japanese, and Korean. These testers
reported nearly a dozen issues related to Asian language input and
rendering. As a result, Ghostty now works
very well
with these languages.
In
devlog 003
I had a section dedicated
to keyboard input titled "Keyboard Input Handling Hates You." I talked
big game about how great things work in Ghostty and I'm here to follow that
up by doubling down on how terribly complex everything is and to once
again say that Ghostty
handles it all great
2
.
More Complex Input States
In
devlog 003
I introduced the concept
of a
dead key state
. Ghostty at that time handled
dead key states for
single codepoints
. I used the example of an accented
English letter. In the example, you'd type something like
'
(apostrophe)
then a letter like
a
and you get
á
.
In languages such as Japanese, you type some characters, get a suggested
input (potentially with a dropdown of more suggestions) and you can press
characters such as enter or tab to complete the suggestion.
Ghostty did not handle multi-codepoint suggestions and also was incorrectly
processing characters such as enter or tab while suggestions were being
shown. This is now all fixed and you can type Japanese (and other languages).
This multi-codepoint suggestion state also introduced a couple edge cases:
typing at the end of a line and typing in a window that is too narrow.
These too are both handled by Ghostty now. Note the video above was recorded
prior to another bug being fixed (if you can spot it), but that too
is now resolved.
Chinese Character Alignment (#982)
Rendering multiple fonts (plus Emoji) in a monospace terminal grid in a way
that looks clean and cohesive is a challenge and Chinese characters did
not look quite right:
Notice the word starting with
草
is rendering a bit low. This was caused
by using incorrect font metric calculations (in this case: the cell baseline)
when mixing certain fonts. This is now fixed in Ghostty.
Linux IME Input (#919)
macOS has great support for
input method editors (IMEs)
built-in to the OS. On Linux with GTK, IMEs are provided by optionally
installed plugins. Because of this, they weren't as well tested with
Ghostty and weren't working at all for Chinese, Japanese, and Korean.
Thankfully, I did a lot of work to support IMEs in the shared core
of Ghostty, so making this work properly on Linux required only a
+47/-1
diff to glue together the proper GTK and Ghostty APIs. And as a result,
IMEs work on Linux:
Note: this video was recorded prior to the above fixes so you can see
the incorrectly rendered characters.
Custom Shaders (#903)
Have you ever wanted your terminal to look like a classic CRT? Or
perhaps a broken VHS tape? What the fuck am I talking about? Have I
lost my mind? Anyways, you can now do all of this and more in Ghostty
by specifying
custom shaders
.
Impracticality aside, this sort of feature looks like it'd be terrible
for battery life. The general inefficiency of most modern software has
taken us all for fools! CPUs and GPUs are super fast and this is barely
doing anything. On my machine, the above effect uses ~1% CPU and ~2% GPU.
It definitely uses more power than if you
didn't use the feature
(of course!) but it isn't going to spin up fans or anything.
Ghostty is a GPU-powered terminal emulator. It uses raw Metal on macOS
and OpenGL on Linux. GPUs render things by invoking
shaders
. A shader
is
waves hands
a program that runs on the GPU.
Shaders are generally written in a technology-specific programming language.
For example, Metal on macOS uses MSL (Metal Shading Language), OpenGL
uses GLSL (GL Shading Language), etc. Ghostty accepts shaders written
in GLSL and will convert them
on the fly
to MSL on macOS. To do this
Ghostty uses
glslang
to
convert GLSL to SPIR-V (roughly an intermediate representation) and
then
SPIRV-Cross
to
convert SPIR-V to the target format such as MSL. We compile and bind
to both of these tools using their exposed C APIs.
Another super cool detail about this feature is that Ghostty exposes
the
Shadertoy
interface, so you can take
many Shadertoy shaders and drop them into Ghostty without any modification.
More importantly, you can use Shadertoy itself as a live, interactive
development tool for Ghostty custom shaders!
Fear not, this feature does not negatively impact performance. Ghostty
uses a multi-threaded rendering architecture and has plenty of idle
time between frames. When custom shaders are in use, there is less idle
time but it has very little to no effect on the other threads (IO and GUI).
When custom shaders are not in use, Ghostty uses the same rendering pipeline
it always has and doesn't add any new resources to existing execution
(except the one boolean check for custom shaders and the minimal memory
footprint to represent an empty list of custom shaders).
Okay, but this is all
completely pointless
,right?
The most common use case
is fun and that's certainly not necessary (yeah, screw fun, right?).
However, the primary practical use case for custom shaders is accessibility. Custom shaders are a really
great way to specifically address certain forms of colorblindness,
affect contrast or brightness to make things more readable, create
"magnifying glass" effects, etc.
I'm not trying to punt accessiblity
onto others and I'm open to making various accessiblity features first-class
but this is a great way for users to take things into their own hands
in scenarios Ghostty doesn't yet have certain functionality.
Xterm Compatibility Audit and Behavior Documentation (#632)
Terminal
emulators
are emulators, but what are they emulating?
Traditionally, a terminal emulator emulated a physical terminal such as the
VT52, VT100, VT220, etc. In practice, its been so long since this hardware
has been readily available or practically used that most modern terminal
emulators just kind of
mimic
each others behavior. This leads to a variety
of behaviors that don't quite match up amongst different terminal emulators,
and many terminal emulators have bugs around edge cases
3
.
xterm
is the standard terminal
emulator for the X window system and is very often touted as the gold standard
for historical terminal behavior. Additionally, xterm is in widespread enough
use that its behavior can be considered a defacto standard for the features
it supports even when ignoring historical terminals.
I've decided that wherever possible and reasonable, Ghostty should exactly
match xterm's behavior. This gives the project a consistent answer to
"why does
<feature>
behave this way?"
4
What do I mean by "wherever possible and reasonable?" I mean that
by default
when implementing a feature, we should match xterm. If a bug is reported with
some features, we always ask "what does xterm do in this situation?" If a
compelling argument can be made to diverge from that behavior, then it is an
exception and not the norm.
To do this, I've begun to slowly audit every documented feature of xterm
and compare it to Ghostty. In the process, I've also been building up our own
documentation that I try to make as detailed as possible. The documentation
also contains shell script validation cases with the expected output so
that end-to-end tests can be written to ensure compatiblity. It looks like
this:
Terminals support many features, xterm's codebase is complex, and this
task is very tedious, so I won't complete it overnight. But over the past
few months I've been slowly checking off feature by feature and so far
this has resulted in dozens of bugs being fixed in Ghostty and dozens of
bugs being found in other terminals (some reported, some I will report
later, none are critical).
This does not mean Ghostty will support every feature xterm supports.
Instead, for the features Ghostty has that xterm supports, Ghostty will
aim for maximum compatibility with xterm (with exceptions allowed with
good reason).
Fin
For the devlogs, I focus on a handful of changes that I find
interesting and want to share. The devlogs aren't changelogs
and I don't want them to ever read as just a boring list of changes. That
being said, I want to point out that in the past two months there have also
been over
100 bug fixes and improvements
in the Ghostty project and
Ghostty becomes closer and closer to being publicly ready every day.
As the beta has grown, so have the number of contributors. Almost 50
people have contributed to Ghostty (nearly 1 in every 6 beta testers
doesn't just report a bug, but contributes code!). This is really amazing
and I'm very thankful for the time and interest in the project.
If you want to keep up to date, follow me on Twitter or Mastodon
(links in footer). This blog also has an
RSS feed
.
Boo. 👻
