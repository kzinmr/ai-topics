---
title: "Announcing Ray 2.4.0: Infrastructure for LLM training, tuning, inference, and serving"
url: "https://anyscale.com/blog/announcing-ray-2-4-0-infrastructure-for-llm-training-tuning-inference-and"
fetched_at: 2026-06-22T07:01:38.582252+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Announcing Ray 2.4.0: Infrastructure for LLM training, tuning, inference, and serving

Source: https://anyscale.com/blog/announcing-ray-2-4-0-infrastructure-for-llm-training-tuning-inference-and

The
Ray 2.4 release
features exciting improvements across the Ray ecosystem. In this blog post, we highlight new features and examples for Generative AI workloads and share four overall additions:
Enhancements to Ray data for ease of use, stability, and observability
Improved Serve observability
Introduce RLlib’s module for custom reinforcement learning
Improved Ray scalability for large clusters
Link
Generative AI model examples and new features using Ray
Over the past few months, we have seen a flurry of innovative activities around
generative AI models
and
large language models (LLMs)
. To continue our steadfast commitment to make Ray a pivotal compute substrate for
generative AI workloads
and address the challenges (as explained in our
blog series
), we have added significant enhancements in this release to ensure that these open source LLM models and workloads are accessible to the open source community and performant with Ray.
Generative AI Workloads:
First, with 2.4 we are releasing a set of new working examples showing how to use Ray with
Stable Diffusion
and LLMs like
GPT-J
. Below we tabulate the workload of each of these models and their respective links. More are underway with respect to Ray’s integration with
LangChain
.
Ray AIR* new trainers:
Second, to further enable additional large model workloads on Ray, we’re also releasing an
AccelerateTrainer
, allowing you to run
HuggingFace Accelerate
and
DeepSpeed
on Ray with minimal code changes. This Trainer integrates with the rest of the Ray ecosystem—including the ability to run distributed
hyperparameter tuning
with each trial dispatched as a distributed training job.
See how
CarperAI/trlx
uses this for RLHF hyperparameter sweeps, and take a peek at the
documentation
too.
from
ray.train.huggingface.accelerate
import
AccelerateTrainer
def
train_func
():
...
trainer = AccelerateTrainer(
train_func,
accelerate_config={}
# you can pass in a config filepath here as well
scaling_config=ScalingConfig(
trainer_resources={
"CPU"
:
0
},
num_workers=
4
,
use_gpu=
True
,
resources_per_worker={
"CPU"
:
2
},
),
)
result = trainer.fit()
# Integration with Ray Tune
tuner = tune.Tuner(
trainer,
param_space={
"lr"
: tune.grid_search([
0.1
,
0.2
,
0.3
]),
)
results = tuner.fit()
You can see the full example for AccelerateTrainer
here
.
Updated LightningTrainer:
Third, in the broader deep learning space, we’re introducing the
LightningTrainer
, allowing you to scale your
PyTorch Lightning
on Ray. As part of our continued effort for seamless integration and ease of use, we have enhanced and replaced our existing
ray_lightning
integration, which was widely adopted, with the latest changes to PyTorch Lighting.
The new
LightningTrainer
provides better compatibility with the other Ray libraries: Ray Tune or Ray Data or Ray Serve directly with Ray connecting APIs.
Check out
the documentation for this component
or take a look
at an example
.
from
pytorch_lightning.loggers.csv_logs
import
CSVLogger
from
pytorch_lightning.callbacks
import
ModelCheckpoint
from
ray.air.config
import
RunConfig, ScalingConfig, CheckpointConfig
from
ray.train.lightning
import
(
LightningTrainer,
LightningConfigBuilder,
LightningCheckpoint,
)
class
MNISTClassifier
:
…
class
MNISTDataModule
:
…
lightning_config = (
LightningConfigBuilder()
.module(MNISTClassifier, lr=
1e-3
, feature_dim=
128
)
.trainer(
max_epochs=
10
,
accelerator=
"cpu"
,
log_every_n_steps=
100
,
logger=CSVLogger(
"logs"
),
)
.fit_params(datamodule=datamodule)
.checkpointing(monitor=
"val_accuracy"
, mode=
"max"
, save_top_k=
3
)
.build()
)
scaling_config = ScalingConfig(
num_workers=
4
, use_gpu=
True
, resources_per_worker={
"CPU"
:
1
,
"GPU"
:
1
}
)
run_config = RunConfig(
name=
"ptl-mnist-example"
,
local_dir=
"/tmp/ray_results"
,
checkpoint_config=CheckpointConfig(
num_to_keep=
3
,
checkpoint_score_attribute=
"val_accuracy"
,
checkpoint_score_order=
"max"
,
),
)
trainer = LightningTrainer(
lightning_config=lightning_config,
scaling_config=scaling_config,
run_config=run_config,
)
result = trainer.fit()
See the full source code
here
.
Link
Enhancements in Ray Data
The enhancements and features in the release cut across a few dimensions: stability, ease of use, and observability.
Data and ease of use:
Data ingestion and preprocessing for machine learning (ML) at scale are central to any end-to-end ML.
To enable ease of use, the default backend execution model for Ray Data is streaming-based under the hood. As such developers need not worry about instructing Ray Data to use the streaming execution backend; it’s the default execution mode. Second, the default streaming backend lends itself well to large scale workloads such as setting up distributed training data streaming and batch inference or preprocessing.
import
ray
from
ray.data
import
ActorPoolStrategy
import
time
def
preprocess_func
(
x
):
# Do some work with the data x
x = ...
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
.map_batches(preprocess_func, compute=ActorPoolStrategy(size=
4
))
.map_batches(preprocess_func, compute=ActorPoolStrategy(size=
3
))
.map_batches(preprocess_func, num_cpus=
1
)
.iter_batches()
):
pass
This launches a simple 4-stage pipeline. We use different compute args for each stage, which forces them to be run as separate operators instead of getting fused together. You should see a log message indicating streaming execution is being used.
While the above example is using dummy tasks, these sort of operator pipelines are a common pattern Ray users desire to scale:
Figure 1. Ray data streaming data with ActorPool
ray_data_distributed_image
Ray data and SQL
: Additionally, we have extended Ray Data’s ability to fetch data from a common
SQL data source
, with
read_sql(...)
, enabling you to connect to a common SQL data store.
import
mysql.connector
import
ray
def
create_connection
():
return
mysql.connector.connect(
user=
"admin"
,
password=...,
host=
"example-mysql-database.c2c2k1yfll7o.us-west-2.rds.amazonaws.com"
,
connection_timeout=
30
,
database=
"example"
,
)
# Get all movies
datastream = ray.data.read_sql(
"SELECT * FROM movie"
, create_connection)
# Get movies after the year 1980
datastream = ray.data.read_sql(
"SELECT title, score FROM movie WHERE year >= 1980"
, create_connection
)
# Get the number of movies per year
datastream = ray.data.read_sql(
"SELECT year, COUNT(*) FROM movie GROUP BY year"
, create_connection
)
Link
Enhancements to Serve observability
In 2.4, we are adding new functionality for observability and monitoring for Ray Serve applications. You can use the Ray dashboard to get a high-level overview of your Ray cluster and Ray Serve application’s states. This includes details such as:
the number of deployment replicas currently running
logs for your Serve controller, deployment replicas, and HTTP proxies
the Ray nodes (i.e., machines) running in your Ray cluster.
You can access the Ray dashboard at port 8265 at your cluster’s URI. For example, if you’re running Ray Serve locally, use
http://localhost:8265
in your browser.
Figure 1. Serve observesability metrics in the Ray Dashboard.
ray_serve_observebility
For more information on the dashboard, read the documentation for the
Serve page
.
Link
RLlib’s new module for custom reinforcement
In RLlib, we are introducing a new
RLModule
abstraction (alpha). RLModule API provides a unified way to define custom reinforcement learning models in RLlib. This API enables you to design and implement your own models to suit specific needs.
To maintain consistency and usability, RLlib offers a standardized approach for defining module objects for both single-agent and multi-agent reinforcement learning environments through the
SingleAgentRLModuleSpec
and
MultiAgentRLModuleSpec
classes. The built-in RLModules in RLlib follow this consistent design pattern, making it easier for you to understand and utilize these modules.
import
gymnasium
as
gym
from
ray.rllib.core.rl_module.rl_module
import
SingleAgentRLModuleSpec
from
ray.rllib.core.testing.torch.bc_module
import
DiscreteBCTorchModule
env = gym.make(
"CartPole-v1"
)
spec = SingleAgentRLModuleSpec(
module_class=DiscreteBCTorchModule,
observation_space=env.observation_space,
action_space=env.action_space,
model_config_dict={
"fcnet_hiddens"
: [
64
]},
)
module = spec.build()
This is an experimental module that serves as a general replacement for ModelV2, and is subject to change. It will eventually match the functionality of the previous stack. If you only use high-level RLlib APIs such as
Algorithm
, you should not experience significant changes, except for a few new parameters to the configuration object. Read more about it in the
documentation
.
Link
Ray Core scaling to 2000 nodes
We’ve also invested time in making sure Ray can support larger scale workloads. With this release, we are announcing official support for Ray clusters to up to 2000 nodes. See
scalability envelope
for more details.
Link
Conclusion
First and foremost, we want to thank all contributors for their valuable contributions to this new release of
Ray 2.4
. Your enduring support continues to foster the wider use of Ray adoption.
This release is a milestone in our efforts to offer Ray as a performant compute infrastructure for LLM training, inference, and serving. We shared a number of examples that speak to these efforts.
Additionally, we enhanced Ray Data, improved Serve observability, introduced a new RLlib customization module, and scaled Ray core to support large workloads, up to 2000 nodes.
Have a go at the latest release with pip install “ray[default]” and let us know of your feedback. We’re always interested to hear from you – feel free to reach out to us on
Github
or
Discuss
.
Link
What’s Next?
Stay tuned for more Generative AI how-to blog series as we continue our efforts to make Ray the platform choice and compute substrate for all your Generative AI workloads.
If you missed our four-part blog series on Generative AI, in which lay out our vision, position, and solution on how Ray addresses the challenges associated with OSS Generative AI workloads, peruse the links below. Much of the above Generative AI examples and features stem from this series.
🔗
How Ray solves common production challenges for generative AI infrastructure
🔗
Training 175B Parameter Language Models at 1000 GPU scale with Alpa and Ray
🔗
Faster stable diffusion fine-tuning with Ray AIR
🔗
How to fine tune and serve LLMs simply, quickly and cost effectively using Ray + DeepSpeed + HuggingFace
🔗
Building an LLM open source search engine in 100 lines using LangChain and Ray
Join our
Ray Community
and the
Ray #LLM slack channel
.
Finally, we have our
Ray Summit 2023
early-bird registration open. Secure your spot, and save some money.
*We are sunsetting the "Ray AIR" concept and namespace starting with Ray 2.7. The changes follow the proposal outlined in
this REP
.
