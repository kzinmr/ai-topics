---
title: "Covering a body with eight smaller copies of itself"
url: "https://www.johndcook.com/blog/2026/11/25/hadwiger-covering/"
fetched_at: 2026-11-26T10:00:51.305844+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Covering a body with eight smaller copies of itself

Source: https://www.johndcook.com/blog/2026/11/25/hadwiger-covering/

It’s obvious that you could cover a cube with smaller cubes. You could, for example, take a cube with side 1 and cover it a cube of side ½ centered on each corner.
It’s not as obvious how you would cover a ball with smaller balls, but you could cover the unit ball with balls of radius ½√3 centered at the points (±½, ±½, ±½).
In fact, you could cover a ball with four smaller balls [1].
Now consider an arbitrary convex shape
K
in three dimensions with non-empty interior. Is it possible to cover
K
by copies of itself? Since
K
has non-empty interior, you could cover
K
by putting a smaller version of
K
around every point. And if
K
is compact, then this cover has a finite subcover. But there might be a
lot
of elements in this finite cover. What’s the minimum number possible in general? It takes eight cubes to cover a cube, so the minimum is at least 8. But could some odd shape take more?
Hadwiger’s covering conjecture says that
K
can be covered by eight copies of itself. That is, there exists a scaling constant 0 < λ < 1 and shift vectors
v
i
such that
Dror Aiger, Sariel Har-Peled, and Goran Žužić posted a proof of Hadwiger’s conjecture on
arXiv
yesterday. The abstract to their paper says “The proof was discovered using an experimental harness on top of Gemini 4 Carbon and formally verified in Lean 4.”
I’ve heard good things about the Google’s new Carbon model. This is the first announcement of a major theorem proved with the assistance of a Google model that I’ve noticed.
Related posts
[1] Inscribe the vertices of regular tetrahedron on the unit sphere, then multiply the vectors representing the vertices by ⅓. Center spheres of radius ⅔√2 at each vertex.
