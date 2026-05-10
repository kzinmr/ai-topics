---
title: "RAG Brag with Shortwave CEO Andrew Lee"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/rag-brag-with-shortwave/"
scraped: "2026-05-10T01:27:37.113611+00:00"
lastmod: "2025-03-14T21:43:41Z"
type: "sitemap"
---

# RAG Brag with Shortwave CEO Andrew Lee

**Source**: [https://www.pinecone.io/blog/rag-brag-with-shortwave/](https://www.pinecone.io/blog/rag-brag-with-shortwave/)

←
Blog
RAG Brag with Shortwave CEO Andrew Lee
Gibbs Cullen
Mar 14, 2024
Company
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
We recently debuted RAG Brag, a new livestream event series where we invite leading AI founders and innovators to share their experiences building with AI. Our first guest was
Andrew Lee
, Co-Founder and CEO of
Shortwave
. Shortwave is an AI-enhanced email app. On top of everything you’d expect from an email app, it brings the full power of LLMs and other modern AI tech into your inbox to help you be more productive.
During this session
, Andrew shared valuable insights from his experience
building Shortwave
and how the overall product has been transformed through AI. While the full discussion is well worth a listen, we’ve highlighted some key takeaways from Andrew that stood out the most.
Betting big on AI
Andrew and this team spent the first few years building out the core email client before deciding to go all in on AI. With the increasing quality and accessibility of LLMs and AI tooling, Andrew and his team believe betting on AI is critical and a “must-win transition”.
Today, Shortwave is well along its AI journey with a series of AI-powered features like
AI Autocomplete
. AI Autocomplete is similar to GitHub Copilot but for your email. As you type, it'll give you suggestions and perform completions using phrases that you would actually use or pulling in specific facts (e.g. office address, phone numbers) from your emails for you.
This works by running two vector searches on the embeddings stored in Pinecone, one on emails that you’ve sent on similar threads or topics, and the other on those similar to what you’ve typed so far. Using
RAG
, results from both searches are then used as a prompt for the model (a fine-tuned version of GPT 3.5) to generate a completion that’s somewhere between half a sentence and a sentence.
Filtering by metadata
and searching by
namespace
enables them to more efficiently and reliably search through and manage embeddings from across their users.
Challenges of getting started with AI
With so many tools and models to choose from, getting started with AI can be challenging. Shortwave’s
AI stack
currently uses six models (split between open source and OpenAI) along with other AI solutions including Pinecone, so Andrew was able to share some valuable perspectives on challenges he's encountered over the years.
Challenge 1: Building a reliable system from unreliable parts
In today’s landscape, many AI tools and products are readily available, easy to use, and affordable. According to Andrew, “We figured out that the base models you can get off the shelf (e.g. GPT-4) are smart enough to produce some really valuable outputs if you can get the right data into the prompt and you can explain it to the LLM the right way. And doing this comes down to retrieval.”
Doing retrieval in such a way that solves hallucinations while making LLMs more trustworthy and usable in user-facing products is hard. Off-the-shelf LLMs are inherently unreliable and will hallucinate without the necessary context for a user’s query. RAG, specifically with more data,
significantly improves
the results of these AI applications. With Pinecone, Shortwave can seamlessly scale their operations while improving the performance and accuracy of results to their users.
Andrew also believes this challenge comes down to better prompting. At Shortwave, they have built an in-house testing infrastructure for test prompts and continue to tweak the prompt until they get the answers they want. He admits this is not a perfect solution, but it also comes down to tradeoffs which leads to the second challenge: cost.
Challenge 2: Costs are still high (but we should expect them to go down)
Running and maintaining a highly reliable, fast, and scalable AI application can be expensive. It requires creating your embeddings, storing the embeddings in a vector database, and making frequent calls to your LLMs. While this all drives up costs for Shortwave, Andrew is counting on the cost of these technologies to come down dramatically.
For example, with
Pinecone serverless
, companies like Shortwave can continue powering remarkable GenAI applications at practically unlimited scale without worrying about cost. On average, Pinecone serverless reduces costs by up to 50x. We’ve seen similar cost reductions on the inference and generation side with OpenAI recently reducing costs for certain models like GPT 4-Turbo.
According to Andrew, “If you're focused on AI right now, you probably want to burn a little bit of money to get the best stuff for building the right product, and count on those cost curves coming down.”
Advice to those starting their AI transition
Andrew wrapped up the discussion with some recommendations to those looking to start investing in AI.
Tip #1: Take a really hard look at AI
Despite all the excitement around AI, we’re still in the early days of adoption. In fact, a recent
survey from Retool
shows that although a majority (77.1%) responded that their companies had made some effort to adopt AI, around half (48.9%) said those efforts were fledgling – just getting started or ad-hoc use cases. For those in these early stages, Andrew urges them to take a really hard look at AI, “There are very few areas that are not going to be radically changed by AI, and you either need to become aware of it and do something about it. Otherwise, your product will quickly fall behind what other people can do.”
Tip #2: Invest in the best solution and focus on the end-user experience
Andrew warns listeners against building or optimizing more than you need to early on. There are many great “building blocks'' out there, and he believes we can count on them to get dramatically better over time.
If you're not someone who's building one of those core technologies, then he advises using the best, most expensive tool out there to start building and prototyping with (no fine-tuning or cost optimization). Prove that you can make this work first, then figure out how to make it fast, cheap, and scalable. He believes, “If you can't make it work with the most expensive or best model out there, or if your users don't love it, then ‘great, you saved yourself some time!’. There's no point in trying to build the rest of those systems.”
More RAG Brag
To learn more about Andrew and Shortwave, make sure to watch the
full recording
or visit their
website
. We will be continuing the RAG Brag series with more engaging and thought-provoking conversations with leaders in the AI space.
Stay tuned for updates
!
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
