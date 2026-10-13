---
title: Google SRE - Understanding sre team lifecycle handbook
source_url: https://sre.google/workbook/team-lifecycles/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/team-lifecycles.html
original_sha256: f46f9ed0d136b4f1631fd713ef22fe0dd51afdbc3e1d62ada693195297df19b5
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/team-lifecycles/
ingested: '2026-10-14'
sha256: cdd307f3a5e150ebac71b99dc52977a5bd7da08e8f40110873815cadb79123df
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
SRE Team Lifecycles
By David Ferguson and Prashant Labhane
with Shylaja Nukala
The
Preface
to this book set a goal to “dispel the idea that SRE is implementable only at ‘Google scale’ or in ‘Google culture.’” This chapter lays out a
roadmap for maturing an SRE organization
from unstaffed but aspirational, through various stages of maturity, to a robust and (potentially) globally distributed set of SRE teams. Regardless of where you are in your journey as an SRE organization, this chapter will help you identify strategies for evolving your SRE organization.
We discuss the
SRE principles
that need to be in place at each stage of this journey. While your own journey will vary depending on the size, nature, and geographic distribution of your organization, the path we describe to successfully apply SRE principles and implement SRE practices should be generalizable to many different types of organizations.
SRE Practices Without SREs
Even if you don’t have SREs, you can adopt SRE practices by using SLOs. As discussed in
Implementing SLOs
, SLO are the
foundations for SRE practices
. As such, they inform our first principle of SRE:
Note
Principle #1
SRE needs SLOs with consequences.
The performance of your service relative to SLOs should guide your business decisions.
We believe that the following practices—which you can achieve without even having a single SRE—are the crucial steps toward implementing SRE practices:
Acknowledge that you don’t want 100% reliability.
Set a reasonable SLO target. This SLO should measure the reliability that is most important to your users.
Agree on an error budget policy that will help defend your user experience. Use the error budget to help guide:
Tactical actions to mitigate outages or to manage changes that return your system to a reliable state
Longer-term prioritization of work to make the system more reliable and use less of the error budget
Measure the SLO and commit to following the error budget policy. This commitment requires agreement from company leadership.
Even if an organization doesn’t have SRE staff, we believe that it is worthwhile to set SLOs for critical customer applications and to implement an error budget policy, if only because an implicit 100% SLO means a team can only ever be reactive. This SRE principle allows you to make data-informed decisions about how to ensure the reliability of your application.
Starting an SRE Role
Finding Your First SRE
It’s possible that your first SRE employees won’t have explicit experience as an SRE. We’ve found the following areas to be relevant to the SRE role, and therefore appropriate to cover in interviews:
Operations
Running applications in production gives invaluable insights that cannot be easily gained otherwise.
Software engineering
SREs need to understand the software they are supporting, and be empowered to improve it.
Monitoring systems
SRE principles require SLOs that can be measured and accounted for.
Production automation
Scaling operations requires automation.
System architecture
Scaling the application requires good architecture.
Your first SRE will likely occupy a difficult and ambiguous position between velocity and reliability goals. They will need to be resilient and flexible in order to provide the right balance between enabling product development and defending the customer experience.
Placing Your First SRE
Once you’ve hired your first SRE, you now need to decide where to embed them in your organization. You have three main choices:
In a product development team
In an operations team
In a horizontal role, consulting across a number of teams
We recommend that you evaluate the pros and cons of each of these three options after reading this chapter, taking into account:
Your own role and sphere of influence.
If you’re able to effectively influence product development team(s), then embedding an SRE in operations or horizontal work can help iron out gnarly production issues early.
The immediate challenges that you face.
If the challenges require hands-on work to mitigate a technical problem or business risk, then embedding an SRE in an operations or product team can be advantageous. Doing so removes organizational silos and facilitates easy communication between team members.
The challenges you expect to face in the next 12 months.
For example, if you’re focusing on launches, embedding the SRE within a product development team might make sense. If you’re focusing on infrastructure changes, embedding the SRE with an operations team might make more sense.
Your plan for how you want to change your organization.
If you plan to move toward a centralized SRE organization, you might not want to embed SREs in product development teams initially—it might be hard to remove them from these teams later.
The person you have identified as your first SRE.
Decide where this first SRE would be most productive based upon their background and skills.
It might make sense to experiment with different models as you figure out which approach works best for you. However, we strongly recommend sticking with one stable and coherent model in the long term; otherwise, the instability will undermine the effectiveness of SRE.
Bootstrapping Your First SRE
Your first SRE’s initial mission is to get up to speed on the service. In order to have a positive impact, an SRE needs to understand the service’s current problems, its required toil (see
Eliminating Toil
) and the engineering required to keep the system within SLOs. If your organization doesn’t already have SLOs and error budgets as per Principle #1, your first SRE needs to perform the engineering required to design and implement these tools. At this point, our second SRE principle comes into play:
Note
Principle #2
SREs must have time to make tomorrow better than today.
Without this principle, toil will only increase as service usage increases and the system becomes correspondingly larger and more complex. A healthy balance between operational responsibilities and project work is essential—if toil becomes too burdensome, talented engineers will flee the team. For more guidance on how an SRE team might obtain that balance, see
Identifying and Recovering from Overload
.
Initial project work might focus on one of the following:
Improving monitoring so you can better understand the system when things go wrong.
Addressing any high-priority actions identified in recent postmortems (see
Postmortem Culture: Learning from Failure
).
Implementing automation to reduce a specific element of toil required to run the service.
It is vital that the SRE has a distinctive role and that their projects benefit the whole team
. Look out for signs that the SRE work is not going well:
Their mix of work is indistinguishable from other engineering work.
If your first SRE is on a product development team, they are doing more than their fair share of operational work, or they are the only person working on service configuration changes.
The SLOs are not being taken seriously, and the SRE isn’t making progress in measuring and defending the customer experience.
Distributed SREs
If your organization doesn’t have (or doesn’t plan to have) a discrete
SRE team
(or teams), it’s important to construct a community for distributed SREs.   This community should advocate the SRE’s distinctive role and drive consistent changes in reliability-focused technology or practices across teams. Without a social grouping, individual SREs may feel very isolated.
Your First SRE Team
You might start an SRE team in a number of ways. Approaches we’ve used at Google, from least to most complex, include:
Creating a new team as part of a major project
Establishing a horizontal SRE team
Converting an existing team (for example, an operations team)
The approach that’s best for your organization is highly situational. A team needs enough SREs to handle the operational tasks required to run the service. Addressing that workload brings us to our  third principle:
Note
Principle #3
SRE teams have the ability to regulate their workload.
Outside of a large SRE organization, a team likely can’t embrace this concept from day one. This principle is open to interpretation and can be difficult to put into practice organizationally. It’s also the most subtle of our three principles, and bears some unpacking. The following sections walk through the stages of building a team, using Tuckman’s performance model and stages of
forming
,
storming
,
norming
, and
performing
.
1
Forming
The team you assemble should have combined experience and expertise that includes the following:
Making changes to application software to improve reliability and performance.
Writing software to:
Expedite the detection and mitigation of problems in production.
Automate manual processes.
Establishing and using strong software practices and standards to facilitate long-term maintainability.
Having a methodical and careful approach to making operational changes: be able to describe why certain practices are reliable.
Understanding system architecture (distributed systems design and operation).
Ideally, your team will be ready to adopt a new way of working, and have a balance of skills and established personal relationships with other teams. If possible, we recommend that you seed the team with internal transfers. This can reduce the time it takes your team to get up and running.
Creating a new team as part of a major project
You might create a
new SRE team
for a major project that is large enough to justify new headcount, and for which reliability and operational capability have been identified as project risks. Examples might include the creation of a new service or a substantial change in your technology (e.g., migration to a public cloud).
Assembling a horizontal SRE team
In this approach (well documented in
Chapter 27
of our first book), a small team of SREs consults across a number of teams. This team might also establish best practices and tools for configuration management, monitoring, and alerting.
Converting a team in place
You might be able to convert an existing team into an SRE team. The existing team likely isn’t a product development team; typical candidates include an operations team or a team responsible for managing a popular open source component that your organization uses heavily. Be careful to avoid renaming a team from “Operations” to “SRE” without first applying SRE practices and principles! If your rebranding effort fails, your organization may be poisoned against the entire concept of SRE in the future.
Storming
Once assembled, the team needs to start working collaboratively: the team members need to work well with each other, and also with other teams.
You might employ any number of tactics to promote this type of cohesion. At Google, we’ve had success providing a regular forum for learning and discussing SRE practices and reflecting on how the team is performing. For example, you might hold a regular television lunch, where you show a video from SREcon, or a book club, where you all preread some relevant content and then discuss how you can apply it.
During this phase, encourage your new SRE team to stretch themselves. Your new SREs should be comfortable speaking out about SRE practices that don’t fit within your organization, and whether it’s worth making the change so they fit.
Risks and mitigations
During this nascent phase of the SRE journey, there are a number of ways the team might fail. Next we present some risks and possible mitigation strategies, broken down by how the new team formed. You might use one or more of the mitigation strategies for each risk.
New team as part of a major project
Risks
The team:
Spreads itself too thin by taking responsibility for too many services at once.
A team that is constantly firefighting doesn’t have time to address risk in a more permanent way.
Becomes too introspective trying to understand SRE principles and how to implement them. As a result, it underdelivers.
For example, the team might become consumed with developing the perfect SLO definition, neglecting the needs of the service in the meantime.
Doesn’t examine its work thoroughly. As a result, service management reverts to previous behaviors.
The team is paged 100 times a day. Since the pages don’t indicate that immediate intervention is required, they ignore the pages.
Abandons SRE principles and practices in order to meet product milestones.
Reliability improvements to defend the SLO, such as architectural changes, may never be implemented because they set back development timelines.
Gets distracted by conflict with existing teams that perceive a loss of influence or power as a result of the new SRE team.
Does not have the necessary breadth of skills, so delivers only part of the necessary improvements.
Without the ability to, for example, program, SREs may be unable to instrument the product to measure reliability.
Mitigations
The team:
Engages initially on a single important service.
Engages as early as possible on the project, ideally at the design stage.
Has input into the design, with a particular focus on defining SLOs and analyzing reliability risks inherent in the design.
Partners with the product development team and works on features specific to reliability and integration with existing operational platforms.
Is not expected to have operational responsibility on day one. Instead, this responsibility initially sits with the product development team or project team. This may be a significant cultural change that needs support from management.
Has clear agreement on the conditions that a service must meet to be onboarded by SRE (see
Chapter 32
of
Site Reliability Engineering
).
In addition:
If the project involves a migration, the team should have a solid understanding of the current and future environments. If you need to recruit team members externally, consider candidates who have knowledge of software engineering and the future environment.
Continue to keep the number of new hires to less than a third of the team so that the training effort doesn’t overwhelm existing team members.
Horizontal SRE team
Risks
The team is perceived as a new “gating” organization that does no real work or adds no real value.
Mitigations
The team:
Is seeded with respected engineers who have relevant subject matter expertise.
Undertakes project work that focuses on delivering tools (for monitoring, alerting, rollouts, best practices, checklists). These tools should have a short-term beneficial impact on at least two other teams.
Communicates successes and benefits. An SRE team that makes an efficiency breakthrough, automates away toil, or permanently eliminates a source of system unreliability should be celebrated.
Sees themselves as enablers, not gatekeepers. Focus on solutions, not just problems.
A team converted in place
Risks
The team:
Perceives that the conversion process is the start of a slow journey to job losses as automation replaces humans.
Doesn’t support the change to an SRE team.
Has no slack capacity they can leverage to change the team’s day-to-day activities.
Sees no benefit to their day-to-day routine after a few months.
Works with systems that do not support scripting or automation.
Doesn’t have the software engineering skills to automate their current workload.
Doesn’t consistently have the skills needed to evolve toward SRE, or an interest in acquiring the skills.
Mitigations
The team:
Secures senior leadership support for the change.
Renegotiates responsibilities to create the slack needed to effect change.
Manages communication of the change very carefully.
Has access to robust personal and technical support throughout the transition.
Deals with the concern about job losses head on. In a lot of environments, automation eliminates portions of work, but not jobs as a whole; while this might be a step on the path to job losses, it does at least have the virtue of freeing up time to do something better (and more sellable to a future employer) than nonautomated toil.
Can escape operational overload and have more significant impact. If engineers reduce the volume of toil enough to necessitate a smaller team, then their experience should be highly reusable elsewhere in your organization. If their experience can’t be used internally, it should provide an advantage in seeking work elsewhere.
Receives training to acquire the skills SREs need. Your product development team can provide product training, while SRE orientation can make use of this book and other external resources.
Changes how performance is evaluated—the metrics that assess both the team and individuals. The former should be aligned with SLOs and adoption of other SRE practices; the latter should be aligned with evidence of SRE skills.
Adds an experienced SRE or developer to the team.
Has the freedom (budget or time) to identify and introduce new open source or cloud-based monitoring and alerting systems to enable automation. Determining whether the existing systems are sufficient should be an early priority.
Regularly reviews progress internally and with stakeholders.
Norming
Norming entails working past the issues raised in
Risks and mitigations
and reaching broad agreement on best practices for the organization’s SRE teams. Teams need to agree on an acceptable level of toil, appropriate alerting thresholds, and
important and relevant SRE practices
. Teams also need to become self-sufficient at proactively identifying the challenges ahead of the service and setting medium- and long-term goals to improve the service.
Teams should reach the following levels of maturity during the norming phase:
SLOs and error budgets are in place, and the error budget policy is exercised following significant incidents. Leadership is interested in SLO measurements.
On-call rotations are established and sustainable (see
On-Call
). On-call engineers are compensated for their on-call time. There is sufficient tooling, documentation
2
, and training to support any team member during a significant incident.
Toil is documented, bounded, and managed. As a result, SREs complete impactful projects that improve reliability and efficiency.
Postmortem culture is well established. (See
Postmortem Culture: Learning from Failure
.)
The team exhibits most of the tenets listed in
How SRE Relates to DevOps
.
As the team solves initial issues listed in
Storming
, they capture what they learned and prevent repeating problems. The team regularly runs training exercises, such as Wheel of Misfortune or DiRT (Disaster Recovery Testing). (For more information on on-call training, see
Chapter 11
in our first book and
SRE Engagement Model
in this book.)
The product development team benefits from remaining involved in the on-call rotation.
The team produces regular reports (e.g., quarterly) for their stakeholders that cover the highlights, lowlights, and key metrics of the reporting period.
Transforming an Existing Team into an SRE Team
by Brian Balser, New York Times
When the
New York Times
formed its Delivery and Site Reliability Engineering department, we assembled SRE teams  from engineers who had SRE-type skills, such as building tooling and operating production systems. Some teams were “greenfield”: they were designed with SRE in mind with respect to talent, vision, and responsibility. Other teams had existed for several years, and had ended up running production architecture due to a combination of skill sets, interests, and chance.
Challenges
One of the existing teams transitioning into SRE was in a very challenging position. Over the years, the team had gained ownership and responsibility for managing configurations, change requests, and operations of a core component of our site-wide architecture. They effectively became a service team supporting all of our product development teams. Their work was driven by tickets and production issues, and they were in a continuous reactive mode. They didn’t have time to make improvements, innovate, or do other higher-value strategic work.
While the team had many great ideas, it was overloaded with toil and a number of high-priority “blocker” service requests that were typically tied to product launches. This model was not sustainable, and the team would need to grow linearly with products to keep up with this support burden. To exacerbate this situation, the small team had a wealth of institutional knowledge that had accumulated over the years. A high volume of interrupts from teams who needed that information compounded the team’s overload, and a
bus factor
loomed over the team.
Working from First Principles
One guiding principle of our SRE organization is to remove ourselves from the critical path and to empower product development teams with self-service solutions. With that in mind, our goal became clear: invert the responsibility model to enable the product development teams to push their own changes. This strategy would both:
Speed up delivery.
Free SREs from managing configuration churn, allowing them to make real improvements to the system as a whole.
Process Improvement
We improved our processes through several stages of change:
We embedded an SRE in the development team to help relieve pressure.
To enable product development teams to take ownership of their service configuration in isolation, we broke out each service configuration into a team-based repo.
We migrated each service from the legacy CI system to our standard Drone CI/CD pipeline. The developer-friendly workflow was completely driven by GitHub events.
We onboarded each of the product teams to the new tooling and workflow so they could submit their own change requests without being blocked by a service ticket.
While these improvements were a big step forward, we hadn’t yet reached our ideal end state. Reviewing pull requests still often required SRE expertise. To make interrupts for time-consuming reviews more manageable, we scheduled daily office hours. This consistent practice allowed us to batch questions and discussions in a more predictive manner, and also provided a venue for sharing knowledge with teams undergoing onboarding.
End Result and Next Steps
The SRE team is now meeting its initial goal of > 50% project work (versus support-related work). The team still has a wealth of institutional knowledge, but that knowledge is now being propagated more broadly, gradually improving the bus factor and reducing interrupts.
Now that we have breathing room for project work, our next steps are to focus on adding more advanced capabilities such as canary deploys, better test tooling, and observability and resilience features. Doing so will give product development teams more confidence in exercising full autonomy over their service configurations without depending on SREs for change management.
Establishing a healthy relationship with your product development team forms the basis of many of these mitigation strategies. Teams should plan work together per your organization’s planning cycle.
Before moving on to the next step: pause, celebrate this success, and write a retrospective that covers your journey so far.
Performing
The SRE team’s experience with production and work up to this point should have earned the respect and attention of the wider organization, and laid the foundation for strategically moving forward. In the final stage of Tuckman’s performance model, performing, you should expect to:
Partner on all architecture design and change.
From the initial design phase onward, SRE should define the patterns for how software is built and structured for reliability.
Have complete workload self-determination.
Teams should consistently apply Principle 3 with a view toward the holistic health of the system.
Partnering on architecture
The product development team should start to reach out to its partner SRE team for advice on all significant service changes. The SRE team now has the opportunity to have some of its greatest impact.
For example, the SRE team might provide early input into the design of new service architecture to reduce the likelihood of high-cost reengineering at a later date. The product development and SRE teams can acknowledge their differences in perspective on architectural decisions to arrive at a good design process. A successful engagement can add value through:
Improved reliability, scalability, and operability
Better reuse of existing patterns
Simpler migration (if required)
Self-regulating workload
Whereas architectural partnerships should emerge somewhat organically over time, an SRE team must clearly assert Principle #3 to its partners. Doing so requires strong team leadership and clear, upfront commitment from senior management. The ability to regulate its own workload secures the SRE team’s position as an engineering team that works on the organization’s most important services, equal to its product development team peers.
In practice, how an SRE team goes about determining its own workload depends on the teams with which SREs interface. At Google, SRE teams most commonly interact with a distinct product development team. In this case, the relationship has the following characteristics:
An SRE team chooses if and when to onboard a service (see
Chapter 32
of
Site Reliability Engineering
).
In the event of operational overload, the team can reduce toil by:
Reducing the SLO
Transferring operational work to another team (e.g., a product development team)
If it becomes impossible to operate a service at SLO within agreed
toil constraints
, the SRE team can hand back the service to the product development team.
SRE engagement
is not perpetual—it feeds itself by solving problems at scale and improving the reliability of services. If an SRE team has solved all such problems for a service, you need to either:
Intentionally consider what other reliability challenges the SRE team needs to tackle.
Make an intentional decision to hand back the service to the product development team.
Otherwise, your team risks attrition as SREs move on to more interesting opportunities. The slow bleed from attrition can put production at risk.
Not all SRE teams have partner product development teams. Some SRE teams are also responsible for developing the systems they run. Some SRE teams package third-party software, hardware, or services (e.g., open source packages, network equipment, something-as-a-service), and turn those assets into internal services. In this case, you don’t have the option to transfer work back to another team. Instead, consider the following tactics:
If the service does not conform to its SLO, stop feature-related project work in favor of reliability-focused project work.
If it becomes impossible to operate a service at SLO within agreed toil constraints, reduce your SLOs—unless management provides more capacity (people or infrastructure) to deal with the situation.
Making More SRE Teams
Once your first SRE team is up and running, you may want to form an additional SRE team. You might do so for one of the following reasons:
Service complexity
As a service gains users and features, it becomes more complex and harder for a single SRE team to support effectively. You might want to split the team into subteams that specialize in parts of the service.
SRE rollout
If your first SRE team has been successful and made a clear difference, there may be an organizational interest in adopting this approach across more services.
Geographically split
You want to split the team into two halves in different time zones and move to 12-hour on-call shifts.
When you’re creating a new SRE team, we recommend that you do the following:
Read any postmortems written after other teams were established. Identify and repeat what went well and fix and explore alternatives for things that didn’t go well.
Seed the new team with SREs from the existing team—some of your best SREs and highest-potential SREs who can rise to the challenge. In our experience, finding qualified SRE candidates is difficult, so growing a team quickly with new hires often isn’t realistic.
Standardize the framework for establishing teams and onboarding services (see
SRE Engagement Model
).
Make changes to the on-call responsibilities slowly. For example:
To avoid a sudden loss of skilled on-call engineers, keep team members on-call for their previous team’s systems for a transitional period.
After the teams split, wait three to six months to split the on-call rotations.
Service Complexity
Where to split
If a service becomes too complex for a single team to manage, there are a number of ways to split the work. Consider the following options to simplify the cognitive load on team members:
Architectural splits
For example, compute, storage, and network; frontend and backend; frontend and database; client and server; frontend and pipelines.
Language splits
SRE principles are not dependent on programming languages. However, if your SREs are deeply involved in your source code, there may be some benefit in a split along these lines.
Location splits
If your organization’s engineering spans multiple offices, you might want to align SRE team placement with application development.
Pitfalls
When a team splits, sometimes none of the new teams pick up responsibility for a component owned by the original team. To mitigate this risk, you can:
Designate one team as responsible for everything not covered in the second team’s charter.
Appoint a senior SRE to an overarching technical lead role across both teams.
SRE Rollout
If your initial SRE team(s) are successful, your organization may want more of them. We recommend carefully prioritizing the services that receive SRE support. Consider the following points:
Prioritize services for which reliability has a high financial or reputational impact. The higher the impact, the higher the priority.
Define the minimal viable set of services that need to be up in order for the product to function. Prioritize those services and make sure that other services degrade gracefully.
A service should not be a priority for SRE simply because it’s unreliable. SRE should be applied tactically where it is most relevant for the business. You also don’t want to allow your developers to ignore reliability until after SREs are engaged.
Geographical Splits
As described in
Chapter 11
of our first book, Google commonly staffs sister SRE teams on different continents. We do this for a number of reasons:
Service reliability
If a major incident (e.g., natural disaster) prevents one team from operating, the other team can continue to support a service.
On-call stress
Splitting the pager rotation into 12-hour shifts allows proper breaks for on-call engineers.
Recruiting and retaining talent
An on-call shift that overlaps the normal working day broadens the base of engineers that we can recruit into SRE roles, and underlines the engineering part of our role.
Production maturity
Splitting service responsibility across two offices tends to lead to an improvement in maturity as the need for documentation, training, and standardization become more important.
If your organization is lucky enough to already have engineering teams on multiple continents, we recommend staffing multisite SRE teams. It’s possible to have an SRE team in a different office than the development team, but in our experience, colocation provides benefits in the form of a healthy and robust interteam dialog. Otherwise, it’s harder for SREs to understand how the services evolve or how the technical infrastructure is used, and it’s harder for product developers to be optimistic about infrastructure improvements.
Placement: How many time zones apart should the teams be?
Assuming you have some choice, time zone separation is an important consideration in deciding where to locate the two teams. Unfortunately, the objectives are mutually exclusive:
Minimizing the number of hours that on-callers have to work outside of normal office hours
Maximizing the overlap time when both teams are online so that they can interact with each other regularly
The situation is complicated by Daylight Saving Time.
In our experience, staffing teams in time zones that are six to eight hours apart works well and avoids 12 a.m. to 6 a.m. on-call shifts. You can use online resources like
https://www.timeanddate.com/worldclock/meeting.html
to visualize time zone overlaps for various locations.
People and projects: Seeding the team
When you split a team geographically, the first SRE team in a new office will set the norms for future SRE teams. Your likelihood of success will be much higher if you can identify one or more SREs who are willing to relocate from the original site on a temporary or long-term basis to establish SRE practices and recruit and train the new team. The new team should also undertake a high-value project that fosters collaboration within the team and requires interaction with their sister team.
Parity: Distributing Work Between Offices and Avoiding a “Night Shift”
Often, one of two sister SRE teams is colocated (or at least in the same time zone) with the product development team (we’ll call this “Office 1”). If this is the case, be vigilant to ensure that the team that is not colocated (“Office 2”) doesn’t become a night shift that has little contact with the product development team, takes more than its fair share of toil, or is assigned only the less interesting or impactful projects.
The workloads of the two offices will have some natural differences:
Your service likely has a daily peak, and one office will be on-call during that peak. As a result, the on-call experience of the two sites will differ.
Your development process will produce new releases with a particular cadence. One office will likely take more of the burden associated with rollouts and rollbacks.
Office 1 is more likely to be interrupted during their working day by questions from the product development team.
It’s easier for Office 1 to undertake project work associated with major releases. Conversely, it’s easier for Office 2 to undertake project work decoupled from immediate product goals.
You can help maintain balance by using the following practices:
Balance the on-call load between offices. Designate a higher percentage of tickets to the office that fields the lower percentage of pages.
Associate development areas with SRE teams in a particular office. This could be short term (e.g., according to project) or longer term (e.g., according to service). Otherwise, the product development team will likely lean on Office 1, and not effectively engage with SREs in Office 2.
Assign a higher percentage of internal service improvement projects (that are likely to require less involvement with the product development team) to Office 2.
Spread the most interesting and impactful projects fairly between the two offices.
Maintain a similar team size and seniority mix between the two offices.
Split projects across the two sites to deliberately foster interoffice interactions between SREs. While running a major project from a single office might gain some efficiencies, splitting projects across the two sites both helps spread knowledge and builds trust between offices.
Allow engineers to travel to the other office regularly. This enables creating better rapport and, hence, willingness to do work for the other side.
Placement: What about having three shifts?
Our attempts at splitting SRE teams across three sites resulted in various issues:
It is impossible to have an interoffice production meeting that all SREs can attend (see
Chapter 31
of our first book).
It is harder to ensure parity of knowledge, capability, and operational response across three offices.
If all on-call duties take place only during office hours, there’s less of an incentive to automate low-level toil and low-value pages. Being the hero that fixes easy problems is fun during office hours. But if it has some amount of personal cost, the motivation to make sure it never happens again is sharp and immediate.
Timing: Should both halves of the team start at the same time?
You might spin up sister teams using any of the following models:
Both halves start at the same time.
Set up the site that is colocated with the product development team first. This allows SREs to get involved earlier in the product lifecycle.
Set up the site that is
not
colocated with the product development team first or, if a service has been in production for some time, the SRE team and the product development team can share the pager.
Start making changes according to where the right people are at the right time.
Finance: Travel budget
It is very important to create opportunities for high-quality interactions between the two halves of the team. Despite the effectiveness of video conferencing for day-to-day meetings, we’ve found that regular face-to-face interactions go a long way toward facilitating healthy relationships and trust. We recommend that:
Every SRE, product development manager, and technical lead in Site 1 visit Site 2 annually (at a minimum), and vice versa.
Every SRE in a management or technical leadership role at Site 1 visit Site 2 at least twice a year, and vice versa.
All SREs convene at least once a year.
Leadership: Joint ownership of a service
If you have multiple SRE sites, you likely  have decision  makers in each office. These parties should meet regularly face-to-face and by video conference. Only by establishing a strong personal relationship can they:
Debate solutions to challenges that the team faces.
Resolve differences of opinion and agree on a joint path forward.
Advocate on behalf of each other’s team (to prevent an “us versus them” mentality).
Support the health of each other’s team.
Suggested Practices for Running Many Teams
New challenges arise as your organization accumulates more SREs and SRE teams. For example, you’ll have to:
Ensure you provide SREs with the career opportunities they need.
Encourage consistency of practices and tooling.
Deal with services that don’t justify a full SRE engagement.
This section describes a number of the practices that we have adopted at Google to deal with these concerns. Depending on the specifics of your organization, some or many may work for you too.
Mission Control
Google’s
Mission Control
program gives engineers from product development teams the opportunity to spend six months embedded in an SRE team. We typically match these engineers to SRE teams working in a distinctly different area from their expertise. The software engineer is trained in production systems and practices and eventually goes on-call for that service. After six months, some engineers decide to stay in SRE; others return to their old teams with a much better appreciation for the production environment and SRE practices. SRE teams benefit from additional engineering resources and gain valuable insight into gaps and inaccuracies in training material and documentation.
SRE Exchange
Google’s SRE Exchange program lets an SRE spend a week working alongside a different SRE team. The visiting SRE observes how the host team works and shares practices from their home team that might be useful to the host team. At the end of the exchange, the visiting SRE writes a trip report describing their week, their observations, and their recommendations for both teams. This program is useful at Google because our SRE teams are highly specialized.
Training
Training is critical to SRE’s ability to operate systems. While most of this is delivered in-team (see
Training roadmap
in
On-Call
), consider establishing a standard
training curriculum
for all SREs. At Google, all new SREs attend SRE EDU, an immersive weeklong training that introduces key concepts, tooling, and platforms that almost all SREs work with. This provides a baseline level of knowledge across all new SREs, and simplifies
team-specific and service-specific training
objectives. The SRE EDU team also runs a second series of classes a few months later that covers the common tools and processes that we use for managing major incidents. Our performance management process specifically recognizes SREs who facilitate this training.
Horizontal Projects
Because SRE teams are tightly aligned with a set of services, there is a temptation for teams to build proprietary solutions to deal with the challenges they encounter—for example, monitoring, software rollout, and configuration tools. This can lead to significant duplication of efforts across teams. While there is value in allowing a number of solutions to compete for “market” adoption, at some point, it makes sense to converge upon a standard solution that:
Meets most teams’ requirements
Provides a stable and scalable platform upon which the next layer of innovation can be built
Google approaches these efforts by using horizontal teams, which are often staffed by experienced SREs. These horizontal teams build and run a standard solution and partner with other SRE teams to ensure smooth adoption. (For more information on horizontal software development, see
Case Study 2: Common Tooling Adoption in SRE
in
Organizational Change Management in SRE
.)
SRE Mobility
Google does its best to ensure that engineers actively want to be part of their respective teams. To this end, we make sure that SREs are able to (and aware that they’re able to) transfer between teams. Assuming there are no performance issues, SREs are free to transfer to other SRE teams with open headcount. SREs who also passed our hiring bar for software engineer roles are free to transfer to product development teams (see
https://bit.ly/2xyQ4aD
).
This level of mobility is very healthy for individuals and teams for a number of reasons:
Engineers are able to identify and occupy roles of interest.
If personal circumstances change and on-call responsibilities become impractical, SREs can explore opportunities on teams with less demanding on-call duties. They can obtain this information by talking to other teams and reviewing team on-call stats.
SREs who move between teams broaden the experience of the teams they join.
SREs who move between offices help build or maintain cultural consistency between different offices.
SREs are not compelled to work on services that are unhealthy, or for managers who aren’t supportive of their personal development.
This policy also has the side effect of keeping your SRE managers focused on healthy and happy services and teams.
Travel
In addition to the travel required to keep geographically split teams healthy (see the section
Finance: Travel budget
), consider funding for:
Building internal company communities of interest that include SREs from a number of offices. Such groups can largely collaborate via email and video conferencing, but meet face-to-face at least annually.
Attending and presenting at industry-wide SRE and SRE-related conferences to broaden knowledge, learn how other organizations tackle similar problems, and, hopefully, be inspired and energized.
Launch Coordination Engineering Teams
As described in
Chapter 27
of our first book, a Launch Coordination Engineering (LCE) team can apply SRE principles to a broader set of product development teams—teams that build services that don’t require the level of attention that merits SRE engagement. Just like any other SRE team, an LCE team should be actively engaged in automating its daily operations. For example, developing standard tooling and frameworks enable product development teams to design, build, and launch their service in a production environment.
Production Excellence
As the number of SRE teams at your organization grows, a number of best practices will emerge. Every SRE team evolves differently, so evaluating them requires senior SREs with insight into multiple teams.
At Google, we run a regular service review called Production Excellence. On a regular basis, senior SRE leaders review every SRE team, assessing them on a number of standard measures (e.g., pager load, error budget usage, project completion, bug closure rates). The review both applauds outstanding performance and provides suggestions for underperforming teams.
Experienced SREs are equipped to evaluate nuanced scenarios. For example, it can be challenging to tease out a drop in project completion rate caused by a team merger or split versus genuine team performance issues. If a team is at risk of becoming overwhelmed, the reviewers can and should to use their organizational position to support the team's leadership in rectifying the situation.
SRE Funding and Hiring
At Google, we use two practices to make sure that every SRE contributes significant value:
Much of SRE funding comes from the same source as product development team funding. Similar to testing or security, reliability is a core pillar of product development, and is funded as such.
In our experience, the supply of SREs is always smaller than the demand for them. This dynamic ensures that we regularly review and prioritize the services that receive SRE support.
In short, you should have fewer SREs than the organization would like, and only enough SREs to accomplish their specialized work.
At Google, the ratio of SREs to engineers on product development teams ranges from around 1:5 (e.g., low-level infrastructure services) to around 1:50 (e.g., consumer-facing applications with a large number of microservices built using standard frameworks). Many services fall in the middle of this range, at a ratio of around 1:10.
Conclusion
We believe an organization of any size can implement SRE practices by applying the following three principles:
SRE needs SLOs with consequences.
SREs must have time to make tomorrow better than today.
SRE teams have the ability to regulate their workload.
Since Google started talking publicly about SRE, it has grown from Google-specific production practices into a profession practiced in many companies. These principles have often proven true—both over our years of direct experience at scale, and during our more recent experience of working with our customers to adopt SRE practices. Because we’ve seen these practices work both within and outside of Google, we feel these recommendations should prove useful across a range of organizations of different types and sizes.
1
Bruce W. Tuckman, “Developmental Sequence in Small Groups,”
Psychological Bulletin
63, no. 6 (1965): 384–99.
2
Shylaja Nukala and Vivek Rau, “Why SRE Documents Matter,”
ACM Queue
(May–June 2018): forthcoming.
