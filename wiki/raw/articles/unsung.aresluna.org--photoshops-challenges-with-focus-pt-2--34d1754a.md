---
title: "Photoshop’s challenges with focus, pt. 2"
url: "https://unsung.aresluna.org/photoshops-challenges-with-focus-pt-2/"
fetched_at: 2026-05-05T07:00:57.824676+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Photoshop’s challenges with focus, pt. 2

Source: https://unsung.aresluna.org/photoshops-challenges-with-focus-pt-2/

First of all, correction
for part 1
– the “focus mode” wasn’t removed. It was renamed to “quiet mode” and relocated to a different part of the UI, and I failed to spot it there. It’s still slightly perplexing, shiftily capitalized, and I doubt fully effective, but the effort is there:
I also want to warn you there will be no more positive things I say in this post.
When Cabel Sasser
posted this on Bluesky in February
…
…I experienced a little existential dread.
Now that I’ve experienced the dialog myself in Photoshop 2026, and a few other dialogs that have been upgraded toward what Adobe calls “modern user interface,” how did it fare?
These are 2025 windows and their 2026 equivalents:
On the surface, it feels like a lateral move. I do not personally find the new design language (Spectrum) attractive, or even particularly “modern.” The gestalt remains off and things are still generally misaligned – they’re just misaligned in net new ways.
But it was digging into the window below that showed all the problems in the still-wet foundations…
…and a lot of them have to do with focus.
1.
The first field is not focused, so you cannot start typing the number after opening this window. You need to immediately move your hand to the mouse.
2.
If you click on any field, the value is not pre-selected, so you cannot start typing a new number then.
A combination of both is rough in practice in repeated use, violating some of the basic things like
this classic principle of interaction design
:
Principle: Defaults within fields should be easy to “blow away”
When a user activates a field, the current entry should be auto-selected so that pressing Backspace/​Delete or starting to type will eliminate the current entry. Users can click within the field to deselect the whole, dropping the text pointer exactly where the user has clicked. The select-on-entry rule is generally followed today. (Sloppy coding, however, has resulted in the text cursor dropping at various unpredictable locations. )
3.
Clicking on parts of the input field doesn’t bring it into focus even though the hover state promises it. (Discrepancies between hover and focus handling are a horrible new thing I’m starting to see more in recent interfaces.)
4.
Simply backspacing through the field shows a crude error modal and – to add a second injury to the first injury – the dialog removes focus from the field!
5.
Tabbing now goes through “Pixels” menu on the way from Width to Height, making it harder to type width → press Tab → type height → press Enter, in a nice quick keyboard gesture.
I will recognize this is a tricky one, because it exposes a core tension with tabbing: some people use it for comprehensive keyboard access, but others want an accelerator “express train” with only relevant stops. However, macOS already has a “Keyboard navigation”
setting
for that – you can choose whether tabbing should go through all the controls, or only those you get to type in. Not only does Photoshop ignore that preference, but it’s inconsistent with itself – you can see that you cannot get to Anchor via tabbing anyway!
6.
Clicking on the “relative” checkbox or canvas extension color does not restore focus to last control like it used to.
7–∞.
There are tons of other transgressions. Some are downwind from focus; for example, undoing after moving a slider no longer works, because the ⌘Z keystroke is now swallowed by a UI element that doesn’t know what to do with it. Some are unrelated: Pull-downs are now
of the slower kind
, pressing ⌥P results in more blinking, and this tooltip below feels so
cheap
that I’m surprised it’s not a talking point of the current U.S. administration:
I am tired even just
noticing
all this. (What is that weird clump of pixels on the left of the bottom edge!? Did no one spot it before launch?)
So now what?
I generally avoid such harsh labels on this blog, but:
this is awful work
.
I’m angry. (Clearly.) We should all be angry in the face of stuff like this. This is how people get fed up with software – because it feels unstable and deteriorates on its own
without needing to
.
I know I
brought up
that an existing power user base can be a huge pain in the ass, and I am a decades-old Photoshop power user. But this is different than other examples where the product needs or at least wants to evolve past its core audience or toward a different market. For Photoshop here, nothing I see indicates any change in course or clientele – and yet all of these good moments in UI that used to help me out no longer exist.
Plus, all those transgressions are solved problems. Those issues are not buried in pages of heavily litigated patents, or in seven collective brains of world-class interface designers whose driveways are presently occupied by cash-filled trucks sent over by frontier companies. This isn’t some long lost art that requires archaeologists to decipher. This feels like carelessness and laziness in face of basic UI engineering; in a likely internally-motivated effort to refresh the interface, the team threw an entire nursery worth of babies with the bathwater.
It’s not just about disservice to craft. It’s not even about disrespect for change management, trivialization of institutional memory, and disinvestment in quality assurance. This isn’t only, in Tog’s words above, “sloppy coding.” This is also
a failure of
imagination
. It’s not that hard to picture people spending 8+ hours a day going through these windows for years if not decades to come, and it’s not hard to add and multiply all of these microfrustrations into numbers that should make one pause. With these many paper cuts, you need to start thinking about establishing a blood bank. How can you expect people to use a professional tool effectively if you throw in so many roadblocks?
In an internally-motivated UI refresh like this, you not only need to meet users where they used to be, you also ideally have to give them
more
to cover for the pains of change. Sometimes that “more” is better storytelling – here, no one even tried to really sell me on the new interface – but ideally “more” means actual felt improvements. I’m not on the team, but it’s not that hard to imagine some of them:
Change those annoying modals that announce typing errors into something lighter and more modern, like attached tooltips.
Add more comprehensive equation support so e.g. I could type “660*2” like I can in increasingly more and more apps.
Announce the invisible shortcuts
that already exist
, or add a few ones.
Add a bit of memory/​stickiness to some options (like Use Legacy in the first window), so I don’t have to keep toggling them over and over again.
I started this post talking about a setting, and there is another setting in Photoshop, buried on the last page – you can turn off this “modern user interface” that feels so underbaked the moment you start actually using it. But is that a real solution to anything? Toggle it on and the existential dread comes back: Am I going to miss out on some good stuff? When is the hammer going to drop? It’s not a tax break, it’s only a tax extension.
Even this view above shows so little care, it would ordinarily deserve its own post.
