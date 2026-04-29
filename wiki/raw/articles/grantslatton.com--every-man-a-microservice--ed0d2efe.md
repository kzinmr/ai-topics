---
title: "Every Man a Microservice"
url: "https://grantslatton.com/every-man-a-microservice"
fetched_at: 2026-04-29T07:02:15.825513+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Every Man a Microservice

Source: https://grantslatton.com/every-man-a-microservice

Every Man a Microservice
Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.
— Melvin E. Conway, How Do Committees Invent?
Conway's law appears true if you observe organizations and systems as they are,
but the causality is reversed
.
Systems are not
conceived
by organizations, but by a single individual or a tight-knit cabal.
As such, there is no communication structure to emulate. The initial idea is conjured as a gestalt and an organization
is built around
the system as it comes into existence and operates.
And thus we invert Conway's law
: A system's design informs the communication structure of the organization that is built around it.
With this in mind, we can ask: what design facilitates the most effective organization?
There's a whole landscape of solutions here, but I just want to focus on one that I saw work
extremely
well in the earlier years of AWS.
The right way
The idea is your system is made up of person-sized services. A person-sized service is one whose codebase is in the realm of a few tens of thousands of lines of code.
This scale is such that a single developer, working on that codebase full-time, can keep the whole codebase in their head.
N.B. By "codebase in head" I don't mean they literally know every line of code. I mean they have a complete picture of all the modules, interfaces, data structures, scaling dimensions, tradeoffs, design decisions, etc.
You want there to be a 1-to-1 mapping between each service and an individual who has that service's code completely loaded into their brain.
The advantages of having the whole service loaded into an individual brain is hard to overstate.
It enables a ton of offline mulling
. Your devs know their domain so well, they'll have regular shower-thoughts about how to optimize their service.
You reach consensus on improvements faster
. Alice has an idea in a shower. She wants Bob's system to start batching requests to hers to improve her cache hit ratio. She tells Bob the idea in the morning. Bob calls over Charlie, whose service would also be affected. In 20 minutes they agree on a path forward. The code is shipped after lunch.
You actually have fewer outages and issues
. You might think an organization that designs features in 20 minutes and ships them after lunch is going to break things by moving so fast. But in practice, a single engineer with 100% context will anticipate and design around issues better than a design review by a whole team of devs who each have 50% context.
Quality goes up
. Each owner has a narrative for the health of their codebase: aspirations for future improvements, haunted by lingering jank. They take this holistic view into account when considering all ideas. They have the familiarity needed to do deep, refactoring integrations, but also to safely add hacks when the business needs it.
Architectural changes are politically manageable
. It's much easier for technical management (i.e. principal engineers) to rearchitect the system, because individual devs have essentially no political power or desire for such. They won't defend their service if it becomes vestigial as long as you give them something else to own.
Engineers develop faster
. Take a college-hire and give them one of the smaller services. Tell them "this service is yours, and you are this service, you are one". This is a sink-or-swim tactic, but a good one. Engineers that can't take individual ownership are toxic to the long-term health of the org. Those that can have a much higher likelihood of evolving into high-value
lieutenants
.
The wrong way
If you've worked at a traditional company, you've probably seen the inverse of all this. Services aren't owned by individuals, but by whole teams. A team of 8 people might own 3 services. Everyone is kind of vaguely familiar with all of them, but nobody is a master of any one.
Because nobody is a master, people will tend to implement changes in a purely accretive way. They're afraid to do deeper refactors to integrate changes more holistically.
And for good reason! When they attempt such deeper refactors without a complete understanding of the service they're operating on, they're stumbling in the dark and cause outages. They do design reviews with the team to try to mitigate this, but nobody knows enough to contribute more than surface-level concerns.
Managers in charge of teams will resist deprecation of the services their team owns. Not only will they do this, but they will actually invent new services that don't need to exist to justify increasing their headcount (which increases their status).
Risks
What happens when the owner of a system gets hit by a bus?
Or, less dramatically, leaves the company.
In practice, engineers in such an org don't
only
have context on their single service. They'll typically have a decent amount of context on the services theirs touches, and vice versa. After all, who is doing code reviews for whom?
Most of the devs who've been around for a while will have owned a few different services at different points in their career. When they joined as a college-hire, they were given a tiny metadata caching service. Then someone left and they were given that guy's medium-sized service. Then they had an idea for a brand new system, built it, and now own it as a senior engineer.
The effect is a senior engineer in the org will have somewhat-stale but easily-refreshable context on a handful of services. It's like riding a bike. This is useful both for bus-factor situations, and also mentoring the juniors who own those services.
So in a bus-factor situation, there are usually enough seniors around who can keep the lights on until a new owner is found. And in this kind of org, you'll always have a cohort of bright up-and-coming juniors who passed the sink-or-swim test and are ready to take ownership of a bigger service.
How to manage such an org?
That is, what is the place for managers in this brave world?
Such a system only needs a few managers, because it won't have
that
many engineers. It won't have that many engineers because there simply don't exist very many systems that
need
that many services.
For context,
AWS S3
was built and operated by fewer than 20 engineers in the early years. And if you were to design a storage service on a whiteboard, you might find yourself with 20 or so boxes. There's the storage node, the webserver, the caching layer, the index, the corruption scanner, etc etc etc. It all adds up. Almost no system needs more than a few dozen boxes on the whiteboard.
In such a world, you only need a handful of managers, and you definitely don't need many layers of management. You want the person in charge of the whole org, a small handful of managers, and then all the engineers.
The person in charge of the whole org should rely on senior technical
lieutenants
as much as (and perhaps more than) management to maintain visibility.
