---
title: "A practical guide to dimensionality reduction techniques | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/dimensionality-reduction-techniques/"
scraped: "2026-05-10T01:29:41.148317+00:00"
lastmod: "2023-07-13"
type: "sitemap"
---

# A practical guide to dimensionality reduction techniques | Hex 

**Source**: [https://hex.tech/blog/dimensionality-reduction-techniques/](https://hex.tech/blog/dimensionality-reduction-techniques/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
A practical guide to dimensionality reduction techniques
Practical examples of common dimensionality reduction algorithms in Python
Gabe Flomo
Data
July 13, 2023
Share:
twitter
linkedin
In this article
The data
Linear methods
Non-linear methods
Get started for free
Dimensionality reduction is a way to simplify complex datasets to make working with them more manageable. As data grows in size and complexity, it becomes increasingly difficult to draw meaningful insights, and even more difficult to visualize. Dimensionality reduction techniques help resolve this issue by giving you a smaller number of dimensions (columns) to work with, while still preserving the most important information. Think of it like casting a shadow of a complex object - you lose some detail, but you gain a simpler representation that's easier to work with and make comparisons with.
In this article, we will demonstrate how to implement various linear and non-linear dimensionality reduction algorithms in Python and visualize the differences between them.
Throughout this article, code snippets are presented alongside real, embedded outputs from
the companion Hex Project
, which you're encouraged to duplicate and use to follow along.
The data
The dataset used for these examples is a 🍷 wine dataset consisting of 13 features, or dimensions, which represent 3 different types of wines. Unfortunately for us, the specific wine types are unknown.
The goal here is to use dimensionality reduction along with the Kmeans clustering algorithm to reveal the wine groups hidden amongst our dataset. Let's take a look at the raw data.
Code cell from Dimensionality reduction - 0
We'll do some very light preprocessing to get the data into a workable state.
It's always good to check if there's any null values in the dataset:
Copy
data.isnull().sum()
Ours has none, so I haven't bothered printing out the long list of 0's that code spat out.
We'll also quickly standardize the data, which maps every column to a similar range and scale— this is important if you want to compare columns to one another directly.
Copy
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data = pd.DataFrame(data = scaler.fit_transform(data), columns = data.columns)
data.head()
Table display cell from Dimensionality reduction
Linear methods
Linear techniques aim to simplify the data while preserving the most important information. They do this by finding a way to represent the data in a lower-dimensional space that captures the original patterns and linear relationships in the data. The techniques we'll be looking at in this tutorial are:
PCA
ICA
TruncatedSVD
Principal component analysis (PCA)
Principal component analysis, or PCA, reduces the number of dimensions in your dataset while maximizing the explained variance per component. So... what does that actually mean? In every dataset, each column describes
something
. That something could be height, weight, or in our case it could be alcohol content. In any case, variance is a way to measure how much the values in a column fluctuate.
The more variance a feature has, the more information that feature contains.
Features with 0 variance add no information, making variance our friend.
PCA works by finding a compressed representation of our original data in a lower dimension that maximizes the overall variance (or fluctuations) of the original data. This means that the overall patterns are still preserved while making the data as simple as possible.
This code implements a PCA in Python:
Copy
from sklearn.decomposition import PCA
# Reduction objects
reducer3D = PCA(n_components=3)
reducer2D = PCA(n_components=2)
# compressed data in 2 and 3 dimensions
reduced_data3D = reducer3D.fit_transform(data)
reduced_data2D = reducer2D.fit_transform(data)
# creates a dataframe to visualize each reduced version
reduced3D_df = pd.DataFrame(data =  reduced_data,
columns = ['component_1', 'component_2', 'component_3'])
reduced2D_df = pd.DataFrame(data =  reduced_data,
columns = ['component_1', 'component_2'])
# Clustering allows us to add distinct colors to each group in our plot
kmeans = KMeans(n_clusters = 3)
reduced2D_df['cluster'] = kmeans.fit_predict(reduced2D_df)
reduced3D_cluster = kmeans.fit_predict(reduced3D_df)
We can see the data nicely forms three clusters in both 3 and 2 dimensions:
Code cell from Dimensionality reduction - 1
PCA in 2D from Dimensionality reduction
Independent Component Analysis (ICA)
The goal of Independent Component Analysis (ICA) is to separate mixed signals into their original sources. In ICA, we assume that the sources are independent from each other, meaning they don't affect each other's behavior. Let's take a simple example to understand this.
In our dataset, we have 3 different types of wine flavors present and we want to separate them back into their original wine types. Even though the wines are currently mixed, we believe that they have nothing to do with each other statistically. This basically means that if we were to drink one flavor of wine, we wouldn't gain any extra information about the other flavors. Assuming each flavor is independent, ICA will untangle the mixed wines and recover their original flavors, although you had no prior knowledge of what flavors were mixed or how they were mixed in the first place.
After selecting the number of desired independent components
(flavors of wine)
, you can use them as a reduced representation of your data. These components, which are statistically independent, capture different aspects of the original data, allowing for a reduced representation.
This code implements an ICA in Python:
Copy
from sklearn.decomposition import FastICA
# Reduction objects
reducer3D = FastICA(n_components=3)
reducer2D = FastICA(n_components=2)
# compressed data in 2 and 3 dimensions
reduced_data3D = reducer3D.fit_transform(data)
reduced_data2D = reducer2D.fit_transform(data)
# creates a dataframe to visualize each reduced version
reduced3D_df = pd.DataFrame(data =  reduced_data,
columns = ['component_1', 'component_2', 'component_3'])reduced2D_df = pd.DataFrame(data =  reduced_data,
columns = ['component_1', 'component_2'])# Clustering allows us to add distinct colors to each group in our plot
kmeans = KMeans(n_clusters = 3)
reduced2D_df['cluster'] = kmeans.fit_predict(reduced2D_df)
reduced3D_cluster = kmeans.fit_predict(reduced3D_df)
We can again visualize this in both 3 and 2 dimensions:
Code cell from Dimensionality reduction - 2
ICA in 2D from Dimensionality reduction
TruncatedSVD
TruncatedSVD, short for Truncated Singular Value Decomposition, is a dimensionality reduction technique that is particularly effective when working with large datasets. It is very closely related to PCA and may even be considered a variant of PCA, although this technique is much better at creating a dense representation from a sparse matrix (a matrix with a lot of zeros).
This code implements a TruncatedSVD in Python:
Copy
from sklearn.decomposition import TruncatedSVD
# Reduction objects
reducer3D = TruncatedSVD(n_components=3)
reducer2D = TruncatedSVD(n_components=2)
# compressed data in 2 and 3 dimensions
reduced_data3D = reducer3D.fit_transform(data)
reduced_data2D = reducer2D.fit_transform(data)
# creates a dataframe to visualize each reduced version
reduced3D_df = pd.DataFrame(data =  reduced_data,
columns = ['component_1', 'component_2', 'component_3'])reduced2D_df = pd.DataFrame(data =  reduced_data,
columns = ['component_1', 'component_2'])
# Clustering allows us to add distinct colors to each group in our plot
kmeans = KMeans(n_clusters = 3)
reduced2D_df['cluster'] = kmeans.fit_predict(reduced2D_df)
reduced3D_cluster = kmeans.fit_predict(reduced3D_df)
Code cell from Dimensionality reduction - 3
Chart cell from Dimensionality reduction - 1
Non-linear methods
Non-linear dimensionality reduction techniques try to capture the more complex non-linear relationships in the data and represent them in a lower dimensional space. In this tutorial, we will be covering the three most commonly used options:
Multidimensional scaling
T-SNE
UMAP
Multidimensional Scaling (MDS)
Multidimensional scaling is a technique used to visually represent the similarity or dissimilarity between observations in a dataset. In this representation, similar observations are placed closer together, while dissimilar observations are positioned farther apart. MDS offers the advantage of performing both linear and nonlinear dimensionality reduction, depending on the specific settings and algorithm being used. In all cases, MDS aims to maintain the distances between data points, ensuring that the lower-dimensional representation preserves these distances.
Copy
from sklearn.manifold import MDS
# Reduction objects
manifold3D = MDS(n_components=3)
manifold2D = MDS(n_components=2)
# compressed data in 2 and 3 dimensions
manifold_data3D = manifold3D.fit_transform(data)
manifold_data2D = manifold2D.fit_transform(data)
# creates a dataframe to visualize each reduced version
manifold3D_df = pd.DataFrame(data =  manifold_data3D,
columns = ['component_1', 'component_2', 'component_3'])manifold2D_df = pd.DataFrame(data =  manifold_data2D,
columns = ['component_1', 'component_2'])
# Clustering allows us to add distinct colors to each group in our plot
kmeans = KMeans(n_clusters = 3)
manifold2D_df['cluster'] = kmeans.fit_predict(manifold2D_df)
manifold3D_cluster = kmeans.fit_predict(manifold3D_df)
Code cell from Dimensionality reduction - 4
Chart cell from Dimensionality reduction - 2
T-distributed Stochastic Neighbor Embedding (TSNE)
T-distributed Stochastic Neighbor Embedding (t-SNE) is an algorithm used to simplify and visualize complex data. It does this by comparing the similarities between data points in both the original high-dimensional space and a lower-dimensional space. Then, it creates probability distributions to represent these similarities, aiming to make them as similar as possible. The algorithm adjusts the positions of the data points in the lower-dimensional space iteratively until the distributions are as close as possible.
One key thing to note about t-SNE is that it focuses more on preserving local relationships rather than global ones. This means that data points that are close together in the original high-dimensional space will likely stay close together in the lower-dimensional representation. However, the overall distances between points might not be preserved. This trade off allows t-SNE to highlight local patterns and clusters, making it useful for visualizing complex data.
Here's Python code to perform a 3D and 2D t-SNE reduction on our data:
Copy
from sklearn.manifold import TSNE
# Reduction objects
manifold3D = TSNE(n_components=3)
manifold2D = TSNE(n_components=2)
# compressed data in 2 and 3 dimensions
manifold_data3D = manifold3D.fit_transform(data)
manifold_data2D = manifold2D.fit_transform(data)
# creates a dataframe to visualize each reduced version
manifold3D_df = pd.DataFrame(data =  manifold_data3D,
columns = ['component_1', 'component_2', 'component_3'])manifold2D_df = pd.DataFrame(data =  manifold_data2D,
columns = ['component_1', 'component_2'])
# Clustering allows us to add distinct colors to each group in our plot
kmeans = KMeans(n_clusters = 3)
manifold2D_df['cluster'] = kmeans.fit_predict(manifold2D_df)
manifold3D_cluster = kmeans.fit_predict(manifold3D_df)
Code cell from Dimensionality reduction - 5
Chart cell from Dimensionality reduction - 3
Uniform Manifold Approximation and Projection (UMAP)
UMAP is like t-SNE's cool older cousin. It also learns a non-linear mapping that keeps clusters intact, and it can do it faster. Additionally, UMAP tends to do a better job at preserving the global structure of the data compared to t-SNE. In this context, global structure refers to the "closeness" between similar wine types whereas local structure would refer to how well wines of the same type cluster together.
UMAP has it's own Python package, which makes it very easy to use:
Copy
from umap import UMAP
# Reduction objects
manifold3D = UMAP(n_components=3)
manifold2D = UMAP(n_components=2)
# compressed data in 2 and 3 dimensions
manifold_data3D = manifold3D.fit_transform(data)
manifold_data2D = manifold2D.fit_transform(data)
# creates a dataframe to visualize each reduced version
manifold3D_df = pd.DataFrame(data =  manifold_data3D,
columns = ['component_1', 'component_2', 'component_3'])manifold2D_df = pd.DataFrame(data =  manifold_data2D,
columns = ['component_1', 'component_2'])
# Clustering allows us to add distinct colors to each group in our plot
kmeans = KMeans(n_clusters = 3)
manifold2D_df['cluster'] = kmeans.fit_predict(manifold2D_df)
manifold3D_cluster = kmeans.fit_predict(manifold3D_df)
Code cell from Dimensionality reduction - 6
Chart cell from Dimensionality reduction - 4
These examples are just scratching the surface of what's possible with dimensionality reduction, but these core techniques are extremely useful when working with any complex dataset.
Remember, dimensionality reduction is not a one-size-fits-all solution; the hardest part is figuring out which method to employ based on the nature of your data and the specific problem you're trying to solve— or if dimensionality reduction is even the right technique to use at all.
If you want to dive in and start exploring, you can duplicate
the companion Hex Project
to start with a template you can customize. It's free to sign up and the demo dataset is built right in, so grab a delicious glass of wine (but which kind?!) and get reducing.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.

If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨ Get started for free
👩‍💻 Open roles
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
