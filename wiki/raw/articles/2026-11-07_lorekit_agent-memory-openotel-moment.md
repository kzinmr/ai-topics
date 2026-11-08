---
title: "Agent memory needs its OpenTelemetry moment (LoreKit)"
type: article
created: 2026-11-08
updated: 2026-11-08
source: https://www.lorekit.io/blog/open-agent-memory-format
published: 2026-11-07
tags: [agent-memory, agent-observability, memory-systems, interoperability]
sha256: 36514a454b7731b10b4994652f54822b7a037a512ea325bb7d6a6c59eb5a17fb
---

Agent memory needs its OpenTelemetry moment — LoreKit blog LoreKit blog Docs ⌘K Sign in All posts Agent memory needs its OpenTelemetry moment Every agent tool stores memory in its own shape, and every week someone builds another one. None of them can read the others. Observability had the same problem until OpenTelemetry gave everyone one data model to share. A tour of today's memory formats, the proposals that already exist, and what a shared spec could look like. Mads Thines · November 7, 2026 · 7 min read On this page Count the memory formats on your machine We've seen this before A tour of the shapes The proposals that already exist What a shared spec could look like What a skeptic would say Open questions Count the memory formats on your machine 
 List every place your coding tools keep something they "remember". A typical setup today: 

 an AGENTS.md or CLAUDE.md in most repos, and .cursor/rules/*.mdc in a few 
 an agent writing files to a /memories directory through Anthropic's memory tool 
 Copilot keeping facts about each repo on GitHub's side 
 a memory MCP server keeping a JSONL knowledge graph 

 That's four different shapes, and none of them can read the others . A lesson your CI agent learns stays in whatever wrote it. Your editor agent can't read it, and neither can the next tool you try. 
 Each format is reasonable on its own. Together, they rebuild the same small idea again and again: a note an agent left for its future self, stored at some address, true for a while. 
 And the list keeps growing. Browse r/ClaudeAI, r/LocalLLaMA or r/cursor and you'll find a steady stream of "I built a memory layer for my agent" posts, each with its own storage, its own schema and its own MCP tools. That's good evidence the problem is real: people keep hitting it badly enough to build something. But every new solution adds one more format that nothing else can read. The problem isn't a missing tool. It's a missing agreement , and that only comes from the community working on it together. 
 I build one of these tools, LoreKit, which is open source. This isn't a pitch that LoreKit has solved memory. Its format is one proposal among several, with gaps of its own. The point is that this is the moment to agree on a shared shape , and that another field has already shown how. 
 We've seen this before 
 Before 2019, every observability vendor shipped its own agent, its own instrumentation library and its own data format. Switching vendors meant instrumenting your code again. Two open projects, OpenTracing and OpenCensus, tried to fix that and competed with each other too. 
 In 2019 they merged into OpenTelemetry . What mattered was what the vendors agreed to stop competing on: 

 A data model : what a span, a metric and a log record are. 
 Semantic conventions : shared names like service.name and http.* . 
 A protocol : OTLP, one way to send the data. 
 Reference implementations : shared SDKs and the Collector. 

 Vendors kept competing on what they do with the data: storage, querying, analysis. Users instrument once. I work with OpenTelemetry every day at Dash0 , and that agreement is why a whole ecosystem of tools can read each other's data. 
 The same four layers. Observability agreed on them and competes on what happens after the data arrives. Agent memory has plenty of implementations, but nothing agreed underneath them. 
 Agent memory is where observability was before 2019. The timing is good: the formats are young enough to change, and there's already a neutral home for agent standards. MCP and AGENTS.md both sit under the Linux Foundation's Agentic AI Foundation. 
 A tour of the shapes 
 These change quickly, so treat the details as a snapshot from late 2026. 
 Family Example The unit of memory Addressed by Forgetting Instruction files AGENTS.md , CLAUDE.md , Cursor .mdc rules A whole Markdown file File path (plus globs for Cursor) Never. A person edits it Agent-managed files Anthropic's memory tool A file under /memories A path the model picks Never, unless the model deletes it Hosted repo facts GitHub Copilot Memory A fact with code citations One repository Deleted after 28 days unused Context blocks Letta core memory A labeled block with a character limit A label on an agent Never. Always in context Extracted facts Mem0 A fact the service extracts from messages user_id / agent_id / run_id / app_id Optional expiration date Namespaced store LangGraph BaseStore A JSON value dict A namespace tuple + key Optional TTL, reset when the item is read (by default) Knowledge graph MCP reference memory server Entities, relations, observations Entity name Never Temporal graph Graphiti / Zep A fact on a graph edge Entities + edge Facts are invalidated rather than deleted, on two timelines Addressed record LoreKit A record with a scope, key and lifecycle A scope string + key Never, unless a TTL is set 
 A few of them got something right that a shared spec should keep. Copilot Memory pairs citations you can check against the code with forgetting by default, though it's locked inside one product. LangGraph shows how small the core can be: put(namespace, key, value) . Graphiti models time properly, with separate timelines for when a fact was true and when it was recorded. And AGENTS.md shows that a plain file at a known path can become a standard. 
 The proposals that already exist 
 Several people have started on this. MacPaw Research's Portable Memory is a .mem bundle with byte-reproducible serialization, deletion tombstones and optional signing; its authors say it isn't widely adopted yet. The Open Memory Protocol is an April 2026 draft for moving conversations and the memories derived from them between platforms as a ZIP with a manifest. Cognee's COGX format imports from Mem0, Letta and Zep. 
 These mostly solve export : moving one person's memory from vendor A to vendor B. Coding tools also have a second, open problem: live addressing . When a CI job, an editor agent and a review bot work in the same repo at once, how do they read and write the same place and agree on what it means? A complete spec needs both. 
 Export moves one owner's memory between vendors. Live addressing lets many tools share one place at the same time. The existing proposals focus on the first. A shared address could sit inside their records to cover the second. 
 What a shared spec could look like 
 Strip away the branding and every format answers the same four questions differently: where a memory is true, what its identity is (does a second write update it or duplicate it?), what it says , and when it stops being true . Nobody disagrees that those matter. The tools only disagree on the answers, which is where OpenTelemetry started too. 
 There's one real fork: who writes the memory . In instruction files it's a person. In the memory tool, Letta and LoreKit, it's the model. In Mem0 and Graphiti, a service extracts facts from the conversation. A spec doesn't need to pick one. It needs to record which, so a reader knows how much to trust what it reads. 
 Here's roughly what one record could look like as a file. It illustrates the data model; the field names aren't a proposal: 
 --- 
 spec : agent-memory/0.1 
 id : 8f0c2a6e-4b1d-4c7a-9e2f-3a5b6c7d8e9f 
 address : { level : repo , value : github.com/acme/checkout } 
 key : tests-need-local-postgres 
 kind : lesson 
 written_by : { type : agent , name : claude-code } 
 content_type : text/markdown 
 lifecycle : { expires_at : null , extended_by : write } 
 attributes : { vcs.pr : 482 , ci.run_url : "https://ci.example/runs/123" } 
 --- 
 Integration tests fail with `ECONNREFUSED 127.0.0.1:5432` unless Postgres 
 is already running. Start it before `pnpm test` : 

 docker compose up -d db 

 The test setup does not start it for you. 
 The frontmatter is the envelope: address and key say where it's true, id is its identity, lifecycle says when it stops, and written_by answers the fork. The Markdown below it is the memory itself, and content_type tells a reader how to treat it. Anything else a tool needs goes in attributes , under a namespace other tools can ignore. The same record serialises to JSON just as well, for a tool that wants to send it over the wire. 
 Around that record, a spec would mirror OpenTelemetry's layers: 

 Conventions : shared names for address levels ( global , project , repo , branch , and whatever monorepos need), for kinds, and for attribute namespaces ( vcs.* , ci.* , agent.* ), in one versioned registry. 
 A contract : a few operations (write, read, list, search, archive) with fixed inputs and outputs, exposed over MCP. Many memory servers now offer an MCP interface, but each exposes different tools with different meanings. 
 Conformance tests in place of a reference implementation: round-trip a record and check nothing was lost, check that unknown attributes survive a rewrite, check that expiry behaves as stated. 

 What stays out matters as much: storage, ranking, embeddings, the user interface. That's where tools should compete. And the spec should live somewhere neutral, not in LoreKit's repo or any single vendor's. 
 What a skeptic would say 
 "You build a memory tool, so of course you want a standard shaped like it." Fair. It's why LoreKit is one row in the table rather than the template. If a shared spec looks different, LoreKit should adopt it anyway. 
 "MCP already is the standard." MCP standardises the call , not the record . OpenTelemetry needed a protocol and a data model. Memory needs both too. 
 "Shared memory is a prompt-injection channel." Yes. Anything an agent reads can steer it, and shared memory widens who gets to write it. A spec should make that visible: record who wrote each memory, allow signatures (Portable Memory already does), and let a record point at the code it depends on so a reader can check whether that code changed. No format makes poisoning impossible. 
 "Another standard won't fix fragmentation." That's xkcd 927 , and it's the strongest objection. My answer is OpenTelemetry's: agreement came when existing projects merged , not when someone added another one. The work here is the same: take what the existing proposals and tools each got right, and agree on the parts they share. 
 Open questions 
 I don't know the answers to these, and I'd rather work them out in public: 

 Which address levels? Monorepos want a level between repo and branch . Should levels be a fixed list or conventions? 
 Should forgetting be the default? Copilot forgets by default, LoreKit doesn't, and LangGraph extends life on read. 
 Should a record point at the code it depends on? It's the best protection against stale memory, but it ties a record to a code host. 
 Who should coordinate? A working group, a foundation, or a draft spec people send changes to? 

 If you build any of the tools in the table, or wrote one of the proposals, I'd like to compare notes. LoreKit's schema and on-disk format are MIT-licensed as one concrete input. To see real records, LoreKit's offline store writes plain Markdown files you can open, grep and diff: 
 npx @lorekit/cli install 
 Compare them with what your other tools write, and tell me what a shared format would need that none of them have yet. Enjoyed this? Show some love. Give your coding agent a memory One command, a folder you own, no signup. Start local today. $ npx @lorekit/cli install Copy Sharing with a team? Create a free account Read the docs Star on GitHub On this page Count the memory formats on your machine We've seen this before A tour of the shapes The proposals that already exist What a shared spec could look like What a skeptic would say Open questions GitHub · Discord · Docs · Blog · API docs · Need help? Join our Discord for support.

## HN discussion highlights (item 50411467, 59pts)

[te_chris] So we need another complicated format to store information so that the machines which read unstructured text can work with it?

[slopinthebag] at this point i'm pretty convinced agent memory is strictly harmful. it remembers the wrong things, and then turns them into an inane focus for each task. i disable it universally on every harness. if i want memory, i specifically instruct the agent to record findings into a file.

[SwellJoe] Same. Everybody builds one, and then eventually realizes it makes the model stupid and confused. The right solution is pretty much always developer documentation in the repo, in roughly the same shape you'd make developer docs for humans that you want to be able to get up to speed about your codebase really quickly. This has the benefit of being something you can easily read over every now and then to make sure the model hasn't baked in some random comment you made about a specific circumstance 

[nonethewiser] I strongly agree. This is becoming a general principle along the lines of “code comments that describe what the code does are bad.” Memory just ensures there is a fairly high level of drift and inaccuracy in your context. Unless YOU are manually curating it. Its similar to wiki systems where your agent produces tons of documentation and decision records, etc. Its a bunch of assertions about your codebase that you aren’t vetting and which is at most 90% correct. Thats good enough for a feature or

[nonethewiser] Also introduces massive confirmation bias. Majorly gimps the model. I remember I was exploring hexagonal architecture on chatgpt and then future conversations with open ended architecture questions just gave me those same patterns. “Oh damn look its recommending something that looks like hexagonal architecture. I guess hexagonal is a really good - hey wait a second …”

[Kwpolska] Agreed. Claude Code often tries to write one-off decisions and transient problems into memory. And when such things appear in the context, Claude will start doing questionable actions, because it saw something unrelated and wrong somewhere in its context

[imgyuri] The need for a unified format or spec is greatly reduced in the case of Agent memory because by definition it is read by agents, and agents are already instructed / programmed to read memory files of different formats. Even if such instructions did not exist, agents are extremely good at traversing files to get the necessary context it needs.

[jstanley] This is true and it probably is actually fine, but in a way you don't want it to be wasting its reasoning abilities and context window on figuring out which text files to read. It would be like trying to accomplish something as a human but all your reference material is always in a different format, it would be maddening.

[troupo] > Agent memory because by definition it is read by agents, and agents are already instructed / programmed to read memory files of different formats. Only it's not read by agents, and largely ignored. From Anthropic's recent self-congratulatory article: ---start quote --- Injected memories use up valuable tokens, and an incorrect note can be carried into every session. Loading a note also doesn’t guarantee that Claude acts on it: our documentation on Claude Code warns that longer instruction file

[Fordec] On the general premise, I agree. But I don't think that moment is today, not yet anyway. I don't think we understand the right way to approach context and memory yet or how long they should last for, never mind standardizing on an abstraction prematurely that ends up being like SOAP or SGML.

[andai] What's better than SGML? What would XML an HTML look like if they were based on that instead?

[dizhn] Fully agree. Any solution people think they have today is working on assumptions that are probably not correct. And things are still moving very fast.

[Implicated] I decided long ago to not wait for you all to figure this out. Index it all. Embed it all. Give your agents the ability to query it all. Eval different configurations to figure out what works best for you.

[hagen8] Well, coding agents are smart, they can use all kinds of memory. A simple skill on how and when to access it is enough...
