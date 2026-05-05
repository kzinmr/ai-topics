---
title: "Randomize HN"
url: "https://danluu.com/randomize-hn/"
fetched_at: 2026-05-05T07:01:35.657740+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Randomize HN

Source: https://danluu.com/randomize-hn/

You ever notice that there's this funny threshold for getting to the front page on sites like HN? The exact threshold varies depending on how much traffic there is, but, for articles that aren't wildly popular, there's this moment when the article is at N-1 votes. There is, perhaps, a 60% chance that the vote will come and the article will get pushed to the front page, where it will receive a slew of votes. There is, maybe, a 40% chance it will never get the vote that pushes it to the front page, causing it to languish in obscurity forever.
It's non-optimal that an article that will receive 50 votes
in expectation
has a 60% chance of getting 100+ votes, and a 40% chance of getting 2 votes. Ideally, each article would always get its expected number of votes and stay on the front page for the expected number of time, giving readers exposure to the article in proportion to its popularity. Instead, by random happenstance, plenty of interesting content never makes it the front page, and as a result, the content that does make it gets a higher than optimal level of exposure.
You also see the same problem, with the sign bit flipped, on low traffic sites that push things to the front page the moment they're posted, like
lobste.rs
and
the smaller sub-reddits
: they displace links that most people would be interested in by putting links that almost no one cares about on the front page just so that the few things people do care about get enough exposure to be upvoted. On reddit, users "fix" this problem by heavily downvoting most submissions, pushing them off the front page, resulting in a problem that's fundamentally the same as the problem HN has.
Instead of implementing some simple and easy to optimize, sites pile on ad hoc rules. Reddit
implemented the rising page
, but it fails to solve the problem. On low-traffic subreddits, like
r/programming
the threshold is so high that it's almost always empty. On high-traffic sub-reddits, anything that's upvoted enough to make it to the rising page is already wildly successful, and whether or not an article becomes successful is heavily dependent on whether or not the first couple voters happen to be people who upvote the post instead of downvoting it, i.e., the problem of getting onto the rising page is no different than the problem of getting to the top normally.
HN tries to solve the problem by manually penalizing certain domains and keywords. That doesn't solve the problem for the 95% of posts that aren't penalized. For posts that don't make it to the front page, the obvious workaround is to
delete and re-submit your post if it doesn't make the front page the first time around
, but that's now
a ban worthy offense
. Of course, people are working around that, and HN has a workaround for the workaround, and so on. It's endless. That's the problem with "simple" ad hoc solutions.
There's an easy fix, but it's counter-intuitive. By adding a small amount of random noise to the rank of an article, we can smooth out the discontinuity between making it onto the front page and languishing in obscurity. The math is simple, but the intuition is even simpler. Imagine a vastly oversimplified model where, for each article, every reader upvotes with a fixed probability and the front page gets many more eyeballs than the new page. The result follows. If you like, you can work through the exercise with a more realistic model, but the result is the same.
Adding noise to smooth out a discontinuity is a common trick when you can settle for an approximate result. I recently employed it to work around the classic floating point problem, where adding a tiny number to a large number results in no change, which is problem when adding many small numbers to some large numbers. For a simple example of applying this, consider keeping a reduced precision counter that uses
loglog(n)
bits to store the value. Let
countVal(x) = 2^x
and
inc(x) = if (rand(2^x) == 0) x++
. Like understanding when to apply Taylor series, this is a simple trick that people are often impressed by if they haven't seen it before.
Update
: HN tried this! Dan Gackle tells me that it didn't work very well (it resulted in a lot of low quality junk briefly hitting the front page and then disappearing. I think that might be fixable by tweaking some parameters, but the solution that HN settled on, having a human (or multiple humans) put submissions that are deemed to be good or interesting into a "second chance queue" that boosts the submission onto the front page, works better than an a simple randomized algorithm with no direct human input could with any amount of parameter tweaking. I think this is also true of moderation, where the "new" dang/sctb moderation regime has resulted in a marked increase in comment quality, probably better than anything that could be done with an automated ML-based solution today — Google and FB have some of the most advanced automated systems in the world, and the quality of the result is much worse than what we see on HN.
Also, at the time this post was written (2013), the threshold to get onto the front page was often 2-3 votes, making the marginal impact of a random passerby who happens to like a submission checking the new page very large. Even during off peak times now (in 2019), the threshold seems to be much higher, reducing the amount of randomness. Additionally, the rise in the popularity of HN increased the sheer volume of low quality content that languishes on the new page, which would reduce the exposure that any particular "good" submisison would get if it were among the 30 items on the new page that would randomly get boosted onto the front page. That doesn't mean there aren't still problems with the current system: most people seem to upvote and comment based on the title of the article and not the content (to check this, read the comments of articles that are mistitled before someone calls this out for a partiular post — it's generally quite clear that most commenters haven't even skimmed the article, let alone read it), but that's a topic for a different post.
