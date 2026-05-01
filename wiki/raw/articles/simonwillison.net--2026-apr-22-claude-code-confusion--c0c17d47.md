---
title: "Is Claude Code going to cost $100/month? Probably not-it’s all very confusing"
url: "https://simonwillison.net/2026/Apr/22/claude-code-confusion/#atom-everything"
fetched_at: 2026-05-01T07:01:21.808375+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Is Claude Code going to cost $100/month? Probably not-it’s all very confusing

Source: https://simonwillison.net/2026/Apr/22/claude-code-confusion/#atom-everything

Is Claude Code going to cost $100/month? Probably not—it’s all very confusing
22nd April 2026
Anthropic today quietly (as in
silently
, no announcement anywhere at all) updated their
claude.com/pricing
page (but not their
Choosing a Claude plan page
, which shows up first for me on Google) to add this tiny but significant detail (arrow is mine,
and it’s already reverted
):
The
Internet Archive copy
from yesterday shows a checkbox there. Claude Code used to be a feature of the $20/month Pro plan, but according to the new pricing page it is now exclusive to the $100/month or $200/month Max plans.
Update
: don’t miss
the update to this post
, they’ve already changed course a few hours after this change went live.
So what the heck is going on? Unsurprisingly,
Reddit
and
Hacker News
and
Twitter
all caught fire.
I didn’t believe the screenshots myself when I first saw them—aside from the pricing grid I could find no announcement from Anthropic anywhere. Then Amol Avasare, Anthropic’s Head of Growth,
tweeted
:
For clarity, we’re running a small test on ~2% of new prosumer signups. Existing Pro and Max subscribers aren’t affected.
And that appears to be the closest we have had to official messaging from Anthropic.
I don’t buy the “~2% of new prosumer signups” thing, since everyone I’ve talked to is seeing the new pricing grid and the Internet Archive has already
snapped a copy
. Maybe he means that they’ll only be running this version of the pricing grid for a limited time which somehow adds up to “2%” of signups?
I’m also amused to see Claude Cowork remain available on the $20/month plan, because Claude Cowork is effectively a rebranded version of Claude Code wearing a less threatening hat!
There are a whole bunch of things that are bad about this.
If we assume this is indeed a test, and that test comes up negative and they decide not to go ahead with it, the damage has still been extensive:
A whole lot of people got scared or angry or both that a service they relied on was about to be rug-pulled. There really is a significant difference between $20/month and $100/month for most people, especially outside of higher salary countries.
The uncertainty is really bad! A tweet from an employee is
not
the way to make an announcement like this. I wasted a solid hour of my afternoon trying to figure out what had happened here. My trust in Anthropic’s transparency around pricing—a
crucial factor
in how I understand their products—has been shaken.
Strategically, should I be taking a bet on Claude Code if I know that they might 5x the minimum price of the product?
More of a personal issue, but one I care deeply about myself: I invest a
great deal of effort
(that’s 105 posts and counting) in teaching people how to use Claude Code. I don’t want to invest that effort in a product that most people cannot afford to use.
Last month I ran
a tutorial for journalists
on “Coding agents for data analysis” at the annual NICAR data journalism conference. I’m not going to be teaching that audience a course that depends on a $100/month subscription!
This also doesn’t make sense to me as a strategy for Anthropic. Claude Code
defined the category
of coding agents. It’s responsible for billions of dollars in annual revenue for Anthropic already. It has a stellar reputation, but I’m not convinced that reputation is strong enough for it to lose the $20/month trial and jump people directly to a $100/month subscription.
OpenAI have been investing heavily in catching up to Claude Code with their Codex products. Anthropic just handed them this marketing opportunity on a plate—here’s Codex engineering lead
Thibault Sottiaux
:
I don’t know what they are doing over there, but Codex will continue to be available both in the FREE and PLUS ($20) plans. We have the compute and efficient models to support it. For important changes, we will engage with the community well ahead of making them.
Transparency and trust are two principles we will not break, even if it means momentarily earning less. A reminder that you vote with your subscription for the values you want to see in this world.
I should note that I pay $200/month for Claude Max and I consider it well worth the money. I’ve had periods of free access in the past courtesy of Anthropic but I’m currently paying full price, and happy to do so.
But I care about the accessibility of the tools that I work with and teach. If Codex has a free tier while Claude Code starts at $100/month I should obviously switch to Codex, because that way I can use the same tool as the people I want to teach how to use coding agents.
Here’s what I think happened. I think Anthropic are trying to optimize revenue growth—obviously—and someone pitched making Claude Code only available for Max and higher. That’s clearly a bad idea, but “testing” culture says that it’s worth putting even bad ideas out to test just in case they surprise you.
So they started a test, without taking into account the wailing and gnashing of teeth that would result when their test was noticed—or accounting for the longer-term brand damage that would be caused.
Or maybe they
did
account for that, and decided it was worth the risk.
I don’t think that calculation was worthwhile. They’re going to have to make a
very
firm commitment along the lines of “we heard your feedback and we commit to keeping Claude Code available on our $20/month plan going forward” to regain my trust.
As it stands, Codex is looking like a much safer bet for me to invest my time in learning and building educational materials around.
Update: they’ve reversed it already
In the time I was
typing this blog entry
Anthropic appear to have reversed course—the
claude.com/pricing page
now has a checkbox back in the Pro column for Claude Code. I can’t find any official communication about it though.
Let’s see if they can come up with an explanation/apology that’s convincing enough to offset the trust bonfire from this afternoon!
Update 2: it may still affect 2% of signups?
Amol
on Twitter
:
was a mistake that the logged-out landing page and docs were updated for this test [
embedded self-tweet
]
Getting lots of questions on why the landing page / docs were updated if only 2% of new signups were affected.
This was understandably confusing for the 98% of folks not part of the experiment, and we’ve reverted both the landing page and docs changes.
So the experiment is still running, just not visible to the rest of the world?
