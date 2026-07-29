---
title: "Fast, Flexible and Scalable Data Loading for ML Training"
url: "https://anyscale.com/blog/fast-flexible-scalable-data-loading-for-ml-training-with-ray-data"
fetched_at: 2026-07-29T10:11:53.297990+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Fast, Flexible and Scalable Data Loading for ML Training

Source: https://anyscale.com/blog/fast-flexible-scalable-data-loading-for-ml-training-with-ray-data

While scaling model training across multiple GPUs is a well-known challenge, data loading and CPU-based preprocessing can also easily become the performance bottleneck in actual ML pipelines, leading to low GPU utilization and high costs. Data preprocessing requirements are also becoming more complicated as the types of data being processed are becoming more diverse.
Ray Data
provides a flexible data loader for ML training that uses Ray core for parallel and distributed preprocessing on heterogeneous compute. It provides a
streaming dataset
abstraction
that allows you to maximize GPU utilization (left) while keeping RAM usage (right) under control.
streaming dataset abstraction chart
GPU utilization (left) and RAM usage (right) during a distributed training job (starting at 12:30) for an image classification model, with Ray Data and 16 1-GPU nodes. Ray Data supports streaming execution for high GPU utilization, while keeping memory usage constant.
In this blog post, we’ll dive into the performance of different OSS data loader solutions, using the public
MLPerf
image classification benchmark as an example. We’ll show how Ray Data provides unmatched flexibility and scale
in multi-node settings, with support for
streaming from cloud storage
,
heterogeneous clusters,
and
in-memory distributed caching
, while also matching popular data loaders such as PyTorch DataLoader and tf.data in performance on a single node.
In particular, we’ll cover some benchmarks that measure:
Using Ray Data to stream large datasets from cloud storage to a distributed training cluster.
Additional scale-out and performance gains with Ray Data, using heterogeneous clusters and dataset caching.
Single-node performance, with a breakdown of performance compared to other open-source data loaders.
Link
A primer on ML data loading with Ray Data
Ray Data
provides last-mile data preprocessing to move data from storage or an ETL pipeline into distributed training or batch inference jobs. It supports:
Working with popular data formats and modalities, from parquet to raw images and video
Streaming from datasets stored on local disk or the cloud
Scale-out to multiple CPUs and multiple nodes
And advanced scaling features like:
Distributed in-memory and on-disk caching
Scale-out with CPU-only nodes, alongside your GPU nodes
Automatic recovery from out-of-memory failures in your data preprocessing pipeline
featured image ml training with ray data
While other OSS data loaders provide some level of support for the first three features, where Ray Data shines is in its
flexibility to build complex data preprocessing pipelines
, and in its ability to
provide performance at scale
. Here’s a closer look at some of the differences:
tf.data
Torch DataLoader
MosaicML StreamingDataset
HuggingFace Datasets
Ray Data
Implementation
Python frontend + C++ multithreading
Python `multiprocessing`
Python `multiprocessing` (based on Torch DataLoader)
Python `multiprocessing`
Python frontend +
Ray core
(C++) for distributed multiprocessing and shared memory
Data format flexibility
✅ - read from open data formats, in-memory format based on TFRecords
✅ - build-your-own datasets, in-memory format based on torch.Tensors
✅ - adds a specialized data format similar to Parquet for faster reads
✅✅ - uses
Arrow
for zero-copy shared-memory reads, support for both TensorFlow and PyTorch models
✅✅ - read
and write
to open data formats, uses
Arrow
for zero-copy shared-memory reads, support for both
TensorFlow and PyTorch
models
Native cloud storage support
❌
❌
✅
✅
✅
Auto-partitioning across (distributed) trainers
✅✅ - automatically assign indices beforehand or on-the-fly
❌ - manually assign indices per worker
✅ - automatically assign indices beforehand
✅ - automatically assign indices beforehand
✅✅ - automatically assign indices beforehand or on-the-fly
Multicore parallelism
✅✅ - dynamically load-balances work across threads, backpressure scheduling to
avoid out-of-memory
✅
✅
✅
✅✅ - dynamically load-balances work across threads, backpressure scheduling to
avoid out-of-memory
Heterogeneous clusters
❌
❌
❌
❌
✅
Recovery from transient errors
❌
❌
❌
❌
✅ -
automatically recovers
from
out-of-memory failures
and (coming soon) spot instance preemption
Dataset caching
✅✅ -
distributed
caching, both
on-disk and in-memory
, of data at
any stage
❌
🆗 - Automatically caches input data from the cloud on local disk. Configuration required.
🆗 - Automatically caches input data from the cloud on local disk. Configuration required.
✅✅ -
distributed
caching, both
on-disk and in-memory
, of data at
any stage
Mid-epoch resumption
✅
❌
✅
❌
❌ - coming soon!
We’ll be comparing these data loaders in more detail next. For the rest of this blog, we’ll be using the
MLPerf
image classification benchmark. This benchmark measures the time to train a ResNet v1.5 model on the
ImageNet-1k dataset
. The raw dataset contains JPEG images that are on average 100KB each, with 150GB total. When decoded, the dataset consumes about ~1TB RAM.
Each image from the original dataset is randomly cropped, flipped, resized, then converted to a tensor. Multiple of these tensors can then be concatenated into a single batch, to be transferred to GPU memory.
The randomized preprocessing steps are used to augment the original dataset. This also means that we need to reapply all of the steps on each pass over the dataset. Also, because the full ImageNet dataset is larger than memory, we will need to reread and decode the images on each epoch.
You can find the public reference implementation of the benchmark
here
, using TensorFlow for training and tf.data for data loading. Here’s the Ray Data code we’ll be using, first defining the preprocessing functions using `torchvision` transforms.
import
os
import
numpy
as
np
import
torch
import
torchvision
import
ray
from
ray
import
train
from
ray.train
import
DataConfig, ScalingConfig
from
ray.train.torch
import
TorchTrainer
# Constants and utility methods for image-based benchmarks.
DEFAULT_IMAGE_SIZE =
224
transform = torchvision.transforms.Compose(
[
torchvision.transforms.RandomResizedCrop(
antialias=
True
,
size=DEFAULT_IMAGE_SIZE,
scale=(
0.05
,
1.0
),
ratio=(
0.75
,
1.33
),
),
torchvision.transforms.RandomHorizontalFlip(),
]
)
def
crop_and_flip_image
(
row
):
# Make sure to use torch.tensor here to avoid a copy from numpy.
row[
"image"
] = transform(torch.tensor(np.transpose(row[
"image"
], axes=(
2
,
0
,
1
))))
return
row
And then we use Ray Train to define and run a distributed training job:
def
train_loop_per_worker
(
config
):
it = train.get_dataset_shard(
"train"
)
for
i
in
range
(config[
"num_epochs"
]):
for
batch
in
it.iter_torch_batches(batch_size=config[
"batch_size"
]):
# Training loop.
pass
session.report({
"epoch"
: i})
def
run
(
data_root, num_epochs, batch_size, num_train_workers, use_gpu
):
ray_dataset = ray.data.read_images(
data_root,
mode=
"RGB"
,
).
map
(crop_and_flip_image)
torch_trainer = TorchTrainer(
train_loop_per_worker,
train_loop_config={
"num_epochs"
: num_epochs,
"batch_size"
: batch_size,
},
datasets={
# If num_train_workers > 1, Ray Data dynamically
# splits this dataset among the trainers.
"train"
: ray_dataset,
},
scaling_config=ScalingConfig(
num_workers=num_train_workers,
use_gpu=use_gpu,
),
dataset_config=ray.train.DataConfig(),
)
result = torch_trainer.fit()
print
(result.metrics)
In this case, we’ll just run an empty loop for training so that we just measure the time of data preprocessing (including time needed to transfer to the GPU). Under the hood, Ray Train+Data will automatically split the preprocessed dataset among the training workers.
Link
Streaming image datasets from the cloud to a training cluster
Large training datasets are generally stored in the cloud, where they can be conveniently accessed from training clusters. Cloud storage is also slower than local disk. While downloading the entire training dataset to local disk can help to maximize preprocessing throughput, there are also many cases where this may not make sense:
If you don’t have enough disk space on each node to store the entire dataset
If you want to overlap downloading the data with data preprocessing and training
If you want each worker node to read a different and random subset of the data on each epoch
streaming image datasets 4GPUs
Streaming and preprocessing a large dataset from cloud storage to a cluster of 4 GPUs.
Ray Data has several useful built-in features for working with cloud datasets in these cases, including:
Streaming from popular cloud storage systems from Amazon, GCP, and Azure to cluster memory (and vice versa). Cloud storage support is provided via `
fsspec
`.
Ability to read and preprocess a subset of a cloud dataset.
Ability to statically or dynamically auto-partition a dataset among a cluster of GPU trainers.
Caching of any stage of the data preprocessing pipeline. Ray also manages the cache for you, swapping data from memory to disk and between nodes as needed.
Before we get into these advanced features, let’s take a look at S3 performance and scalability. This graph shows the total throughput when streaming data from S3 to a cluster of GPU nodes, with one GPU and training worker each[1]. Each training worker runs an empty loop (no model) over the preprocessed dataset, so that we can measure the data loading throughput alone. We’re using PyTorch DataLoader as a comparison here because we found that it performed the best on the single-node benchmarks when reading from local disk.
ray data vs torch dataloader
Here, we can see that Ray Data (blue) scales linearly with the number of training nodes, matching the performance of PyTorch DataLoader (red). Most of the performance here relies on concurrent S3 reads.
For PyTorch DataLoader, this requires some manual tuning. PyTorch offers an
S3FileLoader
that iterates over a list of S3 URLs and yields the data as bytes. Since the iterator is single-threaded, we need to increase the `num_workers` parameter passed to the DataLoader, which controls how many `multiprocessing` workers to use. Setting it too high, however, can slow things down and even cause the job to fail from out-of-memory errors. In this case, we found that setting num_workers to 16x the number of cores worked best, but this number will depend on what preprocessing steps and model you want to use.
This also gets more complicated when you’re doing distributed data-parallel training, and each GPU trainer should read a partition of the dataset. With PyTorch DataLoader, each GPU trainer gets its own data loader, so you’ll need to statically partition the list of image files among the GPU trainers, and then among the data loader workers for each trainer. If you want to make sure to read every image of the dataset in each epoch, you’ll need to make sure that the batch size used during training divides evenly into each data partition size.
With Ray Data, all of this is done automatically. The same code is used, no matter how many cores are available or how many trainers there are.
ray data core arch 2 node GPU cluster
Ray Data+Core architecture in a 2-node GPU cluster. Each Ray task reads a subset of files from the dataset, applies the preprocessing function, and then stores the results in Ray’s shared memory object store. The results can then be fed into a local GPU, remote GPU, preprocessed further, and/or cached for future epochs.
This works because Ray Data leverages Ray Core’s generic distributed execution. Under the hood, Ray Data breaks up the list of files into smaller tasks and submits them to Ray Core for scheduling in the cluster. Each task downloads the files from S3 into memory, applies the preprocessing function, and then outputs the results into Ray’s per-node shared-memory object store, where they can be copied to the nearest GPU’s memory in the background.
Link
Scaling data preprocessing with heterogeneous clusters
If your data preprocessing is CPU- or I/O-bound, ideally you’d want to scale your preprocessing independent of your GPU cluster size. We can do this with
heterogeneous clusters
, or clusters made up of different instance types, in this case GPU+CPU and CPU-only. As long as the GPU nodes have available network bandwidth, we can load data on the CPU-only nodes and transfer the preprocessed data to a GPU node for training.
Unfortunately, this is not possible in existing open-source data loaders because the data preprocessing threads need to be colocated with the data consumer.
ray data core heterogeneous GPU cluster
With Ray Data, however, we can run the
same code
on a heterogeneous cluster and increase the number of cores, memory, and disk that we have available for data preprocessing. This works because Ray Core can schedule tasks in a cluster, unlike other data loaders that are single-node only. Once the data on the CPU-only node is ready, Ray Data+Core transfers it to a GPU node in the background.
torch dataloader ray data and heterogeneous cluster
Here, the blue bar on the far right represents a heterogeneous setup, where we double the number of CPUs in the 16-node cluster by adding 4 additional r5.16xlarge nodes. In return, we can increase the throughput by 65% compared to the homogeneous setup.
Link
Speeding up data preprocessing with dataset caching
Depending on your workload and resources available, it can also help to cache the dataset at different stages of preprocessing. This can avoid the network and CPU overheads needed to download and preprocess the dataset.
dataset preprocessing dataset caching
With Ray Data, this is
as easy as adding the line `ds = ds.materialize()`
to the dataset that you want to cache. Under the hood, the results of the dataset are cached in the Ray object store. If the Ray object store reaches its memory limit, Ray Core also automatically spills the data to disk to avoid running out of memory.
Here are the results comparing a couple different caching schemes in both homogeneous and heterogeneous clusters:
different caching schemes
In this particular workload, caching the raw images (purple) does not improve throughput. This is because caching the images in this case only saves doing the S3 read, but we still have to apply the random preprocessing on each epoch. Also, we are caching the decoded images here. These are larger than Ray’s default object store memory, causing some spilling. In practice, caching the inputs to the dataset will work better if the inputs are much smaller than the final preprocessed output. In the future, Ray Data can also improve upon this by caching the encoded images in memory.
Caching does much better if applied to the preprocessed images, because then the GPU trainers can read directly from the cached output. However, it does mean that the data read will be the same on each epoch.
Link
Comparing Ray Data on a single node
Finally, let’s take a deeper look at Ray Data’s performance compared to other open-source data loaders, when loading image data on a single node and from local disk. We’ll find that overall, although Ray Data has some overheads for image processing compared to other popular data loaders, its flexibility and scalability can more than make up for it.
Here, we compare throughput per core against tf.data and PyTorch DataLoader, using two versions of the benchmark: one that just resizes each image to the same size and the previous version that also applied a random crop and flip. The tf.data version converts to tf.Tensors, while PyTorch and ray.data convert to torch.Tensors.
compare open source data loader
At first glance, there are two trends that stick out:
tf.data is fastest at loading images alone. This is probably because tf.data has a more optimized routine for loading images to tf.Tensor format, while the others use the popular
PIL
library. However, this performance edge will be limited to TensorFlow models.
Ray Data is within ~30% of PyTorch DataLoader’s throughput. This performance gap comes from Ray Data doing extra data conversions compared to PyTorch DataLoader. These are an unintentional side effect of Ray Data’s greater flexibility, but of course we want to avoid them if we can! Keep an eye out for more improvements in this area.
A common way to improve data loading performance is to rearrange our input data. Here, we can rearrange the inputs so that each file stores an array of multiple decoded images, instead of one raw image per file. This helps in two ways, at the cost of extra (~5x) storage:
Avoid overhead from decoding images on each epoch.
Reduce I/O overhead, by reading more bytes at a time.
In fact, we can even use Ray Data to scale out this offline preprocessing step to multiple cores and nodes! Here’s a quick look at how this is done using the parquet format.
def
to_bytes
(
row
):
row[
"height"
] = row[
"image"
].shape[
0
]
row[
"width"
] = row[
"image"
].shape[
1
]
row[
"image"
] = row[
"image"
].tobytes()
return
row
# Offline: Write out batches of images in parquet format.
ds = ray.data.read_images(input_dir, mode=
"RGB"
)
ds = ds.
map
(to_bytes)
ds.write_parquet(output_dir)
def
decode_image
(
row
):
row[
"image"
] = Image.frombytes(
"RGB"
, (row[
"height"
], row[
"width"
]), row[
"image"
])
return
{
"image"
: np.array(row[
"image"
])}
# Online: Read the image data back in during training.
ds = ray.data.read_parquet(output_dir).
map
(decode_image)
Two useful comparison points here are
HuggingFace Dataset
, which supports reading from
Parquet
and MosaicML’s
StreamingDataset
, which uses a specialized
MDS
(Mosaic Data Shard) format. You can think of MDS as an array of records, with an index file for fast random lookup. Both of these Datasets use PyTorch DataLoader for parallelization[2], but add additional utilities for reading, shuffling, and caching datasets from cloud storage. Let’s take a look at performance on these different file formats.
loading raw images vs decoded image arrays
Here, Ray Data gets within 15-25% of the throughput of MosaicML’s StreamingDataset and a Parquet HuggingFace Dataset. Similar to before, this performance gap is due to extra data conversions. Eliminating these and optimizing other single-threaded operations will be an active area of improvement for coming versions of Ray Data. For example, initial investigation shows that we can get speedups of up to 30% by using an
optimized PIL
fork.
You can run these single-node benchmarks for yourself using
this code
. For the multi-node benchmarks, which use
Ray Data+Train
, use
this code
.
Link
Summary
In this blog post, we showed how
Ray Data
outperforms other popular data loaders at scale by leveraging streaming datasets, heterogeneous compute, and more flexible caching schemes. While there is still room for improvement in raw performance, Ray Data provides critical performance features needed for scaling data loading and preprocessing with your ML training job, with much less tuning required than typical `multiprocessing`-based data loaders.
Overall, these results also tend to match what some of our users have found. For example, this
recent blog
from Pinterest showcases how the gap between Ray Data and PyTorch DataLoader grew as the preprocessing became more complex. For their most complex preprocessing tasks, Ray Data was up to 45% faster than PyTorch DataLoader. Combined with the ability to scale with heterogeneous resources, they ultimately saved about 25% on their total training cost!
Link
What’s next?
Ray Data
is under active development. In the near future, we plan to release additional features not covered here including:
Further performance improvements for single-threaded performance, including eliminating unnecessary serialization and optimizing image operations
Automatic recovery for transient errors like out-of-memory failures and spot instance preemption
Mid-epoch resumption to recover from training failures on very large datasets
Ray Data can also be used for batch inference! Check out this
blog post
and
user guide
on scaling inference with Ray Data for more information.
Please feel free to try the project out and reach out on
GitHub
with any feedback. For data preprocessing for distributed training, this
user guide
for working with
Ray Data
and
Ray Train
together is a great place to start.
Finally, we’ll be at
Ray Summit 2023
! Attend
our talk
or stop by our Anyscale booth.
References:
[1] We also tried this with MosaicML’s StreamingDataset, but found that throughput dropped to just a few images/s when caching was disabled. Scaling to large datasets (1TB scale) also caused throughput to drop to 10s of images/s. We believe these are likely due to bugs in the current version, so we are omitting those results here for a fairer comparison.
[2] HuggingFace Dataset also supports
parallel dataset loading
with `multiprocessing`, but we found that getting the best performance also required using multiple PyTorch DataLoader workers.
