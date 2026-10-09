---
title: "Privacy policies and modal logic"
url: "https://www.johndcook.com/blog/2026/10/08/privacy-policies-and-modal-logic/"
fetched_at: 2026-10-09T10:01:08.220712+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Privacy policies and modal logic

Source: https://www.johndcook.com/blog/2026/10/08/privacy-policies-and-modal-logic/

If you’ve followed this blog for a while, you may know that I do a lot of work with data privacy and that I have an interest in modal logic. Recently these two worlds collided: I became aware of work that uses modal logic to reason about data privacy.
The story begins with Helen Nissenbaum’s paper
Privacy as Contextual Integrity
[1]. Rather than simply classifying data as public or private, Nissenbaum looks at norms around the context in which data exists and moves.
… the benchmark of privacy is contextual integrity; that in any given situation, a complaint that privacy has been violated is sound in the event that one or the other types of the informational norms has been transgressed.
A couple years later Nissenbaum coauthored a paper [2] with three Stanford computer scientists using modal logic, specifically
linear temporal logic
(
LTL
), to reason about contextual integrity. The paper uses four modal operators: the usual box and diamond, plus past tense versions with a minus sign across the middle.
These four operators can be read as “henceforth”, “eventually”, “historically”, and “once.”
Henceforth means something will always be true into the future; historically means something was always true in the past.
Eventually means something will happen at some time in the future; once means something occurred at some time in the past.
You could imagine using these operators to formalize statements such as data sharing in some context is permissible (henceforth) if the data subject has (once) signed a consent form.
Understanding simple stand-alone policies does not require the machinery of formal logic, but analyzing large collections of interacting policies may. It may be, for example, that a collection of policies cannot all be satisfied, though this is not obvious from looking at the individual policies. Formalizing policies in the language modal logic makes their analysis amenable to well established algorithms.
Related posts
[1] H. Nissenbaum. Privacy as contextual integrity. Washington Law Review, 79(1):119–158, 2004.
[2] A. Barth, A. Datta, J. C. Mitchell, and H. Nissenbaum, “Privacy and contextual integrity: Framework and applications,” in Proc. 2006 IEEE Symp. Security and Privacy (S&P’06), Berkeley/Oakland, CA, USA, 2006, pp. 184–198, doi: 10.1109/SP.2006.32.
