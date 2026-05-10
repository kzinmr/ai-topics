---
title: "Accelerate prototyping and development with Pinecone Local"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pinecone-local/"
scraped: "2026-05-10T01:27:52.198578+00:00"
lastmod: "2024-12-06T12:55:00Z"
type: "sitemap"
---

# Accelerate prototyping and development with Pinecone Local

**Source**: [https://www.pinecone.io/blog/pinecone-local/](https://www.pinecone.io/blog/pinecone-local/)

←
Blog
Accelerate prototyping and development with Pinecone Local
Ana Wishnoff
Dec 6, 2024
Product
Share:
Jump to section:
Test, prototype, and develop on your local machine
Set up the vector database emulator
Start building today
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Pinecone Local, a self-hosted, in-memory emulator of the vector database, is now available in public preview for all users. This means you can prototype, test, and develop AI applications locally while seamlessly integrating workflow testing into CI/CD pipelines.
Test, prototype, and develop on your local machine
To build robust, production-grade AI applications, you must properly test your vector database across various edge cases in different environments and ensure it fits seamlessly into the rest of your application architecture. However, constantly scaling a suite of infrastructure up and down to run integration tests is not sustainable, as it can incur extra usage and cost and drain resources.
Pinecone Local
allows you to run all your integration or unit tests — including the ones within your CI pipeline —
on your local machine
, avoiding resource-intensive serverless operations.
With Pinecone Local, you can:
Spin up and tear down Pinecone indexes in-memory, perfect for quickly testing and prototyping
Use any of our supported SDKs to make requests to the Pinecone API across the control plane and data plane endpoints, with no API key needed
Run large-scale tests on your own data without incurring any usage cost, enabling you to accurately and reliably experience how your production vector database will function
Develop your Pinecone app locally with no internet connection, providing more flexibility for you and your team
Set up the vector database emulator
Pinecone Local is available via Docker through an image called
pinecone-local
. This image provides the full vector database emulator, which enables you to add/delete indexes using our API to build out your environment and run your full suite of tests.
If you’d rather just spin up a single local Pinecone index without starting the full emulator, see our
documentation
on the
pinecone-index
Docker image.
Installation is easy. You pull down the image and configure your index through Docker Compose or the Docker CLI.
Configure the Docker image
To start, you will pull the
pinecone-local
image from Docker:
docker pull ghcr.io/pinecone-io/pinecone-local:latest
and then start Pinecone Local:
docker run -d \
--name pinecone-local \
-e PORT=5081 \
-e PINECONE_HOST=localhost
-p 5081-6000:5081-6000 \
--platform linux/amd64 \
ghcr.io/pinecone-io/pinecone-local:latest
Initialize your client and locally develop your app
Once you’ve started the Pinecone Local image, you can begin developing your app. First, initialize your Pinecone client, targeting the port specified in your Docker compose file. The below example uses the
Python client
.
pc = PineconeGRPC(api_key="pclocal", host="http://localhost:5081")
Once the client has been initialized, you can create new indexes using the API the same way you’d normally do it in Pinecone:
if not pc.has_index(index_name):  
    pc.create_index(
        name="index1",
        dimension=2,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1",
        )
    )
Now, you can develop your application as normal, including upserting and querying data. Note that an API key is not needed to use Pinecone Local, so when initializing your Pinecone client, you can pass any string to the API key parameter.
Start building today
Pinecone Local is not suitable for use in production applications, due to its nature as an in-memory emulator. It serves as a tool for testing and prototyping, so does not provide the scalability or durability needed for robust production applications.
With that said, Pinecone Local represents an exciting step forward for the Pinecone developer experience — we encourage you to try it out. Visit our
documentation
for detailed instructions, and make sure to leave us your feedback, ask questions, and share your experience on our
Community Forum
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
