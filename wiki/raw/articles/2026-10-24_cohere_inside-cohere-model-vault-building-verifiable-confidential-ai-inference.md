---
title: "Cohere Model Vault: Verifiable Confidential AI Inference"
source: "Cohere Blog"
url: "https://cohere.com/blog/inside-cohere-model-vault-building-verifiable-confidential-ai-inference"
scraped: "2026-10-24T06:00:59.175766+00:00"
lastmod: "2026-10-22"
type: "sitemap"
---

# Cohere Model Vault: Verifiable Confidential AI Inference

**Source**: [https://cohere.com/blog/inside-cohere-model-vault-building-verifiable-confidential-ai-inference](https://cohere.com/blog/inside-cohere-model-vault-building-verifiable-confidential-ai-inference)

In our product launch, we introduced
Confidential Computing on Cohere Model Vault
, now in public beta with NVIDIA GPUs on Microsoft Azure.
This article goes deeper into how the system works.
The goal is not simply to encrypt inference. It is to reduce the infrastructure that customers must trust with plaintext data and give them cryptographic evidence they can verify before sensitive information is released.
That requires more than a confidential virtual machine. A confidential inference system has to protect the computation itself, the path that carries sensitive requests to it, and the mechanism customers use to decide whether the destination can be trusted.
Model Vault brings those pieces together around a dedicated model deployment.
From confidential hardware to confidential inference
Confidential computing protects
data in use
, while an application or model is actively processing it.
At the foundation are two properties:
Isolation
, which uses hardware-enforced controls to protect workload memory from infrastructure outside the confidential environment.
Attestation
, which produces cryptographically signed evidence about the environment so another party can evaluate it before releasing sensitive data.
Together, these properties change the traditional infrastructure trust model. Privileged access to the underlying host no longer automatically implies access to the workload running inside the confidential environment.
For AI inference, however, the boundary cannot end at the CPU.
A substantial portion of model computation runs on accelerators. If the CPU were protected while the accelerator remained outside the confidential boundary, sensitive model state and intermediate computation could become exposed at the point where inference moves to the GPU.
Confidential Computing on NVIDIA GPUs protects GPU memory from infrastructure outside the protected environment and encrypts communication between the CPU and GPU. This allows the confidential boundary to span the confidential virtual machine with the accelerator performing inference.
Inside a confidential Model Vault
No single component makes an inference request confidential.
Model Vault combines several controls around a dedicated model deployment, each addressing a different part of the trust problem.
Confidential CPU and GPU execution
The model-serving stack runs inside a confidential virtual machine.
The operating system, drivers, inference server, and their memory are protected from the host environment through hardware-backed isolation. The workload is also constrained by policy so that only approved software can run inside the environment and operators do not have an interactive path into the workload.
The NVIDIA Confidential Computing extends protection to the accelerator and encrypts traffic between the CPU and GPU.
This matters because the security boundary needs to cover the systems actually performing the inference, not only the CPU coordinating it.
Microsoft Azure provides the underlying confidential computing infrastructure. Model Vault builds the managed model-serving, encrypted request, attestation, and customer-verification layers around that foundation.
The result is that customers do not need to assemble, integrate, and operate these controls independently.
Encrypting the request itself
Protecting the compute environment solves only part of the problem.
Sensitive data also has to reach that environment.
TLS protects network connections, but connection-level encryption alone does not guarantee that every intermediary involved in operating a service remains outside the plaintext path.
Model Vault therefore protects the
application payload itself
.
It uses
Oblivious HTTP, or OHTTP
, to encrypt sensitive request contents to a public key associated with the attested confidential environment. The encrypted message can then pass through intermediary infrastructure as ciphertext.
Only the OHTTP gateway inside the confidential environment has access to the corresponding private key and can decrypt the protected request. The response is protected on the return path in the same way.
This creates an important separation between
operating the service
and
accessing the contents of the request
.
Intermediary infrastructure can still perform functions required by a managed platform, such as routing traffic, without needing access to the sensitive application payload.
Applications continue to use the Model Vault API and familiar request formats. The additional protection is implemented in the client and infrastructure layers rather than requiring customers to redesign their application payloads.
Remote attestation: proving what will process the request
Isolation prevents infrastructure outside the confidential boundary from directly reading protected workload memory.
But isolation alone still leaves an important question:
How does the customer know that the destination is actually running the hardware and software configuration it expects?
Remote attestation addresses that question.
The confidential environment produces cryptographically signed evidence describing the environment that is running. This includes measurements and security-relevant properties associated with the hardware, firmware, operating environment, and application software.
That evidence is then evaluated against an approved policy.
This separation between
evidence
and
policy
is fundamental.
Attestation evidence answers:
What environment is actually running?
The policy answers:
Is this an environment I am willing to trust with my data?
A verifier can require that specific properties match approved values before a protected request is released.
Those requirements can include the expected software measurements and security state of the confidential environment, including whether the GPU is operating in the expected confidential mode.
The customer therefore does not need to rely solely on Cohere's assertion that a particular environment is trustworthy. Verification is performed before sensitive data is released.
Attestation as an enforcement mechanism
Attestation matters most when it changes what the system does.
In Model Vault, verification is part of the decision about whether protected data is released at all.
Before sending a protected request, the client evaluates the destination against the approved policy.
If an expected property is missing or incorrect, for example because a software measurement has changed or the GPU is not operating in the required confidential mode, verification fails and the client refuses to send the protected payload.
The sensitive request therefore remains inside the customer's environment rather than being sent to a destination that did not satisfy verification.
This turns attestation from an audit artifact into an
active security control
.
Attestation evidence is renewed frequently. Each time it is refreshed, the client verifies the new measurements and security state against the approved policy before continuing to send protected requests.
This is the practical meaning of
verify before you trust
.
The trust boundary and threat model
Confidential computing reduces the amount of infrastructure that must be trusted with plaintext data.
It does not eliminate trust entirely.
Understanding the remaining trust boundary is therefore as important as understanding the protections themselves.
What remains trusted
Several components remain part of the trusted computing base, including:
the underlying confidential computing hardware
firmware
measured software running inside the confidential environment
the reference measurements used to define an approved configuration
the attestation infrastructure used to evaluate and sign evidence
The important difference is that this trust can be made more explicit and measurable.
Hardware produces evidence about the environment, while customer-controlled verification checks that evidence against approved values before protected data is released.
The system therefore replaces some forms of broad, implicit infrastructure trust with a smaller set of components whose state can be measured and evaluated.
What is protected
Within its threat model, Confidential Computing on Model Vault protects prompts, documents, responses, and model execution while they are being processed.
Intermediaries outside the confidential environment, including the host operating system, hypervisor, infrastructure administrators, cloud provider, and Cohere operators, are prevented from reading protected workload memory.
Because sensitive application payloads are encrypted end-to-end to the confidential environment, their contents also remain protected while crossing intermediary infrastructure.
The protection therefore spans both:
the path carrying sensitive request contents to the confidential environment
the environment performing the inference
That distinction matters. A confidential execution environment alone would not prevent plaintext exposure elsewhere in the request path.
What remains outside the protection boundary
A useful threat model also needs to state what it does
not
protect.
Confidential computing does not claim to prevent every possible attack.
Physical and side-channel attacks
Some physical and side-channel attacks remain outside the protection boundary. For example, an attacker may be able to infer information indirectly from timing or other shared hardware behavior, even without directly reading protected memory.
Availability
An operator that cannot read a protected workload may still be able to stop it, delay it, or prevent it from running.
Confidential computing therefore does not prevent denial-of-service attacks or provide availability guarantees by itself.
Application-level vulnerabilities
Software running inside the confidential environment still needs to be secure.
Prompt injection, insecure tool use, authorization errors, application vulnerabilities, and other software-level risks are not solved simply by placing the application inside confidential computing hardware.
Observable metadata
The contents of protected application payloads are encrypted, but some information remains visible outside that payload.
This can include:
request timing
message size
traffic volume
routing information
In the current architecture, information required for authentication and routing, including the API credential and model identifier, also remains outside the OHTTP-protected application payload.
That distinction is intentional and important when reasoning about what the system hides and what it does not.
What confidential computing is not
Confidential computing is one security control within a broader architecture.
It is not:
A replacement for application security.
Software inside the confidential boundary still needs to be designed, reviewed, and secured correctly.
A data-residency mechanism.
Confidential computing governs access to data during computation. It does not determine the jurisdiction in which that computation occurs.
A replacement for compliance or contractual controls.
DPAs, access controls, certifications, security reviews, and legal obligations remain necessary.
Homomorphic encryption.
The model still operates on plaintext inside the protected environment. Confidential computing protects that environment rather than computing directly over encrypted values.
Attestation also provides assurance only when signed evidence is actually validated against an appropriate policy.
Evidence describes what is running.
Policy determines whether that environment should be trusted.
Confidential computing does not eliminate trust.
It makes trust smaller, explicit, measurable, and verifiable.
Built in the open
Verification becomes more meaningful when customers and security researchers can understand what they are verifying.
Confidential Computing on Model Vault builds on open-source technologies including
Kata Containers
and
Confidential Containers
.
Cohere intends to open-source the confidential inference stack so that customers and researchers can inspect the implementation, understand the policies being enforced, and reproduce the measurements used during verification.
This matters because attestation should not require customers to accept another black box.
A measurement is more useful when customers can understand what was measured, inspect the code associated with it, and independently reason about whether that state should be trusted.
Open implementation and reproducible measurements make the verification process more transparent and give security teams the ability to evaluate the system at a deeper level.
What's next
The current public beta runs on
NVIDIA H100 GPUs on Microsoft Azure
.
We are also working toward support for
NVIDIA Blackwell infrastructure, including NVIDIA B200 GPUs
, as we move toward general availability.
Confidential Computing on Model Vault is part of a broader goal: making strong technical controls available to enterprises without requiring every organization to build and operate confidential AI inference itself.
The objective is not to ask customers to trust more infrastructure or managed platforms.
It is to give them a way to verify the platforms and infrastructure partners they choose to trust.
Learn more in the
Confidential Computing on Model Vault product announcement
, explore the
Model Vault documentation
, or get started at
vault.cohere.com
.
Blog
Written By
Alhassan Khedr
Manager of Technical Staff, Serving Inference Product
Tags
Technology
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
