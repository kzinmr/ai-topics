---
title: "Programming book recommendations and anti-recommendations"
url: "https://danluu.com/programming-books/"
fetched_at: 2026-05-05T07:01:32.109587+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Programming book recommendations and anti-recommendations

Source: https://danluu.com/programming-books/

There are a lot of “12 CS books every programmer must read” lists floating around out there. That's nonsense. The field is too broad for almost any topic to be required reading for all programmers, and even if a topic is that important, people's learning preferences differ too much for any book on that topic to be the best book on the topic for all people.
This is a list of topics and books
where I've read the book
, am familiar enough with the topic to say what you might get out of learning more about the topic, and have read other books and can say why you'd want to read one book over another.
Algorithms / Data Structures / Complexity
Why should you care? Well, there's the pragmatic argument: even if you never use this stuff in your job, most of the best paying companies will quiz you on this stuff in interviews. On the non-bullshit side of things, I find algorithms to be useful in the same way I find math to be useful. The probability of any particular algorithm being useful for any particular problem is low, but having a general picture of what kinds of problems are solved problems, what kinds of problems are intractable, and when approximations will be effective, is often useful.
Some problems and solutions, with explanations, matching the level of questions you see in entry-level interviews at Google, Facebook, Microsoft, etc. I usually recommend this book to people who want to pass interviews but not really learn about algorithms. It has just enough to get by, but doesn't really teach you the
why
behind anything. If you want to actually learn about algorithms and data structures, see below.
Everything about this book seems perfect to me. It breaks up algorithms into classes (e.g., divide and conquer or greedy), and teaches you how to recognize what kind of algorithm should be used to solve a particular problem. It has a good selection of topics for an intro book, it's the right length to read over a few weekends, and it has exercises that are appropriate for an intro book. Additionally, it has sub-questions in the middle of chapters to make you reflect on non-obvious ideas to make sure you don't miss anything.
I know some folks don't like it because it's relatively math-y/proof focused. If that's you, you'll probably prefer Skiena.
The longer, more comprehensive, more practical, less math-y version of Dasgupta. It's similar in that it attempts to teach you how to identify problems, use the correct algorithm, and give a clear explanation of the algorithm. Book is well motivated with “war stories” that show the impact of algorithms in real world programming.
This book somehow manages to make it into half of these “N books all programmers must read” lists despite being so comprehensive and rigorous that almost no practitioners actually read the entire thing. It's great as a textbook for an algorithms class, where you get a selection of topics. As a class textbook, it's nice bonus that it has exercises that are hard enough that they can be used for graduate level classes (about half the exercises from my grad level algorithms class were pulled from CLRS, and the other half were from Kleinberg & Tardos), but this is wildly impractical as a standalone introduction for most people.
Just for example, there's an entire chapter on Van Emde Boas trees. They're really neat -- it's a little surprising that a balanced-tree-like structure with
O(lg lg n)
insert, delete, as well as find, successor, and predecessor is possible, but a first introduction to algorithms shouldn't include Van Emde Boas trees.
Same comments as for CLRS -- it's widely recommended as an introductory book even though it doesn't make sense as an introductory book. Personally, I found the exposition in Kleinberg to be much easier to follow than in CLRS, but plenty of people find the opposite.
This is a set of lectures and notes and not a book, but if you want a coherent (but not intractably comprehensive) set of material on data structures that you're unlikely to see in most undergraduate courses, this is great. The notes aren't designed to be standalone, so you'll want to watch the videos if you haven't already seen this material.
Fun to work through, but, unlike the other algorithms and data structures books, I've yet to be able to apply anything from this book to a problem domain where performance really matters.
For a couple years after I read this, when someone would tell me that it's not that hard to reason about the performance of purely functional lazy data structures, I'd ask them about part of a proof that stumped me in this book. I'm not talking about some obscure super hard exercise, either. I'm talking about something that's in the main body of the text that was considered too obvious to the author to explain. No one could explain it. Reasoning about this kind of thing is harder than people often claim.
A gentle introduction to functional programming that happens to use Perl. You could probably work through this book just as easily in Python or Ruby.
If you keep up with what's trendy, this book might seem a bit dated today, but only because so many of the ideas have become mainstream. If you're wondering why you should care about this "functional programming" thing people keep talking about, and some of the slogans you hear don't speak to you or are even off-putting (types are propositions, it's great because it's math, etc.), give this book a chance.
I ordered this off amazon after seeing these two blurbs: “Other learning-enhancement features include chapter summaries, hints to the exercises, and a detailed solution manual.” and “Student learning is further supported by exercise hints and chapter summaries.” One of these blurbs is even printed on the book itself, but after getting the book, the only self-study resources I could find were some yahoo answers posts asking where you could find hints or solutions.
I ended up picking up Dasgupta instead, which was available off an author's website for free.
I've probably gotten more mileage out of this than out of any other algorithms book. A lot of randomized algorithms are
trivial to port to other applications
and can simplify things a lot.
The text has enough of an intro to probability that you don't need to have any probability background. Also, the material on tails bounds (e.g., Chernoff bounds) is useful for a lot of CS theory proofs and isn't covered in the intro probability texts I've seen.
Classic intro to theory of computation. Turing machines, etc. Proofs are often given at an intuitive, “proof sketch”, level of detail. A lot of important results (e.g, Rice's Theorem) are pushed into the exercises, so you really have to do the key exercises. Unfortunately, most of the key exercises don't have solutions, so you can't check your work.
For something with a more modern topic selection, maybe see
Aurora & Barak
.
Covers a few theory of computation highlights. The explanations are delightful and I've watched some of the videos more than once just to watch Bernhardt explain things. Targeted at a general programmer audience with no background in CS.
Classic, but dated and riddled with errors, with no errata available. When I wanted to learn this material, I ended up cobbling together notes from a couple of courses, one by
Klivans
and one by
Blum
.
Operating Systems
Why should you care? Having a bit of knowledge about operating systems can save days or week of debugging time. This is a regular theme on
Julia Evans's blog
, and I've found the same thing to be true of my experience. I'm hard pressed to think of anyone who builds practical systems and knows a bit about operating systems who hasn't found their operating systems knowledge to be a time saver. However, there's a bias in who reads operating systems books -- it tends to be people who do related work! It's possible you won't get the same thing out of reading these if you do really high-level stuff.
This was what we used at Wisconsin before
the comet book
became standard. I guess it's ok. It covers concepts at a high level and hits the major points, but it's lacking in technical depth, details on how things work, advanced topics, and clear exposition.
Cox, Kasshoek, and Morris;
xv6
This book is great! It explains how you can actually implement things in a real system, and it
comes with its own implementation of an OS that you can play with
. By design, the authors favor simple implementations over optimized ones, so the algorithms and data structures used are often quite different than what you see in production systems.
This book goes well when paired with a book that talks about how more modern operating systems work, like Love's Linux Kernel Development or Russinovich's Windows Internals.
Nice explanation of a variety of OS topics. Goes into much more detail than any other intro OS book I know of. For example, the chapters on file systems describe the details of multiple, real, filessytems, and discusses the major implementation features of
ext4
. If I have one criticism about the book, it's that it's very *nix focused. Many things that are described are simply how things are done in *nix and not inherent, but the text mostly doesn't say when something is inherent vs. when it's a *nix implementation detail.
The title can be a bit misleading -- this is basically a book about how the Linux kernel works: how things fit together, what algorithms and data structures are used, etc. I read the 2nd edition, which is now quite dated. The 3rd edition has some updates, but
introduced some errors and inconsistencies
, and is still dated (it was published in 2010, and covers 2.6.34). Even so, it's a nice introduction into how a relatively modern operating system works.
The other downside of this book is that the author loses all objectivity any time Linux and Windows are compared. Basically every time they're compared, the author says that Linux has clearly and incontrovertibly made the right choice and that Windows is doing something stupid. On balance, I prefer Linux to Windows, but there are a number of areas where Windows is superior, as well as areas where there's parity but Windows was ahead for years. You'll never find out what they are from this book, though.
The most comprehensive book about how a modern operating system works. It just happens to be about Windows. Coming from a *nix background, I found this interesting to read just to see the differences.
This is definitely not an intro book, and you should have some knowledge of operating systems before reading this. If you're going to buy a physical copy of this book, you might want to wait until the 7th edition is released (early in 2017).
Takes a topic that's normally one or two sections in an operating systems textbook and turns it into its own 300 page book. The book is a series of exercises, a bit like The Little Schemer, but with more exposition. It starts by explaining what semaphore is, and then has a series of exercises that builds up higher level concurrency primitives.
This book was very helpful when I first started to write threading/concurrency code. I subscribe to the
Butler Lampson school of concurrency
, which is to say that I prefer to have all the concurrency-related code stuffed into a black box that someone else writes. But sometimes you're stuck writing the black box, and if so, this book has a nice introduction to the style of thinking required to write maybe possibly not totally wrong concurrent code.
I wish someone would write a book in this style, but both lower level and higher level. I'd love to see exercises like this, but starting with instruction-level primitives for a couple different architectures with different memory models (say, x86 and Alpha) instead of semaphores. If I'm writing grungy low-level threading code today, I'm overwhelmingly likely to be using
c++11
threading primitives, so I'd like something that uses those instead of semaphores, which I might have used if I was writing threading code against the
Win32
API. But since that book doesn't exist, this seems like the next best thing.
I've heard that Doug Lea's
Concurrent Programming in Java
is also quite good, but I've only taken a quick look at it.
Computer architecture
Why should you care? The specific facts and trivia you'll learn will be useful when you're doing low-level performance optimizations, but the real value is learning how to reason about tradeoffs between performance and other factors, whether that's power, cost, size, weight, or something else.
In theory, that kind of reasoning should be taught regardless of specialization, but my experience is that comp arch folks are much more likely to “get” that kind of reasoning and do back of the envelope calculations that will save them from throwing away a 2x or 10x (or 100x) factor in performance for no reason. This sounds obvious, but I can think of multiple production systems at large companies that are giving up 10x to 100x in performance which are operating at a scale where even a 2x difference in performance could pay a VP's salary -- all because people didn't think through the performance implications of their design.
Hennessy & Patterson; Computer Architecture: A Quantitative Approach
This book teaches you how to do systems design with multiple constraints (e.g., performance, TCO, and power) and how to reason about tradeoffs. It happens to mostly do so using microprocessors and supercomputers as examples.
New editions of this book have substantive additions and you really want the latest version. For example, the latest version added, among other things, a chapter on data center design, and it answers questions like,
how much opex/capex is spent on power, power distribution, and cooling, and how much is spent on support staff and machines
, what's the effect of using lower power machines on tail latency and result quality (bing search results are used as an example), and what other factors should you consider when designing a data center.
Assumes some background, but that background is presented in the appendices (which are available online for free).
Presents most of what you need to know to architect a high performance Pentium Pro (1995) era microprocessor. That's no mean feat, considering the complexity involved in such a processor. Additionally, presents some more advanced ideas and bounds on how much parallelism can be extracted from various workloads (and how you might go about doing such a calculation). Has an unusually large section on
value prediction
, because the authors invented the concept and it was still hot when the first edition was published.
For pure CPU architecture, this is probably the best book available.
Read for historical reasons and to see how much better we've gotten at explaining things. For example, compare Amdahl's paper on Amdahl's law (two pages, with a single non-obvious graph presented, and no formulas), vs. the presentation in a modern textbook (one paragraph, one formula, and maybe one graph to clarify, although it's usually clear enough that no extra graph is needed).
This seems to be worse the further back you go; since comp arch is a relatively young field, nothing here is really hard to understand. If you want to see a dramatic example of how we've gotten better at explaining things, compare Maxwell's original paper on Maxwell's equations to a modern treatment of the same material. Fun if you like history, but a bit of slog if you're just trying to learn something.
Algorithmic game theory / auction theory / mechanism design
Why should you care? Some of the world's biggest tech companies run on ad revenue, and those ads are sold through auctions. This field explains how and why they work. Additionally, this material is useful any time you're trying to figure out how to design systems that allocate resources effectively.
In particular, incentive compatible mechanism design (roughly, how to create systems that provide globally optimal outcomes when people behave in their own selfish best interest) should be required reading for anyone who designs internal incentive systems at companies. If you've ever worked at a large company that "gets" this and one that doesn't, you'll see that the company that doesn't get it has giant piles of money that are basically being lit on fire because the people who set up incentives created systems that are hugely wasteful. This field gives you the background to understand what sorts of mechanisms give you what sorts of outcomes; reading case studies gives you a very long (and entertaining) list of mistakes that can cost millions or even billions of dollars.
The last time I looked, this was the only game in town for a comprehensive, modern, introduction to auction theory. Covers the classic
second price auction result
in the first chapter, and then moves on to cover risk aversion, bidding rings, interdependent values, multiple auctions, asymmetrical information, and other real-world issues.
Relatively dry. Unlikely to be motivating unless you're already interested in the topic. Requires an understanding of basic probability and calculus.
Seems designed as an entertaining introduction to auction theory for the layperson. Requires no mathematical background and relegates math to the small print. Covers maybe, 1/10th of the material of Krishna, if that. Fun read.
Discusses things like how FCC spectrum auctions got to be the way they are and how “bugs” in mechanism design can leave hundreds of millions or billions of dollars on the table. This is one of those books where each chapter is by a different author. Despite that, it still manages to be coherent and I didn't mind reading it straight through. It's self-contained enough that you could probably read this without reading Krishna first, but I wouldn't recommend it.
The title is the worst thing about this book. Otherwise, it's a nice introduction to algorithmic game theory. The book covers basic game theory, auction theory, and other classic topics that CS folks might not already know, and then covers the intersection of CS with these topics. Assumes no particular background in the topic.
A survey of various results in algorithmic game theory. Requires a fair amount of background (consider reading Shoham and Leyton-Brown first). For example, chapter five is basically Devanur, Papadimitriou, Saberi, and Vazirani's JACM paper,
Market Equilibrium via a Primal-Dual Algorithm for a Convex Program
, with a bit more motivation and some related problems thrown in. The exposition is good and the result is interesting (if you're into that kind of thing), but it's not necessarily what you want if you want to read a book straight through and get an introduction to the field.
Misc
A description of how Google handles operations. Has the typical Google tone, which is off-putting to a lot of folks with a “traditional” ops background, and assumes that many things can only be done with the SRE model when they can, in fact, be done without going full SRE.
For a much longer description,
see this 22 page set of notes on Google's SRE book
.
At the time I read it, it was worth the price of admission for the section on code smells alone. But this book has been so successful that the ideas of refactoring and code smells have become mainstream.
Steve Yegge has
a great pitch for this book
:
When I read this book for the first time, in October 2003, I felt this horrid cold feeling, the way you might feel if you just realized you've been coming to work for 5 years with your pants down around your ankles. I asked around casually the next day: "Yeah, uh, you've read that, um, Refactoring book, of course, right? Ha, ha, I only ask because I read it a very long time ago, not just now, of course." Only 1 person of 20 I surveyed had read it. Thank goodness all of us had our pants down, not just me.
...
If you're a relatively experienced engineer, you'll recognize 80% or more of the techniques in the book as things you've already figured out and started doing out of habit. But it gives them all names and discusses their pros and cons objectively, which I found very useful. And it debunked two or three practices that I had cherished since my earliest days as a programmer. Don't comment your code? Local variables are the root of all evil? Is this guy a madman? Read it and decide for yourself!
This book seemed convincing when I read it in college. It even had
all sorts of studies
backing up what they said. No deadlines is better than having deadlines. Offices are better than cubicles. Basically all devs I talk to agree with this stuff.
But virtually every successful company is run the opposite way. Even Microsoft is remodeling buildings from individual offices to open plan layouts. Could it be that all of this stuff just doesn't matter that much? If it really is that important, how come companies that are true believers, like Fog Creek, aren't running roughshod over their competitors?
This book agrees with my biases and I'd love for this book to be right, but the meta evidence makes me want to re-read this with a critical eye and look up primary sources.
This book explains how Microsoft's aggressive culture got to be the way it is today. The intro reads:
Microsoft didn't necessarily hire clones of Gates (although there were plenty on the corporate campus) so much as recruiter those who shared some of Gates's more notable traits -- arrogance, aggressiveness, and high intelligence.
…
Gates is infamous for ridiculing someone's idea as “stupid”, or worse, “random”, just to see how he or she defends a position. This hostile managerial technique invariably spread through the chain of command and created a culture of conflict.
…
Microsoft nurtures a Darwinian order where resources are often plundered and hoarded for power, wealth, and prestige. A manager who leaves on vacation might return to find his turf raided by a rival and his project put under a different command or canceled altogether
On interviewing at Microsoft:
“What do you like about Microsoft?” “Bill kicks ass”, St. John said. “I like kicking ass. I enjoy the feeling of killing competitors and dominating markets”.
…
He was unsure how he was doing and thought he stumbled then asked if he was a "people person". "No, I think most people are idiots", St. John replied.
These answers were exactly what Microsoft was looking for. They resulted in a strong offer and an aggresive courtship.
On developer evangalism at Microsoft:
At one time, Microsoft evangelists were also usually chartered with disrupting competitors by showing up at their conferences, securing positions on and then tangling standards commitees, and trying to influence the media.
…
"We're the group at Microsoft whose job is to fuck Microsoft's competitors"
Read this book if you're considering a job at Microsoft. Although it's been a long time since the events described in this book, you can still see strains of this culture in Microsoft today.
An entertaining book about the backstabbing, mismangement, and random firings that happened in Twitter's early days. When I say random, I mean that there were instances where critical engineers were allegedly fired so that the "decider" could show other important people that current management was still in charge.
I don't know folks who were at Twitter back then, but I know plenty of folks who were at the next generation of startups in their early days and there are a couple of companies where people had eerily similar experiences. Read this book if you're considering a job at a trendy startup.
This book is about art and how productivity changes with age, but if its thesis is valid, it probably also applies to programming. Galenson applies statistics to determine the "greatness" of art and then uses that to draw conclusions about how the productivty of artists change as they age. I don't have time to go over the data in detail, so I'll have to remain skeptical of this until I have more free time, but I think it's interesting reading even for a skeptic.
Math
Why should you care? From a pure ROI perspective, I doubt learning math is “worth it” for 99% of jobs out there. AFAICT, I use math more often than most programmers, and I don't use it all that often. But having the right math background sometimes comes in handy and I really enjoy learning math. YMMV.
Introductory undergrad text that tends towards intuitive explanations over epsilon-delta rigor. For anyone who cares to do more rigorous derivations, there are some exercises at the back of the book that go into more detail.
Has many exercises with available solutions, making this a good text for self-study.
This is one of those books where they regularly crank out new editions to make students pay for new copies of the book (this is presently priced at a whopping $174 on Amazon). This was the standard text when I took probability at Wisconsin, and I literally cannot think of a single person who found it helpful. Avoid.
Brualdi is a great lecturer, one of the best I had in undergrad, but this book was full of errors and not particularly clear. There have been two new editions since I used this book, but according to the Amazon reviews the book still has a lot of errors.
For an alternate introductory text, I've heard good things about
Camina & Lewis's book
, but I haven't read it myself. Also,
Lovasz
is a great book on combinatorics, but it's not exactly introductory.
Volume 1 covers what you'd expect in a calculus I + calculus II book. Volume 2 covers linear algebra and multivariable calculus. It covers linear algebra before multivariable calculus, which makes multi-variable calculus a lot easier to understand.
It also makes a lot of sense from a programming standpoint, since a lot of the value I get out of calculus is its applications to approximations, etc., and that's a lot clearer when taught in this sequence.
This book is probably a rough intro if you don't have a professor or TA to help you along. The Spring SUMS series tends to be pretty good for self-study introductions to various areas, but I haven't actually read their intro calculus book so I can't actually recommend it.
Another one of those books where they crank out new editions with trivial changes to make money. This was the standard text for non-honors calculus at Wisconsin, and the result of that was I taught a lot of people to do complex integrals with the methods covered in Apostol, which are much more intuitive to many folks.
This book takes the approach that, for a type of problem, you should pattern match to one of many possible formulas and then apply the formula. Apostol is more about teaching you a few tricks and some intuition that you can apply to a wide variety of problems. I'm not sure why you'd buy this unless you were required to for some class.
Hardware basics
Why should you care? People often claim that,
to be a good programmer, you have to understand every abstraction you use
. That's nonsense. Modern computing is too complicated for any human to have a real full-stack understanding of what's going on. In fact, one reason modern computing can accomplish what it does is that it's possible to be productive without having a deep understanding of much of the stack that sits below the level you're operating at.
That being said, if you're curious about what sits below software, here are a few books that will get you started.
If you only want to read one single thing, this should probably be it. It's a “101” level intro that goes down to gates and Boolean logic. As implied by the name, it takes you from
NAND gates
to a working tetris program.
Much more detail on gates and logic design than you'll see in nand2tetris. The book is full of exercises and appears to be designed to work for self-study. Note that the link above is to the 5th edition. There are newer, more expensive, editions, but they don't seem to be much improved, have a lot of errors in the new material, and are much more expensive.
One level below Boolean gates, you get to VLSI, a historical acronym (very large scale integration) that doesn't really have any meaning today.
Broader and deeper than the alternatives, with clear exposition. Explores the design space (e.g., the section on adders doesn't just mention a few different types in an ad hoc way, it explores all the tradeoffs you can make. Also, has both problems and solutions, which makes it great for self study.
Kang & Leblebici; CMOS Digital Integrated Circuits
This was the standard text at Wisconsin way back in the day. It was hard enough to follow that the TA basically re-explained pretty much everything necessary for the projects and the exams. I find that it's ok as a reference, but it wasn't a great book to learn from.
Compared to West et al., Weste spends a lot more effort talking about tradeoffs in design (e.g., when creating a parallel prefix tree adder, what does it really mean to be at some particular point in the design space?).
One level below VLSI, you have how transistors actually work.
Really beautiful explanation of solid state devices. The text nails the fundamentals of what you need to know to really understand this stuff (e.g., band diagrams), and then uses those fundamentals along with clear explanations to give you a good mental model of how different types of junctions and devices work.
Covers the same material as Pierret, but seems to substitute mathematical formulas for the intuitive understanding that Pierret goes for.
One level below transistors, you have electromagnetics.
Two to three times thicker than other intro texts because it has more worked examples and diagrams. Breaks things down into types of problems and subproblems, making things easy to follow. For self-study, A much gentler introduction than Griffiths or Purcell.
Unlike the other books in this section, this book is about practice instead of theory. It's a bit like Windows Internals, in that it goes into the details of a real, working, system. Topics include hardware bus protocols, how I/O actually works (e.g.,
APIC
), etc.
The problem with a practical introduction is that there's been an exponential increase in complexity ever since the 8080. The further back you go, the easier it is to understand the most important moving parts in the system, and the more irrelevant the knowledge. This book seems like an ok compromise in that the bus and I/O protocols had to handle multiprocessors, and many of the elements that are in modern systems were in these systems, just in a simpler form.
Not covered
Of the books that I've liked, I'd say this captures at most 25% of the software books and 5% of the hardware books. On average, the books that have been left off the list are more specialized. This list is also missing many entire topic areas, like PL, practical books on how to learn languages, networking, etc.
The reasons for leaving off topic areas vary; I don't have any PL books listed because I don't read PL books. I don't have any networking books because, although I've read a couple, I don't know enough about the area to really say how useful the books are. The vast majority of hardware books aren't included because they cover material that you wouldn't care about unless you were a specialist (e.g.,
Skew-Tolerant Circuit Design
or
Ultrafast Optics
). The same goes for areas like math and CS theory, where I left off a number of books that I think are great but have basically zero probability of being useful in my day-to-day programming life, e.g.,
Extremal Combinatorics
. I also didn't include books I didn't read all or most of, unless I stopped because the book was atrocious. This means that I don't list classics I haven't finished like SICP and The Little Schemer, since those book seem fine and I just didn't finish them for one reason or another.
This list also doesn't include many books on history and culture, like Inside Intel or Masters of Doom. I'll probably add more at some point, but I've been trying an experiment where I try to write more like Julia Evans (stream of consciousness, fewer or no drafts). I'd have to go back and re-read the books I read 10+ years ago to write meaningful comments, which doesn't exactly fit with the experiment. On that note, since this list is from memory and I got rid of almost all of my books a couple years ago, I'm probably forgetting a lot of books that I meant to add.
_If you liked this, you might also like Thomas Ptacek's
Application Security Reading List
or
this list of programming blogs
, which is written in a similar style_
_Thanks to @tytr
dev for comments/corrections/discussion.
