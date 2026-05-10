---
title: "April Monthly Product Update"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/april-2024-product-update/"
scraped: "2026-05-10T01:27:31.426635+00:00"
lastmod: "2024-05-01T16:06:25Z"
type: "sitemap"
---

# April Monthly Product Update

**Source**: [https://www.pinecone.io/blog/april-2024-product-update/](https://www.pinecone.io/blog/april-2024-product-update/)

←
Blog
April Monthly Product Update
Xian Huang
May 1, 2024
Product
Share:
Jump to section:
Try serverless for free with 3x more capacity
Build on serverless with Java SDK and expanded regions
Global Control Plane API to streamline resource management
Simplified process to build and search what you need
Seamless access to Pinecone from our partner platforms
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
This month, we continued expanding our
serverless
service and improving your experience building with Pinecone. Check out some of our product highlights below or read the full
release notes
.
Try serverless for free with 3x more capacity
You now get 3x more capacity with the new
serverless free plan
, including 2GB of storage, 2M
Write Units (WU)
(~300k writes), 1M
Read Units (RU)
(~100k reads) per month, and up to 5 indexes. Existing free plan users can easily convert
‘gcp-starter’ indexes to serverless
.
Build on serverless with Java SDK and expanded regions
Pinecone serverless lets you build AI applications for
any size of customer base
with
better performance and costs
. With our
Pinecone Java client (v1.0.0)
adding serverless support, you can build on serverless with Java,
Python
, or
Node.js
.
Start building
in the new eu-west-1 region in addition to the us-west-2 and us-east-1 regions of AWS.
// Maven
<dependency>
  <groupId>io.pinecone</groupId>
  <artifactId>pinecone-client</artifactId>
  <version>1.0.0</version>
</dependency>

// Gradle
implementation "io.pinecone:pinecone-client:1.0.0"
Global Control Plane API to streamline resource management
Our
Global Control Plane API
is now
generally available
(view our new
API lifecycle policy
to learn more details about the lifecycle of Pinecone APIs, features, and client versions), which enables you to use a global URL for all control plane operations (e.g.,
list indexes
,
create indexes
,
list collections
) regardless of the cloud environment.
The Global API is currently supported within our Python, Node, and Java
clients
. If you want to manage your Pinecone resources via infrastructure as code, we support
Terraform
and
Pulumi
. View the
quickstart
to start building today, or check out the
migration guide
to upgrade to the new API.
Simplified process to build and search what you need
Our new
sample apps
allow you to interact with a demo before you build your own. Simply run the npx create-pinecone-app command to make the sample app yours. Check out our
demo
to learn how to build a multi-tenant RAG app with our sample apps.
Looking for something on the Pinecone site? With our new AI chatbot, you can find relevant search results and resources faster from across the Pinecone site — from our docs, blogs, or forums — and even open a support ticket. Check out a quick demo below.
Pinecone AI chatbot
Seamless access to Pinecone from our partner platforms
With the new
Pinecone Partner Program
, our partners can create a seamless signup and login process for joint users to access Pinecone using our
Connect
widget and
monitor
usage.
Check out the
release notes
for a running list of all product and feature releases. If you’re new to Pinecone,
try it out
for free today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
