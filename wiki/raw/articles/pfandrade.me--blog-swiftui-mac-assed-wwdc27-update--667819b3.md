---
title: "A WWDC 27 Update on Building a Mac-assed App with SwiftUI"
url: "https://pfandrade.me/blog/swiftui-mac-assed-wwdc27-update/"
fetched_at: 2026-07-13T07:01:30.719603+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# A WWDC 27 Update on Building a Mac-assed App with SwiftUI

Source: https://pfandrade.me/blog/swiftui-mac-assed-wwdc27-update/

My
last post
on using SwiftUI to build a Mac-assed app got a bit more traction than I expected. It was mentioned on Mastodon
several
times
, included in
iOS Dev Weekly
, inspired May's edition of the
Swift Blog Carnival
, and was eventually mentioned by
John Gruber
, arguably the person most to blame for popularizing the term "Mac-assed", on
Daring Fireball
.
All this attention also resulted in an engineer from Apple reaching out with some notes. We exchanged a few emails, I filed a few radars, and now that WWDC 27 is behind us, this post serves as a small update to the issues I wrote about before.
Selected States
Regarding selected states, there is a
\.backgroundProminence
environment value
I was not aware of when I wrote the previous post.
According to the documentation, "views like List and Table as well as standard shape styles like
ShapeStyle.selection
will automatically update the background prominence of foreground views."
That means SwiftUI already has a built-in concept that is pretty close to what I called
\.isEmphasized
. If you are using
List
or
Table
, you can check this value as selection prominence changes.
Of course, if you are not using
List
or
Table
- and you probably are not if you are trying to do any sort of serious customization - the approach I mentioned before is still the way to go. Track focus yourself and pass that state down through the environment.
The difference is that you can reuse
\.backgroundProminence
instead of creating your own
\.isEmphasized
value. That has the nice side effect of making your custom rows a little more compatible if you ever place them inside a
List
or
Table
in the future.
I also filed
FB23095823
with some ideas for what
List
could expose to make custom rows more useful. I still think this is the right direction. When you're working with AppKit or UIKit, you have a tremendous amount of flexibility with your cells and rows, and the feedback I raised tries to bring
List
closer to what's possible there.
Drag & Drop
There is a new
.onDragSessionUpdated
API
, introduced for the 27 OS releases and apparently already available on macOS 26, that solves my biggest issue with drag and drop in SwiftUI: having visibility into the drag session from the start.
I have not tested this yet, but on paper it seems to be exactly the missing piece. You should finally be able to update your UI when a drag starts and clean it up reliably when the session ends, even if the drop happens outside your view.
That is precisely the kind of thing AppKit has been able to do for ages, so it is good to see SwiftUI get closer here.
Having said that, my apps usually support the last two major OS versions, so I'll probably only start playing with this in two years.
Also worth noting is the new
.reorderable
modifier
in the 27 releases. If you're just looking to allow reordering, this should be the way to go.
Keyboard Shortcuts
As I mentioned before,
.onMoveCommand
is not available on iOS. The workaround is to use a lower-level abstraction such as
.onKeyPress
, which also works on macOS.
That works, but it is not quite the same thing.
.onMoveCommand
is the more appropriate API because it deals in intent. I do not really care that the user pressed the down arrow key. I care that the user wants to move down.
At first I assumed
.onMoveCommand
was not available on iOS because
UIResponder
does not have matching
move*
selectors. Then I noticed
.onMoveCommand
is
available on tvOS.
So now I am back to thinking this is just an API availability gap. If it makes sense on tvOS, it absolutely makes sense on iPadOS, where hardware keyboards are common and arrow-key navigation is expected.
I filed
FB23095985
for this. These little platform differences are exactly the kind of thing that weaken the promise of a cross-platform UI framework. They are small in isolation, but they add up quickly when you are trying to share real UI code.
Other Gripes
For the other issues I mentioned, I filed
FB23097100
for not being able to know whether a context menu is currently open, and
FB23102836
for improving the ergonomics of the toolbar API.
The context menu issue still feels especially frustrating to me. It is the kind of thing that only seems minor if you are not trying to build a proper Mac interface. On iOS, the system can visually lift the item involved in the interaction. On macOS, the app needs enough information to represent the target itself.
Regarding toolbars, WWDC 27 introduced a new
.visibilityPriority
modifier
that helps manage which items should move first to the overflow menu. This doesn't really help with my issue, but I felt I should mention it.
