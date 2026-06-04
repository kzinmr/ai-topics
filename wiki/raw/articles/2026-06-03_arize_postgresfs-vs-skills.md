# Faking a Filesystem For your Agent: PostgresFS

**Source:** X Article (id: 2062229784009256960), bookmarked 2026-06-03
**Authors:** Arize team, co-written by @SufjanFana
**Original URL:** https://x.com/i/article/2062229784009256960
**Content extracted from:** X Article plain_text (full content via xurl bookmark fetch)

---

Working with agent harnesses, it is hard not to be impressed by the power that Bash and filesystems lend to the modern agent. Bash and file operations sit at the core of the tool-calling workflows harnesses use every day. The strength of that foundation has even led some people to say, "Bash might be all you need."

But that raises a deeper question: how far should we push this abstraction? Why does Bash work so well for agents, and where are the edges?

Mintlify recently introduced an approach called ChromaFS, which gives their database a filesystem-like interface. Their write-up was thoughtful and sparked a serious debate. Should every database expose a filesystem-style interface for agents?

## The pattern teams are copying

Mintlify built ChromaFs to make their docs assistant smarter. Plain vector RAG could only return chunks that matched a query embedding; if the answer spanned several pages, or needed exact syntax that never landed in the top-K, the agent was stuck. So they wrapped their Chroma vector store in a filesystem-shaped interface: the agent runs ls, cat, grep, and underneath every command is a database read. They published it as a pattern other teams could copy. The same "wrap the database as a filesystem" move is now showing up on SQL databases that never needed it.

Your agent has the same shape of problem: it needs to work with data in a database. The premise behind the pattern is that agents are fluent at what their training data has seen, so you should hand them a familiar surface. Whether a familiar surface is enough, or whether what matters is where the data actually lives, is what Arize set out to test.

## Hypothesis

Selectively letting an agent pull only the data it needs from a database (via a skill), then giving it the full local Bash toolset, should beat the complexity of building a Bash-like interface into the database itself.

The reason is practical: many shell and pipe workflows only exist in full form locally. The local toolbox is broader than what you can realistically re-create behind a database abstraction. Databases still excel at one thing here: searching and filtering across TB-scale data. But for iterative, branch-heavy analysis loops, local tooling is usually the better execution surface.

So the pattern is a deliberate handoff. The agent uses the database for broad retrieval, materializes a slice locally, runs deeper analysis, and pulls another slice if needed. That gives you a clean tradeoff between large-scale search and complex local reasoning.

As a stand-in for ChromaFS, they used **PostgresFS**. It works over Postgres in the same style: data stays behind the abstraction, and commands like cat, grep, or find are translated into database queries.

**Speed** comes from locality: once the data is local, bash runs over it without another database round-trip, while PostgresFS pays one on every read. **Composability** is that same locality seen again: anything that needs a second pass over the data (staging an intermediate result, using two-input operators like comm or join) needs a writable, re-readable local home that a read-only abstraction can't give it.

## PostgresFS or a skill

Both approaches were built and tested against live Arize AX docs ported into Postgres:

**PostgresFS, the filesystem abstraction** — The five ChromaFs verbs (ls, cat, grep, find, cd) over virtual paths that resolve to Postgres reads, plus the standard coreutils filters (sort, uniq, wc, awk, sed, cut, tr, head, tail, comm). The agent explores the docs like a codebase. Wired with an in-process shell (just-bash) registered as the agent's Bash tool. Read-only: the five verbs become SELECTs, the filters run locally over whatever bytes came back.

**The skill, the SQL workflow** — No abstraction. The agent gets the host's real bash shell plus a small script that takes one SQL query and writes the result to a local file. The workflow it learns: write a query, run it, compose the answer against the file with real grep / jq / sort / pipes. The agent does the translation; the runtime just moves bytes.

Those are the same job done two ways: PostgresFS sends every read back to Postgres, while the skill makes one trip to the database and does everything else locally.

Each agent also gets an orientation prompt. PostgresFS's prompt hands it a decision table mapping question shapes to shell idioms and tells it to keep the number of doc reads down. The skill's prompt teaches a discipline: compute the answer in SQL and return it inline when it reduces to a small set (COUNT, GROUP BY, INTERSECT), otherwise project every candidate row to a file and compose locally — and don't treat the query script as a search tool, because a flurry of narrowing queries means you projected too little.

## How they tested

Both arms run inside the Claude Agent SDK: the production agent loop, identical on each side except for the architecture under test. The agent is claude-sonnet-4-6, the judge is claude-opus-4-7, and the database is a frozen snapshot of the Arize docs. They ran each approach 10 times on each of 10 questions and reported the median. To compare only the part that's actually architectural, they timed the agent's investigation loop: from the prompt to its last tool call.

The ten questions span three tiers: simple (one or a few reads), mid (aggregation over many pages), and complex (extraction or synthesis whose answer depends on how many separate reads the agent must gather — locality pressure).

## Results

On paper, close enough to call even: neither clears 2x on latency, and accuracy splits **93 to 99**. That thin margin is the hypothesis showing through — one quiet property, reading from a local file versus round-tripping every read, never blows out a benchmark; it bills you narrowly in accuracy and heavily in code instead.

Comparing the investigation loop across the ten questions, it's nearly an even split: PostgresFS takes three (q2, q5, q6) on in-process dispatch, the skill takes three (q8, q9, q10) where reads pile up, and four are ties. The real driver is read count; tier is just a proxy for it.

**Accuracy**: Overall: PostgresFS 93/100, the skill 99/100. Both ends are tied at 100%. The whole gap is two mid-tier questions, both on PostgresFS: q7 (synthesis) at 6/10 and q4 (counting) at 7/10. Every other question is 9/10 or 10/10 on both.

## Why PostgresFS lost

The losses aren't about missing operators: they handed PostgresFS every filter, and they work. The split is inside PostgresFS, on the read path:

- **The filters are local.** sort, uniq, awk and friends are pure stream transforms over bytes already in the pipe: in-process, no database, no round-trip.
- **The reads are faked.** ls, cat, grep, find resolve through an adapter that turns each into a Postgres SELECT. Two costs fall out of that.

**Locality collapse.** Every doc read is a database round-trip dressed as a shell verb. Each one pays for query parsing, serialization, and transfer, even when Postgres serves it warm from cache. A grep -rl followed by a burst of cats, near-instant on a real filesystem, becomes a sequence of round-trips. The skill pays that round-trip once: a single query lands the result on a local file, and everything after is local and composable, with no more database hops.

**Composability, capped at one pass.** Single-pass pipelines work on both. But anything needing a second pass over the data doesn't: just-bash has no process substitution <(...) and the adapter is read-only (no /tmp, every write is EROFS), so nothing can be staged and reused. The two-input family (comm, join, diff, paste) is dead even though comm sits in the allowlist. The skill materializes once and reuses freely, while PostgresFS pays a fresh round-trip for every look at the data.

The natural objection is "then just add to the abstraction until it's as good." This is a trap. Every step toward a faithful read path (a better prefetch, closer grep semantics, a real cache) is a step toward real files on a real filesystem, which is the skill, reached less cleanly than just running SQL over the host's own shell. And the code you'd write to get there is the same code that round-trips every read in the first place: the maintenance cost and the performance cost are the same cost.

## Takeaways

**With performance a tie, the cost that's left is maintenance.** What settles it is what you own: PostgresFS is a large custom layer: an adapter, a coarse-filter, a cache, a regex translator. You have to keep that layer correct as the schema moves, while the skill is a prompt and a small script.

**Reach for the real store before the pretty shape.** "What does the host shell actually read from?" beats "what shape would I like to expose?" A familiar interface is necessary, not sufficient.

**This generalizes past SQL.** "Wrap the store as a filesystem" vs. "give the model the store's real query language plus a real shell" is the same decision for Chroma, Mongo, BigQuery, ClickHouse, or whatever's next. The query language is incidental. What's constant is the trap: every time you fake a filesystem, you sign up to maintain one, and the closer you push it to behave like the real thing, the more you've just rebuilt the real thing, slower.

## References

- Arize: https://arize.com
- Mintlify ChromaFS: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant
- Vercel Bash tool: https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval
