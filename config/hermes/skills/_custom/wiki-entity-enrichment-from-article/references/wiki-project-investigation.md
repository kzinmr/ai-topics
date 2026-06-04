# Wiki Project Investigation — Full Reference

Investigate a technology project and integrate findings across wiki.

## Phase 1: Investigation
1. Fetch project metadata: web_extract GitHub repo, README, key docs
2. Identify components (Runtime? Harness? Both? Tools?)
3. Search existing wiki for the project name and technologies
4. Load related concept pages
5. Deep-dive specific docs: capability matrices, architecture diagrams

## Phase 2: Architectural Mapping
Map each component to existing framework layers:
| Framework Layer | Project Component | Role |
|---|---|---|
| Open Models | ... | Model provider/agnostic? |
| Open Runtime | ... | Execution environment? |
| Open Harness | ... | Orchestration/capabilities? |

## Phase 3: Multi-Page Updates (specific → general)
1. Project-specific page (create or expand)
2. Component pages (add references to parent project)
3. Framework pages (add project as example implementation)
4. Related concept pages (add cross-references)
5. Save raw article

## Key Patterns
- **Coupling Insight**: What decides vs. what executes?
- **Differentiation Table**: Compare to similar projects
- **Capability Matrix**: Features with status

## Pitfalls
- Don't create duplicate pages
- Don't skip framework mapping — connect to existing concepts
- Don't forget raw article
- Use `patch` for partial updates, not `write_file`
