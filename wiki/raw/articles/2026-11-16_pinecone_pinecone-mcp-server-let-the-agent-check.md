---
title: "Pinecone MCP Server: Let the Agent Check, Let a Script Load"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pinecone-mcp-server-let-the-agent-check/"
scraped: "2026-11-16T06:00:18.100121+00:00"
lastmod: "2026-11-15T20:16:46Z"
type: "sitemap"
---

# Pinecone MCP Server: Let the Agent Check, Let a Script Load

**Source**: [https://www.pinecone.io/blog/pinecone-mcp-server-let-the-agent-check/](https://www.pinecone.io/blog/pinecone-mcp-server-let-the-agent-check/)

←
Blog
Pinecone MCP Server: Let the Agent Check, Let a Script Load
Team Pinecone
Aug 28, 2025
Engineering
Events
Share:
Jump to section:
What a Coding Agent Can't See Without the MCP
Set Up the Server and Give the Agent a Spec
Create and Test Through the Agent
When to Load With a Script Instead
Have the Agent Write the Loader, Then Check It
Query Both Indexes With Cascading Search
Next Steps
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Ask the agent in Cursor to load 30 product descriptions into Pinecone. It writes a tidy script, you run it, and nothing alarming prints. Did all 30 records land in the right index and namespace? The agent can't tell you. It has never seen your Pinecone project, only the code it wrote.
On August 28, 2025,
Arjun Patel
, Senior Developer Advocate at Pinecone, presented "Zero to Semantic Search with Pinecone's MCP Server, Cursor and Claude Code." He built search for a made-up snack shop from inside both tools: two indexes created and checked through the Pinecone Developer MCP server, loaded by a script the agent wrote.
The server is most useful as the agent's view of index state, and least useful as the thing that loads your data.
This post was adapted from
Arjun Patel
's webinar
Zero to Semantic Search with Pinecone's MCP Server, Cursor and Claude Code
. Here's the full replay:
Watch "
Youtube Video Player
" on YouTube
Watch
What a Coding Agent Can't See Without the MCP
Without the MCP, a coding agent works from the code in your repo and nothing else. It has no way to check whether an index exists, what's in it, how many records it holds, or whether the last upsert succeeded. You'd have to tell it, and you probably don't keep a record of every upsert script you've run inside the IDE.
With the MCP connected, "did that work?" becomes a tool call. The
Model Context Protocol
is a standard way to connect AI applications to outside tools (its docs compare it to a USB-C port for AI applications). The
Pinecone MCP server
gives the agent nine tools:
Job
Tool
What it does
Docs
search-docs
Searches the official Pinecone documentation
Inspect
list-indexes
Lists all Pinecone indexes
Inspect
describe-index
Describes an index's configuration
Inspect
describe-index-stats
Reports on the data in an index, including record count and namespaces
Change
create-index-for-model
Creates a legacy integrated index that embeds text with a hosted model
Change
upsert-records
Inserts or updates records in a legacy integrated index
Query
search-records
Searches a legacy integrated index with a text query, with optional filtering and reranking
Query
cascading-search
Searches across multiple indexes, deduplicating and reranking the results
Query
rerank-documents
Reranks records or text documents with a reranking model
Seven of the nine change nothing. They're how the agent looks before it acts and checks after.
search-records
also saves a step. Instead of writing a script that embeds a query and searches with it, ask the agent to run a few queries and show you what comes back.
search-docs
helps when an agent writes outdated Pinecone code. Point it at the docs before it writes anything, and use it again to check what it wrote.
The server has one hard limit. It works only with indexes that use integrated embedding, where Pinecone embeds your text with a hosted model such as
llama-text-embed-v2
or
pinecone-sparse-english-v0
. If you fill an index with vectors from OpenAI, Cohere or your own Hugging Face model, the MCP can't work with it.
The MCP's create, upsert and search tools work on what the docs now call a legacy integrated index. New indexes are now
document indexes
(as of API version
2026-07
, the REST API creates only those), and legacy indexes keep working for existing workloads. Everything below runs on legacy integrated indexes. When you're ready to move, see
Move to the Documents API
.
Set Up the Server and Give the Agent a Spec
The quickest setup is a plugin. The
Claude Code plugin
and the
Cursor plugin
each bundle the MCP server with Pinecone skills and slash commands (the
AI coding tools overview
covers the rest). In Claude Code:
claude plugin install pinecone
In Cursor, run
/add-plugin pinecone
in chat.
If you only want the MCP server, add it by hand. You'll need Node.js with
npx
on your
PATH
. In Claude Code:
claude mcp add-json pinecone-mcp \
  '{"type": "stdio",
    "command": "npx",
    "args": ["-y", "@pinecone-database/mcp"],
    "env": {"PINECONE_API_KEY": "YOUR_API_KEY"}}'
Restart Claude Code. Then, run the
/mcp
command to check the status:
> /mcp 
    ⎿  MCP Server Status

      • pinecone-mcp: ✓ connected
In Cursor, create
.cursor/mcp.json
in your project root:
{
  "mcpServers": {
    "pinecone": {
      "command": "npx",
      "args": [
        "-y", "@pinecone-database/mcp"
      ],
      "env": {
        "PINECONE_API_KEY": "{{YOUR_API_KEY}}"
      }
    }
  }
}
Then go to
Cursor Settings > MCP
to see the server and its tools. Keep the real key in an environment variable or a
.env
file (the Cursor plugin reads it from
.env
at the workspace root). Don't put it in a file you commit or on a screen you share.
The server gives the agent access to Pinecone. A spec file tells the agent what you're building. In Claude Code that's
CLAUDE.md
, which is injected into every request. In Cursor it's a rule file under
.cursor/rules/
with
alwaysApply: true
, so it rides along with every call to the model. The two can hold the same content.
Here's the spec we used for the snack shop, reconstructed for this post. It carries the same configuration, but it isn't the original file:
# Search and Snack

A snack recommender for a neighborhood snack shop. Users describe what
they're craving; the app returns matching snacks.

## Data
- Every item is savory or sweet, with a one- or two-sentence description.
- Records follow @records_example.jsonl: `_id`, `text` (embedded),
  `name`, `category`.
- If you're upserting a lot of data, write an upsert script, and learn
  how by searching the Pinecone docs with `search-docs`.

## Index configuration
- Dense: `snacks-dense`, model `llama-text-embed-v2`, field map `text`,
  namespace `snack-descriptions`
- Sparse: `snacks-sparse`, model `pinecone-sparse-english-v0`,
  field map `text`, namespace `snack-descriptions`
The
@
reference pulls in an example records file, so generated data matches the schema. Every Pinecone record needs an
_id
,
text
is the field that gets embedded, and the other fields are stored as metadata. Two illustrative rows, written for this post:
{"_id": "snack-001", "text": "Crispy bacon-wrapped jalapeño poppers stuffed with cream cheese and sharp cheddar.", "name": "Bacon Jalapeño Poppers", "category": "savory"}
{"_id": "snack-016", "text": "White chocolate truffles with a tart raspberry center.", "name": "White Chocolate Raspberry Truffles", "category": "sweet"}
With the spec in place, a one-line prompt creates the right index:
Please only create the dense index with the Llama model, and report back to me.
The agent reads the index name and model from the spec and calls
create-index-for-model
for
snacks-dense
with
llama-text-embed-v2
. The prompt names neither the index nor the exact model.
Create and Test Through the Agent
The whole test loop in Claude Code takes seven steps, starting from an empty project:
Run
/mcp
and confirm
pinecone-mcp
is connected.
Ask which indexes exist. The agent calls
list-indexes
and finds none.
Create
snacks-dense
from the spec, as above.
Ask for 30 sample records in
snacks.jsonl
. Following the spec, a short generation prompt and the example file, the agent writes 15 savory and 15 sweet snacks, each with an ID.
Upsert the first five through
upsert-records
.
Call
describe-index-stats
to confirm they're in.
Search for "I'm craving something fried", top 3.
The results are herb-crusted mozzarella sticks, bacon jalapeño poppers and brownies. Brownies came back because the index holds five records, and a top-3 query returns three of them whether or not they're relevant. A test index this small shows the plumbing works but can't show whether ranking does.
Pinecone is eventually consistent, so there can be a short delay before upserted records show up in queries (
known limitations
). The check we recommend is to compare the count from
describe-index-stats
with the number you expect.
No scripts so far. Every Pinecone operation was an MCP tool call you could read before it ran.
When to Load With a Script Instead
So why not upsert all 30 the same way?
Because of how the upsert happens. The agent reads the records, then writes every one of them into the arguments of the
upsert-records
call. Five records make a short call. At 100 or 200 entries, the model has to generate a really long function call, and you might run into some issues.
The server isn't meant for heavy upsert workloads, especially inside the IDE.
Good for
Not meant for
Learning Pinecone and testing your code
Heavy upsert workloads
Creating integrated indexes from Pinecone-hosted models
Replacing scripts entirely
Small upserts to check that an index works
Indexes that use third-party embeddings
Searching the docs to write scripts
That's why we keep bulk loading in a script. It batches records instead of writing each one into a tool call, and you can re-run it. Text records go up to 96 per request, the max batch size of the hosted embedding models that convert them (
operation limits
).
The same split holds for a knowledge base of business documents. Writing a few records through the MCP is probably fine. For the full write workload, use a sync script that re-runs whenever a new file lands in a folder, with chunking code to split documents first. If you only need read-only retrieval over those files, look at an
Assistant MCP server
instead.
Have the Agent Write the Loader, Then Check It
The spec already says that for a lot of data, the agent should write an upsert script and learn the API from
search-docs
. The prompt in Cursor (condensed here) spells it out:
We need to write an upsert script for Pinecone that takes snacks.jsonl,
upserts it using Pinecone's Python SDK into snacks-dense and snacks-sparse,
and reports on the records that are there. Make it as simple as possible and
easy to run with uv in the command line. Use the search-docs tool to
understand how to upsert data for integrated inference in Pinecone in Python.
Call the script upsert_snacks.py.
The
search-docs
instruction sends the agent to the docs before it writes a line, so the script is grounded in current documentation instead of whatever the model saw in training. A second rule file in the project, a short spec for what the upsert script should do, saves typing the details into the prompt.
Don't let the agent run it. Reject the auto-run and read the script: the imports, how it reads the file, the index names, the namespace. Then run it yourself, with your API key and both index hosts (
SNACKS_DENSE_HOST
,
SNACKS_SPARSE_HOST
) in a
.env
file:
uv run --env-file .env upsert_snacks.py
Run Cursor in approval mode for the same reason, so every MCP call shows its arguments before it runs. If an agent keeps reaching for one tool (calling
rerank-documents
on everything, say), switch that tool off in Cursor's MCP settings.
When a generated script is wrong, you can tell the agent to retry and keep calling the MCP until the problem resolves. That only goes so far. At some point you'll probably have to step in, say what's wrong, and adjust the context you're passing the model.
A minimal version of the loader, written for this post from the docs for
upserting text into a legacy integrated index
, reads
snacks.jsonl
and upserts it into both indexes in batches of 96:
# upsert_snacks.py: a minimal loader for snacks.jsonl
import json
import os

from pinecone import Pinecone

NAMESPACE = "snack-descriptions"
BATCH_SIZE = 96  # max batch size for records with text

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
INDEX_HOSTS = {
    "snacks-dense": os.environ["SNACKS_DENSE_HOST"],
    "snacks-sparse": os.environ["SNACKS_SPARSE_HOST"],
}

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

with open("snacks.jsonl") as f:
    records = [json.loads(line) for line in f if line.strip()]

for name, host in INDEX_HOSTS.items():
    index = pc.index(host=host)
    for start in range(0, len(records), BATCH_SIZE):
        index.upsert_records(
            namespace=NAMESPACE,
            records=records[start:start + BATCH_SIZE],
        )
    print(f"{name}: sent {len(records)} records")
For 30 records that's one request per index. The loop matters once the file grows.
The script only knows what it sent. Whether the records landed is a question for the MCP:
I ran the script. Can you check our indexes and see if the 30 records are there in each?
The agent calls
describe-index-stats
on
snacks-dense
and
snacks-sparse
. Both report 30.
Query Both Indexes With Cascading Search
cascading-search
queries several indexes, deduplicates the results and reranks them. Point it at a dense and a sparse index, rerank with the hosted
bge-reranker-v2-m3
model, and you have hybrid search without writing the query code.
Dense search matches on meaning, whatever words the user picks. Sparse search leans on the words themselves, so a query for "chocolatey" can match descriptions that say chocolate.
Query
Top results
"I want chocolatey snacks today!"
White chocolate raspberry truffles, dark chocolate peanut butter cookies
Something spicy and fried
Fried dill pickle chips, spicy dill pickle chips, a Cajun-spiced snack with paprika and cayenne, herb-crusted mozzarella sticks
"really crunchy" (from the app)
Wasabi peas, sriracha honey lime almonds
The Cajun-spiced snack is the interesting one. Paprika and cayenne are what make it spicy, and it still made the list.
The Streamlit app queries both indexes on every request. The MCP's job is to get those indexes ready and prove they work before the app touches them. (Hybrid search on document indexes works differently; see the
hybrid search guide
.)
Which index type should carry more of the load? Patel's view is to choose by the queries you expect rather than by speed. Natural-language questions ("how do I do this thing?") suit dense. Queries that depend on the user already knowing the vocabulary in the index suit sparse.
Search can't answer questions about data the index doesn't hold. Ask for "the top 3 snack choices of today" and the index has nothing to answer with, because search matches the query against descriptions and popularity isn't in them. Add metadata such as how many times each snack was bought, and the search can use it.
Next Steps
Back to those 30 records from the opening. With the MCP connected, whether they landed is one
describe-index-stats
call away. We'd keep the bulk loading in code you can read and re-run, and let the agent check it. Watch the
full replay
, then start with the
MCP server docs
or the plugin for
Claude Code
or
Cursor
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
