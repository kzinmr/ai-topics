---
title: "Strengthening security and increasing control with CMEK and API key roles"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/strengthening-security-and-control/"
scraped: "2026-05-10T01:27:48.612974+00:00"
lastmod: "2024-12-02T10:54:29Z"
type: "sitemap"
---

# Strengthening security and increasing control with CMEK and API key roles

**Source**: [https://www.pinecone.io/blog/strengthening-security-and-control/](https://www.pinecone.io/blog/strengthening-security-and-control/)

←
Blog
Strengthening security and increasing control with CMEK and API key roles
Anshum Garg
,
Adhvik Kanagala
Dec 2, 2024
Product
Share:
Jump to section:
Enhancing data security and tenant isolation with CMEK
Pinecone’s CMEK and hierarchical encryption
Enabling more granular RBAC with API key roles
Start building today
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Security, control, and performance are non-negotiable requirements for Pinecone and for our customers, and we’re pleased to unveil two new features that support these goals:
Customer-managed encryption keys (CMEK)
Role-Based Access Control (RBAC) with API key roles
Below, we’ll explain each feature in detail and show you how to leverage them within your Pinecone projects.
Enhancing data security and tenant isolation with CMEK
By default, Pinecone serverless features strong protections for customer data, including:
Applying AES256 encryption for data at rest
Isolating tenants using strong logical boundaries and provenance checks within the multi-tenant environment
The introduction of CMEK brings with it a range of benefits, including:
Greater control:
With CMEK, you manage the keys used for encryption and decryption, keeping full control over access to your data and preventing third parties from accessing the keys without your consent. You can also revoke keys independently and immediately, providing even more control over data access.
Enhanced tenant isolation:
Because your data is encrypted with different keys from all the other data, CMEK enhances tenant isolation within a multi-tenant environment like Pinecone serverless — even beyond existing measures such as provenance checks and logical isolation of resources.
An additional security layer:
By managing your own keys, you reduce reliance on Pinecone’s internal key management systems, creating an added security layer (via trust boundaries) that can provide additional guarantees that may be required for sensitive data.
Importantly, the additional security and control also:
Supports compliance requirements:
Some regulations (e.g., GDPR, HIPAA, and many financial standards) mandate direct control over encryption keys, which CMEK can help address.
Improves visibility and auditability:
With CMEK, you can more closely monitor and log key usage and access attempts, providing better transparency and further supporting compliance activities.
Note:
While CMEK provides many important benefits, it also requires careful key management and protection measures on the part of the customer, as lost or mismanaged keys can render data inaccessible.
Pinecone’s CMEK and hierarchical encryption
Understanding how Pinecone encrypts your data, along with the associated design considerations, can help you evaluate how and when to use CMEK. To build your knowledge, we’ll briefly cover two closely related topics:
CMEK within a Pinecone serverless environment
Hierarchical encryption with CMEK
CMEK within a Pinecone serverless environment
CMEK is enabled at the Pinecone project level, which forces all indexes in the project to be encrypted. Note that the CMEK toggle cannot be subsequently changed, so
this is a
permanent decision for the project's life.
After the initial setup, the experience using a CMEK-encrypted index is identical to using a serverless Pinecone index.
Securing Pinecone serverless with CMEK and AWS PrivateLink
Encryption service
In the background, all access to stored data that represents the CMEK-encrypted index is abstracted behind an encryption service.
This encryption service manages data encryption and decryption when customers perform data plane operations by accessing and caching encryption material and brokering access to a customer’s Key Management Service (KMS). It also delineates system boundaries, allowing us to ensure that
no stateful services ever handle unencrypted data
and that
stateful services only store encrypted data
.
Moreover,
only stateless services handle unencrypted data
, which they serve upon customer requests. Any cached data in stateless services (e.g., to serve fresh data that is not indexed yet) becomes inaccessible and is evicted upon the encryption service detecting loss of access to encryption keys.
Accessing the customer’s key
Customers using CMEK manage and control encryption keys that are used to encrypt/decrypt data in Pinecone by creating the key in their own AWS account. While we only support AWS KMS today, we are also looking to expand access to other environments.
Pinecone can access this key by assuming a role in your account that has access to the key. The
AssumeRole
operation is enabled by a trust policy in your account. This approach is a fairly standard way of setting up cross-account access in AWS environments, and can be configured with an optional external id that acts as a shared password between accounts for added security.
Key revocation experience
You can disable Pinecone’s access to your data by revoking Pinecone’s access to the key. This is by design and ensures that your data is inaccessible within minutes.
Following revocation, the longest your data will remain accessible is 15 minutes, which corresponds to the longest-lived in-memory cache. After this, Pinecone needs to re-decrypt data using your key. If you revoke Pinecone’s access to your key or disable it, then all Pinecone services will refuse to operate on the inaccessible index. Consequently, any queries/upserts you run on the index will result in a user error.
Hierarchical encryption with CMEK
To maintain high performance and strong security — and to enforce tenant isolation at multiple levels — Pinecone implements a system of hierarchical encryption that encrypts data without directly using the customer’s AWS key for every file.
Key Encryption Keys (KEKs)
In this system, each entity in Pinecone’s logical hierarchy — projects, indexes, and namespaces — is assigned a unique Key Encryption Key (KEK). In the hierarchy, each KEK:
is encrypted by its parent, and
is used to encrypt all of its child KEKs
Each of these KEKs is stored inside Pinecone’s KMS, which lives alongside the data plane in each data center. The root key encrypts project keys, and AWS manages this key to ensure that Pinecone never reveals it.
Crucially, no KEK is accessible outside of the KMS, and all KEKs are encrypted at rest. These measures ensure that:
KEKs never leave the KMS, and
Even in the event of a breach, they would not be accessible in decrypted form to any outside parties
Data Encryption Keys (DEKs)
The final key type is the blob key, which is a Data Encryption Key (DEK). DEKs are uniquely generated for each blob file generated by Pinecone for an index and are encrypted by the namespace key.
It’s worth highlighting that
they are the only encryption keys that leave the KMS
.
After encrypting a file, the DEK is wrapped by the namespace key and then stored alongside the original blob file for future decryption. When reading a blob file inside Pinecone, the DEK is sent to the encryption service for decryption by the namespace key. However, the namespace key is stored encrypted, so this also requires decryption of the index key (and thus the project key). Decrypting the index key requires that Pinecone have access to the customer-managed key,
which ensures that the blob file cannot be decrypted without the customer’s permission
.
This approach is far more complex than the simple alternative of requiring that each blob file be encrypted directly by the customer’s key — but the benefits are worth the effort:
We ensure that we only send encrypted keys to the Customer’s KMS instead of the blob files for encryption. This dramatically improves latencies and network IO costs.
The decrypted key material never leaves the KMS and is a fixed size — which ensures that the KEK wrap/unwrap process is consistent for any blob and all of the data encryption/decryption can happen inside the cluster
This allows us to support CMEK per index in the future and expand our offering.
Hierarchical encryption provides strong security while maintaining high-performance
Enabling more granular RBAC with API key roles
We’re pleased to announce expanded, more granular RBAC with the addition of
API key roles
. Together with our
User Roles
for Projects and Organizations, API key roles equip you with a more robust and flexible RBAC system to help you scale.
Understanding Pinecone API key roles
Assigning a role to an API key determines what permissions the associated user (or other entity) has in your Pinecone account, creating a comprehensive access control system that helps mitigate security risks, streamline operations, and manage resources more efficiently.
This new API key functionality includes six roles — three across our
control plane
(which handles requests to manage resources like indexes and API keys), and three across the
data plane
(which handles requests to write and read records in indexes).
Start building today
API Key Roles and CMEK are now available in public preview. CMEK is currently limited to AWS with support for Azure and GCP coming soon. AWS users can add an additional layer of security with Private Endpoints for AWS PrivateLink, which is now generally available (GA). Review our documentation to
configure CMEK
or
manage API keys
, and start building today!
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
