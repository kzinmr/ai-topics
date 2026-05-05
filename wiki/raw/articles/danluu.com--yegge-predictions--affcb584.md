---
title: "Steve Yegge's prediction record"
url: "https://danluu.com/yegge-predictions/"
fetched_at: 2026-05-05T07:01:33.149157+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Steve Yegge's prediction record

Source: https://danluu.com/yegge-predictions/

I try to avoid making predictions. It's a no-win proposition: if you're right,
hindsight bias
makes it look like you're pointing out the obvious. And most predictions are wrong. Every once in a while when someone does a review of predictions from pundits, they're almost always wrong at least as much as you'd expect from random chance, and then hindsight bias makes each prediction look hilariously bad.
But, occasionally, you run into someone who makes pretty solid non-obvious predictions. I was re-reading some of Steve Yegge's old stuff and it turns out that he's one of those people.
His most famous prediction is probably
the rise of JavaScript
. This now seems incredibly obvious in hindsight, so much so that the future laid out in Gary Bernhardt's
Birth and Death of JavaScript
seems at least a little plausible. But you can see how non-obvious Steve's prediction was at the time by reading both the comments on his blog, and comments from HN, reddit, and the other usual suspects.
Steve was also crazy-brave enough to
post ten predictions about the future
in 2004. He says “Most of them are probably wrong. The point of the exercise is the exercise itself, not in what results.”, but the predictions are actually pretty reasonable.
Prediction #1: XML databases will surpass relational databases in popularity by 2011
2011 might have been slightly too early and JSON isn't exactly XML, but NoSQL databases have done really well for pretty much the reason given in the prediction, “Nobody likes to do O/R mapping; everyone just wants a solution.”. Sure,
Mongo may lose your data, but it's easy to set up and use
.
Prediction #2: Someone will make a lot of money by hosting open-source web applications
This depends on what you mean by “a lot”, but this seems basically correct.
We're rapidly entering the age of hosted web services, and big companies are taking advantage of their scalable infrastructure to host data and computing for companies without that expertise.
For reasons that seem baffling in retrospect, Amazon understood this long before any of its major competitors and was able to get a huge head start on everybody else. Azure didn't get started until 2009, and Google didn't get serious about public cloud hosting until even later.
Now that everyone's realized what Steve predicted in 2004, it seems like every company is trying to spin up a public cloud offering, but the market is really competitive and hiring has become extremely difficult. Despite giving out a large number of offers an integer multiple above market rates, Alibaba still hasn't managed to put together a team that's been able to assemble a competitive public cloud, and companies that are trying to get into the game now without as much cash to burn as Alibaba are having an even harder time.
For both bug databases and source-control systems, the obstacle to outsourcing them is trust. I think most companies would love it if they didn't have to pay someone to administer Bugzilla, Subversion, Twiki, etc. Heck, they'd probably like someone to outsource their email, too.
A lot of companies have moved both issue tracking and source-control to GitHub or one of its competitors, and even more have moved if you just count source-control. Hosting your own email is also a thing of the past for all but the most paranoid (or most bogged down in legal compliance issues).
Prediction #3: Multi-threaded programming will fall out of favor by 2012
Hard to say if this is right or not. Depends on who you ask. This seems basically right for applications that don't need the absolute best levels for performance, though.
In the past, oh, 20 years since they invented threads, lots of new, safer models have arrived on the scene. Since 98% of programmers consider safety to be unmanly, the alternative models (e.g. CSP, fork/join tasks and lightweight threads, coroutines, Erlang-style message-passing, and other event-based programming models) have largely been ignored by the masses, including me.
Shared memory concurrency is still where it's at for really high performance programs, but Go has popularized CSP; actors and futures are both “popular” on the JVM; etc.
Prediction #4: Java's "market share" on the JVM will drop below 50% by 2010
I don't think this was right in 2010, or even now, although we're moving in the right direction. There's a massive amount of dark matter -- programmers who do business logic and don't blog or give talks -- that makes this prediction unlikely to come true in the near future.
It's impossible to accurately measure market share, but basically every language ranking you can find will put
Java in the top 3, with Scala and Clojure not even in the top 10
. Given the near power-law distribution of measured language usage, Java must still be above 90% share (and that's probably a gross underestimate).
Prediction #5: Lisp will be in the top 10 most popular programming languages by 2010
Not even close. Depending on how you measure this, Clojure might be in the top 20 (it is if you believe the Redmonk rankings), but it's hard to see it making it into the top 10 in this decade. As with the previous prediction, there's just way too much inertia here. Breaking into the top 10 means joining the ranks of Java, JS, PHP, Python, Ruby, C, C++, and C#. Clojure just isn't boring enough. C# was able to sneak in by pretending to boring, but Clojure's got no hope of doing that and there isn't really another Dylan on the horizon.
Prediction #6: A new internet community-hangout will appear. One that you and I will frequent
This seems basically right, at least for most values of “you”.
Wikis, newsgroups, mailing lists, bulletin boards, forums, commentable blogs — they're all bullshit. Home pages are bullshit. People want to socialize, and create content, and compete lightly with each other at different things, and learn things, and be entertained: all in the same place, all from their couch. Whoever solves this — i.e. whoever creates AOL for real people, or whatever the heck this thing turns out to be — is going to be really, really rich.
Facebook was founded the year that was written. Zuckerberg is indeed really, really, rich.
Prediction #7: The mobile/wireless/handheld market is still at least 5 years out
Five years from Steve's prediction would have been 2009. Although the iPhone was released in 2007, it was a while before sales really took off. In 2009, the majority of phones were feature phones, and Android was barely off the ground.
Note that this graph only runs until 2013; if you graph things
up to 2015
on a linear scale, sales are so low in 2009 that you basically can't even see what's going on.
Prediction #8: Someday I will voluntarily pay Google for one of their services
It's hard to tell if this is correct (Steve, feel free to
let me know
), but it seems true in spirit. Google has more and more services that they charge for, and they're even experimenting with
letting people pay to avoid seeing ads
.
Prediction #9: Apple's laptop sales will exceed those of HP/Compaq, IBM, Dell and Gateway combined by 2010
If you include tablets, Apple hit #1 in the market by 2010, but I don't think they do better than all of the old workhorses combined. Again, this seems to underestimate the effect of dark matter, in this case, people buying laptops for boring reasons, e.g., corporate buyers and normal folks who want something under Apple's price range.
Prediction #10: In five years' time, most programmers will still be average
More of a throwaway witticism than a prediction, but sure.
That's a pretty good set of predictions for 2004. With the exception of the bit about Lisp, all of the predictions seem directionally correct; the misses are mostly caused by underestimating the sheer about of inertia it takes for a young/new solution to take over.
Steve also has a number of posts that aren't explicitly about predictions that, nevertheless, make pretty solid predictions about how things are today, written way back in 2004. There's
It's Not Software
, which was years ahead of its time about how people write “software”, how writing server apps is really different from writing shrinkwrap software in a way that obsoletes a lot of previously solid advice, like Joel's dictum against rewrites, as well as how service oriented architectures look;
the Google at Delphi
(again from 2004) correctly predicts the importance of ML and AI as well as Google's very heavy investment in ML; an
old interview where he predicts
"web application programming is gradually going to become the most important client-side programming out there. I think it will mostly obsolete all other client-side toolkits: GTK, Java Swing/SWT, Qt, and of course all the platform-specific ones like Cocoa and Win32/MFC/"; etc. A number of Steve's internal Google blog posts also make interesting predictions, but AFAIK those are confidential. Of course these all these things seem obvious in retrospect, but that's just part of Steve's plan to pass as a normal human being.
In
a relatively recent post
, Steve throws Jeff Bezos under the bus, exposing him as one of a number of “hyper-intelligent aliens with a tangential interest in human affairs”. While the crowd focuses on Jeff, Steve is able to sneak out the back. But we're onto you, Steve.
Thanks to Leah Hanson, Chris Ball, Mindy Preston, and Paul Gross for comments/corrections.
