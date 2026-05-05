---
title: "EuroLLVM 2013, Paris, France"
url: "https://blog.llvm.org/2013/05/eurollvm-2013-paris-france.html"
fetched_at: 2026-05-05T07:01:43.222265+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# EuroLLVM 2013, Paris, France

Source: https://blog.llvm.org/2013/05/eurollvm-2013-paris-france.html

EuroLLVM 2013, Paris, France
By rengolin
May 6, 2013
#devmtg
5 minute read
Two days after the end of EuroLLVM 2013, I finally got the energy to write a piece about it. It was a lot of hard work by an amazing team of volunteer organizers lead by Tobias Grosser, Duncan Sands, Sylvestre Ledru and Arnaud de Grandmaison, plus the usual suspects of the previous events, and in the end there was very little that had gone wrong, even in the slightest.
This was our biggest event yet, with 187 attendees, 12 talks, 2 tutorials, 7 lightning talks and 10 posters! The posters, slides and videos are available on the
EuroLLVM 2013 website
, as well as some idea on the abstracts, location (ENS, in Paris) and the great dinner cruise on Monday.
You can also find on the site the results of our questionnaire, distilled and anonymized.
The Talks
The two key notes received high approval ratings (90+% overall). The first was Chandler's, speaking about the missing optimizations still lurking, hinting which ones would be low-hanging fruit, and others that we just have to fix nonetheless. On the second day we had Jakob with a nice break-down of source code into machine code and how it's executed on modern CPUs. Despite their highly technical nature, the talks were delivered in an easy-to-understand format, which the audience didn't find daunting.
We also had many good talks, from Debug Information (Eric's) to PowerPC implementation (Ulrich's) to OpenMP support (Bokhanko & Bataev's), where the announcement that Intel had open sourced their OpenMP on a compatible BSD-license, which is always good news! There were also talks about tools (lld) and Clang usage (AST Tutorial, Pragma Handling).
Since we had two parallel tracks, I was worried that we'd get people divided and not get much visibility on the second track. Some people mentioned it on the questionnaire, but the number of reviews on both tracks are compatible, which shows that there was enough space and content for all tastes.
Other comments reinforced the idea to have more visibility on the official tools (lldb, bugpoint, lli) as well as more basic-level tutorials on how to use LLVM and tools, not just how to hack it. Let this be a lead to you (yes, you!) propose tutorials next time.
Lightning Talks and Posters
There were many interesting lightning talks, all very quick and efficiently exposed. Part of the reason why we had so many was that many of the talks that we couldn't fit were transformed into lightning talks, others in posters, others in both.
The idea was that, since a lightning talk can convey only a limited meaning, having a poster and specifically a poster session, was important to promote discussions between interested parties. That was actually very relevant, because some of the feedback was that there was little extra time to reinforce or create new connections.
Again, there were topics from optimizations (like adaptive parallelization, user-defined optimization, FDO) to tools (MCLinker) to builds (Debian+LLVM), but perhaps the most unusual of the talks was Henning's audio signal processing using LLVM and Haskell, in which we had a live demonstration of the hardware at work. It reminded me of early works from Kraftwerk.
Of the 91 questionnaires returned, 94% said lightning talks were important and 90% that they would want to have it again in future events. Part of this acceptance, I imagine, is due to the extra connection you have with the presenter
after
the presentation.
The Social
As highlighted above, there wasn't much time to socialize in between the talks, but there were specific coffee times, where the queue forced people to connect and meet others, the lunch time at the cafeteria, where finding a place to sit wasn't easy, so you'd end up sitting with completely unrelated people, and the amazing (let me say it again:
amazing
!) cruise dinner.
Floating easily through the Seine, admiring Paris' historical places from a very interesting point of view, we had a great meal and an enjoyable evening. I'd really like to thanks again our sponsors for providing such a great way to end a conference day.
As some have pointed out, the only down-side of the dinner was that the social part fell a bit short, since most people haven't left their tables for the duration of the trip (I have, but I was taking the pictures!), which hindered a bit the
social
part of the event.
But, to be honest, that wasn't so bad, since most (I really mean
most
) of the people decided to walk to the river, spending no less than 1 hour together, enjoying the scenery and each others company.
Prize Draw and Wrapping Up
After the last session, just before the event ended, a great Parot headphone was delivered to Ahmed, who won the lottery.
From my point of view, this was a very successful event, proof that Europe also has interesting LLVM engineering going on. It's also getting in shape with what people hope to find at these events, following the acceptance rates of talks and organization issues.
With offers to help all over Europe (and beyond!), I wonder where the next EuroLLVM will be... But one thing I know: it's going to be great! :-)
