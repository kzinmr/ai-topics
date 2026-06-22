---
title: "Ray 2.7 features major stability improvements to Ray AI Libraries and KubeRay and introduces RayLLM"
url: "https://anyscale.com/blog/ray-2-7-features-major-stability-improvements-to-ray-ai-libraries-and-kuberay-introduces-rayllm"
fetched_at: 2026-06-22T07:01:38.509484+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Ray 2.7 features major stability improvements to Ray AI Libraries and KubeRay and introduces RayLLM

Source: https://anyscale.com/blog/ray-2-7-features-major-stability-improvements-to-ray-ai-libraries-and-kuberay-introduces-rayllm

Ray 2.7
release brings important stability improvements and enhancements to Ray libraries and
KubeRay
for Kubernetes–all for general availability. It also introduces RayLLM for serving open source LLMs with
Ray Serve
.
In this blog, we'll delve into some key features added to the Ray ecosystem, including:
Simplified APIs in Ray Train for general availability
Stabilized and enhanced Ray Serve and KubeRay for general availability
Introduced RayLLM -- LLM model serving on Ray Serve
Stabilized Ray Data for an upcoming general availability
Added initial Accelerator support for TPUs, Trainium, and Inferentia
Link
Simplified APIs in Ray Train for general availability
Ray Train is a library built on Ray for distributed training. In this release, we’re excited to announce general availability for Ray Train.
With this announcement, we are sunsetting the "Ray AIR" concept and namespace to simplify  the number of concepts that users need to learn about. Together, these efforts reduce the friction for new machine learning (ML) practitioners to quickly adopt Ray Train for distributed training at scale.
Our efforts for Ray Train focused on reducing and simplifying the API surface area and expanding support for LLMs.
APIs simplicity --
We made these changes to keep things simple – no more multiple ways to do one thing, and fewer new concepts for users to learn.
We are consolidating various existing trainers for frameworks such as
PyTorch Lightning
and
HuggingFace Transformers
into the TorchTrainer. This reduces the amount of refactoring work that new users need to scale existing training scripts. You can check out the details in the
Ray Train documentation
.
We moved many concepts from the Ray AIR namespace into Ray Train to allow users to stay within usage of fewer modules. You can find all the API changes in the
2.7 Migration guide
.
We adopted a standard approach by relying on common public cloud storage and NFS both for storing and transferring training or data artifacts. This effectively resolves the problems that many of our users faced in the past while dealing with various non-standard storage solutions.
LLM support for fine-tuning --
We’ve implemented new features to better enable users to fine tune and train LLMs easily.
We incorporated
DeepSpeed
and
Accelerate
with
TorchTrainer,
with no code changes. Here is an
example
of how to use both with TorchTrainer.
We support various distributed strategies for large model training such as model parallel, pipeline parallel, and tensor parallel—all now part of TorchTrainer.
We added support for efficient checkpointing of distributed models. It can now save and upload model partitions to cloud storage, reducing memory usage and avoiding OOM errors.
Instacart, Samsara, and other organizations have standardized their deep learning infrastructure on Ray Train.
At Instacart, we offer a diverse range of machine learning products that power every aspect of our marketplace. To support emerging requests, we must scale a large number of workloads on both CPU and GPU instances in a performant and cost-efficient way. We chose Ray as the foundational computational framework for distributed ML. This choice enabled us to run deep learning workloads 12x faster, to reduce costs by 8x, and to train our models on 100x more data.
Link
Stabilized and enhanced Ray Serve and KubeRay for general availability
For this release, the Ray Serve team focused on delivering key features to enhance the Serve functionality for general availability, including:
gRPC ingress support
: Ray Serve now includes a high performant gRPC proxy to serve gRPC requests through Ray Serve. This enables teams to integrate Ray Serve models with other internal systems and achieve significantly lower communication latency than the existing HTTP protocol.
Unified DeploymentHandle API:
This release comes with a new DeploymentHandle API, for unifying existing RayServeHandle and RayServeSyncHandle APIs. The new API simplifies code for model composition, removing a previously non-idiomatic usage of a double “await.”
Support for Websocket with FastAPI:
You can write bi-directional request/response code using websocket with FastAPI simply by installing the websockets package. Here is an illustrative sample:
from
fastapi
import
FastAPI, WebSocket, WebSocketDisconnect
from
ray
import
serve
app = FastAPI()
@serve.deployment
@serve.ingress(
app
)
class
EchoServer
:
@app.websocket(
"/"
)
async
def
echo
(
self, ws: WebSocket
):
await
ws.accept()
try
:
while
True
:
text =
await
ws.receive_text()
await
ws.send_text(text)
except
WebSocketDisconnect:
print
(
"Client disconnected."
)
# deploy it
serve_app = serve.run(EchoServer.bind())
You can query your EchoServer deployment using this sample code:
from
websockets.sync.client
import
connect
with
connect(
"ws://localhost:8000"
)
as
websocket:
websocket.send(
"Eureka!"
)
assert
websocket.recv() ==
"Eureka!"
websocket.send(
"I've found it!"
)
assert
websocket.recv() ==
"I've found it!"
Support for Streaming:
In certain use cases, like text generation in large language models (LLMs) or video processing, we need to send back results or generated tokens incrementally. For example, with LLMs, a complete generated result might take a while, so sharing results incrementally improves the user experience and offers higher throughput. Here is a
tutorial
on how to use streaming responses. Another example in employing streaming response during token generation is this guide:
Building RAG-based LLM Applications for Production
.
Support
batching Serve requests
,
model multiplexing
, and
multi-app support
: For brevity we refer you to examples in the
documentation
of how to write batch requests, use model multiplexing, and a multiplexed deployment.
As part of this release, these Ray Serve feature enhancements fulfill frequently requested features from users developing applications such as LLM chatbots, plugins for their internal services, or serving personalized models.
Together, all the Ray Serve stability efforts and enhancements, along with fixing many
bugs and issues
, afford maturity and reliability as part of its general availability for production.
Samsara
attests to Ray’s merits in general and Ray Serve’s efficacy in particular for their use case:
“We use Ray to run a number of AI workloads at Samsara. Since implementing the platform, we’ve been able to scale the training of our deep learning models to hundreds of millions of inputs and to accelerate deployment while cutting inference costs by 50%. We even use Ray to drive model evaluation on our IoT devices! Ray's performance, resource efficiency, and flexibility made it a great choice for supporting our evolving AI requirements.”
Link
KubeRay general availability
This release is coupled with
KubeRay
’s 1.0 release for general availability.
With this release, we've made major stability upgrades, fixing known problems such as pod failures and high availability issues. Additionally, we've enhanced our documentation on
observability
and running
applications and workloads
on KubeRay, including many
user guides
as examples of best practices. Most of the documentation for KubeRay can now be found on
docs.ray.io
. These improvements provide a solid foundation for organizations to confidently deploy Ray in production on Kubernetes.
Niantic has expressed support for the utility of KubeRay in their Ray deployment:
The KubeRay project has allowed us to achieve these benefits while staying fully integrated into Niantic’s holistic Kubernetes infrastructure. We heavily rely on KubeRay to reliably create, autoscale, and shutdown our production Ray clusters. We are very excited to see KubeRay’s general availability and 1.0 release!
Link
Enhanced Aviary as RayLLM for serving open source LLMs
In an earlier release, we announced Aviary, as a way of evaluating and serving LLMs. While our initial focus was on evaluation, we realized that there was a significant demand for using Aviary to serve LLM models.
In Ray 2.7, we are renaming the
ray-project/aviary
project to RayLLM, with a renewed focus on simplifying the serving of large language models. In particular, we will be providing Ray Serve configurations for popular open source models and simplifying the path to production.
Moving forward, RayLLM will integrate with the most popular open source libraries for LLM model serving, including
vLLM
-- creating a hub for optimized LLM model serving.
Link
Stabilized Ray Data for upcoming general availability
In Ray 2.7, we have improved Ray Data performance with the following critical performance features.
We’ve integrated the Ray Core streaming generator, reducing memory consumption in intermediate stages of the data pipeline and hence improving performance and stability
Zero-copy fusion for map operators, which significantly improves performance for data preprocessing workloads
Multithreaded file reading, which accelerates data loading from storage.
Combining these improvements, we improved the performance of our image batch inference and training data ingestion benchmarks by 3.4x and 6.5x respectively.
To support emerging LLM use cases, we added multiple new features including writing vector databases, JSONL format support, and streaming read from
Hugging Face Dataset
.
Moving forward, Ray Data will improve the memory efficiency for training data ingest and inference, and keep improving reliability for upcoming general availability.
Link
Initial Accelerator support for TPUs, Trainium, and Inferentia
In this release, we’ve integrated support for various accelerator devices at Ray Core: TPUs, Trainium, and Inferentia.
We’ve seen increased demand for different accelerators beyond GPUs over the last year. Now, we’ve worked closely with teams from Google Cloud and AWS to design the best way for users to scale their Ray applications on these devices.
Now, Ray Core will automatically detect these resources instead of requiring custom resources, as follows:
@ray.remote(
resources={
"TPU"
:
4
}
)
def
train
(
config
):
hf = init_hf(
model_name=
"llama2/2B"
,
dataset_name=
"wikitext"
)
return
train_model(
training_args=config[
"training_args"
],
data_args=config[
"data_args"
],
trainer=config[
"trainer"
],
train_dataset=config[
"train_dataset"
])
For TPUs, we’ve also integrated pod support to the TPU cluster launcher. You can find
an example here.
In a future release, we’ll integrate better accelerator support into Ray Serve and Ray Train to enable seamless distributed training and model serving, along with support for more accelerators.
Link
Conclusion
With every new Ray release, we aim for simplicity, better performance, and rock-solid stability. In this release, we took significant steps in that direction to make Ray AI Libraries and KubeRay stable and generally available by:
Simplifying, focusing, and consolidating APIs for Ray Train and reducing the overall cognitive load for Ray users by incorporating Ray AIR concepts into Ray Train for distributed training
Stabilizing Ray Serve by focusing on key features such as support for gRPC, batch requests, websockets, streaming response, multiplexing model support, and brining maturity and reliability for general availability, all to offer both ML developers to serve LLM and other models
Hardening and stabilizing KubeRay for general availability
Adding additional accelerator support in Ray for TPUs, Trainium, and Inferentia
Incorporating Aviary as part of RayLLM, to serve OSS LLMs at scale
Embolding and stabilizing all experimental features in Ray Data for an upcoming general availability
We want to thank all community contributors for their valuable contributions to this new release of
Ray 2.7
. Your enduring support and commitment continues to foster the wider use of Ray adoption.
Have a go at the latest release with pip install “ray[default]” and let us know of your feedback. We’re always delighted to share new Ray releases with you and equally interested to hear your feedback – feel free to reach out to us on
GitHub
or
Discuss
.
Link
What’s next?
In a future release, we will be announcing Ray Data as generally available.
At the
Ray Summit 2023
, in our
Ray Deep Dives track
, we’ll be presenting various aforementioned features in our various Ray related talks. Do join us and
register today!
Be part of our
Ray Community
and the
Ray #LLM slack channel
.
