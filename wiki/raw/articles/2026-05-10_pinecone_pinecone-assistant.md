---
title: "Introducing Pinecone Assistant in Beta"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pinecone-assistant/"
scraped: "2026-05-10T01:27:03.562108+00:00"
lastmod: "2024-08-19T22:54:05Z"
type: "sitemap"
---

# Introducing Pinecone Assistant in Beta

**Source**: [https://www.pinecone.io/blog/pinecone-assistant/](https://www.pinecone.io/blog/pinecone-assistant/)

←
Blog
Introducing Pinecone Assistant in Beta
Nathan Cordeiro
,
Roy Miara
,
Jack Pertschuk
Jun 25, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Update: Pinecone Assistant is now in public preview.
Learn more
.
Today we’re launching Pinecone Assistant in beta. Pinecone Assistant is an API service for answering complex questions about your proprietary data, accurately and securely, within your applications.
With Pinecone Assistant you get:
Simplicity: Just add your files and start building your killer AI app using
the API
.
High-quality results: Relevant answers grounded in your data, with references.
Full control over your data: Your uploaded files help generate useful answers without training the model, and you can easily and permanently remove data.
Prototype and ship AI assistants in minutes
Developers still struggle to build AI assistants that can accurately answer questions about private data. Publicly available models are unaware of this data, and providing it can pose security concerns. Most teams also lack the time or deep AI expertise to build accurate and secure knowledge systems using
Retrieval Augmented Generation (RAG)
.
Pinecone Assistant gives you a better way: Just upload your PDF or text files (support for other file types coming soon) and start asking questions. Prototype quickly with the drag-and-drop upload and chat interface, then add it to your applications in a matter of minutes with the chat-completion-compatible API.
Easily create an Assistant inside the console.
Receive relevant answers grounded in your data, with references.
pc = Pinecone(api_key='<<PINECONE_API_KEY>>')

# Create an assistant
finance_assistant = pc.assistant.create_assistant(assistant_name="Finley")

# Upload information to your assistant
finance_assistant.upload_file("./10q-reports.pdf")

# Once the upload succeeded, ask the assistant a question
msg = Message(content="What share repurchases has NVIDIA done recently?")
resp = finance_assistant.chat_completions(messages=[msg])
All the infrastructure, operations, and optimization of a complex Q&A system are handled for you. That includes chunking, embedding, file storage, query planning, vector search, model orchestration, reranking, and much more. Pinecone Assistant leverages our enterprise-grade
vector database
and extends frontier models — starting with GPT-4o from Azure OpenAI Service with other models coming soon.
Provide more accurate answers with less effort
AI assistants must give accurate and reliable answers during prototyping to demonstrate value, and then in production to provide a great customer experience and minimize liabilities. That’s why we built Pinecone Assistant with a focus on delivering the highest-quality and dependable answers. Today, it already performs better than other assistant APIs for text-heavy technical data such as financial and legal documents.
Combined answer factual accuracy score (F1), reflecting the ability to locate relevant information in private data and accurately grounding the model's responses based on that information.
Answer quality will get even better over time across more domains, and will eventually support complex queries over multi-modal data.
Learn how we measure and benchmark answer quality by assistants.
Protect and control your data
Data sovereignty, privacy, and security is critical for any business shipping AI assistants. That’s why it’s our top priority as we build the Pinecone Assistant:
The data you upload is encrypted and isolated.
Your data is used as context and reference for answers in real-time; it is not used to permanently fine-tune or train the underlying language model. In essence you control what the assistant knows or forgets.
Even for the beta version, Pinecone Assistant is powered by enterprise-grade components that pass strict compliance requirements. Learn more about the security of
Pinecone Database
and
Azure OpenAI Service
.
We’re developing additional privacy and security features for Pinecone Assistant, and we welcome feedback from customers in regulated industries and enterprise environments.
Beta period starts today, with more to come
We’re releasing Pinecone Assistant in beta for developers to try and share their feedback. The starting limits are 1GB of file storage and 100 queries per month, but they may change during the beta period. You can expect some rough edges but also rapid improvement based on your feedback.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
