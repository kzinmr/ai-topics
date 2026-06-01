---
title: "Anyscale Announces Support for AKS, Multi-Cloud, & Multi-Region Deployments"
url: "https://anyscale.com/blog/aks-support-multi-cloud-global-resource-scheduler"
fetched_at: 2026-06-01T07:14:09.635335+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Anyscale Announces Support for AKS, Multi-Cloud, & Multi-Region Deployments

Source: https://anyscale.com/blog/aks-support-multi-cloud-global-resource-scheduler

Fig 1. Resilient, fully managed Ray clusters – VM or Kubernetes-based – in your cloud of choice
Fig 1. Resilient, fully managed Ray clusters – VM or Kubernetes-based – in your cloud of choice
In the past, multi-cloud strategies were mostly an investment for backup and disaster recovery or to avoid vendor lock-in. But as AI workloads scale in size and complexity, cross-cloud flexibility is emerging as a competitive advantage – giving organizations the ability to easily run applications wherever the latest, most cost-effective, or simply available hardware resides.
Ray, an open-source, purpose-built compute framework for scaling Python, is gaining popularity thanks to its ability to easily run anywhere and act as the common framework to run applications across any heterogeneous compute clusters. But
running Ray in production
requires deep distributed systems expertise, especially in order to reliably deploy applications across different cloud service providers and neoclouds.
To enable a broad range of organizations to deploy and run resilient and responsive distributed AI applications across a mix of providers – whether to access scarce hardware, maximize utilization of hardware commitments, accelerate innovation, or optimize cost-performance across environments – Anyscale is excited to announce:
First-Class Support for Azure Kubernetes Service (AKS):
With first-class support for Blob Storage, Anyscale offers reliable, fully featured deployments on AKS – including advanced logging and monitoring directly within the Anyscale console.
Learn more
.
Global Resource Scheduler (GRS) for Capacity Commitments:
Maximize Resource Utilization with the Global Resource Scheduler, giving you the ability to intelligently allocate workloads and ensure premium hardware never sits idle.
Learn more
.
(Coming Soon) Multi-Deployment Management:
Transcend provider and geographic limitations with upcoming support for teams to deploy Anyscale resources across multiple providers, regions, and compute stacks – all from a single logical control plane.
Learn more
.
Link
First-Class Support for Azure Kubernetes Service (AKS)
While The Anyscale operator for Kubernetes has always supported AKS, just like any other cloud-based or on-prem Kubernetes environment, today, we are announcing
cloud-native
support for AKS. This mode includes native integrations with customer-provided Blob storage and Microsoft Entra (identity) services in order to provide the full set of Anyscale features, including purpose-built Ray observability to monitor and debug distributed AI applications from inside the Anyscale console.
This expansion completes our native support across all three major cloud service providers – AWS, Google Cloud, and now Microsoft Azure. It gives you unmatched flexibility to deploy AI workloads wherever it makes the most sense, without the complexity of managing separate toolchains for each environment – so your teams can focus on innovation, not infrastructure.
To learn more read our
documentation
. Or, to get started with a self-hosted Kubernetes deployment on Azure,
contact sales
.
Link
Maximize Utilization of Capacity Commitments with Global Resource Scheduler (GRS)
Dynamic machine allocation works well for abundant resource types, but access to premium accelerators like H200s, H100s, and A100s is shifting toward a more traditional CapEx model, where an upfront purchase is required. But securing these high-demand GPUs, cloud, and neo-cloud providers increasingly requires large upfront capacity commitments. This shift is pushing companies to rethink their workload prioritization and queuing strategies.
Organizations need to prioritize critical production workloads while still enabling developers to experiment on idle capacity. Yet, dynamically allocating these fixed resources quickly becomes complex – often requiring additional software and custom systems to manage access effectively.
That's why we've developed the
Global Resource Scheduler
(GRS) – the final piece in our comprehensive compute optimization suite. While Multi-Deployment Clouds help you access resources anywhere and the Anyscale Control Plane ensures you can launch and secure those resources efficiently, GRS ensures every GPU cycle is properly utilized once you have them.
With the Global Resource Scheduler, you can:
Maximize Capacity Usage:
Whether you're using cloud capacity reservations (like those on EC2 or GCE) or on-prem hardware, GRS dynamically schedules varying workloads (batch jobs, online services, interactive development) against these fixed resource pools, ensuring premium hardware never sits idle.
Enforce Fairness with Prioritization:
The scheduler uses user-defined rules to ensure high-priority workloads receive preferential treatment, while others queue in FIFO order when resources are limited. This prevents critical production workloads from being blocked by lower-priority development tasks.
Queue Intelligently:
Instead of failing when resources aren't immediately available, workloads are held in a queue until the required capacity becomes available, reducing resource fragmentation and wasted compute cycles.
The architecture behind GRS is built on top of Anyscale Machine Pools – fixed-size groups of compute resources defined by parameters like instance types, capacity reservation details, and scheduling rules. When a workload requests resources, GRS performs one of three actions:
Allocation:
Assigns machines from the pool to the workload
Eviction:
Preempts lower-priority workloads to free up capacity for higher-priority tasks
Queueing:
Places the workload in a queue when sufficient capacity isn't available
This approach means your capacity planning isn't wasted – development teams utilize all available hardware during off-hours, while production workloads always get priority during peak periods.
GRS seamlessly works with all Anyscale compute types, giving you comprehensive control over your entire AI infrastructure:
Anyscale Jobs
for discrete production workloads like
batch inference
or
model fine-tuning
Anyscale Workspaces
for data scientists and ML engineers needing managed development environments
Anyscale Services
for deploying
Ray Serve
applications with features like fault tolerance and autoscaling
This approach ensures that critical production workloads are never starved of resources, development teams can use idle capacity when available, and your overall hardware utilization reaches optimal levels – transforming fixed capacity blocks from a management challenge into a strategic advantage.
Link
Access and Manage Resources Anywhere with Multi-Deployment Clouds
An
Anyscale Cloud
is an abstraction of resources and infrastructure necessary for managing Ray clusters. This abstraction maintains details about the cluster’s compute stack (e.g., VMs vs Kubernetes) and the underlying cloud service provider (e.g., AWS). It also offers logical isolation, making it a powerful mechanism for managing separate environments, whether for separating development and production or providing dedicated environments for different team members.
Anyscale is expanding upon the initial concept so that customers can choose to deploy Anyscale resources across multiple providers, regions, and even compute stacks within the same logical entity.
With our upcoming Multi-Deployment support, you can use Anyscale Clouds to:
Deploy resources across multiple providers, regions, and compute stacks – all managed through a single logical entity
Work seamlessly across different regions (like AWS us-east-1, us-east-2, and us-west-2)
Mix and match cloud providers (such as AWS us-west-2 and GCP us-central1)
Integrate diverse compute stacks (like VMs on AWS and your on-prem Kubernetes)
Using simple expressions, Anyscale developers will be able to request clusters using minimum resource requirements (for example, 100 A10G GPUs). Anyscale will scan all deployments within the Cloud abstraction to see where the cluster can be launched successfully, retrying different deployments until sufficient resources are available. Developers will be able to set deployment priorities, ensuring efficient access to compute while maintaining control over where workloads run.
Attaching additional deployments to an Anyscale Cloud will be as easy as provisioning the underlying cloud resources and registering the additional deployment to the desired Anyscale Cloud.
To get access ahead of this upcoming release
contact sales
.
Link
Getting Started
Together, these three capabilities – support for Azure Kubernetes, Multi-Deployment Clouds, and Global Resource Scheduler – provide a comprehensive solution to get the most value from available AI compute whether you are accessing it on-demand or via an upfront commitment.
As AI hardware continues to evolve and cloud providers evolve their hardware availability practices, Anyscale's reliable Ray cluster deployments ensure you remain agile and competitive with the ability to leverage the best available resources without disruption to your development workflows or production systems.
Try this functionality as part of a
self-hosted cloud deployment
. Or to get started,
contact sales
.
