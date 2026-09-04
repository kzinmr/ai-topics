# Historical Retrospective Section Pattern

When ingesting a transcript that is **>1 year old**, consider adding a retrospective section that analyzes the speaker's claims from the current vantage point.

## When to Add
- Transcript is from a prior year (2024 or earlier)
- The topic has evolved significantly since the recording
- The user explicitly asks "how does this look now?"
- The transcript contains predictions, recommendations, or tool evaluations that may have changed

## Section Structure (Japanese)

Add after the last content section, before "Companion Resources":

```markdown
## YYYY年振り返り — N年前の発言はどう見えているか

### 的中した予測・普遍的な洞察
- **「<quote>」** — <current status>

### 変化した状況
- **「<quote>」** — <how it changed>

### この講義の歴史的意義
<1-2 paragraphs on why this recording matters as a historical artifact>
```

## Guidelines
- Write in Japanese (user's primary language for wiki content)
- Cite specific claims from the transcript, not generic summaries
- Be concrete: name the models, tools, versions that exist now vs. then
- The "歴史的意義" section should frame the recording as an artifact of its era — what made it significant at that moment in the ecosystem's evolution
- Keep the retrospective to ~2500-3000 chars — substantive but not exhaustive
- This section is Layer 2 content (can be updated as the ecosystem evolves again)

## Example
See `transcripts/2024-01-12_maven_fsdp-deepspeed-accelerate-office-hours.md` for a full example covering FSDP/DeepSpeed/Accelerate ecosystem changes from Jan 2024 to Jun 2026.
