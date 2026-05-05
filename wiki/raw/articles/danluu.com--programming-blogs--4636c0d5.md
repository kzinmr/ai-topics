---
title: "Some programming blogs to consider reading"
url: "https://danluu.com/programming-blogs/"
fetched_at: 2026-05-05T07:01:31.842563+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Some programming blogs to consider reading

Source: https://danluu.com/programming-blogs/

This is one of those “N technical things every programmer must read” lists, except that “programmer” is way too broad a term and the styles of writing people find helpful for them are too different for any such list to contain a non-zero number of items (if you want the entire list to be helpful to everyone). So here's a list of some things you might want to read, and why you might (or might not) want to read them.
If you want to understand how the JVM really works, this is one of the best resources on the internet.
Performance explorations of a Windows programmer. Often implicitly has nice demonstrations of tooling that has no publicly available peer on Linux.
A mix of summaries of ML conferences, data analyses (e.g.,
on interview data posted to glassdoor
or
compensation data posted to levels.fyi
), and generaly commentary on the industry.
One of the rare blogs that has data-driven position pieces about the industry.
Computer related projects, by which I mean things like
reconstructing the Cray-1A
and
building mechanical computers
. Rarely updated, presumably due to the amount of work that goes into the creations, but almost always interesting.
The blog posts tend to be high-level, more like pitch decks than design docs, but there's often source code available if you want more detail.
More active on Twitter than on her blog, but has posts that review papers as well as some on "big" topics, like
distributed tracing
and
testing in production
.
A lot of great material on how engineering companies should be run. He has a lot of ideas that sound like common sense, e.g.,
choose boring technology
, until you realize that it's actually uncommon to find opinions that are so sensible.
Mostly distilled wisdom (as opposed to, say, detailed explanations of code).
I think of this as “
the C++ blog
”, but it's much wider ranging that that. It's too wide ranging for me to sum up, but if I had to commit to a description I might say that it's a collection of deep dives into various topics, often (but not always) relatively low-level, along with short blurbs about books, often (but not always) technical.
The book reviews tend to be easy reading, but the programming blog posts are often a mix of code and exposition that really demands your attention; usually not a light read.
I think Erik has been
the most consistently insightful writer about tech culture over the past 20 years
. If you look at people who were blogging back when he started blogging, much of
Steve Yegge's
writing holds up as well as Erik's, but Steve hasn't continued writing consistently.
If you look at popular writers from that era, I think they generally tend to
not
really
hold
up very well.
Covers a wide variety of technical topics. Emphasis on computer architecture, compression, graphics, and signal processing, but you'll find many other topics as well.
Posts tend towards being technically intense and not light reading and they usually explain concepts or ideas (as opposed to taking sides and writing opinion pieces).
In depth techincal dives on game related topics, such as
this readthrough of the Doom source code
,
this history of Nvidia GPU architecture
, or
this read of a business card raytracer
.
Not exactly a blog, but every time a new project appears on the front page, it's amazing. Some examples are QEMU, FFMPEG, a 4G LTE base station that runs on a PC,
a JavaScript PC emulator that can boot Linux
, etc.
Explanations of CS-related math topics (with a few that aren't directly CS related).
Another “not exactly a blog”, but it's more informative than most blogs, not to mention more entertaining. This is the best “blog” on
the pervasive brokenness of modern software
that I know of.
rakyll.org
has posts on Go, some of which are quite in depth, e.g.,
this set of notes on the Go generics proposal
and
Jaana's medium blog
has some posts on Go as well as posts on various topics in distributed systems.
Also,
Jaana's Twitter
has what I think of as "intellectually honest critiques of the industry", which I think is unusual for critiques of the industry on Twitter. It's more typical to see people scoring points at the expense of nuance or even being vaugely in the vicinity of correctness, which is why I think it's worth calling out these honest critiques.
I'm so happy that I managed to convince Jamie that, given his preferences, it would make sense to take a crack at blogging full-time to support himself. Since
Jamie started taking donations
until today, this blog has been an absolute power house with posts like
this
series
on problems with SQL,
this
series
on
streaming systems, great work on technical projects like
dida
and
imp
, etc.
It remains to be seen whether or not Jamie will be able to convince me to try blogging as a full-time job.
This is the story of how a professor moved from Grinnel to Whitman and
started a CS program from scratch
. The archives are great reading if you're interested in how organizations form or CS education.
Mostly technical content relating to C++ and Python, but also includes topics that are generally useful for programmers, such as
read-modify-write operations
,
fixed-point math
, and
memory models
.
Jessica is probably better known for
her talks
than her blog? Her talks are great! My favorite is probably
this talk with explains different concurrency models in an easy to understand way
, but
the blog also has a lot of material I like
.
As is the case with her talks, the diagrams often take a concept and clarify it, making something that wasn't obvious seem very obvious in retrospect.
I think of this as the
“C is harder than you think, even if you think C is really hard” blog
, although the blog actually covers a lot more than that. Some commonly covered topics are fuzzing, compiler optimization, and testing in general.
Posts tend to be conceptual. When there are code examples, they're often pretty easy to read, but there are also examples of bizzaro behavior that won't be easy to skim unless you're someone who knows the C standard by heart.
A lot of
posts about networking
, generally
written so that they make sense even with minimal networking background
. I wish more people with this kind of knowledge (in depth knowledge of systems, not just networking knowledge in particular) would write up explanations for a general audience. Also has interesting non-networking content, like
this post on Finnish elections
.
AFAICT, the theme is “things Julia has learned recently”, which can be anything from
Huffman coding
to
how to be happy when working in a remote job
. When the posts are on a topic I don't already know, I learn something new. When they're on a topic I know, they remind me that the topic is exciting and contains a lot of wonder and mystery.
Many posts have more questions than answers, and are more of a live-blogged exploration of a topic than an explanation of the topic.
A mix of security-related topics and explanations of practical programming knowledge.
This article on phishing
, which includes a set of fun case studies on how effective phising can be, even after people take anti-phishing training, is an example of a security post.
This post on printing out text via tracert
. This
post on writing an SSH client
and
this post
on
some coreutils puzzles
are examples of practical programming explanations.
Although the blog is security oriented, posts are written for a general audience and don't assume specific expertise in security.
Mostly small, self-contained explorations like,
what's up with this Python integer behavior
,
how do you make a git blow up with a simple repo
, or
how do you generate hash collisions in Lua
?
Kavya Joshi
I generally prefer technical explanations in text over video, but her exposition is so clear that I'm putting these talks in this list of blogs. Some examples include
an explanation of the go race detector
,
simple math that's handy for performance modeling
, and
time
.
90% of Kyle's posts are explanations of
distributed systems testing, which expose bugs in real systems that most of us rely on
. The other 10% are
musings on programming that are as rigorous as Kyle's posts on distributed systems
. Possibly the most educational programming blog of all time.
For those of us without a distributed systems background, understanding posts often requires a bit of Googling, despite the extensive explanations in the posts. Most new posts are now at
jepsen.io
Very infrequently updated (on the order of once a year) with explanations of things Laura has been working on, from
Oragami PCB
to
Ice-Penetrating Radar
.
This blog has been going since 2004 and its changed over the years. Recently, it's had some of the best posts on benchmarking around:
VM performance, part 1
Thoroughly refutes the idea that you can run a language VM for some warmup period and then take some numbers when they become stable
VM performance, part 2
Why not use minimum times when benchmarking
"Everyone" who's serious about performance knows this and it's generally considered too obvious to write up, but this is still a widely used technique in benchmarking even though it's only appropriate in limited circumstances
The blog isn't purely technical,
this blog post on advice is also stellar
. If those posts don't sound interesting to you, it's worth
checking out the archives
to see if some of the topics Lawrence used to write about more frequently are to your taste.
A mix of
theory
and
wisdom
from a distributed systems engineer on EBS at Amazon. The theory posts tend to be relatively short and easy to swallow; not at all intimidating, as theory sometimes is.
This used to be a blog about random experiments Marek was doing,
like this post on bitsliced SipHash
. Since Marek joined Cloudflare, this has turned into a list of things Marek has learned while working in Cloudflare's networking stack, like
this story about debugging slow downloads
.
Posts tend to be relatively short, but with enough technical specifics that they're not light reads.
Explorations on old systems, often gaming related. Some exmaples are
this post on collision detection in Alf for the Sega Master System
,
this post on getting decent quality output from composite video
, and
this post on the Neo Geo CDZ
.
Nikita has two blogs, both on related topics.
The main blog
has long-form articles, often how about modern software is terrible. THen there's
grumpy.website
, which gives examples of software being terrible.
More than you ever wanted to know about writing fast code for the JVM, from
GV affects data structures
to
the subtleties of volatile reads
.
Posts tend to involve lots of Java code, but the takeaways are often language agnostic.
Adventures in signal processing. Everything from
deblurring barcodes
to figuring out
what those signals from helicopters mean
. If I'd known that signals and systems could be this interesting, I would have paid more attention in class.
Some content on Lisp
, and
some on low-level optimizations
, with
a trend towards low-level optimizations
.
Posts are usually relatively long and self-contained explanations of technical ideas with very little fluff.
Years of
debugging stories
from a long-time SRE, along with stories about
big company nonsense
. Many of the stories come from Lyft, Facebook, and Google. They're anonymized, but if you know about the companies, you can tell which ones are which.
The degree of anonymization often means that the stories won't really make sense unless you're familiar with the operation of systems similar to the ones in the stories.
A blog about restoring old "pizza box" computers, with posts that generally describe the work that goes into getting these machines working again.
An example is the HP 712 ("low cost" PA-RISC workstations that went for roughly $5k to $15k in 1994 dollars, which ended up doomed due to the Intel workstation onslaught that started with the Pentium Pro in 1995),
where the restoration process is described here in part 1
and
then here in part 2
.
In-depth explanations
on how V8 works and
how various constructs get optimized
by a compiler dev on the V8 team. If I knew compilers were this interesting, I would have taken a compilers class back when I was in college.
Often takes topics that are considered hard and explains them in a way that makes them seem easy. Lots of diagrams, where appropriate, and detailed exposition on all the tricky bits.
Her main site has to a variety of interesting tools she's made or worked on, many of which are FPGA or open hardware related, but some of which are completely different.
Whitequark's lab notebook
has a really wide variety of different results, from things like undocumented hardware quirks, to fairly serious home chemistry experiments, to various tidbits about programming and hardware development (usually low level, but not always).
She's also fairly active
on twitter
, with some commentary on hardware/firmware/low-level programming combined with a set of diverse topics that's too broad to easily summarize.
Mostly dormant since
the author started doing art
, but the archives have a lot of great content about hardware, low-level software, and general programming-related topics that aren't strictly programming.
90% of the time, when I get the desire to write a post about a common misconception software folks have about hardware,
Yossi has already written the post
and
taken a lot of flak for it
so I don't have to :-).
I also really like Yossi's career advice, like
this response to Patrick McKenzie
and
this post on how managers get what they want and not what they ask for
.
He's
active on Twitter
, where he posts extremely cynical and snarky takes on management and the industry.
This blog?
Common themes include:
The end
This list also doesn't include blogs that mostly aren't about programming, so it doesn't include, for example,
Ben Kuhn's excellent blog
.
Anyway, that's all for now, but this list is pretty much off the top of my head, so I'll add more as more blogs come to mind. I'll also keep this list updated with what I'm reading as I find new blogs. Please please please
suggest other blogs I might like
, and don't assume that I already know about a blog because it's popular. Just for example, I had no idea who either Jeff Atwood or Zed Shaw were until a few years ago, and they were probably two of the most well known programming bloggers in existence. Even with centralized link aggregators like HN and reddit, blog discovery has become haphazard and random with the decline of blogrolls and blogging as a dialogue, as opposed to the current practice of blogging as a monologue. Also, please don't assume that I don't want to read something just because it's different from the kind of blog I normally read. I'd love to read more from UX or front-end folks; I just don't know where to find that kind of thing!
Last update: 2021-07
Archive
Here are some blogs I've put into an archive section because they rarely or never update.
This post on why making a competitor to Google search is a post in classic Alex Clemmer style
. The post looks at a position that's commonly believed (web search isn't all that hard and someone should come up with a better Google) and explains why that's not an obviously correct position. That's also a common theme of his comments elsewhere, such as these comments on,
stack ranking at MS
,
implementing POSIX on Windows
,
the size of the Windows codebase
,
Bond
, and
Bing
.
He's sort of a modern mini-MSFT, in that it's incisive commentary on MS and MS related ventures.
Explorations of various areas, often Python related, such as
this this series on the Python interpreter
and
this series on the CPython peephole optimizer
. Also, thoughts on broader topics like
debugging
and
learning
.
Often detailed, with inline code that's meant to be read and understood (with the help of exposition that's generally quite clear).
A mix of things from
writing a 64-bit kernel from scratch shortly after learning assembly
to a
high-level overview of computer systems
. Rarely updated, with few posts, but each post has a lot to think about.
Low-level. A good example of a relatively high-level post from this blog is
this post on the low fragmentation heap in Windows
. Posts like
how to hack a pinball machine
and
how to design a 386 compatible dev board
are typical.
Posts are often quite detailed, with schematic/circuit diagrams. This is relatively heavy reading and I try to have pen and paper handy when I'm reading this blog.
Write-ups of papers that (should) have an impact on how people write software, like
this paper on what causes failures in distributed systems
or
this paper on what makes people feel productive
. Not updated much, but
Greg still blogs on his personal site
.
The posts tend to be extended abstracts that tease you into reading the paper, rather than detailed explanations of the methodology and results.
Explanations of how
Linux works, as well as other low-level topics
. This particular blog seems to be on hiatus, but "0xAX" seems to have picked up the slack with the
linux-insides
project.
If you've read Love's book on Linux, Duarte's explanations are similar, but tend to be more about the idea and less about the implementation. They're also heavier on providing diagrams and context. "0xAX" is a lot more focused on walking through the code than either Love or Duarte.
Explanations of various Rust-y things, from back when Huon was working on Rust. Not updated much anymore, but the content is still great for someone who's interested in technical tidbits related to Rust.
Technical explorations of various topics, with a systems-y bent.
Kubernetes
.
Git push
.
Syscalls in Rust
. Also,
some musings on programming in general
.
The technical explorations often get into enough nitty gritty detail that this is something you probably want to sit down to read, as opposed to skim on your phone.
Lengthy and very-detailed explanations of technical topics
,
mixed in
with
a wide variety of other posts
.
The selection of topics is eclectic, and explained at a level of detail such that you'll come away with a solid understanding of the topic. The explanations are usually fine grained enough that it's hard to miss what's going on, even if you're a beginner programmer.
Rebecca Frankel
As far as I know, Rebecca doesn't have a programming blog, but if you look at her apparently off-the-cuff comments on other people's posts as a blog, it's one of the best written programming blogs out there. She used to be prolific on
Piaw's
Buzz
(and probably elsewhere, although I don't know where), and you occasionally see comments elsewhere, like on
this Steve Yegge blog post about brilliant engineers
. I wish I could write like that.
Homemade electronics projects from
vim on a mechanical typewriter
to
building an electrobalance to proof spirits
.
Posts tend to have a fair bit of detail, down to diagrams explaining parts of circuits, but the posts aren't as detailed as specs. But there are usually links to resources that will teach you enough to reproduce the project, if you want.
I find the archives to be fun reading for insight into
what people were thinking about microprocessors and computer architecture
over the past two decades. It can be a bit depressing to see that
the same benchmarking controversies we had 15 years ago
are being repeated today,
sometimes with the same players
. If anything, I'd say that the
average benchmark you see passed around today
is worse than what you would have seen 15 years ago, even though the industry as a whole has learned a lot about benchmarking since then.
The author of walpurgisriot seems to have abanoned the github account and moved on to another user name (and a squatter appears to have picked up her old account name), but this used to be a semi-frequently updated blog with a combination of short explorations on programming and thoughts on the industry. On pure quality of prose, this is one of the best tech blogs I've ever read; the technical content and thoughts on the industry are great as well.
This post was inspired by the two posts Julia Evans has on blogs she reads and by
the Chicago undergraduate mathematics bibliography
, which I've found to be the most useful set of book reviews I've ever encountered.
Thanks to Bartłomiej Filipek and Sean Barrett, Michel Schniz, Neil Henning, and Lindsey Kuper for comments/discussion/corrections.
