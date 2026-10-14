---
title: Google SRE - Operational Work For Balancing SRE Project
source_url: https://sre.google/workbook/part-II-practices/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/part-II-practices.html
original_sha256: b2afdd19e94ca3ee2343238f83ee5c451e4894cd719607be491945371c4fdf46
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/part-II-practices/
ingested: '2026-10-14'
sha256: a4d568d1b989389f8029bb61116d459257dac92d64c82c415b3f9a137ceb9a55
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Part II. Practices
Building upon the solid foundation of SRE principles covered in
Foundations
, Part II dives deep into how to conduct SRE-related activities that Google has found important for operating at scale.
Some of these topics, such as data processing pipelines and managing load, won’t apply to all organizations. Other topics, such as safely handling changes with configuration and canarying, on-call practices, and what to do when things go wrong, contain valuable
lessons for any SRE team
.
This part also introduces an important SRE skill—Non-Abstract Large System Design (NALSD)—and presents a detailed example of how to practice this design process.
As we move from SRE foundations to practices, we wanted to provide a bit more context on the relationship between operational duties and project work, and the engineering it takes to accomplish both strategically.
Defining Operational Work (Versus Project Work and Overhead)
Before we move from foundations to practices, we wanted to touch on the difference between operational and project work, and how these two types of work inform each other. The topic is an area of philosophical debate in the SRE community, so this interlude presents how we define the two types of work in the context of this book.
SRE practices
apply software engineering solutions to operational problems. Because our SRE teams are responsible for the day-to-day functioning of the systems we support, our engineering work often focuses on tasks that might be operations elsewhere: we automate release processes instead of performing them manually; we implement sharding to make our services more reliable and less demanding of human attention; we utilize algorithmic approaches to capacity planning so that engineers don’t have to perform error-prone manual calculations.
While engineering and operational work do inform each other, we can conceptualize the work any given SRE team performs as two separate categories, as shown in
Figure II-1
. Over the years, we’ve worked toward ways to maximize the efficiency and scalability of each bucket of work.
Figure II-1.
The two categories of SRE work
We can break down operational work into four general categories:
On-call work
Customer requests (most commonly, tickets)
Incident response
Postmortems
Each of these categories receives its own detailed treatment in both our first book (
Being On-call
;
Managing Incidents
;
Postmortem Culture: Learning from Failure
) and this one (
Eliminating Toil
;
On-Call
;
Incident Response
;
Postmortem Culture: Learning from Failure
). Here, we show how all four are interconnected, and why it’s important to consider these types of work as closely related.
What types of work are not included in operational work? As shown in
Figure II-1
, project work is the other main bucket of SRE work. When a team’s interrupt work is well managed, they have time for longer-term engineering work to achieve stability, reliability, and availability goals. This might include software engineering projects aimed at improving the reliability of a service, or systems engineering projects like safely rolling out a new feature to a globally replicated service.
Also shown in
Figure II-1
,
overhead
is the administrivia necessary to working at a company: meetings, training, responding to emails, tracking your accomplishments, filling out paperwork, and so on. Overhead isn’t immediately important to the discussion at hand, but all team members spend time on it.
You might notice that we don’t specifically call out documentation as a separate activity. This is because we believe that healthy documentation procedures embed themselves into all of your work. You don’t need to think about documenting code, playbooks, and service features—or even making sure that tickets and bugs contain all of the information they should—as separate from your project or operational tasks. It’s simply another facet of those tasks.
At Google, we specify that SREs should spend at least 50% of their time on project work; anything less makes for unsustainable engineering and burned-out, unhealthy teams. While every team and organization needs to find its own healthy balance, we’ve found that about one-third of time spent on operational tasks and two-thirds of time spent on project work is just about right (this ratio also informs an ideal on-call rotation size, where your engineers are only on-call one-third of the time).
We encourage teams to conduct periodic reviews to track whether you’re striking the appropriate balance between types of work. At Google, we conduct regular Production Excellence (ProdEx) Reviews, which allow senior SRE leadership a view into the state of every SRE team using a clearly defined rubric. You’ll need to determine the appropriate time intervals and rubric according to your own constraints and organizational maturity, but the key here is to generate metrics about team health that you can track over time.
Remember one caveat when finding your ideal balance: a team that spends too little of its time on operational tasks risks operational underload. In this situation, engineers might start to forget crucial aspects of the service they are responsible for. You can counter operational underload by taking more risks and moving faster—for example, shorten your release cycles, push more features per release, or perform more disaster recovery testing. If your team is perpetually underloaded, consider onboarding related services or handing back a service that no longer needs SRE support to the development team (for more discussion of team size, see
On-Call
).
The Relationship Between Operational Work and Project Work
While they are different classes of work, operational and project work aren’t entirely separate concerns. In fact, the issues raised in the former should feed into the latter: SRE project work should be strategic initiatives that make the system more efficient, scalable, and reliable, and/or that reduce operational load and toil. As shown in
Figure II-1
, there should be a continuous feedback loop between the sources of operational load and the project work that systematically improves production. This longer-term work might involve moving to more robust storage systems, redesigning frameworks to reduce brittleness or maintenance load, or addressing systemic sources of outages and incidents. These initiatives are developed and implemented via
projects
, defined as temporary endeavors (with a clear beginning and end) that deliver a specified objective or deliverable.
