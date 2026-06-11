---
title: "Using Reinforcement Learning and $4.80 of GPU Time to Find the Best HN Post Ever (RLHF Part 1)"
author: Kyle Corbitt
date: 2024-10-28
source_url: https://corbt.com/posts/hacker-news-rlhf-part-1
type: article
tags:
  - reinforcement-learning
  - rlhf
  - reward-model
  - fine-tuning
  - openpipe
  - evaluation
---

# Using Reinforcement Learning and $4.80 of GPU Time to Find the Best HN Post Ever (RLHF Part 1)

**Author:** Kyle Corbitt
**Date:** October 28, 2024
**Source:** https://corbt.com/posts/hacker-news-rlhf-part-1

---

I've been exploring how to use RLHF (Reinforcement Learning from Human Feedback) to improve the content curation in my Hacker News reader app, Hacker News Digest. This post shares what I've learned about using LLMs to rank content, collecting human preferences, and building better models.

## The Problem

Hacker News front page only has 30 items, and the signal-to-noise ratio varies. The author wanted to surface stories he'd find most interesting from the full feed.

## Phase 1: Prompt Engineering

Gave Claude a prompt with all stories and asked it to rank them. Worked ~70% of the way but had failure modes: over-ranking AI content, under-ranking niche technical content, failing to account for community signal, and inconsistent preferences.

## Phase 2: Adding Features

Added HN metadata (points, comments), content analysis via smaller models, and historical preferences.

## Phase 3: RLHF

Built a proper pipeline:

1. **Preference data collection**: ~500 pairwise comparisons over a few weeks via a simple web UI. Preferences were ~90% self-consistent.
2. **Feature engineering**: LLM-generated features (quality, novelty, relevance), text embeddings, HN metadata (log(points), log(comments), points_per_hour), and temporal features.
3. **Reward model training**: Two-layer neural network (50→32→1) using Bradley-Terry loss. Achieved 78% accuracy on held-out pairs vs 65% for the prompt-only approach.

## Key Findings from the Reward Model

- Comment count matters more than points
- LLM quality rating was the single most predictive feature
- Topic distribution/variety was important
- Time features mattered less than expected
- Points-per-hour (velocity) was useful

## Results

Click-through rate improved from ~25% (HN default) → ~40% (prompt engineering) → ~60% (RLHF reward model). Time on site increased ~2x. Discovered interesting content that never made the front page.

## Lessons

- Prompt engineering gets you 70% there
- Small preference data goes far
- Feature engineering > model architecture
- LLMs are good feature extractors but bad rankers
- Consistency is the key challenge
- Pairwise comparisons are information-rich

## Next (Part 2)

Online learning, contextual ranking, scaling to other domains, better loss functions, DPO vs separate reward models.
