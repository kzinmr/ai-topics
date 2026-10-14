---
title: Google SRE - Site Reliability Engineering Book Index
source_url: https://sre.google/workbook/index/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/index.html
original_sha256: cce11c7869a0c267200b7c01de47445b99950ca8c5d32f5a0e4bbfc13aa41d3d
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/index/
ingested: '2026-10-14'
sha256: 008d142ead1d0d4562a4a3dcc8b89114765353ef137ee2d379090e04dafc9579
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Index
A
abandoned phase (service lifecycle), SRE engagement in,
Phase 6: Abandoned
Abuse SRE and Common Abuse Tool (CAT) teams, Ares case study,
Case Study 1: Ares
access control policies for data processing pipelines,
Adhere to Access Control and Security Policies
accidents, view in DevOps,
Accidents Are Normal
ACM Queue article on Canary Analysis service,
Conclusion
action items in postmortems,
Key action item characteristics missing
gamification of postmortem action items,
Gamification
in good postmortem example,
Clarity
blamelessness of,
Blamelessness
concrete action items,
Concrete action items
monitoring tool for,
Postmortem follow-up
rewarding closeout of,
Reward action item closeout
active development phase (service lifecycle), SRE engagement in,
Phase 2: Active Development
ADKAR,
Background
,
The Prosci ADKAR Model
AdMob and AdSense systems,
What we decided to do
AdWords NALSD example,
AdWords Example
design process,
Design Process
distributed system,
Distributed System
LogJoiner,
LogJoiner
MapReduce, evaluating,
MapReduce
initial requirements,
Initial Requirements
running application on one machine,
One Machine
scaling resources for parsing logs,
Calculations
alerts
alert suppression,
Alerts
alerting on SLOs,
Alerting on SLOs
burn rate for error budgets,
4: Alert on Burn Rate
considerations in,
Alerting Considerations
increased alert window,
2: Increased Alert Window
incrementing alert duration,
3: Incrementing Alert Duration
low-traffic services and error budget alerting,
Low-Traffic Services and Error Budget Alerting
making sure alerting is scalable,
Alerting at Scale
multiple burn rate alarms,
5: Multiple Burn Rate Alerts
multiwindow, multi-burn-rate alerts,
6: Multiwindow, Multi-Burn-Rate Alerts
services with extreme availability goals,
Extreme Availability Goals
target error rate ࣙ SLO threshold,
1: Target Error Rate ≥ SLO Threshold
contributors to high pager load,
Pager load inputs
paging alerts, defining thresholds for,
Alerting
provided by monitoring system,
Alerts
in metrics-based and logs-based systems,
Sources of Monitoring Data
separating alerting in monitoring systems,
Prefer Loose Coupling
testing alerting logic in monitoring system,
Testing Alerting Logic
using good alerts and consoles to identify cause of pages,
Identification delay
analysis of postmortems,
Postmortem analysis
,
Results of Postmortem Analysis
animated (undesirable) language in postmortems,
Animated language
anycast,
Google Cloud Load Balancing
stabilized, implementation of,
Stabilized anycast
APIs
availability and latency for API calls, Home Depot case study,
Availability and latency for API calls
availability and latency SLIs,
API and HTTP server availability and latency
case study, end-to-end API simplicity,
Background
machine consumable,
Everything Important Eventually Becomes a Platform
proposed SLOs for the API,
Using the SLIs to Calculate Starter SLOs
application errors in data processing pipeline,
Pipeline application or configuration
Application Readiness Reviews (ARRs),
Aligning Goals
architecture and design phase (service lifecycle), SRE engagement in,
Phase 1: Architecture and Design
architecture and design, SRE team partnering on,
Partnering on architecture
architectures (opaque), troubleshooting for,
Troubleshooting for Opaque Architectures
artificial load generation,
Artificial Load Generation
aspirational SLOs,
Improving the Quality of Your SLO
authoring of postmortems, including all participants in,
Include all incident participants in postmortem authoring
autohealing,
Handling Unhealthy Machines
automated builds,
Release Engineering Principles
automated health checking,
New bugs
automation
archiving and migration, in filer-backed home directory decommissioning,
Archiving and migration automation
assessing risks of,
Assess Risk Within Automation
automating this year’s job away,
Automate This Year’s Job Away
automating toil response,
Automate Toil Response
increasing uniformity in production environment,
Increase Uniformity
measuring effectiveness of automated tasks,
Use Feedback to Improve
partial automation with human-backed interfaces,
Start with Human-Backed Interfaces
,
Start with human-backed interfaces
using to reduce toil in datacenter, case study,
Case Study 1: Reducing Toil in the Datacenter with Automation
autoscaling,
Autoscaling
avoiding overloading backends,
Avoiding Overloading Backends
avoiding traffic imbalance,
Avoiding Traffic Imbalance
configuring conservatively,
Configuring Conservatively
handling unhealthy machines,
Handling Unhealthy Machines
implementing for data processing pipelines,
Implement Autoscaling and Resource Planning
in Spotify case study,
Capacity planning
including kill switches and manual overrides,
Including Kill Switches and Manual Overrides
load-based, using with load balancing,
Combining Strategies to Manage Load
load-based, using with load shedding,
Combining Strategies to Manage Load
setting constraints on the autoscaler,
Setting Constraints
using with load balancing and load shedding, precautions with,
Lessons learned
working with stateful systems,
Working with Stateful Systems
availability
alerting on services with extreme availability goals,
Extreme Availability Goals
during canary deployment,
Minimizing Risk to SLOs and the Error Budget
Evernote’s goal for,
Introduction of SLOs: A Journey in Progress
factoring dependencies into,
Troubleshooting for Opaque Architectures
for API calls, SLOs in Home Depot case study,
Availability and latency for API calls
grouping request types into buckets of similar availability requirements,
Alerting at Scale
high availability with GCLB,
GCLB: High Availability
availability SLI,
A Worked Example
API and HTTP server availability,
API and HTTP server availability and latency
measuring availability with health-checking handler,
Improving the Quality of Your SLO
B
backend services, avoiding overloading in autoscaling,
Avoiding Overloading Backends
balance between on-call and project work for SREs,
Recap of “Being On-Call” Chapter of First SRE Book
baseline of a functional team,
Reducing Overload and Restoring Team Health
Beyond Corp network security protocol,
Problem Statement
BGP (Border Gateway Protocol),
Anycast
blameful language, mitigating damage of,
Failing to reinforce the culture
blameless language,
Use blameless language
blameless postmortems,
Compare and Contrast
,
It’s Better to Fix It Yourself; Don’t Blame Someone Else
,
Postmortem Culture: Learning from Failure
blamelessness in good postmortem example,
Blamelessness
modeling and enforcing blameless behavior,
Model and Enforce Blameless Behavior
responding to culture failures in,
Respond to Postmortem Culture Failures
blue/green deployment,
Blue/Green Deployment
boiling the frog,
Vigilance
Borg,
Background
breaks (long-term) in on-call scheduling,
Plan for long-term breaks
Bridges Transition Model,
Emotion-Based Models
,
How These Theories Apply to SRE
bucketing, using with SLIs,
Grading Interaction Importance
bugs
bug tracking systems,
Data quality
new bugs in production environment,
New bugs
preexisting bugs in production environment,
Preexisting bugs
tracking new bugs in production,
New bugs
burn rate (error budgets)
alerting on,
4: Alert on Burn Rate
multiple alerts on,
5: Multiple Burn Rate Alerts
multiwindow multi-burn-rate alerts,
6: Multiwindow, Multi-Burn-Rate Alerts
business intelligence,
Data Analytics
business priorities, communicating between SRE and developer teams,
Communicating Business and Production Priorities
business processes producing toil,
Business Processes
questioning,
Challenge assumptions and retire expensive business processes
C
calculations support (monitoring systems),
Calculations
CALMS (Culture, Automation, Lean, Measurement, and Sharing),
Background on DevOps
canarying releases,
Canarying Releases
,
Identification delay
balancing release velocity and reliability,
Balancing Release Velocity and Reliability
canary implementation,
Canary Implementation
choosing canary population and duration,
Choosing a Canary Population and Duration
minimizing risk to SLOs and error budget,
Minimizing Risk to SLOs and the Error Budget
canarying, defined,
What Is Canarying?
dependencies and isolation,
Dependencies and Isolation
for data processing pipeline,
Canarying
in noninteractive systems,
Canarying in Noninteractive Systems
related concepts,
Related Concepts
artificial load generation,
Artificial Load Generation
blue/green deployment,
Blue/Green Deployment
traffic teeing,
Traffic Teeing
release engineering and canarying,
Release Engineering and Canarying
example setup,
Our Example Setup
requirements of canary process,
Requirements of a Canary Process
release engineering principles,
Release Engineering Principles
requirements on monitoring data,
Requirements on Monitoring Data
roll forward deployment vs. simple canary deployment,
A Roll Forward Deployment Versus a Simple Canary Deployment
selecting and evaluating metrics,
Selecting and Evaluating Metrics
before/after evaluation, riskiness of,
Before/After Evaluation Is Risky
metrics indicating problems,
Metrics Should Indicate Problems
representative and attributable metrics,
Metrics Should Be Representative and Attributable
using gradual canary for better metric selection,
Use a Gradual Canary for Better Metric Selection
separating components that change at different rates,
Balancing Release Velocity and Reliability
with GCLB,
GCLB: High Availability
capacity planning,
Cost Engineering and Capacity Planning
for data processing pipeline,
Implement Autoscaling and Resource Planning
in Spotify case study,
Capacity planning
setting traffic volume SLOs in Home Depot case study,
Traffic volume
CCN (cyclomatic complexity number),
Measuring Complexity
change control,
Organizational Change Management in SRE
change management
in DevOps and SRE,
Compare and Contrast
organizational change management in SRE,
Organizational Change Management in SRE
case study, common tooling adoption in SRE,
Background
case study, scaling Waze,
Background
emotion-based models,
Emotion-Based Models
how change management theories apply to SRE,
How These Theories Apply to SRE
Kotter’s eight-step process,
Kotter’s Eight-Step Process for Leading Change
Lewin’s three-stage model,
Lewin’s Three-Stage Model
McKinsey’s 7-S model,
McKinsey’s 7-S Model
Prosci ADKAR model,
The Prosci ADKAR Model
SRE embracing change,
SRE Embraces Change
changes
avoiding changes that can’t be rolled back,
Mitigation delay
change tracking for configurations,
Ownership and Change Tracking
gradual change in DevOps,
Change Should Be Gradual
monitoring intended changes in services,
Intended Changes
safe configuration change application,
Safe Configuration Change Application
checklist for new SRE team training,
Training roadmap
checklist for postmortems,
Postmortem checklist
checkpointing in data processing pipelines,
Checkpointing
clarity in good postmortem example,
Clarity
click-through rate (CTR),
AdWords Example
calculating,
Initial Requirements
ClickMap (AdWords example),
LogJoiner
in multidatacenter design,
Multidatacenter
scaling, calculations for,
Calculations
in multidatacenter design,
Calculations
client behavior changes, resulting in bugs,
New bugs
Clos network topology,
Background
cloud environment
breaking down SLO wall between GCP and Evernote,
Breaking Down the SLO Wall Between Customer and Cloud Provider
Evernote, on-call setup for cloud datacenters,
Moving our on-prem infrastructure to the cloud
Google Cloud Platform (GCP),
SLO Engineering Case Studies
code
code patterns for data processing pipelines,
Code Patterns
configuration as code or data,
Separate Configuration and Resulting Data
cyclomatic code complexity,
Measuring Complexity
codelabs,
Training roadmap
collaboration in DevOps and SRE,
Compare and Contrast
colocation facilities (colos), racks of proxy/cache machines in,
Case Study
communication
between teams, understanding differences in,
Understand differences in communication
in incident response,
Incident Command System
deciding on communication channel,
Decide on a communication channel
failure in Google Home incident,
Review
keeping your audience informed,
Keep your audience informed
maintaining open line between SRE and other teams,
Maintaining an Open Line of Communication
Communications Lead (CL),
Incident
completeness SLO (Spotify case study),
Completeness
complexity
case study, project lifecycle complexity,
Case Study 2: Project Lifecycle Complexity
measuring,
Measuring Complexity
complexity toil,
Configuration-Induced Toil
components
separating components that change at different rates,
Balancing Release Velocity and Reliability
types of,
Types of components
SLIs for different types,
A Worked Example
Compute Engine,
Breaking Down the SLO Wall Between Customer and Cloud Provider
conciseness in postmortems,
Conciseness
configuration,
Configuration Design and Best Practices
about,
What Is Configuration?
and reliability,
Configuration and Reliability
configuration-induced toil,
Configuration-Induced Toil
reducing,
Reducing Configuration-Induced Toil
critical properties and pitfalls of configuration systems,
Critical Properties and Pitfalls of Configuration Systems
building too much domain-specific optimization,
Pitfall 3: Building Too Much Domain-Specific Optimization
designing accidental or ad hoc language features,
Pitfall 2: Designing Accidental or Ad Hoc Language Features
failing to recognize configuration as programming language problem,
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
interleaving configuration evaluation with side effects,
Pitfall 4: Interleaving “Configuration Evaluation” with “Side Effects”
using general-purpose scripting languages,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
data processing pipeline, causing failures,
Pipeline application or configuration
effectively operating a configuration system,
Effectively Operating a Configuration System
testing,
Testing
using source control,
Source Control
versioning,
Versioning
guarding against abusive configuration,
Guarding Against Abusive Configuration
integrating a configuration language,
Integrating a Configuration Language
driving multiple applications,
Driving Multiple Applications
generating config in specific formats,
Generating Config in Specific Formats
integrating custom applications,
Integrating Custom Applications (In-House Software)
integrating existing application, Kubernetes,
Integrating an Existing Application: Kubernetes
example Kubernetes config,
Example Kubernetes Config
integrating the configuration language,
Integrating the Configuration Language
mechanics of,
Mechanics of Configuration
importance of tooling,
Importance of Tooling
ownership and change tracking,
Ownership and Change Tracking
safe configuration change application,
Safe Configuration Change Application
separating configuration and resulting data,
Separate Configuration and Resulting Data
monitoring system, treating as code,
Treat Your Configuration as Code
philosophy of,
Configuration Philosophy
configuration asks users questions,
Configuration Asks Users Questions
escaping simplicity,
Escaping Simplicity
mandatory and optional questions,
Mandatory and Optional Questions
questions should be close to user goals,
Questions Should Be Close to User Goals
separating philosophy and mechanics,
Separating Philosophy and Mechanics
when to evaluate,
When to Evaluate Configuration
early evaluation, checking in the JSON,
Very Early: Checking in the JSON
late evaluation at runtime,
Late: Evaluate at Runtime
middle of the road, evaluation at build time,
Middle of the Road: Evaluate at Build Time
configuration syntax, tooling for,
Configuration syntax
connection tracking,
Maglev
consensus algorithms,
Multidatacenter
consistent hashing,
Maglev
using with stateful systems,
Working with Stateful Systems
contacts, preparing for an incident,
Prepare a list of contacts
context, missing, in bad postmortem,
Missing context
continuous integration and continuous delivery (CI/CD),
Canarying Releases
,
Change Should Be Gradual
coupled with release automation, virtuous cycle of,
Release Engineering Principles
coordination of incident response effort,
Incident Command System
correctness SLI,
A Worked Example
correctness SLOs,
Data correctness
corrupt data (in data processing pipeline),
Corrupt data
cost engineering,
Cost Engineering and Capacity Planning
coverage SLI,
A Worked Example
implementation for pipeline coverage,
Pipeline freshness, coverage, and correctness
,
Pipeline freshness, coverage, and correctness
coverage, SLO lacking,
Improving the Quality of Your SLO
CRE,
Engaging with CRE
CRITICAL requests,
Alerting at Scale
cross-team reviews of postmortems,
Conduct cross-team reviews
CRUD-style APIs, monitoring system configuration,
Treat Your Configuration as Code
Cs of incident management (coordinate, communicate, control),
Incident Command System
CTR,
AdWords Example
culture
and tooling in DevOps,
Tooling and Culture Are Interrelated
learning from failure in postmortems,
Postmortem Culture: Learning from Failure
responding to postmortem culture failures,
Respond to Postmortem Culture Failures
SLO culture project at Home Depot,
The SLO Culture Project
customers
having a hard time,
When Your Customers Have a Hard Time, You Have to Slow Down
practicing SRE with,
You Will Need to Practice SRE with Your Customers
SRE with, how to,
How to: SRE with Your Customers
cyclomatic code complexity,
Measuring Complexity
D
dashboards
building shared SLO dashboards with customers,
Step 2: Audit the Monitoring and Build Shared Dashboards
for data processing pipeline,
Pipeline maturity matrix
providing for SLOs,
Dashboards and Reports
separate dashboarding system in monitoring,
Prefer Loose Coupling
showing SLI trends,
Dashboards and Reports
VALET dashboard, Home Depot case study,
VALET Dashboard
data analysis pipeline, case study,
Case Study 2: Data Analysis Pipeline
data analytics,
Data Analytics
data collection to monitor causes in on-call load,
Data quality
data correctness,
Data correctness
data formats for configuration information,
Separate Configuration and Resulting Data
data freshness,
Data freshness
data isolation,
Data isolation/load balancing
canarying releases and,
Dependencies and Isolation
in noninteractive systems,
Canarying in Noninteractive Systems
data processing pipelines,
Data Processing Pipelines
best practices,
Pipeline Best Practices
adhering to access control and security policies,
Adhere to Access Control and Security Policies
creating and maintaining pipeline documentation,
Create and Maintain Pipeline Documentation
defining and measuring service level objectives,
Define and Measure Service Level Objectives
implementing autoscaling and resource planning,
Implement Autoscaling and Resource Planning
mapping your development lifecycle,
Map Your Development Lifecycle
planning escalation paths,
Plan Escalation Paths
planning for dependency failure,
Plan for Dependency Failure
reducing hotspotting and workload patterns,
Reduce Hotspotting and Workload Patterns
case study, Spotify,
Case Study: Spotify
customer integration and support,
Customer Integration and Support
event delivery,
Event Delivery
event delivery system design and architecture,
Event Delivery System Design and Architecture
event delivery system operation,
Event Delivery System Operation
failures, prevention and response,
Pipeline Failures: Prevention and Response
potential causes,
Pipeline dependencies
potential failure modes,
Delayed data
pipeline applications,
Pipeline Applications
data analytics,
Data Analytics
event processing and data transformation,
Event Processing/Data Transformation to Order or Structure Data
machine learning,
Machine Learning
requirements and design,
Pipeline Requirements and Design
checkpointing,
Checkpointing
code patterns,
Code Patterns
features,
What Features Do You Need?
idempotent and two-phase mutations,
Idempotent and Two-Phase Mutations
pipeline production readiness,
Pipeline Production Readiness
data-only languages (configuration),
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
datacenters
multidatacenter in AdWords example,
Multidatacenter
using automation to reduce toil, case study,
Case Study 1: Reducing Toil in the Datacenter with Automation
debugging,
Encourage Consistency
for data processing pipeline,
Pipeline maturity matrix
in App Engine errors,
Problem
metrics for,
Implementing Purposeful Metrics
delayed data (in data processing pipeline),
Delayed data
Deming Cycle,
The Deming Cycle
dependencies
canarying releases and,
Dependencies and Isolation
circular dependency, pDNS,
Background
effects on availability,
Troubleshooting for Opaque Architectures
external dependencies and incident response,
Incident
in data processing pipeline, causing failures,
Pipeline dependencies
modeling,
Modeling Dependencies
monitoring system metrics from,
Dependencies
planning for failure in data processing pipelines,
Plan for Dependency Failure
deployments
automated,
Release Engineering Principles
blue/green,
Blue/Green Deployment
continuous,
Change Should Be Gradual
deploying data processing pipeline to production,
Deploying to production
partial, performing for data processing pipelines,
Performing a partial deployment
roll forward deployment vs. simple canary deployment,
A Roll Forward Deployment Versus a Simple Canary Deployment
small,
Release Engineering Principles
deprecation phase (service lifecycle), SRE engagement in,
Phase 5: Deprecation
depth in postmortems,
Depth
design phase (service lifecycle), SRE engagement in,
Phase 1: Architecture and Design
design process (NALSD),
Design Process
destructive testing or fuzzing,
Preexisting bugs
detection time (SLO alerts),
Alerting Considerations
development
development process in Spotify case study,
Development process
mapping data processing pipeline development lifecycle,
Map Your Development Lifecycle
partnership with SRE, critical importance of,
When Can Substitute for Whether
placing your first SRE in development team,
Placing Your First SRE
setting up relationship between SRE and development team,
Setting Up the Relationship
aligning goals,
Aligning Goals
communicating business and production priorities,
Communicating Business and Production Priorities
identifying risks,
Identifying Risks
planning and executing,
Planning and Executing
setting ground rules,
Setting Ground Rules
SRE teams having responsibility for,
Self-regulating workload
SRE-to-developer ratio and support of multiple services by single SRE team,
Supporting Multiple Services with a Single SRE Team
SREs sharing ownership with developers,
Share Ownership with Developers
sustaining an effective ongoing relationship between SRE and development teams,
Sustaining an Effective Ongoing Relationship
DevOps
about,
Background on DevOps
accidents, view of,
Accidents Are Normal
comparing and contrasting with SRE,
Compare and Contrast
elimination of silos,
No More Silos
gradual change,
Change Should Be Gradual
implementation by SRE,
Background on SRE
interrelation of tooling and culture,
Tooling and Culture Are Interrelated
measurement as crucial,
Measurement Is Crucial
organizational context and fostering successful adoption,
Organizational Context and Fostering Successful Adoption
disaster and recovery testing, practicing with customers,
Step 5: Practice, Practice, Practice
disaster recovery testing (DiRT) at Google,
Drills
,
Plan for Dependency Failure
diskerase,
Case Study
Display Ads Spiderweb, simplification of (case study),
Background
distributed SRE teams, running,
Running Cohesive Distributed SRE Teams
distributed SREs,
Distributed SREs
documentation
creating and maintaining for data processing pipelines,
Create and Maintain Pipeline Documentation
Spotify case study, customer integration and support,
Documentation
domain-specific languages (DSLs) for configuration,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
domain-specific optimization (excessive) in configurations,
Pitfall 3: Building Too Much Domain-Specific Optimization
draining requests away from buggy system elements,
Mitigation delay
drills (incident management),
Drills
dropping work,
Prioritize and triage within one quarter
durability SLI,
A Worked Example
duration parameter (alerts), incrementing,
3: Incrementing Alert Duration
E
ease of implementation and transparency
for data processing pipeline,
Pipeline maturity matrix
emergency response, practicing,
Identification delay
emotion-based models for change management,
Emotion-Based Models
end-to-end measurement for data processing pipeline SLOs,
End-to-end measurement
ending SRE engagements,
Ending the Relationship
case study, Ares,
Case Study 1: Ares
case study, data analysis pipeline,
Case Study 2: Data Analysis Pipeline
Equal-Cost Multi-Path (ECMP) forwarding,
Maglev
error budgets,
Introduction of SLOs: A Journey in Progress
addressing missed SLO caused by a dependency,
Modeling Dependencies
adjusting priorities according to,
Adjusting Priorities According to Your SLOs and Error Budget
agreed-upon by SRE and development teams for a service,
Setting Ground Rules
alerting on burn rate,
4: Alert on Burn Rate
multiple alarms,
5: Multiple Burn Rate Alerts
multiwindow, multi-burn-rate alerts,
6: Multiwindow, Multi-Burn-Rate Alerts
calculating,
What to Measure: Using SLIs
dashboard showing error budget consumption,
Dashboards and Reports
decision making using,
Decision Making Using SLOs and Error Budgets
documenting error budget policy,
Documenting the SLO and Error Budget Policy
establishing error budget policy,
Establishing an Error Budget Policy
example policy,
Service Overview
for example game service,
Error Budget
low-traffic services and error budget alerting,
Low-Traffic Services and Error Budget Alerting
combining services,
Combining Services
generating artificial traffic,
Generating Artificial Traffic
lowering the SLO or increasing the window,
Lowering the SLO or Increasing the Window
making service and infrastructure changes,
Making Service and Infrastructure Changes
minimizing risk to by canarying releases,
Minimizing Risk to SLOs and the Error Budget
prerequisites for adopting as SRE approach,
Getting Started
reliability targets and,
Reliability Targets and Error Budgets
rolling back recent changes and,
Mitigation delay
support tickets per day vs. measured loss in budget,
Improving the Quality of Your SLO
errors
alerting for target error rate over SLO threshold,
1: Target Error Rate ≥ SLO Threshold
debugging in different monitoring systems,
Problem
defining SLOs for in Home Depot case study,
Errors
errors per hour metric in canary deployment,
Requirements on Monitoring Data
increased alert window for SLO errors,
2: Increased Alert Window
measurement in Home Depot case study,
The SLO Culture Project
evangelism, SLOs at Home Depot,
Evangelizing SLOs
,
The SLO Culture Project
events
event delivery in Spotify case study,
Event Delivery
event processing to order or structure data,
Event Processing/Data Transformation to Order or Structure Data
Evernote, SLO case study,
Evernote’s SLO Story
current state of SLO use and practice,
Current State
introduction of SLOs, journey in progress,
Introduction of SLOs: A Journey in Progress
why Evernote adopted SRE model,
Why Did Evernote Adopt the SRE Model?
extract, transform, load (ETL) model,
Event Processing/Data Transformation to Order or Structure Data
ETL pipelines,
Event Processing/Data Transformation to Order or Structure Data
in Spotify case study,
Extract Transform Load
F
failures,
Accidents Are Normal
data processing pipeline, prevention and response,
Pipeline Failures: Prevention and Response
potential causes,
Pipeline dependencies
potential failure modes,
Delayed data
dependency failure in data processing pipeline,
Plan for Dependency Failure
failure tolerance in data processing pipeline,
Pipeline maturity matrix
handling mistakes appropriately,
Handling Mistakes Appropriately
not passing off blame for,
It’s Better to Fix It Yourself; Don’t Blame Someone Else
reducing cost of,
Move Fast by Reducing the Cost of Failure
feature isolation,
Mitigation delay
features
feature coverage in SRE with customers,
Be Thoughtful and Disciplined
planning for data processing pipelines,
What Features Do You Need?
separating feature launches from binary releases,
Balancing Release Velocity and Reliability
tradeoffs between feature velocity and reliability,
Reliability Targets and Error Budgets
feedback from users, toil management with,
Use Feedback to Improve
finger pointing in postmortems,
Counterproductive finger pointing
follow-up to pager alerts, rigor in,
Rigor of follow-up
follow-up to postmortems,
Postmortem follow-up
forming your first SRE team,
Forming
Four Golden Signals,
Dependencies
,
The SLO Culture Project
freshness
data freshness SLOs for data processing pipeline,
Data freshness
of data in monitoring system,
Speed
freshness SLI,
A Worked Example
implementation for pipeline freshness,
Pipeline freshness, coverage, and correctness
funding and hiring (SREs),
SRE Funding and Hiring
future protection from overload,
Protect yourself in the future
G
G Suite Team Drive,
What We Decided to Do
GCE,
Incident
GCLB (Google Cloud Load Balancer),
Google Cloud Load Balancing
general availability phase (service lifecycle), SRE engagement in,
Phase 4: General Availability
generic mitigations,
What could have been handled better?
useful, in GKE CreateCluster failure case study,
What could have been handled better?
geographical splits (SRE teams),
Geographical Splits
finance, travel budget,
Finance: Travel budget
leadership, joint ownership of a service,
Leadership: Joint ownership of a service
parity, distributing work and avoiding a night shift,
Parity: Distributing Work Between Offices and Avoiding a “Night Shift”
people and projects, seeding the team,
People and projects: Seeding the team
placement, and having three shifts,
Placement: What about having three shifts?
placement, time zones apart,
Placement: How many time zones apart should the teams be?
should both halves of the team start at the same time,
Timing: Should both halves of the team start at the same time?
Global Service Load Balancer (GSLB),
Global Service Load Balancer
glossary in good postmortem example,
Clarity
,
Good Postmortem
goals, aligning between SRE and development teams,
Aligning Goals
golden signals,
Dependencies
Google AdWords,
AdWords Example
Google Analytics,
Data Analytics
Google Apps Script,
Google’s template
Google Assistant (version 1.88), bug in,
Context
Google Cloud Load Balancer (GCLB),
Google Cloud Load Balancing
high availability with,
GCLB: High Availability
Google Cloud Load Balancing,
Google Cloud Load Balancing
anycast network addressing and routing,
Anycast
stabilized anycast,
Stabilized anycast
case study, Pokémon GO on GCLB,
Case Study 1: Pokémon GO on GCLB
future-proofing,
Future-proofing
migrating to GCLB,
Migrating to GCLB
resolving issue with request spikes and GFE,
Resolving the issue
Global Service Load Balancer (GSLB),
Global Service Load Balancer
Google Front End (GFE),
Google Front End
low latency with GCLB,
GCLB: Low Latency
Maglev packet-level load balancer,
Maglev
Google Cloud Platform (GCP),
Moving our on-prem infrastructure to the cloud
,
SLO Engineering Case Studies
breaking down SLO wall between GCP and Evernote,
Breaking Down the SLO Wall Between Customer and Cloud Provider
Google Compute Engine (GCE),
Data collection
Autoscaler,
Capacity planning
,
Data delivery
losing large number of disk trays, incident response case study,
Incident
Google Front Ends (GFE),
Google Front End
,
Maglev
capacity reduction caused by synchronous client retries,
Migrating to GCLB
Google Home software bug incident response case study,
Case Study 1: Software Bug—The Lights Are On but No One’s (Google) Home
Google Kubernetes Engine (GKE), CreateCluster failure case study,
Case Study 2: Service Fault—Cache Me If You Can
Google’s Colossus File System,
What We Decided to Do
Google’s Customer Reliability Engineering (CRE) team,
Engaging with CRE
,
SLO Engineering Case Studies
Google’s template for postmortems,
Google’s template
GSLB (Global Service Load Balancer),
Global Service Load Balancer
H
HashiCorp Configuration Language,
Generating Config in Specific Formats
health checking, automated, problems with,
New bugs
help, asking for,
Identification delay
HIGH_FAST requests,
Alerting at Scale
HIGH_SLOW requests,
Alerting at Scale
Home Depot, SLO case study,
The Home Depot’s SLO Story
applying VALET to batch applications,
Applying VALET to Batch Applications
automating VALET data collection,
Automating VALET Data Collection
evangelizing SLOs,
Evangelizing SLOs
first set of SLOs,
Our First Set of SLOs
future aspirations,
Future Aspirations
proliferation of SLOs,
The Proliferation of SLOs
using VALET in testing,
Using VALET in Testing
horizontal projects,
Horizontal Projects
horizontal SRE team,
Assembling a horizontal SRE team
risks and mitigations for,
Horizontal SRE team
hotspotting, reducing in data processing pipeline,
Reduce Hotspotting and Workload Patterns
HTTP requests
grading importance of,
Grading Interaction Importance
success of, SLIs for,
What to Measure: Using SLIs
HTTP servers, availability and latency,
API and HTTP server availability and latency
HTTP status codes,
Clarifications and Caveats
,
Errors
,
Problem
including in metrics-based monitoring,
Proposed solution
monitoring system metrics on served traffic,
Status of Served Traffic
human error causing new bugs in production,
New bugs
human processes in pager load,
Pager load inputs
human-backed interfaces, starting with,
Start with Human-Backed Interfaces
,
Start with human-backed interfaces
Hyrum’s Law,
Measuring Complexity
I
IC (Incident Commander),
Main Roles in Incident Response
ICS (Incident Command System),
Incident Command System
idempotent mutations,
Idempotent and Two-Phase Mutations
identification delay for causes of pages,
Identification delay
incentives
for SLO setting and measuring at Home Depot,
The SLO Culture Project
for successful adoption of DevOps and SRE,
Organizational Context and Fostering Successful Adoption
avoiding passing of blame,
It’s Better to Fix It Yourself; Don’t Blame Someone Else
narrow incentives narrowing success,
Narrow, Rigid Incentives Narrow Your Success
striving for parity of esteem,
Strive for Parity of Esteem: Career and Financial
incident response,
Incident Response
basic principles,
Incident Response
best practices, using,
Putting Best Practices into Practice
drills,
Drills
preparing beforehand,
Prepare Beforehand
training,
Incident Response Training
case study, Google Home software bug and failure to communicate,
Case Study 1: Software Bug—The Lights Are On but No One’s (Google) Home
incident,
Incident
review,
Review
case study, Google Kubernetes Engine (GKE), cluster creation failure,
Case Study 2: Service Fault—Cache Me If You Can
incident,
Incident
responses that needed improvement,
What could have been handled better?
responses that went well,
What went well?
case study, incident response at PagerDuty,
Case Study 4: Incident Response at PagerDuty
major incident response,
Major incident response at PagerDuty
tools used,
Tools used for incident response
case study, lightning strikes at Google datacenter,
Case Study 3: Power Outage—Lightning Never Strikes Twice…Until It Does
incident,
Incident
review,
Review
incident management at Google,
Incident Management at Google
Incident Command System (ICS),
Incident Command System
main roles in incident response,
Main Roles in Incident Response
practicing in SRE with customers,
Step 5: Practice, Practice, Practice
incidents
establishing criteria for,
Establish criteria for an incident
finding causes of repeating incidents,
Repeating incidents
incident handling in Spotify case study,
Incident handling
root cause and trigger, in postmortem analysis results,
Results of Postmortem Analysis
weekly reporting of,
Report incidents and outages weekly
infrastructure-centric view (configuration),
Configuration Asks Users Questions
intent-based configuration, monitoring system,
Treat Your Configuration as Code
interpersonal risk taking,
Problem Statement
interrupts,
Identifying and Recovering from Overload
triaging,
Lessons Learned
work overload and,
From Load to Overload
iterations for SLO quality improvement,
Improving the Quality of Your SLO
J
JavaScript,
Generating Config in Specific Formats
jitter,
Future-proofing
JSON,
Generating Config in Specific Formats
configuration data in,
Separate Configuration and Resulting Data
configuration items in Kubernetes represented as JSON objects,
What Kubernetes Provides
examples of bad and good JSON output by Jsonnet,
Integrating Custom Applications (In-House Software)
Jsonnet,
Integrating Custom Applications (In-House Software)
,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
,
Separate Configuration and Resulting Data
converting existing template to,
Integrating the Configuration Language
generating JSON for configuration evaluation,
When to Evaluate Configuration
guarding against abusive configurations in,
Guarding Against Abusive Configuration
library functions for outputting INI and XML,
Generating Config in Specific Formats
quick introduction to,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
using with Kubernetes configurations,
Integrating the Configuration Language
validating JSON with JSONschema,
Integrating Custom Applications (In-House Software)
versioning in,
Versioning
writing tests as Jsonnet files,
Testing
K
key details omitted in bad postmortem,
Key details omitted
kill switches and manual overrides in autoscaling,
Including Kill Switches and Manual Overrides
Kotter’s eight-step process for leading change,
How These Theories Apply to SRE
,
Kotter’s Eight-Step Process for Leading Change
in Waze case study,
Background
Kubernetes,
Integrating an Existing Application: Kubernetes
,
What we decided to do
capabilities of,
What Kubernetes Provides
example Kubernetes config,
Example Kubernetes Config
GKE CreateCluster failure, incident response case study,
Case Study 2: Service Fault—Cache Me If You Can
integrating the configuration language,
Integrating the Configuration Language
using Jsonnet to build and deploy objects,
Guarding Against Abusive Configuration
Kübler-Ross Change Curve,
Emotion-Based Models
,
How These Theories Apply to SRE
L
languages, configuration
choosing language to store configuration in,
Separate Configuration and Resulting Data
configuration syntax features,
Configuration syntax
failing to recognize configuration as programming language problem,
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
integrating a configuration language,
Integrating a Configuration Language
integrating in Kubernetes,
Integrating the Configuration Language
semantic validation,
Semantic validation
using existing general-purpose scripting languges for configuration,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
latency
calculations for multidatacenter design in AdWords example,
Calculations
for API calls in Home Depot case study,
Availability and latency for API calls
low latency with GCLB,
GCLB: Low Latency
measurement in Home Depot case study,
The SLO Culture Project
SLOs in Home Depot case study,
Latency
latency SLI,
A Worked Example
API and HTTP server latency,
API and HTTP server availability and latency
Launch Coordination Engineering (LCE) teams,
Launch Coordination Engineering Teams
leadership in geographically split SRE teams,
Leadership: Joint ownership of a service
legacy systems,
Use Feedback to Improve
decommissioning filer-backed home directories, case study,
Case Study 2: Decommissioning Filer-Backed Home Directories
Lewin’s three-stage model for managing change,
Lewin’s Three-Stage Model
limited audience in bad postmortem example,
Limited audience
limited availability phase (service lifecycle), SRE engagement in,
Phase 3: Limited Availability
line-card repair
design first effort, Saturn line-card repair,
Design First Effort: Saturn Line-Card Repair
Saturn automated line-card repair workflow,
Implementation
Saturn vs. Jupiter line-card repair,
Implementation
workflow before automation,
Background
linters,
Configuration syntax
live version,
Our Example Setup
load
artificial generation of,
Artificial Load Generation
bugs manifesting only at specific levels of load,
New bugs
load-based autoscaling,
Combining Strategies to Manage Load
testing,
Preexisting bugs
load balancing
Google Cloud
case study, Pokémon GO on GCLB,
Case Study 1: Pokémon GO on GCLB
load balancer monitoring,
API and HTTP server availability and latency
load balancing
combining strategies to manage load,
Combining Strategies to Manage Load
precautions with,
Lessons learned
for priority items in data processing pipelines,
Data isolation/load balancing
Google Cloud,
Google Cloud Load Balancing
GCLB, high availability with,
GCLB: High Availability
GCLB, low latency with,
GCLB: Low Latency
Global Service Load Balancer (GSLB),
Global Service Load Balancer
Google Front End,
Google Front End
Maglev load balancer,
Maglev
using anycast,
Anycast
task-level, using with autoscaling on stateful systems,
Working with Stateful Systems
using with autoscaling,
Handling Unhealthy Machines
load shedding,
Combining Strategies to Manage Load
,
New bugs
case study, when load shedding attacks,
Case Study 2: When Load Shedding Attacks
precautions with load shedding,
Lessons learned
LogJoiner (AdWords example),
LogJoiner
scaling, calculations,
Calculations
sharded,
Sharded LogJoiner
logs,
Sources of Monitoring Data
choosing between log-based and metrics-based monitoring systems,
Problem
logging change information,
Identification delay
logs-based monitoring systems,
Sources of Monitoring Data
long term goals (SRE team),
Setting Ground Rules
LOW (availability) requests,
Alerting at Scale
low-traffic services, error budget alerting on,
Low-Traffic Services and Error Budget Alerting
combining services,
Combining Services
generating artificial traffic,
Generating Artificial Traffic
lowering the SLO or increasing the window,
Lowering the SLO or Increasing the Window
making service and infrastructure changes,
Making Service and Infrastructure Changes
M
machine learning,
Machine Learning
example machine learning data processing pipeline,
Machine Learning
Maglev,
Anycast
implementing stabilized anycast with,
Stabilized anycast
packet delivery using consistent hashing and connection tracking,
Maglev
major incident response at PagerDuty,
Major incident response at PagerDuty
manual overrides and kill switches in autoscaling,
Including Kill Switches and Manual Overrides
MapReduce, evaluating for use in AdWords distributed system,
MapReduce
maturity matrix for data processing pipeline,
Pipeline maturity matrix
McKinsey’s 7-S change management model,
McKinsey’s 7-S Model
mean time to repair (MTTR),
Move Fast by Reducing the Cost of Failure
measurements
decision on what/how to measure for SLOs at Evernote,
Introduction of SLOs: A Journey in Progress
effectiveness of automated tasks,
Use Feedback to Improve
end-to-end measurement for data processing pipeline SLOs,
End-to-end measurement
importance in DevOps,
Measurement Is Crucial
in DevOps and SRE,
Compare and Contrast
in SRE with customers,
Step 3: Measure and Renegotiate
measurability in action items in postmortems,
Concrete action items
measuring the SLIs,
Measuring the SLIs
measuring toil,
Identify and Measure Toil
,
Measuring Toil
metrics for Home Depot services,
The SLO Culture Project
sources of, for API and HTTP sever availability and latency SLI,
API and HTTP server availability and latency
with service level indicators (SLIs),
What to Measure: Using SLIs
meeting in person to resolve issues,
Meet in person (or as close to it as possible) to resolve issues
metrics,
Sources of Monitoring Data
choosing between metrics-based and logs-based monitoring systems,
Problem
collecting in canary deployments, time limits on,
Requirements on Monitoring Data
establishing to evaluate team workload,
Protect yourself in the future
indicating work overload,
Recognizing the Symptoms of Overload
metric-based monitoring system,
Sources of Monitoring Data
quantifiable, in good postmortem example,
Clarity
restructuring at Evernote for cloud datacenters,
Restructuring our monitoring and metrics
selecting and evaluating for canary deployments,
Selecting and Evaluating Metrics
selection for canarying in noninteractive systems,
Canarying in Noninteractive Systems
visible and useful, from monitoring system,
Metrics with Purpose
dependencies,
Dependencies
implementing purposeful metrics,
Implementing Purposeful Metrics
intended changes to your service,
Intended Changes
on resource usage saturation,
Saturation
status of served traffic,
Status of Served Traffic
microservices
combining for low-traffic services and error budget alerting,
Combining Services
limiting how much an SRE team can accomplish,
SRE Engagement Model
running hundreds on a shared platform, case study,
Background
using microservice approach to creating data processing pipelines,
Using the microservice approach to creating pipelines
migrations,
Migrations
automation in filer-backed home directory decommissioning,
Archiving and migration automation
Mission Control program (SRE teams),
Mission Control
mistakes, handling appropriately,
Handling Mistakes Appropriately
mitigation delays, reducing,
Mitigation delay
mitigation in incident response,
What could have been handled better?
prioritizing mitigation above all else,
What could have been handled better?
mobility for SREs,
SRE Mobility
Moira portal,
Moira Portal
monitoring,
Monitoring
auditing and building shared dashboards in SRE with customers,
Step 2: Audit the Monitoring and Build Shared Dashboards
calculating SLOs from data,
Introduction of SLOs: A Journey in Progress
choosing between monitoring systems, examples,
Examples
covering in interviews with SREs,
Finding Your First SRE
data collection for causes of on-call paging,
Data quality
decisions on reliability and,
Your Users, Not Your Monitoring, Decide Your Reliability
desirable features of monitoring strategy,
Desirable Features of a Monitoring Strategy
alerts,
Alerts
calculations support,
Calculations
interfaces for data display,
Interfaces
speed of data retrieval,
Speed
for data processing pipeline,
Pipeline maturity matrix
implementation in common tooling adoption in SRE case study,
Implementation: Monitoring
managing monitoring systems,
Managing Your Monitoring System
encouraging consistency,
Encourage Consistency
loose coupling of components,
Prefer Loose Coupling
treating configuration as code,
Treat Your Configuration as Code
of release pipeline,
Release Engineering Principles
or prevention fixes for pager alerts,
Rigor of follow-up
providing visible and useful metrics,
Metrics with Purpose
implementing purposeful metrics,
Implementing Purposeful Metrics
on dependencies,
Dependencies
on resource usage saturation,
Saturation
status of served traffic,
Status of Served Traffic
requirements in canary evaluation,
Requirements on Monitoring Data
restructuring at Evernote for cloud datacenters,
Restructuring our monitoring and metrics
sources of data,
Sources of Monitoring Data
system monitoring in Spotify case study,
System monitoring
testing alerting logic,
Testing Alerting Logic
Moonwalk,
Moonwalk
multidatacenter design (AdWords example),
Multidatacenter
evaluating dataflow,
Evaluation
scaling, calculations for,
Calculations
Murphy-Beyer effect,
Automate This Year’s Job Away
mutations, idempotent and two-phase,
Idempotent and Two-Phase Mutations
N
NALSD,
Introducing Non-Abstract Large System Design
negative acknowledgments (NACKs),
Google Front End
NFS/CIFS protocols,
Background
NO_SLO requests,
Alerting at Scale
non-abstract large system design (NALSD),
Introducing Non-Abstract Large System Design
about,
What Is NALSD?
AdWords example,
AdWords Example
design process,
Design Process
distributed system, designing,
Distributed System
initial requirements,
Initial Requirements
running application on one machine,
One Machine
key questions in design iterations,
Conclusion
why non-abstract,
Why “Non-Abstract”?
noninteractive systems, canarying in,
Canarying in Noninteractive Systems
norming (SRE teams),
Norming
O
Omega,
Background
on-call,
On-Call
actions in incident response,
Incident Response Training
balancing between geographically split SRE teams,
Parity: Distributing Work Between Offices and Avoiding a “Night Shift”
example setup within Google,
Example On-Call Setups Within Google and Outside Google
example setups, Evernote case study,
Moving our on-prem infrastructure to the cloud
flexibility in,
On-Call Flexibility
scenario, a change in personal circumstances,
Scenario: A change in personal circumstances
pager load,
Anatomy of Pager Load
appropriate response times for pages,
Anatomy of Pager Load
contributors to high pager load,
Pager load inputs
scenario, a team in overload,
Scenario: A team in overload
recap from first SRE book,
Recap of “Being On-Call” Chapter of First SRE Book
team dynamics,
On-Call Team Dynamics
scenario, a survive the week culture,
Scenario: A culture of “survive the week”
operational load (or operational workload),
Identifying and Recovering from Overload
operational overload (or work overload),
Identifying and Recovering from Overload
operations,
How SRE Relates to DevOps
and separation between development and production,
Share Ownership with Developers
benefits provided by release engineering principles,
Release Engineering Principles
covering in interviews with SREs,
Finding Your First SRE
creating operational rigor with customers,
Step 5: Practice, Practice, Practice
developer involvement in,
Setting Ground Rules
empowering ops engineers in SRE,
Proposal one: Empower your ops engineers
placing your first SRE in operations team,
Placing Your First SRE
Operations or Ops Lead (OL),
Main Roles in Incident Response
organizational change (positive), rewarding,
Reward positive organizational change
organizational change management in SRE,
Organizational Change Management in SRE
case study, common tooling adoption in SRE,
Background
case study, scaling Waze,
Background
introduction to change management,
Introduction to Change Management
Deming Cycle,
The Deming Cycle
emotion-based models,
Emotion-Based Models
how the theories apply to SRE,
How These Theories Apply to SRE
Kotter’s eight-step process,
Kotter’s Eight-Step Process for Leading Change
Lewin’s three-stage model,
Lewin’s Three-Stage Model
McKinsey’s 7-S model,
McKinsey’s 7-S Model
Prosci ADKAR model,
The Prosci ADKAR Model
SRE embraces change,
SRE Embraces Change
outages
problem summary in postmortems,
Key details omitted
reporting weekly,
Report incidents and outages weekly
top triggers of,
Results of Postmortem Analysis
overload, identifying and recovering from,
Identifying and Recovering from Overload
case study, perceived overload after organizational and workload changes,
Background
decision on the solution,
What We Decided to Do
lessons learned,
Lessons Learned
long-term actions to address,
Long-term actions
mid-term actions to address,
Mid-term actions
problem statement,
Problem Statement
results of actions,
Effects
short-term actions to address,
Short-term actions
case study, work overload when half a team leaves,
Background
decision on the solution,
What We Decided to Do
implementation of the solution,
Implementation
lessons learned,
Lessons Learned
problem statement,
Problem Statement
from load to overload,
From Load to Overload
mitigation strategies,
Strategies for Mitigating Overload
recognizing symptoms of overload,
Recognizing the Symptoms of Overload
reducing overload and restoring team health,
Reducing Overload and Restoring Team Health
ownership
action items in good postmortem example,
Concrete action items
missing, in bad postmortem example,
Missing ownership
of a service in geographically split SRE team,
Leadership: Joint ownership of a service
of configurations,
Ownership and Change Tracking
viewing postmortem owners as leaders,
Hold up postmortem owners as leaders
P
pager load,
Anatomy of Pager Load
appropriate response times,
Anatomy of Pager Load
determining causes of high load,
Pager load inputs
alerting,
Alerting
data quality,
Data quality
identification delay for root cause of pages,
Identification delay
mitigation delay,
Mitigation delay
new bugs in production,
New bugs
preexisting bugs,
Preexisting bugs
rigor of follow-up,
Rigor of follow-up
vigilance,
Vigilance
scenario, a team in overload,
Scenario: A team in overload
PagerDuty, incident response case study,
Case Study 4: Incident Response at PagerDuty
part-time work schedules for on-call engineers,
Plan for part-time work schedules
participatory management,
What We Decided to Do
Paxos consensus algorithm,
Multidatacenter
pDNS (Production DNS), eliminating dependency on itself (case study),
Background
peak-end rule,
Your Users, Not Your Monitoring, Decide Your Reliability
perceived overload,
From Load to Overload
,
Identifying and Recovering from Overload
after organizational and workload changes, case study,
Background
reducing by giving team members more control and power,
Reducing Overload and Restoring Team Health
performance
current performance as determinant of SLOs,
What to Measure: Using SLIs
KPI (key performance indicator), SLO compliance as,
Getting Started
performing (SRE team),
Performing
partnering on architecture,
Partnering on architecture
self-regulating workload,
Self-regulating workload
pets vs. cattle approach,
Increase Uniformity
pipeline components,
Types of components
SLIs for freshness, coverage, and correctness,
Pipeline freshness, coverage, and correctness
pipelines, data processing,
Data Processing Pipelines
Piper/Git-on-Borg version control system,
What We Decided to Do
Plan-Do-Check-Act (or PDCA) Cycle,
The Deming Cycle
planning by SRE and development teams,
Planning and Executing
platforms
everything important becomes a platform,
Everything Important Eventually Becomes a Platform
running, reliability and,
If You Run a Platform, Then Reliability Is a Partnership
playbooks, maintaining,
Training roadmap
entries for data processing pipelines,
Playbook entries
point fixes for paging alerts,
Rigor of follow-up
Pokémon GO on GCLB, case study,
Case Study 1: Pokémon GO on GCLB
positive behaviors,
Be positive
postmortems,
Postmortem Culture: Learning from Failure
bad postmortem example,
Case Study
flaws in,
Why Is This Postmortem Bad?
blameless,
Compare and Contrast
,
It’s Better to Fix It Yourself; Don’t Blame Someone Else
case study, rack decommission leading to service latency,
Case Study
conducting joint postmortems with customers,
Step 5: Practice, Practice, Practice
good postmortem example,
Good Postmortem
good writing practices used,
Why Is This Postmortem Better?
organizational incentives for,
Organizational Incentives
modeling and enforcing blameless behavior,
Model and Enforce Blameless Behavior
responding to postmortem culture failures,
Respond to Postmortem Culture Failures
rewarding postmortem outcomes,
Reward Postmortem Outcomes
sharing postmortems openly,
Share Postmortems Openly
results of postmortem analysis,
Results of Postmortem Analysis
templates for,
Tools and Templates
Google template,
Google’s template
other industry templates,
Other industry templates
tools for,
Postmortem Tooling
checklist,
Postmortem checklist
follow-up on postmortems,
Postmortem follow-up
other industry tools,
Other industry tools
postmortem analysis,
Postmortem analysis
postmortem creation,
Postmortem creation
storage,
Postmortem storage
precision in SLO alerts,
Alerting Considerations
preparations for incidents,
Prepare Beforehand
preventative actions in postmortems,
Concrete action items
,
Key action item characteristics missing
priorities
adjusting according to SLOs and error budget,
Adjusting Priorities According to Your SLOs and Error Budget
business and production, understanding,
Communicating Business and Production Priorities
prioritizing and triaging issues,
Prioritize and triage within one quarter
probers,
Generating Artificial Traffic
,
Introduction of SLOs: A Journey in Progress
,
What to Measure: Using SLIs
use at Evernote in monitoring,
Introduction of SLOs: A Journey in Progress
problem summary (postmortems),
Key details omitted
problems (simulated), practicing with customers,
Step 5: Practice, Practice, Practice
process documentation for data processing pipelines,
Process documentation
production
automation, covering in interviews with SREs,
Finding Your First SRE
boundaries between application development and,
Share Ownership with Developers
contributors to high pager load,
Pager load inputs
preexisting bugs,
Preexisting bugs
data processing pipeline readiness for,
Pipeline Production Readiness
managing services in DevOps and SRE,
Compare and Contrast
priorities, communication by SRE and developer teams,
Communicating Business and Production Priorities
production excellence reviews,
Production Excellence
wisdom from,
Work to Minimize Toil
production interrupts,
Production Interrupts
Production Readiness Reviews (PRRs),
Aligning Goals
,
Pipeline Production Readiness
,
SRE Engagement Model
productionizing a service,
Phase 2: Active Development
programming languages
configuration as code,
Separate Configuration and Resulting Data
designing accidental or ad hoc language features in configuration system,
Pitfall 2: Designing Accidental or Ad Hoc Language Features
failing to recognize configuration as programming language problem,
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
use for configuration,
What Is Configuration?
using existing general-purpose scripting languages for configuration,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
project lifecycle complexity, case study,
Case Study 2: Project Lifecycle Complexity
Prometheus monitoring system,
Prefer Loose Coupling
Prosci ADKAR model,
Background
,
How These Theories Apply to SRE
,
The Prosci ADKAR Model
,
What We Decided to Do
mapping implementation phase of change project,
Design
protocol buffers,
Integrating Custom Applications (In-House Software)
,
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
psychological safety
in on-call rotations,
Recap of “Being On-Call” Chapter of First SRE Book
interpersonal risk taking,
Problem Statement
regaining by identifying and alleviating psychological stressors,
Identify and alleviate psychosocial stressors
publication of postmortems,
Delayed publication
,
Promptness
Q
quality of service (QoS)
agreement on definition at Evernote,
Introduction of SLOs: A Journey in Progress
maintaining while increasing feature velocity,
Evernote’s SLO Story
quality SLI,
A Worked Example
QueryMap (AdWords example),
LogJoiner
scaling, calculations for
in multidatacenter design,
Calculations
QueryStore (AdWords example),
LogJoiner
scaling, calculations for,
Calculations
R
recall (SLO alerts),
Alerting Considerations
recovery efforts (in postmortems),
Key details omitted
region-level outages in data processing pipeline,
Region-level outage
regional groups of instances (RMiGs), autoscalers balancing instances across,
Avoiding Traffic Imbalance
relationships, sustaining between SRE and other teams,
Sustaining an Effective Ongoing Relationship
release candidate version,
Our Example Setup
release engineering,
Canarying Releases
and canarying,
Release Engineering and Canarying
principles,
Release Engineering Principles
releases
benefits of frequent, smaller releases,
Identification delay
canarying,
Canarying Releases
shepherding,
Release Shepherding
reliability
as a partnership if you run a platform,
If You Run a Platform, Then Reliability Is a Partnership
as most important feature,
Reliability Is the Most Important Feature
balancing release velocity and,
Balancing Release Velocity and Reliability
configuration and,
Configuration and Reliability
considering work on as specialized role,
Consider Reliability Work as a Specialized Role
decided by users, not monitoring,
Your Users, Not Your Monitoring, Decide Your Reliability
experimenting with relaxing SLOs,
Experimenting with Relaxing Your SLOs
improvements in, resulting from postmortems,
Highlight improved reliability
reliability hackathon for products at risk,
Reassessing When Ground Rules Start to Slip
reliability targets and error budgets,
Reliability Targets and Error Budgets
rename-and-shame,
Conclusion
repeating incidents, finding causes of,
Repeating incidents
replication toil,
Configuration-Induced Toil
automating for configuration,
Reducing Configuration-Induced Toil
reports on SLO compliance,
Dashboards and Reports
reproducible builds,
Release Engineering Principles
request-driven components,
Types of components
requests
grouping request types into buckets of similar availability requirements,
Alerting at Scale
specific mix of, bugs manifesting with,
New bugs
Requiem (postmortem storage tool),
Postmortem storage
reset time (SLO alerts),
Alerting Considerations
resources
metrics about resource consumption,
Calculations
monitoring resource usage,
Saturation
resource planning for data processing pipelines,
Implement Autoscaling and Resource Planning
unexpected growth in data processing pipeline, causing failures,
Unexpected resource growth
response times to pages,
Anatomy of Pager Load
reusing code in data processing pipelines,
Reusing code
revenue coverage,
Be Thoughtful and Disciplined
reviews, designing in SRE with customers,
Step 4: Design Reviews and Risk Analysis
revision control system, storing monitoring system configuration in,
Treat Your Configuration as Code
risk analysis in SRE with customers,
Step 4: Design Reviews and Risk Analysis
risks and mitigations for first SRE team,
Risks and mitigations
risks, identifying by SRE team to developer team,
Identifying Risks
roadmaps,
Planning and Executing
roll forward deployment vs. simple canary deployment,
A Roll Forward Deployment Versus a Simple Canary Deployment
rollback strategy for releases,
New bugs
configuration changes,
Safe Configuration Change Application
promptly removing bugs from production,
Mitigation delay
rolling update strategy,
Safe Configuration Change Application
root causes and trigger (in postmortems),
Blamelessness
,
Key details omitted
routing
anycast methodology,
Anycast
RPCs (remote procedure calls)
managing load with,
Lessons learned
monitoring system metrics on,
Dependencies
S
satellites,
Case Study
scaling,
Autoscaling
calculations for AdWords NALSD example,
Calculations
calculations for LogJoiner, QueryStore, ClickMap,, and QueryMap in AdWords example,
Calculations
during limited availability phase of service lifecycle,
Phase 3: Limited Availability
of SRE to larger environments,
Scaling SRE to Larger Environments
scalability of data processing pipeline,
Pipeline maturity matrix
Waze case study,
Background
scheduling on-call engineers,
On-Call Flexibility
scenario, a change in personal circumstances,
Scenario: A change in personal circumstances
automating on-call scheduling,
Automate on-call scheduling
planning for long-term breaks,
Plan for long-term breaks
planning for part-time work schedules,
Plan for part-time work schedules
planning for short-term swaps,
Plan for short-term swaps
scripting languages, general-purpose, using for configuration system,
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
security policies for data processing pipeline, adhering to,
Adhere to Access Control and Security Policies
self-healing,
New bugs
self-regulating workload (SRE team),
Self-regulating workload
self-service methods for users,
Build self-service interfaces
,
Provide Self-Service Methods
semantic validation (configuration),
Semantic validation
service complexity and forming more SRE teams,
Where to split
pitfalls of team splits,
Pitfalls
where to split the work,
Where to split
service level agreements (SLAs)
and dependency failures in data processing pipelines,
Plan for Dependency Failure
Google and Evernote,
Breaking Down the SLO Wall Between Customer and Cloud Provider
service level indicators (SLIs),
Implementing SLOs
abstracting your system into types of components,
Types of components
architecture for example mobile phone game,
A Worked Example
automation of collection of data at Home Depot,
The SLO Culture Project
canary metrics and,
Metrics Should Indicate Problems
changing SLI implementation,
Improving the Quality of Your SLO
dashboards showing SLI trends,
Dashboards and Reports
explaining to customers,
Step 1: SLOs and SLIs Are How You Speak
for example game service SLOs,
SLIs and SLOs
implementation,
What to Measure: Using SLIs
measurements with,
What to Measure: Using SLIs
measuring,
Measuring the SLIs
calculating SLIs over previous week,
Calculating the SLIs
moving from specification to implementation,
Moving from SLI Specification to SLI Implementation
API and HTTP server availability and latency,
API and HTTP server availability and latency
pipeline freshness, coverage, and correctness,
Pipeline freshness, coverage, and correctness
specifications,
What to Measure: Using SLIs
using to calculate starter SLOs,
Using the SLIs to Calculate Starter SLOs
service level objectives (SLOs),
Implementing SLOs
adjusting priorities according to,
Adjusting Priorities According to Your SLOs and Error Budget
alerting on,
Alerting on SLOs
considerations in,
Alerting Considerations
low-traffic services and error budget alerting,
Low-Traffic Services and Error Budget Alerting
making sure alerting is scalable,
Alerting at Scale
pager alerts,
Alerting
services with extreme availability goals,
Extreme Availability Goals
significant events,
Ways to Alert on Significant Events
by SRE and development teams for a service,
Setting Ground Rules
continuous improvement of SLO targets,
Continuous Improvement of SLO Targets
improving quality of SLOs,
Improving the Quality of Your SLO
decision making using SLOs and error budgets,
Decision Making Using SLOs and Error Budgets
defining and measuring for data processing pipelines,
Define and Measure Service Level Objectives
data correctness,
Data correctness
data freshness,
Data freshness
data isolation/load balancing,
Data isolation/load balancing
end-to-end measurement,
End-to-end measurement
defining before general availability phase of service lifecycle,
Phase 3: Limited Availability
design and implementation by your first SRE,
Bootstrapping Your First SRE
Evernote case study,
Evernote’s SLO Story
breaking down SLO wall between customer and cloud provider,
Breaking Down the SLO Wall Between Customer and Cloud Provider
current state of SLOs,
Current State
introduction of SLOs,
Introduction of SLOs: A Journey in Progress
why Evernote adopted SRE model,
Why Did Evernote Adopt the SRE Model?
example document for game service,
Example SLO Document
for Spotify event delivery system operation,
Event Delivery System Operation
skewness SLO,
Skewness
timeliness SLO,
Timeliness
fundamental importance in SRE,
SLO Engineering Case Studies
getting started with,
Getting Started
measurements using SLIs,
What to Measure: Using SLIs
reliability targets and error budgets,
Reliability Targets and Error Budgets
Home Depot case study,
The Home Depot’s SLO Story
applying VALET to batch applications,
Applying VALET to Batch Applications
automating VALET data collection,
Automating VALET Data Collection
evangelizing SLOs,
Evangelizing SLOs
first set of SLOs,
Our First Set of SLOs
future aspirations,
Future Aspirations
proliferation of SLOs,
The Proliferation of SLOs
SLO culture project,
The SLO Culture Project
using VALET in testing,
Using VALET in Testing
implementing, worked example,
A Worked Example
choosing appropriate time window,
Choosing an Appropriate Time Window
dashboards and reports,
Dashboards and Reports
documenting SLOs and error budget policy,
Documenting the SLO and Error Budget Policy
establishing error budget policy,
Establishing an Error Budget Policy
getting stakeholder agreement,
Getting Stakeholder Agreement
measuring the SLIs,
Measuring the SLIs
moving from SLI specification to implementation,
Moving from SLI Specification to SLI Implementation
using SLIs to calculate starter SLOs,
Using the SLIs to Calculate Starter SLOs
in SRE with customers,
Step 1: SLOs and SLIs Are How You Speak
auditing monitoring and building shared dashboards,
Step 2: Audit the Monitoring and Build Shared Dashboards
measuring and renegotiating,
Step 3: Measure and Renegotiate
managing by, in SRE,
Manage by Service Level Objectives (SLOs)
minimizing risk to by canarying releases,
Minimizing Risk to SLOs and the Error Budget
refining
experimenting with relaxing SLOs,
Experimenting with Relaxing Your SLOs
grading interaction importance,
Grading Interaction Importance
modeling dependencies,
Modeling Dependencies
modeling user journeys,
Modeling User Journeys
tracking performance over time at Evernote,
Tracking our performance over time
using for SRE practices without SREs,
SRE Practices Without SREs
using to reduce toil,
Use SLOs to Reduce Toil
why SREs need them,
Why SREs Need SLOs
service lifecycle, SRE engagement during,
The Service Lifecycle
abandoned phase,
Phase 6: Abandoned
active development phase,
Phase 2: Active Development
architecture and design phase,
Phase 1: Architecture and Design
deprecation phase,
Phase 5: Deprecation
general availability phase,
Phase 4: General Availability
limited availability phase,
Phase 3: Limited Availability
unsupported phase,
Phase 7: Unsupported
service reviews (regular), performing,
Performing Regular Service Reviews
services
multiple, supporting with single SRE team,
Supporting Multiple Services with a Single SRE Team
SRE rollout for,
SRE Rollout
sharded LogJoiner (AdWords example),
Calculations
sharing postmortems openly,
Share Postmortems Openly
shift length for on-call SREs,
On-Call Flexibility
short term goals (SRE team),
Setting Ground Rules
side effects, interleaving with configuration evaluation,
Pitfall 4: Interleaving “Configuration Evaluation” with “Side Effects”
silos, elimination of,
No More Silos
simplicity,
Simplicity Is End-to-End, and SREs Are Good for That
case study, end-to-end API simplicity,
Background
case study, project lifecycle complexity,
Case Study 2: Project Lifecycle Complexity
escaping in configuration,
Escaping Simplicity
,
Integrating the Configuration Language
regaining
case study, eliminating pDNS dependency on itself,
Background
case study, running hundreds of microservices on shared platform,
Background
case study, simplifying Display Ads Spiderweb,
Background
site reliability engineering,
How SRE Relates to DevOps
site reliability engineers,
Why SREs Need SLOs
skewness SLO (Spotify case study),
Skewness
SLAs,
Breaking Down the SLO Wall Between Customer and Cloud Provider
SLIs,
Implementing SLOs
SLOs,
Implementing SLOs
software engineering,
Finding Your First SRE
software-defined networking (SDN),
Background
source control, using with configurations,
Source Control
speed of data retrieval (monitoring system),
Speed
Spotify case study,
Case Study: Spotify
customer integration and support,
Customer Integration and Support
capacity planning,
Capacity planning
development process,
Development process
documentation,
Documentation
incident handling,
Incident handling
system monitoring,
System monitoring
event delivery,
Event Delivery
event delivery system design and architecture,
Event Delivery System Design and Architecture
data collection,
Data collection
data delivery,
Data delivery
extract, transform, load process,
Extract Transform Load
event delivery system operation,
Event Delivery System Operation
SRE (site reliability engineering)
about,
Background on SRE
comparing and contrasting with DevOps,
Compare and Contrast
development by Google and others,
SLO Engineering Case Studies
organizational context and fostering successful adoption,
Organizational Context and Fostering Successful Adoption
practices without SREs,
SRE Practices Without SREs
principles,
Background on SRE
managing by SLOs,
Manage by Service Level Objectives (SLOs)
moving fast by reducing cost of failure,
Move Fast by Reducing the Cost of Failure
sharing ownership with developers,
Share Ownership with Developers
using same tooling regardless of job title,
Use the Same Tooling, Regardless of Function or Job Title
working to minimize toil,
Work to Minimize Toil
reaching beyond your walls,
SRE: Reaching Beyond Your Walls
reasons for adoption by Evernote,
Why Did Evernote Adopt the SRE Model?
rollout for services,
SRE Rollout
SRE engagement model,
SRE Engagement Model
ending the relationship,
Ending the Relationship
scaling SRE to larger environments,
Scaling SRE to Larger Environments
service lifecycle,
The Service Lifecycle
setting up relationship with development team,
Setting Up the Relationship
sustaining an effective ongoing relationship,
Sustaining an Effective Ongoing Relationship
SRE teams
adjusting structures to changing circumstances,
Adapting SRE Team Structures to Changing Circumstances
cohesive distributed SRE teams, running,
Running Cohesive Distributed SRE Teams
forming new team at Google,
Initial scenario
afterword,
Afterword
initial scenario,
Initial scenario
maintaining playbooks,
Training roadmap
training,
Training roadmap
lifecycles,
SRE Team Lifecycles
making more SRE teams,
Making More SRE Teams
starting an SRE role,
Finding Your First SRE
suggested practices for running many teams,
Suggested Practices for Running Many Teams
your first SRE team,
Your First SRE Team
on-call engineers in survive the week culture,
Scenario: A culture of “survive the week”
single team supporting multiple services,
Supporting Multiple Services with a Single SRE Team
structuring multiple SRE team environment,
Structuring a Multiple SRE Team Environment
work overload when half a team leaves, case study,
Background
SREs (site reliability engineers)
being on-call,
On-Call
exchange program at Google,
SRE Exchange
funding and hiring,
SRE Funding and Hiring
mobility for,
SRE Mobility
starting an SRE role,
Finding Your First SRE
bootstrapping your first SRE,
Bootstrapping Your First SRE
distributed SREs,
Distributed SREs
finding your first SRE,
Finding Your First SRE
placing your first SRE,
Placing Your First SRE
training for,
Training
why they need SLOs,
Why SREs Need SLOs
work overload,
Identifying and Recovering from Overload
staging,
New bugs
stakeholders, getting agreement from on SLOs,
Getting Stakeholder Agreement
stateful systems
traffic teeing in,
Traffic Teeing
using autoscaling with,
Working with Stateful Systems
statsd metric aggregation daemon,
Prefer Loose Coupling
storage systems,
Types of components
alternatives to filer-based home directories,
What We Decided to Do
storming (first SRE team),
Storming
stressors (psychological), identifying and alleviating,
Identify and alleviate psychosocial stressors
string interpolation,
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
sunk cost fallacy,
Problem Statement
superfluous (undesirable) language in postmortems,
Animated language
support for services, deciding on,
When Can Substitute for Whether
survive the week culture,
Scenario: A culture of “survive the week”
empowering ops engineers in SRE,
Proposal one: Empower your ops engineers
improving team relations,
Proposal two: Improve team relations
swaps (short-term) in on-call scheduling,
Plan for short-term swaps
symptoms of overload,
Recognizing the Symptoms of Overload
system architecture, covering in interviews with SREs,
Finding Your First SRE
system diagrams for data processing pipeline,
System diagrams
systemic fixes for pager alerts,
Rigor of follow-up
systems
complexity of, measures for,
Measuring Complexity
keeping architectural drawings of,
Simplicity Is End-to-End, and SREs Are Good for That
maturity levels,
Getting Started
T
TCP,
Anycast
team, existing, converting to SRE team,
Converting a team in place
,
Norming
risks and mitigations for,
A team converted in place
templates
for postmortems,
Postmortem Templates
templating engines, using for configuration,
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
testing templates in a configuration system,
Testing
using for configurations,
Integrating the Configuration Language
testing
alerting logic in monitoring system,
Testing Alerting Logic
automated tests,
Release Engineering Principles
for configuration systems,
Testing
for preexisting bugs in production environment,
Preexisting bugs
quick fixes for bugs,
Mitigation delay
software testing to reduce bugs reaching production,
New bugs
testing pyramid philosophy in Spotify development process,
Development process
unit and integration testing, data processing pipeline,
Pipeline maturity matrix
The Home Depot (THD),
The Home Depot’s SLO Story
three Cs of incident management,
Incident Command System
tickets
new ticket SLO in perceived overload case study,
Background
P1-P5 tickets in Evernote/Google relationship,
Breaking Down the SLO Wall Between Customer and Cloud Provider
SLOs in Home Depot case study,
Tickets
support tickets for Home Depot services,
The SLO Culture Project
ticket toil,
Business Processes
tiered SRE engagement,
Outcomes
time for postmortems, lacking,
Lacking time to write postmortems
time windows for SLOs,
Choosing an Appropriate Time Window
at Evernote,
Introduction of SLOs: A Journey in Progress
timeliness SLO (Spotify case study),
Timeliness
toil
configuration-induced,
Configuration-Induced Toil
reducing,
Reducing Configuration-Induced Toil
getting ahead of by helping customers,
When Your Customers Have a Hard Time, You Have to Slow Down
metrics in work overload,
Recognizing the Symptoms of Overload
working to minimize in SRE,
Work to Minimize Toil
toil, eliminating,
Eliminating Toil
case study, decommissioning filer-backed home directories,
Case Study 2: Decommissioning Filer-Backed Home Directories
background,
Background
decision on the solution,
What We Decided to Do
design and implementation,
Design and Implementation
key components of the solution,
Moonwalk
lessons learned,
Lessons Learned
problem statement,
Problem Statement
case study, reducing toil in datacenter with automation,
Case Study 1: Reducing Toil in the Datacenter with Automation
background,
Background
decision on the solution,
What We Decided to Do
design first effort, Saturn line-card repair,
Design First Effort: Saturn Line-Card Repair
design second effort, Saturn vs. Jupiter line-card repair,
Implementation
implementation, Jupiter line-card repair,
Implementation
implementation, Saturn line-card repair with automation,
Implementation
lessons learned,
Lessons Learned
problem statement,
Problem Statement
characteristics and examples of toil,
What Is Toil?
measuring toil,
Measuring Toil
taxonomy of toil,
Toil Taxonomy
business processes,
Business Processes
cost engineering and capacity planning,
Cost Engineering and Capacity Planning
migrations,
Migrations
production interrupts,
Production Interrupts
release shepherding,
Release Shepherding
troubleshooting for opaque architectures,
Troubleshooting for Opaque Architectures
toil management strategies,
Toil Management Strategies
assessing risks in automation,
Assess Risk Within Automation
automating toil response,
Automate Toil Response
engineering toil out of the system,
Engineer Toil Out of the System
getting support from management and colleagues,
Get Support from Management and Colleagues
identifying and measuring toil,
Identify and Measure Toil
increasing uniformity,
Increase Uniformity
legacy systems,
Use Feedback to Improve
promoting toil reduction as a feature,
Promote Toil Reduction as a Feature
providing self-service methods,
Provide Self-Service Methods
rejecting toil,
Reject the Toil
starting small, then improving,
Start Small and Then Improve
starting with human-backed interfaces,
Start with Human-Backed Interfaces
using feedback to improve,
Use Feedback to Improve
using open source and third-party tools,
Use Open Source and Third-Party Tools
using SLOs to reduce toil,
Use SLOs to Reduce Toil
tooling
in DevOps and SRE,
Compare and Contrast
relationship with culture in DevOps,
Tooling and Culture Are Interrelated
using same tooling regardless of job title,
Use the Same Tooling, Regardless of Function or Job Title
tools
common tooling adoption in SRE, case study,
Background
for configuration systems,
Tooling
for incident response,
Tools used for incident response
for postmortems,
Postmortem Tooling
in configuration system,
Importance of Tooling
increasing uniformity in,
Increase Uniformity
using open source and third-party tools,
Use Open Source and Third-Party Tools
traffic teeing,
Traffic Teeing
traffic volume metrics,
The SLO Culture Project
SLOs in Home Depot case study,
Traffic volume
training
for incident response,
Incident Response Training
for SREs,
Training
new SRE team at Google,
Training roadmap
teaching customers,
You Will Need to Practice SRE with Your Customers
to reduce perceived work overload,
Mid-term actions
using postmortems to train new engineers,
Hold training exercises
travel for SRE teams,
Travel
triaging interrupts,
Lessons Learned
troubleshooting for opaque architectures,
Troubleshooting for Opaque Architectures
truncated exponential backoff,
Future-proofing
two-phase mutations,
Idempotent and Two-Phase Mutations
U
ulimit utility,
Guarding Against Abusive Configuration
unhealthy instances, handling,
Handling Unhealthy Machines
uniformity, increasing,
Increase Uniformity
,
Melt snowflakes
unsupported phase, service lifecycle,
Phase 7: Unsupported
user behaviors causing bugs to manifest,
New bugs
user journeys, modeling,
Modeling User Journeys
user-centric view (configuration),
Configuration Asks Users Questions
mandatory and optional configuration questions,
Mandatory and Optional Questions
questions asked should be close to user goals,
Questions Should Be Close to User Goals
users
deciding reliability,
Your Users, Not Your Monitoring, Decide Your Reliability
helping past difficulties,
When Your Customers Have a Hard Time, You Have to Slow Down
utilization
infrastructure utilization in Home Depot case study,
Infrastructure utilization
measurement in Home Depot case study,
The SLO Culture Project
monitoring system metrics on saturation,
Saturation
V
VALET (SLOs at Home Depot),
VALET
versioning, using with configurations,
Ownership and Change Tracking
,
Versioning
virtual machines run by cloud provider, availability of,
Breaking Down the SLO Wall Between Customer and Cloud Provider
visualizations,
Dashboards and Reports
for data processing pipeline,
Pipeline maturity matrix
volume (traffic),
The SLO Culture Project
in Home Depot VALET SLOs,
VALET
W
Waze, scaling, change management case study,
Background
wisdom of production,
Work to Minimize Toil
work overload,
Identifying and Recovering from Overload
workloads
distributing between geographically split SRE teams,
Parity: Distributing Work Between Offices and Avoiding a “Night Shift”
SRE teams having complete self-determination of,
Performing
SRE teams regulating,
Your First SRE Team
workload coverage,
Be Thoughtful and Disciplined
X
x20 filesystem,
What We Decided to Do
Y
YAML,
Generating Config in Specific Formats
configs written in, JSON and,
Integrating the Configuration Language
JSON object encoded as YAML streams in Kubernetes,
What Kubernetes Provides
