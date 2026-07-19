---
title: "Building Highly Available and Scalable Online Applications on Ray at Ant Group"
url: "https://anyscale.com/blog/building-highly-available-and-scalable-online-applications-on-ray-at-ant"
fetched_at: 2026-07-19T07:01:16.356376+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Building Highly Available and Scalable Online Applications on Ray at Ant Group

Source: https://anyscale.com/blog/building-highly-available-and-scalable-online-applications-on-ray-at-ant

Ant Group has developed Ant Ray Serving which is an online service framework based on
Ray
, which provides users with a Serverless platform to publish Java/Python code as online services. The platform provides users with basic capabilities such as deployment, scaling, traffic routing, and monitoring. This allows users to focus on their own business logic and use Ray's distributed capabilities to develop online applications.
Ray provides a simple and easy-to-use distributed API, flexible scheduling and other capabilities, so that Ant Ray Serving and its users can quickly build a distributed application on this basis, and provide reliable services. Up to now, 5 different usage scenarios have been supported within Ant and Alibaba. Ant Ray Serving has reached a scale of 60,000 cores and 5,000 nodes, and has participated in many years of Double Eleven, Double Twelve, and Chineses New Year’s promotion scenarios.
In this article, we will introduce how Ant's Ray Serving team designed this framework, what work has been done to make it highly available and easy to expand, and its relationship with
Ray Serve
.
Link
First Use Case: Online Distributed Computation
Let us first introduce the first problem we encountered. In 2018 or so, our colleagues in the Ant payment department encountered some computational problems. They developed a system to calculate the indicators and strategies for payment institutions which need to run as online services to support bank card payment transaction flow. When more and more payment institutions and banks became connected, a scaling problem arose.  Specifically, they found that the performance of a single server could no longer complete all computing tasks in time. The logic and dependence of the strategy logic itself is complicated, and the cost of reconstruction is also very large when doing distributed transformation.
The following is a simplified pseudo-code of a typical strategy. The calculation is usually divided into three layers. Each layer has a for loop to split the calculation task into more  granular tasks. It then merges the split task results with post-processing to generate the final result.
public
class
Strategy
{
public
void
calc
(
long
time, Map banksAndIndicator)
{
for
(Entry e : banksAndIndicator.entrySet()){
String bank = e.getKey();
for
(String indicator : e.getValues()){
calcIndicator(time, bank, indicator);
}
}
// do all banks & indicators' data calculation
}
public
void
calcIndicator
(
long
time,
String bank,
List indicators)
{
for
(String indicator : indicators){
calcBankIndicators(time, bank, indicator);
}
// do indicators' data calculation
}
public
void
calcBankIndicators
(
long
time,
String bank,
String
indicator)
{
// do bank data calculation
}
}
Our goal was to help colleagues in the payment department design a new system that can distribute these computing tasks at a relatively low cost and solve the single machine bottleneck. When we discovered
Ray
, we thought that Ray was a very suitable computing framework to solve this problem.
Link
Why Ray?
With Ray, computing tasks can be easily expanded from the original single-machine serial execution to distributed asynchronous execution. Ray's Remote API makes it possible to submit tasks to the computing cluster, dynamically split tasks into more fine-grained computing tasks, execute them in parallel, and collect calculation results asynchronously. Thanks to Ray's very simple and easy-to-use API, users only need to make some fairly simple changes to refactor their code in a distributed manner.
Distributed task process with Ray
Distributed task process with Ray
To build such an online distributed system on Ray, there is still a lot of other work to be done. First, for each Ray Job started by users, an AppMaster needs to be started. The AppMaster is responsible for all control plane work, such as creating and managing all Actors for computation, saving some internal job metadata, and all Actor Handlers, and so on.
The computing task itself has no state in this scenario. Because we need to provide computing services to the upstream system, all of our tasks use resident actors to perform calculations to save process and dependency initialization time. The calculated actors are divided into two categories, namely Trigger Actor and Worker Actor. The former is responsible for starting an RPC service in the Actor and accepting external computing task requests, and the latter is responsible for undertaking distributed computing tasks.
After the user's initial Trigger Actor and Worker Actor are started, Trigger's RPC service accepts external requests. When the computing task reaches the Trigger, the Trigger will split the computing task of the first layer, and hand it over to a Dispatcher role to select the appropriate Worker Actor in the next layer, and dispatch the computing task through the Ray call. The working mechanism of the next layer of Worker follows the same dispatch mechanism.
The final system we designed is shown in the figure below.
New distributed system design
New distributed system design
This Ray-based online distributed computing system reduced the computing time of a task to under 200ms. With additional work on Ray, this monitoring decision-making problem of the payment department has been reduced from the previous minute-level delay to the second-level, and very good results have been achieved.
Link
Other Online Use Cases
The use case shown above was the first online calculation problem we used Ray to solve. We have continued to encounter other similar online scenarios.
The first is model service. The online learning system of Ant Group is based on Ray. The training module will continuously export the model iteratively, usually every 10-30 minutes. We need to deploy the model as a service as soon as possible. In addition to online learning, model services also have requirements for heterogeneous and multi-modal joint reasoning. Ray facilities design and implement good end-to-end solutions through Ray scheduling and remote calls that satisfies all these requirements.
Inference with Ant Ray Serving
InferenceAntRayServing
There is also the
FaaS
scenario that we've been exploring since
2020
which is to use a system similar to Knative Eventing to convert message consumption into RPC calls, trigger the user Function in a Ray Actor for data processing, and use Ray to implement the serverless function with scalability. In the future, we may also explore the capabilities of some distributed functions in Ray.
FaaS with Ant Ray Serving
FaaS with Ant Ray Serving
In addition, we have also built service capabilities on Ray in online operations optimization scenarios. For details, see
Online Resource Allocation with Ray at Ant Group.
Link
Design goals of generic online computation / learning framework)
From the above online scenarios, we can see that a general service framework is necessary. There were several challenges in creating such a system on Ray:
1. Achieve 99.9%+ high availability: As we all know, Ray is a stateful distributed system, and its operation and maintenance is more complicated than a stateless system. At the same time, the head node of Ray is still a single point of failure, and there is no solution to upgrade the Ray job in a non-disruptive way yet.
2. Achieve efficient update capability: when the user's model and code change, the service instance needs to be able to update the new model and code online as quickly as possible without breaking the SLA promised to the user, such as updating 500 instances within 10 minutes.
3. Easy to scale and can quickly adapt to changes in traffic (autoscaling).
Link
Overall architecture
Let's take a look at the overall structure of Ant Ray Serving, so that we have an overall understanding of roles and concepts.
Ant Ray Serving Architecture
Ant Ray Serving Architecture
Serving Client: This SDK encapsulates APIs for deployment/update control plane requirements, and data plane requirements for service calls, and provides a key interface for users to implement their own calculation logic.
AppMaster: As described earlier, AppMaster is the central control of a user's Serving job; it is responsible for all control plane tasks in the job, such as creating and managing all calculated Actors, saving some job internal metadata, and all Actor Handles
Backend: Responsible for executing the calculation logic implemented by the user.
Proxy: Responsible for publishing services and attaching to the service discovery module, and responsible for routing external requests to the corresponding Backend for processing.
Serving Keeper: Responsible for multi-cluster orchestration, traffic control, and coordination of user services.
Link
Some Key Designs
Multi-cluster service
In the area of ​​high availability, it is natural that we first adopted a multi-cluster deployment and disaster recovery solution. In order to add multi-cluster support without adding too much complexity to users, we introduced the role of Serving Keeper.
The positioning of Serving Keeper is to support service publishing across Ray clusters to support cluster disaster recovery and cluster updates that still maintain high availability online service SLAs. It can run on the K8S cluster as an external service, or run on the Ray cluster as a meta Serving job. Serving Keeper saves all the state in external storage (such as MySQL), so it can ensure high availability through multi-instance deployment.
When submitting a Serving job, you only need to add a multi-cluster deployment configuration, and the Serving Client will route the submission request to the Serving Keeper, which automatically selects multiple Ray clusters to start the Serving job according to the configuration. When each independent Serving job is started, an AppMaster Actor will be created, publish the RPC service and register itself to the Serving Keeper to receive control instructions. All subsequent control instructions for this cross-cluster job will be distributed by the Serving Keeper to the corresponding Serving AppMaster, and each job will be coordinated to complete complex workflows such as rolling upgrades.
In order to support user services that can be deployed across clusters, we also need to support service discovery across clusters. In the current architecture, Proxy will actively register its service address to the service discovery component shared by multiple clusters after publishing the service.
Currently, we use the cross-cluster service component developed internally by Ant and Alibaba. It provides two-level service discovery capabilities. The second level usually needs to undertake service discovery for 2-4 Ray clusters. The user application can query all the callable addresses on the client, and preferentially select the address with the network topology closer to itself to initiate RPC calls.
Currently Serving Keeper supports the following functions:
Automatic orchestration of multi-cluster jobs (unitized deployment architecture)
Agent control instructions for multi-cluster (auto scaling up/down, update)
Coordinate the traffic ratio and capacity between clusters according to clusters and capacity events
Support multi-cluster blue-green release and canary release
State Persistence
In the Serving job, each AppMaster Actor is responsible for the management of the job. It stores many current job status, such as service metadata, Proxy/Backend Actor Handler, number and status of replicas, etc. When the Ray cluster where the job is located is down or restarted, the metadata will be lost from the internal state of AppMaster. Our desire is that when the Serving job is restarted in the cluster, metadata and the status of the entire job can be automatically restored.
Therefore, we have designed a state management module in AppMaster, and the data mentioned above will be taken over by this module as the state. When some data in the state changes, it will be immediately persisted to the external storage by the state management module.
If AppMaster only fails over itself, it only needs to read the external storage to restore the state in the memory. However, if the Ray job is restarted, information like Actor Handler will no longer be valid and can be reset directly. AppMaster will enter the recovery state, rebuild the Proxy/Backend according to the configuration, and restore the service state after the rebuild is completed.
Continuous Updates
In Ant's current Ray Serving cluster, thousands of update operations are triggered every day, most of which are completed within a few minutes to ten minutes, and have almost no impact on SLA. In ] practice, we found that there are several important points that can greatly improve the update speed and stability:
1. Select the appropriate update step size when updating, and remove the traffic first before updating
2. Try to use in-place updates to avoid the need to create new Actors.
Scalability
Ray itself is very good in terms of scalability. When running on the cloud, K8s or Yarn, the open source version can be automatically scaled based on
Autoscaler
. Inside Ant, there is an internal auto-scaling component to complete the autoscaling of the cluster.
However, at present, the expansion and contraction of our services is done more by providing APIs and handing it over to users. It is actually a very challenging task to complete the automatic expansion and contraction of the service according to the traffic and load. The main difficulties include how to ensure that the strategy is accurate enough and that the expansion is fast enough.
Ant Ray Serving has currently completed the development of the autoscaling system, but the autoscaling strategy and algorithm development are still under further experimentation and verification. We are currently planning to use time series-based forecasting, machine learning models and more.
Link
Summary
To summarize, we have introduced multi-cluster architecture, service discovery, state persistence, in-place update, and more to make Ant Ray Serving a robust and flexible online system. It has been developed in Ant for more than 3 years, has a scale of close to 5,000 nodes, and supports more than 5 different usage scenarios within Ant and Alibaba.
Link
Future plans
In the future, we plan to improve the performance of updates and serving, apply auto scaling  strategies in the production environment, and explore more complex scenarios such as multi-modal joint reasoning and distributed computing.
In addition, we are working with the Anyscale Ray Serve team to support Java in Ray Serve, create flexible and expandable component capabilities, and contribute other practical features. We plan to merge Ant Ray Serving and open source Ray Serve in late 2021.
If you have any questions about Ant Ray Serving, please feel free to contact me on Ray's Slack or by sending an email to tengweicai@gmail.com. Thank you.
Link
About us
We are the team of Ant's Computing Intelligence Technology Department, spanning Silicon Valley in the United States, Beijing, Shanghai, Hangzhou and Chengdu in China. The engineer culture we pursue is openness, simplicity, iteration, efficiency, and solving problems with technology! We warmly invite you to join us!
Please contact us at
antcomputing@antgroup.com
