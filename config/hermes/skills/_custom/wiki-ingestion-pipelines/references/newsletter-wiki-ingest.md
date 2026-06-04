# Newsletter Wiki Ingest — Full Reference

Full procedure for the downstream newsletter/blog ingestion pipeline.

## Input Format
Triage checkpoint JSON (from `context_from` cron chaining or checkpoint file):
```
${HERMES_HOME}/cron/data/newsletter/triage_latest.json   (newsletter)
${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json   (blog)
```

Structure:
```json
{
  "summary_ja": "...",
  "decisions": [
    {
      "item_id": "...",
      "source": "newsletter",
      "title": "...",
      "url": "...",
      "recommended_action": "take",
      "reason_ja": "★★★★★ ...",
      "candidate_wiki_path": "concepts/slug"
    }
  ]
}
```

## Checkpoint States
- **State A** (ok=true, valid decisions): Filter to `recommended_action === "take"` decisions. If none, respond `[SILENT]`.
- **State B** (no checkpoint file): Fall back to Triage Failure Recovery — scan raw newsletter files.
- **State C** (ok=false, has output_path): Read the triage failure output file to extract embedded newsletter-ingest checkpoint candidates. The triage job's markdown output contains the full prompt including the `candidates` array. Parse candidates, resolve canonical newsletter URLs, perform triage manually. Most common recovery path.

## Prior Batch Detection
Scan last 30-50 lines of log.md for matching source title. If found:
1. Read what was already processed
2. Check if candidate_wiki_path files already exist
3. If all concept-level pages exist, shift to entity-level updates
4. Don't duplicate log entries — append as sub-section

## Source File Fallback
Raw newsletter files may be empty stubs (< 1KB). Fallback:
1. Use `web_extract(url)` from the triage decision
2. For redirect chains (substack.com/redirect/..., link.mail.beehiiv.com/...), search article title + source name
3. Note the fallback in log entry

## Triage Failure Recovery — Full Workflow

When `ok: false` with a valid `output_path`:
1. **Read the failed triage output**: `read_file <output_path>` — the markdown file contains the triage job's full prompt including the embedded newsletter-ingest checkpoint (the `candidates` array with all raw links)
2. **Extract candidates from embedded script output**: The candidates include `publication_id`, `post_id`, and noise URLs. Parse `source_name` (subject line) and `raw_path` for each newsletter.
3. **Resolve canonical newsletter URLs**: From the candidates, find `open.substack.com/pub/{publication}/p/{slug}` links (usually Link 7-9 in Substack emails). These resolve to the actual newsletter post body via `web_extract`.
4. **Extract real article links** from the newsletter post body — NOT from the raw tracking URLs in the candidates array. The post body contains the actual curated article links, titles, and descriptions.
5. **Filter Substack UI noise**: skip `app-link/post?...` with `submitLike=true`, `comments=true`, `action=share`, `@username` author profiles, `utm_campaign=email-read-in-app`, `redirect/app-store`
6. **Triaged articles**: Assign star ratings using Value Assessment Matrix
7. **Proceed to wiki-ingest**: Create/update pages → index.md → log.md → commit
8. **Log**: "Newsletter pipeline: newsletter-triage failed to produce valid JSON; wiki-ingest performed triage directly"

When no output_path or candidates are recoverable:
1. Fall back to scanning raw newsletter files: `ls -la ~/wiki/raw/newsletters/*.md | sort -k5 -rn`
2. Filter noise using Substack Noise Filtering
3. Resolve canonical URLs and extract article links as above
4. Assign star ratings
5. Merge into normal workflow
6. Log: "Triage recovery: Upstream checkpoint completely missing, scanned raw files"

## Noise Filtering Reference
| Pattern | Type | Action |
|---------|------|--------|
| play_audio=true, play_card | Podcast/Audio UI | Skip |
| post-comment, comments=true | Comment section | Skip |
| submitLike=true, reaction | Like/heart button | Skip |
| share=true | Share link | Skip |
| redirect/app-store | App download page | Skip |
| @username mentions | Author profile | Skip |
| redirect/2/eyJ... or redirect/<uuid> | Obfuscated redirect | Try web_extract or skip |
| utm_campaign=email-read-in-app | Read-in-app prompt | Skip |
| link.mail.beehiiv.com | Link tracking | Resolve if possible |
| open.substack.com/pub/{pub}/p/{slug} | ✅ **Canonical newsletter URL** | Use directly with web_extract to get post body |
| app-link/post?publication_id=N&post_id=M | Email tracking link | Extract pub_id + post_id, then construct open.substack.com/pub/{pub}/p/{slug} |

## Substack URL Resolution (CRITICAL)

The raw newsletter checkpoint contains ONLY tracking/redirect URLs. To get the actual newsletter content:

1. Find the `open.substack.com/pub/{publication}/p/{slug}` URL (usually Link 7-9 in the candidates)
2. Call `web_extract` on that URL to get the newsletter post body
3. From the post body, extract the REAL curated article links (with titles and descriptions)
4. These extracted links are what you triage — NOT the tracking URLs in the candidates array

The `substack.com/redirect/2/eyJ...` and `substack.com/redirect/<uuid>` URLs resolve to app download pages or other noise — never to the actual article content.

## Value Assessment Matrix
| Rating | Criteria | Wiki Action |
|--------|----------|-------------|
| ★★★★★ | New AI/ML concept | New concept page |
| ★★★★☆ | Significant update | Update existing page |
| ★★★☆☆ | Minor add to entity | Entity page update |
| ★★☆☆☆ | Minor mention only | Skip |
| ★☆☆☆☆ | Not AI-related | Skip |

## Pitfalls
- Always orient first (SCHEMA.md + index + log)
- Japanese output mandatory for cron reports
- Subagents need absolute paths
- Commit early for large batches
