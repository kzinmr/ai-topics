---
title: "Rejoice, leap seconds are dead!"
url: "https://www.jeffgeerling.com/blog/2026/rejoice-the-utc-leap-second-is-dead/"
fetched_at: 2026-10-31T10:00:56.764461+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Rejoice, leap seconds are dead!

Source: https://www.jeffgeerling.com/blog/2026/rejoice-the-utc-leap-second-is-dead/

There will never be a leap second again. At least not for UTC.
At the CGPM
, they decided the last leap second we'll ever see for UTC, or Coordinated Universal Time, happened back at the
end of 2016
.
Of
course
they made that decision while I was out on vacation, so I'm just getting this video up now:
But what's the CGPM, why does this matter, and why am I excited about it?
CGPM and BIPM
The CGPM is the
General Conference on Weights and Measures
, and yes, 'GCWM' is not 'CGPM', because CGPM is an abbreviation for the
French
title:
Conférence Générale des Poids et Mesures
.
And don't get me started on UTC, which stands for "Coordinated Universal Time". It's not CUT, and it's not even the French version, TUC,
it's a compromise
so
neither
language would win!
Anyway, the CGPM is a conference overseeing the BIPM, the
International Bureau of Weights and Measures
. The CGPM is where they talk about things like redefining measurement units.
This year, they passed Resolution 5, killing the leap second 8 years earlier than the 2035 deadline
they had set
in their 2022 meeting.
Starting on
May 20, 2027
,
UTC will never have another leap second added or taken away
.
UTC will be allowed to deviate from UT1, the Earth rotation time, for up to 1 hour. So we could have 'leap hours' someday, but the resolution doesn't say anything about them, and it'll take centuries to drift that far. That's a problem for future horologists.
Negative leap second
But why now? Why couldn't they just kick the can down the road like we've been doing since 2016?
The big problem is there was a 30% chance we'd need a
negative
leap second between now and 2035, because the Earth's rotation is has been
accelerating
lately. We've had 27
positive
leap seconds between 1972 and today, but we've never taken one
off
.
Imagine every computer program that deals with time having to work in a condition that's never been tested before. It'd likely be worse than
Y2K
!
The resolution called this out specifically:
"Industrial users and the synchronization needs of national critical infrastructures, for example transportation, energy distribution, telecommunication, and space projects require UTC to be continuous without any future adjustment."
(By the way, if you're a time-nut and into this stuff, watch the entire
CGPM Day 3 Livestream
, which the source of the slide at the top of this section. Riveting stuff!)
Technically these industries
can
handle leap seconds, but the pain is not worth the benefit, especially since astronomers
already
deal with time offsets for Earth's rotation, using UT1, which is a variable time offset from UTC.
We still have plenty of other time problems we'll have to deal with like
Y2K38
. So I think BIPM members were thinking, "We have a chance to fix
one
of these problems, so let's at least do that!"
Thus, UTC will forever be locked 37 seconds ahead of TAI (
International Atomic Time
).
By the time it's a problem, we'll probably be working on a
galactic
time standard, and UTC will be a quaint hobby for
time-nuts
, much like water and pendulum clocks.
Why it's okay
But won't it cause problems for scientists and astronomers, if we let UTC drift from the Earth's actual rotation a few seconds? Not really.
At least not worse than things like timezones. Timezones and the politics with things like Daylight Saving Time are all kinds of crazy!
But we can deal with those time
offsets
more easily. We already use them for time zones and astronomy.
It's much harder to deal with absolute time scales (like UTC) that add or remove seconds. Computers hate it when a billion nanoseconds suddenly vanish or appear while they're running.
Companies like Meta, AWS, and Google
spent tons of money
building 'time smearing' features into their infrastructure to deal with
positive
leap seconds, and they
still ran into problems
.
Even assuming technical perfection, there's risk involved in the rollout of a leap second. Since they're decided by committee, you can't automate when one is added, your system has to either constantly update a leapseconds file, or you have to have someone monitor the leap second announcements and update your software to adjust, assuming it's offline. Remember that not every piece of time-critical software is tied into Internet time systems!
And assuming every company monitors for leap seconds, they also have to build and test their own system to add or remove a second. It was hard even for giant corporations in 2016; I can't imagine the vibe-coded disasters that await us now.
A cool side effect is software can drop leap second handling now. That code was always a little flaky, and not all programs even acknolwedged leap seconds'
existence
. Some programs would just YOLO it, and that's a recipe for disaster.
WWV/WWVB
There are downsides. WWV radio time has a special field in its data for leap second handling. They broadcast
DUT1
, which is the Earth Rotation-based time UT1 minus UTC, and their current signals assume it's always less than 1 second.
Astronomers and certain navigation systems use that time for their work, so once it's off by more than 0.9 seconds, that could create problems. They have probably 5 to 10 years to solve it, but it
is
a bit of a pickle.
Why does Earth's rotation change?
But one question you might have is why is Earth's rotation speeding up? I know I did. Apparently there are changes in the Earth's core which are hard for us to see, but easy to measure. And those are speeding up the rotation right now.
I'm not an expert on geodesy, but over the long term, the Earth should go back to slowing down.
Other developments
There are some other reasons I think this is good news. Leap seconds were always an annoyance for timekeepers.
They'd much rather spend time on bigger changes, like redefining the second. Right now it's based on the
hyperfine transition frequency of cesium-133
, as it has been for decades. But newer clocks are orders of magnitude more precise. Seconds will probably be shift to optical, or maybe even
nuclear
clocks (pictured above: NIST's F4, still a cesium fountain clock, but cool nonetheless!).
But changing the second will change
other
definitions governed by the BIPM, like how long a meter is, because
that's based on time
, too!
On top of that, if we
do
start exploring space more rapidly, UTC might lose relevance. We've already seen Lunar clocks running about
56µs faster
per day than clocks on Earth. If we have a mission to Mars, we'll have to figure out a better interplanetary time scale.
Conclusion
But in the end, especially as a programmer who's dealt with time bugs, I'm happy to see one annoying feature of UTC get removed.
