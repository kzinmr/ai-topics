---
title: "Text match filters for agents"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/text-match-filters/"
scraped: "2026-07-17T06:00:49.227766+00:00"
lastmod: "2026-07-13T14:09:47Z"
type: "sitemap"
---

# Text match filters for agents

**Source**: [https://www.pinecone.io/blog/text-match-filters/](https://www.pinecone.io/blog/text-match-filters/)

←
Blog
Text match filters for agents
Delivering scoped, accurate context, without pre-labeling entire datasets
Josh Coyne
Jul 13, 2026
Engineering
Share:
Jump to section:
The ambiguity problem
The solution: text match filtering
Where this generalizes
What changes for agentic applications
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Semantic search returns results that are close in meaning, not necessarily results that answer what someone meant to ask. A person scanning through can tell the difference and skip past the ones that miss the mark. An agent can't: it takes whatever comes back as ground truth and starts acting on it, with nobody checking the work first.
The sharpest version of that gap is unstated context: a query can be perfectly clear to the person asking it and still leave out information a system needs to answer it correctly. This post walks through that failure mode using a public dataset of 10,000 CNN news articles from Hugging Face, spanning 2022 to 2024, with each article's text and topic label stored as metadata, and shows how Pinecone's new text match filters fix it without requiring the dataset to be pre-labeled for every case in advance.
Follow along with the queries and results below in
this notebook
.
The ambiguity problem
Take the query "Who are the top presidential candidates?". A user in the United States asking this almost certainly means the U.S. presidential election. Nothing in the query says so.
Dense vector search alone returns this:
Rank
Article ID
Score
Excerpt
1
3433
0.8168
First round of voting, featuring 11 presidential candidates, takes place on April 23. Le Pen and Macron are tipped to...
2
8054
0.8138
Presidential candidates for France's mainstream parties failed to make the second round. Poll favorite Emmanuel Macron...
3
3421
0.8130
France holds its first round of the presidential election on Sunday. Candidates react quickly to the death of a pol...
Every one of these is about the French election, and every one is a legitimate semantic match, yet none of them answer the question the user actually meant to ask.
The obvious fix is to have the user rewrite the query as "top US presidential candidates," but that comes with two costs. First, it pushes the burden of writing a precise query back onto the user, who came in with what felt like a simple question. Second, in an agentic pipeline, a bad first retrieval costs more than a re-query: ask an agent to chart polling trends and analyze who's rising and falling, and if it builds that analysis on French election data, the tokens spent generating the wrong answer are wasted, so are the follow-on tool calls, and the error compounds at every step downstream. Multiply that across a few thousand queries and the cost stops looking incidental.
Restricting results by country with metadata filtering is possible, but it means labeling every record for every dimension that might matter, in advance: country, election year, local versus national race. Any filter dimension discovered after the fact requires reprocessing the entire dataset, which for production systems can mean billions of records, before it can be applied.
The solution: text match filtering
Full Text Search from Pinecone, now in public preview, supports text match filters: a lexical query that restricts the candidate pool for a semantic search to records matching specific text, without pre-labeling metadata for every case an application might need to handle.
Applying a text match filter for "United States" to the same query changes the candidate pool before the semantic search runs:
Rank
Article ID
Score
Excerpt
1
5326
0.8012
(CNN) Former Vice President Joe Biden swept to victories across southern states on Super Tuesday, but Vermont Sen. Bernie Sanders...
2
7641
0.7992
(CNN) The Human Rights Campaign Foundation announced Thursday it will host a CNN Democratic presidential town hall in California...
3
9859
0.7987
(CNN) President Donald Trump and Democratic presidential nominee Joe Biden have taken very different positions on a range of polic...
The query, model, and index are identical to the search above. The only difference is that the candidate pool was scoped to records containing "United States" in the article body before the vector search ran, and all three results now land on the actual U.S. race.
Where this generalizes
News search makes the ambiguity easy to see, but the same pattern shows up anywhere a query assumes context it doesn't state: industrial manuals scoped to a machine number or error code, insurance claims scoped to a policy number or type, legal search scoped to a case or jurisdiction. Most semantic search applications run into some version of this, since most queries leave something unstated.
These filters chain: combine them with boolean operators, stack them with metadata filters, or layer on more text match filters against other fields, and the candidate pool narrows along several dimensions in a single query.
What changes for agentic applications
An agent has no step where it double-checks that a semantically close result is actually the right one for the task. Whatever filtering needs to happen has to happen before the results reach the agent, not after. Text match filtering moves that correction into the query itself, without requiring the dataset to be pre-labeled for every filter an application might eventually need. For pipelines where a bad retrieval turns into a chain of wasted tool calls, narrowing the candidate pool at query time is cheaper than catching the error after the fact.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
