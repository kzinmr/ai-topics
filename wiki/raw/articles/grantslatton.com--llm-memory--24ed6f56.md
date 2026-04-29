---
title: "LLM Memory"
url: "https://grantslatton.com/llm-memory"
fetched_at: 2026-04-29T07:02:15.939832+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# LLM Memory

Source: https://grantslatton.com/llm-memory

LLM Memory
I've been thinking about LLM memory since GPT3 came out.
Back then, my LLM side project was story generation (i.e. fiction). Context windows for LLMs were tiny back then: 4K tokens, input + output. So just a few pages of text. How to write a novella if your entire knowledge of the text is only a few pages, as if you were an amnesiac author?
Suppose you're writing a scene. Where does the scene take place? Your description must match any previous description of the same place and be consistent with the setting at a whole.
Who's in the scene? What's the emotional state of the characters given recent events? What's some sample dialogue for those characters so you know their speaking style? What are their motivations?
You start to enumerate these things you need to know just to write the simplest scenes, and you pretty quickly blow your 4K token budget. This doesn't even get into the complexity of indexing and retrieving the relevant information.
How do you store a character's hair color? What if they dye their hair in the middle of the story? What if they have a flashback to when they were a blonde baby, but it darkened with age?
How do you represent that the character's new acquaintance can see their current hair color, but has no way of knowing they were a blonde baby?
The more you think about these questions, the more you can find edge cases where any particular memory system is limited.
This post contains a wandering train of thought through some of these systems.
Reference frames
All knowledge has an explicit or implicit reference frame for which it is valid.
This observation didn't come close to first in this region of thought, but I think it's among the most important, so I'm putting it first in this document.
You might think "Berlin is the capital of Germany" is a trivial piece of knowledge you could capture in a key-value store type repository.
capital(germany) = berlin
, or
country(berlin) = germany
.
But what about from 1945-1990? The capital of West Germany was Bonn. And before German unification, the question is nonsensical, though Berlin was the capital of Prussia.
But the capital of Germany is Flensburg in the sci-fi alternate history
Colonization
series. But only for some parts of the story, before Flensburg, it's still Berlin.
If you wrote a naive knowledge-ingestion pipeline, and I fed that sci-fi book to it, it would naively create a key-value entry for the capital of Germany being Flensburg. And another one for Berlin.
Temporal reference frames are the most common, i.e. facts associated with some span of time. Bonn is the capital of West Germany from 1945 to 1990. And then works of fiction essentially create alternate timelines.
The other huge on is spatial reference frames. Animal brains like ours are evolved to store knowledge spatially.
It's interesting that you don't have one global spatial reference frame. Like the floorplan of your house is a reference frame, but that reference frame is mostly disconnected from the reference frame of your neighborhood, and that one might be disconnected from the one of your city.
You can kind of view temporal reference frames a sort of 1D spatial reference frame.
You can also spatialize more abstract things, too. Imagine placing foods onto a 2D grid with saltiness on one axis and spiciness on the other axis.
So there is probably a memory system out there where everything is reference frames, meta-reference frames (where the embedded objects are themselves reference frames), etc.
This vein of thought is inspired by some of Jeff Hawkins'
Thousand Brains book
. The book is worth reading despite it being possible it's entirely wrong.
Vector embeddings
For the uninitiated, a vector embedding is basically where you take some text and convert it to an N-dimensional point, with the property that semantically similar pieces of text map to closer points in the N-dimensional vector space.
So if you were to compute the embedding for "I ate a sandwich" and find all the nearest neighbors to that vector in your database, you'd find other pieces of text about eating sandwiches, and then as you get a little further, you'll find stuff about eating in general, or perhaps sandwiches in general, and then even further you'll find sentences about doing things in the first person, etc.
In the GPT3 era, when I started playing with LLMs, I thought vector databases were all you need to build AGI. I changed my mind as soon as I actually tried it.
It's maybe possible with some extreme engineering, but I am pretty sure there are
much
better ways to do it.
An example of something vector embeddings struggle with is episodic memories. That is, you want to remember a chain of memories in series-order. How do you store the link between the memories in your vector DB? Is it another memory? What text do you embed to query it?
There's probably
some
way to do it, but it's a hell of a lot easier to just put an edge between two nodes in a knowledge graph.
Another major downside of vector embeddings is they are just hard to reason about. If two vectors are anomalously close or far, you don't really have much recourse or explanation. Adjust the training data of your embedding network and try again? Use a different distance metric than cosine similarity? Something else?
And we have just completely ignored the reference frame problem, and I have no idea how to bolt it on to vector DBs in a generalizable way.
Knowledge graphs
Knowledge graphs are a broad set of ideas, but the basic notion is you have memories that are somehow linked together, so "Berlin" is somehow connected to "Germany", and also to "List of world capitals", and also a million other things. Major European Cities. WW2. Cold war. Prussia. Brandenberg. Etc.
There are a bunch of possible implementation details.
Do edges have semantic value? e.g. is "Jerry Stiller" connected to "Ben Stiller" with a "father of" edge? And is there a reverse edge called "son of"?
Or are edges unlabeled, indirected, just vague connections?
The answers to these questions inform your design about how much goes in the nodes, too.
If you have highly semantic edges, your nodes can be tiny. e.g. "Boston" and "1630" nodes connected by a "was-founded-in-year" edge.
If you have unlabeled connections, this is no good, because "Boston" will be connected to tons of nodes that look like years. Instead, you really have to store whole documents that are useful individually.
You'd have a document (or many!) about the founding of Boston, those are connected to other documents about Boston's history, they might be connected to documents like "Everything interesting that happened in 1630" or a "Big American Cities" document. All of those documents are individually useful.
I tend to favor the document-based approach. I feel it's more
Bitter Lesson
-pilled. In the fullness of time, it won't be costly to deploy thousands of little cheap agents to crawl the unlabeled local graph looking for relevant information.
The document approach can also pair well with vector embeddings, since you can embed the documents (or embed questions the document answers, etc) and use those embeddings to jump to a bunch of candidate nodes to start the graph traversal from.
This isn't to say I hate semantic edges. Certain semantic edge feel very natural. Suppose you have two nodes that describe two events, and one event happened after another. It feels right to encode that "happened after" semantic information in the edge.
To recover that information without that semantic edge, the nodes would need to internally contain ordering information such as the timestamp the event in the node occurred, or the latter node needs to explicitly refer to the events of the former node.
In the case of AI systems, simply knowing the timestamp is probably always an option, but still feels wrong. Lots of human memories don't have timestamps but still have happens-before/after relationships for encoding episodic information.
An alternative is to have both nodes connected to some document that is like "Timeline of events at..." that has an ordered list, a brief description of each event, and a connection to the document describing each event. So if you have any event, you can traverse up to the meta-document, and trace that through the chronology, etc.
Meta-documents
Over time, I think the majority of the items in your knowledge graph actually become meta-documents instead of "source" documents.
Every time you run a query over the knowledge graph, you can store the results of that thing as a meta-document.
Like suppose someone asks me what my 5 favorite European cities are. I've never considered that question before. I query my memory and conjure a large amount of information about European cities. Once I've loaded all this, I weight cities against each other and produce my list.
I can now store that list, along with the reasoning process, as a new document! And connect it to the all those source documents.
Now if someone asks me "what are your 5 favorite cities in the world" I can just use this document as a partial cache — it at least covers me for any European results.
I've read that when you recall a memory, you actually recall the last time you recalled it (which can cause it to distort over time!). This process of producing and recalling meta-documents is kind of analogous.
Making connections
It's unclear to me if you want the connection-making process to be automatic, i.e. any documents you have in context when you produce a new document just automatically connect to the new document (and perhaps each other!), or you want something more explicit.
A more explicit strategy: after producing a new document, take every pair of documents in context and ask the model if they should probably be connected. Ask what future queries could be helped by having those documents connected. Are those queries likely? If so, make the connection.
Forgetting
You actually don't want unbounded growth in connections, because then your graph becomes a lot harder to navigate.
Since you will create spurious connections, because your connection-creator code won't be perfect, you need some way to garbage collect connections.
There's probably a bunch of clever techniques here, but I bet you can get pretty far by just reinforcing connections you travel the most, and letting others decay and be deleted. The risk of this is there might be a few connections that always
look
promising to follow but never are. They'll get pointlessly reinforced.
But don't humans do the same thing? There's stuff you just can't forget despite being useless?
A smarter strategy might be to employ the LLM itself to somehow judge connections as being poor, unused, etc and just surgically excise them. If the network is getting too dense in a place, just visit a node and all its neighbors and ask "which connection do you predict will be the least useful in the future" and delete that one.
If the graph is truly dense there, the deleted connection will just be one extra hop away through a sibling node, so the connection can always be remade if it turns out it was useful.
You can also imagine some forgetting logic based on spaced-repetition type engineering. That is, the probability of a connection being deleted has some refreshable decay property.
Episodic Memory
Presumably the primary means of sensory-input document creation is the authoring of "episodes". Just a narrative of what happens to the agent as it happens, with some kind of narrative start and stop points to the document.
Presumably, each document is connected to the episode before and after it, so you can traverse the leaf-level timeline of sensory input if needed.
But also, when the day is done, the model might do a process that looks remarkably like sleep and mull through the last day's episodes. It'll create a meta-document that is "everything that happened on 2025-05-17" with a summary of all the episodes, connected to all those episodes, and the meta-document from yesterday. It might go update the document "Everything that has happened in 2025 so far" if something particularly notable happened.
It might pull out some common themes from the last day's episodes and make meta-documents about synthesized learnings on just those specific topics. Then connect to past documents about related concepts.
It's worth noting that querying memory can itself be an episode. You could probably engineer this system where the vast majority (all?) documents are episodes.
For example, you don't have a document titled "List of European Cities I've Visited", instead, you have a document like "In May 2025, I was asked by Josh what European cities I've visited, and I compiled the following list". That is, the list is individually useful, but also embedded within an episode.
Traversal
As intelligence gets cheaper and context windows get larger, it makes sense to be really liberal with what you throw into context.
This strategy is dead simple but probably surprisingly good:
All the day's episodes are in context
The last 15 daily summaries
The last 15 weekly summaries
The last 15 monthly summaries
All the yearly summaries
Identify all nodes connected to any of those within 2 jumps that look promising
This would be super wasteful, so you can improve it by:
As you scan stuff, you don't need to put the full document into context. You really want to scan the document and
extract
relevant quotes and context from it.
You can make the node expansion more efficient with more of a priority queue type situation than a simple breadth-first search. Just maintain a numbered list and when you expand a node, ask the model to provide insert points for each node based on how promising it looks relative to what's in the queue.
The traversal agent
How to actually design the agent doing the traversal?
Consider a situation where you're looking for information about the query "Which famous European queen was murdered by her nephew?". Suppose you find a document about a queen who was murdered, but it doesn't say anything about the murderer.
Is this document important? Maybe! Maybe not. We need to traverse to adjacent documents now to learn more, see if anything mentions a nephew, etc.
It's probably possible to do this in a straightforward agentic approach. You give the model context on what it's looking for, and it has tools to load documents, take notes, un-load documents (clear up context), can see its own action log, and can return query results when ready.
You can imagine a more sophisticated system where query agents can themselves spin off sub-agents to answer sub-queries, e.g. "who was the nephew of Queen Whatever?". Each agent might be given a search budget that they can allocate to sub-agents (who themselves might delegate further!).
Databases
What about SQLite? A lot of memories would work great in an SQLite table. List of world capitals. The kings of England. German-Spanish bilingual dictionary.
I think it's simplest to just model these as external tool uses rather than part of the core memory system. Similar to humans! You store a memory "I have an SQLite table with all the world capitals" and upon retrieving that memory into context, the agent stops querying memory and goes to use that tool.
Scratchpads
For certain applications, all the memory and state you could need fits in the context window. The simplest possible memory system is just a single scratchpad of text that you append new memories to. When it fills up, you ask the model to select irrelevant stuff to delete or compact.
I think in the fullness of time, this will work for those applications. But today's models are mostly not smart enough to do it well yet. It's better to impose more structure on them.
For example, suppose the agent tried some course of action to accomplish the goal, but failed. That failure goes in the flat log. But later on, the log must be pruned for space. Some models will decide to prune the failure log, after all, what good is it?
But then they try the failed course of action again as soon as it's pruned. You can get really dumb, loopy behavior for non-trivial tasks with this system.
I think most humans would not do well if they had admin edit access to their own memories. Delete some childhood trauma? Whoops there goes a core part of your personality, now you're a different person.
Layers
It's tempting to represent all knowledge in one system, and I bet it
is
possible eventually, but from an engineering point of view, it seems to good to separate some of these.
Things core to identity, motivations, personality, temperament, etc feel fundamentally different than episodic memories. I feel like they should probably be represented differently, but at least separately.
Control
How much control should an agent have over
what
it remembers? Should memory be a
tool
the agent has control over? Or something that happens implicitly?
I kind of lean towards preferring implicit. Both because that's how memory feels like it works in my own mind, but also because the models aren't smart enough to have explicit control of it yet.
Models are prone to overestimating their own abilities. You ask them some historical fact, give them access to a memory tool, they are just as likely to conjure an answer from within the model weights as they are to make extensive use of the tool.
This is mostly fine for a sufficiently large model and sufficiently well-established historical facts, but totally insufficient for recent events that aren't in the training data.
Neural methods
Of course, all of the techniques in this post will probably
eventually
be subsumed by some fully-learned, end-to-end memory approach that is somehow just represented in vectors/weights.
I have no idea what this looks like. It might be some ultra-sparse mixture of experts where you can train new experts every night and plug them in the next day. Might be some recurrent thing. Who knows.
I don't have a lot to say here, so instead focus more on the things I have line-of-sight on.
Conclusion
There's no grand thesis statement to this post, it's just a ramble. Email me if you have any other memory techniques to add.
