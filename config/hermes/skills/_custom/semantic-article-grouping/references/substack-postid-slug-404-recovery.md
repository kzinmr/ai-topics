# Recovering a full Substack body when the guessed /p/ slug 404s

Validated 2026-10-23 (Latent Space "You are the Team — Anekha Sokhal, Moshi", pub 1084089,
post_id 221404681). The newsletter subject / source_name was "The Recommendation Engine for
Commodity Traders — Anekha Sokhal, Moshi" but the real post title was "You are the Team —
Anekha Sokhal, Moshi". The guessed slug `latent.space/p/the-recommendation-engine-for-commodity`
returned a 404 ("Page not found — Latent Space", ~18KB of nav chrome, 0 article paragraphs).

## Two reliable fallbacks (use either, both returned 31 real paragraphs + full transcript)
1. **app-link post_id, no token** — strip the JWT token from the checkpoint's app-link URL:
   `https://substack.com/app-link/post?publication_id=<PUB>&post_id=<POST>&isFreemail=true`
   (the `token=eyJ...` param is what makes web_extract fail; dropping it still resolves).
2. **home/post/p-{post_id}** — `https://substack.com/home/post/p-<POST_ID>` (the existing
   redirect-stub-discovery note already lists this variant; confirmed here it returns full body,
   not just a stub title, for Latent Space).

Both resolve the canonical post and its JSON-LD `<article>` body regardless of the slug being
guessed wrong from the email subject.

## Generalization
When a Substack candidate has `publication_id` + `post_id` in an app-link URL, **prefer post_id
resolution over slug guessing**. The email subject is an unreliable slug source (curation
subjects are often rewritten from the real post title). Pattern:
- Try the slug derived from the subject first (cheap).
- On 404 / nav-chrome-only response (`bytes` < ~25KB, 0 long `<p>`, title contains "Page not found"),
  immediately fall back to app-link-without-token or home/post/p-{post_id}.
- Verify success by paragraph count (>= 20 substantial `<p>` = full body recovered).

## Watch for homonyms in coverage checks
"Moshi" grep-hits existed but were the **Kyutai full-duplex audio model**, not the commodity-trader
startup hellomoshi.ai. A keyword hit in `entities/` / `concepts/` is NOT proof the *specific*
entity is covered — disambiguate by context before downgrading a genuine new-entity take to skip.
