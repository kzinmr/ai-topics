---
title: The Art of SLOs — slides
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- documentation
sources:
- https://sre.google/resources/practices-and-processes/art-of-slos/
source_url: https://sre.google/resources/practices-and-processes/art-of-slos/
ingested: '2026-10-14'
date_unknown: true
license: CC-BY-4.0
attribution: Google Customer Reliability Engineering
content_kind: mechanical_pdf_text_extraction
original_pdf: slides.pdf
original_sha256: e07893ec29528e78f18af18ddfb3ebd3cb390d451dbde38382eb94e374103a80
sha256: 33f58d9d77da1b57768110fe86a3c0db1772d260405563ce2e640e30a0bf8d8a
page_count: 98
extraction_note: Reading aid; PDF remains authoritative for diagrams, tables and text
  ordering.
---
## PDF page 1

https://cre.page.link/art-of-slos-slides
The Art of SLOs
In the midst of chaos, there is also opportunity reliability
— Sun Tzu, The Art of War


## PDF page 2

https://cre.page.link/art-of-slos-slides
Welcome!
Don't be shy … say hello to your neighbours

## PDF page 3

https://cre.page.link/art-of-slos-slides
Group Agreements
⁄ We’re here to learn
⁄ Please ask questions (raise your hand)
⁄ One speaker at a time
⁄ Assume positive intent
⁄ “Why am I speaking?”

## PDF page 4

https://cre.page.link/art-of-slos-slides
Agenda
⁄ Terminology
⁄ Why your services need SLOs
⁄ Spending your error budget
⁄ Choosing a good SLI
⁄ Developing SLOs and SLIs


## PDF page 5

https://cre.page.link/art-of-slos-slides
Service Level Indicator
A quantiﬁable measure of service reliability

## PDF page 6

https://cre.page.link/art-of-slos-slides
Service Level Objectives
Set a reliability target for an SLI

## PDF page 7

https://cre.page.link/art-of-slos-slides
Users? Customers?
Customers are users who directly pay for a service

## PDF page 8

https://cre.page.link/art-of-slos-slides
Services Need SLOs

## PDF page 9

https://cre.page.link/art-of-slos-slides
Don't believe us?
"Since introducing SLOs, the relationship between our operations
and development teams has subtly but markedly improved."
— Ben McCormack, Evernote; The Site Reliability Workbook, Chapter 3
"... it is diﬃcult to do your job well without clearly deﬁning well.
SLOs provide the language we need to deﬁne well."
— Theo Schlossnagle, Circonus; Seeking SRE, Chapter 21

## PDF page 10

https://cre.page.link/art-of-slos-slides
The most
 important feature
of any system
is its reliability
➊

## PDF page 11

https://cre.page.link/art-of-slos-slides
Operators
Stability
How do you 
incentivize
reliability?
Developers
Agility

## PDF page 12

https://cre.page.link/art-of-slos-slides
A principled way
to agree on the 
desired reliability
of a service


## PDF page 13

https://cre.page.link/art-of-slos-slides
What does "reliable" mean?
Think about Netﬂix, Google Search, Gmail, Twitter…
how do you tell if they are ‘working’?

## PDF page 14

https://cre.page.link/art-of-slos-slides
0 ms 300 ms200 ms
Customer“HTTP GET / …”
“Ugh”
Objective  
Agreement 


## PDF page 15

https://cre.page.link/art-of-slos-slides
With me so far?

## PDF page 16

https://cre.page.link/art-of-slos-slides
When do we need to make
a service more reliable?

## PDF page 17

https://cre.page.link/art-of-slos-slides
100%
100% is the wrong reliability target for basically everything
— Benjamin Treynor Sloss, VP 24x7, Google; Site Reliability Engineering, Introduction

## PDF page 18

https://cre.page.link/art-of-slos-slides
😡😋
SLOs should capture the performance and availability levels that, 
if barely met, would keep the typical customer of a service happy
“meets SLO targets” ⇒ “happy customers”
“sad customers” ⇒ “misses SLO targets”


## PDF page 19

https://cre.page.link/art-of-slos-slides
Measure SLO 
achieved & try 
to be slightly 
over target...
Target
SLI


## PDF page 20

https://cre.page.link/art-of-slos-slides
…but don’t be
too much better
or users will
depend on it
"Workﬂow", Randall Munroe, XKCD
Source: https:/ /xkcd.com/1172/
Target
!
SLI


## PDF page 21

https://cre.page.link/art-of-slos-slides
Error Budgets
An SLO implies an acceptable level of unreliability
This is a budget that can be allocated

## PDF page 22

https://cre.page.link/art-of-slos-slides
Implementation Mechanics
Evaluate SLO performance over a set window, e.g. 28 days
Remaining budget drives prioritization of engineering effort

## PDF page 23

https://cre.page.link/art-of-slos-slides
ITIL Approximation
Service in SLO → most operational work is a standard change
Service close to being out of SLO → revert to normal change
(No, I don't understand the difference between "standard" and "normal" either…)

## PDF page 24

https://cre.page.link/art-of-slos-slides
What should we spend
our error budget on?

## PDF page 25

https://cre.page.link/art-of-slos-slides
Error budgets can accommodate
⁄ releasing new features
⁄ expected system changes
⁄ inevitable failure in hardware, networks, etc.
⁄ planned downtime
⁄ risky experiments


## PDF page 26

https://cre.page.link/art-of-slos-slides
⁄ Dev team becomes self-policing
The error budget is a valuable resource for them
⁄ Shared responsibility for system uptime
Infrastructure failures eat into the error budget
⁄ Common incentive for devs and SREs
Find the right balance between innovation and reliability
⁄ Dev team can manage the risk themselves
They decide how to spend their error budget
⁄ Unrealistic reliability goals become unattractive
These goals dampen the velocity of innovation
Beneﬁts of error budgets

## PDF page 27

https://cre.page.link/art-of-slos-slides
Still with me?

## PDF page 28

https://cre.page.link/art-of-slos-slides
Activity
Reliability Principles

## PDF page 29

https://cre.page.link/art-of-slos-slides
Dear Colleagues,
The negative press from our 
recent outage has convinced me that 
we all need to take the reliability of 
our services more seriously. In this 
open letter, I want to lay down three 
reliability principles to guide your 
future decision making.

## PDF page 30

https://cre.page.link/art-of-slos-slides
 
1. ... rebuild user trust by making a 
ﬁnancial commitment to reliability.
2. ... ﬁnd ways to help our users 
tolerate or enjoy future outages.
3. ... meet our users expectations of 
reliability before building features.
4. ... build the features that make our 
users happy faster.
5. ... never suffer another outage,
ever again!
The ﬁrst principle concerns our users. 
We let them down, but they deserve 
better. They deserve to be happy 
when using our services!
Our business must ...

## PDF page 31

https://cre.page.link/art-of-slos-slides
 
1. … choose to fail fast and catch 
errors early through rapid iteration.
2. … have Ops engage in the design of 
new features to reduce risk. 
3. … only release new features publicly 
when they are shown to be reliable.
4. … build and release software in 
small, controlled steps.
5. … reduce feature iteration speed 
when our systems are unreliable.
The second principle concerns the 
way we build our services. We have to 
change our development process to 
incorporate reliability. 
Our business must...


## PDF page 32

https://cre.page.link/art-of-slos-slides
 
1. … share responsibility for reliability 
between Ops and Dev teams.
2. … tie operational response and 
team priorities to a reliability goal.
3. … make our systems more resilient 
to failure to cut operational load.
4. … give Ops a veto on all releases to 
prevent failures reaching our users.
5. … route negative complaints on 
Twitter directly to Ops pagers.
The third principle concerns our 
operational practices. What we're 
doing today isn't working. Our Ops 
teams are burned out and our 
incident rate is too high. We have to 
do things differently to improve!
Our business must...
 

## PDF page 33

https://cre.page.link/art-of-slos-slides
To put these principles into practice, 
we are going to borrow some ideas 
from Google! The next step is to 
deﬁne some SLOs for our  services 
and begin tracking our performance 
against them.
Thanks for reading!
Eleanor Exec, CEO

## PDF page 34

https://cre.page.link/art-of-slos-slides
Break!

## PDF page 35

https://cre.page.link/art-of-slos-slides
Choosing a Good SLI

## PDF page 36

https://cre.page.link/art-of-slos-slides

## PDF page 37

https://cre.page.link/art-of-slos-slides
time
unhappy
users


## PDF page 38

https://cre.page.link/art-of-slos-slides
timetime
metric metricBAD GOOD

## PDF page 39

https://cre.page.link/art-of-slos-slides
timetime
metric
Variance obscures
metric deterioration 
metricBAD GOOD

## PDF page 40

https://cre.page.link/art-of-slos-slides
time
metric
Metric deterioration
correlates with outage
metric
time
BAD GOOD

## PDF page 41

https://cre.page.link/art-of-slos-slides
timetime
metric
Metric provides poor
signal-to-noise ratio
Metric provides good
signal-to-noise ratio
metric
?
✓
BAD GOOD

## PDF page 42

https://cre.page.link/art-of-slos-slides
SLO SLI

## PDF page 43

https://cre.page.link/art-of-slos-slides
SLI : good events
valid events × 100%

## PDF page 44

https://cre.page.link/art-of-slos-slides
 3–5 SLIs*
* per user journey

## PDF page 45

https://cre.page.link/art-of-slos-slides
SLO SLI

## PDF page 46

https://cre.page.link/art-of-slos-slides
What performance
does the 
business need?

## PDF page 47

https://cre.page.link/art-of-slos-slides
User expectations
are strongly tied to
past performance

## PDF page 48

https://cre.page.link/art-of-slos-slides
?
Continuous
Improvement

## PDF page 49

https://cre.page.link/art-of-slos-slides
Information 
overload?

## PDF page 50

https://cre.page.link/art-of-slos-slides
Developing SLOs and SLIs

## PDF page 51

https://cre.page.link/art-of-slos-slides
?

## PDF page 52

https://cre.page.link/art-of-slos-slides
Our Game: Fang Faction
Web Server
API Server
Leaderboards
User Proﬁles
Game Servers
Leaderboard
GenerationLoad
Balancer

## PDF page 53

https://cre.page.link/art-of-slos-slides
SomeUser's Profile
SomeUser
Tribe of Frog
Faction Score: 31337
Midwest Canyon
https:/ /fangfactiongame.com/proﬁle/someuser
Faction Name: Tribe of Frog
Leader Name: SomeUser
Email Address: user@example.com
Update1.
2.
3.
4.
5.
6.
Tri-Bool 65535
Tri Repetae 61995
Triassic Five52391
Tricksy Hobbits37164
Tribe of Frog31337
Trite Examples29243

## PDF page 54

https://cre.page.link/art-of-slos-slides
Loading a Profile Page
API Server
Leaderboards
User ProﬁlesLoad
Balancer
Game Servers
Leaderboard
Generation
Web Server

## PDF page 55

https://cre.page.link/art-of-slos-slides
Request / Response Availability
Latency
Quality
Data Processing Coverage
Correctness
Freshness
Throughput
Storage Throughput
Latency
SLI Menu

## PDF page 56

https://cre.page.link/art-of-slos-slides
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 57

https://cre.page.link/art-of-slos-slides
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 58

https://cre.page.link/art-of-slos-slides
The proportion of valid requests
  served faster than a threshold.
The proportion of valid requests
  served successfully.
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 59

https://cre.page.link/art-of-slos-slides
The proportion of valid requests
  served faster than a threshold.
The proportion of valid requests
  served successfully.
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 60

https://cre.page.link/art-of-slos-slides
The proportion of HTTP GET requests
  for /proﬁle/{user}
  served faster than a threshold.
The proportion of HTTP GET requests
  for /proﬁle/{user} or /proﬁle/{user}/avatar
  served successfully.
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 61

https://cre.page.link/art-of-slos-slides
The proportion of HTTP GET requests
  for /proﬁle/{user}
  served faster than a threshold.
The proportion of HTTP GET requests
  for /proﬁle/{user} or /proﬁle/{user}/avatar
  served successfully.
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 62

https://cre.page.link/art-of-slos-slides
The proportion of HTTP GET requests
  for /proﬁle/{user}
  served within X ms.
The proportion of HTTP GET requests
  for /proﬁle/{user} or /proﬁle/{user}/avatar
  that have 2XX, 3XX or 4XX (excl. 429) status.
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 63

https://cre.page.link/art-of-slos-slides
Measurement Strategies Application-level Metrics
Logs Processing
Front-end Infra Metrics
Synthetic Clients/Data
Client-side Instrumentation
SLI Menu

## PDF page 64

https://cre.page.link/art-of-slos-slides
The proportion of HTTP GET requests
  for /proﬁle/{user}
  that send their entire response within X ms
  measured at the load balancer.
The proportion of HTTP GET requests
  for /proﬁle/{user} or /proﬁle/{user}/avatar
  that have 2XX, 3XX or 4XX (excl. 429) status 
  measured at the load balancer.
● How do we deﬁne success?
● Where is the success / failure recorded?
● How do we deﬁne quickly?
● When does the timer start / stop?
The proﬁle page should load successfully The proﬁle page should load quickly
Availability Latency

## PDF page 65

https://cre.page.link/art-of-slos-slides
Activity
Postmortem

## PDF page 66

https://cre.page.link/art-of-slos-slides
Proportion of HTTP GET requests
  for /proﬁle/{user} or /proﬁle/{user}/avatar
  that have 2XX, 3XX or 4XX (excl. 429) status
  measured at the load balancer
and
Proportion of HTTP GET requests
  for /proﬁle/prober_user and all linked resources
  returning valid HTML containing "ProberUser"
  measured by a black-box prober every 5s
Proportion of HTTP GET requests
  for /proﬁle/{user}
  that send their entire response within X ms
  measured at the load balancer
Availability Latency

## PDF page 67

https://cre.page.link/art-of-slos-slides
Do the SLIs cover the failure modes?
API Server
Leader Boards
User Proﬁles
Load
Balancer
Black Box
Prober
Availability
Availability
Latency
Game Servers
Leaderboard
Generation
Web Server

## PDF page 68

https://cre.page.link/art-of-slos-slides
Activity
Deﬁne SLO Targets

## PDF page 69

https://cre.page.link/art-of-slos-slides
What goals should we set for the reliability of our 
journey?
Service SLO Type Objective
Web: User Proﬁle Availability 
Web: User Proﬁle Latency 
... ... 
99.95% successful in previous 28d 
90% of requests < 500ms in previous 28d
Your objectives should have both a target and a measurement window

## PDF page 70

https://cre.page.link/art-of-slos-slides
Fallen asleep yet?

## PDF page 71

https://cre.page.link/art-of-slos-slides
Break!

## PDF page 72

https://cre.page.link/art-of-slos-slides
Workshop: Let's develop some more SLIs and SLOs!
Follow the process we demonstrated for the Buy In-Game Currency journey:
1. Choose SLI speciﬁcations from the menu (see booklet, p6)
2. Substitute deﬁnitions in to create a detailed SLI implementation
3. Walk through user journey and look for coverage gaps
4. Set aspirational SLOs based on business needs
Once you're done, choose another journey as a group.
You have roughly 45 minutes for each journey.

## PDF page 73

https://cre.page.link/art-of-slos-slides
Our Game: Fang Faction
Web Server
API Server
Leaderboards
User Proﬁles
Game Servers
Leaderboard
GenerationLoad
Balancer
Play
Store

## PDF page 74

https://cre.page.link/art-of-slos-slides
Break!

## PDF page 75

https://cre.page.link/art-of-slos-slides
Buy In-Game Currency
Model Answer

## PDF page 76

https://cre.page.link/art-of-slos-slides
Break Down
The Journey
Five request/response pairs
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
1
2
3
4 5

## PDF page 77

https://cre.page.link/art-of-slos-slides
Break Down
The Journey
Journey has two parts. A: Fetch SKUs
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
1
2

## PDF page 78

https://cre.page.link/art-of-slos-slides
Break Down
The Journey
Journey has two parts. B: Buy Item
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store 3
4 5

## PDF page 79

https://cre.page.link/art-of-slos-slides
Break Down
The Journey
User might choose not to buy an item :-(
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
We have to treat these parts separately!
1
2

## PDF page 80

https://cre.page.link/art-of-slos-slides
Break Down
The Journey
Two requests don't hit API server at all!
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
Server or load balancer metrics may not 
give enough coverage of the journey :-(
2
3

## PDF page 81

https://cre.page.link/art-of-slos-slides
Break Down
The Journey
Two requests don't hit API server at all!
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
Server or load balancer metrics may not 
give enough coverage of the journey :-(
… we'll have to ask our users to consent
to client-side telemetry.
2
3

## PDF page 82

https://cre.page.link/art-of-slos-slides
Buy Flow
What SLIs?
Buy Flow journey is
Request / Response
SLI menu suggests we use
Availability and Latency SLIs

## PDF page 83

https://cre.page.link/art-of-slos-slides
Buy Flow Availability:
Speciﬁcation
B makes money, so let's start with that
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
Availability SLI Speciﬁcation
    The proportion of valid requests
      served successfully.
3
4 5

## PDF page 84

https://cre.page.link/art-of-slos-slides
Buy Flow Availability:
Valid Requests
Availability SLI
    The proportion of valid requests
      served successfully.
… but which requests are valid?
3. User launches Play billing ﬂow
4. Send token to API server?
5. Verify token with Play Store?
Launching the billing ﬂow indicates
a user's intent to buy a product
Users consenting to client-side telemetry
collection allows us to track this intent
3

## PDF page 85

https://cre.page.link/art-of-slos-slides
Buy Flow Availability:
Success Criteria
Availability SLI
    The proportion of launched billing ﬂows
      from users consenting to collection
      served successfully.
… and how do we determine success?
All interactions must be successful!
3. Good status code; purchase token
4. Good status code; account updated
5. Good status code; valid token
○ Return 402 to API call
when token is invalid
3
4 5

## PDF page 86

https://cre.page.link/art-of-slos-slides
Buy Flow Availability:
Measurement
Availability SLI
    The proportion of launched billing ﬂows
      from users consenting to collection
      where the billing ﬂow returns:
● OK and a purchase token
● or FEATURE_NOT_SUPPORTED
● or ITEM_UNAVAILABLE
● or USER_CANCELED
      and /api/completePurchase returns:
● 200 OK and Parseable JSON
● or 402 Payment Required
   … but where are we measuring this?
3
4

## PDF page 87

https://cre.page.link/art-of-slos-slides
Buy Flow Availability:
Measurement
Availability SLI
    The proportion of launched billing ﬂows
      from users consenting to collection
      where the billing ﬂow returns:
● OK
● or FEATURE_NOT_SUPPORTED
● or ITEM_UNAVAILABLE
● or USER_CANCELED
      and /api/completePurchase returns:
● 200 OK
● or 402 Payment Required
● and Parseable JSON
      
      measured by the game client and
      reported back asynchronously.
3
4

## PDF page 88

https://cre.page.link/art-of-slos-slides
Buy Flow Latency:
Speciﬁcation
We want to measure latency for B too!
1. Fetch list of SKUs from API server
2. Fetch SKU details from Play Store
3. User launches Play billing ﬂow
4. Send token to API server
5. Verify token with Play Store
Latency SLI Speciﬁcation
    The proportion of valid requests
      served faster than a threshold.
3
4 5

## PDF page 89

https://cre.page.link/art-of-slos-slides
Buy Flow Latency:
Valid Requests
Latency SLI
    The proportion of valid requests
      served faster than a threshold.
… but which requests are valid?
3. User launches Play billing ﬂow?
4. Send token to API server
5. Verify token with Play Store?
Why not 3?
● Too variable, SLI will have poor SnR
● Billing ﬂow contains lots of "poking
device with a ﬁnger" time
4

## PDF page 90

https://cre.page.link/art-of-slos-slides
Buy Flow Latency:
"Too Slow" Threshold
Latency SLI
    The proportion
      of /api/completePurchase requests
      served faster than a threshold.
… and what is fast enough?
Rough estimate time!
● Verify Token <= 500ms
● Database Write <= 200ms
● Round up a bit…


## PDF page 91

https://cre.page.link/art-of-slos-slides
Buy Flow Latency:
Measurement
Latency SLI
    The proportion
      of /api/completePurchase requests
      served within 1000ms.
… but where are we measuring this?
Where does the timer start/stop?


## PDF page 92

https://cre.page.link/art-of-slos-slides
Buy Flow Latency:
Measurement
Latency SLI
    The proportion
      of /api/completePurchase requests
      where the complete response is
      returned to the client within 1000ms
      measured at the load balancer.


## PDF page 93

https://cre.page.link/art-of-slos-slides
A brief word from
our sponsors...

## PDF page 94

https://cre.page.link/art-of-slos-slides
https://cre.page.link/art-of-slos

## PDF page 95

https://cre.page.link/art-of-slos-slides
Want to learn more about SLOs? Take our course on Coursera:
https:/ /cre.page.link/coursera


## PDF page 96

https://cre.page.link/art-of-slos-slides
Both of these are now available in HTML format for free!
https:/ /landing.google.com/sre/books/


## PDF page 97

https://cre.page.link/art-of-slos-slides
Thanks!
Please ﬁll in the feedback form
Insert QR code link
to feedback form
in this space! 
Insert QR code link
to feedback form
in this space! 

## PDF page 98

https://cre.page.link/art-of-slos-slides
Q&A
Please ask our panelists questions!

