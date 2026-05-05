---
title: "A review of the Julia language"
url: "https://danluu.com/julialang/"
fetched_at: 2026-05-05T07:01:33.523614+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# A review of the Julia language

Source: https://danluu.com/julialang/

Here's a language that gives near-C performance that feels like Python or Ruby with optional type annotations (that you can feed to
one of two
static analysis tools
) that has good support for macros plus decent-ish support for FP, plus a lot more. What's not to like? I'm mostly not going to talk about how great Julia is, though, because you can find plenty of blog posts that do that all over the internet.
The last time I used Julia (around Oct. 2014), I ran into two new (to me) bugs involving bogus exceptions when processing Unicode strings. To work around those, I used a try/catch, but of course that runs into a non-deterministic bug I've found with try/catch. I also hit a bug where a function returned a completely wrong result if you passed it an argument of the wrong type instead of throwing a "no method" error. I spent half an hour writing a throwaway script and ran into four bugs in the core language.
The second to last time I used Julia, I ran into too many bugs to list; the worst of them caused generating plots to take 30 seconds per plot, which caused me to switch to R/ggplot2 for plotting. First there was this bug with
plotting dates didn't work
. When I worked around that I ran into a regression that caused plotting to
break large parts of the core language
, so that data manipulation had to be done before plotting. That would have been fine if I knew exactly what I wanted, but for exploratory data analysis I want to plot some data, do something with the data, and then plot it again. Doing that required restarting the REPL for each new plot. That would have been fine, except that it takes 22 seconds to load Gadfly on my 1.7GHz Haswell (timed by using
time
on a file that loads Gadfly and does no work), plus another 10-ish seconds to load the other packages I was using, turning my plotting workflow into: restart REPL, wait 30 seconds, make a change, make a plot, look at a plot, repeat.
It's not unusual to run into bugs when using a young language, but Julia has more than its share of bugs for something at its level of maturity. If you look at the test process, that's basically inevitable.
As far as I can tell, FactCheck is the most commonly used thing resembling a modern test framework, and it's barely used. Until quite recently, it was unmaintained and broken, but even now the vast majority of tests are written using
@test
, which is basically an assert. It's theoretically possible to write good tests by having a file full of test code and asserts. But in practice, anyone who's doing that isn't serious about testing and isn't going to write good tests.
Not only are existing tests not very good, most things aren't tested at all. You might point out that the coverage stats for a lot of packages aren't so bad, but last time I looked, there was a bug in the coverage tool that caused it to only aggregate coverage statistics for functions with non-zero coverage. That is to say, code in untested functions doesn't count towards the coverage stats! That, plus the weak notion of test coverage that's used (line coverage) make the coverage stats unhelpful for determining if packages are well tested.
The lack of testing doesn't just mean that you run into regression bugs. Features just disappear at random, too. When the REPL got rewritten a lot of existing shortcut keys and other features stopped working. As far as I can tell, that wasn't because anyone wanted it to work differently. It was because there's no way to re-write something that isn't tested without losing functionality.
Something that goes hand-in-hand with the level of testing on most Julia packages (and the language itself) is the lack of a good story for error handling. Although you can easily use
Nullable
(the Julia equivalent of
Some/None
) or error codes in Julia, the most common idiom is to use exceptions. And if you use things in
Base
, like arrays or
/
, you're stuck with exceptions. I'm
not a fan
, but that's fine -- plenty of reliable software uses exceptions for error handling.
The problem is that because the niche Julia occupies doesn't care about error handling, it's extremely difficult to write a robust Julia program. When you're writing smaller scripts, you often want to “fail-fast” to make debugging easier, but for some programs, you want the program to do something reasonable, keep running, and maybe log the error. It's hard to write a robust program, even for this weak definition of robust. There are problems at multiple levels. For the sake of space, I'll just list two.
If I'm writing something I'd like to be robust, I really want function documentation to include all exceptions the function might throw. Not only do the Julia docs not have that, it's common to call some function and get a random exception that has to do with an implementation detail and nothing to do with the API interface. Everything I've written that actually has to be reliable has been exception free, so maybe that's normal when people use exceptions? Seems pretty weird to me, though.
Another problem is that catching exceptions doesn't work (sometimes, at random). I ran into one bug where using exceptions caused code to be incorrectly optimized out. You might say that's not fair because it was
caught using a fuzzer
, and fuzzers are supposed to find bugs, but the fuzzer wasn't fuzzing exceptions or even expressions. The implementation of the fuzzer just happens to involve eval'ing function calls, in a loop, with a
try/catch
to handle exceptions. Turns out, if you do that, the function might not get called. This isn't a case of using a fuzzer to generate billions of tests, one of which failed. This was a case of trying one thing, one of which failed. That bug is now fixed, but there's still a nasty bug that causes exceptions to sometimes fail to be caught by
catch
, which is pretty bad news if you're putting something in a
try/catch
block because you don't want an exception to trickle up to the top level and kill your program.
When I grepped through
Base
to find instances of actually catching an exception and doing something based on the particular exception, I could only find a single one. Now, it's me scanning grep output in less, so I might have missed some instances, but it isn't common, and grepping through common packages finds a similar ratio of error handling code to other code. Julia folks don't care about error handling, so it's buggy and incomplete. I once asked about this and was told that it didn't matter that exceptions didn't work because you shouldn't use exceptions anyway -- you should use Erlang style error handling where you kill the entire process on an error and build transactionally robust systems that can survive having random processes killed. Putting aside the difficulty of that in a language that doesn't have Erlang's support for that kind of thing, you can easily spin up a million processes in Erlang. In Julia, if you load just one or two commonly used packages, firing up a single new instance of Julia can easily take half a minute or a minute. To spin up a million independent instances would at 30 seconds a piece would take approximately two years.
Since we're broadly on the topic of APIs, error conditions aren't the only place where the
Base
API leaves something to be desired. Conventions are inconsistent in many ways, from function naming to the order of arguments. Some methods on collections take the collection as the first argument and some don't (e.g., replace takes the string first and the regex second, whereas match takes the regex first and the string second).
More generally,
Base
APIs outside of the niche Julia targets often don't make sense. There are too many examples to list them all, but consider this one: the UDP interface throws an exception on a partial packet. This is really strange and also unhelpful.
Multiple people stated that on this issue
but the devs decided to throw the exception anyway. The Julia implementers have great intuition when it comes to linear algebra and other areas they're familiar with. But they're only human and their intuition isn't so great in areas they're not familiar with. The problem is that they go with their intuition anyway, even in the face of comments about how that might not be the best idea.
Another thing that's an issue for me is that I'm not in the audience the package manager was designed for. It's backed by git in a clever way that lets people do all sorts of things I never do. The result of all that is that it needs to do
git status
on each package when I run
Pkg.status()
, which makes it horribly slow; most other
Pkg
operations I care about are also slow for a similar reason.
That might be ok if it had the feature I most wanted, which is the ability to specify exact versions of packages and have multiple, conflicting, versions of packages installed. Because of all the regressions in the core language libraries and in packages, I often need to use an old version of some package to make some function actually work, which can require old versions of its dependencies. There's no non-hacky way to do this.
Since I'm talking about issues where I care a lot more than the core devs, there's also benchmarking. The website shows off some impressive sounding speedup numbers over other languages. But they're all benchmarks that are pretty far from real workloads. Even if you have a strong background in workload characterization and systems architecture (computer architecture, not software architecture), it's difficult to generalize performance results on anything resembling real workload from microbenchmark numbers. From what I've heard, performance optimization of Julia is done from a larger set of similar benchmarks, which has problems for all of the same reasons. Julia is actually pretty fast, but this sort of ad hoc benchmarking basically guarantees that performance is being left on the table. Moreover, the benchmarks are written in a way that stacks the deck against other languages. People from other language communities often get rebuffed when they submit PRs to rewrite the benchmarks in their languages idiomatically. The Julia website claims that "all of the benchmarks are written to test the performance of specific algorithms, expressed in a reasonable idiom", and that making adjustments that are idiomatic for specific languages would be unfair. However, if you look at the Julia code, you'll notice that they're written in a way to avoid doing one of a number of things that would crater performance. If you follow the mailing list, you'll see that there are quite a few intuitive ways to write Julia code that has very bad performance. The Julia benchmarks avoid those pitfalls, but the code for other languages isn't written with anywhere near that care; in fact, it's just the opposite.
I've just listed a bunch of issues with Julia. I believe the canonical response for complaints about an open source project is, why don't you fix the bugs yourself, you entitled brat? Well, I tried that. For one thing,
there are so many bugs that I often don't file bugs, let alone fix them, because it's too much of an interruption
. But the bigger issue are the barriers to new contributors. I spent a few person-days fixing bugs (mostly debugging, not writing code) and that was almost enough to get me into the top 40 on GitHub's list of contributors. My point isn't that I contributed a lot. It's that I didn't, and that still put me right below the top 40.
There's lots of friction that keeps people from contributing to Julia. The build is often broken or has failing tests. When I
polled Travis CI stats
for languages on GitHub, Julia was basically tied for last in uptime. This isn't just a statistical curiosity: the first time I tried to fix something, the build was non-deterministically broken for the better part of a week because someone checked bad code directly into master without review. I spent maybe a week fixing a few things and then took a break. The next time I came back to fix something, tests were failing for a day because of another bad check-in and I gave up on the idea of fixing bugs. That tests fail so often is even worse than it sounds when you take into account the poor test coverage. And even when the build is "working", it uses
recursive makefiles
, and often fails with a message telling you that you need to run
make clean
and build again, which takes half an hour. When you do so, it often fails with a message telling you that you need to
make clean all
and build again, with takes an hour. And then there's some chance that will fail and you'll have to manually clean out
deps
and build again, which takes even longer. And that's the good case! The bad case is when the build fails non-deterministically. These are well-known problems that occur when using recursive make, described in
Recursive Make Considered Harmful
circa 1997.
And that's not even the biggest barrier to contributing to core Julia. The biggest barrier is that the vast majority of the core code is written with no markers of intent (comments, meaningful variable names, asserts, meaningful function names, explanations of short variable or function names, design docs, etc.). There's a tax on debugging and fixing bugs deep in core Julia because of all this. I happen to know one of the Julia core contributors (presently listed as the #2 contributor by GitHub's ranking), and when I asked him about some of the more obtuse functions I was digging around in, he couldn't figure it out either. His suggestion was to ask the mailing list, but for the really obscure code in the core codebase, there's perhaps one to three people who actually understand the code, and if they're too busy to respond, you're out of luck.
I don't mind spending my spare time working for free to fix other people's bugs. In fact, I do quite a bit of that and it turns out I often enjoy it. But I'm too old and crotchety to spend my leisure time deciphering code that even the core developers can't figure out because it's too obscure.
None of this is to say that Julia is bad, but the concerns of the core team are pretty different from my concerns. This is the point in a complain-y blog post where you're supposed to suggest an alternative or make a call to action, but I don't know that either makes sense here. The purely technical problems, like slow load times or the package manager, are being fixed or will be fixed, so there's not much to say there. As for process problems, like not writing tests, not writing internal documentation, and checking unreviewed and sometimes breaking changes directly into master, well, that's “easy” to fix by adding a code review process that forces people to write tests and documentation for code, but that's not free.
A small team of
highly talented
developers who can basically hold all of the code in their collective heads can make great progress while eschewing anything that isn't just straight coding at the cost of making it more difficult for other people to contribute. Is that worth it? It's hard to say. If you have to slow down
Jeff
,
Keno
, and the other super productive core contributors and all you get out of it is a couple of bums like me, that's probably not worth it. If you get a thousand people like me, that's probably worth it. The reality is in the ambiguous region in the middle, where it might or might not be worth it. The calculation is complicated by the fact that most of the benefit comes in the long run, whereas the costs are disproportionately paid in the short run. I once had
an engineering professor
who claimed that the answer to every engineering question is "it depends". What should Julia do? It depends.
2022 Update
This post originally mentioned how friendly the Julia community is, but I removed that since it didn't seem accurate in light of the responses. Many people were highly supportive, such as this Julia core developer:
However, a number of people had some pretty nasty responses and I don't think it's accurate to say that a community is friendly when the response is mostly positive, but with a significant fraction of nasty responses, since it doesn't really take a lot of nastiness to make a group seem unfriendly. Also, sentiment about this post has gotten more negative over time as
communities tend to take their direction from the top
and a couple of the Julia co-creators have consistently been quite negative about this post.
Now, onto the extent to which these issues have been fixed. The initial response from the co-founders was that the issues aren't really real and the post is badly mistaken. Over time, as some of the issues had some work done on them, the response changed to being that this post is out of date and the issues were all fixed, e.g.,
here's a response from one of the co-creators of Julia in 2016
:
The main valid complaints in Dan's post were:
Insufficient testing & coverage. Code coverage is now at 84% of base Julia, from somewhere around 50% at the time he wrote this post. While you can always have more tests (and that is happening), I certainly don't think that this is a major complaint at this point.
Package issues. Julia now has package precompilation so package loading is pretty fast. The package manager itself was rewritten to use libgit2, which has made it much faster, especially on Windows where shelling out is painfully slow.
Travis uptime. This is much better. There was a specific mystery issue going on when Dan wrote that post. That issue has been fixed. We also do Windows CI on AppVeyor these days.
Documentation of Julia internals. Given the quite comprehensive developer docs that now exist, it's hard to consider this unaddressed:
http://julia.readthedocs.org/en/latest/devdocs/julia/
So the legitimate issues raised in that blog post are fixed.
The top response to that is:
The main
valid
complaints [...] the
legitimate
issues raised [...]
This is a really passive-aggressive weaselly phrasing. I’d recommend reconsidering this type of tone in public discussion responses.
Instead of suggesting that the other complaints were invalid or illegitimate, you could just not mention them at all, or at least use nicer language in brushing them aside. E.g. “... the main
actionable
complaints...” or “the main
technical
complaints ...”
Putting aside issues of tone, I would say that the main issue from the post, the core team's attitude towards correctness, is both a legitimate issue and one that's unfixed, as we'll see when we look at how the specific issues mentioned as fixed are also unfixed.
On correctness, if the correctness issues were fixed, we wouldn't continue to see showstopping bugs in Julia, but I have a couple of friends who continued to use Julia for years until they got fed up with correctness issues and sent me quite a few bugs that they personally ran into that were serious well after the 2016 comment about correctness being fixed, such as
getting an incorrect result when sampling from a distribution
,
sampling from an array produces incorrect results
,
the product function, i.e., multiplication, produces incorrect results
,
quantile produces incorrect results
,
mean produces incorrect results
,
incorrect array indexing
,
divide produces incorrect results
,
converting from float to int produces incorrect results
,
quantile produces incorrect results (again)
,
mean produces incorrect results (again)
, etc.
There has been a continued flow of very serious bugs from Julia and numerous other people noting that they've run into serious bugs, such as
here
:
I remember all too un-fondly a time in which one of my Julia models was failing to train. I spent multiple months on-and-off trying to get it working, trying every trick I could think of.
Eventually – eventually! – I found the error:
Julia/Flux/Zygote was returning incorrect gradients
. After having spent so much energy wrestling with points 1 and 2 above, this was the point where I simply gave up. Two hours of development work later, I had the model successfully training… in PyTorch.
And
here
I have been bit by incorrect gradient bugs in Zygote/ReverseDiff.jl. This cost me weeks of my life and has thoroughly shaken my confidence in the entire Julia AD landscape. [...] In all my years of working with PyTorch/TF/JAX I have not once encountered an incorrect gradient bug.
And
here
Since I started working with Julia, I’ve had two bugs with Zygote which have slowed my work by several months. On a positive note, this has forced me to plunge into the code and learn a lot about the libraries I’m using. But I’m finding myself in a situation where this is becoming too much, and I need to spend a lot of time debugging code instead of doing climate research.
Despite this continued flow of bugs, public responses from the co-creators of Julia as well as a number of core community members generally claim, as they did for this post, that the issues will be fixed very soon (e.g., see
the comments here by some core devs on a recent post, saying that all of the issues are being addressed and will be fixed soon
, or this
2020 comment about how the there were serious correctness issues in 2016 but things are now good
, etc.).
Instead of taking the correctness issues or other issues seriously, the developers make statements like
the following comments from a co-creator of Julia, passed to me by a friend of mine as my friend ran into yet another showstopping bug
:
takes that Julia doesn't take testing seriously... I don't get it. the amount of time and energy we spend on testing the bejeezus out of everything. I literally don't know any other open source project as thoroughly end-to-end tested.
The general claim is that, not only has Julia fixed its correctness issues, it's as good as it gets for correctness.
On the package issues, the claim was that package load times were fixed by 2016. But this continues to be a major complaint of the people I know who use Julia, e.g., Jamie Brandon switched away from using Julia in 2022 because it took two minutes for his CSV parsing pipeline to run, where most of the time was package loading. Another example is that, in 2020,
on a benchmark where the Julia developers bragged that Julia is very fast at the curious workload of repeatedly loading the same CSV over and over again (in a loop, not by running a script repeatedly) compared to R
, some people noted that this was unrealistic due to Julia's very long package load times, saying that it takes 2 seconds to open the CSV package and then 104 seconds to load a plotting library. In 2022, in response to comments that package loading is painfully slow, a Julia developer responds to each issue saying each one will be fixed; on package loading, they say
We're getting close to native code caching, and more:
https://discourse.julialang.org/t/precompile-why/78770/8
. As you'll also read, the difficulty is due to important tradeoffs Julia made with composability and aggressive specialization...but it's not fundamental and can be surmounted. Yes there's been some pain, but in the end hopefully we'll have something approximating the best of both worlds.
It's curious that these problems could exist in 2020 and 2022 after a co-creator of Julia claimed, in 2016, that the package load time problems were fixed. But this is the general pattern of Julia PR that we see. On any particular criticism, the criticism is one of: illegitimate, fixed soon or, when the criticism is more than a year old, already fixed. But we can see by looking at responses over time that the issues that are "already fixed" or "will be fixed soon" are, in fact, not fixed many years after claims that they were fixed. It's true that there is progress on the issues, but it wasn't really fair to say that package load time issues were fixed and "package loading is pretty fast" when it takes nearly two minutes to load a CSV and use a standard plotting library (an equivalent to ggplot2) to generate a plot in Julia. And likewise for correctness issues when there's still a steady stream of issues in core libraries, Julia itself, and libraries that are named as part of the magic that makes Julia great (e.g.,
autodiff is frequently named as a huge advantage of Julia when it comes to features
, but then
when it comes to bugs, those bugs don't count because they're not in Julia itself
(that last comment, of course, has a comment from a Julia developer noting that all of the issues will be addressed soon).
There's a sleight of hand here where the reflexive response from a number of the co-creators as well as core developers of Julia is to brush off any particular issue with a comment that sounds plausible if read on HN or Twitter by
someone who doesn't know people who've used Julia
. This makes for good PR since, with an emerging language like Julia, most potential users won't have real connections who've used it seriously and the reflexive comments sound plausible if you don't look into them.
I use the word reflexive here because it seems that some co-creators of Julia respond to any criticism with a rebuttal, such as
here
, where a core developer responds to a post about showstopping bugs by saying that having bugs is actually good, and
here
, where in response to my noting that some people had commented that they were tired of misleading benchmarking practices by Julia developers, a co-creator of Julia drops in to say "I would like to let it be known for the record that I do not agree with your statements about Julia in this thread." But my statements in the thread were merely that there existed comments like
https://news.ycombinator.com/item?id=24748582
. It's quite nonsensical to state, for the record, a disagreement that those kinds of comments exist because they clearly do exist.
Another example of a reflexive response is
this 2022 thread
, where someone who tried Julia but stopped using it for serious work after running into one too many bugs that took weeks to debug suggests that the Julia ecosystem needs a rewrite because the attitude and culture in the community results in a large number of correctness issues. A core Julia developer "rebuts" the comment by saying that things are re-written all the time and gives examples of things that were re-written for performance reasons. Performance re-writes are, famously, a great way to introduce bugs, making the "rebuttal" actually a kind of anti-rebuttal. But, as is typical for many core Julia developers, the person saw that there was an issue (not enough re-writes) and reflexively responded with a denial, that there are enough re-writes.
These reflexive responses are pretty obviously bogus if you spend a bit of time reading them and looking at the historical context but this kind of "deny deny deny" response is generally highly effective PR and has been effective for Julia, so it's understandable that it's done. For example,
on this 2020 comment that belies the 2016 comment about correctness being fixed that says that there were serious issues in 2016 but things are "now" good in 2020
, someone responds "Thank you, this is very heartening." since it relieves them of their concern that there are still issues. Of course, you can see basically the same discussion on discussions in 2022, but people reading the discussion in 2022 generally won't go back to see that this same discussion happened in 2020, 2016, 2013, etc.
On the build uptime, the claim is that the issue causing uptime issues was fixed, but my comment there was on the attitude of brushing off the issue for an extended period of time with "works on my machine". As we can see from the examples above, the meta-issue of brushing off issues continued.
On the last issue that was claimed to legitimate, which was also claimed to be fixed, documentation, this is still a common complaint from the community, e.g.,
here in 2018
, 2 years after it was claimed that documentation was fixed in 2016,
here in 2019
,
here in 2022
, etc. In a much lengthier complaint, one person notes
The biggest issue, and one they seem unwilling to really address, is that actually using the type system to do anything cool requires you to rely entirely on documentation which may or may not exist (or be up-to-date).
And another echoes this sentiment with
This is truly an important issue.
Of course,
there's a response saying this will be fixed soon
, as is generally the case. And yet, you can still find people complaining about the documentation.
If you go back and read discussions on Julia correctness issues, three more common defenses are that everything has bugs, bugs are quickly fixed, and testing is actually great because X is well tested. You can see examples of "everything has bugs"
here in 2014
as well as
here in 2022
(and in between as well, of course), as if all non-zero bug rates are the same, even though a number of developers have noted that they stopped using Julia for work and switched to other ecosystems because, while everything has bugs, all non-zero numbers are, of course, not the same. Bugs getting fixed quickly is sometimes not true (e.g., many of the bugs linked in this post have been open for quite a while and are still open) and is also
a classic defense that's used to distract from the issue of practices that directly lead to the creation of an unusually large number of new bugs
. As noted in a number of links, above, it can take weeks or months to debug correctness issues since many of the correctness issues are of the form "silently return incorrect results" and, as noted above, I ran into a bug where exceptions were non-deterministically incorrectly not caught. It may be true that, in some cases, these sorts of bugs are quickly fixed when found, but those issues still cost users a lot of time to track down. We saw an example of "testing is actually great because X is well tested"
above
. If you'd like a more recent example,
here's one from 2022
where, in response to someone saying that ran into more correctness bugs in Julia than than in any other ecosystem they've used in their decades of programming, a core Julia dev responds by saying that a number of things are very well tested in Julia, such as libuv, as if testing some components well is a talisman that can be wielded against bugs in other components. This is obviously absurd, in that it's like saying that a building with an open door can't be insecure because it also has very sturdy walls, but it's a common defense used by core Julia developers. And, of course, there's also just straight-up FUD about writing about Julia. For example, in 2022, on Yuri Vishnevsky's post on Julia bugs, a co-creator of Julia said
"Yuri's criticism was not that Julia has correctness bugs as a language, but that certain libraries when composed with common operations had bugs (many of which are now addressed)."
. This is, of course, completely untrue. In conversations with Yuri, he noted to me that he specifically included examples of core language and core library bugs because those happened so frequently, and it was frustrating that core Julia people pretended those didn't exist and that their FUD seemed to work since people would often respond as if their comments weren't untrue. As mentioned above, this kind of flat denial of simple matters of fact is highly effective, so it's understandable that people employ it but, personally, it's not to my taste.
To be clear, I don't inherently have a problem with software being buggy. As I've mentioned,
I think move fast and break things can be a good value
because it clearly states that velocity is more valued than correctness. Comments from the creators of Julia as well as core developers broadcast that Julia is not just highly reliable and correct, but actually world class ("the amount of time and energy we spend on testing the bejeezus out of everything. I literally don't know any other open source project as thoroughly end-to-end tested.", etc.). But, by revealed preference, we can see that Julia's values are "move fast and break things".
Appendix: blog posts on Julia
2014:
this post
2016:
Victor Zverovich
Julia brags about high performance in unrepresentative microbenchmarks but often has poor performance in practice
Complex codebase leading to many bugs
2022:
Volker Weissman
Poor documentation
Unclear / confusing error messages
Benchmarks claim good performance but benchmarks are of unrealistic workloads and performance is often poor in practice
2022:
Patrick Kidger
comparison of Julia to JAX and PyTorch
Poor documentation
Correctness issues in widely relied on, important, libraries
Inscrutable error messages
Poor code quality, leading to bugs and other issues
2022:
Yuri Vishnevsky
Many very serious correctness bugs in both the language runtime and core libraries that are heavily relied on
Culture / attitude has persistently caused a large number of bugs, "Julia and its packages have the highest rate of serious correctness bugs of any programming system I’ve used, and I started programming with Visual Basic 6 in the mid-2000s"
Stream of serious bugs is in stark contrast to comments from core Julia developers and Julia co-creators saying that Julia is very solid and has great correctness properties
Thanks (or anti-thanks) to Leah Hanson for pestering me to write this for the past few months. It's not the kind of thing I'd normally write, but the concerns here got repeatedly brushed off when I brought them up in private. For example, when I brought up testing, I was told that Julia is better tested than most projects. While that's true in some technical sense (the median project on GitHub probably has zero tests, so any non-zero number of tests is above average), I didn't find that to be a meaningful rebuttal (as opposed to a reply that Julia is still expected to be mostly untested because it's in an alpha state). After getting a similar response on a wide array of topics I stopped using Julia. Normally that would be that, but Leah really wanted these concerns to stop getting ignored, so I wrote this up.
Also, thanks to Leah Hanson, Julia Evans, Joe Wilder, Eddie V, David Andrzejewski, @sasuke___420@mastodon.social, and Yuri Vishnevsky for comments/corrections/discussion.
