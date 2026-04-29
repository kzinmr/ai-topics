---
title: "Ghostty 1.0 is Coming"
url: "https://mitchellh.com/writing/ghostty-is-coming"
fetched_at: 2026-04-29T07:01:59.884871+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty 1.0 is Coming

Source: https://mitchellh.com/writing/ghostty-is-coming

After nearly two years of development and private beta testing
1
, I’m excited
to share that
Ghostty
1.0 will be publicly released in December 2024 as an
open-source project under the MIT license.
In this blog post, I want to restate the broader goals of the Ghostty project
and outline the specific goals for the 1.0 release. I have ambitious plans for
Ghostty, but I also want to set clear expectations for what to expect on
day one versus what will come in the future.
In short, Ghostty 1.0 aims to be the
best drop-in replacement for your
current terminal emulator
on macOS and Linux. Ghostty will be fast,
feature-rich, and have a platform-native GUI while being the most
standards-compliant terminal emulator available.
Best Existing Terminal Emulator
This slide from my
Zig Showtime talk
in September 2023 best summarizes why I started working on a new
terminal emulator:
The number of terminal emulators compared is limited primarily due
to slide design considerations but the broader point remains:
I felt that the existing terminal emulators pushed an unnecessary
choice between speed, features, and platform-native GUIs.
2
With Ghostty, I set out to build a terminal emulator that was
fast, feature-rich, and had a platform-native GUI while still being
cross-platform. I believe Ghostty 1.0 achieves all of these goals.
This goal focuses on being
the best existing terminal emulator
.
Within this goal, Ghostty 1.0 isn't trying to innovate on what a terminal
can do but instead provide the best single terminal emulator experience
available today on macOS and Linux
3
.
Of course, Ghostty isn't perfect or complete. I didn't implement
every feature of every terminal emulator so there are still
plenty of features that Ghostty doesn't have. However, I believe
Ghostty will satisfy a large majority of users as I continue to
improve it.
Fast, Feature-Rich, and Platform-Native
The most common feedback I've received from
people
before
they've used Ghostty is skepticism that any of this
makes a difference. The most common feedback I've received from
people
after
they've used Ghostty is that they didn't realize how
much of a difference it makes and they can't imagine going back.
What does it mean for Ghostty to be fast, feature-rich, and platform-native?
Each of these are large, complex topics so I'll only highlight a few
key points for each area.
For "fast", I recently gave a 5-minute lightning talk at
Systems Distributed 2024 titled
"Making a Terminal Emulator Really, Really Fast: Ghostty"
(timestamp link to 50:15).
This gives a good overview of the performance thought that has gone
into Ghostty, but isn't exhaustive since it is only a lightning talk.
For "feature-rich", Ghostty first and foremost aims to support the
widest range of terminal applications possible. This means Ghostty supports
more of the xterm escape sequences than any other terminal emulator
(besides xterm itself). Ghostty also supports almost all modern terminal
specifications such as styled underlines, Kitty keyboard protocol,
graphics protocol, and more. (Not a terminal escape sequence but
yes, Ghostty does support ligatures!)
For "platform-native", Ghostty uses the native GUI toolkit on macOS
and GTK (plus libadwaita if available) on Linux. This means that
Ghostty looks and feels (and really
is
) a native application on
both platforms. This is in contrast to many terminal emulators that
use the native GUI toolkits only to create a window.
As an example of the platform-native benefits: Ghostty has native
tabs, splits, right-click menus, menu bars, dock integration,
input method support (emoji keyboards, dictation, etc.), confirmation
windows, desktop notifications, macOS secure input mode, and more.
Here are some screenshots of Ghostty on macOS and Linux
(both themed but likely only a few lines of configuration), showing
the platform-native GUI:
(Both images are from the community in our public showcase channel
in the Ghostty Discord server)
The First Release Will Be 1.0
Ghostty has been in private beta testing for nearly two years. At
the time of writing, Ghostty has around 2,000 testers across macOS
and Linux, most of whom have been using Ghostty as their primary
daily terminal emulator without issue.
Due to the extensive private beta testing, the first public release
of Ghostty will be version 1.0. There won't be any
ZeroVer
here!
4
My motivation for the extensive private beta testing was principally
selfish: I had my first child and I wanted to prioritize my time
with my family over external pressures to build features or fix bugs.
In theory, I could have ignored the noise but in practice I know myself
well enough to know that I would have been distracted and it would've
been mentally taxing.
Beyond the family motivation, I am nostalgic for the days when software
was released when it was ready. I like to imagine that if stores like
CompUSA still existed, Ghostty 1.0 would be boxed, shrink-wrapped, and
on the shelf ready for purchase (but also free and open-source).
The other effects of the private beta testing were unexpected or
unintended. For example, I never intended for Ghostty to feel exclusive
(I quite frankly didn't expect that many people to be interested in
a terminal emulator!) and I never intended for the private beta to
artificially create hype around Ghostty. If you were on the negative
side of this, I apologize.
I'm surprised how much criticism I received for this approach and
the number of entitled people who seemed to believe that they were
owed something just because I liked sharing my work and progress.
At the same time, I'm thankful for the much larger number of people
who have been supportive and understanding of my approach.
And finally, thank you to the testers who have been using Ghostty
and providing fantastic feedback. Ghostty's stability is only possible
due to the diverse set of testers who risked using an early version
of what is often a critical piece in a developer's toolkit.
The Big Vision
Looking to the future, Ghostty has ambitious plans in two main areas:
libghostty
and
terminal application functionality
.
libghostty
is the core, cross-platform library that powers Ghostty.
It is available as a Zig and C API and works today on macOS and Linux.
The goal is to allow a large and diverse ecosystem of terminal emulator
applications to emerge ranging from dedicated applications, embedded
terminals such as in editors, web-based terminals, new terminal
multiplexers, and more.
The idea with libghostty is that developers can focus on the hard work
of building a great application and get fast, feature-rich,
standards-compliant terminal emulation for free. In many ways, I describe
Ghostty today as a "reference implementation" of a libghostty consumer.
For Ghostty 1.0, libghostty is not considered stable or available as
a standalone public API. But, Ghostty does use libghostty internally.
The goal after Ghostty 1.0 is to reach a point where libghostty is
released as a standalone library and to expand platform support beyond
macOS and Linux, especially to WebAssembly.
In addition to libghostty, I am interested in building out more
functionality within terminals that applications can take advantage of.
Some ideas include improving the security of escape sequences, allowing
more modern input methods (such as touch gestures, momentum scrolling,
drawing devices, etc.), allowing applications to provide native
context menus, and more.
The goal with expanding terminal application functionality is to
make text-based applications more attractive for developers to build
and for users to use. I believe that text-based applications have
a valuable niche in the software ecosystem and I want to help modernize
the platform.
These are big, long-term goals to demonstrate that I have a bigger vision
for Ghostty that I'm working towards. In the short term, I plan to iteratively
improve Ghostty based on feedback from users and my own ideas according
to the original broad goal of being fast, feature-rich, and platform-native.
There are some major features I'm sad aren't going to make the 1.0 release
but will come in follow-up releases.
Finances and Sustainability
I don't want this to be a major focus of this blog post but given my
background as an entrepreneur and the general interest in the topic,
I will briefly touch on the financial and sustainability aspects of
Ghostty to avoid any confusion or speculation.
Ghostty is a passion project for me and I have no plans to pursue
any sort of commercialization of the project. As stated in the first
paragraph, Ghostty will be released as an open-source project under
the MIT license.
On a personal level, I am fortunate thanks to past successes to have
the financial freedom to work on projects like Ghostty without any
financial pressure. I have stated many times publicly that I view my work
on Ghostty as a form of "technical philanthropy;" a means for me to
give back while also scratching my own itch and having fun.
At the same time, I do want Ghostty to survive long-term without
me and I also want to be able to potentially compensate major contributors
for their work. To that end, I along with the [currently private] community
are exploring not-for-profit structures to help ensure the long-term
sustainability of Ghostty. But this is a long-term goal and not something
that will be in place for the 1.0 release.
See You in December
I'm looking forward to the public release of Ghostty 1.0 in December
2024.
Ghostty has been a huge passion project for me for over two years,
starting as a once-in-awhile side project alongside my full-time job
to becoming my primary (but very much part-time) focus after leaving
my job and welcoming my first child.
Ghostty 1.0 won't be perfect, but its stability and feature set is
something I'm proud of and I think it's ready to be shared with the
rest of the world. Most importantly, I hope people feel how much love
and care I've put into Ghostty and that it brings joy to their daily
work (as much as a terminal emulator can).
👻
