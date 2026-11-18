SOURCE: https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

Cerebras Launches Disaggregated Inference 
 Skip to main content 

 Nov 17 2026
 Cerebras launches disaggregated inference
 Atharva Talpade 

 We’ve deployed Cerebras Wafer Scale Engines with GPUs to deliver lightning-fast tokens at scale 
 The world is hungry for ultrafast tokens. In 2026, Cerebras saw an insatiable demand for fast inference, both on our inference cloud and via our partners. To meet demand, we began developing disaggregated inference: GPUs handle prompt processing (prefill) and Cerebras systems handle output generation (decode).
 This solution is now in production and delivers five times more tokens per megawatt at the same ultrafast Cerebras speeds. 
 We can now serve more ultrafast tokens via Cerebras Inference Cloud to meet market demand. Infrastructure partners can also leverage the Cerebras disaggregated solution to achieve more ultrafast tokens in their own datacenters.
 Alongside our recently announced CS-4, our dramatically scaled manufacturing, and our planned 700MW of data center capacity, disaggregated inference will enable Cerebras and partners to serve many more ultrafast tokens in 2027 and beyond.
 In this blog we cover:
 The need for more ultrafast inference capacity
 Why Cerebras is advantaged for decode
 Cerebras disaggregated inference production results
 Cerebras disaggregated inference for infrastructure partners
 The need for more fast inference capacity
 Agentic applications like Muse, Copilot, and Codex are scaling rapidly and require highly interactive inference to keep users engaged. To meet the growing demand of these applications in a power-constrained environment, our industry must deliver significantly more inference capacity per megawatt, at response speeds that make these applications useful.

 Sources: Goldman Sachs Research, “AI Agents Forecast to Boost Tech Cash Flow as Usage Soars,” May 20, 2026; Goldman Sachs data center capacity estimates, as reported by Investing.com, November 6, 2026. 

 That is why Cerebras invested in disaggregation . Pairing a prefill accelerator for prompt processing with the Cerebras System for response generation increases token throughput per megawatt while preserving Cerebras’ ultrafast generation speeds. For inference providers, that means more capacity to serve customers and greater revenue potential from the same power budget.

 Why Cerebras is advantaged for decode
 An inference request has two main stages. Prompt processing, known as prefill, processes the input and produces intermediate model state. Response generation, known as decode, uses that state to generate output tokens. There are many ways to split the inference workload, including draft–target and attention–FFN among others, but separating prefill from decode is uniquely advantageous when the goal is highly interactive inference.

 Decode is autoregressive. That means the model generates one token at a time, using each generated token as an input to generate the next. Each step means reading model data from memory again, so memory bandwidth matters a lot. In the ultrafast inference domain, SRAM-centric chips have an advantage because they can keep that data on-chip and read it much more quickly. Cerebras takes this to wafer scale, with tens of gigabytes of SRAM and tens of petabytes per second of memory bandwidth on a single chip—350× the SRAM capacity and 5,400× the memory bandwidth of a typical GB300 GPU. This allows the Cerebras System to fit more concurrent requests and model layers directly on the chip, enabling the CS-3, CS-4, and CS-5 to achieve ultrafast speeds at an attractive throughput.

 Cerebras disaggregated inference production results
 Pairing Cerebras systems, which are optimized for ultrafast decode, with accelerators well-suited to the compute needs of prefill, such as AMD Instinct GPUs, allows the delivery of an immense amount of ultrafast inference at scale. In a production deployment on the Cerebras Inference Cloud, AMD Instinct GPUs process prompts, and Cerebras CS-3 systems generate responses. Moving prompt processing to GPUs allows Cerebras systems to devote their serving capacity to response generation. In our measured production deployment, this combination delivered 5X the throughput per megawatt of a CS-3-only configuration, with no loss in token generation speed.

 Source: November 14th shared GPT-OSS-120B endpoint via the Cerebras Inference Cloud throughput per megawatt before and after enabling disaggregated inference, normalized to the aggregated inference baseline (1×). 

 We plan to deploy disaggregated inference broadly across hundreds of megawatts in the Cerebras Inference Cloud and in partner deployments by the end of 2027. Our aim is to increase the ultrafast inference capacity available for our customers.
 Cerebras disaggregated inference for infrastructure partners
 The Cerebras disaggregated inference solution was also built for our partners to adopt. Infrastructure partners can deploy disaggregated inference clusters based on Cerebras-provided reference architecture, co-locating their chosen prefill accelerators and Cerebras systems within a unified network. For software integration, partners can either integrate with the Cerebras end-to-end disaggregated software stack or a decode-only SDK.
 The end-to-end disaggregated software stack is best suited for partners optimizing time-to-market. It consists of:
 A disaggregated inference framework to route requests between prefill and decode pools and manage replica capacity and health.
 A prefill engine to process prompts using open-source inference engines like vLLM or SGLang.
 A Cerebras decode engine for response generation on Cerebras systems.
 KV Portal software, an interface to transfer intermediate model state, including key-value caches, between prefill and decode engines over RDMA.
 The decode-only SDK is best suited for partners optimizing for control. With the decode-only SDK, partners can bring their own inference framework and prefill engine to the Cerebras decode engine and KV Portal software. In addition, the decode-only SDK provides development aids such as a mock Cerebras decode replica and a reference integration to an open-source disaggregated inference framework and prefill engine.

 Trace a request 

 Early-access partners, including Amazon Web Services, Fireworks AI, Gimlet Labs, and General Compute, already have access to the Cerebras disaggregation solution for their deployments. We are now expanding access to additional partners looking to bring ultrafast inference to their customers at scale.
 To discuss the results, solutions, or deployment opportunities in more detail, contact us here .

 Follow

 Get Updates
 Newsletter Signup 

 Company
 About Us 
 Careers 
 Contact Us 
 Investor Relations 
 Website Terms of Use 
 Privacy Policy 
 Cookie Policy 
 Other Terms & Policies 
 Service Status 
 Trust Center 

 News
 Newsroom 
 In the News 
 Press kit 

 Insights
 Customer Spotlight 
 Blog 
 Publications 
 Whitepapers 

 Performance comparisons are based on third-party benchmarking or internal testing. Observed inference speed improvements versus GPU-based systems may vary depending on workload, configuration, date and models being tested.
 info@cerebras.ai Your Privacy Choices 
 1237 E. Arques Ave 
Sunnyvale, CA 94085

 © 2026 Cerebras. 
All rights reserved.