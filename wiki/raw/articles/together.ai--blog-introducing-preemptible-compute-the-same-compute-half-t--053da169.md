---
title: "Introducing preemptible compute: the same compute, half the price"
url: "https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price"
fetched_at: 2026-09-11T10:01:12.358645+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Introducing preemptible compute: the same compute, half the price

Source: https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price

Today we're announcing the public preview of preemptible compute for Together GPU Clusters, available on Kubernetes clusters in all regions. Preemptible nodes give teams a lower-cost way to run interruption-tolerant work — short experiments, inference bursts, batch jobs — on the same GPU infrastructure they already use, billed sub-hourly at a flat 50% of the on-demand rate. You can add preemptible capacity to a new or existing cluster starting today.
‍
How preemptible compute works
Preemptible compute adds a second compute type to Together GPU Clusters. Standard nodes are fulfilled synchronously and are never preempted. Preemptible nodes use the same NVIDIA accelerated compute, draw from un-used capacity, and can be reclaimed when that capacity is needed elsewhere.
Preemptible nodes are billed at a flat 50% of the on-demand rate. The rate remains fixed rather than moving with a spot market.
When a node is reclaimed, the cluster follows a five-minute drain (maximum 5 minutes) sequence:
T+0
— the node is cordoned, a
TogetherPreempted
Kubernetes event fires, and your pods receive SIGTERM.
T+0 to T+5:00
— your workload has up to five minutes (
terminationGracePeriodSeconds
) to checkpoint and exit.
T+5:00
— the node is removed.
The cluster retains its preemptible target after the node is removed and automatically refills toward that target as capacity becomes available. You do not need to request replacement capacity.
Billing is sub-hourly, with usage metered every one to two minutes. A node that runs for 12 minutes is billed for approximately 12 minutes.
Preemptible nodes are not a separate cluster type. They join your existing cluster, labeled
together.ai/compute-class=preemptible
, so interruptible workers run on discounted capacity while coordinators, login pods, and serving replicas stay on standard nodes.
Where preemptible compute fits
The five-minute reclamation sequence makes recovery behavior the deciding factor. Work that can resume, retry, or requeue can use preemptible capacity while critical components should remain on standard nodes.
Short experiments.
Ablations, config sweeps, quick fine-tunes, evals, distillation, and batch inference are good candidates when the work can resume from a checkpoint or retry after a worker disappears. Frameworks such as Ray Train and PyTorch Lightning resume from the latest checkpoint without intervention. As a reference point, a full weight model checkpoint for GLM5.3 Flash, 321B parameter model is roughly 3.5TB which would take between 22s to 4mins to write to a parallel filesystem even at degraded performance. Leaving headroom inside the five-minute drain window.
Temporary bursts.
When batch or internal inference demand spikes, add cheaper preemptible nodes to absorb the burst and non-critical workloads instead of holding standard capacity sized for your peak or risking burst standard compute availability. Interrupted requests requeue; user-facing replicas remain on standard nodes.
The common thread: work that is chunked, checkpointed, or retryable. Multi-day runs without checkpointing and strict-SLO serving with no fallback are not a fit.
Together has a strong culture dogfooding , several internal research, dev/test and non-critical production workloads at Together are based on our preemptible compute based GPU clusters enabling us to leverage our spare capacity across product teams.
Before you enable it
Treat preemptible nodes as ephemeral.
There is no minimum node lifetime during the preview, so checkpoint frequently and plan for capacity to disappear at any time.
Keep critical components on standard nodes.
Coordinators, login pods, and user-facing replicas belong to guaranteed capacity — use the
compute-class
label to enforce it.
Use the drain window.
Set
terminationGracePeriodSeconds
to as much as 300 seconds, checkpoint when the pod receives SIGTERM, and exit before the node is removed.
Clusters require at least one standard node
, and nodes can't be converted between compute types in place.
How to use it
After the workload is prepared for preemption, setup has two parts: set the preemptible target and schedule eligible work onto the labeled nodes.
You can set the target when creating a cluster or on a cluster that is already running, using the Together Cloud console, CLI, or API. The API reports both the requested target,
desired_preemptible_gpus
, and the capacity currently live,
allocated_preemptible_gpus
. Because preemptible nodes draw from unused capacity, allocated capacity can remain below the desired target when capacity is tight.
On a new cluster
Choose your standard node count, then add a preemptible target on top.
tg beta clusters create \
  --name my-cluster --region us-central-2 --gpu-type RTX_6000_PCI \
  --cluster-type KUBERNETES --num-gpus 8 --billing-type ON_DEMAND \
  --num-preemptible-gpus 8 \
  --project-id
On an existing cluster
Scale up the preemptible target when you need additional worker capacity, then lower it when the work is complete. The cluster remains running throughout.
tg beta clusters update
--num-preemptible-gpus 16
Fig: Adding/Deleting Preemptible nodes to an existing cluster
Fig: Preemptible nodes follow the “gpu-preemptible-xxx” naming convention
Scheduling work on preemptible nodes
Target preemptible nodes explicitly:
nodeSelector:
  together.ai/compute-class: preemptible
Preemption notices are delivered as SIGTERM to the pod, as Kubernetes events (
reason=TogetherPreempted
), in the console's Event Timeline, and via the Together API's
node_lifecycle_events
— handling patterns are covered in
the docs
.
Preemptible compute is now in public preview on Kubernetes clusters. Slurm support, additional regions, and in-place conversion between compute types are planned next.
→
Create a cluster
→
Read the docs
