---
title: 'Google SRE: What it Means Being On-Call? | Devops On-Call'
source_url: https://sre.google/workbook/on-call/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/on-call.html
original_sha256: b335139e053f006e383d305ed6e65efb60f56bbe4910f40874a7769945c9467e
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/on-call/
ingested: '2026-10-14'
sha256: a325b9583733ba41b163e4e2870cb1528e97451c39dde4932e6ee7655f69fe14
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
On-Call
By Ollie Cook, Sara Smollett, Andrea Spadaccini,
Cara Donnelly, Jian Ma, and Garrett Plasky (Evernote)
with Stephen Thorne and Jessie Yang
Being on-call means being available during a set period of time, and being ready to respond to production incidents during that time with appropriate urgency.
Site Reliability Engineers
(SREs) are often required to take part in on-call rotations. During on-call shifts, SREs diagnose, mitigate, fix, or escalate incidents as needed. In addition, SREs are regularly responsible for nonurgent production duties.
At Google, being on-call is one of the defining characteristics of SRE. SRE teams mitigate incidents, repair production problems, and automate operational tasks. Since most of our SRE teams have not yet fully automated all their operational tasks, escalations need human points of contact—on-call engineers. Depending on how critical the supported systems are, or the state of development the systems are in, not all SRE teams may need to be on-call. In our experience, most SRE teams staff on-call shifts.
On-call is a large and complex topic, saddled with many constraints and a limited margin for trial and error.
Chapter 11
of our first book (
Site Reliability Engineering
), “Being On-Call,” already explored this topic. This chapter addresses specific feedback and questions we received about that chapter. These include the following:
“We are not Google; we’re much smaller. We don’t have as many people in the rotation, and we don’t have sites in different time zones. What you described in your first book is irrelevant to me.”
“We have a mixture of developers and DevOps for on-call rotation. What’s the best way to organize them? Split the responsibilities?”
“Our on-call engineer gets paged about a hundred times in a typical 24-hour shift. A lot of pages get ignored, while the real problems are buried under the pile. Where should we start?”
“We have a high turnover rate for on-call rotations. How do you address the knowledge gap within the team?”
“We want to reorg our DevOps team into SRE.
1
What’s the difference between SRE on-call, DevOps on-call, and developers on-call? Please be specific, because the DevOps team is very concerned about this.”
We offer practical advice for these situations. Google is a large company with a mature SRE organization, but much of what we’ve learned over the years can be applied to any company or organization, regardless of size or maturity. Google has hundreds of on-call rotations across services of all sizes, and various on-call setups from simple to complicated. On-call is not exclusively an SRE function: many developer teams are directly on-call for their service. Each on-call setup meets the need of a particular service.
This chapter describes on-call setups both within Google and outside of Google. While your setup and situation will likely differ from our specific examples, the essential concepts we cover are widely applicable.
We then delve into the anatomy of pager load, explaining what causes pager load. We suggest strategies to optimize on-call setup and minimize that load.
Finally, we share two examples of practices inside Google: on-call flexibility and on-call team dynamics. These practices show that no matter how mathematically sound an on-call setup is, you cannot solely rely on logistics of the on-call setup. Incentives and human nature play an important role, and should also be taken into account.
Recap of “Being On-Call” Chapter of First SRE Book
Site Reliability Engineering
, in
“Being On-Call”
, explains the principles behind on-call rotations at Google. This section discusses the main points of that chapter.
At Google, the overall goal of being on-call is to provide coverage for critical services, while making sure that we never achieve reliability at the expense of an on-call engineer’s health. As a result, SRE teams strive for
balance
. SRE work should be a healthy mix of duties: on-call and project work. Specifying that SREs spend at least 50% of their time on project work means that teams have time to tackle the projects required to strategically address any problems found in production. Team staffing must be adequate to ensure time for project work.
We target a maximum of two incidents per on-call shift,
2
to ensure adequate time for follow-up. If the pager load gets too high, corrective action is warranted. (We explore pager load later in this chapter.)
Psychological safety
3
is vital for effective on-call rotations. Since being on-call can be daunting and highly stressful, on-call engineers should be fully supported by a series of procedures and escalation paths to make their lives easier.
On-call usually implies some amount of out-of-hours work. We believe this work should be compensated. While different companies may choose to handle this in different ways, Google offers time-off-in-lieu or cash compensation, capped at some proportion of the overall salary. The compensation scheme provides an incentive for being part of on-call, and ensures that engineers do not take on too many on-call shifts for economic reasons.
Example On-Call Setups Within Google and Outside Google
This section describes real-world examples of on-call setups at Google and Evernote, a California company that develops a cross-platform app that helps individuals and teams create, assemble, and share information. For each company, we explore the reasoning behind on-call setups, general on-call philosophy, and on-call practices.
Google: Forming a New Team
Initial scenario
A few years ago, Sara, an SRE at Google Mountain View, started a new SRE team that needed to be on-call within three months. To put this in perspective, most SRE teams at Google do not expect new hires to be ready for on-call before three to nine months. The new Mountain View SRE team would support three Google Apps services that were previously supported by an SRE team in Kirkland, Washington (a two-hour flight from Mountain View). The Kirkland team had a sister SRE team in London, which would continue to support these services alongside the new Mountain View SRE team, and distributed product development teams.
4
The new Mountain View SRE team came together quickly, assembling seven people:
Sara, an SRE tech lead
Mike, an experienced SRE from another SRE team
A transfer from a product development team who was new to SRE
Four new hires (“Nooglers”)
Even when a team is mature, going on-call for new services is always challenging, and the new Mountain View SRE team was a relatively junior team. Nonetheless, the new team was able to onboard the services without sacrificing service quality or project velocity. They made immediate improvements to the services, including lowering machine costs by 40%, and fully automating release rollouts with canarying and other safety checks. The new team also continued to deliver reliable services, targeting 99.98% availability, or roughly 26 minutes of downtime per quarter.
How did the new SRE team bootstrap themselves to accomplish so much? Through starter projects, mentoring, and training.
Training roadmap
Although the new SRE team didn’t know much about their services, Sara and Mike were familiar with Google’s production environment and SRE. As the four Nooglers completed company orientation, Sara and Mike compiled a checklist of two dozen focus areas for people to practice before going on-call, such as:
Administering production jobs
Understanding debugging info
“Draining” traffic away from a cluster
Rolling back a bad software push
Blocking or rate-limiting unwanted traffic
Bringing up additional serving capacity
Using the monitoring systems (for alerting and dashboards)
Describing the architecture, various components, and dependencies of the services
The Nooglers found some of this information on their own by researching existing documentation and
codelabs
(guided, hands-on coding tutorials) and gained understanding on relevant topics by working on their starter projects. When a team member learned about specific topics relevant to the Nooglers’ starter projects, that person led a short, impromptu session to share that information with the rest of the team. Sara and Mike covered the remaining topics. The team also held lab sessions to perform common debugging and mitigation tasks to help everyone build muscle memory and gain confidence in their abilities.
In addition to the checklist, the new SRE team ran a series of “deep dives” to dig into their services. The team browsed monitoring consoles, identified running jobs, and tried debugging recent pages. Sara and Mike explained that an engineer
didn’t
need years of expertise with each of the services to become reasonably proficient. They coached the team to explore a service from first principles, and encouraged Nooglers to become familiar with the services. They were open about the limits of their knowledge, and taught others when to ask for help.
Throughout the ramp-up, the new SRE team wasn’t alone. Sara and Mike traveled to meet the other SRE teams and product developers and learn from them. The new SRE team met with the Kirkland and London teams by holding video conferences, exchanging email, and chatting over IRC. In addition, the team attended weekly production meetings, read daily on-call handoffs and postmortems, and browsed existing service documentation. A Kirkland SRE visited to give talks and answer questions. A London SRE put together a thorough set of disaster scenarios and ran them during Google’s disaster recovery training week (see the section
“Preparedness and Disaster Testing”
in
Site Reliability Engineering
, Chapter 33).
The team also practiced being on-call through “Wheel of Misfortune” training exercises (see the section
“Disaster Role Playing”
in
Site Reliability Engineering
, Chapter 28), where they role-played recent incidents to practice debugging production problems. During these sessions, all SREs were encouraged to offer suggestions on how to resolve mock production failures. After everyone ramped up, the team still held these sessions, rotating through each team member as the session leader. The team recorded these for future reference.
Before going on-call, the team reviewed precise guidelines about the responsibilities of on-call engineers. For example:
At the start of each shift, the on-call engineer reads the handoff from the previous shift.
The on-call engineer minimizes user impact first, then makes sure the issues are fully addressed.
At the end of the shift, the on-call engineer sends a handoff email to the next engineer on-call.
The guidelines also specified when to escalate to others, and how to write postmortems for large incidents.
Finally, the team read and updated on-call
playbooks
. Playbooks contain high-level instructions on how to respond to automated alerts. They explain the severity and impact of the alert, and include debugging suggestions and possible actions to take to mitigate impact and fully resolve the alert. In SRE, whenever an alert is created, a corresponding playbook entry is usually created.  These guides reduce stress, the mean time to repair (MTTR), and the risk of human error.
Maintaining Playbooks
Details in playbooks go out of date at the same rate as production environment changes. For daily releases, playbooks might need an update on any given day. Writing good documentation, like any form of communication, is hard. So how do you maintain playbooks?
Some SREs at Google advocate keeping playbook entries general so they change slowly. For example, they may have just one entry for all “RPC Errors High” alerts, for a trained on-call engineer to read, in conjunction with an architecture diagram for the currently alerting service. Other SREs advocate for step-by-step playbooks to reduce human variability and drive down MTTR. If your team has conflicting views about playbook content, the playbooks might get pulled in many directions.
This is a contentious topic. If you agree on nothing else, at least decide with your team what minimal, structured details your playbooks must have, and try to notice when your playbooks have accumulated a lot of information beyond these structured details. Pencil in a project to turn new, hard-won, production knowledge into automation or monitoring consoles. If your playbooks are a deterministic list of commands that the on-call engineer runs every time a particular alert fires, we recommend implementing automation.
After two months, Sara, Mike, and the SRE transfer shadowed the on-call shifts of the outgoing Kirkland SRE team. At three months, they became the primary on-call, with the Kirkland SREs as backup. That way, they could easily escalate to the Kirkland SREs if needed. Next, the Nooglers shadowed the more experienced, local SREs and joined the rotation.
Good documentation and the various strategies discussed earlier all helped the team form a solid foundation and ramp up quickly. Although on-call can be stressful, the teams’ confidence grew enough to take action without second-guessing themselves. There was psychological safety in knowing that their responses were based on the team’s collective knowledge, and that even when they escalated, the on-call engineers were still regarded as competent engineers.
Afterword
While the Mountain View SREs were ramping up, they learned that their experienced, sister SRE team in London would be moving on to a new project, and a new team was being formed in Zürich to support the services previously supported by the London SRE team. For this second transition, the same basic approach the Mountain View SREs used proved successful. The previous investment by Mountain View SREs in developing onboarding and training materials helped the new Zürich SRE team ramp up.
While the approach used by the Mountain View SREs made sense when a cohort of SREs were becoming a team, they needed a more lightweight approach when only one person joined the team at a given time. In anticipation of future turnover, the SREs created service architecture diagrams and formalized the basic training checklist into a series of exercises that could be completed semi-independently with minimal involvement from a mentor. These exercises included describing the storage layer, performing capacity increases, and reviewing how HTTP requests are routed.
Evernote: Finding Our Feet in the Cloud
Moving our on-prem infrastructure to the cloud
We didn’t set out to reengineer our on-call process, but as with many things in life, necessity is the mother of invention. Prior to December 2016, Evernote ran only on on-prem datacenters, built to support our monolithic application. Our network and servers were designed with a specific architecture and data flow in mind. This, combined with a host of other constraints, meant we lacked the flexibility needed to support a horizontal architecture.  Google Cloud Platform (GCP) provided a concrete solution to our problem. However, we still had one major hurdle to surmount: migrating all our production and supporting infrastructure to GCP. Fast-forward 70 days. Through a Herculean effort and many remarkable feats (for example, moving thousands of servers and 3.5 PB of data), we were happily settled in our new home. At this point, though, our job still wasn’t done: how were we going to monitor, alert, and—most importantly—respond to issues in our new environment?
Adjusting our on-call policies and processes
The move to the cloud unleashed the potential for our infrastructure to grow rapidly, but our on-call policies and processes were not yet set up to handle such growth. Once the migration wrapped up, we set out to remedy the problem. In our previous physical datacenter, we built redundancy into nearly every component. This meant that while component failure was common given our size, generally no individual component was capable of negatively impacting users. The infrastructure was very stable because we controlled it—any small bump would inevitably be due to a failure somewhere in the system. Our alerting policies were structured with that in mind: a few dropped packets, resulting in a JDBC (Java Database Connectivity) connection exception, invariably meant that a VM (virtual machine) host was on the verge of failing, or that the control plane on one of our switches was on the fritz. Even before our first day in the cloud, we realized that this type of alert/response system was not tenable going forward. In a world of live migrations and network latency, we needed to take a much more holistic approach to monitoring.
Reframing paging events in terms of first principles, and writing these principles down as our explicit SLOs (service level objectives), helped give the team clarity regarding what was important to alert on and allowed us to trim the fat from our monitoring infrastructure. Our focus on higher-level indicators such as API responsiveness, rather than lower-level infrastructure such as InnoDB row lock waits in MySQL, meant we could focus more time on the real pain our users experience during an outage. For our team, this meant less time spent chasing transient problems. This translated into more sleep, effectiveness, and ultimately, job satisfaction.
Restructuring our monitoring and metrics
Our primary on-call rotation is staffed by a small but scrappy team of engineers who are responsible for our production infrastructure and a handful of other business systems (for example, staging and build pipeline infrastructure). We have a weekly, 24/7 schedule with a well-oiled handoff procedure, alongside a morning review of incidents at a daily stand-up. Our small team size and comparatively large scope of responsibility necessitates that we make every effort to keep the process burden light, and focus on closing the alert/triage/remediation/analysis loop as quickly as possible. One of the ways we achieve this is to keep our signal-to-noise ratio low by maintaining simple but effective alerting SLAs (service level agreements). We classify any event generated by our metrics or monitoring infrastructure into three categories:
P1: Deal with immediately
Should be immediately actionable
Pages the on-call
Leads to event triage
Is SLO-impacting
P2: Deal with the next business day
Generally is not customer-facing, or is very limited in scope
Sends an email to team and notifies event stream channel
P3: Event is informational only
Information is gathered in dashboards, passive email, and the like
Includes capacity planning–related information
Any P1 or P2 event has an incident ticket attached to it. The ticket is used for obvious tasks like event triage and tracking remediation actions, as well as for SLO impact, number of occurrences, and postmortem doc links, where applicable.
When an event pages (category P1), the on-call is tasked with assessing the impact to users. Incidents are triaged into severities from 1 to 3. For severity 1 (Sev 1) incidents, we maintain a finite set of criteria to make the escalation decision as straightforward as possible for the responder. Once the event is escalated, we assemble an incident team and begin our incident management process. The incident manager is paged, a scribe and communications lead is elected, and our communication channels open. After the incident is resolved, we conduct an automatic postmortem and share the results far and wide within the company. For events rating Sev 2 or Sev 3, the on-call responder handles the incident lifecycle, including an abbreviated postmortem for incident review.
One of the benefits of keeping our process lightweight is that we can explicitly free the on-call from any expectations of project work. This empowers and encourages the on-call to take immediate follow-up action, and also to identify any major gaps in tooling or process after completing the post-incident review. In this way, we achieve a constant cycle of improvement and flexibility during every on-call shift, keeping pace with the rapid rate of change in our environment. The goal is to make every on-call shift better than the last.
Tracking our performance over time
With the introduction of SLOs, we wanted to track performance over time, and share that information with stakeholders within the company. We implemented a monthly service review meeting, open to anyone who’s interested, to review and discuss the previous month of the service. We have also used this forum to review our on-call burden as a barometer of team health, and discuss remediation actions when we exceed our pager budget. This forum has the dual purpose of spreading the importance of SLOs within the company and keeping the technical organization accountable for maintaining the health and wellness of our service and team.
Engaging with CRE
Expressing our objectives in terms of SLOs provides a basis for engaging with Google’s Customer Reliability Engineering (CRE) team. After we discussed our SLOs with CRE to see if they were realistic and measurable, both teams decided CRE would be paged alongside our own engineers for SLO-impacting events. It can be difficult to pinpoint root causes that are hidden behind layers of cloud abstraction, so having a Googler at our side take the guesswork out of black-box event triaging was helpful. More importantly, this exercise further reduced our MTTR, which is ultimately what our users care about.
Sustaining a self-perpetuating cycle
Rather than spending all our time in the triage/root-cause analysis/postmortem cycle, we now have more time as a team to think about how we move the business forward. Specifically, this translates into projects such as improving our microservices platform and establishing production readiness criteria for our product development teams. The latter includes many of the principles we followed in restructuring our on-call, which is particularly helpful for teams in their first “carry the pager” rodeo. Thus, we perpetuate the cycle of improving on-call for everyone.
Practical Implementation Details
So far, we’ve discussed details about on-call setups, both within Google and outside of Google. But what about specific considerations of being on-call? The following sections discuss these implementation details in more depth:
Pager load—what it is, how it works, and how to manage it
How to factor flexibility into on-call scheduling to create a healthier work/life balance for SREs
Strategies for improving team dynamics, both within a given SRE team, and with partner teams
Anatomy of Pager Load
Your pager is noisy and it’s making your team unhappy. You’ve read through
Chapter 31
in
Site Reliability Engineering
, and run regular production meetings, both with your team and the developer teams you support. Now everyone
knows
that your on-call engineers are unhappy. What next?
Pager load
is the number of paging incidents that an on-call engineer receives over a typical shift length (such as per day or per week). An incident may involve more than one page. Here, we’ll walk through the impact of various factors on pager load, and suggest techniques for minimizing future pager load.
Appropriate Response Times
Engineers shouldn’t have to be at a computer and working on a problem within minutes of receiving a page unless there is a very good reason to do so. While a complete outage of a customer-facing, revenue-generating service typically requires an immediate response, you can deal with less severe issues (for example, failing backups) within a few hours.
We recommend checking your current paging setup to see if you actually
should
be paged for everything that currently triggers a page. You may be paging for issues that would be better served by automated repair (as it's generally better for a computer to fix a problem than requiring a human to fix it) or a ticket (if it's not actually high priority).
Table 8-1
shows some sample events and appropriate responses.
Table 8-1.
Examples of realistic response times
Incident description
Response time
SRE impact
Revenue-impacting network outage
5 minutes
SRE needs to be within arm's reach of a charged and authenticated laptop with network access at all times; cannot travel; must heavily coordinate with secondary at all times
Customer order batch processing system stuck
30 minutes
SRE can leave their home for a quick errand or short commute; secondary does not need to provide coverage during this time
Backups of a database for a pre-launch service are failing
Ticket (response during work hours)
None
Scenario: A team in overload
The (hypothetical) Connection SRE Team, responsible for frontend load balancing and terminating end-user connections, found itself in a position of high pager load. They had an established pager budget of two paging incidents per shift, but for the past year they had regularly been receiving five paging incidents per shift. Analysis revealed that fully one-third of shifts were exceeding their pager budget. Members of the team heroically responded to the daily onslaught of pages but couldn’t keep up; there simply was not enough time in the day to find the root cause and properly fix the incoming issues. Some engineers left the team to join less operationally burdened teams. High-quality incident follow-up was rare, since on-call engineers only had time to mitigate immediate problems.
The team’s horizon wasn’t entirely bleak: they had a mature monitoring infrastructure that followed SRE best practices. Alerting thresholds were set to align with their SLO, and paging alerts were symptom-based in nature, meaning they fired only when customers were impacted. When senior management were approached with all of this information, they agreed that the team was in operational overload and reviewed the project plan to bring the team back to a healthy state.
In less positive news, over time the Connection team had taken ownership of software components from more than 10 developer teams and had hard dependencies on Google’s customer-facing edge and backbone networks. The large number of intergroup relationships was complex and had quietly grown difficult to manage.
Despite the team following best practices in structuring their monitoring, many of the pages that they faced were outside their direct control. For example, a black-box probe may have failed due to congestion in the network, causing packet loss. The only action the team could take to mitigate congestion in the backbone was to escalate to the team directly responsible for that network.
On top of their operational burden, the team needed to deliver new features to the frontend systems, which would be used by all Google services. To make matters worse, their infrastructure was being migrated from a 10-year-old legacy framework and cluster management system to a better-supported replacement. The team’s services were subject to an unprecedented rate of change, and the changes themselves caused a significant portion of the on-call load.
The team clearly needed to combat this excessive pager load using a variety of techniques. The technical program manager and the people manager of the team approached senior management with a project proposal, which senior management reviewed and approved. The team turned their full attention to reducing their pager load, and learned some valuable lessons along the way.
Pager load inputs
The first step in tackling high pager load is to determine what is causing it. Pager load is influenced by three main factors: bugs
5
in production, alerting, and human processes. Each of these factors has several inputs, some of which we discuss in more detail in this section.
For production:
The number of existing bugs in production
The introduction of new bugs into production
The speed with which newly introduced bugs are identified
The speed with which bugs are mitigated and removed from production
For alerting:
The alerting thresholds that trigger a paging alert
The introduction of new paging alerts
The alignment of a service’s SLO with the SLOs of the services upon which it depends
For human processes:
The rigor of fixes and follow-up on bugs
The quality of data collected about paging alerts
The attention paid to pager load trends
Human-actuated changes to production
Preexisting bugs
No system is perfect. There will always be bugs in production: in your own code, the software and libraries that you build upon, or the interfaces between them. The bugs may not be causing paging alerts right now, but they are definitely present. You can use a few techniques to identify or prevent bugs that haven’t yet caused paging alerts:
Ensure systems are as complicated as they need to be, and no more (see
Simplicity
).
Regularly update the software or libraries that your system is built upon to take advantage of bug fixes (however, see the next section about new bugs).
Perform regular destructive testing or fuzzing (for example, using Netflix’s
Chaos Monkey
).
Perform regular load testing in addition to integration and unit testing.
New bugs
Ideally, the SRE team and its partner developer teams should detect new bugs before they even make it into production. In reality, automated testing misses many bugs, which are then launched to production.
Software testing is a large topic well covered elsewhere (e.g.,
Martin Fowler on Testing
). However, software testing techniques are particularly useful in reducing the number of bugs that reach production, and the amount of time they remain in production:
Improve testing over time. In particular, for each bug you discover in production, ask “How could we have detected this bug preproduction?” Make sure the necessary engineering follow-up occurs (see
Rigor of follow-up
).
Don’t ignore load testing, which is often treated as lower priority than functional testing. Many bugs manifest only under particular load conditions or with a particular mix of requests.
Run staging (testing with production-like but synthetic traffic) in a production-like environment. We briefly discuss generating synthetic traffic in
Alerting on SLOs
of this book.
Perform canarying (
Canarying Releases
) in a production environment.
Have a low tolerance to new bugs. Follow a “detect, roll back, fix, and roll forward” strategy rather than a “detect, continue to roll forward despite identifying the bug, fix, and roll forward again” strategy. (See
Mitigation delay
for more details.)
This kind of rollback strategy requires predictable and frequent releases so that the cost of rolling back any one release is small. We discuss this and related topics in
Site Reliability Engineering
, in
“Release Engineering”
.
Some bugs may manifest only as the result of changing client behavior. For example:
Bugs that manifest only under specific levels of load—for example, September back-to-school traffic, Black Friday, Cyber Monday, or that week of the year when Daylight Saving Time means Europe and North America are one hour closer, meaning more of your users are awake and online simultaneously.
Bugs that manifest only with a particular mix of requests—for example, servers closer to Asia experiencing a more expensive traffic mix due to language encodings for Asian character sets.
Bugs that manifest only when users exercise the system in unexpected ways—for example, Calendar being used by an airline reservation system! Therefore, it is important to expand your testing regimen to test behaviors that do not occur every day.
When a production system is plagued by several concurrent bugs, it’s much more difficult to identify if a given page is for an
existing
or
new
bug. Minimizing the number of bugs in production not only reduces pager load, it also makes identifying and classifying new bugs easier. Therefore, it is critical to remove production bugs from your systems as quickly as possible. Prioritize fixing existing bugs above delivering new features; if this requires cross-team collaboration, see
SRE Engagement Model
.
Architectural or procedural problems, such as automated health checking, self-healing, and load shedding, may need significant engineering work to resolve. Remember, for simplicity’s sake we’ll consider these problems “bugs,” even if their size, their complexity, or the effort required to resolve them is significant.
Chapter 3
of
Site Reliability Engineering
describes how error budgets are a useful way to manage the rate at which new bugs are released to production. For example, when a service’s SLO violations exceed a certain fraction of its total quarterly error budget—typically agreed in advance between the developer and SRE teams—new feature development and feature-related rollouts can be halted temporarily to focus on stabilizing the system and reducing the frequency of pages.
The Connection team from our example adopted a strict policy requiring every outage to have a tracking bug. This enabled the team’s technical program manager to examine the root cause of their new bugs in aggregate. This data revealed that human error was the second most common cause of new bugs in production.
Because humans are error-prone, it’s better if all changes made to production systems are made by automation informed by (human-developed) intent configuration. Before you make a change to production, automation can perform additional testing that humans cannot. The Connection team was making complex changes to production semimanually. Not surprisingly, the team’s manual changes went wrong sometimes; the team introduced new bugs, which caused pages. Automated systems making the same changes would have determined that the changes were not safe before they entered production and became paging events. The technical program manager took this data to the team and convinced them to prioritize automation projects.
Identification delay
It’s important to promptly identify the cause(s) of alerts because the longer it takes to identify the root cause of a page, the more opportunity it has to recur and page again. For example, given a page that manifests only under high load, say at daily peak, if the problematic code or configuration is not identified before the next daily peak, it is likely that the problem will happen again. There are several techniques you might use to reduce identification delays:
Use good alerts and consoles
Ensure pages link to relevant monitoring consoles, and that consoles highlight where the system is operating out of specification. In the console, correlate black-box and white-box paging alerts together, and do the same with their associated graphs. Make sure playbooks are up to date with advice on responding to each type of alert. On-call engineers should update the playbook with fresh information when the corresponding page fires.
Practice emergency response
Run
“Wheel of Misfortune” exercises
(described in
Site Reliability Engineering
) to share general and service-specific debugging techniques with your colleagues.
Perform small releases
If you perform frequent, smaller releases instead of infrequent monolithic changes, correlating bugs with the corresponding change that introduced them is easier. Canarying releases, described in Canarying Releases gives a strong signal about whether a new bug is due to a new release.
Log changes
Aggregating change information into a searchable timeline makes it simpler (and hopefully quicker) to correlate new bugs with the corresponding change that introduced them. Tools like
the Slack plug-in for Jenkins
can be helpful.
Ask for help
In
Site Reliability Engineering
,
“Managing Incidents”
, we talked about working together to manage large outages. The on-call engineer is never alone; encourage your team to feel safe when asking for help.
Mitigation delay
The longer it takes to mitigate a bug once it’s identified, the more opportunity it has to recur and page again. Consider these techniques for reducing mitigation delays:
Roll back changes
If the bug was introduced in a recent code or configuration rollout, promptly remove the bug from production with a rollback, if safe and appropriate (a rollback alone may be necessary but is not sufficient if the bug caused data corruption, for example). Remember that even a “quick fix” needs time to be tested, built, and rolled out. Testing is vital to making sure the quick fix actually fixes the bug, and that it doesn’t introduce additional bugs or other unintended consequences. Generally, it is better to “roll back, fix, and roll forward” rather than “roll forward, fix, and roll forward again.”
If you aim for 99.99% availability, you have approximately 15 minutes of error budget per quarter. The build step of rolling forward may take much longer than 15 minutes, so rolling back impacts your users much less.
(99.999% availability affords an error budget of 80 seconds per quarter. At this point, systems may need self-healing properties, which is out of scope for this chapter.)
If at all possible, avoid changes that can’t be rolled back, such as API-incompatible changes and lockstep releases.
Use feature isolation
Design your system so that if feature X goes wrong, you can disable it via, for example, a feature flag without affecting feature Y. This strategy also improves release velocity, and makes disabling feature X a much simpler decision—you don’t need to check that your product managers are comfortable with also disabling feature Y.
Drain requests away
Drain requests (i.e., redirect customer requests) away from the elements of your system that exhibit the bug. For example, if the bug is the result of a code or config rollout, and you roll out to production gradually, you may have the opportunity to drain the elements of your infrastructure that have received the update. This allows you to mitigate the customer impact in seconds, rather than rolling back, which may take minutes or longer.
Alerting
Google SRE’s maximum of two distinct incidents per 12-hour shift encourages us to be thoughtful and cautious about how we configure paging alerts and how we introduce new ones.
Site Reliability Engineering
,
“Monitoring Distributed Systems”
, describes Google’s approach to defining the thresholds for paging alerts. Strictly observing these guidelines is critical to maintaining a healthy on-call rotation.
It is worth highlighting some key elements discussed in that chapter:
All alerts should be immediately actionable. There should be an action we expect a human to take immediately after they receive the page that the system is unable to take itself. The signal-to-noise ratio should be high to ensure few false positives; a low signal-to-noise ratio raises the risk for on-call engineers to develop alert fatigue.
If a team fully subscribes to SLO-based alerting, or paging only when error budget is burned (see the section
“Black-Box Versus White-Box”
in
Site Reliability Engineering
), it is critical that all teams involved in developing and maintaining the service agree about the importance of meeting the SLO and prioritize their work accordingly.
If a team fully subscribes to SLO-based and symptom-based alerting, relaxing alert thresholds is rarely an appropriate response to being paged.
Just like new code, new alerts should be thoroughly and thoughtfully reviewed. Each alert should have a corresponding playbook entry.
Receiving a page creates a negative psychological impact. To minimize that impact, only introduce new paging alerts when you really need them. Anyone on the team can write a new alert, but the whole team reviews proposed alert additions and can suggest alternatives. Thoroughly test new alerts in production to vet false positives before they are upgraded to paging alerts. For example, you might email the alert’s author when the alert fires, rather than paging the on-call engineer.
New alerts may find problems in production that you weren’t aware of. After you address these production bugs, alerting will only page on
new
bugs, effectively functioning like regression tests.
Be sure to run the new alerts in test mode long enough to experience typical periodic production conditions, such as regular software rollouts, maintenance events by your Cloud provider, weekly load peaks, and so on. A week of testing is probably about right. However, this appropriate window depends on the alert and the system.
Finally, use the alert’s trigger rate during the testing period to predict the expected consumption of your pager budget as a result of the new alert. Explicitly approve or disallow the new alert as a team. If introducing a new paging alert causes your service to exceed its paging budget, the stability of the system needs additional attention.
Rigor of follow-up
Aim to identify the root cause of every page. “Root causes” extend out of the machine and into the team’s processes. Was an outage caused by a bug that would have been caught by a unit test? The root cause might not be a bug in the code, but rather a bug in the team’s processes around code review.
If you know the root cause, you can fix and prevent it from ever bothering you or your colleagues again. If your team cannot figure out the root cause, add monitoring and/or logging that will help you find the root cause of the page the next time it occurs. If you don’t have enough information to identify the bug, you can always do
something
to help debug the page further next time. You should rarely conclude that a page is triggered by “cause unknown.” Remember that as an on-call engineer, you are never alone, so ask a colleague to review your findings and see if there’s anything you missed. Typically, it’s easiest to find the root cause of an alert soon after the alert has triggered and fresh evidence is available.
Explaining away a page as “transient,” or taking no action because the system “fixed itself” or the bug inexplicably “went away,” invites the bug to happen again and cause another page, which causes trouble for the next on-call engineer.
Simply fixing the immediate bug (or making a “point” fix) misses a golden opportunity to prevent similar alerts in the future.  Use the paging alert as an chance to surface engineering work that improves the system and obviates an entire class of possible future bugs. Do this by filing a project bug in your team’s production component, and advocate to prioritize its implementation by gathering data about how many individual bugs and pages this project would remove. If your proposal will take 3 working weeks or 120 working hours to implement, and a page costs on average 4 working hours to properly handle, there’s a clear break-even point after 30 pages.
For example, imagine a situation where there are too many servers on the same failure domain, such as a switch in a datacenter, causing regular multiple simultaneous failures:
Point fix
Rebalance your current footprint across more failure domains and stop there.
Systemic fix
Use automation to ensure that this type of server, and all other similar servers, are always spread across sufficient failure domains, and that they rebalance automatically when necessary.
Monitoring (or prevention) fix
Alert preemptively when the failure domain diversity is below the expected level, but not yet service-impacting.  Ideally, the alert would be a ticket alert, not a page, since it doesn’t require an immediate response. The system is still serving happily, albeit at a lower level of redundancy.
To make sure you’re thorough in your follow-up to paging alerts, consider the following questions:
How can I prevent this specific bug from happening again?
How can I prevent bugs like this from happening again, both for this system and other systems I’m responsible for?
What tests could have prevented this bug from being released to production?
What ticket alerts could have triggered action to prevent the bug from becoming critical before it paged?
What informational alerts could have surfaced the bug on a console before it became critical?
Have I maximized the impact of the fixes I’m making?
Of course, it’s not enough for an on-call engineer to just file bugs related to the pages that occur on their shift. It’s incredibly important that bugs identified by the SRE team are dealt with swiftly, to reduce the possibility of them recurring. Make sure resource planning for both the SRE and developer teams consider the effort required to respond to bugs.
We recommend reserving a fraction of SRE and developer team time for responding to production bugs as they arise. For example, a Google on-caller typically doesn’t work on projects during their on-call shift. Instead, they work on bugs that improve the health of the system. Make sure that your team routinely prioritizes production bugs above other project work. SRE managers and tech leads should make sure that production bugs are promptly dealt with, and escalate to the developer team decision makers when necessary.
When a paging event is serious enough to warrant a postmortem, it’s even more important to follow this methodology to catalog and track follow-up action items. (See
Postmortem Culture: Learning from Failure
for more details.)
Data quality
Once you identify bugs in your system that caused pages, a number of questions naturally arise:
How do you know which bug to fix first?
How do you know which component in your system caused most of your pages?
How do you determine what repetitive, manual action on-call engineers are taking to resolve the pages?
How do you tell how many alerts with unidentified root causes remain?
How do you tell which bugs are
truly
, not just anecdotally, the worst?
The answer is simple: collect data!
When building up your data collection processes, you might track and monitor the patterns in on-call load, but this effort doesn’t scale. It’s far more sustainable to file a placeholder bug for each paging alert in your bug tracking system (e.g., Jira,
IssueTracker
), and for the on-call engineer to create a link between the paging alerts from your monitoring system and the relevant bug in the bug tracking system, as and when they realize that each alert is symptomatic of a preexisting issue. You will end up with a list of as-yet-not-understood bugs in one column, and a list of all of the pages that each bug is believed to have caused in the next.
Once you have structured data about the causes of the pages, you can begin to analyze that data and produce reports. Those reports can answer questions such as:
Which bugs cause the most pages? Ideally we’d roll back and fix bugs immediately, but sometimes, finding the root cause and deploying the fix takes a long time, and sometimes silencing key alerts isn’t a reasonable option. For example, the aforementioned Connection SRE Team might experience ongoing network congestion that isn’t immediately resolvable but still needs to be tracked. Collecting data on which production issues are causing the most pages and stress to the team supports data-driven conversations about prioritizing your engineering effort systematically.
Which component of the system is the cause of most pages (payments gateway, authentication microservice, etc.)?
When correlated with your other monitoring data, do particular pages correspond to other signals (peaks in request rate, number of concurrent customer sessions, number of signups, number of withdrawals, etc.)?
Tying structured data to bugs and the root causes of your pages has other benefits:
You can automatically populate a list of existing bugs (that is, known issues), which may be useful for your support team.
You can automatically prioritize fixing bugs based on the number of pages each bug causes.
The quality of the data you collect will determine the quality of the decisions either humans or automata can make. To ensure high-quality data, consider the following techniques:
Define and document your team’s policy and expectations on data collection for pages.
Set up nonpaging alerts from the monitoring system to highlight where pages were not handled according to those expectations. Managers and tech leads should make sure that the expectations are met.
Teammates should follow up with each other when handoffs don’t adhere to expectations. Positive comments such as, “Maybe this could be related to bug 123,” “I’ve filed a bug with your findings so we can follow up in more detail,” or “This looks a lot like what happened on my shift last Wednesday: <link to page, bug>” powerfully reinforce the expected behaviors and ensure that you maximize opportunities for improvement. No one wants to be paged for the same issue that paged their teammate in the previous shift.
Vigilance
All too often, teams fall into operational overload by a thousand cuts. To avoid
boiling the frog
, it is important to pay attention to the health of on-call engineers over time, and ensure that production health is consistently and continuously prioritized by both SRE and developer teams.
The following techniques can help a team keep a watchful eye on pager load:
At production meetings (see the section
“Communications: Production Meetings”
in
Site Reliability Engineering
, Chapter 31), regularly talk about trends in pager load based on the structured data collected. We’ve found a 21-day trailing average to be useful.
Set up ticket alerts, possibly targeted at tech leads or managers, for when pager load crosses a “warning” threshold that your team agrees on beforehand.
Hold regular meetings between the SRE team and developer team to discuss the current state of production and the outstanding production bugs that are paging SRE.
On-Call Flexibility
Shift Length
An on-call rotation that has to handle one or more pages per day must be structured in a sustainable way: we recommend limiting shift lengths to 12 hours. Shorter shifts are better for the mental health of your engineers. Team members run the risk of exhaustion when shifts run long, and when people are tired, they make mistakes. Most humans simply can't produce high-quality work if they're on-call continuously. Many countries have laws about maximum working hours, breaks, and working conditions.
While spreading on-call shifts across a team's daylight hours is ideal, a 12-hour shift system doesn't necessitate a globally distributed team. Being on-call overnight for 12 hours is preferable to being on-call for 24 hours or more. You can make 12-hour shifts work even in a single location. For example, instead of asking a single engineer to be on-call for 24 hours a day across an entire week-long shift, it would be better for two engineers to split a week of on-call, with one person on-call during the day and one on-call overnight.
In our experience, 24 hours of on-call duty without reprieve isn't a sustainable setup. While not ideal, occasional overnight 12-hour shifts at least ensure breaks for your engineers. Another option is to shorten shifts to last less than a week—something like 3 days on, 4 days off.
Scenario: A change in personal circumstances
Imagine you are a member of an on-call team for a large service that has a 24/7 follow-the-sun model split across two sites. The arrangement works well for you. While you’re not thrilled about the possibility of a 6 a.m. page, you are happy with the work you and the team are doing to keep the operational load manageable while improving the reliability of the service.
All is well…until one day you realize that the on-call schedule and the demands of your personal life are starting to clash. There are many potential reasons why—for example, becoming a parent, needing to travel on short notice and take a leave from work, or illness.
You need your on-call duties to coexist with your new personal schedule.
Many teams and organizations face this challenge as they mature. People’s needs change over time, and maintaining a healthy balance of diverse teammate backgrounds leads to an on-call rotation characterized by diverse needs. The key to keeping a healthy, fair, and equitable balance of on-call work and personal life is flexibility.
There are a number of ways that you can apply flexibility to on-call rotations to meet the needs of team members while still ensuring coverage for your services or products. It is impossible to write down a comprehensive, one-size-fits-all set of guidelines. We encourage embracing flexibility as a
principle
rather than simply adopting the examples listed here.
Automate on-call scheduling
As teams grow, accounting for scheduling constraints—vacation plans, distribution of on-call weekdays versus weekends, individual preferences, religious requirements, and so on—becomes increasingly difficult. You can’t manage this task manually; it’s hard to find any solution at all, much less a fair one.
“Fairness” doesn’t mean a completely uniform distribution of each type of shift across team members. Different people have different needs and different preferences. Therefore, it’s important for the team to share those preferences and try to meet them in an intelligent way. Team composition and preferences dictate whether your team prefers a uniform distribution, or a more customized way of meeting scheduling preferences.
Using an automated tool to schedule on-call shifts makes this task much easier. This tool should have a few basic characteristics:
It should rearrange on-call shifts to accommodate the changing needs of team members.
It should automatically rebalance on-call load in response to any changes.
It should do its best to ensure fairness by factoring in personal preferences such as “no primary during weekends in April,” as well as historical information such as recent on-call load per engineer.
So that on-call engineers can plan around their on-call shifts, it must never change an already generated schedule.
Schedule generation can be either fully automated or scheduled by a human. Likewise, some teams prefer to have members explicitly sign off on the schedule, while others are comfortable with a fully automated process. You might opt to develop your own tool in-house if your needs are complex, but there are a number of commercial and open source software packages that can aid in automating on-call scheduling.
Plan for short-term swaps
Requests for short-term changes in the on-call schedule happen frequently. No one can promise on Monday that they won’t have the flu on Thursday. Or you might need to run an unforeseen urgent errand in the middle of your on-call shift.
You may also want to facilitate on-call swaps for nonurgent reasons—for example, to allow on-callers to attend sports training sessions. In this situation, team members can swap a subset of the on-call day (for example, half of Sunday). Nonurgent swaps are typically best-effort.
Teams with a strict pager response SLO need to take commute coverage into account. If your pager response SLO is 5 minutes, and your commute is 30 minutes, you need to make sure that someone else can respond to emergencies while you get to work.
To achieve these goals in flexibility, we recommend giving team members the ability to update the on-call rotation. Also, have a documented policy in place describing how swaps should work. Decentralization options range from a fully centralized policy, where only the manager can change the schedule, to a fully decentralized one, where any team member can change the policy independently. In our experience, instituting peer review of changes provides a good tradeoff between safety and flexibility.
Plan for long-term breaks
Sometimes team members need to stop serving in the on-call rotation because of changes in personal circumstances or burnout. It’s important that teams are structured to allow on-callers to temporarily leave the rotation.
Ideally, team size should allow for a (temporary) staff reduction without causing the rest of the team to suffer too much operational load. In our experience, you need a bare minimum of five people per site to sustain on-call in a multisite, 24/7 configuration, and eight people in a single-site, 24/7 configuration. Therefore, it is safe to assume each site will need one extra engineer as protection against staff reduction, bringing the minimum staffing to six engineers per site (multisite) or nine per site (single-site).
Plan for part-time work schedules
Being on-call with part-time working schedules may seem incompatible, but we’ve found that on-call and part-time work arrangements
are
compatible if you take certain precautions. The following discussion assumes that if a member of your on-call rotation works part-time, they’ll be unavailable for on-call shifts outside of their part-time working week.
There are two main models of part-time working:
Working a reduced amount of full days per week—for example, four 8-hour days a week, instead of five
Working a reduced amount of time each day—for example, 6 hours a day, instead of 8 hours a day
Both models are compatible with on-call work, but require different adjustments to on-call scheduling.
The first model easily coexists with on-call work, especially if the nonworking day(s) are constant over time. In response, you can adopt an on-call shift length of fewer than seven days a week (for example, Monday through Thursday, or Friday through Sunday) and configure the automated scheduler not to schedule the part-time engineer(s) to be on-call on the days they don’t work.
The second model is possible in a couple ways:
Split on-call hours with another engineer, so that no one is on-call when they are not supposed to be. For example, if an on-call engineer needs to work from 9 a.m. to 4 p.m., you can assign the first half of the shift (9 a.m. to 3 p.m.) to them. Rotate the second half (3 p.m. to 9 p.m.) within the team the same way you rotate other on-call shifts.
The part-time engineer can work full hours on their on-call days, which may be feasible if the on-call shift is not too frequent.
As mentioned in
Chapter 11
of
Site Reliability Engineering
, Google SRE compensates support outside of regular hours with a reduced hourly rate of pay or time off, according to local labor law and regulations. Take a part-time engineer’s reduced schedule into account when determining on-call compensation.
In order to maintain a proper balance between project time and on-call time, engineers working reduced hours should receive a proportionately smaller amount of on-call work. Larger teams absorb this additional on-call load more easily than smaller teams.
On-Call Team Dynamics
Our first book touched upon how stress factors like high pager load and time pressure can force on-call engineers to adopt decision strategies based on intuition and heuristics rather than reason and data (see the section “Feeling Safe” in
Chapter 11
of that book). Working from this discussion of team psychology, how do you go about building a team with positive dynamics? Consider an on-call team with the following set of hypothetical problems.
Scenario: A culture of “survive the week”
A company begins with a couple of founders and a handful of employees, all feature developers. Everyone knows everyone else, and everyone takes pagers.
The company grows bigger. On-call duty is limited to a smaller set of more experienced feature developers who know the system better.
The company grows even bigger. They add an ops role to tackle reliability. This team is responsible for production health, and the job role is focused on operations, not coding. The on-call becomes a joint rotation between feature developers and ops. Feature developers have the final say in maintaining the service, and ops input is limited to operational tasks. By this time, there are 30 engineers in the on-call rotation: 25 feature developers and 5 ops, all located at the same site.
The team is plagued by high pager volume. Despite following the recommendations described earlier in this chapter to minimize pager load, the team is suffering from low morale. Because the feature developers prioritize developing new features, on-call follow-up takes a long time to implement.
To make matters worse, the feature developers are concerned about their own subsystem’s health. One feature developer insists on paging by error rate rather than error ratio for their mission-critical module, despite complaints from others on the team. These alerts are noisy, and return many false positives or unactionable pages.
Other members of the on-call rotation aren’t especially bothered by the high pager volume. Sure, there are a lot of pages, but most of them don’t take much time to resolve. As one on-call engineer puts it: “I take a quick look at the page subject and know they are duplicates. So I just ignore them.”
Sound familiar?
Some Google teams experienced similar problems during their earlier days of maturity. If not handled carefully, these problems have the potential to tear the feature developer and ops teams apart and hinder on-call operation. There’s no silver bullet to solve these problems, but we found a couple of approaches particularly helpful. While your methodology may differ, your overall goal should be the same: build positive team dynamics, and carefully avoid tailspin.
Proposal one: Empower your ops engineers
You can remodel the operations organization according to the guidelines outlined in this book and
Site Reliability Engineering
, perhaps even including a change of name (SRE, or similar) to indicate the change of role. Simply retitling your ops organization is not a panacea, but it can be helpful in communicating an
actual
change in responsibilities away from the old ops-centric model. Make it clear to the team and the entire company that SREs own the site operation. This includes defining a shared roadmap for reliability, driving the full resolution of issues, maintaining monitoring rules, and so on. Feature developers are necessary collaborators but don’t own these endeavors.
To return to our hypothetical team, this announcement ushered in the following operational changes:
Action items are assigned only to the five DevOps engineers—who are now SREs. SREs work with subject experts—many of them feature developers—to accomplish these tasks. SREs take on the previously mentioned “error rate versus error ratio” debate by negotiating a change in alerting with the feature developers.
SREs are encouraged to dive into the code to make the changes themselves, if possible. They send code reviews to the subject experts. This has the benefit of building a sense of ownership among SREs, as well as upgrading their skills and authority for future occasions.
With this arrangement, feature developers are explicit collaborators on reliability features, and SREs are given the responsibility to own and improve the site.
Proposal two: Improve team relations
Another possible solution is to build stronger team bonds between team members. Google designates a “fun budget” specifically for organizing offsite activities to strengthen team bonds.
We’ve found that more robust team relationships create a spirit of increased understanding and collaboration among teammates. As a result, engineers are more likely to fix bugs, finish action items, and help out their colleagues. For example, say you turned off a nightly pipeline job, but forgot to turn off the monitoring that checked if the pipeline ran successfully. As a result, you accidentally page a colleague at 3 a.m. If you’ve spent a little time with that colleague, you’d feel much worse about what happened, and strive to be considerate by being more careful in the future. The mentality of “I protect my colleagues” translates to a more productive work atmosphere.
We’ve also found that making all members of the on-call rotation sit together, regardless of job title and function area, helps improve team relations tremendously. Encourage teams to eat lunch with each other. Don’t underestimate the power of relatively straightforward changes like these. It plays directly into team dynamics.
Conclusion
SRE on-call is different than traditional ops roles. Rather than focusing solely on day-to-day operations, SRE fully owns the production environment, and seeks to better it through defining appropriate reliability thresholds, developing automation, and undertaking strategic engineering projects. On-call is critical for site operations, and handling it right is crucial to the company’s bottom line.
On-call is a source of much tension, both individually and collectively. But if you’ve stared into the eyes of the monster long enough, there is wisdom to be found. This chapter illustrates some of the lessons about on-call that we learned the hard way; we hope that our experience can help others avoid or tackle similar issues.
If your on-call team is drowning in endless alerts, we recommend taking a step back to observe the situation from a higher level. Compare notes with other SRE and partner teams. Once you’ve gathered the necessary information, address the problems in a systematic way. Thoughtfully structuring on-call is time well spent for on-call engineers, on-call teams, and the whole company.
1
Note that this example is often a red flag situation for organizations that aren’t actually practicing DevOps, in which case, a name change won’t fix more structural problems.
2
One “incident” is defined as one “problem,” no matter how many alerts have been fired for the same “problem.” One shift is 12 hours.
3
There is more on this topic in
Seeking SRE
by David Blank-Edelman (O’Reilly).
4
SRE teams at Google are paired across time zones for service continuity.
5
A “bug” in this context is any undesirable system behavior resulting from software or configuration error. Logic errors in code, incorrect configuration of a binary, incorrect capacity planning, misconfigured load balancers, or newly discovered vulnerabilities are all valid examples of “production bugs” that contribute to pager load.
