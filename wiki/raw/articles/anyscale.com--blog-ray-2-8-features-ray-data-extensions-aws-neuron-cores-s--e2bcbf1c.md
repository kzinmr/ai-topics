---
title: "Ray 2.8 features Ray Data extensions, AWS Neuron cores support, and Dashboard improvements"
url: "https://anyscale.com/blog/ray-2-8-features-ray-data-extensions-aws-neuron-cores-support-and-dashboard-improvements"
fetched_at: 2026-06-22T07:01:38.296457+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Ray 2.8 features Ray Data extensions, AWS Neuron cores support, and Dashboard improvements

Source: https://anyscale.com/blog/ray-2-8-features-ray-data-extensions-aws-neuron-cores-support-and-dashboard-improvements

The
Ray 2.8 release
features focus on a number of enhancements and improvements across the Ray ecosystem. In this blog, we expound on a few key highlights, including:
Reading external data sources like BigQuery and Databricks tables
Supplying Ray data metrics on the Ray Dashboard
Adding AWS neuron cores accelerators
Profiling GPU tasks or actors using Nvidia Nsight
Link
Reading external data stores with Ray Data
Ray data now supports reading from
external data stores
like
BigQuery
and
Databricks tables
. To read from BigQuery, simply install the
Python Client for Google BigQuery
and the
Python Client for Google BigQueryStorage
. After installation, you can query it by using functions like
read_bigquery()
and providing the project id, dataset, and query (if needed).
import
ray
# Read the entire dataset (do not specify query)
ds = ray.data.read_bigquery(
project_id=
"my_gcloud_project_id"
,
dataset=
"bigquery-public-data.ml_datasets.iris"
,
)
# Read from a SQL query of the dataset (do not specify dataset)
ds = ray.data.read_bigquery(
project_id=
"my_gcloud_project_id"
,
query =
"SELECT * FROM `bigquery-public-data.ml_datasets.iris` LIMIT 50"
,
)
# Write back to BigQuery
ds.write_bigquery(
project_id=
"my_gcloud_project_id"
,
dataset=
"destination_dataset.destination_table"
,
)
Similarly, you can read Databricks tables simply by calling
ray.data.read_databricks_tables()
to read from the Databricks SQL warehouse.
import
ray
dataset = ray.data.read_databricks_tables(
warehouse_id=
'a885ad08b64951ad'
,
# Databricks SQL warehouse ID
catalog=
'catalog_1'
,
# Unity catalog name
schema=
'db_1'
,
# Schema name
query=
"SELECT title, score FROM movie WHERE year >= 1980"
,
)
These capabilities extend Ray Data to ingest and supplement additional structured data from external data stores for last-mile ingestion for machine learning training.
Link
Supplying Ray Data Metrics on the Ray Dashboard
You can monitor
Ray Data consumption
, including metrics like bytes spilled, consumed, allocated, outputted, freed, as well as CPU and GPU usage, in real-time during operations such as
map(), map_batches(), take_batch(), and read_data()
.
The Ray data metrics below are emitted from
Ray Data examples
run on an Anyscale cluster. For setup instructions, read the
Ray Dashboard
documentation and series of videos.
Supplying Ray Data Metrics
bytes-output-vs-gpu-usage
Link
Adding AWS Neuron Core accelerator (experimental)
Ray supports a range of
GPU accelerators
to improve heterogeneous training and batch processing performance and efficiency. As an experimental feature, Ray can also schedule Tasks and Actors on AWS neuron core accelerators by specifying them as resources in the
@ray.remote(...)
decorator. For example:
import
ray
import
os
from
ray.util.accelerators
import
AWS_NEURON_CORE
# On trn1.2xlarge instance, there will be 2 neuron cores.
ray.init(resources={
"neuron_cores"
:
2
})
@ray.remote(
resources={
"neuron_cores"
:
1
}
)
class
NeuronCoreActor
:
def
info
(
self
):
ids = ray.get_runtime_context().get_resource_ids()
print
(
"neuron_core_ids: {}"
.
format
(ids[
"neuron_cores"
]))
print
(
f"NEURON_RT_VISIBLE_CORES:
{os.environ[
'NEURON_RT_VISIBLE_CORES'
]}
"
)
@ray.remote(
resources={
"neuron_cores"
:
1
}, accelerator_type=AWS_NEURON_CORE
)
def
use_neuron_core_task
():
ids = ray.get_runtime_context().get_resource_ids()
print
(
"neuron_core_ids: {}"
.
format
(ids[
"neuron_cores"
]))
print
(
f"NEURON_RT_VISIBLE_CORES:
{os.environ[
'NEURON_RT_VISIBLE_CORES'
]}
"
)
neuron_core_actor = NeuronCoreActor.remote()
ray.get(neuron_core_actor.info.remote())
ray.get(use_neuron_core_task.remote())
Such an addition immensely extends Ray’s capabilities to support an array of accelerators suited optimally for large language model fine-tuning, inference, and other compute-intensive batch processing.
Link
Profiling GPU tasks or actors with NVIDIA Nsight
Observability is crucial for distributed systems. It provides a means to assess job progress and resource consumption, offering insights into overall health and progress. Profiling GPU bound tasks and actors is one lens through which to view your job’s health and progress.
NVIDIA
Nsight System
is now natively supported on Ray. For brevity, we refer to our Ray GPU
profiling documentation
on how to install, configure, customize,  run it, and display it on the Ray Dashboard.
nsight-profiler-directory
To enable GPU profiling for your Ray Actors, specify the config in the
runtime_env
as follows:
import
torch
import
ray
ray.init()
@ray.remote(
num_gpus=
1
, runtime_env={
"nsight"
:
"default"
}
)
class
RayActor
:
def
run
():
a = torch.tensor([
1.0
,
2.0
,
3.0
]).cuda()
b = torch.tensor([
4.0
,
5.0
,
6.0
]).cuda()
c = a * b
print
(
"Result on GPU:"
, c)
ray_actor = RayActor.remote()
# The Actor or Task process runs with : "nsys profile [default options] ..."
ray.get(ray_actor.run.remote())
Link
Conclusion
With each release of Ray, we strive toward ease of use, performance, and stability. And this release, as previous ones, marched towards that end by:
Extending Ray Data functionality to accessing common data stores such as BigQuery and Databricks Tables. This enables to augment additional structured data for data ingestion to train your models
Augmenting Ray Databoard with additional metrics to examine your Ray Data operations
Adding experimental AWS neuron core accelerators support to bolster training and batch processing, extending your choice of resources available for target scheduling
Profiling GPU usage by Ray Tasks and Actors with NVIDIA Nsight, adding lenses to perceive the health and progress of your Ray jobs
Thank you to all contributors for your valuable contributions in
Ray 2.8
. Try the latest release with "pip install ray[default]" and share your feedback on
Github
or
Discuss
. We appreciate your ongoing support.
Join our
Ray Community
and the
Ray #LLM slack channel
.
Link
What’s Next?
Stay tuned for additional Ray blogs, meanwhile take a peek at the following material for Ray edification:
