---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/Turning-Production-Logs-into-Evaluation-Datasets"
scraped: "2026-05-10T01:27:49.598171+00:00"
lastmod: "2026-02-12T18:51:01.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/Turning-Production-Logs-into-Evaluation-Datasets](https://fireworks.ai/blog/Turning-Production-Logs-into-Evaluation-Datasets)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Turning Production Logs Into Evaluation Datasets
Turning Production Logs into Evaluation Datasets: A Data-Driven Approach
PUBLISHED
1/23/2026
Table of Contents
The Goal: Representative Coverage
The Technical Method: Semantic Clustering in Action
1. Vector Embeddings
2. Dimensionality Reduction (UMAP)
3. Automated Clustering (HDBSCAN)
4. Stratified Sampling
The Solution: Eval Protocol x Lilac Integration
The Workflow
Why This Matters
Try It Yourself
Table of Contents
Table of Contents
The Goal: Representative Coverage
The Technical Method: Semantic Clustering in Action
1. Vector Embeddings
2. Dimensionality Reduction (UMAP)
3. Automated Clustering (HDBSCAN)
4. Stratified Sampling
The Solution: Eval Protocol x Lilac Integration
The Workflow
Why This Matters
Try It Yourself
Table of Contents
If you are running an LLM in production, you have access to the most valuable resource for improving your model:
your actual user traffic.
Most teams know they need to run evaluations, but creating a high-quality evaluation dataset from scratch is difficult. Manually writing examples is time-consuming and often misses the nuances of how people speak. On the other hand, using your raw production logs directly isn't feasible; there is simply too much volume, noise, and redundancy to run model-based evaluations on everything.
We believe the best evaluation datasets are
inspired by production usage
. They should reflect the reality of what your users are asking, without the overhead of processing every single log.
Here is how we approach creating representative evaluation datasets from production traces.
The Goal: Representative Coverage
The challenge with raw production data is that it is unstructured. You might have 10,000 logs, but 5,000 of them might be variations of the same "Hello" or "Order Status" query.
To turn a stream of logs into a useful dataset, you need to filter out the noise and redundancy while ensuring you capture the diversity of user intent. You want a compact dataset that covers the
full semantic range
of your traffic from the most common questions to the critical edge cases.
The Technical Method: Semantic Clustering in Action
To achieve this structure, we use a workflow that organizes raw text by meaning rather than volume. To illustrate how this works, let’s walk through a real setup where we start with a batch of
100 customer service queries
. We use our integration with lilac to help create a subset.
Lilac
is an open-source tool designed for the exploration, curation, and quality control of datasets for training, fine-tuning, and monitoring LLMs. It allows teams to interactively visualize and quantify their data using on-device models, making it easier to curate high-quality AI data by identifying duplicates, PII, and obscure content. Trusted by companies like Cohere and Databricks,
Lilac
provides a centralized interface to inspect and collaborate on data refinement.
Lilac Integration example repository -
Eval Protocol x Lilac integration on GitHub
Lilac Official GitHub Repository -
Lilac Repository
1. Vector Embeddings
We start by converting those 100 raw text traces into embeddings. This transforms unstructured user queries into dense vector representations. In our setup, we use an embedding model with an
initial size of 512 dimensions
. In this high-dimensional vector space, queries with similar meanings are located close to one another mathematically, even if the phrasing is different.
2. Dimensionality Reduction (UMAP)
Analyzing 512 dimensions is computationally heavy and impossible for humans to visualize. We use
UMAP (Uniform Manifold Approximation and Projection)
to solve this in two steps:
•
First, we reduce the data from
512 dimensions down to 5 dimensions
. This lower-dimensional representation preserves the local relationships and is ideal for efficient clustering.
•
For the actual visual map you see on the screen, we project it down to
2 dimensions
(X and Y coordinates).
3. Automated Clustering (HDBSCAN)
Once the data is mapped in that 5-dimensional space, we need to identify the groups. We utilize
HDBSCAN
, a hierarchical density-based clustering algorithm.
In our example of 100 queries, the algorithm analyzed the density and automatically identified
5 distinct clusters
:
•
Cluster 0: "Account Management Issues"
(14 items)
•
e.g., "Recovery options change"
•
Cluster 1: "Product Return Requests"
(29 items)
•
e.g., "Order inquiry: ORD-21323"
•
Cluster 2: "Customer Service Complaints"
(24 items)
•
e.g., "Ratings are manipulated!"
•
Cluster 3: "Customer Benefits and Discounts"
(16 items)
•
e.g., "Gift wrapping available?"
•
Cluster 4: "Tech Product Comparisons and Availability"
(17 items)
•
e.g., "Compare iPhone 15 vs iPhone 15 Pro"
Notice the distribution:
Product Returns
(29 items) are twice as common as
Account Issues
(14 items). In a random sample, you would over-index on returns and potentially miss the account issues entirely.
4. Stratified Sampling
With our 5 clusters identified, we can finally create the dataset. Instead of randomly picking queries, we sample a representative trace from each of the
5 clusters
.
This effectively turns our noisy list of 100 queries into a clean, focused evaluation set that guarantees coverage across every distinct type of user interaction ensuring that "Account Management" and "Tech Comparisons" are tested just as rigorously as the high-volume "Return Requests."
The Solution: Eval Protocol x Lilac Integration
We have operationalized this method through our integration with
Lilac
. This workflow allows teams to easily pull traces from their observability platform and convert them into a structured evaluation dataset.
The Workflow
•
Ingest:
The integration pulls traces directly from your tracing solution (e.g.,
Langfuse
,
Braintrust
).
1
2
3
from
eval_protocol
import
create_langfuse_adapter
adapter
=
create_langfuse_adapter
(
)
rows
=
adapter
.
get_evaluation_rows
(
limit
=
1000
)
•
Cluster & Visualize:
Lilac processes the text (handling the embedding and UMAP reduction automatically), generating an interactive map of your production traffic. You can visually inspect the clusters to understand what your users are actually doing.
1
2
3
4
5
6
7
8
9
import
pandas
as
pd
from
lilac
as
ll
from
eval_protocol
.
adapters
.
lilac
import
evaluation_rows_to_dataframe
df
=
evaluation_rows_to_dataframe
(
rows
)
dataset
=
ll
.
create_dataset
(
ll
.
DatasetConfig
(
namespace
=
"local"
,
name
=
"traces"
,
source
=
ll
.
PandasSource
(
df
)
,
)
)
dataset
.
cluster
(
input
=
"user_query"
)
•
Curate & Sample:
You select a diverse subset from these clusters. This effectively "compresses" your production traffic into a manageable, high-signal dataset.
1
2
3
4
5
from
eval_protocol
.
adapters
.
lilac
import
dataframe_to_evaluation_rows
clustered
=
dataset
.
to_pandas
(
include_signals
=
True
)
samples
=
clustered
.
groupby
(
clustered
[
"user_query__cluster"
]
.
apply
(
lambda
x
:
x
[
"cluster_id"
]
)
)
.
apply
(
lambda
g
:
g
.
sample
(
min
(
5
,
len
(
g
)
)
)
)
diverse_rows
=
dataframe_to_evaluation_rows
(
samples
)
•
Evaluate:
This subset is automatically formatted and fed into
Eval Protocol
, ready for evaluation.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
from
eval_protocol
import
evaluation_test
,
DynamicDataLoader
,
create_langfuse_adapter
def
langfuse_generator
(
)
:
adapter
=
create_langfuse_adapter
(
)
return
adapter
.
get_evaluation_rows
(
limit
=
1000
)
def
lilac_cluster_and_sample
(
rows
)
:
# Cluster with Lilac, sample diverse subset
# ... (clustering logic from above)
return
diverse_rows
@evaluation_test
(
data_loaders
=
DynamicDataLoader
(
generators
=
[
langfuse_generator
]
,
preprocess_fn
=
lilac_cluster_and_sample
,
# ← Lilac integration
)
,
completion_params
=
[
{
"model"
:
"gpt-4o"
}
]
,
)
def
test_diverse_traces
(
row
)
:
return
evaluate
(
row
)
Why This Matters
This approach solves the "cold start" problem for evaluations. Instead of guessing what to test, you let your production data dictate the test cases.
•
Realism:
Your evaluations test against real user phrasing and intent.
•
Efficiency:
You get maximum signal with minimum compute. By sampling from clusters, you avoid testing the same behavior 50 times.
•
Visibility:
The visualization component gives you a macro-view of your product's usage, helping you spot patterns you might otherwise miss.
By combining the raw truth of production logs with the intelligence of semantic clustering, you can build an evaluation dataset that is both manageable and deeply representative of the real world.
Try It Yourself
Ready to turn your production traces into a high-signal evaluation set? We have built a complete example that you can run today.
👉
Check out the Eval Protocol x Lilac integration on GitHub
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
