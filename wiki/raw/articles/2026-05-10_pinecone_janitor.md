---
title: "Garbage Day: How Pinecone Safely Deletes Billions of Objects at Scale"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/janitor/"
scraped: "2026-05-10T01:27:39.570327+00:00"
lastmod: "2026-03-05T22:57:36Z"
type: "sitemap"
---

# Garbage Day: How Pinecone Safely Deletes Billions of Objects at Scale

**Source**: [https://www.pinecone.io/blog/janitor/](https://www.pinecone.io/blog/janitor/)

←
Blog
Garbage Day: How Pinecone Safely Deletes Billions of Objects at Scale
Lea Wang-Tomic
,
Benny Nazimov
,
Hirad Pourtahmasbi
Mar 5, 2026
Engineering
Share:
Jump to section:
The three deletion modes
The core protocol: identify → verify → execute
Testing month-long behavior in seconds
Lessons from Production
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
TLDR:
Pinecone’s data plane utilizes immutable blob storage. Every write produces a new file rather than modifying an existing one. While this keeps the write path clean, it generates a constant stream of stale and orphaned objects that drive up storage costs. To solve this, we built
Janitor
: a system designed to identify unreachable objects, verify safety, and delete with full auditability.
Deleting data safely in a single-node database is easy. The principles are straightforward: do not delete anything that might still be referenced, verify before deletion, and keep an audit trail. But every team building on immutable storage eventually discovers the same thing: the data you no longer need becomes the problem you can't stop paying for.
In real-world systems, deletion gets hard at scale, because "delete" is rarely one operation. Instead, it's a long chain of services, caches, retries, and failure modes. At Pinecone, we learned this the expensive way. Our data plane is built on immutable objects in blob storage—a design that keeps the write path clean but creates a fundamental coordination problem. Because our writing nodes and reading nodes are separate, a writer cannot simply purge an old file the moment it's superseded; separate reading nodes may still be actively serving a live query from that exact object. This disconnect creates a steady stream of files that never go away on their own, which quietly became one of the largest line items in our infrastructure bill.
This is the
deletion tax
: the growing cost of data you no longer need but can't yet safely remove. Janitor is how we pay it down.
S3 Storage Costs Before and After Implementation of Janitor
Why immutability creates garbage
Immutability is an age-old principle in distributed systems and functional programming. It reduces whole classes of race conditions and makes recovery and audit-ability much simpler. Writes do not modify files in place. Instead, each write produces a new file and metadata is updated automatically with a Compare-and-Swap (CAS) operation to point to the latest state.
The tradeoff is waste. Old versions linger after every write. Worse, if a process crashes between writing a blob and committing its metadata, the file becomes an orphan — present in storage but invisible to every reference path in the system.
So why not just delete aggressively? Because of
propagation lag
. Different parts of the system (caches, routers, replicas) don't all update at the same time. References to old data can stick around longer than the data itself. Delete too early, and you trade storage costs for reliability problems.
The three deletion modes
Not all stale data is stale for the same reason, and not all of it carries the same risk when removed. Janitor treats "deletion" as three distinct problems, each with its own cadence and failure profile.
Normal mode
handles the everyday accumulation. Files that have been superseded by newer writes and are no longer reachable from the
manifest
(the metadata structure that tracks which blob objects are currently live and which version of the data a query should see). Every system that uses immutable storage generates this kind of waste constantly.
Runs scoped cleanup every four hours per shard, with a broader weekly pass across all shards.
The main risk is timing: references to old blobs can linger in caches, so something might still be pointing to a file even after it's been logically replaced.
Orphan mode
handles a harder problem. Normal mode cleans up files the system knows about but no longer needs. Orphan mode cleans up files the system doesn't know about at all, like blobs written by a service that crashed before committing metadata. No manifest entry, no reference path. Just a file sitting in storage, accumulating cost.
Runs as a monthly scan starting from blob storage itself, working backward to prove whether each object is reachable.
Required because orphans are invisible to normal operations by definition.
Customer deletion mode
is the most operationally sensitive of the three. When a customer deletes an index or namespace, the expectation is that the data goes away, but "goes away" and "goes away immediately and irreversibly" are very different promises.
Inserts a deletion operation into the control plane with a resolution date 30 days out.
During that window, accidental deletes are recoverable. After it closes, the data is gone for good.
The core protocol: identify → verify → execute
Each mode identifies a different kind of waste. The protocol is what makes sure removing it is safe.
At scale, the important distinction is between hypothesis ("this looks deletable") and permission ("we are sure it is safe to delete"). Janitor's workflow is built around that separation, and it's intentionally conservative. Every run follows the same three phases, regardless of mode.
Identify.
Compute a candidate set without deleting anything. The candidate set is just a hypothesis, nothing has been touched yet.
In normal mode, this means iterating through the entire manifest and its history to determine what is currently reachable versus what has aged out.
In orphan mode, the direction is reversed: start from blob storage, enumerate objects, and work backward to prove whether each one is reachable.
Either way, candidates are written to a local SQLite database. Persisting the hypothesis makes the process auditable and restartable. If Janitor crashes here, nothing is lost.
Verify.
Recheck the hypothesis against a fresh view of the world. This is where the propagation lag between different parts of the system gets handled.
Recompute reachability and confirm every candidate is still safe to remove.
If any candidate intersects something currently reachable, the response is to delay or drop it.
If the world looks stale, Janitor waits. The cost of a false positive (deleting something live) is vastly higher than the cost of a false negative (keeping something dead around for another cycle), and the verification step is where that asymmetry is enforced.
Execute.
Delete only what has been verified. At scale, processes get interrupted, so every run is built to be picked up cleanly if it stops halfway through.
Every deletion is treated as idempotent work that can be retried safely.
SQLite state tracks exactly what was targeted and what completed, so if a run dies halfway through, the next run knows where to resume.
Blob storage retention and restore tooling provide the practical recovery window underneath, but Janitor's checkpoints are what make it possible to investigate what happened, quantify impact, and drive restoration when things go wrong.
Testing month-long behavior in seconds
This is a bit of an aside, but it's arguably the most sophisticated part of the whole build and too interesting to leave out
Janitor's hardest bugs don't show up in a single run. They emerge from the interaction of repeated writes, rebuilds, partial failures, customer deletes, and scheduled cleanups layered on top of each other. Some of which play out over a 30-day window, but waiting a month to find out a test passed isn't an option.
To make that testable, Janitor uses property-based tests with a mock clock. Define a set of possible actions (writes, rebuilds, crashes, deletes, Janitor runs), generate hundreds of randomized sequences, run them through both the real implementation and a simplified reference model, and compare outcomes. The mock clock collapses days and months into sub-second tests. If the two models ever disagree, we have a reproducible bug in hand.
Lessons from Production
Safe deletion at scale comes from layering defenses — a second reachability check before anything is removed, durable checkpoints that make every run inspectable and restartable, and a testing strategy that compresses weeks of behavior into seconds. Before Janitor, deletion was a source of anxiety. Now it runs continuously in the background, cleans up reliably, and generates an audit trail, so when something unexpected happens, the path to understanding it is already there.
For customers, none of this should be visible, and that's the point. Queries don't fail because a file was deleted too early. Accidental index deletes are recoverable within a 30-day window. Storage costs stay predictable instead of silently climbing. Janitor is the kind of infrastructure that ensures the rest of the team doesn't have to think about garbage at all.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
