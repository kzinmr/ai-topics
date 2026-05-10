---
title: "RAG Brag with Inkeep Co-Founder Nick Gomez"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/rag-brag-inkeep/"
scraped: "2026-05-10T01:27:39.286717+00:00"
lastmod: "2025-03-14T21:42:03Z"
type: "sitemap"
---

# RAG Brag with Inkeep Co-Founder Nick Gomez

**Source**: [https://www.pinecone.io/blog/rag-brag-inkeep/](https://www.pinecone.io/blog/rag-brag-inkeep/)

←
Blog
RAG Brag with Inkeep Co-Founder Nick Gomez
Valeria Gomez
Jul 17, 2024
Company
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
In a recent
RAG Brag
episode, Nick Gomez, Co-founder and CEO of Inkeep, shared insights about his journey and the inspiration behind starting a company focused on helping companies with technical products, improve self-help experiences with AI, and machine learning. He shared his background and the innovative ways Inkeep is addressing challenges in the technical and developer support space.
Nick Gomez
's journey began at Microsoft, where he spent three years working on developer experiences in the identity space. He noticed that while authentication and identity are crucial, they often create hurdles for developers who prefer to focus on their core business logic rather than getting bogged down in technical details. These experiences led him to partner with Robert Tran to create
Inkeep
— an AI search and support copilots for technical products. This conversation explores how it all began and the lessons they learned while building AI software.
What was the inspiration behind founding Inkeep?
When we decided to start a company, we wanted to focus on developer products, a market that often gets overlooked. During our research, we noticed a gap: while most B2B SaaS products use chatbots like Intercom or Zendesk, only about 20% of developer companies do. Developers often see these chatbots as marketing tools, not helpful resources. Our original motivation was to create a product designed for developers that provides immediate, helpful answers without the marketing and sales stigma of traditional chatbots. We’ve since found that that approach actually resonated with many companies with technical products and savvy (or picky) end-users; in particular, if they have high support volumes and tons of content.
What sets Inkeep apart from other support solutions?
Inkeep differentiates itself by offering a completely hands-free solution that maintains a very high bar for quality of answers. Our platform can automatically ingest content from any source—whether it’s documentation, support tickets, or forums—without requiring engineering teams to invest time and resources. We offer simple, embeddable UI components like search bars and chatbots for Slack or Discord, allowing companies to seamlessly integrate Inkeep wherever they interact with their users.
Another key aspect is that we handle the complexities like content ingestion, chunking, and keeping data current. Teams don’t need to worry about setup or maintenance; they just embed Inkeep and focus on their core tasks. Our system also detects when the chatbot can’t find information and turns these gaps into actionable items for documentation or content teams. This helps improve technical content which ultimately enhances the user experience and support deflection rates. We aim to help teams support their users better, turning every interaction into valuable insights for continuous improvement.
Could you explain the different AI/ ML techniques that power Inkeep’s capabilities?
Our approach has been iterative and focused on practical implementation rather than over-engineering upfront. Initially, we started with basic solutions and iterated based on real-world feedback. As we onboarded more customers and encountered diverse use cases, we identified areas where our solutions fell short, such as retrieval issues or model hallucinations. To address these challenges, we continuously experiment with new techniques. Each time we implement a new approach, we leverage a backlog of test cases derived from our early challenges to validate its effectiveness. This approach allows us to refine our methods over time and ensure robust performance across different scenarios.
Early on, we realized we needed to treat various content types differently. For example, documentation, which is structured and authoritative, is treated differently from Slack conversations, which are more dynamic, less structured, and of mixed quality. This approach allows us to manage various content types effectively, delivering accurate and contextually relevant responses, unlike more general methods.
Can you share more details about your chunking strategy and how it contributes to Inkeep’s efficiency?
Our
chunking
strategy is integral to how we process and manage content. By breaking down documents into smaller, contextually coherent chunks, we ensure that our AI solution can handle and analyze the information more effectively. We use hierarchy to break down large documents and treat for example Slack conversations differently from documents. This approach not only improves the accuracy of our responses but also enhances the retrieval process, allowing our system to provide developers with the most relevant information quickly. This chunking strategy also improves indexing and search, making sure even detailed queries get precise answers.
How does Inkeep leverage Pinecone to optimize performance and scalability?
We use Pinecone for vector storage and retrieval which has proved crucial for providing flexibility across different customer needs. For example, we create dedicated instances for enterprise customers using Pinecone's pod architecture to ensure low latency for our search service. However, for chat applications where latency is less critical, we use Pinecone's
serverless
option, which is more cost-efficient. Pinecone also supports
hybrid search
, combining sparse and dense embeddings, to deliver a more robust and accurate search experience. This flexibility allows us to optimize costs and performance, whether dealing with enterprises with extensive documentation or smaller companies with fewer pages.
How does Inkeep minimize hallucinations and ensure reliable answers?
Reducing hallucinations in our AI solution heavily depends on our RAG method. Models hallucinate less when they have the right content to work with. If the content has the answer, hallucination rates drop. The tricky part is when content seems relevant but isn't accurate or lacks context, leading to misleading answers. For instance, if a model only knows "Pinecone is a vector database" without understanding its full range of features, it might over-interpret narrow content. By providing a diverse set of context to our RAG pipeline, we cut down on misinterpretation. We also experiment with prompts to encourage conservative responses and build comprehensive context about our customers to boost accuracy.
What were some of the major challenges Inkeep faced in ingesting content from various sources? How did you overcome them?
One of our biggest challenges was dealing with the diverse formats and structures of content across different platforms. Each company has its unique way of organizing documents or setting up custom documentation sites. Creating a solution that could effectively ingest this varied content at a high fidelity and quality level was incredibly challenging. Unlike traditional search engines that require developers to preprocess and structure content before indexing, our goal was to offer a solution where companies wouldn't have to worry about these technical details. To address this, we developed algorithms that autonomously navigate and extract hierarchical content from arbitrary websites, ensuring comprehensive content ingestion even in complex scenarios.
Another critical aspect we faced was content scraping. For example, many platforms use JavaScript to load tabs, where content only appears when you interact with it. This made scraping tricky, as we had to simulate browser behavior to accurately access hidden content.
What trends do you foresee shaping the future of developer-focused companies, and how is Inkeep preparing for them?
Looking ahead, I see three key phases to generative AI applications: advanced search and retrieval, action-based workflows with human oversight, and autonomous AI agents managing complex tasks. At Inkeep, we're focusing on improving our action-based workflows to help documentation and support teams boost productivity and improve the quality of their content and products. Search and retrieval is relatively mature now, with chatbots helping users find content across various structured and unstructured sources. Action-based workflows, which suggest actions with human oversight, are becoming more common and enhancing productivity. In the future, autonomous AI agents will perform multiple steps with greater autonomy, although this is still in its early stages but holds a lot of promise.
What advice would you give to aspiring entrepreneurs looking to start their own tech companies?
I've had an entrepreneurial itch since I was a kid — like even back in 2nd grade sold candy at school for a bit of profit, though I did get in trouble a few times! What I've learned in my recent startup journey is that you don't need to know everything upfront. Even though I come from a product and engineering background, I had no experience in sales or marketing. But once you start a startup, it naturally pushes you to learn these new skills. You learn by doing and adapting — that's what I call "drive to survive." The key is to focus on solving a real problem that needs to be solved. Listen to your potential or current customers and let their needs guide your solution. Find people who believe in your idea enough to support you. Trust the process and let the market guide you on how to bring your solution to the world.
More RAG Brag
For further insights into Nick and Inkeep, be sure to watch the entire
recording
or visit their
website
. Stay tuned as we continue the RAG Brag series, featuring compelling discussions with AI industry leaders. More episodes are on the way!
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
