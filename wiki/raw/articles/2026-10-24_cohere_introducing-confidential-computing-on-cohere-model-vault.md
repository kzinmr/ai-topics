---
title: "Confidential Computing on Cohere Model Vault"
source: "Cohere Blog"
url: "https://cohere.com/blog/introducing-confidential-computing-on-cohere-model-vault"
scraped: "2026-10-24T06:01:00.676998+00:00"
lastmod: "2026-10-23"
type: "sitemap"
---

# Confidential Computing on Cohere Model Vault

**Source**: [https://cohere.com/blog/introducing-confidential-computing-on-cohere-model-vault](https://cohere.com/blog/introducing-confidential-computing-on-cohere-model-vault)

Key takeaways
Protect data in use:
Model Vault extends protection beyond data at rest and in transit to prompts, documents, responses, and model execution while inference is running.
Encrypt sensitive request contents end-to-end:
Application payloads remain encrypted through intermediary infrastructure and can only be decrypted inside the attested confidential environment.
Verify before you trust:
Customers can cryptographically verify the hardware and software environment before sensitive data leaves their infrastructure.
Use confidential AI as a managed service:
Cohere operates the serving platform on Microsoft Azure infrastructure with NVIDIA H100 GPU Confidential Computing capabilities.
Start today in public beta:
Customers can start deploying encrypted Model Vault workloads today.
Today, we are announcing the public beta of
Confidential Computing on Cohere Model Vault
, bringing hardware-backed protection and independently verifiable security to managed enterprise AI.
Model Vault gives enterprises dedicated, fully managed model inference. With Confidential Computing, we are extending that experience to some of an organization's most sensitive workloads and data, including financial information, clinical records, privileged documents, proprietary source code, and intellectual property.
The goal is simple: enterprises should be able to use the capabilities and operational simplicity of managed AI without giving the infrastructure that operates it access to their sensitive plaintext data.
Protecting data in use
Encryption traditionally protects data in two places: while it is stored and while it travels across a network.
Confidential Computing on Model Vault is designed to protect the third state:
data in use
.
Inference runs within a hardware-backed confidential environment spanning the CPU and GPU. Hardware-enforced isolation protects workload memory from everything outside the confidential boundary, including privileged infrastructure software and operators. With NVIDIA Confidential Computing, GPU memory is protected and traffic between the CPU and GPU is encrypted as the model performs inference.
This enables enterprises to bring more sensitive workloads to AI while reducing the number of parties and systems they need to trust with their data.
Verify before you trust
Protection alone is not enough. Enterprises also need a way to know that those protections are actually in place.
That is why remote attestation is a core part of Confidential Computing on Model Vault.
Before sensitive data is sent, customer-side software verifies cryptographically signed evidence about the environment that will process it, including its hardware, firmware, and software configuration. That evidence is checked against an approved security policy.
If the environment does not satisfy the policy, the client refuses to send the request.
This changes the trust model from
"trust us" to "verify it yourself."
“Enterprises should not have to choose between the simplicity of managed AI and control over their most sensitive information. With Model Vault and Confidential Computing, customers can verify the environment that will process their data before they send it. With hardware attestation, customers not only have cryptographic proof that workloads are running in a secure, confidential computing environment, they also can verify that their data is protected from unauthorized access, even from Cohere.”
- Phil Blunsom, CTO at Cohere
End-to-end protection for sensitive request contents
Confidential Computing protects what happens inside the compute environment. Model Vault also protects sensitive request contents on their way there.
Rather than relying only on connection-level encryption, Model Vault encrypts application payloads end-to-end to the attested confidential environment. The encrypted request can pass through intermediary infrastructure without exposing its contents, and only the confidential environment can decrypt it. Responses are protected on the return path as well.
This preserves the operational advantages of a managed AI platform without exposing the plaintext contents of customer requests to intermediary infrastructure.
Customers continue to use the Model Vault API and familiar request formats. The additional protection is built into the client and infrastructure layers rather than requiring applications to redesign their payloads.
Built with Microsoft Azure and NVIDIA
The public beta is powered by
NVIDIA H100 GPUs on Microsoft Azure
.
Microsoft Azure provides the underlying confidential computing infrastructure.and NVIDIA Confidential Computing extends those capabilities to the NVIDIA H100 GPUs. Cohere brings these technologies together through Model Vault's managed model serving, encrypted request path, remote attestation, and customer-side verification.
The result is a managed AI platform that combines the operational simplicity of cloud AI with stronger technical control over access to sensitive data during inference.
“Enterprises need confidence that their most sensitive AI workloads are protected by more than contractual promises. Our work with Cohere on Model Vault demonstrates how confidential computing can combine the simplicity of managed AI with independently verifiable technical controls.”
- Vikas Bhatia, Head of Product, Azure Confidential Computing at Microsoft
“Confidential Computing opens new possibilities for enterprises that need to run AI on highly sensitive data. NVIDIA Confidential Computing on NVIDIA GPUs provides hardware-backed protections that help platforms like Cohere Model Vault bring confidential AI inference to enterprise workloads.”
- John Fanelli, vice president, Enterprise Software at NVIDIA
Unlocking AI for sensitive enterprise workloads
For many organizations, the question is no longer whether AI can perform a task. The question is whether the data required for that task can safely be used with AI at all.
Confidential Computing on Model Vault is designed to protect workloads where security, contractual, or regulatory requirements may have kept valuable data outside managed AI platforms, including:
Fraud investigations in financial services
Privileged document search and due diligence in legal services
Sensitive public-sector information
Patent and research material
Proprietary engineering design documents (EDD), Interface design documents (IDD) and architecture materials
Search and analysis across proprietary source code
These are the kinds of workloads where reducing privileged infrastructure access and giving customers independently verifiable evidence can make previously restricted AI use cases practical.
Confidential computing does not eliminate all risk, nor does it replace application security, compliance, contractual controls, or data-residency requirements. It provides a hardware-enforced and verifiable protection boundary around data and computation while inference is taking place.
Available now in public beta
Confidential Computing on Cohere Model Vault is now available in public beta, powered by NVIDIA H100 GPUs on Microsoft Azure.
Customers can create and manage encrypted vaults through Model Vault and integrate them using the same Cohere APIs, with customer-side verification and end-to-end encryption protecting sensitive request contents before they leave the customer's environment.
For a deeper look at the confidential compute architecture, encrypted request path, remote attestation, trust boundary, and threat model, read
Inside Cohere Model Vault: Building Verifiable Confidential AI Inference
.
Get started at
vault.cohere.com
Blog
Written By
Alhassan Khedr
Manager of Technical Staff, Serving Inference Product
Tags
Product Launch
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
