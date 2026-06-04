# GitHub Open-Source Tool Research Workflow

Research methodology for creating wiki concept pages about open-source developer tools / coding agent harnesses hosted on GitHub. Differs from paper-based or blog-post-based research because the primary sources are code, READMEs, and community commentary rather than academic publications.

## Source Hierarchy (in order of value)

### Tier 1 — Project's Own Sources (read these first)
| Source | What to extract | Where to find |
|--------|----------------|---------------|
| **README.md** | Project description, features, installation, architecture overview, badges (stars, license, language) | Root of GitHub repo |
| **PHILOSOPHY.md** (if exists) | Project intent, design principles, system-design framing, "why this exists" | Repo root (`PHILOSOPHY.md`, `GUIDE.md`, `MANIFESTO.md`) |
| **USAGE.md / CLI docs** | Quick start, commands, configuration, auth, session management | `USAGE.md`, `docs/`, wiki |
| **ARCHITECTURE.md** (if exists) | System design, crate/module layout, component responsibilities | Repo root or `docs/` |
| **ROADMAP.md** | Future direction, known gaps, cleanup backlog | Repo root |
| **PARITY.md** (for reimplementations) | Feature parity status vs original | Repo root |
| **rust/README.md** (for Rust projects) | Crate map, CLI surface, features, workspace layout | `rust/README.md` |
| **DeepWiki** | Parsed architecture summary, key entities, code structure | `https://deepwiki.com/{owner}/{repo}` |

### Tier 2 — Commentary & Analysis
| Source | What to extract | Where to find |
|--------|----------------|---------------|
| **Comparison articles** (Medium, dev.to, wavespeed) | Feature comparisons, benchmark claims, maturity assessment | Web search |
| **News articles** (CyberNews, Business Insider, TechCrunch) | Origin story, adoption metrics, creator quotes | Web search |
| **Community discussion** (Reddit, Hacker News, X posts) | Reception, bug reports, feature requests | X, Reddit search |
| **Technical deep-dives** (Medium, blog posts) | Architecture analysis, differences from competitors | Web search |

### Tier 3 — Verification & Context
| Source | Check for |
|--------|-----------|
| **GitHub stars/forks** | Popularity, community size, growth velocity |
| **GitHub Issues** | Feature requests, known limitations, controversial discussions |
| **GitHub Discussions** | Community questions, common pitfalls |
| **Scaffold/Setup scripts** | How the project is actually built and deployed |

## Workflow

1. **Start with GitHub repo** → `web_extract` README.md for overview
2. **Check for PHILOSOPHY.md** → this is the most important source for understanding why the project exists (often more revealing than the README)
3. **Check DeepWiki** → architecture summary, saves manual code reading
4. **Check USAGE.md** → feature list, CLI commands, configuration
5. **Search for comparison articles** → position in landscape
6. **Search for news/creator backstory** → when/why/how created
7. **Search for people entities** → check creator, maintainers, org
8. **Verify facts**: always cross-reference claims across 2+ sources

## Template: Concept Page Comparison Sections

For reimplementation / inspired-by tools, structure comparisons in three tiers:

```markdown
## Comparison with Related Concepts

### [Concept] vs [Original/Inspiration]
| Aspect | This Concept | Original |
|--------|-------------|----------|
| **Purpose** | ... | ... |
| **Language** | ... | ... |
| **Model support** | ... | ... |
| **License** | ... | ... |
| **Maturity** | ... | ... |
| **Mantra** | ... | ... |
| **Gaps** | ... | Full implementation |

### [Concept] vs [Similar Tool A]
| Dimension | This Concept | Similar Tool |
|-----------|-------------|--------------|
| **Primary job** | ... | ... |
| **Runtime/UX** | ... | ... |
| **Ecosystem** | ... | ... |

### [Concept] in the [Broader Landscape]
Position within the domain framework.
```

## Example: Claw Code Session

Research sources used (in order):
1. `https://github.com/ultraworkers/claw-code` — README
2. `https://github.com/ultraworkers/claw-code/blob/main/PHILOSOPHY.md` — core philosophy
3. `https://github.com/ultraworkers/claw-code/blob/main/USAGE.md` — CLI features
4. `https://deepwiki.com/ultraworkers/claw-code` — architecture summary
5. `https://github.com/ultraworkers/claw-code/tree/main/rust` — crate layout
6. `https://github.com/ultraworkers/claw-code/blob/main/rust/README.md` — Rust workspace details
7. Web search for comparison articles (wavespeed, Medium)
8. Web search for creator backstory (Business Insider, CyberNews)
9. Web search for Yeachan Heo / oh-my-codex ecosystem

Output: 1 concept page + 3 entity pages + 1 raw article
