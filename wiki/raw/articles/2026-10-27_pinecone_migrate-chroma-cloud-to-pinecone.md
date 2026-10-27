---
title: "How to Migrate from Chroma Cloud to Pinecone"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/migrate-chroma-cloud-to-pinecone/"
scraped: "2026-10-27T06:00:11.127346+00:00"
lastmod: "2026-10-26T16:18:46Z"
type: "sitemap"
---

# How to Migrate from Chroma Cloud to Pinecone

**Source**: [https://www.pinecone.io/blog/migrate-chroma-cloud-to-pinecone/](https://www.pinecone.io/blog/migrate-chroma-cloud-to-pinecone/)

←
Blog
How to Migrate from Chroma Cloud to Pinecone
Migrate a Chroma Cloud collection to a Pinecone serverless index
Aaron Kao
Oct 26, 2026
Product
Share:
Jump to section:
What This Guide Covers
Map Chroma Concepts to Pinecone
Migration Sequence
Re-Embed After Cutover
The $300 Pinecone Standard Trial
A Landing Spot for Chroma Cloud Users
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Chroma Cloud stops accepting writes on November 22, 2026 and stops serving reads on December 22, 2026. This guide moves a collection to Pinecone Database during a planned write pause.
Chroma is winding down Chroma Cloud, its hosted service.
Chroma’s notice
sets two dates:
November 22, 2026: writes stop.
Chroma Cloud becomes read-only. No creates, updates, or deletes.
December 22, 2026: reads stop.
Chroma Cloud no longer serves queries.
Chroma recommends that you start exporting and validating data before November 22 and finish exporting before December 22. Open-source Chroma is not affected and remains available under Apache 2.0.
If you want a managed service instead of running Chroma yourself, Pinecone Database is serverless and fully managed. There are no clusters to operate and no index to size or provision before you load. Read about the architecture
here
. Chroma Cloud users can start today with a 3-week Pinecone Standard trial that includes $300 in credits.
What This Guide Covers
The walkthrough moves
one
Chroma Cloud collection that already has dense embeddings, document text, and metadata into a Pinecone serverless index. It reuses your existing vectors and re-embeds nothing. It assumes a
planned write pause
: your app is read-only for the cutover window. To move several collections, repeat it for each one.
The steps run a toolkit of six Python scripts: preflight, create index, export, convert, load, and validate. Get it at
pinecone-field/chromacloud-migration
.
This toolkit is provided as-is, with
no guarantees
. It may not fit your collection, embedding setup, or cutover plan. Before you pause writes or flip production traffic, run the scripts yourself against your own data, review every finding, and confirm that validation matches what your app needs. You are responsible for verifying the migration works for your use case.
Run It With a Coding Agent
You can also hand the migration to a coding agent such as Claude Code, Cursor, or Codex. The toolkit includes an
Agent Skills
skill
that walks the agent through the same steps as this guide. Install it from the toolkit repo:
npx skills add pinecone-field/chromacloud-migration
Once it's installed, ask the agent to migrate your Chroma Cloud collection to Pinecone. It runs the six scripts in order.
Map Chroma Concepts to Pinecone
Below are some of the key concepts and terminology used in Chroma Cloud and their equivalents in Pinecone.
Chroma
Pinecone
Tenant / database
Organization / project
Collection
Index, or a namespace in a shared index when collections share dimension and metric
ids
_id
: 1 to 512 ASCII characters, no NUL. Other IDs get new ones
embeddings
A
dense_vector
field named
embedding
, declared in the index schema
documents
A
text
field on the document
metadatas
Top-level document fields, filterable automatically. Values are strings, numbers, booleans, or lists of strings
Distance
l2
(default) /
cosine
/
ip
Metric
euclidean
/
cosine
/
dotproduct
where
filter
filter
with
$eq
,
$ne
,
$gt
,
$gte
,
$lt
,
$lte
,
$in
,
$nin
,
$exists
,
$and
,
$or
,
$not
$contains
/
$not_contains
on an array key
{"$in": [value]}
/
{"$nin": [value]}
$contains
/
$not_contains
on a non-array key,
where_document
No equivalent. Redesign these queries
Some data changes on the way to Pinecone, such as remapped IDs, renamed metadata keys, and filters that need redesign. The
repo README
lists each one.
Migration Sequence
Here are 10 simple steps to migrate your Chroma Cloud collection over to Pinecone Database.
Step
What happens
Run
1
Rehearse and size the window
preflight.py
, then a full dry run
2
Create the index and ship the read/write switch
create_index.py
3
Pause writes. Reads stay on Chroma
Your app, then
preflight.py
4
Snapshot the count and export
export.py
5
Convert, then load into a fresh namespace
convert.py
,
load.py
6
Validate
validate.py
7
Decision gate
You
8
Flip reads and writes together
Your app
9
Monitor after cutover
You
10
Retire Chroma Cloud
Your app and accounts
Set up from the toolkit root with uv, which installs the pinned dependencies:
uv sync
export PINECONE_API_KEY=...                         # all Pinecone steps
export CHROMA_API_KEY=... CHROMA_TENANT=... CHROMA_DATABASE=...   # Chroma Cloud
The commands use a collection named
my_collection
, an index named
my-index
, and a namespace named
my-collection-v1
. Replace them with your own. Scripts that read Chroma call
chromadb.CloudClient()
, which reads the three
CHROMA_*
variables. To test against a local open-source Chroma copy, add
--chroma-path PATH
to those scripts.
Step 1: Rehearse
Preflight scans the collection page by page. It reports
collection.count()
, embedding dimension, distance space, the recorded embedding function, every metadata key with its value types and target Pinecone field name, None and empty documents, and IDs Pinecone would reject. Findings are labeled BLOCKING, TRANSFORM, WARNING, or INFO and saved to
preflight.json
.
uv run preflight.py --collection my_collection --workdir migration_work
uv run preflight.py --collection my_collection --workdir migration_work --allow-transforms   # after reviewing TRANSFORM findings
Review the findings from the first run. Blocking findings exit 1: all-zero vectors, mixed dimensions, metadata over 40 KB, unsupported types, and numeric or boolean arrays. Fix them in Chroma before the pause. Transforms (new IDs, renamed keys, dropped None values) also exit 1 until you accept them with
--allow-transforms
.
If preflight reports
metadata_over_40kb
because your document text is long, switch to the full-text-search variant in Step 2, or split the text in the source. Add
--array-policy stringify
only if preflight reports
non_string_arrays
and you accept string lists. To check the filters your app uses, add
--app-filters FILE
, a JSON list of
{"name", "where"}
or
{"name", "where_document"}
objects. Pass the same policy flags to
convert.py
in Step 5.
Then rehearse Steps 2 through 6 on a copy or a small collection, and time the export and load. Use that time to size your write-pause window. We don’t quote durations, because your rehearsal is the only reliable estimate.
Step 2: Create the Index and Ship the Switch
uv run create_index.py --index my-index --workdir migration_work
The script reads dimension and metric from
preflight.json
and creates a document index with one
dense_vector
field, in AWS us-east-1 by default. On Standard,
--cloud
and
--region
choose another location.
--deletion-protection enabled
guards the index against deletion. If the index exists, the script only verifies its schema and exits 1 on a mismatch.
Full-text-search variant.
If your documents exceed about 40 KB, run these commands
instead of
the matching preflight, create_index, and convert commands. Run one path, not both:
uv run preflight.py   --collection my_collection --workdir migration_work --text-mode fts --allow-transforms
uv run create_index.py --index my-index --workdir migration_work --full-text-search
uv run convert.py     --workdir migration_work --text-mode fts
In the same step, ship the app change that performs the cutover: one config flag that switches reads
and
writes between Chroma and Pinecone. You write this code, and it stays pointed at Chroma for now. On the Pinecone side, open the index with
pc.index(name=...)
, write with
index.documents.upsert
, and search with
index.documents.search
. Use the target field names from
preflight.json
, and handle remapped IDs (Step 5).
Step 3: Pause Writes
Set your app to read-only. Reads stay on Chroma. Then rerun preflight with the same flags:
uv run preflight.py --collection my_collection --workdir migration_work --allow-transforms
# Add any policy flags you used in Step 1 (for example --array-policy stringify).
# Full-text-search path: add --text-mode fts.
Step 4: Export
uv run export.py    --collection my_collection --workdir migration_work
The script records
collection.count()
, then streams
collection.get
pages to
export.jsonl
, holding only the set of IDs in memory. It exits 0 only if unique exported IDs equal the count, no ID repeats, and the count did not change during the export. Exit 1 usually means writes are not paused. Because this check compares counts, it can’t detect an update that leaves the count unchanged. Only the write pause protects against those, so enforce it in the app. Keep
export.jsonl
as your archive copy.
Step 5: Convert and Load
uv run convert.py   --workdir migration_work
Add the same policy flags you gave preflight. Convert streams the export twice and writes:
documents.jsonl
: one Pinecone document per line.
field_map.json
: every metadata key and its Pinecone field. Keys that start with
_
or
$
, exceed 64 bytes, or equal a reserved field (
embedding
,
text
,
chroma_id
) become
meta_<key>
. If that name is taken or too long, it is truncated and gets a hash suffix, so keys over 64 bytes always take the hashed form. In our testing,
text
,
_text
, and an existing
meta_text
became
meta_text_982d9e3e
,
meta_text_f47a3f59
, and
meta_text
. The table is deterministic, records each reason, and can be reversed.
id_map.jsonl
: IDs Pinecone rejects become
chroma-sha256-<sha256 of the ID>
, with a
-2
suffix if that string is taken. Each remapped document also stores its original ID in
chroma_id
.
transforms.jsonl
: one line for every per-record change or drop. Nothing is dropped silently.
If any record fails, convert writes no
documents.jsonl
. Then load:
uv run load.py      --index my-index --namespace my-collection-v1 --workdir migration_work
The loader streams
documents.jsonl
with
index.documents.upsert
, one batch in memory at a time. It sends a batch before it would exceed 1,000 documents or 1,900,000 bytes, under the 2 MB request limit, and retries rate-limit, 5xx, connection, and timeout errors with backoff. The namespace must be new or empty. A rerun into the same namespace is allowed only when
load_state.json
shows the same index, namespace, and
documents.jsonl
checksum. Upserts overwrite by
_id
, so a rerun leaves the same content.
Step 6: Validate
Golden queries compare top-k results between Chroma and Pinecone. Build them with the same embedding call your app uses for Chroma queries. Your app’s embedding call is the integration point: replace
my_app_embed
with your own function. The toolkit does not embed text.
import json
queries = ["how do refunds work", "reset my password"]          # real user queries
with open("golden.jsonl", "w") as f:
    for i, q in enumerate(queries):
        emb = my_app_embed(q)   # INTEGRATION POINT: your app's query-embedding function
        f.write(json.dumps({"query_id": f"q{i}", "embedding": list(map(float, emb))}) + "\n")
Then run the validator. Add
--app-filters app_filters.json
to compare your app’s
where
filters.
uv run validate.py  --collection my_collection --index my-index --namespace my-collection-v1 \
                    --workdir migration_work --golden-queries golden.jsonl
Check
Passes when
source_unchanged
collection.count()
still equals the exported count
metric_and_dimension
Chroma's live space and dimension match the index schema
namespace_count
The namespace record count reaches the exported count (polled up to 600 s)
id_set
Source IDs, mapped through
id_map.jsonl
, equal every ID from
index.documents.list(namespace=...)
sample_fields
200 random documents, plus up to 200 records with per-record transforms, match the source field by field and round-trip to the Chroma record. A key rename alone is not a per-record transform, so random sampling covers those records
search_visible
Probe searches return
top_k
results (polled up to 180 s)
golden_queries
Tie-adjusted top-k overlap with Chroma's
collection.query
averages at least 0.9, with no query below 0.6
app_filters
With
--app-filters
, each translated filter returns the same ID set as Chroma's
where
The overlap thresholds are heuristics. Tune them with
--min-mean-overlap
and
--min-query-overlap
.
--golden-from-sample N
uses perturbed stored vectors and is for tests only.
The validator also checks self-retrieval: each sampled vector should find its own record. This check is a diagnostic and never fails the run. Misses point to duplicate vectors,
dotproduct
with unnormalized vectors, near ties, approximate search, or freshness.
If a data check fails: stop, fix, and reload into a fresh namespace
(for example,
my-collection-v2
), then validate again. Don’t patch gaps with an upsert-only pass for missing IDs, because upserts can’t remove records that were deleted in Chroma. If only
app_filters
fails, your data is fine. Fix the app’s filter instead of reloading.
Step 7: Decision Gate
Decide whether to flip. Rolling back is still free: your app has written nothing to Pinecone. If you aren’t confident, resume writes on Chroma and schedule another window.
Step 8: Flip Reads and Writes Together
Flip the config flag, then resume writes. Moving reads and writes at once means no write lands in a store your reads can’t see.
Step 9: Monitor
Watch errors, latency, and result quality. From here, rolling back means replaying Pinecone writes into Chroma, and Chroma Cloud accepts no writes after November 22.
If you reach November 22 first:
Chroma enforces the write pause for you. Steps 4 through 8 still work until December 22, but your app’s writes fail until you flip.
Step 10: Retire Chroma Cloud
Once validation passes and monitoring shows no issues, finish before December 22:
Remove Chroma client code from your app and jobs, and confirm nothing calls Chroma Cloud endpoints.
Rotate or delete your Chroma Cloud credentials.
Archive
export.jsonl
with
field_map.json
,
id_map.jsonl
, and
transforms.jsonl
. You need all four files to reverse renames and ID mappings.
Re-Embed After Cutover
This guide keeps your current embedding model. Once you’re on Pinecone, you can move to
integrated embedding
, where a Pinecone-hosted model such as
llama-text-embed-v2
or
multilingual-e5-large
embeds text at upsert and query time. Integrated embedding removes the client-side embedding step. The switch needs a new index whose schema declares a text field with an
embed
block, and a reload from your stored text. Results will change, so evaluate them for relevance rather than identical IDs.
The $300 Pinecone Standard Trial
The Standard trial gives you 3 weeks and $300 in credits, with no up-front payment. It ends after 21 days or when you use the $300, whichever comes first. A trial started in October ends before November 22, so choose your plan before you cut over.
The trial includes Standard features:
Import from object storage
for bulk loads (the toolkit doesn’t use it)
Backup and restore
Role-based access control (RBAC)
Choice of cloud and region
Higher limits and Developer Support
When the trial ends, add a payment method to stay on Standard ($50/month minimum usage, then pay as you go), upgrade to Enterprise, or downgrade to the free Starter plan.
See the
trial terms
and
pricing
.
A Landing Spot for Chroma Cloud Users
Chroma Cloud is coming to an end on December 22. We want to provide a place for all Chroma Cloud users to land if they want a fully managed service experience. Start your Standard trial today and get $300 in credits, migrate to Pinecone Database, and try out
integrated embedding
or
full-text search
on a new index when you’re ready.
Start your Standard trial
Get 3 weeks and $300 in credits on Pinecone Standard — then migrate with the Chroma Cloud toolkit.
Start your Standard trial
View pricing
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
