---
title: "Introducing Anyscale Job Queues"
url: "https://anyscale.com/blog/introducing-anyscale-job-queues"
fetched_at: 2026-06-01T07:14:09.552115+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Introducing Anyscale Job Queues

Source: https://anyscale.com/blog/introducing-anyscale-job-queues

Newly available, Anyscale Job Queues enable multiple Ray Jobs to be executed on a shared cluster for batch “offline” workloads like data processing, model training, or batch inference.  Job Queues make it easier than ever to streamline job scheduling and optimize resource allocation. With Anyscale Job Queues, you’ll see:
Better Resource Utilization:
Job Queues allow multiple jobs to be scheduled on a single Anyscale cluster, increasing utilization of cluster resources. Customers using Job Queues can save on cluster re-provisioning times and by leveraging concurrency for jobs that consume fractional resources.
Simplified Cluster Management and operational overhead
Manage a single cluster
.  Multiple users and multiple jobs can be run and monitored from one place.
Governance and control:
Choose the type of machines, size of the cluster, and autoscaling parameters for a queue using Anyscale compute configs. Note the queue will require each job to have the same Ray and Python versions, but different containers and dependencies are possible.   Remove jobs from the queue as needed.
Dynamic Scaling:
The job queue cluster can be set to autoscale based on job requirements, subject to what has been defined in the compute config.
Full lifecycle management
Complete Observability
: view job information including the Anyscale Unified Log Viewer and detailed metrics to understand how compute resources are being used
Optimized Scheduling by running on spot nodes and cost efficient instances
: Jobs can run on spot nodes and queue until resources are available.  Anyscale’s Smart Instance Manage will search across availability nodes to find spot nodes or instances to deliver lower costs.
Faster Iteration:
Skip the time and resources needed to provision clusters, ensuring a smoother ramp up and reducing delays.
Advanced Prioritization Algorithms:
Job Queues support FIFO (first-in, first-out), LIFO (last-in, first-out), and priority-based scheduling, so you can ensure the right jobs are done based on urgency and workload dependencies.
Link
Anyscale Jobs and Anyscale Job Queues
Anyscale provides two ways to run Ray Job based workloads: Anyscale Jobs and Anyscale Job Queues.
For workloads with very specific resource requirements or the need to be run on newly created, isolated clusters for consistent environments or for privacy and security, Anyscale Jobs will launch an individual cluster per job–fully dedicating the cluster to that job. Anyscale will orchestrate the launch of the cluster, execution of the job, retries if applicable, and tear down of the cluster.
Shorter lived jobs, smaller jobs that can execute in parallel, or workloads that require more scheduling overhead should use Anyscale Job Queues.
Link
How Job Queues Work
Every Anyscale Job scheduled to be executed via a Job Queue will go through the following (simplified) lifecycle:
Users submit one or more jobs into the target specified queue.
Based on the scheduling policy of the particular queue, Anyscale automatically prioritizes the job and determines the position of the job in the queue based on the configured scheduling policy.
The job is submitted for execution based on its position in the queue. Anyscale ensures that no more than a set number of concurrent jobs will be running on a cluster concurrently (configurable per queue).
The job is executed until its completion, including any retries (configurable per job).
This cycle repeats continuously until all jobs added to the Job Queue have completed or errored
The lifecycle of the Job Queue cluster is as follows:
A new Ray cluster is provisioned when the first job ready for execution is retrieved from the queue.
Once all jobs in the Queue are completed, the cluster enters an idle state.
If no new jobs are submitted into the queue before idle-termination timer expiration, the Job Queue will be closed and the corresponding cluster terminated.
The lifecycle of a job queue cluster on Anyscale.
image1
Link
Next Steps and Future Enhancements
There are a number of future enhancements the team is addressing:
Improved job isolation and resource guarantees to prevent job interference and resource contention in shared environments.
Improvements  in observability and administrative functions, with a focus on refining metrics and job attributions.  This will provide clearer insights into job performance and resource utilization, essential for optimizing workflows.
More powerful scheduling options, including the ability to schedule a job for a specific time
Job Precedence and preemption—including the ability to gracefully pause a running job to replace it with a higher priority job.
Link
Learn More About
Anyscale’s New Job Queues
Getting started is easy, book a demo with our Sales team today.
Sign up for a demo
