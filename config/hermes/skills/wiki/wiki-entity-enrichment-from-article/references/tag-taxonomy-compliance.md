# Tag Taxonomy Compliance

## SCHEMA.md Location
`/opt/data/ai-topics/wiki/SCHEMA.md`

## Critical Rule
**Before writing frontmatter tags on ANY wiki page, check SCHEMA.md for valid tags.** Using non-existent tags causes `git commit` failures.

## Common Invalid → Valid Mappings
| Invalid (don't use) | Valid (use instead) |
|---------------------|---------------------|
| `industry-analysis` | `industry` |
| `investment` | `valuation` |
| `blockchain` | `crypto` |
| `distributed-computing` | `distributed-systems` |
| `datasette` | `tool` |
| `cost-management` | `cost-optimization` |
| `leadership` | `person` |
| `corporate` | `company` |

## Tag Format Rules
- Lowercase kebab-case only: `cost-optimization` not `CostOptimization`
- Prefer plural forms: `memory-systems` not `memory-system`
- No leading dashes, no spaces, no wikilinks
- If you need a new tag, add it to SCHEMA.md taxonomy first, then use it

## Tag Categories (from SCHEMA.md)
- **Core Types**: `concept`, `entity`, `comparison`, `query`, `summary`, `coding-agent`, `memory-system`, `person`
- **Models**: `model`, `multimodal`, `llm`, `transformer-architecture`, etc.
- **People/Orgs**: `company`, `person`, `openai`, `anthropic`, `google`, `meta`, etc.
- **Products**: `product`, `platform`, `tool`, `service`, `protocol`, `framework`
- **Techniques**: `inference`, `fine-tuning`, `rag`, `prompting`, etc.
- **Engineering**: `ai-agents`, `multi-agent`, `orchestration`, `cost-optimization`, etc.
- **Infrastructure**: `platform`, `protocol`, `security`, `architecture`
- **Meta**: `comparison`, `timeline`, `controversy`, `prediction`, `policy`
- **Domain Concepts**: `coordination`, `game-theory`, `crypto`, `distributed-systems`

## Verification
Run before committing: `cd /opt/data/ai-topics && git add wiki/`
- If tag validation fails, fix tags before `git commit`
- Tag validation hook checks against SCHEMA.md taxonomy
