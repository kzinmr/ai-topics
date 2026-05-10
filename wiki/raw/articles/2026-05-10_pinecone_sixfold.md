---
title: "Sixfold's Transformation of Insurance Underwriting with Pinecone"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/sixfold/"
scraped: "2026-05-10T01:27:24.455376+00:00"
lastmod: "2025-03-14T21:40:34Z"
type: "sitemap"
---

# Sixfold's Transformation of Insurance Underwriting with Pinecone

**Source**: [https://www.pinecone.io/blog/sixfold/](https://www.pinecone.io/blog/sixfold/)

←
Blog
Sixfold's Transformation of Insurance Underwriting with Pinecone
Valeria Gomez
Apr 5, 2024
Company
Share:
Jump to section:
A conversation with Gregg Tourville, Head of Product Design at Sixfold
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
A conversation with Gregg Tourville, Head of Product Design at Sixfold
Sixfold
is dedicated to transforming insurance underwriting through the use of generative AI. Their mission is to secure insurmountable advantages for underwriters by understanding a carrier’s unique risk appetite. Sixfold synthesizes applications, extensive datasets and matches the risk to assist underwriters in better understanding and pricing insurance risks, ultimately improving capacity, accuracy and transparency in the industry. In a recent conversation with
Gregg Tourville,
Head of Product Design at Sixfold, we explored the pivotal role Pinecone plays in enhancing insurance underwriting processes, leveraging
hybrid search
that combines semantic and keyword search for more relevant results to underwriters queries.
Can you share more about Sixfold? What are your company's goals, and how do they directly benefit your customers?
At Sixfold, our mission is crystal clear: to revolutionize insurance underwriting through the power of artificial intelligence. We strive to streamline and modernize the underwriting process by harnessing cutting-edge AI technologies to rapidly and accurately synthesize vast volumes of information. By automating segments of insurance underwriting and equipping underwriters with enhanced capabilities, we enable them to focus on strategic decision-making rather than getting entangled in tedious data analysis tasks. Ultimately, our aim is to boost the efficiency, and traceability of underwriting decisions, benefiting our diverse clientele, which includes insurance carriers, reinsurers, and MGAs. Our platform maximizes capacity, enhances accuracy and transparency, and improves the overall quality of life for underwriters, thereby delivering tangible value to our clients and their end customers
Can you provide an overview of your application's functionality?
Our application serves as an underwriting brain, tailored to a carrier’s unique risk appetite, leveraging generative AI to streamline and accelerate various aspects of insurance underwriting. This includes synthesizing and summarizing complex data from diverse structured and unstructured sources such as PDFs, tables, charts, datasets and websites. The role of AI in our application is pivotal, as it enables us to understand, categorize, and contextualize this vast amount of information according to each customer's specific underwriting guidelines. By leveraging AI, we assist underwriters in quickly and accurately evaluating submissions, thus improving the speed, accuracy, and traceability of their decisions.
Can you share insights into your AI technology stack used in your application?
We use a combination of foundational models, open-source tools, and proprietary AI models to meet our specific underwriting needs. Our approach is to remain relatively agnostic, allowing us to use the best AI tools for each task. We've experimented with models from OpenAI, Anthropic, Cohere, and Mistral, among others. Our focus is always on using the models that provide the best results and are fit for purpose, while also ensuring enterprise-grade security and data privacy for our customers.
“We use Pinecone as our core vector database for hybrid search and retrieval of information playing a crucial role in organizing and contextualizing the large datasets involved in insurance underwriting.”
-
Gregg Tourville, Head of Product Design at Sixfold
What are you currently doing with Pinecone?
We recognized the need for a vector database to handle the vast amounts of data in insurance underwriting. Traditional databases often struggle with complex data structures, such as specialty insurance applications, medical records or datasets from various sources. Pinecone enables efficient processing and analysis of this data, extracting valuable insights and enhancing decision-making. Pinecone enables us to conduct sophisticated semantic searches, incorporating hybrid search techniques. This enables us to surface relevant information in response to user queries, ultimately enhancing accuracy and capacity.
When it comes to processing medical records at Sixfold for example, Pinecone plays a pivotal role. Consider the hefty 100-page PDFs we often receive in our Life insurance offering. We must break them down into digestible chunks representing individual doctor visits, adding metadata for easier retrieval later. This use of metadata helps us maintain transparency and credibility with our customers, countering skepticism towards AI-generated summaries in the insurance industry. By citing sources and providing detailed information, we gradually build trust in our AI-driven approach.
Once we complete the
chunking
and
metadata
addition, we dive into each chunk to extract crucial medical facts like diagnoses, prescribed medications, and procedures. Pinecone enables us to embed this extracted data into our database, providing a contextualized view crucial for underwriters to assess insurance risks. We also use
RAG
to enrich the extracted data continuously. This technique allows us to provide underwriters with additional context and details about the medical facts extracted from documents, helping them better understand how medical conditions impact insurance pricing. The goal is to ensure that all information provided is accurate, relevant, and aligned with the carrier's risk perspective. Overall, Pinecone streamlines the entire process, from data chunking to synthesizing actionable insights for underwriters.
What is your favorite Pinecone feature?
One of my favorite Pinecone features is its
hybrid search
. We can leverage both traditional keyword-based search and advanced vector search techniques, providing a versatile approach to data retrieval. This feature has simplified development for us and significantly enhanced the efficiency of our system. It enables underwriters to efficiently locate relevant information using familiar keyword queries while benefiting from the context-awareness and accuracy provided by vector representations. The hybrid retrieval feature not only streamlines the search process but also improves the overall user experience, making it easier for underwriters to access critical data and make informed decisions.
How has Pinecone helped support your team's vision?
Pinecone has been instrumental in supporting our vision of revolutionizing insurance underwriting. By leveraging Pinecone's capabilities, we've streamlined our data processing, facilitating the efficient management of various datasets. This has resulted in quicker access to relevant information for our underwriters, enabling them to make more informed decisions. Pinecone has accelerated our product development cycle, allowing us to quickly incorporate new data sources and improve the accuracy of underwriting query results.
“Pinecone emerged as the darling of the vector database scene, particularly favored by startups like ours. Its rapid deployment significantly expedited our progress, enabling us to showcase a functional product to stakeholders within just a couple of months." - Gregg Tourville, Head of Product Design at Sixfold
Comparing the time before and after Pinecone, what jumps out to you as the biggest impact?
Before Pinecone, extracting relevant information from documents was a time-consuming and expensive process. With Pinecone, what would have taken months of development now takes significantly less time. We estimate that Pinecone has helped us get to market
4X times faster
and has saved us valuable developer resources. As a result, we've been able to deliver a product that greatly speeds up underwriters' processes and focuses on enhancing user experience.
What are your future plans for new applications and how does Pinecone fit into them?
We plan to expand our applications to include interactive QA features, allowing underwriters to dig deeper into specific facts within insurance applications. Pinecone will play a crucial role in enabling this functionality by providing the necessary infrastructure for storing and retrieving relevant data. We aim to continue improving the capacity, accuracy and transparency of insurance underwriting.
"Pinecone has been instrumental in reducing our time to market significantly. By leveraging Pinecone's capabilities, we saved valuable development time and resources, allowing us to deliver our product faster and more efficiently." -
Gregg Tourville, Head of Product Design at Sixfold
As
Sixfold
continues to innovate, Pinecone remains an indispensable partner, propelling the company forward in its mission to redefine the insurance industry through advanced AI-driven solutions. Gregg shares, "Seeing the real impact of our work in the insurance sector is immensely gratifying. Within just eleven months, we've crafted a product that profoundly enriches underwriters' abilities, enhancing their work experience. Being part of a team that pioneers innovation and positive transformation in a traditionally conservative sector is truly fulfilling."
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
