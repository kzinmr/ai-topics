---
title: "The Server That Wasn't Meant to Exist"
url: "https://it-notes.dragas.net/2025/05/13/the_server_that_wasnt_meant_to_exist/"
fetched_at: 2026-04-28T07:02:50.147688+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# The Server That Wasn't Meant to Exist

Source: https://it-notes.dragas.net/2025/05/13/the_server_that_wasnt_meant_to_exist/

Yesterday I read a piece of news that brought back an important - and painful - episode from my career.
A story about trust, technology... and the kind of problems that can't always be solved.
About 16 years ago, I was contacted by an old friend. He was worried about a situation involving some mutual acquaintances.
To keep it short: an entrepreneur - administrator and owner of several companies - had died suddenly.
He was the kind of man who centralized everything, and his wife and children found themselves struggling to manage things.
One of the sons decided to cash out and leave the family business (focusing on his own career), while the others chose to stay involved in day-to-day operations.
The wife, elderly and retired for years, ended up at the helm, but she was clearly out of her depth.
The main issue was the complete lack of information flow: no digital systems of any kind were in place.
Employees had their own PCs (sometimes even personal laptops), and there was zero control over anything.
All the accounting and administrative data were scattered across individual machines, often taken home at the end of the day.
From the owners’ perspective, all they saw was a huge cash flow coming in - yet the accounts were always in the red.
"If we keep going like this, we’ll be bankrupt in just a few years", I was told.
What I could do was set up a proper IT system, structured to make data management transparent and traceable.
I planned - and got immediate approval for - the purchase of routers, switches, various networking devices and a server with several disks.
The OS of choice, as was my habit at the time, was NetBSD
. Thanks to XEN, I set up multiple VMs.
One handled the NAS duties (using Samba, so PCs could connect and store files directly there), another ran
Archivista
.
I even worked on translating Archivista’s interface into Italian, since it wasn’t yet localized, just to make it easier for users.
As usual in those days, I added a caching proxy (Squid) and a content filter (DansGuardian), to ensure proper usage.
The internet connection was very slow and often collapsed under heavy load - mostly recreational use, as logs revealed.
There was no supervision, and many people were downloading movies and such on company time.
As often happens, not everyone was happy.
One figure in particular - the late owner's former right-hand man - opposed the new system in every possible way.
According to him, none of this was necessary. But the real alarm bell had been his sudden change in lifestyle.
He’d made purchases that didn’t remotely align with his salary.
At the time, the company had no oversight and dealt with a lot of cash. It was all technically legal, especially given the nature of the business. I won’t go into detail - privacy matters.
Once everything was up and running, we trained the employees to use the new system.
Most were thrilled - finally able to work properly, with files in the right place and centralized document management.
OCR, archiving, etc. were all seen as major time-savers and a big boost in efficiency.
Some of the accounting staff remained skeptical, of course.
Since all of this was far from where I lived at the time, I went back to my life once the system was stable and everything in place.
A few quiet days passed - then one morning, my phone rang:
"Good morning, this is XYZ - I handle some technical aspects of a software suite used by the company where you've just installed everything.
We need to install our software, and I understand you set up the server. I’ll need the full server diagram and all the admin passwords".
I explained that it wasn’t a Windows machine, as he assumed (without even having seen it), but NetBSD, running NetBSD and Linux VMs.
A few seconds of silence.
"I see. Then I’ll have to wipe it and install Windows. I need Windows, and I don’t have time to wait for a new server - I’ll proceed tomorrow morning".
I froze. I told him that was not possible - the entire workflow now depended on that machine, and erasing it would be catastrophic.
"I’ll speak with the owners", I said, "and I’m sure they’ll provide you with a separate server within hours".
No use. He started to backpedal.
To my (young) eyes, the goal was now obvious: that server had to disappear, and fast.
He said he would "restore the previous situation", and claimed the server couldn’t remain as-is because
he
needed it.
I immediately called the owners. Sadly, due to inexperience and inability to handle the situation, they panicked.
They asked me to consider letting him do it, and then redoing the setup later, covering the cost of new hardware and my time.
I refused. I was young, but I already had this mindset: do what’s right, even at the cost of profit.
This was clearly a maneuver to eliminate controls - the server, the centralized filesystem.
The goal was to hide the real accounting data from owners and auditors. Thousands of euros vanished every day through "transactions".
The owners had started to understand, and this new pressure confirmed just how rotten things really were.
I called that man back and told him clearly: the server I’d built wasn’t to be shut down.
If he needed one, I’d deliver a new server by that evening, just for him.
At that point, he finally spoke more openly:
"You don’t get it, do you? I need
that
server. Not
a
server.
You’d better go along with this — or you’ll have serious trouble working in this area again".
And other similar, "nice" sentences. I replied calmly:
"Look, I’m just doing a favor for some friends. I don’t have clients in your area — and I don’t want any.
I’d rather do a good job for them than gain new clients".
No way through. He kept pushing - confident in his own sense of "power" - until I said what I had been trying to avoid.
Because I had recognized who he was.
And the disappointment hit me twice as hard - I used to admire him.
He, however, had not recognized me.
"Excuse me, but why are you talking to me like this? You’ve known me since I was a child. Don’t you remember? I’m the nephew of..."
He froze.
He understood immediately.
He connected the dots and knew full well that a single phone call to someone extremely close to me - someone he owed a great deal, both personally and professionally - would have the opposite effect he was aiming for.
That person had helped him greatly over the years. So much so that he folded:
"Oh... I’m so sorry... I didn’t recognize you. I’ll find another solution. Sorry again".
He hung up.
Never heard from him again.
I informed the owners that the issue was resolved (leaving out most of the details), but it didn’t last long.
Within days, a series of "unfortunate events" hit the server: the UPS failed, the server was "accidentally" unplugged and plugged back in incorrectly, and finally... it stopped responding on the network.
It was dead.
And when we opened it, the hard disks were just... gone.
But there was one thing nobody (but the owners) knew.
The server - slowly but surely - had been backing up externally.
All the data up to that point had been copied to a device we’d quietly installed at the owners’ home: a tiny PCEngines Alix, running NetBSD with two USB drives.
It was slow, yes - slow hardware, slow disks - but reliable.
That very device still works today (with FreeBSD) and provides services elsewhere.
I handed all the data to the owners and asked what they intended to do.
They took some time - days, then weeks.
Eventually, they said they’d probably investigate whether there were grounds for a theft report.
I never heard more about it.
But then came a tempting offer:
"Come work for us. Manage our network infrastructure and help us overhaul our internal procedures.
Even if you’ve just bought a house far from here, even if you’d have to leave your other clients -
we’ll pay you enough to forget everything else. Name your price".
They would’ve done it, too.
Our mutual friend urged me:
"They’ve got a huge cash flow, but too many people are taking advantage of them due to lack of control.
Take the job - they’ll treat you like gold, and you’ll really help them".
I didn’t think twice.
I turned it down
.
I like my work.
I like doing what I do - and the income is a consequence, not the cause.
I would’ve had to give up my life, my path, to fight battles I don’t enjoy - and that I might not even win.
Because sometimes, dishonest people
do
win.
I’ve never regretted declining that offer.
I lost touch with all of them years ago, but I later heard things went as I predicted:
the owners gradually backed out.
They made another request later on, which I tried to fulfill — but even that was blocked, just when everything was ready.
At some point, I had to walk away.
Not because I wanted to abandon them in a time of need, but because they weren’t giving me the tools to do what was necessary.
They were so overwhelmed, so unprepared, that they ended up yielding to pressure - often from the very people who were hurting them.
And of course, I’ve left out the worst parts of the story.
(Author's note: Many readers, understandably struck by the severity of the events, have speculated about the involvement of organized crime. I want to clarify that, while the situation was extremely problematic and dishonest, that wasn't the case. The "worst parts" I alluded to referred to other internal dynamics, abuses of trust, and improprieties that I prefer not to detail further for privacy reasons and to avoid weighing down the narrative.)
That’s when I realized:
Some situations are so rotten, they simply can’t be salvaged.
And that’s okay.
I solve problems
- it’s what I do best.
But I can’t solve
every
problem.
Especially not when those involved choose to protect the problem instead of fixing it.
