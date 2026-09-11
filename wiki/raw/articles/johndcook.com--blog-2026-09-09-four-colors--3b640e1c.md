---
title: "A 50-year-old computer-assisted proof"
url: "https://www.johndcook.com/blog/2026/09/09/four-colors/"
fetched_at: 2026-09-10T10:01:26.394663+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# A 50-year-old computer-assisted proof

Source: https://www.johndcook.com/blog/2026/09/09/four-colors/

The idea of using computers to assist with proofs is not new. The first major computer-assisted proof was published in 1976, the proof of the four color theorem by Kenneth Appel and Wolfgang Haken. The authors reduced the proof of the four color theorem to verifying calculations on 1,834 configurations, each checked by a computer program.
The proof was simplified over the years, and formalized in Coq in 2005. Everyone is satisfied that the theorem is true, but there has never been a satisfying proof, one that a human could read and say “I see now why any map can be colored using only four colors.” And there may never be one, but see
this post
for a contrary prediction.
The IBM mainframe that ran the calculations completing the proof of the four color theorem did not generate the proof. It simply executed the FORTRAN program that Haken and Appel (and Koch [1]) gave it.
I don’t see the recent proof of finite-time blowup for solutions to the Navier-Stokes equations as entirely different. Computers did higher-level tasks for the OpenAI team than the mainframe did for Haken and Appel, and these tasks were not as directly programmed as the tasks that were given to the mainframe, but still machines do what they are told to do.
Related posts
[1] John A. Koch was a programmer who worked on the four color proof with Haken and Appel. I don’t know how much credit he deserves, but I suspect it may be more than he was given.
