---
title: "The Brain Sandwich"
url: "https://terriblesoftware.org/2026/10/02/the-brain-sandwich/"
fetched_at: 2026-10-03T10:01:01.035762+00:00
source: "terriblesoftware.org"
tags: [blog, raw]
---

# The Brain Sandwich

Source: https://terriblesoftware.org/2026/10/02/the-brain-sandwich/

I was on a 1:1 with Emily, one of our strongest engineers, and we were mostly venting about some of the negatives about AI these days: the crazy amount of code reviews, how the job is changing, and the last one (which is the most relevant for this post), how engineers are sometimes
completely removing their brains from the equation
and just delegating their entire work to AI.
(Btw, I heard that the cool kids are calling this a
Meat Proxy
.)
But anyway, the reason I decided to post about this is that Emily has a very simple framework that she uses for working with AI, which she calls the “Brain Sandwich”, that solves this. It’s
both
about taking full advantage of AI without letting your engineering skills atrophy.
The idea is very simple, and can be summarized by: whenever you work on something, you should use:
Your brain,
and then
AI,
and then
Your brain
Explaining a bit more…
Before you tell the agent to start building anything, you go there and read and understand it
first
.
You don’t need a complete implementation plan, but you need a rough idea of where you’re going. Otherwise, AI can bias you in the wrong direction. Or even worse, it can nudge you into building something that wasn’t even a problem you needed to solve in the first place!
Now that you have all this context,
that’s
the time to bring AI. By all means, do it. Fully delegate this part with no shame! And when the agent brings you the solution, you will know if it’s right, or if it’s too much, or if it’s completely solving the wrong problem, etc.
Then, at the end, your brain comes back. Because before sending your stuff to other people for review, you need to make the work
reviewable
. Read the diff, check if the complexity is worth it in this case, improve the freaking PR description, etc. The rule of thumb is: if you can’t explain what’s changing and why, it’s not ready for someone else to take a look.
