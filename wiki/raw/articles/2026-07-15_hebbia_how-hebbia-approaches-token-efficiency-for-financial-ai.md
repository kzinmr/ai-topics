---
title: "How Hebbia Approaches Token Efficiency for Financial AI"
source: "Hebbia Blog"
url: "https://www.hebbia.com/blog/how-hebbia-approaches-token-efficiency-for-financial-ai"
scraped: "2026-07-15T06:00:12.711726+00:00"
lastmod: "2026-07-14"
type: "sitemap"
---

# How Hebbia Approaches Token Efficiency for Financial AI

**Source**: [https://www.hebbia.com/blog/how-hebbia-approaches-token-efficiency-for-financial-ai](https://www.hebbia.com/blog/how-hebbia-approaches-token-efficiency-for-financial-ai)

Engineering
By Adithya Ramanathan
07.13.26
How Hebbia Approaches Token Efficiency for Financial AI
Processing more than 250 billion tokens each month reveals that the biggest AI efficiency gains come from optimizing workflows, not simply reducing token counts.
Hebbia processes more than 250 billion tokens a month. Operating at that scale has built a precise view of where cost actually accumulates, and where we can unlock the biggest efficiency gains for Hebbia customers and their complex, token-heavy workflows.
Token efficiency breaks into three parts:
Reducing the number of tokens it takes to solve a problem
Optimizing the cost of each token used to solve it
Avoiding token recomputation via caching
Most of the market's attention goes to the first two activities: How do I pick a more cost-efficient model, and how do I build more token-efficient systems? The third presents a genuinely difficult challenge that gets far less attention than it deserves—yet possibly the most effective tactic within the group.
Optimizing any of these is not just a cost exercise. Each has a compounding improvement on user latency, meaning users should feel token efficiency improvements as much as their finance teams do.
Quality over Cost
Hebbia's principle has always been to maximize what tokens a model actually attends to, and that principle has a direct consequence worth stating plainly: As a product philosophy, Hebbia considers answer quality as its first priority and approaches cost efficiency as a second-order challenge. We prosecute and read every relevant document because missed information is worse than an expensive token bill. Finance demands rigor, and an incomplete summary or uncited claim can easily be more costly than an inefficient workflow.
We don’t consume tokens in the same fashion as a
RAG-based search product
, and our efficiency metrics will look different as a result. RAG retrieves a small set of similar passages and conflates document filtering with content retrieval. This places a threshold on token consumption, but fails on questions requiring multi-hop reasoning or compound logic across a document. Hebbia instead identifies which document components actually need full attention for a given question and feeds the model only the relevant subset. Our token spend scales with what a problem requires rather than being capped and silently degraded by an arbitrary retrieval limit.
We will use the number of tokens a given task needs to reach the highest-quality answer, and any optimizations must not interfere with that quality threshold.
Token reduction
Our reduction work is measured against a different baseline than "fewest tokens possible." It's measured against the number of tokens it takes to reach the highest-quality answer.
While we’re not approaching token reduction from a pure “fewest tokens possible” standpoint, the Hebbia platform is still designed to give our models the tools to do the work more efficiently without sacrificing the quality threshold. A few examples:
Code execution
serves as a primitive for financial analysis in a number of different areas, accurately handling the quantitative work that a language model would otherwise spend tokens approximating.
Document parsing
strategies isolate the vision model to only the portions of a document that actually require it. If a document contains images, a vision model reads the pages with images and a non-vision model reads the rest.
Matrix
functions as a token management layer in its own right, reducing a large set of documents down to the information an LLM actually needs to attend to for a given task.
In each case, the principle is the same: break the task down into its component parts, and spend tokens only where they actually move the answer forward.
Token routing
While once a differentiated approach, token routing has become table stakes. Routing layers selects a provider based on pricing, latency, and availability and translates requests into the format that provider would expect. Requests reroute automatically if a provider goes down, and usage is billed centrally instead of through a separate account with every provider.
While this is necessary, it is not sufficient for token management on its own. Tools like OpenRouter, Martian, and Unify automate model routing across providers, selecting the lowest-cost model for each request.
When a new model launches with a higher price tag, the assumption in finance is usually that the higher price buys better answers. Our
Financial AI Benchmark
doesn't support that assumption. Across the finance tasks that matter most, a number of the newer, pricier models post results barely ahead of the model they replaced, and in several cases fall behind it:
Hebbia’s
investment in evaluations
enables us to optimize the internals of our system for both cost and latency without guessing at which steps can tolerate a smaller model. Plenty of use cases inside the Hebbia system, a subagent or a tool inside a larger multi-agent finance workflow, run fine on older generations of model intelligence, and coordination and request scheduling are managed by our
Maximizer service
, which ensures tokens aren't spent on steps that don't need them.
Token caching
Optimizing for cache hit rate is non-trivial and is one of the most economically valuable levers available.
When a model processes a request, it computes a representation of the input context and stores it in a key-value (KV) cache. If the same context appears again on a later request while the cache is still warm, the model skips recomputing it entirely. The savings are large: a cache hit can cut processing cost by as much as 90 percent.
KV cache efficiency is straightforward if you operate in a world with a single model on a single provider with a single GPU. That isn't the world a reliable, scalable, compliant LLM system runs in.
Hebbia maintains both model agnosticism and provider flexibility, so every request to a frontier model is backed by capacity pooled across multiple GCP regions, AWS, and first-party infrastructure. We monitor error rates, reliability, performance, and rate limits continuously to balance request volume across these providers.
In a system built that way, cache awareness becomes genuinely hard. KV caches aren't shared across providers, so a context that's warm on one provider is cold on the next. And you don't want to chase a warm cache to a provider that's underperforming just to capture the discount. What this requires in practice is a continuous Pareto optimization across cache affinity, provider performance, and request priority, producing a single routing decision that balances cost and latency without the customer ever seeing the tradeoff underneath it.
Price the workflow, not the token
With quality as a benchmark, CTOs should approach cost optimization at the workflow level, rather than the token-by-token level. We recommend the following exercise for any team looking to map their AI footprint.
Map the unit of work.
Determine a single end-to-end workflow: a generated PowerPoint presentation, a multi-part research document, a summary of a folder of information. This becomes the cost denominator to measure LLM pricing in a non-abstract way.
Compare token spend per unit, model to model.
The same workflow consumes different token counts on different models. Cheaper models will sometimes need more hops to answer a question than bigger, more expensive models, leading to greater aggregate costs.
Account for retry and review rates.
A cheaper model that requires human review on 15 percent of outputs costs more per completed task than an expensive model with a 3 percent review rate. Quality determines total cost, not token price alone.
Size the full request payload, not just the prompt.
For production applications, input tokens may outnumber a user's actual query by 10 to 50 times. Map the impact of system prompts, conversation history, retrieved context, and function definitions to get a full sense of the workflow’s cost footprint.
Tie cost to business outcomes, not token counts.
Cost per workflow is what the business should actually care about, not cost per token. The organizations that can answer "was it worth it" with data are the ones whose AI investments survive budget audits.
Retries and review deserve particular attention here. A model that's cheaper per token but wrong often enough to need a human to redo the work hasn't actually saved anything. It's shifted the cost from the API bill to an analyst's afternoon, and that hour is priced far higher than the tokens it replaced.
What this adds up to
Token efficiency at Hebbia is an exercise in knowing exactly which tokens were necessary to reach a defensible answer, which were routed to a model better suited to a smaller task, and which tokens have been reused instead of recomputed. The preference for quality is clear, so there’s no tension for users between spend and accuracy.
A cheaper model isn't always the cheaper choice once retries and reviews are factored in. Caching is the piece most teams fail to consider, and at our scale, across a pooled, multi-provider infrastructure, it's also the hardest to get right. The result is an effective approach to cost that starts with the workflow and works backward to the token, not the other way around.
