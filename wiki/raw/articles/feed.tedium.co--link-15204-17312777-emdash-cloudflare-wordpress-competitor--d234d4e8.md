---
title: "A Clever WordPress Revamp, Hold The PHP"
url: "https://feed.tedium.co/link/15204/17312777/emdash-cloudflare-wordpress-competitor"
fetched_at: 2026-05-01T07:01:03.396133+00:00
source: "tedium.co"
tags: [blog, raw]
---

# A Clever WordPress Revamp, Hold The PHP

Source: https://feed.tedium.co/link/15204/17312777/emdash-cloudflare-wordpress-competitor

Cloudflare started its life
nearly 20 years ago, and I found out about it basically because I was running a blog—and obsessed with keeping it online.
ShortFormBlog
was many things, but the most important was that it was barely held together technically because I did not know what I was doing back then. I learned so many things about content management from it, but I had to make a few mistakes first. First: I originally built my numbers and blurbs as custom fields, rather than using something flexible like Markdown. (I eventually figured out a system to optimize them using unordered lists and CSS. But that only happened because—I kid you not—AOL News wanted to publish some ShortFormBlog-style posts and I needed to figure out a way to make them portable.)
In the midst of all this, I stumbled on
Project Honey Pot
, the anti-spam initiative that led to Cloudflare, which they were working on at the time. I realized this was going to be a very useful tool. And as a result, I was such an early customer of Cloudflare that they sent me a T-shirt listing me as one of their first 1,000 customers.
So it would be a weirdly neat homecoming if I could figure out a way to make ShortFormBlog work with Cloudflare’s new content management tool
EmDash
. It exists to convince scores of people to move their old unstable, insecure WordPress blogs over to Astro.
From a cultural perspective, we have moved past WordPress technically in so many ways, but it sticks around in part because sites stick around, and they can be difficult to move or restructure. Site migrations are hard, and I’ve been through a few in my day. But I dread having to move the 16,000 posts on the original ShortFormBlog archive to somewhere else. (I actually tried, and it was just so much damn work that I had to set it aside.)
However, maintaining a WordPress site for something so old is just not a realistic option for most people. It’d be better if the final result was static and relied on minimal plugins.
If you think about it, Cloudflare is really built on the foundation of fixing poorly coded WordPress sites so they actually work. (
DepositPhotos.com
)
EmDash is a path forward for that, utilizing the of-the-moment technical capabilities of
Astro
, a website framework that mixes the benefits of static site generators and React-style interactivity, and Cloudflare workers. However, it looks like WordPress in every public-facing way.
This has been pitched as a spiritual successor to WordPress, and one might wonder why Cloudflare would be interested in such an endeavor. To me, it’s very simple: Essentially, it could potentially help the company save costs by putting very complex sites on static ground. I’ve written in the past about how PHP remains a surprisingly good option for content management systems because it’s mature. But the flipside of that is that PHP is also quite slow, and comes with a ton of additional security risks that more modern systems have built for with a proactive posture, rather than a reactive one.
This move makes 100% sense, and not just because
Cloudflare acquired Astro
three months ago. Essentially, this could solve a problem for the company: By convincing old WordPress sites to move to EmDash, it lowers reliance on the company’s caching infrastructure to simply offer a good experience. That has benefits from both a security and a bandwidth perspective. So many of these sites should be static. But they aren’t, and that’s so much of the reason that CloudFlare exists. But when it has competitors like Vercel, which is essentially built for another generation of website, anything it can do to chip off some of the legacy is welcome.
Sure, it looks like a plain blog, but it’s built on some cutting-edge WordPress mimicry.
No, this won’t work for every site out of the box. Part of the reason these Byzantine old WordPress sites stick around is because they have such strong reliance on old, barely functioning plugins that it’s literally impossible to disconnect them.
This is one exit ramp. But it is an exit ramp with some awkward elements. It is clear, looking at the code of this tool, that you’re essentially meant to use it with Claude Code to do your scaffolding and maybe even some of your plugin design. Given the world we live in, you may or may not love that. But on the other hand, I can see the other side of this—that many of the sites that would benefit from a move to EmDash are likely not getting much love anyway. These are sites that are hobbyist sites, or are corporate sites forever stuck kicking the can down the road.
In one sense, if EmDash takes off, further smoothing the edges of modern development, it could cause a drop in WordPress’ massive user base, which could harm the ecosystem of plugin-makers that support it. (Admittedly, though, it needs to work on the ramp-up process, which can be a bit confusing within Cloudflare’s own interface.)
But in another, these are the sites that are most likely to not update their WordPress installs in numerous years. And because of the way WordPress is designed, the site is a giant attack surface, always at risk of one PHP-based exploit or another. It is the Windows of content management systems, and that puts it in a position where some are just going to want a full reset.
As metaphors go, EmDash wants to be Linux Mint—something that feels like Windows, but has different guts. It may not work, but if we’re going to get rid of some of the internet’s old cruft, someone has to try.
I’m hopeful my messy, complex ShortFormBlog archive makes the leap.
Dash Free Links
There’s no need to double-dip with endless shrimp,
but it seems
Red Lobster is about to
. Hmm, seems like a bad idea.
Drama ahoy:
The speedrunning world is facing a serious scandal after one of the world’s top
Super Mario Bros.
players, Niftski, accused another elite speedrunner, averge11, of
trying to railroad him
for using a specific technique.
Do the Texas Rangers
do delivery? If so, I’m interested in buying
their new hat
.
++
Find this one an interesting read?
Share it with a pal
!
And thanks again to the simple-but-perfect
la machine
for sponsoring.
