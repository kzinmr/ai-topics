---
title: "The Distributed System Behind Hebbia's High-Scale AI"
source: "Hebbia Blog"
url: "https://www.hebbia.com/blog/maximizer-hebbias-distributed-system-for-high-scale-llm-request-scheduling"
scraped: "2026-05-10T01:27:12.862316+00:00"
lastmod: "2026-05-08"
type: "sitemap"
---

# The Distributed System Behind Hebbia's High-Scale AI

**Source**: [https://www.hebbia.com/blog/maximizer-hebbias-distributed-system-for-high-scale-llm-request-scheduling](https://www.hebbia.com/blog/maximizer-hebbias-distributed-system-for-high-scale-llm-request-scheduling)

Engineering
By Ben Devore
03.17.25
The Distributed System Behind Hebbia's High-Scale AI
We built a distributed LLM request scheduler that intelligently routes billions of tokens per day across multiple providers so high-priority work always gets through, even under rate limits.
Introduction
As AI matures, many organizations find themselves contending with fragmented, capacity-constrained infrastructure—especially when it comes to large language models (LLMs).
At Hebbia, we’re building the world’s most capable AI. On any given day, our platform processes billions of tokens for search, summarization, and synthesis. This unprecedented scale runs headlong into a harsh reality:
the global GPU shortage
has forced LLM providers to implement strict rate limits. Requests can spike unpredictably, and we’re often left with a fraction of the tokens we need.
To solve this, we created
Maximizer
—our distributed LLM request scheduler. Below, we’ll explore how it works: from the core abstractions of license requests and model families, to the architecture, to how we scaled it with a distributed partitioned leader election. Welcome to a behind-the-scenes look at how we juggle billions of tokens daily without overrunning our rate limits or underutilizing precious GPU capacity.
The Impetus Behind Maximizer
Hebbia has become one of the heaviest consumers of LLM tokens, surpassing 250 billion tokens per month. Our customers trigger far more requests than any single provider can handle, and in the midst of a global GPU shortage, we often face capacity constraints from the major cloud inference providers.
For us, it wasn’t enough just to queue up requests; we needed to ensure that high-priority tasks always made it through, while at the same time squeezing every ounce of juice from our capacity. We wanted a single place to coordinate, prioritize, and route requests across multiple LLM rate limit pools. That’s why we built Maximizer.
Core Abstractions: License Requests & License Grants
The Maximizer API interface is purposefully straightforward, built around two core concepts:
License Requests
– A request for token capacity for a specific “model family.”
License Grants
– A response from Maximizer detailing when to make the actual LLM call, and what model to make it to.
Here’s an example of each:
A
License Request
asks: “Can I use 50k tokens on GPT-4o at priority level 4?”
A
License Grant
responds: “Yes, you can, but use azure-gpt-4-1106-preview right now."
With these abstractions, we keep separation of concerns: services remain free to generate requests, and Maximizer orchestrates how and when they’re fulfilled.
Model Families: A Flexible Layer Above Providers
Modern LLM capabilities often come in multiple flavors from different providers. We unify these under model families:
Example: “gpt-4o” might include both OpenAI GPT-4o and Azure GPT-4o—each with distinct rate limits.
The user sees a family (e.g., GPT-4o), while under the hood we dynamically select the underlying model that has the fastest or most available capacity.
This approach ensures we never waste tokens that could be used. If one provider is out of capacity, we switch seamlessly to another within the same model family.
Architecture in Practice
We organize Maximizer around simple building blocks that come together into a robust system. Here’s the high-level flow:
Persistent WebSocket Connections
Any service needing LLM tokens connects to Maximizer’s gateway via a WebSocket connection. This gateway is a WebSocket API hosted on AWS API Gateway, which possesses a unique capability: it can convert incoming WebSocket requests into REST requests, and vice versa.
Each WebSocket connection has a callback URL (e.g., https://gateway-url/@connections/abc123) that Maximizer uses to respond with License Grants over REST later.
License Request → REST → DynamoDB
A License Request is sent over WebSocket, which AWS API Gateway transforms into an internal REST request to Maximizer.
Maximizer stores the request (along with its priority and timestamp) in DynamoDB.
Poller Service
Each model family has a polling loop that continuously checks the DynamoDB queue for the highest priority messages.
Upon picking a request, Maximizer evaluates each provider’s capacity in the requested model family, waits for rate-limit tokens if needed, and finalizes a choice.
License Grant → Gateway → WebSocket
Once capacity is assured, a License Grant is created.
Maximizer makes a REST request to the callback URL, which AWS API Gateway translates back into a WebSocket response, returning the License Grant to the original requester.
By leveraging WebSocket/REST duality, we created a simple yet flexible system that can route messages back and forth through AWS API Gateway without coupling the request and response phases to the same server instance.
Under the Hood: The Rate Limiter & Scheduling Algorithm
Model Selection
A request asks for model_family = gpt-4o. Maximizer quickly scans each underlying model (e.g., openai-gpt-4o, azure-gpt-4o-us-east) to see how soon they can accumulate the required tokens.
Rate Limiting
We use an in-memory token bucket to model each provider’s capacity.
If a request arrives that needs 50k tokens, but only 30k are currently available, the poller for the given model family will pause until enough tokens refill to meet that request’s needs.
License Grant
Once tokens are secured, the poller crafts a License Grant with exact instructions about which provider to use.
The system relays that grant back over WebSocket.
This core pipeline ensures we’re always pushing tokens to the highest priority requests first—no matter how many are in the queue.
Scaling for Billions of Tokens per Day
When we first built Maximizer in late 2023, our total LLM capacity hovered around 1 million tokens per minute. That required only two Maximizer servers:
Each server maintained an in-memory bucket of half our total rate limit.
Deployments had to replace servers one by one to avoid over-allocating capacity (leading to temporary 50% capacity drops).
By 2024, we had expanded our capacity by orders of magnitude, reaching more than 450 million TPM on popular models. To handle this demand, we evolved from a simple two-server approach to a partitioned distributed system inspired by
Apache Kafka’s consumer groups
.
Partitioned Leader Election: Ensuring No Rate Limit Overruns
Partitions per Model Family
High-capacity families might be split into 10 partitions. Each partition corresponds to a poller that handles a slice of the overall rate limit.
Lower-capacity families might only have 2 partitions.
Leader Servers
For each partition, exactly one leader server is elected. That leader runs the poller responsible for scheduling requests within that partition.
Leadership is coordinated using Redis locks.
Consistent Hashing
License requests are mapped to partitions using consistent hashing.
Heartbeat & Failover
Leader servers periodically send heartbeats to Redis. If a leader fails, its lock expires, and another server takes over.
Life of a Request: Putting It All Together
Request Creation
A service sends a License Request for 50k tokens on GPT-4o. The request lands in DynamoDB via WebSocket → REST.
Partition Assignment
Consistent hashing maps the request to a specific partition handled by a poller.
Rate Limit Check
The poller verifies capacity using the token bucket.
License Grant
A grant is crafted and sent back via WebSocket.
LLM Call
The client calls the appropriate LLM endpoint without hitting rate-limit errors.
Building for What’s Next
Maximizer embodies our approach at Hebbia: treat capacity as a resource that must be shared intelligently and flexibly. Future expansions might include:
Finer-grained scheduling for sub-priorities or specialized tasks.
Dynamic re-partitioning based on real-time usage patterns.
Support for on-the-fly model additions, enabling new models to be integrated into the application in minutes rather than hours.
Got Questions or Ideas?
If you have thoughts on Maximizer or want to learn more, drop us a line. Interested in pushing the boundaries of AI? We’re hiring—let’s build the future of information retrieval together!
Authors
Ben Devore
Lead Technical Staff
Ben Devore
Engineering
Adithya Ramanathan, Alex Flick
+ all other members of Hebbia technical staff
