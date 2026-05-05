---
title: "Major errors on this blog (and their corrections)"
url: "https://danluu.com/corrections/"
fetched_at: 2026-05-05T07:01:30.194946+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Major errors on this blog (and their corrections)

Source: https://danluu.com/corrections/

Here's a list of errors on this blog that I think were fairly serious. While what I think of as serious is, of course, subjective, I don't think there's any reasonable way to avoid that because, e.g., I make a huge number of typos, so many that the majority of acknowledgements on many posts are for people who e-mailed or DM'ed me typo fixes.
A list that included everything, including typos would both be uninteresting for other people to read as well as high overhead for me, which is why I've drawn the line somewhere. An example of an error I don't think of as serious is,
in this post on how I learned to program
, I originally had the dates wrong on when the competition programmers from my high school made money (it was a couple years after I thought it was). In that case, and many others, I don't think that the date being wrong changes anything significant about the post.
Although I'm publishing the original version of this in 2021, I expect this list to grow over time. I hope that I've become more careful and that the list will grow more slowly in the future than it has in the past, but that remains to be seen. I view it as a good sign that a large fraction of the list is from my first three months of blogging, in 2013, but that's no reason to get complacent!
I've added a classification below that's how I think of the errors, but that classification is also arbitrary and the categories aren't even mutually exclusive. If I ever collect enough of these that it's difficult to hold them all in my head at once, I might create a tag system and use that to classify them instead, but I hope to not accumulate so many major errors that I feel like I need a tag system for readers to easily peruse them.
Insufficient thought
2013
:
Using random algorithms to decrease the probability that good stories get "unlucky" on HN
: this idea was tried and didn't work well as well as putting humans in the loop who decide which stories should be rescued from oblivion.
Since this was a proposal and not a claim, this technically wasn't an error since I didn't claim that this would definitely work, but my feeling is that I should've also considered solutions that put humans in the loop. I didn't because Digg famously got a lot of backlash for having humans influence their front page but, in retrospect, we can see that it's possible to do so in a way that doesn't generate backlash that effective kills the site and I think this could've been predicted with enough thought
Naivete
2013
:
The institution knowledge and culture that create excellence can take a long time to build up
: At this time, I hadn't worked in software and that thought that this wasn't as difficult for software because so many software companies are successful with new/young teams. But, in retrospect, the difference isn't that those companies don't produce bad (unreliable, buggy, slow, etc.) software, it's that product/market fit and network effects are important enough that it frequently doesn't matter that software is bad
2015
:
In this post on how people don't read citations
, I found it mysterious that type system advocates would cite non-existent strong evidence, which seems unlike the other examples, where people pass on a clever, contrarian, result without ever having read it. The thing I thought was mysterious was that, unlike the other examples, there isn't an incorrect piece of evidence being passed around; the assertion that there is evidence is disconnected from any evidence, even misinterpreted evidence. In retrospect, I was being naive in thinking that there was a link to evidence that people wouldn't just fabricate the idea that there is evidence supporting their belief and then pass that around.
Insufficient verification of information
2016
:
Building a search engine isn't trivial
: although I think the overall point is true, one of the pieces of evidence I relied on came out of using numbers that someone who worked on a search engine told me about. But when I measured actual numbers, I found that the numbers I was told were off by multiple orders of magnitude
2022
:
Futurist predictions
, pointed out to me by @ESRogs: I misread nostalgebraist's summary of a report and didn't understand what he was saying with respect to a sensitivity analysis he was referring to. I distinctly remember not being sure what nostaglebraist was saying and originally agreed with the correct interpretation. After re-reading it, I came away with my mistaken reading, which I then wrote into my post. That I had uncertainty about the reading should've caused me to just reproduce his analysis, which would have immediately clarified what he meant, but I didn't do that. This error didn't fundamentally change my own analysis since the broader point I was making didn't hinge on the exact numbers, but I think it's a very bad habit to allow yourself to publish something with the level of uncertainty I had without noting the uncertainty (quite an ironic mistake considering the contents of the post itself). A factor that both led to the mistake in the first place as well as to not checking the math in a way that would've spotted the mistake is that the edits that introduced this mistake were a last-minute change introduced when I had a short window of time to make the changes if I wanted to publish immediately and not some time significantly later. Of course, that should have led to me delaying publication, so this was one bad decision that led to another
Blunder
2015
:
Checking out Butler Lampson's review of what worked in CS, 16 years later
: it was wrong to say that capabilities were a "no" in 2015 given their effectiveness on mobile and that seems so obviously wrong at the time that I would call this a blunder rather than something where I gave it a decent amount of thought but should've thought through it more deeply
2024
:
Diseconomies of scale
: I mixed up which number I was dividing by which when doing arithmetic, causing a multiple order of magnitude error in a percentage. Sophia Wisdom noticed this a few hours after the post was published and I fixed it immediately , but this quite a silly error.
Pointlessly difficult to understand explanation
Errors in retrospect
2015
:
Blog monetization
: I grossly underestimated how much
I could make on Patreon
by looking at how much Casey Muratori, Eric Raymond, and eevee were making on Patreon at the time. I thought that all three of them would out-earn me based for a variety of reasons and that was incorrect. A major reason that was incorrect was that boring, long-form, writing monetizes much better than I exepected, which means that I monetarily undervalued that compared to what other tech folks are doing.
A couple weeks ago, I added a link to Patreon at the top of posts (instead of just having one hidding at the bottom) and mentioned having a Patreon on Twitter. Since then, my earnings have increased by about as much as Eric Raymond makes in total and the amount seems to be increasing at a decent rate, which is a result I wouldn't have expected before the rise of substack. But anyone who realized how well individual writers can monetize their writing could've created substack and no one did until Chris Best, Hamish McKenzie, and Jairaj Sethi created substack, so I'd say that this one was somewhat non-obvious. Also,
it's unclear if the monetization is going to scale up or will plateau
; if it plateaus, then my guess would only be off by a small constant factor.
Thanks to Anja Boskovic and Ville Sundberg for comments/corrections/discussion.
