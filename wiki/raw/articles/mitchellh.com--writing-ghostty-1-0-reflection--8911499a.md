---
title: "Ghostty: Reflecting on Reaching 1.0"
url: "https://mitchellh.com/writing/ghostty-1-0-reflection"
fetched_at: 2026-05-01T07:02:02.968851+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty: Reflecting on Reaching 1.0

Source: https://mitchellh.com/writing/ghostty-1-0-reflection

This isn't a release announcement. Ghostty 1.0 is out. You can download it
and read about it
on the Ghostty website
. This is a
personal reflection on the project.
Ghostty 1.0 is out.
If you told me two years ago that I would be releasing a terminal emulator,
I wouldn't have believed you. I've always been a fan of the terminal,
my entire career was built around shipping terminal-first software. But
they're a solved problem, right? That's what I thought.
I started the project in 2022 merely as a way to play with
Zig, do some graphics programming, and deepen my understanding of
terminals. I never intended to release it. I didn't think there was
innovation to be had. I thought I would learn a lot over a few months
and move on.
But as I worked on it, I looked at other terminals differently. I saw
tradeoffs that I didn't like. I saw features that I wanted. I saw
performance that I could improve. I saw stagnation. There are many
fantastic
terminals out there and you should use them if they work for you. But I wanted
something different and thought maybe others did too.
And so Ghostty was born. It's not perfect, it's not done, it's not for
everyone. But it's mine. It's a reflection of my values and my vision
for what a terminal could be.
To learn more about how Ghostty differentiates itself from other
terminals and my vision for the project, read the
Ghostty 1.0 is coming
post.
The Private Beta
The most controversial part of Ghostty was the private beta. Oh boy,
the private beta. I vastly underestimated the effect this would have
on the project. Good and bad.
The Private Beta: The Good
First, why a private beta? The primary reason was to manage my own
personal bandwidth. I began publicly sharing the project shortly before
my first child was born. I have experience launching software and
I knew the stress that comes with it. I wanted to avoid that stress
and be able to focus on my family. I felt I could curate a small group
of interested users to throttle issues, only increasing the user base
as I felt comfortable.
A secondary, but much less important reason was that I felt a terminal
emulator more than most software either works or it doesn't. You can't
ship a terminal emulator that emulates only half the features Vim needs.
You can't incrementally improve a terminal emulator below a certain
threshold of functionality. I wanted to ensure that the first public
release met that threshold. I wanted people to be able to use it productively
and professionally right away.
On these two fronts, the private beta was a
massive success
(far beyond
my expectations). I was able to manage my bandwidth and focus on my family.
For the first year of my daughter's life, I woke her up every morning,
I played with her every wake window, I went to every doctor's appointment,
I was there for every milestone
1
.
And the beta community was
amazing
. They were patient, they were
understanding, they were helpful. They found bugs, they provided feedback,
and
they made Ghostty so much better
than it would have been without them.
I can't thank them enough.
The Private Beta: The Bad
Everything else was an unintended consequence of the private beta. The
hype, the frustration from those who couldn't get in, the elitisim
perceived by some, etc.
I didn't anticipate the hype. Some people think I am lying when I say
this. I'm not. I'm not so naive to think that private betas and exclusive
access don't generate hype
in principle
. But I didn't think many people
at all would be interested in a terminal emulator. I thought I was building
boring software for a niche audience. No hype!
But I was wrong, and the consequences were real. People were frustrated
that they couldn't get in. People felt left out. People felt like I was
being fake to generate hype. The waitlist grew larger than I was comfortable
allowing in (given my prior stated priorities).
I'm sorry about that. All I can say is that I didn't intend for this
to happen. I ramped up beta invites to try to get as many people in as
I felt comfortable with (well, a bit beyond that). We ended the beta at
around 5,000 users in a Discord of 28,000 at the time. Not quite the percentage
of access I wanted for people but more than I could handle.
The good news is Ghostty is now public and everyone can use it! I hope we can
put the negative aspects of the private beta behind us and focus on the future.
One more negative aspect of the hype is the expectation of Ghostty
being revolutionary.
It is and it isn't. Ghostty has different goals and
tradeoffs than other terminals. For those looking for those properties,
Ghostty is a breath of fresh air and does things that no other terminal
does. But for others, it's just a terminal. And that's okay. I hope you
find a terminal that works for you and I don't claim that Ghostty is the
end all be all of terminals.
The Tech Stack
Ghostty has an unconventional tech stack and architecture:
Zig
for the core and platform-specific code for
the GUIs. More details on the tech stack can be found in the
original talk I gave on Ghostty
.
Two years later, I'm extremely happy with the tech stack and architecture.
I think it was the right choice for the project but more than that,
I think this architecture could be the right choice for many projects
2
.
Zig has been an absolute joy to work with. I have
fun
writing Zig every
single day and that fun hasn't diminished a bit over two years. The build
system is fantastic, the community is amazing, and the core maintainers
are brilliant. My excitement is well known and I've also put my money
where my mouth is by
sponsoring the Zig Software Foundation
.
The split between shared core written in Zig and platform-specific GUIs
has also been a success. I've been able to effortless integrate
platform-native experiences
into Ghostty while keeping over 90% of the code shared.
The beta community has also had no problem contributing to the project.
I think this shows that despite being a new, niche language, Zig is
easily approachable and productive for new contributors. This is great
news for the future of the project.
The community that formed around Ghostty was unexpected and amazing.
To be specific, I'm talking about the private beta community. The public
community is a bit of a wild west due to the unstructured nature of not
having access to the software. But the private community has focus and
purpose and it has been a joy to be a part of.
The Ghostty community is a group of people who are passionate about
terminals (of course!) but also about performance, design, software
quality,
doing things right
and for the right reasons. It's a group
of people that are pleasant to be around and collaborate with. It's a
group of people that I've really enjoyed getting to know and I'm excited
to continue to work with.
For me personally, it's also unlikely because most people in the Ghostty
community are also
new to my work
. Most don't have a background in
infrastructure and therefore aren't familiar with my previous work. It has
been fun to build a new community and it reminds me a lot of the early
days of my career when I was building a community around my first open
source project.
A Post-1.0 Future
Ghostty 1.0 is out but the project is far from done for me. Even the 1.0
is less complete than I would have liked! But I had to draw a line in the
sand somewhere and I think the 1.0 turned out great.
For the short term, I want to continue focusing on the
"best existing terminal"
goal. I want to
shore up the features that didn't make it into 1.0 and fix the bugs that
are still present. I want to make sure that the foundation that Ghostty
is built on is solid for future innovation.
In the medium but not too long term (within 2025), I want to shift focus
to release a stable and standalone
libghostty
that can be used by other
projects to build their own terminal emulator frontends. I think
libghostty
is the most promising part of the project for the long term impact Ghostty
can have within the tech community.
But, regardless of goals, Ghostty will always first and foremost be a
passion project for me. I work on this project because it's fun and I
want to make sure the community and I don't lose sight of that.
Thanks
I believe nothing in this world is accomplished alone. I may have started
Ghostty alone but I didn't finish it alone and I have so many people to
show appreciation for along the way.
The impact of the Ghostty beta community cannot be overstated. I said
this already in this post but Ghostty is only as feature rich and polished
as it is thanks to the attention to detail and feedback of the beta
community. I'm extremely grateful to everyone who participated in the
beta and helped make Ghostty what it is today.
The Discord mods deserve a special shoutout. They worked
hard
to keep
the peace and keep the community focused on the right things. I could see
their effort daily in trying to create an environment that allowed me to
focus and the beta community to thrive. We have less than 10 mods for
30,000 people and they did an amazing job given the circumstances
3
.
And finally, and most importantly, I want to thank my wife.
We're first time parents and juggling a new baby with a side project I
wanted to find time to work on was no small feat (even with the private beta
aspect). She helped me find the time to work on Ghostty and she patiently
listened (fell asleep) to my ramblings about font rendering.
I hope you enjoy Ghostty 1.0 and feel the love and care that went into it.
I'm excited to see where we go from here!
