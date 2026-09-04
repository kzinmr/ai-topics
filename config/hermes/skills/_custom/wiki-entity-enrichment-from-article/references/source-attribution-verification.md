# Source Attribution Verification

When an article attributes a concept or term to a specific person (e.g., "Karpathy called it 'X'"), **verify before accepting the claim**. Articles by secondary authors often frame/interpret/coin terms and attribute them loosely.

## Verification Workflow

1. **Extract the claim**: What specific term or idea is being attributed? Who is it attributed to?

2. **Check the attributed person's public output**:
   - X/Twitter RSS feed via fxtwitter: `curl -s "https://fxtwitter.com/{handle}/feed.xml"` — grep for key terms
   - X search (7-day window): `xurl search "from:{handle} {term}" -n 10`
   - Blog RSS if known
   - Recent long-form articles: `xurl "/2/tweets/{ID}?tweet.fields=article"` or `tweet.fields=note_tweet`

3. **Document findings in the raw article**:
   - If source found: cite the specific tweet/post URL
   - If NOT found: add explicit sourcing caveat explaining the term may be the article author's framing, not the attributed person's direct quote

4. **In the wiki concept page**: use language like "as framed by [article author]" rather than presenting it as the attributed person's own terminology when the original source can't be verified

## Example (2026-06-09)

Avi Chawla's X Article attributed "system prompt learning" to Karpathy. Verification:
- Grepped Karpathy's fxtwitter RSS for "system prompt" → no match
- `xurl search "from:karpathy system prompt learning"` → 0 results
- Conclusion: term is Chawla's framing of Karpathy's broader arguments, not a direct Karpathy quote

In the wiki page, this was documented as:
> **Sourcing caveat:** The specific term "system prompt learning" does not appear in Karpathy's public X feed...

## Pitfalls

- X API free tier only covers ~7 days. For older tweets, use RSS feed or direct ID lookup (`xurl read <ID>`)
- RSS feeds typically contain only the ~40 most recent tweets
- fxtwitter RSS may not include quoted tweets or retweets
- If the attributed person has a blog, check that too — some ideas are published there first
