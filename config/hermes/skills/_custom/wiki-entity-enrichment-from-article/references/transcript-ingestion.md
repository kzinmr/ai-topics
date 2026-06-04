# Transcript Ingestion Workflow

When ingesting a lecture/workshop transcript into `wiki/raw/transcripts/`:

## Directory
- `wiki/raw/transcripts/` — Layer 1 (immutable), same as articles and papers
- Create directory if it doesn't exist: `mkdir -p ~/wiki/raw/transcripts/`

## Naming Convention
Same pattern as articles: `{YYYY-MM-DD}_{source-slug}_{content-slug}.md`
- `YYYY-MM-DD` = lecture/presentation date (not ingestion date)
- `source-slug` = author handle (e.g., `softwaredoug`)
- `content-slug` = descriptive slug

## Frontmatter Template
```yaml
---
title: "<Series Name> — <Topic> (Lecture Transcript)"
author: <Author Name>
date: <YYYY-MM-DD>
date_ingested: <YYYY-MM-DD>
source: <slides URL or source URL>
type: transcript
tags:
  - <topic-specific tags from SCHEMA.md>
  - transcript
related_article: articles/<corresponding-article-filename>.md
participants:
  - <Author Name> (instructor)
  - <Other participants>
---
```

## Content Structure
- Preserve timestamps from the original transcript (`**[HH:MM:SS]**`)
- Use structured headings to organize the lecture flow
- Mark Q&A exchanges with participant names: `**[Participant, HH:MM:SS]**`
- Include a "Companion Resources" section at the end linking back to the article and related wiki pages

## Bidirectional Linking (MANDATORY)
1. **Transcript → Article**: In the transcript's frontmatter (`related_article`) and body (`**Companion slides:**`)
2. **Article → Transcript**: Add `**Lecture transcript:**` link near the top of the article (after source/companion course lines)
   ```
   **Lecture transcript:** [[raw/transcripts/<transcript-filename>|<Display Title>]]
   ```

## Index and Log Updates
- **index.md**: If no "Raw Transcripts" section exists, add one after "Queries" section:
  ```
  ## Raw Transcripts (N pages)
  - [[raw/transcripts/<filename>]] — <Description with key topics covered>
  ```
  If the section already exists, append the new entry and update the count.
- **log.md**: Append entry with created file, updated article, and updated index

## Pitfalls
- Transcripts are Layer 1 (immutable) — do not edit after initial save
- `type: transcript` is the correct frontmatter type (not `type: article`)
- Always add `transcript` to tags list for discoverability
- Transcripts may contain participant names from Q&A — include them in `participants` field
