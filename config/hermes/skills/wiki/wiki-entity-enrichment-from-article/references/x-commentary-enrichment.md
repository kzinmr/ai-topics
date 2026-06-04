# X/Twitter Commentary Enrichment for Existing Wiki Pages

> Workflow for incorporating X/Twitter commentary, reactions, and discussion threads into wiki pages that already exist (raw articles, concept pages, entity pages). Distinct from single-tweet ingestion or megathread ingestion — the tweet is a *reaction* to existing content, not the primary source.

## Trigger

User provides an X URL and says something like "これに対するコメントも取り込んで" / "incorporate the commentary" — meaning an existing wiki page should be enriched with social media reactions.

## Key Differences from Standard X Ingestion

| Aspect | Standard X Ingestion | X Commentary Enrichment |
|--------|---------------------|------------------------|
| Relationship to content | Tweet IS the source | Tweet REACTS to existing source |
| Pages affected | Create new pages | Update 2-3 existing pages |
| Content type | Primary analysis | Meta-commentary, framing, community perspective |
| Typical sources | 1 tweet or thread | Main tweet + follow-ups + quoted/retweeted others |

## Step-by-Step

### 1. Fetch the Tweet

```bash
xurl read <TWEET_ID>
```

### 2. Trace the Full Conversation

Commentary tweets often reference other tweets (quote tweets, replies, retweets). The `xurl read` response includes `referenced_tweets` with quoted/retweeted IDs. **Always fetch those too** — they provide essential context.

```bash
# Fetch referenced tweets
xurl read <QUOTED_TWEET_ID>

# Fetch the author's recent tweets to find follow-ups in the same conversation
xurl "/2/users/<AUTHOR_ID>/tweets?max_results=10&tweet.fields=conversation_id,in_reply_to_user_id,created_at"
```

Filter the author's timeline by `conversation_id` matching the main tweet to find all follow-ups.

**Pitfall**: `xurl read` may truncate long tweet text. If text ends with `https://t.co/` (a link), the tweet may be cut off. For Note Tweets, use `xurl "/2/tweets/<ID>?tweet.fields=note_tweet"` for full text. For regular tweets, the truncation IS the full text (character limit).

### 3. Identify All Participants

A commentary thread often involves multiple voices:
- **Original author** (the person whose work is being discussed)
- **Commenter** (the person whose X URL was provided)
- **Other participants** (quoted, retweeted, or replying)

Fetch author info for any new participants:
```bash
xurl user @<username>
```

### 4. Determine What to Add Where

Typical update targets for a 3-page enrichment:

| Page Type | What to Add |
|-----------|-------------|
| **Raw article** | New "Community Reactions" section at the end with full quotes and source links |
| **Concept page** | New "Research Culture Commentary" or "Community Perspective" section with key quotes |
| **Entity page (commenter)** | Expanded section about the topic + key quotes + X URLs in sources |

### 5. Update Raw Article

Add after the existing References section (separated by `---`):

```markdown
---

## Community Reactions: Author Name on X (YYYY-MM-DD)

[Author] posted a reflective thread on X after publication:

**Main tweet** ([source](https://x.com/...), N likes, N bookmarks, N impressions):

> "exact quote"

**Follow-up tweet** ([source](https://x.com/...)):

> "exact quote"

**Other Participant** ([source](https://x.com/...)):

> "exact quote"

### Meta-commentary

[1-2 paragraph synthesis of what the commentary means beyond the technical content]
```

### 6. Update Concept Page

Add a section before "Related Concepts":

```markdown
## Research Culture Commentary

[Author] framed the work as [broader insight]. In a widely-engaged X thread ([source](...)):

> "key quote"

> "second key quote"

[Other participant] echoed this: "their quote" ([source](...)).
```

Update `sources:` in frontmatter with the new X URLs. Bump `updated:` date.

### 7. Update Entity Page (Commenter)

- Expand the existing section about the topic to include the X thread framing
- Add 1-2 key quotes to the "Key Quotes Collection" section
- Add X URLs to the "Sources" section

### 8. Log and Commit

```bash
# Append to log.md
echo "" >> wiki/log.md
echo "## YYYY-MM-DD" >> wiki/log.md
echo "- **updated** path/to/file.md — description" >> wiki/log.md

# Commit
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: add Author X commentary on Topic" && git push
```

## Pitfalls

| Pitfall | Fix |
|---------|-----|
| Only fetching the main tweet, missing follow-ups | Always check `referenced_tweets` and the author's recent timeline filtered by `conversation_id` |
| Missing other participants' contributions | If the main tweet is a quote tweet, fetch the quoted tweet too |
| Truncated tweet text presented as complete | Check if text ends mid-sentence with a `https://t.co/` link — likely truncated |
| Adding commentary to raw/ without `---` separator | Always use `---` before the Community Reactions section to visually separate from original article |
| Forgetting to update concept page sources | Add all new X URLs to `sources:` frontmatter in the concept page |
| Not bumping `updated:` date | Always update the `updated:` field when modifying concept or entity pages |
