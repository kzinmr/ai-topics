# Verification record: identity of "Adam Rosenthal" stub → David S. H. Rosenthal (DSHR)

**Date:** 2026-09-04
**Performed by:** skeleton-enrich-daily cron
**Subject:** [[entities/adam-rosenthal]] (`status: needs-identification`, created 2026-04-26 via newsletter ingest)

## Question

Which real person does the "Adam Rosenthal" stub refer to?

## Evidence chain

1. **Only wiki-internal mention of any "Rosenthal" in an AI context** is **David Rosenthal (DSHR)**, author of the
   raw article [[raw/articles/2026-06-24_dshr_ai-affordability-crisis]] ("AI's Affordability Crisis",
   blog.dshr.org, published 2026-06-23, archived 2026-06-24). That article is cited by
   [[concepts/ai-affordability-crisis]], which names "David Rosenthal (DSHR, digital preservation blogger)"
   as one of the concept's popularizers alongside Ed Zitron and David Cahn.
2. The stub's original research notes (2026-05-03) found NO notable "Adam Rosenthal" in the AI/LLM ecosystem:
   no GitHub, no blog/Substack, no OSS contributions; multiple unrelated LinkedIn profiles.
3. No other Rosenthal appears anywhere in wiki raw articles, newsletters, transcripts, or X bookmarks.
4. Therefore the stub is almost certainly a **mis-prefixed rendering of "David Rosenthal" (DSHR)** — the only
   Rosenthal the pipeline ever ingested. ("Adam" has no traceable source; the pipeline likely dropped
   "D-**avid** → **Adam**" or hallucinated a first name.)

## Verification of David S. H. Rosenthal's biography (2026-09-04)

Sources fetched live (curl/httpx; Jina Reader timed out on dshr.org):

- **blog.dshr.org/p/blog-page.html** ("Brief Bio of David S. H. Rosenthal") — fetched 2026-09-04, HTTP 200.
  Key facts (self-reported, authoritative):
  - 1998: with Vicky Reich at Stanford Libraries, started the **LOCKSS Program** (NSF-funded, long-term
    preservation of web-published materials). 1999-2002 at Sun Labs; 2002-2017 (retirement) at Stanford Libraries.
  - Awards: **Paul Evan Peters Award** (Coalition for Networked Information, April 2025, with Vicky Reich);
    **NDSA Sustainability Excellence Award** (November 2023).
  - Built and tested the initial LOCKSS prototype; developed the OpenBSD-based network appliance technology;
    part of the research team behind the fault-/attack-resistant P2P network technology — "a decentralized
    consensus system using proof-of-work published **more than five years before** Satoshi Nakamoto's Bitcoin
    protocol, for a different application."
  - Blogging since **2007** at https://blog.dshr.org/ . Topics: economic models for long-term storage,
    emulation as preservation strategy, DNA as storage medium, decentralized Web, P2P economics.
  - Career: joined **Sun Microsystems 1985** from CMU's **Andrew project** (window systems with James Gosling);
    worked on **NeWS** and the **X Window System**, graphics hardware, kernel, sysadmin.
  - **1993: Chief Scientist and employee #4 at Nvidia** (worked on I/O architecture). 1996: Vitria Technology
    (reliable multicast protocols, industrial-strength software testing).
  - Education: Haberdashers' Aske's School, Elstree; MA **Trinity College, Cambridge**; PhD **Imperial College, London**.
    1976-1983 post-doc at EdCAAD (Edinburgh, under Aart Bijl; 1982 sabbatical at Universiteit van Amsterdam /
    Mathematisch Centrum, now CWI). **23 patents.**
- **handwiki.org/wiki/Biography:David_S._H._Rosenthal** (mirrors Wikipedia article "David S. H. Rosenthal"),
  fetched 2026-09-04, HTTP 200:
  - **David Stuart Holmes Rosenthal, born 1948, Cambridge, UK**; British-American computer scientist.
  - 1988: developed **ICCCM** (Inter-Client Communication Conventions Manual) for X; US Patent 5,073,933
    (X window security system, issued 1991).
  - Co-author of **The NeWS Book** (Gosling, Rosenthal, Arden; Springer 1989).
  - 1999 rejoined Sun as Distinguished Engineer; then chief scientist for LOCKSS (Sun, then Stanford from 2002).
  - Author of "Keeping Bits Safe: How Hard Can It Be?" (ACM Queue 8(10), Oct 2010).
- **blog.dshr.org archive counts** (from blog page sidebar, fetched 2026-09-04): 2026: 31 posts YTD (Sep: 1
  "Small Is Beautiful", Jun: 5 incl. the AI affordability post); 2025: 36; 2024: 46; 2023: 54; 2022: 73.

## Conclusion

- The AI-relevant identity behind the stub is **David S. H. Rosenthal of DSHR's Blog** — high confidence
  for "the pipeline ingested DSHR"; the stub's forename "Adam" remains unexplained and is recorded as such.
- Canonical entity page created at [[entities/david-rosenthal-dshr]]; `entities/adam-rosenthal.md` converted
  to a redirect with a full provenance note.
