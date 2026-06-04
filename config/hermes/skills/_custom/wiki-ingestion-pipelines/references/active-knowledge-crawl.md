# Active Knowledge Crawl — Full Reference

Full procedure for the daily active knowledge crawl cron job.

## Prerequisites
- Wiki at `~/wiki/` (resolves to `~/ai-topics/wiki/`)
- Hot-topics config at `~/ai-topics/config/hot-topics.yaml`
- Verify at session start: `realpath ~/wiki`, `realpath ~/ai-topics`

## Gap Discovery (Step 0)
Run when few stale hot-topics exist. Survey major AI domains not in hot-topics.yaml:
```python
domains = ["AI video generation 2026", "AI regulation legislation 2026", "small language models edge 2026"]
```
For each domain: check wiki coverage, score by impact (major/partial/minor gap).
Max: 2 major gaps OR 3 partial gaps. Combined max: 3 pages per run.
Add discovered gaps to hot-topics.yaml with proper fields.

## Source Quality Rules
- Peer-reviewed conference papers only (NeurIPS, ICML, ICLR, ACL, CVPR)
- Tech company tech reports (OpenAI, Meta, Google, MS, Anthropic)
- Well-known blogs (Simon Willison, Karpathy, Antirez)
- arXiv-only non-peer-reviewed: FORBIDDEN
- Official docs and reputable news

## Critical Lessons (from production experience)
1. **Duplicate run detection**: Check `git ls-files` before creating pages
2. **Verify files after delegate_task**: Explicit existence check with `os.path.getsize()`
3. **Git pull --rebase with unstaged changes**: `git stash && pull && stash pop`
4. **YAML str.replace fragile**: Use sed with line numbers for hot-topics.yaml
5. **Git push failure**: Report status, don't retry. Commits are safe locally.
6. **Sibling agent file contamination**: Avoid `git add -A`, use selective `git add`
