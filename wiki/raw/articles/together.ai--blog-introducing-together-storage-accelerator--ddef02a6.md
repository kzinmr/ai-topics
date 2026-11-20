---
title: "Introducing Together Storage Accelerator: fast, free data caching for your GPU cluster"
url: "https://www.together.ai/blog/introducing-together-storage-accelerator"
fetched_at: 2026-11-20T10:01:14.506507+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Introducing Together Storage Accelerator: fast, free data caching for your GPU cluster

Source: https://www.together.ai/blog/introducing-together-storage-accelerator

Your GPUs are only as fast as your data pipelines. Every training run that starts with a 30-minute model download, every node that re-pulls the same dataset from across the country, and every Hugging Face rate limit that stalls a job leads to compute resources sitting idle, waiting for your data, while you are paying for them.
Today we're launching
Together Storage Accelerator (TSA)
, a distributed caching layer for Together GPU Clusters that alleviates the need for repeated data reads from object storage and Hugging Face Hub, dramatically accelerating your AI data pipelines while also cutting your data egress bills. TSA is now included
free
with every Together GPU Cluster.
The problem: your data lives far from your GPUs
Most AI teams keep their source of truth in object storage (Amazon S3, Cloudflare R2, Together AI's T4*) or pull models directly from Hugging Face Hub. That means every cold start pays a WAN tax: cross-cloud or cross-region reads are slow, expensive (egress from AWS runs up to $0.09/GB), and rate-limited. Multiplied across hundreds of nodes pulling the same checkpoint, the waste compounds and costs you time, money, and failed jobs when the origin throttles you.
*T4 is Together AI's in data center S3 compatible object storage solution, currently in Limited Preview. Please contact sales or your account team if you are interested to try it out.
‍
TSA caches the data, improving performance, reliability and cost
TSA provides you a distributed caching layer for GPU clusters. It runs on every GPU node in your cluster and presents drop-in endpoints for the storage you already use. The first time any node reads an object, TSA caches it on cluster NVMe. As a result, every subsequent read, from any node, is served from inside the cluster at dramatically higher local speed.
The result, measured on a Together GPU Cluster H100 node:
~20× faster warm reads
than pulling from a cross-cloud origin, at up to
3.4 GB/s per node
. A 2 GiB object that took 13-15 s to download from Cloudflare R2 can be read from the cache in 0.6 - 0.7 s
Cold reads cost nothing extra
: the first read through TSA ran within ~5% of a direct download
One origin fetch, per cluster.
A 70 GB checkpoint pulled by 200 nodes downloads from the source once, not 200 times
Resilience to outages and rate limits.
Cached data keeps serving even when the upstream won't.
You can start using TSA
without making any changes to your application
. No new SDK, no rewritten data loaders, and you can get started with a single command.
Getting started:
# S3-compatible storage (S3, R2, T4, ...)
export
AWS_ENDPOINT_URL=http://tsa.tsa.svc.cluster.local:18080
# Hugging Face Hub
export
HF_ENDPOINT=http://tsa.tsa.svc.cluster.local:18080
Your existing boto3 code, transformers calls, and CLI workflows work as-is. TSA handles authentication with credentials you configure. Credentials are encrypted and securely stored in a secrets vault.
Measured results
Measured on 2026-10-28 from a pod on one H100 node in a Together GPU Cluster (us-central). Single-stream reads unless noted; clients wrote to /dev/null or node NVMe.
Read a 2 GiB object from a cross-cloud bucket (Cloudflare R2):
143–169 MB/s (12.7–15.0 s) without TSA, 3.0–3.4 GB/s (0.64–0.72 s) with TSA warm.
~20×
Read small files from the same bucket (5 KB, 2.4 MB):
320 ms and 680 ms without TSA, 5 ms and 8 ms with TSA warm.
~60–80×
lower latency
200-node cluster pulling the same checkpoint:
200 origin fetches without TSA, 1 with TSA.
200×
less egress
Measured on a Together GPU Clusters preview deployment (TSA chart 0.6.0); your results depend on origin, object sizes, and network path. Origin speed is regional: the same Hugging Face download ran 5× faster from us-central than from ca-west, so TSA's win is largest where the origin is slowest. Methodology: single-stream curl and aws s3 cp from a pod on the GPU node, repeated reads of the same object, MD5-verified against direct download.
Powered by ASTRA
TSA leverages
ASTRA
(Accelerated Storage Transport & Retrieval Architecture), the distributed caching technology we built to feed some of the largest GPU fleets in the world, including our own inference fleet. We'll share a deeper technical look at ASTRA in an upcoming engineering post.
Better together with T4
TSA works with any S3-compatible store, and it pairs naturally with
T4
, Together AI's managed object storage solution. Point TSA at your existing S3 or R2 buckets today without migrating your data. When you want your warm data living next to your GPUs permanently, T4 is one config change away. T4 is currently in
limited preview
: contact sales or your account team for access.
Get started
Together Storage Accelerator is available now on Together GPU Clusters at no additional cost. Enable it from your cluster's Settings page, or see the
docs
to go from zero to accelerated in under ten minutes.
→
Create a cluster
‍→
Read the docs
