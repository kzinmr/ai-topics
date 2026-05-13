---
title: "Why the Wannacry outbreak was so bad"
url: "https://dfarq.homeip.net/why-the-wannacry-outbreak-was-so-bad/?utm_source=rss&utm_medium=rss&utm_campaign=why-the-wannacry-outbreak-was-so-bad"
fetched_at: 2026-05-13T07:01:25.276330+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Why the Wannacry outbreak was so bad

Source: https://dfarq.homeip.net/why-the-wannacry-outbreak-was-so-bad/?utm_source=rss&utm_medium=rss&utm_campaign=why-the-wannacry-outbreak-was-so-bad

On May 12, 2017, ransomware named Wannacry started spreading across the globe, infecting and encrypting Windows systems by exploiting CVE-2017-0144, a flaw that a two-month-old Microsoft patch, MS17-010, had fixed.
It quickly became one of the biggest Windows outbreaks ever. Why was it so bad, and what could have made it go better?
Reliable exploit code
The Wannacry campaign was able to use weapons-grade exploits from the NSA leaked by the Shadow Brokers in the spring of 2017.
Normally, it takes a while for really good, reliable exploit code to become widespread. This wasn’t the case with MS17-010. The NSA knew about the vulnerability MS17-10 fixed and produced reliable exploit code for it rather than reporting the vulnerability to Microsoft so they could fix it. Then a hacking group called the Shadow Brokers stole the exploit. The NSA then had no choice but to disclose the vulnerability to Microsoft, who rushed out a fix before the Shadow Brokers could figure out what they had and leak it. So in this case, reliable exploit code existed from Day 1. All it really took was for someone to build a campaign around the NSA’s digital weapon, called Eternal Blue.
Security professionals often repeat the phrase “Patch Tuesday, Exploit Wednesday,” but good, reliable exploit code rarely works on day 1. It typically takes weeks or months. Wannacry was a problem because in this case, proven exploit code existed before the patch did.
Delay in patching
Troy Hunt
observed
that a victim had to be two months behind in patching to fall victim to Wannacry. Wanna know a dirty secret? It’s not at all uncommon to be that far behind in patching. I get in trouble for saying stuff like that, but this is my area of specialty.
I used to deploy patches for a living and I was good at it. My MTTR was around 21 days and my success rate was 100 percent. I missed a deadline exactly one time in 4 years under this grueling schedule. But I had about a thousand systems to take care of. I’d estimate I could have scaled up to a couple of thousand systems and still gotten all of my patches down within a month. Scale me higher than that, and my success rate would start to drop, because more than 50% of my work was finding individual systems that didn’t take the update from our patching tool and figuring out how to fix it manually.
The bad news
The problem is that far too many companies put one person in charge of 10,000, 20,000, or even 100,000 systems. When you succeed in pushing patches in an automated fashion 98 percent of the time, that still leaves hundreds or thousands of failed patches every month. And a 98 percent success rate is really, really good. It’s not uncommon for the success rate to be closer to 65 percent, because one very popular patching tool’s agent only responds 80 percent of the time and a responsive agent successfully carries out its task 80 percent of the time.
I have no idea why nobody ever talks about this.
And that’s just the tooling problems.
Learned helplessness
impairing the operator is very much a real phenomenon. For these reasons and more, I’ve become an outspoken proponent of autonomous patching–provided the tools you use let you define a deadline and windows where patching can occur, with nothing potentially disruptive happening outside those windows, and they intelligently deploy the latest update.
The worse news
Another dirty secret is that sometimes the person doing the patching able to start deploying right away. It’s likely that because of tax season, some companies didn’t deploy in March 2017, or any other year. Most industries have a busy season where they hold off on patching altogether. I won’t go into the details of who might skip patching in March but I can think of at least two industries who would.
Some
industry has a reason to skip patching just about any month of the year.
And it get worse still. Guess what happens if you deploy the January update, skip the reboot, then apply the February update, skip the reboot, then apply March and reboot? You don’t get the March update. You get January. It’s common procedure to deploy updates, skip the reboot, then come around and reboot systems manually. It’s a trick that lets you start the deployment a day or two in advance. There usually isn’t time to deploy, wait for it to finish, and reboot everything while the maintenance window is happening. The problem with this trick is it’s very easy to miss some systems, and then you have two problems instead of one. Now you have patch debt
and
reboot debt.
My area of specialty is helping companies find these problems and thread security’s camel through the eyes of the needles of the requirements of the business and IT. Yes, you have to get the camel through the eye of the needle
twice
, usually.
And this is on those systems that are current and can be patched relatively easily. Oh yeah, I’ve got even more bad news for you. You know how on
Shark Tank,
the deals just get worse and worse?
Shark Tank
has nothing on patching.
Vendor provided systems
When Wannacry happened, I had people ask me why hospitals still have ancient Windows XP gear laying around. It’s because whoever made the gear only certified it for XP and upgrading it violates their service contract. Even applying Microsoft’s emergency MS17-010 patch for XP probably violates the contract.
Most companies have a lot of systems like that. It might be the systems that operate the badge readers. It could be a piece of specialty software. In those instances, the vendor who sold the system applies the patches, not the company using it. They may only apply patches quarterly or twice a year. In the meantime, those systems are vulnerable.
And then when the operating system goes end of life, it’s vulnerable forever. The operating system has a 10-year life expectancy but it may be part of a system that’s expected to last 20 or 30 years.
Old stuff
Most companies are careful who they say this to, but they typically still have a few ancient systems laying around. Usually “ancient” means Windows Server 2003. Sometimes it means something worse, like Windows 2000, NT 4.0, or Windows 98. Most security departments know what to do to handle these machines safely. Some have the political authority to fix it.
Good companies power these systems down and power them back up for those rare occasions when they need them. Bad companies rationalize keeping them around forever by saying nothing bad has happened yet, so it ought to be OK to keep them around another 10 or 20 years. I wish I was exaggerating. I also wish I’d only had that conversation once in my career. I won’t say it happens a lot, but it happens more than it should.
These systems, of course, are vulnerable forever, unless Microsoft releases an emergency patch for some end-of-life operating systems like they did in the case of MS17-010. Even then, there’s no guarantee you’ll be allowed to deploy it, out of fear the patch will break something.
A better question than why Wannacry was so bad
Frankly, I don’t think the question of why Wannacry was so bad is a very fair question. I’ve worked in the field of vulnerability management about 13 years by now. I’ve been asking myself a different question for years: Why doesn’t a Wannacry happen more often? My working theory is that a Wannacry-like disaster usually requires the combination of an easily exploitable vulnerability and an unhealthy environment with excessive account permissions, compromised passwords, and/or other lack of hardening to facilitate a successful attack. Something I like to call a toxic combination.
Microsoft thinks that as long as governments stockpile 0-day vulnerabilities,
this will happen more often
. Leaks are inevitable.
And given the understaffed state of patch management in corporate headquarters worldwide, it’s inevitable that this will happen again on a large scale. Not every month, and not even every year. But sometime in the future. And more than once.
On a small scale, that’s different. On a small scale, Wannacry-like disasters
do
happen to someone every month. We just don’t typically hear about them publicly.
Vulnerabilities as dangerous or worse on paper as the one Wannacry exploited aren’t rare at all. New ones surface every month. Yes, there’s usually more than one. The two ingredients we don’t have every month are a reliable exploit on day 1, and a toxic combination on a mass scale for that vulnerability to team up with.
That’s not much comfort, I know.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Like this:
Like
Loading...
Related stories by Dave Farquhar
