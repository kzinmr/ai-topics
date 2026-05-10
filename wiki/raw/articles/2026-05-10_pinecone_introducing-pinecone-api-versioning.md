---
title: "Introducing Pinecone API Versioning"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/introducing-pinecone-api-versioning/"
scraped: "2026-05-10T01:27:52.686140+00:00"
lastmod: "2024-08-16T13:03:48Z"
type: "sitemap"
---

# Introducing Pinecone API Versioning

**Source**: [https://www.pinecone.io/blog/introducing-pinecone-api-versioning/](https://www.pinecone.io/blog/introducing-pinecone-api-versioning/)

←
Blog
Introducing Pinecone API Versioning
Gareth Jones
Jul 18, 2024
Product
Share:
Jump to section:
Why versioning
Our approach
Implementation
Release Schedule
SDKs
Start building today
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Evolving an API is a complex process with implications for both our team and users. At Pinecone, we view an API as a contract between our services and our users. This contract must balance the need for us to innovate while maintaining stability for existing integrations.
API versioning
allows us to manage this balance by providing a way to introduce changes while preserving compatibility.
Why versioning
API versioning is necessary for several reasons. First, it ensures stability and predictability. By maintaining multiple versions of an API, we can introduce new features and improvements without disrupting existing integrations. This approach allows developers to continue using a stable and predictable environment, reducing the risk of breaking changes that could adversely affect their applications.
Second, versioning offers the flexibility to innovate. It enables us to make necessary changes and enhancements to our API, knowing that existing users will not be forced to adapt immediately. While versioning gives us the flexibility to evolve our API, we take extreme care to minimize changes that could impact current users. Outgoing changes are funneled through a review process, where they’re are designed, documented, and reviewed by a broader audience within the company. This visibility helps catch errors and inconsistencies early, ensuring a cleaner and more robust API.
Our approach
In developing our approach to API versioning, we looked to industry best practices of leading developer products like
Stripe
and
Google Cloud
. The most common approach is entity versioning via the URL path, such as using
v1
and
v2
to denote different versions of the API. This method clearly distinguishes between major versions, allowing developers to opt into new versions when they are ready.
However, while this approach is effective, it has its limitations. It can sometimes be challenging to communicate the incremental nature of changes within a major version and to manage the lifecycle of multiple versions simultaneously. As a result, we explored alternative approaches that could offer more nuanced control and communication.
After careful consideration, we opted for a date-based API versioning schema managed via a custom header. This method offers several advantages. By using dates to denote versions, we can clearly communicate the age and stage of each API iteration. This transparency helps developers understand the context of each version and make informed decisions about upgrading.
Additionally, date-based versioning simplifies the upgrade process. Developers can plan and manage updates more effectively, knowing that each version represents a specific snapshot in time with incremental changes. This approach also allows us to introduce improvements more frequently, as we are not constrained by the need to bundle changes into larger, less frequent major releases.
Implementation
Each version of our API is additive and typically contains a small set of incremental changes to ensure a smooth transition for developers. While we strive to minimize disruptions, there may be intentional breaking changes when deprecating features. This approach allows us to introduce improvements and changes without breaking previously released stable versions.
By adopting a date-based API versioning schema, we aim to provide a clear, predictable, and manageable API lifecycle for our users. This strategy enables developers to leverage our platform’s capabilities without unexpected disruptions, ensuring a seamless and productive experience.
Release Schedule
Pinecone will release a new
stable
and a
release candidate
of the API on a quarterly basis, starting in July.
Stable:
Each stable version remains unchanged and supported for a minimum of 12 months. Since stable versions are released every 3 months, you have at least 9 months to test and migrate your app to the newest stable version.
Release candidate:
The release candidate gives you insight into the upcoming changes in the next stable version. It is available for approximately 3 months before the release of the stable version and can include new features, improvements, as well as
breaking changes
.
Below is an example of Pinecone’s version support schedule:
Release Schedule Example
SDKs
Official
Pinecone clients
provide convenient access to Pinecone APIs. Client versions are pinned to specific API versions. When a new API version is released, a new version of the client library is also released.
The mappings between API versions and client library versions are as follows:
2024-04
2024-07
Python client
4.x
5.x
Node.js client
2.x
3.x
Java client
1.x
2.x
Go client
0.x
1.x
Start building today
View our docs
to learn more about our API versioning and
start building
with Pinecone today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
