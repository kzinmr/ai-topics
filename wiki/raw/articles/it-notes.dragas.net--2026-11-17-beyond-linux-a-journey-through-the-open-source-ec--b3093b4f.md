---
title: "Beyond Linux: A Journey Through the Open Source Ecosystem"
url: "https://it-notes.dragas.net/2026/11/17/beyond-linux-a-journey-through-the-open-source-ecosystem/"
fetched_at: 2026-11-17T10:00:44.724921+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Beyond Linux: A Journey Through the Open Source Ecosystem

Source: https://it-notes.dragas.net/2026/11/17/beyond-linux-a-journey-through-the-open-source-ecosystem/

What follows is the text of the talk I gave at Linux Day 2026 in Modena, lightly adapted for the blog. The talk was in Italian, in front of a Linux audience - which explains a few of the jokes.
Linux is one of the best-known players in the open source world, but it's not the only possible path. A journey through the BSDs, illumos and other alternative operating systems, to reflect on Open Source as an idea, a philosophy and a practice of sharing knowledge.
My name is Stefano Marinelli. I'm a sysadmin and consultant, and I run my own small company specialised in open source services and solutions. I like to call myself the "Barista" of the
BSD Cafe
and the
illumos Cafe
, online communities of people passionate about technology, open source and sharing. Today I'm not here just to talk about operating systems, but about freedom, sharing and knowledge. From free software to open source.
My first contact with the Free Software world was in 1996, when I wasn't even 17 yet. I saw a box set advertised in a magazine: "a whole operating system, for free", at a very low price. Something like 30,000 lire. Shortly before, I'd paid roughly ten times as much for the Windows 95 upgrade edition. Dismissive and without a shred of trust, I decided to order it and give it a go. I mean: who would ever write something like that... and release the source code? But six CDs for 30,000 lire... let's try. Worst case, it'll be an experience.
It was love at first shell.
That terminal opened up a whole universe, and to what I already knew (commercial licences, freeware, shareware) I added the concept of Free Software. But I didn't have enough hardware to run two operating systems, so I reinstalled Windows and put it all off. Still, I started thinking. Reflecting. Studying. In 1997 I got a new PC and started using Linux - or, as I was careful to say, GNU/Linux - for everything. Except games. For those, a small Windows partition survived, though not for long.
In 1998 I enrolled in Computer Science at the University of Bologna. Even back then, it was a faculty strongly oriented towards free software. Linux in the labs. I was one of the few who, in the first year, already knew what Free Software was (not free as in price, but...freedom!) and how to use the Linux workstations. That gave me a big advantage, especially from the second year onwards. Renzo Davoli was already pushing hard in that direction. I decided that would be my path. And so it was, and I started pushing too. Windows wasn't the "enemy" to me. The imposition was. Personally, I respect rules, but not impositions. Some people followed me, others watched from a distance. I didn't care. I was widening my horizons.
In the early 2000s I also discovered the BSDs. And I convinced my parents that I needed a laser printer for "university material". In reality, I wanted to print the excellent BSD documentation. Maybe not university material, but the printed FreeBSD Handbook probably served me better than half of the theory exams I took back then. Thanks, mom and dad!
But let's get back to the beginning.
Free Software was born out of a change. In those days, code circulated freely among people. Depending on their needs, they exchanged source code, modified it and shared it again. But at some point this began to change. There's an anecdote that, while not exhaustive, gives the idea: the printer Richard Stallman was using kept jamming, and nobody got notified. He wanted to modify the software so that he'd get a notification, as he'd done with the previous printer. Back then it was common practice, but this time he was refused. "I can't share the source code. It's under NDA." In other words, he had lost control over what he was using. He even wanted to improve the program, and instead he got a refusal.
The rest is history. At least until a few years ago.
Because thirty years ago we fought for Free Software to be taken seriously. When I started working, I was almost laughed at. "That's toy stuff you use at university. The real world uses something else." "Why don't you just use Windows? Everything's easier." And yet, the toys often worked better than the expensive proprietary solutions. Or at least just as well, at a fraction of the cost. "Let's try. Don't pay me until you're satisfied." They smiled, incredulous. Then they paid, happily. We could prove there was an alternative. Free, with no artificial locks. Something that anyone - even the broke but eager student - could study and set up. Technology, that kind of "enterprise" technology, was truly within everyone's reach. There was no need to buy expensive products, or recurring certifications just to have the "right" to work on them. You study, you apply yourself, nobody can stop you. I attended Linux Days. I spoke at Linux Days. For example, here I am, in
Linux Day 2004
.
We won that battle. We won that war.
Linux - chaotic Linux, built by countless external contributors, made of different and varied distributions - has reached everywhere. Open Source is everywhere. But something happened - something beautiful, but terrible: precisely because it reached everywhere, something changed in the spirit. "Too big to fail". And so the big players arrived. Today, Linux development is driven by corporate money: companies like Microsoft (the same Microsoft that once considered Linux its sworn enemy - or Red Hat itself) and other big tech players. In itself, this has been a good thing. In practice, though, it means that they steer its development, even if indirectly. Year after year, it has started to take the shape of a different kind of product. Is the user still at the centre, or is it more code to make Azure run better? Sure, it's Open Source, it's free. But it's increasingly close to the needs of the big companies funding its development and, at times, further from the ordinary user. That's not necessarily bad: many of these investments have given us extraordinary technologies.
But I wonder whether, in the process, we're losing something. Not so much in the code as in the mindset. If not in the kernel, then in the community around it.
Back then, precisely because we were frustrated by "It only works on Windows", we were careful to write portable software. I'll say one word, without going into too much detail: POSIX. Once a mantra: POSIX compliant. A set of standards defining common interfaces between operating systems, so you can write programs that, with few or even no changes, run on different Unix and Unix-like systems. Today, in the communities around Linux, you hear more and more often that POSIX is "outdated". When I send a patch to make a specific tool work on FreeBSD, for example, I often read comments like: "Why don't you just use Linux?". And that déjà vu sends a shiver down my spine: is the community I loved so much turning into a copy, albeit a better one, of its worst enemy?
But careful: I'm not here to speak ill of Linux. That would be absurd. I mean: coming to Linux Day to trash Linux? It's an extraordinary operating system, and I owe it a great deal.
I'm here to remind you that Linux isn't the only way to understand free software. And that a project being less well known doesn't make it less interesting, less valid or less worthy of attention. Because if freedom of choice is truly a value, we must be ready to defend it even when someone chooses something different from what we choose.
So let's see what lies beyond Linux. Because monoculture is a problem, in Open Source too.
Because free software is...free. And we must be free too. Free to choose, to consider alternatives. To contribute, if we want to. To understand which solution best fits our problem. We don't have to pick a single solution "because everyone does". We don't have to turn one monopoly into another. Linux is great. It helps put bread on my table, so I'm a fan. But there are alternatives, other solutions, that can have their advantages. And that's why I want to talk to you about the BSDs and illumos.
The BSDs
BSD stands for Berkeley Software Distribution. And the first curious thing is that its story begins before Linux even existed. We're in the late Seventies. At the University of California, Berkeley, some researchers are working on UNIX, the operating system developed at AT&T's Bell Labs. They don't just use it. They modify it, improve it, write new programs and share that work with other universities.
Remind you of something? We've just been talking about Stallman and the culture of sharing.
BSD was born in exactly that world. So it was born on solid, stable, reliable foundations. Studied by experts, not as a game. BSD was an operating system directly related to Unix. It was a complete and stable system, but it wasn't yet available for "home" systems, the i386 family. Born well before Linux. A curiosity: Linus Torvalds himself, in a 1993 interview, said:
"If 386BSD had been available when I started on Linux, Linux would probably never had happened."
. Yes, you heard that right. Linus Torvalds said it. And we're at a Linux Day!
Then something happened: BSD arrived on the i386, and Unix System Laboratories, controlled by AT&T, started a rather insidious legal dispute: there's our code in BSD and you have no right to use, modify or share it. The University of California was dragged into it too. This was a real blocker for many. Companies were afraid to adopt an operating system with a lawsuit like that in progress. The matter dragged on until 1994, when a settlement was reached and 4.4BSD-Lite was released, with a freely redistributable and legally cleared base.
Meanwhile, Linux was growing, attracting developers, winning users. It didn't have that particular legal uncertainty. I'm not saying Linux succeeded only because of this. That would be unfair to Torvalds and to the thousands of people who contributed to its development.
But it's interesting to think that the history of computing as we know it could have taken a different path. And it's also interesting that, despite these difficulties, BSD didn't disappear. Quite the opposite.
From that story came some of the operating systems I want to talk about today. Systems that took different paths and that are still developed, used and improved. Different operating systems -
careful, not distributions of the same operating system!
- each unique in its own way. Let's start with FreeBSD.
FreeBSD
FreeBSD is probably the most general-purpose BSD. It's a complete operating system, designed to offer stability, performance and a certain consistency in administration. And here's a first difference from Linux I'd like to highlight. In the BSDs, the kernel and the userland, the base tools of the operating system, are developed and maintained within the same project. That doesn't mean Linux works worse. It means the development model is different.
And there's a philosophy I really appreciate:
evolution, not revolution.
It doesn't mean standing still. It means trying to improve without necessarily turning upside down what already works.
Let's talk about some technologies. ZFS, for example. An advanced filesystem, with snapshots, data integrity, replication and many other features. FreeBSD integrates it directly into the system and also lets you use Boot Environments: I can upgrade the system and, if something goes wrong, go back to the previous environment.
Then we have jails. FreeBSD has had a technology for isolating processes, resources and application environments since 2000. Long before Docker arrived. Jails aren't Docker, and I'm not saying they're the same thing. But they let you isolate applications and services simply, with low overhead, using the operating system's own features directly. A bit like LXC on Linux.
For virtualisation we have bhyve, which lets you run virtual machines, including other operating systems. And bhyve is lighter and, often, faster than KVM on Linux. [LINK: my bhyve articles]
But FreeBSD isn't just a system for enthusiasts. Netflix uses it to deliver video content. PlayStation consoles have a FreeBSD-derived base. macOS and iOS also include code from the BSD world. OPNsense and pfSense, two well-known firewall solutions, are based on FreeBSD. In short, we're not talking about a university toy. Remind you of something?
Personally, I've been using FreeBSD for many years, in production too. And it has often let me solve problems simply, while staying in control of what's happening. I've seen cases where, on the same hardware and with the same workload, FreeBSD handled I/O pressure better, with even very significant reductions in execution time. If you're curious, there are several articles about it here on IT Notes. That doesn't mean FreeBSD is always faster than Linux. That would be nonsense. It means there are situations where it can be the better choice.
And for me, this is the point:
I solve problems.
I don't have to defend an operating system. I have to pick the right tool.
OpenBSD
Then there's OpenBSD. OpenBSD was born in 1995 as a fork of NetBSD and is probably one of the most interesting systems when we talk about security and code correctness.
Its philosophy is fairly simple: less complexity, fewer chances for mistakes. The code is continuously reviewed, cleaned up, simplified. Features aren't added just because they might be interesting. Every choice has to make sense within the project. Because the more complex code becomes, the harder it is to maintain, audit and verify.
OpenBSD has also developed some very interesting security mechanisms, like pledge() and unveil(), which let you restrict the operations a program can perform and the parts of the filesystem it can access.
And then there's OpenSSH. Yes, the very OpenSSH you probably use every day to manage your servers. It was born, and is developed, within the OpenBSD project.
But there's another feature I love: the documentation. In the OpenBSD world, insufficient or wrong documentation is considered a bug. The man pages are often enough to understand how to use and configure the system, without hunting for guides of dubious quality scattered across the Internet. And believe me, when you manage dozens or hundreds of systems, knowing where to find correct and consistent information is a huge advantage.
OpenBSD doesn't try to please everyone. The developers follow their own priorities, even when that means giving up something other systems offer. Can it be frustrating? Certainly. But it also offers a great advantage: consistency, predictability and a clear design direction.
For firewalls, routers and systems where security is particularly important, it's an alternative always worth considering.
NetBSD
NetBSD, on the other hand, has a wonderful motto.
"Of course it runs NetBSD!"
And that already says a lot about its philosophy.
NetBSD puts a huge emphasis on portability, correctness of implementation and the ability to run on very different hardware architectures. Not just modern x86 or ARM computers. We're also talking about machines decades old, architectures many consider long forgotten. And careful: it's not just a matter of computing nostalgia.
Keeping an operating system working on such different platforms forces you to write code with great attention to portability, avoiding needless dependencies on a specific architecture.
Remember when, a moment ago, I was talking about POSIX and portability as a value? Well, NetBSD is one of the best examples of that philosophy. Because a system that can run on very different hardware must necessarily care about how correct, clean and portable its code is. And that has positive consequences on the more common platforms too.
There's another aspect I appreciate: continuity. We don't always need the latest novelty, the latest feature, the latest framework. Some devices and applications simply need to keep working, maybe for many years. Think of embedded systems, small computers, hardware that isn't replaced every two years. In these contexts, knowing there's a project that considers portability and support for different architectures a fundamental part of its identity is reassuring.
It's a different philosophy from FreeBSD's and from OpenBSD's. And that's absolutely fine.
NetBSD has also taken a clear stance on AI-generated code: it can't be committed without prior written approval,
because it's considered potentially "tainted" - both in form and in licence
. And in today's extremely polarised world, that's a sigh of relief for anyone who wants to use and develop an operating system without the pressure of always having to do more, add more features and more code.
The BSD Family
There's also DragonFlyBSD, born in 2003 as a fork of FreeBSD, which followed other design choices, especially regarding the kernel and system management. We don't have time to go into everything, but I want to stress one thing. These systems have common origins and share part of their history, but they don't necessarily have the same goals.
FreeBSD is a general-purpose system, also oriented towards performance and production environments. It's stable and secure. On the desktop it might not support all the hardware Linux does, although they're working on it. But on servers it could be one of the best alternatives to Linux.
OpenBSD favours security, simplicity and code correctness. NetBSD focuses heavily on portability and on supporting different hardware. DragonFlyBSD has experimented with other architectural solutions. And yet, they all belong to the big BSD family.
There's no need for one to win over the others. It's not a battle.
There's nothing to sell here. It's freedom. It's diversity.
And that diversity is a strength.
If there's one thing I've learnt over all these years, it's exactly this:
an operating system shouldn't be a religion.
In my daily life, I solve problems. And to solve them, I need to be able to evaluate the alternatives.
Because stability, for example, isn't just a system's ability not to crash. It's also being able to update it without surprises, to understand how it works, to know what happens when something goes wrong. Observability is fundamental, and being able to have it without weaving together fifty Docker containers can sometimes make the difference between ten minutes of work and two hours.
We don't always need to reinvent everything. What's new isn't always better. And the solution chosen by the majority isn't always the best fit for our problem. Often, it's exactly the opposite.
But our journey doesn't end with the BSDs.
illumos
There's another family of operating systems that descends from a different UNIX history. A history that runs through Sun Microsystems, Solaris and OpenSolaris. And that leads us to illumos.
Now someone might ask: weren't you talking about the BSDs? Yes, but the talk is called Beyond Linux, not Only BSD!
illumos isn't a BSD. It descends from another branch of the big UNIX family. The Solaris one, developed by Sun Microsystems. Sun. Anyone remember it? SPARC workstations, servers, Solaris, Java. In the Nineties and the 2000s it was one of the biggest names in professional computing.
And Solaris was a very interesting operating system. Designed for serious machines, serious workloads, situations where a problem could cost a lot. In Bologna, when I was a student, there were some Solaris machines in the UnderLab. I looked at them sideways. To me they were "non-Linux". So I didn't like them.
In 2005 Sun did something significant: it started publishing the Solaris source code through the OpenSolaris project. Imagine: a commercial UNIX system, with years of development behind it, advanced technologies and long experience in enterprise environments, opening up to the community. It wasn't the first free software to be used in companies, of course. But it was another way of doing things. Another model.
And then, in 2010, Oracle acquired Sun. And here things changed. Oracle decided to stop the open development of OpenSolaris and stopped publishing new code updates.
End of the story?
No.
Because the code that had already been released under an open source licence remained available. Oracle could decide not to publish its developments any more, but it couldn't take back the freedoms already granted on that code. And that's how illumos was born. A group of developers decided to carry on the work, starting from the open OpenSolaris base.
Think about it for a moment. A company acquires another company, changes strategy and stops the public development of an operating system. But that system doesn't die. Because the code exists, the skills exist, and there are people willing to keep working on it.
Remind you of something? We began this talk with Stallman and a printer whose code couldn't be shared. Thirty years later, the very possibility of sharing and modifying code allows a whole family of operating systems to keep existing.
This, for me, is one of the most beautiful aspects of free software.
But let's get back to the technology. Because illumos isn't just a nice story.
The technologies and distributions of illumos
From Solaris, illumos inherited some extremely interesting technologies. You already know one: ZFS. ZFS was born at Sun. It's a filesystem, but also a volume manager. It lets you manage storage, snapshots, data replication, integrity checks and much more.
I use ZFS practically everywhere I can. On FreeBSD, on illumos, on NetBSD and on Linux too. And that's already an example of how a good technology can cross different operating systems.
Then we have DTrace. DTrace lets you observe what's happening inside a system, even while it's running. We can analyse kernel calls, processes, performance, behaviours that would otherwise be hard to understand. For a sysadmin, it's an extraordinary tool. Because when a client tells you "the server is slow", the problem isn't knowing it's slow. They already know that. The problem is understanding why.
Then there are Zones. An isolation system that lets you run separate environments sharing the same kernel. Remember FreeBSD's jails? Well, zones were inspired by FreeBSD's jails. The concept is similar, although the implementations and some features differ.
And then Crossbow, for network virtualisation. SMF, for managing services and their dependencies. In short, we're talking about a system with important technologies, born to tackle concrete problems. Not an experiment cobbled together in someone's spare time. And careful, I'm not saying these technologies are necessarily better than those available on Linux or the BSDs. I'm saying they're different, they have their own history and, in certain contexts, they can be particularly useful.
Like Linux, illumos is the base of several distributions, each with different features and goals.
SmartOS
, for example, is focused on virtualisation. It has an interesting peculiarity: the operating system is loaded into RAM, from USB or from the network (or even from the local disk, but then it runs read-only), leaving the disks to the virtual machines and the data, managed with ZFS. It supports native Zones, LX zones to run Linux applications, and virtual machines via KVM and bhyve. Yes, the very bhyve we've already met talking about FreeBSD! Personally, I'm using and experimenting with it a lot. It's not all roses, but I really like some of its solutions. And bhyve on illumos even has a few gems that haven't been brought back to FreeBSD. Open Source and collaboration between projects, at their best!
OmniOS
takes a more traditional road. It's an operating system designed mainly for servers, with particular attention to stability, updates and long-term continuity. It offers stable releases and long-term support versions. You install it, configure your services and use it. Without necessarily having to reinvent everything at every update.
OpenIndiana
is perhaps the closest to the classic idea of a general-purpose UNIX distribution. It can be used on servers, but also as a desktop system, with a full graphical environment. For anyone who'd like to try a Solaris-derived system on their own computer, it could be an interesting starting point.
And then there's
Tribblix
, a rather special project. Created by Peter Tribble, it combines an almost nostalgic, traditional UNIX feel with modern components. It has its own package management system and a modular approach through overlays, which let you install groups of software. A small, independent system with a very precise personality.
Four distributions sharing a technological base, but interpreting it in different ways. Remind you of something? Linux... And that's exactly the point. There's no single way to build an operating system. There's no single development philosophy.
And none of them needs to prevail over the others. What matters is that they keep existing, evolving and offering alternatives. Because, in the end, freedom of choice only has value if we really have something to choose from.
So, why illumos if we already have Linux and the BSDs?
Because there's a whole UNIX tradition that isn't Linux and isn't BSD. Because some technologies now considered fundamental in modern computing were born right there. And, still today, they're stable and reliable. They're refined and polished without being "rewritten" or replaced every five years because there's a new fashion. Because we can use systems that followed different paths, with different architectures and design choices.
But above all, because illumos is also a practical demonstration of the value of free software. Sun opened the code. Oracle decided to stop that open development. The community was able to carry on.
It wasn't easy, and it doesn't mean every open source project can automatically survive the disappearance of whoever was funding it. You need developers, resources, skills. You need someone willing to take care of it. Available code is a necessary condition, but on its own it isn't enough.
And this brings us to a point that, for me, is fundamental. Free software isn't just code. It's also the people who choose to develop it, maintain it, document it and share it.
That's why, alongside the BSD Cafe, I also wanted to create the illumos Cafe. To offer a space to meet, discuss and share experiences about technologies that maybe don't make the front pages of tech sites every day.
Because we don't all have to use the same operating system. We don't even all have to agree. But we can learn something from each other. And maybe discover a solution to a problem we didn't even know we could tackle differently.
Careful, though. I'm not saying the BSD or illumos communities are better than the Linux ones. In our world too there's fundamentalism, prejudice, and people who consider their own choice the only possible one. And that's a problem too. Because it makes no sense to defend software freedom and then look down on someone who decides to use a system different from ours.
We don't all have to agree. In fact, it would be terribly boring. We must be able to disagree, compare ideas, learn something and keep respecting each other - even in disagreement - while building something constructive. What matters, in the end, is being able to choose. And that's true freedom.
More than twenty years ago, at Linux Days, I talked about how Linux could replace Windows in many areas, both on the desktop and on servers. That it was a valid alternative. Today I'm here to tell you not to let yourselves be chained by habit. Linux/Docker/Kubernetes is an exceptional combination,
but not the only one
. It would be serious if it were, because we'd have lost our freedom. The freedom to publish an Open Source project as a tarball of source code instead of putting it "on GitHub" or similar.
Open source is not about doing things the approved way.
It is about giving people the freedom to do things another way.
Open Source and Closed Minds never get along.
Stay free. Always.
