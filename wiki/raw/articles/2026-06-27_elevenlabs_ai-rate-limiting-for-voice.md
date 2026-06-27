---
title: "AI rate limiting for voice: How to handle concurrency limits"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/ai-rate-limiting-for-voice"
scraped: "2026-06-27T06:00:19.221491+00:00"
lastmod: "2026-06-26T14:00:11.506Z"
type: "sitemap"
---

# AI rate limiting for voice: How to handle concurrency limits

**Source**: [https://elevenlabs.io/blog/ai-rate-limiting-for-voice](https://elevenlabs.io/blog/ai-rate-limiting-for-voice)

Blog
Resources
AI rate limiting for voice: Concurrency, queues, and 429s
Written by
Tadas
Petra
Jack
Limebear
Published
Jun 26, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Sign up
Learn more
On this page
Introduction
TL;DR
Why the limit is concurrency, not requests per minute
The per-plan, per-model-family limits
What happens when you hit the concurrency limit?
HTTP vs. WebSocket: How each counts against your limit
Why ~5 concurrency can support ~100 broadcasts
The headers that explain where you stand
Client-side strategies for AI rate limiting
Multi-tenant quota patterns for AI rate limiting
Monitoring your concurrency utilization
When to scale beyond client-side rate limiting
Recapping what to keep in mind for AI rate limiting
Build voice applications with ElevenAPI
AI rate limiting FAQ
Most teams reach for AI rate limiting for voice the same way they handle other APIs: cap requests per minute, retry when the server pushes back, and move on. For workloads on ElevenLabs, that model breaks down on the first burst of traffic, because the limit you are actually hitting is concurrency, not request count.
This guide explains why concurrency is the real constraint, then walks through the client-side patterns that keep you inside it. From bounded concurrency pools and graceful 429 handling to multi-tenant fairness and token and leaky buckets, we offer practical systems that you can implement. We’ve paired each pattern with a working TypeScript implementation you can adapt.
If you
build voice agents
, narration pipelines, or any other production system on top of our models and want to scale, this playbook is for you.
TL;DR
AI rate limiting for voice is concurrency control, not request-per-minute counting.
Hitting the rate limiting ceiling doesn’t reject traffic immediately. Instead, requests enter a priority queue that adds around 50ms.
Going over capacity even after queueing will create an HTTP 429 error.
WebSockets dramatically increases effective capacity, as only active generation counts toward your limit.
Multi-tenant systems need an extra fairness layer: per-tenant buckets, weighted fair queueing, reserved headroom, and sharding across keys for isolation.
Two response headers, current-concurrent-requests and maximum-concurrent-requests, let you know where you stand with AI rate limiting.
Why the limit is concurrency, not requests per minute
Concurrency is the number of requests in flight at the same moment. Requests per minute is throughput over a window. Understanding this distinction is important because it changes which lever keeps you inside your limit.
When using one of the
ElevenLabs
models, the server workload scales with the number of concurrent users. Audio generation holds a slot for the duration of generation, and that duration varies with input length, model, and load.
A request-per-minute cap tells you nothing about how many slots are occupied right now, which is the only thing the server is metering.
The per-plan, per-model-family limits
Your concurrency budget is not a single number. Concurrency limits differ per plan and per model family. For example,
Speech to Text
carries an elevated limit relative to
Text to Speech
, because transcription requests are typically shorter-lived and the system can absorb more of them at once.
Multilingual v2
Free
2
Starter
3
Creator
5
Pro
10
Scale
15
Business
15
Enterprise
Elevated
Flash
Free
4
Starter
6
Creator
10
Pro
20
Scale
30
Business
30
Enterprise
Elevated
STT
Free
8
Starter
12
Creator
20
Pro
40
Scale
60
Business
60
Enterprise
Elevated
Realtime STT
Free
6
Starter
9
Creator
15
Pro
30
Scale
45
Business
45
Enterprise
Elevated
Priority
Free
3
Starter
4
Creator
5
Pro
5
Scale
5
Business
5
Enterprise
6
Plan
Multilingual v2
Flash
STT
Realtime STT
Priority
Free
2
4
8
6
3
Starter
3
6
12
9
4
Creator
5
10
20
15
5
Pro
10
20
40
30
5
Scale
15
30
60
45
5
Business
15
30
60
45
5
Enterprise
Elevated
Elevated
Elevated
Elevated
6
The limit is per model family. If you run Flash for agents and Multilingual v2 for narration, you are working against two separate budgets at once. The current per-plan figures and the concurrency section are documented on the
models page
.
What happens when you hit the concurrency limit?
Reaching the concurrency limit does not reject traffic immediately. The system degrades gracefully through a priority queue, only escalating to complete rejection when you’re still over the rate limit total capacity.
While you’re under your limit, requests run immediately. When you reach it, subsequent requests enter a queue ordered by your plan's priority level. The queue typically adds around 50ms of latency, so a brief overrun is mostly invisible to users.
If the system is still over capacity after queueing, you receive an HTTP 429. That is the signal to back off rather than retry immediately. The priority level in the table determines how your queued requests are ordered relative to other traffic; higher plans clear the queue sooner.
HTTP vs. WebSocket: How each counts against your limit
The transport you choose directly influences rate limiting and budget. The same incoming conversation may consume significantly different amounts of your concurrency budget depending on whether it runs over HTTP or on a WebSocket.
Over HTTP, each request counts individually toward your concurrency limit for its full duration. Over a WebSocket, only the time the model is actively generating audio counts. An open but idle WebSocket mostly does not count.
For a voice agent, a conversation has long stretches where nobody is speaking and the model is generating nothing. With HTTP you would hold a slot for the request duration every turn. With a WebSocket the slot is consumed only during the milliseconds of active generation, so one concurrency slot is time-shared across many conversations.
See the
real-time TTS WebSocket guide
for the protocol details. For interactive traffic, WebSockets are the right default.
Why ~5 concurrency can support ~100 broadcasts
The maths behind concurrency is counterintuitive until you account for playback time. Generation is far faster than playback, and a slot is only actively occupied when audio is being generated. That gap is exactly what lets a small budget serve a large audience.
A request that takes a fraction of a second to generate produces several seconds of audio that the listener then spends time playing back, and during playback the slot is released and available to other listeners.
As a rule of thumb, a concurrency limit of 5 can support roughly 100 simultaneous audio broadcasts. The exact number depends on the voice, the cadence of speech, and how much silence sits between utterances.
The headers that explain where you stand
You don’t need to infer your position relative to your limit. Every response carries two numbers that you can use to measure headroom instead of simply estimating.
Look out for these two headers:
current-concurrent-requests:
how many requests are in flight right now?
maximum-concurrent-requests:
your limit for that model family.
Together, these headers provide a
real-time
overview of your current usage and available capacity. You shouldn’t need to engage in any guesswork before you run into AI rate limits.
Client-side strategies for AI rate limiting
There are four primitives that cover almost every AI rate limiting scenario:
A token bucket:
If tokens are available, allows requests to proceed. Capacity is replenished over time, allowing it to handle short bursts without hitting rate limits.
A leaky bucket:
Attempts to smooth incoming traffic into a fixed output rate, which prevents sudden spikes from overwhelming your downstream systems.
A bounded concurrency pool:
Caps the total number of requests that can be active simultaneously, meaning you never exceed concurrent request limits.
Exponential backoff with full jitter:
Increasingly adds a longer timespan between failed requests to prevent clients from all retrying at once.
The sections below demonstrate how to build them up one at a time, beginning with the one that maps most directly to the concurrency limit.
All the snippets below assume a single client, initialized once:
import
{ ElevenLabsClient }
from
"@elevenlabs/elevenlabs-js"
;
const
elevenlabs
= new ElevenLabsClient({
apiKey:
process.env.
ELEVENLABS_API_KEY
});
Bounded concurrency: the primitive that matches the limit
Since the server meters concurrency, the most direct client control is a bounded worker pool that caps how many requests you have in flight at once. Set the cap a little below your plan's limit to leave room for the priority queue and for jitter.
async function
pool<T, R>(
items
: T[],
maxInFlight
:
number
,
  worker: (
item
: T)
=>
Promise<R>,
): Promise<R[]> {
const
results
: R[] = new Array(items.
length
);
let
next =
0
;
async function
run(): Promise<
void
> {
while
(next < items.
length
) {
const
i
= next++;
      results[i] =
await
worker(items[i]);
// never more than maxInFlight of these run at once
}
  }
await
Promise
.all(
    Array.from({
length:
Math.min(maxInFlight, items.
length
) }, run),
  );
return
results;
}
async function
synthesize(
text
:
string
): Promise<Buffer> {
const
stream
=
await
elevenlabs.textToSpeech.stream(
"JBFqnCBsd6RMkjVDRZzb"
, {
    text,
modelId:
"eleven_flash_v2_5"
,
outputFormat:
"mp3_44100_128"
,
  });
const
chunks
: Buffer[] = [];
for await
(
const
chunk
of stream) chunks.push(Buffer.from(chunk));
return
Buffer.concat(chunks);
}
// Plan Flash limit is, say, 10. Stay under it.
const
texts
= Array.from({
length: 50
}, (
_
,
i
)
=>
`Sentence number ${
i
}.`
);
const
audio
=
await
pool(texts,
8
, synthesize);
// never more than 8 in flight
Token bucket: allow bursts, cap the average
A token bucket holds up to capacity tokens and refills at refillRate tokens per second. Each request consumes a token, so the bucket permits short bursts up to its size while bounding the long-run rate.
It is the right tool for smoothing the moment when a queue of work suddenly arrives, so you do not fire everything at once and spike concurrency.
class
TokenBucket {
private
tokens
:
number
;
private
updated
= performance.now();
constructor
(
private
capacity
:
number
,
private
refillPerSec
:
number
) {
this
.
tokens
= capacity;
  }
private
refill():
void
{
const
now
= performance.now();
const
elapsed
= (now -
this
.
updated
) /
1000
;
this
.
tokens
= Math.min(
this
.
capacity
,
this
.
tokens
+ elapsed *
this
.
refillPerSec
);
this
.
updated
= now;
  }

  tryAcquire(
cost
=
1
):
boolean
{
this
.refill();
if
(
this
.
tokens
>= cost) {
this
.
tokens
-= cost;
return
true
;
    }
return
false
;
  }

  timeUntil(
cost
=
1
):
number
{
this
.refill();
return
this
.
tokens
>= cost ?
0
: ((cost -
this
.
tokens
) /
this
.
refillPerSec
) *
1000
;
  }
}
Leaky bucket: enforce a steady drain
In some cases you do not want to tolerate bursts at all. A leaky bucket admits work at a fixed, constant rate regardless of how bursty the input is. It is the better choice when the downstream system prefers a smooth, predictable load over occasional spikes.
For example, when you are deliberately staying well inside a small concurrency budget shared with other services.
class
LeakyBucket {
private
next
= performance.now();
constructor
(
private
intervalMs
:
number
) {}
// admit at most one item per intervalMs
async
acquire(): Promise<
void
> {
const
now
= performance.now();
const
wait
= Math.max(
0
,
this
.
next
- now);
this
.
next
= Math.max(now,
this
.
next
) +
this
.
intervalMs
;
if
(wait >
0
)
await
new
Promise
((
r
)
=>
setTimeout(r, wait));
  }
}
Exponential backoff with full jitter
When a request fails with a retryable status, retrying immediately makes things worse. Backoff spaces retries out, and full jitter randomizes each delay across the whole interval, which prevents many clients from retrying in lockstep and recreating the same spike that caused the failure.
The snippet below references RetryableError, a small class that carries the failed status and any Retry-After value. It is defined in the graceful 429 handling section below.
async function
withBackoff<T>(
  call: ()
=>
Promise<T>,
opts
: {
maxAttempts
?:
number
;
baseMs
?:
number
;
capMs
?:
number
} = {},
): Promise<T> {
const
{
maxAttempts
=
5
,
baseMs
=
500
,
capMs
=
20_000
} = opts;
let
attempt =
0
;
for
(;;) {
try
{
return await
call();
    }
catch
(e) {
if
(!(e instanceof RetryableError) || ++attempt >= maxAttempts)
throw
e;
// honor Retry-After if present; otherwise capped exponential growth with full jitter
const
delay
=
        e.
retryAfterMs
?? Math.random() * Math.min(capMs, baseMs *
2
** attempt);
await
new
Promise
((
r
)
=>
setTimeout(r, delay));
    }
  }
}
Graceful 429 handling: What to do when you hit the ceiling
A 429 means you were over capacity even after the priority queue, so the correct response is to slow down rather than retry harder. There are four ways to handle it. Handling it well comes down to four strategies:
Detection
Respecting Retry-After
Surfacing backpressure
Avoiding retry storms with a circuit breaker
Let’s break these down in more detail.
The first is detection. Treat HTTP 429 (and transient 500, 502, 503, and 504) as retryable, and treat 400, 401, 403, and 422 as non-retryable; retrying a malformed or unauthorized request never succeeds and only wastes a slot.
The second is respecting Retry-After. If the response carries that header, honor it exactly instead of computing your own delay. The server is telling you when it expects to have capacity, and it knows better than your exponential formula does. Only fall back to jittered backoff when the header is absent.
class
RetryableError
extends
Error {
constructor
(
public
status
:
number
,
public
retryAfterMs
?:
number
) {
super
(
`retryable ${
status
}`
);
  }
}
function
classify(
resp
: Response):
void
{
if
([
429
,
500
,
502
,
503
,
504
].includes(resp.
status
)) {
const
ra
= resp.headers.get(
"retry-after"
);
throw
new RetryableError(resp.
status
, ra ? Number(ra) *
1000
:
undefined
);
  }
if
(!resp.
ok
)
throw
new Error(
`non-retryable ${
resp
.
status
}`
);
}
The third axis is surfacing backpressure. Do not let retries pile up invisibly. If your queue depth or measured headroom indicates you cannot serve a new request soon, reject it at the edge with a clear signal to the caller rather than accepting work you cannot do.
The fourth is avoiding retry storms with a circuit breaker. If failures cross a threshold, open the circuit and fail fast for a cool-down window instead of sending requests you expect to fail. After the window, send a few probe requests; if they succeed, close the circuit.
class
CircuitBreaker {
private
failures
=
0
;
private
openedAt
:
number
|
null
=
null
;
constructor
(
private
threshold
=
5
,
private
cooldownMs
=
10_000
) {}

  allow():
boolean
{
if
(
this
.
openedAt
===
null
)
return
true
;
if
(performance.now() -
this
.
openedAt
>=
this
.
cooldownMs
) {
this
.
openedAt
=
null
;
// half-open: allow a probe
this
.
failures
=
0
;
return
true
;
    }
return
false
;
  }

  record(
ok
:
boolean
):
void
{
if
(ok) {
this
.
failures
=
0
;
this
.
openedAt
=
null
;
    }
else if
(++
this
.
failures
>=
this
.
threshold
) {
this
.
openedAt
= performance.now();
    }
  }
}
Multi-tenant quota patterns for AI rate limiting
Everything so far assumes a single application against a single budget. When you build a SaaS on top of ElevenLabs, the problem changes shape: your concurrency budget is shared across all of your own customers, and one tenant running a batch job should not starve every other tenant's live traffic. You need a fairness layer between your tenants and the single upstream limit.
The foundation is per-tenant token buckets. Give each tenant its own bucket sized to their entitlement, and admit a request only when both the tenant bucket and a global limiter allow it.
class
MultiTenantAdmission {
private
tenantBuckets
= new Map<
string
, TokenBucket>();
constructor
(
private
globalMaxInFlight
:
number
) {}
private
bucket(
tenant
:
string
): TokenBucket {
let
b =
this
.tenantBuckets.get(tenant);
if
(!b) {
// Each tenant: burst of 5, sustained 2 starts/sec. Tune per tier.
b = new TokenBucket(
5
,
2
);
this
.tenantBuckets.set(tenant, b);
    }
return
b;
  }
async
run<R>(
tenant
:
string
, work: ()
=>
Promise<R>): Promise<R> {
const
b
=
this
.bucket(tenant);
if
(!b.tryAcquire()) {
throw
new RetryableError(
429
, b.timeUntil());
    }
// ... then admit through the global limiter (e.g. the bounded pool above)
return
work();
  }
}
Buckets keep any single tenant honest, but they do not decide who wins when tenants compete for the global limiter. For that, use weighted fair queuing.
Do not serve first-come-first-served, which lets a burst from one tenant monopolize slots. Maintain a per-tenant queue and dispatch in proportion to each tenant's weight so a paying tenant gets a larger share of contended capacity than a free one.
On top of fairness, reserve headroom. Never let normal traffic consume 100% of the concurrency limit. Hold back a fraction, say 15-20%, as a buffer for latency-sensitive interactive requests and for the priority queue.
When fairness within a single budget stops being enough, shard across workspaces or keys. A single concurrency budget eventually becomes the bottleneck no matter how fairly you divide it.
At that point, separate workloads onto distinct workspaces or API keys with their own budgets: for instance, one key for real-time agent traffic and another for background narration, so a narration backlog cannot touch agent capacity.
Workspaces also let you apply scope restriction, credit quotas, and
per-key controls
, described in the
authentication docs
.
Monitoring your concurrency utilization
None of this is tunable without measurement; you cannot manage headroom you do not measure. Record current-concurrent-requests and maximum-concurrent-requests on every response, tagged by model family, and emit the utilization ratio as a gauge.
function
recordHeadroom(
resp
: Response,
metrics
: Metrics):
void
{
const
cur
= Number(resp.headers.get(
"current-concurrent-requests"
));
const
max
= Number(resp.headers.get(
"maximum-concurrent-requests"
));
if
(Number.isFinite(cur) && Number.isFinite(max)) {
    metrics.gauge(
"el.concurrency.current"
, cur);
    metrics.gauge(
"el.concurrency.max"
, max);
if
(max >
0
) metrics.gauge(
"el.concurrency.utilization"
, cur / max);
  }
}
Four signals to track:
Utilization (current / maximum).
429 rate as a fraction of total requests.
Retry depth, the number of attempts per logical request.
Time-to-first-audio, measured from your application, not from model inference figures. See understanding latency for what TTFA includes.
A healthy system will keep utilization comfortably below saturation and see 429s only in occasional bursts. Monitoring these signals gives you visibility into rate-limiting pressure, long before it becomes an outage issue.
When to scale beyond client-side rate limiting
Client-side patterns can do a lot of heavy lifting but steady-state demand will eventually outgrow them. When that happens, it’s time to make changes that help with both cost and effort.
Each of the following steps will buy you extra capacity.
Start by switching HTTP to WebSockets for interactive traffic. If your agents or live use cases run over HTTP, moving to a WebSocket changes the accounting so that only active generation counts. For conversational workloads this often multiplies effective capacity without changing your plan, because idle conversation time stops consuming slots.
If your bursts are spiky but your average load fits the budget, a token or leaky bucket plus a bounded pool flattens the peaks into the average.
Then choose the right model. Faster generation holds each slot for less time, which raises the number of broadcasts a fixed concurrency limit can sustain. Eleven Flash v2.5 is the
lowest-latency option
for real-time work; pairing it with an
Instant Voice Clone
or a default voice avoids the per-generation overhead of Professional Voice Clones.
Only after that should you upgrade the plan. When your steady-state demand genuinely exceeds the budget after the client is well-behaved, a higher plan raises both the per-model concurrency limit and your queue priority. Compare tiers on the API pricing page.
If you need limits beyond what is published, Enterprise plans offer elevated and custom concurrency limits and the highest queue priority. Additional controls are available for eligible use cases, such as IP whitelisting (in Enterprise preview) and zero-retention modes. Contact your account manager to raise limits.
Recapping what to keep in mind for AI rate limiting
The core mistake is treating voice AI rate limiting as request counting. Everything here is about concurrency control. The number that decides whether you succeed is how many requests are generating audio at the same instant and how long each one holds its slot.
Build the client around that fact.
Cap in-flight requests with a bounded pool, shape admission with a token or leaky bucket, retry with capped exponential backoff and full jitter, honor Retry-After, and break the circuit before a retry storm forms.
For multi-tenant systems, layer on per-tenant buckets, weighted fairness, reserved headroom, and sharding for isolation. Watch the current-concurrent-requests and maximum-concurrent-requests headers and alert on the utilization trend, not the failures.
When you genuinely need more capacity, work the list in order: WebSockets and better client behavior first, then the right model, then a plan upgrade, and then Enterprise limits.
Build voice applications with ElevenAPI
Production-grade AI rate limiting starts with the right transport, the right model, and headers that tell you exactly where you stand.
ElevenAPI offers low-latency models like Eleven Flash v2.5, real-time WebSocket streaming,
Speech to Text
and
Text to Speech APIs
, and per-response concurrency headers that allow you to build voice agents that scale inside your limits.
Combined with the AI rate-limiting strategies in this article, you’ll deliver responsive voice experiences while maintaining predictable performance (even under load).
Explore
ElevenAPI
to see the full model lineup in action, or
create an account
to start building with ElevenLabs today.
AI rate limiting FAQ
What is rate limiting?
Rate limiting is a control that monitors how much traffic a client sends to a service. For APIs, it’s measured in requests per minute. For AI rate limiting on ElevenLabs, the most relevant constraint is concurrency, which is a measure of how many requests generate audio at the same moment, rather than how many arrive per minute.
What is a 429 error?
A 429 error is an HTTP status code that represents Too Many Requests. What that means in practice is that you’re over capacity for a specific time frame. Treat it as a signal to retry later as the server doesn’t want to crash.
What does too many concurrent requests mean?
When you have numerous different requests all generating audio at the same time, your concurrency limit defines what the total limit is. The limit is per model family, meaning you could run two families at once and draw from separate budgets. You can check the current concurrent-requests and maximum-concurrent requests headers to see your live position for this.
What is exponential backoff?
Exponential backoff is a strategy for error-handling which will increase the wait between attempts. If a retry took 5 seconds, the next will take ~10. After that, it’ll take ~20 seconds. Introducing exponential backoff helps to prevent your servers from being congested by lots of frequent, repeated requests.
How does a WebSocket reduce concurrency usage?
Over HTTP, each request counts toward your limit for its full duration. However, over WebSocket, only the time model actively generates audio counts. Idle connection mostly doesn’t count for your limit. Especially for conversational traffic with long silences, this feature lets one concurrency slot serve many conversations at once.
What is a token bucket?
A token bucket is a rate limiting algorithm that helps to manage how API requests are transmitted. A token bucket has a fixed number of tokens that refills at a steady rate. Every incoming request spends one token, so the bucket only allows short bursts up to its token capacity, capping the long-run average rate. It helps avoid spiking concurrency and is common in API rate limiting.
