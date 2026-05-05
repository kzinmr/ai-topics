---
title: "research!rsc: Go and Dogma"
url: "https://research.swtch.com/dogma"
fetched_at: 2026-05-05T07:01:01.553529+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# research!rsc: Go and Dogma

Source: https://research.swtch.com/dogma

Go and Dogma
Russ Cox
January 9, 2017
research.swtch.com/dogma
Posted on Monday, January 9, 2017.
[
Cross-posting from last year’s
Go contributors AMA
on Reddit, because it’s still important to remember.
]
One of the perks of working on Go these past years has been the chance to have many great discussions with other language designers and implementers, for example about how well various design decisions worked out or the common problems of implementing what look like very different languages (for example both Go and Haskell need some kind of “green threads”, so there are more shared runtime challenges than you might expect). In one such conversation, when I was talking to a group of early Lisp hackers, one of them pointed out that these discussions are basically never dogmatic. Designers and implementers remember working through the good arguments on both sides of a particular decision, and they’re often eager to hear about someone else’s experience with what happens when you make that decision differently. Contrast that kind of discussion with the heated arguments or overly zealous statements you sometimes see from users of the same languages. There’s a real disconnect, possibly because the users don’t have the experience of weighing the arguments on both sides and don’t realize how easily a particular decision might have gone the other way.
Language design and implementation is engineering. We make decisions using evaluations of costs and benefits or, if we must, using predictions of those based on past experience. I think we have an important responsibility to explain both sides of a particular decision, to make clear that the arguments for an alternate decision are actually good ones that we weighed and balanced, and to avoid the suggestion that particular design decisions approach dogma. I hope
the Reddit AMA
as well as discussion on
golang-nuts
or
StackOverflow
or the
Go Forum
or at
conferences
help with that.
But we need help from everyone. Remember that none of the decisions in Go are infallible; they’re just our best attempts at the time we made them, not wisdom received on stone tablets. If someone asks why Go does X instead of Y, please try to present the engineering reasons fairly, including for Y, and avoid argument solely by appeal to authority. It’s too easy to fall into the “well that’s just not how it’s done here” trap. And now that I know about and watch for that trap, I see it in nearly every technical community, although some more than others.
