---
title: "Vectors as AI Data Primitives"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/vectors-as-ai-data-primitives/"
scraped: "2026-05-10T01:27:57.774774+00:00"
lastmod: "2024-01-24T18:41:14Z"
type: "sitemap"
---

# Vectors as AI Data Primitives

**Source**: [https://www.pinecone.io/blog/vectors-as-ai-data-primitives/](https://www.pinecone.io/blog/vectors-as-ai-data-primitives/)

←
Blog
Vectors as AI Data Primitives
Adam Cheer
Jan 24, 2024
Company
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
A year of transformation
OpenAI brought ChatGPT to prime time on November 22nd, 2022. No one anticipated what a B2B and DTC revolution it would become. In response, we’ve seen a chaotic 2023 with the launch of several LLMs (Claude, Falcon, Gemini, to name a few), all of which are incredibly powerful and excel at different tasks.
Adam Selipsky, CEO of AWS, summed it up best:
*“Customers are finding that different models actually work better for different use cases or on different sets of data. Some models are great for summarization, others are good for reasoning and integration, and still others have awesome language support. And then there’s image generation, search use cases, and more, all coming from both proprietary models, and models that are publicly available to everybody”
In this type of dynamic market and period, the ability to adapt is the most valuable capability that you can have. Due to that involved nature, interoperability with the ecosystem and flexibility are paramount.
You need to be able to switch between models rapidly, even combining them with the same use cases. As organizations use these new models and want to capitalize on the promise of GenAI, they’ll need purpose-built infrastructure that allows for that type of ‘switchability’ and dynamism.
We’ve seen this story before.
Transformation means new architectural requirements
New data types have historically necessitated a new database type and new ways to work with data. As GenAI and AI/ML move to become a more core focus, unstructured data will become increasingly important.
*The growth of unstructured data is enormous:
*“The unstructured data market is 20 times bigger than the structured data market that most BI tools have been built on for the last 20, 30 years. What we view is essentially AI as this global opportunity in the technology space to see roughly a 20X increase in the size of the big data opportunity now that there’s a new data type that’s processable” Jeff Denworth of VAST
This type of shift is similar to the early 2010s, which was a transformative period in how Machine Learning (ML) (how models acquire knowledge) infrastructure would evolve, particularly with the advent of Large Language Models and vectors being used at a broader scale. In this period, they were focused on training neural networks to do complicated tasks. It would pave the way for reinforcement learning (algorithm learning to make decisions through trial and error) to emerge and be used to enable use cases like image detection, translation, and NLP.
The apparent companies to solve this problem were the likes of Google and Microsoft. They had massive resources, massive scale, and a lot of intelligent people. Easy win, right?
Microsoft had a belief that the computational challenges could be solved by servers on Windows, using the methods of how they scaled SQL Server. Spinning up more resources and replicating the data across them was how they wanted to attempt reinforcement learning.
Google had the most significant data center footprint in the world at the time. They used the same shared-nothing principles for solving other problems; they thought they could uplevel compute similarly for better deep learning. To ‘teach’ the neural network, they forced it to learn from payloads of text and images.
Neither of these approaches was inherently wrong; they were the standard of the time. Using the traditional database methods of scale, it became costly and was computationally slow. Both approaches believed that building bigger, faster, stronger systems around CPUs was the way.
DNNresearch, a University of Toronto research group, and Alex Krizhevsky, a computer scientist, recognized these limitations. They had a different idea. Shifting from the traditional training methods used by the industry, they tried reinforcement training with new hardware via Atari games to make neural networks learn complex tasks.
At the time, GPUs (specialized hardware that can do parallel processing) were only considered primarily utilized for gaming due to their adept handling of intricate visual/graphic computation and were underutilized in AI. This insight was contrary to the prevailing norm, where most ML computations were conducted using CPUs. DNNresearch recognized GPUs could run multiple operations simultaneously and parallelize operations, enabling better performance & scale for training.
This innovative strategy led to a remarkable achievement: winning the prestigious ImageNet (aka ILSVRC-annual competition to develop algorithms that could classify and detect objects in a large dataset of images) with a GPU running under Alex’s desk.
Following this win and change in how we would run computational patterns for training, they named this method ‘AlexNet.’ DNNresearch would later be acquired by Google due to its prowess.
The GPUs adoption reverberates to GenAI & ML today
Source:
DALL E
The success of AlexNet was not just in its victory but in showcasing that the new world we were entering would require a new way of solving new problems. This was when we saw the shift from CPUs to GPUs for training. It led to massive investment in GPUs by all the cloud providers as part of their data centers.
This story is similar to what we are seeing in our market today.
Bringing it back to the LLM Era: why new architecture matters
As technology evolves, we continue to evolve in how we want to represent and retrieve data.
As the power of personal computing rose, databases and search engines began to prop up around access to this technology to allow for faster data analysis & retrieval on structured data. Cloud infrastructure then became prominent, allowing these databases and search engines to be scaled cheaper, at a broader scale, and more effectively. This additional computational power and access then led to people trying to extract more knowledge and value from unstructured data with new databases.
We now see the convergence of databases, unstructured data, search, and scale with vector databases designed for vector embeddings. Put simply, vector embeddings represent your enterprise's data in the language that AI can read to give the data more context and characteristics that cannot be captured in rows and columns or key-value pairs.
Purpose-built architecture for GenAI & ML is necessitated over traditional architecture
Source:
DALL E
If using architecture not built to support these new patterns, you see scale issues, meaning it becomes computationally challenging to use this new technology, hurting your ability to get the full promise of these new technologies.
This was the same reason DNNresearch, a team of 3, outperformed the likes of major players with significantly more resources, as we explored above.
The landscape
Many players in our ecosystem are modern data platforms offering fully integrated vertical or horizontal AI/ML stacks or integrated models.
These modern data platforms are the relational and non-relational databases that helped launch the data renaissance in the 2010s as data volume and computation power grew. They were purpose-built to handle the specific data requirements of the time.
MongoDB is a prime example of a purpose-built database of this era. Unlike traditional storage systems that require everything to be neatly categorized and uniform, MongoDB was built to handle schemaless data (no predefined schema, adapts to data changes).
At its core, MongoDB was crafted to solve the challenges of managing vast amounts of JSON-like documents. With that in mind, MongoDB's retrieval and storage mechanisms were built to optimize for this type of workload pattern.
To deviate from traditional databases (inclusive of relational databases), MongoDB built something that stored data in BSON (binary JSON), a format that enables hierarchical data representation (a tree-like structure). MongoDB would then index in a document-oriented way (ex: identify something cross-document) instead of how things had typically been done in a table (ex: orders are related to customers). This enables array or document-based queries, which have a different data shape and query pattern than relational databases. Because traditional databases rely so heavily on SQL and rows and columns, these databases couldn't simply add bolt-on features that could optimally do this.
This same purpose-built mindset is necessitated by this new wave of technology today. Similar to how companies couldn’t just bolt-on functionality to handle document data as efficiently as MongoDB, companies can't just simply bolt-on functionality to handle vectors.
When these modern data platforms were built, the biggest things we could think of at the time were long strings, huge numbers, and a massive amount of rows and/or columns of a database, and how we craft a query to find an answer. With Gen AI & this new wave of ML, we are thinking of millions to billions of vectors, high dimensionality, and methods like ANN (approximate nearest neighbor). This inhibits these modern systems' ability to deliver on additional use cases and provide consistent performance.
So that modern data platforms can try to accommodate this new data pattern, they add a vector index or bolt-on feature. A vector index is a tool that quickly finds and organizes data by its similarities, enhancing search capabilities. However, it cannot represent the dimensionality or perform the management functions of a pure play vector database.
These bolt-on features use architectures and compute engines not built to handle the high dimensionality or compute that vector embeddings pose. You compromise both the performance and scalability of the primary database and these new bolt-on vector capabilities. Your team is now focused on optimizing and tuning infrastructure rather than solving unique business problems.
To scale, you can increase the size of your compute resources. This risks longer recovery times if those resources fail. Alternatively, you can have an army of smaller compute resources, but because you have more compute resources, you have a larger surface area that poses a risk of failure. If one of these smaller compute resources goes down, your application stops—both present inherent risks.
From a performance perspective, as you add more resources into one of these shared-nothing clusters, you see a lot more traffic since you have more resources. This traffic grows, which then leads to diminishing returns in performance. This leads to increasing complexity with capacity planning for theoretical peak requirements and introducing additional operational overhead to optimize sharding strategies across multiple indexes and various node configurations and replicas. This can scale, but to do so, it will always be overprovisioned and waste significant resources.
Your resilience as a business-critical platform for applications and cost-effectiveness will be complex to manage for the team with the fast things are moving in the industry.
Why Pinecone?
As we explored prior with the 2010s and the move to GPUs, new architectures for new problems matter. LLMs and this new era of ML require new architecture.
From our founder, Edo Liberty:
*“You can think of LLMs and, in general, AI developing computational reasoning…they represent objects as numerical objects called vectors. That becomes the key to search. The database that you need to be able to use to be able to operate and house that information and retrieve it efficiently is different. It’s not a traditional database.”
Pinecone was GA’d in 2019. The intention was to create a platform that would be purpose-built to handle the new physics of data we are now in. The transformer and vectors necessitated a new database type. Our technology wasn’t based on a prior paradigm or existing system like most of the technology in space.
We were built from scratch, purpose-built to be the developer's de facto choice for all things vector embeddings. It also isn't tightly integrated to a specific cloud or model provider, giving you more flexibility. With how we have architected our product, we are a truly unbounded database for the era of Gen AI & a new era of ML.
Enterprises are building on Pinecone because we have the best vector infrastructure layer to enable the full spectrum of Gen AI and ML use cases with adaptability to what your enterprise needs to innovate. The traditional, modern data platforms cannot deliver on this because they were built for the more unidimensional world of data. And very importantly - it's offered as a service. You hired your team to develop applications and products, not to handle knob-turning and infrastructure. No matter the payload or scale, Pinecone will dynamically respond to manage your workload.
Pinecone: purpose-built architecture for GenAI, LLMs, and ML
Source:
DALL E
Purpose-built to handle vector embeddings and GenAI in a serverless fashion, Pinecone provides:
Choice and flexibility:
pick the cloud, region, and model(s) you want to work with. No services tightly coupled to a specific cloud or vendor
Serverless Orchestration: d
elivered as a service, Pinecone provides a turnkey service to minimize maintenance efforts and ensure the health and availability of your AI applications. Infrastructure is orchestrated for you based on usage. This includes index rebuilds, managing pod fullness, scaling resources, and more
Blob Storage Utilization:
we employ vector clustering atop blob storage to provide low-latency searches for virtually unlimited records, combining memory efficiency with cost-effective access. With the nature of this retrieval being very deterministic, the cluster-based structure of our indexed data allows our retrieval algorithm to scan only data relevant to the user query incisively
Separation of storage from compute and READ/WRITE paths:
resources' Eliminates idle resources ‘running the meter.' This separation also ensures that operations for reads and writes are handled in isolation, achieving high throughput and low latency
Innovative Indexing:
tasked with creating a geometrically partitioned index, the index builder plays a crucial role in doing the extensive work needed to optimize an index for efficient querying. This allows for continuous data addition without the need for frequent re-indexing. This enables freshness for search within seconds
Cost-Effective Consumption Model: o
ur model is based on actual usage, billing you only for storage and compute operations performed. This means you aren't paying for any warm-up or idle time of nodes and can efficiently index & manage billions of vectors while only paying for resources used
All of the features above are purpose-built to handle vector embeddings. They are not features being augmented with new libraries or forcing an existing product to try to perform on data types it wasn't optimized for. This differentiated architecture matters because optimizing for scale, search speed, and availability is essential in these types of use cases and applications, which traditional databases or indexes were not built to do. Pick your cloud and model, and let our API run your application and provision infrastructure based on demand.
*Quote citations:
Adam Selipsly:
AWS 2023 re:Invent keynote /w Adam Selipsky
Jeff Denworth of Vast:
SiliconAngle
Edo Liberty:
GenerativeNow Interview
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
