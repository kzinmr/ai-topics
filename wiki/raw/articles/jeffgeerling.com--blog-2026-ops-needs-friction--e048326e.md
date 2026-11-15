---
title: "Ops needs friction"
url: "https://www.jeffgeerling.com/blog/2026/ops-needs-friction/"
fetched_at: 2026-11-15T10:00:55.744078+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Ops needs friction

Source: https://www.jeffgeerling.com/blog/2026/ops-needs-friction/

Between
Microsoft's two-day outage
and the
FAA ground stop yesterday
, there's plenty of ink spilled about who's responsible, why these things happened, etc.
But it made me think back to some of the infrastructure and ops teams I've worked on, and similar (though much smaller scale) outages we encountered.
Having an ops mindset is fundamentally different from a development or project management mindset. And it took me over a decade of software development to understand why.
Ops is about staying collected when systems fail. Usually debugging code written by other people, in conditions they were never prepared for.
There's a lot of creativity and exploration in debugging critical failures, and IMO sysadmins are usually an undervalued part of any team.
I always found it helpful to have a curmudgeonly person on the team who got annoyed when some of my code generated an extra 10,000 log lines a day, or caused a small but measurable slowdown in a database backend.
I became that curmudgeon, in fact: I distinctly remember pushing back on a dev team enabling debug-level logs permanently in production. We were filling up packet buffers with mostly useless data, to help them 'debug in prod' with live data.
My argument was that if this were a well-defined short-term plan, with specific goals, it could be useful. But they were pushing a lot of new features and didn't want to go through their normal QA cycle in the staging environment.
Ultimately, we compromised on the logging: I added functionality to the cluster that lowered log verbosity in new containers when they scaled in response to traffic spikes. That led to more useful infrastructure for development, without giving up (
too
much) resilience.
Calling things out early is sometimes a nuisance, but sometimes prevents a small problem from manifesting as a much larger disaster when some other part of the system breaks down.
These are the types of people who see the risk in merging an old and new system and have the persistence—despite others on the team pushing back—to effect change, or buy more time for upgrades and maintenance.
We need that friction in our system, because without it, the wheels fly off instead of making a wear pattern that can be measured and mitigated.
