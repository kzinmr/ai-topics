---
title: "Announcing Ray 2.3: performance improvements, new features and new platforms"
url: "https://anyscale.com/blog/announcing-ray-2-3-performance-improvements-new-features-and-new-platforms"
fetched_at: 2026-06-22T07:01:39.335648+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Announcing Ray 2.3: performance improvements, new features and new platforms

Source: https://anyscale.com/blog/announcing-ray-2-3-performance-improvements-new-features-and-new-platforms

The Ray 2.3 release features exciting improvements across the Ray ecosystem. In this blog post, we will highlight new features, performance enhancements, and support for new platforms. In particular we want to highlight six overall additions in this release:
Observability enhancements to the Ray Dashboard
Ray Dataset Streaming (developer preview)
Boost in Ray core scheduling performance
Additions of Gym/Gymnasium library to RLlib
Support for ARM and Python 3.11
Support for multiple applications for Ray Serve (developer preview)
Ray 2.3
main_release_image
For specific details, see the
release notes
on all the various improvements made across the Ray ecosystem. Let’s start with observability improvements.
Link
Observability improvements to the Ray Dashboard
In 2.3, we restructured the Ray dashboard UI layout to improve the information hierarchy and usability. By taking a user-journey driven approach of organizing the dashboard, we organized the dashboard by top level concepts like jobs, cluster (nodes and autoscaler) and logs; provide better navigability so you can quickly click to go to the information you need; and added visualizations and content so that you can double click into details of your application.
Figure 1. Overview of high-level lens into Ray resources and metrics
dashboard_1
Additionally, we added a new
timeline view,
which is a higher level view that lets you optimize or debug errors in your job. As a result, you can quickly see how long tasks are taking to run in your application and how well the workload is distributed across all the workers in your cluster.
Figure 2: Task timeline view
dashboard_2
Figure 3: Granular task time lines
dashboard-3
Finally, we added improvements to the progress bar, which makes it easier to view tasks from a higher level grouping and to determine if errors occurred within the task itself or because a downstream dependency errored.
Figure 4: Additional drilled down into individual activities within a task
dashboard-4
Link
Ray Dataset Streaming (developer preview)
There are two key machine learning (ML) workloads common during any ML pipeline. First is ingesting data, and second is doing batch inference; both demand high throughput and scale.
training data ingest
: where distributed trainer processes (e.g., PyTorch workers), read, preprocess, and ingest data
batch inference
: where a pretrained model across a large dataset generates predictions for each batch
Both workloads are extremely performance sensitive, for they require maximizing GPU utilization.
Prior to 2.3, Ray Dataset users have been generally successful when operating on small to medium datasets (e.g., 1-100GB) that fit in the Ray object store memory. However, users often struggle to use and work with the old Ray's pipelined data API to load and operate efficiently on larger-than-memory datasets. In particular, three operational issues surface immediately:
Data batch size and parallelism are challenging to tune, resulting in poor performance and frustration.
Performance is subpar due to suboptimal or unnecessary data conversions, copy, and materialization to object store.
Certain aspects of its execution model, such as recreating actor pools for each data batch/window, add significant overheads.
In the 2.3 release, we introduce major performance developer preview changes to Datasets to address these above issues:
Introducing a
Datasets streaming execution backend
that improves efficiency and removes the need to carefully tune the configuration of
DatasetPipeline
making
Datasets lazy by default
-- meaning that each operation is not executed immediately, but is added to the execution plan (i.e., lazily). When a user calls a consumption/action API (e.g.,
fully_executed()
,
iter_batches()
,
take()
etc), all operations within the execution plan are executed together
introducing a
dataset Iterator
that replaces
Dataset
and
DatasetPipeline
as the default data iterator interface in Ray AIR* trainers
Below is a code example of how to use the default streaming execution backend.
import
ray
import
time
ray.data.context.DatasetContext.get_current().use_streaming_executor =
True
def
sleep
(
x
):
time.sleep(
0.1
)
return
x
for
_
in
(
ray.data.range_tensor(
5000
, shape=(
80
,
80
,
3
), parallelism=
200
)
.map_batches(sleep, num_cpus=
2
)
.map_batches(sleep, compute=ray.data.ActorPoolStrategy(
2
,
4
))
.map_batches(sleep, num_cpus=
1
)
.iter_batches()
):
pass
This launches a simple 4-stage pipeline. We use different compute args for each stage, which forces them to be run as separate operators instead of getting fused together. You should see a log message indicating streaming execution is being used:
2023-01-2414:59:06,327
INFO streaming_executor.py:57 -- Executing DAG InputDataBuffer[Input]
-> MapOperator[read] -> MapOperator[map_batches]
-> MapOperator[map_batches] -> MapOperator[map_batches]
Currently, the Ray dataset streaming execution backend is in
developer preview
and not yet ready for production, while the other two (lazy execution and dataset iterator) are enabled by default. You can find
the developer guide here
!
Link
Scheduling speed improvement for parallel workloads
Worker startup is one of the primary overheads when running jobs in Ray. It is very common that the first set of runs (e.g., starting a bunch of actors or starting many tasks) is way slower than later runs because of the worker startup overhead.
We have worked on performance enhancements for launch times of actors or tasks to improve this user experience. As the chart below shows, a
8X
improvement.
Figure 5: Worker startup benchmark with 8X improvements
startup_improvements
All these improvements require no API code changes. They are done under the hood, so you can take advantage of these performance improvements.
Link
Gym/Gymnasium migration for RLlib
In releases prior to Ray 2.3, RLlib supported
gym
version 0.23.
However,
gym
was updated to 0.26.x some time ago. The upgrade resulted in breaking API changes that RLlib did not support. Furthermore,
OpenAI has dropped the support for their original gym library
in favor of a new
gymnasium
, which is a drop in replacement maintained by the
Farama Foundation
.
In 2.3, RLlib now supports the new gymnasium and
gym>=0.26.0
APIs to ensure that the library remains up to date with the latest developments in the field of RL.
Options to auto-convert existing
(gym < 0.26.0)
Env subclasses have been added such that a transition from Ray 2.2 to Ray 2.3 should be completely seamless.
For more details about the migration path, please consult the
migration guide
.
Link
Support for ARM and Python 3.11
We are excited to announce support for:
This addresses some of the top questions and requests from the community since mid-2022, bringing Ray support up to date with emerging platforms.
Link
Multi-application support for Ray Serve (developer preview)
In the 2.0 release, the Ray Serve project introduced a new major experimental API centered around
serve.run
, as a way to deploy and run your Serve deployment. However, after the 2.0 release and its subsequent use by users, we heard from them that they need to manage multiple applications on a single cluster and would want to extend the functionality to support it. This includes separate individual models, deployment graphs, and/or FastAPI apps.
To that end, in the 2.3 release, Ray Serve offers experimental support for multiple applications on the same Serve cluster with 2.x API, with the ability to deploy and delete applications separately. Note that this API is experimental, and we would love your feedback.
from
ray
import
serve
import
requests
import
startlette.requests
@serve.deployment
class
Model
:
def
__init__
(
self, model_name
):
# some model loading logic
self.model_name = model_name
async
def
__call__
(
self, req: startlette.requests.Request
):
return
self.model
model1 = Model.bind(
"Model1"
)
serve.run(model1, app=
"app1"
, route_prefix=
"/app1"
)
model2 = Model.bind(
"Model2"
)
serve.run(model2, app=
"app2"
, route_prefix=
"/app2"
)
requests.post(
"http://127.0.0.1:8000/app1"
, json={
"text"
:
"hello"
}
#Model1
requests.post(
"http://127.0.0.1:8000/app2"
, json={
"text"
:
"world"
}
#Model2
Concluding comments
First and foremost, we want to thank all contributors for their valuable contributions to this new release of Ray 2.3. Your enduring support continues to foster the wider use of Ray adoption.
We have a ton of exciting improvements planned in subsequent Ray releases ahead with focus on bolstering stability, improving performance, extending integration with larger Python and ML ecosystem, and offering observability into Ray jobs and clusters, so please let us know if you have any questions or feedback.
Have a go at the latest release with
pip install -U "ray[default]"
and let us know of your feedback. We’re always interested to hear from you – feel free to reach out to us on
Github
or
Discourse
.
Finally, we have our Ray Summit 2023 coming up later in the year. If you have a Ray story or use case to share with the global Ray Community, we are
accepting proposals for speakers
!
*We are sunsetting the "Ray AIR" concept and namespace starting with Ray 2.7. The changes follow the proposal outlined in
this REP
.
