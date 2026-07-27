---
title: "How Ant Group uses Ray to build a Large-Scale Online Serverless Platform"
url: "https://anyscale.com/blog/how-ant-group-uses-ray-to-build-a-large-scale-online-serverless-platform"
fetched_at: 2026-07-27T10:17:13.334879+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# How Ant Group uses Ray to build a Large-Scale Online Serverless Platform

Source: https://anyscale.com/blog/how-ant-group-uses-ray-to-build-a-large-scale-online-serverless-platform

Ant Ray Serving is an online service platform developed by
Ant Group
based on
Ray
. It can deploy users' Java and Python code as distributed online services and provide scaling, traffic routing, and monitoring capabilities. Ant Ray Serving users can focus on their business logic without worrying about the underlying complexity of distributed services.
This year, Ant Ray Serving has reached a scale of
240,000
cores in Ant Group, four times the scale of last year. The use cases include machine learning (ML) model inference, operational research optimization, and serverless online computing. In this blog, we introduce the key business scenarios of Ant Ray Serving in 2022 and the integration with the open source
Ray Serve
.
Link
Two business scenarios for serving architectures
In
Building Highly Available and Scalable Online Applications on Ray at Ant Group
,
we introduced the architecture design of Ant Ray Serving. The architecture remains the same this year. The following sections introduce two business scenarios running on top of this architecture: Model Serving and EventBus.
Link
Model Serving
Machine learning models are prevalent in Ant Financial’s business workflows. Efficiently and reliably serving the hundreds of machine learning models help Ant Financial to perform optimization, product recommendation, and fraud detection.
Link
Previous pain points
Without Ray Serve, model serving can be challenging. For example, Ant’s model inference services generally deploy multiple models to run traffic comparison experiments. Before using Ray, we separated each business use-case into an independent cluster, and all models for this use case were combined and deployed homogeneously in each worker process of the cluster. When the memory size of the worker process was not suitable for deploying the new model, the cluster needed to expand the memory or create a new one. Under stable traffic, this solution ensured that the cluster’s computing power (number of CPUs) did not need to scale frequently, and service management was relatively simple.
However, we found a few issues with this solution.
Difficulties with performance and traffic isolation
Firstly, because every process in the cluster loads the same batch of models, when a problem occurs in one of the models, all service instances will be affected. Secondly, the number of instances for loading the low-traffic model is exactly the same as the number of instances for the high-traffic model, which exceeds actual needs and will waste additional memory resources.
Lastly, these models only provide HTTP services for direct model inference. When the user needs to perform aggregated prediction (Model Ensembling) on ​​multiple models, the original solution deploys a unified and independent application outside the model service to provide the Ensemble Serving service. All ensemble traffic is not isolated from each other leading to risks of influencing each other.
Difficulties with elasticity given traffic fluctuations
The original solution is not required to scale computing power frequently because of traffic fluctuations, so it only needs to build relatively simple elastic capabilities. However, if the above isolation problem is to be completely solved, we can only deploy one model per cluster. This will increase the number of clusters by more than 10 times, and the complexity of operation and maintenance will far exceed the scope that the current engineering team can support.
At the same time, when the original solution is deployed based on Kubernetes (K8s), K8s has different delivery capabilities for Pods of different specifications. Larger models need to apply for K8s Pods with bigger resource specifications, and it is easier to encounter situations where the scale out needs to wait for a long time to complete.
Link
Benefits of using Ray
Ray is a general-purpose framework for distributed computing to scale your Python and ML/AI workloads. The core part provides simple but common programming abstractions, allowing Ray to complete all the basic but difficult tasks in distributed computing (memory sharing, distributed fault tolerance, scaling, scheduling, and observable functions, etc.). This philosophy allows developers to use Ray with existing Python and Java libraries and systems.
By building on top of Ray, we find a better solution to address the above questions.
Ray Serving
solves the above problems in model service.
Service isolation
Our first step is to split each model into an independent Ray service for deployment so that the service discovery and traffic of each model will be naturally isolated. Under normal circumstances, a process will only load one model, so different models will not affect each other.
This architecture also brings new challenges. The one-to-one and model-to-service strategy raises the number of services and the complexity of operation, leading to higher requirements for our automatic operation and maintenance capabilities. We discuss the work in this area in more detail in the following "Automatic Scaling."
Resource isolation
Next, in terms of isolation, we use Ray's
Runtime Environment
and add support for starting nested docker containers inside Ray worker pods. Ray Serving puts actors that load model services in containers and isolates them from each other.
This capability has three advantages. First, it can meet the different requirements of different models for their respective environment requirements, achieving flexibility. Second, it can support the isolation of data directories of different actors, without the actors themselves having to deal with file path conflicts. And third, cgroups can also be used to limit the CPU or memory and other resource requirements of different actors. We have used the Container mode in many scenarios of Ant, and verified the effect of the file system and resource isolation features in some experimental scenarios.
Automatic scaling
After deployment, the model service instance will be hosted by Ray Serving and implement the automatic scaling strategy to reduce the human cost required for operation and maintenance. Here we divide it into a two-layer autoscaling model to solve the elasticity problems of service instances and Ray clusters respectively.
Currently, our strategy is mainly based on horizontal autoscaling. Autoscaling the number of model copies will use several important indicators such as service traffic, latency, and CPU usage of the process, and make comprehensive decisions based on the moving window algorithm and the cycle prediction algorithm (STL/Holt-Winters).
The autoscaling of the Ray cluster resource itself is directed by the number of pending actors and the size of the configured resource buffer. The effect we want to achieve is that the new small service can directly start the actor without waiting for the Ray worker pod application when starting, and at the same time, the buffer will not be too large, which will lead to unsatisfactory resource utilization of the cluster.
Ant uses an independent optimization service called Cougar to make autoscaling decisions for both service and cluster workloads. Our idea is that aggregating all the data required by  autoscaling into a centralized service is more likely to make a globally optimal decision, and we are still exploring this point.
Model ensemble
The legacy approach uses an independently deployed Java application to complete the ensemble of multiple models. Because the traffic of this service cannot be isolated among the models, there have been problems in which the sudden traffic of individual models has caused the overall impact.
Thanks to the very convenient independent deployment capability and good support for multiple languages, Ray Serving can easily migrate the original Java ensemble service to Ray Actor, and deploy ensembles and models into a Ray service. In the future, we will also explore the ability to use the
Ray Serve Deployment Graph
to complete the ensemble.
Link
Scaling with Ray Serve
Based on the advantages brought by Ray and Ray Serving, the scale of our deployment in model services is gradually expanding. As of this year's
Double 11
(China’s biggest online sales event, similar to Black Friday/Cyber Monday, and over 10B RMB transactions), Ant Ray Serving has deployed
240,000 cores in the Model Serving scenario, which has increased by about 3.5 times compared to last year. The peak throughput during Double 11 was 1.37 million TPS.
Link
EventBus
EventBus is an event-driven serverless platform based on Ant Ray Serving. It was detailed in last year’s post:
Building Highly Available and Scalable Online Applications on Ray at Ant Group.
It is an end to end application built on top of Ray Serving.
Link
Platform architecture
On this platform, users can arrange the data sources and data processing functions that need processing in the form of a Pipeline. Among them, the data source defines which events the user pipeline needs to receive, and the function defines how to process the data. EventBus provides various types of Function templates, for example:
Filter
is used for data filtering,
Convert
is responsible for data conversion,
Join
can merge data from multiple data sources, and so on. Users can choose which Function templates to use as needed, and arrange these Functions in a Pipeline.
Figure 1: Eventbus Architecture
Eventbus Architecture
In terms of architecture, EventBus consists of two parts, Eventing and Serving:
Eventing
: responsible for connecting various data sources, and sending received events to Serving for processing. These data sources include various types of message, middleware, various types of RPC, and so on.
Serving
: After receiving an event from Eventing, it will be processed according to the pipeline programmed by the user. Currently, Ray Serving Java Deployment is used.
Using Ant Ray Serving to deploy EventBus as an online service is fast and convenient, and it can also make full use of Ray's scheduling, distributed fault tolerance, observability, and other capabilities. The isolation and auto-scaling capabilities mentioned in the model service can also benefit the EventBus scenario.
Link
The scale of the event bus system
As of
Double 11
in 2021, the EventBus scenario deployed a
656-core service
on Ant Ray Serving, and participated in the Double 11 promotion for the first time. During the peak period,
168,000 TPS
traffic were processed. Other indicators are as follows:
a single Actor (8 cores) peak traffic processed: 2050 TPS
maximum CPU utilization: 72.8%
average response: 49.7 ms
P99: 286 ms
As of Double 11 in 2022, the scale of EventBus will be expanded to about
4800 cores (7x growth)
. The business scenarios expand from payment processing to related use cases such as finance, insurance, and marketing. Among them, the business volume participating in the Double 11 peak has also increased compared with last year.
The peak traffic reached 325,000 TPS
. Other indicators are as follows: peak traffic processed by a
In Ant, more and more scenarios are embracing serverless applications. We expect that there will be relatively large-scale growth in this scenario next year.
Link
Open source collaboration with Ray Team
While building Ant Ray Serving, we are also cooperating with the
Anyscale
Ray Serve team, with the goal of integrating Ant Ray Serving into the open source Ray Serve architecture. These include support for Java in Ray Serve, cross-language deployment, and componentization capabilities with flexible scalability.
Our goal is that Ant Ray Serving can continue to develop on top of Ray Serve. Not only can it use the scalable componentization capabilities to meet the specific needs of Ant, but also reuse the community capabilities to meet the business, and continue to contribute to our internal functions.
Link
Ant open source contribution
At present, we have contributed Java language support in Ray Serve. Users can deploy Java code as
Serve Deployment
, and they can also manage or access Serve Deployment through Java API. With this contribution,
Serve API
can also be used across languages such as Python API to deploy and access Java Deployment.
Java business scenarios in Ant Ray Serving account for a large proportion, so the support of Ray Serve Java language is more conducive to the integration of the two architectures.
Figure 2: Ray Serving Architecture
ray-serving-adapt-ray-serve
In Ant Ray Serving, we have integrated the backend component with Ray Serve's Replica. During the Double 11 promotion in 2022, Ray Serve Replica, as the computing execution unit of Ant Ray Serving, covers business code execution in all scenarios. More in-depth work integrating other components is still in progress as part of our future plans.
Link
Future plans
Next, we will continue to integrate the architecture of Ant Ray Serving and Ray Serve.
AppMaster
is the central control role of each cluster job in Ant Ray Serving. It controls
Proxy
and
Replica
while accepting the scheduling of
ServingKeeper
.
ServeController
is the control role in the open source Ray Serve. After the integration,
AppMaster
and
ServeController
will coexist in our system. The open source
ServeController
will manage all the Proxy and Replicas. Our legacy
AppMaster
will manage the
ServingKeeper
to execute our internal unique logic and send control instructions to
ServeController
. There are also several key steps:
Merge open source and internal Proxy
Plug-in design to flexibly plug and unplug various types of components in different environments, such as state storage, service discovery, service agreement, etc
Cross-language interaction is needed between Java
AppMaster
and Python
ServeController
, and Python's
ServeController
needs cross-language control of Java
Proxy
and Java
Replica
, which requires a reasonable design of API and data transmission format.
In terms of open source contributions, we are preparing for two things:
Provide Java Ingress API so that Java users can better use Ray Serve
Provide support for C++ language in Ray Serve, so as to meet C++ business scenarios
Link
Summary
In this blog, we introduced how the Ant Computing Intelligence team built a large-scale online service system, Ant Ray Serving, based on Ray, and elevated  technical benefits to the upper platform in two typical business scenarios.
For Ant, building an online system on Ray is still in the process of exploration. We expect to have more synergies with other Ray libraries such as
Serve Deployment Graph
,
Ray Datasets
,
Ray AI runtime
, and bring more benefits to the business.
We are the team of Ant's Computing Intelligence Technology Department. We pursue an open and simple engineering culture and use technology to solve problems. Looking forward to more outstanding engineers joining us! If you have any questions, please feel free to connect on the  Ray Slack or send an email to
tengweicai@gmail.com
to discuss.
Link
Reference
Historical article:
Building Highly Available and Scalable Online Applications on Ray at Ant Group
Ray Serve:
Serve: Scalable and Programmable Serving
Java Support in Ray Serve:
Experimental Java API
