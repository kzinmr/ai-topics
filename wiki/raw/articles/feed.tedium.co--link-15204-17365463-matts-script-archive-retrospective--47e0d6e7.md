---
title: "The Scripts That Reshaped The Web"
url: "https://feed.tedium.co/link/15204/17365463/matts-script-archive-retrospective"
fetched_at: 2026-06-23T07:00:56.959748+00:00
source: "tedium.co"
tags: [blog, raw]
---

# The Scripts That Reshaped The Web

Source: https://feed.tedium.co/link/15204/17365463/matts-script-archive-retrospective

Currently, I’m in the midst of writing
a big post about the roots of web forums, but I hit on an aside weird enough that I decided to stop writing that and work on a separate post. Because I think it actually explains a lot about the way people use the internet.
Essentially, here’s the deal. Around 1995 or so, a high schooler named
Matt Wright
decided to launch a website that shared some basic website tools that he programmed. Many of these were dead-simple, things like contact forms, guestbooks, and web counters. One in particular, WWWboard, became a massive hit, becoming one of the first widely used web forum apps on the internet.
The copyright notice for WWWboard, Wright’s widely used forum-hosting software.
The site Wright built,
Matt’s Script Archive
, unwittingly helped to highlight the divergence between how normal people think about software, and the developer’s perspective.
Wright, and others like him, hit upon an obvious need. Regular people found these scripts, ran them, and suddenly had forums, counters, and contact forms. They got the job done. But programmers who weren’t in high school and weren’t so wet behind the ears looked aghast at what Wright had done: He had spread poorly designed, but widely used software across the internet. This software was packed with security issues, but worst of all, it wasn’t really getting updated all that much.
How serious are the security issues? Well,
a look at OpenCVE
points out some very serious problems that range from bugs that emerged from massive exposure to some questionable design decisions. (Keeping an encrypted password file in the root? Making it possible to grab env variables via a URL? Not smart!)
One exploit in particular, affecting Wright’s textcounter tool, stands out among the list:
CVE-1999-1479
, with a score of 10.0 critical, effectively allows exploiters to execute code on the server as root.
You mean Matt has a script archive? Let’s have the Perl pros take a turn.
This state of affairs got serious enough that a competing website, called
nms
, essentially was launched to replace Matt’s buggy scripts with drop-in versions aren’t full of security exploits from bad coding. Their POV:
The problem is that the scripts in Matt’s Script Archive aren’t very good. The scripts are well known amongst the Perl community to be badly written, buggy, and insecure. Anyone asking for support on Matt’s scripts in any forum will be told in no uncertain terms that they shouldn’t use his scripts.
Unfortunately for some time there were no replacements for Matt’s scripts that you would want people to use. In 2001, the London Perl Mongers decided to address this problem and write a series of drop-in replacements for Matt’s scripts. This project is the result.
(I will note that, since nms itself hasn’t been updated in like 20 years, so maybe you might also want to hold off on using that in 2026.)
TFW your old computer is at risk of getting hacked by a guestbook. (
DepositPhotos.com
)
Matt’s scripts, the easy option, and the problem with overexposure
When so many people use something that it becomes part of the internet’s lingua franca, it’s inevitable exploits are going to emerge. There’s a reason WordPress and Windows each have reputations as bug-ridden, and it’s largely because of the number of eyes on the given tools.
With that in mind, I don’t think it’s fair to blame Wright for having bad code—after all, it wasn’t like he knew it was going to become a huge platform. I think there is a lesson for security teams, however, who are going to be stuck trying to work around people who grab the lowest hanging fruit.
The average person does not want to spend hours looking over every option under the sun to find something good. They just want it to work, and they may not necessarily think much about how to make it better.
That, of course, is why vibe coding is such a big thing nowadays. It hits on the very same tension that an easy-to-access script archive did. And just as with these scripts, you can look at vibe-coded apps as insecure dreck created by someone who didn’t know better, or you can look at them as a democratizing tool.
Problem is, they’re technically both. Can you appreciate one while appreciating the other? I have the answer, and it’s yes.
Matt’s Web Scripts, as it appeared on worldwidemart.com in 1997. One example of many of a random website becoming popular, no real rhyme or reason to it. But hey, Matt had some pretty good scripts! (
Internet Archive
)
Matt’s scripts, remembered
Recently, I spotted an incredible project at the domain that once hosted Matt’s Script Archive. As of a year ago, worldwidemart.com was hosting spam gambling content of the kind that might give your computer a virus.
But that owner let the domain expire late last year. This turned out to be the best thing. Someone who really cared about the legacy of Matt’s Script Archive decided to buy the domain, build a new site explaining the legacy of what once existed there, and why those scripts, as broken as they are, matter.
For something vibe coded, it’s surprising how hard it goes.
The new site
has the definite smell of vibe coding, but you know what? It’s also doing something incredibly important for the history of the internet. As you know, I’m the kind of guy that complains loudly when someone
takes over a historically important website
for less-than-stellar reasons. But I have looked through this page and I do not see any reason to complain—no under-the-radar sketchy “yeah, we did this to sell you something” drama. The page where I thought I would see that, a link located at
/hosting/
, is instead an explanation of how web hosting has changed in the past 30+ years.
Put another way, this website rules. If we’re going to revive domains into zombie websites, I’d rather it was a vibe-coded thing that explains why this was once historically relevant than something that a spammer doesn’t even want.
What was Matt thinking? He just wanted to be helpful. And that he was.
Script-Free Links
If you love old stuff like this,
I recommend checking out the dead-website archive
rip.so
, which hits this very dopamine zone.
On a related note,
this
Verge story
about the security risks of vibe coding feels especially relevant given today’s piece.
I find the fact that LinkedIn
has like a dozen games that it expects you to play every day to be bizarre. We needed a name for it, and “
corporate puzzleslop
,” what Juniper Dev landed on, is basically perfect. (Great channel, too, she knows her stuff.)
--
Find this one an interesting read?
Share it with a pal
! (Did Matt run your guestbook in 1997?)
And be sure to check out the latest stuff on the
Tedium Shopping Network
.
