---
title: "Glasp achieves 5X cost savings in knowledge access for millions of users with Pinecone"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/glasp/"
scraped: "2026-05-10T01:27:07.268846+00:00"
lastmod: "2025-03-14T21:41:41Z"
type: "sitemap"
---

# Glasp achieves 5X cost savings in knowledge access for millions of users with Pinecone

**Source**: [https://www.pinecone.io/blog/glasp/](https://www.pinecone.io/blog/glasp/)

←
Blog
Glasp achieves 5X cost savings in knowledge access for millions of users with Pinecone
Valeria Gomez
Jun 5, 2024
Company
Share:
Jump to section:
A conversation with Kazuki Nakayashiki, CEO at Glasp
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
A conversation with Kazuki Nakayashiki, CEO at Glasp
Glasp
is a social web highlighter that enables users to highlight and organize quotes and ideas from the web, without the need to switch between screens, while also accessing the insights and learning of like-minded individuals. More than just a knowledge management tool, Glasp is a social hub that champions the democratization of learning. In a recent conversation with Kazuki Nakayashiki, CEO and co-founder at Glasp, we explored the pivotal role Pinecone plays in supporting Glasp’s mission to democratize access to learning and experiences with semantic search and retrieval of information.
Can you share more about Glasp? What are your company's goals, and how do they directly benefit your customers?
Glasp is a knowledge management platform with a unique social twist. We aim to enable users to capture and share valuable insights from the internet. By allowing users to highlight and annotate content, we help them curate information that resonates with them. This not only saves time but also builds a community where users can discover and learn from each other's curated content. Our mission is to democratize access to knowledge, making it easier for everyone to benefit from shared learning and insights. What I love most about working at Glasp is the impact we have on our users' lives. Knowing that we are building a tool that helps people find, organize, and share important information is incredibly fulfilling. It's exciting to see the positive feedback from our users and to know that we're making a difference in how people learn and connect.
Can you provide an overview of your application's functionality?
Glasp offers browser extensions and an iOS app that enable users to highlight, annotate, and summarize content they find online. AI plays a crucial role in enhancing these functionalities. For instance, AI helps in summarizing the content that users highlight, making it easier to digest and share. Our AI-driven features include finding similar ideas and creating personalized digital clones that can interact with users based on their saved information. These AI clones can answer questions and provide insights, creating a more interactive and personalized learning experience.
Can you share insights into your AI technology stack used in your application?
We leverage several advanced AI and ML techniques to power Glasp. For example, we use vector search with OpenAI embeddings to convert user highlights into vectors, which are then stored in Pinecone. This allows us to perform efficient similarity searches. For generating responses and summaries, we use large language models (LLMs) like ChatGPT 3.5 and 4.0. We also use models from Anthropic and Mistral AI for content summarization. Our custom-built Retrieval Augmented Generation (RAG) pipeline integrates with these models to provide accurate and contextually relevant information to users.
What are you currently doing with Pinecone?
Pinecone is integral to how we manage and retrieve data. When a user highlights text from a web page, article, or research paper, this text is first converted into a vector using OpenAI embeddings. These vectors capture the semantic meaning of the highlighted content and are stored in Pinecone. To ensure user privacy, each user's data is stored in a separate
namespace
. When a user seeks related content or recommendations, Pinecone identifies vectors similar to the query within the user's namespace. These vectors are then
filtered
and ranked to ensure relevance, and the most relevant results are presented to the user. For example, if a user highlights information about artificial intelligence in medical research, Pinecone helps us find and recommend similar content, enabling the user to explore related studies and insights. This process not only streamlines the organization and retrieval of learning materials but also enhances user engagement through personalized content suggestions.
In addition to content recommendations, we also use Pinecone for our AI clone. It acts like a digital clone, allowing users to ask their clone questions about the information they have captured. This digital clone functions similar to a chatbot but is tailored to look like the user based on the information they have saved. Whenever a user asks their digital clone a question, Glasp uses LLMs to understand the intention behind the question. The system edits, rephrases, and vectorizes the intention of the question. It then searches for similar answers using Pinecone. Once we get the results from Pinecone, we filter and review them ourselves. Based on the user's past highlights and notes, we use LLMs to generate an answer to the question.
How did you decide on a chunking strategy? Did you ever evaluate it against other methods?
In our chunking strategy, we're really honing in on user behavior and technical efficiency. What we've noticed is that users tend to highlight 2-3 sentences at a time while engaging with text on the web. This behavior has been instrumental in determining the ideal size for data vectorization. This method strikes a good balance between readability and contextual completeness. This strategy enhances the interaction with our AI clone feature, allowing users to ask questions based on their highlights and notes. These more focused chunks align perfectly with the typically concise queries our AI clone receives, ensuring more accurate and relevant responses.
When it comes to evaluation, we regularly assess the effectiveness of our chunking strategy and preprocessing methods using a combination of user feedback, human evaluation by our team, and technical performance metrics. We strive to constantly improve these methods to make our platform more user-friendly and technically reliable.
Do you have any data pre-processing tips or lessons learned?
Our primary objective with data pre-processing is to preserve the data's integrity while minimizing any unwanted noise. We carefully remove unnecessary spaces, special characters, and irrelevant formatting elements that could potentially impact retrieval performance. This cleanup process is essential to ensure our search queries yield high-quality vectors, maintaining the accuracy and relevance of our results.
What is your favorite Pinecone feature?
What I really like about Pinecone is its simplicity and user-friendly API. Integrating it into our system was a smooth process, and its impressive performance, including low latency and fast retrieval times, ensures a seamless user experience. The community support is also fantastic, offering valuable insights and assistance when needed.
“I really value Pinecone's simplicity and speed. It's easy to integrate with our AI stack, and the community support is exceptional. When I need guidance, I can count on the Pinecone community for valuable insights. It was an obvious choice for us due to its ease of use and the positive feedback we received from other developers.” -
Kazuki Nakayashiki, CEO and co-founder at Glasp
How has Pinecone helped support your team's vision?
Pinecone plays a crucial role in realizing our mission to democratize learning. Its efficient data storage and retrieval mechanisms enable us to gain insights into our users' interests, facilitating the delivery of personalized recommendations. This capability forms the cornerstone of our efforts to cultivate a vibrant community where knowledge exchange flourishes. Pinecone empowers us to cultivate meaningful connections among users who share similar interests, fostering a collaborative environment for learning and knowledge exchange.
Comparing the time before and after Pinecone, what jumps out to you as the biggest impact?
Pinecone has truly transformed our operations. Without it, we'd be struggling with the complexities of managing our vector database, draining our time and resources. It would have required a software engineer to manage it. However, Pinecone's managed service simplifies everything for us, allowing us to focus on innovating our platform rather than worrying about infrastructure management. With one millisecond query latency, Pinecone ensures that our users receive prompt and seamless access to the information they need.
“Pinecone saves us time and money by eliminating the need for a full-time data scientist to manage our vector database. It's simple, fast, and retrieves information in just one millisecond, so we never worry about latency” -
Kazuki Nakayashiki, CEO and co-founder at Glasp
What are your future plans for new applications and how does Pinecone fit into them?
Looking ahead, we plan to enhance our AI clone feature and explore voice cloning to create even more personalized interactions. Additionally, we aim to integrate blogging capabilities, allowing users to create content based on their collected information. Pinecone will continue to play a crucial role in these developments by providing the backbone for efficient data storage and retrieval, ensuring that our new features are both powerful and user-friendly.
As Glasp continues to grow, Pinecone remains a key partner driving the company forward in its mission to democratize access to other people’s learning and experiences. Kazuki shares, “I'm proudest of the vibrant community we've cultivated at Glasp, where users can unearth valuable insights, forge connections, and contribute to a shared pool of knowledge. Knowing that we're reshaping how people learn and engage with information fuels our passion every day."
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
