---
title: "Easily build knowledgeable chat and agent-based applications in minutes with Pinecone Assistant, now generally available"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pinecone-assistant-generally-available/"
scraped: "2026-05-10T01:27:16.199413+00:00"
lastmod: "2026-02-24T11:51:51Z"
type: "sitemap"
---

# Easily build knowledgeable chat and agent-based applications in minutes with Pinecone Assistant, now generally available

**Source**: [https://www.pinecone.io/blog/pinecone-assistant-generally-available/](https://www.pinecone.io/blog/pinecone-assistant-generally-available/)

←
Blog
Easily build knowledgeable chat and agent-based applications in minutes with Pinecone Assistant, now generally available
Gibbs Cullen
,
Nathan Cordeiro
Jan 22, 2025
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Today, we're excited to announce that Pinecone Assistant is generally available (GA) for all users. Developers of all skill levels have already created thousands of their own knowledgeable AI assistants across diverse use cases with Pinecone Assistant (e.g., financial analysis, legal discovery, and compliance assistants). Now, we’ve made it even easier to upload your documents, ask questions, and receive accurate, grounded responses. Increase time to value by creating and deploying production-grade solutions in minutes, knowing under the hood your assistants are powered by the same safeguards and benefits as our fully managed vector database.
Tl;dr: What’s new
With GA, Pinecone Assistant now includes:
Optimized interfaces
with new chat and context APIs powering chat and agent-based applications
Custom instructions
to tailor your assistant’s behavior and responses to specific use cases or requirements
New input and output formats
with added support for JSON, .md, and .docx files in addition to PDF and .txt
Region control
with options to build in the EU or US
Unlock immediate value for your team – just bring your data
Pinecone Assistant
is an API service built to power grounded chat and agent-based applications with precision and ease. Abstracting away the many systems and steps required to build
Retrieval Augmented Generation (RAG)
-powered applications (e.g., chunking, embedding, file storage, query planning, vector search, model orchestration, reranking, and more), Assistant accelerates RAG development, enabling you to launch knowledgeable production-grade applications in under 30 minutes, regardless of experience.
"Pinecone Assistant has become essential to our generative AI projects, accelerating the time between idea and implementation by 70%. It simplifies complex tasks like document chunking, embedding, and retrieval, letting us focus on outcomes, cut maintenance and scaling costs by 30%, and quickly demonstrate real results to clients." - Mark Kashef, CEO, Prompt Advisers
The underlying serverless architecture, intuitive interface, and built-in evaluation and benchmarking framework make it easy to get started (just upload your raw files via a simple API), quick to experiment and iterate, and effortless to scale and maintain. We’ve optimized the workflow end-to-end to ensure you have access to accurate, grounded information at every step—from document ingestion to query planning and reasoning to response generation. In fact,
our benchmarks
show Pinecone Assistant delivers up to 12% more accurate results than OpenAI Assistants.
The average “answer alignment score” reflects the ability to locate relevant information in private data and ground the model's responses accurately based on that information. Note: These results are x100 for increased readability.
Pinecone Assistant is powered by our fully managed vector database and shares the same safeguards. Your data is encrypted at rest and in transit, never used for training, and can be permanently deleted at any time.
What’s new with Pinecone Assistant:
During public preview, we introduced the
Evaluation API
,
expanded LLM support
, and
metadata filters
for Assistant. We've continued to develop Assistant to further improve the relevance of responses, increase customization capabilities, and expand the ways you can build with it.
Optimized interfaces to bring knowledge to chat and agentic applications
The new
Chat API
delivers structured, grounded responses with citations in a few simple steps. It supports both streaming and batch modes, allowing citations to be presented in real time or added to the final output. In short, you have control over how references appear.
We recommend that you chat with your assistant through the standard chat interface. It returns either a JSON object or a text stream, and provides more functionality and control than the OpenAI-compatible chat interface.
The new
Context API
, the context engine behind Pinecone Assistant, follows the same augmented retrieval process as the Chat API—but without the generation step—to deliver structured context (i.e., a collection of the most relevant data for the input query) as a set of expanded chunks with relevancy scores and references.
This makes it a powerful tool for agentic workflows, providing the necessary context to verify source data, prevent hallucinations, and identify the most relevant data for generating precise, reliable responses.
Context API can be used with your preferred LLM, combined with other data sources, or seamlessly integrated into agentic workflows as the core knowledge layer.
Here's how you can try it out:
-- To use the Python SDK, install the plugin:
pip install --upgrade pinecone pinecone-plugin-assistant requests 
-- If you are using Jupyter notebook or google Colab use
!pip install --upgrade pinecone pinecone-plugin-assistant requests
First, install the Python SDK and Assistant Plugin, and create a 'download util' function to download the DJI mini2 manual (below) and load it into Assistant.
wget -O dji_mini_2_user_manual.pdf https://dl.djicdn.com/downloads/DJI_Mini_2/20210630/DJI_Mini_2_User_Manual-EN.pdf
from pinecone import Pinecone
pc = Pinecone(api_key="YOUR_API_KEY")

# Let's download a file, in this case DJI user manual 
file_name = "dji_mini_2_user_manual.pdf"

# Create an Assistant and upload the file
assistant = pc.assistant.create_assistant(
    assistant_name="example-assistant", 
    region="us", # Region to deploy assistant. Options: "us" (default) or "eu".
)
response = assistant.upload_file(
	file_path=file_name,
	metadata={"type": "manual"},
	timeout=None
)
Easily include metadata and then you're ready to query your Assistant.
response = assistant.context(
    query="What are the DJI mini 2 pre-flight checks we need to perform?",
    filter={"type":{"$eq": "manual"}}
)

print(response.snippets[0])
# {'type': 'text', 'content': '© 2021 DJI All Rights Reserved...', ...}
Note: You can load the conversation history into Pinecone Assistant to better contextualize and tune your queries and results.
response = assistant.context(
	messages=[
{"role": "user", "content": "What is the DJI mini 2 battary capacity?"},
	{"role": "assistant","content": "The battery capacity for the DJI mini 2 is 2250 mAh"},
	{"role": "user","content": "And what are the pre-flight checks we need to perform?"}
],
filter={"type":{"$eq": "manual"}}
)


print(response.snippets[0])
# {'type': 'text', 'content': '...', ...}
Learn more and see an example output as a JSON object in our
documentation
.
Custom instructions to fine-tune assistants for your use case
In addition to metadata filters, Assistant now supports
custom instructions
, allowing you to further fine-tune responses to meet your needs.
Metadata filters
restrict vector search by user, group, or category, while instructions let you tailor responses by providing short descriptions or directives. For example, you can set your assistant to act as a legal expert for authoritative answers or as a customer support agent for troubleshooting and user assistance.
assistant = pc.assistant.update_assistant(
    assistant_name="example-assistant", 
    instructions="Use American English for spelling and grammar."
)
Customize the instructions to reflect your assistant’s role or purpose, for example, “Use American English for spelling and grammar.”
Expanded region control and input/output formats
With some recent additions to Assistant, it’s even easier to get started. You can now
create an assistant
in both the EU and US regions. In addition to PDF and .txt files, Assistant now also supports JSON, .md, and .docx files as inputs, and JSON format as an output. Additional support will be added in the coming months.
import json
msg = {
	"role": "user", 
	"content":"What is the Max Ascent Speed? Strucutre your answer as a json with the format: {'mode_name': 'speed'}"
}

response = assistant.chat(messages=[msg], json_response=True)

print(json.loads(response.message.content))
# {'Sport Mode': '5 m/s', 'Normal Mode': '3 m/s', 'Cine Mode': '2 m/s'}
Easily configure the region and output parameters for your assistant. This example uses the json_response parameter to instruct the assistant to return a JSON response.
Start building today
Pinecone Assistant is now generally available in US and EU regions for all users. For Standard and Enterprise users, usage starts at $0.05/Assistant per hour, and Context Processed Tokens are $5/1M tokens. See our
pricing page
for more information.
Register for our Pinecone Assistant 101 on-demand webinar
,
learn more in our deep dive
, and
start building knowledgeable AI applications in minutes today
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
