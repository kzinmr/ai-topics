---
title: "Image search using text classification"
author: Ashpreet Bedi
source: https://www.ashpreetbedi.com/image-search-using-text-classification
date: 2026-05-29
date_ingested: 2026-06-01
type: blog_post
tags:
  - image-search
  - agentic-data-labeling
  - multimodal
  - search
  - gemini
  - embeddings
  - pgvector
---

# Image search using text classification

Agentic data labeling is one of those workhorse use-cases that keeps on delivering unexpected results.

In this post, I'll show you how to build a working image search engine using agents that label images using search terms and then running search on those descriptions instead of the images.

## Why?

Image search has generally been a HARD problem. CLIP, multimodal vectors, fine-tuned encoders. So many use cases are blocked because of the complexity whereas the truth is that not every use-case needs google photos like infrastructure.

Some just need a quick and dirty image search engine and now that's possible in about 100 lines of code.

## The old default

For years, the assumed path for "search images by natural language" looked like:
1. Run every image through a multimodal encoder (CLIP and friends) to get a vector.
2. Run the query string through the same encoder to get a vector.
3. Nearest-neighbor in shared embedding space.

It's the right approach, but comes bearing costs. Swap encoders and you re-embed your whole library. The vectors are opaque, can't read them, can't grep them, can't explain a miss. And one-word queries like "car" or "drink" tend to land in fuzzy regions of the latent space where the wrong things are also nearby.

## The new approach - classify using vision models

Gemini 3.5 flash turns images into a structured description that reads like a search query a human would type. The model already knows that a yellow NYC taxi is also a car, a vehicle, a piece of transportation, and a thing that lives in Manhattan.

Once we have the description, we don't need image embeddings. We need text embeddings, which we've known how to do for a decade. And you get full-text search for free: stemming, prefix match.

> The cheap version of image search might be the right version for most use cases.

## The labeling schema

```python
class ImageDescription(BaseModel):
    caption: str         # one or two sentences, written like a search query
    subjects: list[str]  # 1-5 noun phrases, specific + generic
    scene: str           # short noun phrase: "urban street at night"
    visual_style: str    # "soft morning light", "vibrant macro"
    tags: list[str]      # 12-20 lowercase keywords
```

The agent returns this as structured output. We flatten it into one string and embed that string.

## Search becomes free

Once your index is text, everything you've ever wanted from search is in the box:
- **Cosine similarity** over embedded descriptions for semantic recall
- **PostgreSQL full-text search** (`to_tsvector` + `websearch_to_tsquery`) with stemming
- **Hybrid fusion,** pgvector blends the two scores into one ranked list

## Run it yourself

The full cookbook: https://github.com/agno-agi/agno/tree/main/cookbook/data_labeling/image_search

Clone, `pip install -r requirements.txt`, set `GOOGLE_API_KEY`, point at a pgvector, and you have a working image search engine in a couple of minutes.

Ashpreet - *built with 🧡 using [Agno](https://github.com/agno-agi/agno)*
