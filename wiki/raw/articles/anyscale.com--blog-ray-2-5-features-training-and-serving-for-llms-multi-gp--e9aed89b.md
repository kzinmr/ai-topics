---
title: "Training & Serving for LLMs, Multi-GPU Training & More"
url: "https://anyscale.com/blog/ray-2-5-features-training-and-serving-for-llms-multi-gpu-training-in-rllib"
fetched_at: 2026-06-22T07:01:38.528221+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Training & Serving for LLMs, Multi-GPU Training & More

Source: https://anyscale.com/blog/ray-2-5-features-training-and-serving-for-llms-multi-gpu-training-in-rllib

The
Ray 2. 5
release features focus on a number of enhancements and improvements across the Ray ecosystem. In this blog, we expound on a few key features, including:
Support for training LLMs with Ray Train
Ability to serve LLMs with Ray Serve
Multi-GPU learner stack in RLlib for cost efficiency and scalable RL-agent training
Performant and improved approach to batch inference at scale
Link
Improved support for LLMs in Ray Train
This release comes with a couple key features for improving LLM support in
Ray Train
.
Distributed Checkpointing for distributed models:
With the recent influx of LLMs, we’ve noticed that there has been a lack of support across different frameworks for managing large model checkpoints.
One common workaround is to gather the entire model checkpoint onto a single worker, before uploading it to some cloud storage. This introduces two problems (see Figure 1):
An extra step of communication bottleneck by the bandwidth of a single node.
Can lead to out of memory (OOM) issues for sufficiently large models during gathering of model states.
In this release, we’re introducing a new experimental feature for supporting large model checkpoints that resolves these problems.
Figure 1. Single node uploading the full checkpoint after gathering from all workers
ray_2.5_release_fig_1
In model parallel training workloads, different partitions of a model are held by different workers, in contrast to data parallel training workloads, where the same model is replicated across different workers. To support proper checkpointing of distributed models, Ray Train can now be configured to save different partitions of the model held by each worker and upload its respective partitions directly to cloud storage.
Figure 2. Individual worker nodes uploading their respective checkpoints
ray_2.5_figure_2
To use this feature, enable cloud storage, then include
_checkpoint_keep_all_ranks
and
_checkpoint_upload_from_workers
as part of
RunConfig
. This feature will work for the following trainer APIs:
Note
: This feature should only be turned on if your training loop is configured to save the sharded model state per worker. For example, when using
TransformersTrainer
or
AccelerateTrainer
with deepspeed, the
gather_16bit_weights_on_model_save deepspeed configuration
should be set to False. See the example below for a skeleton of what your training script should look like:
def
trainer_init_per_worker
(
train_dataset, eval_dataset=
None
, **config
):
deepspeed = {
...,
"zero_optimization"
: {
# Configure deepspeed to save checkpoint shards.
"gather_16bit_weights_on_model_save"
:
False
,
...
}
}
training_args = TrainingArguments(
...,
deepspeed=deepspeed,
)
trainer = Trainer(..., args=training_args)
return
trainer
trainer = TransformersTrainer(
trainer_init_per_worker=trainer_init_per_worker,
scaling_config=ScalingConfig(num_workers=
4
),
run_config=RunConfig(
# Requirement: Use cloud storage
# Your checkpoints will be found within "s3://your-s3-bucket/example"
storage_path=
"s3://your-s3-bucket"
,
name=
"example"
,
checkpoint_config=CheckpointConfig(
_checkpoint_keep_all_ranks=
True
,
_checkpoint_upload_from_workers=
True
,
),
)
datasets=...
For other supported trainers, we plan to write full-fledged examples showing their distributed checkpoint configuration in the documentation shortly.
LightningTrainer FSDP support:
In
Ray 2.4,
we released alpha support for the LightningTrainer. After user feedback, we’ve introduced support for
FSDP
in
LightningTrainer
, and an example can be found
here
.
HuggingFace Trainer renaming:
In this release, for naming consistency and logical modularity, we are also renaming the
HuggingFaceTrainer
to
TransformersTrainer
, and we are also moving the
AccelerateTrainer
into the
HuggingFace
package, so that we can have a more intuitive organization of these integrations. For example,
from
ray.train.huggingface
import
AccelerateTrainer, TransformersTrainer
Link
Ray Serve for serving LLMs
We have added two experimental features that augment the use of Ray Serve for online batch inference for streaming responses and model multiplexing for load balancing and serving multiple models across multiple replicas.
Streaming Response
: Some applications, in particular text generation in large language models (LLMs) or video processing, require return of incremental results to the caller. For instance, in the case of LLMs or large neural networks, a full forward pass could take multiple seconds, so providing incremental results offers a better user experience.
You can achieve returning a
StreamingResponse
from your HTTP request by wrapping a Python generator in your HTTP handler. Supported in basic HTTP ingress deployments in
FastAPI
, the code snippet below shows how to.
import
time
from
typing
import
Generator
import
requests
from
starlette.responses
import
StreamingResponse
from
starlette.requests
import
Request
from
ray
import
serve
@serve.deployment
class
StreamingResponder
:
def
generate_numbers
(
self,
max
:
int
) -> Generator[
str
,
None
,
None
]:
for
i
in
range
(
max
):
yield
str
(i)
time.sleep(
0.1
)
def
__call__
(
self, request: Request
) -> StreamingResponse:
max
= request.query_params.get(
"max"
,
"25"
)
gen = self.generate_numbers(
int
(
max
))
return
StreamingResponse(gen, status_code=
200
, media_type=
"text/plain"
)
serve.run(StreamingResponder.bind())
r = requests.get(
"http://localhost:8000?max=10"
, stream=
True
)
start = time.time()
r.raise_for_status()
for
chunk
in
r.iter_content(chunk_size=
None
, decode_unicode=
True
):
print
(
f"Got result
{
round
(time.time()-start,
1
)}
s after start: '
{chunk}
'"
)
This short snippet yields the following streaming response:
…
Got result 0.0s after start: '0'
Got result 0.1s after start: '1'
Got result 0.2s after start: '2'
Got result 0.3s after start: '3'
Got result 0.4s after start: '4'
Got result 0.5s after start: '5'
Got result 0.6s after start: '6'
Got result 0.7s after start: '7'
Got result 0.8s after start: '8'
Got result 0.9s after start: '9'
(ServeReplica:default_StreamingResponder pid=41052) INFO 2023-05-25 10:49:52,230 default_StreamingResponder default_StreamingResponder#qlZFCa yomKnJifNJ / default replica.py:634 - __CALL__ OK 1017.6ms
Model Multiplexing:
A common use case we observe among ML practitioners is deploying multiple models that have dissimilar model shapes. For example, a different network architecture is trained for a particular SKU, user_id, or geo-location but takes similar inputs and produces a respective output. The multiple models are deployed across a pool of replicas among which requests are load balanced. When a request arrives, depending on the request header that contains model id such as SKU, user_id, or zip_code, the request is routed to the right and respective model replica.
For brevity we refer you to an example in the
documentation
of how to write a multiplexed deployment for the above mentioned use case.
Link
Multi-GPU stack for cost efficient, scalable, Multi-GPU RL agents training
The training of reinforcement learning (RL) agents is hindered by the sampling process, which acts as the main bottleneck. While sampling can be distributed across multiple compute nodes as RolloutWorkers and simulators, the training phase is restricted to a single node. Consequently, the number of GPUs available for training is limited to a single GPU. This again creates another bottleneck on the batch size that can be effectively trained due to the memory constraints of a single GPU.
Figure 3. Challenges and solutions for RLlib data collection and training
ray_2.5_release_figure_3
In RLlib we introduce a multi-node, multi-gpu training stack that addresses both the challenges  and bottlenecks shown in Figure 3. With this new stack we can combine different types of GPUs to reduce costs by
1.7x.
In this this
RLlib blog
, we detail implementation and experimentation showing RLlib's Proximal Policy Optimization (PPO) implementation on the
ALE/Breakout-V5
environment on the new multi GPU training stack, using an increasing number of GPUs and larger batch sizes.
Link
Performant and improved batch inference
One common and imperative workload that requires efficiency and optimized usage of hardware accelerators–both CPUs and GPUs–is batch inference. In the 2.4 Ray release, we introduced
Ray Data streaming execution
mode, which allows saturation of CPUs and GPUs for workloads such as offline
batch inference
.
Further improving Ray Data in this release, Ray Data provides additional enhancements. For instance, a
strict mode
is enabled by default. This means that schemas are required for all Datasets, and standalone Python objects are no longer supported. Together with benefits from simplification, this also aligns the Ray Data API closer to industry-standard distributed data APIs like Apache Spark and emerging standards for machine learning datasets like HuggingFace.
Also, the default batch format is fixed to
NumPy
, giving better performance for
batch inference
, along with the support of concurrent actors for
ActorPool
helps too.
from
typing
import
Dict
import
numpy
as
np
import
ray
# Step 1: Create a Ray Dataset from in-memory Numpy arrays.
# You can also create a Ray Dataset from many other sources and file
# formats.
ds = ray.data.from_numpy(np.asarray([
"Complete this"
,
"for me"
]))
# Step 2: Define a Predictor class for inference.
# Use a class to initialize the model just once in `__init__`
# and re-use it for inference across multiple batches.
class
HuggingFacePredictor
:
def
__init__
(
self
):
from
transformers
import
pipeline
# Initialize a pre-trained GPT2 Huggingface pipeline.
self.model = pipeline(
"text-generation"
, model=
"gpt2"
)
# Logic for inference on 1 batch of data.
def
__call__
(
self, batch:
Dict
[
str
, np.ndarray]
) ->
Dict
[
str
,
list
]:
# Get the predictions from the input batch.
predictions = self.model(
list
(batch[
"data"
]), max_length=
20
, num_return_sequences=
1
)
# `predictions` is a list of length-one lists. For example:
# [[{'generated_text': 'output_1'}], ..., [{'generated_text': 'output_2'}]]
# Modify the output to get it into the following format instead:
# ['output_1', 'output_2']
batch[
"output"
] = [sequences[
0
][
"generated_text"
]
for
sequences
in
predictions]
return
batch
# Use 2 parallel actors for inference. Each actor predicts on a
# different partition of data.
scale = ray.data.ActorPoolStrategy(size=
2
)
# Step 3: Map the Predictor over the Dataset to get predictions.
predictions = ds.map_batches(HuggingFacePredictor, compute=scale)
# Step 4: Show one prediction output.
predictions.show(limit=
1
)
Link
Conclusion
With each release of Ray, we strive toward ease of use, performance, and stability. This release marched towards that end by:
extending Ray Train functionality to support distributed checkpointing for large language models
enhancing user experience in Ray Serve by returning HTTP streaming response to HTTP input requests
extending Ray Serve functionality for multi-model serving by multiplexing among replicas of dissimilar shaped model architectures but similar input data types
solving bottlenecks and challenges in RLlib agent training by introducing a new multi-gpu, multi-node training stack for RLlib
improving easy use of Ray Data for batch inference
We want to thank all contributors for their valuable contributions to this new release of
Ray 2.5
. Your enduring support continues to foster the wider use of Ray adoption.
Have a go at the latest release with pip install “ray[default]” and let us know of your feedback. We’re always delighted to share new Ray releases with you and equally interested to hear your feedback – feel free to reach out to us on
Github
or
Discuss
.
Join our
Ray Community
and the
Ray #LLM slack channel
.
Finally, we have our
Ray Summit 2023
early-bird registration open until 6/30. Secure your spot, save some money, savor the community camaraderie at the summit.
Link
What’s Next?
Stay tuned for additional Ray 2.5 related blogs on RLlib, meanwhile take a peek at the following blogs:
