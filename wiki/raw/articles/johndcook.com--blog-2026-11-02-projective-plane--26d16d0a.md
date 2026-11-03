---
title: "Making peace with the projective plane"
url: "https://www.johndcook.com/blog/2026/11/02/projective-plane/"
fetched_at: 2026-11-03T10:01:42.992806+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Making peace with the projective plane

Source: https://www.johndcook.com/blog/2026/11/02/projective-plane/

In my newsletter I give an introduction to the latest few posts and occasionally give some additional commentary. In my latest newsletter I wrote
Projective space and homogeneous coordinates seemed like arbitrary abstractions when I was a student because they were presented without any motivation. Much later I came to realize that they’re natural, almost inevitable. Exceptional cases and hand-wavy references to objects “at infinity” go away when moving to projective space.
My mathematics education was very top-down: abstractions first, specifics later (if ever). I was OK with that for a while, until I hit my abstraction tolerance sometime in grad school. Now I would advocate more of a bottom-up approach, motivating abstractions first rather than presenting them as a
fait accompli
.
The first time I saw the projective plane was probably in a topology class where someone said you could construct the plane by starting with a square and gluing opposite edges in a physically impossible way. This seemed like a gimmick, a way to construct a non-orientable manifold but not anything practical. Another construction is to say the projective plane is an ordinary sphere with antipodal points identified. I found that a little more satisfying, but it still unmotivated.
What I would have appreciated was someone saying that the projective plane was invented to make geometry more elegant by eliminating exceptional cases and making rigorous the idea of things “at infinity.” For example, geometric calculations often have to treat vertical lines specially, but vertical lines are not special in projective geometry.
You could start by saying we’re going to represent points in the plane not simply as (
x
,
y
) but as (
x
,
y
, 1) and use (
x
,
y
, 0) for the point at infinity in the direction (
x
,
y
). That may seem like a hack, but it’s certainly motivated. It’s exactly the sort of thing a graphics programmer would do. In fact, I imagine many programmers have done just that, independently bumping into projective geometry.
After having introduced this extra coordinate, it’s natural to ask what would it mean if the last coordinate were something other than 0 or 1. You’ll quickly run into this when you start doing calculations on these extended coordinates. You could have a rule that you always normalize by dividing by the last coordinate, if it’s not zero, and then you have essentially discovered homogeneous coordinates.
You’ll see something like the approach above in elliptic curve cryptography. Programmers wanting to implement encryption algorithms are thinking concretely in terms of (
x
,
y
) points, until they have to worry about a mysterious “point at infinity” and handle it correctly. Then homogenous coordinates appear as a tool for getting out of a bind.
***
I thought about titling this post something like “Dr. Strangelove, or: How I Learned to Stop Worrying and and Love the Projective Plane” but I wasn’t sure how well that would go over. I doubt many readers have seen the 1964 movie this is alluding to, but the trope “How I Learned to Stop Worrying and Love …” is more widely known than the movie itself.
