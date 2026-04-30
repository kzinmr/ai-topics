---
title: "Never Use the Confirm Dialog"
url: "https://danieldelaney.net/confirm/"
fetched_at: 2026-04-30T07:00:42.129246+00:00
source: "danieldelaney.net"
tags: [blog, raw]
---

# Never Use the Confirm Dialog

Source: https://danieldelaney.net/confirm/

It’s a standard function of all browsers, it’s everywhere, and it’s time to retire it. Here’s an example from
JIRA
. Trying to “Cancel” a comment brings up
the confirm dialog
:
Even if we assume confirmation is necessary, the standard confirm dialog is a bad way to get it:
Most of what’s shown is
junk
.
The browser logo, the URL of the page, the paragraph that nobody reads—none of it helps me cancel the comment. The buttons are what matter.
“OK” is ambiguous.
Buttons should say what they do. If an action is important enough to need confirmation, it’s important enough to need a clear label.
“Cancel” is ambiguous.
Clicking “Cancel” doesn’t cancel my comment. It cancels cancelation. Whoops.
Forcing my hand isn’t nice.
This dialog hijacks the whole page. There’s a friendlier way to prevent errors.
With little effort we can make the dialog better. Let’s do it. We’ll use more thoughtful labeling to make the behavior clearer. For an added bonus, we can use color to highlight the riskier option:
Already we’ve done better than the confirm dialog. But let’s not open the champagne yet. We can do even better. We’re still freezing the page every time the user clicks “Cancel”. This interrupts the user, second-guesses his decisions, and makes him repeat himself. Why shouldn’t we let him work, and provide the tools to reverse mistakes?
Gmail
does this to great effect:
Sorry, this video didn’t work.
A confirmation might be necessary in some circumstances. In others, an undo might be best. Either way, the standard confirm dialog is never the best option. Conciseness is always better than clutter. Clear labels are always better than generic ones. Never use the confirm dialog.
