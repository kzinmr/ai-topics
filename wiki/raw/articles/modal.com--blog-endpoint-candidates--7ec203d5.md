---
title: "Endpoint Candidates: evaluate and promote inference endpoints"
url: "https://modal.com/blog/endpoint-candidates"
fetched_at: 2026-10-13T10:01:09.204839+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Endpoint Candidates: evaluate and promote inference endpoints

Source: https://modal.com/blog/endpoint-candidates

Latency, throughput, and cost optimization are at the core of modern inference engineering. Without testing and measurement, these metrics cannot be reliably improved.
We’ve been focused on inference performance
for
some
time
now
, and we’re building several new tools to help you optimize your own inference servers–starting with
Endpoint Candidates
.
Endpoint Candidates allow you to stage alternative deployments for your
Dedicated Endpoints
, so you can evaluate the impact on quality, latency, throughput, and cost. Each Candidate can mirror production, handling a sample of production traffic while Modal runs the underlying infrastructure. When you’re ready, promote your Candidate to production from the dashboard.
With Candidates, you can test new model checkpoints–or even entirely different models–without rolling your own traffic-mirroring and deployment infrastructure. Endpoint Candidates are generally available for all Modal workspaces.
Getting started
To create a new Candidate, start with an existing Dedicated Endpoint in your Modal environment. Select
Create candidate
to choose an open model from Modal’s catalog or bring your own weights from a Hugging Face repo or a Modal Volume.
Once your Candidate is ready, configure your traffic sample to start mirroring production traffic to it. Production continues to handle every original request and return the response your users see.
Use the dashboard to inspect the Candidate’s inference metrics, including latency and throughput, and run
performance benchmarks
to understand its behavior under load. Each Candidate also has its own URL, so you can run your existing evaluations against it to assess output quality.
When you’re ready, promote the Candidate from the dashboard. Modal starts a production rollout at the existing Endpoint URL. Your other Candidates remain available, so you can continue testing them independently.
Endpoint Candidates use
standard Modal compute pricing
, including compute used for mirrored requests.
Keeping production moving
One of the challenging parts of building traffic mirroring was keeping slow mirrors from holding up production. When several Candidates receive copies of a large request, they may read the data at different speeds. A proxy can end up
buffering substantial amounts of data
while waiting for the slower Candidates.
To address this, we extended our Pingora-based proxy to fork each request stream into a separate, bounded buffer for every Candidate receiving a copy. Each mirror reads independently: if a new chunk arrives and a buffer is full, the proxy cancels that mirrored request while production and the other mirrors continue.
But a bounded buffer for each mirror still leaves a problem: a busy proxy may be mirroring many requests at once. So we also cap the body data retained by mirrors within each proxy process. They share request-body chunks, so each chunk counts only once against this budget.
Removing a chunk from a buffer doesn’t necessarily free its memory, since a network write may still be holding it. We keep counting that chunk until the last mirror releases it. If adding the next chunk would exceed the budget, the proxy cancels that request’s mirrors while the original request continues.
Mirroring is best-effort by design: mirrored requests may be dropped under pressure, so production doesn't have to wait for a slow or failing Candidate.
What’s next
We’re expanding how you can create and evaluate Candidates, from more control over compute placement and serving recipes to richer metrics views for comparing deployments.
We’re working to automate more of that experimentation, too. When we
introduced Auto Endpoints
, we described our work on automating inference optimization. Candidates give those optimizations a place to prove themselves: a way for Modal to test promising changes against your traffic, then surface measured improvements in latency, throughput, or cost.
