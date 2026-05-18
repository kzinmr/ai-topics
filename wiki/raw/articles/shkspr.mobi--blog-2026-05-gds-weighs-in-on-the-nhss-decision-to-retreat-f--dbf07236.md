---
title: "GDS weighs in on the NHS’s decision to retreat from Open Source"
url: "https://shkspr.mobi/blog/2026/05/gds-weighs-in-on-the-nhss-decision-to-retreat-from-open-source/"
fetched_at: 2026-05-18T07:01:09.922874+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# GDS weighs in on the NHS’s decision to retreat from Open Source

Source: https://shkspr.mobi/blog/2026/05/gds-weighs-in-on-the-nhss-decision-to-retreat-from-open-source/

Within the UK's Civil Service you occasionally hear the expression "being invited to a meeting
without
biscuits". It implies a
rather
frosty discussion without any of the polite niceties of a normal meeting
. In general though, even when people have severe disagreements, it is rare for tempers to fray. It is even rarer for those internal disagreements to spill over into public.
Which is what makes GDS's latest guidance so surprising. At the start of the month, NHS England made the bizarre and irresponsible decision
to close all their Open Source repositories
due to unfounded fears of AI hacking
. Lots of people within the NHS were outraged. As were many outside - with
this petition
against the move gathering over 2,000 signatures.
Within other parts of government there was also alarm. Although I no longer work for Government Digital Service, I was contacted by several concerned people there who remembered all my work on Open Source. The brilliant team in Whitechapel have now published their guidance "
AI, open code and vulnerability risk in the public sector
".
It is
brutal
.
They utterly repudiate the NHS's stance and forensically eviscerate it. I'll let you read the whole thing, but here are a few choice excerpts:
Recent public reporting about organisations restricting access to public repositories due to AI-enabled code analysis illustrates how quickly leaders may reach for blanket closure in response to uncertainty.
Basically, non-technical managers need to stop over-reacting.
Private repositories can create a false sense of security.
I think that's the crux of the argument. Closing code doesn't solve the underlying problems.
Making code private is not an appropriate mitigation for lack of ownership, patching capability, or operational assurance, so systems that cannot be safely maintained should be remediated or retired.
If you are so concerned about the poor security of your systems, you should shut them down completely to mitigate the threat.
Closure can become a one-way door.
As I said to the BMJ, "
nothing lasts longer than a temporary fix
".
Where code has been developed in the open, making a repository private later may not remove access for a capable adversary as popular repositories are often mirrored or forked
Indeed. A friend of mine has already archived all of the NHS's repositories. You can
see the ones they've tried to hide
.
But the killer blow, I think, is this:
Moving code from public to private as a substitute for investment in secure-by-design delivery, ownership and remediation is a warning sign because it reduces sharing and scrutiny, can slow coordinated improvement across government and suppliers, and does not remove the underlying weaknesses in a running service.
Exactly! Coding in the open has been shown time and again to produce high quality and secure work. The looming threat of AI vulnerability scanners doesn't change that - security is a shared responsibility. Technical teams need to be well enough resourced to create secure systems; hiding code is as reliable as papering over structural cracks.
GDS was created was to be a
strong
centre with vast technology expertise. This was to counter the frankly shoddy approach to tech in other departments. Back then, a
Service Assessment
was a way for a department to prove that they were actually capable of designing, launching, and managing a complex IT project.
Most departments have become significantly better at the development and running of these sorts of projects, so the
raison d'etre
of GDS has somewhat waned. Departments feel more confident in running off on their own. Usually I'd celebrate that - it's important that GDS doesn't become a bottleneck and that the talent is distributed throughout the whole Civil Service.
But NHS England has always been a bit of a weird one. One of the reasons NHSX was created
was to ensure that the health service had strong expertise in technology and its deployment. As the Head of Open Technology there, I helped craft the policies which embedded Open Source and Open Standards within it
.
I don't know what discussions have taken place within NHS England - although
I looking forward to receiving a response to my FOI request
. It looks to me like a small group within NHS England have received a report showing some potential vulnerabilities discovered by Mythos. Rather than following their own internal guidance, they've over-reacted and slapped a blanket ban on coding in the open.
I fervently hope that this new guidance will encourage DHSC to bring NHS England into line with best practice. If not, perhaps GDS ought to reassert itself as the technical authority with power to veto a department's incomprehensible decisions?
