---
title: "Bringing the leading vector database to your cloud"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/byoc-early-access/"
scraped: "2026-05-10T01:27:16.511696+00:00"
lastmod: "2026-02-19T17:27:41Z"
type: "sitemap"
---

# Bringing the leading vector database to your cloud

**Source**: [https://www.pinecone.io/blog/byoc-early-access/](https://www.pinecone.io/blog/byoc-early-access/)

←
Blog
Bringing the leading vector database to your cloud
Ben Esh
,
Shimshon Zimmerman
Feb 20, 2025
Product
Share:
Jump to section:
More ways to access Pinecone the way you want
How it works
Getting started
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Update: BYOC is now in public preview with a zero-access operating model, self-serve deployment, and support for AWS, GCP, and Azure →
Pinecone BYOC: Pinecone in your AWS, GCP, or Azure account, no vendor access
We’re excited to announce early access for a Bring Your Own Cloud (BYOC) offering of the Pinecone vector database on AWS. This solution lets you deploy a privately managed Pinecone region within your cloud account, giving you the security and control of a self-hosted solution while retaining the seamless experience of a fully managed SaaS product. Your data is stored and processed exclusively within your cloud account, ensuring complete data sovereignty—while our team handles all operational aspects, from deployment and maintenance to monitoring and updates.
More ways to access Pinecone the way you want
Companies are eager to unlock the potential of their unstructured data to build new products and capabilities. Pinecone’s purpose-built vector database retrieves accurate, well-informed, and up-to-date insights for customers to build uniquely knowledgeable AI applications. Since launching Pinecone serverless, we've seen increasing demand from large enterprises and regulated industries that require strict data sovereignty—where storing or processing data outside their own cloud is not an option.
At Pinecone, we believe engineers should spend time building AI applications, not managing infrastructure. That’s why we designed a best-in-class vector database as a managed service, prioritizing ease of use from day one. Deploying Pinecone in your cloud account gives you the flexibility to build AI solutions in the way that works best for you and your requirements.
Key benefits:
Security and compliance:
Pinecone ensures your sensitive data stays within your account so you can meet your data sovereignty requirements.
Enterprise-grade access controls:
Control user access, set security and usage policies, and monitor users and workloads operating within their environment.
Private multi-tenant region:
Use your private Pinecone environment to host multiple workloads for your company and enjoy the cost-performance tradeoffs of multi-tenant resource sharing.
Any AWS region:
Pinecone can be deployed in any AWS region of your choice, ensuring low-latency communication with your applications.
Cost savings:
Deploying a Pinecone service within your AWS account allows you to take advantage of your existing AWS discounts, saving plans, and commitments.
How it works
The Pinecone vector database is comprised of two main components:
The
Control Plane
is responsible for managing the index lifecycle, as well as operating all region-agnostic services such as user management, authentication, and billing. The control plane does not hold or process any records.
The
Data Plane
is responsible for storing and processing your records. It runs compute pods for executing vector similarity search queries and indexing operations, interacting with object storage to retrieve and persist index data.
When you create a serverless Pinecone index, all of its underlying data is stored in a Pinecone-managed Data Plane instance located within a region of your choice. This is the recommended offering for most users, as it provides the simplest way to use the Pinecone vector database.
However, for use cases with strict data sovereignty requirements, the Data Plane can be deployed to a dedicated VPC inside your AWS account, ensuring that all data is stored and processed locally and does not leave your organizational boundaries. Private Endpoints for AWS PrivateLink can be established as an additional security measure to protect your data plane API calls.
When setting up BYOC, Pinecone employs the principle of least privilege. We enforce role-based access control (RBAC) with specific IAM permissions and boundary policies to protect your assets. Access for maintenance and troubleshooting is secured through a customer-controlled VPN, with comprehensive logging and auditing.
Despite this split model, this is still a managed service: by operating a Pinecone agent service in each environment, we maintain communication with the global Pinecone-hosted control plane to allow ongoing management, health monitoring, and software updates. This design will enable us to provide the same service and reliability level as you would normally get with Pinecone while meeting enterprise security and compliance requirements.
Getting started
Pinecone’s BYOC offering for AWS is now in early access. To learn more, read the
BYOC documentation
or
contact us
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
