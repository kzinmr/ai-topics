---
title: "Financial Research Assistant on AWS"
source: "Cohere Blog"
url: "https://cohere.com/blog/financial-research-assistant-cohere-aws"
scraped: "2026-10-30T06:01:01.291618+00:00"
lastmod: "2026-10-29"
type: "sitemap"
---

# Financial Research Assistant on AWS

**Source**: [https://cohere.com/blog/financial-research-assistant-cohere-aws](https://cohere.com/blog/financial-research-assistant-cohere-aws)

Key takeaways
Build a financial research assistant on Amazon Web Services.
Combine Cohere models with Amazon services to search financial filings and generate answers with page-level citations.
Optimize retrieval quality, latency, and cost.
Use Embed Pro for high-quality document indexing and Embed Fast for low-latency queries, with configurable embedding dimensions and quantization to balance accuracy and storage.
Improve search relevance with Rerank.
Reorder retrieved pages using Rerank Pro, and use Context Focus to identify relevant passages and reduce the amount of text sent to the answer model.
Handle complex financial documents.
Use Cohere Parse for scanned or table-heavy pages, and combine text and page images to help the answer model interpret financial figures and preserve context.
Deploy and experiment in your own AWS account.
Use the CloudFormation-based demo to explore retrieval, reranking, Context Focus, and citation-backed answers while understanding the tradeoffs of different configurations.
As a financial analyst much of the day comes down to finding one number in a filing that runs to hundreds of pages, and then proving where it came from. Neither is as easy as it sounds. The number is rarely in the body text. It usually lives in a table, a footnote, or a chart, and it can show up in different places under different names.
In this post, we show how to build a research assistant for financial filings with Cohere models on Amazon SageMaker AI — Embed for search, Rerank for ordering the results, and Parse for turning hard pages into clean text. Anthropic Claude on Amazon Bedrock will be used to write the answers, with a citation for every claim.
We will start with what makes this work difficult followed by an overview of the solution, and then spend most of the post on the design decisions behind it and when you would decide differently. At the end, we show how to deploy the solution in your own AWS account and try it yourself.
Why financial research is hard to automate
Financial research looks like a search problem, but it has features that break simple approaches.
The answer lives in the layout.
Take a 10-K, the annual report that US public companies file with the Securities and Exchange Commission, covering the business, its risks and its audited financial statements (
what a Form 10-K contains
). The figure you need from it is usually in a table in the form of net interest income by year, regulatory capital by tier, charge-offs by loan type etc. When a PDF is converted to plain text, tables lose their row and column relationships, multi-column pages can come out in the wrong order, and charts often disappear.
An unverifiable answer is not useful.
An analyst cannot put "the CET1 ratio was 11.9%" in a memo without knowing which filing and which page it came from, and whether the figure came from a table, a chart or a sentence. An assistant for this work has to show its sources, and the person reading has to be able to check them quickly.
Volume and cost add up.
A research team might index thousands of filings across many years. Every page is embedded once, but every question is embedded too, and every model that runs on every question adds time and cost.
Not every document is clean.
Filings arrive as digital PDFs, but also as scanned exhibits, faxed agreements, and photographed pages that have no text layer at all.
Questions do not always come in the document's language.
Teams that cover several markets often ask in one language about documents written in another.
So a useful assistant has to do a few things like find the right page when the answer is in a table, make every answer checkable, keep cost and latency under control, cope with pages that are not clean, and work across languages.
Solution overview
The solution is a research assistant that answers questions about a collection of filings and shows for every claim, the page it came from. It uses four models, each with one job:
Cohere Embed
turns each page, and each question, into a vector which is a list of numbers that captures its meaning, so that pages about the same thing as the question sit close to it.
Embed comes in two tiers
:
Embed Pro
, built for the highest retrieval quality and offline indexing, and
Embed Fast
, built for low latency on the live request path.
Cohere Rerank
takes the question and the best candidate pages from the vector search, reads each pair together, and puts them in a better order. With
Context Focus
, Rerank can also mark the passages on each page that answer the question. Like Embed, Rerank comes in two tiers:
Rerank Pro
, built for the highest accuracy, and
Rerank Fast
, built for lower latency. We use
Rerank Pro
, because for a financial assistant finding the right page usually matters more than a faster answer.
Cohere Parse
reads a page image and returns a clean Markdown, with tables as real rows and columns. It is used for pages whose text is weak.
Anthropic Claude on Amazon Bedrock
reads the top pages and writes the answer, citing each page.
People can use it through a web app with three functions:
Assistant.
Ask a question about the filings. The assistant finds the most relevant pages, reads them, and writes an answer in which every claim cites its page. Each citation also says whether the fact came from a table, a chart, body text, a footnote or a figure, and one click opens the page image to check it.
Search.
The same search, without a generated answer. It can show the results with and without Rerank side by side, so you can see how reordering changes them, and the Rerank column shows the passage Context Focus picked on each page.
Parse.
Parse extracts tables as rows from pages that you can download, and scanned-looking pages turned into text.
Under the hood there are two flows.
Ingestion
runs once per page where Parse runs first, for the pages that need it, then text is embedded with Embed Pro, and the vector is stored into a vector index.
Answering
runs on every question where Embed Fast embeds the question then the closest pages are retrieved and, optionally, reordered by Rerank. Finally, Claude writes the answer from the top pages. The Cohere models run as real-time endpoints on Amazon SageMaker AI, deployed from AWS Marketplace; the vector index is Amazon OpenSearch Serverless; the web app, sign-in, API and ingestion pipeline are serverless AWS services.
Design decisions, and why we made them
Each ofthe challenges forced a choice.
Challenge
What we decided
Why
Answers live in tables
Search on page text that keeps the table markup, and let Claude look at the page image when it writes the answer
Text is cheap to embed and search; the image recovers what the text lost, at the moment a figure is quoted
Answers must be checkable
Cite every claim with its page and where on the page it is (table, chart, text, footnote, figure), and show the page image
The reader can go straight to the source and see what kind of evidence it is
Cost and latency
Index with Embed Pro and query with Embed Fast. Store vectors with 1,024-dimension int8 vectors and make Rerank and Parse optional stages, making the endpoints easy to switch off
Spend on quality once, at indexing; keep every question fast; pay for extra stages only where they help
Pages that are not clean
Route only low-text and table-heavy pages to Parse
Parse is applied where it can change the result, and each page is parsed once
Long pages where only a few lines matter
Send Claude the passages that Rerank's Context Focus picks, together with the page image
Fewer input tokens, the image keeps the context the passages leave out, and the reader sees exactly what the answer used
Questions in other languages
Search all languages in one multilingual embedding space, with no translation step
Eliminates the need for a separate translation step, simplifying the pipeline and avoiding translation-related processing costs.
Index with Embed Pro, query with Embed Fast
Indexing and querying have different needs. A page is embedded once, ahead of time, so you can afford the most accurate model. A question is embedded while someone waits, thousands of times a day, so speed and cost per call matter most. Embed Pro and Embed Fast share
one embedding space
, which means a question embedded with Fast can be compared directly with pages embedded with Pro. You get Pro's quality in the index and Fast's speed on every question, without rebuilding the index. The figure below shows where each model sits.
The second choice is the size of each vector. Embed offers
six output sizes, from 256 to 2,048 dimensions, in float, int8 or binary
. The embeddings are Matryoshka representations where the model is trained so that the first dimensions carry the most meaning, so a shorter vector keeps most of what a longer one says. We chose
1,024 dimensions stored as int8
, one byte per dimension:
Storage
-
A 1,024-dimension int8 vector takes 1 KB of raw storage, compared to 8 KB for a 2,048-dimension float32 vector—an 8x reduction. For a million pages, that translates to approximately 1 GB versus 8 GB of raw vector data. Actual vector index storage and costs will also depend on indexing structures, metadata, and infrastructure overhead.
Quality
- 1,024 is the middle of the range, and int8 keeps far more detail than binary. That is a sensible default when the answer has to be the right page, not just a similar one.
When to change it
- Use 2,048 dimensions if retrieval quality matters more than storage. Use 512, 256 or binary vectors for very large archives where cost dominates; binary is 32 times smaller than float32.
Whatever you choose, the query side must use the same size and format as the index. Changing it later means embedding every page again, so it is worth settling early.
Embed the page text, and keep the image for the answer
Embed can embed a page's text, the page as an image, or both together as one vector, all in the same space. Each choice suits a different kind of document.
Page text
is the cheapest and simplest: one vector per page, Rerank reads text, so it can work on the same pages, and you can show a text snippet next to each result. The catch is that it is only as good as the extracted text where most of the time tables can lose their structure, charts disappear, and a scan has no text at all until something reads it.
The page image
needs no text extraction. Tables, charts and layout are seen as the page looks, and it works on scans and photographs. It costs more per page, it is harder to show why a page matched, and Rerank still needs text.
Both together
(a fused text-and-image vector) gives the search both views of the page, at the cost of the image price and a larger embedding call.
Annual reports and 10-Ks are digital documents with good text, so we embed the page text. What text loses, mostly charts and complex tables, we recover at answer time instead, by letting Claude see the page image. If your pages are mostly scans, slides, diagrams or charts, such as investor presentations, scanned agreements or faxed exhibits, embed the image or both.
One embedding space for every language
Embed supports more than 100 languages and a 128K-token context window
. A question and a page land in the same space regardless of language, so a French question such as "impact de l'immobilier commercial sur le segment Global Banking de Bank of America" can find the English Bank of America pages directly. Claude then writes the answer in the language of the question and keeps the citations as they are.
We chose this over translating questions into English first. There is no translation step to build, run or pay for, and no risk of a mistranslated term sending the search the wrong way. Rerank Pro is also
multilingual, with support for more than 100 languages
. As always, check the languages that matter to you on your own documents.
Make Rerank an optional stage, and make its effect visible
Vector search is fast because each page is compared with the question through a single number, the distance between two vectors. A reranker works differently where it reads the question and each candidate page together, which lets it weigh details a single vector cannot hold. Rerank Pro
reads up to 32K tokens of question and page together, works across more than 100 languages, and handles semi-structured content such as tables and JSON
. In this design, vector search returns 30 candidates and Rerank picks the five that go to Claude.
Rerank sits on the query path, so its latency is felt on every question. We still chose Rerank Pro over Rerank Fast, because in financial research a wrong page costs more than a slower answer. If interactive speed matters more for your users, Rerank Fast takes the same requests and returns the same kind of results, so switching between them is a configuration change, not a code change.
That extra reading costs time on every question and an endpoint to run, and how much it helps depends on your documents and your questions. So we made Rerank a stage you can switch on or off, and made its effect visible: the Assistant shows how long each step took, and Search can show the two result lists side by side, with arrows for how each page moved.
When should you turn it on? Look at where the right page lands without it. If it is usually at or near the top, leave Rerank off and keep answers fast. If it often appears lower in the list, or questions are long and specific, Rerank is the usual fix.
Rerank 5 also returns a
calibrated relevance score between 0 and 1
for each page, so the same cut-off means the same thing from one question to the next. You can use it to tell the user that no page is a good match, or to trigger another search, instead of answering from weak pages.
Parse only the pages that need it
Parse reads a page image and returns
Markdown or content blocks, with bounding boxes, and understands tables, forms, diagrams and images
. It is a GPU endpoint you pay for by the hour, and a clean digital page already has usable text, so we use it selectively. A router in the ingestion step decides page by page:
Pages with very little text go to Parse (a cover, or a scan with no text layer)
Pages where most of the text sits inside tables go to Parse
All other pages keep their existing text.
The Parse output is saved, so each page is parsed once, however often you rebuild the index. If you need tables as data, for a spreadsheet or a database, Parse is also the way to get them out of the page.
Let the answer model read the page, and say where each fact came from
Search runs on page text, but the answer does not have to. For each of the five pages it picks, the query function sends Claude the page image together with the page text, either the full extracted text or only the passages Rerank marked (see the next section), and tells Claude to trust the image where the two disagree. That is what lets an answer come from a chart, or from a table whose structure the text lost.
Claude is also told to answer only from those pages, to say so plainly when they do not contain the answer, and to cite every claim in the form [document page | kind], where the kind is table, chart, text, footnote or figure. The app turns each citation into a numbered link to the page image, shows the kind next to it, and repeats it on the page ("Answer taken from: table"). An analyst can see which page and type of content the assistant cites as supporting a capital figure, and open the original page to verify the information directly.
The tradeoff is additional input tokens and processing time for Claude. Including five page images alongside their text increases token consumption and response latency, depending on image resolution, page content, and the model used. The demo has a switch to leave the images out, so you can see the difference on your own questions.
Send Claude only the passages that matter
Even with the right five pages, most of each page is not about the question. A 10-K page can hold a whole table, a page of risk factors or several unrelated notes, and Claude reads, and you pay for, all of it.
Rerank 5 can do more than order pages. With Context Focus turned on, it also returns the passages on each page that match the question, as character ranges with a relevance score. It is a setting on the Rerank request, not a separate model, and it does not change the ranking. In this design, the query function asks Rerank for the passages on the five chosen pages, and sends Claude only those passages, in page order, instead of the full page text.
That has three effects:
Fewer input tokens.
Claude reads only the relevant part of each page's text, so answers cost less and come back faster.
A sharper prompt.
With the unrelated text gone, there is less for the answer model to be distracted by.
Easier checking.
The app highlights the passages in the page text, so the reader sees exactly what the answer was based on, not just which page.
The tradeoff is context. A passage on its own can lose what surrounds it, such as a table's column headings or the year a column refers to. Context Focus is most effective for targeted questions where specific information can be identified and retrieved. Structured content, such as tables and forms, can be more challenging to split into meaningful chunks because important relationships may span multiple sections. For broader tasks, such as summarizing an entire page, providing the full page content generally produces more complete and accurate results. However, Cohere's internal evaluations show that Context Focus retains the vast majority of answer accuracy even when reducing input tokens by 50–75%, demonstrating that the tradeoff between token reduction and accuracy is far from linear.
This is where the page image earns its place, Claude still sees the whole page, so it can read the headings and units the passages left out. If the lowest token count matters most, send the passages without the images; if the figures must be exact, send the passages with the images. Context Focus returns relevant passages as part of the same Rerank request, without requiring a separate model or additional API call.
The demo has a switch for each: Context Focus and Page images. Each answer shows how many tokens went to Claude and highlights the passages that were sent, so you can see the tradeoff on your own questions.
Make the expensive parts easy to switch off
The Cohere models run as real-time SageMaker endpoints, and a real-time endpoint bills for every hour it exists, whether or not anyone is asking questions. For a pilot, or a team that works in bursts, idle GPU hours are the largest cost. So the deployment has one setting that removes all the model endpoints while keeping the data, the index and the web app. Turning the models back on later needs no new ingestion. In steady production use, you would add autoscaling and alarms instead.
Choosing a pipeline for your documents
Which stages you need depends on your documents. The figure below is the decision guide we use. It has two steps:
1. Whether to parse the pages before embedding them
2. Whether to rerank the results
Embed + Rerank
is a good starting point for clean digital documents when ordering matters more than speed.
Embed only
is the fastest, when speed matters more than ordering.
Parse + Embed
(with or without Rerank) is for scans, faxes, photos, and dense tables where exact figures matter.
Parse only
is for turning tables, forms, and invoices into structured data, not search.
Note:
Rerank is not limited to vector search. It can also improve results from keyword-based retrieval methods such as BM25, enabling workflows like Parse + Rerank without requiring embeddings.
Questions to ask about your own documents:
if .....
Then consider
Your documents are digital and have good text
Embed the text; start without Parse
Pages are scans, photographs or faxes
Parse before embedding, or embed the page image
Answers are exact figures in dense tables
Parse those pages, and let the answer model read the page image
Pages are mostly charts, slides or diagrams
Embed the page image, alone or with the text; let the answer model read it
Interactive speed matters most
Query with Embed Fast; leave Rerank off
The right page often appears low in the results
Add Rerank
Pages are long, or the cost of input tokens matters
Turn on Rerank with Context Focus, and send the answer model the passages
Users ask in several languages
Use the multilingual embeddings directly; no translation step
Whatever you choose, test it on your own documents and questions. A public benchmark tells you how a model behaves on that benchmark's pages, not on your filings, scans or company specific style guides.
Beyond financial filings
The pipeline is not specific to banks. The input is a set of page images and their text, so a different set of documents gives you a different assistant. The same pattern applies wherever answers sit in tables, forms and layouts:
Insurance:
policy documents, claims and forms, where Parse's structured output can feed downstream systems.
Legal:
contracts, case files and regulatory material, where clause lookup needs page-level citations.
Manufacturing and energy:
technical manuals and compliance documents with diagrams and tables, where embedding or reading the page image keeps figures usable.
Public sector and life sciences:
government and regulatory reports, scientific papers.
Try it yourself
We built a demo of this solution that you can deploy into your own AWS account with one AWS CloudFormation template. The template creates the Cohere model endpoints, the vector index, the ingestion pipeline, the API, and the web app with sign-in.
The code is on GitHub
.
Scope of the demo
The demo is a working starting point, not a production system. It runs on three public annual reports (Bank of America, Morgan Stanley and Wells Fargo, fiscal 2024; 928 pages) from the finance subset of the
ViDoRe V3 benchmark
(
paper
), which also provides the sample questions in English, French, Spanish, German, Italian and Portuguese.
To keep the demo small and quick to try, we made some choices that differ from the design above:
Pre-extracted document text:
Pages are indexed using text provided by the benchmark dataset, simplifying deployment. While the architecture supports Cohere Parse for scanned and complex documents, the demo does not include parsing arbitrary uploaded PDFs.
Embed Pro for both indexing and querying:
The demo uses Embed Pro for document indexing and query embeddings, eliminating the need for a separate Embed Fast endpoint and reducing GPU costs.
Rerank Fast instead of Rerank Pro:
Rerank Fast runs on smaller GPU instances, avoiding the higher GPU requirements and potential capacity constraints of Rerank Pro. Both use the same request and response format, so switching to Rerank Pro requires only a template configuration change.
Configurable retrieval and answer generation:
Rerank is enabled by default in the Assistant, with switches for Rerank, Context Focus, and page images. Search runs without Rerank by default but allows side-by-side comparisons to evaluate the impact on relevance, latency, and token usage.
Minimal GPU infrastructure:
The demo uses one
ml.g5.xlarge
instance per deployed model in
us-east-1
, with AWS Marketplace model packages configured for that Region.
Simplified security and access:
The demo includes one user, an OpenSearch collection with public network access protected by a data access policy, and no Bedrock Guardrails. These settings minimize deployment complexity and are intended for evaluation, not production.
Fixed document dataset:
The demo loads a predefined set of financial filing pages rather than supporting ingestion of user-uploaded PDFs.
Things to consider before deploying in a production environment:
Network:
use a VPC endpoint and private access for OpenSearch Serverless.
Identity:
use your identity provider, with per-user or per-team access to documents.
Encryption:
the data bucket uses a customer-managed AWS KMS key; other stores use AWS-managed or AWS-owned keys.
Operations:
add monitoring, alarms, endpoint autoscaling and a budget alarm.
Query model:
add Embed Fast for questions.
Reranker:
use Rerank Pro.
Deploy it
The
README in the GitHub repository
walks through the deployment step by step: the Marketplace subscriptions and Bedrock access it needs, deploying the stack, loading the data, and signing in. It also covers the cost and how to clean up. The model endpoints bill every hour they run, so turn them off when you finish.
Key takeaways
Building a financial research assistant requires more than finding relevant documents. It means retrieving the right information, preserving context from tables and figures, and making answers easy to verify. By combining Cohere Embed, Rerank, and Parse with AWS services, this architecture provides a starting point for building research assistants that work with complex financial documents.
The key design considerations are:
Start with retrieval quality.
Choose an embedding strategy based on your documents and validate retrieval performance before optimizing answer generation.
Match the pipeline to your documents.
Use text embeddings for clean documents, Parse for complex layouts and scanned pages, and image embeddings when visual information matters.
Balance quality, latency, and cost.
Use Embed Pro for indexing and Embed Fast for querying, and add Rerank and Parse where they provide value.
Send the model only what it needs.
Rerank's Context Focus picks the passages that answer the question, and the page image keeps the context around them.
Make answers verifiable.
Provide page-level citations and access to the original document so analysts can check the supporting evidence.
Learn more
To explore the models, technologies, and performance benchmarks relevant to this solution:
Cohere Embed
Cohere Rerank
Cohere Rerank 5 – Retrieval Quality and Context Focus Benchmarks
Cohere Embed 5 – Model Capabilities and Improvements
Cohere Documentation
Amazon SageMaker AI
Amazon OpenSearch Serverless
Amazon Bedrock
Blog
Written By
Payal Singh
Solutions Architect, Partnerships
Tags
Enterprise AI
AI for Developers
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
