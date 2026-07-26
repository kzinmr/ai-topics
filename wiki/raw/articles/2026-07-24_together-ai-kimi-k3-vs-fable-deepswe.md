# Kimi K3 vs Claude Fable 5 on DeepSWE: Cost and Coding

**Source**: [Together AI Blog](https://www.together.ai/blog/kimi-k3-vs-claude-fable-5-on-deepswe-cost-and-coding)
**Published**: July 24, 2026
**Authors**: Zain Hasan, Shobhit Dixit

---

## Key Takeaways

Kimi K3 matches Claude Fable 5 on quality, costs a third as much per solved task, and as an open model gives teams full control over their deployment.

- Kimi K3 vs Claude Fable 5 is close on DeepSWE pass@1: Fable leads 69.9% to 68.5%, a 1.4 point gap.
- Give the models more attempts and Kimi K3 pulls ahead. It wins pass@2 (82.0 vs 80.2) and pass@4 (89.4% vs 88.5%).
- Kimi K3 is far cheaper: $4.65 per rollout vs $13.41, and 2.8x more solved tasks per dollar.
- Claude Fable 5 is the more reliable model: it solves more tasks four-for-four (58 vs 45).

In our Kimi K3 vs Claude Fable 5 comparison on DeepSWE, a benchmark that tests a model's software engineering capabilities across many task types and programming languages, the most interesting model this month is not the one at the top of the leaderboard. It is Kimi K3, the new open-weight model parked 1.4 points behind Claude Fable 5, at a third of the price.

Kimi K3 landed in DeepSWE on July 16, 2026, with 452 graded rollouts at max effort: 113 real, long-horizon feature requests from live open-source repos, four trials each, graded pass/fail by a hidden test suite. We analyzed all of them against Claude Fable 5 at its best setting (xhigh), Anthropic's strongest configuration and the former benchmark leader. Every figure below comes from this run, so it can differ from other public Kimi K3 vs Claude Fable 5 scorecards.

## The DeepSWE scoreboard: pass@1 and pass@k

Fable xhigh solves 69.9% of tasks on the first try under DeepSWE's official scoring. Kimi K3 max solves 68.5%. One point four between an open-weight model and Anthropic's flagship, the K3 +38 point leap is the largest between model releases in this entire dataset.

Also when you allow for larger pass@k's the ranking flips. pass@2 Kimi is ahead, 82.0 vs 80.2. pass@4 Kimi is 89.4% above Fable's 88.5 and Sol's 85.8; across the entire 44-config export, only two cheap GPT configs (Luna max and GPT-5.5 high, at 90.3) have ever reached more.

## Coverage vs reliability: where Kimi K3 and Fable 5 differ

Decompose pass@1 into coverage (tasks solved at least once) and reliability (pass rate on those tasks) and the two models occupy different corners. Kimi reaches 89.4% of the benchmark - higher than any peak, with only 12 tasks it never cracks (Fable: 13). But it's less reliable on 4/4 tries: 76.6% reliability and only 45 tasks solved four-for-four, against Fable's 79.0% and 58. Fable is steadier and more deterministic; Kimi is the wider net, which accounts for its gains at pass@2 and @4.

## Cost comparison: Kimi K3 vs Claude Fable 5 pricing

- Kimi K3: $4.65 per rollout. Fable xhigh: $13.41. The full 452-rollout sweep: $2,103 vs $6,010.
- Per solved task, Kimi delivers 14.7 solves per $100 versus Fable's 5.3 - 2.8x the work per dollar.
- Kimi takes a much longer time but this will no doubt improve when the model is open sourced and inference is optimized!

## How similar are Kimi K3 and Claude Fable 5?

Per-task correlation between Kimi K3 and Fable is 0.72 - the highest cross-vendor similarity in the entire benchmark. In fact the top four cross-vendor similarities in the export are all Kimi-K3-versus-Anthropic pairs. There is not a single task where one goes four-for-four and the other zero-for-four, in either direction - a first across every pairing we have analyzed. Both solve 96 tasks, Kimi alone adds 5, Fable alone adds 4, and the same 8 resist both.

Their failure anatomies match too: 65% of failures are near misses for both, and both protect the repo's existing test suite (11% vs 10% baseline regressions).

In practice, Kimi K3 and Claude Fable 5 succeed and fail on nearly the same tasks, so pairing them buys you almost no diversity: their union covers 105 of 113 tasks, barely above Kimi alone at 101.

## Kimi K3 vs Fable 5 by programming language

Kimi takes Go decisively (79 vs 71). Fable holds the other four: Python 74-68, JavaScript 70-65, TypeScript 64-60, and Rust 75-65.

The really interesting detail here is how much K3 catches up with Fable on Rust tasks - no other model, not even GPT 5.6 Sol, is as good at Rust.

## What it means

Kimi K3 is now the rational default: near-flagship reach, the best pass@4 of any flagship-tier config, at 35 cents on Fable's dollar.

## Run Kimi K3 on Together AI

Kimi K3 ships as an open-weight model, which is what makes the pass@4 reach and the cost profile above usable on your own terms. Once the weights are available, Together AI's inference stack is built to serve open models like Kimi K3 at production scale, so you can chase the wider pass@k net without frontier token prices.

[See Together AI inference pricing](https://www.together.ai/pricing)

## FAQs

### Is Kimi K3 better than Claude Fable 5?

It depends on the metric. Claude Fable 5 wins single-attempt reliability on DeepSWE (pass@1 69.9% vs 68.5%) and solves more tasks four-for-four. Kimi K3 wins pass@2 and pass@4 and costs far less, so it is the stronger value pick for high volume or retry-tolerant agent work.

### How much cheaper is Kimi K3 than Claude Fable 5?

In our run, Kimi K3 cost $4.65 per rollout versus $13.41 for Claude Fable 5 at its xhigh setting, roughly a third of the price. Measured per solved task, Kimi K3 returned 14.7 solves per $100 against Fable's 5.3, about 2.8x the work per dollar.

### Is Kimi K3 open weight?

Yes. Kimi K3 is an open-weight model from Moonshot AI, so once the weights are released it can be self-hosted or served through inference providers. Claude Fable 5 is a closed model available only through Anthropic and its partners.

### Which is better for coding, Kimi K3 or Claude Fable 5?

For coding they are close. In our language breakdown Kimi K3 takes Go decisively, while Claude Fable 5 leads Python, JavaScript, TypeScript, and Rust. Fable is steadier on any single attempt; Kimi casts a wider net across multiple attempts.

### What is pass@k on DeepSWE?

pass@k measures whether at least one of k attempts at a task passes the hidden test suite. pass@1 rewards getting it right first try; higher k rewards a model that can eventually reach a solution across several tries. Kimi K3's edge grows as k increases.
