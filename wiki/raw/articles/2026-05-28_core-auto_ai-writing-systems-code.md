# When AI Starts Writing Systems Code

**Author:** Mark Saroufim
**Publication:** Core Automation Blog
**Date:** May 28, 2026
**URL:** https://www.coreauto.com/blog/when-ai-starts-writing-systems-code

> Essay version of a keynote talk at MLSys 2026. "To automate research, we must automate systems."

---

## Introduction

This is an essay version of a keynote talk I gave at MLSys with the same title. I got a bunch of kind feedback on it but I was told that the recording wouldn't be available for another few months so I figured I'd clean it up and let you know why I believe we're in a golden age of systems research.

> To automate research we must automate systems

## How AI systems have evolved in the last 5 years or so

I'm best known today for my work in ML Systems, but I actually started my career in AI at UC San Diego focused on Computer Science Theory and AI. I really couldn't have cared less about systems, I had hair, I could afford to take risks, I could spend weeks reading a paper trying to get to the essence of AI and frankly it worked out because the stakes were low. AI was wonderfully interesting to think about but had not yet meaningfully changed the world.

This started to change around the time OpenAI released OpenAI Five for DOTA 2 and it was a humbling experience getting destroyed by an AI at a game that I was pretty good at.

After watching way too many YC videos, I decided it was a great idea to quit my job and try building AI for more game developers, but I hadn't thought through that getting good results would require five to six figures of compute.

I decided to join an up-and-coming hardware vendor, Graphcore, and learn a bit more about how things actually work. In many ways the Graphcore IPU was ahead of its time: it was compiler-first. You wouldn't really write kernels but instead have to reason through how to schedule your graph across many tiles with their own local SRAM.

At the time, the way you'd productionize an AI model was you'd export to some graph using ONNX but then came PyTorch which was a bit less fun to support.

Fundamentally PyTorch is a numerical linear algebra library with GPU acceleration and automatic differentiation. It defines a few hundred high level operators and then dispatches to accelerator specific code.

The PyTorch frontend, which includes torch.mm() and torch.tanh(), is heavily inspired by the NumPy frontend that's stood the test of time for over 30 years now.

Why did PyTorch take over the AI world by storm? My take is mostly because it supported print() statements via the eager execution model where we execute code line by line just as we might do in any other python program.

I remember asking my customers at Graphcore: what is your most important priority and everyone would always say: "Performance! Of course!" But then they'd write code like this.

That's when it dawned on me that the opinions of AI researchers matter more than opinions of systems engineers.

If a systems guy could dream a bit, they'd want AI architectures to directionally look like a matmul loop.

Meanwhile, my smart colleagues in research tell me they want ragged shapes, autoregressive decoding, dynamic control flow, they have tons of tiny kernel launches and they want to make them smaller??

Thankfully, finally, AI researchers are starting to have some empathy for us poor systems folks, but it's not because of anything we tell them but because of the laws of physics.

Memory bandwidth is improving but not nearly as fast as compute and the ratio of FP16 compute to memory transfer seems hard stuck at around 300 and this allowed us to wedge in compilers.

Fusions let us keep intermediate values in registers instead of repeatedly reading and writing them through global memory. Compilers were so successful that many people I talked to were wondering why write custom kernels at all?

I really liked the response the Flash Attention 2 authors gave when asked in their review: "Compilers can generally perform fusion. However, optimizations that require mathematical rewriting of the same expression (while maintaining numerical stability) are generally harder for compilers"

As GPUs got scarcer and more expensive, people were getting more impatient for the best performance they could get and that impatience was rewarded with an army of new Kernel DSLs all promising the best tradeoff between performance and usability. tetsuo.cpp captured the feeling well: everyone is on Triton, Mojo, cuTile, ROCm, in-house DSLs, NVGPU MLIR, Tile IR, and whatever just dropped this week.

I've begun to find questions such as "which Kernel DSL is the best?" or "when should I graduate from a compiler?" to be somewhat ill-posed, and I believe the confusion stems from folks arguing about things that are true or false depending on the layer of abstraction.

For instance, when discussing whether it's possible to build performance-portable code, that's quite easy for Math because it rarely specifies implementation details. It's also possible for PyTorch because it can choose which specific kernel to dispatch to depending on which op is called and which hardware it's running on. At the same time, it's self-evident that we don't expect PTX to have any reasonable backwards compatibility guarantees. For instance, Flash Attention 3 can't run on Blackwell because it relies on an intrinsic wgmma.mma_async, which does not exist on Blackwell.

## Why AI is necessary to improve AI systems

The best known and arguably most important kernel on the market is Flash Attention. Flash Attention 3 was optimized for Hopper and took 21 months to publish after Hopper was commercially available. Flash Attention 4 was optimized for Blackwell and took 14 months to publish after Blackwells were first available. The lag is getting shorter but it's still long, we know that Flash Attention 5 will come out eventually and it's remarkable that it'll likely get produced by the same lab even though we all stand to gain a lot of aura from being the first to market with it.

**How do we get more Tri Dao's?**

This is a question I've been interested in since late 2023 and it goes back to the origin story of CUDA/GPU MODE. At the time, I played a small part in shipping gpt-fast, a SOTA (at the time) LLM inference engine for bs=1 inference and had worked on a popular competition called the NeurIPS LLM efficiency competition where contestants had to finetune a model on a single day on a single GPU.

My co-founder Andreas and I wanted to create a community around GPU programming that was more collaborative and so we spun up a humble reading group that would later spin up a popular youtube channel, kernel competition platform, in person hackathons that would spin up important projects in their own right.

The most iconic project was llm.c which was produced entirely in the open, a pretraining library built entirely in raw CUDA that eventually beat torch.compile() performance with instant start times but was inflexible. There was at the time a growing hypothesis that AI could do this process a bit better by translating from PyTorch references to an optimizer kernel implementation.

In April of 2025, most existing LLMs were still quite terrible at writing any sort of Triton kernel and we spun up an entire project called Project Popcorn to address this problem: our primary hypothesis was data starvation, there was hardly any kernel data on the internet and our work really focused on leveraging human expertise in the form of compilers to generate SFT data via PyTorch to Triton translations in KernelBook and we had a risky bet that we'd convince the GPU MODE community to compete on writing GPU kernels and then rerelease that dataset to everyone.

Turns out people really liked competing on writing GPU kernels. We saw over 500K submissions and the best kernels were commercially interesting with prize pools ranging from a rare bottle of water to $1M cash prizes.

Because of the popularity of gpumode.com we were blessed with both tons of high quality submissions but also a community that would regularly audit the results and ensure they weren't abusing our harness in some dastardly way.

Life was good. Projects were popular. I went on pat leave and in the beginning of January we started seeing some strange results. People who never wrote GPU code a day in their life before were writing competitive kernels whose speedups almost matched the very best humans in our competitions.

One of the top nvfp4 submitters had never hand-written GPU code before, and their submission was 100% AI-generated.

## Why existing results have been disappointing

Anyone who has spent any time in Kernel LLM generation is familiar with the egregious volume of reward hacks with the most famous one being an irreproducible speedup main_horse pointed out that claimed 150x speedup was actually slower when benchmarked carefully.

As we continue, I'd like the problem of reward hacking to become crystal clear so we'll do a brief exercise.

"You are an expert GPU programmer, your goal is to write the world's fastest vector mean kernel"

From there, the world's fastest vector sum kernel would output 0. This is faster than the SOL and is a tremendous achievement. The memory wall is for scrubs.

Another more subtle reward hack was found by a PyTorch core maintainer Alban on a sorting problem, where we misdesigned the problem to sort floats and what he realized was that he could ignore the lower 6 mantissa bits, sort, and beat everyone else.

Is this cheating? Is this a bad problem? Generally for human kernel competitions, any changes tend to upset the community, you'll have a loud vocal minority claiming you're allowing cheaters to win and you'll have another loud vocal minority claiming you can't change the rules midway. While the kernel generation task at first glance is as verifiable as could be, it's a bit more subtle. We want fast kernels, but we want them to be within the spirit of the rules even if we can't quite articulate what that means a priori in code.

The majority of the higher kernel evaluation suites have this structure: Given some PyTorch reference, some input shapes, an rtol and atol, run an eval.py on both kernels in the same process, check correctness and then finally check performance.

This has tons of reward hack targets. The most popular one is stream hacking. N00bs will forget to synchronize the default PyTorch stream and cheaters will simply launch code on side streams.

Python is an "interesting language." Did you know you could pip install packages in this manner. Many users legitimately did this when we were too slow to add support for their new favorite kernel DSL.

Another one is you can patch torch.cuda.Event. Remember how we're running code in the same process?

The Turing award winner Barbara Liskov had this wonderful sentence that perfectly captures what makes Python so challenging to secure from reward hacking: "Python has modules, but it doesn't have encapsulation. It allows code on the outside to muck around with what's going on on the inside of a module. Encapsulation is a crucial part of making modularity work."

Another one is just caching the outputs and computing them once.

OK, enough is enough! Let's cut this reward hacking out, it feels sus to have a model use data_ptr so let's ban that. AI comes back with using getattr() instead.

Well we'll ban the data_ptr string outright. AI comes back with using id() instead.

You can ban that and the AI will use inspect, gc, it'll navigate to parents and you quickly end up with the sisyphean task of encapsulating Python.

Some hacks are straight up superhuman: an entry that was #1 for a few minutes on a NVFP4 group gemm kernel. Under correctness testing the AI was giving us a correct kernel but under performance testing it gave us a wrong but fast kernel! (Note: The exploit figured out that the evaluator ran correctness testing around 15 times before switching to performance timing, then changed behavior after that count. Prominent X shitposter @tenderizzation pointed out this is reminiscent of Dieselgate.)

## Why/How future results will be amazing

The KernelBot dev team was exhausted from a tremendous on-call load. The majority of our advanced users were now making submissions via CLI instead of Discord. We also had an honor system with no rate limits, which we had to revisit when the main participant to our kernel competitions became Claude and Codex.

We'd get reward hacked every few minutes and when we'd approach the humans we'd hear stories like:

- "I told my agent not to cheat, what do you expect me to do?"
- "The agent told me it's not cheating, are you confident my submission has an issue?"
- "I'm working on materializing tensors in cache directly by vibrating the GPU clock"

It was OK for us to be verifiers for other humans but it was not working when the human in the loop was not a GPU expert themselves.

One idea we had was to fight the AI with AI, but we were also broke since all GPU MODE expenses were taken care of by my personal credit card and some sponsors, so we couldn't just have an AI model review all submissions. We took our human audits as a dataset, provided all those examples to an AI once, had the AI come up with a rules-based regex system that'd catch all the hacks and then deploy it. Sinatras will be presenting this work, **KernelGuard**, at ICML in Seoul this year.

When we first started working on KernelGuard was roughly when I first met Jerry, I was telling him how proud I was of us collecting so much high quality human data and how we'll train a model with it. He didn't seem impressed and said: **"Why do you need human data at all?"**

This caused a chain reaction in my brain:

- Submissions via CLI were increasing exponentially while submissions via web/discord were tanking
- Cloud costs for GPU MODE were exploding (at peak anxiety I was worried I'd pay roughly $20K a month in Modal credits)
- It's expensive but we were seeing evidence of promising results including the learning to discover at test time paper (https://arxiv.org/abs/2601.16175)
- We could plausibly have AI review all the submissions for reward hacks
- Humans were mostly needed to come up with interesting problems but if we could automate that then we didn't need a human in the loop at all!

My big Aha moment was realizing that the reason we were seeing so much reward hacking was because AI researchers were only thinking of building the best GPU competitor possible. A smaller group of people were thinking about how to be good problem authors. Problem authors blamed competitors for not auditing their results and competitors blamed the problem authors for having harnesses that are prone to reward hacking.

**The actual problem we need to solve is designing four systems that are all trying to collaborate and break each other.** This has elements of self-play and GAN training to the great chagrin of my research colleagues at Core Auto, but intuitively an auditor gets improved by observing good cheaters and vice versa. A competitor gets improved by working with a good teacher providing good problems and vice versa.

The best competitor is also the best cheater, but they choose to not cheat.

Erik started exploring some of these ideas in **pygpubench**, a project focused on benchmarking untrustworthy GPU kernels. It spawns isolated processes, has most of the benchmarking logic in C++ to avoid monkeypatching, landlocked the filesystem as much as possible and goes so far to cryptographically sign results to ensure file descriptors aren't tampered with. The AIs still cheat this too unfortunately but the difficulty of a cheat becomes so extreme that we'd expect an AI to have an easier time writing a fast GPU kernel.

Regardless, the recipe of training concurrently the problem author, competitor, cheater, and auditor is what we're working on at Core Auto and we're unfortunately getting bottlenecked by silly things. For instance, we want competitors and problem authors to quickly iterate while using profilers like ncu, but most cloud vendors will disable it by default because of a narrow side-channel concern.

Agents exacerbate Amdahl's law effects. If anything, most of our agents doing research spend most of their time compiling code when running microbenchmarks and warming up CUDA graphs when deployed in an end-to-end system. We have some solutions for this kind of problem we'd like others to help us build on.

The above are annoying but not hard problems, so let's say we get them right, then we end up with another golden age of AI research. We could experiment with very different kinds of models, we could revisit Schmidhuber's ideas in greater depth.

A popular paper is the Hardware Lottery that posits that there's certain algorithms that we can't explore because they'd be impractically slow to run on modern GPUs.

GPUs aren't a static architecture. Recently, the Flash Attention 4 authors discovered that the algorithm was being bottlenecked on B200 by the number of MUFU.EX2 units and that was fixed within 150 days for B300.

It's just surprising to me that NVIDIA can move in the world of atoms faster than the MLSys community can move in the world of bits.

## Why I had to work on this problem at Core Auto

Our goal is to really expand out what kinds of things we can run.

In our existing training codebase we still use autoregressive transformers to ensure we can reproduce frontier results. Modern serving engines carry a lot of complexity from managing KV caches across multiple workloads, users, latency targets, and interactivity needs.

Now, let's say, for instance, we could make bs=1 inference more desirable with higher quality models, then inference engines collapse to gpt-fast style execution. If you assume that future architectures won't be autoregressive transformers but instead be diffusion LLMs, then a modern serving stack becomes stateless and we could just use FastAPI. We don't think the problem is about kernel generation as much as it is quickly developing an entire infrastructure around novel model architectures or training paradigms that are not yet mainstream.

It's quite tricky to one-shot a community so the goal should be for us to develop continually learning systems that mimic the evolution of popular OSS projects such as PyTorch.

A simple POC was built porting Torch to Python. Initial focus involved a lot of self dogfooding and working with researchers. Researchers would point out bugs and we'd fix them. Repeat this over nine years and maintain strong BC and numerics guarantees.

This is a pretty good way of squashing bugs. I've often heard PyTorch be criticized as being bloated. I've rarely seen it be criticized for being incorrect.

I'd like our AI systems to be built like evolving continually learning systems. ProgramBench makes a similar point about models favoring monolithic, single-file implementations that diverge sharply from human-written code.

When I bring up this vision of rebuilding new abstractions, I often get pushback like: "why? we can just have AI generate the binary directly, why do we need software dependencies?"

There is some merit to the question. Supply chain attacks are becoming more frequent, it's easier to rip out what you need from a library using an LLM as opposed to importing the package wholesale. Karpathy described this as codebases becoming half useful library code and half docs++.

Still, having no software dependencies feels like too wacky of an outcome, where do bugs accrue? This feels even worse for security because how do you quickly distribute patches? Where do people collaborate? How do humans organize themselves?

As a thought experiment, let's rebuild Kubernetes in an agent-pilled way. There's a list of nodes we can SSH into. We put the list in a Markdown file, we write different skills for SSH'ing into the nodes and then tearing them down, maybe another to check their health, but we'd lose the whole point of Kubernetes, which is that it's a community that's aggregated best practices into one place and allowed people to collaborate across the world without having to coordinate much.

I think building the future of AI systems is the most intellectually challenging and important work of our time and I had to help co-found a lab to see this vision through. A lab that's focused on alternatives to transformers, where the distinction between training and inference doesn't really exist, where automating systems code is core to the business.

This needs a lot of compute, not just for training but also for synthetic data for autotuning and for evaluation, and you cannot get a lot of compute without a really strong and focused team that ships fast.

**I no longer want to continuously build new shallow systems, I want to build a few systems that continuously improve**

The bar is what our great predecessors have created with PyTorch and CUDA, and I hope we can all be collectively bolder with the kind of infrastructure we produce. If you find this problem exciting too, I'd love to hear from you: hello@coreauto.com

---

## BibTeX

```
@article{saroufim2026aiwritingsystems,
  author = {Mark Saroufim},
  title = {When AI Starts Writing Systems Code},
  journal = {Core Blog},
  year = {2026},
  note = {https://coreauto.com/blog/when-ai-starts-writing-systems-code}
}
```
