---
name: opinion-leader-depth-analysis
description: Systematic depth analysis framework for opinion leaders tracking research completion across 4 layers - L1 Profile, L2 Timeline, L3 Thought Analysis, L4 Ongoing Monitoring
version: 1.0.0
metadata:
  hermes:
    tags: [wiki, research, depth-analysis, opinion-leaders, quality-control]
    homepage: https://github.com/kzinmr/ai-topics
prerequisites:
  skills: [blog-author-thought-analysis, wiki-entity-upgrade]
---

# Opinion Leader Depth Analysis Framework

## Purpose
Track research completion depth for each opinion leader in the wiki. Ensures consistent quality and prevents duplicate effort by making "what's done" and "what's next" explicit in frontmatter.

## The 4 Layers

### L1: Basic Profile
- [ ] Name, handles, primary platforms
- [ ] Blog URL, RSS feed, social accounts
- [ ] Current role/company/affiliation
- [ ] Brief bio (1-2 paragraphs)

### L2: Timeline & Works
- [ ] Chronological activity timeline (date x event)
- [ ] Major projects with descriptions
- [ ] Published articles/blog posts/videos list
- [ ] Key milestones and inflection points

### L3: Thought Analysis (Core Differentiator)
- [ ] Core Philosophy: 3-5 central ideological positions
- [ ] Direct Quotes: Verbatim quotes with source URLs (>30% of analysis)
- [ ] Thought Evolution: How positions changed over time
- [ ] Key Questions: What they are currently exploring
- [ ] Conceptual Frameworks: Coined terms, mental models
- [ ] Cross-References: Links to other thinkers, concepts, wiki pages
- [ ] Citations: Every claim has a source URL

### L4: Ongoing Monitoring
- [ ] RSS feed registered in blogwatcher
- [ ] Social/X account tracked
- [ ] Auto-alerts for new posts/tweets
- [ ] Periodic review schedule

## Frontmatter Structure

```yaml
research_depth:
  L1_profile: done
  L2_timeline: done
  L3_thought_analysis: done
  L4_monitoring: active
  last_deep_dive: 2026-04-10
  next_review: 2026-05-10
  confidence_score: 0.85
  sources_analyzed:
    - blog: 12 articles
    - x_posts: 50+ tweets
    - podcasts: 2 episodes
    - papers: 1
```

## Quality Checklist for L3 Completion

1. **Direct Quote Ratio**: At least 30% of thought analysis content should be direct quotes
2. **Source Completeness**: Every major claim has a URL citation
3. **Evolution Tracking**: At least 2 time periods compared
4. **Framework Extraction**: At least 2 named concepts/frameworks identified
5. **Cross-Reference Density**: At least 3 wiki page links

## Workflow

### For New Opinion Leaders
1. Check `~/scripts/blog_authors.json` or `~/x-accounts.yaml` for pre-scraped data
2. Run L1: Create basic entity page
3. Run L2: Add timeline and works
4. Run L3: Extract thoughts, quotes, frameworks (use blog-author-thought-analysis skill)
5. Run L4: Set up monitoring

### For Existing Pages
1. Read current page and check frontmatter
2. Identify which layers are missing
3. Fill gaps using blog posts, tweets, podcasts
4. Update frontmatter with `research_depth`
5. Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: depth-analysis <person> L1-L4" && git push`

## Priority Order
1. Core AI/Agent thought leaders (Karpathy, Willison, Antirez already done)
2. Harness/Infrastructure leaders (Ryan Lopopolo, Boris Cherny)
3. Platform/Tool leaders (Addy Osmani, Simon Willison)
4. Emerging voices (gm8xx8, Daniel Han)

## Page Naming Convention
- Use full domain name: `simon-willison.md` (not `simonw.md`)
- If duplicate pages exist (e.g., simonw.md + simon-willison.md), merge into canonical name and delete the duplicate
- Check for duplicates before declaring L3 incomplete

## Pitfalls
- **Don't paraphrase quotes**: Use exact wording for citations
- **Don't create duplicate pages**: Check existing entity pages first
- **Don't skip L3**: This is the core value - philosophy extraction
- **Don't leave stale monitoring**: Update L4 status when feeds change
- **L3 auto-check must not rely on specific header names**: Many completed pages use `## Core Ideas`, `## Philosophy`, `## Thought Framework` etc. Check for substance, not exact header match
- **Do NOT track "which sources have been read"** as a binary flag: the same source yields different insights at different analytical depths. Track depth level and last_review date instead.