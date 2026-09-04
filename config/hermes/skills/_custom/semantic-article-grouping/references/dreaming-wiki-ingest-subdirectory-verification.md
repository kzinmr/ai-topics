# Subdirectory Surrogate Verification (Dreaming Wiki Ingest Recovery 2026-06-22)

## Problem
Triage recommended creating `concepts/claude-code/claude-code-hooks.md` (new page for Claude Code hooks/steering).
The correct page `concepts/claude-code/claude-code-steering-methods.md` already existed and covered hooks comprehensively.
The triage was made before the steering-methods page was created by a separate pipeline run (active-crawl, June 21).

## Root Cause
- Triage agent evaluates articles at time of grouping (June 22, 18:00 UTC)
- A separate pipeline (active-crawl or manual enrichment) created the steering-methods page on June 21
- The triage `candidate_wiki_path` was `claude-code-hooks.md` but actual content lived under `claude-code-steering-methods.md`
- The Post-Recovery Verification check for `os.path.exists(candidate_wiki_path)` returned False → would have triggered "proceed with creation"
- Only a broader `ls concepts/claude-code/` revealed the surrogate

## Fix
Extend the Post-Recovery Verification procedure to include subdirectory listing:
```bash
# List ALL pages in the candidate's parent subdirectory
ls ~/ai-topics/wiki/concepts/claude-code/ | sort
```
Check each for content overlap before declaring "page does NOT exist."

## Detection Pattern in This Session
```
find /opt/data/ai-topics/wiki/concepts/claude-code -name "*.md" | sort
```
Returned 13 files including `claude-code-steering-methods.md` (184 lines, comprehensive).
The steering-methods page had tags: claude-code, coding-agents, ai-agents, customization, **hooks**, skills, rules, claudefile, developer-tooling

## Score After Fix
- Dream-001: ★★★★★ → ★★☆☆☆ skip (content fully captured, minor cross-ref only)
- Saved: ~30 minutes of redundant page creation + pre-commit fixing
