---
title: "Vibecoding an inference chip"
source: https://ankitg.me/blog/vibecoding-inference-chip/
date: 2026-11-21
type: article
sha256: 0f95cecb895ad3b0dc0df03e7a4c169d078b65cfef81515e2db7bb9bc7cb08d5
---

> HN discussion: https://news.ycombinator.com/item?id=50579297 (152 pts)

Vibecoding an inference chip 

 Ankit Gupta 

 Blog 

 Contact 
 
 /

 Github 
 
 /

 Vibecoding an inference chip

 Or rather, I vibe-coded an FPGA into running an LLM. And it… just worked.

 Friday. November 20, 2026 

 One of the more entertaining things about programming recently is that coding agents let me work in entirely new domains by giving me access to new programming languages and paradigms. Lately, that has meant hacking on hardware, now that writing low-level software is much easier. So, in this blog post, I’m going to try to recount the experience of vibe coding an FPGA, going through a series of “oh shit” moments several times, and giving myself a new appreciation for what’s possible if you have a large token budget (thanks YC) and interesting problems to point the models at.

 I overheard some founders recently talk about how FPGAs work. I’ll admit I was relatively naive about them. I’d never really experimented with them in my startup or in college, so I knew little about them before. The basic idea I was familiar with: you can program a circuit into a reprogrammable chip. So rather than having a general purpose computing architecture (like a CPU) you can have a reprogrammable one, i.e. the configuration loaded onto the chip determines how its logic and routing are connected, and that (in theory) enables performance advantages. I also know that it took a mountain of C++ to write and involved manually analyzing waveforms for simulation and verification. I had never done this before though and it seemed cumbersome.

 That’s about what I knew going into this.

 Naturally, my ML brain thought “could we use these for AI inference”. I’m not the first to think this — there are a few repos attempting to port ML models to FPGAs on Github. But I hadn’t actually seen a writeup on whether coding agents are good at writing the low level C++ and Verilog code to program them and verifying the outputs so that they actually run accurately. (Spoiler alert, they are incredible at programming them.)

 So I decided I needed to get my hands on one. AWS has F2 instances with FPGA hardware, and that seemed easier than going and buying physical hardware, so I asked Codex to spin up a reservation and got cooking. It had a relatively limited memory of 16 GB of FPGA HBM. Around the same time, I was working with the DeepGrove founders who were discussing their new ternary weight architecture that is well suited for memory limited cases. It’s SOTA on Mac hardware with actual agentic tool calling, so I figured why not, let’s see if I can get this working on an FPGA and fast enough to be useful.

 What followed was a cloud agent running in Conductor for several days with me mostly just encouraging it periodically while it both (1) got a model fully running and (2) increased its speed by 33× from the first full-model bit-exact baseline to get it to a real-time relevant speed. It was one of the most mind blowing autoresearch loops I’ve run, ultimately writing roughly 3M lines across the experiment history and parsing 30M lines of output files, burning only $10,000 in Claude and OpenAI tokens to run hundreds of experiments. Most of the code is C++ and some Verilog. It’s been probably a decade since the last time I wrote any serious amount of C++ and I’ve never written Verilog. I honestly don’t know the first thing about Verilog. Most of my prompts were not particularly clever: they consisted mostly of me saying things like “you’re a superintelligent model, time to be more creative” and “let’s go for 2x faster, you got this”. Sometimes I brought some ML knowhow like “hey it’s time to consider speculative decoding” or “why is that running on CPU, you should port it”. But for the most part, it was just vibes and I’m pretty sure that with enough time the model would have figured out those things. Also, it seemed that both Astra and Opus (new Fable wasn’t out yet) were pretty capable at this and I could use them interchangeably. I’m sure someone has a good benchmark for which is smarter but both passed my smart-enough threshold.

 Summary of my most impactful prompts. Most of that first third is just getting AWS set up and approving quota for f2 instances. 

 From “it works” to 213 tokens per second

 Getting faster, one experiment at a time 
 Measured benchmark tokens/s · select a step to see what changed

 Baseline 
 
 6.43 

 Host overhead 
 
 8.07 

 Burst attention 
 
 14.02 

 Parallel router 
 
 20.53 

 Glue engine 
 
 30.24 

 New pipeline 
 
 49.21 

 Prompt speculation 
 
 51.25 

 Router relay 
 
 58.43 

 Head shadow 
 
 94.44 

 Draft model 
 
 105.63 

 Memory ports 
 
 108.81 

 Attention overlap 
 
 134.99 

 Weight packing 
 
 171.3 

 Re-speculation 
 
 184.19 

 Parallel head loader 
 
 213.13 

 Step 14 · 33.13× baseline 
 A head loader that reads both of its memory banks at once (+17.3%, measured on and off on one image), a runtime expert-prefetch policy, and the router-job timing fix; run one clock step lower (225/425 MHz) after a soak test found random faults at 231.25.

 The chart follows the measured optimization sequence: 6 → 213 tokens/s , or 33× the baseline.

 How much did the human advice help?

 At one point, around when it got to 10 TPS, I messaged the DeepGrove founders about this, and they replied surprised that it was working so easily, saying they had tried this a few months back and the models were not quite good enough to be particularly effective. They sent me a prompt that summarizes some of their lessons and I copy-pasted it into my session to see if it’d matter. It was essentially the most significant piece of actual guidance I added to this session. The prompt is reproduced below.

 Read the full FPGA design prompt 

 here is what someone else did for a dense bs=1 decode optimized fpga implementation for a dense qwen style model with ternary weights. you should take this with a grain of salt and pick things that you believe are acutally useful to add to your plan. Please also dont do things if you dont think is useful that take a lot of times like runnning really long test of a cycle accurate simulation etc or like physical design since those can take like hours. here are some ideas please pick and choose use this as context and not somehting that you shoudl be strictly guided by somethings that could help. prioritiize speed of like getting this up and running though..

 MATMUL (TERNARY ENGINE)

 No multipliers. A 2-bit weight drives a 3:1 mux that picks x, ~x, or 0.
The unused 4th code raises an error flag, so corrupt weights get caught.

 Negation is ~x + 1. Lanes flag negatives, and the row reducer adds the +1s
once per row instead of once per lane.

 Activations are grouped integers: INT12, or INT16 where we needed more
range (MLP down projection). Reduce as integers, apply FP32 group scales,
accumulate in FP32.

 The pre-projection RMSNorm is deferred: quantize the activation first,
apply the normalization scale after accumulation. It’s cheaper and
numerically equivalent.

 8 cores in two clusters. Projections that are independent (gate/up) run
at the same time on separate core groups.

 Result: about half the DSPs of an INT8/INT16 design at the same rate,
traded for more LUTs.

 MEMORY

 Weights are packed at 2 bits, 8x more per transfer than 16-bit. At batch 1,
weight fetch costs far more energy and time than the math.

 Weights stream from HBM straight into the compute lanes and skip the
on-chip buffers (they’re used once per token). Activations are cached next
to each core and reused across rows.

 HBM routing is one chain per memory channel instead of a big crossbar.
Lay out data so all 32 channels stay busy.

 On-chip buffers are typed slots with an explicit lifecycle
(open -> write -> commit -> read -> release). Each slot has a side memory
for scales/exponents. The buffer checks format, range and producer, which
catches scheduling bugs in hardware.

 The KV cache is MXINT8: 8-bit values with one shared exponent per
32-channel block. That’s small enough to stream, with accuracy held.

 For MoE: stripe each expert across every channel, and map expert ID to
address at runtime instead of using a fixed program.

 ATTENTION

 Attention streams over the cache in 64-token tiles with an online softmax
(FP32 running max/sum). The full score matrix is never stored.

 Probabilities are UINT16 and the context accumulates in FP32.

 Each attention unit interleaves two independent jobs on one datapath
(C-slow), which hides pipeline latency without duplicating hardware.

 Q/K head norm and RoPE got their own small vector unit, so they don’t
block the general vector path. The V projection overlaps with that work.

 New K/V is appended to HBM as soon as it’s produced. We used a sliding
window to bound cache reads.

 SCHEDULING

 One controller issues work in program order, with tags and barriers.
Engines overlap only when the buffer dependencies are explicit, so we got
overlap without races.

 For MoE: the router is the new critical path, because nothing can fetch
until it finishes. Keep it in FP32 (lower precision changed which experts
were picked), and overlap whatever you can around it.

 CORRECTNESS (maybe not neecessary to folow super close)

 We fixed a numerics contract first (formats, rounding points, operation
order) and built hardware to match it. Vector ops must match the reference
model’s order and precision, not just be “close”.

 Verification ladder:
 
 Per-block cocotb unit tests.

 One full layer co-simulated against the real checkpoint.

 Multi-token, full 24-layer decode compared token-for-token with a
reference oracle.

 Byte-level accounting of KV cache writes.

 We kept simulation results, timing signoff and board results separate,
and never claimed one from another.

 Every published number links to the report it came from.

 PHYSICAL DESIGN (maybe not necessary for u)

 The chip has 3 regions (SLRs). Keep wide datapaths inside one region and
register every crossing. Long links use credits, not combinational ready.

 We placed engines next to their data: memory logic near HBM, attention in
the DSP-dense region.

 Screen logic depth (10 levels max at 250 MHz) right after synthesis, and
fix it with pipelining, sharding, or C-slow. Full place-and-route is
saved for integration.

 Dev loop: small change -> lint -> unit test -> quick synthesis ->
depth/timing check -> restructure.

 The coding agent diligently considered these asks, but it didn’t seem to make all that much of a difference qualitatively. Indeed, when I asked it later to read all of the logs and determine which of these instructions it actually used, it said:

 Read the agent’s retrospective: what it adopted and rejected 

 Its biggest design ideas were already in my plan before you pasted it.
You pasted it on Oct 29 at 21:50 UTC: 4,741 characters describing what someone else did for a dense, batch-1, ternary FPGA decoder. Within 70 seconds I had sorted it into ten ideas to adopt and five to reject, and written that into every design agent’s brief. The shorter remark from your friend Edward, about using lookup tables as logic gates, came 24 minutes earlier and left nothing on the speed line.

 Design ideas I adopted: mostly confirmation. 

 Already planned: streaming weights straight into the compute lanes, running rows in parallel, and reading the attention cache in bursts were all in the design brief I’d launched 35–40 minutes earlier.

 Match what was later built:
 
 interleaved lanes in the router (step 3);

 a separate unit for head norms and RoPE (step 4);

 a program-order sequencer (step 5);

 a registered boundary on every crossing between dies (steps 8 and 12).

 I can’t show these wouldn’t have happened without the notes.

 Ideas I rejected: all five numerics shortcuts. 
 Lower-precision activations, a deferred norm, an 8-bit KV cache, online softmax and 16-bit probabilities each change the output bits. That is where their design got its efficiency, and your bit-exact rule ruled it out.

 Process advice: this changed things right away. 

 What you asked: not to do things that take hours.

 What I stopped: a simulation that had run for about 24 hours, and two 250 MHz builds.

 What I switched to: a short loop of C tests, synthesis and a logic-depth check, with one place-and-route per integration.

 Likely gain: it got hardware results sooner.

 Possible cost, which I can’t prove: two hangs that only RTL simulation could show reached the board the next day, and the big integration lost 38 hours to them.

 One real find it triggered. 
 While checking their memory ideas, I found AWS’s own reference memory design, which reaches 426 GB/s across all 32 memory channels. The memory subsystem was built from it.

 In other words, for most of the actual design ideas it is unclear but there is good reason to believe the model would have figured them out, especially because it came up with them many cycles later after several compaction cycles. But the process advice was useful immediately for getting to hardware results sooner and increasing iteration speed. In other words, the humans are still useful at defining how to iterate fast and what correctness looks like, and the agents are great to manage the exploration.

 The optimization log

 Here are the changes the autoresearch loop found. Interestingly, it’s mostly a series of modest improvements that compound 1.5x ish every time, rather than one or two giant ones.

 0 Baseline 6.43 tok/s 
 
 Baseline: the first full-model bit-exact FPGA image (R8), served with host-side prefix caching.

 1.0× from baseline

 1 Host overhead 8.07 tok/s 
 
 Host software only: per-command overhead fell from ~10 ms to 0.9 ms (persistent register mapping, streaming reads, no per-command SDK calls or fsyncs).

 1.25× this step · 1.25× from baseline

 2 Burst attention 14.02 tok/s 
 
 A 128-lane attention engine that reads the KV cache in bursts instead of a word at a time, keeping the reference's exact summation order.

 1.74× this step · 2.18× from baseline

 3 Parallel router 20.53 tok/s 
 
 A parallel MoE router with an exact GCC-sort tie-breaker plus a streaming output head with built-in argmax; moderate-effort routing let it run at 250 MHz.

 1.46× this step · 3.19× from baseline

 4 Glue engine 30.24 tok/s 
 
 A glue engine that parallelizes norms, RoPE, quantization and copies between engines in certified exact orders.

 1.47× this step · 4.70× from baseline

 5 New pipeline 49.21 tok/s 
 
 The full new pipeline (streaming ternary projection lanes + a new sequencer replacing R8's control path), after fixing two hangs that only appeared in hardware.

 1.63× this step · 7.65× from baseline

 6 Prompt speculation 51.25 tok/s 
 
 Exact speculative decoding: the host drafts tokens by prompt lookup and the FPGA verifies several in one pass.

 1.04× this step · 7.97× from baseline

 7 Router relay 58.43 tok/s 
 
 Fixed a relay that moved router weights between dies at 1/6 speed: router stall per layer 43,862 → 12,292 cycles.

 1.14× this step · 9.08× from baseline

 8 Head shadow 94.44 tok/s 
 
 Head shadow v2 (start the next token on a provisional guess; catch misses early) plus cross-die timing fixes, enabling 237.5 MHz kernel / 450 MHz memory.

 1.62× this step · 14.68× from baseline

 9 Draft model 105.63 tok/s 
 
 Exact speculative decoding with a real draft model: a cut-down Maple on the F2's host CPUs drafts ahead, and the FPGA verifies every token.

 1.12× this step · 16.42× from baseline

 10 Memory ports 108.81 tok/s 
 
 Doubled the memory ports from 4 to 8 (two projection lanes, output head striped across banks): 1.39× per clock, but congestion cut the clock to 181/375 MHz.

 1.03× this step · 16.91× from baseline

 11 Attention overlap 134.99 tok/s 
 
 Hid the attention engine's KV fetches behind its compute, and replaced the router's 2,048-step serial sum with an exact order-independent one (12,292 → 2,338 cycles per layer).

 1.24× this step · 20.98× from baseline

 12 Weight packing 171.3 tok/s 
 
 Lossless 5-trit weight packing (−20% weight bytes), shorter serial steps, and moving the output head to the far die, which relieved congestion and allowed 225/400 MHz.

 1.27× this step · 26.63× from baseline

 13 Re-speculation 184.19 tok/s 
 
 Re-speculation after head-shadow misses, speculative MoE expert prefill during the router, and a die rebalance (without the unused DDR controller) that ran 231.25/450 MHz on both boots.

 1.08× this step · 28.63× from baseline

 14 Parallel head loader 213.13 tok/s 
 
 A head loader that reads both of its memory banks at once (+17.3%, measured on and off on one image), a runtime expert-prefetch policy, and the router-job timing fix; run one clock step lower (225/425 MHz) after a soak test found random faults at 231.25.

 1.16× this step · 33.13× from baseline

 How it compares

 It’s difficult to do a 1:1 comparison across these configurations. I didn’t run the same autoresearch loop on every alternative, and I assume there is more performance to extract if I did. The point is to show how slow the FPGA was in its first implementation, and how far the optimization loop took it.

 The measurements below are from November 15 on AWS, replaying the same 8-chat × 3-turn benchmark . Prices are the on-demand rates recorded with that experiment. “Exact turns” counts outputs that matched the pinned CPU reference. The GPU implementations are included for context but did not satisfy the same bit-exact criterion but are pretty close in practice.

 What 
 Instance 
 Price per hour 
 Bench tok/s 
 Exact turns 
 FPGA is faster by 

 F2 FPGA, r9 (final image) 
 f2.6xlarge 
 $1.98 
 213.13 
 24/24 
 — 

 Exact CPU twin, 32 threads 
 m8a.8xlarge (32 Zen 5 cores) 
 $1.95 
 129.5 
 24/24 
 1.65× 

 Exact CPU twin, 24 threads 
 c7i.12xlarge (24 Sapphire Rapids cores) 
 $2.14 
 99.6 
 24/24 
 2.14× 

 Pinned scalar reference, all 32 cores 
 m8a.8xlarge 
 $1.95 
 40.6 
 24/24 
 5.25× 

 Pinned scalar reference as pinned, 1 thread 
 r7i.2xlarge 
 $0.53 
 1.1 
 24/24 
 195× 

 Exact CPU twin, 4 threads (small instance) 
 m8a.xlarge (4 Zen 5 cores) 
 $0.24 
 67.6 
 24/24 
 3.16× 

 DeepGrove’s own fork with GPU offload (not bit-exact, shown for reference) 
 g4dn.xlarge (T4 GPU) 
 $0.53 
 35.7 
 1/24 
 5.97× 

 Community CUDA port (not bit-exact, shown for reference) 
 g4dn.xlarge (T4 GPU) 
 $0.53 
 166.3 
 0/24 
 1.28× 

 What happens as the context grows?

 This is one generation starting with a 16-token prompt and continuing until the 8,192-token context is full: 8,176 generated tokens . The five middle columns show decode speed in tokens/s at the indicated context length for several generations of iteration. The last column is wall-clock time for the whole run/

 Image 
 16–64 
 1–2k 
 2–4k 
 4–6k 
 6–8k 
 Whole run (s) 

 r5 
 108 
 70 
 57 
 45 
 37 
 162.3 s 

 r6b 
 142 
 111 
 90 
 72 
 60 
 102.3 s 

 r7 
 181 
 140 
 111 
 88 
 72 
 83.6 s 

 r8 
 186* 
 155* 
 121 
 94 
 77 
 77.6 s 

 r9 
 233* 
 151* 
 120 
 93 
 76 
 77.8 s 

 * For r8 and r9, the first two columns come from separate, shorter runs generating 2,032 tokens. The other columns come from the full-context run.

 r9 improves short-context speed, while the complete long-context run is roughly tied with r8.

 What the model actually says

 These examples come from the final r9 image.

 Arithmetic, with the steps

 246 tokens · 229.7 tokens/s · 1.16 s end to end

 Read the arithmetic transcript 

 USER: What is 37 × 48? Explain the steps briefly.

MODEL: <think>
We need to compute 37 × 48. The user asks to explain steps briefly. So I'll do multiplication: 37 × 48 = 37 × (50 - 2) = 37×50 - 37×2 = 1850 - 74 = 1776. Or directly: 37×40=1480, 37×8=296, sum=1776. I'll present a brief explanation.
</think>

To multiply 37 by 48, you can break it down:

- 37 × 48 = 37 × (50 – 2) = (37 × 50) – (37 × 2) = 1850 – 74 = 1776.

Alternatively, 37 × 40 = 1480 and 37 × 8 = 296, so 1480 + 296 = 1776.

The final answer is **1776**.

 A little Python

 140 tokens · 220.0 tokens/s · 0.76 s end to end

 System prompt: “You are a helpful assistant. Think briefly before you answer, then reply clearly and concisely.”

 Read the Python transcript 

 USER: Write a Python function is_palindrome(s) that ignores case, spaces and punctuation.

MODEL: <think>
We need to write a Python function is_palindrome(s) that ignores case, spaces, and punctuation. So we need to filter out non-alphanumeric characters, convert to lowercase, then check if the resulting string is equal to its reverse. Provide the code.
</think>

```python
def is_palindrome(s: str) -> bool:
 """
 Returns True if the string s is a palindrome, ignoring case, spaces, and punctuation.
 """
 # Filter to keep only alphanumeric characters and convert to lowercase
 filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
 # Compare with its reverse
 return filtered == filtered[::-1]
```

 Where this puts us

 This was a fun project. I’m not sure I’m ever going to use this specific chip architecture in this specific way, and I’m certainly not claiming that an 8,192-token-context model running on an FPGA is the way I’d recommend anyone use something like this in production. But it’s pretty epic that this just works . Capability like this completely shifts the overton window for what a committed team of engineers can work on. It should mean that entirely new types of ideas (scientific discoveries, products, startups) are possible if you can point the models in the right direction. I’m excited to see what everyone builds.
