# Rich Thread-Only Bookmark Processing

When an X bookmark has NO external article URL but the tweet thread itself contains substantial technical content (10-part announcements, benchmark results, paper links, code/model repos), treat the thread as the article.

## Detection Signals

- Bookmark has `external_urls: []` (no external article)
- Tweet text contains numbered thread markers: `[1/N]`, `[2/N]`, etc.
- High engagement: >100 bookmarks, >500 likes, >50 retweets
- Contains technical claims: benchmarks, model names, architecture descriptions, paper/code links
- Author is a known researcher/engineer with verifiable credentials

## Workflow

### 1. Fetch Author Profile
```bash
/opt/data/bin/xurl user <handle> > /tmp/author.json
```

Extract: name, description, institution, followers, prior work mentions.

### 2. Reconstruct Full Thread
```bash
# Save to file (pipe_to_interpreter blocked in cron)
/opt/data/bin/xurl search "conversation_id:<tweet_id>" --max-results 100 > /tmp/thread_full.json
```

Process with Python script (write_file → terminal python3):
```python
import json

with open('/tmp/thread_full.json') as f:
    d = json.load(f)

author_id = '...'  # from author profile
thread_tweets = []

for t in d.get('data', []):
    if t.get('author_id') == author_id:
        thread_tweets.append({
            'id': t['id'],
            'created_at': t.get('created_at', ''),
            'text': t['text']
        })

# Sort by creation time
thread_tweets.sort(key=lambda x: x['created_at'])

# Combine into article body
full_text = '\n\n'.join(t['text'] for t in thread_tweets)
print(full_text)
```

### 3. Extract Paper/Code/Model Links
Thread tweets often contain links in replies (not in the bookmark metadata):
- Paper URL (arXiv, OpenReview)
- Code repository (GitHub)
- Model weights (HuggingFace)
- Collaborator mentions (@handles)

### 4. Save Raw Article
Save the combined thread text as a raw article:
- Path: `wiki/raw/articles/{YYYY-MM-DD}_{author-slug}_{topic-slug}.md`
- Frontmatter: include `source: x-thread`, `author: @handle`, `conversation_id`, `url`
- Body: combined thread text with section markers

### 5. Wiki Actions (by content type)

| Thread Content | Wiki Action |
|---------------|-------------|
| New model/agent announcement with benchmarks | Create entity page for model + create concept page for technique |
| Research paper thread | Entity page for author + enrich concept page |
| Tool/OSS release announcement | Entity page for tool + entity page for creator |
| Framework/thesis thread | Create concept page + entity page for author |

### 6. Entity Page Creation for Author
Use xurl user profile + web search for background. Follow `wiki-entity-enrichment-from-article` skill's skeleton enrichment pattern (Section 5b).

## Pitfalls

- **Missing thread tweets**: xurl search may not return all replies in one page. Check for `next_token` in the meta and paginate.
- **Truncated tweets**: xurl may truncate long tweet text. Verify tweets ending with `…` or `https://t.co/` are complete.
- **pipe_to_interpreter block**: In cron mode, always use write_file → terminal python3 pattern. Never pipe xurl output to python3.
- **Duplicate entity detection**: Before creating author entity page, search for existing pages under different slugs (handle vs real name).

## Example: Harness-1 Thread (Jun 2026)

Patrick Jiang (@patpcj) announced Harness-1 in a 10-part thread with 2470 bookmarks, 1999 likes.

- **Thread content**: Full technical description of state-externalizing harness, 20B model, benchmark results vs Opus-4.6/GPT-5.4, transfer learning results (+17.0 recall), training data details (899 SFT + 3453 RL queries), ablation results
- **Paper/Code/Model links**: Found in thread reply tweet (arXiv, GitHub, HuggingFace)
- **Collaborators**: @zhiyiscs, @HammadTime, @kellyhongsn, @PatrickXu565299, @SunJiashuo36
- **Wiki actions**: Entity page for Patrick Jiang + concept page for state-externalizing harness + enrich harness-engineering concept

The bookmark had 0 external_urls but was the highest-value item in the batch. The "thread-only → skip" rule would have discarded it.
