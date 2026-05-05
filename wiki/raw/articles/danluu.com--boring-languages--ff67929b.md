---
title: "A defense of boring languages"
url: "https://danluu.com/boring-languages/"
fetched_at: 2026-05-05T07:01:33.363038+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# A defense of boring languages

Source: https://danluu.com/boring-languages/

Boring languages are underrated. Many appear to be rated quite highly, at least if you look at market share. But even so, they're underrated. Despite the popularity of Dan McKinley's
"choose boring technology"
essay, boring languages are widely panned. People who use them are too (e.g., they're a target of essays by Paul Graham and Joel Spolsky,
and other people have picked up a similar attitude
).
A commonly used pitch for interesting languages goes something like "Sure, you can get by with writing blub for boring work, which almost all programmers do, but if you did interesting work, then you'd want to use an interesting language". My feeling is that this has it backwards. When I'm doing boring work that's basically bottlenecked on the speed at which I can write boilerplate, it feels much nicer to use an interesting language (like F#), which lets me cut down on the amount of time spent writing boilerplate. But when I'm doing interesting work, the boilerplate is a rounding error and I don't mind using a boring language like Java, even if that means a huge fraction of the code I'm writing is boilerplate.
Another common pitch, similar to the above, is that learning interesting languages will teach you new ways to think that will make you a much more effective programmer. I can't speak for anyone else, but I found that line of reasoning compelling when I was early in my career and learned ACL2 (a Lisp), Forth, F#, etc.; enough of it stuck that I still love F#. But, despite taking the advice that "learning a wide variety of languages that support different programming paradigms will change how you think" seriously, my experience has been that the things I've learned mostly let me crank through boilerplate more efficiently. While that's pretty great when I have a boilerplate-constrained problem, when I have a hard problem, I spend so little time on that kind of stuff that the skills I learned from writing a wide variety of languages don't really help me; instead, what helps me is having domain knowledge that gives me a good lever with which I can solve the hard problem. This explains something I'd wondered about when I finished grad school and arrived in the real world: why is it that the programmers who build the systems I find most impressive typically have deep domain knowledge rather than interesting language knowledge?
Another perspective on this is Sutton's response when asked why he robbed banks, "because that's where the money is". Why do I work in boring languages? Because that's what the people I want to work with use, and what the systems I want to work on are written in. The vast majority of the systems I'm interested in are writing in boring languages. Although that technically doesn't imply that the vast majority of people I want to work with primarily use and have their language expertise in boring languages, that also turns out to be the case in practice. That means that, for greenfield work, it's also likely that the best choice will be a boring language. I think F# is great, but I wouldn't choose it over working with the people I want to work with on the problems that I want to work on.
If I look at the list of things I'm personally impressed with (things like Spanner, BigTable, Colossus, etc.), it's basically all C++, with almost all of the knockoffs in Java. When I think for a minute, the list of software written in C, C++, and Java is really pretty long. Among the transitive closure of things I use and the libraries and infrastructure used by those things, those three languages are ahead by a country mile, with PHP, Ruby, and Python rounding out the top 6. Javascript should be in there somewhere if I throw in front-end stuff, but it's so ubiquitous that making a list seems a bit pointless.
Below are some lists of software written in boring languages. These lists are long enough that I’m going to break them down into some arbitrary sublists. As is often the case, these aren’t really nice orthogonal categories and should be tags, but here we are. In the lists below, apps are categorized under “Backend” based on the main language used on the backend of a webapp. The other categories are pretty straightforward, even if their definitions a bit idiosyncratic and perhaps overly broad.
C
Operating Systems
Linux, including variants like KindleOS
BSD
Darwin (with C++)
Plan 9
Windows (kernel in C, with some C++ elsewhere)
Platforms/Infrastructure
Memcached
SQLite
nginx
Apache
DB2
PostgreSQL
Redis
Varnish
HAProxy
AWS Lambda workers (with most of the surrounding infrastructure written in Java), according to @jayachdee
Desktop Apps
git
Gimp (with perl)
VLC
Qemu
OpenGL
FFmpeg
Most GNU userland tools
Most BSD userland tools
AFL
Emacs
Vim
C++
Operating Systems
BeOS/
Haiku
Platforms/Infrastructure
GFS
Colossus
Ceph
Dremel
Chubby
BigTable
Spanner
MySQL
ZeroMQ
ScyllaDB
MongoDB
Mesos
JVM
.NET
Backend Apps
Google Search
PayPal
Figma (
front-end written in C++ and cross-compiled to JS
)
Desktop Apps
Chrome
MS Office
LibreOffice (with Java)
Evernote (originally in C#, converted to C++)
Firefox
Opera
Visual Studio (with C#)
Photoshop, Illustrator, InDesign, etc.
gcc
llvm/clang
Winamp
Z3
Most AAA games
Most pro audio and video production apps
Elsewhere
Also see
this list
and
some of the links here
.
Java
Platforms/Infrastructure
Hadoop
HDFS
Zookeeper
Presto
Cassandra
Elasticsearch
Lucene
Tomcat
Jetty
Backend Apps
Gmail
LinkedIn
Ebay
Most of Netflix
A large fraction of Amazon services
Desktop Apps
Eclipse
JetBrains IDEs
SmartGit
Minecraft
VHDL/Verilog
I'm not even going to make a list because basically every major microprocessor, NIC, switch, etc. is made in either VHDL or Verilog. For existing projects, you might say that this is because you have a large team that's familiar with some boring language, but I've worked on greenfield hardware/software co-design for deep learning and networking virtualization, both with teams that are hired from scratch for the project, and we still used Verilog, despite one of the teams having one of the larger collections of bluespec proficient hardware engineers anywhere outside of Arvind's group at MIT.
Please suggest
other software that you think belongs on this list; it doesn't have to be software that I personally use. Also, does anyone know what EC2, S3, and Redshift are written in? I suspect C++, but I couldn't find a solid citation for that. This post was last updated 2021-08.
One thing I find interesting is that, in personal conversations with people, the vast majority of experienced developers I know think that most mainstream languages are basically fine, modulo performance constraints, and this is even more true among people who've built systems that are really impressive to me. Online discussion of what someone might want to learn is very different, with learning interesting/fancy languages being generally high up on people's lists. When I talk to new programmers, they're often pretty influenced by this (e.g., at Recurse Center, before ML became trendy, learning fancy languages was the most popular way people tried to become better as a programmer, and I'd say that's now #2 behind ML). While I think learning a fancy language does work for some people, I'd say that's overrated in that there are many other techniques that seem to click with at least the same proportion of people who try it that are much less popular.
A question I have is, why is online discussion about this topic so one-sided while the discussions I've had in real life are so oppositely one-sided. Of course, neither people who are loud on the internet nor people I personally know are representative samples of programmers, but I still find it interesting.
Thanks to Leah Hanson, James Porter, Waldemar Q, Nat Welch, Arjun Sreedharan, Rafa Escalante, @matt_dz, Bartlomiej Filipek, Josiah Irwin, @jayachdee, Larry Ogrondek, Miodrag Milic, Presto, Matt Godbolt, Leah Hanson, Noah Haasis, Lifan Zeng, @chozu@fedi.absturztau.be, and Josiah Irwin for comments/corrections/discussion.
