---
title: "A data model for Git (and other docs updates)"
url: "https://jvns.ca/blog/2026/01/08/a-data-model-for-git/"
fetched_at: 2026-05-05T07:01:45.973726+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# A data model for Git (and other docs updates)

Source: https://jvns.ca/blog/2026/01/08/a-data-model-for-git/

Hello! This past fall, I decided to take some time to work on Git’s
documentation. I’ve been thinking about working on open source docs for a long
time – usually if I think the documentation for something could be improved,
I’ll write a blog post or a zine or something. But this time I wondered: could I
instead make a few improvements to the official documentation?
So
Marie
and I made a few changes to the Git
documentation!
After a while working on the documentation, we noticed that Git uses the terms
“object”, “reference”, or “index” in its documentation a lot, but that it didn’t
have a great explanation of what those terms mean or how they relate to other
core concepts like “commit” and “branch”. So we wrote a new “data model” document!
You can
read the data model here for now
.
I assume at some point (after the next release?) it’ll also be on the
Git website
.
I’m excited about this because understanding how Git organizes its commit and
branch data has really helped me reason about how Git works over the years,
and I think it’s important to have a short (1600 words!) version of the data
model that’s accurate.
The “accurate” part turned out to not be that easy: I knew the basics of how
Git’s data model worked, but during the review process I learned some new
details and had to make quite a few changes (for example how merge conflicts are
stored in the staging area).
I also worked on updating the introduction to some of Git’s core man pages.
I quickly realized that “just try to improve it according to my best judgement”
was not going to work: why should the maintainers believe me that my version is
better?
I’ve seen a problem a lot when discussing open source documentation changes
where 2 expert users of the software argue about whether an explanation
is clear or not (“I think X would be a good way to explain it! Well, I think Y
would be better!”)
I don’t think this is very productive (expert users of a piece of software
are notoriously bad at being able to tell if an explanation will be clear to
non-experts), so I needed to find a way to identify problems with the man
pages that was a little more evidence-based.
I asked for test readers on Mastodon to read the current version of
documentation and tell me what they find confusing or what questions they have.
About 80 test readers left comments, and I learned so much!
People left a huge amount of great feedback, for example:
terminology they didn’t understand (what’s a pathspec? what does “reference” mean? does “upstream” have a specific meaning in Git?)
specific confusing sentences
suggestions of things things to add (“I do X all the time, I think it should be included here”)
inconsistencies (“here it implies X is the default, but elsewhere it implies Y is the default”)
Most of the test readers had been using Git for at least 5-10 years, which
I think worked well – if a group of test readers who have been using Git
regularly for 5+ years find a sentence or term impossible to understand, it
makes it easy to argue that the documentation should be updated to make it
clearer.
I thought this “get users of the software to comment on the existing
documentation and then fix the problems they find” pattern worked really
well and I’m excited about potentially trying it again in the future.
We ended updating these 4 man pages:
The
git push
and
git pull
changes were the most interesting to me: in
addition to updating the intro to those pages, we also ended up writing:
Making those changes really gave me an appreciation for how much work it is
to maintain open source documentation: it’s not easy to write things that are
both clear and true, and sometimes we had to make compromises, for example the sentence
“
git push
may fail if you haven’t set an upstream for the current branch,
depending on what
push.default
is set to.” is a little vague, but the exact
details of what “depending” means are really complicated and untangling that is
a big project.
It took me a while to understand Git’s development process.
I’m not going to try to describe it here (that could be a whole other post!), but a few quick notes:
Git has a
Discord server
with a “my first contribution” channel for help with getting started contributing.
I found people to be very welcoming on the Discord.
I used
GitGitGadget
to make all of my contributions.
This meant that I could make a GitHub pull request (a workflow I’m comfortable
with) and GitGitGadget would convert my PRs into the system the Git developers
use (emails with patches attached). GitGitGadget worked great and I was very
grateful to not have to learn how to send patches by email with Git.
Otherwise I used my normal email client (Fastmail’s web interface) to reply
to emails, wrapping my text to 80 character lines since that’s the mailing
list norm.
I also found the mailing list archives on
lore.kernel.org
hard to navigate, so I hacked together
my own git list viewer
to make it easier to read the long mailing list threads.
Many people helped me navigate the contribution process and review the changes:
thanks to Emily Shaffer, Johannes Schindelin (the author of GitGitGadget),
Patrick Steinhardt, Ben Knoble, Junio Hamano, and more.
(I’m experimenting with
comments on Mastodon, you can see the comments here
)
