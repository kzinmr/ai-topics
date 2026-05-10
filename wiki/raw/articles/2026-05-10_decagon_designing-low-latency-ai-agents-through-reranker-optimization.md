---
title: "Designing low-latency AI agents through reranker optimization"
source: "Decagon Blog"
url: "https://decagon.ai/blog/designing-low-latency-ai-agents-through-reranker-optimization"
scraped: "2026-05-10T01:19:39.323658+00:00"
lastmod: "None"
type: "sitemap"
---

# Designing low-latency AI agents through reranker optimization

**Source**: [https://decagon.ai/blog/designing-low-latency-ai-agents-through-reranker-optimization](https://decagon.ai/blog/designing-low-latency-ai-agents-through-reranker-optimization)

Introducing Proactive Agents.
Learn more
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Build
AOPs
Workflows for AI agents
Integrations
Support tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & Reporting
Voice of the Customer
Watchtower
Always-on QA
Suggestions
AI-powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
AI and the next generation of customer experience
Why exceptional service is the new brand differentiator as AI reshapes consumer expectations.
Spring ’26 Release: Proactive Agents
See how user memory, outbound voice, and Agent Workbench can help you build stronger customer relationships
Company
About
Careers
Security
Sign in
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Technology & Research
Blog
/
Designing low-latency AI agents through reranker optimization
Designing low-latency AI agents through reranker optimization
March 25, 2026
Written by
Nick Liu
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
At Decagon, low latency is a hard product requirement. When you're speaking with a voice agent, an extra 200–300ms of silence is the difference between a natural conversation and a robotic one, full of awkward pauses and missed cues. Every millisecond we can reclaim translates directly into a better user experience.
We traced a meaningful chunk of our response latency back to a single stage in our RAG pipeline: reranking. Here's what we found, and how we cut reranking latency without replacing the underlying model.
The hidden cost of reranking
RAG is an often-overlooked aspect of agent architecture that can quietly eat into response time. A typical RAG pipeline looks like this:  query rewrite → embedding generation → vector retrieval → reranking → final response generation.
Aside from final response generation, reranking typically incurs the largest latency cost, as it must process tens to hundreds of candidate documents before a single token of the final response can be generated, creating a bottleneck for everything that comes after it.
The root cause comes down to how reranking works, and specifically which kind of reranker you're using.
List-wise vs. Point-wise reranking
List-wise rerankers
take all candidate documents as input and output a ranked ordering from most to least relevant given the user’s query. The constructed prompts frequently run into the tens of thousands of tokens, which drives up latency due to the quadratic time complexity of transformer attention. The more tokens in the sequence, the disproportionately more expensive the forward pass becomes.
Point-wise rerankers
, by contrast, score the relevance between a user query and a single document in isolation. They compute a score for each (query, document) pair independently and then sort the documents in decreasing order of relevance. Because each input is just one query paired with one document, sequence lengths are dramatically shorter and per-call cost becomes far more predictable.
We recently moved from list-wise to point-wise reranking at Decagon and saw a significant reduction in reranking latency as a result.
Efficient batching with attention masking
In practice, however, naively sending tens or hundreds of independent model requests is not always more efficient. The overall reranking step is gated on the slowest individual call, and the overhead of many sequential requests adds up quickly. Instead, we use a technique that manipulates the attention mask to score multiple (query, document) pairs in a single batched forward pass.
Here's how it works: we concatenate multiple (query, document) pairs into a single packed sequence, separated by a delimiter token. We then modify the attention mask so that tokens within each pair attend only to each other, while attention to tokens from other pairs is masked out entirely. This produces a block-diagonal attention pattern (see diagram below) — each document is scored in isolation, but we amortize the overhead of a model call across many pairs at once.
Because relevance scoring isn't an autoregressive process (unlike text generation, it doesn't need to predict tokens one at a time), this packing approach is valid: the pairs don't need to interact with each other to produce correct scores. We get the efficiency of batching without compromising the point-wise scoring semantics.
Finding the optimal batch size
With this packing approach in place, the remaining challenge is straightforward: find the optimize batch size that minimizes end-to-end latency for your system.
Using too few pairs per batch means sending many requests, where the overall step is gated on the slowest call. Using too many causes the packed sequence to grow long enough that per-call processing time starts to climb. We can see in our empirical results below that batch size 2 yields the best latency improvements.
Your optimal batch size will depend on your model, hardware, and document length distribution, but the shape of the curve is likely to be similar. Latency improves quickly with small batches, then degrades gradually as sequences grow.
What’s next
Building low-latency AI agents requires more than fast models. It requires deep diving every layer of the pipeline and asking where the real bottlenecks are hiding. Reranking is just one of the many places for step wise improvements.
By moving to point-wise reranking and applying attention masking to batch document scoring efficiently, we drove down reranking latency substantially without overhauling the underlying model. The gains came not from brute-force optimization but from a well-placed structural insight: use of attention masking that preserved scoring quality while unlocking far more efficient computation.
At Decagon, this is how we think about building. The best performance wins are often not the most obvious ones. They come from pressure-testing assumptions at each layer and finding the places where a targeted change compounds into a meaningful product improvement. We will keep sharing what we find along the way.
Recent posts
Bringing the AI concierge to Australia
Decagon is opening a new office in Sydney, Australia
Introducing automatic optimization and Root Cause Analysis
Today, we’re excited to announce two new capabilities to help you rapidly improve your agent’s performance.
Bringing Decagon’s AI concierge solution to Google Cloud Marketplace
We're excited to announce that Decagon is now available on Google Cloud Marketplace.
Deliver the concierge experiences your customers deserve
Get a demo
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
