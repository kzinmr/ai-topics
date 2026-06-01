---
title: "Introducing Anyscale on Kubernetes"
url: "https://anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s"
fetched_at: 2026-06-01T07:14:09.656074+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Introducing Anyscale on Kubernetes

Source: https://anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s

Anyscale has expanded its capabilities with Kubernetes support, allowing users to integrate distributed AI workloads into their existing Kubernetes-managed infrastructure. This update addresses the growing demand for flexibility, control, and seamless integration with the tools and environments users already have in place for machine learning and AI tasks.
Link
Background
Historically, Anyscale’s platform operated on a virtual machine (VM)-based architecture on top of Amazon EC2 and Google GCE, offering robust scalability for users interested in adopting Anyscale's specific infrastructure setup. While this has worked well for many teams, Kubernetes-focused users sought deeper integration with their existing clusters to meet their infrastructure management standards. To meet this need, we are thrilled to introduce the Anyscale Operator for Kubernetes, providing access to our high-performance unified AI compute platform.
Link
Architecture
Anyscale has developed a scalable, reliable, and secure control plane and data plane architecture to manage Ray clusters across accounts, cloud providers, on-premises machines, and now Kubernetes.
Control Plane
: The control plane is designed to be horizontally scalable to handle concurrent Ray clusters that span millions of CPU cores and GPUs. It offers a comprehensive console and API for workload scheduling, resource optimization, and monitoring across customer data planes.
Data Plane:
The customer data plane comprises one or more deployments of Anyscale called Clouds. Anyscale Clouds are mapped to a deployment mode on Virtual Machines, Kubernetes, or on Anyscale managed compute. Ray clusters within these Clouds run within the customer data plane and have access to any resources explicitly granted to the Ray clusters, enabling customers to deploy clusters securely within their infrastructure while maintaining control over the data required for machine learning tasks.
Link
Managing Ray Clusters on Kubernetes
Before the Anyscale Operator for Kubernetes, Ray users relied on the open-source KubeRay operator to run jobs and services on Kubernetes clusters. While KubeRay offers simplicity and minimal dependencies, it lacks the security, reliability, performance optimizations, and suite of developer tools available on Anyscale.
To bridge this gap, we developed the
Anyscale Operator for Kubernetes
, an operator that connects the Anyscale control plane with
customer-managed
Kubernetes clusters. Deployed in a dedicated namespace, the Anyscale Operator translates user actions from the Anyscale UI or APIs into Kubernetes operations, allowing seamless pod and services management. The Anyscale Operator supports all Anyscale optimizations and can be customized for specific setups using our Patch API.
Link
Key Benefits
Unified ML Platform:
Anyscale on Kubernetes inherits all the security, governance, and observability tools available in
Anyscale’s platform
.
Leverage Existing Infrastructure:
Anyscale integrates directly with your Kubernetes clusters, enabling your organization to maintain existing tooling and governance systems
Cost Optimization:
With support for spot instances and resource prioritization, you can optimize cloud costs for high-demand AI workloads.
Custom Pod Definitions:
Define resource allocations for different shapes of resources, including custom CPU, memory, and GPU configurations.
Integrated Monitoring and Logging:
Built-in observability tools allow you to monitor logs, job performance, and resource consumption directly through your Kubernetes environment.
Link
Comparing the Anyscale Operator for Kubernetes vs. Kuberay
Link
Deployment and Cloud Provider Support
The Anyscale Operator for Kubernetes offers integrated support for almost all Kubernetes clusters, streamlining cloud management and simplifying scaling and can be enhanced by deploying alongside other resources like object storage and network file systems. KubeRay, as a cloud-agnostic framework, requires more manual setup.
Link
Customization and Support
Anyscale’s Patch API allows for rapid customization and deployment, while KubeRay, though fully customizable, demands more configuration and maintenance.
Link
Observability
Anyscale provides enhanced observability with proprietary dashboards. KubeRay offers more basic functionality in these areas.
Link
Workload Management
Anyscale extends job management with job queues, automatic retries, and advanced service rollouts in addition to a number of other enhancements, while KubeRay provides more basic features.
Link
Usability and Security
Anyscale enhances usability with features like improved logging, reusable configurations, and integrated consoles, along with robust security features such as user management, authentication, and audit logs. KubeRay lacks these enterprise-grade tools out of the box.
Link
Performance Optimizations
Anyscale offers an optimized version of Ray called
RayTurbo
to bolster performance including improved scalability, speed, and cost efficiency.  Learn more HERE
Link
Launch Partners
We are thrilled to share our key launch partners for the Anyscale Operator for Kubernetes:
Thank you so much to these launch partners for their support. Any customer of these cloud Kubernetes offerings can now run on Anyscale seamlessly.
Link
Conclusion
Anyscale’s integration with Kubernetes offers a seamless, powerful solution for managing AI workloads on user-managed infrastructure. By leveraging your existing Kubernetes clusters, you can maintain your preferred environment while benefiting from Anyscale’s enhanced performance, security, and usability features. Whether you're scaling AI workloads or optimizing costs, Anyscale on Kubernetes is a robust, enterprise-ready platform that simplifies complex machine learning operations.
Ready to take your AI infrastructure to the next level? Get started with Anyscale on Kubernetes today!
Book a Demo →
