---
title: "A Week With the New Privacy Controls in MacOS 27.3 Beta 2"
url: "https://daringfireball.net/2026/11/a_week_with_the_new_privacy_controls_in_macos_273"
fetched_at: 2026-11-22T10:01:11.468524+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# A Week With the New Privacy Controls in MacOS 27.3 Beta 2

Source: https://daringfireball.net/2026/11/a_week_with_the_new_privacy_controls_in_macos_273

A Week With the New Privacy Controls in MacOS 27.3 Beta 2
Saturday, 21 November 2026
On Monday, when the second betas of the v27.3 OSes came out,
I posted about Apple adding the new privacy controls
they had
promised a month prior
, in the wake of Meta’s Muse app
surprising some users
with what information it had access to (e.g., incoming iMessages) after being granted Full Disk Access — which authorization some users just clicked right through. I also posted a link to Apple’s
corresponding new support documents
. My initial take on Monday:
I’m installing it now, but from what I’ve seen so far, these
changes not only alleviate my concerns that Apple might
over-tighten the screws, I actually think they add clarity and
give users
more
, not less, control over their Macs.
After a week, I’m willing to call it: this overhaul of these settings and permissions is a win. I really like the way that, for apps asking for Full Disk Access, users can now grant access to a list of folders instead. That’s what I mean about these new settings giving users
more
control.
Are these new dialog boxes “scarier”? Yes, and the point is, they should be. You should be slightly jolted into attention when an app prompts for any of these permissions. The question is whether they are unnecessarily scary. I would say no, not at all. The descriptions are fair and accurate. Is it unnecessarily scary to show you thumbnails of your personal photos before permitting Full Disk Access that would grant an application unfettered access to your personal photos? No! It’s a bit of a jolt to see them, but that’s just reducing the abstraction. The words “full disk access” feel different than actually
seeing
a snapshot of what full disk access entails.
Might this discourage some Mac users from granting Full Disk Access to AI agent apps? Yes. And it should! Users who actually understand the stakes will not be dissuaded by these new permissions — when granting them is what they know they want to do. Additionally, I think these new dialog boxes represent very good UI design.
They look like a new modern take on MacOS “system chrome” design
— not skinny iPhone-sized alerts.
My only gripe about the new stuff is the prominent menu bar indicator that now appears when one app is controlling another. You can’t turn it off (except via an undocumented hidden
defaults
setting), and it’s distracting on most Macs, and
extra
distracting on the new MacBook Pros with PROLED displays because on those Macs, it appears in the Dynamic Island!
Chance Miller, on Threads
(with screenshots):
Most of the changes in macOS 27.3 are reasonable, but this Live
Activity thing for system access has got to go. It’s way too
aggressive.
It takes over the Dynamic Island on the new MacBook Pro!
As I write this article on a new MacBook Pro review unit, I have 8 of these indicators in my Dynamic Island:
Scroll Reverser
,
Keyboard Maestro Engine
,
HazeOver
,
SteerMouse Manager
,
Moom
,
Chest
(a promising new utility for managing menu bar icons),
System Events
, and a new text snippet expansion utility I’m beta testing.
Every one of these apps is running all of the time for me. This indicator being on, all the time, for every one of them isn’t helping me notice unusual activity. If anything, if Apple doesn’t rethink this idea, it’s going to make me
miss
the indication if an app is taking advantage of access permissions in an unwanted or unexpected way.
Zac Hall, Miller’s colleague at 9to5Mac, published an article on Tuesday
showing the command-line
defaults
incantation to disable this
. That’s better than not being able to disable it at all, but I expect Apple to revisit this based on feedback. It seems like a well-intentioned feature that was designed by people who didn’t realize how many always-on utilities “control other apps”.
