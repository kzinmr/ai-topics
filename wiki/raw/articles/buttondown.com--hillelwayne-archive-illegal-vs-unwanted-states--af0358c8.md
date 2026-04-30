---
title: "Illegal vs Unwanted States"
url: "https://buttondown.com/hillelwayne/archive/illegal-vs-unwanted-states/"
fetched_at: 2026-04-30T07:00:48.834484+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# Illegal vs Unwanted States

Source: https://buttondown.com/hillelwayne/archive/illegal-vs-unwanted-states/

An
illegal state
is a state we never want our system to be in. An
unwanted state
is a state we don't want to stay in. Many states that we wish were illegal are actually unwanted.
Considering a calendaring software which stores calendar events as
{user: {events: [event]}}
, where each event has a start and end time. This allows one person to attend two events at the same time. We might consider this illegal and replace the data type with
{user: {time: optional event}}
which makes this impossible. However, a scheduling conflict isn't illegal, only unwanted! It is possible for a person to sign up for two overlapping events. Maybe they're supposed to choose one event, maybe they'll decide which event to go to later, maybe one of the events doesn't actually represent an in-person meeting.
In that case it's acceptable, if not ideal, to remain in the unwanted state. Other unwanted states lead to invalid states if not exited quickly. An airline flight is in an unwanted state if there are more passengers booked to fly than seats available. This must be resolved before passengers actually board, as "more passengers physically on the plane than seats available" is an illegal state.
In some cases, an unwanted state does not lead to illegal states, but permanently remaining in the unwanted state is still a problem. We might guarantee that a network partition does not ever lead to inconsistent data. Even though the unwanted state of a network partition cannot cause the illegal state of corrupt data, we still have a big problem if we don't ever fix the partition.
Why systems must represent unwanted states
Generally, unwanted states can happen if we don't have complete control over our system's behavior. We can't guarantee our network is perfectly reliable, our servers are always up, our users all put in correct data. If our system gets input from the external world then the world can push us into an unwanted state. We need to be able to detect these states so we can resolve them.
Even when we have complete control over the system, we still may want to be able to temporarily dip into unwanted states. If they wanted, airlines could make overbooking flights impossible. But airlines want to be able to overbook because they expect some number of no-shows. We need to allow them their unwanted state and then put systems in place to prevent it evolving into an illegal state.
Sometimes we need unwanted states to make certain workflows possible. It may be the case that 95% never, ever want to accepted conflicting events, and preventing that unwanted state would make their lives better. But without that unwanted state, intentionally double booking yourself is impossible. Some people might need that! In these cases we want to make it very clear to users that they're entering an unwanted state, and then let them decide for themselves how to leave it.
(The airlines and users want the unwanted state! It's us engineers who consider it "unwanted" because it can lead to problems down the road.)
Formal models of unwanted states
Illegal states correspond to violated invariants. Conventionally speaking we write this as
[]!Illegal
: it should be true at all times that
Illegal
is not true. If a single state ever satisfies
Illegal
then our system has a bug.
Unwanted states are trickier, since they can be both
safety and liveness properties
. If modeling an airline system, we don't necessarily want to check properties of overbooking, we only need to check that no overflights happen.
We may discover in the process of verifying that that overbooking is the main cause of overflights and/or that if overbooking is not resolved, then we will eventually have an overflight. Further, if "we never overbook" guarantees "we never overflight", we'd say that "no overbooks" is a
stronger
property than "no overflights".
"We never remain in a network partition" is
formalized
as
[]<>!Partition
: we can enter a partition and stay partitioned a long time but must eventually heal the partition. The
P specification language
calls these
hot states
.
(PS: if all goes well, there should be a new
Logic for Programmers
release next week!)
