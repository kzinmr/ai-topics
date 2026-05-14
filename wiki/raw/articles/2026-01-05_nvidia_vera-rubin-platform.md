---
title: "Inside the NVIDIA Vera Rubin Platform: Six New Chips, One AI Supercomputer"
date_published: 2026-01-05
date_updated: 2026-03-16
source: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
type: article
author: Kyle Aubrey
---

Inside the NVIDIA Vera Rubin Platform: Six New Chips, One AI Supercomputer | NVIDIA Technical Blog 
	
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 DEVELOPER 
 
 
 
 Home Blog Forums Docs Downloads Training 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Join
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Technical Blog 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Subscribe
 
 
 
 
 
 
 

 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 Related Resources 
 
 
 
 
 
 
 
 
 
 Data Center / Cloud 
 

 
 
 
 English 日本語 中文 
 
 

 Inside the NVIDIA Vera Rubin Platform: Six New Chips, One AI Supercomputer 

 
 
 
 
 Jan 05, 2026
 

 
 By Kyle Aubrey 

 
 
 
	
 
 Like
 
 

 
 
 Discuss (2)
 
 
 
 

 
 
 

 
 
 L 
 T 
 F 
 R 
 E 
 

 
 
 Update March 16, 2026: The NVIDIA Vera Rubin platform now has a seventh chip. Learn more about NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform . 

 AI has entered an industrial phase. 

 What began as systems performing discrete AI model training and human-facing inference has evolved into always-on AI factories that continuously convert power, silicon, and data into intelligence at scale. These factories now underpin applications that generate business plans, analyze markets, conduct deep research, and reason across vast bodies of knowledge. 

 To deliver these capabilities at scale, next generation AI factories must process hundreds of thousands of input tokens to provide the long-context required for agentic reasoning, complex workflows, and multimodal pipelines, while sustaining real-time inference under constraints on power, reliability, security, deployment velocity, and cost. 

 The NVIDIA Vera Rubin platform was designed specifically for this new reality. 

 Extreme co-design is the foundation of the Vera Rubin platform.&nbsp;GPUs, CPUs, networking, security, software, power delivery, and cooling are architected together as a single system rather than optimized in isolation. By doing so, the Vera Rubin platform treats the data center, not a single GPU server, as the unit of compute. This approach establishes a new foundation for producing intelligence efficiently, securely, and predictably at scale. It ensures that performance and efficiency hold up in production deployments, not just isolated component benchmarks. 

 This technical deep dive explains why AI factories demand a new architectural approach; how NVIDIA Vera Rubin NVL72 functions as a rack-scale architecture; and how the Vera Rubin platform’s silicon, software, and systems translate into sustained performance and lower cost per token at scale. 

 The blog is organized as follows: 

 
 Why AI factories need a new platform : The shift to reasoning-driven, always-on AI and the constraints that now define scale: power, reliability, security, and speed of deployment. 

 Meet the NVIDIA Vera Rubin platform : The rack-scale platform thesis and the core breakthroughs that enable sustained intelligence production. 

 Six new chips, one AI supercomputer : The six-chip architecture and how GPUs, CPUs, networking, and infrastructure operate as one tightly integrated system. 

 From chips to systems: NVIDIA Vera Rubin superchip to DGX SuperPOD : How Vera Rubin scales from superchips to racks to NVIDIA DGX SuperPOD-scale AI factory deployments. 

 Software and developer experience : The software stack that makes rack-scale programmable, from NVIDIA CUDA and NVIDIA CUDA-X to training and inference frameworks. 

 Operating at AI factory scale : The production foundations: operations, reliability, security, energy efficiency, and ecosystem readiness. 

 Performance and efficiency at scale : How Vera Rubin converts architecture into real gains at scale, including one-fourth as many GPUs to train, 10x higher inference throughput, and 10x lower cost per token. 

 Why Vera Rubin is the AI factory platform : How extreme co-design delivers predictable performance, economics, and scalability in real deployments. 
 

 1. Why AI factories need a new platform 

 AI factories differ fundamentally from traditional data centers. Rather than serving intermittent, human-driven requests, they function as always-on intelligence production systems, where efficiency in reasoning, context handling, and data movement, not just the peak compute of a server, determines performance. 

 Modern AI workloads increasingly rely on reasoning and agentic models that execute multi-step inference over extremely long contexts. These workloads simultaneously stress every layer of the platform: delivered compute performance, GPU-to-GPU communication, interconnect latency, memory bandwidth and capacity, utilization efficiency, and power delivery. Even small inefficiencies, when multiplied across trillions of tokens, undermine optimal cost, throughput, and competitiveness. 

 This dynamic is captured by three scaling laws driving AI progress: 

 
 Pre-training scaling: where models learn their inherent knowledge 

 Post-training scaling: where models learn to think through fine-tuning and reinforcement 

 Test-time scaling: where models reason by generating more tokens during inference 
 

 
 
 
 
 
 Figure 1. Three scaling laws and exponential growth of compute 

 As these scaling laws compound, infrastructure requirements intensify. NVIDIA Blackwell NVL72 was the first rack-scale architecture, freeing GPUs, CPUs, and interconnects from the confines of the traditional server boundary and elevating the rack to the primary unit of integration. This shift enabled major advances in scale-up bandwidth, efficiency, and deployability, and underpins many of today’s largest AI deployments. 

 As AI factories are pushed to deliver more intelligence, lower cost per token, and greater business impact, there is relentless demand to extend rack-scale performance while maintaining data-center-scale determinism within tightly constrained power and cooling limits. 

 2. Meet the NVIDIA Vera Rubin platform 

 The NVIDIA Vera Rubin platform was designed for the shift in how intelligence is produced at scale, applying extreme co-design across compute, networking, power delivery, cooling, and system architecture to enable sustained intelligence production at AI factory scale. 

 At the platform level, Vera Rubin delivers five generational breakthroughs: 

 
 
 
 
 
 Figure 2. Vera Rubin platform-level breakthroughs enabled by extreme co-design 

 Together, these capabilities allow Rubin-based systems to behave as predictable, secure, continuously available units of intelligence production rather than collections of independent components. 

 The flagship of the Vera Rubin platform is the Vera Rubin NVL72 rack-scale system, engineered so that the entire rack operates as one rack-scale accelerator within a larger AI factory. The NVL72 system is optimized not just for peak performance, but for sustained intelligence production: predictable latency, high utilization across heterogeneous execution phases, and efficient conversion of power into usable intelligence. 

 
 
 
 
 
 Figure 3. Vera Rubin NVL72 overview 

 workloads. 

 To help visualize how the Vera Rubin platform comes together as a unified system, the following video provides an overview of the rack-scale architecture and how each major component plays in sustained intelligence production. 

 
 
 Video 1. NVIDIA Vera Rubin platform overview video 

 This system-level overview sets the foundation for understanding how the Vera Rubin platform’s chips have been architected to operate as one AI supercomputer. 

 3. Six new chips, one AI supercomputer 

 Extreme co-design is expressed most clearly at the chip level. 

 The Vera Rubin platform is built from six new chips, each engineered for a specific role in the AI factory and designed from the outset to operate as part of a unified rack-scale system. Rather than treating compute, networking, and infrastructure as loosely coupled layers, Vera Rubin integrates them directly into the architecture. It ensures that communication, coordination, security, and efficiency are first-class design considerations. 

 
 
 
 
 
 Figure 4. NVIDIA Vera Rubin platform chips 

 The six new chips are: 

 
 NVIDIA Vera CPU : 88 NVIDIA custom-designed Olympus cores optimized for the next generation of AI factories with full Arm-compatibility.&nbsp; 

 NVIDIA Rubin GPU : High-performance AI compute with HBM4 and new NVIDIA Transformer Engine. 

 NVIDIA NVLink 6 switch : Sixth-generation scale-up fabric delivering 3.6 TB/s GPU-to-GPU bandwidth. 

 NVIDIA ConnectX-9 : High-throughput, low-latency networking interface at the endpoint for scale-out AI. 

 NVIDIA BlueField-4 data processing unit (DPU) : A dual-die package combining:
 
 A 64-core NVIDIA Grace CPU for infrastructure offload and security. 

 An integrated NVIDIA ConnectX-9 high-speed networking chip for tightly coupled data movement. 
 
 

 NVIDIA Spectrum-6 Ethernet switch : Scale-out connectivity using co-packaged optics for efficiency and reliability. 
 

 Together, these chips form a synchronized architecture in which GPUs execute transformer-era workloads, CPUs orchestrate data and control flow, scale-up and scale-out fabrics move tokens and state efficiently, and dedicated infrastructure processors operate and secure the AI factory itself. 

 In the sections that follow, we examine each of these building blocks in detail, starting with the Vera CPU, which orchestrates data movement, memory, and control flow to sustain GPU utilization at AI factory scale. 

 Vera CPU: Purpose-built for AI factories 

 As AI factories scale, GPU performance alone is no longer sufficient to sustain throughput. High utilization across thousands of GPUs depends on how efficiently data, memory, and control flow through the system. The Vera CPU is designed specifically for this role, acting as the high-bandwidth, low-latency data movement engine that keeps AI factories operating efficiently at scale. 

 Rather than functioning as a traditional general-purpose host, Vera is optimized for orchestration, data movement, and coherent memory access across the rack. Paired with Rubin GPUs as a host CPU, or deployed as a standalone platform for agentic processing, Vera enables higher sustained utilization by removing CPU-side bottlenecks that emerge in training and inferencing environments. 

 
 
 
 
 
 Figure 5. Vera CPU with NVIDIA-built custom cores 

 From NVIDIA Grace to Vera—scaling the CPU for AI factories 

 NVIDIA Grace established NVIDIA’s approach to high-bandwidth, energy-efficient CPU design. Vera extends that foundation with increased core density, significantly higher memory bandwidth, expanded coherency, and full confidential computing support, all tailored for AI factory workloads. 

 As shown in the table below, Vera delivers 2.4x higher memory bandwidth and 3x greater memory capacity to support data-intensive workloads, while doubling NVLink-C2C bandwidth to sustain coherent CPU–GPU operation at rack scale. Together, these advances elevate the CPU from a supporting role to a key enabler of next-generation GPU efficiency in AI factories. 

 Feature Grace CPU Vera CPU Cores 72 Neoverse V2 cores&nbsp; 88 NVIDIA Custom Olympus cores Threads 72 176&nbsp;Spatial Multithreading&nbsp; L2 Cache per core 1 MB 2 MB Unified L3 Cache&nbsp; 114 MB 164 MB Memory bandwidth (BW) Up to 512GB/s Up to 1.2TB/s Memory capacity Up to 480GB LPDDR5X Up to 1.5TB LPDDR5X SIMD 4x 128b SVE2 6x 128b SVE2&nbsp;FP8 NVLINK-C2C 900 GB/s 1.8 TB/s PCIe/CXL Gen5 Gen6/CXL 3.1 Confidential compute NA Supported Table 1. Grace vs. Vera CPU comparison 

 NVIDIA Olympus core with Spatial Multithreading 

 At the heart of the Vera CPU are 88 NVIDIA custom Olympus cores, designed for high single-thread performance and energy efficiency with full Arm-compatibility. The cores employ a wide, deep microarchitecture with improved branch prediction, prefetching, and load-store performance, optimized for control-heavy and data-movement-intensive workloads. 

 Vera introduces Spatial Multithreading, a new type of multithreading that runs two hardware threads per core by physically partitioning resources instead of time-slicing, enabling a run-time tradeoff between performance and efficiency. This approach increases throughput and virtual CPU density while maintaining predictable performance and strong isolation, a critical requirement for multi-tenant AI factories 

 Scalable Coherency Fabric—deterministic data movement 

 The second-generation NVIDIA Scalable Coherency Fabric (SCF) connects all 88 Olympus cores to a shared L3&nbsp; cache and memory subsystem on a single monolithic compute die. By avoiding chiplet boundaries, SCF delivers consistent latency and sustains over 90% of peak memory bandwidth under load, eliminating bottlenecks between cores and memory controllers. 

 By providing deterministic, high-throughput data movement across the CPU, SCF ensures that orchestration and data-processing workloads scale linearly as core count increases. This is essential for keeping GPUs fed with data and commands at AI factory scale. 

 Memory bandwidth and coherent execution 

 Vera pairs SCF with up to 1.5TB of LPDDR5X memory subsystem, delivering up to 1.2 TB/s of bandwidth at low power. Small Outline Compression Attached Memory Modules (SOCAMM) with LPDDR5X improve serviceability and fault isolation, improving AI factory uptime requirements. 

 Second-generation NVLink-C2C provides 1.8 TB/s of coherent bandwidth between Vera CPUs and Rubin GPUs, enabling a unified address space across CPU and GPU memory. Applications can treat LPDDR5X and HBM4 as a single coherent pool, reducing data movement overhead and enabling techniques such as KV-cache offload and efficient multi-model execution. 

 
 
 
 
 
 Figure 6. NVLink-C2C coherent memory architecture 

 Software compatibility and secure operation&nbsp; 

 Vera supports the Arm v9.2 architecture and integrates seamlessly with the Arm software ecosystem. Major Linux distributions, AI frameworks, and orchestration platforms run unmodified, allowing existing infrastructure software to scale onto Vera-based systems without disruption. 

 Confidential computing is supported natively, enabling secure execution across CPU–GPU boundaries and across multi-socket configurations while preserving performance. 

 The data engine for AI factories 

 Vera is a purpose-built CPU engineered to keep GPUs fully utilized by efficiently moving, processing, and coordinating data at AI factory scale. Rather than acting as a passive host, Vera functions as a data engine that accelerates control-heavy and communication-intensive paths, including data staging, scheduling, orchestration, and agentic workflows. It also delivers exceptional standalone performance for analytics, cloud, storage, and infrastructure services. 

 By combining Olympus CPU cores, second-generation SCF, high-bandwidth LPDDR5X memory, and coherent NVLink-C2C connectivity, Vera ensures Rubin GPUs remain productive across training, post-training, and inference workloads, even as execution shifts between compute, memory, and communication-dominated phases. 

 In the next section, we examine the Rubin GPU, the execution engine that transforms this rack-scale accelerator foundation into sustained training and inference performance. 

 Rubin GPU: Execution engine for transformer-era AI 

 With the Vera CPU providing the orchestration and data-movement foundation, the Rubin GPU serves as the execution engine that turns rack-scale capability into intelligence. It is designed for continuous training, post-training, and inference in always-on AI factories. 

 Modern AI workloads—including reasoning, mixture-of-experts (MoE), long-context inference, and reinforcement learning—are not limited by peak floating point operations (FLOPS) alone. They are constrained by whether execution efficiency can be sustained across compute, memory, and communication. The Rubin GPU is purpose-built for this reality, optimizing the full execution path that turns power, bandwidth, and memory into tokens at scale. 

 To sustain throughput under these conditions, the Rubin GPU advances its architecture across three tightly coupled dimensions: compute density, memory bandwidth, and rack-scale communication. 

 
 
 
 
 
 Figure 7. Rubin GPU 

 At the silicon level, Rubin builds on NVIDIA’s proven GPU foundation while scaling every critical subsystem for transformer-era workloads. The GPU integrates 224 Streaming Multiprocessors (SMs) equipped with fifth-generation Tensor Cores optimized for low-precision NVFP4 and FP8 execution. These Tensor Cores are tightly coupled with expanded Special Function Units (SFUs) and execution pipelines designed to accelerate attention, activation, and sparse compute paths common in modern AI models. 

 Building on NVIDIA Blackwell, Rubin extends NVIDIA’s extreme hardware–software co-design to deliver higher sustained throughput and lower cost per token across training, post-training, and inference workloads. Improved NVFP4 support increases arithmetic density and efficiency, allowing more useful computation per watt while maintaining model accuracy. By integrating low-precision execution deeply into both the architecture and software stack, Rubin translates advances in numerical formats directly into real-world gains in throughput, utilization, and AI factory economics. 

 Across the full device, Rubin delivers a step-function increase in sustained throughput across pre-training, post-training, and inference. By increasing scale-up bandwidth, improving collective efficiency, and sustaining higher utilization under communication-heavy execution, Rubin raises the effective performance ceiling for large-scale training while delivering significant gains in post-training and inference workflows. 

 Sustained compute and execution scaling 

 Rubin scales compute capability, Transformer Engine support, and execution balance together to avoid the utilization cliffs that limit real-world throughput. 

 The table below highlights how core compute characteristics have evolved since Blackwell. Additional Rubin compute specifications can be found on the Vera Rubin NVL72 product page. 

 Feature Blackwell Rubin Transistors (full chip) 208B 336B Compute dies 2 2 NVFP4 inference (PFLOPS) 10 50* NVFP4 training (PFLOPS) 10 35** Softmax acceleration&nbsp;(SFU EX2 Ops/Clk/SM for FP32 | FP16) 16 32 | 64 Table 2. NVIDIA GPU compute capability comparison * Transformer Engine compute ** Dense compute 

 Converging AI and scientific computing 

 The launch of the NVIDIA Vera Rubin platform marks a new phase in scientific computing, where AI and simulation increasingly reinforce one another. In many supercomputing environments today, simulations are treated as endpoints—computationally intensive runs that produce a single result. Increasingly, high-fidelity simulations are also used as engines for dataset generation, producing training data for AI models that augment traditional solvers. 

 These AI models can act as intelligent pre-conditioners, accelerate convergence, or serve as fast surrogate models in iterative workflows. While AI surrogates can deliver dramatic speedups—sometimes with reduced precision—classical simulation remains essential for establishing ground truth and final validation. The result is a converging workload profile that demands strong performance across both AI and scientific computing. 

 The table below compares the FP32 and FP64 compute capability of the NVIDIA Hopper, Blackwell, and Rubin GPUs.&nbsp; 

 Feature Hopper GPU Blackwell GPU Rubin GPU FP32 vector (TFLOPS) 67 80 130 FP32 matrix (TFLOPS) 67 227* 400* FP64 vector (TFLOPS) 34 40 33 FP64 matrix (TFLOPS) 67 150* 200* Table 3. NVIDIA GPU FP32 and FP64 compute capability. *Peak performance using Tensor Core-based emulation algorithms 

 The matrix performance shown above is achieved through a combination of architectural enhancements and software techniques that deliver higher effective throughput relative to prior generations. This reflects NVIDIA’s continued focus on application-level performance rather than isolated peak metrics. 

 Across both AI and scientific computing, the NVIDIA extreme co-design philosophy prioritizes sustained performance on real workloads. Analysis of production simulation codes shows that the highest sustained FP64 performance often comes from matrix-multiply kernels. Hopper used dedicated hardware to accelerate these paths. With Blackwell and now Rubin, NVIDIA has evolved this strategy, achieving high FP64 matrix throughput via multiple passes over lower-precision tensor cores while preserving architectural flexibility for converged workloads. More information on how Ozaki FP64 emulation is an effective way to achieve true FP64-level accuracy on low-precision AI hardware while delivering impressive performance gains can be found in our blog on Unlocking Tensor Core Performance with Floating Point Emulation in cuBLAS . 

 At the same time, dedicated FP64 vector performance remains critical for scientific applications that are not dominated by matrix kernels. In these cases, performance is constrained by data movement through registers, caches, and high-bandwidth memory (HBM) rather than raw compute. A balanced GPU design therefore provisions sufficient FP64 resources to saturate available memory bandwidth, avoiding over-allocation of compute capacity that cannot be effectively utilized. 

 With the Vera Rubin platform, real application performance continues to improve each generation. The figure below shows projected gains across representative high-performance computing (HPC) simulation codes, driven by architectural and system-level improvements rather than increases in raw FP64 vector throughput. 

 
 
 
 
 
 Figure 8. NVIDIA GPU simulation performance 

 Transformer Engine 

 The third-generation NVIDIA Transformer Engine builds upon the prior innovations with new hardware-accelerated adaptive compression designed to boost NVFP4 performance while preserving accuracy. This capability enables up to 50 PetaFLOPS NVFP4 for inference&nbsp;&nbsp; 

 Fully compatible with Blackwell GPUs, the new Transformer Engine preserves the existing programming model, allowing previously optimized code to transition seamlessly to Rubin while automatically benefiting from higher arithmetic density and improved execution efficiency. 

 Memory and decode efficiency 

 As context lengths grow and inference becomes increasingly interactive, achieved memory performance becomes a dominant factor in overall efficiency. The Rubin GPU incorporates a new generation of high-bandwidth memory, HBM4, which doubles interface width compared to HBM3e.&nbsp; 

 Through new memory controllers, deep co-engineering with the memory ecosystem, and tighter compute-memory integration, the Rubin GPU nearly triples memory bandwidth compared to Blackwell. 

 Key characteristics include: 

 
 Up to 288 GB of HBM4 per GPU 

 Aggregate bandwidth of up to 22 TB/s 

 Improved decode and front-end efficiency to keep execution pipelines fed under load 
 

 
 
 
 
 
 Figure 9. HBM bandwidth scaling across GPU generations 

 Together, these advances enable the Rubin GPU to sustain long-context inference, high-batch MoE execution, and interactive reasoning without sacrificing concurrency or utilization. 

 Scale-up interconnect—built for communication-dominated AI 

 The Vera Rubin platform supports sixth-generation NVIDIA NVLink (NVLink 6) for GPU-to-GPU communication within the system, NVIDIA NVLink-C2C (chip-to-chip) for coherent CPU-GPU connectivity with Vera CPUs, and PCIe Gen6 for host and device integration. 

 NVIDIA NVLink 6 delivers 3.6 TB/s of bidirectional GPU-to-GPU bandwidth per GPU, doubling scale-up bandwidth over the prior generation. Within an NVL72 system, this enables all-to-all communication across 72 GPUs with predictable latency, a critical requirement for MoE routing, collectives, and synchronization-heavy inference paths. 

 By eliminating scale-up bottlenecks, the Rubin GPU ensures that communication does not cap utilization as model size, expert count, and reasoning depth increase. 

 The table below compares GPU interconnect bandwidth from Blackwell to Rubin. 

 Interconnect Blackwell Rubin NVLink (GPU-GPU)(GB/s, bi-directional) 1,800 3,600 NVLink-C2C (CPU-GPU)(GB/s, bi-directional) 900 1,800 PCIe Interface(GB/s, bi-directional) 256 (Gen 6) 256 (Gen 6) Table 4. Interconnect comparison of Blackwell and Rubin 

 Built for AI factory workloads 

 The NVIDIA Rubin GPU is optimized for the workloads that define modern AI factories, where performance is governed less by peak compute and more by sustained efficiency across compute, memory, and communication. These workloads include MoE models dominated by dynamic all-to-all communication, agentic pipelines that interleave reasoning with tool use, and long-running training and post-training workflows that must maintain high utilization over extended periods. 

 By combining adaptive execution with massive scale-up bandwidth, the Vera Rubin platform keeps GPUs productive across all phases of execution, including compute-heavy kernels, memory-intensive attention, and communication-bound expert dispatch, rather than optimizing only for dense matrix math. This is not a point upgrade over prior generations. The Vera Rubin platform rebalances GPU architecture for continuous operation at scale, working in concert with the Vera CPU, NVLink 6 scale-up, and platform software to efficiently convert power and silicon into usable intelligence across the rack. 

 In the next section, we examine NVLink 6 switching, the rack-scale fabric that allows 72 GPUs to operate as a single, tightly coupled system. 

 NVLink 6 Switch: The rack-scale scale-up fabric 

 At the AI factory scale, communication is key to determining performance. MoE routing, collective operations, synchronization-heavy training, and reasoning inference all depend on fast, predictable all-to-all data movement. When scale-up bandwidth falls short, GPUs sit idle and cost per token rises. 

 NVLink 6 is designed to eliminate this bottleneck. It is the scale-up fabric of the Vera Rubin platform, enabling 72 Rubin GPUs within an NVL72 system to operate as a single, tightly coupled accelerator with uniform latency and sustained bandwidth under communication-dominated workloads. 

 
 
 
 
 
 Figure 10. NVLink 6 switch 

 Each Rubin GPU connects to NVLink 6 with 3.6 TB/s of bidirectional bandwidth, doubling per-GPU scale-up bandwidth over the prior generation. NVLink 6 switch trays form a single all-to-all topology across the rack, allowing any GPU to communicate with any other GPU with consistent latency and bandwidth. 

 This uniform topology removes hierarchical bottlenecks and hop-dependent behavior. From the software perspective, the rack behaves as one large accelerator, simplifying scaling for communication-heavy models. 

 All-to-all scaling for MoE and reasoning 

 Fast MoE training and inference uses expert parallelism (EP), which relies on fine-grained, dynamic routing of tokens across experts that may reside on different GPUs. These patterns generate frequent, bursty communication that overwhelms hierarchical or partially connected fabrics. 

 NVLink 6 is deployed as a full all-to-all fabric across the NVL72 system. Expert routing, synchronization, and collectives scale efficiently across all 72 GPUs without saturating links or introducing unpredictable latency. 

 For MoE inference at scale, NVLink 6 delivers up to 2x higher throughput compared to the prior generation for all-to-all operations. 

 
 
 
 
 
 Figure 11. Vera Rubin NVL72 NVLink all-to-all topology 

 In-network compute for collective operations 

 NVLink 6 integrates NVIDIA Scalable Hierarchical Aggregation and Reduction Protocol (SHARP) in-network compute to accelerate collective operations directly inside the fabric. Portions of all-reduce, reduce-scatter, and all-gather execute within the switch, reducing redundant data movement and GPU synchronization overhead. 

 Each NVLink 6 switch tray delivers 14.4 TFLOPS of FP8 in-network compute, enabling collective-heavy phases to execute with lower latency and higher efficiency. By offloading collective reductions into the network, SHARP can reduce all-reduce communication traffic by up to 50% and improve tensor-parallel execution time by up to 20% in large-scale AI workloads. 

 This offload increases effective GPU utilization and improves scaling efficiency as cluster size grows. Results are dependent on model architecture, parallelism strategy, participant count, and NCCL configuration. 

 Operability at AI factory scale 

 Scale-up networking must be operable, not just fast. The NVLink 6 switch tray incorporates new features for resiliency and maintenance, including hot-swappable trays, continued operation with partially populated racks, and dynamic traffic rerouting when a switch goes offline. It also supports in-service software updates and streams fine-grained link telemetry through the switch interfaces for real-time monitoring. 

 Together, software-defined routing, detailed telemetry, and serviceable switch trays enable traffic to be dynamically rerouted around faults or maintenance events without draining the rack or interrupting active workloads. These capabilities allow NVLink 6 to meet the zero-downtime expectations of production AI factories. 

 By doubling per-GPU bandwidth, enabling uniform all-to-all connectivity, and accelerating collectives directly inside the fabric, NVLink 6 allows communication-heavy workloads to scale predictably at rack scale. 

 In the next section, we turn to ConnectX-9, which provides the endpoint interface that extends this performance beyond the rack by connecting GPUs to the Spectrum-X Ethernet scale-out fabric. 

 ConnectX-9: Pushing the limits of AI scale-out bandwidth 

 ConnectX-9 serves as the intelligent endpoints of the Spectrum-X Ethernet fabric, delivering predictable scale-out performance while enforcing traffic isolation and secure operation as AI factories grow. 

 
 
 
 
 
 Figure 12. ConnectX-9 

 In the Vera Rubin NVL72 rack-scale architecture, each compute tray contains quad ConnectX-9 SuperNIC boards, delivering 1.6Tb/s of network bandwidth per Rubin GPU. Each quad ConnectX-9 SuperNIC board connects to each Vera CPU. This ensures GPUs can participate fully in expert dispatch, collective operations, and synchronization without becoming bottlenecked at the network edge. 

 Endpoint control for bursty AI traffic 

 AI workloads such as MoE inference and training generate highly correlated traffic patterns. Large numbers of GPUs often attempt to inject data into the network simultaneously, creating transient traffic congestion spikes that traditional NICs are not designed to manage. 

 ConnectX-9 addresses this challenge by enforcing programmable congestion control, traffic shaping, and packet scheduling directly at the endpoint. Working in concert with Spectrum-6 switches, ConnectX-9 prevents congestion from forming in the first place rather than reacting after queues build. 

 This coordinated endpoint-to-fabric behavior: 

 
 Smooths traffic injection during all-to-all phases 

 Reduces head-of-line blocking and victim flows 

 Maintains high effective bandwidth under load 
 

 Performance isolation for multi-tenant AI factories 

 As AI factories consolidate workloads, isolation becomes as important as throughput. Bursty or misconfigured jobs must not degrade cluster-wide performance. 

 ConnectX-9 enforces fairness and isolation at the endpoint, ensuring that each job or tenant receives predictable network behavior regardless of the activity of others. This capability is critical for shared AI infrastructure, where inference, training, and post-training workloads often run concurrently on the same fabric. 

 By shifting enforcement to the endpoint, the platform avoids relying solely on switch-level mechanisms, improving scalability and reducing operational complexity. 

 Secure endpoints for AI infrastructure 

 ConnectX-9 also plays a central role in securing AI factory networking. Integrated cryptographic engines support high-throughput encryption for data in motion and data at rest, enabling secure operation without sacrificing performance. 

 Key security capabilities include: 

 
 Data-in-transit encryption acceleration for IP Security (IPsec) and Platform Security Protocol (PSP) to secure GPU-to-GPU communications 

 Data-at-rest encryption acceleration to secure storage platforms 

 Secure boot, firmware authentication, and device attestation 
 

 These features allow AI factories to operate securely in shared, cloud, or regulated environments while maintaining near-native network performance. 

 From endpoint control to infrastructure offload 

 ConnectX-9 completes the Spectrum-X Ethernet scale-out architecture by controlling how traffic enters the fabric. By shaping, scheduling, isolating, and securing communication at the endpoint, it ensures that AI factory networks behave predictably under real workloads. 

 With fabric-level behavior defined by Spectrum-6 and endpoint behavior enforced by ConnectX-9, the remaining challenge is how to operate, secure, and manage this infrastructure at scale without consuming valuable CPU and GPU resources. 

 That responsibility shifts to BlueField-4 DPUs, which provide the software-defined infrastructure layer for operating the AI factory itself. In the next section, we examine how BlueField-4 powers networking, storage, security, and control services across the Vera Rubin platform. 

 BlueField-4 DPU: Powering the operating system of the AI factory 

 As AI infrastructure grows to thousands of GPUs and petabytes of data, AI factories must be operated with the rigor, automation, and control of modern cloud infrastructure. The challenge extends beyond connecting GPUs to orchestrating highly distributed systems that can scale, secure, and operate AI workloads efficiently. Applying cloud-scale principles to AI infrastructure requires automation, elasticity, and end-to-end security to be foundational from the start. 

 Meeting these demands calls for a specialized data processing unit dedicated to the infrastructure layer itself. NVIDIA BlueField-4 fulfills this role by handling control, security, data movement, and orchestration independently of AI computation. In effect, BlueField-4 is the processor powering the operating system of the AI factory, purpose-built to connect, secure, and manage the infrastructure that powers AI at scale. 

 Within the Rubin platform, BlueField-4 operates as a software-defined control plane for the AI factory, enforcing security, isolation, and operational determinism independently of host CPUs and GPUs. By offloading and accelerating infrastructure services onto a dedicated processing layer, BlueField-4 enables AI factories to scale while maintaining consistent performance, strong isolation, and efficient operations. 

 
 
 
 
 
 Figure 13. BlueField-4 DPU 

 BlueField-4 integrates a 64-core Grace CPU and high-bandwidth LPDDR5X memory together with ConnectX-9 networking, delivering up to 800 Gb/s of ultra-low-latency Ethernet or InfiniBand connectivity while running infrastructure services directly on the DPU. 

 The table below highlights key advancements in BlueField-4 compared to BlueField-3 across bandwidth, compute, and memory. These improvements allow AI factories to scale pods and services without infrastructure becoming a limiting factor. 

 Feature BlueField-3 BlueField-4 Bandwidth 400 Gb/s 800 Gb/s Compute 16 Arm A78 Cores 64 Arm Neoverse V2 6x Compute Performance Memory bandwidth 75 GB/s 250 GB/s Memory capacity 32GB 128GB Cloud networking 32K hosts 128K hosts Data-in-transit encryption 400Gb/s&nbsp; 800Gb/s NVMe storage disaggregation 10M IOPs at 4K 20M IOPs at 4K Table 5. NVIDIA BlueField DPU capability comparison 

 This generational increase allows AI factories to scale pods, services, and tenants while also advancing infrastructure operations, efficiency, and cybersecurity. 

 Infrastructure acceleration at AI factory scale 

 In traditional systems, infrastructure services run on host CPUs, introducing variability, contention, and security risk as workloads scale. BlueField-4 eliminates this coupling by executing networking, storage, telemetry, and security services entirely off-host. This separation delivers: 

 
 Deterministic infrastructure behavior independent of workload mix 

 Higher GPU and CPU utilization for AI execution 

 Improved fault isolation and operational resilience 
 

 NVIDIA DOCA provides a consistent software foundation across BlueField generations, enabling reuse of infrastructure services while allowing rapid innovation without disrupting application workloads. DOCA is a comprehensive software framework and SDK that enables developers to build, deploy, and accelerate secure, software-defined data center services on BlueField DPUs and ConnectX devices using open APIs and hardware offloads. 

 Built for secure, multi-tenant operation 

 As AI factories increasingly adopt bare-metal and multi-tenant deployment models, maintaining strong infrastructure control and isolation becomes essential, particularly for environments processing proprietary data, regulated content, and high-value models. 

 As part of the Vera Rubin platform, BlueField-4 introduces Advanced Secure Trusted Resource Architecture (ASTRA), a system-level trust architecture that establishes a trust domain within the compute tray. ASTRA provides AI infrastructure builders with a single, trusted control point to securely provision, isolate, and operate large-scale AI environments without compromising performance. 

 By isolating control, data, and management planes from tenant workloads, BlueField ASTRA enables secure bare-metal operation, strong multi-tenant isolation, and trusted infrastructure control that operates independently of host software. 

 NVIDIA Inference Context Memory Storage—AI-native storage infrastructure 

 The Vera Rubin platform introduces NVIDIA Inference Context Memory Storage (ICMS) , an AI-native infrastructure tier designed for the agentic era, where inference state routinely outlives a single GPU execution window. As long-context, multi-turn, and multi-agent workloads push toward millions of tokens, KV cache capacity grows fast, forcing that state into either scarce GPU HBM or durability-optimized enterprise storage, which drives up latency, power, and cost per token. 

 ICMS, powered by NVIDIA BlueField-4, bridges the gap between GPU memory tiers and shared storage. ICMS establishes a pod-level “G3.5” context memory layer, an Ethernet-attached, flash-based tier optimized specifically for ephemeral, latency-sensitive KV cache, sized for petabytes of shared capacity per GPU pod and built for frequent pre-staging back into host and GPU memory to avoid decode stalls. 

 At scale, ICMS turns reusable KV cache into a shared pod resource rather than a per-node liability, improving utilization and reducing redundant recomputation. NVIDIA reports up to 5x higher tokens-per-second and up to 5x better power efficiency versus traditional storage approaches by reliably serving and prestaging KV from this dedicated tier. 

 
 G3.5 tier: Ethernet-attached flash purpose-built for KV cache, positioned between local tiers (HBM, DRAM, local SSD) and durable shared storage, so context stays close enough to be reused without paying “G4 latency.” 

 BlueField-4 offload: BlueField-4 runs the KV I/O plane and efficiently terminates NVMe-over-Fabrics and object/RDMA protocols, reducing host overhead while keeping KV movement fast, predictable, and secure. 

 Spectrum-X fabric: Spectrum-X Ethernet provides predictable, low-latency, low-jitter RDMA connectivity between Rubin compute nodes and ICMS target nodes for consistent shared KV access across the pod. 

 Orchestration: NVIDIA Dynamo and NIXL coordinate KV block management and prestaging across the hierarchy, with DOCA providing KV communication and storage interfaces that treat context as a first-class resource. 
 

 Operating the AI factory as a system 

 BlueField-4 establishes infrastructure as a first-class architectural layer of the AI factory. By operating the control, security, data movement, and orchestration planes on a dedicated processing layer, it enables AI factories to remain predictable, secure, and efficient at scale. 

 Within the Vera Rubin platform, NVLink defines scale-up behavior, ConnectX-9 and Spectrum-X Ethernet switches govern scale-out and scale-across communication, and BlueField-4 operates the AI factory itself. 

 Spectrum-6 Ethernet switch: Scale-out and scale-across for AI factories 

 AI factories must also scale beyond a single Vera Rubin NVL72 system and often need to scale across geographically dispersed data centers. Performance is then determined not just by bandwidth, but by how predictably the network behaves under synchronized, bursty AI traffic. 

 To support both scale-out and scale-across AI factory deployments, the Vera Rubin platform introduces NVIDIA Spectrum-X Ethernet Photonics, a new generation of Spectrum-X Ethernet switching based on co-packaged optics, advancing NVIDIA’s purpose-built Ethernet fabric for accelerated computing. 

 
 
 
 
 Figure 14. Spectrum-6 Ethernet switch chip 

 Spectrum-6 is engineered specifically for AI workloads, where traffic is highly synchronized, bursty, and asymmetric. Spectrum-6 doubles per-switch-chip bandwidth to 102.4 Tb/s using 200G PAM4 SerDes, enabling dense, high-port count fabrics optimized for AI traffic patterns.&nbsp; 

 High effective bandwidth, fine-grained telemetry, and hardware-assisted performance isolation enable deterministic behavior in large, multi-tenant AI fabrics, while remaining fully standards-based and interoperable with open networking software. 

 Spectrum-X Ethernet fabric 

 Unlike off-the-shelf Ethernet, Spectrum-X Ethernet delivers predictable, low-latency, high-bandwidth connectivity at scale through advanced congestion control, adaptive routing, and lossless Ethernet behavior. These capabilities minimize jitter, tail latency, and packet loss under sustained AI load. 

 Anchored on Spectrum-6, Spectrum-X Ethernet was co-designed with the Vera Rubin platform to ensure that routing behavior, congestion control, and telemetry reflect real AI communication patterns rather than traditional enterprise networking assumptions. This alignment allows scale-out performance to track application behavior, not theoretical peak throughput. 

 Spectrum-X Ethernet also incorporates Spectrum-XGS Ethernet scale-across technology, which adds distance-aware congestion control for large, geographically distributed AI deployments. End-to-end telemetry and deterministic routing enable efficient load balancing across sites, keeping multi-site AI factories operating at high utilization. 

 Spectrum-X Ethernet Photonics: Redefining network efficiency at AI scale 

 Spectrum-X Ethernet Photonics fundamentally improves network efficiency by eliminating pluggable transceivers and DSP retimers. Integrated silicon photonics combined with external laser arrays reduce component count and failure points compared to network fabrics based on traditional pluggable transceivers. Spectrum-X Ethernet Photonics delivers: 

 
 ~5x better network power efficiency 

 Lower end-to-end latency 

 Dramatically improved signal integrity 
 

 By reducing optical loss from ~22 dB to ~4 dB, Spectrum-X Ethernet achieves up to 64x better signal integrity. It enables higher uptime, simplified serviceability with high-density MMC-12 cabling, and lower total cost of ownership for large training and inference clusters. 

 
 
 
 
 
 Figure 15. NVIDIA Spectrum-X Ethernet Photonics switches 

 Built for real AI traffic patterns 

 Modern MoE training and inference introduce a variable all-to-all communication phase driven by stochastic expert token dispatch. These workloads generate highly bursty traffic that can overwhelm traditional Ethernet fabrics, leading to packet loss, congestion collapse, and degraded job completion times. 

 Spectrum-X Ethernet addresses this at the fabric level through coordinated congestion control and adaptive routing across switches and endpoints. The result is significantly faster job completion for expert dispatch and collective operations under real AI load. 

 
 
 
 
 
 Figure 16. Spectrum-X Ethernet variable all-to-all performance 

 Advancing the fabric without re-architecting the network 

 Spectrum-X Ethernet evolves generation-over-generation through end-to-end co-design across switch silicon, optics, SuperNICs, and system software. This delivers coordinated gains in bandwidth, signaling, and scalability without requiring a fundamental fabric redesign, allowing customers to scale AI clusters predictably as performance requirements grow. 

 Feature Grace Blackwell Vera Rubin Key component Spectrum-X SN5000 series ConnectX-8 SuperNIC Spectrum-X SN6000 series ConnectX-9 SuperNIC Chip Spectrum-4 ConnectX-8 Spectrum-6 ConnectX-9 Maximum bandwidth 51.2 Tb/s per switch chip(64 x 800 Gb/s) 800 Gb/s (2 x 400G) per GPU 102.4 Tb/s per switch chip(128 x 800 Gb/s) 1600 Gb/s (2 x 800 GB/s) per GPU SerDes 100G PAM4 100/200G PAM4 200G PAM4 200G PAM4 Protocol Ethernet Ethernet, InfiniBand Ethernet Ethernet, InfiniBand Connectivity OSFP OSFP, QSFP112 OSFP OSFP, QSFP112 Table 6. NVIDIA Spectrum-X Ethernet platform evolution 

 For more on Spectrum-X Ethernet Photonics, check out this blog . 

 4. From chips to systems: NVIDIA Vera Rubin superchip to DGX SuperPOD 

 AI factory performance is not determined by individual chips in isolation, but by how those chips are composed into systems that can be deployed, operated, and scaled reliably. The Vera Rubin platform is designed with this progression in mind, moving deliberately from silicon-level innovation to rack-scale systems and finally to full AI factory deployments. 

 This section traces that progression, starting with the Vera Rubin superchip as the foundational compute building block, then scaling through the NVL72 rack architecture and its integrated networking fabrics, and culminating in the NVIDIA DGX SuperPOD as the deployment-scale unit of an AI factory. At each step, the goal is the same: Preserve the efficiency and utilization gains achieved at the chip level as the system scales outward. 

 NVIDIA Vera Rubin superchip&nbsp; 

 At the heart of the Rubin platform is the NVIDIA Vera Rubin superchip, the foundational compute building block that tightly integrates AI execution with high-bandwidth data movement and orchestration. Each superchip combines two Rubin GPUs with one Vera CPU through memory-coherent NVLink-C2C interconnect, collapsing traditional CPU-GPU boundaries into a unified, rack-scale execution domain. 

 This approach is not new for NVIDIA. Beginning with NVIDIA Grace Hopper and continuing through subsequent generations, close CPU-GPU integration has been a core design principle to co-optimize compute, memory, and interconnect to sustain utilization under real training and inference workloads. 

 In the Vera Rubin superchip, the CPU functions as a data engine tightly coupled to GPU execution. This coupling enables low-latency coordination, shared memory access, and efficient orchestration across training, post-training, and inference workloads. Rather than acting as an external host, the Vera CPU participates directly in execution, handling data movement, scheduling, synchronization, and execution flow without introducing bottlenecks. 

 By integrating GPU compute with a high-bandwidth CPU data engine on a single host processing motherboard, the superchip improves data locality, reduces software overhead, and sustains higher utilization across heterogeneous execution phases. It serves as the architectural bridge between chip-level innovation and rack-scale intelligence. 

 
 
 
 
 
 Figure 17. Vera Rubin superchip 

 Vera Rubin NVL72 compute tray 

 The compute tray translates the Vera Rubin superchip into a deployable, serviceable unit designed for AI factory scale. Each tray integrates two superchips, power delivery, cooling, networking, and management into a modular, cable-free assembly optimized for density, reliability, and ease of operation. 

 A redesigned internal liquid manifold and universal quick-disconnects support significantly higher flow rates than prior generations, enabling stable performance under sustained, high-power workloads. The modular compute tray uses independent front and rear bays to streamline assembly and service. Although the compute tray must be taken offline during maintenance, the modular cable-free design reduces service time by up to 18x. Assembly that used to take more than 1.5 hours for Blackwell now takes only ~5 minutes with Vera Rubin. 

 
 
 
 
 
 Figure 18. Vera Rubin NVL72 compute tray 

 ConnectX-9 SuperNICs provide high-bandwidth scale-out connectivity (1.6 Tb/s per GPU), while BlueField-4 DPUs offload networking, storage, and security services, allowing CPUs and GPUs to remain focused on AI execution. 

 
 
 
 
 
 Figure 19. ConnectX-9 and BlueField-4 modules for the Vera Rubin compute tray 

 Vera Rubin NVL72 NVLink switch tray 

 To transform multiple compute trays into one rack-scale accelerator Vera Rubin introduces the NVLink 6 switch tray.&nbsp; 

 Each switch tray incorporates four NVLink 6 switch chips, doubling the per-GPU scale-up bandwidth as well as the in-network compute for accelerating collective operations directly inside the fabric. This is critical for MoE routing, synchronization-heavy inference, and communication-intensive training phases where scale-up efficiency directly determines cost and latency. 

 By integrating scale-up networking as a first-class rack component, the NVLink switch tray ensures that performance scales predictably as models, batch sizes, and reasoning depth continue to increase. 

 
 
 
 
 
 Figure 20. Vera Rubin NVLink switch tray 

 Spectrum-X Ethernet switching for scale-out AI factories 

 NVLink 6 allows 72 GPUs to behave as one rack-scale accelerator inside the rack. Spectrum-X Ethernet extends that capability beyond the rack, enabling predictable, high-throughput scale-out connectivity across rows and data centers, without the variability that traditional Ethernet often introduces under synchronized AI traffic. 

 AI factory communication patterns are fundamentally different from enterprise workloads. MoE dispatch, collective operations, and synchronization-heavy phases generate bursty, asymmetric, and highly correlated flows that can amplify congestion, tail latency, and performance jitter at scale. Spectrum-X Ethernet is engineered specifically for these patterns through coordinated congestion control, adaptive routing, and end-to-end telemetry that keep effective bandwidth high and performance repeatable under load. 

 Within the Vera Rubin NVL72 platform, Spectrum-X is realized through the combination of Spectrum-6 switches and ConnectX-9 SuperNIC endpoints included in the compute nodes. Together, they form a tightly co-designed scale-out system where the fabric and endpoints cooperate to shape traffic, isolate workloads, and prevent hotspots, enabling high utilization in multi-job, multi-tenant AI factories. 

 
 
 
 
 
 Figure 21. Spectrum-X Ethernet switching for the Vera Rubin platform 

 NVIDIA DGX SuperPOD: the AI factory deployment unit 

 DGX SuperPOD represents the blueprint for deployment-scale realization of the Vera Rubin platform. Built with eight DGX Vera Rubin NVL72 systems, it defines the minimum unit at which AI factory economics, reliability, and performance converge in production environments. 

 Unlike traditional clusters assembled from discrete components, DGX SuperPOD is designed as a complete system. Every layer, from silicon and interconnects to orchestration and operations, is co-designed and validated to deliver sustained utilization, predictable latency, and efficient conversion of power into tokens at scale. 

 Within each NVIDIA DGX Vera Rubin NVL72 system, 72 Rubin GPUs operate as one rack-scale accelerator through NVLink 6. Spectrum-X Ethernet extends the platform beyond the rack with deterministic, high-throughput scale-out connectivity, allowing multiple DGX Vera Rubin NVL72 systems to be composed into a DGX SuperPOD. Integrated with NVIDIA Mission Control software and certified storage, these elements create a validated, production-ready AI factory building block, ready to scale into tens of thousands of GPUs. 

 This design enables DGX SuperPOD to deliver true AI factory abilities: continuous operation, high-uptime serviceability, and consistent performance across training, post-training, and real-time inference workloads. 

 
 
 
 
 
 Figure 22. DGX SuperPOD with DGX Vera Rubin NVL72 Systems 

 5. Software and developer experience 

 Vera Rubin also has been designed to accelerate innovation without forcing developers to re-architect their software. At its foundation, the platform maintains full CUDA backward compatibility across hardware generations, ensuring existing models, frameworks, and workflows run seamlessly while automatically benefiting from generational improvements in compute, memory, and interconnect. 

 CUDA-X libraries—the performance foundation 

 The CUDA platform encompasses a programming model, core libraries, and communication stacks that accelerate applications and expose the full distributed capabilities of the rack-scale system. Developers can program Rubin GPUs as individual devices or as part of a single 72-GPU NVLink domain using NVIDIA Collective Communications Library (NCCL) , NVIDIA Inference Transfer Library (NIXL), and NVLink-aware collectives. This design enables models to scale across the rack without custom partitioning, topology-aware workarounds, or manual orchestration. 

 
 
 
 
 
 Figure 23. Accelerated computing starts with CUDA-X 

 At the kernel and library layer, NVIDIA provides highly optimized building blocks for the most demanding AI workloads. Libraries such as NVIDIA cuDNN , NVIDIA CUTLASS , FlashInfer , and a new Transformer Engine deliver peak efficiency for attention, activation, and narrow-precision execution. These components are tightly coupled with Rubin’s Tensor Cores, HBM4 memory subsystem, and NVLink 6 interconnect, enabling sustained performance across dense, sparse, and communication-heavy workloads. 

 Together, these libraries allow developers to focus on model behavior rather than hardware-specific tuning, while still extracting maximum performance from the underlying platform. 

 Large-scale training—from research to production with NVIDIA NeMo 

 Higher-level frameworks build directly on the Vera Rubin platform to maximize developer productivity and scalability. PyTorch and JAX frameworks ship with native NVIDIA acceleration to enable training, post-training, and inference workflows to scale across racks with minimal code changes. 

 At the core of NVIDIA’s training and customization stack is the NVIDIA NeMo Framework , which provides an end-to-end workflow for building, adapting, aligning, and deploying large models at AI factory scale. NeMo unifies data curation, large-scale distributed training, alignment, and parameter-efficient customization into a single, production-oriented framework. Through NVIDIA NeMo Run , developers can configure, launch, and manage experiments consistently across local environments, SLURM clusters, and Kubernetes-based AI factories. 

 
 
 
 
 
 Figure 24. NeMo framework for large-scale model training, alignment, and deployment 

 For extreme-scale training, NeMo integrates tightly with NVIDIA Megatron Core , which supplies the underlying distributed training engine. Megatron Core provides advanced parallelism strategies, optimized data loaders, and support for modern model architectures including dense LLMs, MoE, state-space models, and multimodal networks. This integration allows NeMo to scale training across thousands of GPUs while abstracting the complexity of parallelism and communication from the user. 

 NeMo also supports advanced post-training workflows, including reinforcement learning and alignment techniques such as reinforcement learning with human feedback (RLHF), direct preference optimization (DPO), proximal policy optimization (PPO), and supervised fine-tuning. These capabilities enable developers to move seamlessly from pre-training to alignment and customization within a single framework—without re-architecting pipelines. 

 To link ecosystem workflows, NVIDIA NeMo Megatron Bridge enables bidirectional checkpoint conversion and verification between Hugging Face and Megatron formats. This tool allows models to move reliably between community tooling, NeMo-based training, reinforcement learning, and optimized inference deployments, while preserving correctness and reproducibility. 

 Inference frameworks and optimization—serving real-time intelligence 

 The Vera Rubin platform has been architected to deliver significant gains for modern inference workloads, which are increasingly defined by low latency, high concurrency, and communication-heavy execution. The platform integrates with widely used open source and NVIDIA inference frameworks—including SGLang, NVIDIA TensorRT-LLM, vLLM, and NVIDIA Dynamo—to enable efficient execution of long-context, MoE, and agentic workloads as software support is enabled with platform availability.&nbsp; 

 The NVIDIA Model Optimizer extends inference performance through quantization, pruning, distillation, and speculative decoding, and it translates architectural advances directly into lower latency and lower cost per token. At the serving layer, NVLink-enabled communication, disaggregated inference, LLM-aware routing, KV-cache offloading to storage, and Kubernetes autoscaling are exposed through Dynamo–enabling scalable serving of communication-intensive workloads such as MoE inference and multi-agent pipelines. 

 
 
 
 
 
 Figure 25. NVIDIA inference software stack 

 A developer-ready programmable rack-scale platform 

 NVIDIA’s architecture is designed from the ground up to maximize platform software performance and developer usability at rack scale. By integrating platform software and developer experience directly into the architecture, the Vera Rubin platform is not only powerful, but practical to deploy and program. Developers can focus on models, agents, and services rather than infrastructure complexity, while operators retain control over performance, reliability, and efficiency at AI factory scale. 

 6. Operating at AI factory scale 

 Operating an AI factory at scale requires more than raw performance. It demands systems that can run continuously, securely, efficiently, and predictably in real-world data center environments. The Vera Rubin platform is engineered not only to deliver breakthrough compute capability, but to sustain it over time through intelligent reliability, full-stack security, energy-aware design, and a mature rack ecosystem. Together, these capabilities ensure that AI factories built on the Vera Rubin platform can scale rapidly, operate with minimal disruption, and convert power, infrastructure, and silicon into usable intelligence at industrial scale. 

 Deployment and operations 

 NVIDIA Mission Control accelerates every aspect of AI factory operations, from configuring Vera Rubin NVL72 deployments to integrating with facilities to managing clusters and workloads. Enabled by intelligent, integrated software, enterprises gain improved control over cooling and power events and redefine infrastructure resiliency. Mission Control enables faster response with rapid leak detection, unlocks access to NVIDIA’s latest efficiency innovations, and maximizes AI factory productivity with autonomous recovery. 

 
 
 
 
 
 Figure 26. NVIDIA Mission Control software to configure, validate, and operate Vera Rubin-based AI factories 

 Mission Control offers a validated implementation for enterprises to simplify and scale how AI factories are deployed and operated throughout the entire cluster lifecycle: 

 
 Seamless workload orchestration: Empower model builders with effortless and simplified workload management with NVIDIA Run:ai functionality. 

 Power optimizations: Balance power requirements and tune GPU performance for various workload types with developer-selectable controls. 

 Autonomous recovery engine: Identify, isolate, and recover from problems without manual intervention for maximum productivity and infrastructure resiliency. 

 Customizable dashboards: Track key performance indicators with access to critical telemetry data about your cluster and easy-to-set dashboards 

 Continuous health checks: Validate hardware and cluster performance throughout the life cycle of your infrastructure. 
 

 Enterprise software and lifecycle support&nbsp; 

 NVIDIA AI Enterprise provides the enterprise-grade software foundation required to operate AI factories at scale. It delivers a validated, supported software stack that spans application development libraries, frameworks, and microservices, as well as infrastructure software for GPU management. It enables predictable performance, security, and stability for production AI deployments. 

 
 
 
 
 
 Figure 27. NVIDIA AI Enterprise software suite for AI factories 

 For agentic AI development, NVIDIA AI Enterprise includes NVIDIA NIM, NeMo, and other containerized libraries and microservices that enable optimized inference, model training, and customization through standardized APIs. With support for NVIDIA, partner, and community AI models, NIM microservices enable enterprises to deploy agentic AI capabilities faster. 

 Additionally, application development SDKs, frameworks, and libraries translate the Vera Rubin platform’s architectural capabilities into performance improvements. CUDA, Transformer Engine, cuDNN, and related libraries are validated as an accelerated stack, ensuring that hardware advances are automatically realized by higher-level frameworks and services. 

 For infrastructure management, NVIDIA AI Enterprise integrates with Kubernetes through purpose-built operators and validated GPU, networking, and virtualization drivers. These components enable secure multi-tenant operation, workload orchestration, and cluster-wide observability, and allow operators to maximize utilization while maintaining reliability and compliance. 

 Delivered with long-term support, regular security updates, and compatibility validation across hardware generations, NVIDIA AI Enterprise serves as the software backbone of NVIDIA AI factories. It transforms rack-scale systems into a programmable, secure, and operable production platform across data center, cloud, and edge environments. 

 NVIDIA AI Enterprise is supported by a wide ecosystem of partners, including solution integrators, data and enterprise platforms, hybrid and multi-cloud providers, and AIOps solutions. It integrates seamlessly with existing enterprise software stacks to enable production grade AI and accelerate time to market. 

 Reliability, availability, and serviceability 

 AI factories are no longer batch systems that can afford maintenance windows. They are always-on environments running continuous training, real-time inference, retrieval, and analytics. Vera Rubin NVL72 is engineered for this reality, introducing a rack-scale RAS architecture designed to maximize uptime, improve goodput, the amount of useful AI work actually completed over time, and ensure predictable completion of long-running AI workloads. 

 In this context, goodput reflects how effectively the system converts powered-on time into finished training steps, completed inference requests, and delivered tokens, without losses from job restarts, checkpoint rollbacks, stragglers, or performance degradation caused by component faults. Even brief interruptions or localized failures can materially reduce goodput when workloads span thousands of GPUs and run for days or weeks. 

 Resiliency in the Vera Rubin platform is designed end to end, spanning silicon, interconnect, and physical system architecture. The result is a unified, intelligent approach to reliability that allows the system to isolate faults, reroute traffic, and continue executing workloads without interruption, enabling zero planned downtime at rack scale while preserving sustained throughput and predictable job completion. 

 Rack-scale resiliency: Designed from the ground up 

 Vera Rubin NVL72 is built on a third-generation NVIDIA MGX rack design that treats reliability and serviceability as first-order architectural requirements. Compute trays, NVLink switch trays, and power and cooling infrastructure are modular, hot-swappable, and designed for in-field replacement without draining racks or interrupting active workloads. 

 As shown in the animation below, a cable-free, hose-free, fanless compute tray architecture eliminates many manual PCIe, networking, and management connections within the tray, removing common assembly and service friction seen in prior cabled tray designs. This mechanical simplification enables up to 18x faster assembly compared with previous generation tray architectures and significantly reduces services time during in-field maintenance, lowering deployment time and ongoing operational overhead.&nbsp; 

 A mature ecosystem of more than 80 MGX partners ensures global manufacturability, service readiness, and scalable deployment, allowing AI factories to ramp quickly while maintaining consistent reliability at scale. 

 
 
 
 
 
 Figure 28. NVIDIA Blackwell Ultra GB300 vs. Vera Rubin compute tray 

 Intelligent resiliency across the interconnect 

 At the system level, NVIDIA NVLink Intelligent Resiliency enables racks to remain fully operational during maintenance, partial population, or component replacement. Using software-defined routing and intelligent failover, traffic is dynamically rerouted around faults without disrupting active training or inference jobs. 

 This capability is critical as AI factories scale to thousands of GPUs. Rather than treating interruptions as stop-the-world events, the system adapts in real time, maintaining high utilization and predictable performance even as components are serviced or replaced to improve goodput. 

 Silicon-level health monitoring with zero downtime 

 At the heart of this architecture is the Rubin GPU’s second-generation Reliability Availability and Scalability Engine (RAS), which delivers continuous, in-system health monitoring without taking GPUs offline. Health checks are performed during idle execution windows, enabling full diagnostics with no impact to running workloads. 

 The RAS engine supports in-field SRAM repair and zero-downtime self-testing during execution, increasing effective mean time between failures and improving overall system yield. This capability is especially important for long-running training jobs and persistent inference services, where unplanned interruptions can be costly or unacceptable. 

 Vera CPUs complement GPU-level resiliency with in-system CPU core validation, reduced diagnostic times, and SOCAMM LPDDR5X memory designed for improved serviceability and fault isolation. 

 Predictive operations at AI factory scale 

 These hardware capabilities are paired with NVIDIA AI-powered predictive management, which analyzes thousands of hardware and software telemetry signals across the rack. Potential issues are identified early, localized precisely, and addressed proactively. Operators can rebalance workloads, adjust checkpoint strategies, activate standby capacity, or schedule maintenance without impacting service-level objectives. 

 Together, these capabilities transform RAS from a reactive process into an intelligent, predictive system that minimizes downtime, reduces operational complexity, and ensures AI workloads complete on schedule. 

 With Vera Rubin NVL72, reliability is no longer a limiting factor for scale. From silicon to system, the platform is engineered to keep AI factories running continuously, efficiently, and predictably at unprecedented scale. 

 Full stack confidential computing 

 As AI factories move into production, security requirements expand from protecting individual devices to protecting entire systems operating continuously at scale. Modern AI workloads routinely process proprietary training data, regulated content, and high-value models, often in shared or cloud environments where infrastructure cannot be implicitly trusted. Meeting these requirements demands security that spans silicon, interconnect, and system software, without introducing performance penalties or operational friction. 

 Vera Rubin NVL72 was designed with full-stack confidential computing as a foundational capability, extending trust from individual components to the entire rack. 

 Third–generation confidential computing: rack-level security 

 As shown in the figure below, Vera Rubin NVL72 extends confidential computing beyond individual devices to create a unified, rack-scale trusted execution environment spanning CPUs, GPUs, and interconnects. This design enables sensitive AI workloads to run securely at scale with near-native performance, even in shared or cloud environments. 

 
 
 
 
 
 Figure 29. Confidential computing on Vera Rubin NVL72 

 AI factories increasingly process proprietary data, regulated content, and mission-critical models that cannot be exposed, even to the infrastructure they run on. Vera Rubin NVL72 addresses this requirement by delivering end-to-end encryption across CPU-to-GPU, GPU-to-GPU, and device I/O paths, allowing enterprises to deploy secure training, inference, retrieval, and analytics pipelines without sacrificing throughput or latency. 

 From device-level security to rack-scale trust 

 NVIDIA has advanced GPU security over multiple generations. Hopper introduced high-performance confidential computing for GPUs. Blackwell expanded these capabilities, eliminating the traditional tradeoff between security and performance. Vera Rubin NVL72 completes this progression by unifying CPU and GPU security into a single unified trust domain across the entire rack. 

 This rack-level approach ensures that proprietary models, training data, embeddings, and inference prompts remain protected not only from other tenants, but also from the underlying cloud provider infrastructure itself. 

 Cryptographic attestation and verifiable compliance 

 Vera Rubin NVL72 integrates with NVIDIA remote attestation services (NRAS) to provide cryptographic proof of system integrity. Organizations can verify that CPUs, GPUs, NICs, firmware, drivers, and the running workload match known-good reference measurements supplied by NVIDIA, achieving zero trust architecture at rack scale. 

 The platform supports both on-demand attestation through NVIDIA Attestation Cloud services and deployment models that require cached results or fully air-gapped operation. This flexibility allows enterprises to meet stringent regulatory, compliance, and data-sovereignty requirements while maintaining operational efficiency. 

 Unified security across the entire rack 

 Vera Rubin NVL72 establishes a unified security domain using a combination of industry standards and NVIDIA technologies, including: 

 
 TEE Device Interface Security Protocol (TDISP) for device-level trust 

 PCIe integrity and data encryption (IDE) for secure I/O 

 NVLink-C2C encryption for protected CPU-to-GPU and CPU-to-CPU communication 

 NVLink encryption for secure GPU-to-GPU data movement at scale 
 

 Together, these capabilities enable a fully encrypted, unified trusted execution environment designed to scale to the world’s largest AI models and most demanding enterprise workloads. From the user’s device to cloud-scale AI factories, Vera Rubin NVL72 delivers full-stack confidential computing that protects every type of data, even the most sensitive workloads, wherever it runs. 

 Energy for tokens: thermal and power innovations&nbsp; 

 AI factories can draw hundreds of megawatts of power. Yet by the time that power reaches the GPUs doing the work, roughly 30% of it is lost to power conversion, distribution, and cooling. This energy is consumed by systems that support compute but do not directly generate tokens, the fundamental unit of AI output. Known as parasitic energy, it represents billions of dollars in wasted potential revenue at scale. 

 
 
 
 
 
 Figure 30. Grid-to-token energy flow and parasitic power loss in AI factories 

 Every watt wasted is a watt that could have been used to generate tokens. As AI becomes a primary engine of knowledge creation, improving energy efficiency directly translates into higher throughput, lower cost per token, and better sustainability. 

 Cutting parasitic energy means delivering more usable power to GPUs, the engines that produce tokens. The Vera Rubin platform has been engineered to minimize these hidden costs through simpler power paths, higher-efficiency cooling, and system-level orchestration designed for always-on AI factories. 

 Traditional data centers heavily rely on air cooling, which consumes significant energy to move and condition air. Similar to Blackwell, Vera Rubin NVL72 systems use warm-water, single-phase direct liquid cooling (DLC) with a 45-degree Celsius supply temperature. Liquid cooling captures heat far more efficiently than air, and by maintaining Blackwell’s 45-degree cooling temperature, data centers can cool water with ambient air. This translates to significant cost, complexity, and power savings relative to other solutions that require 35-degree liquid cooling.&nbsp; 

 Building on Blackwell’s liquid-cooled design, Vera Rubin further increases cooling efficiency by nearly doubling thermal performance in the same rack footprint without introducing new cooling complexities or costs. This ensures rapid heat removal under sustained, extreme workloads, preventing thermal throttling and keeping performance consistent. Less energy spent on cooling means more energy available for compute and higher sustained utilization across the AI factory. 

 Rack-level power smoothing and site-level energy storage 

 AI workloads are inherently dynamic. Large-scale training introduces synchronized all-to-all communication phases with megawatt-scale power ramps, while inference generates sharp, bursty demand spikes. 

 
 
 
 
 
 Figure 31. Synchronized GPU power swings in AI training workloads 

 Without mitigation, these swings can stress power delivery networks, violate grid constraints, or force operators to overbuild infrastructure or throttle GPUs, both of which waste energy and limit deployable compute. 

 Vera Rubin AI factories address this challenge with a multi-layered approach.&nbsp; 

 
 
 
 
 
 Figure 32. Multi-layer power smoothing and energy storage for AI factories 

 At the rack level, Vera Rubin NVL72 evens out power swings with power smoothing and incorporates approximately 6x more local energy buffering than Blackwell Ultra, absorbing rapid power transients directly at the source. The figure below shows the effect of rack-level power smoothing in operation: synchronized AI workload power swings are reshaped into controlled ramps bounded by a stable power ceiling and floor, with local energy buffering absorbing rapid transients at the source. The result is a smoother, more predictable power profile that aligns GPU execution with data center and grid constraints. 

 
 
 
 
 
 Figure 33. ​​Rack-level power smoothing with local energy buffering 

 The figure below breaks this behavior down into the three complementary mechanisms that make it possible. Together, controlled ramps, enforced limits, and local energy storage operate as a coordinated system, reducing peak demand, limiting ramp-rate violations, and stabilizing power delivery without throttling performance. These mechanisms allow AI factories to plan around sustained power rather than worst-case spikes, directly increasing deployable compute per megawatt. 

 
 
 
 
 
 Figure 34. Power-smoothing mechanisms: ramps, limits, and storage 

 At the site level, battery energy storage systems (BESS) provide fast-response capacity to handle grid events and maintain stability without interrupting workloads. 

 AI infrastructure power management works by using the NVIDIA Domain Power Service (DPS) to provide power domain-level controls and enable the NVIDIA Workload Power Profile Solution (WPPS) for each job to optimize performance per watt for schedulers like SLURM and NVIDIA Mission Control. Mission Control provides cluster-wide telemetry, coordinated power-aware policies, and integration with facilities (including energy-optimized power profiles and building management system interfaces) for efficient large-scale operations. Low-level GPU telemetry, power capping, and health control are handled through NVIDIA System Management Interface (SMI) and NVIDIA Data Center GPU Management (DCGM) APIs. 

 
 
 
 
 
 Figure 35. Power stability and energy optimization for AI factory operations 

 By reducing peak-to-average power ratios, Vera Rubin NVL72 enables operators to provision more GPUs per megawatt of available grid capacity, and plan around sustained power rather than worst-case spikes. This improves utilization, lowers infrastructure overhead, and directly increases tokens produced per unit of energy. 

 Power optimization and grid awareness for sustainable AI factory scale 

 AI factories do not operate in isolation. They are tightly coupled to utility grids that impose limits on ramp rates, peak demand, and operational stability. Managing these constraints manually is impractical at scale and can result in forced throttling or downtime. NVIDIA is building a Vera Rubin NVL72 AI factory research center in Manassas, Va. , to optimize and validate the reference design for 100 MW up to gigawatt-scale AI factories. The reference design integrates the Vera Rubin NVL72 rack designs at scale with power and cooling infrastructure and implements APIs to connect grid power controls with the AI factory telemetry and controls. 

 Vera Rubin NVL72 AI factories integrate the NVIDIA Omniverse DSX reference design for software-defined power control. DSX Flex translates electric utility signals into actionable cluster-level power events. DSX Boost enforces ramp-rate compliance and dynamically orchestrates workload power budgets across the factory.&nbsp; 

 Together, these capabilities allow AI factories to remain compliant with grid requirements while keeping workloads running at high utilization. By coordinating power behavior across racks, nodes, and jobs, DSX enables Vera Rubin NVL72 AI factories to provision up to 30% more GPU capacity within the same power envelope, directly increasing token output and revenue potential. 

 A seamless transition enabled by a mature ecosystem 

 
 
 
 
 
 Figure 36. The NVIDIA MGX wall demonstrating the huge ecosystem of partners and components needed to build and scale Vera Rubin NVL72 

 Vera Rubin NVL72 is built on the third-generation NVIDIA MGX rack architecture, preserving the same physical rack footprint while advancing performance, reliability, and serviceability. This continuity is intentional. By evolving the platform without forcing disruptive infrastructure changes, NVIDIA enables exponential gains in AI capability while maintaining a predictable and efficient deployment model. 

 With Vera Rubin NVL72 delivering up to 3.6 exaFLOPS of AI inference compute per rack, the challenge is no longer just performance, but how quickly that performance can be deployed at scale. The MGX design ensures that power, cooling, mechanical integration, and service workflows are already proven, allowing partners and operators to focus on accelerating time to production rather than redesigning infrastructure. 

 This consistency translates directly into faster ramps. Vera Rubin is supported by a mature ecosystem of more than 80 MGX partners spanning system manufacturers, integrators, and data-center solution providers, many of whom are already ramping the platform. These partners bring hard-earned operational experience from prior generations, reducing risk and accelerating global deployment. 

 For data-center operators, this means a smooth transition to Vera Rubin with minimal friction. Existing facilities can adopt the next generation of agentic AI infrastructure without retooling layouts, retraining service teams, or requalifying fundamental rack designs. The result is faster deployment, predictable operations, and the ability to scale AI factories quickly as demand grows. 

 Vera Rubin’s mature ecosystem ensures that platform innovation does not come at the cost of deployment velocity, enabling enterprises and cloud providers to move from innovation to production at unprecedented speed. 

 Where operations meets performance 

 Taken together, these capabilities define what it means to operate at AI factory scale. Vera Rubin NVL72 combines zero-downtime reliability, full-stack security, energy-aware system design, and a mature rack ecosystem to ensure that performance gains translate into real, sustained output in production environments. By removing operational, power, and deployment bottlenecks, the platform allows AI factories to focus on what matters most: delivering more intelligence per watt, per rack, and per data center. With this foundation in place, the next section examines how Vera Rubin converts these system-level advantages into measurable performance gains at scale. 

 7. Performance and efficiency at scale&nbsp; 

 A useful way to understand the performance impact of Vera Rubin NVL72 is through the lens of model evolution. The industry is simultaneously pushing toward extreme-scale training, exemplified by 10 trillion parameter mixture-of-experts (MoE) models, and toward low-latency inference required for reasoning agents and complex workflows. At this scale, the challenge is no longer peak throughput in isolation, but how efficiently an entire platform converts infrastructure into sustained model progress. 

 As the industry has advanced from Hopper to Blackwell and now Rubin, performance gains increasingly come from architectural efficiency rather than brute-force scaling. Vera Rubin NVL72 shifts the performance frontier on both ends, delivering the architectural density required to train giant MoE models without unmanageable cluster sprawl, while also enabling the sustained execution efficiency needed for real-time, high-reasoning inference. 

 Unlocking the 10T MoE era via extreme co-design&nbsp; 

 Training the next generation of frontier models requires extreme co-design. As parameter counts continue to climb, the industry is rapidly approaching a point where 10T MoE architectures become operationally viable. These models offer enormous capacity and more efficient inference, but they introduce substantial communication overhead during training due to dynamic expert routing and frequent all-to-all exchanges. 

 The Vera Rubin platform is designed to absorb this overhead through tight co-design across compute, memory, and networking. Higher compute density per rack and more efficient interconnects reduce the cost of synchronization and expert communication, allowing training efficiency to scale rather than collapse as cluster size increases. 

 The figure below illustrates the impact of this co-design using a fixed training objective. To train a 10T MoE model on 100 trillion tokens within a one-month window, Vera Rubin NVL72 achieves the target using approximately one-quarter the number of GPUs required by Grace Blackwell NVL72. Instead of scaling out to ever-larger clusters to meet aggressive timelines, Vera Rubin concentrates effective training capacity into fewer GPUs. 

 
 
 
 
 
 Figure 37. Vera Rubin NVL72 enables one-fourth the GPUs to train 10T MoE vs. Blackwell NVL72 

 This reduction in required GPU count represents a structural shift in large-scale training. By minimizing cluster sprawl and communication overhead, Vera Rubin NVL72 eliminates much of the complexity that has historically limited MoE scalability. Architectural efficiency, not raw GPU volume, becomes the dominant factor in making 10T-class models practical at scale. 

 Real-time reasoning at scale&nbsp; 

 The shift toward multi-agent AI systems fundamentally changes inference behavior. Instead of short, stateless requests, agents now operate with persistent context, continuously exchanging state across turns and across agents. Each request may carry tens of thousands of tokens, including conversation history, tool definitions, structured API schemas, retrieved RAG context, and intermediate outputs from other agents in the workflow. Maintaining responsiveness under this sustained context load requires far more than peak compute, it demands high sustained throughput across compute, memory, and communication. 

 At the same time, modern “thinking” models, such as Moonshot AI’s Kimi-K2-Thinking, introduce an additional execution phase. Before producing a final response, these models generate long internal reasoning sequences, significantly increasing output token counts. For workloads requiring on the order of 8,000 output tokens, conventional user inference rates, roughly 50 tokens per second per user, translate into multi-minute response times. At scale, this latency compounds across concurrent users, degrading both user experience and system efficiency. 

 Vera Rubin NVL72 is designed to remove this bottleneck. By sustaining high throughput at elevated interactivity levels, the platform enables reasoning-heavy inference without sacrificing responsiveness. The figure below illustrates this generational shift. On the Kimi-K2-Thinking workload, Vera Rubin NVL72 delivers up to 10x higher token factory throughput per megawatt than the NVIDIA Blackwell GB200 NVL72 system at comparable user interactivity. While prior architectures experience steep throughput collapse as TPS per user increases, Vera Rubin NVL72 maintains efficiency across the operating range required for fluid, interactive reasoning. This allows large 1-trillion-parameter MoE models to serve real-time agentic workloads without the “waiting for thought” penalty. 

 
 
 
 
 
 Figure 38. Vera Rubin NVL72 enables up to 10x higher AI factory inference throughput per MW 

 Beyond throughput, Vera Rubin NVL72 fundamentally shifts the economics of reasoning inference. The figure below shows cost per million tokens as a function of output latency for the same workload. For long-context, reasoning-dominated inference, Vera Rubin NVL72 delivers up to 10x lower cost per million tokens compared to Blackwell NVL72. 

 The advantage is most pronounced at the service levels required for interactive agents, where prior platforms may encounter an efficiency wall where costs rise steeply to incrementally improve responsiveness. Vera Rubin remains cost-efficient across this region, transforming long-chain reasoning from a premium capability into a scalable, production-ready service. 

 
 
 
 
 
 Figure 39. Vera Rubin NVL72 delivers one-tenth the cost per token for inference 

 Redefining the Pareto frontier&nbsp; 

 Together, these results redefine the traditional tradeoff between responsiveness and efficiency in AI inference. Where prior platforms forced operators to choose between low latency and reasonable cost, Vera Rubin NVL72 sustains both simultaneously. This enables large-context, reasoning-heavy models to operate interactively at scale, transforming high-intelligence inference from a premium capability into a production-standard service. 

 8. Why Vera Rubin is the AI factory platform 

 AI infrastructure has reached an inflection point. As models evolve toward long-context reasoning, agentic execution, and continuous post-training, performance is no longer determined by any single component. It is determined by how efficiently an entire system converts power, silicon, and data movement into usable intelligence at scale. 

 Vera Rubin has been purpose-built for this reality. 

 Rather than optimizing isolated chips, the Vera Rubin platform treats the data center as the unit of compute. Through extreme co-design across GPUs, CPUs, scale-up and scale-out networking, infrastructure offload, power delivery, cooling, security and system software, Vera Rubin enables AI factories to operate as tightly integrated, predictable, and continuously available systems. 

 At the execution layer, Rubin GPUs deliver sustained throughput for compute, memory, and communication-dominated workloads. Vera CPUs act as high-bandwidth data engines, streaming data efficiently to the GPUs and accelerating system-level orchestration without becoming a bottleneck. NVLink 6 unifies the rack into a single NVLink domain, enabling predictable performance across all GPUs. BlueField-4 completes the stack by operating the AI factory itself, offloading infrastructure services and enforcing security, isolation, and control at scale. Spectrum-X Ethernet and ConnectX-9 then extend this deterministic behavior beyond the rack, enabling efficient, scalable AI factories across multi-rack deployments. 

 Most importantly, these capabilities are not theoretical. They are delivered as a validated, production-ready platform through the DGX SuperPOD, supported by NVIDIA Mission Control, enterprise software, and a mature MGX ecosystem. This design allows organizations to deploy secure AI factories faster, operate them more reliably, and scale them more efficiently as demand grows. 

 The result is a fundamental shift in AI economics. By maximizing utilization, reducing operational friction, and minimizing wasted power, the Vera Rubin platform lowers the cost per token while increasing tokens per watt and tokens per rack. What once required sprawling, fragile clusters can now be delivered with higher density, higher reliability, and predictable performance. 

 The Vera Rubin platform is not just the next generation of accelerated computing. It is the platform that enables AI factories to move from experimentation to industrial-scale intelligence production. 

 9. Learn more 

 Explore the Vera Rubin platform , Vera CPU, Vera Rubin NVL72 , NVIDIA NVLink 6 switch , NVIDIA ConnectX-9 SuperNIC , NVIDIA BlueField-4 DPU, NVIDIA Spectrum-6 Ethernet switch , DGX SuperPOD configurations , and other deployment options at nvidia.com . And read the CES press release . 

 ​​Acknowledgments 

 Thanks to Alex Sandu, Amr Elmeleegy, Ashraf Eassa, Brian Sparks, Casey Dugas, Chris Hoge, Chris Porter, Dave Salvator, Eduardo Alvarez, Erik Pounds, Farshad Ghodsian, Fred Oh, Gilad Shainer, Harry Petty, Ian Buck, Itay Ozery, Ivan Goldwasser, Jamie Li, Jesse Clayton, Joe DeLaere, Jonah Alben, Kirthi Devleker, Laura Martinez, Nate Dwarika, Praveen Menon, Rohil Bhargava, Ronil Prasad, Santosh Bhavani, Scot Schultz, Shar Narasimhan, Shruti Koparkar, Stephanie Perez, Taylor Allison, and Traci Psaila—along with many other NVIDIA product leaders, engineers, architects, and partners who contributed to this post. 
 

 
 
 
 Discuss (2)
 
 
 
 
 
	
 
 Like
 
 
 

 
 
 Tags 
 
 
 Agentic AI / Generative AI | Data Center / Cloud | Networking / Communications | Cloud Services | AI Enterprise | Blackwell | BlueField DPU | ConnectX | CUDA | DGX | Dynamo | GB200 | Grace CPU | Hopper | InfiniBand | MGX | NeMo | NeMo Microservices | Run:ai | Spectrum-X Ethernet | Intermediate Technical | Deep dive | AI Agent | AI Factory | Blackwell Ultra | CES26 | CUDA-X | featured | GB300 | News | NVL72 | NVLink | Rubin | Spectrum-X | Vera CPU | Vera Rubin NVL72 
 

 
 
 
 
 About the Authors
 
 
 
 
 
 
 

 
 About Kyle Aubrey
 
 
 
 Kyle Aubrey is the director of Technical Marketing at NVIDIA, where he leads initiatives in AI inference and training across NVIDIA accelerated computing platforms, including Hopper, Blackwell, Rubin, and beyond. With a passion for demystifying complex technologies, he empowers diverse audiences to harness the full potential of NVIDIA's cutting-edge solutions. Kyle holds a bachelor’s degree in Electrical Engineering from Rose-Hulman Institute of Technology and an MBA from Pepperdine University.
 
 
 
 
 View all posts by Kyle Aubrey 
 
 
 
 
 
 

 
 
 
 
 Comments