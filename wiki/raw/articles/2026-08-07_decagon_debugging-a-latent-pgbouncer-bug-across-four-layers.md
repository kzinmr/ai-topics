---
title: "How we debugged a latent PgBouncer bug across four layers of the stack"
source: "Decagon Blog"
url: "https://decagon.ai/blog/debugging-a-latent-pgbouncer-bug-across-four-layers"
scraped: "2026-08-07T06:00:40.326866+00:00"
lastmod: "None"
type: "sitemap"
---

# How we debugged a latent PgBouncer bug across four layers of the stack

**Source**: [https://decagon.ai/blog/debugging-a-latent-pgbouncer-bug-across-four-layers](https://decagon.ai/blog/debugging-a-latent-pgbouncer-bug-across-four-layers)

Decagon Dialogues 2026 is here.
Register today
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Duet AI partner
Build
AOPs
Workflows for AI agents
Integrations
Support for tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & reporting
Voice of the customer
Watchtower
Always on QA
Suggestions
AI powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Security
Sign in
Get a demo
Sign in
Get a demo
Research & Technology
How we debugged a latent PgBouncer bug across four layers of the stack
Posted on
August 5, 2026
Jon Wong
Member of Technical Staff, Infra
Article
Table of contents
Introduction
What is an Agent Engineer?
Subscribe to our Newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Must be a valid company email (i.e. example@companydomain.com)
Get a demo
Done!
Oops! Something went wrong while submitting the form.
Recently, we migrated Decagon from GCP's managed connection pooler to self-managed PgBouncer. Because GCP's managed pooler also uses PgBouncer, we expected the migration to be straightforward. The overall data path remained the same — requests would still travel from the application through PgBouncer to Postgres over the same wire protocol.
Staging seemed to validate that assumption. But during our initial production canary, a small number of voice requests began stalling mid-conversation and timing out after exactly 300 seconds.
The initial signals didn't appear to be related. Sentry showed a handful of "SSL connection has been closed unexpectedly" errors, while other requests failed much earlier with SQLAlchemy connection-pool exhaustion. The SSL errors only appeared after PostgreSQL's idle-in-transaction session timeout terminated the stalled sessions, making them look like isolated connection failures.
Read on to see how we tracked the bug down by tracing a single database response through every layer between Postgres and our application.
The first clue: Postgres wasn't the problem
The investigation began with an error from SQLAlchemy's connection pool:
sqlalchemy.exc.TimeoutError: QueuePool limit of size 2 overflow 20 reached, connection timed out, timeout 30.00
‍
At first glance, it looked like the application had simply run out of database connections. But the surrounding signals did not match a capacity problem. Postgres query latency remained at 1–3 milliseconds at p95, and PgBouncer's
maxwait
—the time clients spent waiting for a server connection—stayed at zero.
The most useful clue came from comparing the application and database timelines. Postgres consistently finished the affected queries in milliseconds, yet the corresponding application spans remained open for exactly 300 seconds before finally returning the expected rows. The affected stack traces all pointed to the application's database call.
The discrepancy also explained why we were seeing two seemingly unrelated failures. The 300-second stalls kept connections checked out from SQLAlchemy's QueuePool, while other requests timed out after 30 seconds waiting to borrow those same connections.
That changed the direction of the investigation. Postgres wasn't slow, and the queries weren't hanging. The application was still blocked waiting for a query that Postgres had already finished.
Postgres finishes the query, but the application stays blocked for 300 seconds.
Following the response through four layers
At this point, we knew the response was getting stuck somewhere after Postgres. To find where the response stopped, we traced it through four parts of the stack:
SQLAlchemy's QueuePool
PgBouncer's packet parser and event loop
OpenSSL's TLS record buffer
The Linux kernel's
epoll()
interface
PostgreSQL's
application name
parameter identifies queries in logs and monitoring tools. We set it to the current request path so we could attribute database activity to individual endpoints. Whenever the value changes, Postgres sends the new value back to the client in a ParameterStatus packet.
After reproducing the stall, we narrowed it down to three conditions:
The application name parameter was set to a new value longer than 41 bytes, producing a ParameterStatus packet larger than 64 bytes.
The query response landed in a narrow size range that caused the ParameterStatus packet to cross a 4096-byte read buffer in PgBouncer.
Both parts of the split packet were carried in the same TLS record between Postgres and PgBouncer.
The first two conditions had existed in our system for some time. Migrating away from GCP's managed connection pooler introduced the third by enabling a different TLS path between PgBouncer and Postgres, supplying the missing third condition. That completed the set of conditions that exposed the bug.
In our backend API, only two endpoints generated application name values long enough to satisfy the first condition. Even on those endpoints, only a small fraction of query responses landed on the required buffer boundary. The bug was deterministic for those exact response layouts, but the layouts themselves were rare, which is what caused the bug to not trigger in staging.
The bug: OpenSSL had bytes epoll() could not see
PgBouncer's read loop is straightforward: wait for
epoll()
to report that a socket is readable, copy the available data into its read buffer, parse PostgreSQL messages, and repeat.
That assumption holds when reading directly from a socket.
TLS complicates things.
SSL_read()
, an OpenSSL function, first drains an entire TLS record from the kernel socket into OpenSSL's internal buffer. It decrypts the data and returns plaintext to the caller. If the caller requests fewer bytes than are available, the remaining plaintext stays buffered inside OpenSSL even though the kernel socket has already been drained.
For example, in one reproduction case:
Postgres returned a single
4,118-byte TLS record.
PgBouncer read its normal
4,096-byte buffer.
An
86-byte ParameterStatus packet straddled that buffer boundary.
PgBouncer saw only the first
70 bytes of the ParameterStatus packet, concluded it needed more data, and returned to waiting on
epoll()
.
The remaining
16 bytes
were already available—but they were buffered inside OpenSSL rather than the kernel socket. Because PgBouncer returned to
epoll()
without first checking
SSL_pending()
, nothing ever woke the connection again.
Sixteen response bytes remain buffered in OpenSSL, while PgBouncer waits on an empty socket.
Why unrelated requests started failing
The stalled query was only the first-order effect.
Because it was blocked inside
cursor.execute()
, its database connection never returned to SQLAlchemy's QueuePool. The query had already finished on Postgres, but from SQLAlchemy's perspective the connection was still in use. It remained checked out until Postgres eventually killed the session after 300 seconds via its configured idle session timeout.
A few wedged connections were enough to reduce the effective size of the connection pool. Once that happened, unrelated requests started queueing behind healthy connections and eventually failed with pool exhaustion.
The key observation was that the triggering requests and the impacted requests were usually different.
Only a small number of endpoints satisfied the conditions needed to wedge a connection, but once a connection was poisoned,
any
request sharing that process-level QueuePool could become the next victim.
Wedged connections shrink the pool, causing unrelated requests to time out.
Mitigation and upstream fix
We addressed the issue in two ways: an application-level mitigation and an upstream fix.
In our application, we shortened the application name parameter, ensuring the resulting ParameterStatus packet stayed below PgBouncer's small-packet parsing threshold. That removed one of the three conditions required to trigger the bug and let us continue the migration safely.
Upstream, we proposed a fix for the underlying event-loop bug. The issue wasn't specific to our application or our traffic pattern — it was that PgBouncer went back to waiting on
epoll()
without checking whether OpenSSL already had decrypted bytes buffered internally.
The fix is surprisingly small: before sleeping, check
SSL_pending()
. If OpenSSL already has plaintext available, continue reading instead of waiting for another kernel event that will never arrive.
That eliminates the deadlock regardless of packet size or response layout.
Takeaways
One important lesson from this investigation is that infrastructure migrations don't just change your own systems — they can also expose latent bugs elsewhere in the stack. In this case, moving to self-managed PgBouncer introduced the final condition needed to surface a long-standing edge case involving SQLAlchemy, PgBouncer, OpenSSL, and the PostgreSQL wire protocol.
We were able to mitigate this issue quickly in production, and the investigation ultimately led to an upstream fix in PgBouncer's source code.
Jon Wong
—
Member of Technical Staff, Infra
Jonathan Wong is an engineer on the Infrastructure team. Outside of work, he enjoys reading and spending time with his dachshund, Kirby.
“With Decagon Voice, we’re able to combine high performance and seamless brand customization with cross-channel memory, ensuring every interaction is connected and true to Chime’s member-first values.”
Janelle Sallenave
Chief Operating Officer
Start improving your workflow with Decagon
With Decagon, CX teams don’t have to guess whether a change will improve CSAT or deflection. They can move quickly, measure what matters, and act on what works.
Get a demo
Your browser does not support the video tag.
Join us
There are very few places where you can prototype with frontier LLMs, ship to production in days, and watch users engage with the systems you built—all while owning the entire stack, from intent parsing and tool usage to API integration and observability. This role at Decagon is one of those places.
From my own experience working across both agent development and broader engineering initiatives at Decagon, I’ve seen firsthand how uniquely impactful this work can be. Whether I’m building intelligent workflows for customers or designing infrastructure that supports our agent platform, it’s rare to find an environment where the work transitions from concept to production within days, actively powering user experiences and transforming how businesses operate.
If you’re looking for a role where you can:
Build at the frontier of LLMs, automation, and user interaction
Deploy AI agents that solve high-value business use cases across industries including retail, travel and hospitality, fintech, edtech, and more
Work directly with customers on high-impact use cases
Ship fast, iterate constantly, and own your work from idea to production
Join a fast-moving, collaborative team solving real-world challenges with AI
We’d love to hear from you!
Explore careers
Related posts
Research & Technology
What an air-gapped AI deployment actually requires
Posted on
July 9, 2026
Research & Technology
DuetBench: An evaluation of self-improving customer service agents
Posted on
June 9, 2026
Research & Technology
Why MCP alone isn’t enough for reliable agent tool use
Posted on
April 14, 2026
Explore more topics
AI agent building
Test & experimentation
Analytics & Voice of Customer
Voice & omnichannel support
Guardrails, security, & governance
Use cases & experiences
Workplace
The AI concierge for every customer.
Get a demo
Footer
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
