---
title: "There's No Limit to How Bad Code Can Get"
url: "https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/"
fetched_at: 2026-09-07T10:01:44.990005+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# There's No Limit to How Bad Code Can Get

Source: https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/

[In reply to a comment about burning it down to start from scratch when technical debt becomes overwhelming]
In my experience it's
so rare
for that to work.
You announce the old thing is irrecoverably drowning in tech debt. You spin up a team to rewrite it from scratch. Work begins.
Meanwhile the old thing remains a moving target: it's running the core business, so changes are still necessary. The developers working on it know that it's going to be made obsolete by the new thing soon, so they don't have any incentive to go beyond the smallest effort possible to add the new features. Technical debt continues to mount.
Meanwhile, the team working on the new thing are ambitious and probably a little naive. They start out at a great pace - it's greenfield after all - but as time progresses it becomes apparent that nobody fully understands the behavior and scope of the thing they are replacing. If it was well documented and tested it wouldn't
need
to be replaced, after all...
After months (or even years) without delivering value, the pressure is on to "ship it", so the new system is launched to handle a subset of what the old system handled - or often for some new feature that was too hard to build with the now mostly unmaintained old system.
... so now you have TWO systems in production - the janky old system that nobody wants to touch, and a new system which handles just a few production features and is 80% inactive code that is meant to replace the old system, eventually.
If you're
really lucky
the company won't have lost patience with the new system and will allow that work to continue. The longer this all takes, and the longer the old system stays in production and stubbornly continues to work, the higher the risk that "priorities have changed" and the new system total replacement work is abandoned, leaving you with two systems where you used to have one.
The best article I've read about completing this process responsibly is
Migrations: the sole scalable fix to tech debt
by Will Larson.
If I run into a situation like this in the future, my strong recommendation will be to shore up the old system with as much automated testing as possible and then seeing if targeted refactors can get it to the desired shape. My hunch is that in many cases that will have a much higher chance of success than the siren call of a greenfield replacement.
