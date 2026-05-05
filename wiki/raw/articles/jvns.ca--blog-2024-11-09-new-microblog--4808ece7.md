---
title: "New microblog with TILs"
url: "https://jvns.ca/blog/2024/11/09/new-microblog/"
fetched_at: 2026-05-05T07:01:47.031177+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# New microblog with TILs

Source: https://jvns.ca/blog/2024/11/09/new-microblog/

I added a new section to this site a couple weeks ago called
TIL
(“today I learned”).
One kind of thing I like to post on Mastodon/Bluesky is “hey, here’s a cool
thing”, like
the great SQLite repl litecli
, or
the fact that cross compiling in Go Just Works and it’s amazing, or
cryptographic right answers
,
or
this great diff tool
. Usually I don’t want to write
a whole blog post about those things because I really don’t have much more to
say than “hey this is useful!”
It started to bother me that I didn’t have anywhere to put those things: for
example recently I wanted to use
diffdiff
and I just
could not remember what it was called.
So I quickly made a new folder called
/til/
, added some
custom styling (I wanted to style the posts to look a little bit like a tweet),
made a little Rake task to help me create new posts quickly (
rake new_til
), and
set up a separate RSS Feed for it.
I think this new section of the blog might be more for myself than anything,
now when I forget the link to Cryptographic Right Answers I can hopefully look
it up on the TIL page. (you might think “julia, why not use bookmarks??” but I
have been failing to use bookmarks for my whole life and I don’t see that
changing ever, putting things in public is for whatever reason much easier for
me)
So far it’s been working, often I can actually just make a quick post in 2
minutes which was the goal.
My page is inspired by
Simon Willison’s great TIL blog
, though my TIL posts are a lot shorter.
This came about because I spent a lot of time on Twitter, so I’ve been thinking
about what I want to do about all of my tweets.
I keep reading the advice to “POSSE” (“post on your own site, syndicate
elsewhere”), and while I find the idea appealing in principle, for me part of
the appeal of social media is that it’s a little bit ephemeral. I can
post polls or questions or observations or jokes and then they can just kind of
fade away as they become less relevant.
I find it a lot easier to identify specific categories of things that I actually
want to have on a Real Website That I Own:
and then let everything else be kind of ephemeral.
I really believe in the advice to make email lists though – the first two
(blog posts & comics) both have email lists and RSS feeds that people can
subscribe to if they want. I might add a quick summary of any TIL posts from
that week to the “blog posts from this week” mailing list.
