---
title: "Examples for the tcpdump and dig man pages"
url: "https://jvns.ca/blog/2026/03/10/examples-for-the-tcpdump-and-dig-man-pages/"
fetched_at: 2026-05-05T07:01:46.232695+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# Examples for the tcpdump and dig man pages

Source: https://jvns.ca/blog/2026/03/10/examples-for-the-tcpdump-and-dig-man-pages/

Hello! My big takeaway from last month’s
musings about man pages
was that examples in man pages are really great, so I worked on adding (or
improving) examples to two of my favourite tools’ man pages.
Here they are:
The goal here was really just to give the absolute most basic examples of how to
use the tool, for people who use tcpdump or dig infrequently (or have never used
it before!) and don’t remember how it works.
So far saying “hey, I want to write an examples section for beginners and
infrequent users of this tools” has been working really well. It’s easy to
explain, I think it makes sense from everything I’ve heard from users about what
they want from a man page, and maintainers seem to find it compelling.
Thanks to Denis Ovsienko, Guy Harris, Ondřej Surý, and everyone else who
reviewed the docs changes, it was a good experience and left me motivated to do
a little more work on man pages.
I’m interested in working on tools’ official documentation right now
because:
Man pages can actually have close to 100% accurate information!
Going through a review process to make sure that the information is actually true has a lot of value.
Even with basic questions “what are the most commonly used tcpdump flags”,
often maintainers are aware of useful features that I’m not! For
example I learned by working on these tcpdump examples that if you’re saving
packets to a file with
tcpdump -w out.pcap
, it’s useful to pass
-v
to print
a live summary of how many packets have been captured so far. That’s really
useful, I didn’t know it, and I don’t think I ever would have noticed it on
my own.
It’s kind of a weird place for me to be because honestly I always kind of assume
documentation is going to be hard to read, and I usually just skip it and read
a blog post or Stack Overflow comment or ask a friend instead. But right now
I’m feeling optimistic, like maybe the documentation doesn’t have to be bad?
Maybe it could be just as good as reading a really great blog post, but with the
benefit of also being actually correct? I’ve been using the Django documentation
recently, and it’s really good! We’ll see.
The
tcpdump
project tool’s man page is
written in the roff language
,
which is kind of hard to use and that I really did not feel like learning it.
I handled this by writing a
very basic markdown-to-roff script
to
convert Markdown to roff, using similar conventions to what the man page was
already using. I could maybe have just used pandoc, but the output pandoc
produced seemed pretty different, so I thought it might be better to write my
own script instead. Who knows.
I did think it was cool to be able to just use an existing Markdown library’s
ability to parse the Markdown AST and then implement my own code-emitting
methods to format things in a way that seemed to make sense in this context.
I went on a whole rabbit hole learning about the history of
roff
, how it’s
evolved since the 70s, and who’s working on it today, inspired by learning about
the
mandoc
project that BSD systems (and some Linux
systems, and I think Mac OS) use for formatting man pages. I won’t say more
about that today though, maybe another time.
In general it seems like there’s a technical and cultural divide in how
documentation works on BSD and on Linux that I still haven’t really understood,
but I have been feeling curious about what’s going on in the BSD world.
The
comments section is here
.
