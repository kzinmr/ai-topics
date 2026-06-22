---
title: "Ray 2.6 | Streaming for Serve & Train | Multi-GPU Learner API"
url: "https://anyscale.com/blog/ray-2-6-features-streaming-for-serve-and-train-and-new-multi-gpu-learner-api"
fetched_at: 2026-06-22T07:01:38.476775+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Ray 2.6 | Streaming for Serve & Train | Multi-GPU Learner API

Source: https://anyscale.com/blog/ray-2-6-features-streaming-for-serve-and-train-and-new-multi-gpu-learner-api

The
Ray 2.6 release
features focus on a number of enhancements and improvements across the Ray ecosystem. In this blog, we expound on a few key highlights, including:
Streaming responses in Ray Serve for real-time capabilities
Ray Data streaming integration with Ray Train
Distributed Ray Training and Tuning sync with cloud storage persistence
Public alpha release of the new Multi-GPU Learner API
Let's examine each in detail.
Link
Streaming responses in Ray Serve for real-time capabilities
This release introduces two new features to Ray Serve: streaming responses (including WebSockets) and batch requests. Both enhance and extend Ray Serve’s capabilities for batch inference and online real-time inference for serving, including LLM workloads.
Streaming responses:
Certain applications, like text generation in large language models (LLMs), need to return results incrementally to the user. For example, large neural networks may take multiple seconds for a full forward pass, so providing incremental results enhances the user experience. Ray Serve supports
StreamingResponse
. Using basic HTTP ingress deployments in
FastAPI,
you can return this response from your HTTP request by wrapping a Python generator in your HTTP handler.
For example, this partial code snippet shows how, but check our full
chatbot tutorial example
.
fastapi_app = FastAPI()
@serve.deployment
@serve.ingress(
fastapi_app
)
class
Textbot
:
def
__init__
(
self, model_id:
str
):
self.loop = asyncio.get_running_loop()
self.model_id = model_id
self.model = AutoModelForCausalLM.from_pretrained(self.model_id)
self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
@fastapi_app.post(
"/"
)
def
handle_request
(
self, prompt:
str
) -> StreamingResponse:
logger.info(
f'Got prompt: "
{prompt}
"'
)
streamer = TextIteratorStreamer(
self.tokenizer, timeout=
0
, skip_prompt=
True
skip_special_tokens=
True
)
self.loop.run_in_executor(
None
, self.generate_text,prompt,streamer)
return
StreamingResponse(
self.consume_streamer(streamer), media_type=
"text/plain"
)
def
generate_text
(
self, prompt:
str
, streamer: TextIteratorStreamer
):
input_ids = self.tokenizer([prompt], return_tensors=
"pt"
).input_ids
self.model.generate(input_ids, streamer=streamer, max_length=
10000
)
async
def
consume_streamer
(
self, streamer: TextIteratorStreamer
):
while
True
:
try
:
for
token
in
streamer:
logger.info(
f'Yielding token: "
{token}
"'
)
yield
token
break
except
Empty:
# The streamer raises an Empty exception if the next token
# hasn't been generated yet. `await` here to yield control
# back to the event loop so other coroutines can run.
await
asyncio.sleep(
0.001
)
In the above example, we focused on streaming responses. However,
WebSockets
allow bi-directional input and output streaming in applications. Ray Serve now supports WebSockets for bi-directional streaming with this release. For more details and a complete
WebSocket example tutorial
, please refer to our Serve documentation.
Batch requests:
Batching is a normal pattern for many machine learning operations, including streaming requests, as it provides the receiver a batch of data to process in bulk. When done in parallel, over many Serve replicas, you benefit in the overall performance.
Batching becomes essential when your model is computationally expensive, and you want to utilize all your hardware resources. ML frameworks such as PyTorch and TensorFlow support evaluating multiple samples simultaneously. Ray Serve enables you to employ this capability through dynamic request batching.
You can enable batching by using the
ray.serve.batch
decorator. Let’s take a look at a simple example in the
Model
class to accept a batch. Note that for brevity the code snippets are partial, while the full example is in our
dynamic batch requests documentation
.
import
numpy
as
np
from
typing
import
List
import
ray
from
ray
import
serve
@serve.deployment
class
Model
:
@serve.batch(
max_batch_size=
8
, batch_wait_timeout_s=
0.1
)
async
def
__call__
(
self, multiple_samples:
List
[
int
]
) ->
List
[
int
]:
# Use numpy's vectorized computation to efficiently process a batch.
return
np.array(multiple_samples) *
2
handle = serve.run(Model.bind())
assert
ray.get([handle.remote(i)
for
i
in
range
(
8
)]) == [i *
2
for
i
in
range
(
8
)]
While the above example illustrates batch processing, you can stream batch responses too with
ray.serve.batch
decorator. For example:
import
asyncio
from
typing
import
List
, AsyncGenerator,
Union
from
starlette.requests
import
Request
from
starlette.responses
import
StreamingResponse
from
ray
import
serve
@serve.deployment
class
StreamingResponder
:
@serve.batch(
max_batch_size=
5
, batch_wait_timeout_s=
0.1
)
async
def
generate_numbers
(
self, max_list:
List
[
str
]
) -> AsyncGenerator[
List
[
Union
[
int
, StopIteration]],
None
]:
for
i
in
range
(
max
(max_list)):
next_numbers = []
for
requested_max
in
max_list:
if
requested_max > i:
next_numbers.append(
str
(i))
else
:
next_numbers.append(StopIteration)
yield
next_numbers
await
asyncio.sleep(
0.1
)
async
def
__call__
(
self, request: Request
) -> StreamingResponse:
max
=
int
(request.query_params.get(
"max"
,
"25"
))
gen = self.generate_numbers(
max
)
return
StreamingResponse(gen, status_code=
200
,  media_type=
"text/plain"
)
Link
Ray Data Streaming Integration with Ray Train
Following changes in
2.5
with
Ray Data
becoming lazily executed by default, we are introducing a new streaming integration of Ray Data and Ray Train. This allows streaming data ingestion for model training, reducing the amount of cluster memory needed to perform training on big data. Further, on each epoch, data preprocessing will be rerun, enabling per-epoch preprocessing.
From the user API, preprocessing is now specified in an explicit step outside of the train loop, and the
dataset_config
argument now has a
DataConfig
object that is used to configure the execution of the data processing during training.
Here is an example of using the new API:
import
ray
from
ray.air
import
session
from
ray.air.config
import
ScalingConfig
from
ray.train.torch
import
TorchTrainer
import
numpy
as
np
from
typing
import
Dict
def
train_loop_per_worker
():
# Get an iterator to the dataset we passed in below.
it = session.get_dataset_shard(
"train"
)
# Train for 10 epochs over the data. We'll use a shuffle buffer size
# of 10k elements, and prefetch up to 10 batches of size 128 each.
for
_
in
range
(
10
):
for
batch
in
it.iter_batches(
local_shuffle_buffer_size=
10000
, batch_size=
128
, prefetch_batches=
10
):
print
(
"Do some training on batch"
, batch)
dataset_a = ray.data.read_text(
"s3://anonymous@ray-example-data/sms_spam_collection_subset.txt"
)
dataset_b = ray.data.read_csv(
"s3://anonymous@ray-example-data/dow_jones.csv"
)
my_trainer = TorchTrainer(
train_loop_per_worker,
scaling_config=ScalingConfig(num_workers=
2
),
datasets={
"a"
: dataset_a,
"b"
: dataset_b},
dataset_config=ray.train.DataConfig(
datasets_to_split=[
"a"
],
),
)
The reason for these changes is twofold:
Separate preprocessors from Trainers. That is, users now can
explicitly perform data preprocessing
on the Datasets before passing it into the Trainer.
Simplify the API configuration during training.
You can further refer to this
Ray Enhancement Proposal
, and more details about configuration can be
found in the documentation
.
Link
Distributed Ray Training and Tuning sync with cloud storage persistence
To ensure reliable persistence of Ray training and tuning artifacts, users can now specify a cloud storage or an NFS path in their configuration for distributed training or tuning. Local paths are not supported.
This change allows different worker machines to sync artifacts directly to the cloud storage instead of syncing with the head node, significantly reducing the overall network bandwidth and memory usage. For detailed information, check the PR #
37177
Link
Public Alpha Release of the New Multi-GPU Learner API
In our previous
blog post
, we discussed cost savings by using the newly introduced multi-gpu training stack in RLlib. With this release, we are introducing an alpha release of a new multi-gpu learner API that is less complex and more powerful than what we showed in the blog. By default this API is enabled under PPO algorithm.
import
ray
from
ray
import
air, tune
from
ray.rllib.algorithms.ppo
import
PPOConfig
ray.init()
config = (
PPOConfig()
.framework(args.framework)
.environment(
"CartPole-v1"
)
.resources(num_learner_workers=
2
, num_gpus_per_learner_worker=
1
)
)
tuner = tune.Tuner(
"PPO"
,
param_space=config.to_dict(),
run_config=air.RunConfig(
stop={
"training_iteration"
:
1
},
failure_config=air.FailureConfig(fail_fast=
"raise"
),
),
)
tuner.fit()
Link
Conclusion
With each release of Ray, we strive toward ease of use, performance, and stability. And this release, as previous ones, marched towards that end by:
Extending Ray Serve to incorporate both streaming requests and responses for important workloads such as LLMs. Additionally, support for bi-directional streaming using WebSockets
Enhancing Ray Train to capitalize on Ray Data’s streaming lazily execution for efficient training and optimize use of memory
Increasing reliability for supporting external cloud storage as mechanisms for Ray Train to persist its training and experimental artifacts instead of syncing with the head node, reducing overall network latency
Introducing a simple and efficient multi-GPU Learner API use in PPO algorithm
We want to thank all contributors for their valuable contributions to this new release of
Ray 2.6
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
Finally,
Ray Summit 2023
registration is open. Check our lineup of
keynote speakers
,
full-day of training
, and a
dedicated LLM track
. Secure your spot, save some money, savor the community camaraderie at the summit.
Link
What’s Next?
Stay tuned for additional Ray blogs, meanwhile take a peek at the following material for Ray edification:
