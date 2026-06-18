---
title: "LLM Serving Fairness"
source: "Cohere Blog"
url: "https://cohere.com/blog/serving-fairness"
scraped: "2026-06-18T06:00:40.227519+00:00"
lastmod: "2026-06-17"
type: "sitemap"
---

# LLM Serving Fairness

**Source**: [https://cohere.com/blog/serving-fairness](https://cohere.com/blog/serving-fairness)

Running large language models as a multi-tenant SaaS platform comes with a deceptively hard problem: many organizations share the same pool of GPUs, and their traffic is bursty and uneven. Left unmanaged, one customer's spike can become every other customer's latency problem.
In this blog post, we’ll walk you through Cohere’s new solution to scheduling inference requests
fairly
across tenants, using a combination of architectural patterns and a classic scheduling algorithm.
The problem: the noisy neighbor
Inference is most efficient when requests are processed in batches. A GPU that’s been fed a full batch runs hot and economically, while one handling a single request at a time mostly sits idle. So, requests queue up briefly and get packed into batches before hitting the hardware.
The catch is
ordering
. Imagine a naive queue: a single, shared line ordered only by priority and deadline. Now, consider what happens when one organization fires 10,000 requests in a burst while a second organization sends just five. With a single global queue, the 10,000 requests pile in front, and the five well-behaved requests wait at the back.
This is the classic noisy-neighbor problem, and a multi-tenant LLM platform is no different from any other shared system that faces these traffic patterns.
The goal of Serving Fairness is to isolate tenants from one another, so that the share of inference capacity that a tenant receives depends on fair scheduling — not on how aggressively it floods the queue. At the same time, it still preserves priority and deadline ordering
within
each tenant while maintaining batching efficiency.
The Solution: A layered approach to capacity management
Cohere manages workloads fairly across tenants by combining four distinct mechanisms, each solving a different slice of the problem. They run in a fixed order: a
Rate Limiter
controls admission on the way
in
, and then three selectors —
Performance Tier
,
Deficit Round Robin
, and
Priority
— select the next request on the way out.
Here is the architecture and step-by-step flow:
1. Rate Limiter
Before a request ever joins the scheduling queue, it passes through
admission control
. Rate limiting caps the maximum number of inference requests that a single tenant can submit within a given timeframe,such as requests per minute or per month.
At Cohere, these limits are configured at the
endpoint level
and differ between models based on how many resources each model consumes. For example, a heavyweight generative model carries tighter limits than a lightweight embedding model.
There is also a real-time throttling check: if the queue is already so backlogged that a new request could not be served within its latency target, the request is simply rejected early instead. This protects the system from accepting work it cannot honor and keeps latencies predictable under load.
After requests have been admitted, they proceed to the series of selectors below.
2. Performance Tier (selector one)
The first selection decision is the
tier
. Compute resources are prioritized based on service-level agreements (SLAs): higher-paid tiers are allocated greater processing priority and faster queue handling than lower tiers (or Trial Tiers). In turn, these latter customers are served as capacity allows.
Crucially, tiering determines
who goes first
; it does not, by itself, prevent a single large tenant
within
a tier from dominating. That is the purpose of the next two layers.
3. Deficit Round Robin (selector two)
The heart of the system is the Deficit Round Robin (DRR) algorithm, which ensures an equitable distribution of compute across the fleet
within a tier
.
Each tenant (an "organization") gets its own line. Instead of draining whichever line is longest, the scheduler takes turns between tenants. Each tenant is granted a small budget — a
quantum
— of work that it may perform on its turn. When a tenant uses its turn, its budget is debited by the cost of the request it just sent through. A tenant that runs out of budget is skipped until its budget is replenished on the following round.
The elegance of DRR is that it is both
work-conserving
and
weighted
. Cheap requests let a tenant come up more often, and expensive ones less, so no tenant can run away with the GPU — but no capacity is wasted either. Returning to our earlier example: even if Org A queued 10,000 requests and Org B only five, Org B still gets its due turn every cycle. Org A's burst no longer translates into Org B's latency.
What the budget measures
The scheme hinges on two key variables:
Quantum:
How much budget a tenant is granted each round
Cost:
How much budget each request consumes
The crucial design choice lies in
what unit
those variables are expressed in. Critically, this determines how we might conceptualize “fairness” in different inference contexts. At Cohere, we use two cost models depending on the endpoint: request-based budgeting and token-based budgeting.
Request-based budgeting
For simplicity, the cost of every request is given as 1, and the quantum is a count of requests that a tenant may send per turn. Fairness is, therefore, measured purely in the
number of requests.
This is suboptimal for
generative endpoints
, such as chat and completions, where request serving costs can vary dramatically. A request with a 100K-token prompt may consume orders of magnitude more resources than one with a 1K-token prompt. For reasoning-capable models, the total cost depends not only on the input size, but also on the amount of intermediate reasoning, planning, and output generation triggered by the specific context of the request.
Ideally, DRR would use a feedback loop based on the EMA (Exponential Moving Average) of a request's token-normalized serving cost, allowing budgets to adapt to observed resource consumption. Static budgeting works best when requests within an endpoint are
broadly similar in size and cost
.
Token-based budgeting
Here, the cost of a request is its token count, and the quantum is a
token budget
per round. Fairness is now measured in actual work performed. This is the natural fit for
batched endpoints
like embeddings and rerankers, where the
token sum
of a batch — not the number of items — drives GPU cost. A tenant sending a few very large documents spends its budget quickly and yields the floor sooner; a tenant sending many small requests is charged little per request and surfaces more often. This way, no tenant can monopolize a GPU by submitting a handful of extra large requests.
What each model means for your request
Request-based
Token-based
Cost of one request
Always 1, regardless of size
Proportional to its token count
Quantum (budget per turn)
A number of requests
A token allowance
A large request
Counts the same as a small one
Are charged more and consumes more of the tenant's share
A tenant of small requests
Gets the same # turns as anyone
Gets more turns (each request is cheap)
Best for
Generative / streaming endpoints
Embedding / reranker (batched) endpoints
Fairness measurement
Requests served
Work (tokens) done
So, under
request-based
budgeting, your request waits behind (at most) a fixed number of requests from each competing tenant, no matter how large those requests are. This count may be predictable, but a neighbor's large requests can still cost you GPU time on each of their turns.
Under
token-based
budgeting, a large request is "heavier": it draws down its tenant's budget faster, so that tenant moves on sooner and smaller requests can efficiently flow through. This model is a more faithful reflection of the true cost of the work and is the stronger guarantee against bottlenecks created by a single tenant's heavy traffic.
The quantum is also sized to the endpoint's batching strategy: streaming endpoints rotate after roughly one request per tenant for tight interleaving, while batched endpoints grant a budget close to a full batch. A tenant can, therefore, contribute a meaningful chunk before the scheduler moves on — preserving batching efficiency without sacrificing fairness.
4. Priority (selector three)
If fairness is about deciding which
tenant
goes next, then the Priority selector determines
which of that tenant's requests
goes next.
Once Deficit Round Robin selects a tenant for its turn, the scheduler pulls out a single request from that tenant’s line — but not blindly. Each line is a systematized queue ordered by:
Priority:
Explicitly higher-priority requests are served first.
Deadline:
Among equal priorities, the request with the earliest deadline wins, so time-sensitive work isn't left to expire.
Arrival time:
As a final tiebreaker, earlier requests go first, giving stable, predictable first-in-first-out behavior.
Keeping this ordering
inside
each tenant — rather than in one global queue — is what lets
fairness
and
urgency
coexist in the platform. A tenant never loses its priority and deadline guarantees just because it shares the platform; it simply applies those guarantees to its own fair share of capacity.
Putting it together
The four stages compose into a clean request lifecycle. Rate limiting governs admission
on the way in
; tiering, fairness, and per-tenant urgency govern selection
on the way out
as each batch is assembled.
Separately, each of these mechanisms — rate limiting, tiering, round-robin scheduling, and priority queues — are well familiar to MLOps and Platform Engineers. Their novel value comes from how they
integrate
:
Rate limiting
protects the system from overload and enforces per-tenant quotas.
Tiering
honors commercial commitments.
Deficit Round Robin
guarantees that, among admitted traffic of equal tier, every tenant gets a fair, burst-proof share.
Priority
preserves each tenant's own urgency and deadline ordering within its fair share.
Steps 2–4 repeat until the batch is full, and the batch is then sent to the GPU. The result is a platform where your experience depends on your tier and your fair share of capacity — not on how loud your neighbor happens to be that day.
Enjoy fairer, friction-free inference today
Serving Fairness is now enabled for all customers using any Cohere model through our SaaS API and third-party marketplace deployments, including AWS.
We’ve developed this feature with customer needs front and center. If you’re using Cohere models and have feedback, observed performance issues, or suggestions for improvement, please reach out to our engineering team on our
Discord
.
Blog
Written By
Manoj Govindassamy
Manager of Technical Staff
Musa Talluzi
Member of Technical Staff
Tags
Technology
AI for Developers
Enterprise AI
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
