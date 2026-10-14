---
title: Google SRE - Root Cause Analysis for Probing Incident
source_url: https://sre.google/workbook/incident-response/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/incident-response.html
original_sha256: 11894e848cfccc52f073e998815027e7ea56915ca3e16d53df20eb7d28ab7184
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/incident-response/
ingested: '2026-10-14'
sha256: 542d318348e974287d7153bd2d0499fd2b502a9e903b3cf7e473d7c38c67597f
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Incident Response
By Jennifer Mace, Jelena Oertel, Stephen Thorne,
and Arup Chakrabarti (PagerDuty)
with Jian Ma and Jessie Yang
Everyone wants their services to run smoothly all the time, but we live in an imperfect world in which outages
do
occur. What happens when a not-so-ordinary, urgent problem requires multiple individuals or teams to resolve it? You are suddenly faced with simultaneously managing the incident response and resolving the problem.
Resolving an incident means mitigating the impact and/or restoring the service to its previous condition. Managing an incident means coordinating the efforts of responding teams in an efficient manner and ensuring that communication flows both between the responders and to those interested in the incident’s progress. Many tech companies, including Google, have adopted and adapted best practices for managing incidents from
emergency response
organizations, which have been using these practices for many years.
The basic premise of
incident management
is to respond to an incident in a structured way. Large-scale incidents can be confusing; a structure that teams agree on beforehand can reduce chaos. Formulating rules about how to communicate and coordinate your efforts
before
disaster strikes allows your team to concentrate on resolving an incident when it occurs. If your team has already practiced and familiarized themselves with communication and coordination, they don’t need to worry about these factors during an incident.
Setting up an incident response process doesn’t need to be a daunting task. There are a number of widely available resources that can provide some guidance, such as
Managing Incidents
in the first SRE Book. The basic principles of incident response include the following:
Maintain a clear line of command.
Designate clearly defined roles.
Keep a working record of debugging and mitigation as you go.
Declare incidents early and often.
This chapter shows how incident management is set up at Google and PagerDuty, and gives examples of where we got this process right and where we didn’t. The simple checklist in
Putting Best Practices into Practice
can help you get started on creating your own incident response practice, if you don’t already have one.
Incident Management at Google
Incident response provides a system for responding to and managing an incident. A framework and set of defined procedures allow a team to respond to an incident effectively and scale up their response. Google’s incident response system is based on the
Incident Command System (ICS)
.
Incident Command System
ICS was established in 1968 by firefighters as a way to manage wildfires. This framework provides standardized ways to communicate and fill clearly specified roles during an incident. Based upon the success of the model, companies later adapted ICS to respond to computer and system failures. This chapter explores two such frameworks:
PagerDuty’s Incident Response process
and Incident Management At Google (
IMAG
).
Incident response frameworks have three common goals, also known as the “three Cs” (3Cs) of incident management:
Coordinate
response effort.
Communicate
between incident responders, within the organization, and to the outside world.
Maintain
control
over the incident response.
When something goes wrong with incident response, the culprit is likely in one of these areas. Mastering the 3Cs is essential for effective incident response.
Main Roles in Incident Response
The main roles in incident response are the Incident Commander (IC), Communications Lead (CL), and Operations or Ops Lead (OL). IMAG organizes these roles into a hierarchy: the IC leads the incident response, and the CL and OL report to the IC.
When disaster strikes, the person who declares the incident typically steps into the IC role and directs the high-level state of the incident. The IC concentrates on the 3Cs and does the following:
Commands and
coordinates
the incident response, delegating roles as needed. By default, the IC assumes all roles that have not been delegated yet.
Communicates
effectively.
Stays in
control
of the incident response.
Works with other responders to resolve the incident.
The IC may either hand off their role to someone else and assume the OL role, or assign the OL role to someone else. The OL works to respond to the incident by applying operational tools to mitigate or resolve the incident.
While the IC and OL work on mitigating and resolving the incident, the CL is the public face of the
incident response team
. The CL’s main duties include providing periodic updates to the incident response team and stakeholders, and managing inquiries about the incident.
Both the CL and OL may lead a team of people to help manage their specific areas of incident response. These teams can expand or contract as needed. If the incident becomes small enough, the CL role can be subsumed back into the IC role.
Case Studies
The following four large-scale incidents illustrate how incident response works in practice. Three of these case studies are from Google, and the last is a case study from PagerDuty, which provides perspective on how other organizations use ICS-derived frameworks. The Google examples start with an incident that wasn’t managed effectively, and progress to incidents that were managed well.
Case Study 1: Software Bug—The Lights Are On but No One’s (Google) Home
This example shows how failing to declare an incident early on can leave a team without the tools to respond to an incident quickly and efficiently. While this incident was resolved without major calamity, early escalation would have produced a quicker, more organized response, and a better outcome.
Context
Google Home is a smart speaker and home assistant that responds to voice commands. The voice commands interact with Google Home’s software, which is called Google Assistant.
Interacting with Google Home starts when a user says a
hotword
, a given phrase that triggers Google Assistant. Multiple users can use the same Google Home device by training the assistant to listen for a given hotword. The hotword model that identifies speakers is trained on the client, but the training data (i.e., the speaker recognition files) is stored on the server. The server handles bidirectional streaming of data. To handle overload during busy times, the server has a quota policy for Google Assistant. In order to protect servers from overly large request values, the quota limit is significantly higher than the baseline usage for Google Assistant on a given device.
A bug in Google Assistant version 1.88 caused speaker recognition files to be fetched 50 times more often than expected, exceeding this quota. Initially, Google Home users in the central United States experienced only small traffic losses. As the rollout increased progressively to all Google Home devices, however, users lost half of their requests during the weekend of June 3, 2017.
Incident
At 11:48 a.m. PST on Monday, May 22, Jasper, the developer on-call for Google Home, happened to be looking at the queries per second (QPS) graphs and noticed something strange: Google Assistant had been pinging training data every 30 minutes, instead of once per day as expected. He stopped the release of version 1.88, which had rolled out to 25% of users. He raised a bug—let’s call it bug 12345—with Google’s bug tracking system to explore why this was happening. On the bug, he noted that Google Assistant was pinging data 48 times a day, causing it to exceed its QPS capacity.
Another developer, Melinda, linked the issue to a previously reported bug, which we’ll call bug 67890: any time an app refreshed the device authentication and enrollment state, the speech processor restarted. This bug was slated to be fixed after the version 1.88 release, so the team requested a temporary increase in quota for the model to mitigate the overload from extra queries.
The version 1.88 release was started again and continued to roll out, reaching 50% of users by Wednesday, May 31. Unfortunately, the team later learned that bug 67890, while responsible for some extra traffic, was not the actual root cause of the more frequent fetches that Jasper had noticed.
That same morning, customers started reporting an issue to Google’s support team: any time someone said “OK Google” (or any other hotword to activate Google Home), the device responded with an error message. This issue prevented users from giving commands to Google Assistant. The team began to investigate what could be causing the errors that users reported. They suspected quota issues, so they requested another increase to the quota, which seemed to mitigate the problem.
Meanwhile, the team continued to investigate bug 12345 to see what was triggering the errors. Although the quota connection was established early in the debugging process, miscommunication between the client and server developers had led developers down the wrong path during troubleshooting, and the full solution remained out of reach.
The team also puzzled over why Google Assistant’s traffic kept hitting quota limits. The client and server developers were confused by client-side errors that didn’t seem to be triggered by any problems on the server side. The developers added logging to the next release to help the team understand the errors better, and hopefully make progress in resolving the incident.
By Thursday, June 1, users reported that the issue had been resolved. No new issues were reported, so the version 1.88 release continued to roll out. However, the root cause of the original issue had not yet been identified.
By early Saturday morning, June 3, the version 1.88 release rollout surpassed 50%. The rollout was happening on a weekend, when developers were not readily available. The team had not followed the best practice of performing rollouts only during business days to ensure developers are around in case something goes wrong.
When the version 1.88 release rollout reached 100% on Saturday, June 3, the client once more hit server limits for Google Assistant traffic. New reports from customers started coming in. Google employees reported that their Google Home devices were throwing errors. The Google Home support team received numerous customer phone calls, tweets, and Reddit posts about the issue, and Google Home’s help forum displayed
a growing thread
discussing the issue. Despite all the user reports and feedback, the bug wasn’t escalated to a higher priority.
On Sunday, June 4, as the number of customer reports continued to increase, the support team finally raised the bug priority to the highest level. The team did not declare an incident, but continued to troubleshoot the issue via “normal” methods, using the bug tracking system for communication. The on-call developer noticed error rates in one of the datacenter clusters and pinged SRE, asking them to drain it. At the same time, the team submitted another request for a quota increase. Afterward, an engineer on the developer team noticed the drain had pushed errors into other cells, which provided additional evidence of quota issues. At 3:33 p.m., the developer team manager increased the quota for Google Assistant once again, and the impact on users stopped. The incident was over. The team identified the root cause (see the previous “Context” section) shortly thereafter.
Review
Some aspects of incident handling went really well, while others had room for improvement.
First, the developers rallied on the weekend and provided valuable input to resolve the issue. This was both good and bad. While the team valued the time and effort these individuals contributed over the weekend, successful incident management shouldn’t rely on heroic efforts of individuals. What if the developers had been unreachable? At the end of the day, Google supports a good work-life balance—engineers shouldn’t be tapped during their free time to fix work-related problems. Instead, we should have conducted rollouts during business hours or organized an on-call rotation that provided paid coverage outside of business hours.
Next, the team worked to mitigate the issue. Google always aims to first stop the impact of an incident, and then find the root cause (unless the root cause just happens to be identified early on). Once the issue is mitigated, it’s just as important to understand the root cause in order to prevent the issue from happening again. In this case, mitigation successfully stopped the impact on three separate occasions, but the team could only prevent the issue from recurring when they discovered the root cause. After the first mitigation, it would have been better to postpone the rollout until the root cause was fully determined, avoiding the major disruption that happened over the weekend.
Finally, the team did not declare an incident when problems first appeared. Our experience shows that managed incidents are resolved faster. Declaring an incident early ensures that:
Miscommunication between the client and server developers is prevented.
Root-cause identification and incident resolution occur sooner.
Relevant teams are looped in earlier, making external communications faster and smoother.
Centralized communication is an important principle of the IMAG protocol. For example, when disaster strikes, SREs typically gather in a “war room.” The war room can be a physical location like a conference room, or it can be virtual: teams might gather on an IRC channel or Hangout. The key here is to gather all the incident responders in one place and to communicate in real time to manage—and ultimately resolve—an incident.
Case Study 2: Service Fault—Cache Me If You Can
The following incident illustrates what happens when a team of experts tries to debug a system with so many interactions that no single person can grasp
all
the details. Sound familiar?
Context
Kubernetes is an open source container management system built collaboratively by many companies and individual contributors. Google Kubernetes Engine, or GKE, is a Google-managed system that creates, hosts, and runs Kubernetes clusters for users. This hosted version operates the control plane, while users upload and manage workloads in the way that suits them best.
When a user first creates a new cluster, GKE fetches and initializes the Docker images their cluster requires. Ideally, these components are fetched and built internally so we can validate them. But because Kubernetes is an open source system, new dependencies sometimes slip in through the cracks.
Incident
One Thursday at 6:41 a.m. PST, London’s on-call SRE for GKE, Zara, was paged for CreateCluster prober failures across several zones. No new clusters were being successfully created. Zara checked the prober dashboard and saw that failures were above 60% for two zones. She verified this issue was affecting user attempts to create new clusters, though traffic to existing clusters was not affected. Zara followed GKE’s documented procedure and declared an incident at 7:06 a.m.
Initially, four people were involved in the incident:
Zara, who first noticed the problem, and was therefore the designated default Incident Commander
Two of Zara’s teammates
Rohit, the customer support engineer paged by the incident procedure
Since Rohit was based in Zurich, Zara (the IC) opened a GKE Panic IRC channel where the team could debug together. While the other two SREs dug into monitoring and error messages, Zara explained the outage and its impact to Rohit. By 7:24 a.m., Rohit posted a notice to users that CreateCluster was failing in the Europe-West region. This was turning into a large incident.
Between 7 a.m. and 8:20 a.m., Zara, Rohit, and the others worked on troubleshooting the issue. They examined cluster startup logs, which revealed an error:
error: failed to run Kubelet: cannot create certificate signing request: Post
https://192.0.2.53/apis/certificates.k8s.io/v1beta1/certificatesigningrequests
They needed to determine which part of the certificate creation failed. The SREs investigated the network, resource availability, and the certificate signing process. All seemed to work fine separately. At 8:22 a.m., Zara posted a summary of the investigation to the incident management system, and looked for a developer who could help her.
Thankfully, GKE had a developer on-call who could be paged for emergencies. The developer, Victoria, joined the channel. She asked for a tracking bug and requested that the team escalate the issue to the infrastructure on-call team.
It was now 8:45 a.m. The first Seattle SRE, Il-Seong, arrived at the office, lightly caffeinated and ready for the day. Il-Seong was a senior SRE with many years of experience in incident response. When he was informed about the ongoing incident, he jumped in to help. First, Il-Seong checked the day’s release against the timing of the alerts, and determined that the day’s release did not cause the incident. He then started a working document
1
to collect notes. He suggested that Zara escalate the incident to the infrastructure, cloud networking, and compute engine teams to possibly eliminate those areas as root causes. As a result of Zara’s escalation, additional people joined the incident response:
The developer lead for GKE nodes
Cloud Networking on-call
Compute Engine on-call
Herais, another Seattle SRE
At 9:10 a.m., the incident channel had a dozen participants. The incident was 2.5 hours old, with no root cause and no mitigation. Communication was becoming a challenge. Normally, on-call handover from London to Seattle occurred at 10 a.m., but Zara decided to hand over incident command to Il-Seong before 10 a.m., since he had more experience with IMAG.
As Incident Commander, Il-Seong set up a formal structure to address the incident. He then designated Zara as Ops Lead and Herais as Communications (Comms) Lead. Rohit remained the External Communications Lead. Herais immediately sent an “all hands on deck” email to several GKE lists, including all developer leads, and asked experts to join the incident response.
So far, the incident responders knew the following:
Cluster creation failed where nodes attempted to register with the master.
The error message indicated the certificate signing module as the culprit.
All cluster creation in Europe was failing; all other continents were fine.
No other GCP services in Europe were seeing network or quota problems.
Thanks to the call for all hands on deck, Puanani, a GKE Security team member, joined the effort. She noticed the certificate signer was not starting. The certificate signer was trying to pull an image from DockerHub, and the image appeared to be corrupted. Victoria (the on-call GKE developer) ran Docker’s
pull
command for the image in two geographic locations. It failed when it ran on a cluster in Europe and succeeded on a cluster in the US. This indicated that the European cluster was the problem. At 9:56 a.m., the team had identified a plausible root cause.
Because DockerHub was an external dependency, mitigation and root causing would be especially challenging. The first option for mitigation was for someone at Docker to quickly fix the image. The second option was to reconfigure the clusters to fetch the image from a different location, such as Google Container Registry (GCR), Google’s secure image hosting system. All the other dependencies, including other references to the image, were located in GCR.
Il-Seong assigned owners to pursue both options. He then delegated a team to investigate fixing the broken cluster. Discussion became too dense for IRC, so detailed debugging moved to the shared document, and IRC became the hub for decision making.
For the second option, pushing a new configuration meant rebuilding binaries, which took about an hour. At 10:59 a.m., when the team was 90% done rebuilding, they discovered another location that was using the bad image fetch path. In response, they had to restart the build.
While the engineers on IRC worked on the two mitigation options, Tugay, an SRE, had an idea. Instead of rebuilding the configuration and pushing it out (a cumbersome and risky process), what if they intercepted Docker’s
pull
requests and substituted the response from Docker with an internal cached image? GCR had a mirror for doing precisely this. Tugay reached out to contacts on GCR’s SRE team, and they confirmed that the team could set
--registry-mirror=
https://mirror.gcr.io
on the Docker configuration. Tugay started setting up this functionality and discovered that
the mirror was already in place!
At 11:29 a.m., Tugay reported to IRC that these images were being pulled
from the GCR mirror, not DockerHub
. At 11:37 a.m., the Incident Commander paged GCR on-call. At 11:59 a.m., GCR on-call purged the corrupt image from their European storage layer. By 12:11 p.m., all European zones had fallen to 0% error.
The outage was over. All that remained was cleanup, and writing a truly epic postmortem.
CreateCluster had failed in Europe for 6 hours and 40 minutes before it was fixed. In IRC, 41 unique users appeared throughout the incident, and IRC logs stretched to 26,000 words. The effort spun up seven IMAG task forces at various times, and as many as four worked simultaneously at any given time. On-calls were summoned from six teams, not including those from the “all hands on deck” call. The postmortem contained 28 action items.
Review
The GKE CreateCluster outage was a large incident by anyone’s standards. Let’s explore what went well, and what could have been handled better.
What went well?
The team had several documented escalation paths and was familiar with incident response tactics. Zara, the GKE on-call, quickly verified that the impact was affecting actual customers. She then used an incident management system prepared beforehand to bring in Rohit, who communicated the outage to customers.
What could have been handled better?
The service itself had some areas of concern. Complexity and dependence on specialists were problematic. Logging was insufficient for diagnosis, and the team was distracted by the corruption on DockerHub, which was not the real issue.
At the beginning of the incident, the Incident Commander didn’t put a formal incident response structure in place. While Zara assumed this role and moved the conversation to IRC, she could have been much more proactive in coordinating information and making decisions. As a result, a handful of first responders pursued their own investigations without coordination. Il-Seong put a formal incident response structure in place two hours after the first page.
Finally, the incident revealed a gap in GKE’s disaster readiness: the service didn’t have any early generic mitigations that would reduce user pain.
Generic mitigations
are actions that first responders take to alleviate pain, even before the root cause is fully understood. For example, responders could roll back a recent release when an outage is correlated with the release cycle, or reconfigure load balancers to avoid a region when errors are localized. It’s important to note that generic mitigations are blunt instruments and may cause other disruptions to the service. However, while they may have broader impact than a precise solution, they can be put in place quickly to stop the bleeding while the team discovers and addresses the root cause.
Let’s look at the timeline of this incident again to see where a generic mitigation might have been effective:
7 a.m. (Assessed impact).
Zara confirmed that users were affected by the outage.
9:56 a.m. (Found possible cause).
Puanani and Victoria identified a rogue image.
10:59 a.m. (Bespoke mitigation).
Several team members worked on rebuilding binaries to push a new configuration that would fetch images from a different location.
11:59 a.m. (Found root cause and fixed the issue).
Tugay and GCR on-call disabled GCR caching and purged a corrupt image from their European storage layer.
A generic mitigation after step 2 (found possible cause) would have been very useful here. If the responders had rolled back all images to a known good state once they discovered the issue’s general location, the incident would have been mitigated by 10 a.m. To mitigate an incident, you don’t have to fully understand the details—you only need to know the location of the root cause. Having the ability to mitigate an outage before its cause is fully understood is crucial for running robust services with high availability.
In this case, the responders would have benefited from some sort of tool that facilitated rollbacks. Mitigation tools do take engineering time to develop. The right time to create general-purpose mitigation tools is before an incident occurs, not when you are responding to an emergency. Browsing postmortems is a great way to discover mitigations and/or tools that would have been useful in retrospect, and build them into services so that you can better manage incidents in the future.
It’s important to remember that first responders must
prioritize mitigation above all else
, or time to resolution suffers. Having a generic mitigation in place, such as rollback and drain, speeds recovery and leads to happier customers. Ultimately, customers do not care whether or not you fully understand what caused an outage. What they want is to stop receiving errors.
With mitigation as top priority, an active incident should be addressed as follows:
Assess the impact of the incident.
Mitigate the impact.
Perform a root-cause analysis of the incident.
After the incident is over, fix what caused the incident and write a postmortem.
Afterward, you can run incident response drills to exercise the vulnerabilities in the system, and engineers can work on projects to address these vulnerabilities.
Case Study 3: Power Outage—Lightning Never Strikes Twice…Until It Does
The previous examples showed what can go wrong when you don’t have good incident response strategies in place. The next example illustrates an incident that was successfully managed. When you follow a well-defined and clear response protocol, you can handle even rare or unusual incidents with ease.
Context
Power grid events, such as lightning strikes, cause the power coming into a datacenter facility to vary wildly. Lightning strikes affecting the power grid are rare, but not unexpected. Google protects against sudden, unexpected power outages with backup generators and batteries, which are well tested and known to work in these scenarios.
Many of Google’s servers have a large number of disks attached to them, with the disks located on a separate tray above or below the server. These trays have their own uninterruptible power supply (UPS) battery. When a power outage occurs, the backup generators activate but take a few minutes to start. During this period, the backup batteries attached to the servers and disk trays provide power until the backup generators are fully running, thereby preventing power grid events from impacting datacenter operation.
Incident
In mid-2015, lightning struck the power grid near a Google datacenter in Belgium four times within two minutes. The datacenter’s backup generators activated to supply power to all the machines. While the backup generators were starting up, most of the servers ran on backup batteries for a few minutes.
The UPS batteries in the disk trays did not swap power usage to the backup batteries on the third and fourth lightning strikes because the strikes were too closely spaced. As a result, the disk trays lost power until the backup generators kicked in. The servers did not lose power, but were unable to access the disks that had power cycled.
Losing a large number of disk trays on persistent disk storage resulted in read and write errors for many virtual machine (VM) instances running on Google Compute Engine (GCE). The Persistent Disk SRE on-call was immediately notified of these errors. Once the Persistent Disk SRE team established the impact, a major incident was declared and announced to all affected parties. The Persistent Disk SRE on-call assumed the role of Incident Commander.
After an initial investigation and communication between stakeholders, we established that:
Each machine that lost a disk tray because of the temporary power outage needed to be rebooted.
While waiting for the reboot, some customer VMs had trouble reading and writing to their disks.
Any host that had both a disk tray and customer VMs could not simply be “rebooted” without losing the customer VMs that hadn’t been affected. Persistent Disk SRE asked GCE SRE to migrate unaffected VMs to other hosts.
The Persistent Disk SRE’s primary on-call retained the IC role, since that team had the best visibility into customer impact.
Operations team members were tasked with the following objectives:
Safely restore power to use grid power instead of backup generators.
Restart all machines that were not hosting VMs.
Coordinate between Persistent Disk SRE and GCE SRE to safely move VMs away from the affected machines before restarting them.
The first two objectives were clearly defined, well understood, and documented. The datacenter ops on-call immediately started working to safely restore power, providing regular status reports to the IC. Persistent Disk SRE had defined procedures for restarting all machines not hosting virtual machines. A team member began restarting those machines.
The third objective was more vague and wasn’t covered by any existing procedures. The Incident Commander assigned a dedicated operations team member to coordinate with GCE SRE and Persistent Disk SRE. These teams collaborated to safely move VMs away from the affected machines so the affected machines could be rebooted. The IC closely monitored their progress and realized that this work called for new tools to be written quickly. The IC organized more engineers to report to the operations team so they could create the necessary tools.
The Communications Lead observed and asked questions about all incident-related activities, and was responsible for reporting accurate information to multiple audiences:
Company leaders needed information about the extent of the problem, and assurance that the problem was being addressed.
Teams with storage concerns needed to know when their storage would be fully available again.
External customers needed to be proactively informed about the problem with their disks in this cloud region.
Specific customers who had filed support tickets needed more information about the problems they were seeing, and advice on workarounds and timelines.
After we mitigated the initial customer impact, we needed to do some follow-up, such as:
Diagnosing why the UPS used by the disk trays failed, and making sure that it doesn’t happen again.
Replacing the batteries in the datacenter that failed.
Manually clearing “stuck” operations caused by losing so many storage systems simultaneously.
Post-incident analysis revealed that only a small number of writes—the writes pending on the machines that lost power during the incident—weren’t ever written to disk. Since Persistent Disk snapshots and all Cloud Storage data are stored in multiple datacenters for redundancy, only 0.000001% of data from running GCE machines was lost, and only data from running instances was at risk.
Review
By declaring the incident early and organizing a response with clear leadership, a carefully managed group of people handled this complex incident effectively.
The Incident Commander delegated the normal problems of restoring power and rebooting servers to the appropriate Operations Lead. Engineers worked on fixing the issue and reported their progress back to the Operations Lead.
The more complex problem of meeting the needs of both GCE and Persistent Disk required coordinated decision making and interaction among multiple teams. The Incident Commander made sure to assign appropriate operations team members from both teams to the incident, and worked directly with them to drive toward a solution. The Incident Commander wisely focused on the most important aspect of the incident: addressing the needs of the impacted customers as quickly as possible.
Case Study 4: Incident Response at PagerDuty
by Arup Chakrabarti of PagerDuty
PagerDuty has developed and refined our internal incident response practices over the course of several years. Initially, we staffed a permanent, company-wide Incident Commander and dedicated specific engineers per service to take part in incident response. As PagerDuty grew to over 400 employees and dozens of engineering teams, our Incident Response processes also changed. Every few months, we take a hard look at our processes, and update them to reflect business needs. Nearly everything we have learned is documented at
https://response.pagerduty.com.
Our Incident Response processes are purposefully not static; they change and evolve just as our business does.
Major incident response at PagerDuty
Typically, small incidents require only a single on-call engineer to respond. When it comes to larger incidents, we place heavy emphasis on teamwork. An engineer shouldn’t feel alone in high-stress and high-impact scenarios. We use the following techniques to help promote teamwork:
Participating in simulation exercises
One way we teach teamwork is by participating in
Failure Friday
. PagerDuty drew inspiration from
Netflix’s Simian Army
to create this program. Originally, Failure Friday was a manual failure injection exercise aimed at learning more about the ways our systems could break. Today, we also use this weekly exercise to recreate common problems in production and incident response scenarios.
Before Failure Friday starts, we nominate an Incident Commander (typically, a person training to become an IC). They are expected to behave and act like a real IC while conducting failure injection exercises. Throughout the drill, subject-matter experts use the same processes and vernacular they would use during an actual incident. This practice both familiarizes new on-call engineers with incident response language and processes and provides more seasoned on-call engineers with a refresher.
Playing time-bound simulation games
While Failure Friday exercises go a long way toward training engineers on different roles and processes, they can’t fully replicate the urgency of actual major incidents. We use simulation games with a time-bound urgency to capture that aspect of incident response.
“Keep Talking and Nobody Explodes”
is one game we’ve leveraged heavily. It requires players to work together to defuse bombs within time limits. The stressful and communication-intensive nature of the game forces players to cooperate and work together effectively.
Learning from previous incidents
Learning from previous incidents helps us respond better to major incidents in the future. To this end, we conduct and regularly review postmortems.
PagerDuty’s postmortem process involves open meetings and thorough documentation. By making this information easily accessible and discoverable, we aim to reduce the resolution time of future incidents, or prevent a future incident from happening altogether.
We also record all of the phone calls involved in a major incident so we can learn from the real-time communication feed.
Let’s look at a recent incident in which PagerDuty had to leverage our incident response process. The incident occurred on October 6, 2017, and lasted more than 10 hours, but had very minimal customer impact.
7:53 p.m.
A member of the PagerDuty SRE team was alerted that PagerDuty internal NTP servers were exhibiting clock drift. The on-call SRE validated that all automated recovery actions had been executed, and completed the mitigation steps in relevant runbooks. This work was documented in the SRE team’s dedicated Slack channel.
8:20 p.m.
A member of PagerDuty Software Team A received an automated alert about clock drift errors in their services. Software Team A and the SRE team worked toward resolving the problem.
9:17 p.m.
A member of PagerDuty Software Team B received an automated alert about clock drift errors on their services. The engineer from Team B joined the Slack channel where the issue was already being triaged and debugged.
9:49 p.m.
The SRE on-call declared a major incident and alerted the Incident Commander on-call.
9:55 p.m.
The IC assembled the response team, which included every on-call engineer that had a service dependent on NTP, and PagerDuty’s customer support on-call. The IC had the response team join the dedicated conference call and Slack channel.
For the next eight hours, the response team worked on addressing and mitigating the issue. When the procedures in our runbooks didn’t resolve the issue, the response team started trying new recovery options in a methodical manner.
During this time, we rotated on-call engineers and the IC every four hours. Doing so encouraged engineers to get rest and brought new ideas into the response team.
5:33 a.m.
The on-call SRE made a configuration change to the NTP servers.
6:13 a.m.
The IC validated that all services had recovered with their respective on-call engineers. Once validation was complete, the IC shut off the conference call and Slack channel and declared the incident complete. Given the wide impact of the NTP service, a postmortem was warranted. Before closing out the incident, the IC assigned the
postmortem analysis
to the SRE team on-call for the service.
Tools used for incident response
Our Incident Response processes leverage three main tools:
PagerDuty
We store all of our on-call information, service ownership, postmortems, incident metadata, and the like, in PagerDuty. This allows us to rapidly assemble the right team when something goes wrong.
Slack
We maintain a dedicated channel (#incident-war-room) as a gathering place for all subject-matter experts and Incident Commanders. The channel is used mostly as an information ledger for the scribe, who captures actions, owners, and timestamps.
Conference calls
When asked to join any incident response, on-call engineers are required to dial in to a static conference call number. We prefer that all coordination decisions are made in the conference call, and that decision outcomes are recorded in Slack. We found this was the fastest way to make decisions. We also record every call to make sure that we can recreate any timeline in case the scribe misses important details.
While Slack and conference calls are our communication channels of choice, you should use the communication method that works best for your company and its engineers.
At PagerDuty, how we handle incident response relates directly to the success of the company. Rather than facing such events unprepared, we purposefully prepare for incidents by conducting simulation exercises, reviewing previous incidents, and choosing the right tools to help us be resilient to any major incident that may come our way.
Putting Best Practices into Practice
We’ve seen examples of incidents that were handled well, and some that were not. By the time a pager alerts you to a problem, it’s too late to think about how to manage the incident. The time to start thinking about an incident management process is
before
an incident occurs. So how do you prepare and put theory into practice before disaster strikes? This section provides some recommendations.
Incident Response Training
We highly recommend training responders to organize an incident so they have a pattern to follow in a real emergency. Knowing how to organize an incident, having a common language to use throughout the incident, and sharing the same expectations reduce the chance of miscommunication.
The full Incident Command System approach may be more than you need, but you can develop a framework for handling incidents by selecting the parts of the incident management process that are important to your organization. For example:
Let on-calls know they can delegate and escalate during an incident.
Encourage a mitigation-first response.
Define Incident Commander, Communications Lead, and Operations Lead roles.
You can adapt and summarize your incident response framework, and create a slide deck to present to new team members. We’ve learned that people are more receptive to
incident response training
when they can connect the theory of incident response to actual scenarios and concrete actions. Therefore, be sure to include hands-on exercises and share what happened in past incidents, analyzing what went well and what didn’t go so well. You might also consider using external agencies that specialize in incident response classes and training.
Prepare Beforehand
In addition to incident response training, it helps to prepare for an incident beforehand. Use the following tips and strategies to be better prepared.
Decide on a communication channel
Decide and agree on a communication channel (Slack, a phone bridge, IRC, HipChat, etc.) beforehand—no Incident Commander wants to make this decision during an incident. Practice using it so there are no surprises. If possible, pick a communications channel the team is already familiar with so that everyone on the team feels comfortable using it.
Keep your audience informed
Unless you acknowledge that an incident is happening and actively being addressed, people will automatically assume nothing is being done to resolve the issue. Similarly, if you forget to call off the response once the issue has been mitigated or resolved, people will assume the incident is ongoing. You can preempt this dynamic by keeping your audience informed throughout the incident with regular status updates. Having a prepared list of contacts (see the next tip) saves valuable time and ensures you don’t miss anyone.
Think ahead about how you’ll draft, review, approve, and release public blog posts or press releases. At Google, teams seek guidance from the PR team. Also, prepare two or three ready-to-use templates for sharing information, making sure the on-call knows how to send them. No one wants to write these announcements under extreme stress with no guidelines. The templates make sharing information with the public easy and minimally stressful.
Prepare a list of contacts
Having a list of people to email or page prepared beforehand saves critical time and effort. In
Case Study 2: Service Fault—Cache Me If You Can
, the Comms Lead made an “all hands on deck” call by sending an email to several GKE lists that were prepared beforehand.
Establish criteria for an incident
Sometimes it’s clear that a paging issue is truly an incident. Other times, it’s not so clear. It’s helpful to have an established list of criteria for determining if an issue is indeed an incident. A team can come up with a solid list of criteria by looking at past outages, taking known high-risk areas into consideration.
In summary, it’s important to establish common ground for coordination and communication when responding to incidents. Decide on ways to communicate the incident, who your audience is, and who is responsible for what during an incident. These guidelines are easy to set up and have high impact on shortening the resolution time of an incident.
Drills
The final step in the incident management process is practicing your incident management skills. By practicing during less critical situations, your team develops good habits and patterns of behavior for when lightning strikes—figuratively and literally. After introducing the theory of incident response through training, practice ensures that your incident response skills stay fresh.
There are several ways to conduct incident management drills. Google runs company-wide resilience testing (called Disaster Recovery Testing, or DiRT; see Kripa Krishnan’s article “Weathering the Unexpected”
2
), in which we create a controlled emergency that doesn’t actually impact customers. Teams respond to the controlled emergency as if it were a real emergency. Afterward, the teams review the emergency response procedures and discuss what happened. Accepting failure as a means of learning, finding value in gaps identified, and getting our leadership on board were key to successfully establishing the DiRT program at Google. On a smaller scale, we practice responding to specific incidents using exercises like Wheel of Misfortune (see
“Disaster Role Playing”
in
Site Reliability Engineering
).
You can also practice incident response by intentionally treating minor problems as major ones requiring a large-scale response. This lets your team practice with the procedures and tools in a real-world situation with lower stakes.
Drills are a friendly way of trying out new incident response skills. Anyone on your team who could get swept into incident response—SREs, developers, and even customer support and marketing partners—should feel comfortable with these tactics.
To stage a drill, you can invent an outage and allow your team to respond to the incident. You can also create outages from postmortems, which contain plenty of ideas for incident management drills. Use real tools as much as possible to manage the incident. Consider breaking your test environment so the team can perform real troubleshooting using existing tools.
All these drills are far more useful if they’re run periodically. You can make drills impactful by following up each exercise with a report detailing what went well, what didn’t go well, and how things could have been handled better. The most valuable part of running a drill is examining their outcomes, which can reveal a lot about any gaps in incident management. Once you know what they are, you can work toward closing them.
Conclusion
Be prepared for when disaster strikes. If your team practices and refreshes your incident response procedures regularly, you won’t panic when the inevitable outage occurs.
The circle of people you need to collaborate with during an incident expands with the size of the incident. When you’re working with people you don’t know, procedures help create the structure you need to quickly move toward a resolution. We strongly recommend establishing these procedures ahead of time when the world is
not
on fire. Regularly review and iterate on your incident management plans and playbooks.
The Incident Command System is a simple concept that is easily understood. It scales up or down according to the size of the company and the incident. Although it’s simple to understand, it isn’t easy to implement, especially in the middle of an incident when panic suddenly overtakes you. Staying calm and following the response structure during an emergency takes practice, and practice builds “muscle memory.” This gives you the confidence you’ll need for a real emergency.
We strongly recommend carving out some time in your team’s busy schedule to practice incident management on a regular basis. Secure support from leadership for dedicated practice time, and make sure they understand how incident response works in case you need to involve them in a real incident. Disaster preparedness can shave off valuable minutes or hours from response time and gives you a competitive edge. No company gets it right all the time—learn from your mistakes, move on, and do better the next time.
1
When three or more people work on an incident, it’s useful to start a collaborative document that lists working theories, eliminated causes, and useful debugging information, such as error logs and suspect graphs. The document preserves this information so it doesn’t get lost in the conversation.
2
Kripa Krishan, “Weathering the Unexpected,”
Communications of the ACM
10, no. 9 (2012),
https://queue.acm.org/detail.cfm?id=2371516
.
