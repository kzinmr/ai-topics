---
title: "For systems, research is development and development is research"
url: "https://databasearchitects.blogspot.com/2023/01/for-systems-research-is-development-and.html"
fetched_at: 2026-05-05T07:01:27.963254+00:00
source: "Database Architects"
tags: [blog, raw]
---

# For systems, research is development and development is research

Source: https://databasearchitects.blogspot.com/2023/01/for-systems-research-is-development-and.html

The
Conference on Innovative Data Systems Research (CIDR) 2023
is over, 
and as usual both the official program and the informal discussions have
 been great. CIDR encourages innovative, risky, and controversial ideas 
as well as honest exchanges. One intensely-discussed talk was the
keynote by Hannes Mühleisen
, who together with Mark Raasveldt is the 
brain behind DuckDB.
In the keynote, Hannes lamented the incentives of systems 
researchers in academia (e.g., papers over running code). He also 
criticized the often obscure topics database systems researchers work on
 while neglecting many practical and pressing problems (e.g., top-k 
algorithms rather than practically-important issues like strings).
Michael Stonebraker has similar
thoughts
on the database systems 
community.
 I share many of these criticisms, but I'm more optimistic regarding 
what systems research in academia can do, and would therefore like to 
share my perspective.
Software is different: copying it is free, which has two 
implications: (1) Most systems are somewhat unique -- otherwise one 
could have used an existing one. (2) The cost of software is dominated 
by development effort. I argue that, together, these two observations 
mean that systems research and system development are two sides of the 
same coin.
Because developing complex systems is difficult, reinventing the 
wheel is not a good idea -- it's much better to stand on the proverbial 
shoulders of giants. Thus, developers should look at the existing 
literature to find out what others have done, and should experimentally 
compare existing approaches. Often there are no good solutions for some 
problems, requiring new inventions, which need to be written up to 
communicate them to others. Writing will not just allow communication, 
it will also improve conceptual clarity and understanding, leading to 
better software. Of course, all these activities (literature review, 
experiments, invention, writing) are indistinguishable from systems 
research.
On the other hand, doing systems research without integrating the 
new techniques into real systems can also lead to problems. Without 
being grounded by real systems, researchers risk wasting their time on 
intellectually-difficult, but practically-pointless problems. (And 
indeed much of what is published at the major database conferences falls
 into this trap.) Building real systems leads to a treasure trove of 
open problems. Publishing solutions to these often directly results in 
technological progress, better systems, and adoption by other systems.
To summarize: systems research is (or should be) indistinguishable 
from systems development. In principle, this methodology could work in 
both industry and academia. Both places have problematic incentives, but
 different ones. Industry often has a very short time horizon, which can
 lead to very incremental developments. Academic paper-counting 
incentives can lead to lots of papers without any impact on real 
systems.
Building systems in academia may not be the best strategy to publish
 the maximum number of papers or citations, but can lead to real-world impact, 
technological progress, and (in the long run even) academic accolades. 
The key is therefore to work with people who have shown how to overcome 
these systemic pathologies, and build systems over a long time horizon. There are many examples such academic projects (e.g., PostgreSQL, C-Store/Vertica, H-Store/VoltDB, ShoreMT, Proteus, Quickstep, Peloton, 
KÙZU, AsterixDB, MonetDB, Vectorwise, DuckDB, Hyper, LeanStore, and Umbra).
