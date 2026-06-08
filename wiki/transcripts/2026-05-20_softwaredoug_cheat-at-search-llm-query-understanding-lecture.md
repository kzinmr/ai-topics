---
title: "Cheat at Search — LLM Query Understanding (Lecture Transcript)"
author: Doug Turnbull (SoftwareDoug)
date: 2026-05-20
date_ingested: 2026-06-03
source: https://docs.google.com/presentation/d/1sAmb4NoDOFWXM3WiQGmgbU4e0X5Za6gAMbv1coYLYuw/edit
type: transcript
tags:
  - query-understanding
  - search
  - model
  - model
  - bm25
  - transcript
related_article: articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search.md
participants:
  - Doug Turnbull (instructor)
  - Prasad Seemakurthi
  - Joel Turner
  - Shreesha Jagadeesh
  - Gordon
  - Joey
  - Asim
  - Zenit
---

# Cheat at Search — LLM Query Understanding (Lecture Transcript)

**Author:** Doug Turnbull (SoftwareDoug / softwaredoug.com)
**Context:** Guest lecture for Turnbull & Trey Grainger's AI-powered search class, May 2026
**Companion slides:** [[articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search|LLM Query Understanding — Cheat at Search (Slides)]]
**Companion course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)

---

## What is Query Understanding?

**[00:09:25]** I really mean taking queries apart into their metadata.

So, we have queries. Crimson Suede Couch, Purple Ashley Recliner, desk for kids, and we have products. And these products have properties, category, color, brand, blah blah blah. And this… not… not only e-commerce, but it comes up a lot in e-commerce. E-commerce search can be in some ways more about structured… did you give me the thing with the right attributes? Rather than just, say, like, question answering or passage similarity, like, ranking most similar to least similar.

So, we tend to think in these attribute ways of thinking about almost like a structured SQL table.

### Managed Vocabularies

**[00:10:21]** Often our vocabulary, when we do a query understanding, is controlled in some way, like, we have a bunch of… maybe we may have a legal set of colors, or a legal category tree. We call that a **managed vocabulary**.

Oftentimes, it's flat, so here we have a flat color set of attributes. Other times, it might be hierarchical, like this category. You see, like, it has some hierarchy in it.

Many times there are some cases where there's, like, 7 things we're classifying into, like, maybe 7 primary colors is all we care about. Other cases, we may have messier data, like a brand. If you've worked in e-commerce search, you may, you know, one product says Ashley, another says Ashley Furniture Unlimited, or something. And that can be annoying, right, when there's variations.

### Content Understanding = Query Understanding

**[00:11:13]** And what you'll hear a lot of query understanding people talk about, and if you take the AI-powered search course with me and Trey, where we talk about query understanding even more. **Content understanding really is query understanding.** Because, if you can understand your content really well, then it gets a lot easier to map queries into…

Crimson Suede Couch obviously means, like, oh, crimson means red, because we have a set of colors, and we trust that our content's gonna be categorized correctly, and now we just need to map all of the ways that users talk about colors into that vocabulary. That'd be a classic, old-school way of doing query understanding.

And really, what we're going to talk about today, we're not necessarily going to talk about the enriching of the content itself. Although that is an interesting topic. We're gonna be talking explicitly about taking queries and mapping it to an existing vocabulary on the content.

### Mapping Queries → Attributes → Actions

**[00:12:14]** So, we have Crimson Sway Couch. We do query understanding, we use our some vocabulary, and we map this to a legal color in our color vocabulary, right? That's kind of what we're talking about.

And we would take red, and we would decide what to do with it. So now we decide we might filter. So that only red things show up?

**[00:12:50]** We could also boost, so maybe if our colors are actually a bit more sophisticated? We may decide to filter to this color.

**[Prasad Seemakurthi, 00:13:14]** My question was, like, what is legal here? Is it, like, an approved list, or…

**[Doug Turnbull, 00:13:20]** Yeah, so it would be managed by somebody, so teams often have explicit taxonomies that they're controlling or managing for this kind of thing.

### Filtering vs. Boosting

**[00:13:41]** Yeah, so we're gonna decide whether we filter or boost this attribute.

**[00:13:48]** So the reason I say filtering is obvious, like, we always talk about metadata filtering. And metadata filtering is a kind of thing where, we might have… this comes up in vector databases, but basically we have some original set of search results that are ranked by a retrieval function, whether it's vector search or keyword ranking, like BM25. And we just decide, oh, we're only going to include the things that are color. You often see the syntax for filters, color colon red, attribute color colon red.

So that's very common, that's sort of the classic case. But we might also boost, so we might also say our colors are a bit more complicated than that. We have colors that are exact matches, red. Should match and rank other reds higher, and we have colors that are close to red, like pink or maroon, in our product catalog for some reason. And what we're gonna do is rank the exact matches above the partial matches. And we have some way of managing this.

So really what we're doing is turning our query into a dictionary of attributes that we're gonna somehow use to improve the relevance of our results.

---

## Why Not Just Use Embeddings?

**[00:15:12]** And you might ask, why don't we just… this is something that we do a lot, and it sort of starts to… in some ways, this is what we honestly would call a semantic search. Years ago, before embeddings existed.

### Embedding Collapse / Hubness

**[00:15:34]** So people ask, why don't we just use embeddings for this kind of thing? The main problems that come up with vector databases are, a lot of embedding models are trained on the entire world. Whereas your corpus is in this tiny corner.

So, if you embedded everything in your corpus, just by default of, like, for example, here we've got all furniture. Every piece of furniture is going to be very similar to every other piece of furniture in your corpus. So a query for couch is actually going to return couches first, but you'd be really surprised how close a table can be to a couch.

And I call… people have called this different things, but **embedding collapse, hubness** — everything you care about is actually in a tiny little corner of your embedding model, of the global embedding model trained on the entire Internet of Information.

**[00:16:58]** You can even see this as: couch and table are 0.7 similar, it's just because they're furniture. And in the global set of everything, that's surprisingly close. That's close, compared to, like, a Wikipedia article about, like, Steve Jobs or something.

### Threshold Problem

**[00:17:21]** So that creates complications for us when we just use embedding search. You might argue this is a bad embedding model, but it also might just be something that happens because the embedding model might be trained on just generic CLIP data. And it decides that being a couch is more important than being blue. But there may be couch-like things that are below this, farther down, that are blue, that we don't want to filter out.

So it's hard to basically find a threshold of where do you draw the line to include or exclude search results. And how this really manifests itself is: you will be working as a search professional, you will have a search system that is entirely based on embeddings, and someone will ask you, how do I filter out things that are not relevant? Or why is this showing results that are not relevant?

**[00:18:19]** Things might be ranked perfectly, but finding… you go and you tinker with cutoffs and things, and you realize this is a very difficult task to figure out how to find a cutoff. It's also very query-specific, so, Blue Couch might have a cutoff at, like, .6. But very specific queries, like blue leather couch two-seater, that cutoff might be very different.

### Chat-Style Queries

**[00:20:00]** Chat context gets really complex, too. That's the other thing that happens. You have this back and forth conversation. And there are bits of requirements along the way of what you actually want.

So, we might get some very specific query, like, if we summarize this chat, it's like a bright sky blue sleeper sofa for a living room. And what happens in these situations, and this is more of a case if you were actually to go fine-tune a model. It's very hard to fine-tune a model with many, many unique occurrences of this long chat.

### Fine-Tuning Is Expensive

**[00:21:03]** And the other thing is, the vast majority of teams, it's very challenging to do fine-tuning of embedding models. The reality is, what everyone does is they go to OpenAI and use whatever their embedding model is. That's the 80% case. And then there's the 19% case of people who can get an embedding from Hugging Face or sentence transformers that is tailored to a domain. And then there's the 1% case of people who try and succeed at fine-tuning or developing their own embedding model. So it's not for the faint of heart.

---

## The Alternative: Structured Query Understanding

**[00:22:00]** And the other option is to have a more structured query. So you're treating… in this case, you basically turn the query into a struct instead of a piece of text, and you treat each attribute as its own little similarity problem.

So, what does it mean to search for something in living room? Is that a filter? Do we need to include rooms related to living room that we would not want to filter out or rank more closely? Same with color, item attributes, categories, everything like that. You have to search each of these little things becomes its own little search problem.

**[00:22:23]** And people talk about lexical search as one pillar of search. People talk about embedding search as one pillar of search. The reality is there's a **third pillar** that is roughly, you might call it just **metadata similarity**. Like, how similar is the item's metadata to the metadata extracted from your query.

**[00:23:07]** And there are some advantages to this. Again, it's not mutually exclusive, but one of the big things… you can obviously have simple LLMs interpret this and generate metadata. It's very human manageable. So, if there is ever any need to do some kind of management of the attributes, or have a rule about turning, like, take this query and treat it as the color red — you can do those kinds of things. People on your team can inspect and intervene if they need to.

---

## Five Types of Query Understanding

**[00:30:18]** So there are many types of query understanding.

### 1. Rules

**[00:30:20]** Rules, literally, someone sitting down, say, when you see red in the query, expand to color red. And there are entire systems that do this, using basically regex kind of syntax. There's one famous one called **Quirky** that seems to be popular.

### 2. Historical Data

**[00:30:39]** Another one is just historical data, like, whenever anyone searches for this query, and we see what they click on, they always click on furniture. Anytime someone searches for couch, they click on an item in the furniture category. That's a very common technique.

### 3. ML-Based

**[00:31:00]** Then, if we notice that pattern of, here is a bunch of queries and what people click on, like, the category they click on, or the color of the item they click on, that can also turn into ML training data. So we can say, oh, can we build a model that can predict what users actually… the kind of category or color or whatever they actually click on from the query? Using the interactions with search results as the training data.

### 4. Embedding-Based

**[00:31:36]** The other thing people do is they'll literally say, I'm going to take a query for Crimson Couch. And I have the embedding of the 7 colors that are in my index, like red, blue, yellow. And I take this query, and I do an embedding similarity into these 7 colors, and red is the most similar to the query Crimson Couch, because crimson and red are synonymous. And then they say, aha, I'm gonna take red out, and that's gonna be the color I use.

**[00:32:18]** But all of these could be its own hour and a half conversation. We're going to jump, because we're cool kids and we do stuff with LLMs, we're going to jump to **prompt-based**.

### 5. Prompt-Based

**[00:33:14]** And finally, what we care about is this approach. Query, given this query scarlet sofa, please return the color 1 of blah blah blah blah blah. And scarlet being a kind of red, it would get red back.

**[00:33:29]** And we will do examples all using OpenAI. But these are the kind of dead simple, stupid tasks that it's really easy to load your whatever your favorite local model is, and do this locally and host it yourself. Even though we use OpenAI just for simplicity. You could easily do this in **Ollama**.

**[00:34:01]** And if you remember last time, I talked about structured outputs. Structured outputs are a feature also of Ollama's API, so Ollama has the ability to take a Pydantic model and produce and force a vocabulary that it has to come back as.

**[00:34:19]** And then the third and final thing I'll mention is, Jason Liu, now of OpenAI, has a library called **Instructor**, which basically retries until something corresponds with the schema.

**[Prasad Seemakurthi, 00:34:49]** Doug, can you repeat the last thing? Like, what's the instructor?

**[Doug Turnbull, 00:34:57]** Instructor is just a tool that, you give it a Pydantic model, a schema that the output has to conform to. And it will literally retry the prompt over and over again until it gets back that structure exactly.

---

## Q&A: Rules, Embeddings, and Entity Types

**[Joel Turner, 00:35:23]** Wouldn't human-derived rules suffer from cold start problem for unseen queries?

**[Doug Turnbull, 00:35:35]** Oh, for sure. But you can define patterns, too, so you could say, whether or not it's a good idea, if the term red occurs in a query, then you should filter to red, which kind of helps with cold start problems.

**[Shreesha Jagadeesh, 00:35:53]** For the embeddings-based approach of doing query entity extraction, how do we handle a situation where there are multiple types of entities to be extracted?

**[Doug Turnbull, 00:35:59]** You would just do multiple passes. So you would have, like, a list of all your item types, and… sofa, or maybe couch is the closest thing to sofa. So you would just have different… these are just tiny embedding indices in your search API that can do this kind of lookup for you.

**[Shreesha Jagadeesh, 00:36:36]** So you would run a separate cosine similarity against each entity type, then?

**[Doug Turnbull, 00:36:39]** Exactly, and it's usually very fast and not a big deal.

---

## Synonym Extraction with LLMs

**[00:37:04]** So, really quickly, just, this is a fun experiment. I'm not sure I recommend doing this.

**[00:37:21]** There is a notebook here, which I'm not gonna go deeply into, for LLMs for synonyms. So all this is — back when ChatGPT was first a thing, of course, every search PM and every search developer wanted to see what happens if I just use an LLM to expand my query to synonyms? And that's what we do.

### Pydantic Models for Structured Output

**[00:38:00]** We're gonna talk about this way that we're doing structured outputs. If you remember from Monday, there is this Pydantic notion of a Pydantic model, which is really just a way in Python of specifying a schema. Under the hood, this is really a JSON schema.

You can see here what we have is a class called `SynonymMapping`. Which maps between a phrase from the query to synonyms that are good expansions. And then we have this class here, which is just wrapping a list of synonym mappings.

**[00:38:54]** The other thing to remember is that everything you see here on the left becomes part of the prompt. So we don't want to have stale comments, we want to have nicely named classes that make sense to the LLM. All of this, the schema itself, with all of these type names and descriptions and things, go to the LLM. And that informs how it's going to fill the stuff out.

### Example: "rack glass"

**[00:42:18]** We get this interesting result where we have rack → synonyms shelf, stand, holder. We have glass → synonyms cup, cupware, drinking glass. So, kind of interesting.

**[00:42:36]** And when we use this in search, you can see we get synonyms back. And all we do is we just add their BM25 score of the… just search the name, product name, product description.

**[00:42:54]** And it does a little tiny bit of improvement. BM25 is roughly… gives us a tiny, tiny boost to do synonym expansion.

### Failure Modes

**[00:44:07]** One thing that happens all the time is our LLMs sometimes make decisions that, in the abstract, makes sense, but then for a furniture search dataset, might not make sense.

So, bistro table is kind of a funny thing in the US, where if you talk to your partner about getting a bistro table, you're probably talking about putting some patio furniture on your deck or your porch. But GPT-4 might see Bistro and assume you want restaurant equipment. Those kinds of things happen.

And that's a tricky thing with some of this query understanding stuff — and that goes back to classic AI evals, and how do we do few-shot prompting? Do we give examples? Do we add rules to set exceptions? All that stuff's really important, but that's just the kind of failure mode that you tend to see.

---

## Category Classification

**[00:45:18]** We're gonna jump over to doing the actual classification task that we've talked about so far, where we're actually taking a query and mapping it into some vocabulary.

### Few-Label Classification

**[00:45:31]** In Python, there is this `Literal` type. And a literal is a list of legal values. It's sort of like an enum in other programming languages. When we set up a Pydantic type with a literal, it forces the output to return one of those values. Relatively straightforward.

### Deep Multi-Label Classification

**[00:48:01]** What's more interesting is when we have something like this. It's one thing to classify into 15 categories. It's another thing — and this is probably more typical of our search lives — to have to say, I need to classify this query into this extensive product catalog taxonomy. These people have extensive, lengthy classification systems. This could also be a list of thousands of brands.

**[00:48:30]** But that's actually a bit more typical of search, where our vocabulary is maybe messy, it's large, and it's just something we have to deal with.

### Returning Multiple Classifications

**[00:49:49]** The other thing that is nice to do is to not just return a single classification, but potentially return a list. If we return a single classification and filter to that classification, that creates a lot of risk that we're actually going filter out the right thing. And sometimes these are messy situations.

**[00:50:39]** So the prompt asks for: diverse sets of categories. Different top-level categories are better than very similar classifications where most of their tree and subtree is shared. Return an empty list if no classification fits or it's ambiguous.

### BM25 Boosting Strategy

**[00:51:09]** When we actually use this in search, we're only gonna boost on the top-level category match, and then this subcategory matching. So if the LLM says, I think this item is a furniture slash office slash whatever. First thing we do is boost the furniture products higher. The next thing we do is, within that, we boost office slightly higher.

**[00:52:19]** If you do this, and you're basically looping over every category the LLM returned, you get actually a really nice NDCG boost. The token cost, though, is pretty high. The input tokens, we have to put in this giant list of results into the prompt.

---

## Cost Optimization: Dynamic Pydantic Enums (Search-Then-Classify)

**[01:10:07]** Two approaches have come up prominently when doing this work. Independently discovered techniques that I see over and over again by search teams.

### Approach 1: Search-Then-Classify

**[01:10:16]** The idea here is that you search for relevant results first, you get the top N.

So the first thing we would do is select some relevant results first. We're doing a BM25 search before we do classification, so it's sort of like the opposite of what we would normally do. Instead of giving the LLM the full category list, we then say, I'm only going to let you classify within the categories that occurred in, like, the top 100 results.

**[01:12:48]** But now, instead of classifying into hundreds of labels, we're classifying into, like, 10 or so. That helps a bit. Input tokens came down, you're using a cheaper model, output tokens are also less.

**[01:13:29]** I think what model were we using? GPT-4.1 Nano. So before, we were using just GPT-4.1, so the big, beefy model.

This is a technique I see all the time, very useful. Requires you to search, and then classify. You might do this as a batch on a backend.

### Approach 2: Hypothetical Categories

**[01:14:13]** The other concept is something I like to call **hypothetical categories**.

We all know LLMs hallucinate. So we say, let's use that. We tell an LLM, we give the LLM a query as the prompt. And we say, you need to create novel, never-before-seen-before furniture, home goods, or hardware classification that best fit this search category. And the LLM is given some examples of what product classifications look like.

We don't want the LLM to produce a valid classification. We just wanted to produce something that looks good, that looks fake, but is convincing. It's very similar to this notion of **hypothetical document embeddings** (HyDE).

**[01:15:53]** So we do hypothetical classifications, or hallucinated classifications. We say, create a classification for a product that might be relevant to this query.

**[01:16:34]** So that category does not exist in our dataset. But, remember before, when I talked about using embedding-based query understanding? What we can do is take our real categories, and build, embed them all, keep them in memory. And for every fake hypothetical classification, we can look up the most similar real classification.

So it's based kind of like an **entity resolution** from a hypothetical hallucinated thing the LLM built to something real. And that also gets us a really nice NDCG boost.

**[Erie, 01:18:33]** So you're basically mining the latent space of the models and trying to force it towards something.

**[Doug Turnbull, 01:18:36]** That's basically right, we're just like, be creative. And we actually, in the prompt, if you go through the notebook, basically says something like, be creative, try to be novel and interesting, and that seemed to help.

**[Gordon, 01:19:27]** Is there a sweet spot?

**[Doug Turnbull, 01:19:27]** I haven't really found a sweet spot, I don't know. It seems like a couple here seems to help, 3 or 4. But definitely, I'd be curious if people experiment with this.

---

## Ground Truth from Eval Data

**[00:59:34]** The other thing to think about is: could we create a classifier using the eval data directly, just to get a measure of the opportunity?

**[01:00:01]** We have the actual judgment data, and we have queries here, like salon chair, and we might notice that, like, 90% of the time, salon chair, the relevant items have category furniture. And that could be a thing that we remember as kind of a ground truth.

**[01:00:49]** And we can take that, and we can just say, I'm gonna build a classifier that cheats, basically. That always returns the right answer.

**[01:03:58]** When you do that, that's pretty neat, because you can see the opportunity of correctly classifying the query. So you can see that the best we could possibly do with a perfect classifier — we could get as high as .575 on NDCG if we did a reasonable attempt at getting every query to the right category and subcategory.

---

## Category Precision ≠ NDCG

**[01:22:53]** There is not a neat linear relationship between category precision, or whatever your precision of your classifier, and NDCG. And there's a lot of reasons for that.

**[01:23:51]** You're gonna see that there's this population of queries that actually benefits from classification. And a population of queries that, even if you classified them correctly, it's not going to change their NDCG at all. And that's why there's not necessarily a linear relationship between classification accuracy and your NDCG. You might improve things, you might see NDCG not move at all, and it might just be because the queries that you're classifying correctly now are already good with BM25 or something.

---

## Latency Considerations

**[01:20:00]** Even going out to your search API, going out and doing a call out to Nano to do the easiest version of this is still, like, 300 milliseconds the latency, I think, in a best-case scenario. And then maybe you have 100 milliseconds out to your vector database or search engine to actually do search.

**[01:20:32]** Of course, if we're doing chat, all of this stuff can just apply. You can just do this stuff at query time, it's not a big deal, because you're already having seconds of latency talking to a chat API.

**[01:20:47]** Everything I've talked about, we probably are pre-computing information about queries. We're not doing this in real time. So, often there's a nightly job where we're taking yesterday's queries and classifying them.

### Semantic Cache

**[01:21:23]** And then the other thing I want to throw out here is this idea of a **semantic cache**. You could also have a vector database for queries that helps you find similar queries that have been processed with your query understanding. So if you have "shoes comma red" and you've pre-computed a well-understood "red shoes" query, you might be able to reuse the existing understanding without even having to go to an LLM.

---

## Deep Attribute Discussion

**[Zenit, 01:26:14]** Let's have a more complex example with the shoes. Let's say Nike shoes, red, 42, 42 being a shoe size. Or even an unknown brand. Would you have a classifier for each of these? Do we have examples of using agents to split up the query?

**[Doug Turnbull, 01:28:33]** I hear a couple of things in what you're saying. Extremely extensive sets of attributes, like dozens and dozens.

**[01:28:53]** One thing to do is classify your queries into domain-specific sets — fashion will have its own set of attributes, and furniture will have its own. If you're working at a major marketplace, that can be really important, because that can help shrink the problem a lot. Getting into the right location, then you're like, oh, well, fashion, now I have to understand these particular attributes of the query.

**[01:30:10]** In those situations, like, I wouldn't bend the universe to try to solve that problem, I would just accept that that's a problem, and that's where we need to fall back on a maybe less precise version of search that's just doing embedding retrieval and lexical retrieval.

**[01:30:45]** A lot of search is actually in layers. You kind of have this layer where you really understand some set of queries, but then there's another set of queries that kind of sneaks through, and you really then just focus on general ranking for those sets of queries, or you're not entirely sure on the intent.

**[01:31:14]** You can't necessarily model every attribute in your system, because you would go crazy. I would start with the most important ones, and then gradually get down and down to finer grain as you need to.

---

## Industry Benchmarks

**[AA, 01:33:00]** Are there any NDCG metrics in the industry to follow for organic search slot position levels?

**[Doug Turnbull, 01:33:05]** I would say, generally, no. The benchmarks you find are on open datasets, like WANDS, or MS MARCO, or whatever. There are things like BEIR for benchmarking information retrieval that might be worth looking at.

---

## Companion Resources

- **Slides:** [[articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search|LLM Query Understanding — Cheat at Search (Slides)]]
- **Course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)
- **Author:** [softwaredoug.com](http://softwaredoug.com)
- **Related:** [[entities/doug-turnbull]], [[entities/doug-turnbull-core-ideas]], [[concepts/query-understanding]], [[concepts/bm25]], [[concepts/vector-search]]
