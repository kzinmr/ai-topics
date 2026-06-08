---
title: "SwiftUI Only Makes It Easy to Develop Bad Apps"
url: "https://daringfireball.net/2026/06/swiftui_only_makes_it_easy_to_develop_bad_apps"
fetched_at: 2026-06-08T07:01:15.409508+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# SwiftUI Only Makes It Easy to Develop Bad Apps

Source: https://daringfireball.net/2026/06/swiftui_only_makes_it_easy_to_develop_bad_apps

SwiftUI Only Makes It Easy to Develop Bad Apps
Sunday, 7 June 2026
Paulo Andrade, last month, “
Using SwiftUI to Build a Mac-Assed App in 2026
”:
I recently launched the macOS version of
Shopie
, an app I first
released on the iOS App Store late last year. Shopie helps you
keep track of products you’re interested in by letting you create
wishlists and notifying you whenever a product’s price,
availability, and other details change.
Unlike my other apps, where I typically blend AppKit (or UIKit)
with SwiftUI, Shopie is built entirely in SwiftUI. I wanted to
keep it that way to maximize code reuse across iOS, iPadOS, and
now macOS. This post explores how far SwiftUI can take you on the
Mac in 2026, especially if your goal is to build an app that feels
truly native to the platform. It’s not meant to be an exhaustive
review of SwiftUI on macOS. It’s simply a collection of recipes
and issues I ran into while porting
Shopie
, a fairly small app,
and keeping it 100% SwiftUI.
Andrade’s examples are copious. His conclusion is damning:
Apple dropped the ball here. AppKit was ahead of its time and
UIKit was a more polished version of AppKit. A serious
cross-platform framework that unified the two should have happened
long before SwiftUI. Instead, Apple left AppKit to fossilize and
then tried to leapfrog the problem.
You can see the result everywhere. SwiftUI is productive, modern,
and often delightful, right up until you try to make a really good
Mac app. Then suddenly you’re fighting the framework for things
the Mac solved 20 years ago.
There’s something really wrong with SwiftUI. Amongst the apps I use, the best example is Apple Journal. Basic stuff that’s worked reliably for decades — some things that heretofore had worked forever — are dangerously broken. If you’re running MacOS 26 Tahoe, open Journal and make a new dummy entry. Type something like “The quick brown fox.” Then double-click on the word “brown” and delete it. Now invoke Undo.
What you expect is for the word “brown” to reappear. What happens is ...
the whole sentence disappears
. Gone. Invoke Redo and you only get back to “The quick fox.” The word “brown” is just gone forever. It’s nowhere in the Undo stack. That’s just profoundly fucked up. I’ve never seen anything like this with an AppKit app, ever. (I’ve never seen it with a UIKit app either — and the same thing happens on iOS with Journal. It’s just that you notice it less often because we don’t invoke Undo and Redo nearly as often there.)
I actually use the Journal app and I’ve lost entire sentences of text to this incompetent implementation of Undo. Editing text in Journal is
dangerous
because SwiftUI is so bad at something as fundamental as text editing. AppKit has had this solved since 1989 or so, a decade before Apple reunified with NeXT. And my example here is just one of many. Andrade documents a whole bunch more in his post.
Shopie
is a good modern Mac app — you can practically see from reading his post that Andrade’s hands are scarred from dozens of paper cuts.
So while the world is largely focused on Apple’s AI-related announcements at WWDC tomorrow, I’ve got SwiftUI (on all platforms) and Mac-assed Mac development high on my list. Apple’s developer message used to be that it was not just easy to develop apps for their platforms, but that it was easy to develop
good idiomatically native
apps. You got the correct complex behavior — for things like Undo/Redo — out of the box. That’s still true for AppKit and UIKit, but it’s never been true for SwiftUI, and
SwiftUI is now seven years old
. That’s too long for any excuses to hold water.
