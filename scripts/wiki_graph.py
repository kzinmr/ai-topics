#!/usr/bin/env python3
"""Wiki Bipartite Graph Analysis — Person × Concept unified analysis.

Builds a bipartite graph of persons and concepts from:
1. Explicit wikilinks (entities/ ↔ concepts/)
2. Shared tags
3. Core Ideas section keywords (semantic proximity)

Outputs:
- Intellectual clusters (persons grouped by shared concepts)
- Concept constellations (concepts grouped by shared persons)
- Cross-reference gap recommendations
- Relationship strength scores

Usage:
  python scripts/wiki_graph.py                # full report
  python scripts/wiki_graph.py --format json   # machine-readable
  python scripts/wiki_graph.py --html          # interactive HTML visualization
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import NamedTuple

try:
    import yaml
except ImportError:
    yaml = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"
ENTITIES_DIR = WIKI_ROOT / "entities"
CONCEPTS_DIR = WIKI_ROOT / "concepts"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_fm(path: Path) -> dict:
    try:
        text = path.read_text(errors='replace')
    except OSError:
        return {}
    if not text.startswith('---'):
        return {}
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}
    if yaml:
        try:
            d = yaml.safe_load(parts[1])
            return d if isinstance(d, dict) else {}
        except Exception:
            return {}
    return {}


def read_text(path: Path) -> str:
    try:
        return path.read_text(errors='replace')
    except OSError:
        return ''


def extract_wikilinks(text: str) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]', text)}


def extract_core_ideas(text: str) -> list[str]:
    """Extract ### headings under ## Core Ideas."""
    ideas = []
    in_section = False
    for line in text.split('\n'):
        if re.match(r'^## Core Ideas', line):
            in_section = True
            continue
        if in_section and re.match(r'^## ', line) and not line.startswith('### '):
            break
        if in_section and line.startswith('### '):
            idea = line.replace('### ', '').strip()
            # Clean up numbering and quotes
            idea = re.sub(r'^\d+\.\s*', '', idea)
            idea = idea.strip('"\u201c\u201d')
            ideas.append(idea)
    return ideas


def extract_tags(fm: dict) -> list[str]:
    raw = fm.get('tags', [])
    if isinstance(raw, list):
        return [str(t) for t in raw if t]
    if isinstance(raw, str):
        return [t.strip() for t in raw.strip('[]').split(',') if t.strip()]
    return []


# ---------------------------------------------------------------------------
# Build the graph
# ---------------------------------------------------------------------------

class PersonNode(NamedTuple):
    slug: str
    title: str
    tags: frozenset
    core_ideas: tuple
    linked_concepts: frozenset
    linked_persons: frozenset


class ConceptNode(NamedTuple):
    slug: str
    title: str
    tags: frozenset
    linked_persons: frozenset
    linked_concepts: frozenset


def build_graph():
    """Build person and concept nodes with all relationship edges."""

    # Collect all slugs
    entity_files = {f.stem: f for f in ENTITIES_DIR.rglob('*.md')}
    concept_files = {f.stem: f for f in CONCEPTS_DIR.rglob('*.md')}

    # Identify person entities (have 'person' or 'blogger' tag, or Core Ideas section)
    person_slugs = set()
    for slug, path in entity_files.items():
        text = read_text(path)
        fm = parse_fm(path)
        tags = extract_tags(fm)
        if 'person' in tags or 'blogger' in tags or '## Core Ideas' in text:
            person_slugs.add(slug)

    # Build person nodes
    persons: dict[str, PersonNode] = {}
    for slug in person_slugs:
        path = entity_files[slug]
        text = read_text(path)
        fm = parse_fm(path)
        tags = frozenset(extract_tags(fm))
        core_ideas = tuple(extract_core_ideas(text))
        links = extract_wikilinks(text)

        # Classify links
        linked_concepts = set()
        linked_persons = set()
        for link in links:
            target = link.split('/')[-1]
            if target in concept_files or link.startswith('concepts/'):
                linked_concepts.add(target)
            if target in person_slugs:
                linked_persons.add(target)

        persons[slug] = PersonNode(
            slug=slug,
            title=fm.get('title', slug),
            tags=tags,
            core_ideas=core_ideas,
            linked_concepts=frozenset(linked_concepts),
            linked_persons=frozenset(linked_persons),
        )

    # Build concept nodes
    concepts: dict[str, ConceptNode] = {}
    for slug, path in concept_files.items():
        text = read_text(path)
        fm = parse_fm(path)
        tags = frozenset(extract_tags(fm))
        links = extract_wikilinks(text)

        linked_persons = set()
        linked_concepts = set()
        for link in links:
            target = link.split('/')[-1]
            if target in person_slugs:
                linked_persons.add(target)
            if target in concept_files or link.startswith('concepts/'):
                linked_concepts.add(target)

        concepts[slug] = ConceptNode(
            slug=slug,
            title=fm.get('title', slug),
            tags=tags,
            linked_persons=frozenset(linked_persons),
            linked_concepts=frozenset(linked_concepts),
        )

    # Merge bidirectional links
    for pslug, pnode in persons.items():
        for cslug in pnode.linked_concepts:
            if cslug in concepts:
                concepts[cslug] = concepts[cslug]._replace(
                    linked_persons=concepts[cslug].linked_persons | {pslug}
                )

    for cslug, cnode in concepts.items():
        for pslug in cnode.linked_persons:
            if pslug in persons:
                persons[pslug] = persons[pslug]._replace(
                    linked_concepts=persons[pslug].linked_concepts | {cslug}
                )

    return persons, concepts


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def compute_person_similarity(persons: dict[str, PersonNode]) -> list[tuple[float, str, str, dict]]:
    """Compute similarity between person pairs via shared concepts, tags, and ideas."""
    results = []
    person_list = sorted(persons.keys())

    for i, p1_slug in enumerate(person_list):
        p1 = persons[p1_slug]
        for p2_slug in person_list[i+1:]:
            p2 = persons[p2_slug]

            # Shared concepts (explicit links)
            shared_concepts = p1.linked_concepts & p2.linked_concepts
            concept_score = len(shared_concepts) * 3.0  # high weight

            # Shared tags (excluding generic ones)
            generic_tags = {'person', 'blogger', 'hn-popular', 'x-account', 'entity', 'ai'}
            p1_meaningful = p1.tags - generic_tags
            p2_meaningful = p2.tags - generic_tags
            shared_tags = p1_meaningful & p2_meaningful
            tag_score = len(shared_tags) * 1.5

            # Core ideas keyword overlap (lightweight semantic)
            p1_idea_words = set()
            for idea in p1.core_ideas:
                p1_idea_words.update(w.lower() for w in re.findall(r'\b[A-Za-z]{4,}\b', idea))
            p2_idea_words = set()
            for idea in p2.core_ideas:
                p2_idea_words.update(w.lower() for w in re.findall(r'\b[A-Za-z]{4,}\b', idea))
            # Remove very common words
            stopwords = {'that', 'this', 'with', 'from', 'will', 'have', 'just',
                         'about', 'over', 'your', 'what', 'than', 'they', 'been',
                         'more', 'when', 'into', 'some', 'should', 'every', 'also',
                         'actually', 'people', 'problem', 'future', 'thinking',
                         'approach', 'philosophy'}
            p1_idea_words -= stopwords
            p2_idea_words -= stopwords
            shared_ideas = p1_idea_words & p2_idea_words
            idea_score = min(len(shared_ideas) * 0.3, 5.0)  # capped

            # Direct person links
            direct_link = 1.0 if (p2_slug in p1.linked_persons or p1_slug in p2.linked_persons) else 0.0

            total = concept_score + tag_score + idea_score + direct_link

            if total >= 3.0:  # minimum threshold
                results.append((total, p1_slug, p2_slug, {
                    'concepts': sorted(shared_concepts),
                    'tags': sorted(shared_tags),
                    'idea_keywords': len(shared_ideas),
                    'direct_link': bool(direct_link),
                    'score_breakdown': {
                        'concept': concept_score,
                        'tag': tag_score,
                        'idea': idea_score,
                        'direct': direct_link,
                    }
                }))

    results.sort(key=lambda x: -x[0])
    return results


def find_concept_clusters(concepts: dict[str, ConceptNode]) -> list[tuple[float, str, str, dict]]:
    """Find concept pairs connected through shared persons."""
    results = []
    # Only consider concepts with person links
    linked_concepts = {k: v for k, v in concepts.items() if v.linked_persons}
    concept_list = sorted(linked_concepts.keys())

    for i, c1_slug in enumerate(concept_list):
        c1 = linked_concepts[c1_slug]
        for c2_slug in concept_list[i+1:]:
            c2 = linked_concepts[c2_slug]
            shared_persons = c1.linked_persons & c2.linked_persons
            if len(shared_persons) >= 2:
                shared_tags = c1.tags & c2.tags
                direct_link = 1.0 if (c2_slug in c1.linked_concepts or c1_slug in c2.linked_concepts) else 0.0
                score = len(shared_persons) * 2.0 + len(shared_tags) * 0.5 + direct_link
                results.append((score, c1_slug, c2_slug, {
                    'shared_persons': sorted(shared_persons),
                    'shared_tags': sorted(shared_tags),
                    'direct_link': bool(direct_link),
                }))

    results.sort(key=lambda x: -x[0])
    return results


def find_gap_recommendations(persons, concepts, person_sim, concept_clusters):
    """Find missing links that should exist based on the graph."""
    recs = []

    # Person pairs with high similarity but no direct link
    for score, p1, p2, detail in person_sim[:50]:
        if not detail['direct_link'] and score >= 5.0:
            recs.append({
                'type': 'person_link_missing',
                'from': p1,
                'to': p2,
                'score': score,
                'reason': f"Share {len(detail['concepts'])} concepts + {len(detail['tags'])} tags but no direct link",
                'shared': detail['concepts'][:5],
            })

    # Persons connected to a concept cluster but missing link to one concept
    for score, c1, c2, detail in concept_clusters[:30]:
        for person in detail['shared_persons']:
            if person in persons:
                p = persons[person]
                if c1 not in p.linked_concepts and c2 in p.linked_concepts:
                    recs.append({
                        'type': 'concept_link_gap',
                        'person': person,
                        'missing_concept': c1,
                        'via_concept': c2,
                        'reason': f"{person} links to {c2} but not its sibling {c1}",
                    })
                elif c2 not in p.linked_concepts and c1 in p.linked_concepts:
                    recs.append({
                        'type': 'concept_link_gap',
                        'person': person,
                        'missing_concept': c2,
                        'via_concept': c1,
                        'reason': f"{person} links to {c1} but not its sibling {c2}",
                    })

    return recs[:40]  # top recommendations


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(persons, concepts, person_sim, concept_clusters, gap_recs):
    lines = []
    lines.append("# \U0001f578\ufe0f Wiki Graph Analysis \u2014 Person \u00d7 Concept Unified Map\n")
    lines.append(f"**{len(persons)}** persons, **{len(concepts)}** concepts analyzed\n")

    # --- Intellectual Clusters ---
    lines.append("## \U0001e97c Intellectual Clusters (Person Pairs by Proximity)\n")
    lines.append("Persons connected through shared concepts, tags, and idea keywords.\n")
    lines.append("| Score | Person 1 | Person 2 | Shared Concepts | Tags | Ideas |")
    lines.append("|-------|----------|----------|-----------------|------|-------|")
    for score, p1, p2, detail in person_sim[:30]:
        concepts_str = ', '.join(detail['concepts'][:3])
        if len(detail['concepts']) > 3:
            concepts_str += f" +{len(detail['concepts'])-3}"
        tags_str = ', '.join(detail['tags'][:3])
        link_marker = " \U0001f517" if detail['direct_link'] else ""
        lines.append(f"| {score:.1f}{link_marker} | {p1} | {p2} | {concepts_str} | {tags_str} | {detail['idea_keywords']}kw |")
    lines.append("")
    lines.append("_\U0001f517 = already linked in wiki_\n")

    # --- Thought Schools ---
    lines.append("## \U0001f3db\ufe0f Thought Schools (Concept Constellations)\n")
    lines.append("Concepts that share multiple opinion leaders.\n")
    lines.append("| Score | Concept 1 | Concept 2 | Shared Persons | Linked? |")
    lines.append("|-------|-----------|-----------|----------------|---------|")
    for score, c1, c2, detail in concept_clusters[:25]:
        persons_str = ', '.join(detail['shared_persons'][:4])
        if len(detail['shared_persons']) > 4:
            persons_str += f" +{len(detail['shared_persons'])-4}"
        linked = "\u2705" if detail['direct_link'] else "\u274c"
        lines.append(f"| {score:.1f} | {c1} | {c2} | {persons_str} | {linked} |")
    lines.append("")

    # --- Hub Persons ---
    lines.append("## \U0001f31f Hub Persons (Most Connected)\n")
    hub_scores = []
    for slug, p in persons.items():
        conn = len(p.linked_concepts) + len(p.linked_persons)
        if conn > 0:
            hub_scores.append((conn, len(p.linked_concepts), len(p.linked_persons), len(p.core_ideas), slug))
    hub_scores.sort(reverse=True)
    lines.append("| Person | Concepts | Persons | Core Ideas | Total |")
    lines.append("|--------|----------|---------|------------|-------|")
    for total, nc, np, ni, slug in hub_scores[:20]:
        lines.append(f"| **{slug}** | {nc} | {np} | {ni} | {total} |")
    lines.append("")

    # --- Bridge Concepts ---
    lines.append("## \U0001f309 Bridge Concepts (Most Persons Connected)\n")
    bridge_scores = [(len(c.linked_persons), slug) for slug, c in concepts.items() if c.linked_persons]
    bridge_scores.sort(reverse=True)
    lines.append("| Concept | Persons | Who |")
    lines.append("|---------|---------|-----|")
    for count, slug in bridge_scores[:15]:
        c = concepts[slug]
        who = ', '.join(sorted(c.linked_persons)[:6])
        if count > 6:
            who += f" +{count-6}"
        lines.append(f"| **{slug}** | {count} | {who} |")
    lines.append("")

    # --- Gap Recommendations ---
    lines.append("## \U0001f50d Cross-Reference Gap Recommendations\n")
    person_gaps = [r for r in gap_recs if r['type'] == 'person_link_missing']
    concept_gaps = [r for r in gap_recs if r['type'] == 'concept_link_gap']

    if person_gaps:
        lines.append("### Person Links to Add\n")
        lines.append("These persons are intellectually close but don't reference each other:\n")
        for r in person_gaps[:15]:
            shared = ', '.join(r['shared'])
            lines.append(f"- **{r['from']}** \u2194 **{r['to']}** (score {r['score']:.1f}) \u2014 shared: {shared}")
        lines.append("")

    if concept_gaps:
        lines.append("### Concept Links to Add\n")
        lines.append("These persons link to one concept but not its closely related sibling:\n")
        seen = set()
        for r in concept_gaps[:15]:
            key = (r['person'], r['missing_concept'])
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- **{r['person']}** should link to **{r['missing_concept']}** (already links to {r['via_concept']})")
        lines.append("")

    lines.append("---")
    lines.append("_Generated by `scripts/wiki_graph.py`_")
    return "\n".join(lines)


def generate_html(persons, concepts, person_sim, concept_clusters):
    """Generate interactive HTML visualization."""
    # Build nodes and edges for visualization
    nodes = []
    edges = []
    node_ids = {}
    idx = 0

    # Add person nodes (only those with connections)
    connected_persons = set()
    for _, p1, p2, _ in person_sim[:60]:
        connected_persons.add(p1)
        connected_persons.add(p2)

    for slug in sorted(connected_persons):
        p = persons[slug]
        node_ids[f"p:{slug}"] = idx
        nodes.append({
            'id': idx,
            'label': slug.replace('-', ' ').title()[:25],
            'slug': slug,
            'type': 'person',
            'ideas': len(p.core_ideas),
            'concepts': len(p.linked_concepts),
        })
        idx += 1

    # Add concept nodes (only those bridging persons)
    bridge_concepts = set()
    for _, c1, c2, detail in concept_clusters[:40]:
        if len(detail['shared_persons']) >= 2:
            bridge_concepts.add(c1)
            bridge_concepts.add(c2)
    # Also add concepts from top person similarities
    for _, p1, p2, detail in person_sim[:40]:
        for c in detail['concepts'][:3]:
            bridge_concepts.add(c)

    for slug in sorted(bridge_concepts):
        if slug in concepts:
            node_ids[f"c:{slug}"] = idx
            nodes.append({
                'id': idx,
                'label': slug.replace('-', ' ').title()[:25],
                'slug': slug,
                'type': 'concept',
                'persons': len(concepts[slug].linked_persons),
            })
            idx += 1

    # Add person-person edges
    for score, p1, p2, detail in person_sim[:60]:
        if f"p:{p1}" in node_ids and f"p:{p2}" in node_ids:
            edges.append({
                'source': node_ids[f"p:{p1}"],
                'target': node_ids[f"p:{p2}"],
                'weight': min(score / 3, 5),
                'type': 'person-person',
                'label': ', '.join(detail['concepts'][:2]),
            })

    # Add person-concept edges
    for slug in connected_persons:
        if slug in persons:
            for cslug in persons[slug].linked_concepts:
                if f"c:{cslug}" in node_ids:
                    edges.append({
                        'source': node_ids[f"p:{slug}"],
                        'target': node_ids[f"c:{cslug}"],
                        'weight': 1,
                        'type': 'person-concept',
                    })

    graph_data = json.dumps({'nodes': nodes, 'edges': edges})

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Wiki Graph: Person \u00d7 Concept</title>
<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
<style>
  body {{ margin: 0; font-family: system-ui, sans-serif; background: #0d1117; color: #c9d1d9; }}
  h1 {{ text-align: center; padding: 12px 0 0; font-size: 1.2em; color: #58a6ff; }}
  .legend {{ position: absolute; top: 50px; left: 16px; font-size: 12px; }}
  .legend div {{ margin: 4px 0; }}
  .legend span {{ display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-right: 6px; vertical-align: middle; }}
  svg {{ width: 100%; height: calc(100vh - 50px); }}
  .tooltip {{ position: absolute; background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 8px 12px; font-size: 12px; pointer-events: none; opacity: 0; }}
</style>
</head>
<body>
<h1>\U0001f578\ufe0f Wiki Graph: Person \u00d7 Concept Bipartite Network</h1>
<div class="legend">
  <div><span style="background:#58a6ff"></span> Person</div>
  <div><span style="background:#f97583"></span> Concept</div>
  <div style="margin-top:8px; font-size:11px; color:#8b949e;">Drag to rearrange. Hover for details.</div>
</div>
<div class="tooltip" id="tooltip"></div>
<svg id="graph"></svg>
<script>
const data = {graph_data};

const svg = d3.select('#graph');
const width = window.innerWidth;
const height = window.innerHeight - 50;
svg.attr('viewBox', [0, 0, width, height]);

const tooltip = d3.select('#tooltip');

const simulation = d3.forceSimulation(data.nodes)
  .force('link', d3.forceLink(data.edges).id(d => d.id).distance(d => d.type === 'person-concept' ? 80 : 120))
  .force('charge', d3.forceManyBody().strength(-200))
  .force('center', d3.forceCenter(width / 2, height / 2))
  .force('collision', d3.forceCollide().radius(20));

const link = svg.append('g')
  .selectAll('line')
  .data(data.edges)
  .join('line')
  .attr('stroke', d => d.type === 'person-person' ? '#30363d' : '#21262d')
  .attr('stroke-width', d => Math.max(0.5, d.weight * 0.5))
  .attr('stroke-opacity', 0.6);

const node = svg.append('g')
  .selectAll('circle')
  .data(data.nodes)
  .join('circle')
  .attr('r', d => d.type === 'person' ? Math.max(5, (d.concepts || 0) + 4) : Math.max(4, (d.persons || 0) * 1.5 + 3))
  .attr('fill', d => d.type === 'person' ? '#58a6ff' : '#f97583')
  .attr('stroke', '#0d1117')
  .attr('stroke-width', 1.5)
  .call(d3.drag()
    .on('start', (event, d) => {{ if (!event.active) simulation.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }})
    .on('drag', (event, d) => {{ d.fx = event.x; d.fy = event.y; }})
    .on('end', (event, d) => {{ if (!event.active) simulation.alphaTarget(0); d.fx = null; d.fy = null; }}))
  .on('mouseover', (event, d) => {{
    let info = `<strong>${{d.label}}</strong><br>Type: ${{d.type}}`;
    if (d.type === 'person') info += `<br>Concepts: ${{d.concepts}} | Ideas: ${{d.ideas}}`;
    else info += `<br>Persons connected: ${{d.persons}}`;
    tooltip.html(info).style('opacity', 1)
      .style('left', (event.pageX + 10) + 'px').style('top', (event.pageY - 10) + 'px');
  }})
  .on('mouseout', () => tooltip.style('opacity', 0));

const label = svg.append('g')
  .selectAll('text')
  .data(data.nodes)
  .join('text')
  .text(d => d.label)
  .attr('font-size', d => d.type === 'person' ? 9 : 8)
  .attr('fill', d => d.type === 'person' ? '#c9d1d9' : '#f0aaaa')
  .attr('text-anchor', 'middle')
  .attr('dy', d => (d.type === 'person' ? -10 : -8));

simulation.on('tick', () => {{
  link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
  node.attr('cx', d => d.x).attr('cy', d => d.y);
  label.attr('x', d => d.x).attr('y', d => d.y);
}});
</script>
</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Wiki bipartite graph analysis')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown')
    parser.add_argument('--html', action='store_true', help='Generate HTML visualization')
    args = parser.parse_args()

    persons, concepts = build_graph()
    person_sim = compute_person_similarity(persons)
    concept_clusters = find_concept_clusters(concepts)
    gap_recs = find_gap_recommendations(persons, concepts, person_sim, concept_clusters)

    if args.html:
        html = generate_html(persons, concepts, person_sim, concept_clusters)
        out_path = WIKI_ROOT.parent / 'scripts' / 'cache' / 'wiki_graph.html'
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html)
        print(f"HTML visualization written to {out_path}")
        return

    if args.format == 'json':
        output = {
            'persons_count': len(persons),
            'concepts_count': len(concepts),
            'person_similarity': [
                {'score': s, 'p1': p1, 'p2': p2, 'detail': d}
                for s, p1, p2, d in person_sim[:50]
            ],
            'concept_clusters': [
                {'score': s, 'c1': c1, 'c2': c2, 'detail': d}
                for s, c1, c2, d in concept_clusters[:30]
            ],
            'gap_recommendations': gap_recs,
        }
        print(json.dumps(output, indent=2))
    else:
        print(generate_report(persons, concepts, person_sim, concept_clusters, gap_recs))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f"# Wiki Graph Analysis \u2014 ERROR\n\n```\n{exc}\n```", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
    sys.exit(0)
