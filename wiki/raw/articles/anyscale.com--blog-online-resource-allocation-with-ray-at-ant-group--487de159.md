---
title: "Online Resource Allocation with Ray at Ant Group"
url: "https://anyscale.com/blog/online-resource-allocation-with-ray-at-ant-group"
fetched_at: 2026-07-19T07:01:16.369431+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Online Resource Allocation with Ray at Ant Group

Source: https://anyscale.com/blog/online-resource-allocation-with-ray-at-ant-group

Double 11 has become the largest online shopping event in the world. To support this level of online activity, Ant Group has implemented a flexible, high-performance, stable, and scalable
online resource allocation system
based on
Ray
. The system’s deployment scale has reached more than 6000 CPU cores, and it is currently used for a very wide range of application scenarios including marketing and order allocation. In order to do this, there were many technical challenges that needed to be considered like:
How to reduce the cost of development and maintenance of multiple systems due to the complexity of engineering links across online, nearline, and offline systems.
How to achieve high-performance solutions with large-scale linear programming (LP) problems.
How to ensure high availability of online services when the SLA required is 99.99%, that is, service downtime in one year should not exceed one hour.
This post uses marketing, search, recommendation, and advertising scenarios as examples to introduce some applications of the online resource allocation system based on
Ray
.
Link
1. Problem description
In recommendation, search, marketing and advertising systems, online decisions need to consider preference indicators such as click through rate and conversion rate as well as restrictions like capital, cost, and traffic. Online resource allocation is about maximizing the overall ROI under the constraint of limited resources. For example:
The increase of purchase rate brought by coupons
The increase of purchase rate brought by coupons
When there are only two coupons in total, the traditional way to maximize the total sales volume is to allocate coupons based on first come, first served. Using this approach, user1 and user2 get coupons, but user3 and user4 do not. Based on Table 1, this is not ideal as the CVR Uplift is higher for user3 and user4. A better way to allocate coupons would be to give them to user3 and user4 so that the overall revenue of the platform is maximized.
Link
2. Abstract model of online resource allocation
In an online resource allocation system, it is necessary to match the appropriate resources online for each incoming request while considering the limited resources available in order to maximize the revenue of the whole system. In the context of the coupon case, the subject of the request is the user, and the resource is the coupon. For each user
i
, the platform can estimate the revenue value
of
j
coupons and choose one of them to push to the user. When there are no resource constraints, every online decision is to choose the one with the largest
. When there are resource constraints, such as each coupon
j
having an inventory limit, the optimal solution is not trivial. Suppose that there are
K
resource constraints
in total, and each user
i
is given
copies of a coupon j, each of which will consume
from the kth resource constraint. Then the online resource allocation can be modeled as an LP problem
to solve for the decision variables
which maximize the overall revenue under the global resource constraints
. For industrial application scenarios, such as recommendations, search, and advertising, the variable scale of the problem is often 100 million (users) * 10000 (candidate set), and the resource constraint scale can exceed 10000.
From the perspective of real-time decision-making, future information is unpredictable and the global optimal solution cannot be determined in advance. In order to solve this problem, we need to consider the estimation and uncertainty of future information. On one hand, we can decompose the global problem into real-time subproblems for learning. Considering that the environment of an online application changes rapidly, subproblems need to be solved with high timeliness (minute level). On the other hand, we need to be able to service a single decision request quickly.
In the design of the implementation scheme, we disassembled different technical modules, including:
Online resource allocation scheme in a recommender system
onlineDecisionRealTimePlanning
The online decision service uses the equivalent form of the problem from the
linear programming duality
, and takes the dual variable
calculated by a real-time programming algorithm as the input parameter to realize fast online serving.
In the technical scheme of a real-time planning algorithm, around the control of precise budget control and revenue estimation, several algorithm modules were designed, including:
Real time model calibration: probabilistic calibration (such as CTR and CVR) of the prediction of the pre model can be carried out in combination with real-time user feedback to ensure good point estimation property.
Real time traffic prediction: estimate the traffic of the scenario and activity in the future, and split and smooth the total budget in real time.
Real time constraint correction: considering the uncertainty or lag of the consumption of some resources, we need to combine the actual consumption of resources to correct for the expected budget consumption progress in real time.
Large scale/Online LP Optimization: solve the planning problem of maximizing revenue under given constraints.
The implementation of these algorithms involves offline, nearline, and online links as well as different computing paradigms. Online is directly for user requests, synchronized RPC calls, and requires high availability and low latency (ms level). Nearline allows for real-time planning based on a snapshot of online request results. It can adopt the optimization algorithm and return the needed solution result within seconds. Offline allows for flow estimation according to historical data, and can return the needed solution result within minutes.
The following diagram shows the logical architecture of the online resource allocation system based on Ray.
Logical architecture of the online resource allocation solution
architectureOnlineResourceAllocationSolution
Link
3. System Architecture and Implementation
The online resource allocation solution involves a complex engineering implementation relying on offline and real-time data. The algorithm’s implementation relies on both real-time and iterative calculations. We built streaming, serving and iterative calculations based on Ray. The physical architecture is shown in the figure below:
Physical architecture of the online resource allocation solution
Physical architecture of online resource allocation solution
The logic of the real-time planning algorithm based on Ray includes:
An iterative calculation which pulls historical data and uses a time series model to predict future traffic data.
Stream processing of real-time data and generation of batch samples. When the LP solution cycle is reached, streaming sends batch samples to serving. After receiving batch samples, serving uses them to solve LP optimization problems. Ray’s
placement group feature
is used to deploy the solver's actor on the GPU machine, and the GPU is used to parallelize the algorithm.
Online learning and training of a real-time calibration model. The natural networking characteristics of Ray actors are used to realize the iterative calculation of the bulk synchronous parallel mode.
Ray streaming which can be used to accumulate the real-time allocation results to correct the LP algorithm when there is a gap between the final result of the business system resource allocation and the result of the algorithm decision.
After the dual variables are solved, they can be directly used in online rerank, which is an online system which requires high SLA. An online service framework was built based on Ray. It allows users to publish any business logic as an online service and control traffic without care about resource deployment, resource scaling, and cluster disaster recovery.
Physical architecture of online rerank
PhysicalArchitecture
Each online service instance is a Ray job consisting of three types of Actors：
Master Actor: It manages Router Actors and Worker Actors.
Router Actor: It is responsible for receiving requests from the business systems and routing requests to the designated Worker Actors according to the traffic control policy.
Worker Actor: It receives requests from a Router Actor and executes user-defined business logic.
In the case of multiple data centers/Clusters, this online service framework includes a component named Keeper, which ensures that users' online service jobs can be started in each Ray Cluster, and that traffic switching can be carried out between Clusters, so as to achieve the ability of failover between Clusters.
Once an online service instance is created, it can be called by the online business systems through the Client provided by this framework. The online service request will be received by the Router Actor in the Ray job and routed to a Worker Actor to execute business logic.
Online resource allocation based on the Ray scheme has the following advantages:
Ray provides a simple and easy-to-use API. Developers can quickly implement the upper framework. For example, we use
50 lines of code
to implement the iterative calculation of bulk synchronous parallel mode. The offline, nearline and online links involved in online resource allocation are all implemented based on Ray, which greatly reduces the learning and maintenance cost of development.
// Driver
public
class
LpMain
{
public
static
void
main
(String[] args)
throws
Exception
{
// Step1: Divide offline data into partitions.
// Step2: Start actors to load the data of the corresponding partition.
for
(....) {
Ray.createActor(...)
}
// Step3: Start a Merger actor.
merger = Ray.createActor(...)
// Step4: Start solving.
result = Ray.call(Merger::solve...).get();
}
}
// Merger
@RayRemote
public
class
LpMerger
{
public
Result
solve
()
{
Result res =
new
Result();
// Iterate until the result is converged.
while
(res.isConverged()) {
// Call all workers to start local calculation.
workes.forEach(wk -> {
workerResult = Ray.call(LpWorker::calculate, wk, ...).get();
// Merge the calculation results of the workers.
res.merge(workerResult);
});
}
return
res;
}
}
// Worker
@RayRemote
public
class
LpWorker
{
// Load the data of the corresponding partition.
public
LpWorker
(...)
{...}
public
LpWorkerResult
calculate
(...)
{...}
}
Ray supports convenient resource scheduling. Through placement groups, IO operations, and GPU support, algorithms can be easily deployed to the nodes of corresponding resources to make full use of heterogeneous acceleration. Compared with just using CPUs, the performance of the algorithm can be improved dozens of times.
Ray actors have second level fault-tolerant recovery ability, and can sense whether the remote calling actor is abnormal within one second, so it can forward the request to other alive actors, ensuring the availability of the service.
Link
4. Summary
The online resource allocation solution based on Ray has been running stably in Ant Group, successfully supporting large-scale activities such as Double 11 and Double 12 where the deployment scale reached more than 6000 CPU cores. At present, LP optimization problems with millions of variables and hundreds of constraints are solved in seconds based on Ray using a single GPU card. To prepare for increased future demand, Ant Group is currently exploring GPU-based LP solutions on Ray -- with multiple GPU cards on the same machine, or multiple GPU cards across multiple machines. This is in addition to Ant Group’s other uses and contributions to Ray. For example,
Ant Group also uses Ray as a distributed computing foundation for it’s fusion engine
and regularly makes large contributions to
Ray
such as the
Java API
. If you would like to learn more about how we use Ray, check out our talks at the upcoming
Ray Summit
!
