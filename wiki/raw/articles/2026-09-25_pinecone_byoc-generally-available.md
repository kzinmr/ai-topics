---
title: "Pinecone BYOC: Trusted AI Knowledge in the Customer Cloud"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/byoc-generally-available/"
scraped: "2026-09-25T06:00:30.934410+00:00"
lastmod: "2026-09-23T12:00:01Z"
type: "sitemap"
---

# Pinecone BYOC: Trusted AI Knowledge in the Customer Cloud

**Source**: [https://www.pinecone.io/blog/byoc-generally-available/](https://www.pinecone.io/blog/byoc-generally-available/)

←
Blog
Pinecone BYOC: Trusted AI Knowledge in the Customer Cloud
Jeff Zhu
,
Joerg Schad
Sep 23, 2026
Product
Share:
Jump to section:
Keeping proprietary knowledge inside the customer cloud
Zero-access BYOC model
Keep the managed Pinecone experience
Toyota brings manufacturing knowledge to AI within its environment
Bringing trusted AI knowledge to more environments
Get started
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Today, we are announcing the general availability of Pinecone Bring Your Own Cloud (BYOC) on AWS, Google Cloud, and Azure, bringing Pinecone’s trusted AI knowledge platform to where enterprise data needs to live. AI becomes transformative when it works with a company’s proprietary knowledge. Customer context, policies, and operational history allows its agents to make decisions and carry out work using expertise the business has built over years.
Organizations have spent years controlling where sensitive knowledge lives and who can reach it. Providing access to it typically meant managing knowledge infrastructure ranging from inference, document parsing, and vector databases. Platform teams shouldered the burden of tuning and maintaining the system, including keeping retrieval quality and performance stable across a diverse set of AI workloads.
With BYOC, customer data and the knowledge derived from it remain in the customer’s account, while Pinecone manages the platform operations. This means teams can bring sensitive AI workloads to production without taking on the complexity of operating knowledge infrastructure themselves. The APIs and interfaces remain the same as the managed service, providing organizations with the flexibility to select the right deployment model for each workload based on its security, connectivity, and operational requirements.
Keeping proprietary knowledge inside the customer cloud
Pinecone’s platform architecture separates the systems that manage the service from those that store and process customer data.
Control Plane:
Handles management operations such as resource lifecycle, authentication, and service health. It does not store or process customer content or request payloads.
Data Plane
: Stores, processes, and serves customer data and knowledge. AI agents and applications connect directly to this for read and write operations. The only data shared with Pinecone are anonymized operational metrics and traces for monitoring and support.
With BYOC, the data plane runs inside the customer's selected cloud account and region, including those beyond where Pinecone's standard service is available. Vectors, documents, metadata, and request payloads remain within the customer-controlled boundary.
Zero-access BYOC model
Pinecone does not require SSH, VPN, inbound network access, or a standing cross-account IAM role to manage the service. Upgrades, scaling actions, and maintenance work are retrieved using an outbound call from the Pinecone control plane and executed locally.
This pull-based mechanism allows Pinecone to manage the database without a persistent access path into the customer environment. Additionally, BYOC works alongside SSO, RBAC, SCIM + SAML, audit logging, encryption, and private-networking controls available with Pinecone's Enterprise plan so customers can have complete confidence in ensuring their proprietary knowledge is secure.
Keep the managed Pinecone experience
In addition to Pinecone handling upgrades, scaling, maintenance, and service health monitoring, customers retain access to Pinecone’s support and engineering teams for troubleshooting, incident response, and ongoing operational guidance.
Teams use the same Pinecone APIs, SDKs, and control plane workflows across the BYOC and standard deployments. This means each workload can use the deployment model that fits its data governance and access requirements without creating a separate development path.
Toyota brings manufacturing knowledge to AI within its environment
Toyota Motor North America (TMNA) was one of Pinecone’s first BYOC customers. TMNA used Pinecone to ground AI applications with decades of proprietary manufacturing knowledge while keeping that knowledge secure inside Toyota’s environment.
“Decades of engineering expertise and R&D knowledge live across our technical documentation, specifications, test data, and research. R&D GPT, backed by Pinecone’s vector database, helps bring that institutional knowledge together, giving our engineers a faster and more intuitive way to discover, connect, and apply the information they need while maintaining the security, governance, and access controls our enterprise requires. It helps our teams spend less time searching for knowledge and more time applying it to accelerate innovation.”
— Ravi Chandu Ummadisetti, Head of Agentic AI & Product Research, Toyota Motor North America
“A vast amount of our manufacturing know-how lives in our documentation, and that institutional knowledge is one of the most valuable assets we have. It also happens to be complex — highly structured engineering data sitting alongside unstructured process documents, across a lot of formats and a lot of different access patterns. Pinecone BYOC runs inside our own environment, so that knowledge never leaves our boundary and is served only to models we’ve already vetted. It handles that complexity at the scale our operations demand, with the enterprise security and governance controls our teams require. A critical requirement for how our team can use AI with confidence.”
— Kordel France, Head of AI Engineering, Toyota Motor North America
Bringing trusted AI knowledge to more environments
Our mission is to make AI knowledgeable, everywhere. BYOC extends Pinecone’s trusted AI knowledge platform to customer-controlled cloud environments today, and our work continues beyond BYOC.
We are developing a fully self-managed option for air-gapped and highly restricted networks where both the control plane and data plane will run inside the customer environment. Reach out if you're interested in shaping the security and deployment requirements of a self-managed Pinecone offering.
Get started
Talk with your Pinecone account team to review your requirements and plan your BYOC deployment, or
contact us
to get connected with us.
For more information, the
Pinecone BYOC product page
and the
BYOC documentation
cover the operating model and the architecture in detail.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
