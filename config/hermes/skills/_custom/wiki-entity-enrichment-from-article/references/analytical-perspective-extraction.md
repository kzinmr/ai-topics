# Extracting Analytical Perspectives During Article Ingestion

When a user asks to ingest an article AND extract reusable analytical perspectives (not just summarize content), the output should include frameworks, checklists, or lenses that can be applied to future analysis.

## Trigger Phrases
- "分析・取り込みの際の視点に活かせる点があれば取り込んで"
- "extract analytical frameworks"
- "what perspectives can we use for future analysis"
- "この辺りの言及はありましたか？" (checking if existing wiki covers specific angles)

## Workflow

### 1. Ingest the Article Normally
- Save raw article
- Create/update entity and concept pages

### 2. Extract Reusable Perspectives
From the article's analysis, extract:
- **Evaluation dimensions** — what to look at when assessing similar documents
- **Comparison frameworks** — axes along which to compare entities
- **Red flags / signal patterns** — what absence or presence of certain features means
- **Regulatory mapping** — how artifacts map to compliance frameworks

### 3. Create a Concept Page with Analysis Framework
The concept page should include a section like `## Analysis Perspectives` or `## When Reviewing [X], Focus On:` with numbered, actionable items.

Example from model-cards-system-cards.md:
```
### 1. Capability vs. Disclaimer Gap
### 2. Benchmark Selection Bias
### 3. Safety Layer Architecture
### 4. Absence as Signal
### 5. Regulatory Alignment
```

### 4. Cross-Reference to Existing Coverage
When the user asks "この辺りの言及はありましたか？":
- Search existing wiki for the specific angle they mention
- If found: point to it, update if needed
- If NOT found: add it to the relevant page (this is a high-value update)

## Pitfalls
- Don't just summarize — extract FRAMEWORKS that apply beyond this one article
- Perspectives should be actionable (something you can DO when reviewing a new document)
- Link perspectives to specific examples from the article for grounding
