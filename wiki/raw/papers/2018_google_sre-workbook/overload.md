---
title: 'Google SRE: Handling Operational Overload, Workload Management'
source_url: https://sre.google/workbook/overload/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/overload.html
original_sha256: a9ef230b2bc1534fb9998741e280f6a9e28b05445bcb02c33bdf6d149f504c4b
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/overload/
ingested: '2026-10-14'
sha256: f31ff0ddfdf27a045a7542f4d4fa8b2b495c52970bd5cb3cd8d48b22b016a651
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Identifying and Recovering from Overload
By Maria-Hendrike Peetz, Luis Quesada Torres, and Marilia Melo with Diane Bates
When an SRE team is running smoothly, team members should feel like they can comfortably handle all of their work. They should be able to work on tickets and still have time to work on long-term projects that make it easier to manage the service in the future.
But sometimes circumstances get in the way of a team’s work goals. Team members take time off for long-term illnesses or move to new teams. Organizations hand down new production-wide programs for SRE. Changes to the service or the larger system introduce new technical challenges. As workload increases, team members start working longer hours to handle tickets and pages and spend less time on engineering work. The whole team starts to feel stressed and frustrated as they work harder but don’t feel like they are making progress. Stress, in turn, causes people to make more mistakes, impacting reliability and, ultimately, end users. In short, the team loses its ability to regulate its daily work and effectively manage the service.
At this point, the team needs to find a way out of this overloaded state. They need to rebalance their workload so that team members can focus on essential engineering work.
Operational load
(or
operational workload
) is a term that describes the ongoing maintenance tasks that keep systems and services running at optimal performance. There are three distinct types of operational load:
pages
,
tickets
, and
ongoing operational responsibilities
. Pages typically require immediate attention, and tickets related to urgent problems can have tight deadlines. Both pages and urgent tickets interrupt SREs from working on engineering projects that support the team’s operational responsibilities. For that reason, we refer to them as
interrupts
.
Chapter 29
of
Site Reliability Engineering
discusses techniques to manage the interrupts that naturally arise when a team is maintaining a complex system in a functional state.
When operational load outstrips a team’s ability to manage it, the team ends up in a state of
operational overload
(also called
work overload
). A team is in a state of operational overload when it can’t make progress toward key priorities because urgent issues continually preempt project work. In addition to detracting from the team’s priorities and service improvements, overload can increase the chance that engineers make errors.
1
The threshold of operational overload can vary from team to team. Google SRE teams cap operational work at 50% of an engineer’s time. A successful SRE team must have confidence that over the long term, they will be able to complete the engineering projects required to reduce the operational load for the services they manage.
This chapter describes how teams at Google progressed from a difficult situation characterized by operational overload to a
well-managed workload.
Two case studies show the detrimental effect of operational overload on team health, and how the teams made changes to their daily tasks so they could focus on long-term impactful projects. In Case Study 1, overload results when remaining members on a shrinking team are unable to keep up with the workload. In Case Study 2, a team suffers from
perceived overload
—a state that has the same effects as operational overload, but starts as a misperception of the real workload.
While these case studies highlight specific actions that worked for two Google SRE teams, the section
Strategies for Mitigating Overload
provides practices for identifying and mitigating overload that apply to any company or organization. Therefore, this chapter should be useful to managers of overloaded teams, or any SRE team concerned about overload.
From Load to Overload
Regardless of its origin, overload is an occupational stress that can cripple productivity. Left unchecked,
it can cause serious illness
. For SRE teams, operational load is typically a combination of cognitively difficult tasks (like debugging memory leaks or segmentation faults) and many small tasks that require frequent context switches (working through quota requests, starting binary rollouts, etc.).
Work overload often happens when a team doesn’t have enough time to handle all these tasks—an objective reality when the number of tasks assigned to a team can’t be completed within the given deadline for each task. Perceived overload is more subjective, and happens when individuals on the team
feel
that they have too much work. This usually happens when several organizational or work changes take place over a short period of time, but the team has little opportunity to communicate with leadership about the changes.
It’s never clear what problems will develop when you’re on-call, or what your workload will be. On the one hand, a single, seemingly innocent ticket about running out of disk space might lead to an in-depth investigation of a recurring garbage collection job. On the other hand, a pager storm with 20+ pages might turn out to be a case of bad monitoring. When it’s hard to estimate or predict your workload, you can easily fall victim to cognitive biases and misjudge your workload—for example, you might gauge a ticket queue as too large to finish during your on-call shift. Even if you can finish all the tickets quickly and the actual workload is low, you
feel
overloaded when you first look at the ticket queue. This perceived overload
2
itself has a psychological component that affects your approach and attitude toward your work. If you
don’t
start your day with the preconception that there’s too much work, you’re more likely to dive in and start working your way through the ticket queue. Perhaps you work all day and don’t finish your workload (thus facing work overload), but you make a lot more progress than if you had started your day feeling overwhelmed.
Accumulating many interrupts can lead to work overload, but it doesn’t have to. But when frequent interruptions are paired with external stress factors, a large workload (or even a small workload) can easily turn into perceived overload. This stress might stem from the fear of disappointing other team members, job insecurity, work-related or personal conflicts, illness, or health-related issues like the lack of sleep or exercise.
If your work isn’t properly prioritized, every task can seem equally urgent, leading to both actual and perceived overload. In the case of actual overload, the urgency of tickets and alerts might cause team members to work until they resolve the problem, even if doing so means continuous long hours. When a team faces perceived overload, reprioritizing can help decrease the amount of urgent work, creating space for them to tackle the sources of overload through project work.
When analyzing your specific situation, you shouldn’t necessarily assume that the workload itself needs to change. Instead, we recommend first quantifying the work your team faces, and how it has (or hasn’t) changed over time. For example, you might measure workload by the number of tickets and pages the team handles. If your workload hasn’t actually changed over time, the team might feel overloaded simply because they perceive the work as overwhelming. To get a more holistic view of the team’s current workload, you can collect a one-time snapshot by asking every member to list all the work tasks they face. Then take a look at psychological stress factors your team faces, such as organizational changes or reprioritization. Once you’ve done your research, you have a stable basis for making decisions about changing the workload.
Strategies for Mitigating Overload
talks more about how to identify overload, both real and perceived. First, we present two case studies of teams that recognized that they were in overload and took steps to alleviate it.
Case Study 1: Work Overload When Half a Team Leaves
Background
One of Google’s internal storage SRE teams was in charge of backends for multiple services, including Gmail, Google Drive, and Google Groups, and many other internal or user-facing services. We experienced a crisis in mid-2016 when two-thirds of the team—including the most senior engineer (the manager)—transferred to other opportunities within a relatively short window, for genuinely entirely unrelated reasons. This event obviously led to a huge workload management problem: fewer SREs available to cover the same operational and project work quickly resulted in overload. Our work was also bottlenecked because each team member’s expertise was siloed to a different area of production. While the addition of new team members and three interns would improve our workload in the long term, ramping up those engineers would take a serious investment of time and energy.
Problem Statement
The preceding factors significantly decreased team productivity. We started to fall behind on project work, and tickets related to the many services we managed began to pile up. We didn’t have the bandwidth to address this backlog, as all of our work was consumed by higher-priority tasks. It wouldn’t be long before we weren’t able to undertake all of the critical and urgent work we needed to. Meanwhile, our team was slated to receive more high-priority work soon.
If we didn’t move some work off our plate, it was only a matter of time before we accidentally began to drop important work. However, as soon as we started offloading work, we hit some psychological barriers:
Dropping any work that was in progress felt like we had just wasted our efforts. Most of the backlog seemed to be either critical or worth the effort to us, so it just didn’t feel right to cancel or delay projects indefinitely. We didn’t realize we were in the grip of a
sunk cost fallacy
.
Putting effort into automating processes or fixing the root cause of the workload was not as critical as immediately dealing with high-priority interrupts. When this work was added to the top of an already huge pile, all of the work felt overwhelming.
What We Decided to Do
We gathered the team in a room and listed all the team’s responsibilities, including project backlog, operational work, and tickets. Then we triaged every list item. Viewing every single one of our work tasks (even though the list barely fit on the whiteboard) helped us identify and redefine our actual priorities. We were then able to find ways to minimize, hand off, or eliminate lower-priority work items.
Implementation
We identified low-effort automation that, while not critical, would significantly reduce operational load once deployed.
We also identified common problems that we could document that would enable self-service. Writing the procedures our customers needed didn’t take long, and removed some repetitive work from our queue.
We closed as many of our backlogged tickets as we reasonably could. Most of these tickets turned out to be obsolete, redundant, or not as urgent as they claimed. Some tickets were monitoring artifacts that were nonactionable, so we fixed the relevant monitoring. In some cases, we were actively addressing issues that weren’t critical. We set these issues aside to work on more urgent tickets, but first documented our progress so we wouldn’t lose context before we were able to work on them again.
When in doubt, we dropped a task, but marked it for a second phase of triage. Once our plates were (almost) empty, we revisited this tentative list to decide what tasks to resume. It turned out that almost none of these tasks were impactful or important enough to resume.
In two days—one day of intensive triage plus one day of documenting processes and implementing automation—our much smaller team addressed a backlog of several months of interrupts. We could then deal with the few remaining interrupts, which were related to active issues in production.
Lessons Learned
Our team learned that
identifying and scoping overload
is the first step toward fixing it. We needed to get everyone in a room and reevaluate the backlog before we could help our team get back to a healthy state.
In order to avoid a new pile-up of interrupts, we started triaging interrupts once every two weeks. Our technical lead periodically checks the task queue and evaluates whether the team is at risk of becoming overloaded. We decided that each team member should have 10 or fewer open tickets to avoid overload. If the team lead notices that team members have more than 10 tickets, they can do one or some combination of the following:
Remind the team to close out stale tickets.
Sync with overloaded team members and offload tickets from them.
Prompt individual team members to address their ticket queue.
Organize a team-wide one-day ticket fix-it.
Assign work to fix the sources of tickets, or operational work to reduce future tickets.
Case Study 2: Perceived Overload After Organizational and Workload Changes
Background
The Google SRE team in this case study was split between two locations, with six or seven on-call engineers at each site (for more discussion on team size, see
Chapter 11
of
Site Reliability Engineering
. While the Sydney team was operationally healthy, the Zürich team was overloaded.
Before the Zürich team went into overload, we were stable and content. The number of services we managed was relatively stable, and each was varied and high maintenance. While the SLOs of the services we supported were mismatched with the SLOs of their external dependencies, this mismatch hadn’t caused any issues. We were working on a number of projects to improve the services we managed (for example, improving load balancing).
Simultaneous triggers sent the Zürich team into overload: we started onboarding new services that were noisier and less integrated into Google’s general infrastructure, and the technical lead manager and another team member left our team, leaving it two people short. The combination of the additional workload and knowledge drain triggered more problems:
Untuned monitoring for the new services and the migration-related monitoring resulted in more pages per shift. This buildup was gradual, so we didn’t notice the uptick as it occurred.
SREs felt relatively helpless with the new services. We didn’t know enough about them to react appropriately, and often needed to ask the development team questions. While the overload perhaps warranted handing a service back to developers, our team had never handed back a service, so we didn’t really consider this a viable option.
A smaller on-call rotation of five people cut into the hours we normally spent on operational work.
New ticket alerts were surfacing problems that existed before the recent team changes. While we had simply ignored these problems in the past, we were now required to move ignored email alerts to tickets. Project planning hadn’t taken this new source of technical debt into account.
A new ticket SLO required us to handle tickets within three days, meaning that on-callers had to resolve tickets created during their on-call shift much sooner.
3
The SLO aimed to reduce the number of tickets being added to our (mostly ignored) backlog, but created a side effect that was perhaps even worse. Now SREs felt that they couldn’t get the rest they needed after a shift because they had to immediately tackle follow-up work. The higher priority placed on these tickets also meant that SREs didn’t have enough time for other operational work.
During this time, our team was assigned to a new manager who also managed two other teams. The new manager was not part of the on-call rotation and therefore didn’t directly feel the stress team members were experiencing. When the team explained the situation to the manager, nothing changed. Team members felt that they weren't being heard, which left them feeling distant from the management team.
The overload from tickets continued for months, making team members grumpy, until a cascade of unhappiness spread across the team.
Problem Statement
After losing two people and receiving additional and varied work, our team felt overloaded. When we tried to communicate this feeling to our direct manager, the manager disagreed. As the long hours continued, exhaustion set in. Productivity was declining and tasks started accruing faster than the team could resolve them. The perceived overload now became objective overload, making the situation worse.
The emotional stress caused by overload was lowering morale and causing some team members to burn out. As individuals dealt with the physical effects from overwork (illness and lower productivity), other people on the team had to pick up more work. The work assigned in weekly team meetings wasn’t getting done.
We then started assuming we couldn’t depend on other people to get their work done, which eroded feelings of trust and dependability within the team. As a result, we did not feel safe about
interpersonal risk taking
, an important factor in psychological safety (see
Chapter 11
in
Site Reliability Engineering
). Team members didn’t feel accepted and respected by other team members, so they didn’t freely collaborate with each other. As psychological safety diminished on the team, collaboration stopped, slowing down information sharing and causing further inefficiencies.
Team surveys also revealed a loss of psychological safety—team members said they didn’t feel like they belonged on the team. They no longer cared about their own career development, and the promotion rate on the team dropped to an all-time low.
We finally hit a breaking point when upper management assigned us new mandatory company-wide projects. At this point, we renewed our conversations with management about overload with renewed vigor. A series of discussions revealed that our unhappy situation wasn’t just a result of too much work—our perceptions of team safety led us to stop trusting and collaborating with each other.
What We Decided to Do
Upper management assigned our team a new manager who wasn’t shared among three teams. The new manager used a
participatory management style
to improve psychological safety on the team so that we could once again collaborate. This method empowers team members to actively participate in solving team problems. The entire team, including our direct manager, engaged in a set of simple team-building exercises to improve the effectiveness of our team (some of which were as simple as drinking tea together).
4
As a result, we were able to draft a set of goals:
Short term
Relieve stress and improve psychological safety to establish a healthy work atmosphere.
Medium term
Build confidence of individual team members through training.
Find the root cause of the issues that are causing overload.
Long term
Resolve ongoing problems that contributed to the cascade.
In order to set these goals, we had to first achieve some kind of baseline psychological safety within the team. As morale improved, we began to share knowledge and build on each other’s ideas to figure out ways to get our workload under control.
Implementation
Short-term actions
Long-term stress, whether caused by overwork or perceptions of team safety, decreases productivity and impacts people’s health. Therefore, our most important short-term action was to provide stress relief and improve trust and psychological safety. Once relieved of some stress, team members could think more clearly and participate in driving the whole team forward. Within a month of identifying the overload, we implemented the following:
Started a semiregular round table to discuss issues.
The team released frustration and brainstormed possible causes of the overload.
Found a better metric for measuring load.
We decided to improve upon our original metric of number of pages. We auto-assigned tickets to on-callers, and the on-caller was responsible for these tickets even after their shift ended. Our new metric measured how much time an on-caller needed to resolve a ticket after their shift.
Audited and removed spamming alerts.
We reviewed alerts and removed the ones that didn’t represent user-facing problems.
Silenced alerts generously.
The team deliberately didn’t try to find the source for every single alert, but focused on relieving the stress from being paged and ticketed continuously for issues we already knew about. We used the following strategy:
Alerts that surfaced were silenced until they were fixed.
Alerts could be silenced only for a limited period of time (typically a day, sometimes up to a week). Otherwise, they might mask outages.
Alerts that couldn’t be fixed within a few minutes were assigned to a tracking ticket.
Added a direct manager dedicated to a single team.
Making a well-respected team member the new manager reestablished trust in management. Rather than managing three teams, the new manager could focus more time on the individual team and its members.
Rebalanced the team.
We introduced a new perspective and on-call relief by adding technically experienced SREs that didn’t have preconceptions about the team or organization. Finding appropriate people was by no means an easy task, but was well worth the effort.
Instituted team events like lunches and board game sessions.
Talking about non-work-related topics and laughing together eased tension on the team and improved psychological safety.
Mid-term actions
Short-term solutions alone wouldn’t sustain a healthy atmosphere—for example, one of our short-term tactics was to silence alerts without actually fixing the cause. Within three months, we also took the following actions:
Limited operational work to on-call time as much as possible
(see
Chapter 29
in
Site Reliability Engineering
) so the team could concentrate on permanent fixes and project work.
Returned responsibility for one service back to its development team.
Trained each other (and new team members).
While training requires an investment of time and energy, disseminating knowledge meant that all team members (and future hires) could troubleshoot and fix issues more quickly in the future. Training coworkers improved our confidence, because we came to realize that we actually knew quite a bit about the services. As they gained knowledge, team members started to find new ways to manage services, improving their reliability and reducing overload.
Brought in SREs from the remote team to staff some of our on-call shifts and participate in training.
They noticed the strain on the team and provided some valuable new perspective.
Backfilled the two open roles on the team.
Tackled each alert as the silences expired.
We discussed repetitive pages and pages that resulted in no action at length in the weekly production meeting, which led us to tune alerts and/or fix the underlying problems. While these were important (and obvious) actions, we only had the space to analyze and take action once the alert was silenced and not creating constant noise.
Organized listening events.
Management (including the skip-level manager and team leads) made a conscious effort to listen to the team’s pain points and to find a team-driven solution.
Added perspective.
Hope is not a strategy, but it certainly helps team morale. With the promise of new members joining the on-call rotation, a shift to clearer priorities, and an end to noise-generating projects, the team’s mood improved.
Long-term actions
To help maintain our newfound stability, we are currently aligning our SLOs with the SLOs of their service backends, and working toward making the services more uniform. Uniformity has a double benefit: it decreases cognitive load for SREs and makes it easier to write automation that can be used across services. We’re also reviewing services that have been around for a long time and updating them to current production standards. For example, some services are operating poorly under load that’s increased significantly over the years. Some services need to be updated per changes to their backend services’ policies. Other services simply haven’t been updated for several years.
Effects
A few months after our first brainstorming meeting, results began to surface: on-call shifts became quieter, and our team managed to quickly and efficiently deal with a difficult incident collaboratively as a group. A bit later, new team members arrived. When we discussed psychological safety during a round-table session, the new members said they couldn’t imagine that the team ever had such problems. In fact, they saw our team as a warm and safe place to work. About one year after the original escalation, little of the original overload remained and an anonymous survey showed that team members now felt the team was effective and safe.
Lessons Learned
Workplace changes can have a psychological impact on the people on the team—after all, your teammates are not machines. You need to attend to the team’s stress levels so that people start trusting each other enough to work together; otherwise, the team can enter a vicious cycle of overload that causes stress, which in turn prevents you from tackling overload.
Perceived overload
is
, in fact, overload, and has as much impact to a team as work overload caused by other factors. In our case, our sister team in Sydney didn’t experience the same issues, and the number of pages we fielded didn’t actually change very much compared to previous years. Instead, the loss of two team members, increased cognitive load, increased ticket noise, and a new three-day SLO on tickets led the team to perceive overload. In the end, the difference between objective and perceived overload didn’t matter: the perceived overload of a few team members can very quickly lead to overload for the whole team.
Strategies for Mitigating Overload
An outside perspective can sometimes quite easily identify when a team is overloaded. Similarly, it’s easy to comment on what actions should have been taken in retrospect. But how do you identify overload when you’re in the middle of experiencing it? The path toward a healthy, friendly, and happy work atmosphere can be hard to visualize when you’re mired in overload. This section describes practices for both identifying and mitigating overload on your team.
Recognizing the Symptoms of Overload
It’s pretty easy to identify an overloaded team if you know the symptoms of overload:
Decreased team morale
Overload might manifest as rants and complaints. Surveys on relevant topics (job conditions, work satisfaction, projects, peers, and managers) usually reflect team morale and yield more negative results when a team is overloaded. Regular active listening sessions with team leaders can surface issues that you weren’t aware of. An essential element of active listening is to listen without judgment.
Team members working long hours, and/or working when sick
Working overtime without compensation can be a psychosocial stressor. Leaders should set a good example: work contractual hours and stay home when sick.
More frequent illness
5
Overworked team members tend to get run down and sick more often.
An unhealthy tasks queue
We recommend regularly reviewing your team’s tasks queue to see how many tickets are backlogged, who is dealing with which issues, and what tasks can be delayed or dropped. If the team is missing deadlines, or if urgent matters prevent you from performing this review regularly, the team is very likely accumulating interrupts faster than it can attend to them.
Imbalanced metrics
A few key metrics might indicate that your team is overloaded:
Long time periods to close a single issue
High proportion of time spent on toil
Large number of days to close issues originating from an on-call session
The team should work together to decide what measures to use. There is no one-size-fits-all approach; every team’s overload is reflected in different ways. As a manager, don’t impose a measure on the team without getting an idea of each individual’s workload and work habits. Team members might feel that you don’t understand the work if you insist on using a specific measure. For example, if you’re evaluating load by the number of days it takes to fix an issue, one person might work a full day fixing an issue, while another person might distribute the work across several days, along with other work.
Reducing Overload and Restoring Team Health
After reading through the criteria, you might think your team is already overloaded. Don’t despair! This section provides a list of ideas to get your team back to a healthy state.
In general, giving team members more control and power reduces perceived overload.
6
While managers might be tempted to resort to micro-management in stressful situations, it’s important to keep the team in the loop and work on prioritization together in order to increase the level of performance and job satisfaction.
7
This model assumes
baseline of a functional team
, where you have (at minimum) a somewhat healthy relationship between management and team members, and between team members.
Identify and alleviate psychosocial stressors
When it comes to fixing a dysfunctional team, first and foremost, individual team members need to regain their sense of psychological safety. A team can function only as well as its individual members.
You can start by identifying and alleviating psychosocial stressors
8
for each individual and the team as a whole. Which of these factors do you actually have control over? You can’t control whether or not a team member has a major illness, but you
can
control the size of your team’s backlog (as seen in Case Study 1) or silence pages (as in Case Study 2).
Communicate with your partner product developer teams, and let them know your team is overloaded. They might be able to give a helping hand, provide compassion, or even take over entire projects.
When your team members rely on each other and achieve a certain level of
psychological safety
(such that they’re able to take interpersonal risks), you can give more responsibility to individual team members. Uncovering areas of expertise and assigning point people and technical leads to specific technologies increases their self-confidence and therefore enables them to take risks.
Decision making should be transparent and, if possible, democratic. Each team member should have a feeling of control over the situation. For example, the brainstorming session in Case Study 2 helped the team identify and discuss issues.
Prioritize and triage within one quarter
A healthy team can prioritize and triage issues. Case Study 1 provides a good example of this exercise: the team sat together in a room and reviewed their backlog. The review helped them realize they were overloaded. They reprioritized their work, and worked on the tasks that would quickly reduce some of the overload. The team in Case Study 2 now meets at the end of each quarter to plan and prioritize existing and future work together.
If possible, we recommend that SREs schedule
interrupt-free time
(no on-call) on their calendars, so that they have time to work on qualitatively difficult tasks like developing automation and investigating the root causes of interrupts. In Case Study 2, when the remote team gave the on-call some relief, team members then had precious time to focus on their projects.
If absolutely necessary, drop work: in Case Study 2, the team dropped on-call support for one of their services by returning this responsibility to the development team.
Protect yourself in the future
We strongly recommend establishing metrics to evaluate the team’s workload. Regularly review the metrics to make sure they are measuring the right things.
Once your team emerges from overload, you can prevent future overload by taking steps to monitor or resolve the underlying problems. For example, the team in Case Study 1 now maintains a lightweight triage process to detect a growing backlog of tasks. The team in Case Study 2 is currently working on a long-term plan to align backend and service SLOs.
When your team is in overload, prioritize project work that pays down repetitive toil even more than you would if you weren’t overloaded. You will profit in the future.
Finally, everyone on the team should feel responsible for the early warning signs (see
Recognizing the Symptoms of Overload
) that indicate a possible overload situation. Managers should sit down and talk with team members if they feel that the team is moving toward overload.
Conclusion
In a perfect world, SRE teams would always be able to manage interrupts with the tactics described in our first book. But we’re only human, and sometimes our teams don’t reach that ideal. This chapter examined some of the ways that overload can consume a team and discussed how to detect and respond when it does.
Particularly when it comes to operational work, excessive interrupts can very easily cause a team to slip from a normal workload to overload. Frequent interrupts can lead to overload, and overload negatively affects health and productivity. Overload creates psychosocial stressors for team members, which impacts work even further, causing a self-enforcing cycle.
Perceived overload is a special form of overload that can’t be measured by the amount of toil or operational work. It is hard to pinpoint and to eliminate.
In order to keep a team’s workload in balance, it’s important to constantly monitor (perceived or nonperceived) overload. To better serve your users and do good work, you need to first show respect to yourself and your team. Maintaining a healthy balance in your daily work goes a long way in helping you and your team accomplish that goal.
1
Kara A. Latorella,
Investigating Interruptions: Implications for Flightdeck Performance
(Hampton, VA: Langley Research Center, 1999),
https://go.nasa.gov/2Jc50Nh
; NTSB,
Aircraft Accident Report: NWA DC-9-82 N312RC, Detroit Metro, 16 August 1987 (No. NTSB/AAR-88/05)
(Washington, DC: National Transportation Safety Board, 1988),
https://libraryonline.erau.edu/online-full-text/ntsb/aircraft-accident-reports/AAR88-05.pdf
.
2
Emmanuelle Brun and Malgorzata Milczarek,
Expert Forecast on Emerging Psychosocial Risks Related to Occupational Safety and Health
(Bilbao, Spain: European Agency for Safety and Health at Work, 2007),
https://osha.europa.eu/en/tools-and-publications/publications/reports/7807118
; M. Melchior, I. Niedhammer, L. F. Berkman, and M. Goldberg, “Do Psychosocial Work Factors and Social Relations Exert Independent Effects on Sickness Absence? A Six-Year Prospective Study of the GAZEL Cohort,”
Journal of Epidemiology and Community Health
57, no. 4 (2003): 285–93,
https://jech.bmj.com/content/jech/57/4/285.full.pdf
.
3
For context, according to estimates, an SRE needed at least one additional day of ticket follow-up per shift.
4
We used the Google program based on Project Aristotle:
https://bit.ly/2LPemR2
.
5
Kurt G. I. Wahlstedt and Christer Edling, “Organizational Changes at a Postal Sorting Terminal—Their Effects Upon Work Satisfaction, Psychosomatic Complaints and Sick Leave,”
Work and Stress
11, no. 3 (1997): 279–91.
6
Robert A. Karasek Jr., “Job Demands, Job Decision Latitude, and Mental Strain—Implications for Job Redesign,”
Administrative Science Quarterly
24, no. 2 (1979): 285–308.
7
Frank W. Bond and David Bunce, “Job Control Mediates Change in a Work Reorganization Intervention for Stress Reduction,”
Journal of Occupational Health Psychology
6, no. 4 (2001): 290–302; Toby D. Wall, Paul R. Jackson, and Keith Davids, “Operator Work Design and Robotics System Performance: A Serendipitous Field Study,”
Journal of Applied Psychology
77, no. 3 (1992): 353–62.
8
Brun and Malgorzata,
Expert Forecast
.
