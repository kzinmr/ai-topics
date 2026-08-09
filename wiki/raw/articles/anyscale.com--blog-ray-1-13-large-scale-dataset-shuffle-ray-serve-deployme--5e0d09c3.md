---
title: "Ray 1.13: Improving support for shuffling terabyte-scale and larger datasets"
url: "https://anyscale.com/blog/ray-1-13-large-scale-dataset-shuffle-ray-serve-deployment-graph-api-kuberay"
fetched_at: 2026-08-09T10:13:07.066172+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Ray 1.13: Improving support for shuffling terabyte-scale and larger datasets

Source: https://anyscale.com/blog/ray-1-13-large-scale-dataset-shuffle-ray-serve-deployment-graph-api-kuberay

Ray 1.13 is here! The highlights in this release include:
Scalable shuffle in Ray Datasets
(now in alpha), improving support for shuffling terabyte-scale and larger datasets
Performance fixes and other enhancements
to the Ray Serve Deployment Graph API
Enhancements to KubeRay
, including improved ​​stability of autoscaling support (alpha)
Usage stats data collection
, now on by default (guarded by an opt-out prompt), helping the open source Ray engineering team better understand how to improve our libraries and core APIs
You can run pip
install -U ray
to access these features and more. With that, let’s dive in.
Link
Improved support for shuffling terabyte-scale and larger datasets with Ray Datasets
Large-scale (terabyte-scale datasets or larger and/or 1,000+ partitions) Ray Datasets users who are using
random_shuffle
for ML ingest or sort: this one’s for you. We’ve improved support for shuffling terabyte-scale and larger datasets (now in alpha). The affected API calls are
Dataset.random_shuffle
and
Dataset.sort
. In addition to stability improvements in Ray Core, we’ve also introduced a new shuffle algorithm in the Datasets library for scaling to larger clusters and datasets.
Check out the documentation
for more information.
Fun fact
: This feature was inspired by an
academic paper
co-authored by the Anyscale team — and the team will be giving a
talk on this topic at Ray Summit
as well.
Read the release notes
for more on Ray Datasets improvements now available in 1.13.
Note
:
Ray AI Runtime (AIR)
is currently in alpha. Prior to the Ray AIR beta release, we plan to improve the documentation and scope of the Ray Datasets integrations with Ray AIR.
Link
Deployment Graph API enhancements
Ray 1.13 introduces performance fixes and other enhancements to the
Ray Serve Deployment Graph API
, which provides a Python-native API to create a complex inference graph of multiple models to complete an inference or prediction, such as chaining, ensembling, and dynamic control flow.
The API is also now nearly ready for beta — but we want your feedback! If you have suggestions on how the Deployment Graph API can work better for your use case, head over to our
user forums
or file an issue or feature request on
GitHub
, or
get in touch with us via this form
. We can’t wait to partner with you to adopt Ray Serve in your project!
For more on creating inference graphs with Ray Serve,
check out our recent Ray Meetup
or
read the full end-to-end walkthrough in the documentation
.
Link
Improved autoscaling support in KubeRay
KubeRay
is a toolkit for running Ray applications on Kubernetes. Since the
Ray 1.12.0 release
, we’ve improved the stability of autoscaling support (currently in alpha). We’ve also introduced CI tests guaranteeing functionality of autoscaling, Ray Client, and Ray Job Submission when deploying using the KubeRay operator.
Link
Usage stats collection
Starting in Ray 1.13, Ray collects usage stats data by default (guarded by an opt-out prompt). This data will be used by the open-source Ray engineering team to better understand how to improve our libraries and core APIs, and how to prioritize bug fixes and enhancements.
Here are the guiding principles of our collection policy:
No surprises
: You will be notified before we begin collecting data. You will be notified of any changes to the data being collected or how it is used.
Easy opt-out
: You will be able to easily opt out of data collection
Transparency
: You will be able to review all data that is sent to us.
Control
: You will have control over your data, and we will honor requests to delete your data.
We will
not
collect any personally identifiable data or proprietary code/data.
We will
not
sell data or buy data about you.
For more details, check the
official documentation
or
RFC
.
Link
Other highlights
Python 3.10 support is now in alpha.
Ray Tune can now synchronize Trial data from worker nodes via the object store (without rsync!).
Ray Workflow comes with a new API and is integrated with Ray DAG.
Link
Learn more
Many thanks to all those who contributed to this release. To learn about all the features and enhancements in this release,
check out the Ray 1.13.0 release notes
. If you would like to keep up to date with all things Ray, follow
@raydistributed
on Twitter and
sign up for the Ray newsletter
.
