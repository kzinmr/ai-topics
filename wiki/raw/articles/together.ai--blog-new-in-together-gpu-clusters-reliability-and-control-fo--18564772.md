---
title: "New in Together GPU Clusters: Reliability and control for production GPU clusters"
url: "https://www.together.ai/blog/new-in-together-gpu-clusters-reliability-and-control-for-production-gpu-clusters"
fetched_at: 2026-07-16T07:01:39.259354+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# New in Together GPU Clusters: Reliability and control for production GPU clusters

Source: https://www.together.ai/blog/new-in-together-gpu-clusters-reliability-and-control-for-production-gpu-clusters

We’ve spent the last several weeks shipping a set of changes to Together GPU Clusters aimed at the operational reality of running training and inference at scale: hardware fails, schedulers leak, and teams outgrow the single-admin-kubeconfig workflow they started with. This post walks through what we shipped, why we built it the way we did, and what it means for the workloads you’re running on Together today.
The changes group into two themes. The first is
platform health
: passive health checks, auto node repair, and Slinky 1.0, focused on catching and recovering from the failure modes that actually take down jobs. The second is
operational control
: a new cluster details view, external OIDC, startup scripts, and an acceptance-test opt-out, focused on giving your team the visibility, access, and customization hooks needed to run clusters as your organization grows.
Catching and fixing failures as they happen
If you’ve run a multi-day training job on a large cluster, you know the pattern. A GPU falls off the PCIe bus. An Xid error takes a node out of rotation. Thermal throttling silently caps a job’s throughput and you don’t notice until the loss curve flattens.
These are steady-state failure modes at scale. What matters is how quickly you catch them and how cleanly you recover.
We already ran
active health checks
, synthetic tests that exercise the hardware against a known-good baseline. Active checks are useful at provisioning time and on idle nodes. Passive checks extend that coverage to failures that appear while real workloads are running.
Fig: Health checks tab shows all the active health-checks currently running and the historical information
So we built
passive health checks
, which work like alerts and run continuously across every node in your cluster, observing real workloads, logs, and metrics to surface degradation as it happens. The coverage list today includes GPUs falling off the bus, thermal throttling, Xid errors, Slurm node drains on failure, and an expanding set of hardware and software failure signals.
The checks observe live workloads with near-zero overhead on running jobs. Learn more about health checks
here
.
Fig: Repair tab for node repair recommendations and repair history of the cluster
Detection on its own is just a dashboard, so we paired passive checks with
auto node repair
. When our monitoring system detects a node-level issue, it generates a recommended remediation and surfaces it for an operator to review. There are four repair actions, mapped automatically based on the failure signature:
Reboot:
In-place restart that preserves local data. The default for transient issues
Reprovision:
Rebuilds the node from a clean image and clears local data
Failover:
Moves the workload to a fresh bare-metal node and clears local data
Remove:
Pulls the node out of the pool and sends it to RMA
We believe in automation with a human touch: Your training checkpoints and inference replicas are too valuable to risk on automated drains. Our 'human-in-the-loop' approach keeps you in control — the system detects and recommends, you approve, and Together handles the graceful recovery. It’s the perfect balance of intelligence and safety. We’re already building fully automated node-repair options for specific failure modes, but for now, we prioritize keeping your production workloads uninterrupted. Learn more about node auto repair
here
.
The result? You’ve traded hours of support tickets for minutes of in-product workflow. From detection to resolution, you’re back in the pool faster than ever.
Together Slurm-on-K8s 2.0: The future of Slurm on Kubernetes
Running Slurm on Kubernetes shouldn't feel like a constant battle against crashing daemons, zombie processes, or scheduler drift. We’ve rebuilt our Slurm-on-Kubernetes stack from the ground up, based on our fork of OSS project Slinky, to make those 'scale-at-failure' headaches a thing of the past.
Here’s what our upgraded stack brings to your cluster:
Self-healing worker daemons:
Transient failures are inevitable, but they shouldn't take down your node. Our new stack supervises workers, auto-restarting them in place so long training runs stay resilient.
No more zombie processes:
Forget the days of orphaned processes clogging your PID tables and blocking new jobs. Our stack automatically reaps orphans, ensuring your nodes stay clean and ready for work, every single time.
Durable job accounting:
sacct
history used to live on ephemeral storage, which meant a pod restart could wipe your entire accounting database. We've moved accounting to durable, PVC-backed storage, so restarts and reschedules no longer touch your data. Billing reconciliation and post-hoc job analysis stay intact across the lifecycle of the cluster.
Reliable process cleanup:
When jobs ended, daemonized child processes used to slip out from under Slurm's view and stay running — holding GPU memory and /dev/shm segments hostage between runs, sometimes for days until someone cleaned them up by hand. The new stack tracks every descendant of a job at the kernel level and cleans them all up reliably at job end. The next job on the node starts on a clean machine every time.
Accurate GPU state after reschedules:
After a pod reschedules, Slurm's view of which GPUs existed used to drift from reality — stale GPU identifiers from the previous incarnation would mismatch the real hardware, and affected GPUs would silently drop out of the schedulable pool. The new stack rebuilds Slurm's GPU view fresh on every node start, so the schedulable pool always matches the hardware actually in the node.
Beyond reliability, our new stack exposes DCGM metrics in your cluster's Grafana dashboards, so you get fine-grained per-cluster GPU utilization visibility out of the box.
All newly provisioned Slurm clusters run on the latest stack by default. If you're on an existing managed Slurm cluster, we can migrate you in place at no cost via. a maintenance window — contact your account team to schedule. Learn more about Slurm-on-K8s GPU Clusters
here
.
Operational control
Reliability is half the picture. As clusters grow across teams, access, visibility, and customization become operational problems in their own right. More people need access, with different permissions. Operators need to know what’s happening on the cluster without SSHing into nodes. Workflows need customization without turning every change into a support ticket. Below are the latest features that we built to enable our users to adapt to their most critical needs.
A new cluster details view
We rebuilt the cluster overview page around the three questions operators actually ask about a cluster:
Is it healthy?
Is it being used?
What's happened to it recently?
The new view surfaces node health at a glance: healthy, booting, unhealthy, pending, and paused. It also shows live usage metrics across all GPU nodes, including utilization, memory, and network bandwidth, with drill-down to Grafana for deeper analysis. The same page includes an event timeline showing node state transitions across the cluster and the cluster’s full configuration in one place: region, GPU type, driver version, networking, OS image, and billing rate.
Three new tabs sit alongside the overview:
Nodes
to give a detailed list and grid view with utilization data, health signal, and node operations like repair/run health-check and ssh commands.
Health checks
give you the historical timeline of active and passive check events for the cluster.
Repair
gives you the same historical view for node repair actions. Both exist for the incident retro question, “what actually happened on this cluster last week?”, and they replace what used to be a Slack thread with us.
‍
Fig: Cluster overview page for high level health and utilization information
‍
Fig: Nodes page for node details information and actions
External OIDC for Kubernetes RBAC
If your team accesses the Kubernetes API today, you’re probably sharing the admin kubeconfig. That works for one operator and breaks down quickly past that. Teams need per-user audit trails, per-user revocation, least-privilege access, and a cleaner path for joiners and leavers.
We’ve added
External OIDC support for K8s RBAC
to solve for this. You can now configure a cluster to authenticate against your existing identity provider (IdP), including Google, Okta, Auth0, Microsoft Entra ID, or another OIDC-compatible provider. Each team member runs kubectl with their own identity, the API server validates their token against your IdP, and standard Kubernetes RBAC controls what they can do via ClusterRoleBindings and RoleBindings. You get per-user Kubernetes access, revocation through your IdP, audit trails tied to individual users, and standard Kubernetes RBAC for least-privilege access.
For teams managing access at any meaningful scale, this is a significant unlock. The admin kubeconfig becomes a break-glass tool. Joiners and leavers are handled in your IdP, where they should be. And the audit trail of who did what on the cluster comes from a system your security team already trusts.
External OIDC must be configured at cluster creation time. See the
OIDC setup guide
for the full flow, including provider-specific notes for Auth0, Okta, and Google. Together OIDC support for Slurm and Kubernetes clusters is coming soon.
Startup scripts for cluster customization
Most production clusters need some kind of setup that isn’t in the base image: internal packages, scratch space prep, monitoring agents, Slack notifications when a job finishes. We were watching customers SSH into every node to do this by hand, or file support tickets and wait on us. Startup scripts move that setup into cluster configuration as a self-serve capability.
Startup scripts
let you customize Slurm worker nodes, login nodes, and the controller via shell scripts that fire at specific lifecycle events:
At node boot:
install packages, configure tooling, run any setup that needs to happen before the node accepts work
At job start:
stage data, prepare scratch space, configure the per-job environment
At job end:
clean up scratch files and stray processes, send Slack notifications, kick off downstream pipelines
Scripts are configured in the Together Cloud console and can be applied to new clusters at creation time with no rebuild required. The result: The customizations you’d otherwise file a ticket for, or run by hand, are now declared once and applied automatically across the cluster. We even validate the scripts for errors so you do not face silent failures later. Learn more about how to set up startup scripts based on customizations
here.
‍
"Slurm startup Scripts"; startup scripts configuration in the console
Acceptance testing, opt-in for larger and longer-running clusters
At Together AI, we serve both large-scale production training/inference workloads as well as short burst experimentation or single-node research clusters. For these smaller or short-lived clusters, we skip the acceptance test battery by default, which validates GPU health, networking, and storage, and go straight to availability. For most clusters, faster time-to-availability is the better default: less waiting and faster time to value, especially given we constantly run health checks on idle nodes in our fleet.
For larger clusters or long-running training jobs, the calculus flips. Catching a bad node at provisioning time is much cheaper than catching it on epoch 47, and the cost of validation is small relative to the lifetime of the cluster. For these cases, we recommend enabling acceptance testing at cluster creation.
This is a deliberate tradeoff, and we surface it in the UI: acceptance tests are disabled by default for faster provisioning; for multi-GPU training or long-running production clusters, we recommend enabling it at cluster creation time.
What changes operationally
Taken together, these changes give operators a shorter path from “something is wrong” to “the cluster is usable again,” with health signals, repair actions, access controls, and cluster history in the product.
Researchers and ML engineers get greater reliability and resilience for their jobs from hardware faults and clearer signals when something degrades. Platform teams get a better control surface for access, repair, customization, and incident review. Operators get durable accounting data, per-cluster GPU utilization metrics, and a cluster view that answers the basic questions first: is it healthy, is it being used, and what happened recently?
What’s next
The themes you’ll continue to see from us: more failure modes covered by passive health checks, more remediation actions safe to automate end-to-end, deeper observability into what’s actually happening on your nodes, and continued investment in the Slurm and Kubernetes stacks that most large training jobs depend on.
If you’re running training or inference workloads on Together GPU Clusters and any of this is relevant to what you’re hitting, get in touch. We’re the team that built it, and we’d like to hear what’s working and what still needs to be easier.
→
Share feedback
→
Book customer office hours
→
Read the docs
‍
