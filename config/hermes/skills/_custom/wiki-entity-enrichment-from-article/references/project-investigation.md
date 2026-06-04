# Project Investigation Workflow (extracted from SKILL.md)

Full methodology for investigating a technology project (GitHub repo, docs, blog) and integrating findings across multiple wiki pages.

## When to Use
- User provides a project link and asks "add this to the wiki"
- User asks for a deep-dive into a tool/project
- A newsletter mentions a tool you want to fully document

## Workflow

### Phase 1: Article Loading and Initial Scan
1. Save primary source to `raw/articles/{date}_{slug}.md`
2. Multi-source research: GitHub README, docs site, blog post, X/Twitter, product page
3. Search wiki for existing entity/concept pages
4. List all pages needing creation or enrichment

### Phase 2: Entity and Concept Page Creation
1. Create concept pages for core ideas, patterns, frameworks
2. Create entity pages for people, organizations, tools
3. Create comparison pages for competitive analysis
4. Cross-reference with wikilinks

### Phase 3: Integration
1. Update index.md + log.md
2. Commit each page incrementally

## Pitfalls
- Don't create duplicate entity pages
- Use `comparisons/` directory for comparison pages, not `concepts/`
- Aim for depth matching `entities/antirez-com.md`
- Verify GitHub stars, follower counts from live data

## Session Examples
- OpenAI in-house data agent + Cognition DANA → umbrella `data-analysis-agents.md`
- `concepts/_index.md` is auto-generated; patches can accidentally remove section headers if old_string spans too many lines
