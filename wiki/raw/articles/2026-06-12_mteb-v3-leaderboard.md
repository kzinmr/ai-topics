---
title: "MTEB Leaderboard: From a slow demo to feature-rich leaderboard"
type: article
source: huggingface.co/blog
author: Solomatin Roman, Kenneth C. Enevoldsen, Isaac Chung
date: 2026-06-12
url: https://huggingface.co/blog/Samoed/mteb-v3-leaderboard
scraped_at: 2026-06-15T22:30:00Z
---

# MTEB Leaderboard: From a slow demo to feature-rich leaderboard

TL;DR: A new version of the MTEB leaderboard has been released that is much faster, with improved filtering, model comparison, and transparency features.

Since its initial release, MTEB has had multiple benchmarks, starting from a simple table view with minimal filtering to a granular leaderboard. With the increase in both the number of models and benchmarks, the previous leaderboard became unreliable in terms of speed and uptime. The new leaderboard is built on a more reliable and scalable framework using FastAPI and Svelte.

## Key Features

- **Speed**: The new leaderboard is significantly faster than the previous version
- **Customization**: Users can filter benchmarks by domain, language, modality, and individual tasks
- **Transparency**: The leaderboard allows inspection of datasets used to evaluate models, with a viewer for Hugging Face datasets, results, and task metadata. It also indicates whether a model has been trained on the task's training set or is seeing it for the first time (zero-shot)
- **Broader improvements**: The ranking encourages development across the frontier rather than just the top models, by ensuring quick views display top models for their size bracket and providing performance-by-runtime analytics
- **Model comparison**: Users can pin models for easy comparison and get head-to-head analysis
- **API**: Leaderboard scores can be fetched locally via CSV download or API (https://mteb-leaderboard-backend.hf.space/docs)

The leaderboard is available at: https://huggingface.co/spaces/mteb/leaderboard
