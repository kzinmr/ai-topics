---
title: "Watch out for cache read costs"
url: "https://martinalderson.com/posts/watch-out-for-cache-read-costs/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-08-11T10:16:30.990817+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Watch out for cache read costs

Source: https://martinalderson.com/posts/watch-out-for-cache-read-costs/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I know I'm guilty of just scanning OpenRouter's pricing tables and looking at input and output costs per million token. I've realised that's the wrong number to be focused on these days and cache read costs are actually far more important.
Most of your spend is likely cache reads
If you're running agentic workloads,
cache reads
are almost certainly the biggest driver of costs. Since we've got
much longer context windows
, you probably need to update your mental maths to take into account what this does to pricing.
To take a hypothetical agentic session starting at 60k context length, with each tool call resulting in 500 tokens written and 5,000 tokens read, after 20 turns we get something like this:
Model
Cache reads
Fresh input
Output
Total
DeepSeek V4-Flash
$0.01 (18.4%)
$0.02 (72.8%)
$0.00 (8.8%)
$0.03
Claude Opus 5
$1.04 (44.9%)
$1.03 (44.3%)
$0.25 (10.8%)
$2.32
GPT 5.6 Sol
$1.04 (48.1%)
$0.82 (38.0%)
$0.30 (13.9%)
$2.16
Cache reads are nearly half the bill. Now look what happens when we take the same session to 100 turns:
Model
Cache reads
Fresh input
Output
Total
DeepSeek V4-Flash
$0.09 (48.1%)
$0.08 (44.5%)
$0.01 (7.4%)
$0.19
Claude Opus 5
$16.31
(76.4%)
$3.78 (17.7%)
$1.25 (5.9%)
$21.34
GPT 5.6 Sol
$29.55
(81.6%)
$4.70 (13.0%)
$1.96 (5.4%)
$36.20
You quickly see the issue. The main cost driver becomes cache reads - while you are only
adding
5.5k tokens each turn, the
existing
context window has to be read on each turn, so the cumulative cost grows quadratically with the number of turns.
This also underscores how
reducing
number of tool calls per run has an outsized impact on costs. If you can give the agent more specialised tools that require fewer turns, even cutting the number of turns down by 10% reduces cost per agent run by around 16%.
The case of the shrinking KV cache
While context windows have rocketed up in size, their size in memory has
shrank rapidly
. DeepSeek's KV cache algos (Compressed Sparse Attention and Heavily Compressed Attention), for example, allow a 1M context window at ~fp8 precision in around 5GB.
This has allowed KV cache to be offloaded to system memory and, increasingly, NVMe flash drives - explaining why the cost of NVMe has skyrocketed recently. Given the huge leaps in KV cache compression, a 1-5GB KV cache can be written to SSD and read back
extremely
quickly, especially with RAID-style setups and PCIe 5.0 flash storage (in theory
well
under 100ms is possible). And with both Nvidia and AMD supporting direct NVMe read and writes to the GPU, it doesn't even need to touch system RAM.  As such a bank of NVMe drives can host tens of thousands of agentic sessions.
DeepSeek have made this a huge selling point of their inference API - offering cache reads at a tenth of the cost of other providers of the same model. As I'm writing this they are rumoured to be
increasing
this price, but I'm sure this is because of huge hardware imbalances on their side, not any underlying reason. I'm sure the market will start bidding the price of cache reads down significantly.
This is (probably?) a huge profit centre
Cache reads are almost certainly outrageously profitable for the frontier labs. You're effectively paying over and over again to read a handful of GB of (V)RAM. Given most serving architectures allow you to boot this off VRAM quickly and onto system RAM (or even NVMe), you're effectively renting a few GB of system RAM at a spectacular markup.
The maths on the 100-turn run above shows us that Opus 5 spends $16.31 on cache reads. At two minutes a turn that session runs about 3.3 hours, and the context averages roughly 330k tokens over its life, so even assuming a much-larger-than-deepseek 30KB/token you're holding around 10GB. That works out at somewhere around
$0.5 per GB-hour
. AWS will rent you memory for well under a cent per GB-hour.
Now I'm oversimplifying here, because there
are
definite costs to tiered KV cache storage that go beyond RAM and NVMe (such as very complex and expensive networking to make sure the KV cache is in the right place at the right time). But, if we start seeing more local and on prem LLM solutions, this cost is pretty minimal for most organisations - it only gets super complex at huge scale.
The key learning I took away from this is that cache read costs is increasingly going to be the main cost you need to look out for. There has been
huge
innovation in making the underlying caches far, far smaller and the pricing mechanism hasn't really adjusted.
