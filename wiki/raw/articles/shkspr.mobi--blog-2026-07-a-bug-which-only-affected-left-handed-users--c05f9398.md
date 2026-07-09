---
title: "A bug which only affected left-handed users"
url: "https://shkspr.mobi/blog/2026/07/a-bug-which-only-affected-left-handed-users/"
fetched_at: 2026-07-09T07:01:31.343563+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# A bug which only affected left-handed users

Source: https://shkspr.mobi/blog/2026/07/a-bug-which-only-affected-left-handed-users/

Verily, some of our brethren (and sistren) be afflicted with a sinister disposition. While the righteous scroll using the thumb of their right hand - as is good and proper - an accurs'd minority swing the other way.
Look, you try writing an interesting bug report without sounding like a clanker, OK!
I try to optimise my blog as much as possible. It may not look like much, but it has got it where it counts. I've made a lot of special modifications myself to the base WordPress install.
One of those modifications is reducing the amount of JavaScript in use to the bare minimum. Everything functions without it, but there are a few places where it helps - the most notable being comments.
That's why I was distressed when a loyal reader wrote in saying there was a bug on my site. When they were scrolling the page a comment box would suddenly appear and interrupt their browsing.
I scroll my own site a lot (probably more than is healthy) so why hadn't I noticed this bug?
Because I scroll on my phone's touchscreen with my right thumb and the bug reporter uses their left. The "reply" link which was being triggered is on the left side of the page. A bug which won't be triggered by righteous people but infuriating to those who will surely be left behind after The Rapture™.
To be fair,
this bug was reported seven years ago
- but I guess the WordPress team have been too busy cleaning up after their mad God-Emperor to take a look at it.
Back in 2017, a developer
added a
touchstart
listener to link clicks
. I don't really understand why. At one point in history, browsers couldn't be sure if a touch event was the start of a
click
or a double-tap to zoom. So firing an event when a touch occurred on a link sort of made sense to avoid a 300ms delay.
But that hadn't been the case for several years -
as this 2013 blog post makes clear
.  Even in 2015
it was no longer an issue
.
So why was this lefty-baiting code added? Not a clue.
Anyway,
seven years
after the bug was reported
I committed a fix
. It isn't the most sophisticated change to WordPress - merely deleting a couple of lines. But hopefully it will stop those strange and unusual mutants from complaining that their unnatural thumb-usage is accidentally triggering unwanted events on my website.
Sadly, there is as yet no way to prevent the corrupt from using our blessed sites. The WHAT-WG haven't seen fit to take on board my suggestion of
<meta handed="right">
to keep out the unwanted and polluted. So, hopefully, this change will at least prevent them complaining.
Why, yes officer, I have had a glass or two of tonic wine. Why do you ask?
